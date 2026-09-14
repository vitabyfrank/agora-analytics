# 유지관리 가이드

이 저장소의 고객용 HTML과 한국어·영어 Markdown 문서를 일관되게 업데이트하는 절차입니다.

## 필수 환경

- Python 3.10 이상
- 별도의 `pip` 또는 `npm` 패키지 없음

## 파일 구조

| 경로 | 역할 |
| --- | --- |
| `src/render.py` | 고객용 한국어 HTML의 내용과 마크업 원본 |
| `src/styles/base.css` | 공통 레이아웃과 접근성 스타일 |
| `src/styles/theme.css` | 색상·타이포그래피·컴포넌트 스타일 |
| `assets/fonts/PretendardVariable.woff2` | HTML에 포함되는 Pretendard Variable 폰트 |
| `assets/fonts/OFL.txt` | 폰트 라이선스 고지 |
| `scripts/build.py` | 원본으로부터 `index.html` 생성 |
| `scripts/check.py` | 생성 결과와 필수 콘텐츠 검사 |
| `index.html` | 생성된 고객용 한국어 가이드 |
| `docs/ko/guide.md` | 한국어 상세 문서 |
| `docs/en/guide.md` | 영어 상세 문서 |

`index.html`을 직접 편집하지 마세요. `src/`를 수정하고 빌드하면 변경 내용이 재현 가능하게 유지됩니다.

## 업데이트 순서

1. 기능, 가격, 플랜 권한, 보존기간과 API 제한을 공식 문서에서 다시 확인합니다.
2. 확인일과 변경 근거를 정리하고, 문서가 서로 다르면 하나를 임의로 확정하지 않습니다.
3. 고객용 화면의 원본인 `src/render.py`와 필요한 CSS를 수정합니다.
4. `docs/ko/guide.md`와 `docs/en/guide.md`에 같은 사실과 주의사항을 반영합니다.
5. 한국어·영어 문서를 문장 단위로 직역하기보다 의미, 숫자, 조건과 링크가 같은지 대조합니다.
6. HTML을 다시 생성하고 검사합니다.
7. 로컬 브라우저에서 데스크톱, 모바일, 키보드 탐색과 인쇄 화면을 확인합니다.
8. 변경 사항과 검증 결과를 Pull Request에 기록합니다.

## 공식 자료 검증

최소한 다음 자료를 확인합니다.

