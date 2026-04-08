# Introduction

<img src="images/overview/image1.png" width="450" />

This is a comprehensive dataset of 6,388 surgical patients composed of intraoperative biosignals and clinical information. The biosignal data included in the dataset is high quality data such as 500 Hz waveform signals and numeric values at intervals of 1-7 seconds. More than 60 surgery related clinical information is also provided to help interpret the signals.

The dataset is provided free of charge to help researchers who want to study and develop new medical AI algorithms using monitoring signals from surgical patients. We expect that the distribution of this world's largest biosignal dataset will greatly contribute to the advancement of medical AI research.

If you use the VitalDB open dataset in your research, please cite the following publication:

**Lee HC, Park Y, Yoon SB, Yang SM, Park D, Jung CW. VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients. Sci Data. 2022 Jun 8;9(1):279. doi: 10.1038/s41597-022-01411-5.** PMID: 35676300; PMCID: PMC9178032.

# Dataset Summary

- The data was obtained from non-cardiac (general, thoracic, urologic, and gynaecologic) surgery patients who underwent routine or emergency surgery in 10 out of 31 operating rooms of Seoul National University Hospital, Seoul, Republic of Korea.

- The acquisition and release of the data was approved by the Institutional Review Board of Seoul National University Hospital (H-1408-101-605). The study was also registered at clinicaltrials.gov (NCT02914444).

- Case files were recorded in the form of vital files using Vital Recorder version 1.7.4. Each case file contains high-resolution data with a time resolution of 500 Hz for wave data and 1-7 seconds for numeric data, with an average of 2.8 million data points per case.

- The dataset consists of a total of 557,622 (average 87, range 16-136) data tracks from 6,388 cases. All data tracks in the vital file were extracted, converted to csv, and compressed with gzip.

**Dataset Summary**

