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
  error text not null default ''
);

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
