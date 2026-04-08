# Introduction

바이탈서버(Vitalserver)는 기존에 클라우드에서 제공되던 [VitalDB](https://vitaldb.net) 서버 기능을 병원의 내부망에서 이용 가능하도록 개발되었습니다. 본 매뉴얼은 관리자와 사용자들에게 바이탈 서버 설정 및 실행 방법 그리고 사용 방법을 설명합니다.

참고: 본 가이드의 설명은 2023-01-04 버전을 기준으로 합니다.

# Installation

* 서울대병원 연구팀이 기관을 직접 방문하여 설치 및 설정했다면 이 섹션을 건너뛰셔도 됩니다.

1.  [https://vitaldb.net/vitalserver.php](https://vitaldb.net/vitalserver.php)에서 vitalserver.zip을 다운받은 후 C 드라이브에 vitalserver.zip 압축을 풀어줍니다.

2.  C:/vitalserver/service/include/config.js 우클릭 > 편집을 클릭합니다.

3.  const file_folder = “바이탈 파일 저장 경로" 를 입력합니다. **바이탈 파일을 NAS에 저장할 경우** 다음 링크를 참고해주십시오. [로컬 네트워크 내에서 Windows PC의 파일을 Synology NAS에 어떻게 저장합니까?](https://kb.synology.com/ko-kr/DSM/tutorial/How_to_map_shared_folder_Windows_PC) NAS 공유드라이브 예) const file_folder = “Z:/”

4.  C:/vitalserver 에 있는 server_start.bat 을 더블클릭하여 서버를 실행합니다. 편의를 위해 serverstart.bat을 바탕화면으로 이동하는 것을 권장합니다.

5.  서버 IP와 Port는127.0.0.1:80으로 설정되어있습니다. 서버 정보 변경은 아래 Server Configuration의 [Server IP Setting](#server-ip-setting) 섹션을 참고해 주십시오.

# Server Configuration

서버 설정을 위해 바이탈 서버에 어드민 계정으로 로그인합니다.

1.  서버를 설치한 PC에서 웹브라우저를 엽니다.

2.  주소창에 “localhost” 입력 후 Enter키를 눌러 바이탈 서버 접속합니다.

3.  ID: admin, PW: admin 으로 어드민 계정으로 로그인합니다. 어드민 비밀번호 변경은 아래 User Profile을 참고해 주십시오.

4.  바이탈 서버 > Manage 에서 서버 설정을 변경합니다.

> <img src="images/user_manual_ko/image9.png" width="450" />

<img src="images/user_manual_ko/image5.png" width="450" />

## Server IP Setting

Server IP 기본값은 127.0.0.1 이므로 같은 내부망에 있는 다른 PC로 서버에 접속하기 위해서 서버 PC의 고정 IP 값으로 Server IP를 수정해야합니다. 또한 포트가 기본값인 80 외 다른 값이라면 Server Port 수정 후 Submit 버튼을 눌러 저장합니다.

**서버의 IP 또는 Port 변경 시 서버 PC에 열려있는 cmd 창 종료 후 serverstart.bat으로 서버를 다시 시작해야 변경사항이 적용됩니다.**

## Filter Server IP Setting

웹모니터링에서 필터 기능 사용 시 필요한 설정입니다. VitalRecorder for Windows에 있는 필터와 동일한 기능입니다.

## VitalRecorder(VR) Upgrade

Manage Vital Recorder 버튼은 VR 기기 업그레이드를 위한 기능입니다.

<img src="images/user_manual_ko/image22.png" width="450" />

- 외부망 사용이 가능한 PC로 [VitalRecorder: VitalDB](https://vitaldb.net/vital-recorder/?action=versions)에서 최신 업그레이드 파일을 다운받은 후, 바이탈 서버에 파일을 업로드합니다.

  - Manage Vital Recorder > 파일 선택 > 최신 업그레이드 파일 선택 > Upload 클릭

  - **설치한 운영체제(OS)별로 다운로드 파일이 다르니 꼭 확인부탁드립니다.**<img src="images/user_manual_ko/image16.png" width="450" />

## User Profile

Users에선 유저를 추가 및 삭제할 수 있습니다. 계정을 만들어서 원내망을 사용하고 있는 다른 연구자에게 웹모니터링이나 녹화된 파일을 공유할 수 있습니다. 서버를 중앙모니터로 사용할 경우 병동 또는 로젯 단위로 계정을 만들면 편리합니다.

<img src="images/user_manual_ko/image12.png" width="450" />

- 페이지 우측에서 User ID, Name, Email, Profile 입력 후 Submit을 클릭하면 유저가 추가됩니다.

- **새로운 계정의 패스워드는 User ID와 동일합니다.**

- 페이지 좌측의 유저 리스트에서 체크박스 선택 후 Delete 버튼을 클릭하면 체크된 유저가 삭제됩니다.

## HL7 Settings

EMR 기록을 돕기위한 기능입니다. HL7 기능 사용 문의는 이메일로 부탁드립니다.

# Account Settings

사용자의 개인 정보 수정이 가능합니다.

<img src="images/user_manual_ko/image8.png" width="450" /><img src="images/user_manual_ko/image25.png" width="450" />

본인인증을 위해 Password에 비밀번호 입력 후 Submit 버튼 클릭으로 변경된 정보를 저장합니다.

# Web Monitoring

원내에 설치된 PiVR 또는 VitalRecorder for Windows에서 실시간 중계되는 환자의 생체신호를 볼 수 있습니다. 웹모니터링 페이지 좌측 상단 기능부터 순서대로 설명하겠습니다.

<img src="images/user_manual_ko/image2.png" width="450" />

## Group

<img src="images/user_manual_ko/image20.png" width="450" /><img src="images/user_manual_ko/image1.png" width="450" />

웹모니터링 페이지에서 그룹 버튼을 클릭하면 위와 같이 그룹 목록이 볼 수 있습니다.

- 그룹이 선택되어있지 않은 경우, 그룹 지정이 안된 모니터를 포함한 모든 모니터가 보입니다.

- All을 선택한 경우, 그룹이 지정된 모든 모니터를 볼 수 있습니다.

- 하나 이상의 그룹 선택 시, 선택한 그룹의 모니터가 보입니다.

- 그룹에 마우스 커서를 올리면 상단 좌측 그림과 같이 그룹명 우측에 연필 버튼이 보입니다. 클릭 시, Edit Group Name 창이 뜨며 그룹 이름을 편집할 수 있습니다.

## Manage VR

VR 설정을 일괄 적용할 수 있는 VR 관리 기능입니다. 모든 VR 이름, VR code, OS 등 여러 정보를 한 번에 볼 수 있습니다.

<img src="images/user_manual_ko/image14.png" width="450" />

- 좌측 상단 CCU 라고 적혀있는 칸은 그룹 선택 기능입니다. 그룹별로 VR 기기 목록을 볼 수 있습니다. 그룹 선택 우측에 있는 Add Group으로 새로운 그룹 추가가 가능합니다.

- Actions 메뉴에 있는 기능들은 모두 일괄 적용이 가능합니다. 적용하고자 하는 VR의 체크박스 클릭 후 Actions 메뉴를 선택하면 적용됩니다.

  - Change Group: 선택한 VR의 그룹을 일괄 변경합니다. Add Group 선택 후 새 그룹명을 입력하면, 해당 이름으로 그룹 설정됩니다.

> <img src="images/user_manual_ko/image24.png" width="450" />

- Change Permission: 다른 계정에 권한을 부여하는 기능입니다.

  - View: 웹모니터링 페이지에서 실시간 모니터링을 할 수 있는 권한

  - Download: 모니터에서 녹화된 파일을 My Files에서 조회 및 다운로드할 수 있는 권한

  - Manage: 모니터의 기기설정, 원격 업그레이드, 재시작 등, 원격제어할 수 있는 권한

> <img src="images/user_manual_ko/image21.png" width="450" />

- Filter Settings: 저혈압 예측 등 모니터의 데이터를 이용해서 여러 요소를 예측할 수 있는 기능입니다. Filter 기능을 사용하려면 Filter 서버를 설치해야합니다.

> <img src="images/user_manual_ko/image17.png" width="450" />

- Upgrade VR: VR 기기를 원격으로 업그레이드하는 기능입니다. 위에 [VR Upgrade](#vitalrecordervr-upgrade) 섹션을 참고하여 업그레이드 파일을 서버에 업로드 후 사용해 주십시오.

> <img src="images/user_manual_ko/image4.png" width="450" />

- Delete VR: VR를 서버에서 삭제하는 기능입니다. “delete”를 아래 입력란에 입력해야만 삭제됩니다.

> <img src="images/user_manual_ko/image19.png" width="450" />

## Other Functions

웹모니터링 페이지에서 Group, Manage VR을 제외한 메뉴에 관한 설명입니다. 왼쪽부터 차례대로 설명하겠습니다.

<img src="images/user_manual_ko/image15.png" width="450" /><img src="images/user_manual_ko/image10.png" width="450" />

아래 CCU_1, CCU_2, CCU_3 는 기능 설명을 위한 예제 그림입니다.

<img src="images/user_manual_ko/image7.png" width="450" />

- 환자 유무 필터

  - 클릭 시, 병상에 환자가 있는 모니터만 보입니다. 위의 예제로 보자면 CCU_1만 보이게 됩니다.

- 온/오프라인 필터

  - 한 번 클릭 시, 네트워크에 연결된 모니터만 보입니다. 예) CCU_1, CCU_3

  - 두 번 클릭 시, 네트워크가 끊긴 모니터만 보입니다. 예) CCU_2

  - 위의 예제에서 CCU_2는 네트워크가 끊긴 모니터입니다. CCU_2 옆에 와이파이가 끊겼다는 뜻의 아이콘이 있고 “7d 13h”라고 쓰여 있는데 7일 13시간째 네트워크가 끊겨 있다는 뜻입니다.

  - CCU_3는 네트워크는 연결되어있지만 병상에 환자가 없어 standby 중인 모니터입니다.

- 모니터 칼럼 설정

  - 칼럼 갯수는 1부터 10까지 설정할 수 있습니다.

  - 위에선 3으로 설정되어있으므로 한 줄에 CCU_1, CCU_2, CCU_3 세 개의 모니터가 보입니다.

- 새로고침 버튼: 페이지 새로고침 버튼입니다.

- 전체화면 버튼: 웹 브라우저가 전체화면으로 바뀌고 웹모니터링 페이지 또한 전체화면 모드로 전환됩니다.

## Monitor Menu

<img src="images/user_manual_ko/image3.png" width="450" />

- 모니터에 마우스를 올리면 위 그림 중앙에 표시된 부분과 같이 해당 VR 정보 확인이 가능합니다. 왼쪽부터 순서대로 베드명, VR Code, VitalRecorder 소프트웨어 버전입니다. 마지막으로 모자이크 처리되어 있는 부분은 VR 기기의 IP 주소입니다.

- 위 그림 우측 상단 “+ Add Event” 기능은 녹화 중인 파일에 현재시간으로 이벤트를 추가하는 기능입니다.

모니터를 더블클릭하면 선택된 모니터가 아래 그림과 같이 확대모드로 전환됩니다.

<img src="images/user_manual_ko/image26.png" width="450" />

- 화면 좌측 그래프는 지난 4시간의 트렌드 기록입니다.

- 화면 좌측 하단 컨트롤러로 지난 4시간 가량의 기록을 재생해볼 수 있습니다.

모니터를 우클릭하면 아래와 같이 우클릭 메뉴 목록이 나옵니다.

- Network Settings (*Only available with PiVR)*: PiVR 네트워크 설정 기능<img src="images/user_manual_ko/image23.png" width="450" />

- Device Settings: VR 기기 설정 기능으로 VR과 의료기기를 연결할 때 추가/수정할 수 있는 기능입니다.

- Filter Settings: 저혈압 예측 등 모니터의 데이터를 이용해서 여러 요소를 예측할 수 있는 기능입니다. Filter 기능을 사용하려면 Filter 서버를 설치해야합니다.

- View Logs (*Only available with PiVR)*: PiVR의 로그를 실시간으로 읽어오는 기능입니다. 브라우저의 개발자도구 콘솔에서 로그를 확인할 수 있습니다.

- Change Permission: 해당 모니터에 관한 권한 설정을 편집할 수 있습니다.

- Change Group: 그룹 설정 기능

- Upgrade VR (*Only available with PiVR)*: PiVR 원격 업그레이드 기능

- Delete Bed: VR 삭제

- Restart VR: VR 원격 재시작 기능

- Reboot: VR 기기 전원 원격 재인가 기능

# My Files

원내에 설치된 PiVR 또는 VitalRecorder for Windows에서 녹화되어 서버에 저장된 환자의 생체신호 파일을 조회, 열람, 다운로드할 수 있습니다.

<img src="images/user_manual_ko/image6.png" width="450" />

## Search Files

My Files 페이지에서 위 그림과 같이 여러 조건으로 파일 조회가 가능합니다.

- Start Date, End Date: 파일이 녹화된 날짜 기준으로 파일 조회

- Bed: 베드/수술방 별 파일 조회

- Search Keyword: 파일 이름 기준 조회

- Tracks: 기기/트랙별 파일 조회

## File List

- 파일명, 녹화 시작 시간, 녹화 종료 시간, 파일 업로드된 시간, 파일 사이즈를 확인할 수 있습니다.

- 페이지를 새로고침하면 검색결과가 리셋되고 기본적으로 오늘 날짜로 녹화된 파일 목록이 결과로 나옵니다.

- 예시 그림에서는 2022-12-27에 녹화된 파일 중, 인텔리뷰 기기로부터 ABP, CO2, CVP, ECG_II_WAV, HR 트랙을 취득한 파일을 조회했습니다. 위 그림의 가운데 나온 파일 목록이 조회 결과입니다.

## File View

<img src="images/user_manual_ko/image11.png" width="450" /><img src="images/user_manual_ko/image27.png" width="450" />

- 파일 목록에서 파일명을 클릭하면 My Files 페이지 우측에서 파일 미리보기 기능이 보입니다.

- 파일을 다운로드하지 않아도 전반적인 기록 확인이 가능합니다.

- Track View (좌측 그림) 조작 방법

  - 마우스 스크롤1: 트랙명 위에서 마우스 스크롤 조작 시, 위 아래로 스크롤 이동

  - 마우스 스크롤2: 데이터 화면 위에서 마우스 스크롤 조작 시, 데이터를 확대하거나 축소할 수 있습니다.

  - 마우스 드래그: 좌우로 마우스 드래그 시, 시간을 이동할 수 있습니다.

- Monitor View (우측 그림)

  - 트랙뷰 우측 상단에 Monitor View 버튼 클릭 시 모니터뷰 모드도 전환됩니다.

  - 웹모니터링 페이지의 모니터와 조작법이 같습니다.

# Frequently Asked Questions

## 서버가 실행 중인데 페이지가 브라우저에 안나타납니다. 어떻게 해야하나요?

서버가 실행되고 있는 cmd 프롬프트 창이 여러개 열려있는 것은 아닌지 확인해주십시오.

NAS를 사용하실 경우 아래 두가지가 대표적 원인입니다.

- NAS 전원이 꺼진 경우

  - 아래 그림에 표시된 전원 버튼에서 푸른 불빛이 나오지 않는 다면 전원 버튼을 눌러서 NAS를 켜 줍니다.

> <img src="images/user_manual_ko/image18.png" width="450" />

- 서버 PC와 NAS 연결이 끊긴 경우

  - 아래 예시 좌측에 있는 Y 드라이브는 연결이 끊긴 경우이고, Z 드라이브는 정상적인 드라이브 입니다. 서버 PC > 파일 탐색기 > 내 PC 에서 확인 가능합니다. Y 드라이브와 같이 연결이 끊겨있다면 [Installation](#installation) 3번을 참고해 주십시오.

> <img src="images/user_manual_ko/image13.png" width="450" />

# Contacts

**서버 구입 문의**

한상규 이사 (아이테크) sghan39@naver.com

**개발 및 연구 관련 문의**

이형철 교수 (서울대학교/서울대학교병원) vital@snu.ac.kr

**서버 사용 관련 문의**

이은선 연구원 (서울대학교/서울대학교병원) eunsun.lee93@snu.ac.kr

**PiVR 기기 관련 문의**

심다연 연구원 (서울대학교/서울대학교병원) dayeonsim@snu.ac.kr

# Acknowledgement

바이탈서버의 권리는 서울대학교 산학협력단에 귀속되어 있으며 배포 및 판매의 권리는 아이테크 사에 양도되었습니다.

본 프로그램의 무단 복제 및 배포는 법적 제한을 받습니다.
