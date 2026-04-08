# 시작하기

## 사전 안내

> 본 문서에서는 Vital Recorder 프로그램을 이용하여 다양한 환자 모니터로부터 데이터를 취득하기 위한 **하드웨어 준비 방법**에 대해 설명합니다.
>
> 본 문서의 내용은 참고용이며 연결 과정의 오류에 대해 Vital Recorder 개발 팀은 어떠한 책임도 지지 않습니다.
>
> 만일 본 문서의 내용과 의료 장비 제조사 매뉴얼이 상이할 경우 제조사 매뉴얼을 따르기 바랍니다.
>
> Vital Recorder 이용 중 의문점에 대해 질문하거나, 개선점을 제안할 때는 vitaldb.org 홈페이지 내의 게시판을 이용하여 주시기 바랍니다.

## 개요

> 한 두 개의 의료 장비를 PC에 연결하여 Vital Recorder를 이용하는 것은 매우 간단히 시작해 볼 수 있습니다.
>
> 장비 연결 및 프로그램 사용이 익숙해 지면 저희팀에서 하고 있는 것처럼 5-6개 장비로부터 동시에 데이터를 모으는 것도 가능합니다.
>
> (아래 그림 참고)
>
> <img src="images/hw_guide_ko/image140.png" width="450" />

## 준비물

### 컴퓨터

> Vital Recorder는 윈도우 운영체제 상에서 작동하므로 윈도우 시스템이 설치된 컴퓨터가 필요합니다.
>
> Vital Recorder는 윈도우 Vista, 7, 8, 10에 대하여 시험되었습니다.
>
> Vital Recorder를 동작시키기 위한 컴퓨터의 최소 사양은 매우 낮습니다.
>
> 안정적인 작동을 테스트해 본 최저 시스템 사양은 인텔 N330 CPU 기반의 넷북(MSI U-100)이었으며
>
> 전체 화면에서 데이터를 실시간 기록할 때 CPU 사용률이 최대 30%까지 상승함을 관찰했습니다.
>
> 임상 진료에 사용되지 않는 별도의 컴퓨터에서 vitalrecorder를 실행시켜야합니다.
>
> 수술장은 공간이 협소하므로 pc보다는 중고 노트북 혹은 근래에 나온 저가 윈도우 태블릿을 추천합니다.
>
> 어느쪽이든 10만원 남짓한 비용으로 구하실 수 있습니다. 대부분의 태블릿은 사양이 비슷하므로 어느 것을 선택해도 상관없지만,
>
> 여러 장비들이 연결되어야 하므로 full size USB 포트가 여러개 있는 시스템이 안정적으로 운영하기에 용이합니다.

### 시리얼 케이블