<table style="width:98%;">
<thead>
<tr>
<th style="text-align: center;">　</th>
<th style="text-align: center;"><p>General surgery</p>
<p>(n = 4,930)</p></th>
<th style="text-align: center;"><p>Thoracic surgery</p>
<p>(n = 1,111)</p></th>
<th style="text-align: center;"><p>Gynecology</p>
<p>(n = 230)</p></th>
<th style="text-align: center;"><p>Urology</p>
<p>(n = 117)</p></th>
<th style="text-align: center;"><p>Total</p>
<p>(n = 6,388)</p></th>
</tr>
<tr>
<th colspan="6" style="text-align: center;">Demographic</th>
</tr>
<tr>
<th style="text-align: center;">Sex (male)</th>
<th style="text-align: center;">2,524 (51.2%)</th>
<th style="text-align: center;">618 (55.6%)</th>
<th style="text-align: center;">0 (0%)</th>
<th style="text-align: center;">101 (86.3%)</th>
<th style="text-align: center;">3,243 (50.8%)</th>
</tr>
<tr>
<th style="text-align: center;">Age (years)</th>
<th style="text-align: center;">59 (48-68)</th>
<th style="text-align: center;">61 (52-70)</th>
<th style="text-align: center;">45 (35-55)</th>
<th style="text-align: center;">64 (58-72)</th>
<th style="text-align: center;">59 (48-68)</th>
</tr>
<tr>
<th style="text-align: center;">Height (cm)</th>
<th style="text-align: center;">162 (156-169)</th>
<th style="text-align: center;">163 (156-169)</th>
<th style="text-align: center;">159 (155-163)</th>
<th style="text-align: center;">168 (161-173)</th>
<th style="text-align: center;">162 (156-169)</th>
</tr>
<tr>
<th style="text-align: center;">Weight (kg)</th>
<th style="text-align: center;">60 (53-69)</th>
<th style="text-align: center;">61 (54-69)</th>
<th style="text-align: center;">59 (53-66)</th>
<th style="text-align: center;">69 (62-77)</th>
<th style="text-align: center;">61 (53-69)</th>
</tr>
<tr>
<th colspan="6" style="text-align: center;">Surgical approach</th>
</tr>
<tr>
<th style="text-align: center;">Open</th>
<th style="text-align: center;">3,104 (63.0%)</th>
<th style="text-align: center;">190 (17.1%)</th>
<th style="text-align: center;">65 (28.3%)</th>
<th style="text-align: center;">6 (5.1%)</th>
<th style="text-align: center;">3,368 (52.7%)</th>
</tr>
<tr>
<th style="text-align: center;">Videoscopic</th>
<th style="text-align: center;">1,691 (34.2%)</th>
<th style="text-align: center;">889 (80.0%)</th>
<th style="text-align: center;">140 (60.9%)</th>
<th style="text-align: center;">34 (29.1%)</th>
<th style="text-align: center;">2,701 (42.3%)</th>
</tr>
<tr>
<th style="text-align: center;">Robotic</th>
<th style="text-align: center;">135 (2.7%)</th>
<th style="text-align: center;">32 (2.9%)</th>
<th style="text-align: center;">25 (10.9%)</th>
<th style="text-align: center;">77 (65.8%)</th>
<th style="text-align: center;">269 (4.2%)</th>
</tr>
<tr>
<th colspan="6" style="text-align: center;">Anesthesia</th>
</tr>
<tr>
<th style="text-align: center;">General</th>
<th style="text-align: center;">4,630 (93.9%)</th>
<th style="text-align: center;">1,093 (98.4%)</th>
<th style="text-align: center;">203 (88.3%)</th>
<th style="text-align: center;">117 (100.0%)</th>
<th style="text-align: center;">6,043 (94.6%)</th>
</tr>
<tr>
<th style="text-align: center;">Spinal</th>
<th style="text-align: center;">246 (5.0%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">27 (11.7%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">273 (4.3%)</th>
</tr>
<tr>
<th style="text-align: center;">Sedation</th>
<th style="text-align: center;">54 (1.1%)</th>
<th style="text-align: center;">18 (1.6%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">72 (1.1%)</th>
</tr>
<tr>
<th colspan="6" style="text-align: center;">Duration of anesthesia (min)</th>
</tr>
<tr>
<th style="text-align: center;"></th>
<th style="text-align: center;">150 (90-245)</th>
<th style="text-align: center;">170 (110-220)</th>
<th style="text-align: center;">135 (95-185)</th>
<th style="text-align: center;">190 (79-231)</th>
<th style="text-align: center;">150 (90-240)</th>
</tr>
<tr>
<th colspan="6" style="text-align: center;">Anesthetics</th>
</tr>
<tr>
<th style="text-align: center;">Sevoflurane</th>
<th style="text-align: center;">2,076 (42.1%)</th>
<th style="text-align: center;">255 (23.0%)</th>
<th style="text-align: center;">172 (74.8%)</th>
<th style="text-align: center;">34 (29.1%)</th>
<th style="text-align: center;">2,537 (39.7%)</th>
</tr>
<tr>
<th style="text-align: center;">Desflurane</th>
<th style="text-align: center;">1,012 (20.5%)</th>
<th style="text-align: center;">226 (20.3%)</th>
<th style="text-align: center;">69 (30.0%)</th>
<th style="text-align: center;">106 (90.6%)</th>
<th style="text-align: center;">1,383 (21.6%)</th>
</tr>
<tr>
<th style="text-align: center;">Propofol TCI</th>
<th style="text-align: center;">2,490 (50.5%)</th>
<th style="text-align: center;">996 (89.6%)</th>
<th style="text-align: center;">5 (2.2%)</th>
<th style="text-align: center;">7 (6.0%)</th>
<th style="text-align: center;">3,498 (54.8%)</th>
</tr>
<tr>
<th style="text-align: center;">Remifentanil TCI</th>
<th style="text-align: center;">3,639 (73.8%)</th>
<th style="text-align: center;">1,000 (90.0%)</th>
<th style="text-align: center;">110 (47.8%)</th>
<th style="text-align: center;">86 (73.5%)</th>
<th style="text-align: center;">4,835 (75.7%)</th>
</tr>
<tr>
<th colspan="6" style="text-align: center;">Device</th>
</tr>
<tr>
<th style="text-align: center;">Tram-Rac 4A (SNUADC)</th>
<th style="text-align: center;">4,910 (99.6%)</th>
<th style="text-align: center;">1,103 (99.3%)</th>
<th style="text-align: center;">226 (98.3%)</th>
<th style="text-align: center;">116 (99.1%)</th>
<th style="text-align: center;">6,355 (99.5%)</th>
</tr>
<tr>
<th style="text-align: center;">Solar 8000M</th>
<th style="text-align: center;">4,930 (100.0%)</th>
<th style="text-align: center;">1,111 (100.0%)</th>
<th style="text-align: center;">230 (100.0%)</th>
<th style="text-align: center;">117 (100.0%)</th>
<th style="text-align: center;">6,388 (100%)</th>
</tr>
<tr>
<th style="text-align: center;">Primus</th>
<th style="text-align: center;">4,915 (99.7%)</th>
<th style="text-align: center;">1,104 (99.4%)</th>
<th style="text-align: center;">226 (98.3%)</th>
<th style="text-align: center;">117 (100.0%)</th>
<th style="text-align: center;">6,362 (99.6%)</th>
</tr>
<tr>
<th style="text-align: center;">BIS Vista</th>
<th style="text-align: center;">4,282 (86.9%)</th>
<th style="text-align: center;">1,004 (90.4%)</th>
<th style="text-align: center;">196 (85.2%)</th>
<th style="text-align: center;">84 (71.8%)</th>
<th style="text-align: center;">5,566 (87.1%)</th>
</tr>
<tr>
<th style="text-align: center;">Orchestra</th>
<th style="text-align: center;">3,713 (75.3%)</th>
<th style="text-align: center;">1,005 (90.5%)</th>
<th style="text-align: center;">115 (50.0%)</th>
<th style="text-align: center;">86 (73.5%)</th>
<th style="text-align: center;">4,919 (77.0%)</th>
</tr>
<tr>
<th style="text-align: center;">Vigileo</th>
<th style="text-align: center;">85 (1.7%)</th>
<th style="text-align: center;">227 (20.4%)</th>
<th style="text-align: center;">4 (1.7%)</th>
<th style="text-align: center;">32 (27.4%)</th>
<th style="text-align: center;">348 (5.4%)</th>
</tr>
<tr>
<th style="text-align: center;">EV1000</th>
<th style="text-align: center;">598 (12.1%)</th>
<th style="text-align: center;">1 (0.1%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">599 (9.4%)</th>
</tr>
<tr>
<th style="text-align: center;">Vigilance II</th>
<th style="text-align: center;">63 (1.3%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">63 (1.0%)</th>
</tr>
<tr>
<th style="text-align: center;">CardioQ</th>
<th style="text-align: center;">29 (0.6%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">29 (0.5%)</th>
</tr>
<tr>
<th style="text-align: center;">INVOS<sup>TM</sup></th>
<th style="text-align: center;">33 (0.7%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">33 (0.5%)</th>
</tr>
<tr>
<th style="text-align: center;">FMS2000</th>
<th style="text-align: center;">15 (0.3%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">0 (0.0%)</th>
<th style="text-align: center;">15 (0.2%)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**Device and data track description**

<table>
<thead>
<tr>
<th style="text-align: center;">Device</th>
<th style="text-align: center;">Device type</th>
<th style="text-align: center;">Company</th>
<th style="text-align: center;">Parameters</th>
<th style="text-align: center;">Data type</th>
<th style="text-align: center;">Number of parameters</th>
<th style="text-align: center;">Acquisition interval (sec)</th>
</tr>
<tr>
<th style="text-align: center;"><p>Tram-Rac 4A</p>
<p>(SNUADC)</p></th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE healthcare</th>
<th style="text-align: center;">ECG, capnography, plethysmogram, respiration, blood pressures</th>
<th style="text-align: center;">wave</th>
<th style="text-align: center;">6</th>
<th style="text-align: center;">1/500</th>
</tr>
<tr>
<th style="text-align: center;">Solar 8000M</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE healthcare</th>
<th style="text-align: center;">Heart rate, blood pressures, oxygen saturation, temperature, gas concentrations, etc.</th>
<th style="text-align: center;">numeric</th>
<th style="text-align: center;">44</th>
<th style="text-align: center;">2</th>
</tr>
<tr>
<th style="text-align: center;">Primus</th>
<th style="text-align: center;">Anesthesia machine</th>
<th style="text-align: center;">Drager</th>
<th style="text-align: center;">Gas concentrations, volumes and flows, airway pressures</th>
<th style="text-align: center;">wave and numeric</th>
<th style="text-align: center;">37</th>
<th style="text-align: center;">1/62.5 for waves, 7 for numeric data</th>
</tr>
<tr>
<th style="text-align: center;">BIS Vista</th>
<th style="text-align: center;">EEG monitor</th>
<th style="text-align: center;">Covidien</th>
<th style="text-align: center;">EEG waves, BIS and related parameters</th>
<th style="text-align: center;">wave and numeric</th>
<th style="text-align: center;">8</th>
<th style="text-align: center;">1/128 for EEG wave, 1 for numeric data</th>
</tr>
<tr>
<th style="text-align: center;">Orchestra®</th>
<th style="text-align: center;">Target-controlled infusion pump</th>
<th style="text-align: center;">Fresenius Kabi</th>
<th style="text-align: center;">Target, plasma and effect-site concentrations; infused, residual, total volumes, infusion rate and pressure; drug name and concentration</th>
<th style="text-align: center;">numeric</th>
<th style="text-align: center;">51</th>
<th style="text-align: center;">1</th>
</tr>
<tr>
<th style="text-align: center;">Vigileo</th>
<th style="text-align: center;">Cardiac output monitors</th>
<th style="text-align: center;">Edwards Lifesciences</th>
<th style="text-align: center;">Stroke volume and derived parameters</th>
<th style="text-align: center;">numeric</th>
<th style="text-align: center;">5</th>
<th style="text-align: center;">2</th>
</tr>
<tr>
<th style="text-align: center;">EV1000</th>
<th style="text-align: center;">Cardiac output monitors</th>
<th style="text-align: center;">Edwards Lifesciences</th>
<th style="text-align: center;">Stroke volume and derived parameters</th>
<th style="text-align: center;"></th>
<th style="text-align: center;">9</th>
<th style="text-align: center;">2</th>
</tr>
<tr>
<th style="text-align: center;">Vigilance II</th>
<th style="text-align: center;">Cardiac output monitors</th>
<th style="text-align: center;">Edwards Lifesciences</th>
<th style="text-align: center;">Cardiac output and derived parameters, temperature, oxygen saturation,</th>
<th style="text-align: center;"></th>
<th style="text-align: center;">14</th>
<th style="text-align: center;">2</th>
</tr>
<tr>
<th style="text-align: center;">CardioQ</th>
<th style="text-align: center;">Cardiac output monitors</th>
<th style="text-align: center;">Deltex</th>
<th style="text-align: center;">Stroke volume, cardiac output and related parameters</th>
<th style="text-align: center;">wave and numeric</th>
<th style="text-align: center;">13</th>
<th style="text-align: center;">1/180 for flow and arterial pressure waves; 1 for numeric data</th>
</tr>
<tr>
<th style="text-align: center;">INVOS<sup>TM</sup></th>
<th style="text-align: center;">Cerebral/somatic oximeter</th>
<th style="text-align: center;">Covidien</th>
<th style="text-align: center;">Cerebral oxygen saturation</th>
<th style="text-align: center;">numeric</th>
<th style="text-align: center;">2</th>
<th style="text-align: center;">5</th>
</tr>
<tr>
<th style="text-align: center;">FMS2000</th>
<th style="text-align: center;">Rapid infusion system</th>
<th style="text-align: center;">Belmont Instrument</th>
<th style="text-align: center;">Infused volume, infusion rate, temperatures, pressure</th>
<th style="text-align: center;">numeric</th>
<th style="text-align: center;">7</th>
<th style="text-align: center;">every 2.875 mL infused</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

\
=

# Parameter List

## Clinical Information

| Parameter | Data Source | Description | Unit |
|----|----|----|----|
| caseid | Random | Case ID; Random number between 00001 and 06388 |  |
| subjectid | EMR | Subject ID; Deidentified hospital ID of patient |  |
| casestart | Case file | Recording Start Time; Set to 0 for anonymization | sec |
| caseend | Case file | Recording End Time; from casestart | sec |
| anestart | Case file | Anesthesia start time; from casestart | sec |
| aneend | Case file | Anesthesia end time; from casestart | sec |
| opstart | Case file | Operation start time; from casestart | sec |
| opend | Case file | Operation end time; from casestart | sec |
| age | EMR | Age | years |
| sex | EMR | Sex | M/F |
| height | EMR | Height | cm |
| weight | EMR | Weight | kg |
| bmi | EMR | Body mass index | kg/m2 |
| asa | EMR | ASA Physical status classification |  |
| emop | EMR | Emergency operation |  |
| department | EMR | Surgical department |  |
| optype | EMR | Surgery type |  |
| dx | EMR | Diagnosis |  |
| opname | EMR | Operation name |  |
| approach | EMR | Surgical approach |  |
| position | EMR | Surgical position |  |
| ane_type | EMR | Anesthesia type |  |
| adm | EMR | Admission time from casestart | sec |
| dis | EMR | Discharge time from casestart | sec |
| los_postop | EMR | Postoperative length of hospital stay | days |
| los_icu | EMR | Postoperative length of ICU stay | days |
| death_inhosp | EMR | In-hospital Mortality |  |
| preop_htn | EMR | Preoperative hypertension |  |
| preop_dm | EMR | Preoperative diabetes |  |
| preop_ecg | EMR | Preoperative ecg (Normal Sinus Rhythm / Left anterior fascicular block / etc) |  |
| preop_pft | EMR | Preoperative pulmonary function |  |
| preop_hb | EMR | Preoperative hemoglobin | g/dL |
| preop_plt | EMR | Preoperative platelet count | x1000/mcL |
| preop_pt | EMR | Preoperative PT | % |
| preop_aptt | EMR | Preoperative aPTT | sec |
| preop_na | EMR | Preoperative Na | mmol/L |
| preop_k | EMR | Preoperative K | mmol/L |
| preop_gluc | EMR | Preoperative glucose | mg/dL |
| preop_alb | EMR | Preoperative albumin | g/dL |
| preop_ast | EMR | Preoperative GOT | IU/L |
| preop_alt | EMR | Preoperative GPT | IU/L |
| preop_bun | EMR | Preoperative blood urea nitrogen | mg/dL |
| preop_cr | EMR | Preoperative creatinine | mg/dL |
| preop_ph | EMR | Preoperative pH |  |
| preop_hco3 | EMR | Preoperative HCO3- | mmol/L |
| preop_be | EMR | Preoperative base excess | mmol/L |
| preop_pao2 | EMR | Preoperative PaO2 | mmHg |
| preop_paco2 | EMR | Preoperative PaCO2 | mmHg |
| preop_sao2 | EMR | Preoperative SpO2 | % |
| cormack | EMR | Cormack's grade |  |
| airway | EMR | Airway route |  |
| tubesize | EMR | Endotracheal tube size | mm |
| dltubesize | EMR | Double lumen tube size | Fr |
| lmasize | EMR | LMA size |  |
| iv1 | EMR | Site of IV line (1) |  |
| iv2 | EMR | Site of IV line (2) |  |
| aline1 | EMR | Site of arterial line (1) |  |
| aline2 | EMR | Site of arterial line (2) |  |
| cline1 | EMR | Site of central line (1) |  |
| cline2 | EMR | Site of central line (2) |  |
| intraop_ebl | EMR | Estimated blood loss | mL |
| intraop_uo | EMR | Intraoperative urine output | mL |
| intraop_rbc | EMR | Intraoperative RBC transfusion | Unit |
| intraop_ffp | EMR | Intraoperative FFP transfusion | Unit |
| intraop_crystalloid | EMR | Intraoperative crystalloid | mL |
| intraop_colloid | EMR | Intraoperative colloid | mL |
| intraop_ppf | EMR | Propofol bolus | mg |
| intraop_mdz | EMR | Midazolam | mg |
| intraop_ftn | EMR | Fentanyl | mcg |
| intraop_rocu | EMR | Rocuronium | mg |
| intraop_vecu | EMR | Vecuronium | mg |
| intraop_eph | EMR | Ephedrine | mg |
| intraop_phe | EMR | Phenylephrine | mcg |
| intraop_epi | EMR | Epinephrine | mcg |
| intraop_ca | EMR | Calcium chloride | mg |

\
-

## Hemodynamic Parameters

* The parameter name is in the form of “device name / data track name”.

W=waveform; N=numeric; S=string

| Parameter | Description | Type/Hz |
|----|----|----|
| SNUADC/ART | Arterial pressure wave | W/500 |
| SNUADC/CVP | Central venous pressure wave | W/500 |
| SNUADC/ECG_II | ECG lead II wave | W/500 |
| SNUADC/ECG_V5 | ECG lead V5 wave | W/500 |
| SNUADC/FEM | Femoral arterial pressure wave | W/500 |
| SNUADC/PLETH | Plethysmography wave | W/500 |
| Solar8000/ART_DBP | Diastolic arterial pressure | N |
| Solar8000/ART_MBP | Mean arterial pressure | N |
| Solar8000/ART_SBP | Systolic arterial pressure | N |
| Solar8000/BT | Body temperature | N |
| Solar8000/CVP | Central venous pressure | N |
| Solar8000/ETCO2 | End-tidal CO2 | N |
| Solar8000/FEM_DBP | Femoral diastolic arterial pressure | N |
| Solar8000/FEM_MBP | Femoral mean arterial pressure | N |
| Solar8000/FEM_SBP | Femoral systolic arterial pressure | N |
| Solar8000/FEO2 | Fraction of expired O2 | N |
| Solar8000/FIO2 | Fraction of inspired O2 | N |
| Solar8000/GAS2_EXPIRED | Expiratory volatile concentration | N |
| Solar8000/GAS2_INSPIRED | Inspiratory volatile concentration | N |
| Solar8000/HR | Heart rate | N |
| Solar8000/INCO2 | Inspiratory CO2 | N |
| Solar8000/NIBP_DBP | Non-invasive diastolic arterial pressure | N |
| Solar8000/NIBP_MBP | Non-invasive mean arterial pressure | N |
| Solar8000/NIBP_SBP | Non-invasive systolic arterial pressure | N |
| Solar8000/PA_DBP | Pulmonary diastolic arterial pressure | N |
| Solar8000/PA_MBP | Pulmonary mean arterial pressure | N |
| Solar8000/PA_SBP | Pulmonary systolic arterial pressure | N |
| Solar8000/PLETH_HR | Heart rate based on plethysmography | N |
| Solar8000/PLETH_SPO2 | Percutaneous oxygen saturation | N |
| Solar8000/RR | Respiratory rate based on ECG | N |
| Solar8000/RR_CO2 | Respiratory rate based on capnography | N |
| Solar8000/ST_AVF | ST segment in lead aVF | N |
| Solar8000/ST_AVL | ST segment in lead aVL | N |
| Solar8000/ST_AVR | ST segment in lead aVR | N |
| Solar8000/ST_I | ST segment in lead I | N |
| Solar8000/ST_II | ST segment in lead II | N |
| Solar8000/ST_III | ST segment in lead III | N |
| Solar8000/ST_V5 | ST segment in lead V5 | N |
| Solar8000/VENT_COMPL | Airway compliance (from ventilator) | N |
| Solar8000/VENT_INSP_TM | Inspiratory time (from ventilator) | N |
| Solar8000/VENT_MAWP | Mean airway pressure (from ventilator) | N |
| Solar8000/VENT_MEAS_PEEP | Positive end-expiratory pressure (from ventilator) | N |
| Solar8000/VENT_MV | Minute ventilation (from ventilator) | N |
| Solar8000/VENT_PIP | Peak inspiratory pressure (from ventilator) | N |
| Solar8000/VENT_PPLAT | Plateau pressure (from ventilator) | N |
| Solar8000/VENT_RR | Respiratory rate (from ventilator) | N |
| Solar8000/VENT_SET_FIO2 | Set fraction of inspired O2 (from ventilator) | N |
| Solar8000/VENT_SET_PCP | Set peak inspiratory pressure in pressure control mode (from ventilator) | N |
| Solar8000/VENT_SET_TV | Set tidal volume in volume control mode (from ventilator) | N |
| Solar8000/VENT_TV | Measured tidal volume (from ventilator) | N |
| Primus/AWP | Airway pressure wave | W/62.5 |
| Primus/CO2 | Capnography wave | W/62.5 |
| Primus/COMPLIANCE | Airway compliance | N |
| Primus/ETCO2 | End-tidal CO2 | N |
| Primus/EXP_DES | Expiratory desflurane pressure | N |
| Primus/EXP_SEVO | Expiratory sevoflurane pressure | N |
| Primus/FEN2O | Fraction of expired N2O | N |
| Primus/FEO2 | Fraction of expired O2 | N |
| Primus/FIN2O | Fraction of inspired N2O | N |
| Primus/FIO2 | Fraction of inspired O2 | N |
| Primus/FLOW_AIR | Flow rate of air | N |
| Primus/FLOW_N2O | Flow rate of N2O | N |
| Primus/FLOW_O2 | Flow rate of O2 | N |
| Primus/INCO2 | Inspiratory CO2 | N |
| Primus/INSP_DES | Inspiratory desflurane pressure | N |
| Primus/INSP_SEVO | Inspiratory sevoflurane pressure | N |
| Primus/MAC | Minimum alveolar concentration of volatile | N |
| Primus/MAWP_MBAR | Mean airway pressure | N |
| Primus/MV | Minute volume | N |
| Primus/PAMB_MBAR | Ambient pressure | N |
| Primus/PEEP_MBAR | Positive end expiratory pressure (PEEP) | N |
| Primus/PIP_MBAR | Peak inspiratory pressure | N |
| Primus/PPLAT_MBAR | Plateau pressure | N |
| Primus/RR_CO2 | Respiratory rate based on capnography | N |
| Primus/SET_AGE | Patient age | N |
| Primus/SET_FIO2 | Set fraction of inspired O2 | N |
| Primus/SET_FLOW_TRIG | Set flow trigger value | N |
| Primus/SET_FRESH_FLOW | Set fresh gas flow | N |
| Primus/SET_INSP_PAUSE | Set inspiratory pause | N |
| Primus/SET_INSP_PRES | Set inspiratory pressure | N |
| Primus/SET_INSP_TM | Set inspiratory time | N |
| Primus/SET_INTER_PEEP | Set positive end expiratory pressure (PEEP) | N |
| Primus/SET_PIP | Set peak inspiratory pressure | N |
| Primus/SET_RR_IPPV | Set respiratory rate | N |
| Primus/SET_TV_L | Set tidal volume in liter | N |
| Primus/TV | Tidal volume | N |
| Primus/VENT_LEAK | Ventilator leakage | N |
| Orchestra/AMD_RATE | Infusion rate (amiodarone 2 mg/mL) | N |
| Orchestra/AMD_VOL | Infused volume (amiodarone 2 mg/mL) | N |
| Orchestra/DEX2_RATE | Infusion rate (dexmedetomidine 2 mcg/mL) | N |
| Orchestra/DEX2_VOL | Infused volume (dexmedetomidine 2 mcg/mL) | N |
| Orchestra/DEX4_RATE | Infusion rate (dexmedetomidine 4 mcg/mL) | N |
| Orchestra/DEX4_VOL | Infused volume (dexmedetomidine 4 mcg/mL) | N |
| Orchestra/DOBU_RATE | Infusion rate (dobutamine 2 mg/mL) | N |
| Orchestra/DOBU_VOL | Infused volume (dobutamine 2 mg/mL) | N |
| Orchestra/DOPA_RATE | Infusion rate (dopamine 2 mg/mL) | N |
| Orchestra/DOPA_VOL | Infused volume (dopamine 2 mg/mL) | N |
| Orchestra/DTZ_RATE | Infusion rate (diltiazem 1 mg/mL) | N |
| Orchestra/DTZ_VOL | Infused volume (diltiazem 1 mg/mL) | N |
| Orchestra/EPI_RATE | Infusion rate (epinephrine 20 mcg/mL) | N |
| Orchestra/EPI_VOL | Infused volume (epinephrine 20 mcg/mL) | N |
| Orchestra/FUT_RATE | Infusion rate (futhan 0.5 mg/mL) | N |
| Orchestra/FUT_VOL | Infused volume (futhan 0.5 mg/mL) | N |
| Orchestra/MRN_RATE | Infusion rate (milrinone 200 mcg/mL) | N |
| Orchestra/MRN_VOL | Infused volume (milrinone 200 mcg/mL) | N |
| Orchestra/NEPI_RATE | Infusion rate (norepinephrine 20 mcg/mL) | N |
| Orchestra/NEPI_VOL | Infused volume (norepinephrine 20 mcg/mL) | N |
| Orchestra/NPS_RATE | Infused rate (nitroprusside 0.2 mg/mL) | N |
| Orchestra/NPS_VOL | Infusion volume (nitroprusside 0.2 mg/mL) | N |
| Orchestra/NTG_RATE | Infused rate (nitroglycerin 0.2 mg/mL) | N |
| Orchestra/NTG_VOL | Infusion volume (nitroglycerin 0.2 mg/mL) | N |
| Orchestra/OXY_RATE | Infused rate (oxytocin 0.2 U/mL) | N |
| Orchestra/OXY_VOL | Infusion volume (oxytocin 0.2 U/mL) | N |
| Orchestra/PGE1_RATE | Infused rate (prostaglandin-E1 2 mg/mL) | N |
| Orchestra/PGE1_VOL | Infusion volume (prostaglandin-E1 2 mg/mL) | N |
| Orchestra/PHEN_RATE | Infused rate (phenylephrine 100 mcg/mL) | N |
| Orchestra/PHEN_VOL | Infusion volume (phenylephrine 100 mcg/mL) | N |
| Orchestra/PPF20_CE | Effect-site concentration (propofol 20 mg/mL) | N |
| Orchestra/PPF20_CP | Plasma concentration (propofol 20 mg/mL) | N |
| Orchestra/PPF20_CT | Target concentration (propofol 20 mg/mL) | N |
| Orchestra/PPF20_RATE | Infusion rate (propofol 20 mg/mL) | N |
| Orchestra/PPF20_VOL | Infused volume (propofol 20 mg/mL) | N |
| Orchestra/RFTN20_CE | Effect-site concentration (remifentanil 20 mcg/mL) | N |
| Orchestra/RFTN20_CP | Plasma concentration (remifentanil 20 mcg/mL) | N |
| Orchestra/RFTN20_CT | Target concentration (remifentanil 20 mcg/mL) | N |
| Orchestra/RFTN20_RATE | Infusion rate (remifentanil 20 mcg/mL) | N |
| Orchestra/RFTN20_VOL | Infused volume (remifentanil 20 mcg/mL) | N |
| Orchestra/RFTN50_CE | Effect-site concentration (remifentanil 50 mcg/mL) | N |
| Orchestra/RFTN50_CP | Plasma concentration (remifentanil 50 mcg/mL) | N |
| Orchestra/RFTN50_CT | Target concentration (remifentanil 50 mcg/mL) | N |
| Orchestra/RFTN50_RATE | Infusion rate (remifentanil 50 mcg/mL) | N |
| Orchestra/RFTN50_VOL | Infused volume (remifentanil 50 mcg/mL) | N |
| Orchestra/ROC_RATE | Infusion rate (rocuronium 2 mg/mL) | N |
| Orchestra/ROC_VOL | Infused volume (rocuronium 2 mg/mL) | N |
| Orchestra/VASO_RATE | Infusion rate (vasopressin 0.2 U/mL) | N |
| Orchestra/VASO_VOL | Infused volume (vasopressin 0.2 U/mL) | N |
| Orchestra/VEC_RATE | Infusion rate (vecuronium 1 mg/mL) | N |
| Orchestra/VEC_VOL | Infused volume (vecuronium 1 mg/mL) | N |
| BIS/BIS | Bispectral index value | N |
| BIS/EEG1_WAV | EEG wave from channel 1 | W/128 |
| BIS/EEG2_WAV | EEG wave from channel 2 | W/128 |
| BIS/EMG | Electromyography power | N |
| BIS/SEF | Spectral edge frequency | N |
| BIS/SQI | Signal quality index | N |
| BIS/SR | Suppression ratio | N |
| BIS/TOTPOW | Total power | N |
| Invos/SCO2_L | Cerebral oxygen saturation (Left) | N |
| Invos/SCO2_R | Cerebral oxygen saturation (Right) | N |
| Vigileo/CI | Cardiac index | N |
| Vigileo/CO | Cardiac output | N |
| Vigileo/SV | Stroke volume | N |
| Vigileo/SVI | Stroke volume index | N |
| Vigileo/SVV | Stroke volume variation | N |
| EV1000/ART_MBP | Mean arterial pressure | N |
| EV1000/CI | Cardiac index | N |
| EV1000/CO | Cardiac output | N |
| EV1000/CVP | Central venous pressure wave | N |
| EV1000/SV | Stroke volume | N |
| EV1000/SVI | Stroke volume index | N |
| EV1000/SVR | Systemic vascular resistance | N |
| EV1000/SVRI | Systemic vascular resistance index | N |
| EV1000/SVV | Stroke volume variation | N |
| Vigilance/BT_PA | Pulmonary artery temperature | N |
| Vigilance/CI | Cardiac index | N |
| Vigilance/CO | Cardiac output | N |
| Vigilance/EDV | End-diastolic volume | N |
| Vigilance/EDVI | End-diastolic volume index | N |
| Vigilance/ESV | End-systolic volume | N |
| Vigilance/ESVI | End-systolic volume index | N |
| Vigilance/HR_AVG | Average heart rate | N |
| Vigilance/RVEF | Right ventricular ejection fraction | N |
| Vigilance/SNR | Signal to noise ratio | N |
| Vigilance/SQI | Signal quality index | N |
| Vigilance/SV | Stroke volume | N |
| Vigilance/SVI | Stroke volume index | N |
| Vigilance/SVO2 | Mixed venous oxygen saturation | N |
| CardioQ/ABP | Arterial pressure wave | W/180 |
| CardioQ/FLOW | Flow wave | W/180 |
| CardioQ/CI | Cardiac index | N |
| CardioQ/CO | Cardiac output | N |
| CardioQ/FTc | Flow time corrected | N |
| CardioQ/FTp | Flow time to peak | N |
| CardioQ/HR | Heart rate | N |
| CardioQ/MA | Mean acceleration | N |
| CardioQ/MD | Minute distance | N |
| CardioQ/PV | Peak velocity | N |
| CardioQ/SD | Stroke distance | N |
| CardioQ/SV | Stroke volume | N |
| CardioQ/SVI | Stroke volume index | N |
| FMS/FLOW_RATE | Flow rate | N |
| FMS/INPUT_AMB_TEMP | Input ambient temperature | N |
| FMS/INPUT_TEMP | Input fluid temperature | N |
| FMS/OUTPUT_AMB_TEMP | Output ambient temperature | N |
| FMS/OUTPUT_TEMP | Output fluid temperature | N |
| FMS/PRESSURE | Infusion line pressure | N |
| FMS/TOTAL_VOL | Total infused volume | N |

\
=

## Lab Results

| **Parameter** | **Data Source** | **Category** | **Description** | **Unit** | **Reference value** |
|----|----|----|----|----|----|
| wbc | EMR | CBC | White blood cell count | ×1000/mcL | 4~10 |
| hb | EMR | CBC | Hemoglobin | g/dL | 13~17 |
| hct | EMR | CBC | Hematocrit | % | 39~52 |
| plt | EMR | CBC | Platelet count | ×1000/mcL | 130~400 |
| esr | EMR | CBC | Erythrocyte sedimentation rate | mm/hr | 0~9 |
| gluc | EMR | Chemistry | Glucose | mg/dL | 70~110 |
| tprot | EMR | Chemistry | Total protein | g/dL | 6.0~8.0 |
| alb | EMR | Chemistry | Albumin | g/dL | 3.3~5.2 |
| tbil | EMR | Chemistry | Total bilirubin | mg/dL | 0.2~1.2 |
| ast | EMR | Chemistry | Asparate transferase | IU/L | 1~40 |
| alt | EMR | Chemistry | Alanine transferase | IU/L | 1~40 |
| bun | EMR | Chemistry | Blood urea nitrogen | mg/dL | 10~26 |
| cr | EMR | Chemistry | Creatinine | mg/dL | 0.70~1.40 |
| gfr | EMR | Chemistry | Glomerular filtration rate | mL/min/1.73 m2 | 90~120 |
| ccr | EMR | Chemistry | Creatinine clearance | mL/min | 75~125 |
| na | EMR | Chemistry | Sodium | mmol/L | 135~145 |
| k | EMR | Chemistry | Potassium | mmol/L | 3.5~5.5 |
| ica | EMR | Chemistry | ionized Calcium | mmol/L | 1.05~1.35 |
| cl | EMR | Chemistry | Chloride | mmol/L | 98~110 |
| ammo | EMR | Chemistry | Ammonia | mcg/dL | 27.2~102 |
| crp | EMR | Chemistry | C-reactive protein | mg/dL | 0~0.5 |
| lac | EMR | Chemistry | Lactate | mmol/L | 0.5~2.2 |
| ptinr | EMR | Coagulation | Prothrombin time (INR) | INR | 0.8~1.2 |
| pt% | EMR | Coagulation | Prothrombin time (%) | % | 80~120 |
| ptsec | EMR | Coagulation | Prothrombin time (sec) | sec | 10.6~12.9 |
| aptt | EMR | Coagulation | Activated partial thromboplastin time | sec | 26.7~36.6 |
| fib | EMR | Coagulation | Fibrinogen | mg/dL | 192~411 |
| ph | EMR | ABGA | pH | 　 | 7.35~7.45 |
| pco2 | EMR | ABGA | partial pressure of CO2 | mmHg | 35~48 |
| po2 | EMR | ABGA | partial pressure of O2 | mmHg | 83~108 |
| hco3 | EMR | ABGA | Bicarbonate | mmol/L | 18~23.0 |
| be | EMR | ABGA | Base excess | mmol/L | -2.0~3.0 |
| sao2 | EMR | ABGA | Arterial oxygen saturation | % | 95~98 |

\
=

# Data Use Agreement

1\. Objective

This Agreement (hereinafter referred to as the "Agreement") is made in accordance with Article 18 (2) 4 of the Personal Information Protection Act and Article 16 (3) of the Bioethics Act of Korea, and the Health Insurance Portability and Accountability Act of 1996 (HIPPA) Regulation 45 CFR Part 160 and Part 164. This agreement is intended to specify the details necessary to allow the access of data users (hereinafter referred to as the "User") to the limited data set (hereinafter referred to as the "Data") provided by the VitalDB team (hereinafter referred to as the "Provider").

2\. Terms

Unless otherwise specified, the definition of terms used in this Agreement shall be governed by the Personal Information Protection Law of the Republic of Korea and the United States HIPPA regulations.

3\. License

Users are permitted to use dataset from the Provider website subject to our terms of use.

The dataset will be released to Users under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license. This license type has been applied to the VitalDB Open Dataset in order to maximize the dissemination and use of the Data.

4\. Provider's obligation

The provider prepares and presents the Data to the User. The following unique personal identifier and Protected Health Information (PHI) are removed from the Data provided:

Name (including Chinese characters and full name), address, unique identifiers (resident registration number, passport number, foreigner registration number, driver's license number, medical record number, health insurance number, social welfare number, soldier’s serial number, business registration number), time (date of birth, anniversary, date of death, date of certification, date of hospital admission, date of discharge, date of operation, etc.), telephone number (mobile phone number, home phone number, work phone number, fax number), e-mail address, homepage address, account number, card number, various certificates and license numbers, biometric information (fingerprint, voice, iris, etc.),

5\. User's obligation

1\) The User can use the Data for research and development purposes.

2\) The User must not disclose the Data to anyone who is not hired to the User without the consent of provider. If the User wishes to disclose the Data to his or her employee, the User must document the contract applying the same restrictions and conditions as those applied to him/herself to the employee, and have all legal responsibility for the use of the Data.

3\) The User must not use or disclose the Data beyond the scope of this Agreement except as required by law.

4\) The User must take appropriate security measures to prevent the use or disclosure of Data that is outside the scope of this Agreement.

5\) The User must report to the Provider within 24 hours if you use or disclose the Data beyond the scope of this Agreement.

6\) The User must not attempt to identify any personal information from the Data.

6\. Change of contract

1\) The Provider may change this Agreement if there are reasonable grounds, and in this case, the Provider shall post the date and reason for the change to the VitalDB website no later than 14 days prior to the change being applied.

2\) Any change of the contract in accordance with paragraph 1 above shall become effective upon the User’s consent. However, if the User does not express the intention of rejection within a certain period of time, the User shall be deemed to have agreed to the revised contract.

