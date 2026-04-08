# 시작

> 본 가이드 문서는 수술장/중환자실/응급실 등에서 환자 모니터로부터 생체 신호 데이터를 수집하여 연구를 진행하고자 하는
>
> 임상연구자들에게 Vital Recorder를 이용한 생체 신호 데이터 수집 방법을 안내하고자 만들어졌습니다.
>
> 본 문서를 따라 Vital Recorder를 빠르게 설치하고 데이터를 수집해 볼 수 있습니다
>
> .

##  준비물

- Vital Recorder를 실행할 수 있는 윈도우 호환 PC

- USB to Serial Converter (1포트, 2포트, 4포트 등): 한 쪽은 시리얼 단자, 반대쪽은 USB 단자로 되어 있는 변환기입니다.

> 근래의 컴퓨터들은 시리얼 단자가 없는 경우가 많으므로 의료 장비의 시리얼 단자로부터 신호를 받아 컴퓨터의 USB 단자로 입력해 주기 위한 변환기가 필요합니다.

- 크로스 젠더 (일부 장비에서 필요함): 일부 장비에서는 시리얼 단자의 핀 연결이 달라 cross connection이 필요합니다.

> 크로스 젠더가 필요한 장비들은 “장비 연결 방법” 문서에 표시되어 있습니다.

##  시리얼 케이블의 종류

> Vital recorder는 시리얼 통신을 하는 의료 장비들로부터만 데이터를 취득할 수 있습니다.
>
> 일반적으로 시리얼 통신은 DB9라고 불리는 9핀 커넥터를 사용합니다.
>
> DB9 커넥터는 단자의 모양에 따라 male, female 단자로 구분되고 또한 핀 연결 방법에 따라 direct, cross (또는 null modem) 방식으로 구분됩니다.
>
> 의료 장비에 따라 맞는 단자 모양과 핀 연결을 사용하여야만 합니다.
>
> 의료 장비 종류에 따라 필요한 케이블 혹은 젠더의 예는 다음과 같습니다.

<table style="width:75%;">
<thead>
<tr>
<th style="text-align: center;"><p><strong>장비쪽</strong></p>
<p><strong>커텍터</strong></p></th>
<th style="text-align: center;"><strong>연결 방식</strong></th>
<th style="text-align: center;"><p><strong>PC 쪽</strong></p>
<p><strong>커텍터</strong></p></th>
<th style="text-align: center;"><strong>Device port</strong></th>
<th style="text-align: center;"><strong>장비 종류</strong></th>
</tr>
<tr>
<th style="text-align: center;">Female</th>
<th style="text-align: center;">Direct</th>
<th style="text-align: center;">Male</th>
<th style="text-align: center;">불필요. USB Serial Converter를 직접 연결</th>
<th style="text-align: center;">GE, BIS</th>
</tr>
<tr>
<th style="text-align: center;">Female</th>
<th style="text-align: center;">Cross</th>
<th style="text-align: center;">Male</th>
<th style="text-align: center;"><p>F-M 널모뎀</p>
<p><img src="images/getting_started_ko/image5.png" width="450" /><img src="images/getting_started_ko/image2.png" width="450" /></p>
<p>주황색으로 반드시 “NULL MODEM”</p>
<p>이라고 쓰여있음</p></th>
<th style="text-align: center;">Orchestra</th>
</tr>
<tr>
<th style="text-align: center;">Male</th>
<th style="text-align: center;">Direct</th>
<th style="text-align: center;">Male</th>
<th style="text-align: center;"><p>F-F 젠더 체인처</p>
<p><img src="images/getting_started_ko/image7.png" width="450" /><img src="images/getting_started_ko/image7.png" width="450" /></p>
<p>노란색으로 “NULL MODEM” 이라고 안 쓰여있고 “gender changer” 혹은 “US Patent” 라고 쓰여있음</p></th>
<th style="text-align: center;">없음</th>
</tr>
<tr>
<th style="text-align: center;">Male</th>
<th style="text-align: center;">Cross</th>
<th style="text-align: center;">Male</th>
<th style="text-align: center;"><p>F-F 널모뎀</p>
<p><img src="images/getting_started_ko/image5.png" width="450" /><img src="images/getting_started_ko/image5.png" width="450" /></p>
<p>주황색으로 반드시 NULL MODEM</p>
<p>이라고 쓰여있음</p>
<p>없을 경우 F-M 널모뎀 뒤에</p>
<p>F-F 널모뎀을 끼워도 됨</p></th>
<th style="text-align: center;"><p>Invos, Edwards 장비들,</p>
<p>필립스 MP400-500 모니터,</p>
<p>CardioQ,</p>
<p>FMS2000</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 윈도우 설정

## 절전 모드 끄기

> 데이터 기록 중 윈도우가 절전 모드로 들어가 기록이 중단되는 것을 방지하기 위해 설정 > 시스템 > 전원 및 절전 탭 에서 아래와 같이 화면 끄기와 절전 모드 사용을 “없음”으로 설정합니다.
>
> <img src="images/getting_started_ko/image6.png" width="450" />

