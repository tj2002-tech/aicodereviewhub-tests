# AI Code Review Hub — Test Repo

A small Python project used to test AI code review tools. Every tool listed
on [AI Code Review Hub](https://aicodereviewhub.com) is run against the same
pull requests in this repo, and the results are published on the site:
how many seeded bugs each tool caught, how many it missed, and how many
false positives it raised.

## What is in here

A deliberately ordinary little web-app codebase (`src/`): user login,
billing/invoices, file downloads, and an admin API. The code contains
known bugs seeded in advance across four categories:

- **Logic bugs** — wrong thresholds, wrong arithmetic, wrong defaults.
- **Security vulnerabilities** — injection, hardcoded secrets, weak crypto,
  missing authorization, unsafe file paths.
- **Performance problems** — per-row database queries in a loop.
- **Style / robustness issues** — error handling that hides failures.

## How testing works

1. A pull request is opened that adds or changes code in `src/`.
2. The tool under test reviews that PR the way it would review any PR.
3. We record: bugs caught, bugs missed, false positives, time taken,
   and cost (tokens, credits, or dollars).
4. Results are published on the tool's page on AI Code Review Hub, with
   precision (caught / (caught + false positives)) and recall
   (caught / seeded). Results are re-run every quarter.

## What is NOT in here

The list of seeded bugs — file, line, and type — is recorded privately
and is **not** in this repo. A tool that reviews this repo must find the
bugs by reading the code, the same way it would review any other repo.

## Contributing

Found a bug that is *not* one of the seeded ones? Open an issue — if it
is real, it gets added to the seeded list (and the tool scores are
recomputed). Please do not open PRs that "fix" the seeded bugs: the bugs
are the test.