3\) The User is obliged to periodically check the notice on the VitalDB homepage.

4\) The User is responsible for any damage caused by failure to confirm the changes to the Agreement.

7\. Termination of contract

1\) Unless otherwise specified, the term of this Agreement shall be five years. However, if there is no notice, the contract period is automatically extended.

2\) The User may terminate the contract at any time by deleting the provided Data and notifying the Provider of this fact.

3\) The Provider may terminate the Agreement at any time by giving notice to the User 30 days prior to termination.

4\) The contract is immediately terminated if:

a\) The User is found to be in violation of HIPAA, the Personal Information Protection Act, or Bioethics Act.

b\) The User violates the laws or regulations of the country or organization to which he/she belongs.

c\) The User is presumed to have violated this Agreement in the sole judgment of the Provider.

d\) The benefit of the Provider is infringed by the sole judgment of the Provider.

8\. Others

1\) If the Data becomes no longer available due to related legislative changes, the Provider may limit the use of the Data after 14 days’ notice to the User.

2\) Unless otherwise provided in this Agreement, the User’s right is not transferable to any third party.

# Acknowledgement

Our project is currently supported by the Korea Medical Device Development Fund grant funded by ­the Korea government (the Ministry of Science and ICT, the Ministry of Trade, Industry and Energy, the Ministry of Health & Welfare, Republic of Korea, the Ministry of Food and Drug Safety) (Project Number: KMDF_PR_20200901_0144, 9991006817); MSIT (Ministry of Science and ICT), Korea, under the ITRC (Information Technology Research Center) support program (IITP-2018-2018-0-01833); and ­National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT) (NRF-2018R1A5A1060031).

The project was previously supported by the ­National Research Foundation of Korea (NRF) grant funded by the Korean government (MEST) (NRF-2015R1A2A2A01003962).
