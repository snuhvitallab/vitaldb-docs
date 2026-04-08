# Intellivue Settings to Collect Ventilator Data

## 인공호흡기 파라미터가 필립스 Intellivue 모니터로 넘어오도록 설정하는 방법

> Intellivue와 연결된 Ventilator에서 넘어오는 data를 추출하기 위해서는 아래와 같은 설정이 필요합니다.
>
> <img src="images/intellivue_ko/image6.png" width="450" />
>
> Ventilator와 연결되어 있는 IntelliBridge EC10 모듈의 set up 버튼을 누릅니다.
>
> <img src="images/intellivue_ko/image16.png" width="450" />
>
> Setup Ventilator 창이 뜨면 “Device Driver” - “Setup Numerics”를 차례대로 누릅니다.
>
> <img src="images/intellivue_ko/image13.png" width="450" />
>
> 화면 아래 Add 버튼을 누르면 “Choices” 에서 최대 12개 까지 원하는 parameter를 선택할 수 있습니다.
>
> 잘못 선택 시 Delete를 버튼을 눌러 삭제할 수 있습니다.
>
> 흔히 사용되는 설정 및 의미는 아래와 같습니다.
>
> FiO2 : 측정된 FiO2
>
> sFiO2 : 설정된 FiO2
>
> PEEP : 측정된 Positive End Expiratory Pressure
>
> sPEEP : Positive End Expiratory Pressure 설정값
>
> sSIMV : SIMV 모드에서 Respiration Rate 설정값
>
> sCMV : CMV 모드에서 Respiration Rate 설정값
>
> sΔPi-e : Pressure Control 설정값
>
> sΔPEEP : Pressure Support 설정값
>
> IE 1; : IE ratio 중 expiration 파트
>
> RRaw : 측정된 Respiration Rate
>
> PIP : 측정된 Peak Inspiratory Pressure
>
> TV : 측정된 Tidal Volume
>
> MINVOL : 측정된 Minute Volume
>
> 상기 방법을 통해 추가된 Parameter가 화면을 차지하여 디스플레이에 빈 공간이 부족해 문제가 되는 경우가 있습니다.
>
> 예를 들어 PPV 등 추가 파라미터가 모니터에 보이지 않는 경우가 생길 수 있습니다.
>
> 이를 방지하기 위해 데이터는 수집되지만 모니터 화면에는 보이지 않도록 설정을 변경할 수 있습니다.
>
> <img src="images/intellivue_ko/image17.png" width="450" />
>
> 모니터 화면에서 연구용으로만 사용하는 항목을 누른 후 “Setup Spirometer” - “Change Numeric” - “Blank”를 차례로 누릅니다.
>
> Balnk 설정 시, 모니터에는 보이지 않지만 Vital Recorder를 통해 값을 얻을 수 있습니다.
>
> 마지막으로 변경한 설정을 저장하기 위한 설정이 필요합니다.

## 현재 모니터 설정을 기본 프로파일로 저장하는 방법

> <img src="images/intellivue_ko/image10.png" width="450" />
>
> 모니터의 “Main Setup” 버튼을 누른 후 “Operating Modes” - “Config”를 선택합니다.
>
> Password는 “71034”입니다.
>
> 우선, 다른 설정이 함께 저장되는 것을 방지하기 위해 기본 설정값을 불러오는 것이 필요합니다.
>
> <img src="images/intellivue_ko/image14.png" width="450" />
>
> Config 모드에서 “Main setup” - “Profiles” - “Load”를 누릅니다.
>
> <img src="images/intellivue_ko/image2.png" width="450" />
>
> “Please Confirm” 창에서 “Confirm”을 누르면 기본 설정값으로 모니터 셋팅이 됩니다.
>
> 그 다음, 위의 “인공호흡기 파라미터가 필립스 Intellivue 모니터로 넘어오도록 설정하는 방법”을 참고하여 인공호흡기 파라미터를 추가합니다.
>
> <img src="images/intellivue_ko/image9.png" width="450" />
>
> 다시, “Main setup”을 누른 후 “Profiles” - “Save all”를 누릅니다.
>
> <img src="images/intellivue_ko/image18.png" width="450" />
>
> Please Confirm 창에 “Confirm”을 누르면 변경된 설정이 모두 저장됩니다.
>
> <img src="images/intellivue_ko/image4.png" width="450" />
>
> “Config” - “Operating Modes” - “Monitoring” - Please confirm “Confirm”을 순서대로 누르면 config 모드에서 Monitoring로 변경됩니다.

