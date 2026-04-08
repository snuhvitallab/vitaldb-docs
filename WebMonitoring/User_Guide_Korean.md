# Web monitoring 이란?

<img src="images/user_guide_ko/image23.png" width="450" />

> Vital Recorder를 통해 데이터가 수집되는 동안 장비의 연결 및 수집 상태를 원격에서 감시할 수 있습니다.
>
> 이는 Vital Recorder에 의해 수집된 데이터가 서버로 업로드되고 이를 사용자의 웹브라우저로 전달하는 과정을 통해 이루어집니다.
>
> 데이터의 흐름도는 다음과 같습니다.
>
> **의료 장비 → Vital Recorder → 인터넷 → 데이터 서버→ 인터넷 → 사용자 웹 브라우저**
>
> 이때 Vital Recorder가 설치된 컴퓨터와 웹브라우저가 설치된 컴퓨터 모두 인터넷에 연결되어 있어야 합니다.
>
> 웹모니터링을 위해서는 데이터가 데이터 수집 기관 밖으로 이동하게 되므로 국가 또는 지역에 따라서 법률이나 규정에 의해 사용이 제한될 수 있습니다.
>
> 따라서 웹모니터링은 연구용으로 이용하실 것을 권합니다.
>
> 데이터는 서버에 12시간 동안 임시로 보관된 후 영구히 삭제됩니다.
>
> 연구용 데이터의 기록 및 보관은 로컬 저장소를 이용하시기 바랍니다.

## 필요한 준비물

> Vital Recorder를 실행할 수 있는 PC: 데이터 업로드를 하기 위해서는 Vital Recorder가 설치되고 인터넷 이용이 가능한 컴퓨터가 필요합니다.
>
> 웹 브라우저: 크롬, 파이어폭스, 엣지, 크로미움 브라우저 사용을 권장합니다. 또한 모바일 웹브라우저도 지원합니다.

# 웹 모니터링 시작하기

## Vital Recorder 설정

<img src="images/user_guide_ko/image4.png" width="450" />

> Vital Recorder 상단에 톱니바퀴로된 설정 버튼을 눌러 위의 그림과 같은 Settings 창을 열어줍니다.
>
> Management 섹션에서 “Enable Web Monitoring”을 선택합니다.
>
> VR code는 9자리의 임의의 숫자와 문자로 된 코드입니다. 이를 기록해 두거나 “Copy code” 버튼을 눌러 메모리에 복사해 둡니다.
>
> “OK” 버튼을 누르고 설정창을 빠져 나옵니다.

## 웹 브라우저 설정

