# Agora Analytics 플랜 가이드

데이터 보존기간, API 제공 범위, 분석 기능과 연동 요구사항을 기준으로 Agora Analytics 플랜을 선택할 수 있도록 만든 고객용 자료입니다.

고객에게 공유할 한국어 가이드는 [`index.html`](./index.html)입니다. 폰트 자산을 포함한 단일 HTML 파일로도 사용할 수 있습니다.

## 문서

- [한국어 상세 가이드](./docs/ko/guide.md)
- [English guide](./README.md)
- [한국어 유지관리 가이드](./docs/ko/maintenance.md)
- [English maintenance guide](./docs/en/maintenance.md)

## 빠른 시작

Python 3.10 이상이 필요하며 별도의 패키지 설치는 필요하지 않습니다.

```bash
git clone https://github.com/vitabyfrank/agora-analytics.git
cd agora-analytics
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8000
```

서버를 실행한 다음 `http://localhost:8000`을 엽니다.

`index.html`은 생성 파일입니다. HTML을 직접 편집하지 말고 `src/` 아래 원본을 수정한 뒤 다시 빌드하고 검사하세요.

## 검증 기준

내용은 **2026-09-14** 기준 Agora와 Datadog의 공개 문서를 대조했습니다. 가격, 제공 기능, 한도와 제품 동작은 변경될 수 있으므로 최종 제안 전에는 고객 계약과 실제 활성화 범위를 확인해야 합니다.
