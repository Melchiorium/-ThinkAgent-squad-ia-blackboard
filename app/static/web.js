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

  const labels = {
    queued: "En attente",
    running: "En cours",
    done: "Terminé",
    failed: "Échec",
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

  let finished = false;

  const applyPayload = async (payload) => {
    setBadge(payload.status);
    setSpinner(payload.status);
    setMessage(payload.status);
    setError(payload.error);

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
        clearInterval(intervalId);
      }
    } catch (error) {
      return;
    }
  };

  let intervalId = window.setInterval(poll, 3000);
  poll();
})();
