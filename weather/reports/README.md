# 🌺 Hawaiʻi State Weather Database

> **RootRecord's continuously updated, source-preserving weather database and reporting layer for Hawaiʻi.**

## 🌐 What This Is

This directory is the human-readable reporting layer built from the locally collected Hawaiʻi weather database.

The system is designed around a strict separation between:

- **Raw collected data** — the original fetched source material remains authoritative.
- **Official Sources** — readable copies preserved by issuing source, without processing-level mixing.
- **0 Level Processing** — statewide readable reports.
- **1 County Processing** — deterministic county/geographic reports.
- **Archives** — prior report versions are retained when substantive source content changes.

The live report below is regenerated automatically from the current statewide report data. It is not manually maintained.

## 🛰️ Imagery

![GOES-18 Hawaii GeoColor](https://raw.githubusercontent.com/rootrecordsoftwaresolutions/RootRecord-Weather-Database/main/Hawai%27i/hfo/cdn.star.nesdis.noaa.gov/GOES18/ABI/SECTOR/hi/GEOCOLOR/GOES18-HI-GEOCOLOR-600x600/GOES18-HI-GEOCOLOR-600x600_current.gif)

**GOES-18 Hawaii — GeoColor** is the selected live README banner. The image is the locally collected `_current.gif` product from the weather database, published through the existing weather-data synchronization pipeline.

The imagery pipeline uses stable NOAA/NESDIS product URLs. The stable URL is fetched repeatedly; when the returned image changes, the previous version is archived and the current product keeps its real source filename followed by `_current`.

## 🧭 Data Architecture

```text
Official / NOAA / NWS / NESDIS sources
                │
                ▼
        Raw Weather Database
                │
                ├──────────────► Official Sources
                │                    │
                ▼                    ▼
          0 Level Processing ───► 1 County Processing
                │                    │
                └──────────────┬─────┘
                               ▼
                     Live README / Reports
```

### Source integrity

- Original source identity is retained.
- Raw source material is not replaced by generated reports.
- Official-source records remain isolated from processing levels.
- County routing uses deterministic geographic rules.
- Products without authoritative geographic assignment are not silently copied into counties.
- Current reports are archived when substantive content changes.
- The live README and statewide report are generated from the same current product sections.

## 📚 Report Layers

| Layer | Purpose |
|---|---|
| **Official Sources** | Preserve readable official-source products grouped by issuing source |
| **0 Level Processing** | Statewide Hawaiʻi reporting |
| **1 County Processing** | Deterministically routed county reporting |
| **Archives** | Historical versions of changed reports |

## 🔄 Automatic Updating

Each scheduler/report-generation cycle can regenerate this README locally from the latest collected data.

The README is published through the existing RootRecord Git synchronization workflow alongside the other generated weather/report/media artifacts.

## 🤖 Machine / LLM Use

The database is structured so a local model can consume:

1. raw source material,
2. source-preserved official records,
3. statewide processing,
4. county-level processing,
5. historical archives,

without treating a generated summary as the original source.

## 🛡️ Integrity Boundary

Generated reports are presentation/processing artifacts. The raw collected weather data remains the authoritative local record.

No AI/LLM is used to decide geographic ownership of weather products.

---

## 🌦️ Live Hawaiʻi Statewide Weather Report

> **Automatically regenerated from the latest locally collected official weather products.**

| Status | Coverage | Updated | Sections |
|---|---|---|---:|
| 🟢 Active | Hawaiʻi statewide | 2026-09-25T21:24:16-10:00 HST | 35 |

The report below is generated from the same current product sections as `0 Level Processing/Hawaii_State_Weather_Report_current.md`. It is a presentation layer only; official-source records and raw source data remain preserved separately.

---

### 1. 7-Day Zone Forecasts (all islands)

| Field | Value |
|---|---|
| **Resource ID** | zfp_zone_forecast |
| **Official source** | https://api.weather.gov/products/types/ZFP/locations/HFO |
| **Collected** | 2026-09-25T17:03:51.498040-10:00 HST |

```text
{"@id": "https://api.weather.gov/products/89550b4e-369e-4a12-bdf7-93c632312524", "id": "89550b4e-369e-4a12-bdf7-93c632312524", "wmoCollectiveId": "FPHW50", "issuingOffice": "PHFO", "issuanceTime": "2026-09-26T02:58:00+00:00", "productCode": "ZFP", "productName": "Zone Forecast Product"}
```

---

### 2. AIRMETs

| Field | Value |
|---|---|
| **Resource ID** | wa0_airmets |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=WA0&issuedby=HI |
| **Collected** | 2026-09-25T18:06:52.680483-10:00 HST |

```text
988
WAHW31 PHFO 260337
WA0HI

HNLS WA 260400
AIRMET SIERRA FOR IFR VALID UNTIL 261000
.
AIRMET MTN OBSC...KAUAI OAHU MOLOKAI MAUI
N THROUGH E SECTIONS.
TEMPO MTN OBSC ABV 025 EXP DUE TO CLD AND SHRA.
COND CONT BEYOND 1000Z.
.
AIRMET IFR...BIG ISLAND
UPOLU POINT TO CAPE KUMUKAHI TO SOUTH CAPE.
TEMPO CEILING BLW 010 AND/OR VIS BLW 3SM SHRA.
COND CONT BEYOND 1000Z.

=HNLT WA 260400
AIRMET TANGO FOR TURB VALID UNTIL 261000
.
AIRMET TURB...HI
OVER AND IMT S THRU W OF MTN.
TEMPO MOD TURB EXP BLW 070.
COND CONT BEYOND 1000Z.

=HNLZ WA 260400
AIRMET ZULU FOR ICE AND FZLVL VALID UNTIL 261000
.
NO SIGNIFICANT ICE EXP.
.
FZLVL...159.
```

---

### 3. Area Forecast Discussion

| Field | Value |
|---|---|
| **Resource ID** | afd_area_forecast_discussion |
| **Official source** | https://api.weather.gov/products/types/AFD/locations/HFO |
| **Collected** | 2026-09-25T16:59:00.066176-10:00 HST |

```text
{"@id": "https://api.weather.gov/products/8759e216-9e2f-4366-8f44-be01140d2cfb", "id": "8759e216-9e2f-4366-8f44-be01140d2cfb", "wmoCollectiveId": "FXHW60", "issuingOffice": "PHFO", "issuanceTime": "2026-09-26T02:55:00+00:00", "productCode": "AFD", "productName": "Area Forecast Discussion"}
```

---

### 4. Coastal Waters Forecast (within 40nm)

| Field | Value |
|---|---|
| **Resource ID** | cwf_coastal_waters |
| **Official source** | https://api.weather.gov/products/types/CWF/locations/HFO |
| **Collected** | 2026-09-25T16:49:18.233970-10:00 HST |

```text
{"@id": "https://api.weather.gov/products/b8546f14-f95e-4408-9f14-de0911476e7f", "id": "b8546f14-f95e-4408-9f14-de0911476e7f", "wmoCollectiveId": "FZHW50", "issuingOffice": "PHFO", "issuanceTime": "2026-09-26T02:25:00+00:00", "productCode": "CWF", "productName": "Coastal Waters Forecast"}
```

---

### 5. Daily Climate Summary — HNL

| Field | Value |
|---|---|
| **Resource ID** | cli_daily_climate_summary_HNL |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLI&issuedby=HNL |
| **Collected** | 2026-09-25T18:15:57.215574-10:00 HST |

```text
791
CDHW40 PHFO 251245
CLIHNL

CLIMATE REPORT
NATIONAL WEATHER SERVICE HONOLULU HI
245 AM HST FRI SEP 25 2026

...................................

...THE HONOLULU CLIMATE SUMMARY FOR SEPTEMBER 24 2026...

CLIMATE NORMAL PERIOD 1991 TO 2020
CLIMATE RECORD PERIOD 1940 TO 2026

WEATHER ITEM OBSERVED TIME RECORD YEAR NORMAL DEPARTURE LAST
VALUE (LST) VALUE VALUE FROM YEAR
NORMAL
...................................................................
TEMPERATURE (F)
YESTERDAY
MAXIMUM 89 259 PM 93 1966 88 1 90
MINIMUM 79 656 AM 68 1955 75 4 74
AVERAGE 84 81 3 82

PRECIPITATION (IN)
YESTERDAY 0.00 0.68 1983 0.02 -0.02 0.01
MONTH TO DATE 0.32 0.72 -0.40 0.60
SINCE SEP 1 0.32 0.72 -0.40 0.60
SINCE JAN 1 22.35 10.31 12.04 9.48

DEGREE DAYS
HEATING
YESTERDAY 0 0 0 0
MONTH TO DATE 0 0 0 0
SINCE SEP 1 0 0 0 0
SINCE JUL 1 0 0 0 0

COOLING
YESTERDAY 19 16 3 17
MONTH TO DATE 436 401 35 429
SINCE SEP 1 436 401 35 429
SINCE JAN 1 3646 3478 168 3914
...................................................................

WIND (MPH)
HIGHEST WIND SPEED 28 HIGHEST WIND DIRECTION E (70)
HIGHEST GUST SPEED 42 HIGHEST GUST DIRECTION E (80)
AVERAGE WIND SPEED 13.8

SKY COVER
POSSIBLE SUNSHINE MM
AVERAGE SKY COVER 0.5

WEATHER CONDITIONS
THE FOLLOWING WEATHER WAS RECORDED YESTERDAY.
NO SIGNIFICANT WEATHER WAS OBSERVED.

RELATIVE HUMIDITY (PERCENT)
HIGHEST 77 300 AM
LOWEST 50 300 PM
AVERAGE 64

..........................................................

THE HONOLULU CLIMATE NORMALS FOR TODAY
NORMAL RECORD YEAR
MAXIMUM TEMPERATURE (F) 88 93 1966
1991
MINIMUM TEMPERATURE (F) 75 69 1945
1955
1971

SUNRISE AND SUNSET
SEPTEMBER 25 2026.....SUNRISE 621 AM HST SUNSET 625 PM HST
SEPTEMBER 26 2026.....SUNRISE 622 AM HST SUNSET 624 PM HST

- INDICATES NEGATIVE NUMBERS.
R INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T INDICATES TRACE AMOUNT.
```

---

### 6. Daily Climate Summary — ITO

| Field | Value |
|---|---|
| **Resource ID** | cli_daily_climate_summary_ITO |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLI&issuedby=ITO |
| **Collected** | 2026-09-25T18:17:57.738879-10:00 HST |

```text
790
CDHW43 PHFO 251245
CLIITO

CLIMATE REPORT
NATIONAL WEATHER SERVICE HONOLULU HI
245 AM HST FRI SEP 25 2026

...................................

...THE HILO/GEN.LYMAN FLD CLIMATE SUMMARY FOR SEPTEMBER 24 2026...

CLIMATE NORMAL PERIOD 1991 TO 2020
CLIMATE RECORD PERIOD 1949 TO 2026

WEATHER ITEM OBSERVED TIME RECORD YEAR NORMAL DEPARTURE LAST
VALUE (LST) VALUE VALUE FROM YEAR
NORMAL
...................................................................
TEMPERATURE (F)
YESTERDAY
MAXIMUM 81 129 PM 89 1995 83 -2 84
2005
2014
MINIMUM 73 746 AM 64 1955 70 3 67
1970
AVERAGE 77 76 1 76

PRECIPITATION (IN)
YESTERDAY 0.92 1.13 1979 0.29 0.63 0.11
MONTH TO DATE 12.40 6.93 5.47 2.69
SINCE SEP 1 12.40 6.93 5.47 2.69
SINCE JAN 1 120.64 81.92 38.72 38.07

DEGREE DAYS
HEATING
YESTERDAY 0 0 0 0
MONTH TO DATE 0 0 0 0
SINCE SEP 1 0 0 0 0
SINCE JUL 1 0 0 0 0

COOLING
YESTERDAY 12 12 0 11
MONTH TO DATE 319 288 31 307
SINCE SEP 1 319 288 31 307
SINCE JAN 1 2748 2399 349 2808
...................................................................

WIND (MPH)
HIGHEST WIND SPEED 13 HIGHEST WIND DIRECTION E (90)
HIGHEST GUST SPEED 21 HIGHEST GUST DIRECTION E (90)
AVERAGE WIND SPEED 6.6

SKY COVER
POSSIBLE SUNSHINE MM
AVERAGE SKY COVER 1.0

WEATHER CONDITIONS
THE FOLLOWING WEATHER WAS RECORDED YESTERDAY.
HEAVY RAIN
RAIN
LIGHT RAIN
FOG

RELATIVE HUMIDITY (PERCENT)
HIGHEST 97 800 AM
LOWEST 74 100 PM
AVERAGE 86

..........................................................

THE HILO/GEN.LYMAN FLD CLIMATE NORMALS FOR TODAY
NORMAL RECORD YEAR
MAXIMUM TEMPERATURE (F) 83 90 2014
MINIMUM TEMPERATURE (F) 70 64 1970

SUNRISE AND SUNSET
SEPTEMBER 25 2026.....SUNRISE 610 AM HST SUNSET 613 PM HST
SEPTEMBER 26 2026.....SUNRISE 610 AM HST SUNSET 613 PM HST

- INDICATES NEGATIVE NUMBERS.
R INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T INDICATES TRACE AMOUNT.
```

---

### 7. Daily Climate Summary — LIH

| Field | Value |
|---|---|
| **Resource ID** | cli_daily_climate_summary_LIH |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLI&issuedby=LIH |
| **Collected** | 2026-09-25T18:16:43.299589-10:00 HST |

```text
789
CDHW41 PHFO 251245
CLILIH

CLIMATE REPORT
NATIONAL WEATHER SERVICE HONOLULU HI
245 AM HST FRI SEP 25 2026

...................................

...THE LIHUE CLIMATE SUMMARY FOR SEPTEMBER 24 2026...

CLIMATE NORMAL PERIOD 1991 TO 2020
CLIMATE RECORD PERIOD 1950 TO 2026

WEATHER ITEM OBSERVED TIME RECORD YEAR NORMAL DEPARTURE LAST
VALUE (LST) VALUE VALUE FROM YEAR
NORMAL
...................................................................
TEMPERATURE (F)
YESTERDAY
MAXIMUM 84 328 PM 89 2019 85 -1 86
MINIMUM 77 619 AM 67 1952 75 2 73
AVERAGE 81 80 1 80

PRECIPITATION (IN)
YESTERDAY 0.03 0.76 1971 0.08 -0.05 0.02
MONTH TO DATE 3.02 1.70 1.32 1.60
SINCE SEP 1 3.02 1.70 1.32 1.60
SINCE JAN 1 42.81 23.80 19.01 13.06

DEGREE DAYS
HEATING
YESTERDAY 0 0 0 0
MONTH TO DATE 0 0 0 0
SINCE SEP 1 0 0 0 0
SINCE JUL 1 0 0 0 0

COOLING
YESTERDAY 16 15 1 15
MONTH TO DATE 361 360 1 380
SINCE SEP 1 361 360 1 380
SINCE JAN 1 3064 2994 70 3318
...................................................................

WIND (MPH)
HIGHEST WIND SPEED 24 HIGHEST WIND DIRECTION NE (60)
HIGHEST GUST SPEED 34 HIGHEST GUST DIRECTION NE (60)
AVERAGE WIND SPEED 17.6

SKY COVER
POSSIBLE SUNSHINE MM
AVERAGE SKY COVER 0.6

WEATHER CONDITIONS
THE FOLLOWING WEATHER WAS RECORDED YESTERDAY.
LIGHT RAIN
FOG

RELATIVE HUMIDITY (PERCENT)
HIGHEST 82 1000 AM
LOWEST 64 600 PM
AVERAGE 73

..........................................................

THE LIHUE CLIMATE NORMALS FOR TODAY
NORMAL RECORD YEAR
MAXIMUM TEMPERATURE (F) 85 89 1981
MINIMUM TEMPERATURE (F) 75 67 1965

SUNRISE AND SUNSET
SEPTEMBER 25 2026.....SUNRISE 627 AM HST SUNSET 630 PM HST
SEPTEMBER 26 2026.....SUNRISE 627 AM HST SUNSET 629 PM HST

- INDICATES NEGATIVE NUMBERS.
R INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T INDICATES TRACE AMOUNT.
```

---

### 8. Daily Climate Summary — OGG

| Field | Value |
|---|---|
| **Resource ID** | cli_daily_climate_summary_OGG |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLI&issuedby=OGG |
| **Collected** | 2026-09-25T18:17:27.321797-10:00 HST |

```text
880
CDHW42 PHFO 251245
CLIOGG

CLIMATE REPORT
NATIONAL WEATHER SERVICE HONOLULU HI
245 AM HST FRI SEP 25 2026

...................................

...THE KAHULUI/MAUI CLIMATE SUMMARY FOR SEPTEMBER 24 2026...

CLIMATE NORMAL PERIOD 1991 TO 2020
CLIMATE RECORD PERIOD 1954 TO 2026

WEATHER ITEM OBSERVED TIME RECORD YEAR NORMAL DEPARTURE LAST
VALUE (LST) VALUE VALUE FROM YEAR
NORMAL
...................................................................
TEMPERATURE (F)
YESTERDAY
MAXIMUM 87 201 PM 95 2019 90 -3 86
MINIMUM 76 230 AM 62 2006 71 5 70
AVERAGE 82 80 2 78

PRECIPITATION (IN)
YESTERDAY T 0.14 2006 0.01 -0.01 0.00
MONTH TO DATE 0.60 0.36 0.24 0.01
SINCE SEP 1 0.60 0.36 0.24 0.01
SINCE JAN 1 30.28 10.68 19.60 6.58

DEGREE DAYS
HEATING
YESTERDAY 0 0 0 0
MONTH TO DATE 0 0 0 0
SINCE SEP 1 0 0 0 0
SINCE JUL 1 0 0 0 0

COOLING
YESTERDAY 17 15 2 13
MONTH TO DATE 391 382 9 381
SINCE SEP 1 391 382 9 381
SINCE JAN 1 3175 3229 -54 3236
...................................................................

WIND (MPH)
HIGHEST WIND SPEED 29 HIGHEST WIND DIRECTION NE (40)
HIGHEST GUST SPEED 40 HIGHEST GUST DIRECTION NE (50)
AVERAGE WIND SPEED 18.1

SKY COVER
POSSIBLE SUNSHINE MM
AVERAGE SKY COVER 0.5

WEATHER CONDITIONS
THE FOLLOWING WEATHER WAS RECORDED YESTERDAY.
LIGHT RAIN

RELATIVE HUMIDITY (PERCENT)
HIGHEST 90 1200 AM
LOWEST 57 200 PM
AVERAGE 74

..........................................................

THE KAHULUI/MAUI CLIMATE NORMALS FOR TODAY
NORMAL RECORD YEAR
MAXIMUM TEMPERATURE (F) 90 95 2022
MINIMUM TEMPERATURE (F) 71 60 2011

SUNRISE AND SUNSET
SEPTEMBER 25 2026.....SUNRISE 615 AM HST SUNSET 619 PM HST
SEPTEMBER 26 2026.....SUNRISE 616 AM HST SUNSET 618 PM HST

- INDICATES NEGATIVE NUMBERS.
R INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T INDICATES TRACE AMOUNT.
```

---

### 9. Hawaii Rainfall Summary direct product

| Field | Value |
|---|---|
| **Resource ID** | hfo_rra_direct |
| **Official source** | https://forecast.weather.gov/product.php?issuedby=HFO&product=RRA&site=hfo |
| **Collected** | 2026-09-25T21:18:13.282240-10:00 HST |

```text
325
SRHW80 PHFO 260646
RRAHFO

Hawaii Rainfall Summary
National Weather Service Honolulu HI
845 PM HST Fri Sep 25 2026

:
.B HFO  0925 H  DH20 /DRH-03/PPT/DRH-06/PPQ/DRH-12/PPK/DRH-24/PPD
:
:Automated rain gage reports from around the State of Hawaii.
:These are provisional reports that have not been quality
:controlled.
:
:T=Trace Rainfall, M=Missing Data
:
:Precipitation totals ending  8 PM HST
:
:Island of Kauai                                   Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
:       Windward/Mauka Sites
MKAH1 : Makaha Ridge (RAWS)         :    0.00  /  0.00  /  0.00  /  0.00
PLRH1 : Puu Lua (RAWS)              :    0.02  /  0.02  /  0.02  /  0.02
WKRH1 : Waiakoali (USGS)            :    0.27  /  0.32  /  0.33  /  0.37
KLOH1 : Kilohana (USGS)             :    0.73  /  0.90  /  1.34  /  1.54
MCRH1 : Mohihi Crossing (USGS)      :    0.23  /  0.25  /  0.28  /  0.32
WLGH1 : Waialae (USGS)              :    0.06  /  0.06  /  0.06  /  0.07
LLMH1 : Lower Limahuli (UHM)        :    0.09  /  0.10  /  0.10  /  0.14
WNHH1 : Wainiha (12010)             :    0.18  /  0.21  /  0.22  /  0.31
WIPH1 : Waipa (UHM)                 :    0.14  /  0.15  /  0.16  /  0.25
HNIH1 : Hanalei (12009)             :    0.14  /  0.18  /  0.20  /  0.26
WLLH1 : Mount Waialeale (USGS)      :      M   /    M   /    M   /    M
PRIH1 : Princeville Airport (12011) :    0.03  /  0.05  /  0.05  /  0.07
CMGH1 : Common Ground (UHM)         :    0.09  /  0.09  /  0.09  /  0.11
HLIH1 : Hanalei (RAWS)              :    0.12  /  0.17  /  0.18  /  0.20
MLDH1 : Moloaa Dairy (RAWS)         :    0.00  /  0.00  /  0.00  /  0.00
ANHH1 : Anahola (12001)             :    0.02  /  0.02  /  0.02  /  0.02
KPIH1 : Kapahi (12003)              :    0.13  /  0.14  /  0.15  /  0.17
WLDH1 : N Wailua Ditch (USGS)       :    0.12  /  0.12  /  0.16  /  0.19
WUHH1 : Wailua (12005)              :    0.21  /  0.27  /  0.27  /  0.33
WIRH1 : Waiahi Rain Gage (USGS)     :    0.11  /  0.17  /  0.30  /  0.33
LIHH1 : Lihue Var. Stn. (12006)     :    0.20  /  0.21  /  0.21  /  0.25
HNMH1 : Hanamaulu (UHM)             :    0.15  /  0.17  /  0.22  /  0.23
HLI   : Lihue Airport (ASOS)        :    0.01  /  0.03  /  0.03  /  0.04
:       Leeward Sites
OMAH1 : Omao (12004)                :    0.18  /  0.18  /  0.21  /  0.21
LNTH1 : Lawai NTBG (UHM)            :    0.11  /  0.11  /  0.12  /  0.12
KHEH1 : Kalaheo (12008)             :    0.08  /  0.09  /  0.10  /  0.10
PAKH1 : Port Allen (HSOIS)          :    0.00  /  0.00  /  0.00  /  0.00
HNPH1 : Hanapepe (12002)            :    0.01  /  0.01  /  0.01  /  0.01
POPH1 : Puu Opae (RAWS)             :    0.00  /  0.00  /  0.00  /  0.00
WHGH1 : Waimea Heights (RAWS)       :    0.00  /  0.00  /  0.00  /  0.00
WMTH1 : Waimea Tank (12007)         :    0.00  /  0.00  /  0.00  /  0.00
MNRH1 : Mana (RAWS)                 :    0.00  /  0.00  /  0.00  /  0.00
:
:Island of Oahu                                    Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
:       Windward/Mauka Sites
KAHH1 : Kahuku (13027)              :    0.02  /  0.02  /  0.02  /  0.02
KTAH1 : Kahuku Training Area (RAWS) :    0.00  /  0.00  /  0.00  /  0.00
KFWH1 : Kii (RAWS)                  :    0.00  /  0.00  /  0.00  /  0.00
PUNH1 : Punaluu Pump (13013)        :    0.04  /  0.06  /  0.07  /  0.15
PNSH1 : Punaluu Stream (USGS)       :    0.02  /  0.08  /  0.18  /  0.24
KNRH1 : Kahana (USGS)               :    0.03  /  0.06  /  0.17  /  0.31
HAKH1 : Hakipuu Mauka (13004)       :    0.02  /  0.02  /  0.06  /  0.32
WPPH1 : Waihee Pump (13002)         :    0.01  /  0.04  /  0.05  /  0.12
WHSH1 : Waiahole (USGS)             :    0.02  /  0.04  /  0.06  /  0.10
OFRH1 : Oahu Forest NWR (USFWS)     :    0.03  /  0.03  /  0.06  /  0.11
AHUH1 : Ahuimanu Loop (13005)       :    0.02  /  0.04  /  0.05  /  0.07
HRRH1 : Heeia NERR (NOAA/NOS)       :    0.01  /  0.05  /  0.07  /  0.12
LULH1 : Luluku (13016)              :    0.00  /  0.00  /  0.00  /  0.00
NRSH1 : Nuuanu Res No. 1 (UHM)      :    0.00  /  0.00  /  0.02  /  0.09
KWIH1 : Kalawahine (UHM)            :    0.01  /  0.01  /  0.06  /  0.23
LYOH1 : Lyon (UHM)                  :    0.00  /  0.00  /  0.08  /  0.33
MNLH1 : Manoa Lyon Arboretum (13023):    0.00  /  0.01  /  0.03  /  0.27
STVH1 : St. Stephens (13006)        :    0.00  /  0.02  /  0.04  /  0.16
MAUH1 : Maunawili (13008)           :      M   /    M   /    M   /    M
OFSH1 : Olomana Fire Station (13009):    0.00  /  0.00  /  0.00  /  0.04
WMLH1 : Waimanalo (13011)           :    0.00  /  0.00  /  0.01  /  0.07
BELH1 : Bellows AFS (HSOIS)         :    0.00  /  0.00  /  0.00  /  0.00
KMHH1 : Kamehame (13012)            :    0.00  /  0.00  /  0.00  /  0.08
HAJH1 : Hawaii Kai Golf Crse (13015):    0.00  /  0.00  /  0.00  /  0.17
:       Leeward/Central Sites
KUXH1 : Kaluanui (UHM)              :    0.00  /  0.01  /  0.04  /  0.13
NIUH1 : Niu Valley (13001)          :    0.00  /  0.00  /  0.02  /  0.24
PFSH1 : Palolo Fire Station (13010) :    0.00  /  0.00  /  0.03  /  0.15
HNL   : Honolulu Airport (ASOS)             See note at bottom  :
MOAH1 : Moanalua (13003)            :    0.01  /  0.02  /  0.03  /  0.10
MOGH1 : Moanalua RG (USGS)          :    0.04  /  0.15  /  0.16  /  0.39
TNLH1 : Tunnel RG (USGS)            :    0.01  /  0.11  /  0.19  /  0.39
PACH1 : Palisades (13020)           :    0.01  /  0.02  /  0.02  /  0.05
WAWH1 : Waiawa C.F. (13025)         :    0.02  /  0.02  /  0.03  /  0.03
MITH1 : Mililani (13022)            :    0.01  /  0.01  /  0.01  /  0.01
SCBH1 : Schofield Barracks (RAWS)   :    0.00  /  0.00  /  0.00  /  0.00
SCEH1 : Schofield East (RAWS)       :      M   /    M   /    M   /    M
WAFH1 : Wheeler Airfield            :    0.04  /  0.04  /  0.04  /  0.04
POAH1 : Poamoho (13018)             :    0.00  /  0.00  /  0.00  /  0.00
KRGH1 : Kalahee Ridge (UHM)         :    0.03  /  0.03  /  0.06  /  0.06
KMRH1 : Kamananui Stream (USGS)     :    0.14  /  0.17  /  0.20  /  0.27
PPRH1 : Pupukea Road (USGS)         :    0.11  /  0.13  /  0.16  /  0.21
PMHH1 : Poamoho RG 1 (USGS)         :    0.04  /  0.07  /  0.15  /  0.41
DLGH1 : Dillingham (RAWS)           :    0.00  /  0.00  /  0.00  /  0.00
AALH1 : Kaala (UHM)                 :    0.06  /  0.14  /  0.25  /  0.29
PECH1 : Waipio (13019)              :    0.00  /  0.00  /  0.00  /  0.00
KUNH1 : Kunia Substation (13021)    :    0.00  /  0.00  /  0.00  /  0.00
HOFH1 : Honouliuli (RAWS)           :    0.00  /  0.00  /  0.00  /  0.00
PTWH1 : Ewa Beach USGS (13024)      :    0.00  /  0.00  /  0.00  /  0.00
HJR   : Kalaeloa Airport (ASOS)             See note at bottom  :
PLHH1 : Palehua (RAWS)              :    0.01  /  0.01  /  0.02  /  0.02
LUAH1 : Lualualei (13017)           :    0.00  /  0.00  /  0.00  /  0.00
WNVH1 : Waianae Valley (RAWS)       :    0.00  /  0.00  /  0.00  /  0.00
WBHH1 : Waianae Boat Harbor (HSOIS) :    0.00  /  0.00  /  0.00  /  0.00
WAIH1 : Waianae (13014)             :      M   /    M   /    M   /    M
MKHH1 : Makaha Stream (USGS)        :    0.00  /  0.00  /  0.00  /  0.01
MKRH1 : Makua Range (RAWS)          :    0.00  /  0.00  /  0.00  /  0.00
KKRH1 : Kuaokala (RAWS)             :    0.00  /  0.00  /  0.00  /  0.00
:
:Island of Molokai                                 Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
KOPH1 : Keopukaloa (UHM)            :    0.01  /  0.01  /  0.01  /  0.01
HOMH1 : Honolimaloo (UHM)           :    0.04  /  0.04  /  0.04  /  0.10
KMLH1 : Kamalo (14013)              :    0.00  /  0.00  /  0.00  /  0.00
MKPH1 : Makapulapai (RAWS)          :    0.00  /  0.00  /  0.00  /  0.02
PAFH1 : Puu Alii (RAWS)             :    0.06  /  0.07  /  0.08  /  0.59
MLKH1 : Molokai 1 (RAWS)            :      M   /    M   /    M   /    M
KACH1 : Kaunakakai Mauka (14004)    :    0.00  /  0.00  /  0.00  /  0.00
HMK   : Molokai Airport (ASOS)      :    0.00  /  0.00  /  0.00  /    T
:
:Island of Lanai                                   Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
LANH1 : Lanai City (14012)          :    0.00  /  0.00  /  0.00  /  0.00
HNY   : Lanai Airport (ASOS)        :    0.00  /  0.00  /  0.00  /  0.00
LNIH1 : Lanai 1 (RAWS)              :    0.00  /  0.00  /  0.00  /  0.00
:
:Island of Kahoolawe                               Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
KAOH1 : Kaneloa (RAWS)              :      M   /    M   /    M   /    M
:
:Island of Maui                                    Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
:       Windward Sites
HNAH1 : Hana Airport (HSOIS)        :      M   /    M   /    M   /    M
WWKH1 : West Wailuaiki (USGS)       :    0.15  /  0.51  /  0.86  /  1.85
EBYH1 : EMI Baseyard (UHM)          :    0.02  /  0.04  /  0.04  /  0.31
AIKH1 : Haiku (14001)               :    0.01  /  0.01  /  0.01  /  0.08
HOG   : Kahului Airport (ASOS)      :    0.00  /  0.00  /  0.00  /    T
WUKH1 : Wailuku (14007)             :    0.00  /  0.00  /  0.00  /  0.00
KHKH1 : Kahakuloa (14002)           :    0.00  /  0.00  /  0.00  /  0.00
PKKH1 : Puu Kukui (USGS)            :    0.11  /  0.16  /  0.90  /  2.50
:       Leeward/Upcountry Sites
NKUH1 : Na Kula (RAWS)              :    0.00  /  0.00  /  0.00  /  0.00
KPNH1 : Kepuni (USGS)               :    0.00  /  0.00  /  0.00  /  0.00
PILH1 : Piiholo (UHM)               :    0.07  /  0.07  /  0.09  /  0.19
WKTH1 : Waikamoi Treeline (UHM)     :    0.21  /  0.22  /  0.24  /  0.53
PUKH1 : Pukalani (14006)            :    0.00  /  0.00  /  0.00  /  0.00
KBSH1 : Kula Branch Station (14008) :      M   /    M   /    M   /    M
KLGH1 : Kula Ag (UHM)               :    0.00  /  0.00  /  0.00  /  0.00
PHQH1 : Park HQ (UHM)               :    0.03  /  0.03  /  0.03  /  0.03
NNEH1 : Nene Nest (UHM)             :    0.03  /  0.03  /  0.03  /  0.03
SUMH1 : Summit (UHM)                :    0.00  /  0.00  /  0.00  /  0.00
KLFH1 : Kula 1 (RAWS)               :    0.00  /  0.00  /  0.00  /  0.00
KKNH1 : Kahikinui 1 (RAWS)          :    0.00  /  0.00  /  0.00  /  0.00
KMEH1 : Kamehamenui 1 (RAWS)        :    0.00  /  0.00  /  0.00  /  0.00
KKEH1 : Keokea (UHM)                :    0.00  /  0.00  /  0.00  /  0.00
ULUH1 : Ulupalakua (14003)          :    0.00  /  0.00  /  0.00  /  0.00
LPOH1 : Lipoa (UHM)                 :    0.00  /  0.00  /  0.00  /  0.00
KHIH1 : Kihei #2 (14009)            :      M   /    M   /  0.00  /    M
KPDH1 : Kealia Pond (USFWS)         :    0.00  /  0.00  /  0.00  /  0.00
WCCH1 : Waikapu Country Club (14005):    0.00  /  0.00  /  0.00  /  0.00
HULH1 : Hanaula (UHM)               :    0.00  /  0.00  /  0.01  /  0.14
OLUH1 : Olowalu (UHM)               :    0.00  /  0.00  /  0.01  /  0.02
LAHH1 : Lahainaluna (14011)         :    0.00  /  0.00  /  0.00  /  0.00
LWTH1 : Lahaina WTP (UHM)           :    0.00  /  0.00  /  0.00  /  0.00
HOOH1 : Honolua (UHM)               :    0.00  /  0.00  /  0.00  /  0.05
:
:Island of Hawaii                                  Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
:       Windward Sites
UPLH1 : Upolu Airport (HSOIS)       :    0.02  /  0.05  /  0.16  /  0.20
KMMH1 : Kaluamakani (UHM)           :    0.15  /  0.30  /  0.30  /  0.30
KWSH1 : Kawainui Stream (USGS)      :    1.37  /  1.91  /  2.74  /  4.20
KUUH1 : Kamuela Upper (15002)       :    0.45  /  0.74  /  1.06  /  1.67
KMUH1 : Kamuela (15005)             :    0.21  /  0.45  /  0.46  /  0.56
HNKH1 : Honokaa (15010)             :    1.01  /  1.58  /  1.71  /  2.39
PMLH1 : Puu Mali (RAWS)             :    0.17  /  0.45  /  0.47  /  0.47
WPNH1 : Waipunalei (UHM)            :      M   /    M   /  0.20  /    M
KNKH1 : Kanakaleonui (UHM)          :    0.85  /  1.86  /  2.12  /  2.14
LPHH1 : Laupahoehoe PD (15001)      :    0.00  /  0.83  /  1.35  /  1.82
LAUH1 : Laupahoehoe (UHM)           :    1.86  /  3.67  /  4.19  /  4.96
SPNH1 : Spencer (UHM)               :    0.17  /  1.22  /  2.02  /  4.60
HKUH1 : Hakalau (RAWS)              :    1.07  /  2.10  /  2.32  /  2.49
KLXH1 : Kulaimano (UHM)             :    0.00  /  0.31  /  0.89  /  1.23
NLIH1 : Honolii Stream (USGS)       :    0.09  /  0.72  /  1.47  /  2.31
SDQH1 : Saddle Quarry (USGS)        :    0.98  /  1.71  /  2.28  /  2.67
PIOH1 : Piihonua (UHM)              :    0.44  /  0.94  /  1.75  /  2.89
PIIH1 : Piihonua (15016)            :    0.00  /  0.00  /  0.01  /  0.03
IPIH1 : IPIF (UHM)                  :    0.00  /  0.35  /  1.13  /  1.54
WKAH1 : Waiakea Uka (15017)         :    0.04  /  0.30  /  1.20  /  1.70
WEXH1 : Waiakea Exp Stn (NOAA/CRN)  :    0.00  /  0.25  /  0.72  /  0.83
HTO   : Hilo Airport (ASOS)         :      T   /  0.08  /  0.89  /  1.18
PHAH1 : Pahoa (15015)               :    0.00  /  0.29  /  1.36  /  1.78
PAOH1 : Pahoa (UHM)                 :    0.01  /  0.44  /  1.12  /  1.40
MTVH1 : Mountain View (15014)       :    0.15  /  0.63  /  1.76  /  2.18
GLNH1 : Glenwood (15013)            :    0.86  /  1.56  /  2.23  /  3.09
:       Leeward Sites
MOBH1 : Mauna Loa Ob Stn (NOAA/CRN) :    0.21  /  0.46  /  0.56  /  0.56
NHKH1 : Nahuku (UHM)                :    0.67  /  1.52  /  1.95  /  2.24
KKUH1 : Keaumo (RAWS)               :    0.35  /  0.99  /  1.02  /  1.02
KMOH1 : Kealakomo (RAWS)            :    0.00  /  0.17  /  0.19  /  0.20
PLIH1 : Pali 2 (RAWS)               :    0.06  /  0.13  /  0.13  /  0.13
KPRH1 : Kapapala (RAWS)             :    0.00  /  0.02  /  0.02  /  0.04
KAYH1 : Kapapala Ranch (15003)      :    0.00  /  0.00  /  0.00  /  0.00
PPLH1 : Pahala (15004)              :    0.00  /  0.06  /  0.06  /  0.13
KIOH1 : Kaiholena (UHM)             :      M   /    M   /    M   /    M
NENH1 : Nene Cabin (RAWS)           :    0.29  /  0.64  /  0.70  /  0.70
SOPH1 : South Point (HSOIS)         :    0.10  /  0.17  /  0.18  /  0.19
LKHH1 : Lower Kahuku (RAWS)         :    0.23  /  0.66  /  0.68  /  0.69
KRCH1 : Kahuku Ranch (RAWS)         :    0.01  /  0.01  /  0.01  /  0.01
KOMH1 : Kona Hema (UHM)             :    0.00  /  0.01  /  0.01  /  0.02
PHRH1 : Puho CS (RAWS)              :    0.00  /  0.00  /  0.00  /  0.00
HAUH1 : Honaunau (15007)            :    0.01  /  0.01  /  0.01  /  0.02
KLEH1 : Kealakekua (15008)          :    0.00  /  0.00  /  0.00  /  0.02
WIHH1 : Waiaha Stream (15009)       :    0.01  /  0.01  /  0.01  /  0.01
KOUH1 : Keahuolu (UHM)              :    0.01  /  0.01  /  0.01  /  0.01
KHOH1 : Kaloko-Honokohau (RAWS)     :    0.00  /  0.00  /  0.00  /  0.00
HKO   : Kona Intl Airport (ASOS)    :    0.00  /  0.00  /  0.00  /  0.00
PLMH1 : Palamanui (UHM)             :    0.00  /  0.00  /  0.01  /  0.01
KIRH1 : Kiholo RG (USGS)            :    0.00  /  0.00  /  0.00  /  0.00
KPLH1 : Kaupulehu (RAWS)            :    0.00  /  0.00  /  0.00  /  0.00
PULH1 : Puuanahulu (RAWS)           :    0.00  /  0.00  /  0.00  /  0.00
MMLH1 : Mamalahoa (UHM)             :    0.00  /  0.00  /  0.00  /  0.00
PWWH1 : Puu Waawaa (RAWS)           :    0.00  /  0.00  /  0.00  /  0.00
PWAH1 : Puu Waawaa (UHM)            :    0.00  /  0.00  /  0.00  /  0.00
KIUH1 : Kaiaulu Puu Waawaa (UHM)    :    0.00  /  0.00  /  0.00  /  0.00
PKAH1 : Pohakuloa Kipuka Alala RAWS :    0.00  /  0.00  /  0.00  /  0.00
PTRH1 : Pohakuloa Range 17 (RAWS)   :    0.00  /  0.00  /  0.00  /  0.00
PKWH1 : Pohakuloa West (RAWS)       :    0.00  /  0.00  /  0.00  /  0.00
PKMH1 : Pohakuloa Keamuku (RAWS)    :    0.00  /  0.00  /  0.00  /  0.00
AHMH1 : Ahumoa (RAWS)               :    0.00  /  0.00  /  0.00  /  0.00
WHIH1 : Waikii (15011)              :    0.00  /  0.00  /  0.00  /  0.00
LLAH1 : Lalamilo (UHM)              :    0.09  /  0.13  /  0.17  /  0.23
WKVH1 : Waikoloa (RAWS)             :    0.00  /  0.00  /  0.00  /  0.00
PERH1 : Puhe CS (RAWS)              :    0.00  /  0.00  /  0.00  /  0.00
KHRH1 : Kohala Ranch (RAWS)         :    0.00  /  0.00  /  0.00  /  0.00
KASH1 : Kahua Ranch (15006)         :    0.22  /  0.39  /  0.50  /  0.64
KEHH1 : Kehena (UHM)                :    0.82  /  1.18  /  1.69  /  2.29
PLAH1 : Puuloa (UHM)                :    0.22  /  0.30  /  0.30  /  0.30
.END

Service Note
Due to software decoder issues, rainfall totals for Honolulu Airport (PHNL)
and Kalaeloa Airport (PHJR) are temporarily unavailable.
Daily totals for both sites are available in the CF6 product on the web at
https://www.weather.gov/wrh/Climate?wfo=hfo
Select the Observed Weather tab and choose the Preliminary Monthly Climate Data
(CF6) product.
We apologize for the inconvenience and hope to have this issue resolved soon.

$$
```

---

### 10. HFO statewide surf observations direct page

| Field | Value |
|---|---|
| **Resource ID** | hfo_surf_reports_direct |
| **Official source** | https://www.weather.gov/hfo/surfreports |
| **Collected** | 2026-09-25T21:18:15.325084-10:00 HST |

```text
948
SXHW80 PHFO 260115
OMRHFO

SURF OBSERVATIONS
NATIONAL WEATHER SERVICE HONOLULU HI
315 PM HST FRI SEP 25 2026

FULL FACE SURF OBSERVATIONS ARE TAKEN BY COUNTY LIFE GUARDS AND
COOPERATIVE OBSERVERS AND RELAYED TO THE NATIONAL WEATHER SERVICE
FOR DISSEMINATION. THESE OBSERVATIONS ARE NOT QUALITY CONTROLLED.

HIZ003-004-029>031-260100-
KAUAI-

LOCATION        TIME   SURF HEIGHT DIR   PER                  REMARKS
KEE          1235 PM           2-5  NE     9
HAENA        1235 PM           2-5  NE     9
HANALEI      1235 PM           0-2
ANAHOLA      1235 PM           3-6 ENE     9
KEALIA       1235 PM          6-10 ENE    10
LYDGATE      1235 PM          4-8+ ENE    10
POIPU        1235 PM           2-4
SALT POND    1235 PM           2-4
KEKAHA       1235 PM           1-3
$$

HIZ006-007-009>011-032>036-260100-
OAHU-

LOCATION        TIME   SURF HEIGHT DIR PER         WIND      REMARKS
DIAMOND HEAD
SUNSET
WAIKIKI      1145 AM           0-1            ENE 10-15       CANOES
SANDY BEACH  1145 AM           2-3            ENE 15-20  SHORE BREAK
MAKAPUU      1145 AM           4-6            ENE 10-15
EHUKAI       1145 AM           0-1             NE 10-15
MAKAHA       1145 AM           0-1               VRB 05
$$

HIZ015>018-022-045>050-260100-
MAUI-MOLOKAI-LANAI-KAHOOLAWE-

LOCATION        TIME   SURF HEIGHT   DIR         WIND      REMARKS
KANAHA       1108 AM           1-3          NE 10-20+  PARTLY CLDY
BALDWIN SHOR 1109 AM           1-2           NE 15-25  PARTLY CLDY
BALDWIN OUTE 1109 AM           3-6           NE 15-25  PARTLY CLDY
HOOKIPA      1110 AM           1-4           NE 10-20  MOSTLY CLDY
KAMAOLE I    1111 AM           1-2           NE 10-20        SUNNY
KAMAOLE III  1112 AM           0-1           NE 20-30  PARTLY CLDY
HANAKAOO
FLEMING
$$

HIZ023-026>028-051>054-260100-
BIG ISLAND OF HAWAII-

LOCATION        TIME   SURF HEIGHT   DIR         WIND      REMARKS
RICHARDSONS  1101 AM           2-3     E      VRB 0-5  OVERCAST/RA
HONOLII      1102 AM           3-5            L/V 0-5         RAIN
PUNALU`U
ISAAC HALE   1103 AM          5-6+            NE 5-10         RAIN
HAPUNA
KAHALUU      1105 AM           3-5    NW      L/V 0-5     OVERCAST
MAGIC SANDS  1106 AM           0-1            L/V 0-5     OVERCAST
KUA BAY      1107 AM    1-2 OCNL 3           SW 10-15     OVERCAST
$$

LEGEND
   SURF HEIGHT              - Reported in feet
   WIND AND SWELL DIRECTION - Reported in 16 pt compass
   PERIOD /PER/             - Reported in seconds
   VISIBILITY /VIS/         - Reported in statute miles
   CLARITY                  - Water clarity
   TIME                     - Hawaiian Standard Time
   WIND SPEED               - Reported in miles per hour
   + /IN SURF HEIGHT/       - Occasionally higher sets
   0 /IN SURF HEIGHT/       - Flat

$$
```

---

### 11. High Seas Forecast N. Pacific

| Field | Value |
|---|---|
| **Resource ID** | hsf_high_seas_npac |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=HSF&issuedby=NP |
| **Collected** | 2026-09-25T17:19:23.329650-10:00 HST |

```text
597
FZPN40 PHFO 260312
HSFNP

HIGH SEAS FORECAST
NATIONAL WEATHER SERVICE HONOLULU HI
0500 UTC SAT SEP 26 2026

SUPERSEDED BY NEXT ISSUANCE IN 6 HOURS

SEAS GIVEN AS SIGNIFICANT WAVE HEIGHT...WHICH IS THE AVERAGE HEIGHT
OF THE HIGHEST 1/3 OF THE WAVES. INDIVIDUAL WAVES MAY BE MORE THAN
TWICE THE SIGNIFICANT WAVE HEIGHT.

THIS HIGH SEAS FORECAST USES 1-MINUTE AVERAGE WINDS WHICH MAY BE
HIGHER THAN 10-MINUTE AVERAGE WINDS.

SECURITE

NORTH PACIFIC EQUATOR TO 30N BETWEEN 140W AND 180W

SYNOPSIS VALID 0000 UTC SEP 26 2026.
24 HOUR FORECAST VALID 0000 UTC SEP 27 2026.
48 HOUR FORECAST VALID 0000 UTC SEP 28 2026.

.WARNINGS.

...HURRICANE WARNING...
.HURRICANE NOLO NEAR 16.9N 155.3W 975 MB AT 0300 UTC SEP 26
MOVING N OR 010 DEG AT 3 KT. MAXIMUM SUSTAINED WINDS 90 KT GUSTS
110 KT. TROPICAL STORM FORCE WINDS WITHIN 120 NM N
SEMICIRCLE...110 NM SE QUADRANT AND 90 NM SW QUADRANT. WINDS 20 TO
34 KT ELSEWHERE FROM 19N TO 13N BETWEEN 157W AND 152W. SEAS 4 M
OR GREATER WITHIN 150 NM OF CENTER EXCEPT 180 NM SW QUADRANT WITH
SEAS TO 7 M. SEAS 2.5 TO 4 M ELSEWHERE DESCRIBED IN SYNOPSIS AND
FORECAST SECTION.
.24 HOUR FORECAST HURRICANE NOLO NEAR 17.1N 156.4W. MAXIMUM
SUSTAINED WINDS 95 KT GUSTS 115 KT. TROPICAL STORM FORCE WINDS
WITHIN 130 NM N SEMICIRCLE...90 NM SE QUADRANT AND 80 NM SW
QUADRANT. WINDS 20 TO 34 KT ELSEWHERE FROM 19N TO 14N BETWEEN 157W
AND 153W. SEAS 4 M OR GREATER FROM 19N TO 14N BETWEEN 158W AND
153W WITH SEAS TO 7.5 M. SEAS 2.5 TO 4 M ELSEWHERE DESCRIBED IN
SYNOPSIS AND FORECAST SECTION.
.48 HOUR FORECAST HURRICANE NOLO NEAR 16.9N 159.8W. MAXIMUM
SUSTAINED WINDS 110 KT GUSTS 135 KT. TROPICAL STORM FORCE WINDS
WITHIN 150 NM NE QUADRANT...80 NM SE QUADRANT...70 NM SW
QUADRANT...AND 120 NM NW QUADRANT. WINDS 20 TO 34 KT ELSEWHERE 19N
TO 13N BETWEEN 157W AND 153W. SEAS 4 M OR GREATER FROM 20N TO 13N
BETWEEN 162W AND 156W WITH SEAS TO 8.5 M. SEAS 2.5 TO 4 M
ELSEWHERE DESCRIBED IN SYNOPSIS AND FORECAST SECTION.

FORECAST WINDS IN AND NEAR ACTIVE TROPICAL CYCLONES SHOULD BE
USED WITH CAUTION DUE TO UNCERTAINTY IN FORECAST TRACK...SIZE AND
INTENSITY.

.SYNOPSIS AND FORECAST.

.TROUGH 26N170W 20N172W MOVING W 10 KT.
.24 HOUR FORECAST TROUGH 26N176W 22N178W.
.48 HOUR FORECAST TROUGH MOVED W OF AREA.

.WINDS 20 TO 34 KT FROM 26N TO 19N BETWEEN 162W AND 148W.
.24 HOUR FORECAST WINDS 20 TO 34 KT FROM 26N TO 19N BETWEEN 165W
AND 146W.
.48 HOUR FORECAST WINDS 20 TO 34 KT FROM 26N TO 19N BETWEEN 168W
AND 150W.

.WINDS 20 KT OR LESS OVER REMAINDER OF FORECAST AREA.

.SEAS 2.5 TO 4 M FROM 25N TO 09N BETWEEN 162W AND 145W.
.24 HOUR FORECAST SEAS 2.5 TO 4 M E OF LINE 24N140W 26N151W
29N159W 28N167W 12N161W 11N149W 14N140W.
.48 HOUR FORECAST SEAS 2.5 TO 4 M N OF LINE 30N167W 25N172W
19N171W 10N159W 14N154W 07N140W.

.SEAS 2.5 M OR LOWER OVER REMAINDER OF FORECAST AREA.

.MONSOON TROUGH 14N140W 14N149W...AND 07N173W 06N176W 08N180W.

.ISOLATED MODERATE TSTMS S OF 06N BETWEEN 177W AND 167W.

.FORECASTER TROTTER. HONOLULU HI.
```

---

### 12. Hourly Wind/Precip Observations

| Field | Value |
|---|---|
| **Resource ID** | oso_hourly_obs |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=OSO&issuedby=HFO |
| **Collected** | 2026-09-25T20:53:12.372940-10:00 HST |

```text
583
SXHW50 PHFO 260044
OSOHFO

Hawaii Wind Da a
Na ional Wea her Service Honolulu HI
243 PM HST Fri Sep 25 2026

W I N D D A T A
----------------------
IN KNOTS
ID Loca ion Da e Time DIR SPD GUST
-------- ------------------------- ------- -(HST)- ---- ---- ----
0000LLMH1 Lower Limahuli Kauai 25Sep26 14:15 310 4 10
0000CMGH1 Common Ground Kauai 25Sep26 14:15 90 8 13
0000HLIH1 Hanalei Kauai 25Sep26 13:41 110 10 18
0000MLDH1 Moloaa Dairy Kauai 25Sep26 12:45 90 3 11
0000HNMH1 Hanamaulu Kauai 25Sep26 14:15 40 8 16
0000PHLI Lihue Kauai 25Sep26 14:00 40 20 23
0000NWWH1 Nawiliwili NOS Kauai 25Sep26 14:30 30 16 23
0000POIH1 Poipu Kauai MSG MSG MSG MSG
0000LNTH1 Lawai NTBG Kauai 25Sep26 14:15 70 18 28
0000PAKH1 Por Allen Kauai 25Sep26 14:00 80 17 29
0000MKAH1 Makaha Ridge Kauai 25Sep26 14:11 60 4 15
0000MNRH1 Mana Kauai 25Sep26 14:34 250 4 11
0000PHBK Barking Sands Kauai 25Sep26 14:00 240 6 MSG
0000PLRH1 Puu Lua Kauai 25Sep26 14:35 90 7 18
0000POPH1 Puu Opae Kauai 25Sep26 14:34 200 4 20
0000WHGH1 Waimea Heigh s Kauai 25Sep26 14:35 30 6 10

0000KRGH1 Kalahee Ridge Oahu 25Sep26 14:10 40 8 20
0000KAHH1 Kahuku Oahu MSG MSG MSG MSG
0000KTAH1 Kahuku Trng Oahu 25Sep26 13:59 100 3 22
0000KFWH1 Kii Oahu 25Sep26 13:45 70 15 23
0000OFRH1 Oahu Fores NWR Oahu 25Sep26 14:36 80 27 44
0000KWMH1 Kaaawa Makai Oahu 25Sep26 14:15 40 5 9
0000PHNG Kaneohe MCBH Oahu 25Sep26 14:00 50 13 21
0000MOKH1 Mokuoloe Is NOS Oahu 25Sep26 14:30 50 14 17
0000BELH1 Bellows AFS Oahu 25Sep26 14:15 40 17 MSG
0000KUXH1 Kaluanui Oahu 25Sep26 14:15 190 5 12
0000LYOH1 Lyon Oahu 25Sep26 14:15 310 5 18
0000NRSH1 Nuuanu Res No 1 Oahu 25Sep26 14:15 360 7 18
0000PHNL Honolulu AP Oahu 25Sep26 14:00 70 12 24
0000OOUH1 Honolulu Hbr NOS Oahu 25Sep26 14:24 10 6 15
0000HOFH1 Honouliuli PHB Oahu 25Sep26 14:41 60 12 21
0000SCBH1 Schofield Brks Oahu 25Sep26 13:57 60 5 16
0000SCEH1 Schofield Eas Oahu MSG MSG MSG MSG
0000HWLH1 HECO Wilikina Oahu 25Sep26 14:30 30 4 10
0000PHJR Kalaeloa Oahu 25Sep26 14:18 50 9 25
0000HFHH1 HECO Farring on Oahu 25Sep26 14:30 70 11 22
0000HPLH1 HECO Palehua Oahu 25Sep26 14:30 60 10 22
0000HPDH1 HECO Palehua 2 Oahu 25Sep26 14:30 60 17 25
0000HPHH1 HECO Palehua 3 Oahu 25Sep26 14:30 50 9 19
0000HPRH1 HECO Paakea Oahu 25Sep26 14:30 30 9 25
0000HLRH1 HECO Lualualei Oahu 25Sep26 14:30 50 11 22
0000HWVH1 HECO Waianae Vly Oahu 25Sep26 14:30 10 7 17
0000PLHH1 Palehua Oahu 25Sep26 14:36 50 0 0
0000WNVH1 Waianae Valley Oahu 25Sep26 14:37 60 8 30
0000HHSH1 HECO Ala Hema S Oahu 25Sep26 14:30 90 6 12
0000WBHH1 Waianae Harbor Oahu MSG MSG MSG MSG
0000HKRH1 HECO Kili Dr Oahu 25Sep26 14:30 340 8 16
0000HMVH1 HECO Makaha Vly Oahu 25Sep26 14:30 340 8 20
0000MKRH1 Makua Range Oahu 25Sep26 13:58 70 14 29
0000KKRH1 Kuaokala Oahu 25Sep26 14:36 30 14 36
0000AALH1 Kaala Oahu 25Sep26 14:15 60 6 13
0000HFRH1 HECO Farring on2 Oahu 25Sep26 14:30 60 7 15
0000HFYH1 HECO Farring on3 Oahu 25Sep26 14:30 70 17 23
0000DLGH1 Dillingham Oahu 25Sep26 13:49 50 8 16

0000MKPH1 Makapulapai Molokai 25Sep26 14:15 90 22 34
0000PAFH1 Puu Alii Molokai 25Sep26 14:22 90 3 13
0000HOMH1 Honolimaloo Molokai 25Sep26 14:15 80 8 15
0000KOPH1 Keopukaloa Molokai 25Sep26 14:15 90 13 19
0000MLKH1 Molokai 1 Molokai MSG MSG MSG MSG
0000MMPH1 MECO Makaena Molokai 25Sep26 14:30 80 11 25
0000MKYH1 MECO Kalae Hwy Molokai 25Sep26 14:30 80 9 20
0000PHMK Molokai AP Molokai 25Sep26 14:00 80 16 32
0000ANPH1 Anapuka Molokai 25Sep26 14:15 60 20 31

0000LNIH1 Lanai 1 Lanai 25Sep26 14:37 60 0 2

0000KAOH1 Kaneloa Kahoolawe MSG MSG MSG MSG

0000PHOG Kahului AP Maui 25Sep26 14:00 40 22 32
0000KLIH1 Kahului Hbr NOS Maui 25Sep26 14:24 50 15 23
0000MHRH1 MECO Hansen Rd Maui 25Sep26 14:30 30 19 30
0000MHKH1 MECO Haleakala Hwy Maui 25Sep26 14:30 30 23 33
0000MMKH1 MECO Makawao Maui 25Sep26 14:30 100 13 27
0000MKTH1 MECO Kula 2 Maui 25Sep26 14:30 90 11 24
0000PILH1 Piiholo Maui 25Sep26 14:15 100 6 17
0000EBYH1 EMI Baseyard Maui 25Sep26 14:10 100 1 5
0000HNAH1 Hana Maui MSG MSG MSG MSG
0000NKUH1 Na Kula Maui 25Sep26 14:35 100 30 48
0000AWAH1 Auwahi Maui MSG MSG MSG MSG
0000KLFH1 Kula 1 Maui 25Sep26 13:48 310 5 9
0000KKNH1 Kahikinui 1 Maui 25Sep26 14:34 150 3 11
0000KMEH1 Kamehamenui 1 Maui 25Sep26 13:48 310 3 9
0000SUMH1 Summi Maui 25Sep26 14:15 80 7 10
0000NNEH1 Nene Nes Maui 25Sep26 14:15 130 2 5
0000PHQH1 Park HQ Maui 25Sep26 14:15 70 2 8
0000WKTH1 Waikamoi Treeline Maui 25Sep26 14:15 130 4 10
0000MCTH1 MECO Cra er Rd Maui 25Sep26 14:30 300 2 4
0000KLGH1 Kula Ag Maui 25Sep26 14:15 280 3 7
0000MWAH1 MECO Waipoli Rd Maui 25Sep26 14:30 270 2 5
0000KKEH1 Keokea Maui 25Sep26 14:15 290 2 5
0000MKUH1 MECO Kula Maui 25Sep26 14:30 200 5 9
0000PHUH1 Pulehu Maui 25Sep26 14:15 220 5 11
0000MNDH1 MECO Naalaea Rd Maui 25Sep26 14:30 210 5 9
0000MURH1 MECO Ulupalakua Maui 25Sep26 14:30 180 9 15
0000LPOH1 Lipoa Maui 25Sep26 14:15 190 8 15
0000MVHH1 MECO Ve erans Hwy Maui 25Sep26 14:30 330 20 29
0000KPDH1 Kealia Pond Maui 25Sep26 14:20 20 20 34
0000MMAH1 MECO Maalaea Maui 25Sep26 14:30 360 17 30
00000P36 Maalaea Bay Maui 25Sep26 14:15 0 0 0
0000HULH1 Hanaula Maui 25Sep26 14:15 60 8 27
0000OLUH1 Olowalu Maui 25Sep26 14:15 60 7 20
0000MMMH1 MECO Mamane Pl Maui 25Sep26 14:30 320 19 27
0000MHOH1 MECO Honoapiilani Maui 25Sep26 14:30 10 27 35
0000MHHH1 MECO Honoapiilani2 Maui 25Sep26 14:30 340 15 25
0000MKEH1 MECO Kealaloloa Rg Maui 25Sep26 14:30 10 29 41
0000MUGH1 MECO Ukumehame Gul Maui 25Sep26 14:30 360 18 34
0000MOOH1 MECO Olowalu Maui 25Sep26 14:30 50 16 37
0000OLUH1 Olowalu Maui 25Sep26 14:15 60 7 20
0000MLPH1 MECO Launiupoko Maui 25Sep26 14:30 260 3 8
0000MLTH1 MECO Launiupoko 2 Maui 25Sep26 14:30 50 16 28
0000MLRH1 MECO Lahainaluna Maui 25Sep26 14:30 220 4 8
0000LWTH1 Lahaina WTP Maui 25Sep26 14:15 240 5 7
0000MKNH1 MECO Kaanapali Maui 25Sep26 14:30 230 5 9
0000PHJH Kapalua-W Maui Maui 25Sep26 14:00 30 20 30
0000HOOH1 Honolua Maui 25Sep26 14:15 120 12 28

0000UPLH1 Upolu Airpor Hawaii 25Sep26 14:15 90 15 23
0000KMMH1 Kaluamakani Hawaii 25Sep26 14:15 50 16 24
0000PMLH1 Puu Mali Hawaii 25Sep26 14:00 90 20 30
0000KNKH1 Kanakaleonui Hawaii 25Sep26 14:15 90 5 7
0000WPNH1 Waipunalei Hawaii 25Sep26 13:30 140 3 10
0000LAUH1 Laupahoehoe Hawaii 25Sep26 14:15 100 6 12
0000SPNH1 Spencer Hawaii 25Sep26 14:15 120 6 11
0000HKUH1 Hakalau Hawaii 25Sep26 13:45 100 3 10
0000KLXH1 Kulaimano Hawaii 25Sep26 14:15 0 2 5
0000PIOH1 Piihonua Hawaii 25Sep26 14:15 50 1 3
0000PHTO Hilo AP Hawaii 25Sep26 14:16 320 6 MSG
0000ILOH1 Hilo Hbr NOS Hawaii 25Sep26 14:24 360 8 10
0000IPIH1 IPIF Hawaii 25Sep26 14:15 30 3 5
0000WEXH1 Waiakea Exp S n Hawaii 25Sep26 14:00 MSG 1 4
0000KEUH1 Keaau Hawaii 25Sep26 14:15 340 3 7
0000PAOH1 Pahoa Hawaii 25Sep26 14:15 20 1 5
0000NHKH1 Nahuku Hawaii 25Sep26 14:15 20 14 25
0000KKUH1 Keaumo Hawaii 25Sep26 14:34 20 12 20
0000MOBH1 Mauna Loa Obs Hawaii 25Sep26 14:00 MSG 18 28
0000PLIH1 Pali 2 Hawaii 25Sep26 14:01 30 19 30
0000KMOH1 Kealakomo Hawaii 25Sep26 13:44 10 19 30
0000KPRH1 Kapapala Hawaii 25Sep26 13:48 30 10 20
0000NENH1 Nene Cabin Hawaii 25Sep26 14:23 80 10 24
0000KIOH1 Kaiholena Hawaii 25Sep26 14:15 360 4 6
0000LKHH1 Lower Kahuku Hawaii 25Sep26 14:23 350 3 13
0000SOPH1 Sou h Poin Hawaii 25Sep26 14:00 60 14 24
0000KOMH1 Kona Hema Hawaii 25Sep26 14:15 230 4 5
0000KRCH1 Kahuku Ranch Hawaii 25Sep26 14:29 300 4 12
0000PHRH1 Puho CS Hawaii 25Sep26 14:22 290 3 7
0000HLNH1 HELCO Lolo Ln Hawaii 25Sep26 14:30 270 2 4
0000HHUH1 HELCO Hualalai Rd Hawaii 25Sep26 14:30 280 2 5
0000KOUH1 Keahuolu Hawaii 25Sep26 14:15 270 2 3
0000PHKO Kona In l AP Hawaii 25Sep26 14:00 230 7 MSG
0000KHOH1 Kaloko-Honokohau Hawaii 25Sep26 14:15 250 5 8
0000PLMH1 Palamanui Hawaii 25Sep26 14:15 230 2 6
0000PWAH1 Puu Waawaa (UHM) Hawaii 25Sep26 14:15 230 0 1
0000KIUH1 Kaiaulu Puu Waawaa Hawaii 25Sep26 14:15 340 6 9
0000KPLH1 Kaupulehu Hawaii 25Sep26 14:36 240 7 10
0000PWWH1 Puu Waawaa Hawaii 25Sep26 14:37 280 4 8
0000HMHH1 HELCO Mamalahoa 2 Hawaii 25Sep26 14:30 280 6 9
0000MMLH1 Mamalahoa Hawaii 25Sep26 14:15 290 1 4
0000HMWH1 HELCO Mamalahoa 3 Hawaii 25Sep26 14:30 40 9 14
0000PULH1 Puuanahulu Hawaii 25Sep26 14:37 40 8 16
0000AHMH1 Ahumoa Hawaii 25Sep26 14:35 320 3 8
0000AIPH1 Aipaloa Hawaii 25Sep26 14:15 360 3 5
0000HSRH1 HELCO Saddle Rd Hawaii 25Sep26 14:30 250 4 6
0000HMYH1 HELCO Mamalahoa Hawaii 25Sep26 14:30 20 19 26
0000HHCH1 HELCO Hokuloa UCC Hawaii 25Sep26 14:30 40 20 31
0000HWRH1 HELCO Waikoloa Rd Hawaii 25Sep26 14:30 50 23 40
0000HWXH1 HELCO Waikoloa 2 Hawaii 25Sep26 14:30 80 25 39
0000WKVH1 Waikoloa Hawaii 25Sep26 14:35 70 21 37
0000HLOH1 HELCO Lalamilo Hawaii 25Sep26 14:30 40 27 36
0000LLAH1 Lalamilo Hawaii 25Sep26 14:15 30 6 15
0000HKWH1 HELCO Kawaihae Rd Hawaii 25Sep26 14:30 50 28 41
0000PKAH1 PTA Kipuka Alala Hawaii 25Sep26 13:55 110 16 26
0000PKWH1 PTA Wes Hawaii 25Sep26 13:56 320 7 15
0000PKMH1 PTA Keamuku Hawaii 25Sep26 13:50 30 0 0
0000PTRH1 PTA Range 17 Hawaii MSG MSG MSG MSG
0000PERH1 Puhe CS Hawaii 25Sep26 14:24 60 9 29
0000KWHH1 Kawaihae NOS Hawaii MSG MSG MSG MSG
0000HHKH1 HELCO Hulukupuna Hawaii 25Sep26 14:30 90 15 25
0000PLAH1 Puuloa Hawaii 25Sep26 14:15 310 36 49
0000HMLH1 HELCO Maluokalani Hawaii MSG MSG MSG MSG
0000HKDH1 HELCO Ala Kahua Hawaii 25Sep26 14:30 220 29 41
0000KHRH1 Kohala Ranch Hawaii 25Sep26 14:35 50 28 43
0000KEHH1 Kehena Hawaii 25Sep26 14:15 10 8 20
```

---

### 13. Monthly Climate Summary — HNL

| Field | Value |
|---|---|
| **Resource ID** | clm_monthly_climate_summary_HNL |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLM&issuedby=HNL |
| **Collected** | 2026-09-25T16:46:18.012145-10:00 HST |

```text
434
CXHW50 PHFO 011625
CLMHNL

CLIMATE REPORT
NATIONAL WEATHER SERVICE HONOLULU HI
625 AM HST TUE SEP 01 2026

...................................

...THE HONOLULU CLIMATE SUMMARY FOR THE MONTH OF AUGUST 2026...

CLIMATE NORMAL PERIOD 1991 TO 2020
CLIMATE RECORD PERIOD 1940 TO 2026

WEATHER OBSERVED NORMAL DEPART LAST YEAR`S
VALUE DATE(S) VALUE FROM VALUE DATE(S)
NORMAL
................................................................
TEMPERATURE (F)
RECORD
HIGH 95 08/31/2019
LOW 25 08/02/2024
HIGHEST 90 08/09 89 1 92 08/11
08/11
08/22
LOWEST 74 08/19 75 -1 74 08/11
08/20
08/14
08/30
AVG. MAXIMUM 88.3 88.8 -0.5 89.2
AVG. MINIMUM 76.7 75.6 1.1 76.6
MEAN 82.5 82.2 0.3 82.9
DAYS MAX >= 93 0 0
DAYS MAX >= 90 6 13
DAYS MAX <= 80 0 0
DAYS MIN >= 72 31 31
DAYS MIN <= 60 0 0
DAYS MIN <= 55 0 0

PRECIPITATION (INCHES)
RECORD
MAXIMUM 3.74 2004
MINIMUM T 2025
TOTALS 0.91 0.84 0.07 T
DAILY AVG. 0.03 0.03 0.00 T
DAYS >= .01 1 5.7 -4.7 0
DAYS >= .10 0 1.2 -1.2 0
DAYS >= .50 0 0.4 -0.4 0
DAYS >= 1.00 0 0.2 -0.2 0
GREATEST
24 HR. TOTAL 0.86 08/15 TO 08/16 T

DEGREE DAYS
HEATING TOTAL 0 0 0 0
SINCE 7/1 0 0 0 MM
COOLING TOTAL 550 533 17 561
SINCE 1/1 3210 3077 133 MM
................................................................

WIND (MPH)
AVERAGE WIND SPEED 12.5
HIGHEST WIND SPEED/DIRECTION 38/050 DATE 08/16
HIGHEST GUST SPEED/DIRECTION 53/060 DATE 08/16

SKY COVER
POSSIBLE SUNSHINE (PERCENT) MM
AVERAGE SKY COVER 0.45
NUMBER OF DAYS FAIR 10
NUMBER OF DAYS PC 19
NUMBER OF DAYS CLOUDY 2

AVERAGE RH (PERCENT) 66

WEATHER CONDITIONS. NUMBER OF DAYS WITH
THUNDERSTORM MM MIXED PRECIP MM
HEAVY RAIN 1 RAIN 1
LIGHT RAIN 12 FREEZING RAIN MM
LT FREEZING RAIN MM HAIL MM
HEAVY SNOW MM SNOW MM
LIGHT SNOW MM SLEET MM
FOG 3 FOG W/VIS <= 1/4 MILE MM
HAZE MM

- INDICATES NEGATIVE NUMBERS.
R INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T INDICATES TRACE AMOUNT.
```

---

### 14. Monthly Climate Summary — ITO

| Field | Value |
|---|---|
| **Resource ID** | clm_monthly_climate_summary_ITO |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLM&issuedby=ITO |
| **Collected** | 2026-09-25T16:47:03.681413-10:00 HST |

```text
433
CXHW53 PHFO 011625
CLMITO

CLIMATE REPORT
NATIONAL WEATHER SERVICE HONOLULU HI
625 AM HST TUE SEP 01 2026

...................................

...THE HILO/GEN.LYMAN FLD CLIMATE SUMMARY FOR THE MONTH OF AUGUST 2026...

CLIMATE NORMAL PERIOD 1991 TO 2020
CLIMATE RECORD PERIOD 1949 TO 2026

WEATHER OBSERVED NORMAL DEPART LAST YEAR`S
VALUE DATE(S) VALUE FROM VALUE DATE(S)
NORMAL
................................................................
TEMPERATURE (F)
RECORD
HIGH 93 08/15/1950
LOW 63 08/01/1955
HIGHEST 87 08/21 83 4 88 08/11
LOWEST 70 08/30 69 1 67 08/24
AVG. MAXIMUM 83.7 82.9 0.8 84.9
AVG. MINIMUM 72.6 70.4 2.2 70.0
MEAN 78.2 76.6 1.6 77.5
DAYS MAX >= 93 0 0
DAYS MAX >= 90 0 0
DAYS MAX <= 80 2 2
DAYS MIN >= 72 20 6
DAYS MIN <= 60 0 0
DAYS MIN <= 55 0 0

PRECIPITATION (INCHES)
RECORD
MAXIMUM 48.85 2018
MINIMUM 2.06 2025
TOTALS 20.85 11.30 9.55 2.06
DAILY AVG. 0.67 0.36 0.31 0.05
DAYS >= .01 25 27.2 -2.2 19
DAYS >= .10 16 18.2 -2.2 5
DAYS >= .50 8 6.0 2.0 1
DAYS >= 1.00 3 2.2 0.8 0
GREATEST
24 HR. TOTAL 9.24 08/15 TO 08/16 0.70

DEGREE DAYS
HEATING TOTAL 0 0 0 0
SINCE 7/1 0 0 0 MM
COOLING TOTAL 416 361 55 393
SINCE 1/1 2429 2111 318 MM
................................................................

WIND (MPH)
AVERAGE WIND SPEED 6.8
HIGHEST WIND SPEED/DIRECTION 39/090 DATE 08/15
HIGHEST GUST SPEED/DIRECTION 56/080 DATE 08/15

SKY COVER
POSSIBLE SUNSHINE (PERCENT) MM
AVERAGE SKY COVER 0.78
NUMBER OF DAYS FAIR 1
NUMBER OF DAYS PC 11
NUMBER OF DAYS CLOUDY 19

AVERAGE RH (PERCENT) 81

WEATHER CONDITIONS. NUMBER OF DAYS WITH
THUNDERSTORM MM MIXED PRECIP MM
HEAVY RAIN 15 RAIN 15
LIGHT RAIN 27 FREEZING RAIN MM
LT FREEZING RAIN MM HAIL MM
HEAVY SNOW MM SNOW MM
LIGHT SNOW MM SLEET MM
FOG 25 FOG W/VIS <= 1/4 MILE MM
HAZE 8

- INDICATES NEGATIVE NUMBERS.
R INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T INDICATES TRACE AMOUNT.
```

---

### 15. Monthly Climate Summary — LIH

| Field | Value |
|---|---|
| **Resource ID** | clm_monthly_climate_summary_LIH |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLM&issuedby=LIH |
| **Collected** | 2026-09-25T16:46:33.063649-10:00 HST |

```text
436
CXHW51 PHFO 011625
CLMLIH

CLIMATE REPORT
NATIONAL WEATHER SERVICE HONOLULU HI
625 AM HST TUE SEP 01 2026

...................................

...THE LIHUE CLIMATE SUMMARY FOR THE MONTH OF AUGUST 2026...

CLIMATE NORMAL PERIOD 1991 TO 2020
CLIMATE RECORD PERIOD 1950 TO 2026

WEATHER OBSERVED NORMAL DEPART LAST YEAR`S
VALUE DATE(S) VALUE FROM VALUE DATE(S)
NORMAL
................................................................
TEMPERATURE (F)
RECORD
HIGH 91 08/31/2019
08/25/2019
09/19/1994
LOW 59 08/27/2020
HIGHEST 87 08/13 85 2 88 08/16
LOWEST 72 08/07 75 -3 72 08/11
AVG. MAXIMUM 84.7 85.2 -0.5 86.6
AVG. MINIMUM 75.7 75.2 0.5 75.7
MEAN 80.2 80.2 0.0 81.2
DAYS MAX >= 93 0 0
DAYS MAX >= 90 0 0
DAYS MAX <= 80 1 0
DAYS MIN >= 72 31 31
DAYS MIN <= 60 0 0
DAYS MIN <= 55 0 0

PRECIPITATION (INCHES)
RECORD
MAXIMUM 8.13 1959
MINIMUM 0.44 2007
TOTALS 2.43 2.33 0.10 1.25
DAILY AVG. 0.08 0.08 0.00 0.04
DAYS >= .01 22 18.0 4.0 12
DAYS >= .10 4 5.3 -1.3 2
DAYS >= .50 1 0.9 0.1 1
DAYS >= 1.00 1 0.4 0.6 0
GREATEST
24 HR. TOTAL 1.18 08/16 TO 08/17 0.83

DEGREE DAYS
HEATING TOTAL 0 0 0 0
SINCE 7/1 0 0 0 MM
COOLING TOTAL 480 471 9 508
SINCE 1/1 2703 2634 69 MM
................................................................

WIND (MPH)
AVERAGE WIND SPEED 14.6
HIGHEST WIND SPEED/DIRECTION 39/070 DATE 08/16
HIGHEST GUST SPEED/DIRECTION 53/070 DATE 08/16

SKY COVER
POSSIBLE SUNSHINE (PERCENT) MM
AVERAGE SKY COVER 0.61
NUMBER OF DAYS FAIR 3
NUMBER OF DAYS PC 19
NUMBER OF DAYS CLOUDY 9

AVERAGE RH (PERCENT) 78

WEATHER CONDITIONS. NUMBER OF DAYS WITH
THUNDERSTORM MM MIXED PRECIP MM
HEAVY RAIN 3 RAIN 3
LIGHT RAIN 19 FREEZING RAIN MM
LT FREEZING RAIN MM HAIL MM
HEAVY SNOW MM SNOW MM
LIGHT SNOW MM SLEET MM
FOG 17 FOG W/VIS <= 1/4 MILE MM
HAZE 10

- INDICATES NEGATIVE NUMBERS.
R INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T INDICATES TRACE AMOUNT.
```

---

### 16. Monthly Climate Summary — OGG

| Field | Value |
|---|---|
| **Resource ID** | clm_monthly_climate_summary_OGG |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLM&issuedby=OGG |
| **Collected** | 2026-09-25T16:46:48.623641-10:00 HST |

```text
435
CXHW52 PHFO 011625
CLMOGG

CLIMATE REPORT
NATIONAL WEATHER SERVICE HONOLULU HI
625 AM HST TUE SEP 01 2026

...................................

...THE KAHULUI/MAUI CLIMATE SUMMARY FOR THE MONTH OF AUGUST 2026...

CLIMATE NORMAL PERIOD 1991 TO 2020
CLIMATE RECORD PERIOD 1954 TO 2026

WEATHER OBSERVED NORMAL DEPART LAST YEAR`S
VALUE DATE(S) VALUE FROM VALUE DATE(S)
NORMAL
................................................................
TEMPERATURE (F)
RECORD
HIGH 97 08/22/2015
08/31/1994
LOW 60 08/30/2019
HIGHEST 90 08/11 88 2 92 08/16
08/21
08/24
08/23
08/27
LOWEST 70 08/20 71 -1 65 08/25
AVG. MAXIMUM 87.1 89.9 -2.8 89.5
AVG. MINIMUM 74.4 72.3 2.1 71.7
MEAN 80.8 81.1 -0.3 80.6
DAYS MAX >= 93 0 0
DAYS MAX >= 90 3 17
DAYS MAX <= 80 0 0
DAYS MIN >= 72 28 16
DAYS MIN <= 60 0 0
DAYS MIN <= 55 0 0

PRECIPITATION (INCHES)
RECORD
MAXIMUM 1.93 2018
MINIMUM 0.01 2025
TOTALS 1.47 0.53 0.94 0.01
DAILY AVG. 0.05 0.02 0.03 0.00
DAYS >= .01 5 7.4 -2.4 1
DAYS >= .10 3 1.3 1.7 0
DAYS >= .50 1 0.2 0.8 0
DAYS >= 1.00 0 0.0 0.0 0
GREATEST
24 HR. TOTAL 1.20 08/15 TO 08/16 0.01

DEGREE DAYS
HEATING TOTAL 0 0 0 0
SINCE 7/1 0 0 0 MM
COOLING TOTAL 400 499 -99 490
SINCE 1/1 2784 2847 -63 MM
................................................................

WIND (MPH)
AVERAGE WIND SPEED 15.9
HIGHEST WIND SPEED/DIRECTION 38/050 DATE 08/15
HIGHEST GUST SPEED/DIRECTION 62/050 DATE 08/15

SKY COVER
POSSIBLE SUNSHINE (PERCENT) MM
AVERAGE SKY COVER 0.40
NUMBER OF DAYS FAIR 15
NUMBER OF DAYS PC 14
NUMBER OF DAYS CLOUDY 2

AVERAGE RH (PERCENT) 73

WEATHER CONDITIONS. NUMBER OF DAYS WITH
THUNDERSTORM MM MIXED PRECIP MM
HEAVY RAIN 1 RAIN 2
LIGHT RAIN 15 FREEZING RAIN MM
LT FREEZING RAIN MM HAIL MM
HEAVY SNOW MM SNOW MM
LIGHT SNOW MM SLEET MM
FOG 12 FOG W/VIS <= 1/4 MILE MM
HAZE 2

- INDICATES NEGATIVE NUMBERS.
R INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T INDICATES TRACE AMOUNT.
```

---

### 17. NHC Atlantic Tropical Weather Outlook — 2 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_atlc_2day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=atlc&fdays=2 |
| **Collected** | 2026-09-25T20:19:49.399430-10:00 HST |

```text
489 ACCA62 KNHC 260525TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL200 AM EDT sábado 26 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Tormenta Tropical Gonzalo, ubicada justo aleste-noreste de las Islas de Cabo Verde, y sobre la TormentaTropical Fay, ubicada al oeste-suroeste de las Azores.No se espera la formación de ciclones tropicales durante lospróximos 7 días.$$Pronosticador Pierce/Evans/Berg*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 18. NHC Atlantic Tropical Weather Outlook — 7 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_atlc_7day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=atlc&fdays=7 |
| **Collected** | 2026-09-25T20:40:27.782301-10:00 HST |

```text
489 ACCA62 KNHC 260525TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL200 AM EDT sábado 26 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Tormenta Tropical Gonzalo, ubicada justo aleste-noreste de las Islas de Cabo Verde, y sobre la TormentaTropical Fay, ubicada al oeste-suroeste de las Azores.No se espera la formación de ciclones tropicales durante lospróximos 7 días.$$Pronosticador Pierce/Evans/Berg*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 19. NHC Central Pacific Tropical Weather Outlook — 2 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_cpac_2day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=cpac&fdays=2 |
| **Collected** | 2026-09-25T20:03:51.685934-10:00 HST |

```text
489 ACCA62 KNHC 260525TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL200 AM EDT sábado 26 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Tormenta Tropical Gonzalo, ubicada justo aleste-noreste de las Islas de Cabo Verde, y sobre la TormentaTropical Fay, ubicada al oeste-suroeste de las Azores.No se espera la formación de ciclones tropicales durante lospróximos 7 días.$$Pronosticador Pierce/Evans/Berg*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 20. NHC Central Pacific Tropical Weather Outlook — 7 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_cpac_7day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=cpac&fdays=7 |
| **Collected** | 2026-09-25T20:04:51.998769-10:00 HST |

```text
489 ACCA62 KNHC 260525TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL200 AM EDT sábado 26 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Tormenta Tropical Gonzalo, ubicada justo aleste-noreste de las Islas de Cabo Verde, y sobre la TormentaTropical Fay, ubicada al oeste-suroeste de las Azores.No se espera la formación de ciclones tropicales durante lospróximos 7 días.$$Pronosticador Pierce/Evans/Berg*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 21. NHC Eastern Pacific Tropical Weather Outlook — 2 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_epac_2day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=epac&fdays=2 |
| **Collected** | 2026-09-25T20:05:51.602645-10:00 HST |

```text
489 ACCA62 KNHC 260525TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL200 AM EDT sábado 26 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Tormenta Tropical Gonzalo, ubicada justo aleste-noreste de las Islas de Cabo Verde, y sobre la TormentaTropical Fay, ubicada al oeste-suroeste de las Azores.No se espera la formación de ciclones tropicales durante lospróximos 7 días.$$Pronosticador Pierce/Evans/Berg*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 22. NHC Eastern Pacific Tropical Weather Outlook — 7 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_epac_7day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=epac&fdays=7 |
| **Collected** | 2026-09-25T20:18:50.035110-10:00 HST |

```text
489 ACCA62 KNHC 260525TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL200 AM EDT sábado 26 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Tormenta Tropical Gonzalo, ubicada justo aleste-noreste de las Islas de Cabo Verde, y sobre la TormentaTropical Fay, ubicada al oeste-suroeste de las Azores.No se espera la formación de ciclones tropicales durante lospróximos 7 días.$$Pronosticador Pierce/Evans/Berg*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 23. NHC source index

| Field | Value |
|---|---|
| **Resource ID** | nhc_homepage |
| **Official source** | https://www.nhc.noaa.gov/ |
| **Collected** | 2026-09-25T21:24:15.821166-10:00 HST |

```text
Home




Mobile Si e




Tex Version




RSS
















Local Forecas



















NATIONAL HURRICANE CENTER and
CENTRAL PACIFIC HURRICANE CENTER


Na ional Oceanic and A mospheric Adminis ra ion































Analysis & Forecas s




Tropical Cyclone Produc s


Tropical Wea her Ou looks


Marine Produc s


Rip Curren s Map


RSS Feeds


GIS Produc s


Al erna e Forma s


Tropical Cyclone Produc Descrip ions


Tropical Cyclone Produc Examples


Marine Produc Descrip ions










Da a & Tools




Sa elli e Imagery


Radar Imagery


Aircraf Reconnaissance


Tropical Analysis Tools


Experimen al Produc s


La /Lon Dis ance Calcula or


Blank Tracking Maps










Educa ional Resources






Be Prepared!
NWS Hurricane Prep Week




Ou reach Documen s


TC Videos


Rip Curren s


S orm Surge


Wa ch/Warning Breakpoin s


Clima ology


Tropical Cyclone Names


Wind Scale


Records and Fac s


His orical Hurricane Summaries


Forecas Models


NHC Publica ions


NHC Glossary


Acronyms


Frequen Ques ions










Archives




Tropical Cyclone Advisories


Tropical Wea her Ou looks


Tropical Cyclone Repor s and Season Summaries


Tropical Cyclone Forecas Verifica ion


NHC News Archive


O her Archives: HURDAT, Track Maps, Marine Produc s, and more










Abou




Na ional Hurricane Cen er


Cen ral Pacific Hurricane Cen er


Library


Con ac Us










Search









Search for


Search


















































Top News of he Day...
view pas news




Las upda e Sa , 26 Sep 2026 07:22:36 UTC













NHC issuing advisories for he A lan ic on


TS Fay

and

TS Gonzalo







NHC issuing advisories for he Eas ern Pacific on


Hurricane Odalys

and

Hurricane Polo







NHC issuing advisories for he Cen ral Pacific on


Hurricane Nolo











Marine warnings are in effec for he A lan ic and Eas ern Pacific













Key messages regarding Hurricane Polo

(en Español: Mensajes Claves)




Key messages regarding Hurricane Nolo

(en Español: Mensajes Claves)





Local info on Nolo:
Honolulu










































Graphical Tropical Wea her Ou look (S a ic Images)



JavaScrip is curren ly disabled in your browser or you are using an older browser ha is incompa ible wi h his map. To view he in erac ive map, please enable JavaScrip or upda e your browser if possible. Direc links o he la es high-resolu ion forecas images are provided below:







View A lan ic 2-Day Ou look






View A lan ic 7-Day Ou look






View Eas ern Pacific 2-Day Ou look






View Eas ern Pacific 7-Day Ou look






View Cen ral Pacific 2-Day Ou look






View Cen ral Pacific 7-Day Ou look



















Cen ral Pacific




Pacific




A lan ic













2-Day Forecas




7-Day Forecas
























Dis urbances:


None













Dis urbances:


None











Dis urbances:








ALL








1








2













Dis urbances:








ALL








1








2













Dis urbances:








ALL








1








2













Dis urbances:








ALL








1








2













Dis urbances:








ALL








1








2













Dis urbances:








ALL








1








2













Dis urbances:








ALL








1








2













Dis urbances:








ALL








1








2













Dis urbances:








ALL








1













Dis urbances:








ALL








1













Dis urbances:








ALL








1













Dis urbances:








ALL








1




























































































































































































































































































































































































































































































































































































































View Full Graphical Tropical Wea her Ou look
| Marine Produc s

































Close (X)












View S orm De ails


















Cen ral Nor h Pacific
(140°W o 180°)
















Tropical Wea her Ou look

(en Español*)


800 PM HST Fri Sep 25 2026
























Hurricane Nolo








Sa elli e |
Buoys |
Grids |
S orm Archive














...NOLO NEARLY STATIONARY SOUTH OF THE BIG ISLAND OF HAWAII...









8:00 PM HST Fri Sep 25

Loca ion: 16.9°N 155.2°W


Moving: S a ionary


Min pressure: 975 mb

Max sus ained: 105 mph





Public

Advisory

#22A

800 PM HST



Forecas

Advisory

#22

0300 UTC



Forecas

Discussion

#22

500 PM HST



Wind Speed

Probabili ies

#22

0300 UTC


























NWS Local

Produc s

520 PM HST









Produc os en español:

(más información)










Aviso

Publico









Pronós ico

Discusión























Wind Speed
Probabili ies










Arrival Time
of Winds










Wind
His ory










In erac ive
Cone










Warnings/Cone
S a ic Images










Warnings/Cone
In erac ive Map










Experimen al Cone
S a ic Images























Experimen al Cone
In erac ive Map














Warnings and
Surface Wind














Key
Messages










Mensajes
Claves



























Peak
Surge















Rainfall
Po en ial




















































A lan ic - Caribbean Sea - Gulf of America

















Tropical Wea her Ou look

(en Español*)


200 AM EDT Sa Sep 26 2026



Tropical Wea her Discussion

0615 UTC Sa Sep 26 2026
























Tropical S orm Gonzalo








Sa elli e |
Buoys |
Grids |
S orm Archive














...GONZALO WEAKENS AS IT CONTINUES NORTHWARD...









2:00 AM CVT Sa Sep 26

Loca ion: 16.9°N 22.5°W


Moving: N a 9 mph


Min pressure: 1002 mb

Max sus ained: 45 mph





Public

Advisory

#5

200 AM CVT



Forecas

Advisory

#5

0300 UTC



Forecas

Discussion

#5

200 AM CVT



Wind Speed

Probabili ies

#5

0300 UTC












Produc os en español:

(más información)










Aviso

Publico









Pronós ico

Discusión























Wind Speed
Probabili ies










Arrival Time
of Winds










Wind
His ory










In erac ive
Cone










Warnings/Cone
S a ic Images










Warnings/Cone
In erac ive Map










Experimen al Cone
S a ic Images























Experimen al Cone
In erac ive Map














Warnings and
Surface Wind



















Rip
Curren s






























































Tropical S orm Fay








Sa elli e |
Buoys |
Grids |
S orm Archive














...FAY CONTINUES TO WEAKEN OVER THE ATLANTIC OCEAN...









3:00 AM GMT Sa Sep 26

Loca ion: 29.9°N 43.4°W


Moving: WSW a 7 mph


Min pressure: 1006 mb

Max sus ained: 40 mph





Public

Advisory

#24

300 AM GMT



Forecas

Advisory

#24

0300 UTC



Forecas

Discussion

#24

300 AM GMT



Wind Speed

Probabili ies

#24

0300 UTC












Produc os en español:

(más información)










Aviso

Publico









Pronós ico

Discusión























Wind Speed
Probabili ies










Arrival Time
of Winds










Wind
His ory










In erac ive
Cone










Warnings/Cone
S a ic Images










Warnings/Cone
In erac ive Map










Experimen al Cone
S a ic Images























Experimen al Cone
In erac ive Map














Warnings and
Surface Wind



















Rip
Curren s



































































Eas ern Nor h Pacific
(Eas of 140°W)
















Tropical Wea her Ou look

(en Español*)


1100 PM PDT Fri Sep 25 2026



Tropical Wea her Discussion

0405 UTC Sa Sep 26 2026
























Hurricane Polo








Sa elli e |
Buoys |
Grids |
S orm Archive














...POLO REMAINS AN EXTREMELY DANGEROUS CATEGORY 5 HURRICANE...
...EXPECTED TO MAKE LANDFALL IN BAJA CALIFORNIA SUR ON MONDAY AS A POWERFUL HURRICANE...









11:00 PM MST Fri Sep 25

Loca ion: 17.5°N 110.5°W


Moving: WNW a 10 mph


Min pressure: 911 mb

Max sus ained: 175 mph





Public

Advisory

#22A

1100 PM MST



Forecas

Advisory

#22

0300 UTC



Forecas

Discussion

#22

800 PM MST



Wind Speed

Probabili ies

#22

0300 UTC












Produc os en español:

(más información)










Aviso

Publico









Pronós ico

Discusión























Wind Speed
Probabili ies










Arrival Time
of Winds










Wind
His ory










In erac ive
Cone










Warnings/Cone
S a ic Images










Warnings/Cone
In erac ive Map










Experimen al Cone
S a ic Images























Experimen al Cone
In erac ive Map














Warnings and
Surface Wind














Key
Messages










Mensajes
Claves















Rip
Curren s



























Rainfall
Po en ial















































Hurricane Odalys








Sa elli e |
Buoys |
Grids |
S orm Archive














...ODALYS STILL A MAJOR HURRICANE AS IT MOVES SLOWLY NORTHWARD...









8:00 PM PDT Fri Sep 25

Loca ion: 18.8°N 123.6°W


Moving: N a 5 mph


Min pressure: 952 mb

Max sus ained: 120 mph





Public

Advisory

#25

800 PM PDT



Forecas

Advisory

#25

0300 UTC



Forecas

Discussion

#25

800 PM PDT



Wind Speed

Probabili ies

#25

0300 UTC












Produc os en español:

(más información)










Aviso

Publico









Pronós ico

Discusión























Wind Speed
Probabili ies










Arrival Time
of Winds










Wind
His ory










In erac ive
Cone










Warnings/Cone
S a ic Images










Warnings/Cone
In erac ive Map










Experimen al Cone
S a ic Images























Experimen al Cone
In erac ive Map














Warnings and
Surface Wind



















Rip
Curren s








































































Building Your Hurricane Knowledge Ki







‹































Na ional Hurricane Cen er Track Forecas Cone (2026)






























Building Your Hurricane "Knowledge" Ki : S orm Surge Warning






























Building Your Hurricane "Knowledge" Ki : Po en ial Tropical Cyclones






























Tropical Cyclone Names






























Tropical Waves






























Ar ificial In elligence (AI) in Hurricane Forecas ing






























Building Your Hurricane "Knowledge" Ki : Tropical Wea her Ou look






























Building Your Hurricane "Knowledge" Ki : Time of Arrival






























Building Your Hurricane "Knowledge" Ki : Wind Speed Probabili ies






























Building Your Hurricane "Knowledge" Ki : Saffir-Simpson Hurricane Wind Scale






























Building Your Hurricane "Knowledge" Ki : S orm Surge Wa ch






























Na ional Hurricane Preparedness Week Preview: Assembling Your Hurricane "Knowledge" Ki









›






















Quick Links and Addi ional Resources





Tropical Cyclone Forecas s

Tropical Cyclone Advisories

Tropical Wea her Ou look

Audio/Podcas s

Abou Advisories



Marine Forecas s

Offshore Wa ers Forecas s

Gridded Forecas s

Graphicas

Abou Marine





Social Media


NHC on Facebook



NHC on X



NHC on YouTube



NHC Blog:
"Inside he Eye"




Hurricane Preparedness


Preparedness Guide


Hurricane Hazards


Wa ches and Warnings


Marine Safe y


Ready.gov Hurricanes


Wea her-Ready Na ion


Emergency Managemen Offices






Research and Developmen


NOAA Hurricane Research Division


Hurricane and Ocean Tes bed


Hurricane Forecas Improvemen Program




O her Resources

Q & A wi h NHC


NHC/AOML Library Branch



NOAA: Hurricane FAQs


Na ional Hurricane Opera ions Plan


WX4NHC Ama eur Radio






NWS Forecas Offices


Wea her Predic ion Cen er



S orm Predic ion Cen er



Ocean Predic ion Cen er



Local Forecas Offices




Worldwide Tropical Cyclone Cen ers


Canadian Hurricane Cen re



Join Typhoon Warning Cen er


O her Tropical Cyclone Cen ers


WMO Severe Wea her Info Cen re
























US Dep of Commerce



Na ional Oceanic and A mospheric Adminis ra ion


Na ional Hurricane Cen er

11691 SW 17 h S ree

Miami, FL, 33165

nhcwebmas er@noaa.gov









Cen ral Pacific Hurricane Cen er

2525 Correa Rd

Sui e 250

Honolulu, HI 96822

W-HFO.webmas er@noaa.gov









Disclaimer

Informa ion Quali y

Help

Glossary









Privacy Policy

Freedom of Informa ion Ac (FOIA)

Abou Us

Career Oppor uni ies
```

---

### 24. NOAA solar calculation table

| Field | Value |
|---|---|
| **Resource ID** | solar_calculation_table |
| **Official source** | https://gml.noaa.gov/grad/solcalc/table.php?lat=21.3&lon=-157.85&year=2026 |
| **Collected** | 2026-09-25T20:03:50.351846-10:00 HST |

```text
Solar Calcula or - NOAA Global Moni oring Labora ory


















































Skip o main con en







An official websi e of he Uni ed S a es governmen Here's how you know














Official websi es use .gov

A .gov websi e belongs o an official governmen organiza ion in he Uni ed S a es.














Secure .gov websi es use HTTPS

A lock () or h ps:// means you’ve safely connec ed o he .gov websi e. Share sensi ive informa ion only on official, secure websi es.
































Search


Search GML:















Global Moni oring Labora ory













Menu
















Home






Abou


Abou GML
Science Reviews
Safe y Program

Employmen
Visi ing
Con ac Us

In rane







People


Organiza ion
S aff
Employee Spo ligh







Research


Research Overview
Carbon Cycle Greenhouse Gases
Greenhouse gases and Ozone-deple ing Subs ances
Ozone and Wa er Vapor
Global Radia ion, Aerosols and Clouds
Publica ions
Calibra ion Facili ies
WMO Cen ral Calibra ion Labora ory
Cen ral UV Calibra ion Facili y
Broadband Solar Calibra ion Facili y
World Dobson Ozone Calibra ion Cen re








Observing Ne works






Overview
Observa ions Overview
Measuremen Si es
Field Campaigns




A mospheric Baseline Observa ories
Observa ory Opera ions
Barrow, Alaska
Mauna Loa, Hawaii
American Samoa
Sou h Pole




Observing Ne works
Greenhouse Gas Reference Ne work
Halocarbons and Trace Gases
Surface Radia ion
Federa ed Aerosol Ne work
Ozone
Wa er Vapor













Da a & Produc s








Da a
Da a & Produc s Por al
Da a Finder
ObsPack Da a Produc s
Measuremen Si es




Visualiza ion & Tools

Da a Viewer
Sou h Pole Ozone Hole
Mauna Loa Apparen Transmission
Barrow Snow Mel Da es





Produc s
Greenhouse Gas Index
Ozone Deple ion Index
Trends in CO2, CH4, N2O, SF6
Modeling












Informa ion



News
Seminars
Educa ion/Ou reach
S uden Oppor uni ies
FAQ's
Publica ions

Webcams
Sou h Pole Webcam
Mauna Loa Webcams
Barrow Webcam

Global Moni oring Annual Conference
GMAC Conference




















Search


Search GML:

































PDF Forma





Sunrise Table for 2026



Loca ion: La i ude 21.30000 Longi ude -157.85000

Time Zone Offse : Pacific/Honolulu -10.0

All imes are in local ime. Cells wi h ligh green color indica e when dayligh saving ime is in effec .







Day

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oc

Nov

Dec





1

07:09

07:09

06:52

06:24

06:00

05:49

05:53

06:05

06:15

06:23

06:34

06:53





2

07:09

07:08

06:51

06:23

06:00

05:49

05:53

06:05

06:15

06:23

06:35

06:53





3

07:10

07:08

06:50

06:22

05:59

05:49

05:54

06:06

06:16

06:23

06:36

06:54





4

07:10

07:07

06:49

06:21

05:59

05:49

05:54

06:06

06:16

06:24

06:36

06:55





5

07:10

07:07

06:48

06:21

05:58

05:49

05:54

06:07

06:16

06:24

06:37

06:55





6

07:10

07:06

06:48

06:20

05:57

05:49

05:55

06:07

06:16

06:24

06:37

06:56





7

07:11

07:06

06:47

06:19

05:57

05:49

05:55

06:07

06:17

06:24

06:38

06:56





8

07:11

07:06

06:46

06:18

05:56

05:49

05:56

06:08

06:17

06:25

06:38

06:57





9

07:11

07:05

06:45

06:17

05:56

05:49

05:56

06:08

06:17

06:25

06:39

06:58





10

07:11

07:05

06:44

06:16

05:55

05:49

05:56

06:08

06:17

06:25

06:39

06:58





11

07:11

07:04

06:43

06:15

05:55

05:49

05:57

06:09

06:18

06:26

06:40

06:59





12

07:11

07:03

06:42

06:15

05:54

05:49

05:57

06:09

06:18

06:26

06:41

07:00





13

07:11

07:03

06:41

06:14

05:54

05:49

05:57

06:09

06:18

06:26

06:41

07:00





14

07:11

07:02

06:41

06:13

05:54

05:49

05:58

06:10

06:18

06:27

06:42

07:01





15

07:11

07:02

06:40

06:12

05:53

05:49

05:58

06:10

06:19

06:27

06:42

07:01





16

07:11

07:01

06:39

06:11

05:53

05:49

05:59

06:10

06:19

06:28

06:43

07:02





17

07:11

07:00

06:38

06:10

05:52

05:50

05:59

06:11

06:19

06:28

06:44

07:02





18

07:11

07:00

06:37

06:10

05:52

05:50

05:59

06:11

06:19

06:28

06:44

07:03





19

07:11

06:59

06:36

06:09

05:52

05:50

06:00

06:11

06:20

06:29

06:45

07:04





20

07:11

06:58

06:35

06:08

05:51

05:50

06:00

06:12

06:20

06:29

06:45

07:04





21

07:11

06:58

06:34

06:07

05:51

05:50

06:01

06:12

06:20

06:29

06:46

07:05





22

07:11

06:57

06:33

06:07

05:51

05:51

06:01

06:12

06:20

06:30

06:47

07:05





23

07:11

06:56

06:32

06:06

05:50

05:51

06:01

06:12

06:21

06:30

06:47

07:06





24

07:11

06:56

06:31

06:05

05:50

05:51

06:02

06:13

06:21

06:31

06:48

07:06





25

07:11

06:55

06:31

06:04

05:50

05:51

06:02

06:13

06:21

06:31

06:49

07:06





26

07:10

06:54

06:30

06:04

05:50

05:52

06:03

06:13

06:21

06:32

06:49

07:07





27

07:10

06:53

06:29

06:03

05:50

05:52

06:03

06:14

06:22

06:32

06:50

07:07





28

07:10

06:52

06:28

06:02

05:49

05:52

06:03

06:14

06:22

06:33

06:51

07:08





29

07:10



06:27

06:02

05:49

05:52

06:04

06:14

06:22

06:33

06:51

07:08





30

07:09



06:26

06:01

05:49

05:53

06:04

06:14

06:22

06:33

06:52

07:08





31

07:09



06:25



05:49



06:05

06:15



06:34



07:09












Sunse Table for 2026



Loca ion: La i ude 21.30000 Longi ude -157.85000

Time Zone Offse : Pacific/Honolulu -10.0

All imes are in local ime. Cells wi h ligh green color indica e when dayligh saving ime is in effec .







Day

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oc

Nov

Dec





1

18:01

18:22

18:36

18:46

18:57

19:10

19:18

19:10

18:47

18:19

17:55

17:48





2

18:02

18:22

18:36

18:47

18:57

19:10

19:18

19:10

18:46

18:18

17:55

17:49





3

18:03

18:23

18:37

18:47

18:58

19:11

19:18

19:09

18:45

18:17

17:54

17:49





4

18:03

18:24

18:37

18:47

18:58

19:11

19:18

19:09

18:44

18:16

17:54

17:49





5

18:04

18:24

18:37

18:48

18:58

19:11

19:18

19:08

18:44

18:15

17:53

17:49





6

18:04

18:25

18:38

18:48

18:59

19:12

19:18

19:07

18:43

18:14

17:53

17:49





7

18:05

18:25

18:38

18:48

18:59

19:12

19:18

19:07

18:42

18:13

17:52

17:49





8

18:06

18:26

18:39

18:49

19:00

19:13

19:17

19:06

18:41

18:13

17:52

17:50





9

18:06

18:26

18:39

18:49

19:00

19:13

19:17

19:05

18:40

18:12

17:51

17:50





10

18:07

18:27

18:39

18:49

19:00

19:13

19:17

19:05

18:39

18:11

17:51

17:50





11

18:08

18:27

18:40

18:50

19:01

19:14

19:17

19:04

18:38

18:10

17:51

17:51





12

18:09

18:28

18:40

18:50

19:01

19:14

19:17

19:03

18:37

18:09

17:50

17:51





13

18:09

18:29

18:40

18:50

19:02

19:14

19:17

19:03

18:36

18:08

17:50

17:51





14

18:10

18:29

18:41

18:51

19:02

19:14

19:17

19:02

18:35

18:07

17:50

17:52





15

18:11

18:30

18:41

18:51

19:03

19:15

19:16

19:01

18:34

18:07

17:49

17:52





16

18:11

18:30

18:41

18:51

19:03

19:15

19:16

19:01

18:33

18:06

17:49

17:53





17

18:12

18:31

18:42

18:52

19:03

19:15

19:16

19:00

18:32

18:05

17:49

17:53





18

18:13

18:31

18:42

18:52

19:04

19:16

19:16

18:59

18:31

18:04

17:49

17:53





19

18:13

18:32

18:42

18:52

19:04

19:16

19:15

18:58

18:30

18:04

17:49

17:54





20

18:14

18:32

18:43

18:53

19:05

19:16

19:15

18:57

18:29

18:03

17:49

17:54





21

18:15

18:32

18:43

18:53

19:05

19:16

19:15

18:57

18:28

18:02

17:48

17:55





22

18:15

18:33

18:43

18:53

19:06

19:16

19:15

18:56

18:27

18:01

17:48

17:55





23

18:16

18:33

18:43

18:54

19:06

19:17

19:14

18:55

18:26

18:01

17:48

17:56





24

18:17

18:34

18:44

18:54

19:07

19:17

19:14

18:54

18:25

18:00

17:48

17:56





25

18:17

18:34

18:44

18:54

19:07

19:17

19:13

18:53

18:24

17:59

17:48

17:57





26

18:18

18:35

18:44

18:55

19:07

19:17

19:13

18:53

18:24

17:59

17:48

17:57





27

18:19

18:35

18:45

18:55

19:08

19:17

19:13

18:52

18:23

17:58

17:48

17:58





28

18:19

18:35

18:45

18:56

19:08

19:17

19:12

18:51

18:22

17:57

17:48

17:59





29

18:20



18:45

18:56

19:09

19:17

19:12

18:50

18:21

17:57

17:48

17:59





30

18:20



18:46

18:56

19:09

19:17

19:11

18:49

18:20

17:56

17:48

18:00





31

18:21



18:46



19:09



19:11

18:48



17:56



18:00












Solar Noon Table for 2026



Loca ion: La i ude 21.30000 Longi ude -157.85000

Time Zone Offse : Pacific/Honolulu -10.0

All imes are in local ime. Cells wi h ligh green color indica e when dayligh saving ime is in effec .







Day

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oc

Nov

Dec





1

12:34:56

12:44:58

12:43:43

12:35:15

12:28:31

12:29:15

12:35:18

12:37:46

12:31:26

12:21:06

12:14:56

12:20:24





2

12:35:24

12:45:06

12:43:31

12:34:57

12:28:24

12:29:25

12:35:29

12:37:42

12:31:07

12:20:46

12:14:55

12:20:47





3

12:35:52

12:45:13

12:43:19

12:34:40

12:28:18

12:29:35

12:35:40

12:37:37

12:30:48

12:20:27

12:14:54

12:21:10





4

12:36:19

12:45:19

12:43:06

12:34:22

12:28:12

12:29:45

12:35:51

12:37:32

12:30:28

12:20:09

12:14:55

12:21:34





5

12:36:46

12:45:24

12:42:52

12:34:05

12:28:07

12:29:55

12:36:01

12:37:26

12:30:08

12:19:50

12:14:56

12:21:59





6

12:37:13

12:45:28

12:42:38

12:33:48

12:28:02

12:30:06

12:36:12

12:37:19

12:29:48

12:19:32

12:14:58

12:22:24





7

12:37:39

12:45:32

12:42:24

12:33:31

12:27:58

12:30:17

12:36:21

12:37:12

12:29:28

12:19:15

12:15:01

12:22:50





8

12:38:04

12:45:34

12:42:10

12:33:15

12:27:54

12:30:29

12:36:31

12:37:05

12:29:07

12:18:57

12:15:05

12:23:16





9

12:38:29

12:45:36

12:41:55

12:32:58

12:27:52

12:30:40

12:36:40

12:36:56

12:28:46

12:18:41

12:15:10

12:23:43





10

12:38:54

12:45:37

12:41:39

12:32:42

12:27:49

12:30:52

12:36:48

12:36:47

12:28:25

12:18:24

12:15:16

12:24:10





11

12:39:18

12:45:38

12:41:23

12:32:27

12:27:47

12:31:04

12:36:57

12:36:38

12:28:04

12:18:09

12:15:22

12:24:37





12

12:39:41

12:45:37

12:41:07

12:32:11

12:27:46

12:31:17

12:37:04

12:36:28

12:27:43

12:17:53

12:15:29

12:25:05





13

12:40:04

12:45:36

12:40:51

12:31:56

12:27:46

12:31:29

12:37:12

12:36:18

12:27:22

12:17:38

12:15:38

12:25:33





14

12:40:26

12:45:34

12:40:35

12:31:41

12:27:46

12:31:42

12:37:18

12:36:06

12:27:01

12:17:24

12:15:47

12:26:02





15

12:40:47

12:45:31

12:40:18

12:31:26

12:27:46

12:31:55

12:37:25

12:35:55

12:26:39

12:17:10

12:15:56

12:26:30





16

12:41:08

12:45:28

12:40:01

12:31:12

12:27:47

12:32:07

12:37:30

12:35:43

12:26:18

12:16:57

12:16:07

12:26:59





17

12:41:28

12:45:24

12:39:44

12:30:58

12:27:49

12:32:20

12:37:36

12:35:30

12:25:56

12:16:44

12:16:19

12:27:29





18

12:41:47

12:45:19

12:39:26

12:30:45

12:27:51

12:32:33

12:37:40

12:35:17

12:25:35

12:16:32

12:16:31

12:27:58





19

12:42:06

12:45:13

12:39:09

12:30:32

12:27:54

12:32:47

12:37:44

12:35:03

12:25:14

12:16:21

12:16:44

12:28:27





20

12:42:24

12:45:07

12:38:51

12:30:19

12:27:57

12:33:00

12:37:48

12:34:49

12:24:52

12:16:10

12:16:59

12:28:57





21

12:42:41

12:45:00

12:38:33

12:30:07

12:28:01

12:33:13

12:37:51

12:34:34

12:24:31

12:16:00

12:17:13

12:29:27





22

12:42:58

12:44:53

12:38:15

12:29:55

12:28:05

12:33:26

12:37:54

12:34:19

12:24:10

12:15:51

12:17:29

12:29:57





23

12:43:13

12:44:44

12:37:57

12:29:44

12:28:10

12:33:39

12:37:56

12:34:04

12:23:49

12:15:42

12:17:46

12:30:26





24

12:43:28

12:44:36

12:37:39

12:29:33

12:28:15

12:33:52

12:37:57

12:33:48

12:23:28

12:15:34

12:18:03

12:30:56





25

12:43:42

12:44:26

12:37:21

12:29:23

12:28:21

12:34:04

12:37:58

12:33:31

12:23:07

12:15:26

12:18:21

12:31:26





26

12:43:56

12:44:16

12:37:03

12:29:13

12:28:28

12:34:17

12:37:58

12:33:15

12:22:46

12:15:20

12:18:40

12:31:55





27

12:44:08

12:44:06

12:36:45

12:29:03

12:28:34

12:34:30

12:37:57

12:32:57

12:22:26

12:15:14

12:18:59

12:32:25





28

12:44:20

12:43:55

12:36:27

12:28:54

12:28:42

12:34:42

12:37:56

12:32:40

12:22:05

12:15:09

12:19:19

12:32:54





29

12:44:31



12:36:09

12:28:46

12:28:50

12:34:54

12:37:55

12:32:22

12:21:45

12:15:04

12:19:40

12:33:23





30

12:44:41



12:35:51

12:28:38

12:28:58

12:35:06

12:37:52

12:32:04

12:21:25

12:15:01

12:20:02

12:33:52





31

12:44:50



12:35:33



12:29:06



12:37:49

12:31:45



12:14:58



12:34:21
































Global Moni oring Labora ory

» U.S. Depar men of Commerce

» Na ional Oceanic & A mospheric Adminis ra ion

» NOAA Research










Privacy Policy  |
Accessibili y  |
Disclaimer  |
Disclaimer for Ex ernal Links  |
FOIA  |
Usa.gov














Si e Con en s

Con ac Us  |  Webmas er

Take Our Survey
```

---

### 25. Nws Cwa Boundaries Catalog

| Field | Value |
|---|---|
| **Resource ID** | nws_cwa_boundaries_catalog |
| **Official source** | https://www.weather.gov/gis/CWABounds |
| **Collected** | 2026-09-25T21:16:22.042398-10:00 HST |

```text
Coun y Warning Area Boundaries
















































































HOME








FORECAST








Local




Graphical




Avia ion




Marine




Rivers and Lakes




Hurricanes




Severe Wea her




Fire Wea her




Sunrise/Sunse




Long Range Forecas s




Clima e Predic ion




Space Wea her












PAST WEATHER








Pas Wea her




As ronomical Da a




Cer ified Wea her Da a












SAFETY








INFORMATION








Wireless Emergency Aler s




Wea her-Ready Na ion




Brochures




Coopera ive Observers




Daily Briefing




Damage/Fa ali y/Injury S a is ics




Forecas Models




GIS Da a Por al




NOAA Wea her Radio




Publica ions




SKYWARN S orm Spo ers




S ormReady




TsunamiReady




Service Change No ices












EDUCATION








NEWS








SEARCH













Search For





NWS

All NOAA


















ABOUT








Abou NWS




Organiza ion




For NWS Employees




Na ional Cen ers




Careers




Con ac Us




Glossary




Social Media




NWS Transforma ion




































GIS


Na ional Program






Coun y Warning Area Boundaries



Wea her.gov
> GIS
> Coun y Warning Area Boundaries

















CloudGIS Web Services








NWS Na ional GIS Viewer








AWIPS Basemaps








Me ada a Page





















Shapefile Type: polygon



Da a source: Derived from NWS Public Forecas Zones



Naming conven ion: W_ddmmyy  where ddmmyy = day-mon h-year



NWS Specifica ions: NWSI 10-507



Descrip ion: The CWA boundaries are he coun ies/zones for which each Wea her Forecas Office (WFO) is responsible for issuing forecas s and warnings.  The shapefile was crea ed by aggrega ing public zones wi h he same CWA designa ion in o a single polygon and manually adjus ing he boundaries of he excep ions o he rule.





Due o echnical issues, he implemen a ion da e for zone changes has been moved o April 16, 2026. New files will be available by March 4, 2026, and he files will be locked down on March 24, 2026.








Descrip ion


Valid Da e


Da a Download


#Records


MD5sum


Documen a ion








Coun y Warning Areas


18 March 2025


w_18mr25.zip


125


cc80d248f0918cfdbfd1d3f0440d1874


Da e Las Upda ed: 23-DEC-24


Change His ory


Me ada a






16 April 2026


w_16ap26.zip


125


b8614c30e80d68b7ccb74ff599c57c39


Da e Las Upda ed: 03-MAR-26












Shapefile A ribu es:








Field Name


Type


Wid h


Descrip ion








WFO


charac er


3


WFO Iden ifier (name of CWA)






CWA


charac er


3


CWA Iden ifier (same as WFO)






LON


numeric


10,5


Longi ude of cen roid [decimal degrees]






LAT


numeric


9,5


La i ude of cen roid [decimal degrees]






REGION


charac er


2


NWS Region (Eas ern (ER), Wes ern (WR), Cen ral (CR), Sou hern (SR), Alaska (AR), Pacific (PR)






FULLSTAID


charac er


4


Full 4 charac er in ernal NWS S a ion ID for CWA






CITYSTATE


charac er


50


Ci y and s a e in which he WFO office is loca ed






CITY


charac er


50


Ci y designa or for office






STATE


charac er


50


Full s a e name in which office is loca ed






ST


charac er


2


Two charac er s a e abbrevia ion for s a e where office is loca ed












































































US Dep of Commerce


Na ional Oceanic and A mospheric Adminis ra ion


Na ional Wea her Service


GIS




,







Commen s? Ques ions? Please Con ac Us.









Disclaimer


Informa ion Quali y


Help


Glossary





Privacy Policy


Freedom of Informa ion Ac (FOIA)


Abou Us


Career Oppor uni ies
```

---

### 26. Nws Fire Zones Catalog

| Field | Value |
|---|---|
| **Resource ID** | nws_fire_zones_catalog |
| **Official source** | https://www.weather.gov/gis/firezones |
| **Collected** | 2026-09-25T21:12:13.932752-10:00 HST |

```text
NWS Fire Wea her Zones
















































































HOME








FORECAST








Local




Graphical




Avia ion




Marine




Rivers and Lakes




Hurricanes




Severe Wea her




Fire Wea her




Sunrise/Sunse




Long Range Forecas s




Clima e Predic ion




Space Wea her












PAST WEATHER








Pas Wea her




As ronomical Da a




Cer ified Wea her Da a












SAFETY








INFORMATION








Wireless Emergency Aler s




Wea her-Ready Na ion




Brochures




Coopera ive Observers




Daily Briefing




Damage/Fa ali y/Injury S a is ics




Forecas Models




GIS Da a Por al




NOAA Wea her Radio




Publica ions




SKYWARN S orm Spo ers




S ormReady




TsunamiReady




Service Change No ices












EDUCATION








NEWS








SEARCH













Search For





NWS

All NOAA


















ABOUT








Abou NWS




Organiza ion




For NWS Employees




Na ional Cen ers




Careers




Con ac Us




Glossary




Social Media




NWS Transforma ion




































GIS


Na ional Program






NWS Fire Wea her Zones



Wea her.gov
> GIS
> NWS Fire Wea her Zones

















CloudGIS Web Services








NWS Na ional GIS Viewer








AWIPS Basemaps








Me ada a Page





















Shapefile Type: Polygon



Da a source: Derived from NWS Public Forecas Zones



Naming conven ion: z_ddmmyy  where ddmmyy = day-mon h-year



Descrip ion: This da ase depic s he areas of responsibili y for fire wea her forecas s and warnings for each WFO.



Due o echnical issues, he implemen a ion da e for zone changes has been moved o April 16, 2026. New files will be available by March 4, 2026, and he files will be locked down on March 24, 2026.








Descrip ion


Valid da e


Da a Download


# Records


MD5SUM


Documen a ion








Fire Wea her Zones


18 March 2025


fz18mr25.zip


3643


cd7def338de06aa4a6343697e059dd81


Da e las upload: 5-FEB-25


Change His ory


Me ada a






16 April 2026


fz16ap26.zip


3683


17862cbdb414d7b0807ac1765b2af3d0


Da e las upload: 03-MAR-26












Shapefile A ribu es:








Field Name


Type


Wid h, Decimals


Descrip ion








STATE


Charac er


2


U.S. Pos al S andard wo le er abbrevia ion






ZONE


Charac er


3


Zone Number






CWA


Charac er


3


CWA (WFO) abbrevia ion






NAME


Charac er


254


Zone name from






STATE_ZONE


Charac er


5


Conca ena ion of S a e and Zone






TIME_ZONE


Charac er


2


Time zone abbrevia ion






FE_AREA


Charac er


2


Cardinal area of s a e






LON


Numeric


10,5


Longi ude of Cen roid (decimal degrees)






LAT


Numeric


9,5


La i ude of Cen roid (decimal degrees)








































































US Dep of Commerce


Na ional Oceanic and A mospheric Adminis ra ion


Na ional Wea her Service


GIS




,







Commen s? Ques ions? Please Con ac Us.









Disclaimer


Informa ion Quali y


Help


Glossary





Privacy Policy


Freedom of Informa ion Ac (FOIA)


Abou Us


Career Oppor uni ies
```

---

### 27. Nws Marine Zones Catalog

| Field | Value |
|---|---|
| **Resource ID** | nws_marine_zones_catalog |
| **Official source** | https://www.weather.gov/gis/MarineZones |
| **Collected** | 2026-09-25T20:50:14.912559-10:00 HST |

```text
NWS Coas al, Offshore and High Seas Zones
















































































HOME








FORECAST








Local




Graphical




Avia ion




Marine




Rivers and Lakes




Hurricanes




Severe Wea her




Fire Wea her




Sunrise/Sunse




Long Range Forecas s




Clima e Predic ion




Space Wea her












PAST WEATHER








Pas Wea her




As ronomical Da a




Cer ified Wea her Da a












SAFETY








INFORMATION








Wireless Emergency Aler s




Wea her-Ready Na ion




Brochures




Coopera ive Observers




Daily Briefing




Damage/Fa ali y/Injury S a is ics




Forecas Models




GIS Da a Por al




NOAA Wea her Radio




Publica ions




SKYWARN S orm Spo ers




S ormReady




TsunamiReady




Service Change No ices












EDUCATION








NEWS








SEARCH













Search For





NWS

All NOAA


















ABOUT








Abou NWS




Organiza ion




For NWS Employees




Na ional Cen ers




Careers




Con ac Us




Glossary




Social Media




NWS Transforma ion




































GIS


Na ional Program






NWS Coas al, Offshore and High Seas Zones



Wea her.gov
> GIS
> NWS Coas al, Offshore and High Seas Zones

















CloudGIS Web Services








NWS Na ional GIS Viewer








AWIPS Basemaps








Me ada a Page





















Overview of Coas al, Offshore and High Seas Marine Zones







De ailed view of he Marine Zones and access o forecas s.


De ailed view of he Offshore Zones and access o forecas s.



Shapefile Type: Polygon



Da a source: Coas line derived from US Coun ies



Naming conven ion: mzddmmyy (coas al marine zones), ozddmmyy (offshore zones), hzddmmyy (high seas zones)  where ddmmyy = day-mon h-year



NWS Specifica ions: NWSI 10-302



Descrip ion: The NWS issues marine forecas s, wa ches, warnings and advisories for a se of defined zone for offshore and coas al wa ers of he U.S.



Due o echnical issues, he implemen a ion da e for zone changes has been moved o April 16, 2026. New files will be available by March 4, 2026, and he files will be locked down on March 24, 2026. (High Seas Zones are curren ly valid.)








Descrip ion


Valid da e


Da a Download


# Records


MD5SUM


Documen a ion








Coas al Marine Zones


Including he Grea Lakes


18 March 2025


mz18mr25.zip


566


df33ce3efc028639d870a9848c636669


Da e las upload: 20-FEB-25


Change His ory


Me ada a






16 April 2026


mz16ap26.zip


569


f191552ac0810b4bc4d11b46a87c2aeb


Da e las upload: 03-MAR-26






Offshore Marine Zones


18 March 2025


oz18mr25.zip


130


45ba9aca774938a4f8534fa798c8cb90


Da e las upload: 20-FEB-25


Change His ory


Me ada a






16 April 2026


oz16ap26.zip


130


aa39c4bca11fcb4d949078cef292fd7d


Da e las upload: 03-MAR-26






High Seas Marine Zones


20 February 2025


hz20fe25.zip


6


33a74c3f06339ca5080ef45101bb532f


Da e las upload: 20-FEB-25


Change His ory


Me ada a






17 February 2026


hz17fe26.zip


5


9d89a9b2c485418a2848861cf047eb6c


Da e las upload: 12-FEB-26












Shapefile A ribu es:








Field Name


Type


wid h,dec


Descrip ion






ID


charac er


6


Marine Zone Iden ifier






WFO


charac er


3


Assigned WFO (Office Iden ifier)






GL_WFO


charac er


3


Grea lakes WFO responsible for Open Lake Forecas s






NAME


charac er


250


Name of Marine Zone (In he offshore zone file, his a ribu e is "Name")






AJOIN0


charac er


5


No Used






AJOIN1


charac er


5


No Used






LON


numeric


10,5


Longi ude of Cen roid [decimal degrees]






LAT


numeric


9,5


La i ude of Cen roid [decimal degrees]












































































US Dep of Commerce


Na ional Oceanic and A mospheric Adminis ra ion


Na ional Wea her Service


GIS




,







Commen s? Ques ions? Please Con ac Us.









Disclaimer


Informa ion Quali y


Help


Glossary





Privacy Policy


Freedom of Informa ion Ac (FOIA)


Abou Us


Career Oppor uni ies
```

---

### 28. Nws Public Counties Catalog

| Field | Value |
|---|---|
| **Resource ID** | nws_public_counties_catalog |
| **Official source** | https://www.weather.gov/gis/Counties |
| **Collected** | 2026-09-25T21:15:46.134777-10:00 HST |

```text
nn northern         ss southern         ea east
 ee eastern          ww western          er east central upper
 cc central          pa panhandle        eu eastern upper 
 ne north eastern    se south eastern    nr north central upper
 nw north western    sw south western    sr south central upper  
 nc north central    sc south central    wu western upper
 ec east central     wc west central     so south
 mi middle           pd piedmont
 bb big bend         up upstate
```

---

### 29. Nws Public Zones Catalog

| Field | Value |
|---|---|
| **Resource ID** | nws_public_zones_catalog |
| **Official source** | https://www.weather.gov/gis/publiczones |
| **Collected** | 2026-09-25T21:11:38.087083-10:00 HST |

```text
NWS Public Forecas Zones
















































































HOME








FORECAST








Local




Graphical




Avia ion




Marine




Rivers and Lakes




Hurricanes




Severe Wea her




Fire Wea her




Sunrise/Sunse




Long Range Forecas s




Clima e Predic ion




Space Wea her












PAST WEATHER








Pas Wea her




As ronomical Da a




Cer ified Wea her Da a












SAFETY








INFORMATION








Wireless Emergency Aler s




Wea her-Ready Na ion




Brochures




Coopera ive Observers




Daily Briefing




Damage/Fa ali y/Injury S a is ics




Forecas Models




GIS Da a Por al




NOAA Wea her Radio




Publica ions




SKYWARN S orm Spo ers




S ormReady




TsunamiReady




Service Change No ices












EDUCATION








NEWS








SEARCH













Search For





NWS

All NOAA


















ABOUT








Abou NWS




Organiza ion




For NWS Employees




Na ional Cen ers




Careers




Con ac Us




Glossary




Social Media




NWS Transforma ion




































GIS


Na ional Program






NWS Public Forecas Zones



Wea her.gov
> GIS
> NWS Public Forecas Zones

















CloudGIS Web Services








NWS Na ional GIS Viewer








AWIPS Basemaps








Me ada a Page





















Shapefile Type: Polygon



Da a source: Derived from US Coun ies



Naming conven ion: z_ddmmyy  where ddmmyy = day-mon h-year



NWS Specifica ions: NWSM 10-507



Descrip ion: The NWS issues forecas s and some wa ches and warnings for public zones which usually are he same as coun ies bu in many cases are subse s of coun ies.  Coun ies are subse in o zones o allow for more accura e forecas s because of he differences in wea her wi hin a coun y due o such hings as eleva ion or proximi y o large bodies of wa er.



Due o echnical issues, he implemen a ion da e for zone changes has been moved o April 16, 2026. New files will be available by March 4, 2026, and he files will be locked down on March 24, 2026.












Descrip ion


Valid da e


Da a Download


# Records


MD5SUM


Documen a ion








Public Forecas Zones


18 March 2025


z_18mr25.zip


4114


388062c3036e4518d07c9fb09d68ff6f


Da e las upload: 5-FEB-25


Change His ory


Me ada a






16 April 2026


z_16ap26.zip


4157


004dc6501dc3d50e7b36652cb9d02bd3


Da e las upload: 13-APR-26












Shapefile A ribu es:








Field Name


Type


Wid h, Decimals


Descrip ion








STATE


Charac er


2


U.S. Pos al S andard wo le er abbrevia ion






ZONE


Charac er


3


Zone Number from NWSI 10-507.






CWA


Charac er


3


CWA (WFO) abbrevia ion from NWSI 10-507.






NAME


Charac er


254


Zone name from NWSI 10-507.






STATE_ZONE


Charac er


5


Conca ena ion of S a e and Zone






TIME_ZONE


Charac er


2


Time zone abbrevia ion






FE_AREA


Charac er


2


Cardinal area of s a e






LON


Numeric


10,5


Longi ude of Cen roid (decimal degrees)






LAT


Numeric


9,5


La i ude of Cen roid (decimal degrees)






SHORTNAME


Charac er


32


Name runca ed o 32 charac ers












































































US Dep of Commerce


Na ional Oceanic and A mospheric Adminis ra ion


Na ional Wea her Service


GIS




,







Commen s? Ques ions? Please Con ac Us.









Disclaimer


Informa ion Quali y


Help


Glossary





Privacy Policy


Freedom of Informa ion Ac (FOIA)


Abou Us


Career Oppor uni ies
```

---

### 30. Nws Zone County Catalog

| Field | Value |
|---|---|
| **Resource ID** | nws_zone_county_catalog |
| **Official source** | https://www.weather.gov/gis/ZoneCounty |
| **Collected** | 2026-09-25T20:58:54.560234-10:00 HST |

```text
Zone-coun y Correla ion File
















































































HOME








FORECAST








Local




Graphical




Avia ion




Marine




Rivers and Lakes




Hurricanes




Severe Wea her




Fire Wea her




Sunrise/Sunse




Long Range Forecas s




Clima e Predic ion




Space Wea her












PAST WEATHER








Pas Wea her




As ronomical Da a




Cer ified Wea her Da a












SAFETY








INFORMATION








Wireless Emergency Aler s




Wea her-Ready Na ion




Brochures




Coopera ive Observers




Daily Briefing




Damage/Fa ali y/Injury S a is ics




Forecas Models




GIS Da a Por al




NOAA Wea her Radio




Publica ions




SKYWARN S orm Spo ers




S ormReady




TsunamiReady




Service Change No ices












EDUCATION








NEWS








SEARCH













Search For





NWS

All NOAA


















ABOUT








Abou NWS




Organiza ion




For NWS Employees




Na ional Cen ers




Careers




Con ac Us




Glossary




Social Media




NWS Transforma ion




































GIS


Na ional Program






Zone-coun y Correla ion File



Wea her.gov
> GIS
> Zone-coun y Correla ion File

















CloudGIS Web Services








NWS Na ional GIS Viewer








AWIPS Basemaps








Me ada a Page





















File ype: Pipe delimi ed ex



Da a Source: Derived from U.S. Coun ies and NWS Public Forecas Zones



Naming Conven ion: bp ddmmyy.dbx. where ddmmyy = day-mon h-year



Descrip ion: Each record represen s a single polygon from he public forecas zone shapefile.  Whenever a coun y is divided in o mul iple zones, here will exis a record for each coun y wi h he same zone.



No e: S ar ing wi h he 1 May 2018 file (bp01my18.dbx - now invalid), he CWA field will be a reference o he zone field, and no he coun y field.





Due o echnical issues, he implemen a ion da e for zone changes has been moved o April 16, 2026. New files will be available by March 4, 2026, and he files will be locked down on March 24, 2026.












Descrip ion


Valid da e


Da a Download






Coun y-Public Forecas Zones Correla ion file


18 March 2025


Da e las upload: 05-FEB-2025


bp18mr25.dbx






16 April 2026


Da e las upload: 03-MAR-2026


bp16ap26.dbx












Record Forma :








Name


Descrip ion








STATE


Two charac er s a e abbrevia ion






ZONE


Three charac er zone number






CWA


Three charac er CWA ID (of he zone, s ar ing wi h 01 May 2018 file)






NAME


Zone name






STATE_ZONE


5 charac er s a e + hree charac er zone number






COUNTY


Coun y name






FIPS


5 charac er s a e-coun y FIPS code






TIME_ZONE


Time zone of polygon (See commen s on coun y page)






FE_AREA


Fea ure Area (loca ion in STATE - See commen s on coun y page)






LAT


La i ude of cen roid of he zone






LON


Longi ude of cen roid of he zone












































































US Dep of Commerce


Na ional Oceanic and A mospheric Adminis ra ion


Na ional Wea her Service


GIS




,







Commen s? Ques ions? Please Con ac Us.









Disclaimer


Informa ion Quali y


Help


Glossary





Privacy Policy


Freedom of Informa ion Ac (FOIA)


Abou Us


Career Oppor uni ies
```

---

### 31. Offshore Forecast (40-240nm)

| Field | Value |
|---|---|
| **Resource ID** | off_offshore_forecast |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=OFF&issuedby=HFO |
| **Collected** | 2026-09-25T17:19:08.105755-10:00 HST |

```text
779
FZHW60 PHFO 260301
OFFHFO

Offshore Wa ers Forecas for Hawaii
Na ional Wea her Service Honolulu HI
501 PM HST Fri Sep 25 2026

Hawaiian offshore wa ers beyond 40 nau ical miles ou o 240
nau ical miles including he por ion of he Papahanaumokuakea
Marine Na ional Monumen eas of French Friga e Shoals

Seas given as significan wave heigh , which is he average heigh
of he highes 1/3 of he waves. Individual waves may be more han
wice he significan wave heigh .

PHZ105-261130-
501 PM HST Fri Sep 25 2026

.Synopsis for he Hawaiian offshore wa ers...
S rong winds and hazardous seas will accompany Hurricane Nolo as
i advances nor h and hen wes ward across area wa ers oday
hrough he weekend.

AT 500 PM HST HURRICANE NOLO WAS CENTERED AT 16.9N 155.3W...MOVING N
AT 3 KT

NOLO FORECAST POSITIONS
200 AM HST SATURDAY 17.1N 155.5W
200 PM HST SATURDAY 17.1N 156.4W
200 AM HST SUNDAY 16.9N 157.9W
200 PM HST SUNDAY 16.9N 159.8W
200 AM HST MONDAY 17.7N 161.7W
200 PM HST MONDAY 19.1N 163.2W
200 PM HST TUESDAY 22.0N 164.5W
200 PM HST MONDAY 23.6N 165.5W
200 PM HST TUESDAY 25.0N 168.0W
200 PM HST WEDNESDAY 25.0N 171.0W

PHZ180-261130-
Hawaiian Offshore Wa ers-
501 PM HST Fri Sep 25 2026

...HURRICANE WARNING IN EFFECT...

.TONIGHT...Hurricane condi ions expec ed. E winds 15 o 25 k NW
Half, E 80 o 90 k SE Half. Seas 8 o 14 f . Sca ered
hunders orms SE Wa ers.

.SATURDAY...Hurricane condi ions expec ed. E winds 20 o 30 k NW
Half, E 85 o 95 k SE Half. Seas 8 o 14 f . Isola ed
hunders orms SE Wa ers.
.SATURDAY NIGHT...Hurricane condi ions expec ed. E winds 20 o 30
k NW Half, E 90 o 100 k SE Half. Seas 9 o 14 f . Sca ered
hunders orms SE Wa ers.
.SUNDAY...Hurricane condi ions expec ed. NW Half, E winds 30 o
40 k , rising o 40 o 50 k la e in he af ernoon. SE Half, E
winds 90 o 100 k , diminishing o 50 o 60 k . Seas 9 o 14 f .
Isola ed hunders orms NW Half - sca ered hunders orms SE
Wa ers.
.SUNDAY NIGHT...Hurricane condi ions expec ed. E winds 75 o 85
k NW Half, E 40 o 50 k SE Half. Seas 8 o 14 f . Isola ed
hunders orms S of 20N.
.MONDAY...Hurricane condi ions expec ed. E winds 95 o 105 k NW
Half, E 20 o 30 k SE Half. Seas 7 o 13 f . Isola ed
hunders orms S of 24N.
.TUESDAY...Hurricane condi ions possible. E winds 80 o 90 k NW
Half, E 15 o 25 k SE Half. Seas 6 o 13 f . Isola ed
hunders orms S of 24N.
.WEDNESDAY...Hurricane condi ions possible. SE winds 30 o 40 k
NW Half, E 15 o 25 k SE Half. Seas 6 o 11 f .
```

---

### 32. Radar status/outage text messages

| Field | Value |
|---|---|
| **Resource ID** | ftm_radar_status |
| **Official source** | /hfo/FTM |
| **Collected** | 2026-09-25T16:42:31.196621-10:00 HST |

```text
Kauai Radar (PHKI/SOK)
No outage message at this time.

----

Molokai Radar (PHMO/HMO)
858
NOUS60 PHFO 242239
FTMHMO

WSR-88D NOTIFICATION
NATIONAL WEATHER SERVICE HONOLULU HI
1239 PM HST THU SEP 24 2026

WSR-88D PHMO/HMO MOLOKAI RADAR IS BACK IN SERVICE.

----

Upolu Point/North Kohala Radar (PHKM/UPP)
646
NOUS60 PHFO 252159
FTMHKM

WSR-88D NOTIFICATION
NATIONAL WEATHER SERVICE HONOLULU HI
1159 AM HST FRI SEP 25 2026

WSR-88D PHKM/UPP UPOLU POINT RADAR IS BACK IN SERVICE.

LF

----

Naalehu/South Hawaii (PHWA/HWC)
No outage message at this time.
```

---

### 33. State Forecast for Hawaii

| Field | Value |
|---|---|
| **Resource ID** | sfp_state_forecast |
| **Official source** | https://api.weather.gov/products/types/SFP/locations/HFO |
| **Collected** | 2026-09-25T17:09:33.005853-10:00 HST |

```text
{"@id": "https://api.weather.gov/products/a55c50e8-ef57-4b0a-9a1e-9be99cc0ba7a", "id": "a55c50e8-ef57-4b0a-9a1e-9be99cc0ba7a", "wmoCollectiveId": "FPHW60", "issuingOffice": "PHFO", "issuanceTime": "2026-09-26T02:59:00+00:00", "productCode": "SFP", "productName": "State Forecast"}
```

---

### 34. Statewide Surf Observations

| Field | Value |
|---|---|
| **Resource ID** | surfreports_statewide_observations |
| **Official source** | /hfo/surfreports |
| **Collected** | Unknown HST |

```text
948
SXHW80 PHFO 260115
OMRHFO

SURF OBSERVATIONS
NATIONAL WEATHER SERVICE HONOLULU HI
315 PM HST FRI SEP 25 2026

FULL FACE SURF OBSERVATIONS ARE TAKEN BY COUNTY LIFE GUARDS AND
COOPERATIVE OBSERVERS AND RELAYED TO THE NATIONAL WEATHER SERVICE
FOR DISSEMINATION. THESE OBSERVATIONS ARE NOT QUALITY CONTROLLED.

HIZ003-004-029>031-260100-
KAUAI-

LOCATION        TIME   SURF HEIGHT DIR   PER                  REMARKS
KEE          1235 PM           2-5  NE     9
HAENA        1235 PM           2-5  NE     9
HANALEI      1235 PM           0-2
ANAHOLA      1235 PM           3-6 ENE     9
KEALIA       1235 PM          6-10 ENE    10
LYDGATE      1235 PM          4-8+ ENE    10
POIPU        1235 PM           2-4
SALT POND    1235 PM           2-4
KEKAHA       1235 PM           1-3
$$

HIZ006-007-009>011-032>036-260100-
OAHU-

LOCATION        TIME   SURF HEIGHT DIR PER         WIND      REMARKS
DIAMOND HEAD
SUNSET
WAIKIKI      1145 AM           0-1            ENE 10-15       CANOES
SANDY BEACH  1145 AM           2-3            ENE 15-20  SHORE BREAK
MAKAPUU      1145 AM           4-6            ENE 10-15
EHUKAI       1145 AM           0-1             NE 10-15
MAKAHA       1145 AM           0-1               VRB 05
$$

HIZ015>018-022-045>050-260100-
MAUI-MOLOKAI-LANAI-KAHOOLAWE-

LOCATION        TIME   SURF HEIGHT   DIR         WIND      REMARKS
KANAHA       1108 AM           1-3          NE 10-20+  PARTLY CLDY
BALDWIN SHOR 1109 AM           1-2           NE 15-25  PARTLY CLDY
BALDWIN OUTE 1109 AM           3-6           NE 15-25  PARTLY CLDY
HOOKIPA      1110 AM           1-4           NE 10-20  MOSTLY CLDY
KAMAOLE I    1111 AM           1-2           NE 10-20        SUNNY
KAMAOLE III  1112 AM           0-1           NE 20-30  PARTLY CLDY
HANAKAOO
FLEMING
$$

HIZ023-026>028-051>054-260100-
BIG ISLAND OF HAWAII-

LOCATION        TIME   SURF HEIGHT   DIR         WIND      REMARKS
RICHARDSONS  1101 AM           2-3     E      VRB 0-5  OVERCAST/RA
HONOLII      1102 AM           3-5            L/V 0-5         RAIN
PUNALU`U
ISAAC HALE   1103 AM          5-6+            NE 5-10         RAIN
HAPUNA
KAHALUU      1105 AM           3-5    NW      L/V 0-5     OVERCAST
MAGIC SANDS  1106 AM           0-1            L/V 0-5     OVERCAST
KUA BAY      1107 AM    1-2 OCNL 3           SW 10-15     OVERCAST
$$

LEGEND
   SURF HEIGHT              - Reported in feet
   WIND AND SWELL DIRECTION - Reported in 16 pt compass
   PERIOD /PER/             - Reported in seconds
   VISIBILITY /VIS/         - Reported in statute miles
   CLARITY                  - Water clarity
   TIME                     - Hawaiian Standard Time
   WIND SPEED               - Reported in miles per hour
   + /IN SURF HEIGHT/       - Occasionally higher sets
   0 /IN SURF HEIGHT/       - Flat

$$
```

---

### 35. Tsunami Bulletin product type reference

| Field | Value |
|---|---|
| **Resource ID** | hfo_tib_reference |
| **Official source** | https://forecast.weather.gov/product_types.php |
| **Collected** | 2026-09-25T21:17:28.837777-10:00 HST |

```text
Na ional Wea her Service







































Toggle naviga ion











HOME




FORECAST






Local




Graphical




Avia ion




Marine




Rivers and Lakes




Hurricanes




Severe Wea her




Fire Wea her




Sunrise/Sunse




Long Range Forecas s




Clima e Predic ion




Space Wea her









PAST WEATHER






Pas Wea her




As ronomical Da a




Cer ified Wea her Da a









SAFETY











INFORMATION






Wireless Emergency Aler s




Wea her-Ready Na ion




Brochures




Coopera ive Observers




Daily Briefing




Damage/Fa ali y/Injury S a is ics




Forecas Models




GIS Da a Por al




NOAA Wea her Radio




Publica ions




SKYWARN S orm Spo ers




S ormReady




TsunamiReady




Service Change No ices









EDUCATION











NEWS











SEARCH











Search For





NWS

All NOAA















ABOUT






Abou NWS




Organiza ion




For NWS Employees




Na ional Cen ers




Careers




Con ac Us




Glossary




Social Media




NWS Transforma ion



















NWS Wea her Forecas Office Produc Lis ing



Click on he produc iden ifier or descrip ion o view produc s:





Produc Iden ifier

Produc Descrip ion



ABV

Rawinsonde Da a Above 100 Millibars



ADA

Alarm/Aler Adminis ra ive Msg



ADM

Aler Adminis ra ive Message



ADR

NWS Adminis ra ive Message



ADV

Generic Space Environmen Advisory



AFD

Area Forecas Discussion



AFM

Area Forecas Ma rices



AFP

Area Forecas Produc



AFW

Fire Wea her Ma rix



AGF

Agricul ural Forecas



AGO

Agricul ural Observa ions



ALT

Space Environmen Aler



AQA

Air Quali y Aler



AQI

Air Quali y Index S a emen



ASA

Air S agna ion Advisory



AVA

Avalanche Wa ch



AVG

Avalanche Wea her Guidance



AVW

Avalanche Warning



AWO

Area Wea her Ou look



AWS

Area Wea her Summary



AWU

Area Wea her Upda e



AWW

Airpor Wea her Warning



BLU

Blue Aler



BOY

Buoy Repor



BRG

Coas Guard Observa ions



BRT

Hourly Roundup for Wea her Radio



CAE

Child Abduc ion Emergency



CCF

Coded Ci y Forecas



CDW

Civil Danger Warning



CEM

Civil Emergency Message



CF6

WFO Mon hly/Daily Clima e Da a



CFP

Convec ive Forecas Produc



CFW

Coas al Flood Warnings/Wa ches/S a emen s



CGR

Coas Guard Surface Repor



CHG

Compu er Hurricane Guidance



CLA

Clima ological Repor (Annual)



CLI

Clima ological Repor (Daily)



CLM

Clima ological Repor (Mon hly)



CLQ

Clima ological Repor (Quar erly)



CLS

Clima ological Repor (Seasonal)



CLT

Clima e Repor



CMM

Coded Clima ological Mon hly Means



COD

Coded Analysis and Forecas s



CPF

Grea Lakes Por Forecas



CUR

Rou ine Space Environmen Produc s



CWA

Cen er (CWSU) Wea her Advisory



CWF

Coas al Wa ers Forecas



CWS

Cen er (CWSU) Wea her S a emen



DAY

Rou ine Space Environmen Produc (Daily)



DDO

Daily Dispersion Ou look



DGT

Drough Informa ion S a emen



DMO

Prac ice/Demo Warning



DSA

Unnumbered Depression / Suspicious Area Advisory



DSM

ASOS Daily Summary



DSW

Dus S orm Warning and Dus Advisory



EFP

3 To 5 Day Ex ended Forecas



EOL

Average 6 To 10 Day Wea her Ou look (Local)



EQI

Tsunami Bulle in



EQR

Ear hquake Repor



EQW

Ear hquake Warning



ESF

Flood Po en ial Ou look



ESG

Ex ended S reamflow Guidance



ESP

Ex ended S reamflow Predic ion



ESS

Wa er Supply Ou look



EVI

Evacua ion Immedia e



EWW

Ex reme Wind Warning



FA0

Avia ion Area Forecas s (Pacific)



FA1

Avia ion Area Forecas s (Nor heas )



FA2

Avia ion Area Forecas s (Sou heas )



FA3

Avia ion Area Forecas s (Nor h Cen ral)



FA4

Avia ion Area Forecas s (Sou h Cen ral)



FA5

Avia ion Area Forecas s (Rocky Moun ains)



FA6

Avia ion Area Forecas s (Wes Coas )



FA7

Avia ion Area Forecas s (Juneau, AK)



FA8

Avia ion Area Forecas s (Anchorage, AK)



FA9

Avia ion Area Forecas s (Fairbanks, AK)



FD0

24 Hr Fd Winds Alof Fcs (45,000 and 53,000 F )



FD1

6 Hour Winds Alof Forecas



FD2

12 Hour Winds Alof Forecas



FD3

24 Hour Winds Alof Forecas



FD4

Winds Alof Forecas



FD5

Winds Alof Forecas



FD6

Winds Alof Forecas



FD7

Winds Alof Forecas



FD8

6 Hour Fd Winds Alof Fcs (45,000 and 53,000 F )



FD9

12 Hr Fd Winds Alof Fcs (45,000 and 53,000 F )



FDI

Fire Danger Indices



FFA

Flash Flood Wa ch



FFG

Flash Flood Guidance



FFH

Headwa er Guidance



FFS

Flash Flood S a emen



FFW

Flash Flood Warning



FLN

Na ional Flood Summary



FLS

Flood S a emen



FLW

Flood Warning



FOF

Upper Wind Fallou Forecas



FRW

Fire Warning



FSH

Na l Marine Fisheries Adminis ra ive Service Message



FTM

WSR-88D Radar Ou age No ifica ion / Free Tex Message



FTP

FOUS Prog Max/Min Temp/Pop Guidance



FWA

Fire Wea her Adminis ra ive Message



FWD

Fire Wea her Ou look Discussion



FWF

Rou ine Fire Wx Fcs (Wi h/Wi hou 6-10 Day Ou look)



FWL

Land Managemen Forecas s



FWM

Miscellaneous Fire Wea her Produc



FWN

Fire Wea her No ifica ion



FWO

Fire Wea her Observa ion



FWS

Spo Forecas



FZL

Freezing Level Da a (RADAT)



GLF

Grea Lakes Forecas



GLS

Grea Lakes S orm Summary



GRE

GREEN



HD1

RFC Derived QPF Da a Produc



HD2

RFC Derived QPF Da a Produc



HD3

RFC Derived QPF Da a Produc



HD4

RFC Derived QPF Da a Produc



HD7

RFC Derived QPF Da a Produc



HD8

RFC Derived QPF Da a Produc



HD9

RFC Derived QPF Da a Produc



HLS

Hurricane Local S a emen



HMD

Hydrome eorological Discussion



HML

AHPS XML



HMW

Hazardous Ma erials Warning



HP1

RFC QPF Verifica ion Produc



HP2

RFC QPF Verifica ion Produc



HP3

RFC QPF Verifica ion Produc



HP4

RFC QPF Verifica ion Produc



HP5

RFC QPF Verifica ion Produc



HP6

RFC QPF Verifica ion Produc



HP7

RFC QPF Verifica ion Produc



HP8

RFC QPF Verifica ion Produc



HRR

Wea her Roundup



HSF

High Seas Forecas



HWO

Hazardous Wea her Ou look



HWR

Hourly Wea her Roundup



HYD

Daily Hydrome eorological Produc s



HYM

Mon hly Hydrome eorological Plain Language Produc



ICE

Ice Forecas



IDM

Ice Drif Vec ors



INI

ADMINISTR [NOUS51 KWBC]



IOB

Ice Observa ion



KPA

Keep Alive Message



LAE

Local Area Emergency



LCD

Preliminary Local Clima ological Da a



LCO

Local Coopera ive Observa ion



LEW

Law Enforcemen Warning



LFP

Local Forecas



LKE

Lake S ages



LLS

Low-Level Sounding



LOW

Low Tempera ures



LSR

Local S orm Repor



LTG

Ligh ning Da a



MAN

Rawinsonde Observa ion Manda ory Levels



MAP

Mean Areal Precipi a ion



MAW

Amended Marine Forecas



MFM

Marine Forecas Ma rix



MIM

Marine In erpre a ion Message



MIS

Miscellaneous Local Produc



MOB

MOB Observa ions



MON

Rou ine Space Environmen Produc Issued Mon hly



MRP

Techniques Developmen Labora ory Marine Produc



MSM

ASOS Mon hly Summary Message



MTR

METAR Forma ed Surface Wea her Observa ion



MTT

METAR Tes Message



MVF

Marine Verifica ion Coded Message



MWS

Marine Wea her S a emen



MWW

Marine Wea her Message



NOU

Wea her Reconnaisance Fligh s



NOW

Shor Term Forecas



NOX

Da a Mg Message



NPW

Non-Precipi a ion Warnings / Wa ches / Advisories



NSH

Nearshore Marine Forecas



NUW

Nuclear Power Plan Warning



NWR

NOAA Wea her Radio Forecas



OAV

O her Avia ion Produc s



OBS

Observa ions



OFA

Offshore Avia ion Area Forecas



OFF

Offshore Forecas



OMR

O her Marine Produc s



OPU

O her Public Produc s



OSO

O her Surface Observa ions



OSW

Ocean Surface Winds



OUA

O her Upper Air Da a



OZF

Zone Forecas



PFM

Poin Forecas Ma rices



PFW

Fire Wea her Poin Forecas Ma rices



PLS

Plain Language Ship Repor



PMD

Prognos ic Me eorological Discussion



PNS

Public Informa ion S a emen



POE

Probabili y of Exceed



PRB

Hea Index Forecas Tables



PRC

S a e Pilo Repor Collec ive



PRE

Preliminary Forecas s



PSH

Pos S orm Hurricane Repor



PTS

Probabilis ic Ou look Poin s



PWO

Public Severe Wea her Ou look



PWS

Tropical Cyclone Probabili ies



QPF

Quan i a ive Precipi a ion Forecas



QPS

Quan i a ive Precipi a ion S a emen



RDF

Revised Digi al Forecas



REC

Recrea ional Repor



RER

Record Repor



RET

EAS Ac iva ion Reques



RFD

Rangeland Fire Danger Forecas



RFI

RFI Observa ion



RFR

Rou e Forecas



RFW

Red Flag Warning



RHW

Radiological Hazard Warning



RMT

Required Mon hly Tes



RNS

Rain Informa ion S a emen



RR1

Hydro-Me Da a Repor Par 1



RR2

Hydro-Me Da a Repor Par 2



RR3

Hydro-Me Da a Repor Par 3



RR4

Hydro-Me Da a Repor Par 4



RR5

Hydro-Me Da a Repor Par 5



RR6

Hydro-Me Da a Repor Par 6



RR7

Hydro-Me Da a Repor Par 7



RR8

Hydro-Me Da a Repor Par 8



RR9

Hydro-Me Da a Repor Par 9



RRA

Au oma ed Hydrologic Observa ion S a Repor (AHOS)



RRM

Miscellaneous Hydrologic Da a



RRS

HADS Da a



RRY

ASOS SHEF Hourly Rou ine Tes Message



RSD

Daily Sno el Da a



RSM

Mon hly Sno el Da a



RTP

Regional Max/Min Temp and Precipi a ion Table



RVA

River Summary



RVD

Daily River Forecas s



RVF

River Forecas



RVI

River Ice S a emen



RVM

Miscellaneous River Produc



RVR

River Recrea ion S a emen



RVS

River S a emen



RWR

Regional Wea her Roundup



RWS

Regional Wea her Summary



RWT

Required Weekly Tes



SAB

Special Avalanche Bulle in



SAF

Speci Agri Wx Fcs / Advisory / Flying Farmer Fcs Ou look



SAG

Snow Avalanche Guidance



SAT

APT Predic ion



SAW

Prelim No ice of Wa ch & Cancella ion Msg (Avia ion)



SCC

S orm Summary



SCD

Supplemen ary Clima ological Da a (ASOS)



SCN

Soil Clima e Analysis Ne work Da a



SCP

Sa elli e Cloud Produc



SCS

Selec ed Ci ies Summary



SDO

Supplemen ary Da a Observa ion (ASOS)



SDS

Special Dispersion S a emen



SEL

Severe Local S orm Wa ch and Wa ch Cancella ion Msg



SEV

SPC Wa ch Poin Informa ion Message



SFP

S a e Forecas



SFT

Tabular S a e Forecas



SGL

Rawinsonde Observa ion Significan Levels



SHP

Surface Ship Repor a Synop ic Time



SIG

In erna ional Sigme / Convec ive Sigme



SIM

Sa elli e In erpre a ion Message



SLS

Severe Local S orm Wa ch and Areal Ou line



SMF

Smoke Managemen Wea her Forecas



SMW

Special Marine Warning



SOO

SOO Produc



SPE

Sa elli e Precipi a ion Es ima es (TXUS20 KWBC)



SPF

S orm S rike Probabili y Bulle in (TPC)



SPS

Special Wea her S a emen



SPW

Shel er in Place Warning



SQW

Snow Squall Warning



SRD

Surf Discussion



SRF

Surf Forecas



SRG

Soaring Guidance



SSM

Main Synop ic Hour Surface Observa ion



STA

Ne work and Severe Wea her S a is ical Summaries



STD

Sa elli e Tropical Dis urbance Summary



STO

Road Condi ion Repor s (S a e Agencies)



STP

S a e Max/Min Tempera ure and Precipi a ion Table



STQ

Spo Forecas Reques



SUM

Space Wea her Message



SVR

Severe Thunders orm Warning



SVS

Severe Wea her S a emen



SWO

Severe S orm Ou look Narra ive (AC)



SWS

S a e Wea her Summary



SYN

Regional Wea her Synopsis



TAF

Terminal Aerodrome Forecas



TAP

Terminal Aler ing Produc s



TAV

Travelers Forecas Table



TCA

Avia ion Tropical Cyclone Advisory



TCD

Tropical Cyclone Discussion



TCE

Tropical Cyclone Posi ion Es ima e



TCM

Marine/Avia ion Tropical Cyclone Advisory



TCP

Public Tropical Cyclone Advisory



TCS

Sa elli e Tropical Cyclone Summary



TCU

Tropical Cyclone Upda e



TCV

Tropical Cyclone Wa ch/Warning Break Poin s



TIB

Tsunami Bulle in



TID

Tide Repor



TMA

Tsunami Tide/Seismic Message Acknowledgemen



TOE

911 Telephone Ou age Emergency



TOR

Tornado Warning



TPT

Tempera ure Precipi a ion Table (Na l and In nl)



TSU

Tsunami Wa ch/Warning



TUV

Wea her Bulle in



TVL

Travelers Forecas



TWB

Transcribed Wea her Broadcas



TWD

Tropical Wea her Discussion



TWO

Tropical Wea her Ou look and Summary



TWS

Tropical Wea her Summary



URN

Aircraf Reconnaissance



UVI

Ul raviole Index



VAA

Volcanic Ac ivi y Advisory



VER

Forecas Verifica ion S a is ics



VFT

Terminal Aerodrome Forecas (TAF) Verifica ion



VOW

Volcano Warning



WA0

Airme (Pacific)



WA1

Airme (Nor heas )



WA2

Airme (Sou heas )



WA3

Airme (Nor h Cen ral)



WA4

Airme (Sou h Cen ral)



WA5

Airme (Rocky Moun ains)



WA6

Airme (Wes Coas )



WA7

Airme (Juneau, AK)



WA8

Airme (Anchorage, AK)



WA9

Airme (Fairbanks, AK)



WAR

Space Environmen Warning



WAT

Space Environmen Wa ch



WCN

Wea her Wa ch Clearance No ifica ion



WCR

Weekly Wea her and Crop Repor



WDA

Weekly Da a for Agricul ure



WDU

Warning Decision Upda e



WEK

Rou ine Space Environmen Produc Issued Weekly



WOU

Tornado/Severe Thunders orm Wa ch



WS1

Sigme (Nor heas )



WS2

Sigme (Sou heas )



WS3

Sigme (Nor h Cen ral)



WS4

Sigme (Sou h Cen ral)



WS5

Sigme (Rocky Moun ains)



WS6

Sigme (Wes Coas )



WST

Tropical Cyclone Sigme



WSV

Volcanic Ac ivi y Sigme



WSW

Win er Wea her Warnings / Wa ches / Advisories



WWA

Wa ch S a us Repor



WWP

Severe Thunders orm / Tornado Wa ch Probabili ies



ZFP

Zone Forecas Produc



















US Dep of Commerce


Na ional Oceanic and A mospheric Adminis ra ion


Na ional Wea her Service


1325 Eas Wes Highway




Silver Spring, MD 20910




Commen s? Ques ions? Please Con ac Us.










Disclaimer


Informa ion Quali y


Help


Glossary










Privacy Policy


Freedom of Informa ion Ac (FOIA)


Abou Us


Career Oppor uni ies
```

---

---

_Generated automatically by the RootRecord weather reporting pipeline._
