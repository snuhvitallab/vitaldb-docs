#

# VitalConnect란?

> Vital Recorder를 통해 데이터를 수집하기 위해서는 다수의 유선 연결이 필요합니다.
>
> 데이터 수집을 위한 많은 케이블들은 진료에 불편을 초래하고 단선으로 인해 의도하지 않은 데이터 기록의 누락을 유발합니다.
>
> 이러한 문제를 해결하기 위해 wifi 무선 통신 기술을 이용하여 시리얼 단자의 출력을 Vital Recorder로 보내줄 수 있는 장비를 개발하게 되었습니다.
>
> 본 장비는 Arduino 호환 보드인 Wemos(ESP-8266)를 바탕으로 하여 제작되었습니다.
>
> 본 장비를 한 마디로 정의하자면 “Serial to Wi-Fi “ 장비라 할 수 있습니다.
>
> 장치의 회로도는 다음과 같습니다.
>
> <img src="images/vitalconnect_ko/image8.png" width="450" />
>
> 실제 회로기판은 아래와 같습니다.
>
> <img src="images/vitalconnect_ko/image12.png" width="450" />
>
> 장치의 외관은 아래와 같습니다.
>
> <img src="images/vitalconnect_ko/image3.png" width="450" />
>
> RJ-45 단자는 8핀 랜포트와 모양은 동일하지만 시리얼 연결을 하도록 만들어져 있습니다.
>
> Micro USB 단자는 컴퓨터와 연결하여 펌웨어 수정, 장치 설정 등을 할 수 있으며 단독으로 사용 시에는 전원공급 단자로 사용됩니다.

# 필요한 준비물

## 컴퓨터

> VitalConnect의 설정은 다양한 운영체제에서 할 수 있지만 본 문서에서는 윈도우 시스템을 중심으로 설명합니다.
>
> Vital Recorder를 통해서 VitalConnect 설정을 합니다.
>
> 다수의 장비를 효과적으로 운용하기 위해서는 데이터 수집용 컴퓨터와 다른 별도의 컴퓨터에 Vital Recorder와 VitalConnect의 드라이버를 설치하는 것이 좋습니다.

## 케이블

###

### 마이크로 USB 케이블

> VitalConnect는 micro USB 단자를 통해 컴퓨터와 통신합니다. 장치의 설정을 위해서는 컴퓨터와 유선 연결을 반드시 1회 실행해야 합니다.
>
> 설정 후에는 VitalConnect는 독립적으로 작동하며 이 때 micro USB 단자는 전력 공급용으로 사용합니다.

### Serial to RJ-45 cable

> Vitalconnect에는 RJ-45 포트(8핀 유선랜 포트와 동일)가 있습니다. 의료장비와의 연결은 시리얼 케이블을 통해 이루어집니다.
>
> 따라서 VitalConnect 장비와 의료장비의 연결을 위한 DB-9 to RJ-45 케이블이 필요합니다.
>
> Cable을 만들려면 아래와 같이 준비합니다. (Philips Intellivue MP/MX 시리즈 연결시와 동일한 케이블입니다).
>
> [ Direct cable ]
>
> <img src="images/vitalconnect_ko/image13.png" width="450" />
>
> [ Cross cable ]
>
> <img src="images/vitalconnect_ko/image24.png" width="450" />

# 드라이버 설치