## 인공호흡기에서 airway pressure와 flow wave가 넘어오도록 설정하는 방법

> Intellivue와 연결된 Ventilator에서 넘어오는 wave를 얻기 위해서는 아래와 같은 설정이 필요합니다.
>
> <img src="images/intellivue_ko/image6.png" width="450" />.
>
> Ventilator와 연결되어 있는 IntelliBridge EC10 모듈의 set up 버튼을 누릅니다.
>
> <img src="images/intellivue_ko/image11.png" width="450" />
>
> Setup Ventilator 창이 뜨면 “Device Driver” - “Setup Waves”를 차례대로 누릅니다.
>
> <img src="images/intellivue_ko/image3.png" width="450" />
>
> 화면 아래 Add 버튼을 눌러 “Choices” 창에서 AWP와 AWF를 선택합니다. 선택 후 창을 닫으면 설정이 적용됩니다.
>
> <img src="images/intellivue_ko/image1.png" width="450" />
>
> 위와 같이 Vital Recorder file을 통해 airway pressure와 flow wave data가 수집되는 것을 확인할 수 있습니다.

# Troubleshooting

## Q. 파라미터를 추가 후 PPV 값이 안 나올 때는 어떻게 하나요?

> PPV 값을 디스플레이에 보이도록 하는 설정은 다음과 같습니다.
>
> <img src="images/intellivue_ko/image15.png" width="450" />
>
> 우선, ABP를 누른 후 “Setup ABP” - “PPV” - “Setup PPV” - PPV: On, Measurement: Enabled 설정을 합니다.
>
> <img src="images/intellivue_ko/image8.png" width="450" />
>
> 그 다음, PPV 값을 나타낼 칸을 누르면 “Setup Spirometer” 창이 나타납니다. “Change Numeric” - “PPV”를 차례대로 누릅니다.

## Q. AWP, AWF 추가 설정했는데 웹모니터에 Wave가 보이지 않을 땐 어떻게 하나요?

> intellivue와 연동된 인공호흡기에서 AWF, AWP 설정 후 웹모니터에서 wave가 보이지 않는다면 VR 버전을 확인합니다.
>
> 1.8.17.1 버전부터 AWF, AWP wave 기능이 추가되어 있습니다. 해당 버전이 아닐 경우 VR upgrade를 시행합니다.
>
> <img src="images/intellivue_ko/image5.png" width="450" />
>
> 웹모니터에서 해당 bed 칸에서 우클릭을 누른 후 “Upgrade VR”을 클릭하면 됩니다. 최신 버전으로 VR upgrade 후 자동으로 VR이 재시작이 됩니다.

## Q. 웹모니터에 AWP wave가 이상하게 나올 땐 어떻게 해야 하나요?

> <img src="images/intellivue_ko/image12.png" width="450" />
>
> 위와 같은 AWP wave는 IntelliBridge EC10 wave set up에서 AWP, AWF 설정이 되지 않은 경우입니다.
>
> “인공호흡기에서 airway pressure와 flow wave가 넘어오도록 설정하는 방법”을 참고하여 AWP, AWF wave 설정을 추가합니다.
>
> <img src="images/intellivue_ko/image7.png" width="450" />
>
> AWP, AWF wave 설정이 완료되면 올바른 AWP wave를 확인할 수 있습니다.
