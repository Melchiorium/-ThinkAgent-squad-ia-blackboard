(function () {
  const statusShell = document.querySelector("[data-job-status-shell]");
  if (!statusShell) {
    return;
  }

  const statusUrl = statusShell.dataset.jobStatusUrl;
  const pageUrl = statusShell.dataset.jobPageUrl || window.location.href;
  const statusBadge = statusShell.querySelector("[data-job-status-badge]");
  const statusMessage = statusShell.querySelector("[data-job-state-message]");
  const spinner = statusShell.querySelector("[data-job-spinner]");
  const errorBox = statusShell.querySelector("[data-job-error]");
  const resultShell = statusShell.querySelector("[data-job-result-shell]");
  const progressShell = statusShell.querySelector("[data-job-progress-shell]");
  const progressCurrentLabel = progressShell?.querySelector("[data-progress-current-label]");
  const progressCurrentDetail = progressShell?.querySelector("[data-progress-current-detail]");
  const progressCounter = progressShell?.querySelector("[data-progress-counter]");
  const progressElapsed = progressShell?.querySelector("[data-progress-since]");
  const progressElapsedValue = progressShell?.querySelector("[data-progress-elapsed]");
  const progressStale = progressShell?.querySelector("[data-progress-stale]");
  const progressAlert = progressShell?.querySelector("[data-progress-alert]");
  const progressAlertTitle = progressShell?.querySelector("[data-progress-alert-title]");
  const progressAlertMessage = progressShell?.querySelector("[data-progress-alert-message]");
  const progressBlocks = progressShell?.querySelector("[data-progress-blocks]");
  const progressEvents = progressShell?.querySelector("[data-progress-events]");

  const labels = {
    queued: "En attente",
    running: "En cours",
    done: "Terminé",
    failed: "Échec",
  };

  const progressGroups = ["Brief", "Product", "Growth / GTM", "Tech", "Finalisation"];

  let currentPayload = {};
  let finished = false;

  const setText = (element, value) => {
    if (!element) {
      return;
    }
    element.textContent = value || "";
  };

  const setVisible = (element, visible) => {
    if (!element) {
      return;
    }
    element.classList.toggle("is-hidden", !visible);
  };

  const setBadge = (status) => {
    if (!statusBadge) {
      return;
    }
    statusBadge.textContent = labels[status] || status;
    statusBadge.className = `status-badge status-badge--${status}`;
  };

  const setSpinner = (status) => {
    if (!spinner) {
      return;
    }
    spinner.classList.toggle("is-active", status === "queued" || status === "running");
  };

  const setMessage = (status) => {
    if (!statusMessage) {
      return;
    }
    const messages = {
      queued: "En attente de traitement.",
      running: "Génération en cours.",
      done: "Génération terminée.",
      failed: "Génération en échec.",
    };
    statusMessage.textContent = messages[status] || status;
  };

  const setError = (error) => {
    if (!errorBox) {
      return;
    }
    const pre = errorBox.querySelector("pre");
    if (error) {
      errorBox.classList.remove("is-hidden");
      if (pre) {
        pre.textContent = error;
      }
    } else {
      errorBox.classList.add("is-hidden");
    }
  };

  const loadResultShell = async () => {
    if (!resultShell) {
      return;
    }
    try {
      const response = await fetch(pageUrl, {
        headers: {
          "X-Requested-With": "XMLHttpRequest",
        },
      });
      if (!response.ok) {
        return;
      }
      const html = await response.text();
      const parsedDocument = new DOMParser().parseFromString(html, "text/html");
      const nextShell = parsedDocument.querySelector("[data-job-result-shell]");
      if (nextShell) {
        resultShell.replaceWith(nextShell);
      }
    } catch (error) {
      return;
    }
  };

  function readInitialProgressState() {
    if (!progressShell) {
      return {};
    }
    return {
      status: statusShell.dataset.jobState || "",
      progress_stage: progressShell.dataset.progressStage || "",
      progress_label: progressShell.dataset.progressLabel || "",
      progress_detail: progressShell.dataset.progressDetail || "",
      progress_order: toNumber(progressShell.dataset.progressOrder),
      progress_total: toNumber(progressShell.dataset.progressTotal),
      progress_started_at: progressShell.dataset.progressStartedAt || "",
      progress_last_event_at: progressShell.dataset.progressLastEventAt || "",
      progress_timeout_seconds: toNumber(
        progressShell.dataset.progressTimeoutSeconds,
        600
      ),
      progress_error_type: progressShell.dataset.progressErrorType || "",
      progress_error_message: progressShell.dataset.progressErrorMessage || "",
      progress_blocks: [],
      progress_events: [],
    };
  }

  function toNumber(value, fallback = 0) {
    const number = Number.parseInt(value || "", 10);
    return Number.isFinite(number) ? number : fallback;
  }

  const parseTimestamp = (value) => {
    if (!value) {
      return null;
    }
    const timestamp = Date.parse(value);
    return Number.isNaN(timestamp) ? null : timestamp;
  };

  const formatElapsed = (seconds) => {
    const safeSeconds = Math.max(0, Math.floor(seconds));
    if (safeSeconds < 60) {
      return `${safeSeconds} s`;
    }
    const minutes = Math.floor(safeSeconds / 60);
    const remainingSeconds = safeSeconds % 60;
    if (minutes < 60) {
      return `${minutes} min ${remainingSeconds} s`;
    }
    const hours = Math.floor(minutes / 60);
    const remainingMinutes = minutes % 60;
    return `${hours} h ${remainingMinutes} min`;
  };

  const formatClock = (value) => {
    const timestamp = parseTimestamp(value);
    if (timestamp === null) {
      return "";
    }
    return new Date(timestamp).toLocaleTimeString("fr-FR", {
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    });
  };

  const renderProgress = (payload) => {
    if (!progressShell) {
      return;
    }

    const blocks = Array.isArray(payload.progress_blocks) ? payload.progress_blocks : [];
    const events = Array.isArray(payload.progress_events) ? payload.progress_events : [];
    const hasProgress = blocks.length > 0 || events.length > 0 || payload.progress_total > 0;
    progressShell.classList.toggle("job-progress--empty", !hasProgress);

    const fallbackLabel = {
      queued: "Brief reçu",
      running: "Génération en cours",
      done: "Génération terminée",
      failed: "Génération interrompue",
    };
    setText(progressCurrentLabel, payload.progress_label || fallbackLabel[payload.status] || "Génération en cours");
    setText(
      progressCurrentDetail,
      payload.progress_detail ||
        (payload.status === "queued"
          ? "Le brief a été soumis et attend le démarrage de la génération."
          : payload.status === "running"
            ? "La génération suit les étapes Product, Growth et Tech."
            : payload.status === "done"
              ? "Les artefacts sont prêts."
              : payload.status === "failed"
                ? "La génération s’est arrêtée avant la fin."
                : "")
    );

    if (progressCounter) {
      if (payload.progress_total > 0) {
        progressCounter.classList.remove("is-hidden");
        progressCounter.textContent = `${payload.progress_order || 0} / ${payload.progress_total}`;
      } else {
        progressCounter.classList.add("is-hidden");
      }
    }

    renderBlocks(blocks);
    renderEvents(events);
    renderAlert(payload);
    updateElapsedLabels();
  };

  const renderBlocks = (blocks) => {
    if (!progressBlocks) {
      return;
    }
    progressBlocks.innerHTML = "";
    if (!blocks.length) {
      const emptyParagraph = document.createElement("p");
      emptyParagraph.className = "empty";
      emptyParagraph.textContent = "La progression détaillée apparaîtra ici dès le démarrage de la génération.";
      progressBlocks.append(emptyParagraph);
      return;
    }

    const groupedBlocks = new Map();
    blocks.forEach((block) => {
      const group = block.group || "Autres";
      if (!groupedBlocks.has(group)) {
        groupedBlocks.set(group, []);
      }
      groupedBlocks.get(group).push(block);
    });

    const orderedGroups = [
      ...progressGroups,
      ...Array.from(groupedBlocks.keys()).filter((group) => !progressGroups.includes(group)),
    ];

    const fragment = document.createDocumentFragment();
    orderedGroups.forEach((groupName) => {
      const groupBlocks = groupedBlocks.get(groupName);
      if (!groupBlocks || !groupBlocks.length) {
        return;
      }

      const section = document.createElement("section");
      section.className = "job-progress__group";

      const header = document.createElement("div");
      header.className = "job-progress__group-header";

      const heading = document.createElement("h2");
      heading.textContent = groupName;
      header.append(heading);
      section.append(header);

      const list = document.createElement("ul");
      list.className = "job-progress__block-list";
      groupBlocks.forEach((block) => {
        const item = document.createElement("li");
        item.className = `job-progress__block job-progress__block--${block.status || "pending"}`;

        const dot = document.createElement("span");
        dot.className = "job-progress__block-dot";
        dot.setAttribute("aria-hidden", "true");

        const label = document.createElement("span");
        label.className = "job-progress__block-label";
        label.textContent = block.label || block.id || "";

        item.append(dot, label);
        list.append(item);
      });

      section.append(list);
      fragment.append(section);
    });

    progressBlocks.append(fragment);
  };

  const renderEvents = (events) => {
    if (!progressEvents) {
      return;
    }
    progressEvents.innerHTML = "";

    const header = document.createElement("div");
    header.className = "job-progress__group-header";
    const heading = document.createElement("h2");
    heading.textContent = "Derniers événements";
    header.append(heading);
    progressEvents.append(header);

    if (!events.length) {
      const emptyParagraph = document.createElement("p");
      emptyParagraph.className = "empty";
      emptyParagraph.textContent = "Aucun événement pour le moment.";
      progressEvents.append(emptyParagraph);
      return;
    }

    const list = document.createElement("ol");
    list.className = "job-progress__event-list";
    events.slice(-8).forEach((event) => {
      const item = document.createElement("li");
      item.className = "job-progress__event";

      const time = document.createElement("span");
      time.className = "job-progress__event-time";
      time.textContent = formatClock(event.timestamp);

      const label = document.createElement("span");
      label.className = "job-progress__event-label";
      label.textContent = event.label || "";

      item.append(time, label);

      if (event.detail) {
        const detail = document.createElement("span");
        detail.className = "job-progress__event-detail";
        detail.textContent = event.detail;
        item.append(detail);
      }

      list.append(item);
    });

    progressEvents.append(list);
  };

  const renderAlert = (payload) => {
    if (!progressAlert) {
      return;
    }

    const hasError = Boolean(payload.progress_error_type || payload.progress_error_message);
    progressAlert.classList.toggle("is-hidden", !hasError);
    if (!hasError) {
      return;
    }

    const typeLabels = {
      timeout: "Timeout agent",
      network: "Erreur réseau/API",
      llm: "Erreur LLM",
      storage: "Erreur de stockage",
      unknown: "Erreur de progression",
    };
    setText(progressAlertTitle, typeLabels[payload.progress_error_type] || "Erreur de progression");

    const fallbackMessages = {
      timeout: "Une étape a dépassé le délai attendu.",
      network: "Un appel réseau a échoué pendant la génération.",
      llm: "Un appel modèle a échoué pendant la génération.",
      storage: "La persistance des données a échoué.",
      unknown: "La progression a rencontré une erreur inattendue.",
    };
    setText(
      progressAlertMessage,
      payload.progress_error_message || fallbackMessages[payload.progress_error_type] || fallbackMessages.unknown
    );
  };

  const updateElapsedLabels = () => {
    if (!progressShell || !currentPayload) {
      return;
    }

    const isRunning = currentPayload.status === "running";
    const startedAt = parseTimestamp(currentPayload.progress_started_at);
    const lastEventAt = parseTimestamp(currentPayload.progress_last_event_at || currentPayload.progress_started_at);

    if (startedAt !== null && progressElapsed) {
      const elapsedSeconds = (Date.now() - startedAt) / 1000;
      if (progressElapsedValue) {
        progressElapsedValue.textContent = formatElapsed(elapsedSeconds);
      }
      progressElapsed.classList.remove("is-hidden");
    } else if (progressElapsed) {
      progressElapsed.classList.add("is-hidden");
    }

    if (!progressStale) {
      return;
    }

    const timeoutSeconds = currentPayload.progress_timeout_seconds || 0;
    const isStale =
      isRunning &&
      timeoutSeconds > 0 &&
      lastEventAt !== null &&
      Date.now() - lastEventAt > timeoutSeconds * 1000 &&
      !currentPayload.progress_error_type;

    if (isStale) {
      progressStale.textContent = "Cette étape prend plus de temps que prévu.";
      progressStale.classList.remove("is-hidden");
    } else {
      progressStale.classList.add("is-hidden");
      progressStale.textContent = "";
    }
  };

  const applyPayload = async (payload) => {
    currentPayload = payload;
    setBadge(payload.status);
    setSpinner(payload.status);
    setMessage(payload.status);
    setError(payload.error);
    renderProgress(payload);

    if (payload.status === "done" && !finished) {
      finished = true;
      if (!resultShell || !resultShell.querySelector("[data-run-result]")) {
        await loadResultShell();
      }
    }

    if (payload.status === "failed") {
      finished = true;
    }
  };

  const poll = async () => {
    try {
      const response = await fetch(statusUrl, {
        headers: {
          Accept: "application/json",
        },
      });
      if (!response.ok) {
        return;
      }
      const payload = await response.json();
      await applyPayload(payload);
      if (finished && intervalId) {
        window.clearInterval(intervalId);
      }
    } catch (error) {
      return;
    }
  };

  currentPayload = readInitialProgressState();
  const intervalId = window.setInterval(poll, 3000);
  const timerId = window.setInterval(updateElapsedLabels, 1000);
  poll();
  updateElapsedLabels();

  window.addEventListener("beforeunload", () => {
    window.clearInterval(intervalId);
    window.clearInterval(timerId);
  });
})();