> 시리얼 케이블에는 다이렉트(direct) 케이블과, 크로스(cross) 케이블 두 종류가 있습니다.
>
> 이는 케이블 내부에서 배선이 교차하는지 여부에 따라 정의되는 것으로 겉보기에는 아무런 차이가 없을 수도 있습니다.
>
> 다이렉트 케이블은 내부 배선이 교차하지 않는 케이블로서, 흔히 시리얼 연장 케이블 이라고도 하며 흔히 양쪽에 각각 9핀 암/수 단자를 갖고 있습니다.
>
> 다양한 길이가 있으니 필요한 길이로 구입하시기 바랍니다. 아래 링크는 “3미터 다이렉트 시리얼 케이블 (M/F)”입니다.
>
> http://cableguy.com/shop/mall.php?cat=025013001&query=view&no=15641
>
> <img src="images/hw_guide_ko/image8.png" width="450" />
>
> 대부분의 의료 장비는 다이렉트 시리얼 케이블로 PC와 통신하지만 일부 의료 장비(Fresenius Vial Orchestra, Edwards사의 장비들)는 크로스 케이블을 이용해야 합니다.
>
> 만일 다이렉트 케이블을 요하는 장치에 크로스 케이블을 연결하면 (혹은 반대의 경우) 장비와 PC간에 전기적 쇼트 상태가 유발되어 장비의 오동작이나 고장을 초래할 수 있으며
>
> 드물게 폭발이나 화재가 발생할 수도 있습니다. 따라서 이 점에 항상 유의해야합니다.
>
> 저희가 추천하는 방식은, 모든 케이블은 다이렉트 케이블로만 구비하고 크로스 연결이 필요한 경우는
>
> 아래 그림과 같은 크로스 젠더(M/F cross gender 혹은 F/F cross gender)를 구매하여 이용하는 것입니다.
>
> 크로스 젠더를 장치에 나사로 고정해 놓으면 빠질 염려도 없고 케이블에 대해 고민할 필요가 없어져 혼란을 줄일 수 있습니다.
>
> <Null modem(M/F cross gender) >
>
> [http://cableguy.com/shop/mall.php?cat=007001001&query=view&no=33688](http://cableguy.com/shop/mall.php?cat=007001001&query=view&no=33688)
>
> <img src="images/hw_guide_ko/image195.png" width="450" />
>
> <Null modem(F/F cross gender)>
>
> [http://cableguy.com/shop/mall.php?cat=007001001&query=view&no=189324](http://cableguy.com/shop/mall.php?cat=007001001&query=view&no=189324)
>
> <img src="images/hw_guide_ko/image190.png" width="450" />

### 장비별 젠더 종류 (정리)

> PC측 단자가 Male이므로 장비쪽은 항상 Female 포트가 되어야 합니다.
>
> 다이렉트 연결을 하는 경우 PC쪽 9핀 시리얼 포트 (DB-9) 연결핀은 2번이 RX, 3번이 TX입니다.
>
> 크로스 연결이 필요한 경우 연결핀은 각각 3, 2번으로 바뀝니다.
>
> 권장드리는 방법은 모든 케이블은 다이렉트 케이블로 준비하고, 필요시에 젠더를 추가로 사용하는 것입니다

<table>
<thead>
<tr>
<th style="text-align: center;"><strong>Device</strong></th>
<th style="text-align: center;"><strong>Device port</strong></th>
<th style="text-align: center;"><p><strong>Gender type</strong></p>
<p><strong>(Male/Female)</strong></p></th>
<th style="text-align: center;"><p><strong>Gender</strong></p>
<p><strong>(Direct/Cross)</strong></p></th>
<th style="text-align: center;"><strong>Vital connect cable</strong></th>
</tr>
<tr>
<th style="text-align: center;">GE solar 8000M</th>
<th style="text-align: center;">Female</th>
<th style="text-align: center;">M / F</th>
<th style="text-align: center;">D</th>
<th style="text-align: center;">M / D</th>
</tr>
<tr>
<th style="text-align: center;">BIS</th>
<th style="text-align: center;">Female</th>
<th style="text-align: center;">M / F</th>
<th style="text-align: center;">D</th>
<th style="text-align: center;">M / D</th>
</tr>
<tr>
<th style="text-align: center;">PLEM</th>
<th style="text-align: center;">Female</th>
<th style="text-align: center;">M / F</th>
<th style="text-align: center;">C</th>
<th style="text-align: center;">M / C</th>
</tr>
<tr>
<th style="text-align: center;"><p>Base Primea</p>
<p>(Orchestra)</p></th>
<th style="text-align: center;">Female</th>
<th style="text-align: center;">M / F</th>
<th style="text-align: center;">C</th>
<th style="text-align: center;">M / C</th>
</tr>
<tr>
<th style="text-align: center;"><p>Vigileo, EV1000A,</p>
<p>Vigilance, Hemosphere</p></th>
<th style="text-align: center;">Female</th>
<th style="text-align: center;">M / F</th>
<th style="text-align: center;">C</th>
<th style="text-align: center;">M / C</th>
</tr>
<tr>
<th style="text-align: center;">EV1000 구형</th>
<th style="text-align: center;">Male</th>
<th style="text-align: center;">F / F</th>
<th style="text-align: center;">C</th>
<th style="text-align: center;"><strong>F / C</strong></th>
</tr>
<tr>
<th style="text-align: center;">INVOS</th>
<th style="text-align: center;">Male</th>
<th style="text-align: center;">F / F</th>
<th style="text-align: center;">C</th>
<th style="text-align: center;"><strong>F / C</strong></th>
</tr>
<tr>
<th style="text-align: center;">MP400-500</th>
<th style="text-align: center;">Male</th>
<th style="text-align: center;">F / F</th>
<th style="text-align: center;">C</th>
<th style="text-align: center;"><strong>F / C</strong></th>
</tr>
<tr>
<th style="text-align: center;">CardioQ</th>
<th style="text-align: center;">Male</th>
<th style="text-align: center;">F / F</th>
<th style="text-align: center;">C</th>
<th style="text-align: center;"><strong>F / C</strong></th>
</tr>
<tr>
<th style="text-align: center;">FMS</th>
<th style="text-align: center;">Male</th>
<th style="text-align: center;">F / F</th>
<th style="text-align: center;">C</th>
<th style="text-align: center;"><strong>F / C</strong></th>
</tr>
<tr>
<th style="text-align: center;">MP20-90</th>
<th style="text-align: center;">Male</th>
<th style="text-align: center;">F / F</th>
<th style="text-align: center;">D</th>
<th style="text-align: center;">-</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### VR connections

<table>
<thead>
<tr>
<th style="text-align: center;"><strong>Device name</strong></th>
<th style="text-align: center;"><strong>Device type</strong></th>
<th style="text-align: center;"><strong>Manufacturer</strong></th>
<th style="text-align: center;"><strong>Device port</strong></th>
<th style="text-align: center;"><strong>Connection 1</strong></th>
<th style="text-align: center;"><strong>Connection 2</strong></th>
<th style="text-align: center;"><strong>Connection 3</strong></th>
<th style="text-align: center;"><strong>PC port</strong></th>
<th style="text-align: center;"><strong>Setting required</strong></th>
<th style="text-align: center;"><strong>Notes</strong></th>
</tr>
<tr>
<th style="text-align: center;">Carescape B450, B650, B850</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE</th>
<th style="text-align: center;">USB</th>
<th style="text-align: center;">ATEN UC-232A USB serial converter</th>
<th style="text-align: center;"><p>Null modem</p>
<p>(F/F cross gender)</p></th>
<th style="text-align: center;">generic USB serial converter</th>
<th style="text-align: center;">USB</th>
<th style="text-align: center;">N</th>
<th style="text-align: center;">시리얼 포트에 연결하면 안됨</th>
</tr>
<tr>
<th style="text-align: center;">Carescape B20, B40</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE</th>
<th style="text-align: center;">Serial (DB9F)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;">N</th>
<th style="text-align: center;">4번 핀 제거</th>
</tr>
<tr>
<th style="text-align: center;">Solar 8000m, 8000i</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE</th>
<th style="text-align: center;">Serial (DB9F)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;">N</th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Tram Rac-4A</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE</th>
<th style="text-align: center;">ANALOG OUT</th>
<th style="text-align: center;"><strong>ADC</strong></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">USB</th>
<th style="text-align: center;">N</th>
<th style="text-align: center;">Fig.2</th>
</tr>
<tr>
<th style="text-align: center;">Dash 2000, 3000, 4000</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE</th>
<th style="text-align: center;">AUX (RJ45)</th>
<th style="text-align: center;"><p><strong>RJ45 to DB9F</strong></p>
<p><strong>custom serial cable</strong></p></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;">N</th>
<th style="text-align: center;">Fig.1</th>
</tr>
<tr>
<th style="text-align: center;">Dash 2500</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE</th>
<th style="text-align: center;"><p>Host Comm</p>
<p>(DB9F)</p></th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;"><strong>Y</strong></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Defib.Sync.</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE</th>
<th style="text-align: center;"><p>Analog</p>
<p>(7pin mini DIN)</p></th>
<th style="text-align: center;"><strong>ADC</strong></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">USB</th>
<th style="text-align: center;">N</th>
<th style="text-align: center;">Fig.3</th>
</tr>
<tr>
<th style="text-align: center;">Intellivue MP, MX</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">Philips</th>
<th style="text-align: center;">MIB (RJ45)</th>
<th style="text-align: center;"><p><strong>RJ45 to DB9F</strong></p>
<p><strong>custom serial cable</strong></p></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;"><strong>Y</strong></th>
<th style="text-align: center;">Fig.4</th>
</tr>
<tr>
<th style="text-align: center;">Intellivue MX 400-550</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">Philips</th>
<th style="text-align: center;">ASIB (RJ45)</th>
<th style="text-align: center;"><p><strong>RJ45 to DB9F</strong></p>
<p><strong>custom serial cable</strong></p></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;"><strong>Y</strong></th>
<th style="text-align: center;">Fig.5</th>
</tr>
<tr>
<th style="text-align: center;">Infinity</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">Drager</th>
<th style="text-align: center;">X3 or X5 (mini-D)</th>
<th style="text-align: center;"><strong>mini-D to DB9F custom serial cable</strong></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;">N</th>
<th style="text-align: center;"><p>Fig.6,</p>
<p>Fig.7</p></th>
</tr>
<tr>
<th style="text-align: center;"><p>Infinity</p>
<p>(analog/sync)</p></th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">Drager</th>
<th style="text-align: center;">X10</th>
<th style="text-align: center;"><strong>ADC</strong></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">USB</th>
<th style="text-align: center;">N</th>
<th style="text-align: center;">Fig.8</th>
</tr>
<tr>
<th style="text-align: center;">MP1300</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">MEKICS</th>
<th style="text-align: center;">WiFi</th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">WiFi</th>
<th style="text-align: center;"><strong>Y</strong></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">BSM</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">Nihon Kohden</th>
<th style="text-align: center;">Serial (DB9F)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;">N</th>
<th style="text-align: center;"></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| **Device name** | **Device type** | **Manufacturer** | **Device port** | **Connection 1** | **Connection 2** | **Connection 3** | **PC port** | **Setting required** | **Notes** |
|----|----|----|----|----|----|----|----|----|----|
| Primus | Anesthesia Machine | Drager | COM1 (DB9F) | Direct serial cable (DB9M-DB9F) |  |  | Serial (DB9M) | **Y** |  |
| Datex-Ohmeda | Anesthesia Machine | GE | Serial (DB15F) | **DB15M to DB9F custom serial cable** |  |  | Serial (DB9M) | N |  |
| Flow-i | Anesthesia Machine | Maquet | Serial (DB9F) | Direct serial cable (DB9M-DB9F) | Null modem (M/F cross gender) |  | Serial (DB9M) | N |  |
| EV-1000 | Hemodynamic monitor | Edwards Lifesciences | Serial (DB9M) | Direct serial cable (DB9M-DB9F) | Null modem (F/F cross gender) |  | Serial (DB9M) | **Y** |  |
| EV-1000 A | Hemodynamic monitor | Edwards Lifesciences | Serial (DB9F) | Direct serial cable (DB9M-DB9F) | Null modem (M/F cross gender) |  | Serial (DB9M) | **Y** |  |
| Vigilance | Hemodynamic monitor | Edwards Lifesciences | COM1 or COM2 (DB9F) | Direct serial cable (DB9M-DB9F) | Null modem (M/F cross gender) |  | Serial (DB9M) | **Y** |  |
| Vigileo | Hemodynamic monitor | Edwards Lifesciences | Serial (DB9F) | Direct serial cable (DB9M-DB9F) | Null modem (M/F cross gender) |  | Serial (DB9M) | **Y** |  |
| HemoSphere | Hemodynamic monitor | Edwards Lifesciences | Serial (DB9F) | Direct serial cable (DB9M-DB9F) | Null modem (M/F cross gender) |  | Serial (DB9M) | **Y** |  |
| Cardio Q | Hemodynamic monitor | Deltex | Serial (DB9M) | Direct serial cable (DB9M-DB9F) | Null modem (F/F cross gender) |  | Serial (DB9M) | **Y** |  |

<table style="width:100%;">
<thead>
<tr>
<th style="text-align: center;"><strong>Device name</strong></th>
<th style="text-align: center;"><strong>Device type</strong></th>
<th style="text-align: center;"><strong>Manufacturer</strong></th>
<th style="text-align: center;"><strong>Device port</strong></th>
<th style="text-align: center;"><strong>Connection 1</strong></th>
<th style="text-align: center;"><strong>Connection 2</strong></th>
<th style="text-align: center;"><strong>Connection 3</strong></th>
<th style="text-align: center;"><strong>PC port</strong></th>
<th style="text-align: center;"><strong>Setting required</strong></th>
<th style="text-align: center;"><strong>Notes</strong></th>
</tr>
<tr>
<th style="text-align: center;">Orchestra</th>
<th style="text-align: center;">Syringe pump</th>
<th style="text-align: center;">Fresenius Kabi</th>
<th style="text-align: center;">RS232-3 (DB9F)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
<th style="text-align: center;">Null modem (M/F cross gender)</th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;"><strong>Y</strong></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Agilia</th>
<th style="text-align: center;">Syringe pump</th>
<th style="text-align: center;">Fresenius Kabi</th>
<th style="text-align: center;">Serial (7pin mini DIN)</th>
<th style="text-align: center;"><strong>전용 케이블</strong></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;">N</th>
<th style="text-align: center;">전용 케이블 구매 필요</th>
</tr>
<tr>
<th style="text-align: center;">SpaceCom</th>
<th style="text-align: center;">Syringe pump</th>
<th style="text-align: center;">BBraun</th>
<th style="text-align: center;">Serial (9pin mini DIN)</th>
<th style="text-align: center;"><strong>전용 케이블</strong></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;"><strong>Y</strong></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Pion TCI</th>
<th style="text-align: center;">Syringe pump</th>
<th style="text-align: center;">Bionet</th>
<th style="text-align: center;">Serial (DB9F)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;">N</th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">BIS</th>
<th style="text-align: center;">Brain monitor</th>
<th style="text-align: center;">Medtronic</th>
<th style="text-align: center;">RS232-3 (DB9F)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;"><strong>Y</strong></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Invos</th>
<th style="text-align: center;"><p>Cerebral/</p>
<p>Somatic oximetry</p></th>
<th style="text-align: center;">Medtronic</th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
<th style="text-align: center;">Null modem (F/F cross gender)</th>
<th style="text-align: center;"><p>generic Serial to USB converter /</p>
<p>DB-9(male) to RJ45 cable</p></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;"><strong>Y</strong></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Radical7</th>
<th style="text-align: center;">Pulse CO-Oximeter</th>
<th style="text-align: center;">Masimo</th>
<th style="text-align: center;">Serial (DB9F)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;"><strong>Y</strong></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">ROOT</th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Masimo</th>
<th style="text-align: center;">USB1 or USB2</th>
<th style="text-align: center;">generic USB serial converter</th>
<th style="text-align: center;">Null modem (F/F cross gender)</th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;"><strong>Y</strong></th>
<th style="text-align: center;"><p>Masimo</p>
<p>USB cable 사용 가능</p></th>
</tr>
<tr>
<th>ANI Monitor V2</th>
<th style="text-align: center;">Analgesia nociception monitor</th>
<th style="text-align: center;">MDMS</th>
<th style="text-align: center;">Serial (DB9F)</th>
<th style="text-align: center;">generic USB serial converter</th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;">N</th>
<th style="text-align: center;"></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Serial to USB 컨버터

> 노트북이나 태블릿 PC 처럼 시리얼 포트가 없는 컴퓨터에서는 Serial to USB 케이블을 이용하여 연결합니다.
>
> Serial to USB 컨버터는 시리얼 포트 생성과 다이렉트 케이블 역할을 동시에 하는 장치입니다.
>
> 따라서 크로스 연결이 필요한 장치는 시리얼 젠더와 함께 이용해야합니다.
>
> 멀티 포트 Serial to USB 컨버터도 나와있으며 테스트해 본 장비로 추천드리는 것은 Netmate 4 port serial to USB converter (강원전자)입니다.
>
> 이 장치를 연결하게 되면 컴퓨터의 장치관리자에 4개의 COM 포트가 생기는 것을 볼 수 있습니다.
>
> 따라서 한개의 USB 포트만을 차지하면서 4개의 시리얼 장비로부터 동시에 데이터 취득이 가능해집니다.
>
> http://cableguy.com/shop/mall.php?cat=005004003&query=view&no=39206
>
> <img src="images/hw_guide_ko/image89.png" width="450" />

### USB 허브

> USB 포트가 한개 밖에 없거나 부족한 경우에는 USB 허브를 이용할 수도 있습니다.
>
> USB 허브는 가급적 전원 공급이 따로 되는 것(‘유전원’이라 표기돼 있습니다)이 좋습니다.
>
> 저희가 사용하는 제품은 ORICO 4포트 제품입니다.
>
> [http://www.enuri.com/detail.jsp?modelno=10534644&cate=&IsDeliverySum=N](http://www.enuri.com/detail.jsp?modelno=10534644&cate=&IsDeliverySum=N)
>
> <img src="images/hw_guide_ko/image185.png" width="450" />

### USB 연장선

> 컴퓨터와 장비들 사이의 거리가 먼 경우에 USB 연장선이 필요한 경우가 있습니다.
>
> 10미터 정도 이내에서는 신호가 줄어들 걱정이 전혀 없으므로 저렴한 제품을 필요한 길이로 구매하시면 됩니다. 저희는 아래의 제품을 사용합니다.

[http://cableguy.com/shop/mall.php?cat=025011002&query=view&no=541](http://cableguy.com/shop/mall.php?cat=025011002&query=view&no=541)

> <img src="images/hw_guide_ko/image58.png" width="450" />

### 요약

> 이상을 정리하면 기본 준비물을 마련하기 위한 총비용은 아래와 같습니다. (동시에 4가지 장비와 통신하며 데이터를 취득하기 위한 구성)

<table style="width:100%;">
<thead>
<tr>
<th style="text-align: center;"><strong>이름</strong></th>
<th style="text-align: center;"><strong>구매 링크</strong></th>
<th style="text-align: center;"><strong>단가(원)</strong></th>
<th style="text-align: center;"><strong>수량(개)</strong></th>
<th style="text-align: center;"><strong>총액(원)</strong></th>
<th style="text-align: center;"><strong>비고</strong></th>
</tr>
<tr>
<th style="text-align: center;"><p>Null modem</p>
<p>(M/F cross gender)</p></th>
<th style="text-align: center;">http://cableguy.com/shop/mall.php?cat=007001001&amp;query=view&amp;no=33688</th>
<th style="text-align: center;"></th>
<th style="text-align: center;">6</th>
<th style="text-align: center;">11,724</th>
<th style="text-align: center;">넉넉히 사두는 것을 권함</th>
</tr>
<tr>
<th style="text-align: center;"><p>direct serial cable</p>
<p>(M/F, 3m)</p></th>
<th style="text-align: center;">http://cableguy.com/shop/mall.php?cat=025013001&amp;query=view&amp;no=15641</th>
<th style="text-align: center;">1,954</th>
<th style="text-align: center;">4</th>
<th style="text-align: center;">7,816</th>
<th style="text-align: center;">필요한 길이로 구매</th>
</tr>
<tr>
<th style="text-align: center;">serial to USB 컨버터</th>
<th style="text-align: center;">http://cableguy.com/shop/mall.php?cat=005004003&amp;query=view&amp;no=39206</th>
<th style="text-align: center;">50,500</th>
<th style="text-align: center;">1</th>
<th style="text-align: center;">50,500</th>
<th style="text-align: center;">4포트 추천</th>
</tr>
<tr>
<th style="text-align: center;">USB 허브</th>
<th style="text-align: center;"><a href="http://www.enuri.com/detail.jsp?modelno=10534644&amp;cate=&amp;IsDeliverySum=N">http://www.enuri.com/detail.jsp?modelno=10534644&amp;cate=&amp;IsDeliverySum=N</a></th>
<th style="text-align: center;">30,000</th>
<th style="text-align: center;">1</th>
<th style="text-align: center;">30,000</th>
<th style="text-align: center;">유전원 허브 추천</th>
</tr>
<tr>
<th style="text-align: center;">USB 연장선 (M/F, 5m)</th>
<th style="text-align: center;">http://cableguy.com/shop/mall.php?cat=025011002&amp;query=view&amp;no=541</th>
<th style="text-align: center;">2,000</th>
<th style="text-align: center;">1</th>
<th style="text-align: center;">2,000</th>
<th style="text-align: center;">필요한 길이로 구매</th>
</tr>
<tr>
<th colspan="5" style="text-align: right;">총액 102,040</th>
<th>　</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 환자 모니터와의 연결

> 이제 본격적으로 의료 장비와 PC를 연결해보도록 합시다.
>
> 장비에 따라 어떤 의료 장비의 경우에는 케이블만 꽂으면 즉시 데이터를 받을 수 있지만
>
> 어떤 의료 장비는 암호 입력 후 관리자 모드로 들어가 설정 변경을 해야하는 경우도 있습니다.
>
> 다행히도 연결 설정은 한 번 해놓으면 이후에 다시 손 댈 필요가 없습니다.
>
> 안전을 위해 반드시 장비가 환자 혹은 피험자와 연결되기 전에 모든 장비를 미리 셋업하시기 바랍니다.
>
> 또 앞서 말씀 드린 바 대로 몇몇 장비(Fresenius Vial Orchestra, Edwards lifesciences사의 장비)는 일반 시리얼 케이블이 아니라 크로스 케이블로 연결을 해야 합니다.
>
> 그러한 경우는 해당 장비 설명 시 다시 언급해 드리겠습니다.

## GE CARESCAPE B850, B650, B450

> 이 프로토콜은 GE S5 computer Interface 라고 하며 이를 통해 GE B850/650/450 등 모니터와 B40/20, Datex-Ohmeda S/5 monitor에서 사용합니다.
>
> GE의 오래된 데이터 수집 프로그램인 S5 Collect 라고 하는 프로그램이 있었는데 이 프로그램에서 사용하는 통신 프로토콜입니다.
>
> CARESCAPE B850, B650, B450 는 3.1 버전 이상에서 연결이 가능하며 Startech ICUSB232V2 USB to RS232 converter가 있어야 합니다.
>
> ([https://www.amazon.ca/dp/B00GRP8EZU/ref=redir_mobile_desktop/146-2308166-9887501?\_encoding=UTF8&ref\_=ya_aw_od_pi&th=1](https://www.amazon.ca/dp/B00GRP8EZU/ref=redir_mobile_desktop/146-2308166-9887501?_encoding=UTF8&ref_=ya_aw_od_pi&th=1))
>
> Bx50 v2 라면 ATEN UC232A 구형 케이블(시리얼 넘버가 Z3L1이거나 더 빠른 알파벳으로 시작)만 가능하나 현재 단종되어 케이블을 구할 수 없습니다.
>
> 모니터 버전은 Monitor setup > defaults&service > service 에서 확인할 수 있습니다.
>
> 이 변환 케이블을 장비 뒷면의 USB 포트에 꽂습니다. 모니터 뒷면의 4개의 USB 포트 중 어떤 포트에 꽂아도 상관없습니다.
>
> <img src="images/hw_guide_ko/image4.png" width="450" />
>
> 그런 다음 PC의 시리얼 포트 (혹은 일반적인 USB serial converter)와 “Null modem(F/F cross gender)”를 통해 연결합니다.
>
> VRZero를 사용한다면 VRzero에 연결되는 쪽의 usb케이블은 핸드쉐이킹이 되는 제품을 사용해야 합니다.
>
> [강원전자] NETmate USB 2.0 to RS232 변환케이블, 0.45M [KW-525]
>
> http://www.compuzone.co.kr/product/product_detail.htm?ProductNo=374732&BigDivNo=&MediumDivNo=1139&DivNo=2659
>
> [ATEN] 에이텐 USB 1.1 to RS232 변환케이블, 0.35M [UC232A]
>
> http://www.compuzone.co.kr/product/product_detail.htm?ProductNo=60189&BigDivNo=&MediumDivNo=1139&DivNo=2659

## GE S/5 AM

> GE S/5 AM monitor의 경우 아래 그림과 같이 X8번 포트에 연결합니다. (“Null modem(F/F cross gender)” 필요)
>
> <img src="images/hw_guide_ko/image139.png" width="450" />

## GE B40, B20

> B40/B20 모니터의 경우 아래와 같은 9핀 시리얼 포트에 연결합니다.
>
> 4번핀이 제거된 9핀 케이블을 사용해야합니다.
>
> <img src="images/hw_guide_ko/image42.png" width="450" />

##

## GE B105M, B125M, B155M

<img src="images/hw_guide_ko/image90.png" width="450" />

> 장비 후면의 빨간색으로 표시된 시리얼 포트에 다이렉트 시리얼 케이블을 연결합니다.\
> Vital Recorder 에서 장비 추가시에는 GE: Bx50을 선택합니다.

## GE Solar 8000m, 8000i

> 가장 간단합니다. 장비 후면 우측의 “RS-232 1”이라고 쓰여 있는 포트에 다이렉트 시리얼 케이블을 연결하면 됩니다. 다른 특별한 설정은 필요 없습니다.
>
> <img src="images/hw_guide_ko/image135.png" width="450" />
>
> Vital Recorder 에서 장비 추가시에는 GE::Solar 8000m을 선택하세요.
>
> 참고 : 이 프로토콜은 GE Unity 프로토콜이라고 합니다. GE Solar 8000m, Solar 8000i, Dash 3000, 4000, 5000 이 이 프로토콜을 이용합니다.

## GE Dash 2000/3000/4000

> 뒷면의 AUX 단자에 있는 RJ45 커넥터를 통하여 Serial 통신을 합니다.
>
> 따라서 한쪽은 시리얼 케이블이면서 반대편은 랜선처럼 생긴 전용 케이블이 필요합니다.
>
> <img src="images/hw_guide_ko/image103.png" width="450" />
>
> USB 시리얼 컨버터와 랜선을 이용하여 케이블을 직접 제작해도 되지만
>
> 인터넷을 통해 케이블 제작 업체에 의뢰하는 것도 방법입니다. 의뢰 시에는 아래 배선으로 제작을 요청하면 됩니다.
>
> <img src="images/hw_guide_ko/image60.png" width="450" /> Fig. 1
>
> Vital Recorder 에서 장비 추가시에는 GE::Dash x000 을 선택하세요.
>
> 참고 : 이 프로토콜은 GE Unity 프로토콜이라고 합니다. GE Solar 8000m, Solar 8000i, Dash 3000, 4000, 5000 이 이 프로토콜을 이용합니다.

## GE Dash 2500

> 마찬가지로 다이렉트 시리얼 케이블을 이용합니다. 뒷면의 Host Comm Port 단자 그대로 꽂으면 됩니다.
>
> <img src="images/hw_guide_ko/image20.png" width="450" />
>
> 만일 통신이 되지 않는다면 모니터에서 다음과 같이 설정 합니다.

- Trim Knob 를 돌려 Main Menu 를 연다

- other system setting 선택

- go to config mode 선택 후 yes 선택

- 2508 입력 후 done 선택

- 장치가 재부팅 됨

- Trim Knob 를 돌려 Configuration Menu 선택

- other system settings 선택

- Config HostComm 선택

- Remote access 를 선택한 후 Serial 2 선택

- Serial 2 setup 선택 후 ASCII cmd, 9600 baud 선택 (기본값)

- go to previous menu 선택

- save default changes 선택

- exit config mode 선택 후 yes 선택

- 장치가 재부팅 됨

> Vital Recorder 에서 장비를 추가할 때는 GE::Dash 2500 를 선택하세요.
>
> 참고: 이 프로토콜은 GE Dinamap 프로토콜이라 하며 Dash 2500 에서만 사용합니다.

## GE TRAM RAC 4A

> 심전도, 동맥압 등 파형 데이터는 GE 모니터의 Tram-RAC 4A (여러 개의 모듈을 삽입하는 장치) 뒤에 있는 15핀 ANALOG OUT 단자를 통해서만 받을 수 있습니다.
>
> <img src="images/hw_guide_ko/image71.png" width="450" />
>
> 이 포트는 디지털 통신을 위한 포트가 아니라 측정된 동맥압, 심전도 파형 등을 전압으로 변환되어 출력하는 아날로그 포트입니다.
>
> 아날로그 포트의 전압값은 PC에서 바로 읽을 수가 없기 때문에 이를 디지털로 변환해 주는 아날로그 디지털 컨버터 (Analog-Digital Converter, ADC) 라는 장비가 필요합니다.
>
> ADC는 종류가 다양하여 $50 이내의 저가 제품부터 수천 달러짜리까지 있습니다.
>
> 현재 테스트된 장비는 DataQ사의 DI-149, DI-155가 있습니다.
>
> 두 제품의 가장 큰 차이는 전압 해상도 차이로 일반적 모니터링 목적이라면 저렴한 DI-149로 충분합니다만 심전도상 T-wave나 P-wave 등의 분석을 위해서는 DI-155를 추천합니다.
>
> [http://www.dataq.com/products](http://www.dataq.com/products/di-149/)
>
> ADC를 구입한 후에는 GE TRAM RAC의 ANALOG OUT 포트의 각 핀에 출력되는 전압을 ADC의 입력으로 넣기 위한 케이블을 제작해야합니다.
>
> 이 케이블 또한 직접 만들 수 도 있지만 케이블 제작 업체에 맡길 수 도 있습니다. 주문 시에는 아래와 같이 핀이 연결되도록 제작 요청합니다.
>
> <img src="images/hw_guide_ko/image187.png" width="450" />
>
> Fig. 2
>
> <img src="images/hw_guide_ko/image136.png" width="450" />
>
> [http://www.cableguy.com/](http://www.cableguy.com/) 에서 주문 제작한 케이블을 DI-149에 연결한 모습입니다.
>
> 상기 방법대로 DataQ 사의 DI-149를 이용할 경우 통관, 배송에 따른 추가 비용과 아날로그 채널에 맞게 연결해 주는 15핀 어댑터를 추가로 주문해야해서
>
> 최종적으로 대당 10-20만원 정도가 들게 됩니다.
>
> DI-1110 등의 최신 DataQ 사의 아날로그 디지털 컨버터는 두가지 모드로 동작할 수 있습니다.
>
> (libusb 모드와 CDC 모드) 이 중, CDC 모드로 동작할 때만 Vital Recorder 에서 인식이 가능하므로
>
> 이들 장비의 이용을 위해서는 아래의 제조사 매뉴얼에 따라 장비의 모드를 변경해 주시기 바랍니다.
>
> [https://www.dataq.com/blog/data-acquisition/usb-daq-products-support-libusb-cdc](https://www.dataq.com/blog/data-acquisition/usb-daq-products-support-libusb-cdc)
>
> 참고로 이러한 비용 문제를 해결하고 누구나 값싸게 데이터 취득을 가능하게 하고자 저희는 SNU-ADC라는 이름의 장비를 자체적으로 설계, 제작 했습니다.
>
> SNU-ADC는 8채널 ADC 기능을 갖고 있을 뿐만아니라 이벤트 마커를 넣기 위해 유무선 푸쉬 버튼을 연결할 수 있습니다.
>
> <img src="images/hw_guide_ko/image155.png" width="450" />
>
> 주의할 점은 어떤 ADC를 이용하든 TRAM RAC에서 PLETH 파형을 받으려면 왼쪽에서 두번째 BP 커넥터(BP2)의 케이블 자체를 빼놓아야 한다는 점입니다.
>
> BP2에 예를 들어 CVP나 두번째 동맥압을 측정하는 Transducer 케이블이 꽂혀있으면 PLETH가 아니라 BP2가 기록됩니다.
>
> PLETH와 BP는 웨이브가 비슷하므로 알아차리기도 힘듭니다.
>
> 아래 그림이 이러한 잘못된 연결을 보여주는 예입니다.
>
> PLETH 채널에 CVP가 기록되고 CVP가 제대로 넘어오지 않습니다.

****
<img src="images/hw_guide_ko/image61.png" width="450" />

| **잘못된 연결** | **올바른 연결** |
|----|----|
| <img src="images/hw_guide_ko/image207.png" width="450" /> | <img src="images/hw_guide_ko/image25.png" width="450" /> |
| CVP Transducer 케이블이 왼쪽에서부터 두번째 BP 커넥터(BP2)에 연결 → 잘못된 연결 | CVP Transducer 케이블이 왼쪽에서부터 세번째 BP 커넥터(BP3)에 연결 → 올바른 연결 |

<img src="images/hw_guide_ko/image166.png" width="450" />

또한, ICP를 모니터링할 경우 반드시 ICP를 TRAM RAC에서 첫 번째 슬롯에 꽂아야 합니다.

## GE Defib connectors

> 아날로그 포트가 다른 목적으로 이용되고 있을 경우 전면부의 Defib.Sync 커넥터로부터 ECG, ABP를 전압 형태로 받을 수 있습니다.
>
> 핀 번호는 아래과 같으며 전압은 TramRac 아날로그 포트와 같습니다.
>
> 7핀 딘(DIN) 케이블을 구입하여 (혹은 8핀 딘케이블도 호환이 가능합니다) 중간을 잘라 사용합니다.
>
> <img src="images/hw_guide_ko/image114.png" width="450" />

## <img src="images/hw_guide_ko/image137.png" width="450" />

Fig. 3

##

## Philips Intellivue MP/MX series

> 필립스 Intellivue 환자 모니터는 모니터 후면에 위치한, 흡사 LAN 포트처럼 보이는 MIB 포트를 통해 시리얼 통신을 할 수 있습니다.
>
> 센트럴 모니터에 연결된 상태이든 아니든 상관 없이 데이터 취득에 사용할 수 있습니다.
>
> <img src="images/hw_guide_ko/image209.png" width="450" />
>
> MIB 포트는 아래와 같이 여러 종류가 있습니다. 기종에 따라 표시가 다르므로 주의하시기 바랍니다.
>
> <img src="images/hw_guide_ko/image192.png" width="450" />
>
> MIB 포트를 통한 연결을 위해서는 RJ-45 단자의 4,5,7번과 DB-9 female 단자의 5,2,3번이 각각 연결된 Female 시리얼 케이블을 준비해야 합니다.
>
> RJ-45 단자는 모니터의 MIB 포트와 연결되고 DB-9 female 단자는 USB to Serial Converter를 거쳐 PC와 연결됩니다.
>
> <img src="images/hw_guide_ko/image1.png" width="450" />

Fig. 4

> 만일 MX400-550 시리즈의 경우엔 Advanced Interface Card 를 통해서도 통신이 가능합니다.
>
> (MX600-800 시리즈는 반드시 MIB 보드가 있어야 합니다).
>
> 이 경우 상기 Rx, Tx 핀의 연결이 다르므로 주의하시기 바랍니다. (DB-9의 2,3번 연결이 반대입니다).
>
> <img src="images/hw_guide_ko/image33.png" width="450" />

Fig. 5

> 물리적 연결이 되었다면 다음으로 환자 모니터의 설정을 변경해야 합니다.
>
> <img src="images/hw_guide_ko/image148.png" width="450" /><img src="images/hw_guide_ko/image141.png" width="450" />
>
> 모니터의 “Main Setup” 버튼을 누르고
>
> “Operation Modes” 를 선택합니다. 그런 다음 “Service”를 누릅니다.
>
> <img src="images/hw_guide_ko/image57.png" width="450" />
>
> 서비스 모드 진입을 위해서는 암호를 입력해야합니다.
>
> 기본 암호는 “1345” 입니다. 다를 경우 제조사에 문의하세요.
>
> <img src="images/hw_guide_ko/image122.png" width="450" /><img src="images/hw_guide_ko/image31.png" width="450" />
>
> 그런 다음 “Main Setup” 으로 다시 들어가면 맨 아래에 “Hardware” 라는 메뉴가 생겨있습니다.
>
> 이것을 누르고 들어간 다음 “Data Export 1”과 “Data Export 2”에 통신 속도를 “Fix 115200” 으로 설정합니다.
>
> <img src="images/hw_guide_ko/image130.png" width="450" />
>
> “Interfaces” 로 들어갑니다.
>
> <img src="images/hw_guide_ko/image212.png" width="450" />
>
> 01a 포트의 Driver 가 “DtOut1” 인지 확인합니다.
>
> 이것이 다른 것(예를 들어 GM, AGM) 이라면 화면 아래에서 “Change Driver” 버튼을 클릭한 후 “DtOut1” 으로 바꿉니다.
>
> DtOut 뒤의 숫자는 할당된 포트에 따라 달라질 수 있습니다.
>
> 변경 사항은 모니터를 껐다 켜야 적용 됩니다.
>
> 주) MP2와 X2 모니터의 경우에는 시리얼 통신이 안 되므로 데이터 취득이 불가능합니다.
>
> 마지막으로 ETCO2 wave를 받기 위해서는 아래와 같은 설정이 필요합니다.
>
> <img src="images/hw_guide_ko/image80.png" width="450" />
>
> “Main setup” - “Operating Modes” - “Config” 를 누릅니다.
>
> Password는 “71034”입니다.
>
> <img src="images/hw_guide_ko/image85.png" width="450" />
>
> 마취기와 연결되어 있는 IntelliBridge EC10 모듈에 setup 버튼을 누릅니다.
>
> <img src="images/hw_guide_ko/image77.png" width="450" />
>
> 모니터 하단에 “Setup Device” 로 들어갑니다.
>
> <img src="images/hw_guide_ko/image191.png" width="450" /><img src="images/hw_guide_ko/image67.png" width="450" />
>
> “Setup Anesth. Machine” -” Device Driver” - “Setup Waves” 를 차례로 누릅니다.\
> Add 버튼으로 원하는 웨이브를 추가할 수 있습니다. “CO2”, “AWP”를 선택합니다.
>
> (잘못된 웨이브가 나올 경우에 모두 Delete 한 후에 Add버튼을 눌러 재설정 합니다.)
>
> <img src="images/hw_guide_ko/image193.png" width="450" />
>
> “Select to change operating mode” -”monitoring” 을 차례로 선택합니다.
>
> <img src="images/hw_guide_ko/image111.png" width="450" />
>
> “Confirm”을 버튼을 누르면 설정 변경이 적용 됩니다.

## Drager Infinity Kappa

> <img src="images/hw_guide_ko/image40.png" width="450" />
>
> 이 계열 모니터는 모듈, 모니터, 혹은 docking station 의 X5 혹은 X3의 Mini-D 케이블을 통해 통신합니다.
>
> 케이블은 아래와 같이 제작하여도 되고 회사를 통해 주문해도 됩니다.
>
> (drager 파트 번호 5206441 export protocol cable)
>
> <img src="images/hw_guide_ko/image56.png" width="450" />
>
> Fig. 6 , Fig. 7
>
> Vital Recorder 에서는 Infinity 모니터를 선택하여 통신이 가능하며 대부분의 numeric data를 2초 간격으로 추출할 수 있으나 waveform 데이터의 추출은 불가능합니다.
>
> Waveform 데이터를 추출하기 위해서는 X10 Analog/Sync 포트에 연결해야합니다.
>
> 12-13번 및 6-7번 핀을 이용합니다. (drager 부품 번호 4314618)
>
> <img src="images/hw_guide_ko/image24.png" width="450" />
>
> 12: CH1 (+)
>
> 13: CH1 (-)
>
> 7: CH2 (+)
>
> 6: CH2 (-)
>
> Fig. 8

## Drager Infinity C500/C700

> Infinity C500/ C700 장비는 추가설정이 필요하지 않습니다.
>
> <img src="images/hw_guide_ko/image70.png" width="450" />
>
> <img src="images/hw_guide_ko/image29.png" width="450" />
>
> P2500의 RJ10 포트에서 numeric data를 추출할 수 있습니다.
>
> RJ10 단자의 3,2,4번과 DB-9 female 단자의 2,3,5번이 각각 연결된 serial cable을 준비해야 합니다. <img src="images/hw_guide_ko/image5.png" width="450" />

RJ10 단자는 P2500의 RJ10 포트와 연결되고 DB-9 female 단자는 USB to Serial Converter를 거쳐 PC와 연결됩니다.

<img src="images/hw_guide_ko/image41.png" width="450" /><img src="images/hw_guide_ko/image170.png" width="450" />

Waveform 데이터를 추출하기 위해서는 Analog sync cable이 필요합니다.

Analog/Sync cable은 Infinity Mcable -Microstream CO2 와 함께 사용할 경우 Y cable을 통해 M540모니터에 연결합니다.

Analog/Sync cable의 MDR 포트와 ADC를 연결하기 위해 MDR14 to RJ45케이블이 필요합니다.

> 케이블은 아래와 같이 제작하여도 되고 회사를 통해 주문해도 됩니다.

MDR 14 핀 번호는 아래 사진과 같습니다. 커넥터는 따로 구매해야 합니다..

(커넥터 구매 링크 : [http://www.cableguy.com/shop/mall.php?cat=007002007&query=view&no=210644](http://www.cableguy.com/shop/mall.php?cat=007002007&query=view&no=210644))

<img src="images/hw_guide_ko/image125.png" width="450" />

(제작된 케이블 구매 링크 : http://www.cableguy.com/shop/mall.php?cat=025015011&query=view&no=209983)

|     |
|-----|

## MEKICS MP1300

> MEKICS 기기와 VR과 무선 연결을 위해서 우선 무선 공유기 설정이 필요합니다.
>
> 본 매뉴얼에서는 iptime 무선 공유기를 이용하여 설정하는 방법을 안내해 드리겠습니다.
>
> (다른 공유기도 크게 다르지 않습니다)

- **무선 공유기 설정**

> <img src="images/hw_guide_ko/image198.png" width="450" />
>
> 공유기에 전원을 연결하고 PC에서 무선랜 목록을 열어 iptime-mini 라는 이름의 AP에 연결합니다.
>
> <img src="images/hw_guide_ko/image105.png" width="450" />
>
> 웹브라우저를 열고 주소창에 192.168.0.1 을 입력하여 공유기 설정 화면으로 들어갑니다.
>
> Login ID와 Password 초기값은 admin 입니다.
>
> <img src="images/hw_guide_ko/image102.png" width="450" />
>
> Setup을 누릅니다.
>
> <img src="images/hw_guide_ko/image101.png" width="450" />
>
> 고급설정 - 무선랜 관리- 무선설정/ 보안 메뉴로 들어갑니다. 위 그림과 같이 네트워크 이름과 암호를 설정합니다.
>
> 암호화 옵션은 ‘WPA2PSK+AES(권장)’을 선택합니다. 네트워크 이름 알림 옵션은 해제 후 적용 버튼을 누릅니다.
>
> 저장을 하면 공유기의 SSID가 iptime_mini에서 mekics_r7으로 변경 되었기 때문에 자동으로 공유기 접속이 단절됩니다.
>
> <img src="images/hw_guide_ko/image99.png" width="450" />
>
> 네트워크 이름 알림 옵션을 해제 했기 때문에 해당 네트워크로 연결할 때 숨겨진 네트워크- 이전 설정한 SSID와 Password를 입력하여 접속합니다.
>
> 웹브라우저를 열고 주소창에 192.168.0.1 을 입력하여 공유기 설정 화면으로 들어갑니다.
>
> <img src="images/hw_guide_ko/image147.png" width="450" />
>
> 만일 공유기를 상위망 (인터넷, 혹은 원내망)에 연결시킬 계획이라면 이 단계를 수행합니다. 아니라면 건너뛰어도 됩니다.
>
> 고급설정 - 무선랜 관리- 무선확장설정 메뉴로 들어갑니다.
>
> 무선 확장 방식은 무선 WAN으로 설정하고 SSID와 Password를 입력합니다.
>
> 여기서 설정할 네트워크 이름과 암호는 MEKICS기기에 연결할 VR의 hotspot ssid와 Password를 입력하면 됩니다.
>
> <img src="images/hw_guide_ko/image63.png" width="450" />
>
> 고급설정 - 시스템 관리- 기타 설정 메뉴로 들어갑니다.
>
> 유선 포트 기능 설정에서 LAN포트를 누른 후 오른쪽 아래 적용 버튼을 누릅니다.

- **MP1300 설정**

> <img src="images/hw_guide_ko/image3.png" width="450" />
>
> 설정이 완료된 공유기를 MP1300 기기와 연결합니다.
>
> 기기 뒷편 usb 포트에 공유기 전원과 연결하고 랜선을 연결합니다.
>
> <img src="images/hw_guide_ko/image186.png" width="450" />
>
> System- Network 를 선택하면 위 그림과 같은 설정 화면이 나옵니다. IP와 gateway 주소를 설정합니다.
>
> 이 때 앞 세번째 까지 IP 주소는 공유기 IP 주소와 동일해야 하며 (상기 예에서 192.168.0 까지 동일) 마지막 자리만 다른 기기가 사용하지 않는 2~255사이의 임의의 숫자로 기기 고유의 값을 가져야 합니다.
>
> IP : 192.168.0.***
>
> gateway: 192.168.0.1(공유기 주소)
>
> <img src="images/hw_guide_ko/image87.png" width="450" />
>
> System-Network-Central-Mode 메뉴로 들어갑니다. MP601 을 선택합니다.
>
> <img src="images/hw_guide_ko/image78.png" width="450" />
>
> Central 설정화면에서 Server IP : 192.168.137.1 , port:6002 로 설정합니다.
>
> 변경 사항은 모니터 전원을 껐다 켜야 적용 됩니다.
>
> <img src="images/hw_guide_ko/image79.png" width="450" />
>
> WinVR 에 MP1300을 추가하기 위해서는 “Add Device” -” MEKICS” 클릭 후 port 를 6002로 설정 합니다.

## Nihon Kohden BSM

> (Vital Recorder 1.8.16.2 이상 버전에서 사용 가능합니다.)
>
> <img src="images/hw_guide_ko/image14.png" width="450" />
>
> BSM 모니터에서 데이터를 얻기 위해서는 QI-373P 보드가 설치되어 있어야 합니다. 이 보드는 RS-232C 시리얼 포트와 ECG/BP OUT 포트를 내장하고 있습니다. Numeric data를 얻기 위해서는 빨간색으로 표시된 시리얼 포트에 “Null modem(M/F cross gender)”를 연결 후 다이렉트 시리얼 케이블을 연결합니다.
>
> ECG와 ART 파형 데이터는 ECG/BP output 포트를 통해서 취득할 수 있습니다.
>
> <img src="images/hw_guide_ko/image115.png" width="450" />
>
> ECG/BP OUT 포트를 통해 데이터를 취득하기 위해서는 니혼코덴사의 ECG/BP output cable이 필요합니다.
>
> <img src="images/hw_guide_ko/image176.png" width="450" />
>
> ECG/BP output cable의 아날로그 신호를 ADC(Analog to Digital Converter)의 입력으로 넣기 위해서는 5.5pi Mono to RJ45 케이블을 제작해야 합니다.\
> 핀 번호는 위 사진과 같습니다.
>
> <img src="images/hw_guide_ko/image84.png" width="450" />
>
> 5.5pi Mono to RJ45 cable을 ADC에 연결한 후 USB케이블을 통해 PC에 연결하면 ECG/ART 파형 데이터를 추출할 수 있습니다.\
> 위 사진에서는 SNUADCM을 사용했습니다.

# 마취기와의 연결

## Drager Anesthesia Machine

> Apollo/Cicero EM color/Julian/Primus/Vamos는 추가 설정이 필요하지 않습니다.
>
> <img src="images/hw_guide_ko/image133.png" width="450" />
>
> Drager 후면의 COM1 포트에 다이렉트 시리얼 케이블로 연결합니다.

###

### Drager Fabius

> Fabius GS/Fabius Tiro/Infinity Evita V500/Zeus는 **크로스 젠더(널 모뎀)**을 중간에 끼우고 연결 합니다.
>
> 또한 Fabius의 경우 아래 그림의 빨간색 원으로 표시된 3개 버튼을 동시에 누르면 서비스 모드로 들어가 시리얼 설정을 변경해야합니다.
>
> <img src="images/hw_guide_ko/image95.png" width="450" />
>
> <img src="images/hw_guide_ko/image93.png" width="450" />

###

### COM1 포트가 이미 점유되어있을 때

> 만일 Drager COM1 포트가 마취기로부터 환자 모니터로의 CO2 curve, airway pressure curve 등의 정보 전송을 위해 이미 사용되고 있다면,
>
> 다음과 같은 데이터 훔쳐보기용 Y 케이블을 제작하여 사용해야 기존의 데이터 통신을 방해하지 않고 정보를 추출할 수 있습니다.
>
> <img src="images/hw_guide_ko/image50.png" width="450" />
>
> Atlan 마취기의 경우는 위 케이블의 마취기쪽과 CON1 쪽에 각각 단자 모양에 맞는 cross gender를 부착해야 합니다.
>
> 데이터를 읽는 CON2는 그대로 이용합니다.
>
> Drager DB9F —-- F/F Cross gender — DB9M —---------- CON1 (DB9F) —--- M/F Cross gender

### Drager Perseus

Perseus는 “Null modem(F/F cross gender)”를 연결 후 다이렉트 시리얼 케이블을 연결합니다.

<img src="images/hw_guide_ko/image98.png" width="450" />

> 시스템 설정 > 시스템 메뉴를 눌러 서비스 모드로 진입합니다.
>
> 암호는 0000 입니다.
>
> <img src="images/hw_guide_ko/image34.png" width="450" />
>
> 인터페이스 구성 메뉴를 누릅니다.
>
> <img src="images/hw_guide_ko/image178.png" width="450" />
>
> COM1과 COM2 중 연결된 포트에 프로토콜은 MEDIBUS, 보 레이트를 9600으로 설정합니다.
>
> <img src="images/hw_guide_ko/image142.png" width="450" />

## GE Datex-Ohmeda Anesthesia Machine

> Datex-Ohmeda 마취기는 뒷면의 커버를 열면 나오는 15핀 커넥터(Female)를 이용하여 연결합니다.
>
> 15핀 커넥터는 일반적인 시리얼 통신에 사용되는 9핀 커넥터와 높이는 같지만 더 길게 생겼습니다.
>
> <img src="images/hw_guide_ko/image188.png" width="450" />
>
> 우리가 흔히 사용하는 Serial To USB 커넥터는 9핀(Male)이기 때문에 이를 15핀(Male)로 변경하는 케이블을 제작하여야 합니다.
>
> <img src="images/hw_guide_ko/image131.png" width="450" />
>
> 만일 Datex-Ohmeda 마취기의 15핀 포트가 마취기로부터 환자 모니터로의 CO2 curve, airway pressure curve 등의 정보 전송을 위해 이미 사용되고 있다면,
>
> 다음과 같은 데이터 훔쳐보기용 Y 케이블을 제작하여 사용해야 기존의 데이터 통신을 방해하지 않고 정보를 추출할 수 있습니다.
>
> 이 때, Vital Recorder에서 장치 추가 시 “읽기 전용(Read only) 모드” 옵션을 선택하여야 합니다.
>
> <img src="images/hw_guide_ko/image18.png" width="450" />
>
> 참고 : 이 프로토콜을 GE Ohmeda Serial 프로토콜이라고 하며 Aespire, Aespire View, Aestiva, Avance, Avance CS2, Aisys, Aisys CS2, Carestation 620/650/650c 등에서 사용합니다.

## Maquet Flow-i

> Flow-i는 장비에서 추가 설정이 필요하지 않습니다.

#

> <img src="images/hw_guide_ko/image129.png" width="450" />
>
> Flow-i 마취기는 기기 뒷면 오른쪽 하단의 시리얼 포트에 “Null modem(M/F cross gender)”와 다이렉트 시리얼 케이블을 연결합니다. (Vital Recorder 1.8.16.0 이상 버전에서 사용 가능합니다.)

## Maquet Servo-i Ventilator

> Servo-i 장비에서 추가 설정이 필요하지 않습니다. 장비에는 2개의 RS-232 포트가 있습니다. 이 중 아래에 있는 RS-232 포트에 연결합니다. Null modem(M/F cross gender)를 이용하여 연결해야 합니다.
>
> 해당 포트가 환자 모니터 등 다른 장비에 선점되어 있을 경우 데이터 수집이 불가능합니다. 이 경우 환자 모니터 등 장비를 통해서 Ventilator 파형 데이터 등을 전달 받아야 합니다.(예를 들어 Marquet Servo-i → Philips Intellivue → Vital Recorder)
>
> <img src="images/hw_guide_ko/image126.png" width="450" />

## Hamilton G5 Ventilator

> <img src="images/hw_guide_ko/image117.png" width="450" /><img src="images/hw_guide_ko/image154.jpg" width="450" />

<img src="images/hw_guide_ko/image2.png" width="450" />

> Hamilton G5는 1.10.2버전 이상 버전에서 사용 가능합니다.Hamilton G5 기기 후면에는 2개의 RS-232포트가 있습니다.
>
> Monitoring interface 1 혹은 Monitoring interface2 2개의 RS-232포트 중 어떤 곳에 연결해도 상관 없습니다. Null modem(M/F cross gender)와 다이렉트 시리얼 케이블을 연결합니다.
>
> 포트에 케이블을 연결 후 configuration 모드로 들어가 시리얼 설정을 변경해야합니다.

<img src="images/hw_guide_ko/image36.png" width="450" />

기기가 동작중이지 않을 때 configuration 모드로 들어갈 수 있습니다.

<img src="images/hw_guide_ko/image86.png" width="450" />버튼을 동시에 누르면 좌측 하단에 configuration 메뉴가 생성됩니다.

<img src="images/hw_guide_ko/image165.png" width="450" />

변경사항 적용을 위해선 Test mode를 활성화 해야 합니다.

Test mode 활성화를 위해 <img src="images/hw_guide_ko/image163.png" width="450" />버튼을 동시에 누릅니다.

<img src="images/hw_guide_ko/image91.png" width="450" />

Test mode까지 활성화가 되었다면 Configuration - Interface 메뉴를 차례대로 누릅니다.

COM1과 COM중 Vital recorder에 연결한 쪽의 포트를 Block 프로토콜로 변경합니다.

Close - Close/Save 버튼을 차례대로 누르면 설정이 적용됩니다.

# 심기능 감시 장치와의 연결

## Edwards Lifesciences EV-1000

> Edwards Lifesciences사의 장비들은 설정이 모두 똑같습니다.
>
> 단 시리얼 포트의 위치나 메뉴의 구성에 조금 차이가 있으니 아래 가이드를 따라 설정하시기 바랍니다.
>
> Edwards Lifesciences의 제품들 (Vigileo, EV1000A, Vigilance, Vigilance II, Hemosphere 등)의 연결시
>
> 모두 “Null modem(M/F cross gender)”를 사용하여 연결해야 합니다.
>
> 단, EV1000 제품의 구형 모델은 단자가 달라 “Null modem(F/F cross gender)”를 이용하여 연결해야 합니다.
>
> 먼저 EV-1000 구형의 경우를 알아보겠습니다.
>
> “Null modem(F/F cross gender)”와 다이렉트 시리얼 케이블을 오른쪽에서 두번째 포트에 연결합니다.
>
> <img src="images/hw_guide_ko/image43.png" width="450" />
>
> 신형(1000A)의 경우는 아래와 같습니다. “Null modem(M/F cross gender)”를 이용해 연결합니다.
>
> <img src="images/hw_guide_ko/image28.png" width="450" />
>
> 장치에서의 설정은 다음과 같이 합니다.
>
> <img src="images/hw_guide_ko/image179.png" width="450" />
>
> “설정(Settings)” 버튼을 누릅니다.
>
> <img src="images/hw_guide_ko/image144.png" width="450" />
>
> “Monitor Settings”를 누릅니다.
>
> <img src="images/hw_guide_ko/image55.png" width="450" />
>
> “Serial Port Setup”을 누릅니다.
>
> <img src="images/hw_guide_ko/image17.png" width="450" />
>
> “Device”를 “IFMout”으로 설정합니다.
>
> <img src="images/hw_guide_ko/image15.png" width="450" />
>
> “Baud Rate”을 “9600”으로 설정합니다.

## Edwards Lifesciences Vigilance

> Vigilance 의 뒤쪽 패널에는 2개의 시리얼 포트가 있습니다.
>
> 이 중 COM1을 기준으로 설명하겠습니다. (시스템 설정에 따라 COM1, COM2 중 어느것이든 이용할 수 있습니다.)
>
> Edwards Lifesciences 사의 다른 장비들처럼 “Null modem(M/F cross gender)”를 연결 후 시리얼 케이블을 연결합니다.
>
> <img src="images/hw_guide_ko/image174.png" width="450" />
>
> <img src="images/hw_guide_ko/image157.png" width="450" />
>
> “Setup” 버튼을 누릅니다.
>
> <img src="images/hw_guide_ko/image19.png" width="450" />
>
> “System Config” 를 선택합니다.
>
> <img src="images/hw_guide_ko/image88.png" width="450" />
>
> “Return” 을 선택합니다.
>
> <img src="images/hw_guide_ko/image177.png" width="450" />
>
> “Digital Ports” 를 선택합니다.
>
> <img src="images/hw_guide_ko/image48.png" width="450" />
>
> 앞서 COM1 포트를 이용하기로 했다면, COM1의 설정을 아래와 같이 변경합니다.
>
> Device : IFMout
>
> Baud Rate : 9600
>
> Parity : None
>
> Stop Bits : 1
>
> Data Bits : 8
>
> Flow Control : 2 seconds

## Edwards Lifesciences Vigilance II

> <img src="images/hw_guide_ko/image16.png" width="450" />
>
> 모니터 후면의 두 개의 시리얼 포트 중 위쪽의 1번 포트에 “Null modem(M/F cross gender)”를 연결 후 시리얼 케이블을 연결합니다.
>
> <img src="images/hw_guide_ko/image11.png" width="450" />
>
> “설정(Setup)” 버튼을 누릅니다.
>
> <img src="images/hw_guide_ko/image175.png" width="450" />
>
> “Serial Port Setup”을 선택합니다.
>
> <img src="images/hw_guide_ko/image199.png" width="450" />
>
> “Port 1”을 선택합니다.
>
> <img src="images/hw_guide_ko/image49.png" width="450" />
>
> “Device”를 “IFMout”, “Baud Rate”를 “9600”으로 설정합니다.

## Edwards Lifesciences Vigileo

> <img src="images/hw_guide_ko/image110.png" width="450" />
>
> 후면에 1개의 시리얼 포트가 있습니다. “Null modem(M/F cross gender)”를 연결 후 시리얼 케이블을 연결합니다.
>
> <img src="images/hw_guide_ko/image81.png" width="450" />
>
> 화면의 왼쪽 아래 빈 공간을 선택하면 설정 메뉴로 들어갑니다.
>
> <img src="images/hw_guide_ko/image116.png" width="450" />
>
> “Serial Port Setup”을 선택합니다.
>
> <img src="images/hw_guide_ko/image26.png" width="450" />
>
> “Device”에서 “IFMout”을 선택합니다.
>
> <img src="images/hw_guide_ko/image167.png" width="450" />
>
> “Baud Rate”에서 “9600”을 선택합니다.
>
> “Return”을 선택해 빠져나옵니다.

## Edwards Lifesciences Hemosphere

> <img src="images/hw_guide_ko/image161.png" width="450" />
>
> 기기 후면 시리얼 포트에 “Null modem(M/F cross gender)”와 다이렉트 시리얼 케이블을 연결합니다.
>
> <img src="images/hw_guide_ko/image9.png" width="450" />
>
> 모니터 왼쪽 하단에 설정(setup)버튼을 누릅니다.
>
> <img src="images/hw_guide_ko/image76.png" width="450" />
>
> “Advanced Setup” 버튼을 누릅니다.
>
> <img src="images/hw_guide_ko/image23.png" width="450" />
>
> Advanced setup Password는 “55555555”입니다.
>
> <img src="images/hw_guide_ko/image72.png" width="450" />
>
> “Connectivity” 를 선택합니다.
>
> <img src="images/hw_guide_ko/image120.png" width="450" />
>
> “Serial Port Setup”을 선택합니다.
>
> <img src="images/hw_guide_ko/image134.png" width="450" />
>
> “Device”에서 “IFMout”
>
> “Baud Rate”에서 9600을 선택합니다.
>
> 이후 장비를 재부팅해야 변경사항이 적용 됩니다.
>
> (Vital Recorder 1.8.16.4 이상 버전에서 사용 가능합니다.)

## Deltex CardioQ

> 환자에게 장비를 연결하기 전에 설정해야 합니다. 사용 중에는 설정할 수 없습니다.
>
> 설정이 완료되면 DEMO 모드를 통해 데이터 전송 여부를 확인할 수 있습니다.
>
> 후면에 1개의 시리얼 포트가 있습니다. “Null modem(F/F cross gender)”를 연결 후 시리얼 케이블을 연결합니다.
>
> <img src="images/hw_guide_ko/image196.png" width="450" />
>
> 부팅 시 General > Patient monitors > Monitor Setup 을 누른 후 CardioQ Serial Protocol v2 를 선택합니다.
>
> Baud Rate 57600, No Flow Control 로 세팅 되어있음을 확인한 후 (아니라면 변경합니다) Finished 버튼을 눌러 빠져 나옵니다.
>
> <img src="images/hw_guide_ko/image160.png" width="450" />
>
> <img src="images/hw_guide_ko/image156.png" width="450" />
>
> <img src="images/hw_guide_ko/image37.png" width="450" />
>
> <img src="images/hw_guide_ko/image180.png" width="450" />

## LiDCO

> 후면에 1개의 시리얼 포트가 있습니다. “Null modem(F/F cross gender)”를 연결 후 시리얼 케이블을 연결합니다.
>
> <img src="images/hw_guide_ko/image59.png" width="450" />
>
> Settings > Communications > Serial 로 들어가 LiDCOserial Enabled를 선택합니다.
>
> Baud rate 57600, Stop Bits 1, Data bits 8, Parity None 을 유지합니다. (기본 값)
>
> Average Never, Observation beat-to-beat 으로 변경합니다.
>
> <img src="images/hw_guide_ko/image68.png" width="450" />

# 수액 및 약물 주입 장치와의 연결

## Fresenius Vial Orchestra (Base Primea with Module DPS)

> 다소 복잡하니 차근차근 따라하시기 바랍니다.
>
> <img src="images/hw_guide_ko/image172.png" width="450" />
>
> 먼저 전원을 끄고 붉은 원으로 표시한 버튼 3개(파란 버튼 중 가장 위의 것, 음소거 버튼, 전원 버튼)를 동시에 눌러서 전원을 켭니다.
>
> <img src="images/hw_guide_ko/image181.png" width="450" />
>
> “Serial & …”을 선택하기 위해 위에서 4번째 파란 버튼을 누릅니다.
>
> <img src="images/hw_guide_ko/image47.png" width="450" />
>
> “SERIAL PORTS” 항목에서 오른쪽 위에서 두 번째의 “COM NEW SUP”을 선택합니다 (조그 다이얼을 돌려서 선택).
>
> 선택후 나오는 숫자 중에서 “3을 선택합니다.
>
> 오른쪽 아래의 COMM NEW SUP 의 Send a frame on every change 의 체크를 풀고 Send every: 1 s으로 설정합니다.
>
> 전원 버튼을 눌러 전원을 끕니다. 이어서 다시 전원 버튼을 눌러 전원을 켭니다.
>
> <img src="images/hw_guide_ko/image46.png" width="450" />
>
> 전원이 켜진 상태에서 오른쪽 하단의 버튼들 중 “OPT” 버튼을 누릅니다.
>
> <img src="images/hw_guide_ko/image75.png" width="450" />
>
> “CUSTOMISATION”을 선택합니다.
>
> <img src="images/hw_guide_ko/image21.png" width="450" />
>
> “CODE”가 선택될 때까지 조그다이얼을 시계방향으로 돌립니다.
>
> 코드를 입력할 수 있는 상태가 되면 차례로 “00123”을 입력합니다.
>
> <img src="images/hw_guide_ko/image94.png" width="450" />
>
> 이제 “SERIAL PORTS AND PRINTER”를 선택할 수 있게 되었습니다.
>
> 조그다이얼을 돌려서 선택합니다.
>
> <img src="images/hw_guide_ko/image39.png" width="450" />
>
> “RS-232-3”을 선택하고 이어서 “IDMS”를 선택합니다.
>
> <img src="images/hw_guide_ko/image184.png" width="450" />
>
> RS 232-3 포트가 IDMS로 설정된 것을 확인 후 저장하고 빠져나옵니다. 변경 사항이 있다면 다시 껐다켜야 적용 됩니다.
>
> <img src="images/hw_guide_ko/image92.png" width="450" />
>
> Base Primea (오케스트라의 하단)의 오른쪽 옆을 보면 여러 개의 단자들이 있습니다.
>
> 3개의 시리얼 포트 중 오른 쪽 끝의 세로로 서있는 것(RS 232-3)이 우리가 이용할 포트입니다.
>
> 여기에 “Null modem(M/F cross gender)”를 연결 후(!!!) 시리얼 케이블을 연결합니다.

##

## Fresenius Kabi Agilia

> 뒷면의 원형 소켓에 꽂을 수 있는 전용 케이블로 연결합니다.
>
> 전용 케이블은 Fresenius Kabi 측에 문의하여 구매할 수 있으며 가격은 약 13만원 정도 입니다.
>
> 케이블의 반대편은 DB9 female로 되어 있으므로 별도의 젠더 없이 일반적인 USB Serial cable (DB9 male) 과 연결하면 됩니다.
>
> <img src="images/hw_guide_ko/image65.png" width="450" />

##

## Fresenius Kabi Agilia Link+

> Link+ 장비의 측면 하단에 있는 USB-b 포트에 USB 2.0 AM-Mini 5핀 케이블을 연결합니다.
>
> 케이블과 별도로 Link+와 PC를 연결하여 초기 설정이 추가로 필요합니다.
>
> <img src="images/hw_guide_ko/image182.png" width="450" /><img src="images/hw_guide_ko/image162.png" width="450" />
>
> <img src="images/hw_guide_ko/image201.png" width="450" /><img src="images/hw_guide_ko/image12.png" width="450" />
>
> PC에서 제어판 > 네트워크 및 인터넷 > 네트워크 연결 > 이더넷에 들어갑니다.
>
> 이더넷을 우클릭하여 속성창에 들어갑니다.
>
> <img src="images/hw_guide_ko/image151.png" width="450" />
>
> “인터넷 프로토콜 버전4”를 체크 후 속성에 들어갑니다.
>
> <img src="images/hw_guide_ko/image30.png" width="450" />
>
> “다음 IP 주소 사용”을 체크 후 IP 주소를 “192-168-0-100”으로 입력합니다.
>
> IP 주소를 입력하면 서브넷 마스크는 자동으로 입력이 됩니다.
>
> 기본 게이트웨이는 “192-168-0-1”로 입력합니다.
>
> 입력을 완료한 후 확인 버튼을 누릅니다.
>
> <img src="images/hw_guide_ko/image159.png" width="450" />
>
> 인터넷 주소창에 “192.168.0.1”를 입력합니다.
>
> <img src="images/hw_guide_ko/image152.png" width="450" />
>
> 주소를 입력하면 Agilia Link+ 로그인창이 나타납니다.
>
> ID는 “admin”, Password는 “fresenius”입니다.
>
> <img src="images/hw_guide_ko/image10.png" width="450" />
>
> 로그인 후 Configuration > Data Export를 누릅니다.
>
> <img src="images/hw_guide_ko/image32.png" width="450" />
>
> Data Export에 들어간 후, Enabled 옆을 체크표시를 합니다.
>
> 체크 후 Apply를 누릅니다.
>
> <img src="images/hw_guide_ko/image13.png" width="450" />
>
> Apply를 후 다음과 같은 창이 나타나면 OK를 누릅니다.
>
> <img src="images/hw_guide_ko/image106.png" width="450" />
>
> 마지막으로 Exit Configuration을 누르면 자동으로 재시작이 되면 설정이 완료됩니다.
>
> 장비의 측면 하단에 있는 USB-B 포트에 USB 2.0 - Mini 5핀 케이블을 연결합니다.
>
> 별도의 젠더 없이 Mini 5핀 쪽을 장비에, USB 쪽을 Vital Recorder에 연결하면 됩니다.

## BBraun SpaceCom

> BCC Protocol settings 하부 메뉴로 들어가 아래와 같이 설정합니다.
>
> <img src="images/hw_guide_ko/image54.png" width="450" />
>
> 전용 케이블이 필요합니다. 부품을 구매해 제작할 수 있습니다.
>
> 9핀 mini DIN 단자의 2번, 3번, 5번을 Female 9핀 DSUB 단자의 3번, 2번, 5번으로 연결한 케이블을 제작합니다.
>
> 이후 SpaceCom의 설정 변경이 필요합니다. SpaceCom은 설정 변경을 위해 웹인터페이스(SpaceOnline)를 제공합니다.
>
> 장비의 웹인터페이스에 접속하기 위해 컴퓨터와 SpaceCom을 direct LAN cable로 연결합니다.
>
> SpaceCom의 기본 IP 설정은 192.168.100.41 입니다.
>
> 따라서 컴퓨터를 192.168.100.42로 (서브넷마스크 255.255.255.0 게이트웨이 192.168.100.1)로 설정합니다.
>
> 웹 브라우저를 켜고 192.168.100.41 주소를 입력하여 웹인터페이스에 접속합니다.
>
> Configuration 메뉴로 들어갑니다. 초기 사용자명은 config 암호는 config 입니다.
>
> <img src="images/hw_guide_ko/image194.png" width="450" />
>
> <img src="images/hw_guide_ko/image74.png" width="450" /><img src="images/hw_guide_ko/image143.png" width="450" /><img src="images/hw_guide_ko/image38.png" width="450" />
>
> Save 버튼을 누르면 변경 사항이 저장됩니다.

## Bionet Pion TCI

> 장비 뒷면의 9핀 포트를 통해 통신합니다. 별도의 젠더는 필요없고 다이렉트 시리얼 케이블을 연결하면 됩니다.
>
> <img src="images/hw_guide_ko/image104.png" width="450" />
>
> 여러 개의 Pion 펌프를 동시에 하나의 Vital Recorder 에 연결하여 녹화하는 경우가 생길 수 있습니다.
>
> 때문에 Vital Recorder 에서는 Pion 펌프의 장비명(Add Device 시 지정 가능) 내에 있는 첫 숫자를 인식하여 트랙명에 반영합니다.
>
> 예를 들어 장비명이 Pion2 라면 이로부터 취득되는 데이터는 PUMP2 라는 앞에 이름이 붙습니다. 만일 숫자가 없으면 PUMP1이 됩니다.
>
> <img src="images/hw_guide_ko/image121.png" width="450" />

##

## Belmont FMS (RI-2)

> 이 장비의 통신 포트는 하단 환풍구 옆에 숨어있습니다.

#### <img src="images/hw_guide_ko/image119.png" width="450" />

> 장비쪽이 Male 커넥터이므로.“Null modem(F/F cross gender)”를 연결 후 시리얼 케이블을 연결합니다.

# 뇌 감시 장비와의 연결

## Medtronic BIS VISTA

> <img src="images/hw_guide_ko/image27.png" width="450" />
>
> 메뉴를 누릅니다.
>
> <img src="images/hw_guide_ko/image204.png" width="450" />
>
> “NEXT”를 누릅니다.
>
> <img src="images/hw_guide_ko/image7.png" width="450" />
>
> 다시 “NEXT”를 누릅니다.
>
> <img src="images/hw_guide_ko/image107.png" width="450" />
>
> “Maintenance”를 선택합니다.
>
> <img src="images/hw_guide_ko/image169.png" width="450" />
>
> “Serial Protocol”을 선택합니다.
>
> <img src="images/hw_guide_ko/image73.png" width="450" />
>
> “ASCII”를 선택하면 BIS 모니터에서 생성되는 모든 숫자 데이터를 얻을 수 있습니다.
>
> <img src="images/hw_guide_ko/image51.png" width="450" />
>
> “Legacy Binary”를 선택하고Vital Recorder에서 BIS (binary)를 선택하면 EEG wave를 얻을 수 있습니다.
>
> 여기까지 설정이 끝나면 저장하고 Home으로 돌아옵니다.
>
> 주의 : 프로토콜 변경은 장비가 재시작되어야 적용 되므로 BIS 장비를 재시작합니다.
>
> <img src="images/hw_guide_ko/image6.png" width="450" />
>
> 장비의 후면에 시리얼 포트가 보입니다. 이곳에 다이렉트 시리얼 케이블을 연결합니다.
>
> 혹시라도 크로스케이블을 잘못 연결하게 되면 아래와 같은 화면을 보게 되니 조심하시기 바랍니다.
>
> <img src="images/hw_guide_ko/image171.png" width="450" />

##

## Medtronic BIS A2000

> Medtronic BIS A2000 장비는 BIS Vista와 비슷하지만 2채널 256Hz 뇌파를 얻을 수 있다는 차이가 있습니다.
>
> <img src="images/hw_guide_ko/image158.png" width="450" />
>
> 장비 뒷면의 9핀 포트에 다이렉트 케이블을 이용하면 되고 장비 설정 방법은 다음과 같습니다.
>
> 메뉴 버튼을 누르고
>
> <img src="images/hw_guide_ko/image109.png" width="450" />
>
> “Advanced Setup” 을 선택합니다.
>
> <img src="images/hw_guide_ko/image138.png" width="450" />
>
> “Diagnostic Menu”를 선택합니다.
>
> <img src="images/hw_guide_ko/image69.png" width="450" />
>
> “System Configuration Menu”를 선택합니다.
>
> <img src="images/hw_guide_ko/image62.png" width="450" />
>
> Serial Port Protocol 에서 Binary를 선택 (검정색 배경에 노란 글씨가 되도록) 합니다.
>
> Return To Diagnostic Menu > Return to Advanced Setup Menu > Save Settings 를 누릅니다.

## Medtronic INVOS Cerebral/Somatic Oximetry

> <img src="images/hw_guide_ko/image150.png" width="450" />
>
> 장비 뒷면의 \|O\|O\| 포트에 케이블을 연결합니다.”Null nodem(F/F cross gender)”를 이용합니다.
>
> <img src="images/hw_guide_ko/image124.png" width="450" />
>
> 설정 창을 열기 위해서는 다음 화면으로 이동해야합니다.” Next Menu“ 버튼을 누릅니다.
>
> <img src="images/hw_guide_ko/image112.png" width="450" />
>
> “Output Select” 버튼을 누릅니다.
>
> <img src="images/hw_guide_ko/image82.png" width="450" />
>
> “Digital Output” 버튼을 누릅니다.
>
> <img src="images/hw_guide_ko/image202.png" width="450" />
>
> “PC Link” 로 들어갑니다.
>
> <img src="images/hw_guide_ko/image128.png" width="450" />
>
> “OUTPUT FORMAT 1” 을 선택합니다.

# 다기능 감시 장비와의 연결

## Masimo Radical7

> 이 장치는 Docking Station에 연결될 경우 실시간 SpO2, HR, PI 데이터 및 waveform 을 추출할 수 있습니다.
>
> Docking Station 의 뒷면 패널의 P1 (RS-232) 포트를 통해 디지털 데이터를 추출합니다.
>
> 일반 Direct Male 케이블을 이용합니다. Serial To USB 컨버터의 경우 젠더 없이 그냥 연결하시면 됩니다.
>
> P2 라고 씌여진 아날로그 포트를 통해 pleth waveform을 추출합니다.
>
> <img src="images/hw_guide_ko/image22.png" width="450" />
>
> 장치에서 설정이 먼저 필요합니다.
>
> <img src="images/hw_guide_ko/image113.png" width="450" />
>
> main menu에서 “Device settings”로 들어갑니다.
>
> <img src="images/hw_guide_ko/image206.png" width="450" />
>
> 우측으로 스와이프하여 “Device output”을 터치합니다.
>
> <img src="images/hw_guide_ko/image108.png" width="450" />
>
> serial 종류를 ASCII 1 으로, analog 1과 2는 Pleth 로 설정합니다.
>
> <img src="images/hw_guide_ko/image52.png" width="450" />
>
> 아래로 swipe 하여 docking station baud rate 를 9600 으로 설정합니다.

## Masimo ROOT

> 이 장비는 장치에서의 설정이 먼저 필요합니다.
>
> <img src="images/hw_guide_ko/image132.png" width="450" />
>
> main menu에서 “Device settings”로 들어갑니다.
>
> <img src="images/hw_guide_ko/image197.png" width="450" />
>
> 우측으로 스와이프하여 “Access control”을 터치합니다.
>
> <img src="images/hw_guide_ko/image205.png" width="450" />
>
> enter password는 “6274”입니다.
>
> <img src="images/hw_guide_ko/image146.png" width="450" />
>
> <img src="images/hw_guide_ko/image208.png" width="450" />
>
> access control에 진입하면 아래쪽의 USB Port 1 baudrate, USB Port 2 baudrate 를 모두 19200으로 변경합니다.
>
> 변경 후 이전 화면으로 나와 장치의 출력 프로토콜을 변경합니다
>
> .<img src="images/hw_guide_ko/image123.png" width="450" />
>
> “Device output”을 터치합니다.
>
> <img src="images/hw_guide_ko/image189.png" width="450" />
>
> USB Port 1과 USB Port 2를 모두 ASCII 1으로 변경합니다.
>
> 이후 장비를 재부팅해야 변경 사항이 적용 됩니다.
>
> ROOT 오른쪽 아래의 전원 버튼을 8초 이상 눌러서 전원을 끈 후 다시 전원 버튼을 눌러 장비를 켭니다.
>
> 설정이 끝났으면 케이블을 연결합니다.
>
> Masimo에서 제공하는 데이터취득용 USB 케이블을 사용하면 연결이 간편합니다.
>
> ROOT 뒤쪽의 USB1또는 USB2 포트에 케이블을 꽂고 나머지 한 쪽을 PC에 연결합니다.
>
> <img src="images/hw_guide_ko/image35.png" width="450" />
>
> PC에 새로운 USB serial COM 포트가 생성됩니다.

Vital Recorder에서 Add device 버튼을 눌러 ROOT를 추가한 후 새로 생성된 COM 포트를 지정합니다.

> Masimo USB cable을 이용하지 않을 경우 USB to serial converter와 “Null modem(F/F cross gender)”을 이용합니다.
>
> (ROOT USB1 or 2 - USB to serial - null modem(F/F cross gender) - serial to USB - PC USB port )
>
> 위와 마찬가지로 Vital Recorder에서 ROOT를 추가 후 USB serial COM 포트에 지정합니다.
>
> <img src="images/hw_guide_ko/image153.png" width="450" /> <img src="images/hw_guide_ko/image127.png" width="450" />
>
> 모든 과정이 완료되면 아래와 같이 데이터가 기록됩니다.
>
> 만약 데이터 일부가 안 들어오는 등의 문제가 생기는 경우 재부팅을 2-3회 더 반복하거나 USB 포트를 변경해 봅니다.
>
> <img src="images/hw_guide_ko/image45.png" width="450" />
>
> * 주의 1
>
> 대부분의 USB-serial converter들이 ROOT에서 제대로 인식되지 않습니다.
>
> 저희가 확인한 제품 중에는 다음 제품만이 제대로 작동합니다.

- NEXT(넥스트) USB 2.0 to SERIAL 변환기 1포트 [NEXT-RS232U20] [**http://cableguy.com/shop/mall.php?cat=005004001&query=view&no=6028**](http://cableguy.com/shop/mall.php?cat=005004001&query=view&no=6028)

> * 주의 2
>
> 레인보우 센서의 데이터가 출력되게 하기 위해서는 반드시 Radical-7이 먼저 켜지고 이후에 ROOT가 켜져야 합니다.
>
> ROOT가 먼저 켜져 있다면 일단 ROOT를 종료시키고 Radical-7을 켠 후에 다시 ROOT를 켭니다.
>
> 따라서 실수없이 항상 데이터를 취득하기 위해 추천하는 방법은 “항상 Radical-7을 켜놓는 것”입니다.
>
> PiVR 기기와 유선으로 연결하는 경우, 다음과 같은 설정이 필요합니다.
>
> <img src="images/hw_guide_ko/image132.png" width="450" />
>
> main menu에서 “Device settings”로 들어갑니다.
>
> <img src="images/hw_guide_ko/image173.png" width="450" />
>
> 우측으로 스와이프하여 “ETHERNET”을 터치합니다.
>
> <img src="images/hw_guide_ko/image44.png" width="450" />
>
> ethernet 설정창의 맨 위 ethernet ON을 눌러 활성화시켜 줍니다.
>
> <img src="images/hw_guide_ko/image168.png" width="450" />
>
> LAN cable을 ROOT 기기 뒷 쪽의 LAN port와 PiVR의 LAN port에 연결합니다.

## Sentec: SDM

> Sentec SDM 장비는 뒷면의 Serial Port 에 일반 USB Serial Converter를 연결하여 통신 가능합니다.
>
> <img src="images/hw_guide_ko/image53.png" width="450" />
>
> Interfaces > Serial Interface 메뉴로 들어가 Protocol 을 SenTecLink로, Baud Rate 를 115200 으로 수정하면 됩니다.
>
> <img src="images/hw_guide_ko/image164.png" width="450" />

## MDMS ANI Monitor V2

> <img src="images/hw_guide_ko/image210.jpg" width="450" />
>
> 센서를 장착 후 New patient 메뉴를 누르고 1분 가량 기다리면 위와 같은 화면이 나옵니다.
>
> <img src="images/hw_guide_ko/image64.png" width="450" />
>
> <img src="images/hw_guide_ko/image83.jpg" width="450" />
>
> 장비 오른편에 있는 serial port에 USB to serial converter( NEXT(넥스트) USB 2.0 to SERIAL 변환기 1포트 [NEXT-RS232U20] )를 연결합니다.

## GE: Corometrics 170

<img src="images/hw_guide_ko/image66.png" width="450" />

<img src="images/hw_guide_ko/image100.png" width="450" />

모니터의 설정 모드로 들어가기 위해 setup 버튼(시계, 달력 그림)을 누른 채로 전원 버튼을 누릅니다. 설정하는 동안 setup 버튼을 누르고 있어야 합니다.

<img src="images/hw_guide_ko/image183.png" width="450" />

> UA reference button 을 사용해서 FHR display 또는 UA display의 설정을 활성화 할 수 있습니다.
>
> Communication mode와 baudrate 설정을 변경해야 합니다. Communication mode는 FHR display에서 30,31이며 115 update(UA display에서 5)로 설정합니다. baudrate 설정은 FHR display에서 40,41이고 9600(UA display에서 96)으로 설정합니다. Volume button을 이용해서 아래의 숫자를 변경할 수 있습니다.
>
> RS232 port1 에 연결 할 경우: FHR display(30) : UA display(5), FHR display(40) : UA display(96)
>
> RS232 port2 에 연결 할 경우: FHR display(31): UA display(5), FHR display(41): UA display(96),

# 신경근 감시 장비와의 연결

## BlinkDC: TwitchView

> TwichView 모니터와 연결이 되면 RJ45 커넥터를 통해 데이터가 출력됩니다.
>
> TwichView의 데이터가 출력되게 하기 위해서는 configuration code를 입력하여 메뉴를 열고 밑에 사진과 같이 설정을 바꿔 주어야 합니다.
>
> <img src="images/hw_guide_ko/image145.png" width="450" />
>
> Menu - Device settings로 들어갑니다.
>
> <img src="images/hw_guide_ko/image200.png" width="450" />
>
> Clock - SET을 터치합니다.
>
> <img src="images/hw_guide_ko/image213.png" width="450" />
>
> 시간을 Hour : 1AM, Minute : 2, Month : March, Day: 4, Year: 2018로 변경하고 Set을 터치합니다.
>
> <img src="images/hw_guide_ko/image211.png" width="450" />
>
> Serial을 선택하고 set을 터치하면 설정이 변경됩니다.
>
> 흔히 사용되는 Serial To USB로 기기를 연결하기 위해서 다음과 같은 케이블을 제작하여야 합니다.
>
> <img src="images/hw_guide_ko/image96.png" width="450" />

## IDMed TOFscan

> <img src="images/hw_guide_ko/image97.png" width="450" /><img src="images/hw_guide_ko/image118.png" width="450" />
>
> IDMed로부터 TOF-RS1 이라고 하는 케이블을 구매하여 USB-Serial-Converter에 젠더 없이 직결하면 데이터 수집이 가능합니다.

# 흔히 발생하는 문제의 해결법

> Vital Recorder에 장치를 잘 연결했음에도 불구하고 **장치가 인식되지 않는 경우** 다음 문제 중 하나일 수 있습니다.

## 장치 드라이버 문제

- 원인 : 장치가 운영체에서 인식되기 위해서는 드라이버가 설치되어야 합니다.

- 진단 : 장치 관리자에서 장치의 포트가 보여지는지 확인합니다. 아래 그림의 왼쪽과 같이 USB Serial Port 장비에 노란색 느낌표가 있다면 장비의 고장이거나 드라이버 문제입니다. 우측과 같이 포트(COM & LPT)에 장비가 보여져야 정상입니다.

- <img src="images/hw_guide_ko/image203.png" width="450" />

<!-- -->

- 해결 방법 : Serial to USB 컨버터의 드라이버를 제조사 홈페이지에서 받아 설치해 보세요. 문제가 계속된다면 Serial to USB 컨버터를 교체해 보는 것도 감별을 위한 방법입니다.

## 잘못된 포트에 연결

- 원인 : 4포트 USB 허브의 경우 간혹 물리적 포트 번호와 인식되는 COM 포트 번호의 순서가 바뀌는 경우가 있습니다.

<!-- -->

- 진단 및 해결 방법 : 장치를 1개씩 연결하면서 Device 추가 대화상자에서 COM 포트를 변경해서 인식시켜 보세요.

> Vital Recorder에서 장치가 연결 되고 **통신되지만 몇 초 ~ 몇 시간 마다 장치 연결이 끊기는 경우** 다음 원인일 수 있습니다.

## 허브 전원 부족 문제

> 장비 연결이 되다가 끊기는 가장 흔한 원인은 전원 부족 문제입니다.

- 원인 : USB 포트에서 장비에 공급할 전을 충분히 제공하지 못할 경우 장비는 일시적으로 정상 동작할 수 있지만 언제든 끊기거나 오작동할 수 있습니다. 특히 USB 포트 하나에 여러 장비를 연결하기 위해 USB 허브를 사용하는 경우 이 문제일 가능성이 높습니다.

<!-- -->

- 해결 방법 : 외부 아답터로부터 별도의 전원을 공급받는 유전원 USB 허브를 이용하여야 합니다.

## 외부 노이즈

- 원인 : 수술장에는 전기 소작기(electrocautery), 심폐기, 공기 가온기(air warmer), 신경근 전위 유발 장비 등 많은 전자 장비들이 사용됩니다. 이들에서 발생하는 전원 노이즈가 데이터 취득용 컴퓨터나 ADC등 장비의 작동을 방해할 수 있습니다.

- 진단 : 전기 소작기 등 외부 장치를 사용할 때 장치 연결이 끊어지거나 컴퓨터 전원이 꺼지는 경우

<!-- -->

- 해결 방법 : 가급적 모든 장비들과 데이터 취득용 컴퓨터의 전원을 분리하세요. 특히 전기 소작기의 전원 선은 데이터 취득용 컴퓨터 및 허브 장비와 분리하세요. 장비와 USB 포트 사이의 연결은 가급적 최대한 짧은 길이의 절연선(shielded cable) 혹은 꼬인선(twisted cable)을 사용합니다.

## USB 포트와의 접촉 불량

> 잘 작동하는 방비가 가끔씩 끊어지는 두번째로 흔한 원인입니다. 특히 컴퓨터 포트를 변경하여 장치를 인식시켰을 때 안정적으로 연결 된다면 포트 불량일 가능성이 있습니다.

- 원인 : 컴퓨터 상의 포트와 케이블 사이의 접촉이 헐거워졌거나 포트에 케이블이 꽂힌 채로 당겨지거나 하는 등의 원인으로 컴퓨터의 USB 포트가 망가질 수 있습니다. 수술장은 특히 suction 튜브나 각종 케이블 등으로 인해 장비와 컴퓨터 사이의 연결선이 이 당겨지기 쉬운 환경이므로 포트에 케이블을 단단히 고정해 두지 않으면 데이터 취득용 컴퓨터의 포트가 망가지는 경우가 매우 흔합니다.

- 해결 방법 : 당겨지거나 빠질 가능성이 없도록 반드시 모든 케이블을 마취기 등 고정된 장비에 고정하세요. 케이블이 당겨져도 포트에 힘이 가해지지 않도록 케이블 타이를 이용해 단단히 고정하는 것이 좋습니다.

- 컴퓨터의 포트가 망가졌다면 포트를 변경하세요. 남은 포트가 부족하다면 정상 동작하는 포트를 통해 2포트 혹은 4포트 유전원 USB 허브를 이용하여 장치를 연결하세요. 남은 포트가 하나도 없다면 컴퓨터의 보드 제조사에 A/S를 의뢰하거나 컴퓨터를 교체하세요.

## USB 케이블 불량

- 원인 : USB 케이블이 밟히거나 꼬이거나 당겨져서 내부의 단선이 발생하거나 포트쪽 커넥터가 망가져 접촉 불량이 발생할 수 있습니다.

- 진단 : USB 케이블을 바꿔서 문제가 해결되는지 확인합니다.

- 해결 방법 : 케이블을 교체합니다.

## USB 연장 케이블

- 원인 : USB 케이블의 길이가 짧을 경우 USB 연장 케이블을 이용하여 USB 케이블의 길이를 연장합니다. 그러나 USB 연장 케이블과 기존 USB 장비 사이의 접촉 불량이 발생할 수 있고 너무 긴 전송 거리로 인해 신호 왜곡 등의 문제가 발생하여 장치가 이상 작동할 수 있습니다.

- 진단 : USB 연장 케이블을 제거하고 직접 USB 장비를 컴퓨터에 연결하여 문제가 해결되는지 확인합니다.

- 해결 방법 : USB 연장 케이블을 제거합니다.

###
