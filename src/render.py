"""Render the Korean customer guide. Run scripts/build.py from the repository."""

from pathlib import Path
from html import escape
import base64
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://docs.agora.io/en/realtime-media/agora-analytics/'
URL = {
 'overview':BASE+'product-overview', 'pricing':BASE+'reference/pricing',
 'call':BASE+'build/explore-and-analyze-data/call-search',
 'insight':BASE+'build/explore-and-analyze-data/data-insight',
 'plus':BASE+'build/explore-and-analyze-data/data-insight-plus',
 'monitor':BASE+'build/monitor-and-get-alerts/monitor',
 'alerts':BASE+'build/monitor-and-get-alerts/alarm',
 'datadog':BASE+'build/integrate-and-embed/datadog-integration',
 'embed':BASE+'build/integrate-and-embed/embedded',
 'api':'https://docs.agora.io/en/api-reference/api-ref/agora-analytics/analytics-rest-api',
 'auth':'https://docs.agora.io/en/api-reference/api-ref/agora-analytics/analytics-restful-authentication',
 'dd':'https://docs.datadoghq.com/integrations/agora-analytics/'
}
def link(key,label):
 return f'<a class="source" href="{URL[key]}" target="_blank" rel="noopener noreferrer" aria-label="{label} (새 탭)">{label}<span aria-hidden="true"> ↗</span></a>'
