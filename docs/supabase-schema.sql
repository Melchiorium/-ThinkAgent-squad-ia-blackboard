create table if not exists web_jobs (
  job_id text primary key,
  session_id text not null,
  status text not null,
  created_at timestamptz not null,
  updated_at timestamptz not null,
  brief_text text not null,
  brief_preview text not null,
  project_title text not null default '',
  project_name text not null default '',
  output_dir text not null default '',
  run_project text not null default '',
  run_version text not null default '',
  error text not null default '',
  progress_stage text not null default '',
  progress_label text not null default '',
  progress_detail text not null default '',
  progress_order integer not null default 0,
  progress_total integer not null default 0,
  progress_blocks jsonb not null default '[]'::jsonb,
  progress_events jsonb not null default '[]'::jsonb,
  progress_started_at text not null default '',
  progress_last_event_at text not null default '',
  progress_timeout_seconds integer not null default 600,
  progress_error_type text not null default '',
  progress_error_message text not null default ''
);

alter table web_jobs add column if not exists progress_stage text not null default '';
alter table web_jobs add column if not exists progress_label text not null default '';
alter table web_jobs add column if not exists progress_detail text not null default '';
alter table web_jobs add column if not exists progress_order integer not null default 0;
alter table web_jobs add column if not exists progress_total integer not null default 0;
alter table web_jobs add column if not exists progress_blocks jsonb not null default '[]'::jsonb;
alter table web_jobs add column if not exists progress_events jsonb not null default '[]'::jsonb;
alter table web_jobs add column if not exists progress_started_at text not null default '';
alter table web_jobs add column if not exists progress_last_event_at text not null default '';
alter table web_jobs add column if not exists progress_timeout_seconds integer not null default 600;
alter table web_jobs add column if not exists progress_error_type text not null default '';
alter table web_jobs add column if not exists progress_error_message text not null default '';

create table if not exists web_run_artifacts (
  run_project text not null,
  run_version text not null,
  version_number integer not null,
  filename text not null,
  content_text text,
  content_bytes bytea,
  content_type text not null,
  created_at timestamptz not null default now(),
  primary key (run_project, run_version, filename)
);

create index if not exists web_run_artifacts_run_idx
on web_run_artifacts (run_project, version_number);
