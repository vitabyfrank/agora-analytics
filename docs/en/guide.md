# Agora Analytics Plans and Capabilities

Verified on: **2026-09-14**

**Quality analytics for real-time voice, video, and live streaming.**

This guide compares Agora Analytics plans based on customer requirements for data retention, analysis, and integration. It covers Agora-based Voice Calling, Video Calling, Interactive Live Streaming, and Broadcast Streaming scenarios described in the [product overview](https://docs.agora.io/en/realtime-media/agora-analytics/product-overview). It does not recommend a plan based on price or tier name alone.

Available metrics vary by SDK, platform, product, and feature. The plan and API tables in this guide do not imply coverage for unrelated external CDN delivery, VOD, or chat systems.

In customer-facing explanations, **service session** is a descriptive umbrella for a user's call or live-streaming experience. It does not replace the specific meanings of call, API session, user, and channel in Agora Console and API fields.

> Product prices and entitlements can change. Before a final proposal, confirm the customer's contract, enabled features, and the latest official documentation.

## Start with the customer requirements

Four questions usually determine the right plan:

1. How long must individual call details and aggregated service data remain available?
2. Will users work in the Console, or must data be collected through REST APIs?
3. Is live operational monitoring or retrospective trend analysis more important?
4. Does the team need to narrow issues by country, device, or SDK version, or integrate with Datadog?

## Plans and published monthly prices

| Plan | Monthly price (USD) | Best fit |
| --- | ---: | --- |
| Starter | $0 | Basic call analysis and product evaluation for a real-time service |
| Standard | $449 | Longer call investigation history and basic service usage and quality analytics |
| Premium | $999 | Advanced comparisons, Alerts, Datadog, and Data Insights and Monitoring APIs |
| Enterprise | $1,599 | The longest Console retention and larger API history and quotas |

Enterprise is not the default recommendation. Premium is a reasonable choice when it provides the required capabilities and its retention and API limits are sufficient. Choose Enterprise when the additional history or API capacity is an operational requirement.

Sources: [Agora Analytics plans and pricing](https://docs.agora.io/en/realtime-media/agora-analytics/reference/pricing), [Agora Analytics pricing page](https://www.agora.io/en/pricing/analytics/)

### Plan coverage for major capabilities

| Capability | Starter | Standard | Premium | Enterprise |
| --- | :---: | :---: | :---: | :---: |
| Call Inspector · Console | Included | Included | Included | Included |
| Call Inspector · REST API and embedding | — | Included | Included | Included |
| Call Overview | — | — | Included | Included |
| Data Insights · Console | — | Included | Included | Included |
| Data Insights · REST API and embedding | — | — | Included | Included |
| Data Insights Plus · comparisons and samples | — | — | Included | Included |
| Plus multidimensional analysis | — | Confirm¹ | Included | Included |
| Real-time Monitoring · Console | — | Included | Included | Included |
| Real-time Monitoring · REST API | — | — | Included | Included |
| Alerts · Console | — | — | Included | Included |
| Datadog integration | — | — | Included | Included |

¹ The pricing matrix conflicts with explanatory and setup content on Standard availability. Confirm the effective entitlement. Embedding scope must also be confirmed for each page.

## Data retention and API history

Console retention and the historical range available through REST APIs are different.

| Data path | Starter | Standard | Premium | Enterprise |
| --- | ---: | ---: | ---: | ---: |
| Call Inspector · Console | 3 days | 7 days | 14 days | 30 days |
| Call Inspector · REST API | Not available | 1 day | 7 days | 15 days |
| Data Insights · Console | Not available | 30 days | 60 days | 90 days |
| Data Insights · REST API | Not available | Not available | 14 days | 30 days |

This distinction directly affects support and retention design. For example, a Premium customer can view 14 days of calls in the Console, but the Call Inspector API only retrieves the previous 7 days.

If data must be retained beyond the plan's API history, collect it within the available window and store it in a customer-managed repository. The collection design must account for request quotas, data delay, failures, and retries.

Sources: [Agora Analytics plans and pricing](https://docs.agora.io/en/realtime-media/agora-analytics/reference/pricing), [Analytics REST API](https://docs.agora.io/en/api-reference/api-ref/agora-analytics/analytics-rest-api)

## What each capability does

| Capability | Role | Problem addressed | Customer value | Example |
| --- | --- | --- | --- | --- |
| Call Inspector | Inspect users, events, sender-receiver paths, and quality metrics for an individual call | A reported call issue is difficult to reproduce from the customer's description | Narrows the investigation and reduces support time | Search for a reported call and identify the affected user and time range |
| Data Insights | Aggregate usage and quality trends over time | Individual calls do not reveal recurring patterns across a voice, video, or live-streaming service | Supports operations and product decisions with trend data | Review hourly or daily join success and freeze-rate trends across the service |
| Data Insights Plus | Segment data with dimensions, samples, and comparative analysis | Affected countries, devices, or SDK versions are hidden by overall values | Narrows the affected population and finds calls to investigate | Observe quality by SDK version and drill into supported related calls |
| Real-time Monitoring | Observe recent conditions with short-interval aggregates | An operational issue in a calling or live-streaming service may be missed while waiting for retrospective reports | Detects an active issue sooner | Watch recent channel, user, and quality changes during service operation |
| Alerts | Notify email, WeCom, or an HTTP callback when thresholds or predefined events occur | Operators must otherwise watch the Console continuously | Starts the response workflow sooner | Notify a team channel when join success declines |
| Embedding | Display supported Analytics pages in a customer portal through an iframe | Operators switch between multiple consoles | Brings supported analysis into the team's existing workflow | Open call search inside a support portal |
| REST API | Retrieve supported call, aggregate, and real-time data from a customer server | A customer needs its own portal, storage, or data processing | Integrates analytics with customer-owned systems | Add the call list and supported service aggregates to an operations tool |
| Datadog integration | Send App ID-level RTC aggregate metrics to Datadog | Voice, video, or live-streaming RTC signals and infrastructure signals are separated across monitoring tools | Places service and RTC conditions on the same timeline | Compare server incidents with changes in join success |

Overview: [Agora Analytics product overview](https://docs.agora.io/en/realtime-media/agora-analytics/product-overview)

## The exact scope of Comparative Analysis

Data Insights Plus supports three comparative analysis modes.

| Mode | Behavior | Useful question |
| --- | --- | --- |
| Indicator comparison | Compare one primary indicator with up to three additional indicators for the same period | Did quality, usage, or network indicators move at the same time? |
| Time comparison | Compare the same indicator with the previous cycle, the corresponding period in the previous month, or a custom period | How does the current period differ from an earlier period of the same length? |
| Filtered group versus global | Compare a dimension-filtered group with the overall value | How does a country, device, or SDK group differ from the global result? |

A custom time comparison uses whole days and the same number of days as the current period. Dates must fall within the plan's available history. Selecting multiple indicators can clear an existing global dimension filter, so verify the filter state after changing indicators.

Do not describe this as a general-purpose A/B tool that directly compares any two arbitrary groups. An SDK version is also different from the customer's application version. A before-and-after change is an investigation clue, not proof of causation. Review geography, devices, network conditions, usage, and individual call evidence before reaching a conclusion.

Source: [Data Insights Plus](https://docs.agora.io/en/realtime-media/agora-analytics/build/explore-and-analyze-data/data-insight-plus)

## REST API design limits

The base URL is `https://api.agora.io`. A customer backend authenticates with HTTP Basic authentication using the **Customer ID and Customer Secret** created for Agora REST APIs. These credentials are different from a Datadog API key or RTC App Certificate and must not be shipped in a browser or mobile application.

Authentication source: [Analytics REST API authentication](https://docs.agora.io/en/api-reference/api-ref/agora-analytics/analytics-restful-authentication)

### Call Inspector API

| Plan | Per-second limit | Daily limit | Historical range |
| --- | ---: | ---: | ---: |
| Standard | 1 | 1,000 | 1 day |
| Premium | 3 | 2,000 | 7 days |
| Enterprise | 10 | 10,000 | 15 days |

The maximum time span per call-list request is 8 hours for Standard, 16 hours for Premium, and 24 hours for Enterprise. For session and detailed-metric requests, the limits are 1, 3, and 6 hours. Data delay also varies by endpoint, so evaluate history and freshness separately.

### Data Insights API

| Plan | Per-minute limit | Daily limit | Historical range | Maximum time-series request |
| --- | ---: | ---: | ---: | ---: |
| Premium | 3 | 40 | 14 days | 3 days |
| Enterprise | 10 | 60 | 30 days | 7 days |

Usage time series support daily and hourly granularity. Quality time series also support minute granularity. Dimension aggregation APIs use daily and hourly granularity for both usage and quality. Do not assume that REST APIs reproduce every filter and interaction available in the Data Insights Plus Console.

### Real-time Monitoring API

| Plan | Per-minute limit | Daily limit | History and maximum request | Data delay | Time-series granularity |
| --- | ---: | ---: | ---: | ---: | ---: |
| Premium | 3 | 480 | 40 minutes | 40 seconds | 20 seconds |
| Enterprise | 10 | 1,440 | 60 minutes | 20 seconds | 20 seconds |

Twenty-second data granularity does not grant permission to poll every 20 seconds. Polling once every 20 seconds for 24 hours produces **4,320 requests**, exceeding both daily quotas. One request every 3 minutes consumes all 480 Premium requests; one request every minute consumes all 1,440 Enterprise requests. Leave capacity for other metrics and retries.

Limits and endpoints: [Analytics REST API](https://docs.agora.io/en/api-reference/api-ref/agora-analytics/analytics-rest-api)

## Datadog integration scope

The Datadog integration is available for Premium and Enterprise after activation. Configure the metrics and Datadog API key in Agora, confirm the Online state, and then install the Agora Analytics integration in Datadog. Confirm the supported Datadog package and separate Datadog charges.

The RTC integration provides nine App ID-level aggregate metrics under the `agora.rtc.app_id.` prefix:

- Online users and channels
- Join attempts and successful joins
- Join success rate and success within five seconds
- Audio and video freeze rates
- Network delay rate

Metrics are calculated every minute, which does not guarantee that the complete collection-to-display path takes one minute. The standard integration does not provide raw UID- or channel-level logs, call recordings, or distributed traces. It also does not provide Datadog Events or Service Checks.

Retention and cost for metrics received by Datadog follow the customer's Datadog contract and settings. Do not apply Agora REST API quotas to the native Datadog delivery path or assume that the two products retain data for the same period.

Sources: [Agora Datadog integration guide](https://docs.agora.io/en/realtime-media/agora-analytics/build/integrate-and-embed/datadog-integration), [Datadog Agora Analytics integration](https://docs.datadoghq.com/integrations/agora-analytics/)

## Proposal checklist

- **Evaluate Premium first** when Comparative Analysis, Alerts, Datadog, or Data Insights and Monitoring APIs are required and Premium's retention and quotas are sufficient.
- **Evaluate Enterprise** when 30-day Call Inspector Console history, 90-day Data Insights Console history, a longer API range, or larger API quotas are operational requirements.
- **Long-term retention:** define the data, collection interval, storage location, and privacy policy when data must outlive Console or API history.
- **Embedding:** confirm the exact page, user authentication, permissions, and plan entitlement.
- **Metric interpretation:** quality thresholds and aggregation can vary by page. Confirm definitions before using Analytics data for billing or SLA decisions.

Two areas require confirmation because the public documentation is internally inconsistent or differs in scope:

1. The pricing matrix marks Plus multidimensional analysis for Standard, while explanatory and setup content describes it as Premium and Enterprise.
2. Confirm whether the Enterprise Alerts embedding entitlement in the pricing matrix matches the pages documented in the embedding implementation guide.

Do not interpret “customizable dashboard” as a guarantee that custom development services are included in the subscription. Confirm implementation scope and commercial terms separately.

## Official references

- [Product overview](https://docs.agora.io/en/realtime-media/agora-analytics/product-overview)
- [Plans and pricing](https://docs.agora.io/en/realtime-media/agora-analytics/reference/pricing)
- [Call Inspector](https://docs.agora.io/en/realtime-media/agora-analytics/build/explore-and-analyze-data/call-search)
- [Data Insights](https://docs.agora.io/en/realtime-media/agora-analytics/build/explore-and-analyze-data/data-insight)
- [Data Insights Plus](https://docs.agora.io/en/realtime-media/agora-analytics/build/explore-and-analyze-data/data-insight-plus)
- [Real-time Monitoring](https://docs.agora.io/en/realtime-media/agora-analytics/build/monitor-and-get-alerts/monitor)
- [Alerts](https://docs.agora.io/en/realtime-media/agora-analytics/build/monitor-and-get-alerts/alarm)
- [Embedding](https://docs.agora.io/en/realtime-media/agora-analytics/build/integrate-and-embed/embedded)
- [Analytics REST API](https://docs.agora.io/en/api-reference/api-ref/agora-analytics/analytics-rest-api)
- [Datadog integration](https://docs.agora.io/en/realtime-media/agora-analytics/build/integrate-and-embed/datadog-integration)