def table(head,rows,cls=''):
 return '<p class="table-help">표를 좌우로 밀어 전체 내용을 확인하세요.</p><div class="table-scroll" tabindex="0" role="region" aria-label="'+escape(head[0])+' 비교표 (가로 스크롤 가능)"><table class="'+cls+'"><thead><tr>'+''.join('<th scope="col">'+x+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<th scope="row">'+v+'</th>' if i==0 else '<td>'+v+'</td>' for i,v in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div>'
def detail(title,content,id=''):
 return f'<details{(" id="+chr(34)+id+chr(34)) if id else ""}><summary>{title}<span aria-hidden="true">+</span></summary><div class="detail-body">{content}</div></details>'
YES='<span class="yes">포함</span>'
NO='<span class="no" aria-label="미포함">—</span>'
css = (ROOT / 'src/styles/base.css').read_text(encoding='utf-8')

parts=['<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Agora Analytics의 플랜별 데이터 보존기간, REST API 조회 범위·호출 한도, 주요 기능을 비교합니다."><title>Agora Analytics 플랜 비교 가이드</title><style>'+css+'</style></head><body><a class="skip" href="#retention">본문으로 이동</a>']
parts.append('<div class="wrap"><header class="top"><div class="document-title"><strong>Agora Analytics</strong><span>플랜 비교 가이드</span></div><div class="top-links">'+link('overview','공식 제품 안내')+'<button type="button" class="print" id="print-page">인쇄 / PDF 저장</button></div></header><div class="hero"><div><h1>좋은 통화 경험을 위한<br>분석과 모니터링</h1><p class="intro">통화 문제를 조사할 수 있는 기간부터 확인하세요. 데이터 보존기간과 REST API 조회 범위, 필요한 분석 기능을 기준으로 플랜을 선택할 수 있습니다.</p><div class="hero-actions"><a class="button primary" href="#retention">보존·조회 기간 비교</a><a class="button secondary" href="#plans">플랜 비교하기</a></div></div><aside class="history-hero" aria-labelledby="history-hero-title"><h2 id="history-hero-title">통화 상세를 확인할 수 있는 기간</h2><p>Call Inspector · Console과 REST API 기준</p><table aria-label="Premium과 Enterprise 통화 상세 조회 기간"><thead><tr><th scope="col">조회 경로</th><th scope="col">Premium</th><th scope="col">Enterprise</th></tr></thead><tbody><tr><th scope="row">Console 보존</th><td>14<small>일</small></td><td>30<small>일</small></td></tr><tr class="api-row"><th scope="row">REST API 조회</th><td>7<small>일</small></td><td>15<small>일</small></td></tr></tbody></table><p>같은 플랜이라도 화면과 API에서 확인할 수 있는 과거 범위가 다릅니다.</p>'+link('pricing','Console 기준')+' · '+link('api','API 기준')+'</aside></div></div>')
parts.append('<div class="nav-shell"><nav class="wrap nav" aria-label="페이지 목차"><a href="#retention" aria-current="location">보존·조회 기간</a><a href="#features">활용 기능</a><a href="#plans">플랜 비교</a><a href="#comparison">비교 분석</a><a href="#integration">Datadog·API</a><a href="#conditions">제공 조건</a></nav></div><main class="wrap">')

parts.append('<section class="section" id="retention"><div class="section-head"><div><h2>얼마나 오래 확인할 수 있나요?</h2><p>늦게 접수된 문의를 조사하거나 과거 추세를 비교하려면, 필요한 데이터와 조회 경로의 기간을 함께 확인해야 합니다.</p></div></div><div class="retention-intro"><p><strong>Console 보존기간</strong><br>Agora 분석 화면에서 확인할 수 있는 과거 이력입니다.</p><p><strong class="api-word">REST API 과거 조회 범위</strong><br>고객 서버가 API로 가져올 수 있는 과거 이력입니다. 한 번의 요청에 담을 수 있는 구간은 별도 제한을 따릅니다.</p></div>')
parts.append(table(['데이터 · 조회 경로','Starter','Standard','Premium','Enterprise'],[
 ['통화 상세 · Console<small>Call Inspector 보존기간</small>','<b>3일</b>','<b>7일</b>','<b>14일</b>','<b>30일</b>'],
 ['통화 상세 · REST API<small>Call Inspector 과거 조회 범위</small>',NO,'<b>1일</b>','<b>7일</b>','<b>15일</b>'],
 ['사용량·품질 집계 · Console<small>Data Insights 보존기간</small>',NO,'<b>30일</b>','<b>60일</b>','<b>90일</b>'],
 ['사용량·품질 집계 · REST API<small>Data Insights 과거 조회 범위</small>',NO,NO,'<b>14일</b>','<b>30일</b>']
 ],'matrix retention-matrix'))
parts.append('<p class="muted">— 미제공. 표의 기간은 조회 가능한 과거 범위입니다. 데이터 반영 지연과 1회 요청 구간 제한은 별도로 적용됩니다.</p><div class="table-links">'+link('pricing','Console 보존기간 근거')+link('api','REST API 조회 범위 근거')+'</div><div class="retention-note"><div><h3>90일 집계와 30일 통화 상세를 구분하세요</h3><p>Enterprise의 90일 보존은 Data Insights 집계 데이터 기준입니다. 통화 상세는 Console에서 30일, REST API에서 15일 범위로 확인합니다.</p></div><div><h3>더 오래 보관하려면 별도 수집·저장이 필요합니다</h3><p>필요한 데이터를 API 조회 가능 기간 안에 고객 저장소로 수집하는 방식을 검토하세요. 수집한 데이터의 보관기간은 고객 시스템에서 관리합니다. API별 제공 필드와 호출 한도에 맞춘 구현이 필요합니다.</p></div></div>')
parts.append('<div class="api-essential" id="api-essentials"><h3>REST API는 조회 기간과 호출 한도를 함께 봐야 합니다</h3><p>정기 수집과 과거 데이터 조회를 계획할 때, 아래 한도에 페이지 조회·지표별 요청·재시도를 위한 여유를 두세요.</p>')
parts.append(table(['API별 요청 한도','Standard','Premium','Enterprise'],[
 ['Call Inspector','<b>일 1,000회</b><small>초당 1회 이하</small>','<b>일 2,000회</b><small>초당 3회 이하</small>','<b>일 10,000회</b><small>초당 10회 이하</small>'],
 ['Data Insights',NO,'<b>일 40회</b><small>분당 3회 이하</small>','<b>일 60회</b><small>분당 10회 이하</small>'],
 ['Real-time Monitoring',NO,'<b>일 480회</b><small>분당 3회 이하 · 최근 40분 조회</small>','<b>일 1,440회</b><small>분당 10회 이하 · 최근 60분 조회</small>']
 ],'matrix'))
parts.append('<p><b>실시간 API의 40분·60분은 과거 조회 범위이자 1회 최대 조회 구간입니다.</b> 데이터는 20초 단위로 제공되며, 20초마다 하루 종일 호출하면 4,320회로 두 플랜의 일별 한도를 넘습니다. 수집 중단 후 누락 구간을 다시 가져올 때도 조회 범위를 확인해야 합니다.</p><p class="muted">호출 한도는 서버 UTC 기준으로 계산됩니다. 위 수치는 각 API 문서의 제한이며, 실제 계정의 적용 단위와 한도는 도입 시 확인해주세요.</p><div class="table-links"><a class="source" href="#api-limits">API별 1회 조회 구간·반영 지연 자세히 보기</a>'+link('api','공식 API 한도')+'</div></div></section>')

jobs=[
 ('investigate','통화 문제 조사','어느 통화에서 문제가 생겼나요?','문제가 생긴 통화를 찾아,<br>사용자별로 확인합니다.','재현하기 어려운 문의도 통화 시간·채널·사용자 정보를 바탕으로 조사할 수 있습니다. 송신자와 수신자의 상태를 나눠 보며 확인할 범위를 좁힙니다.',[
  ('Call Inspector','전 플랜','통화 검색, 사용자별 품질 지표와 이벤트, 송신자–수신자 구간을 확인합니다.'),
  ('Call Overview','Premium · Enterprise','하나의 통화에서 품질 분포와 영향 사용자군을 살펴, 조사 우선순위를 정합니다.')],
  '통화 상세는 플랜별 보존기간 안에서 조회할 수 있습니다. Call Diagnosis는 가능한 원인을 제시하는 Beta 기능이며, 진단 결과는 추가 확인에 활용합니다. 통화 녹화·재생 기능은 포함하지 않습니다.','call','Call Inspector 자세히 보기'),
 ('operate','운영 상태 확인','지금 통화 품질은 어떤가요?','운영 중 품질을 관찰하고,<br>설정한 조건에 따라 알림을 받습니다.','진행 중인 수업·상담·라이브 이벤트의 규모와 품질을 살펴보고 이상 징후가 나타난 통화로 조사를 이어갑니다.',[
  ('Real-time Monitoring','Standard 이상','최근 30분의 규모·품질을 확인합니다. 주요 값은 20초, 품질 히트맵은 60초마다 갱신됩니다.'),
  ('Alert notifications','Premium · Enterprise','설정한 지표 임계값이나 이벤트 조건에 따라 이메일·WeCom·HTTP 알림을 받습니다.')],
  '화면 갱신 주기는 장애 탐지 시간의 보장이 아닙니다. 알림 조건과 대응 담당자 설정이 필요하며, 지원 지표는 SDK·플랫폼에 따라 다를 수 있습니다.','monitor','실시간 모니터링 자세히 보기'),
 ('analyze','품질 변화 분석','어떤 환경에서 반복되나요?','전체 추세와 특정 환경의<br>품질 변화를 살펴봅니다.','사용량 증가, 지역·기기별 차이, 변경 전후 추세를 함께 검토해 추가 조사가 필요한 환경을 찾습니다.',[
  ('Data Insights','Standard 이상','주기적으로 집계되는 사용량·품질 시계열과 환경별 분포를 확인합니다.'),
  ('Data Insights Plus','Premium · Enterprise 기준','최대 3개 차원 필터, 품질 샘플 드릴다운, 지표·기간·전체값 비교로 분석을 확장합니다.')],
  '집계 분석의 데이터 반영에는 지연이 있습니다. 샘플링은 조사할 통화·사용자를 찾는 기능이며 전체 사용자의 통계적 대표성을 보장하지 않습니다.','plus','Data Insights Plus 자세히 보기'),
 ('connect','업무 도구 연동','기존 도구에서 볼 수 있나요?','통화 데이터를 기존<br>관제·업무 도구에 연결합니다.','이미 사용하는 대시보드와 고객 지원 화면에 분석을 연결해 도구를 오가는 작업을 줄일 수 있습니다.',[
  ('Datadog','Premium · Enterprise','RTC 집계 지표를 기존 Datadog 운영 지표와 함께 확인합니다.'),
  ('REST API · Embed','기능별 제공 플랜 상이','API로 데이터를 직접 조회·가공하거나, 지원되는 분석 화면을 내부 포털에 넣습니다.')],
  'Datadog 활성화·패키지 조건, API 조회 한도, 임베딩할 페이지와 사용자 접근 권한을 확인해야 합니다.','api','Analytics API 자세히 보기')
]
parts.append('<section class="section" id="features"><div class="section-head"><div><h2>필요한 업무부터 살펴보세요</h2><p>하나의 통화 조사부터 서비스 전체 분석까지, 업무에 맞는 기능을 연결할 수 있습니다.</p></div></div><div class="explorer"><div class="jobs" role="tablist" aria-label="업무별 기능">')
for i,(key,title,question,*_) in enumerate(jobs):
 parts.append(f'<button type="button" id="job-{key}" role="tab" aria-controls="panel-{key}" aria-selected="{"true" if i==0 else "false"}" tabindex="{0 if i==0 else -1}" data-job="{key}">{title}<small>{question}</small></button>')
parts.append('</div><div>')
for key,title,question,headline,body,capabilities,conditions,source,label in jobs:
 parts.append(f'<article class="job-panel" id="panel-{key}" role="tabpanel" aria-labelledby="job-{key}" tabindex="0"><h3>{headline}</h3><p>{body}</p><div class="capabilities">'+''.join(f'<div class="capability"><strong>{name}<small>{tier}</small></strong><p>{desc}</p></div>' for name,tier,desc in capabilities)+'</div>'+detail('이용 조건',f'<p>{conditions}</p>')+link(source,label)+'</article>')
parts.append('</div></div></section>')

parts.append('<section class="section" id="plans"><div class="section-head"><div><h2>운영 범위에 맞는 플랜</h2><p>개별 통화 확인에서 시작해, 집계 분석·알림·외부 연동으로 확장할 수 있습니다.</p></div>'+link('pricing','공식 플랜·가격')+'</div><div class="plans">')
for name,price,purpose,note in [
 ('Starter','$0','최근 통화의 기본 상태 확인','통화 상세 · Console / API<br><b>3일 / 미제공</b>'),
 ('Standard','$449','통화 조사와 서비스 현황 분석','통화 상세 · Console / API<br><b>7일 / 1일</b>'),
 ('Premium','$999','심화 분석과 운영 도구 연동','통화 상세 · Console / API<br><b>14일 / 7일</b>'),
 ('Enterprise','$1,599','더 긴 조회 범위와 높은 API 한도','통화 상세 · Console / API<br><b>30일 / 15일</b>')]:
 parts.append(f'<article class="plan"><h3>{name}</h3><div class="price">{price}<small>USD / 월</small></div><p>{purpose}</p><p class="plan-note">{note}</p></article>')
parts.append('</div><p class="muted">Analytics 월 구독료의 공개 정가입니다. RTC 사용료와 Datadog 이용료는 각 서비스의 요금·계약 조건을 따릅니다. 아래 보존기간은 Console 화면 기준이며, API 조회 범위는 별도로 적용됩니다.</p>')
parts.append('<p class="callout"><b>Premium과 Enterprise 선택 기준:</b> 비교 분석·알림·Datadog 연동은 두 플랜 모두 제공합니다. 통화가 끝난 뒤 언제까지 조사해야 하는지, API로 얼마나 오래된 데이터를 가져와야 하는지를 기준으로 선택하세요. Enterprise는 더 긴 보존·조회 기간과 더 높은 API 한도를 제공하며, 공개 정가 차이는 월 $600입니다. <a href="#retention">기간과 한도 비교로 이동</a></p>')
parts.append(table(['주요 기능 · Console 기준','Starter','Standard','Premium','Enterprise'],[
 ['Call Inspector · 통화 조사','3일 보존','7일 보존','14일 보존','30일 보존'],
 ['Call Overview · 통화 전체 요약',NO,NO,YES,YES],
 ['Data Insights · 집계 분석',NO,'30일 보존','60일 보존','90일 보존'],
 ['Plus · 다차원 필터',NO,'<a class="confirm" href="#plus-scope">제공 범위 확인¹</a>',YES,YES],
 ['Plus · 품질 샘플 드릴다운',NO,NO,YES,YES],
 ['Plus · Comparative Analysis',NO,NO,YES,YES],
 ['Real-time Monitoring',NO,YES,YES,YES],
 ['Alert notifications',NO,NO,YES,YES],
 ['Datadog 연동',NO,NO,'별도 활성화','별도 활성화'],
 ['Call Inspector API',NO,'Standard 한도','Premium 한도','Enterprise 한도'],
 ['Data Insights · Monitoring API',NO,NO,YES,YES],
 ['분석 화면 임베딩',NO,'Call Inspector<br>Monitoring','Call Inspector<br>Data Insights · Monitoring','Call Inspector<br>Data Insights · Monitoring<br>Alerts 제공 범위 확인²']
 ],'matrix'))
parts.append('<div class="conditions"><p id="plus-scope"><b>¹ Data Insights Plus:</b> Premium·Enterprise 기준으로 안내합니다. Standard의 다차원 필터 제공 여부는 도입 전 확인이 필요합니다.</p><p><b>² 임베딩:</b> 지원되는 페이지에 한해 제공됩니다. Enterprise의 Alerts 임베딩과 필요한 상세 화면의 지원 여부는 도입 전 확인해주세요.</p></div>')
parts.append(detail('집계 단위와 데이터 반영 시간 비교',
 '<p>집계 단위는 차트 한 점이 나타내는 시간 범위입니다. 데이터 반영 지연과 구분해서 확인해주세요.</p>'+table(['Data Insights','Standard','Premium','Enterprise'],[
 ['사용량 집계 단위','일','일 · 시간','일 · 시간'],
 ['품질 집계 단위','일 · 시간','일 · 시간 · 분','일 · 시간 · 분'],
 ['사용량 반영 지연','24시간','12시간','6시간'],
 ['품질 반영 지연','12시간','6시간','6시간']
 ],'matrix')+'<p>Data Insights는 과거 추세 분석에 활용합니다. 진행 중인 상태를 확인하려면 Real-time Monitoring을 사용하세요. Data Insights Plus의 조회 범위는 플랜의 보존기간과 화면의 조회 기간 제한을 함께 따릅니다.</p>'+link('insight','Data Insights 집계 기준')))
parts.append(detail('통화 조사·샘플링·임베딩의 상세 범위',
 '<ul class="clean"><li><b>Call Details:</b> 최대 20명의 사용자를 동시에 선택해 상세 지표와 이벤트를 확인합니다. 통화 녹음·녹화 재생 기능은 아닙니다.</li><li><b>Call Overview:</b> 통화 전체 품질을 요약합니다. 참여자 수가 적은 통화에서는 일부 통계가 표시되지 않을 수 있습니다.</li><li><b>Call Diagnosis:</b> 최대 10명 대상의 Beta 진단 기능입니다. 관측된 현상에 대한 가능한 원인을 제시하며, 이용 가능한 범위는 계정에서 확인해주세요.</li><li><b>Plus 품질 샘플:</b> 오디오 끊김·비디오 끊김·네트워크 지연율에서 30분 구간, 최대 500개 행을 조회해 통화 상세로 이동합니다. 전체 영향 사용자 수를 추정하는 대표 표본으로 해석하지 않습니다.</li><li><b>임베딩:</b> 서버에서 접근 URL을 발급해 지원 화면을 iframe으로 표시합니다. 문서에 명시된 페이지는 통화 검색, Data Insights 사용량, 실시간 모니터링이며 접근 토큰은 2시간 유효합니다.</li></ul>'+link('call','통화 분석 범위')+' · '+link('plus','Plus 샘플링')+' · '+link('embed','임베딩 가이드')))
parts.append('</section>')

parts.append('<section class="section" id="comparison"><div class="section-head"><div><h2>비교 분석으로 달라진 점을 찾습니다</h2><p>Comparative Analysis는 지표 간 비교, 기간 비교, 선택한 조건과 전체값 비교를 제공합니다.</p><span class="scope">Data Insights Plus · Premium / Enterprise</span></div>'+link('plus','공식 기능 가이드')+'</div><div class="comparisons">')
for title,en,body,example in [
 ('지표 간 비교','Indicator comparison','같은 기간에 서로 다른 지표를 함께 표시합니다. 기준 지표에 최대 3개를 더해 총 4개 지표를 살펴볼 수 있습니다.','사용량이 증가한 시점에 오디오 끊김률도 함께 변했는지 확인합니다.'),
 ('기간 비교','Time comparison','같은 지표를 직전 비교 주기, 지난달 대응 기간 또는 직접 지정한 기간과 비교합니다.','SDK 업데이트 전후의 동일 길이 기간을 비교해 품질 변화가 나타나는지 확인합니다.'),
 ('전체값 비교','Global comparison','차원 필터로 선택한 그룹의 기준 지표를 전체 데이터의 같은 지표와 비교합니다.','한국 사용자 그룹의 비디오 끊김률이 전체값과 얼마나 차이 나는지 확인합니다.')]:
 parts.append(f'<article class="comparison"><h3>{title}<small>{en}</small></h3><p>{body}</p><p class="example"><span>활용 예</span>{example}</p></article>')
parts.append('</div><p class="muted" style="margin-top:16px">관찰된 변화의 원인을 판단할 때는 이용 지역·기기·네트워크·사용량을 함께 검토하세요.</p><div class="callout"><b>지역·SDK 버전별 차이도 분석할 수 있습니다.</b> 차원별 분석과 필터를 사용하세요. Comparative Analysis의 전체값 비교는 <b>선택한 그룹과 전체</b>를 비교하는 방식입니다. 특정 두 그룹을 직접 나란히 비교하는 맞춤 화면은 REST API로 별도 구성할 수 있습니다.</div>')
parts.append(detail('비교 조건과 결과를 해석할 때 확인할 점',
 '<ul class="clean"><li><b>직접 지정하는 기간:</b> 일 단위로 선택하며 현재 기간과 같은 일수여야 합니다. 시작일은 플랜의 조회 가능 범위 안에 있어야 합니다. 자동 기간 비교는 화면에 표시되는 실제 날짜를 확인하세요.</li><li><b>필터:</b> 최대 3개 차원을 조합할 수 있습니다. 여러 지표를 비교하도록 바꾸면 기존 전역 차원 필터가 해제될 수 있으므로 적용 상태를 다시 확인해주세요. 전체값 비교에는 기준 지표와 차원 필터가 필요합니다.</li><li><b>비교 차원:</b> 국가·지역·OS·기기·SDK 제품·SDK 버전·네트워크 유형 등을 사용합니다. 선택 가능한 차원은 지표에 따라 다릅니다. SDK 버전은 고객 애플리케이션의 버전과 다릅니다.</li><li><b>변화의 의미:</b> 배포 전후의 차이만으로 배포가 원인이라고 단정할 수는 없습니다. 이용 지역, 기기, 네트워크와 사용량 변화를 함께 살펴보세요.</li></ul>'+link('plus','비교 분석·필터 조건')))
parts.append('</section>')

parts.append('<section class="section" id="integration"><div class="section-head"><div><h2>Datadog과 업무 시스템에 연결</h2><p>기존 관제에 RTC 지표를 더하거나, 필요한 데이터를 직접 조회해 맞춤 화면을 구성할 수 있습니다.</p></div></div><div class="integrations"><article class="integration"><h3>Datadog 연동</h3><p class="sub">기존 관제 화면에서 RTC 상태도 함께 확인</p><div class="route" aria-label="Datadog 데이터 흐름"><b>Agora Analytics</b><span aria-hidden="true">→</span><b>Datadog</b></div><p>기본 연동을 활성화하면 Agora가 App ID별 RTC 집계 지표를 Datadog으로 전송합니다. 서비스 인프라 지표와 같은 시간축에서 비교하고 Datadog의 대시보드·모니터에 활용할 수 있습니다.</p><span class="scope">Premium / Enterprise · 활성화 신청 필요</span><ul class="clean"><li>온라인 사용자·채널, 입장 성공, 미디어 품질 등 RTC 지표 9개</li><li>각 지표는 매분 계산되는 App ID 수준의 집계값</li><li>Datadog 지원 패키지와 API Key 설정 필요</li></ul>'+link('datadog','Agora 연동 가이드')+' · '+link('dd','Datadog 통합 문서')+'</article><article class="integration"><h3>REST API</h3><p class="sub">내부 포털·데이터 파이프라인을 직접 구성</p><div class="route" aria-label="REST API 데이터 흐름"><b>고객 서버</b><span aria-hidden="true">↔</span><b>Agora API</b><span aria-hidden="true">→</span><b>업무 시스템</b></div><p>고객 서버에서 통화·집계·실시간 데이터를 조회합니다. 고객 지원 화면에 통화 정보를 연결하거나, 지원 차원별 값을 가져와 자체 대시보드에서 비교할 수 있습니다.</p><span class="scope">Call Inspector: Standard 이상 · 그 외: Premium 이상</span><ul class="clean"><li>조회·저장·가공·재시도 로직을 고객 시스템에서 구현</li><li>분당·일별 호출 한도와 조회 가능 기간 적용</li><li>Console의 모든 기능·보존기간과 일치하지 않음</li></ul>'+link('api','REST API 레퍼런스')+'</article></div>')
parts.append(table(['도입 방식','Datadog 기본 연동','REST API로 직접 구성'],[
 ['주요 목적','기존 Datadog 관제에 RTC 집계 지표 추가','자체 포털·보고서·데이터 분석 구성'],
 ['수집 방식','Agora가 지표 전송','고객 서버가 API로 조회'],
 ['데이터 범위','App ID별 RTC 집계 지표 9개','API별 통화·사용량·품질·차원 데이터'],
 ['외부 저장 후 보존기간','수신한 지표의 보존기간은 Datadog 계약·설정 기준','조회 가능한 기간 안에 수집한 데이터는 고객 저장소의 보존 정책 기준'],
 ['구축·운영','활성화·키 설정 후 대시보드 구성','수집기·저장소·오류 처리 직접 운영'],
 ['선택 시 고려점','빠르게 연결할 수 있으나 기본 지표·집계 범위에 맞춰 활용','조회·가공이 유연하나 개발·운영과 호출 한도 설계 필요']
 ],'text-table'))
parts.append('<div class="callout"><b>실시간 요구 수준에 맞춰 수집 방식을 선택하세요.</b> 20초 단위 데이터가 제공되더라도 API를 하루 종일 20초마다 호출할 수 있다는 의미는 아닙니다. Datadog 기본 연동, 알림 또는 API 수집 주기를 목적에 맞게 선택해야 합니다.</div>')
parts.append(detail('Datadog: 전송 지표·설정·지원 범위',
 '<p>RTC 기본 지표의 접두사는 <code>agora.rtc.app_id.</code>입니다.</p>'+table(['지표 이름 · 접두사 제외','역할'],[
 ['<code>online_user</code> · <code>online_channel</code>','접속 규모와 활성 채널 상태 파악'],
 ['<code>join_attempt</code> · <code>join_success_count</code>','입장 시도 수와 성공 수 확인'],
 ['<code>join_success_rate</code> · <code>join_success_in_5s_rate</code>','입장 성공률과 5초 이내 성공률 확인'],
 ['<code>audio_freeze_rate</code> · <code>video_freeze_rate</code>','오디오·비디오 끊김 정도 관찰'],
 ['<code>network_delay_rate</code>','네트워크 지연 정도 관찰']
 ],'text-table')+
 '<h4>설정 흐름</h4><p>Agora에서 연동 활성화 신청 → 전송 지표 선택 및 Datadog API Key 설정 → Online 상태 확인 → Datadog의 Agora Analytics 통합 설치·대시보드 구성 순으로 진행합니다.</p>'+
 '<h4>지원 범위</h4><ul class="clean"><li>기본 연동은 UID·채널별 상세 로그, 통화 녹화, 트레이스를 제공하는 경로가 아닙니다. 국가·SDK 버전 등 추가 태그와 사용자 단위 분석이 필요하면 별도 데이터 수집 가능 범위를 확인해주세요.</li><li>Datadog 공식 통합은 Events와 Service Checks를 제공하지 않습니다. 수신한 지표를 사용하는 Datadog 모니터 설정과는 구분됩니다.</li><li>매분 계산은 수집부터 화면 반영까지 1분을 보장한다는 뜻이 아닙니다. 활성화·비활성화 변경 후 전송 재개·중단에는 최대 5분이 걸릴 수 있습니다.</li><li>Datadog의 비용·보존기간·지원 패키지는 해당 계약 조건을 따릅니다. Agora REST API 조회 한도를 Datadog 기본 전송에 그대로 적용하지 않습니다.</li></ul>'+link('datadog','연동 설정·지표')+' · '+link('dd','Datadog 지원 범위')))
parts.append(detail('REST API: 인증과 주요 엔드포인트',
 '<p>기본 주소는 <code>https://api.agora.io</code>입니다. Agora Console의 REST API용 <b>Customer ID와 Customer Secret</b>으로 HTTP Basic 인증을 구성하고 서버에서 호출합니다. Datadog API Key나 RTC App Certificate를 사용하는 인증과 다릅니다.</p>'+table(['용도','메서드 · 경로'],[
 ['통화 목록·사용자 세션·상세 지표','GET <code>/beta/analytics/call/lists</code><br>GET <code>/beta/analytics/call/sessions</code><br>GET <code>/beta/analytics/call/metrics</code>'],
 ['집계 시계열','GET <code>/beta/insight/usage/by_time</code><br>GET <code>/beta/insight/quality/by_time</code>'],
 ['차원별 집계','POST <code>/beta/insight/usage/aggregation</code><br>POST <code>/beta/insight/quality/aggregation</code>'],
 ['실시간 시계열','GET <code>/beta/realtime/usage/by_time_20sec</code><br>GET <code>/beta/realtime/quality/by_time_20sec</code>'],
 ['실시간 차원별 상위 20개','GET <code>/beta/realtime/usage/dimension/top20</code><br>GET <code>/beta/realtime/quality/dimension/top20</code>']
 ],'text-table')+
 '<p>집계 API의 <code>sdkVersion</code>과 실시간 API의 <code>sdk</code>처럼 차원 이름은 API마다 다릅니다. 지원되는 <code>dimensionValues</code>로 두 버전의 값을 조회해 맞춤 비교 화면을 구성할 수 있습니다. Plus 화면의 모든 필터·비교 동작이 API에 동일하게 제공되는 것은 아닙니다.</p>'+link('auth','REST 인증 가이드')+' · '+link('api','요청·응답 필드')))
parts.append(detail('REST API: 플랜별 호출 한도와 조회 범위',
 '<p>아래는 API 문서의 공개 플랜 기준입니다. 서로 다른 API에 동일한 한도를 가정하지 마세요. 계정의 실제 한도와 적용 단위는 도입 시 확인해주세요.</p><h4>Call Inspector API</h4>'+table(['항목','Standard','Premium','Enterprise'],[
 ['호출 한도','초당 1회 · 일 1,000회','초당 3회 · 일 2,000회','초당 10회 · 일 10,000회'],
 ['조회 가능한 과거 데이터','1일','7일','15일'],
 ['통화 목록 · 1회 조회 구간','8시간','16시간','24시간'],
 ['통화 목록 · 데이터 지연','60초','20초','20초'],
 ['세션·지표 · 1회 조회 구간','1시간','3시간','6시간'],
 ['세션·지표 · 데이터 지연','300초','150초','100초']
 ],'matrix')+'<h4>Data Insights API</h4>'+table(['항목','Premium','Enterprise'],[
 ['호출 한도','분당 3회 · 일 40회','분당 10회 · 일 60회'],
 ['조회 가능한 과거 데이터','14일','30일'],
 ['시계열 API · 1회 최대 조회 구간','3일','7일'],
 ['사용량 · 데이터 지연','12시간','6시간'],
 ['품질 · 데이터 지연','6시간','6시간'],
 ['시계열 집계 단위','사용량: 일·시간<br>품질: 일·시간·분','사용량: 일·시간<br>품질: 일·시간·분'],
 ['차원별 집계 단위','사용량·품질 모두 일·시간','사용량·품질 모두 일·시간']
 ],'matrix')+'<h4>Real-time Monitoring API</h4>'+table(['항목','Premium','Enterprise'],[
 ['호출 한도','분당 3회 · 일 480회','분당 10회 · 일 1,440회'],
 ['과거 조회 범위 · 1회 최대 구간','40분','60분'],
 ['데이터 지연','40초','20초'],
 ['시계열 단위','20초','20초']
 ],'matrix')+
 '<p><b>수집 주기 예:</b> 하루 24시간 동안 20초마다 한 번 호출하면 4,320회입니다. 실시간 API의 두 플랜 모두 일별 한도를 넘습니다. 한 번 호출할 때 최근 구간의 여러 20초 데이터 포인트를 가져올 수 있으므로, 필요한 신선도와 하루 총 호출량을 함께 설계하세요.</p><p>Premium에서 3분마다, Enterprise에서 1분마다 하나의 호출을 하면 각각 일 480회·1,440회로 일별 한도를 모두 사용합니다. 다른 지표 조회·재시도를 위한 여유가 필요합니다.</p>'+link('api','공식 API 한도·데이터 지연'), 'api-limits'))
parts.append('</section>')

parts.append('<section class="section" id="conditions"><div class="section-head"><div><h2>도입 전 확인할 제공 조건</h2><p>원하는 분석 화면과 운영 방식에 맞춰 다음 항목을 확인해주세요.</p></div></div><div class="onboarding"><h3>필요한 데이터 범위를<br>먼저 정하세요</h3><ul><li><b>조회 기간:</b> Console 화면과 API에서 각각 며칠 전 데이터가 필요한가요?</li><li><b>데이터 반영 시간:</b> 진행 중인 통화 대응인지, 다음 날 추세 분석인지 구분해주세요.</li><li><b>분석 수준:</b> App ID 전체 집계, 국가·SDK 차원 분석, 개별 통화 중 필요한 범위를 정해주세요.</li><li><b>연동 방식:</b> Datadog 패키지, API 호출량, 임베딩할 화면과 접근 권한을 확인해주세요.</li><li><b>최종 제공 범위:</b> Standard의 Plus 다차원 필터와 Enterprise의 Alerts 임베딩은 도입 전 확인이 필요합니다.</li></ul></div>')
parts.append(detail('품질 지표를 읽을 때 알아둘 점',
 '<ul class="clean"><li><b>화면별 정의:</b> 비디오 끊김 판정 기준은 Plus에서 500ms 초과, 기본 Data Insights에서 600ms 초과로 다릅니다. Monitoring은 Native 600ms, Web 500ms 기준을 사용합니다. 서로 다른 화면의 값을 비교할 때 지표 정의를 확인해주세요.</li><li><b>비율의 의미:</b> 끊김률·지연율은 해당 지표의 시간 기반 비율입니다. 문제가 발생한 사용자 비율과 같은 의미가 아닙니다. Plus의 네트워크 지연율은 네트워크 지터를 제외합니다.</li><li><b>사용자 수:</b> UID 기반 집계가 실제 사람 수와 항상 같지는 않습니다. 기기·계정·UID 설계에 따라 해석이 달라집니다.</li><li><b>운영 지표와 계약 지표:</b> 품질 분석 지표를 청구 사용량이나 계약 SLA 판정값과 동일하게 사용하려면 별도 정의와 집계 기준 확인이 필요합니다.</li></ul>'+link('insight','기본 집계 지표')+' · '+link('plus','Plus 품질 지표')+' · '+link('monitor','Monitoring 지표')))
parts.append('</section></main><footer class="footer"><div class="wrap"><p><b>Agora Analytics 기능과 플랜 안내</b> · 2026년 9월 14일 공개 문서 기준</p><p>기능·가격·조회 한도는 변경될 수 있습니다. 실제 제공 범위는 적용 플랜, SDK·플랫폼, 활성화 상태와 계약 조건에 따라 확인해주세요.</p><div class="footer-links">'+link('overview','제품 개요')+link('pricing','플랜·가격')+link('plus','Data Insights Plus')+link('api','REST API')+link('datadog','Datadog 연동')+'</div></div></footer>')
parts.append('''<script>
document.documentElement.classList.add('js');
const jobTabs = [...document.querySelectorAll('[data-job]')];
function selectJob(tab, focus=false) {
  jobTabs.forEach(item => {
    const active = item === tab;
    item.setAttribute('aria-selected', String(active));
    item.tabIndex = active ? 0 : -1;
    document.getElementById(item.getAttribute('aria-controls')).hidden = !active;
  });
  if (focus) tab.focus();
}
jobTabs.forEach((tab, index) => {
  tab.addEventListener('click', () => selectJob(tab));
  tab.addEventListener('keydown', event => {
    let next;
    if (['ArrowRight','ArrowDown'].includes(event.key)) next = (index + 1) % jobTabs.length;
    if (['ArrowLeft','ArrowUp'].includes(event.key)) next = (index - 1 + jobTabs.length) % jobTabs.length;
    if (event.key === 'Home') next = 0;
    if (event.key === 'End') next = jobTabs.length - 1;
    if (next !== undefined) { event.preventDefault(); selectJob(jobTabs[next], true); }
  });
});
selectJob(jobTabs[0]);
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', () => {
    const target = document.getElementById(link.hash.slice(1));
    if (target?.tagName === 'DETAILS') target.open = true;
  });
});
const directTarget = document.getElementById(location.hash.slice(1));
if (directTarget?.tagName === 'DETAILS') directTarget.open = true;
document.getElementById('print-page').addEventListener('click', () => window.print());
let closedDetails = [];
window.addEventListener('beforeprint', () => {
  closedDetails = [...document.querySelectorAll('details:not([open])')];
  closedDetails.forEach(item => item.open = true);
});
window.addEventListener('afterprint', () => {
  closedDetails.forEach(item => item.open = false);
  closedDetails = [];
});
const sections = [...document.querySelectorAll('main > section')];
const navLinks = [...document.querySelectorAll('.nav a')];
let scrollPending = false;
function updateNav() {
  let active = sections[0];
  sections.forEach(section => { if (section.getBoundingClientRect().top <= 160) active = section; });
  navLinks.forEach(a => {
    if (a.hash === '#' + active.id) a.setAttribute('aria-current','location');
    else a.removeAttribute('aria-current');
  });
  scrollPending = false;
}
window.addEventListener('scroll', () => {
  if (!scrollPending) { scrollPending = true; requestAnimationFrame(updateNav); }
}, {passive:true});
updateNav();
</script></body></html>''')
html = ''.join(parts).replace('max-width: seventy;','')
html = html.replace('Call Inspector: Standard 이상 · 그 외: Premium 이상','Call Inspector API: Standard 이상<br>Data Insights / Monitoring API: Premium 이상')
html = html.replace('Datadog 지원 패키지와 API Key 설정 필요','Datadog 지원 패키지·비용·보존기간 확인 및 API Key 등록 필요')
html = html.replace('각 지표는 매분 계산되는 App ID 수준의 집계값','각 지표는 매분 계산되는 App ID 수준의 집계값이며, 화면 반영까지 1분을 보장하는 것은 아닙니다')
assets = ROOT / 'assets/fonts'
font_data=base64.b64encode((assets/'PretendardVariable.woff2').read_bytes()).decode()
font_css="@font-face{font-family:'Pretendard Variable';font-weight:45 920;font-style:normal;font-display:swap;src:url(data:font/woff2;base64,"+font_data+") format('woff2');}"
theme_css=(ROOT/'src/styles/theme.css').read_text()
license_text=(assets/'OFL.txt').read_text().replace('--','—')
html=html.replace('</head>','<style>'+font_css+theme_css+'</style><!-- Embedded font license\n'+license_text+'\n--></head>')
html=re.sub(r'<b>(\d+)일</b>',r'<b>\1<span class="duration-unit">일</span></b>',html)
