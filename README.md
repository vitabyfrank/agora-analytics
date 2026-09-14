# Agora Analytics Plan Guide

A customer-facing reference for choosing an Agora Analytics plan based on data retention, API access, analysis features, and integration needs.

The generated Korean guide is available in [`index.html`](./index.html). It is designed to work as a standalone file, including its font assets.

## Documentation

- [English guide](./docs/en/guide.md)
- [한국어 가이드](./README.ko.md)
- [English maintenance guide](./docs/en/maintenance.md)
- [한국어 유지관리 가이드](./docs/ko/maintenance.md)

## Quick start

Requires Python 3.10 or later. No package installation is required.

```bash
git clone https://github.com/vitabyfrank/agora-analytics.git
cd agora-analytics
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8000
```

Open `http://localhost:8000` after starting the server.

`index.html` is generated. Update the files under `src/`, rebuild, and run the checks instead of editing the generated HTML directly.

## Verification basis

Content was checked against public Agora and Datadog documentation on **2026-09-14**. Prices, entitlements, limits, and product behavior can change. Confirm the applicable contract and enabled features before presenting a final proposal.
