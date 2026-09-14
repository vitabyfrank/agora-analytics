# Maintenance Guide

Use this process to keep the customer-facing HTML and the Korean and English Markdown documentation consistent.

## Requirements

- Python 3.10 or later
- No `pip` or `npm` packages

## Repository structure

| Path | Purpose |
| --- | --- |
| `src/render.py` | Source content and markup for the Korean customer HTML |
| `src/styles/base.css` | Shared layout and accessibility styles |
| `src/styles/theme.css` | Color, typography, and component styles |
| `assets/fonts/PretendardVariable.woff2` | Pretendard Variable font embedded in the HTML |
| `assets/fonts/OFL.txt` | Font license notice |
| `scripts/build.py` | Generates `index.html` from source files |
| `scripts/check.py` | Checks generated output and required content |
| `index.html` | Generated Korean customer guide |
| `docs/ko/guide.md` | Detailed Korean reference |
| `docs/en/guide.md` | Detailed English reference |

Do not edit `index.html` directly. Update `src/` and rebuild so that the output remains reproducible.

## Update workflow

1. Recheck features, prices, plan entitlements, retention, and API limits in official documentation.
2. Record the verification date and evidence. If official pages disagree, do not resolve the conflict by assumption.
3. Update `src/render.py` and the relevant CSS files.
4. Apply the same facts and limitations to `docs/ko/guide.md` and `docs/en/guide.md`.
5. Compare meaning, numbers, conditions, and links across languages instead of translating sentence by sentence.
6. Regenerate and check the HTML.
7. Review desktop, mobile, keyboard navigation, and print output in a local browser.
8. Record the change and validation results in the pull request.

## Source audit

Review at least these primary sources:

- [Product overview](https://docs.agora.io/en/realtime-media/agora-analytics/product-overview)
- [Plans and pricing](https://docs.agora.io/en/realtime-media/agora-analytics/reference/pricing)
- [Data Insights](https://docs.agora.io/en/realtime-media/agora-analytics/build/explore-and-analyze-data/data-insight)
- [Data Insights Plus](https://docs.agora.io/en/realtime-media/agora-analytics/build/explore-and-analyze-data/data-insight-plus)
- [Real-time Monitoring](https://docs.agora.io/en/realtime-media/agora-analytics/build/monitor-and-get-alerts/monitor)
- [Alerts](https://docs.agora.io/en/realtime-media/agora-analytics/build/monitor-and-get-alerts/alarm)
- [Embedding](https://docs.agora.io/en/realtime-media/agora-analytics/build/integrate-and-embed/embedded)
- [Analytics REST API](https://docs.agora.io/en/api-reference/api-ref/agora-analytics/analytics-rest-api)
- [REST API authentication](https://docs.agora.io/en/api-reference/api-ref/agora-analytics/analytics-restful-authentication)
- [Agora Datadog integration](https://docs.agora.io/en/realtime-media/agora-analytics/build/integrate-and-embed/datadog-integration)
- [Datadog Agora Analytics integration](https://docs.datadoghq.com/integrations/agora-analytics/)

Record these items for every factual update:

- Documentation review date
- Changed numbers and conditions
- Differences between Console and REST API behavior
- Plan entitlements
- Conflicts or interpretation limits in public documentation
- Items not confirmed with a live account or authenticated API

The currently unresolved items are Standard access to Plus multidimensional analysis and the implementation scope of Enterprise Alerts embedding. Keep customer-facing statements conditional until the public documentation is aligned.

## Korean and English parity

These values must stay identical in both languages:

- Prices and plan names
- Console retention and REST API historical range
- API per-second, per-minute, and daily quotas, data delay, and request windows
- The three Comparative Analysis modes and their limitations
- Datadog metric count, aggregation level, and excluded data
- Entitlements that require final confirmation
- Verification date and official source links

If one language changes first, update the other in the same pull request. For product terms that may lose meaning in translation, include the English term on first use and use a consistent translation afterward.

## Build and checks

Run from the repository root:

```bash
python3 scripts/build.py
python3 scripts/check.py
```

The pull request validation workflow confirms that generated output is current and then runs all repository checks:

The checks compare numeric price, retention, and API tables across both languages,
and compare the Markdown retention table with the HTML. They also check local links,
HTML anchors, embedded font/license data, and accidental personal filesystem paths.
They do not establish whether a product entitlement has changed or replace visual review.

```bash
python3 scripts/build.py --check
python3 scripts/check.py
```

Start a local preview:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000` and verify:

- No page-level horizontal overflow at a 320px or 390px mobile viewport
- Wide tables scroll only inside their table container
- Page links, capability tabs, disclosure sections, and the print button work
- Tabs and links remain usable with a keyboard
- PDF or print output includes disclosed details
- Pretendard loads without an external font request

## Branches and commits

Use a dedicated branch for content or feature changes.

- Documentation additions or restructuring: `docs/<short-description>`
- Content corrections: `fix/<short-description>`
- User-facing features: `feat/<short-description>`

Use [Conventional Commits](https://www.conventionalcommits.org/):

```text
feat(guide): add retention-focused plan comparison
fix(content): correct real-time API polling guidance
docs(i18n): synchronize Korean and English guides
style(ui): refine table typography and neutral colors
chore(build): strengthen generated HTML validation
```

Keep one purpose per commit. When generated source changes, include the regenerated `index.html` in the same pull request.

## Pull request checklist

- Does the description explain the purpose and customer-visible behavior?
- Are the source links and verification date included?
- Were numbers and plan entitlements compared across Korean and English?
- Do `python3 scripts/build.py` and `python3 scripts/check.py` pass?
- After building, does `git diff --exit-code` confirm that generated output is current?
- Were mobile, keyboard, and print views reviewed?
- Are unconfirmed entitlements still expressed as conditions rather than guarantees?

This repository does not assume a deployment environment. If deployment is required, decide and document the destination, visibility, and release process separately.
