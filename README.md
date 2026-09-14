# Agora Analytics Plan Guide

**Quality analytics for real-time voice, video, and live streaming.**

A customer-facing reference for choosing an Agora Analytics plan based on data retention, API access, analysis features, and integration needs. The guide covers Agora-based Voice Calling, Video Calling, Interactive Live Streaming, and Broadcast Streaming scenarios described in the [product overview](https://docs.agora.io/en/realtime-media/agora-analytics/product-overview).

Available metrics vary by SDK, platform, product, and feature. The plan and API tables do not imply coverage for unrelated external CDN delivery, VOD, or chat systems.

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