## 윈도우 자동 업데이트 방지

> 윈도우 자동 업데이트에 의해 Vital Recorder 프로그램의 사용이 중단될 수 있습니다.
>
> 다음과 같은 프로그램을 사용하여 윈도우 자동 업데이트를 강제로 중단시킬 수 있습니다.
>
> [http://greatis.com/blog/stopupdates10](http://greatis.com/blog/stopupdates10)
>
> 윈도우 자동 업데이트를 중단하더라도 데이터 기록 사이의 시간에 주기적인 수동 업데이트를 통해 윈도우 보안을 유지하시길 권장합니다.

## 로그인 시 암호 입력을 하지 않도록 설정

> 윈도우 시작 버튼을 오른쪽 클릭하고 실행(R)을 누르거나 윈도우키+R 을 눌러 실행 창을 띄웁니다.
>
> “control userpasswords2” 라고 입력합니다.
>
> <img src="images/getting_started_ko/image9.png" width="450" />
>
> 사용자 이름과 암호를 입력해야 이 컴퓨터를 사용할 수 있음(E) 옵션을 해제합니다. 확인을 클릭하면 현재 암호를 한번 입력해야할 수 있습니다.
>
> <img src="images/getting_started_ko/image3.png" width="450" />

# Vital Recorder 설정

## Vital Recorder 설치

> [https://vitaldb.net](http://vitaldb.net) 에서 최신 버전의 vital recorder를 다운로드 받아 컴퓨터에 설치합니다.

## Vital 파일 저장 경로 설정

> Vital 파일을 저장할 폴더를 생성하고 Vital Recorder의 설정에서 지정해 줍니다. 아래에서는 “C:\vital” 경로를 사용하였습니다.
>
> <img src="images/getting_started_ko/image8.png" width="450" />

##

## RPM (Remote Patient Monitoring) 설정

> Vital Recorder의 실시간 모니터링 기능을 이용하여 원격지에서 데이터 수집을 감시할 수 있습니다.
>
> 이를 위해서는 컴퓨터가 인터넷에 연결되어야 합니다.
>
> Vital Recorder의 Settings 메뉴에서 Management 메뉴에 있는 VR code를 복사합니다.
>
> <img src="images/getting_started_ko/image1.png" width="450" />
>
> vitaldb.net에 본인 계정으로 로그인하고 [http://vitaldb.net/web-monitoring/](http://vitaldb.net/web-monitoring/) 에서 VR Code 란에 복사한 코드를 등록합니다.

<img src="images/getting_started_ko/image11.png" width="450" />

# 데이터 백업

> Vital Recorder는 프로그램이 설치된 컴퓨터의 로컬 저장소(HDD, SSD)에 데이터를 저장합니다.
>
> 하지만 개인 또는 상용 클라우드를 이용하여 데이터를 백업함으로써 안정성을 유지할 수 있습니다.
>
> 개인 NAS (Network Attached Storage)의 양방향 싱크 기능을 이용하여 클라우드로의 데이터 백업과 로컬 컴퓨터에서의 주기적인 데이터 삭제를 하는 것을 권합니다.
>
> 아래는 개인 NAS의 대표적인 장비인 Synology를 사용한 예입니다.

## 동기화 프로그램을 이용한 연동 설정

> 시놀로지 NAS와 로컬 저장소와의 데이터 동기화를 위해서 cloud station drive를 설치합니다.
>
> [https://global.download.synology.com/download/Tools/CloudStationDrive/4.2.7-4415/Windows/Installer/Synology%20Cloud%20Station%20Drive-4.2.7-4415.msi](https://global.download.synology.com/download/Tools/CloudStationDrive/4.2.7-4415/Windows/Installer/Synology%20Cloud%20Station%20Drive-4.2.7-4415.msi)
>
> 자세한 사용법은 Synology 홈페이지를 참조하시기 바랍니다.

## 연구자 컴퓨터에서의 전체 파일 관리

> 동기화된 NAS의 폴더는 다시 연구자 컴퓨터와 동기화될 수 있습니다.
>
> 연구용 컴퓨터에 cloud station drive를 설치한 후 NAS의 데이터 업로드 폴더와 양방향 동기화시킵니다.
>
> 이제 연구자의 폴더에서 동기화 폴더의 파일들을 삭제하면 NAS와 Vital Recorder가 설치된 모든 컴퓨터의 로컬 저장소에서도 동시에 삭제가 됩니다.
>
> 모든 저장소들의 저장 공간을 계산하며 주기적으로 백업과 삭제를 반복할 필요가 있습니다.

## Hyper Backup을 이용한 자동 백업 및 버저닝

> 시놀로지의 Hyper Backup 패키지를 이용하면 실수로 데이터를 삭제하거나 덮어씌우더라도 원하는 이전 시점으로 데이터를 복구할 수 있습니다.
>
> 하이퍼 백업에 대해 자세히 알아보시려면 아래 링크를 참고하십시오.
>
> [https://www.synology.com/ko-kr/knowledgebase/DSM/tutorial/Backup_Restore/How_to_back_up_your_data_to_a_remote_Synology_NAS_or_file_server_with_Hyper_Backup](https://www.synology.com/ko-kr/knowledgebase/DSM/tutorial/Backup_Restore/How_to_back_up_your_data_to_a_remote_Synology_NAS_or_file_server_with_Hyper_Backup)

# 수집한 데이터를 이용한 연구

> Vital Recorder를 통해 자동적으로 수집된 생체 신호 데이터는 case 단위의 파일(*.vital)로 저장됩니다.

##

## 환자 정보 요약 파일 만들기

> Vital Recorder는 어떠한 개인 정보도 취급하지 않으므로 vital 파일에 대응하는 환자 정보와의 매칭이 필요합니다.
>
> 엑셀 혹은 구글 스프래드쉬트를 이용하여 각 환자의 병록번호와 관련 임상 정보를 레지스트리화 하고 각 환자의 케이스 파일명 (*.vital)을 함께 기록하도록 합니다.

<img src="images/getting_started_ko/image4.png" width="450" />

##

## 데이터 일괄 추출

> Vital Recorder와 함께 배포되는 Vital Utility 프로그램을 이용하면 특정 폴더 내의 Vital 파일로부터 원하는 트랙을 원하는 해상도로 일괄 추출할 수 있습니다.
>
> 추출된 파일은 csv 포맷으로 SPSS, R, 엑셀 등의 분석 프로그램에서 로딩할 수 있습니다.

<img src="images/getting_started_ko/image10.png" width="450" />

#

# 프로그래밍 언어를 이용하여 데이터 일괄 처리

> 여러 vital 파일들로부터 데이터를 읽거나 일괄 추출하여 처리하기 위해서는 프로그래밍 언어를 이용해야 합니다.
>
> Vital Recorder와 함께 설치되는 유틸리티들을 이용하여 이를 시행할 수 있습니다.
>
> 예를 들면 vital_recs.exe는 데이터의 일괄 추출을 위한 유틸리티 프로그램입니다.
>
> 이를 이용하면 vital 파일로부터 샘플을 추출하는 작업을 자신에게 익숙한 각종 프로그래밍 언어에서 할 수 있습니다.

## Python 으로 vital 파일 열기

> import csv
>
> import subprocess
>
> ipath = "1.vital"
>
> interval = 1
>
> p = subprocess.Popen('**vital_recs.exe** -h "{}" {}'.format(ipath, interval), stdout=subprocess.PIPE)
>
> output = p.communicate()[0].decode("utf-8")
>
> for row in csv.reader(output.splitlines()):
>
> print(row)

## Python 과 Pandas 라이브러리를 이용하여 vital 파일 열기

> import io
>
> import subprocess
>
> import pandas as pd
>
> ipath = "1.vital"
>
> interval = 1
>
> p = subprocess.Popen('**vital_recs.exe** -h "{}" {}'.format(ipath, interval), stdout=subprocess.PIPE)
>
> df = pd.read_csv(io.StringIO(p.stdout.read().decode('utf-8')), index_col=0)
>
> print(df)

##

## Python과 Pandas로 특정 폴더의 vital 파일 트랙 추출하기

> import io
>
> import os
>
> import csv
>
> import subprocess
>
> import pandas as pd
>
> rootdir = r"//Vitalnew/vital_data/Monthly_Confirmed/SNUH_OR"
>
> for dir, dirs, files in os.walk(rootdir):
>
> for file in files:
>
> ipath = '{}/{}'.format(dir, file)
>
> cmd = '**vital_trks** {}'.format(ipath)
>
> p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
>
> df = pd.read_csv(io.StringIO(p.stdout.read().decode('utf-8')), comment='#')
>
> devs = []
>
> for index, row in df.iterrows():
>
> if row['tname'] != 'SV':
>
> continue
>
> devs.append(row['dname'])
>
> if not devs:
>
> continue
>
> print('{},{}'.format(ipath[len(rootdir)+1:], ','.join(devs)))

##

## R 로 vital 파일 열기

> load_vital <- function (path, interval=1) {
>
> cmd <- paste0("**vital_recs.exe** -h ", path, " ", interval)
>
> return (read.csv(pipe(cmd)))
>
> }
>
> \# load vital file and get samples at 1 sec interval
>
> vit <- load_vital("1.vital", 1)
>
> \# print maximum arterial pressure
>
> print(max(vit$SNUADC.ART1, na.rm=TRUE))

#

# 마치며

> 이 글을 통해 생체 신호 데이터 수집 및 연구를 시작하게 된 것을 축하드립니다.
>
> 수집된 데이터를 다른 연구자들과의 협동 연구에도 이용해 보시기 바랍니다.
