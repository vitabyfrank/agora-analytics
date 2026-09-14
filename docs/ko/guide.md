# Agora Analytics 플랜 및 기능 가이드

검증 기준일: **2026-09-14**

**음성·영상 통화부터 라이브 스트리밍까지**

서비스 품질을 확인하고 문제를 추적하세요.

이 문서는 고객의 데이터 보존기간, 분석 목적과 연동 방식을 기준으로 Agora Analytics 플랜을 비교합니다. [제품 개요](https://docs.agora.io/en/realtime-media/agora-analytics/product-overview)에 안내된 Agora 기반 Voice Calling, Video Calling, Interactive Live Streaming, Broadcast Streaming 시나리오를 다루며, 가격이나 플랜 이름만으로 플랜을 일괄 추천하지 않습니다.

제공 지표는 SDK, 플랫폼, 제품과 기능에 따라 다릅니다. 이 문서의 플랜·API 표는 별도의 외부 CDN 전송, VOD 또는 채팅 시스템까지 지원한다는 의미가 아닙니다.

고객 설명에서 사용하는 **서비스 세션**은 한 사용자의 통화 또는 라이브 스트리밍 경험을 묶어 표현하는 일반 용어입니다. Agora Console과 API 필드의 통화, API 세션, 사용자, 채널이 가진 개별 기술적 의미를 대체하지 않습니다.

> 제품 가격과 제공 범위는 변경될 수 있습니다. 최종 제안 전에는 고객 계약, 활성화 상태와 최신 공식 문서를 확인하세요.

## 먼저 결정할 사항

플랜 선택에서 가장 중요한 질문은 다음 네 가지입니다.

1. 개별 통화 상세와 서비스 집계 데이터를 각각 며칠 동안 다시 조회해야 하는가?
2. Console에서 직접 분석할 것인가, REST API로 고객 시스템에 수집할 것인가?
3. 실시간 운영 관제와 사후 추세 분석 중 어느 쪽이 더 중요한가?
4. 국가, 기기, SDK 버전 등으로 문제군을 좁히거나 Datadog과 연동해야 하는가?

## 플랜과 공개 월 가격

| 플랜 | 월 가격(USD) | 적합한 요구사항 |
| --- | ---: | --- |
| Starter | $0 | 실시간 서비스의 기본 통화 분석과 기능 평가 |
| Standard | $449 | 개별 통화 조사 기간 확대와 서비스의 기본 사용량·품질 분석 |
| Premium | $999 | 고급 비교 분석, Alerts, Datadog, Data Insights·Monitoring API |
| Enterprise | $1,599 | 가장 긴 Console 보존기간과 높은 API 한도·조회 범위 |

Enterprise가 항상 권장되는 것은 아닙니다. Premium의 기능으로 목적을 충족할 수 있고 추가 보존기간이나 API 용량이 필요하지 않다면 Premium이 합리적입니다. Enterprise는 더 긴 이력과 더 높은 API 한도가 실제 운영 요건일 때 선택합니다.

근거: [Agora Analytics 플랜 및 가격](https://docs.agora.io/en/realtime-media/agora-analytics/reference/pricing), [Agora Analytics 가격 페이지](https://www.agora.io/en/pricing/analytics/)

### 주요 기능의 플랜 범위

| 기능 | Starter | Standard | Premium | Enterprise |
| --- | :---: | :---: | :---: | :---: |
| Call Inspector · Console | 제공 | 제공 | 제공 | 제공 |
| Call Inspector · REST API·임베딩 | — | 제공 | 제공 | 제공 |
| Call Overview | — | — | 제공 | 제공 |
| Data Insights · Console | — | 제공 | 제공 | 제공 |
| Data Insights · REST API·임베딩 | — | — | 제공 | 제공 |
| Data Insights Plus · 비교·샘플링 | — | — | 제공 | 제공 |
| Plus 다차원 분석 | — | 확인 필요¹ | 제공 | 제공 |
| Real-time Monitoring · Console | — | 제공 | 제공 | 제공 |
| Real-time Monitoring · REST API | — | — | 제공 | 제공 |
| Alerts · Console | — | — | 제공 | 제공 |
| Datadog 연동 | — | — | 제공 | 제공 |

¹ Pricing 표와 같은 문서의 설명·설정 가이드가 서로 달라 실제 제공 범위를 확인해야 합니다. 임베딩도 화면별 지원 범위를 확인하세요.

## 데이터 보존기간과 API 조회 범위

Console의 보존기간과 REST API가 조회할 수 있는 과거 범위는 서로 다릅니다.

| 데이터 경로 | Starter | Standard | Premium | Enterprise |
| --- | ---: | ---: | ---: | ---: |
| Call Inspector · Console | 3일 | 7일 | 14일 | 30일 |
| Call Inspector · REST API | 미제공 | 1일 | 7일 | 15일 |
| Data Insights · Console | 미제공 | 30일 | 60일 | 90일 |
| Data Insights · REST API | 미제공 | 미제공 | 14일 | 30일 |

이 차이는 고객 지원과 데이터 보관 설계에 직접 영향을 줍니다. 예를 들어 Premium 고객이 Console에서 14일 전 통화를 볼 수 있어도 Call Inspector API로는 최근 7일만 조회할 수 있습니다.

플랜의 조회 범위보다 오래 데이터를 보관해야 한다면, 조회 가능한 기간 안에 데이터를 수집해 고객 저장소에 보관해야 합니다. 데이터 수집기는 호출 한도, 데이터 반영 지연, 오류 처리와 재시도를 함께 설계해야 합니다.

근거: [Agora Analytics 플랜 및 가격](https://docs.agora.io/en/realtime-media/agora-analytics/reference/pricing), [Analytics REST API](https://docs.agora.io/en/api-reference/api-ref/agora-analytics/analytics-rest-api)

## 기능이 해결하는 문제

| 기능 | 역할 | 해결하는 문제 | 고객 가치 | 사용 예 |
| --- | --- | --- | --- | --- |
| Call Inspector | 개별 통화의 사용자, 이벤트, 송수신 구간과 품질 지표를 조사 | 고객 문의만으로 재현하기 어려운 통화 문제 | 조사 범위를 빠르게 좁혀 지원 시간을 단축 | 고객이 제보한 통화를 검색해 어느 사용자·구간에서 품질이 저하됐는지 확인 |
| Data Insights | 사용량과 품질 추세를 기간별로 집계 | 개별 통화만 봐서는 음성·영상·라이브 스트리밍 서비스의 반복 패턴을 알기 어려움 | 서비스 상태와 변화 추이를 운영·제품 의사결정에 활용 | 서비스 전체의 입장 성공률이나 끊김률을 일·시간 단위로 확인 |
| Data Insights Plus | 차원 필터, 샘플링과 비교 분석으로 문제군을 세분화 | 전체값에 가려진 특정 지역·기기·SDK 문제 | 영향 범위를 좁히고 조사할 통화를 찾음 | SDK 버전별 품질 지표를 관찰하고 지원되는 관련 통화로 이동 |
| Real-time Monitoring | 최근 상태를 짧은 간격의 집계로 관찰 | 통화·라이브 스트리밍 서비스의 운영 이상을 집계 보고서가 반영될 때까지 놓침 | 진행 중인 이상을 빠르게 인지 | 서비스 운영 중 최근 채널·사용자 수와 품질 변화를 확인 |
| Alerts | 임계값 또는 사전 정의된 이벤트를 이메일, WeCom, HTTP callback으로 알림 | 담당자가 Console을 계속 보고 있어야 함 | 대응 시작 시간을 줄이고 기존 운영 흐름에 연결 | 입장 성공률 저하 시 담당 채널과 webhook으로 알림 |
| Embedding | 지원되는 Analytics 화면을 고객 포털에 iframe으로 표시 | 운영자가 여러 Console을 오가야 함 | 업무 화면 안에서 필요한 분석을 제공 | 고객 지원 포털에서 통화 검색 화면 열기 |
| REST API | 고객 서버가 지원되는 통화·집계·실시간 데이터를 조회 | 자체 포털, 장기 보관 또는 맞춤 가공이 필요함 | 고객 데이터 파이프라인과 업무 시스템에 통합 | 통화 목록과 지원되는 서비스 집계를 운영 시스템에 연결 |
| Datadog 연동 | App ID 단위 RTC 집계 지표를 Datadog으로 전송 | 음성·영상·라이브 스트리밍 RTC 지표와 인프라 지표가 서로 다른 관제 도구에 분리됨 | 같은 시간축에서 서비스와 RTC 상태를 함께 관찰 | 서버 장애 지표와 입장 성공률 변화를 하나의 대시보드에서 비교 |

기능 개요: [Agora Analytics 제품 개요](https://docs.agora.io/en/realtime-media/agora-analytics/product-overview)

## Comparative Analysis의 정확한 범위

Data Insights Plus의 Comparative Analysis는 다음 세 가지 비교 방식을 제공합니다.

| 비교 방식 | 동작 | 판단에 유용한 질문 |
| --- | --- | --- |
| 지표 비교 | 같은 기간에 주 지표 1개와 추가 지표 최대 3개를 비교 | 품질 저하와 사용량·네트워크 지표가 같은 시점에 움직였는가? |
| 기간 비교 | 같은 지표를 직전 비교 주기, 전월 대응 기간 또는 사용자 지정 기간과 비교 | 최근 변화가 이전의 같은 길이 기간과 어떻게 다른가? |
| 필터 그룹과 전체 비교 | 차원 필터로 선택한 그룹의 지표를 전체값과 비교 | 특정 국가·기기·SDK 그룹이 전체값과 얼마나 다른가? |

기간 비교의 사용자 지정 기간은 일 단위이며 현재 기간과 같은 일수를 사용합니다. 플랜별 조회 가능 이력 안에서 날짜를 선택해야 합니다. 여러 지표를 선택하면 기존 차원 필터가 해제될 수 있으므로 필터 적용 상태를 다시 확인합니다.

이 기능을 임의의 두 그룹을 자유롭게 선택하는 범용 A/B 분석으로 설명하면 안 됩니다. SDK 버전은 고객 앱 버전과도 다릅니다. 또한 배포 전후 차이는 조사 단서이며 그 자체로 원인을 증명하지 않습니다. 원인을 판단하려면 이용 지역, 기기, 네트워크, 사용량과 개별 통화 증거를 함께 확인해야 합니다.

근거: [Data Insights Plus](https://docs.agora.io/en/realtime-media/agora-analytics/build/explore-and-analyze-data/data-insight-plus)

## REST API 설계 기준

기본 주소는 `https://api.agora.io`입니다. 고객 서버에서 Agora Console의 REST API용 **Customer ID와 Customer Secret**으로 HTTP Basic 인증을 사용합니다. 이 값은 Datadog API Key나 RTC App Certificate와 다르며 브라우저·모바일 앱에 포함하면 안 됩니다.

인증 근거: [Analytics REST API 인증](https://docs.agora.io/en/api-reference/api-ref/agora-analytics/analytics-restful-authentication)

### Call Inspector API

| 플랜 | 초당 한도 | 일별 한도 | 과거 조회 범위 |
| --- | ---: | ---: | ---: |
| Standard | 1회 | 1,000회 | 1일 |
| Premium | 3회 | 2,000회 | 7일 |
| Enterprise | 10회 | 10,000회 | 15일 |

통화 목록의 1회 조회 구간은 Standard 8시간, Premium 16시간, Enterprise 24시간입니다. 세션·상세 지표의 1회 조회 구간은 각각 1시간, 3시간, 6시간입니다. API별 데이터 반영 지연도 다르므로 조회 범위와 신선도를 별도로 확인하세요.

### Data Insights API

| 플랜 | 분당 한도 | 일별 한도 | 과거 조회 범위 | 시계열 1회 최대 구간 |
| --- | ---: | ---: | ---: | ---: |
| Premium | 3회 | 40회 | 14일 | 3일 |
| Enterprise | 10회 | 60회 | 30일 | 7일 |

사용량 시계열은 일·시간 단위이고, 품질 시계열은 일·시간·분 단위입니다. 차원별 집계 API는 사용량과 품질 모두 일·시간 단위입니다. Console의 Plus 화면과 REST API가 동일한 필터와 상호작용을 모두 제공한다고 가정하지 마세요.

### Real-time Monitoring API

| 플랜 | 분당 한도 | 일별 한도 | 과거 조회·1회 최대 구간 | 데이터 지연 | 시계열 단위 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Premium | 3회 | 480회 | 40분 | 40초 | 20초 |
| Enterprise | 10회 | 1,440회 | 60분 | 20초 | 20초 |

20초 단위 데이터가 20초마다 호출할 수 있다는 뜻은 아닙니다. 24시간 동안 20초마다 한 번 호출하면 하루 **4,320회**로 두 플랜의 일별 한도를 모두 초과합니다. Premium에서 3분마다 호출하면 480회, Enterprise에서 1분마다 호출하면 1,440회로 일일 한도를 모두 사용하므로 다른 조회와 재시도 여유를 남겨야 합니다.

API 한도와 엔드포인트: [Analytics REST API](https://docs.agora.io/en/api-reference/api-ref/agora-analytics/analytics-rest-api)

## Datadog 연동 범위

Datadog 기본 연동은 Premium과 Enterprise에서 활성화를 신청해 사용합니다. Agora에서 전송 지표와 Datadog API Key를 설정하고 Online 상태를 확인한 뒤, Datadog에서 Agora Analytics 통합을 설치합니다. 지원되는 Datadog 패키지와 비용은 별도로 확인해야 합니다.

RTC 연동은 `agora.rtc.app_id.` 접두사를 사용하는 App ID 단위의 집계 지표 9개를 제공합니다.

- 온라인 사용자 및 채널 수
- 입장 시도 및 성공 수
- 입장 성공률 및 5초 이내 입장 성공률
- 오디오·비디오 끊김률
- 네트워크 지연률

지표는 매분 계산되지만 수집부터 화면 반영까지 1분을 보장한다는 의미는 아닙니다. 기본 연동은 UID·채널별 원시 로그, 통화 녹화나 분산 트레이스를 제공하는 경로가 아닙니다. Datadog의 Events와 Service Checks도 제공하지 않습니다.

Datadog에 수신된 지표의 보존기간과 비용은 고객의 Datadog 계약·설정에 따릅니다. Agora REST API 호출 한도를 Datadog 기본 전송에 적용하거나, 두 시스템의 보존기간이 같다고 가정하지 마세요.

근거: [Agora의 Datadog 연동 가이드](https://docs.agora.io/en/realtime-media/agora-analytics/build/integrate-and-embed/datadog-integration), [Datadog의 Agora Analytics 통합 문서](https://docs.datadoghq.com/integrations/agora-analytics/)

## 제안 시 확인할 항목

- **Premium 우선 검토:** Comparative Analysis, Alerts, Datadog 또는 Data Insights·Monitoring API가 필요하지만 Premium의 보존기간과 한도로 충분한 경우
- **Enterprise 검토:** Call Inspector Console 30일, Data Insights Console 90일, 더 긴 API 조회 범위나 더 높은 호출 한도가 운영상 필수인 경우
- **장기 보관:** Console 또는 API 조회 범위를 넘어 보관해야 하는 데이터, 저장 위치, 수집 주기와 개인정보 정책
- **임베딩:** 실제로 임베딩할 화면, 사용자 인증, 권한과 지원되는 플랜
- **지표 해석:** 화면마다 품질 임계값과 집계 방식이 다를 수 있으므로 SLA나 과금 지표로 사용할 때 별도 정의 확인

다음 두 항목은 공개 문서 사이에 범위 차이가 있어 최종 제안 전에 확인이 필요합니다.

1. Pricing 표에는 Standard의 Plus 다차원 분석이 표시되지만, 같은 문서의 설명과 설정 가이드는 Premium·Enterprise 범위로 안내합니다.
2. Pricing 표의 Enterprise Alerts 임베딩 권한과 임베딩 구현 가이드에서 명시한 화면 범위가 일치하는지 확인해야 합니다.

맞춤 대시보드라는 표현을 별도의 커스텀 개발 서비스가 구독에 포함된다는 의미로 확대하지 마세요. 개발·구축 범위는 계약과 제공 조건을 별도로 확인합니다.

## 공식 자료

- [제품 개요](https://docs.agora.io/en/realtime-media/agora-analytics/product-overview)
- [플랜 및 가격](https://docs.agora.io/en/realtime-media/agora-analytics/reference/pricing)
- [Call Inspector](https://docs.agora.io/en/realtime-media/agora-analytics/build/explore-and-analyze-data/call-search)
- [Data Insights](https://docs.agora.io/en/realtime-media/agora-analytics/build/explore-and-analyze-data/data-insight)
- [Data Insights Plus](https://docs.agora.io/en/realtime-media/agora-analytics/build/explore-and-analyze-data/data-insight-plus)
- [Real-time Monitoring](https://docs.agora.io/en/realtime-media/agora-analytics/build/monitor-and-get-alerts/monitor)
- [Alerts](https://docs.agora.io/en/realtime-media/agora-analytics/build/monitor-and-get-alerts/alarm)
- [Embedding](https://docs.agora.io/en/realtime-media/agora-analytics/build/integrate-and-embed/embedded)
- [Analytics REST API](https://docs.agora.io/en/api-reference/api-ref/agora-analytics/analytics-rest-api)
- [Datadog 연동](https://docs.agora.io/en/realtime-media/agora-analytics/build/integrate-and-embed/datadog-integration)