- [제품 개요](https://docs.agora.io/en/realtime-media/agora-analytics/product-overview)
- [플랜 및 가격](https://docs.agora.io/en/realtime-media/agora-analytics/reference/pricing)
- [Data Insights](https://docs.agora.io/en/realtime-media/agora-analytics/build/explore-and-analyze-data/data-insight)
- [Data Insights Plus](https://docs.agora.io/en/realtime-media/agora-analytics/build/explore-and-analyze-data/data-insight-plus)
- [Real-time Monitoring](https://docs.agora.io/en/realtime-media/agora-analytics/build/monitor-and-get-alerts/monitor)
- [Alerts](https://docs.agora.io/en/realtime-media/agora-analytics/build/monitor-and-get-alerts/alarm)
- [Embedding](https://docs.agora.io/en/realtime-media/agora-analytics/build/integrate-and-embed/embedded)
- [Analytics REST API](https://docs.agora.io/en/api-reference/api-ref/agora-analytics/analytics-rest-api)
- [REST API 인증](https://docs.agora.io/en/api-reference/api-ref/agora-analytics/analytics-restful-authentication)
- [Agora의 Datadog 연동](https://docs.agora.io/en/realtime-media/agora-analytics/build/integrate-and-embed/datadog-integration)
- [Datadog의 Agora Analytics 통합](https://docs.datadoghq.com/integrations/agora-analytics/)

각 변경에서 다음 항목을 따로 기록합니다.

- 문서 확인일
- 변경된 숫자와 제공 조건
- Console과 REST API의 차이
- 플랜별 제공 범위
- 공개 문서 사이의 상충 또는 해석상 제한
- 실제 계정이나 API로 확인하지 못한 사항

현재 확인이 필요한 항목은 Standard의 Plus 다차원 분석 제공 여부와 Enterprise의 Alerts 임베딩 구현 범위입니다. 공개 문서가 정리되기 전까지 고객 문서에는 확정 표현을 사용하지 않습니다.

## 한국어·영어 문서 동기화

다음 값은 두 언어에서 항상 같아야 합니다.

- 가격과 플랜명
- Console 보존기간과 REST API 과거 조회 범위
- API의 초당·분당·일별 한도, 데이터 지연과 1회 조회 구간
- Comparative Analysis의 세 가지 유형과 제한
- Datadog의 지표 수, 데이터 수준과 제공하지 않는 범위
- 최종 확인이 필요한 제공 조건
- 검증 기준일과 공식 자료 링크

한 언어만 먼저 수정한 경우 같은 Pull Request에서 다른 언어도 수정합니다. 의미가 달라질 수 있는 제품 용어는 첫 등장에 영문 이름을 함께 쓰고, 이후 표현을 일관되게 유지합니다.

## 빌드와 검사

저장소 루트에서 실행합니다.

```bash
python3 scripts/build.py
python3 scripts/check.py
```

Pull Request의 검증 워크플로는 생성 결과가 최신인지 확인한 뒤 전체 검사를 실행합니다.

한·영 가격·보존기간·API 표의 수치를 대조하고, Markdown 보존기간 표와 HTML을 비교합니다.
로컬 링크, HTML 앵커, 내장 폰트·라이선스, 개인 파일 경로 포함 여부도 검사합니다.
이 검사는 제품 제공 조건이 변경되었는지 판단하거나 화면 검토를 대신하지 않습니다.

```bash
python3 scripts/build.py --check
python3 scripts/check.py
```

로컬 미리보기:

```bash
python3 -m http.server 8000
```

브라우저에서 `http://localhost:8000`을 열고 다음을 확인합니다.

- 320px 또는 390px 모바일 폭에서 페이지 전체 가로 넘침이 없는지
- 넓은 표가 표 영역 안에서만 가로 스크롤되는지
- 본문 링크, 업무별 탭, 펼침 영역과 인쇄 버튼이 동작하는지
- 키보드만으로 탭과 링크를 사용할 수 있는지
- PDF 또는 인쇄 화면에 숨겨진 상세 정보가 포함되는지
- 외부 폰트 요청 없이 Pretendard가 로드되는지

## 브랜치와 커밋

기능 또는 콘텐츠 변경은 별도 브랜치에서 작업합니다.

- 문서 추가·개편: `docs/<short-description>`
- 콘텐츠 오류 수정: `fix/<short-description>`
- 사용자 기능 추가: `feat/<short-description>`

[Conventional Commits](https://www.conventionalcommits.org/) 형식을 사용합니다.

```text
feat(guide): add retention-focused plan comparison
fix(content): correct real-time API polling guidance
docs(i18n): synchronize Korean and English guides
style(ui): refine table typography and neutral colors
chore(build): strengthen generated HTML validation
```

한 커밋에는 한 가지 목적을 담습니다. 생성 원본을 변경했다면 재생성된 `index.html`도 같은 Pull Request에 포함합니다.

## Pull Request 확인사항

- 변경 목적과 고객에게 달라지는 내용을 설명했는가?
- 공식 자료 링크와 검증일을 기록했는가?
- 수치와 플랜 권한을 한국어·영어에서 대조했는가?
- `python3 scripts/build.py`와 `python3 scripts/check.py`가 통과했는가?
- 생성 후 `git diff --exit-code`로 누락된 생성 결과가 없는지 확인했는가?
- 모바일, 키보드와 인쇄 화면을 확인했는가?
- 확정할 수 없는 범위를 조건부 표현으로 유지했는가?

이 저장소는 배포 환경을 전제로 하지 않습니다. 배포가 필요하면 대상, 공개 범위와 배포 절차를 별도로 결정하고 문서화하세요.