> 웹 브라우저를 통한 원격 모니터링을 하기 위해서는 VitalDB 에 회원 가입이 되어 있어야 합니다.
>
> 아직 가입을 안 하셨다면 다음 링크를 눌러 약관에 동의한 후에 회원 가입을 완료하시기 바랍니다.
>
> [https://vitaldb.net/registration-agreement](https://vitaldb.net/registration-agreement)
>
> 로그인을 한 후 Web monitoring 페이지로 갑니다.
>
> [https://vitaldb.net/web-monitoring/](https://vitaldb.net/web-monitoring/#)

<img src="images/user_guide_ko/image6.png" width="450" />

> 하단의 “Register VR Code” 버튼을 누릅니다.
>
> 팝업창에 미리 복사해 둔 코드를 입력하고 “Register” 버튼을 누릅니다.

<img src="images/user_guide_ko/image5.png" width="450" />

> 해당 Vital Recorder에 생체신호가 녹화되는 중이라면 즉시 웹모니터링 화면이 나타납니다. 데이터의 표시는 업로드, 다운로드 시간 때문에 최대 5초까지 지연될 수 있습니다.

<img src="images/user_guide_ko/image17.png" width="450" />

> 여러 방을 모니터링 하는 경우는 다음 이미지와 같이 계속 방을 추가할 수 있습니다.

<img src="images/user_guide_ko/image8.png" width="450" />

# 웹 모니터링의 여러가지 기능

## 페이지 설정

> 웹 모니터링 페이지에는 다양한 설정 옵션과 실시간 통계 기능이 있습니다.
>
> 우선 페이지 상단 메뉴부터 살펴보겠습니다.

<img src="images/user_guide_ko/image2.png" width="450" />

> <img src="images/user_guide_ko/image26.png" width="450" />그룹 버튼을 클릭하면 현재 그룹 목록이 나옵니다. 필터링할 그룹을 선택하면 페이지에 해당 그룹의 베드들만 보이게 되며 그룹 이름을 편집할 수 있습니다.
>
> <img src="images/user_guide_ko/image3.png" width="450" />버튼을 클릭하면 환자와 연결된 베드들만 보이게 됩니다. 그리고 “4/129 beds” 통계는 실시간으로 환자와 연결되어 있는 베드의 수와 현재 선택된 그룹에 속한 총 베드의 수를 나타냅니다.
>
> <img src="images/user_guide_ko/image15.png" width="450" />버튼은 모든 VR을 관리할 수 있는 Manage VR 페이지를 좌측에 열어줍니다. Manage VR에 있는 기능들은 다음 섹션에서 다루겠습니다.
>
> <img src="images/user_guide_ko/image9.png" width="450" />은 한 줄에 표시되는 베드의 수를 선택할 수 있는 옵션입니다. 예를들어, 5를 선택하면 다음 이미지와 같이 한 줄에 5개의 베드가 나열됩니다.
>
> <img src="images/user_guide_ko/image20.png" width="450" />
>
> <img src="images/user_guide_ko/image1.png" width="450" />버튼은 새로고침 기능을 합니다.
>
> <img src="images/user_guide_ko/image10.png" width="450" /> 확장 버튼으로, 선택될 경우 상단의 홈페이지 메뉴가 사라지며 다음 이미지와 같이 전체화면 모드가 됩니다.
>
> <img src="images/user_guide_ko/image19.png" width="450" />

##

##  **Manage VR**

<img src="images/user_guide_ko/image11.jpg" width="450" />

> 웹모니터링 페이지에서 <img src="images/user_guide_ko/image15.png" width="450" />버튼을 클릭하면 위의 사진과 같이 페이지 좌측에 Manage VR이 열립니다.
>
> Manage VR에선 사용자가 등록한 모든 VR을 관리할 수 있습니다.
>
> 베드 별로 그룹 지정을 해놨다면 Manage VR 상단에서 그룹을 선택하여 그룹 별 VR 리스트를 볼 수 있습니다.
>
> 상단 우측의 + VR 버튼으로 VR을 등록 할 수 있습니다.
>
> VR 행은 사진에서처럼 회색으로 되어있습니다. 좌측에 여러 VR을 선택할 수 있는 체크박스와 우측에 공유 버튼과 VR 삭제 버튼이 있습니다.
>
> 체크박스로 여러 VR을 선택해 상단에 있는 “Issue Access Code” 버튼을 클릭하면 선택된 VR의 모니터뷰를 볼 수 있는 임시 코드가 주어집니다.
>
> 아래 그림과 같이 로그인을 하지 않아도 웹모니터링 페이지에서 access code 입력 칸에 임시코드를 입력하면 선택된 VR 모니터뷰를 볼 수 있습니다.
>
> <img src="images/user_guide_ko/image22.png" width="450" />
>
> 공유 버튼으로 다른 사용자에게 해당 VR의 모니터뷰나 녹화된 vital 파일을 공유할 수 있습니다.
>
> VR 삭제 버튼으로 해당 VR을 삭제할 수 있습니다.
>
> VR 행 밑에 <img src="images/user_guide_ko/image14.png" width="450" />표시가 되어있는 줄은 해당 VR을 보고있는 사용자 리스트 입니다. 각 사용자의 권한을 알 수 있고 삭제 및 변경도 할 수 있습니다.

## 베드별 설정

<img src="images/user_guide_ko/image24.png" width="450" />

> 베드별 설정 메뉴는 해당 베드을 우클릭하면 열리고, 다른 곳을 클릭하면 사라집니다.
>
> Upgrade VR은 Vital Recorder의 Settings 창에서 “Enable web configuration”을 체크해야 사용할 수 있는 기능으로 원격으로 Vital Recorder 업데이트합니다.
>
> Change Permission은 해당 베드 웹모니터링의 보기 권한이나 생체신호파일 다운로드 권한을 다른 사용자에게 부여하거나 부여한 권한을 편집, 삭제 관리하는 기능을 합니다.
>
> Delete VR는 해당 베드를 삭제합니다.
>
> Vital Recorder 1.8.8.9 이상버전의 경우, Patient Information은 환자의 나이, 성별, 무게, 키 등 환자정보를 입력합니다.
>
> 환자정보를 입력하면 Stroke Volume (Filter Settings에서 선택) 계산 알고리즘의 정확도를 올려줍니다.

<img src="images/user_guide_ko/image13.png" width="450" />

> Device Settings에서 해당 VR의 기기 목록을 원격으로 편집할 수 있습니다. (Vital Recorder 1.8.8.9 이상)
>
> <img src="images/user_guide_ko/image7.png" width="450" />
>
> (Vital Recorder 1.8.8.9 이상) Filter Settings에서 해당 VR의 필터 목록을 원격으로 편집할 수 있습니다.
>
> <img src="images/user_guide_ko/image21.png" width="450" />
>
> Alarm Settings는 모니터의 실시간 상황을 텔레그램 알림으로 받을 수 있는 설정입니다.
>
> 처음 알림 기능 사용 시 텔레그램 Chat ID를 VitalDB 계정에 등록하기 위한 가이드가 나옵니다.
>
> 가이드에 따라 Chat ID를 등록하면 텔레그램을 통해 해당 모니터에 대한 알림을 받아볼 수 있습니다.
>
> Chat ID 변경은 Manage My Account에서 할 수 있습니다.
>
> <img src="images/user_guide_ko/image16.png" width="450" />
>
> Restart VR, Reboot는 Vital Recorder의 Settings 창에서 “Enable web configuration”을 체크해야 사용할 수 있는 기능으로 각각 VR 업데이트, VR 재시작, PC 재부팅의 기능을 합니다.

## 베드선택 메뉴

<img src="images/user_guide_ko/image18.png" width="450" />

> 여러개의 모니터를 선택해서 한 번에 관리가 가능합니다.
>
> 위의 그림과 같이 모니터를 클릭하면 선택되고 상단 메뉴에 Check All과 Actions 버튼이 나옵니다.
>
> Check All 버튼을 클릭하면 화면에 보이는 모든 모니터 전체선택/선택해제가 됩니다.
>
> Actions는 드롭다운 메뉴로 Share VR로 선택된 모니터의 보기 권한이나 생체신호파일 다운로드 권한을 다른 사용자에게 부여할 수 있습니다.
>
> Change Group로 선택된 모니터들의 그룹 지정을 할 수 있습니다. Delete VR로 선택한 모니터들을 한 번에 삭제할 수 있습니다.
>
> Update VR, Restart VR, Reboot는 Vital Recorder의 Settings 창에서 “Enable web configuration”을 체크해야 사용할 수 있는 기능으로 각각 선택한 모니터들을 VR 업데이트, VR 재시작, PC 재부팅 합니다.

## 화면 확대

> 특정한 베드의 모니터를 확대해서 볼 경우나 12시간 이내의 Vital Recorder 기록을 열람해야 할 경우, 화면 확대 기능을 사용해야 합니다.
>
> 확대 기능을 사용하기 위해서는 해당 방의 모니터화면을 더블클릭하면 됩니다.
>
> ESC 키나 화면 더블 클릭을 통해 원래의 모니터링 화면으로 돌아갈 수 있습니다.

<img src="images/user_guide_ko/image27.png" width="450" />

> 화면 확대 시, 상단 이미지와 같은 화면이 열립니다.
>
> 상단 중앙에는 현재 케이스의 데이터 기록 시간이 붉은 글씨로 표시됩니다. 아래의 예에서는 21분 5초의 기록이 이루어진 상태입니다.
>
> 하단의 슬라이더는 지금으로부터 4시간 전까지 원하는 시간으로 이동할 수 있도록 도와줍니다.
>
> 우측 하단의 이동 버튼을 통해 7초씩 움직일 수 있습니다.
>
> <img src="images/user_guide_ko/image25.png" width="450" />버튼을 통해 해당 수술의 시작시간으로 움직일 수 있습니다.
>
> 시간 이동 시, 좌측 하단의 멈춤 버튼이 재생 버튼으로 변하는데, 이 때 재생 버튼을 누르면 해당 시간의 기록을 재생시킬 수 있습니다.
>
> <img src="images/user_guide_ko/image12.png" width="450" />버튼을 통해 실시간 모니터링으로 돌아갈 수 있습니다.