> 앞서 말한 것처럼 VitalConnect는 Wemos 장비를 베이스로 하며 컴퓨터에서 장치를 인식하도록 하기 위해 Wemos의 윈도우용 드라이버의 설치가 필요합니다.
>
> 드라이버는 아래의 사이트에서 다운로드 합니다.
>
> [http://www.wch.cn/download/CH341SER_ZIP.html](http://www.wch.cn/download/CH341SER_ZIP.html)
>
> <img src="images/vitalconnect_ko/image2.png" width="450" />
>
> 파일을 다운로드하고 압축을 풉니다.
>
> <img src="images/vitalconnect_ko/image17.png" width="450" />
>
> setup.exe를 실행하여 드라이버를 설치합니다.
>
> <img src="images/vitalconnect_ko/image26.png" width="450" />
>
> VitalConnect를 컴퓨터와 USB 케이블로 연결하고 장치관리자에서 USB-SERIAL CH340 포트가 생성된 것을 확인합니다.
>
> <img src="images/vitalconnect_ko/image11.png" width="450" />

# VitalConnect 설정하기

> VitalConnect를 컴퓨터와 USB 케이블로 연결한 상태에서 Vital Recorder를 실행하고 와이파이 아이콘을 클릭합니다.
>
> <img src="images/vitalconnect_ko/image22.png" width="450" />
>
> CH340 포트가 자동으로 선택됩니다. Connect 버튼을 누르면 Connected 라는 메세지가 출력되어야 합니다.
>
> <img src="images/vitalconnect_ko/image14.png" width="450" />
>
> VitalConnect가 접속할 핫스팟의 SSID와 접속 암호를 입력합니다. 암호는 *로 표시됩니다.
>
> Connect ID는 Vital Recorder의 장비 추가 시 Serial Port 목록에서 보이는 이름입니다.
>
> VitalConnect를 연결할 장비명으로 설정하시면 편리합니다.
>
> <img src="images/vitalconnect_ko/image16.png" width="450" />
>
> 설정이 완료되면 ”Write” 버튼을 눌러 설정값을 전송합니다. 전송이 완료되면 “Disconnect” 버튼을 누른 후 컴퓨터에서 분리합니다.

# 무선 연결: 무선공유기를 이용한 연결

> 핫스팟을 이용한 연결에서 데이터의 누락이 발생한다면 무선 공유기를 이용한 연결로 바꿔보는 것을 권장합니다.
>
> 개방된 작은 공간에서 (예: 회복실) 하나의 공유기를 사용하여 여러 개의 Vital Recorder에 VitalConnect로부터의 데이터를 연결할 수 있지만
>
> 가급적이면 하나의 Vital Recorder에 하나의 공유기를 사용하시기를 권합니다.
>
> 무선공유기 사용시의 데이터 흐름도는 다음과 같습니다.
>
> **의료 장비 → VitalConnect → 무선 공유기 → (무선 또는 유선 연결) Vital Recorder → 무선 공유기 → 인터넷**

## 공유기 설정

> 저희가 테스트해 본 저렴하고 성능좋은 공유기는 EFM사의 ipTIME mini 2/3 입니다.
>
> 인터넷쇼핑몰에서 11,000원 정도에 구매할 수 있습니다. 이후의 설명은 이 공유기를 중심으로 합니다.
>
> 문서 작성 시점의 펌웨어는 10.06.8 (2018년 7월 26일) 버전입니다. 이 이전의 펌웨어인 경우 펌웨어 업그레이드를 먼저 하시기 바랍니다.
>
> <img src="images/vitalconnect_ko/image7.png" width="450" /><img src="images/vitalconnect_ko/image1.png" width="450" />
>
> 공유기에 대해 무선 설정과 무선 확장 설정이 필요합니다.

### 무선 네트워크 설정 (ipTIME mini 2/3)

> 스마트폰보다는 랩탑의 무선랜을 이용해서 설정하는 것이 간편합니다.
>
> 스마트폰 사용 시에는 Wifi analyzer 류의 앱을 이용하여 와이파이에 접속하면 편리합니다.
>
> 공유기에 전원을 연결하고 랩탑의 무선랜 목록을 열면 iptime_mini 라는 이름의 AP가 보입니다.
>
> “연결” 버튼을 눌러 공유기의 무선랜에 접속합니다. 스마트폰의 경우 데이터 연결을 끄고 진행하는 것이 좋습니다.
>
> <img src="images/vitalconnect_ko/image34.png" width="450" />
>
> 웹브라우저를 열고 주소창에 192.168.0.1 을 입력하여 공유기의 설정 화면으로 들어갑니다.
>
> 사용자 이름의 초기값은 admin 입니다. 초기 암호도 admin 입니다. 캡쳐의 글자를 입력하고 로그인합니다.
>
> <img src="images/vitalconnect_ko/image18.png" width="450" />
>
> Setup 을 눌러 설정 화면으로 갑니다.
>
> <img src="images/vitalconnect_ko/image4.png" width="450" />
>
> 랩탑을 이용하여 접속했을 때 초기 설정 화면입니다.
>
> <img src="images/vitalconnect_ko/image6.png" width="450" />
>
> ‘Wireless Setup’을 클릭하면 다음 화면이 나옵니다.
>
> <img src="images/vitalconnect_ko/image30.png" width="450" />
>
> 기본 무선 네트워크의 설정창이 뜹니다. 여기서 설정할 것은 수술방 내에서 사용할 무선네트워크입니다.
>
> 아래와 같이 네트워크 이름과 암호를 설정합니다. 아래는네트워크 이름을 vital_d5, 암호를 111111111 로 설정하였습니다.
>
> SSID 아래의 ‘이름 알림’ 옵션을 선택합니다. 암호화 옵션은 WPA2PSK+AES(권장)’을 선택합니다. 설정이 끝나면 오른쪽 아래의 “Apply” 버튼을 누릅니다.
>
> <img src="images/vitalconnect_ko/image23.png" width="450" />
>
> 저장을 하면 자동으로 공유기 접속이 단절됩니다. 이는 공유기의 SSID가 iptime_mini로부터 vital_d5로 변경되었기 때문입니다.

### 무선 확장 설정

> 기존의 무선랜을 이용하여 외부 인터넷으로 연결하고자 할 때 필요합니다.
>
> 데이터 수집 기관 외부에서 웹모니터링을 시행하기 위해 필요한 설정입니다.
>
> 무선랜을 검색하여 vital_d5에 연결합니다. 암호를 물어보면 앞서 설정한 111111111 을 입력합니다. 공유기에 연결은 되고 인터넷은 연결되지 않은 상태가 됩니다.
>
> <img src="images/vitalconnect_ko/image25.png" width="450" />
>
> 다시 웹브라우저를 열고 192.168.0.1 을 입력하여 설정 화면으로 들어갑니다.
>
> Advanced Setup/ Wirelss/ Wireless Multibridge 로 들어갑니다.
>
> <img src="images/vitalconnect_ko/image20.png" width="450" />
>
> Mode에서 ‘WISP’’ 을 선택합니다. (Wireless Internet Service Provider)
>
> <img src="images/vitalconnect_ko/image28.png" width="450" />
>
> “Apply” 버튼 아래의 “AP scan” 버튼을 누릅니다. 외부 인터넷이 되는 SSID (무선AP)를 선택합니다. 만약 인증이 필요한 경우 ‘Encryption’에서 암호를 입력합니다.
>
> <img src="images/vitalconnect_ko/image5.png" width="450" />
>
> “Apply” 버튼을 눌러 변경사항을 모두 적용하고 접속을 중단합니다.

### 유선랜 설정

> ipTIME mini2/3에는 유선랜 포트가 있습니다. 유선 포트의 기본 설정은 WAN으로 되어 있어,
>
> 이를 랜케이블을 이용하여 유선인터넷이 제공되는 포트에 연결시 인터넷을 사용할 수 있게 됩니다.
>
> 그러나 우리는 위에서 WAN을 무선으로 설정했기 때문에 이 포트를 VR 컴퓨터와 연결되는 로컬 유선 네트워크 (유선 LAN)의 포트로 이용할 수 있습니다.
>
> 이 경우 VR 컴퓨터와 무선 공유기 사이의 무선 트래픽을 줄일 수 있게 되어 전체 무선망의 연결이 더욱 원활해 집니다.
>
> 유선 포트를 유선 LAN 포트로 설정하기 위해서 “Advanced Setup/ System/ Misc Setup’ 을 클릭합니다.
>
> <img src="images/vitalconnect_ko/image10.png" width="450" />
>
> “Wired Port Setup”으로 들어갑니다 초기값은 ‘WAN port’입니다. 이를 ‘LAN port’로 변경합니다.
>
> <img src="images/vitalconnect_ko/image39.png" width="450" />
>
> “Apply 버튼을 누르면 장치가 재시작됩니다.
>
> <img src="images/vitalconnect_ko/image19.png" width="450" />
>
> 공유기가 다시 켜지면 다음과 같은 Status Summary를 확인할 수 있습니다.
>
> <img src="images/vitalconnect_ko/image31.png" width="450" />
>
> 공유기의 유선 포트와 VR 컴퓨터의 유선 포트를 다이렉트 랜선으로 연결합니다.
>
> VR 컴퓨터의 무선랜을 사용 안 함으로 설정하고 유선랜을 켭니다.
>
> 컴퓨터를 재부팅합니다.

# Vital Recorder에서 장비 추가하기

> 윈도우 핫스팟 또는 공유기의 무선 AP에 VitalConnect가 성공적으로 연결되면 해당 장비를 Vital Recorder에 추가할 수 있습니다.
>
> 의료 장비와 연결된 VitalConnect에 전원을 공급합니다. VitalConnect의 전면에 파란 불이 켜집니다.
>
> “Add Device” 버튼을 누릅니다.
>
> 왼쪽 컬럼에서 장비 종류를 선택합니다.
>
> 오른쪽 컬럼의 Serial Port 선택 창에서 앞서 설정한 VitalConnect의 Connect ID를 볼 수 있습니다.
>
> <img src="images/vitalconnect_ko/image9.png" width="450" />
>
> Connect ID 이름을 선택하면 장비가 추가됩니다.
>
> <img src="images/vitalconnect_ko/image29.png" width="450" />
>
> vitalconnect 장치가 성공적으로 추가되면 장치의 파란 불이 지속적으로 켜진 상태로부터 약 1초 간격으로 깜박이는 상태로 변합니다.

# 무선 연결: 윈도우 핫스팟을 이용한 연결

> **윈도우 핫스팟을 이용한 연결은 컴퓨터 성능에 따라 불안정할 수 있어 현단계에서 추천하지 않습니다.**
>
> 데이터의 흐름은 다음과 같습니다.
>
> **의료 장비 → VitalConnect → 컴퓨터 무선랜 (핫스팟) → Vital Recorder → 컴퓨터 무선랜 (인터넷)**
>
> 윈도우10의 최신 버전(1609부터 이후 버전. 1803 업데이트를 권장함)에서 이용 가능합니다.
>
> 컴퓨터에 무선랜이 장착되어 있어야 합니다.
>
> 랩탑의 경우 자체 무선랜을 사용할 수 있고 데스크탑의 경우 USB 무선랜 또는 무선랜 카드의 추가 장착이 필요합니다.
>
> 알림 창(우측 하단 구석)을 클릭하고 모바일 핫스팟 버튼에서 마우스우클릭하여 ‘설정으로 이동’ 합니다.
>
> <img src="images/vitalconnect_ko/image36.png" width="450" />
>
> 모바일 핫스팟에서 ‘다른 디바이스와 인터넷 연결 공유’를 켭니다. 내 인터넷 연결 공유는 ‘Wi-Fi’로 합니다. 내 인터넷 연결 공유 항목에서 “편집”을 누릅니다.
>
> <img src="images/vitalconnect_ko/image35.png" width="450" />
>
> 네트워크 이름, 암호에 VitalConnect 장치가 연결될 SSID와 암호를 입력하고 저장합니다.
>
> 단, VitalConnect 장치 설정 시 핫스팟에 접속하기 위한 동일한 정보가 입력되어 있어야 합니다.
>
> <img src="images/vitalconnect_ko/image21.png" width="450" />
>
> 의료 장비와 연결된 VitalConnect에 전원을 공급합니다. VitalConnect의 전면에 파란 불이 켜집니다.
>
> 곧이어 VitalConnect가 핫스팟에 연결되고 알림창에 핫스팟 이름과 연결된 장비의 갯수가 표시됩니다. 최대 8개까지 연결할 수 있습니다.
>
> <img src="images/vitalconnect_ko/image33.png" width="450" />

## 핫스팟을 안정적으로 운용하기

> 핫스팟에 VitalConnect가 연결되지 않은 경우에 컴퓨터에서는 자동으로 핫스팟을 중단합니다. 다음 과정을 통해 핫스팟이 저절로 꺼지지 않도록 합니다.
>
> 설정의 모바일 핫스팟으로 들어가서 중간의 관련설정 부분을 봅니다. “어댑터 옵션 변경”을 클릭합니다.
>
> <img src="images/vitalconnect_ko/image38.png" width="450" />
>
> “로컬 영역 연결*숫자”로 표시된 아이콘을 마우스 우클릭하여 “속성”을 선택합니다.
>
> <img src="images/vitalconnect_ko/image27.png" width="450" />
>
> “구성(C)”을 클릭합니다.
>
> <img src="images/vitalconnect_ko/image32.png" width="450" />
>
> 마지막 탭(전원관리)을 선택합니다.
>
> <img src="images/vitalconnect_ko/image37.png" width="450" />
>
> “전원을 절약하기 위해…”의 체크를 해제하고 확인을 누릅니다.
>
> <img src="images/vitalconnect_ko/image15.png" width="450" />

## 주의사항

1.  윈도우 자체의 핫스팟이 아직 충분히 안정적이지 않아 보입니다. (현재 1803 버전)

> 핫스팟이 저절로 끊어지는 경우도 있으니 주의해서 관리하시기 바랍니다.

2.  랩탑의 내장 무선랜을 이용하여 윈도우 핫스팟 사용시 데이터 전송이 자주 끊긴다면,

> USB 무선랜을 추가로 장착하여 이용해 보시기 바랍니다.

3.  모든 장비를 무선 연결하는 것은 권장하지 않습니다.

> vitalconnect 간에 무선 간섭이 생길 수도 있고 vitalconnect 전체의 데이터전송량이 무선망의 bandwidth를 넘어서는 경우 데이터의 누락이 생길 수도 있습니다.

4.  vitalconnect 이용시 권장하는 세팅은, Vital Recorder가 설치된 컴퓨터에서 수 미터 이상 떨어져 있는 장비 중 다른 장소로의 이동이 없는 장비에 한정해서 vitalconnect를 이용하고,

> 이동이 잦은 장비의 경우는 데이터가 다른 환자의 Vital Recorder로 전송될 우려가 있으므로 유선연결을 하는 것입니다.
>
> 이 경우 비어있는 시리얼 포트에 미리 장비명을 할당하고, 이동 장비를 사용시 직접 연결을 하면 즉시 데이터를 수집할 수 있게 됩니다.

<img src="images/vitalconnect_ko/image40.jpg" width="450" />
