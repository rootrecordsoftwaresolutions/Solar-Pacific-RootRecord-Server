# 🌺 Hawaiʻi State Weather Database

> **RootRecord's continuously updated, source-preserving weather reporting layer for Hawaiʻi.**

## 🛰️ Live GOES-18 Hawaii GeoColor

<img src="https://raw.githubusercontent.com/rootrecordsoftwaresolutions/RootRecord-Weather-Database/main/Hawai%27i/reports/assets/GOES18-HI-GEOCOLOR-README-banner.gif" width="100%" alt="GOES-18 Hawaii GeoColor" />

## 🌐 What This Is

This directory is the human-readable reporting layer built from the locally collected Hawaiʻi weather database.

The system keeps a strict separation between:

- **Raw collected data** — the original fetched source material remains authoritative.
- **Official Sources** — readable copies preserved by issuing source, without processing-level mixing.
- **0 Level Processing** — statewide readable reports.
- **1 County Processing** — deterministic county/geographic reports.
- **Archives** — prior report versions retained when substantive source content changes.

The live report below is regenerated automatically from the current statewide report data. It is not manually maintained.

## 📚 Report Layers

- **Official Sources** — source-preserved products grouped by issuing authority.
- **0 Level Processing** — statewide Hawaiʻi reports.
- **1 County Processing** — deterministically routed county reports.
- **Archives** — previous report versions retained when source content changes.

[**Open the current statewide report →**](https://github.com/rootrecordsoftwaresolutions/RootRecord-Weather-Database/blob/main/Hawai%27i/reports/0%20Level%20Processing/Hawaii_State_Weather_Report_current.md)

## 🛡️ Source Integrity

Raw collected source data remains the authoritative record. Generated reports are separate processing/presentation layers, and products without authoritative geographic assignment are not silently assigned to counties.

---

## 🌦️ Current Conditions

| Location | Conditions | Temp | Dew point | RH | Wind | Pressure |
|---|---|---:|---:|---:|---|---:|
| Honolulu | Partly cloudy | 80°F | 69°F | 69% | Northeast 18 gusts to 31 | 29.92F |
| Lihue | Partly cloudy | 79°F | 72°F | 79% | Northeast 17 | 29.97F |
| Kahului | Clear | 80°F | 64°F | 58% | Northeast 24 gusts to 39 | 29.87F |
| Hilo | Clear | 71°F | 56°F | 58% | Southwest 8 | 29.99S |
| Kona | Cloudy | 83°F | 74°F | 74% | West 15 | — |

_Source: locally collected NWS-HFO Regional Weather Roundup (RWR). Values are °F._

---

## 🌦️ Live Hawaiʻi Statewide Weather Report

> **Automatically regenerated from the latest locally collected official weather products.**

| Status | Coverage | Updated | Sections |
|---|---|---|---:|
| 🟢 Active | Hawaiʻi statewide | 2026-09-28T05:25:19-10:00 HST | 29 |

The report below is generated from the same current product sections as `Hawaii_State_Weather_Report_current.md`.

---

### 1. 7-Day Zone Forecasts (all islands)

| Field | Value |
|---|---|
| **Resource ID** | zfp_zone_forecast |
| **Official source** | https://api.weather.gov/products/types/ZFP/locations/HFO |
| **Collected** | 2026-09-28T04:53:20.741084-10:00 HST |

```text
000
FPHW50 PHFO 281446
ZFPHFO

Zone Forecast Product for Hawaii
National Weather Service Honolulu HI
446 AM HST Mon Sep 28 2026

HIZ001-290715-
Niihau-
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny and windy. Highs 81 to 87. East winds 15 to
30 mph. 
.TONIGHT...Windy. Mostly cloudy with scattered showers. Lows
72 to 79. East winds 20 to 30 mph. Chance of rain 50 percent. 
.TUESDAY...Windy. Numerous showers in the morning, then
occasional showers in the afternoon. Highs 80 to 85. Southeast
winds 25 to 35 mph with gusts to 55 mph. Chance of rain near
100 percent. 
.TUESDAY NIGHT...Windy. Mostly cloudy with occasional showers.
Lows 71 to 78. Southeast winds 20 to 35 mph with gusts to 55 mph.
Chance of rain 90 percent. 
.WEDNESDAY...Windy. Mostly cloudy with numerous showers. Highs
80 to 85. Southeast winds 20 to 35 mph with gusts to 55 mph.
Chance of rain 70 percent. 
.WEDNESDAY NIGHT...Windy. Mostly cloudy with numerous showers.
Lows 72 to 78. Southeast winds 15 to 35 mph with gusts to 55 mph.
Chance of rain 70 percent. 
.THURSDAY...Partly sunny. Windy. Numerous showers in the morning,
then scattered showers in the afternoon. Highs 80 to 85.
Southeast winds 15 to 35 mph. Gusts up to 55 mph in the morning.
Chance of rain 60 percent. 
.THURSDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Breezy. Scattered showers. Lows 71 to 78.
Southeast winds 15 to 25 mph. Chance of rain 40 percent. 
.FRIDAY...Breezy. Mostly sunny with isolated showers. Highs 79 to
85. Southeast winds 10 to 25 mph. Chance of rain 20 percent. 
.FRIDAY NIGHT...Partly cloudy. Isolated showers in the evening,
then scattered showers after midnight. Lows 71 to 77. East winds
10 to 15 mph. Chance of rain 30 percent. 
.SATURDAY...Mostly sunny. Breezy. Isolated showers in the
morning. Highs 79 to 85. East winds 10 to 25 mph. Chance of rain
20 percent. 
.SATURDAY NIGHT...Partly cloudy. Breezy. Isolated showers in the
evening, then scattered showers after midnight. Lows 71 to 77.
Northeast winds 10 to 20 mph. Chance of rain 30 percent. 
.SUNDAY...Mostly sunny. Breezy. Isolated showers in the morning.
Highs 79 to 85. Northeast winds 10 to 15 mph increasing to 10 to
25 mph in the afternoon. Chance of rain 20 percent. 

HIZ029-290715-
Kauai North-
Including Princeville, Hanalei, Na Pali State Park
446 AM HST Mon Sep 28 2026

.TODAY...Breezy. Mostly sunny with scattered showers. Highs 72 to
89. East winds up to 20 mph. Chance of rain 50 percent. 
.TONIGHT...Breezy. Mostly cloudy with isolated showers. Lows
67 to 77. East winds up to 15 mph increasing to 10 to 20 mph
after midnight. Chance of rain 20 percent. 
.TUESDAY...Partly sunny with scattered showers. Highs 72 to 88.
Southeast winds 10 to 15 mph. Chance of rain 50 percent. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows 67 to
76. Southeast winds 10 to 15 mph. Chance of rain 50 percent. 
.WEDNESDAY...Mostly cloudy with scattered showers. Highs 72 to
87. Southeast winds 10 to 15 mph. Chance of rain 50 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with isolated showers. Lows
67 to 76. Southeast winds up to 10 mph. Chance of rain
20 percent. 
.THURSDAY...Partly sunny with isolated showers. Highs 72 to 87.
East winds around 10 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Mostly cloudy with isolated showers. Lows 66 to
76. East winds up to 10 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny. Isolated showers in the morning, then
scattered showers in the afternoon. Highs 72 to 87. East winds
around 10 mph. Chance of rain 50 percent. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 66 to
75. Light winds. Chance of rain 50 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 72 to 87.
East winds around 10 mph shifting to the northeast in the
afternoon. Chance of rain 50 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
65 to 75. Northeast winds up to 10 mph. Chance of rain
50 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 71 to 87.
Northeast winds up to 10 mph increasing to 10 to 15 mph in the
afternoon. Chance of rain 50 percent. 

HIZ030-290715-
Kauai East-
Including Lihue, Kapaa, Anahola
446 AM HST Mon Sep 28 2026

.TODAY...Mostly sunny with scattered showers. Highs 78 to 86.
East winds 10 to 15 mph. Chance of rain 50 percent. 
.TONIGHT...Mostly cloudy with isolated showers. Lows 68 to 78.
East winds 10 to 15 mph. Chance of rain 20 percent. 
.TUESDAY...Mostly cloudy. Numerous showers in the morning, then
occasional showers in the afternoon. Highs 77 to 86. Southeast
winds 10 to 15 mph. Chance of rain 90 percent. 
.TUESDAY NIGHT...Mostly cloudy with occasional showers. Lows
68 to 77. Southeast winds 10 to 15 mph. Chance of rain
90 percent. 
.WEDNESDAY...Mostly cloudy with numerous showers. Highs 77 to 86.
Southeast winds 10 to 15 mph. Chance of rain 70 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with numerous showers. Lows
68 to 77. Southeast winds up to 10 mph. Chance of rain
70 percent. 
.THURSDAY...Mostly cloudy with scattered showers. Highs 78 to 86.
East winds around 10 mph. Chance of rain 50 percent. 
.THURSDAY NIGHT...Mostly cloudy with scattered showers. Lows
67 to 77. East winds around 10 mph in the evening becoming light.
Chance of rain 30 percent. 
.FRIDAY...Partly sunny. Isolated showers in the morning, then
scattered showers in the afternoon. Highs 78 to 86. East winds
around 10 mph. Chance of rain 50 percent. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 67 to
77. Light winds. Chance of rain 50 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 78 to 86.
East winds around 10 mph. Chance of rain 50 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
66 to 76. Northeast winds up to 10 mph. Chance of rain
50 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 78 to 86.
Light winds becoming northeast around 10 mph in the afternoon.
Chance of rain 50 percent. 

HIZ031-290715-
Kauai South-
Including Poipu, Kalaheo, Koloa
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Breezy. Mostly sunny with scattered showers. Highs 81 to
90. East winds 15 to 20 mph. Chance of rain 40 percent. 
.TONIGHT...Breezy. Mostly cloudy with isolated showers. Lows
72 to 78. East winds 10 to 20 mph. Chance of rain 20 percent. 
.TUESDAY...Mostly cloudy. Numerous showers in the morning, then
occasional showers in the afternoon. Highs 80 to 89. Southeast
winds 10 to 15 mph. Chance of rain 90 percent. 
.TUESDAY NIGHT...Cloudy with occasional showers. Lows 72 to 77.
Southeast winds 10 to 15 mph. Chance of rain 90 percent. 
.WEDNESDAY...Mostly cloudy. Occasional showers in the morning,
then numerous showers in the afternoon. Highs 80 to 88. Southeast
winds 10 to 15 mph. Chance of rain 80 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with numerous showers. Lows
72 to 78. East winds 10 to 15 mph. Chance of rain 70 percent. 
.THURSDAY...Mostly cloudy. Numerous showers in the morning, then
scattered showers in the afternoon. Highs 80 to 89. East winds
10 to 15 mph. Chance of rain 60 percent. 
.THURSDAY NIGHT...Mostly cloudy with scattered showers. Lows
71 to 77. East winds around 10 mph. Chance of rain 30 percent. 
.FRIDAY...Partly sunny with isolated showers. Highs 79 to 89.
East winds 10 to 15 mph. Chance of rain 20 percent. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 70 to
77. East winds around 10 mph. Chance of rain 50 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 79 to 89.
East winds 10 to 15 mph. Chance of rain 50 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
70 to 77. Northeast winds 10 to 15 mph. Chance of rain
50 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 79 to 89.
Northeast winds 10 to 15 mph. Chance of rain 50 percent. 

HIZ003-290715-
Kauai Southwest-
Including Waimea, Waimea Canyon State Park, Hanapepe, Kekaha, 
Barking Sands
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny and breezy. Isolated showers in the morning, then
scattered showers in the afternoon. Highs 87 to 92 near the shore
to around 79 above 3000 feet. East winds up to 25 mph increasing
to 10 to 25 mph in the afternoon. Chance of rain 50 percent. 
.TONIGHT...Windy. Mostly cloudy with isolated showers. Lows
around 76 near the shore to around 67 above 3000 feet. East winds
10 to 30 mph. Chance of rain 20 percent. 
.TUESDAY...Partly sunny. Breezy. Numerous showers in the morning,
then occasional showers in the afternoon. Highs around 87 near
the shore to around 77 above 3000 feet. Southeast winds 10 to
25 mph. Chance of rain 90 percent. 
.TUESDAY NIGHT...Breezy. Mostly cloudy with occasional showers.
Lows 65 to 77. Southeast winds 15 to 20 mph. Chance of rain
90 percent. 
.WEDNESDAY...Breezy. Partly sunny with numerous showers. Highs
76 to 88. Southeast winds 10 to 25 mph. Chance of rain
70 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with scattered showers. Lows
65 to 77. Southeast winds 10 to 15 mph. Chance of rain
50 percent. 
.THURSDAY...Partly sunny with scattered showers. Highs 77 to 89.
Southeast winds 10 to 15 mph. Chance of rain 50 percent. 
.THURSDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Isolated showers. Lows 64 to 77. East winds around
10 mph in the evening becoming light. Chance of rain 20 percent. 
.FRIDAY...Partly sunny with isolated showers. Highs 76 to 89.
Southeast winds up to 10 mph. Chance of rain 20 percent. 
.FRIDAY NIGHT...Mostly cloudy with isolated showers. Lows 64 to
76. Light winds. Chance of rain 20 percent. 
.SATURDAY...Mostly sunny with isolated showers. Highs 76 to 89.
Light winds becoming east around 10 mph in the afternoon. Chance
of rain 20 percent. 
.SATURDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Isolated showers. Lows 63 to 76. Light winds.
Chance of rain 20 percent. 
.SUNDAY...Mostly sunny with isolated showers. Highs 76 to 90.
Light winds becoming northeast around 10 mph in the afternoon.
Chance of rain 20 percent. 

HIZ004-290715-
Kauai Mountains-
Including Kokee State Park
446 AM HST Mon Sep 28 2026

.TODAY...Mostly sunny. Breezy. Scattered showers in the morning,
then numerous showers in the afternoon. Highs 71 to 83. East
winds 10 to 20 mph. Chance of rain 60 percent. 
.TONIGHT...Windy. Mostly cloudy with isolated showers. Lows
around 71 in the valleys to around 63 above 4000 feet. East winds
10 to 30 mph. Chance of rain 20 percent. 
.TUESDAY...Breezy. Mostly cloudy with occasional showers. Highs
75 to 82 in the valleys to around 74 above 4000 feet. Southeast
winds 10 to 25 mph. Chance of rain 90 percent. 
.TUESDAY NIGHT...Breezy. Mostly cloudy with occasional showers.
Lows 62 to 73. Southeast winds 10 to 25 mph with gusts to 45 mph.
Chance of rain 90 percent. 
.WEDNESDAY...Breezy. Mostly cloudy with scattered showers. Highs
70 to 83. Southeast winds 10 to 20 mph. Gusts up to 40 mph in the
morning. Chance of rain 50 percent. 
.WEDNESDAY NIGHT...Breezy. Mostly cloudy with scattered showers.
Lows 62 to 73. Southeast winds 10 to 20 mph. Chance of rain
50 percent. 
.THURSDAY...Mostly cloudy with scattered showers. Highs 71 to 83.
East winds 10 to 15 mph. Chance of rain 50 percent. 
.THURSDAY NIGHT...Mostly cloudy with isolated showers. Lows 61 to
72. East winds 10 to 15 mph. Chance of rain 20 percent. 
.FRIDAY...Mostly cloudy. Isolated showers in the morning, then
scattered showers in the afternoon. Highs 70 to 83. East winds
around 10 mph. Chance of rain 50 percent. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 61 to
72. East winds up to 10 mph. Chance of rain 50 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 70 to 83.
East winds 10 to 15 mph. Chance of rain 50 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
60 to 71. Northeast winds up to 10 mph. Chance of rain
50 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 70 to 82.
Northeast winds up to 10 mph increasing to 10 to 15 mph in the
afternoon. Chance of rain 50 percent. 

HIZ032-290715-
East Honolulu-
Including Hawaii Kai, Aina Haina, Kahala
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny and breezy. Isolated showers in the morning. Highs
82 to 89. East winds 15 to 25 mph. Chance of rain 20 percent. 
.TONIGHT...Partly cloudy. Breezy. Lows around 78. East winds
10 to 20 mph. 
.TUESDAY...Mostly sunny in the morning then becoming partly
sunny. Highs 83 to 89. East winds around 10 mph. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows
around 78. Southeast winds around 10 mph. Chance of rain
50 percent. 
.WEDNESDAY...Mostly cloudy. Scattered showers in the morning.
Highs 82 to 88. Southeast winds around 10 mph. Chance of rain
50 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with scattered showers. Lows
around 77. East winds around 10 mph. Chance of rain 40 percent. 
.THURSDAY...Partly sunny. Scattered showers in the morning. Highs
81 to 88. East winds around 10 mph. Chance of rain 40 percent. 
.THURSDAY NIGHT...Mostly cloudy with isolated showers. Lows
around 77. East winds around 10 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny. Highs 81 to 88. East winds around 10 mph
in the morning becoming light. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows around
77. Light winds. Chance of rain 40 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 81 to 87.
Light winds. Chance of rain 40 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
around 77. Light winds. Chance of rain 40 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 81 to 87.
Light winds becoming northeast around 10 mph in the afternoon.
Chance of rain 40 percent. 

HIZ033-290715-
Honolulu Metro-
Including Honolulu, Waikiki
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny and breezy. Isolated showers in the morning. Highs
85 to 90. East winds 10 to 20 mph. Chance of rain 20 percent. 
.TONIGHT...Partly cloudy in the evening then becoming mostly
cloudy. Lows around 77. East winds 10 to 15 mph. 
.TUESDAY...Mostly sunny. Highs 85 to 90. Southeast winds around
10 mph. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows
around 77. Light winds. Chance of rain 50 percent. 
.WEDNESDAY...Partly sunny with scattered showers. Highs 84 to 89.
Southeast winds around 10 mph. Chance of rain 50 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with scattered showers. Lows
around 77. Light winds. Chance of rain 40 percent. 
.THURSDAY...Partly sunny with scattered showers in the morning,
then mostly sunny in the afternoon. Highs around 86. East winds
around 10 mph. Chance of rain 40 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows
around 76. Light winds. Chance of rain 20 percent. 
.FRIDAY...Partly sunny in the morning then becoming mostly sunny.
Highs around 86. East winds around 10 mph. 
.FRIDAY NIGHT...Partly cloudy with isolated showers. Lows around
76. Light winds. Chance of rain 20 percent. 
.SATURDAY...Mostly sunny with isolated showers. Highs around 86.
East winds around 10 mph. Chance of rain 20 percent. 
.SATURDAY NIGHT...Partly cloudy with isolated showers. Lows
around 76. Light winds. Chance of rain 20 percent. 
.SUNDAY...Mostly sunny with isolated showers. Highs 83 to 88.
Light winds becoming east around 10 mph in the afternoon. Chance
of rain 20 percent. 

HIZ034-290715-
Ewa Plain-
Including Kapolei
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny and breezy. Highs 85 to 91. East winds up to
20 mph increasing to 15 to 20 mph in the afternoon. 
.TONIGHT...Partly cloudy. Lows around 76. East winds 10 to
15 mph. 
.TUESDAY...Mostly sunny. Highs 85 to 90. Southeast winds 10 to
15 mph. 
.TUESDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Scattered showers. Lows around 77. Southeast winds
around 10 mph. Chance of rain 50 percent. 
.WEDNESDAY...Partly sunny with scattered showers. Highs 84 to 89.
Southeast winds 10 to 15 mph. Chance of rain 50 percent. 
.WEDNESDAY NIGHT...Partly cloudy with scattered showers. Lows
around 76. East winds around 10 mph. Chance of rain 50 percent. 
.THURSDAY...Partly sunny with scattered showers in the morning,
then mostly sunny with isolated showers in the afternoon. Highs
84 to 89. East winds 10 to 15 mph. Chance of rain 40 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows
around 75. Light winds. Chance of rain 20 percent. 
.FRIDAY...Partly sunny. Scattered showers in the afternoon. Highs
84 to 89. East winds around 10 mph. Chance of rain 30 percent. 
.FRIDAY NIGHT...Partly cloudy. Lows around 75. Light winds. 
.SATURDAY...Mostly sunny. Highs 84 to 89. East winds around
10 mph. 
.SATURDAY NIGHT...Mostly clear. Lows around 74. Light winds. 
.SUNDAY...Mostly sunny. Highs 83 to 89. Light winds becoming east
around 10 mph in the afternoon. 

HIZ006-290715-
Waianae Coast-
Including Nanakuli, Waianae, Makaha
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny and breezy. Highs 87 to 94. East winds 15 to
25 mph. 
.TONIGHT...Partly cloudy. Breezy. Lows 71 to 79. East winds 10 to
20 mph. 
.TUESDAY...Mostly sunny. Highs 86 to 93. Southeast winds around
10 mph. 
.TUESDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Scattered showers. Lows 72 to 79. Southeast winds
around 10 mph. Chance of rain 50 percent. 
.WEDNESDAY...Partly sunny with scattered showers. Highs 84 to 91.
Southeast winds around 10 mph. Chance of rain 50 percent. 
.WEDNESDAY NIGHT...Partly cloudy with scattered showers. Lows
71 to 78. East winds around 10 mph in the evening becoming light.
Chance of rain 50 percent. 
.THURSDAY...Mostly sunny with scattered showers. Highs 85 to 91.
Southeast winds around 10 mph. Chance of rain 40 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows 71 to
78. Light winds. Chance of rain 20 percent. 
.FRIDAY...Partly sunny. Highs 84 to 91. Southeast winds around
10 mph. 
.FRIDAY NIGHT...Partly cloudy with isolated showers. Lows 70 to
78. Light winds. Chance of rain 20 percent. 
.SATURDAY...Mostly sunny with isolated showers. Highs 84 to 91.
Northeast winds around 10 mph. Chance of rain 20 percent. 
.SATURDAY NIGHT...Partly cloudy with isolated showers. Lows 70 to
77. Light winds. Chance of rain 20 percent. 
.SUNDAY...Mostly sunny with isolated showers. Highs 84 to 91.
Light winds becoming northeast around 10 mph in the afternoon.
Chance of rain 20 percent. 

HIZ007-290715-
Oahu North Shore-
Including Waialua, Haleiwa, Pupukea
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and breezy. Isolated showers in the morning. Highs
81 to 89. East winds 10 to 25 mph. Chance of rain 20 percent. 
.TONIGHT...Partly cloudy. Breezy. Lows 71 to 77. East winds 10 to
25 mph. 
.TUESDAY...Mostly sunny in the morning then becoming partly
sunny. Highs 82 to 89. Southeast winds around 10 mph. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows 71 to
77. Southeast winds up to 10 mph. Chance of rain 50 percent. 
.WEDNESDAY...Partly sunny with scattered showers. Highs 81 to 88.
Southeast winds around 10 mph. Chance of rain 50 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with scattered showers. Lows
71 to 77. East winds up to 10 mph. Chance of rain 40 percent. 
.THURSDAY...Partly sunny. Scattered showers in the morning, then
isolated showers in the afternoon. Highs 81 to 88. East winds
around 10 mph. Chance of rain 40 percent. 
.THURSDAY NIGHT...Partly cloudy. Lows 70 to 77. East winds up to
10 mph. 
.FRIDAY...Partly sunny. Scattered showers in the afternoon. Highs
81 to 88. East winds around 10 mph. Chance of rain 30 percent. 
.FRIDAY NIGHT...Partly cloudy with scattered showers. Lows 70 to
77. Light winds. Chance of rain 40 percent. 
.SATURDAY...Mostly sunny with scattered showers. Highs 81 to 87.
Northeast winds 10 to 15 mph. Chance of rain 40 percent. 
.SATURDAY NIGHT...Partly cloudy with scattered showers. Lows
70 to 76. Northeast winds up to 10 mph. Chance of rain
50 percent. 
.SUNDAY...Mostly sunny with scattered showers. Highs 80 to 87.
Northeast winds up to 10 mph increasing to 10 to 15 mph in the
afternoon. Chance of rain 40 percent. 

HIZ035-290715-
Koolau Windward-
Including Kahuku, Laie, Punaluu, Kahaluu, Ahuimanu
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and breezy. Scattered showers in the morning.
Highs 77 to 87. East winds 10 to 25 mph. Chance of rain
40 percent. 
.TONIGHT...Mostly cloudy. Breezy. Lows 69 to 79. East winds 10 to
25 mph. 
.TUESDAY...Mostly cloudy. Highs 77 to 88. East winds 10 to
15 mph. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows 69 to
79. Southeast winds 10 to 15 mph. Chance of rain 40 percent. 
.WEDNESDAY...Mostly cloudy with scattered showers. Highs 76 to
86. Southeast winds 10 to 15 mph. Chance of rain 50 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with scattered showers. Lows
69 to 79. East winds 10 to 15 mph. Chance of rain 40 percent. 
.THURSDAY...Mostly cloudy. Scattered showers in the morning, then
isolated showers in the afternoon. Highs 76 to 86. East winds
10 to 15 mph. Chance of rain 40 percent. 
.THURSDAY NIGHT...Mostly cloudy with isolated showers. Lows 69 to
78. East winds around 10 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny. Isolated showers in the morning, then
scattered showers in the afternoon. Highs 76 to 86. East winds
around 10 mph. Chance of rain 40 percent. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 68 to
78. East winds up to 10 mph in the evening becoming light. Chance
of rain 50 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 76 to 86.
East winds up to 10 mph. Chance of rain 50 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
68 to 77. Light winds. Chance of rain 50 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 75 to 85.
Light winds becoming northeast up to 10 mph in the afternoon.
Chance of rain 50 percent. 

HIZ036-290715-
Koolau Leeward-
Including Nuuanu, Manoa, Palolo
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and windy. Scattered showers in the morning. Highs
77 to 87. East winds 15 to 30 mph. Chance of rain 40 percent. 
.TONIGHT...Mostly cloudy. Breezy. Lows 68 to 77. East winds 10 to
25 mph. 
.TUESDAY...Partly sunny. Highs 77 to 88. Southeast winds 10 to
15 mph. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows 68 to
77. Southeast winds 10 to 15 mph. Chance of rain 50 percent. 
.WEDNESDAY...Mostly cloudy with scattered showers. Highs 76 to
86. Southeast winds around 10 mph. Chance of rain 50 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with scattered showers. Lows
67 to 77. East winds around 10 mph. Chance of rain 40 percent. 
.THURSDAY...Mostly cloudy with scattered showers. Highs 76 to 86.
East winds 10 to 15 mph. Chance of rain 40 percent. 
.THURSDAY NIGHT...Mostly cloudy with isolated showers. Lows 67 to
76. East winds around 10 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny. Isolated showers in the morning, then
scattered showers in the afternoon. Highs 76 to 86. East winds
around 10 mph. Chance of rain 40 percent. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 67 to
76. East winds up to 10 mph. Chance of rain 50 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 75 to 86.
East winds 10 to 15 mph. Chance of rain 50 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
66 to 75. Northeast winds up to 10 mph. Chance of rain
50 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 75 to 86.
Light winds becoming northeast around 10 mph in the afternoon.
Chance of rain 50 percent. 

HIZ009-290715-
Olomana-
Including Kailua, Kaneohe, Waimanalo
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and breezy. Isolated showers in the morning. Highs
80 to 86. East winds up to 20 mph increasing to 10 to 20 mph in
the afternoon. Chance of rain 20 percent. 
.TONIGHT...Mostly cloudy. Breezy. Lows 73 to 79. East winds 10 to
20 mph. 
.TUESDAY...Partly sunny. Highs 80 to 87. East winds around
10 mph. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows 72 to
78. Southeast winds around 10 mph in the evening becoming light.
Chance of rain 50 percent. 
.WEDNESDAY...Mostly cloudy. Scattered showers in the morning.
Highs 80 to 85. Southeast winds around 10 mph. Chance of rain
50 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with scattered showers. Lows
72 to 78. East winds around 10 mph. Chance of rain 40 percent. 
.THURSDAY...Partly sunny. Scattered showers in the morning. Highs
79 to 85. East winds around 10 mph in the morning becoming light.
Chance of rain 40 percent. 
.THURSDAY NIGHT...Mostly cloudy with isolated showers. Lows 72 to
78. Light winds. Chance of rain 20 percent. 
.FRIDAY...Partly sunny with isolated showers. Highs 79 to 85.
East winds around 10 mph in the morning becoming light. Chance of
rain 20 percent. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 72 to
78. Light winds. Chance of rain 40 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 79 to 85.
Light winds. Chance of rain 40 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
71 to 77. Light winds. Chance of rain 40 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 79 to 84.
Light winds. Chance of rain 40 percent. 

HIZ010-290715-
Central Oahu-
Including Mililani, Wahiawa, Pearl City
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and breezy. Isolated showers in the morning. Highs
81 to 88. East winds 10 to 25 mph. Chance of rain 20 percent. 
.TONIGHT...Partly cloudy. Breezy. Lows 70 to 76. East winds 10 to
25 mph. 
.TUESDAY...Mostly sunny in the morning then becoming partly
sunny. Highs 81 to 89. Southeast winds around 10 mph. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows
around 73. Light winds. Chance of rain 50 percent. 
.WEDNESDAY...Partly sunny with scattered showers. Highs 80 to 86.
Southeast winds around 10 mph. Chance of rain 50 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with scattered showers. Lows
70 to 75. Light winds. Chance of rain 40 percent. 
.THURSDAY...Partly sunny with scattered showers. Highs 80 to 86.
East winds around 10 mph. Chance of rain 40 percent. 
.THURSDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Isolated showers. Lows 69 to 74. Light winds.
Chance of rain 20 percent. 
.FRIDAY...Partly sunny. Scattered showers in the afternoon. Highs
80 to 87. East winds around 10 mph. Chance of rain 30 percent. 
.FRIDAY NIGHT...Partly cloudy. Scattered showers in the evening,
then isolated showers after midnight. Lows 69 to 74. Light winds.
Chance of rain 40 percent. 
.SATURDAY...Mostly sunny with isolated showers. Highs 80 to 86.
East winds around 10 mph. Chance of rain 20 percent. 
.SATURDAY NIGHT...Partly cloudy with isolated showers. Lows
around 71. Light winds. Chance of rain 20 percent. 
.SUNDAY...Mostly sunny with isolated showers. Highs 79 to 86.
Light winds becoming northeast around 10 mph in the afternoon.
Chance of rain 20 percent. 

HIZ011-290715-
Waianae Mountains-
Including Makakilo
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and breezy. Highs 80 to 94. East winds 15 to
25 mph. 
.TONIGHT...Partly cloudy. Breezy. Lows 66 to 76. East winds 10 to
20 mph. 
.TUESDAY...Mostly sunny. Highs 78 to 93. Southeast winds around
10 mph. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows 67 to
76. Southeast winds around 10 mph. Chance of rain 50 percent. 
.WEDNESDAY...Partly sunny with scattered showers. Highs 76 to 91.
Southeast winds 10 to 15 mph. Chance of rain 50 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with scattered showers. Lows
66 to 76. East winds around 10 mph. Chance of rain 40 percent. 
.THURSDAY...Partly sunny with scattered showers. Highs 76 to 91.
East winds around 10 mph. Chance of rain 40 percent. 
.THURSDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Lows 65 to 75. East winds around 10 mph. 
.FRIDAY...Partly sunny. Scattered showers in the afternoon. Highs
76 to 91. East winds around 10 mph. Chance of rain 30 percent. 
.FRIDAY NIGHT...Partly cloudy with scattered showers. Lows 65 to
75. East winds around 10 mph in the evening becoming light.
Chance of rain 40 percent. 
.SATURDAY...Mostly sunny with scattered showers. Highs 76 to 91.
Northeast winds around 10 mph. Chance of rain 30 percent. 
.SATURDAY NIGHT...Partly cloudy with scattered showers. Lows
65 to 74. Northeast winds up to 10 mph in the evening becoming
light. Chance of rain 40 percent. 
.SUNDAY...Mostly sunny with scattered showers. Highs 76 to 91.
Light winds becoming northeast 10 to 15 mph in the afternoon.
Chance of rain 30 percent. 

HIZ037-290715-
Molokai Windward-
Including Kalaupapa, Halawa Valley
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and breezy. Isolated showers in the morning. Highs
73 to 85. East winds 10 to 25 mph. Chance of rain 20 percent. 
.TONIGHT...Mostly cloudy. Breezy. Lows 62 to 77. East winds 10 to
25 mph. 
.TUESDAY...Partly sunny. Isolated showers in the afternoon. Highs
73 to 86. East winds 10 to 15 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy with isolated showers. Lows 62 to
77. East winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY...Partly sunny. Isolated showers in the morning. Highs
73 to 85. East winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with isolated showers. Lows
62 to 77. East winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY...Partly sunny. Breezy. Highs 72 to 84. East winds
10 to 20 mph. 
.THURSDAY NIGHT...Mostly cloudy. Lows 61 to 77. East winds 10 to
15 mph. 
.FRIDAY...Partly sunny. Highs 72 to 84. East winds 10 to 15 mph. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 61 to
76. East winds 10 to 15 mph. Chance of rain 50 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 72 to 83.
East winds 10 to 15 mph. Chance of rain 40 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
60 to 76. East winds 10 to 15 mph. Chance of rain 50 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 72 to 83.
Northeast winds 10 to 15 mph. Chance of rain 40 percent. 

HIZ038-290715-
Molokai Southeast-
Including Pukoo
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and windy. Isolated showers in the morning. Highs
80 to 86. East winds 15 to 30 mph. Chance of rain 20 percent. 
.TONIGHT...Mostly cloudy. Breezy. Lows 62 to 78. East winds 10 to
25 mph. 
.TUESDAY...Partly sunny. Isolated showers in the afternoon. Highs
80 to 86. East winds 10 to 15 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy. Lows 62 to 78. East winds 10 to
15 mph. 
.WEDNESDAY...Partly sunny. Isolated showers in the morning. Highs
79 to 85. East winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Lows 62 to 77. East winds 10 to
15 mph. 
.THURSDAY...Partly sunny. Breezy. Highs 79 to 84. East winds
15 to 20 mph. 
.THURSDAY NIGHT...Mostly cloudy. Lows 61 to 77. East winds 10 to
15 mph. 
.FRIDAY...Partly sunny. Highs 79 to 84. East winds 10 to 15 mph. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 61 to
77. East winds 10 to 15 mph. Chance of rain 40 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 79 to 84.
East winds 10 to 15 mph. Chance of rain 40 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
61 to 77. East winds 10 to 15 mph. Chance of rain 40 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 78 to 84.
Northeast winds 10 to 15 mph. Chance of rain 40 percent. 

HIZ039-290715-
Molokai North-
Including Hoolehua
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and windy. Highs 77 to 88. East winds 10 to
30 mph. 
.TONIGHT...Partly cloudy. Breezy. Lows 67 to 78. East winds 10 to
25 mph decreasing to 10 to 15 mph after midnight. 
.TUESDAY...Mostly sunny. Highs 78 to 88. East winds 10 to 15 mph.
.TUESDAY NIGHT...Partly cloudy with isolated showers. Lows 68 to
79. East winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY...Partly sunny. Scattered showers in the morning.
Highs 77 to 87. East winds 10 to 15 mph. Chance of rain
40 percent. 
.WEDNESDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Isolated showers. Lows 67 to 78. East winds 10 to
15 mph. Chance of rain 20 percent. 
.THURSDAY...Breezy. Mostly sunny with isolated showers in the
morning, then partly sunny in the afternoon. Highs 77 to 86. East
winds 15 to 20 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Lows 67 to 77. East winds 10 to 15 mph. 
.FRIDAY...Partly sunny in the morning then becoming mostly sunny.
Breezy. Highs 77 to 85. East winds 10 to 20 mph. 
.FRIDAY NIGHT...Partly cloudy with scattered showers. Lows 66 to
77. East winds 10 to 15 mph. Chance of rain 40 percent. 
.SATURDAY...Breezy. Mostly sunny with scattered showers. Highs
76 to 85. Northeast winds 10 to 20 mph. Chance of rain
40 percent. 
.SATURDAY NIGHT...Breezy. Partly cloudy with scattered showers.
Lows 66 to 77. East winds 10 to 20 mph. Chance of rain
40 percent. 
.SUNDAY...Breezy. Mostly sunny with scattered showers. Highs
76 to 84. Northeast winds 10 to 20 mph. Chance of rain
40 percent. 

HIZ040-290715-
Molokai West-
Including Kepuhi
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and breezy. Highs 83 to 89. East winds 10 to
25 mph with gusts to 45 mph. 
.TONIGHT...Partly cloudy. Breezy. Lows around 76. East winds
10 to 25 mph decreasing to 10 to 15 mph after midnight. 
.TUESDAY...Mostly sunny. Highs 83 to 89. East winds around
10 mph. 
.TUESDAY NIGHT...Partly cloudy with scattered showers. Lows
around 77. Southeast winds around 10 mph. Chance of rain
40 percent. 
.WEDNESDAY...Mostly sunny with scattered showers in the morning,
then partly sunny in the afternoon. Highs 82 to 88. Southeast
winds 10 to 15 mph. Chance of rain 40 percent. 
.WEDNESDAY NIGHT...Partly cloudy with scattered showers. Lows
around 76. East winds 10 to 15 mph. Chance of rain 30 percent. 
.THURSDAY...Mostly sunny. Isolated showers in the morning. Highs
81 to 88. East winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Lows around 76. East winds 10 to 15 mph. 
.FRIDAY...Mostly sunny. Highs 81 to 87. East winds 10 to 15 mph. 
.FRIDAY NIGHT...Partly cloudy. Isolated showers in the evening,
then scattered showers after midnight. Lows around 76. East winds
10 to 15 mph. Chance of rain 30 percent. 
.SATURDAY...Breezy. Mostly sunny with isolated showers. Highs
81 to 87. Northeast winds 10 to 20 mph. Chance of rain
20 percent. 
.SATURDAY NIGHT...Partly cloudy. Isolated showers in the evening,
then scattered showers after midnight. Lows around 76. Northeast
winds 10 to 15 mph. Chance of rain 30 percent. 
.SUNDAY...Mostly sunny with isolated showers. Highs 80 to 86.
Northeast winds 10 to 15 mph. Chance of rain 20 percent. 

HIZ041-290715-
Molokai Leeward South-
Including Kaunakakai, Maunaloa
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny and breezy. Highs 78 to 91. East winds up to
25 mph increasing to 10 to 25 mph in the afternoon. 
.TONIGHT...Partly cloudy. Lows 63 to 78. East winds 10 to 15 mph.
.TUESDAY...Mostly sunny. Highs 78 to 92. East winds around
10 mph. 
.TUESDAY NIGHT...Partly cloudy with isolated showers. Lows 64 to
78. East winds up to 10 mph in the evening becoming light. Chance
of rain 20 percent. 
.WEDNESDAY...Mostly sunny with scattered showers in the morning,
then partly sunny in the afternoon. Highs 78 to 91. East winds up
to 10 mph. Chance of rain 30 percent. 
.WEDNESDAY NIGHT...Partly cloudy with isolated showers. Lows
64 to 78. East winds around 10 mph. Chance of rain 20 percent. 
.THURSDAY...Mostly sunny. Isolated showers in the morning. Highs
77 to 90. East winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Lows 63 to 77. East winds around 10 mph. 
.FRIDAY...Mostly sunny. Highs 77 to 90. East winds 10 to 15 mph. 
.FRIDAY NIGHT...Partly cloudy. Scattered showers in the evening,
then isolated showers after midnight. Lows 63 to 77. East winds
up to 10 mph. Chance of rain 40 percent. 
.SATURDAY...Mostly sunny with isolated showers. Highs 76 to 90.
Northeast winds 10 to 15 mph. Chance of rain 20 percent. 
.SATURDAY NIGHT...Partly cloudy with isolated showers. Lows 63 to
77. Northeast winds up to 10 mph. Chance of rain 20 percent. 
.SUNDAY...Mostly sunny with isolated showers. Highs 76 to 89.
Northeast winds up to 10 mph increasing to 10 to 15 mph in the
afternoon. Chance of rain 20 percent. 

HIZ042-290715-
Lanai Windward-
Including Shipwreck Beach
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and breezy. Highs 79 to 87. Northeast winds up to
25 mph. 
.TONIGHT...Mostly clear. Breezy. Lows 67 to 77. Northeast winds
up to 25 mph decreasing to up to 15 mph after midnight. 
.TUESDAY...Mostly sunny. Highs 79 to 87. East winds 10 to 15 mph.
.TUESDAY NIGHT...Partly cloudy. Lows 67 to 78. East winds 10 to
15 mph. 
.WEDNESDAY...Mostly sunny. Isolated showers in the morning. Highs
78 to 86. Southeast winds 10 to 15 mph. Chance of rain
20 percent. 
.WEDNESDAY NIGHT...Mostly clear. Lows 67 to 77. East winds 10 to
15 mph. 
.THURSDAY...Mostly sunny. Breezy. Highs 77 to 86. Northeast winds
10 to 20 mph. 
.THURSDAY NIGHT...Partly cloudy. Lows 66 to 77. Northeast winds
10 to 15 mph. 
.FRIDAY...Mostly sunny. Highs 77 to 86. Northeast winds 10 to
15 mph. 
.FRIDAY NIGHT...Mostly clear. Lows 66 to 77. Northeast winds
10 to 15 mph. 
.SATURDAY...Breezy. Mostly sunny with isolated showers. Highs
77 to 85. Northeast winds 10 to 20 mph. Chance of rain
20 percent. 
.SATURDAY NIGHT...Mostly clear. Lows 66 to 76. Northeast winds
10 to 15 mph. 
.SUNDAY...Breezy. Mostly sunny with isolated showers. Highs 77 to
85. Northeast winds 10 to 15 mph increasing to 15 to 25 mph with
gusts to 45 mph in the afternoon. Chance of rain 20 percent. 

HIZ043-290715-
Lanai Leeward-
Including Kaumalapau Harbor
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny and breezy. Highs 82 to 88. Northeast winds up to
15 mph shifting to the southwest in the afternoon. 
.TONIGHT...Mostly clear. Breezy. Lows 72 to 78. Northeast winds
up to 20 mph becoming around 10 mph after midnight. 
.TUESDAY...Mostly sunny. Highs 82 to 88. Southeast winds 10 to
15 mph. 
.TUESDAY NIGHT...Partly cloudy with isolated showers. Lows 73 to
78. East winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY...Mostly sunny. Isolated showers in the morning. Highs
81 to 87. Southeast winds 10 to 15 mph. Chance of rain
20 percent. 
.WEDNESDAY NIGHT...Mostly clear with isolated showers. Lows 72 to
78. East winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY...Mostly sunny. Highs 81 to 87. East winds 10 to
15 mph. 
.THURSDAY NIGHT...Partly cloudy. Lows 71 to 77. East winds 10 to
15 mph. 
.FRIDAY...Mostly sunny. Highs 80 to 86. East winds 10 to 15 mph. 
.FRIDAY NIGHT...Mostly clear. Lows 71 to 77. East winds 10 to
15 mph. 
.SATURDAY...Breezy. Mostly sunny with isolated showers. Highs
80 to 86. Northeast winds 10 to 20 mph. Chance of rain
20 percent. 
.SATURDAY NIGHT...Mostly clear. Lows 71 to 77. Northeast winds
10 to 15 mph. 
.SUNDAY...Breezy. Mostly sunny with isolated showers. Highs 80 to
86. Northeast winds 10 to 15 mph increasing to 15 to 25 mph in
the afternoon. Chance of rain 20 percent. 

HIZ044-290715-
Lanai South-
Including Manele
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny. Highs around 83. Light winds becoming southwest
around 10 mph in the afternoon. 
.TONIGHT...Mostly clear. Lows around 76. Light winds becoming
east up to 15 mph after midnight. 
.TUESDAY...Mostly sunny. Breezy. Highs 80 to 85. East winds
around 10 mph shifting to the southeast 15 to 20 mph in the
afternoon. 
.TUESDAY NIGHT...Partly cloudy with isolated showers. Lows around
76. Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY...Mostly sunny. Isolated showers in the morning. Highs
around 81. Southeast winds 10 to 15 mph. Chance of rain
20 percent. 
.WEDNESDAY NIGHT...Mostly clear. Lows 73 to 78. East winds around
10 mph. 
.THURSDAY...Mostly sunny. Highs around 81. East winds around
10 mph. 
.THURSDAY NIGHT...Mostly clear. Lows 73 to 78. East winds around
10 mph. 
.FRIDAY...Mostly sunny. Highs around 81. East winds around
10 mph. 
.FRIDAY NIGHT...Mostly clear. Lows around 75. East winds around
10 mph in the evening becoming light. 
.SATURDAY...Sunny with isolated showers. Highs 78 to 83. East
winds 10 to 15 mph. Chance of rain 20 percent. 
.SATURDAY NIGHT...Mostly clear. Lows 72 to 77. Northeast winds
10 to 15 mph. 
.SUNDAY...Breezy. Sunny with isolated showers. Highs around 81.
Northeast winds 10 to 15 mph shifting to the north 15 to 25 mph
with gusts to 45 mph in the afternoon. Chance of rain 20 percent.

HIZ015-290715-
Lanai Mauka-
Including Lanai City
446 AM HST Mon Sep 28 2026

.TODAY...Sunny. Highs 79 to 86. Light winds becoming west up to
10 mph in the afternoon. 
.TONIGHT...Mostly clear. Lows 69 to 74. North winds up to 10 mph.
.TUESDAY...Mostly sunny. Breezy. Highs 79 to 85. Southeast winds
around 10 mph increasing to 15 to 20 mph in the afternoon. 
.TUESDAY NIGHT...Partly cloudy with isolated showers. Lows 69 to
74. East winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY...Mostly sunny. Breezy. Isolated showers in the
morning. Highs 78 to 84. Southeast winds 15 to 20 mph. Chance of
rain 20 percent. 
.WEDNESDAY NIGHT...Mostly clear. Lows around 71. East winds
around 10 mph. 
.THURSDAY...Mostly sunny. Highs 77 to 84. Northeast winds 10 to
15 mph. 
.THURSDAY NIGHT...Partly cloudy. Lows 68 to 73. Northeast winds
around 10 mph. 
.FRIDAY...Mostly sunny. Highs 77 to 83. Northeast winds 10 to
15 mph. 
.FRIDAY NIGHT...Mostly clear. Lows 68 to 73. Northeast winds
around 10 mph. 
.SATURDAY...Mostly sunny. Breezy. Isolated showers in the
morning, then scattered showers in the afternoon. Highs 77 to 83.
East winds 10 to 15 mph shifting to the northeast 15 to 25 mph in
the afternoon. Chance of rain 30 percent. 
.SATURDAY NIGHT...Mostly clear. Lows 68 to 73. Northeast winds
10 to 15 mph. 
.SUNDAY...Mostly sunny. Windy. Isolated showers in the morning,
then scattered showers in the afternoon. Highs 77 to 83.
Northeast winds 10 to 15 mph increasing to 20 to 30 mph in the
afternoon. Chance of rain 30 percent. 

HIZ016-290715-
Kahoolawe-
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny and windy. Highs 81 to 88. East winds 25 to
30 mph. 
.TONIGHT...Mostly clear. Windy. Lows 72 to 77. East winds 25 to
30 mph. 
.TUESDAY...Mostly sunny. Windy. Highs 80 to 87. East winds 15 to
20 mph increasing to 20 to 30 mph in the afternoon. 
.TUESDAY NIGHT...Breezy. Mostly clear with isolated showers. Lows
72 to 77. East winds 15 to 25 mph. Chance of rain 20 percent. 
.WEDNESDAY...Sunny and breezy. Highs 80 to 86. East winds 10 to
15 mph increasing to 20 to 25 mph in the afternoon. 
.WEDNESDAY NIGHT...Mostly clear. Breezy. Lows 72 to 77. East
winds 10 to 20 mph. 
.THURSDAY...Sunny and breezy. Highs 79 to 85. East winds 10 to
15 mph increasing to 15 to 25 mph in the afternoon. 
.THURSDAY NIGHT...Mostly clear. Lows 71 to 76. East winds 10 to
15 mph. 
.FRIDAY...Sunny. Highs 79 to 85. East winds 10 to 15 mph. 
.FRIDAY NIGHT...Partly cloudy. Lows 71 to 76. East winds around
10 mph. 
.SATURDAY...Sunny. Highs 79 to 85. East winds 10 to 15 mph. 
.SATURDAY NIGHT...Mostly clear. Lows 70 to 76. Light winds. 
.SUNDAY...Sunny. Highs 79 to 85. Light winds becoming east around
10 mph in the afternoon. 

HIZ017-290715-
Maui Windward West-
Including Wailuku
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and breezy. Isolated showers in the morning. Highs
around 84 makai to around 77 mauka. Northeast winds up to 20 mph.
Chance of rain 20 percent. 
.TONIGHT...Partly cloudy. Breezy. Lows 68 to 76 makai to around
60 mauka. Northeast winds up to 20 mph. 
.TUESDAY...Partly sunny. Highs around 84 makai to around
77 mauka. East winds 10 to 15 mph. 
.TUESDAY NIGHT...Mostly cloudy. Lows 61 to 76. East winds around
10 mph in the evening becoming light. 
.WEDNESDAY...Partly sunny. Highs 73 to 87. East winds 10 to
15 mph. 
.WEDNESDAY NIGHT...Mostly cloudy. Lows 60 to 76. East winds
around 10 mph. 
.THURSDAY...Partly sunny. Highs 72 to 86. East winds 10 to
15 mph. 
.THURSDAY NIGHT...Mostly cloudy. Lows 59 to 75. East winds 10 to
15 mph. 
.FRIDAY...Partly sunny. Highs 72 to 86. East winds up to 10 mph
shifting to the northeast in the afternoon. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 59 to
75. East winds up to 10 mph. Chance of rain 50 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 72 to 85.
Northeast winds up to 10 mph increasing to 10 to 15 mph in the
afternoon. Chance of rain 40 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
59 to 75. East winds around 10 mph. Chance of rain 40 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 72 to 85.
East winds up to 10 mph shifting to the northeast in the
afternoon. Chance of rain 40 percent. 

HIZ018-290715-
Maui Leeward West-
Including Lahaina, Kaanapali
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny. Highs 82 to 90. Southwest winds up to 15 mph. 
.TONIGHT...Partly cloudy. Lows 71 to 79. Northeast winds up to
15 mph. 
.TUESDAY...Mostly sunny. Highs 82 to 89. East winds up to 10 mph.
.TUESDAY NIGHT...Partly cloudy. Lows 71 to 79. Light winds. 
.WEDNESDAY...Mostly sunny. Highs 82 to 88. East winds up to
10 mph. 
.WEDNESDAY NIGHT...Partly cloudy. Lows 71 to 78. East winds up to
10 mph. 
.THURSDAY...Mostly sunny. Highs 80 to 87. East winds up to 10 mph
increasing to 10 to 15 mph in the afternoon. 
.THURSDAY NIGHT...Partly cloudy. Lows 70 to 77. East winds up to
10 mph. 
.FRIDAY...Mostly sunny. Highs 80 to 86. Northeast winds around
10 mph. 
.FRIDAY NIGHT...Partly cloudy with scattered showers. Lows 70 to
77. Northeast winds up to 10 mph. Chance of rain 30 percent. 
.SATURDAY...Mostly sunny. Isolated showers in the morning, then
scattered showers in the afternoon. Highs 79 to 86. Northeast
winds up to 10 mph increasing to 10 to 15 mph in the afternoon.
Chance of rain 30 percent. 
.SATURDAY NIGHT...Partly cloudy. Isolated showers in the evening,
then scattered showers after midnight. Lows 70 to 77. Northeast
winds up to 10 mph. Chance of rain 30 percent. 
.SUNDAY...Mostly sunny. Isolated showers in the morning, then
scattered showers in the afternoon. Highs 79 to 86. Northeast
winds up to 10 mph increasing to 10 to 15 mph in the afternoon.
Chance of rain 30 percent. 

HIZ045-290715-
Maui Central Valley North-
Including Kahului
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and breezy. Highs 83 to 91. East winds up to
20 mph. 
.TONIGHT...Partly cloudy. Breezy. Lows 70 to 76. East winds up to
20 mph. 
.TUESDAY...Mostly sunny in the morning then becoming partly
sunny. Breezy. Highs 83 to 90. East winds 10 to 20 mph. 
.TUESDAY NIGHT...Partly cloudy. Lows around 74. East winds around
10 mph in the evening becoming light. 
.WEDNESDAY...Mostly sunny. Highs 83 to 89. Northeast winds 10 to
15 mph. 
.WEDNESDAY NIGHT...Partly cloudy. Lows 71 to 76. East winds
around 10 mph in the evening becoming light. 
.THURSDAY...Mostly sunny. Breezy. Highs 82 to 88. Northeast winds
10 to 20 mph. 
.THURSDAY NIGHT...Partly cloudy. Lows 70 to 75. East winds around
10 mph in the evening becoming light. 
.FRIDAY...Mostly sunny. Scattered showers in the afternoon. Highs
82 to 88. Northeast winds 10 to 15 mph. Chance of rain
30 percent. 
.FRIDAY NIGHT...Partly cloudy with isolated showers. Lows 70 to
75. East winds around 10 mph in the evening becoming light.
Chance of rain 20 percent. 
.SATURDAY...Mostly sunny with isolated showers. Highs 82 to 88.
Northeast winds 10 to 15 mph. Chance of rain 20 percent. 
.SATURDAY NIGHT...Partly cloudy with isolated showers. Lows 70 to
75. Northeast winds around 10 mph in the evening becoming light.
Chance of rain 20 percent. 
.SUNDAY...Mostly sunny with isolated showers. Highs 81 to 88.
Light winds becoming northeast 10 to 15 mph in the afternoon.
Chance of rain 20 percent. 

HIZ046-290715-
Maui Central Valley South-
Including Maalaea
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny. Highs around 91. Northwest winds up to 10 mph
shifting to the west in the afternoon. 
.TONIGHT...Mostly clear. Lows 70 to 80. Northwest winds up to
15 mph shifting to the northeast after midnight. 
.TUESDAY...Sunny in the morning then becoming partly sunny. Highs
around 90. East winds 10 to 15 mph. 
.TUESDAY NIGHT...Partly cloudy. Lows 72 to 81. East winds up to
10 mph. 
.WEDNESDAY...Mostly sunny. Highs around 90. East winds 10 to
15 mph. 
.WEDNESDAY NIGHT...Mostly clear. Lows 72 to 80. East winds 10 to
15 mph. 
.THURSDAY...Mostly sunny. Highs around 89. Northeast winds 10 to
15 mph. 
.THURSDAY NIGHT...Partly cloudy. Lows 70 to 80. East winds around
10 mph. 
.FRIDAY...Mostly sunny in the morning then becoming partly sunny.
Highs around 88. Northeast winds 10 to 15 mph. 
.FRIDAY NIGHT...Mostly clear. Lows 70 to 80. East winds up to
10 mph. 
.SATURDAY...Sunny. Highs around 88. Northeast winds 10 to 15 mph.
.SATURDAY NIGHT...Mostly clear. Lows 70 to 79. Northeast winds
around 10 mph. 
.SUNDAY...Sunny. Highs around 88. Northeast winds 10 to 15 mph. 

HIZ047-290715-
Windward Haleakala-
Including Haiku, Makawao, Hana
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and breezy. Highs 80 to 85 near the shore to
around 71 near 5000 feet. Southeast winds up to 25 mph. 
.TONIGHT...Mostly cloudy. Breezy. Lows around 73 near the shore
to around 56 near 5000 feet. Southeast winds up to 20 mph. 
.TUESDAY...Partly sunny. Isolated showers in the afternoon. Highs
around 82 near the shore to around 70 near 5000 feet. East winds
10 to 15 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows 57 to
76. Southeast winds up to 10 mph. Chance of rain 40 percent. 
.WEDNESDAY...Partly sunny. Isolated showers in the morning, then
scattered showers in the afternoon. Highs 68 to 85. East winds
around 10 mph. Chance of rain 40 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Lows 57 to 76. East winds
around 10 mph. 
.THURSDAY...Partly sunny. Scattered showers in the afternoon.
Highs 67 to 84. East winds around 10 mph. Chance of rain
30 percent. 
.THURSDAY NIGHT...Mostly cloudy with isolated showers. Lows 56 to
76. East winds around 10 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny. Isolated showers in the morning, then
scattered showers in the afternoon. Highs 67 to 84. East winds up
to 10 mph. Chance of rain 30 percent. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 55 to
76. East winds up to 10 mph in the evening becoming light. Chance
of rain 50 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 66 to 83.
Light winds. Chance of rain 50 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
55 to 75. Light winds. Chance of rain 40 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 66 to 83.
Light winds becoming northeast up to 10 mph in the afternoon.
Chance of rain 50 percent. 

HIZ048-290715-
Kipahulu-
Including Hamoa
446 AM HST Mon Sep 28 2026

.TODAY...Sunny. Highs 75 to 84. East winds 10 to 15 mph. 
.TONIGHT...Mostly cloudy. Breezy. Lows 64 to 77. East winds 10 to
15 mph increasing to 10 to 25 mph after midnight. 
.TUESDAY...Partly sunny. Breezy. Isolated showers in the
afternoon. Highs 75 to 84. East winds 10 to 20 mph. Chance of
rain 20 percent. 
.TUESDAY NIGHT...Breezy. Mostly cloudy with scattered showers.
Lows 65 to 77. East winds 10 to 20 mph. Chance of rain
40 percent. 
.WEDNESDAY...Partly sunny. Breezy. Scattered showers in the
afternoon. Highs 75 to 84. East winds 10 to 20 mph. Chance of
rain 30 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Breezy. Lows 65 to 76. East
winds 10 to 20 mph. 
.THURSDAY...Partly sunny. Breezy. Scattered showers in the
afternoon. Highs 75 to 84. East winds 10 to 20 mph. Chance of
rain 30 percent. 
.THURSDAY NIGHT...Breezy. Mostly cloudy with isolated showers.
Lows 64 to 76. East winds 10 to 20 mph. Chance of rain
20 percent. 
.FRIDAY...Partly sunny. Isolated showers in the morning, then
scattered showers in the afternoon. Highs 74 to 83. East winds
10 to 15 mph. Chance of rain 30 percent. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 64 to
76. East winds 10 to 15 mph. Chance of rain 40 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 74 to 83.
East winds around 10 mph becoming up to 15 mph in the afternoon.
Chance of rain 40 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
64 to 76. East winds up to 15 mph. Chance of rain 40 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 74 to 83.
Northeast winds around 10 mph. Chance of rain 40 percent. 

HIZ049-290715-
South Maui/Upcountry-
Including Kihei, Makena, Pukalani, Kula, Ulupalakua
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny. Highs around 90 near the shore to around 78 near
4000 feet. North winds up to 10 mph shifting to the west in the
afternoon. 
.TONIGHT...Partly cloudy. Lows 71 to 76 near the shore to around
58 near 4000 feet. North winds up to 10 mph shifting to the
northeast after midnight. 
.TUESDAY...Mostly sunny in the morning then becoming partly
sunny. Highs around 89 near the shore to around 77 near
4000 feet. East winds up to 15 mph. 
.TUESDAY NIGHT...Partly cloudy. Lows 57 to 77. East winds up to
10 mph in the evening becoming light. 
.WEDNESDAY...Mostly sunny in the morning then becoming partly
sunny. Highs 71 to 90. Light winds becoming east up to 10 mph in
the afternoon. 
.WEDNESDAY NIGHT...Partly cloudy. Lows 57 to 76. Light winds. 
.THURSDAY...Mostly sunny. Highs 70 to 89. East winds up to
10 mph. 
.THURSDAY NIGHT...Partly cloudy. Lows 55 to 75. Light winds. 
.FRIDAY...Mostly sunny in the morning, then partly sunny with
scattered showers in the afternoon. Highs 70 to 89. Light winds
becoming east up to 10 mph in the afternoon. Chance of rain
30 percent. 
.FRIDAY NIGHT...Partly cloudy. Lows 56 to 75. Light winds. 
.SATURDAY...Mostly sunny. Highs 70 to 89. Light winds becoming
northeast up to 10 mph in the afternoon. 
.SATURDAY NIGHT...Mostly clear. Lows 56 to 75. Light winds. 
.SUNDAY...Mostly sunny. Highs 70 to 89. Light winds becoming
northeast up to 10 mph in the afternoon. 

HIZ050-290715-
South Haleakala-
Including Kipahulu, Kaupo
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny and windy. Highs 78 to 88. East winds 10 to
30 mph. 
.TONIGHT...Partly cloudy. Windy. Lows 57 to 76. East winds 10 to
30 mph. 
.TUESDAY...Breezy. Mostly sunny in the morning, then partly sunny
with isolated showers in the afternoon. Highs 77 to 86. East
winds 10 to 25 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Breezy. Partly cloudy with scattered showers.
Lows 59 to 77. East winds 10 to 20 mph. Chance of rain
40 percent. 
.WEDNESDAY...Mostly sunny in the morning, then partly sunny with
isolated showers in the afternoon. Highs 77 to 86. East winds
10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Breezy. Lows 58 to 76. East winds 10 to 20 mph. 
.THURSDAY...Mostly sunny in the morning then becoming partly
sunny. Breezy. Highs 76 to 85. East winds 10 to 20 mph. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows 57 to
75. East winds 10 to 15 mph. Chance of rain 20 percent. 
.FRIDAY...Mostly sunny with isolated showers. Highs 75 to 84.
East winds 10 to 15 mph. Chance of rain 20 percent. 
.FRIDAY NIGHT...Partly cloudy with isolated showers. Lows 56 to
75. East winds around 10 mph. Chance of rain 20 percent. 
.SATURDAY...Mostly sunny with isolated showers. Highs 75 to 84.
East winds around 10 mph becoming up to 15 mph in the afternoon.
Chance of rain 20 percent. 
.SATURDAY NIGHT...Partly cloudy with isolated showers. Lows 56 to
75. East winds up to 10 mph in the evening becoming light. Chance
of rain 20 percent. 
.SUNDAY...Mostly sunny with isolated showers. Highs 75 to 84.
Light winds becoming east up to 15 mph in the afternoon. Chance
of rain 20 percent. 

HIZ022-290715-
Haleakala Summit-
Including Haleakala National Park Above 6000 feet
446 AM HST Mon Sep 28 2026

.TODAY...Sunny and breezy. Highs 65 to 84. East winds up to
25 mph decreasing to up to 15 mph in the afternoon. 
.TONIGHT...Partly cloudy. Lows around 53 at the visitor center to
around 48 at the summit. East winds up to 15 mph. 
.TUESDAY...Mostly sunny in the morning, then partly sunny with
isolated showers in the afternoon. Highs around 71 at the visitor
center to around 68 at the summit. Light winds. Chance of rain
20 percent. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows 46 to
65. Light winds. Chance of rain 40 percent. 
.WEDNESDAY...Partly sunny. Scattered showers in the afternoon.
Highs 63 to 82. Light winds. Chance of rain 40 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Lows 49 to 65. Light winds. 
.THURSDAY...Partly sunny. Scattered showers in the afternoon.
Highs 63 to 81. Light winds. Chance of rain 30 percent. 
.THURSDAY NIGHT...Mostly cloudy with isolated showers. Lows 48 to
64. Light winds. Chance of rain 20 percent. 
.FRIDAY...Partly sunny. Isolated showers in the morning, then
scattered showers in the afternoon. Highs 64 to 81. Light winds.
Chance of rain 30 percent. 
.FRIDAY NIGHT...Mostly cloudy with isolated showers. Lows 47 to
63. Light winds. Chance of rain 20 percent. 
.SATURDAY...Mostly sunny with isolated showers. Highs 64 to 81.
Light winds. Chance of rain 20 percent. 
.SATURDAY NIGHT...Mostly clear in the evening then becoming
mostly cloudy. Isolated showers. Lows 47 to 63. Light winds.
Chance of rain 20 percent. 
.SUNDAY...Mostly sunny with isolated showers. Highs 64 to 81.
North winds up to 10 mph. Chance of rain 20 percent. 

HIZ023-290715-
Kona-
Including Kailua-Kona, Kealakekua, Milolii
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny in the morning, then mostly cloudy with isolated
showers in the afternoon. Highs 85 to 90 near the shore to around
72 near 5000 feet. Light winds. Chance of rain 20 percent. 
.TONIGHT...Partly cloudy. Lows 70 to 76 near the shore to around
56 near 5000 feet. Light winds becoming northeast up to 10 mph
after midnight. 
.TUESDAY...Mostly sunny. Scattered showers in the afternoon.
Highs 85 to 90 near the shore to around 72 near 5000 feet. West
winds up to 10 mph. Chance of rain 40 percent. 
.TUESDAY NIGHT...Partly cloudy. Lows 54 to 79. Light winds
becoming northeast around 10 mph after midnight. 
.WEDNESDAY...Mostly sunny. Scattered showers in the afternoon.
Highs 69 to 90. West winds up to 10 mph. Chance of rain
40 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Lows 54 to 79. Light winds
becoming northeast around 10 mph after midnight. 
.THURSDAY...Partly sunny. Scattered showers in the afternoon.
Highs 68 to 89. West winds around 10 mph. Chance of rain
40 percent. 
.THURSDAY NIGHT...Mostly cloudy. Lows 54 to 78. Light winds. 
.FRIDAY...Partly sunny. Highs 67 to 89. West winds around 10 mph
in the morning becoming light. 
.FRIDAY NIGHT...Mostly cloudy. Lows 53 to 78. Light winds. 
.SATURDAY...Mostly sunny in the morning then becoming partly
sunny. Highs 67 to 89. Light winds. 
.SATURDAY NIGHT...Mostly cloudy. Lows 53 to 78. Light winds. 
.SUNDAY...Mostly sunny. Highs 68 to 89. Light winds. 

HIZ051-290715-
Big Island South-
Including Ocean View
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Mostly sunny. Windy. Highs around 85 near the shore to
around 71 near 5000 feet. East winds up to 30 mph. 
.TONIGHT...Partly cloudy. Breezy. Lows around 76 near the shore
to around 59 near 5000 feet. East winds up to 25 mph increasing
to 10 to 25 mph after midnight. 
.TUESDAY...Mostly sunny. Breezy. Highs around 85 near the shore
to around 70 near 5000 feet. East winds 10 to 20 mph. 
.TUESDAY NIGHT...Partly cloudy. Lows 60 to 79. East winds 10 to
15 mph. 
.WEDNESDAY...Sunny in the morning then becoming partly sunny.
Highs 69 to 85. East winds 10 to 15 mph. 
.WEDNESDAY NIGHT...Mostly cloudy. Lows 60 to 79. East winds 10 to
15 mph. 
.THURSDAY...Partly sunny. Scattered showers in the afternoon.
Highs 69 to 85. East winds 10 to 15 mph. Chance of rain
40 percent. 
.THURSDAY NIGHT...Mostly cloudy. Lows 59 to 78. East winds 10 to
15 mph. 
.FRIDAY...Partly sunny. Highs 68 to 85. East winds 10 to 15 mph. 
.FRIDAY NIGHT...Mostly cloudy. Lows 59 to 78. East winds around
10 mph. 
.SATURDAY...Mostly sunny in the morning then becoming partly
sunny. Highs 68 to 85. East winds up to 10 mph in the morning
becoming light. 
.SATURDAY NIGHT...Mostly cloudy. Lows 59 to 78. Light winds
becoming northeast up to 10 mph after midnight. 
.SUNDAY...Partly sunny. Highs 69 to 85. Northeast winds up to
10 mph in the morning becoming light. 

HIZ052-290715-
Big Island Southeast-
Including South Point, Pahala
446 AM HST Mon Sep 28 2026

.TODAY...Mostly sunny. Isolated showers in the morning. Highs
83 to 91 near the shore to 70 to 75 near 4000 feet. Northeast
winds up to 15 mph shifting to the east in the afternoon. Chance
of rain 20 percent. 
.TONIGHT...Partly cloudy. Lows 69 to 75 near the shore to 57 to
62 near 4000 feet. Northeast winds up to 15 mph. 
.TUESDAY...Mostly sunny in the morning then becoming partly
sunny. Highs 82 to 88 near the shore to 68 to 74 near 4000 feet.
East winds up to 10 mph. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows 58 to
78. Northeast winds up to 10 mph. Chance of rain 40 percent. 
.WEDNESDAY...Mostly sunny in the morning, then partly sunny with
isolated showers in the afternoon. Highs 68 to 88. East winds up
to 10 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with isolated showers. Lows
58 to 77. Northeast winds up to 10 mph. Chance of rain
20 percent. 
.THURSDAY...Partly sunny. Highs 67 to 88. East winds around
10 mph. 
.THURSDAY NIGHT...Mostly cloudy with isolated showers. Lows 57 to
77. Northeast winds up to 10 mph. Chance of rain 20 percent. 
.FRIDAY...Mostly sunny with isolated showers in the morning, then
partly sunny in the afternoon. Highs 67 to 88. East winds around
10 mph. Chance of rain 20 percent. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 57 to
77. Northeast winds up to 10 mph. Chance of rain 50 percent. 
.SATURDAY...Mostly sunny in the morning then becoming partly
sunny. Scattered showers. Highs 68 to 89. East winds up to
10 mph. Chance of rain 40 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
57 to 77. Northeast winds up to 10 mph. Chance of rain
50 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 68 to 89.
East winds up to 15 mph. Chance of rain 40 percent. 

HIZ053-290715-
Big Island East-
Including Hilo, Volcano, Pahoa, Mountain View, Laupahoehoe
446 AM HST Mon Sep 28 2026

.TODAY...Sunny in the morning then becoming partly sunny.
Isolated showers. Highs around 84 near the shore to around 70 at
4000 feet. South winds up to 10 mph shifting to the east in the
afternoon. Gusts up to 30 mph. Chance of rain 20 percent. 
.TONIGHT...Mostly cloudy. Lows 67 to 73 near the shore to around
59 at 4000 feet. South winds up to 10 mph. 
.TUESDAY...Partly sunny. Isolated showers in the afternoon. Highs
around 84 near the shore to around 70 at 4000 feet. Southeast
winds around 10 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows 57 to
78. South winds up to 10 mph. Chance of rain 40 percent. 
.WEDNESDAY...Partly sunny. Isolated showers in the afternoon.
Highs 67 to 85. East winds around 10 mph. Chance of rain
20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Lows 56 to 77. Light winds. 
.THURSDAY...Partly sunny. Highs 66 to 85. East winds up to
10 mph. 
.THURSDAY NIGHT...Mostly cloudy with isolated showers. Lows 55 to
77. Light winds. Chance of rain 20 percent. 
.FRIDAY...Partly sunny. Isolated showers in the morning. Highs
66 to 85. Light winds becoming east around 10 mph in the
afternoon. Chance of rain 20 percent. 
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 55 to
77. Light winds. Chance of rain 50 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 66 to 85.
Light winds. Chance of rain 50 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
55 to 77. Light winds. Chance of rain 50 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 66 to 84.
Light winds becoming northeast around 10 mph in the afternoon.
Chance of rain 50 percent. 

HIZ054-290715-
Big Island North-
Including Honokaa, Kamuela, Waipio Valley, Hawi
446 AM HST Mon Sep 28 2026

.TODAY...Sunny in the morning then becoming partly sunny. Breezy.
Highs around 84 near the shore to 74 to 83 near 3000 feet. East
winds up to 20 mph. 
.TONIGHT...Mostly cloudy. Lows 67 to 75 near the shore to 61 to
68 near 3000 feet. East winds up to 15 mph. 
.TUESDAY...Partly sunny. Isolated showers in the afternoon. Highs
around 84 near the shore to 74 to 82 near 3000 feet. East winds
around 10 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy. Lows 56 to 76. Light winds. 
.WEDNESDAY...Partly sunny. Highs 68 to 85. Northeast winds around
10 mph. 
.WEDNESDAY NIGHT...Mostly cloudy. Lows 55 to 76. East winds up to
10 mph in the evening becoming light. 
.THURSDAY...Partly sunny. Highs 67 to 85. East winds around
10 mph. 
.THURSDAY NIGHT...Mostly cloudy. Lows 54 to 75. East winds up to
10 mph in the evening becoming light. 
.FRIDAY...Partly sunny. Highs 65 to 84. East winds around 10 mph.
.FRIDAY NIGHT...Mostly cloudy with scattered showers. Lows 54 to
75. Light winds. Chance of rain 50 percent. 
.SATURDAY...Partly sunny with scattered showers. Highs 66 to 84.
Northeast winds around 10 mph. Chance of rain 50 percent. 
.SATURDAY NIGHT...Mostly cloudy with scattered showers. Lows
53 to 75. East winds up to 10 mph in the evening becoming light.
Chance of rain 50 percent. 
.SUNDAY...Partly sunny with scattered showers. Highs 65 to 84.
Light winds becoming northeast around 10 mph in the afternoon.
Chance of rain 50 percent. 

HIZ026-290715-
Kohala-
Including Kawaihae, Waikoloa, Waikii, Puuanahulu
446 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST THIS EVENING...

.TODAY...Sunny. Highs 86 to 92 near the shore to 71 to 77 above
4000 feet. Northeast winds up to 10 mph shifting to the northwest
in the afternoon. 
.TONIGHT...Partly cloudy. Lows 72 to 77 near the shore to 56 to
61 above 4000 feet. Light winds. 
.TUESDAY...Mostly sunny in the morning then becoming partly
sunny. Highs 86 to 91 near the shore to 71 to 76 above 4000 feet.
Northwest winds up to 10 mph. 
.TUESDAY NIGHT...Partly cloudy. Lows 55 to 77. Light winds. 
.WEDNESDAY...Mostly sunny. Highs 68 to 92. Northwest winds up to
15 mph. 
.WEDNESDAY NIGHT...Partly cloudy. Lows 55 to 77. East winds up to
10 mph in the evening becoming light. 
.THURSDAY...Mostly sunny. Highs 68 to 91. Northwest winds 10 to
15 mph. 
.THURSDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Lows 54 to 77. East winds up to 10 mph in the
evening becoming light. 
.FRIDAY...Mostly sunny. Highs 67 to 90. Northwest winds 10 to
15 mph. 
.FRIDAY NIGHT...Partly cloudy. Lows 54 to 76. East winds up to
10 mph in the evening becoming light. 
.SATURDAY...Mostly sunny. Highs 67 to 91. Northwest winds 10 to
15 mph. 
.SATURDAY NIGHT...Partly cloudy. Lows 53 to 76. East winds up to
10 mph. 
.SUNDAY...Mostly sunny. Highs 67 to 91. Light winds becoming
northwest 10 to 15 mph in the afternoon. 

HIZ027-290715-
Big Island Interior-
Including Bradshaw Field, Saddle Road Above 5000 feet
446 AM HST Mon Sep 28 2026

.TODAY...Mostly sunny. Isolated showers in the afternoon. Highs
67 to 76 near 5000 feet to 62 to 69 near 8000 feet. East winds up
to 10 mph. Chance of rain 20 percent. 
.TONIGHT...Partly cloudy. Lows 53 to 59 near 5000 feet to around
51 near 8000 feet. East winds up to 10 mph in the evening
becoming light. 
.TUESDAY...Mostly sunny in the morning, then mostly cloudy with
isolated showers in the afternoon. Highs 67 to 75 near 5000 feet
to 62 to 68 near 8000 feet. North winds up to 10 mph. Chance of
rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy. Lows 49 to 60. Light winds. 
.WEDNESDAY...Mostly sunny in the morning, then mostly cloudy with
scattered showers in the afternoon. Highs 60 to 76. North winds
up to 10 mph. Chance of rain 40 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Lows 48 to 60. Light winds. 
.THURSDAY...Mostly sunny in the morning, then mostly cloudy with
scattered showers in the afternoon. Highs 60 to 75. North winds
up to 10 mph. Chance of rain 40 percent. 
.THURSDAY NIGHT...Mostly cloudy. Lows 47 to 59. Light winds. 
.FRIDAY...Mostly sunny in the morning then becoming partly sunny.
Highs 59 to 75. North winds up to 10 mph. 
.FRIDAY NIGHT...Mostly cloudy. Lows 46 to 59. Light winds. 
.SATURDAY...Mostly sunny in the morning then becoming partly
sunny. Highs 60 to 75. North winds up to 10 mph. 
.SATURDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Lows 46 to 59. Light winds. 
.SUNDAY...Mostly sunny. Highs 60 to 76. Light winds becoming
north around 10 mph in the afternoon. 

HIZ028-290715-
Big Island Summits-
Including Mauna Loa and Mauna Kea Above 8000 feet
446 AM HST Mon Sep 28 2026

.TODAY...Sunny. Highs around 61 at the visitor information
station to around 51 near the summits. East winds up to 10 mph. 
.TONIGHT...Partly cloudy. Lows around 47 at the visitor
information station to around 40 near the summits. Light winds. 
.TUESDAY...Mostly sunny in the morning, then mostly cloudy with
isolated showers in the afternoon. Highs around 60 at the visitor
information station to around 49 near the summits. Light winds.
Chance of rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy. Lows 37 to 54. Light winds
becoming west up to 10 mph after midnight. 
.WEDNESDAY...Mostly sunny in the morning, then mostly cloudy with
isolated showers in the afternoon. Highs 49 to 72. Northwest
winds up to 10 mph in the morning becoming light. Chance of rain
20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Lows 39 to 54. Light winds. 
.THURSDAY...Mostly sunny in the morning then becoming partly
sunny. Highs 51 to 71. Light winds becoming north around 10 mph
in the afternoon. 
.THURSDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Lows 38 to 53. Northwest winds up to 10 mph in the
evening becoming light. 
.FRIDAY...Mostly sunny in the morning then becoming partly sunny.
Highs 51 to 71. Light winds. 
.FRIDAY NIGHT...Mostly cloudy in the evening then becoming partly
cloudy. Lows 39 to 52. Light winds. 
.SATURDAY...Mostly sunny. Highs 51 to 71. Light winds becoming
north up to 10 mph in the afternoon. 
.SATURDAY NIGHT...Partly cloudy. Lows 40 to 52. East winds up to
10 mph shifting to the west after midnight. 
.SUNDAY...Mostly sunny. Highs 50 to 72. Northeast winds up to
10 mph in the morning becoming light.
```

---

### 2. AIRMETs

| Field | Value |
|---|---|
| **Resource ID** | wa0_airmets |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=WA0&issuedby=HI |
| **Collected** | 2026-09-27T23:31:24.329941-10:00 HST |

```text
442
WAHW31 PHFO 280924
WA0HI

HNLS WA 281000
AIRMET SIERRA UPDATE 1 FOR IFR VALID UNTIL 281600
.
NO SIGNIFICANT IFR EXP.

=HNLT WA 281000
AIRMET TANGO UPDATE 1 FOR TURB VALID UNTIL 281600
.
AIRMET TURB...HI
OVER AND IMT S THRU W OF MTN.
TEMPO MOD TURB BLW 090.
COND CONT BEYOND 1600Z.
.
AIRMET STG SFC WND...MOLOKAI LANAI MAUI AND BIG ISLAND...UPDATE
ENTIRE AREA.
CANCEL AIRMET. CONDS HAVE IMPROVED.

=HNLZ WA 281000
AIRMET ZULU UPDATE 1 FOR ICE AND FZLVL VALID UNTIL 281600
.
NO SIGNIFICANT ICE EXP.
.
FZLVL...164-169.
```

---

### 3. Area Forecast Discussion

| Field | Value |
|---|---|
| **Resource ID** | afd_area_forecast_discussion |
| **Official source** | https://api.weather.gov/products/types/AFD/locations/HFO |
| **Collected** | 2026-09-28T05:02:21.062282-10:00 HST |

```text
000
FXHW60 PHFO 281452
AFDHFO

Area Forecast Discussion
National Weather Service Honolulu HI
452 AM HST Mon Sep 28 2026

.SYNOPSIS...
Deepening high pressure north of the state will produce drier and
fair conditions across the region through Tuesday. Major hurricane
Nolo will continue to move west away from the state. Nolo is 
expected to turn toward the northwest on Tuesday and Wednesday, 
passing west of Kauai and Niihau. Trailing moisture associated 
with the eastern part of Nolo's circulation will bring an 
increase in shower activity beginning on Tuesday night and 
continuing into Thursday. High pressure system will re-establish 
again by the end of the week. 

.DISCUSSION...
Radar images detected an increase in trade wind showers across 
the coastal waters. These showers were moving mainly northeast of
the islands with some making its way into Molokai and Oahu from
time to time. Rainfall accumulation were minimal. A relatively 
dry weather pattern is expected to continue statewide through 
Tuesday as a high pressure system briefly dominates the area.
Winds have diminished since yesterday. As a result, the wind
advisory which was in effect for portions of Maui, Molokai, Oahu,
and the Big Island was cancelled.

Major hurricane Nolo continues to move west away from the local
region. However, by Tuesday Nolo is expected to turn northwest
passing around 200 miles west of Niihau and Kauai. Although the
core of the hurricane will pass at a safe distance from the
islands,trailing moisture associated with Nolo's circulation is 
expected to affect both islands, and possible Oahu from Tuesday 
night into Wednesday. Latest model guidance are projecting 
rainfall accumulation between one to two inches. Although no 
significant flooding is expected at this time, we will closely 
monitor the evolution of Nolo as latest guidance are showing deep
tropical moisture moving over the islands from Tuesday through 
Thursday which could enhance the amount of rainfall expected. 
Precipitable water values are expected to increase from 1.10 
inches up to 2.4 inches by Tuesday night and Wednesday. 

In the long term, no significant weather events are forecast to 
affect the state as a high pressure system builds north and 
northeast of the region. 

.AVIATION...
Breezy to locally strong trades will prevail today but will be
noticeably less than the past couple of days as Hurricane Nolo 
moves further away from the state and the pressure gradient over
the islands begins to relax. Showers will be fairly limited 
today, with just a few light showers embedded within the trades 
favoring windward and mountain locations. 

AIRMET Tango remains in effect for moderate turbulence below 
9,000 feet over and immediately downwind of island terrain. This
AIRMET will likely be needed through mid-week.

.MARINE...
Strong to near gale force trade winds and large, rough seas will 
gradually diminish through tonight as high pressure far north of 
the state begins to weaken and Hurricane Nolo, several hundred
miles southwest of the Hawaiian Islands, moves farther west. The 
Small Craft Advisory (SCA) for all Hawaiian coastal waters (with
the exception of Maalaea Bay) has been extended through tonight.
Beyond that point, trade winds are expected to weaken below small
craft advisory for most waters. Higher seas and strong winds may
persist for favored channels and waters near Kauai, where the
current National Hurricane Center forecast has Nolo tracking
around 230 nautical miles west of on Wednesday. Expect moderate 
to locally strong winds to veer out of the east-southeast to 
southeast during this time. Winds will gradually ease and back 
more easterly by Thursday as Nolo moves westward away from the 
islands.

A mix of long to medium period south-southwest swell and building
short to medium south swell from a powerful Hurricane Nolo now 
located southwest of the Hawaiian Islands will bring advisory level 
surf to south facing shores of all islands and west facing shores of 
the Big Island today. The hurricane-generated swell will gradually 
shift southwest, then west, as Nolo tracks northwest roughly parallel
to the islands through Wednesday. While the forecast currently shows 
this swell gradually decreasing, and in particular, falling below 
advisory criteria tonight, Nolo is forecast to remain a major 
hurricane through Tuesday, which could maintain advisory level surf 
for longer than currently depicted. By mid-week, these swells will
originate from the west and be diminishing as the hurricane will be
weaker and it begins to track away from the islands.

East shore surf will slowly decline through Wednesday as trade winds
diminish. However, small, medium period swells from distant East 
Pacific hurricanes will maintain moderate surf during the remainder of
the week. On north facing shores, a small medium period swell will 
fade through Wednesday. Some wrapping west swell from Hurricane Nolo 
is possible by Wednesday.

.FIRE WEATHER...
Issued at 342 AM HST Mon Sep 28 2026

Dry weather conditions are expected to prevail across the state
today into Tuesday. An increase in shower activity is expected on
Tuesday and Wednesday as deep tropical moisture makes its way
towards the islands as Hurricane Nolo pass west of the area. 
Fire concern will remain low for now as relative humidity values 
will remain above critical levels and winds have diminished as 
well.

.HFO WATCHES/WARNINGS/ADVISORIES...
Wind Advisory until 6 AM HST early this morning for Big Island 
North-Central Oahu-East Honolulu-Honolulu Metro-Kipahulu-Kohala-
Koolau Leeward-Maui Central Valley North-Maui Central Valley 
South-Maui Leeward West-Maui Windward West-Molokai Leeward South-
Molokai North-Molokai Southeast-Molokai West-Molokai Windward-
Oahu North Shore-South Haleakala.

High Surf Advisory until 6 AM HST early this morning for Kauai 
East-Kauai South-Koolau Windward-Olomana.

Small Craft Advisory until 6 PM HST this evening for Alenuihaha 
Channel-Big Island Leeward Waters-Big Island Southeast Waters-
Big Island Windward Waters-Kaiwi Channel-Kauai Channel-Kauai 
Leeward Waters-Kauai Northwest Waters-Kauai Windward Waters-Maui 
County Leeward Waters-Maui County Windward Waters-Oahu Leeward 
Waters-Oahu Windward Waters-Pailolo Channel.

DISCUSSION...Castro
AVIATION...Vaughan
MARINE...Quesada
Fire....Castro
```

---

### 4. Coastal Waters Forecast (within 40nm)

| Field | Value |
|---|---|
| **Resource ID** | cwf_coastal_waters |
| **Official source** | https://api.weather.gov/products/types/CWF/locations/HFO |
| **Collected** | 2026-09-28T04:05:21.206973-10:00 HST |

```text
000
FZHW50 PHFO 281358
CWFHFO

Coastal Waters Forecast
National Weather Service Honolulu HI
358 AM HST Mon Sep 28 2026

Hawaiian coastal waters within 40 nautical miles including the
Hawaiian Islands Humpback Whale National Marine Sanctuary.

PHZ100-290215-
358 AM HST Mon Sep 28 2026

.Synopsis for Hawaiian coastal waters...
Strong to near gale force trade winds and rough seas will 
gradually decline today as Hurricane Nolo remains several hundred
miles southwest of the Hawaiian Islands, tracking northwest. 
Fresh to strong winds will veer out of the southeast tonight 
through Tuesday night as Nolo begins to pass west of Kauai. Nolo 
is forecast to move farther away to the west beginning Wednesday,
allowing winds to diminish and back out of the east for the latter
half of the week.

PHZ110-290215-
Kauai Northwest Waters-
358 AM HST Mon Sep 28 2026

...SMALL CRAFT ADVISORY IN EFFECT THROUGH EARLY TUESDAY MORNING...

.TODAY...East winds 25 to 30 knots, easing to 20 to 25 knots this
afternoon. Seas 8 to 10 feet. Wave Detail: East 9 feet at
8 seconds, south southwest 5 feet at 10 seconds and north
northwest 3 feet at 12 seconds. Scattered showers. 
.TONIGHT...East winds 20 to 25 knots. Seas 8 to 10 feet. Wave
Detail: East 8 feet at 7 seconds and south southwest 5 feet at
11 seconds. Scattered showers. 
.TUESDAY...East southeast winds 25 to 30 knots. Seas 8 to
11 feet. Wave Detail: Southeast 9 feet at 7 seconds and southwest
5 feet at 9 seconds. Scattered showers in the morning, then
occasional showers in the afternoon. 
.TUESDAY NIGHT...Southeast winds 25 to 30 knots. Seas 8 to
11 feet. Wave Detail: Southeast 9 feet at 7 seconds, west
northwest 4 feet at 11 seconds and south southwest 4 feet at
15 seconds. Occasional showers. 
.WEDNESDAY...Southeast winds 25 to 30 knots, easing to 20 to
25 knots in the afternoon. Seas 7 to 10 feet. Wave Detail:
Southeast 9 feet at 7 seconds, west northwest 4 feet at
10 seconds and south southwest 4 feet at 15 seconds. Numerous
showers. 
.WEDNESDAY NIGHT...Southeast winds 20 to 25 knots. Seas 6 to
9 feet. Wave Detail: Southeast 8 feet at 7 seconds and south
southwest 3 feet at 14 seconds. Numerous showers. 
.THURSDAY...Southeast winds 15 to 20 knots. Seas 5 to 8 feet.
Wave Detail: East southeast 7 feet at 6 seconds. Numerous
showers, mainly in the morning. 
.FRIDAY...Southeast winds 10 to 15 knots. Seas 5 to 6 feet. Wave
Detail: East 5 feet at 6 seconds and south southwest 3 feet at
12 seconds. Scattered showers.  

PHZ111-290215-
Kauai Windward Waters-
358 AM HST Mon Sep 28 2026

...SMALL CRAFT ADVISORY IN EFFECT THROUGH EARLY TUESDAY MORNING...

.TODAY...East winds 20 to 25 knots. Seas 8 to 11 feet. Wave
Detail: East southeast 9 feet at 8 seconds, south southwest
5 feet at 9 seconds and north northwest 3 feet at 14 seconds.
Scattered showers this morning, then numerous showers this
afternoon. 
.TONIGHT...East southeast winds 20 to 25 knots. Seas 8 to
10 feet. Wave Detail: East 8 feet at 7 seconds and south
southwest 4 feet at 7 seconds. Scattered showers. 
.TUESDAY...East southeast winds 20 to 25 knots. Seas 7 to 9 feet.
Wave Detail: South southeast 8 feet at 7 seconds. Scattered
showers in the morning, then numerous showers in the afternoon. 
.TUESDAY NIGHT...Southeast winds 20 to 25 knots. Seas 7 to
8 feet. Wave Detail: East 7 feet at 7 seconds and south 4 feet at
15 seconds. Occasional showers. 
.WEDNESDAY...Southeast winds 20 to 25 knots, easing to 15 to
20 knots in the afternoon. Seas 6 to 8 feet. Wave Detail: East
7 feet at 7 seconds and south 4 feet at 15 seconds. Numerous
showers. 
.WEDNESDAY NIGHT...Southeast winds 15 to 20 knots. Seas 6 to
7 feet. Wave Detail: East 6 feet at 6 seconds and south 3 feet at
14 seconds. Numerous showers. 
.THURSDAY...East southeast winds 15 to 20 knots. Seas 5 to
7 feet. Wave Detail: East 6 feet at 6 seconds. Numerous showers,
mainly in the morning. 
.FRIDAY...East southeast winds 10 to 15 knots. Seas 5 to 6 feet.
Wave Detail: East 5 feet at 6 seconds and south 3 feet at
13 seconds. Isolated showers through the night, then scattered
showers through the day.  

PHZ112-290215-
Kauai Leeward Waters-
358 AM HST Mon Sep 28 2026

...SMALL CRAFT ADVISORY IN EFFECT THROUGH EARLY TUESDAY MORNING...

.TODAY...East winds 20 to 25 knots. Seas 9 to 10 feet. Wave
Detail: East southeast 9 feet at 8 seconds and south southwest
5 feet at 9 seconds. Isolated showers. 
.TONIGHT...East southeast winds 20 to 25 knots, rising to 25 to
30 knots after midnight. Seas 9 to 10 feet. Wave Detail:
Southeast 9 feet at 8 seconds and south southwest 5 feet at
11 seconds. Numerous showers. 
.TUESDAY...Southeast winds 25 to 30 knots. Seas 8 to 11 feet.
Wave Detail: Southeast 9 feet at 8 seconds and southwest 5 feet
at 7 seconds. Occasional showers. 
.TUESDAY NIGHT...Southeast winds 25 to 30 knots. Seas 9 to
12 feet. Wave Detail: Southeast 9 feet at 7 seconds, west
northwest 6 feet at 11 seconds and south southwest 4 feet at
15 seconds. Occasional showers. 
.WEDNESDAY...South southeast winds 25 to 30 knots. Seas 8 to
11 feet. Wave Detail: Southeast 7 feet at 7 seconds, west
northwest 6 feet at 10 seconds and south southwest 4 feet at
15 seconds. Occasional showers. 
.WEDNESDAY NIGHT...Southeast winds 25 to 30 knots. Seas 7 to
9 feet. Wave Detail: Southeast 6 feet at 6 seconds, west
northwest 4 feet at 9 seconds and south southwest 3 feet at
14 seconds. Occasional showers. 
.THURSDAY...Southeast winds 25 to 30 knots, easing to 20 to
25 knots. Seas 5 to 8 feet. Wave Detail: East southeast 5 feet at
6 seconds, northwest 3 feet at 9 seconds and south southwest
3 feet at 13 seconds. Occasional showers through the night, then
scattered showers through the day. 
.FRIDAY...Southeast winds 15 to 20 knots, easing to 10 to
15 knots. In the Kaulakahi Channel, southeast winds 25 to
30 knots, becoming east southeast 10 to 15 knots. Seas 4 to
6 feet. Wave Detail: East southeast 5 feet at 6 seconds and south
southwest 4 feet at 12 seconds. Scattered showers.  

PHZ113-290215-
Kauai Channel-
358 AM HST Mon Sep 28 2026

...SMALL CRAFT ADVISORY IN EFFECT THROUGH EARLY TUESDAY MORNING...

.TODAY...East winds 20 to 25 knots. Seas 9 to 10 feet. Wave
Detail: East southeast 9 feet at 8 seconds and south southwest
5 feet at 9 seconds. 
.TONIGHT...East winds 20 to 25 knots, becoming east southeast
15 to 20 knots after midnight. Seas 7 to 10 feet. Wave Detail:
East northeast 8 feet at 7 seconds and southwest 5 feet at
7 seconds. Isolated showers. 
.TUESDAY...Southeast winds 15 to 20 knots. Seas 7 to 9 feet. Wave
Detail: South 7 feet at 7 seconds. Scattered showers in the
morning, then occasional showers in the afternoon. 
.TUESDAY NIGHT...Southeast winds to 20 knots. Seas 7 to 9 feet.
Wave Detail: Southeast 7 feet at 7 seconds, south southwest
4 feet at 15 seconds and west northwest 3 feet at 11 seconds.
Occasional showers. 
.WEDNESDAY...South southeast winds 15 to 20 knots. Seas 7 to
9 feet, subsiding to 6 to 7 feet in the afternoon. Wave Detail:
Southeast 7 feet at 6 seconds, south southwest 4 feet at
15 seconds and west northwest 3 feet at 10 seconds. Occasional
showers. 
.WEDNESDAY NIGHT...Southeast winds to 15 knots. Seas 6 to 7 feet.
Wave Detail: Southeast 6 feet at 6 seconds and south southwest
3 feet at 14 seconds. Occasional showers. 
.THURSDAY...East southeast winds to 15 knots. Seas 5 to 6 feet.
Wave Detail: Southeast 5 feet at 6 seconds and south 3 feet at
13 seconds. Numerous showers, mainly in the morning. 
.FRIDAY...East southeast winds 10 to 15 knots. Seas 4 to 6 feet.
Wave Detail: East 5 feet at 6 seconds and south 3 feet at
13 seconds. Scattered showers.  

PHZ114-290215-
Oahu Windward Waters-
358 AM HST Mon Sep 28 2026

...SMALL CRAFT ADVISORY IN EFFECT THROUGH EARLY TUESDAY MORNING...

.TODAY...East winds 20 to 25 knots. Seas 8 to 11 feet. Wave
Detail: East southeast 9 feet at 7 seconds, south southwest
4 feet at 9 seconds and north northwest 3 feet at 14 seconds.
Scattered showers. 
.TONIGHT...East winds 20 to 25 knots. Seas 6 to 8 feet. Wave
Detail: East 7 feet at 7 seconds and south southwest 4 feet at
8 seconds. Isolated showers. 
.TUESDAY...East southeast winds to 20 knots. Seas 6 to 8 feet.
Wave Detail: East 7 feet at 7 seconds and south southwest 3 feet
at 13 seconds. Isolated showers in the afternoon. 
.TUESDAY NIGHT...Southeast winds 15 to 20 knots. Seas 5 to
7 feet. Wave Detail: East 6 feet at 6 seconds. Scattered showers.
.WEDNESDAY...Southeast winds 15 to 20 knots. Seas 5 to 7 feet.
Wave Detail: East 6 feet at 6 seconds. Scattered showers in the
morning. 
.WEDNESDAY NIGHT...East southeast winds 15 to 20 knots. Seas 5 to
6 feet. Wave Detail: East southeast 6 feet at 6 seconds.
Scattered showers. 
.THURSDAY...East southeast winds 15 to 20 knots. Seas 5 to
6 feet. Wave Detail: East 5 feet at 6 seconds. Scattered showers
in the morning. Isolated showers through the day. 
.FRIDAY...East southeast winds 10 to 15 knots. Seas to 5 feet.
Wave Detail: East 5 feet at 6 seconds. Isolated showers through
the night, then scattered showers through the day.  

PHZ115-290215-
Oahu Leeward Waters-
358 AM HST Mon Sep 28 2026

...SMALL CRAFT ADVISORY IN EFFECT THROUGH EARLY TUESDAY MORNING...

.TODAY...East winds 15 to 20 knots. Seas 9 to 10 feet, subsiding
to 7 to 9 feet this afternoon. Wave Detail: East southeast 9 feet
at 8 seconds and south southwest 5 feet at 9 seconds. 
.TONIGHT...East southeast winds 15 to 20 knots. Seas 7 to 9 feet.
Wave Detail: East southeast 7 feet at 7 seconds and south
southwest 5 feet at 7 seconds. Isolated showers. 
.TUESDAY...Southeast winds 15 to 20 knots. Seas 6 to 8 feet. Wave
Detail: Southeast 7 feet at 7 seconds and south southwest 4 feet
at 16 seconds. Scattered showers. 
.TUESDAY NIGHT...Southeast winds 15 to 20 knots. Seas 6 to
7 feet, building to 7 to 9 feet after midnight. Wave Detail:
Southeast 5 feet at 6 seconds, west northwest 5 feet at
11 seconds and south southwest 4 feet at 15 seconds. Scattered
showers. 
.WEDNESDAY...Southeast winds 15 to 20 knots, becoming south
southeast 10 to 15 knots in the afternoon. Seas 6 to 8 feet. Wave
Detail: Southeast 6 feet at 6 seconds, west northwest 4 feet at
10 seconds and south southwest 4 feet at 15 seconds. Numerous
showers. 
.WEDNESDAY NIGHT...Southeast winds 10 to 15 knots. Seas 5 to
7 feet. Wave Detail: Southeast 5 feet at 6 seconds, west
northwest 3 feet at 9 seconds and south southwest 3 feet at
14 seconds. Numerous showers. 
.THURSDAY...East southeast winds 10 to 15 knots. Seas 5 to
7 feet. Wave Detail: Southeast 5 feet at 6 seconds and south
southwest 3 feet at 13 seconds. Numerous showers through the
night. Scattered showers through the day. 
.FRIDAY...East southeast winds to 10 knots. Seas 4 to 5 feet.
Wave Detail: Southeast 4 feet at 5 seconds and south southwest
3 feet at 13 seconds. Isolated showers.  

PHZ116-290215-
Kaiwi Channel-
358 AM HST Mon Sep 28 2026

...SMALL CRAFT ADVISORY IN EFFECT THROUGH EARLY TUESDAY MORNING...

.TODAY...East winds 25 to 30 knots, easing to 20 to 25 knots this
afternoon. Seas 8 to 11 feet, subsiding to 8 to 9 feet this
afternoon. Wave Detail: East 10 feet at 7 seconds and south
southwest 5 feet at 9 seconds. 
.TONIGHT...East winds 20 to 25 knots. Seas 7 to 9 feet. Wave
Detail: East 7 feet at 7 seconds and south southwest 4 feet at
12 seconds. 
.TUESDAY...East southeast winds 15 to 20 knots. Seas 6 to 8 feet.
Wave Detail: Southeast 6 feet at 7 seconds and south southwest
4 feet at 12 seconds. 
.TUESDAY NIGHT...Southeast winds 15 to 20 knots, easing to 10 to
15 knots after midnight. Seas 6 to 8 feet. Wave Detail: Southeast
5 feet at 6 seconds, south southwest 4 feet at 16 seconds and
northwest 3 feet at 11 seconds. Scattered showers. 
.WEDNESDAY...Southeast winds 10 to 15 knots, rising to 15 to
20 knots in the afternoon. Seas 5 to 7 feet. Wave Detail:
Southeast 5 feet at 6 seconds, south southwest 4 feet at
15 seconds and northwest 3 feet at 10 seconds. Scattered showers
in the morning. 
.WEDNESDAY NIGHT...East southeast winds 10 to 15 knots. Seas 5 to
6 feet. Wave Detail: Southeast 5 feet at 6 seconds and south
southwest 3 feet at 14 seconds. Scattered showers. 
.THURSDAY...East southeast winds 15 to 20 knots, becoming east
10 to 15 knots. Seas 5 to 6 feet. Wave Detail: Southeast 5 feet
at 6 seconds and south 3 feet at 13 seconds. Scattered showers in
the morning. Isolated showers through the day. 
.FRIDAY...East southeast winds 10 to 15 knots. Seas 4 to 5 feet.
Wave Detail: East 4 feet at 5 seconds and south southwest 3 feet
at 13 seconds. Isolated showers through the night. Scattered
showers through the day.  

PHZ117-290215-
Maui County Windward Waters-
358 AM HST Mon Sep 28 2026

...SMALL CRAFT ADVISORY IN EFFECT THROUGH EARLY TUESDAY MORNING...

.TODAY...East southeast winds 25 to 30 knots, easing to 20 to
25 knots this afternoon. Seas 7 to 10 feet, subsiding to 6 to
8 feet this afternoon. Wave Detail: Southeast 8 feet at 7 seconds
and north northwest 3 feet at 15 seconds. Scattered showers. 
.TONIGHT...East southeast winds 20 to 25 knots. Seas 5 to 7 feet.
Wave Detail: Southeast 6 feet at 6 seconds and north northwest
3 feet at 12 seconds. Isolated showers. 
.TUESDAY...East southeast winds to 20 knots. Seas 5 to 6 feet.
Wave Detail: East southeast 5 feet at 6 seconds. 
.TUESDAY NIGHT...East southeast winds 15 to 20 knots. Seas 4 to
5 feet. Wave Detail: Southeast 5 feet at 5 seconds. Isolated
showers. 
.WEDNESDAY...East southeast winds 15 to 20 knots. Seas 4 to
5 feet. Wave Detail: East southeast 5 feet at 5 seconds. Isolated
showers in the morning. 
.WEDNESDAY NIGHT...East southeast winds 15 to 20 knots. Seas 4 to
5 feet. Wave Detail: East southeast 5 feet at 5 seconds. Isolated
showers. 
.THURSDAY...East southeast winds 15 to 20 knots. Seas 4 to
5 feet. Wave Detail: East 4 feet at 5 seconds. Isolated showers
in the morning. Isolated showers through the day. 
.FRIDAY...East southeast winds 15 to 20 knots, easing to 10 to
15 knots after midnight. Seas 4 to 5 feet. Wave Detail: East
northeast 4 feet at 5 seconds. Scattered showers through the day.

PHZ118-290215-
Maui County Leeward Waters-
358 AM HST Mon Sep 28 2026

...SMALL CRAFT ADVISORY IN EFFECT THROUGH EARLY TUESDAY MORNING...

.TODAY...East southeast winds 25 to 30 knots, backing to east
20 to 25 knots this afternoon. Seas 8 to 11 feet. Wave Detail:
East southeast 10 feet at 8 seconds and south southwest 5 feet at
9 seconds. 
.TONIGHT...East winds 20 to 25 knots, rising to 25 to 30 knots
after midnight. Seas 7 to 10 feet. Wave Detail: East southeast
8 feet at 7 seconds and south southwest 4 feet at 12 seconds.
Isolated showers. 
.TUESDAY...East southeast winds 20 to 25 knots, becoming
southeast 15 to 20 knots in the afternoon. Seas 7 to 10 feet,
subsiding to 6 to 8 feet in the afternoon. Wave Detail: Southeast
8 feet at 7 seconds and south southwest 4 feet at 12 seconds.
Isolated showers in the morning. Scattered showers in the
afternoon. 
.TUESDAY NIGHT...Southeast winds 15 to 20 knots. Seas 6 to
8 feet. Wave Detail: South southeast 5 feet at 6 seconds, west
northwest 4 feet at 11 seconds and south southwest 4 feet at
16 seconds. Scattered showers. 
.WEDNESDAY...Southeast winds 20 to 25 knots, easing to 15 to
20 knots in the afternoon. Seas 5 to 8 feet. Wave Detail: South
southeast 5 feet at 6 seconds, west northwest 4 feet at
10 seconds and south southwest 4 feet at 15 seconds. Scattered
showers in the morning. 
.WEDNESDAY NIGHT...East southeast winds 20 to 25 knots. Seas 5 to
7 feet. Wave Detail: South southeast 5 feet at 6 seconds and
south southwest 3 feet at 14 seconds. Scattered showers. 
.THURSDAY...East southeast winds 15 to 20 knots, becoming east
10 to 15 knots in the evening, rising to 15 to 20 knots after
midnight. Seas 4 to 6 feet. Wave Detail: South southeast 5 feet
at 6 seconds and south southwest 3 feet at 13 seconds. Scattered
showers in the morning. Scattered showers through the day. 
.FRIDAY...East southeast winds 15 to 20 knots, easing to 10 to
15 knots. Seas 3 to 5 feet. Wave Detail: South southeast 4 feet
at 5 seconds and south southwest 3 feet at 13 seconds. Isolated
showers through the night. Isolated showers after midnight.  

PHZ119-290215-
Maalaea Bay-
358 AM HST Mon Sep 28 2026

.TODAY...North winds 15 to 20 knots. Seas to 3 feet this morning,
then to 2 feet or less. Wave Detail: South southeast 3 feet at
8 seconds and south southwest 3 feet at 9 seconds. 
.TONIGHT...North northeast winds 15 to 20 knots. Seas to 2 feet
or less. Wave Detail: South southeast 2 feet at 7 seconds. 
.TUESDAY...East southeast winds to 10 knots, rising to 15 knots
in the afternoon. Seas to 2 feet or less, then to 3 feet in the
afternoon. Wave Detail: South southeast 3 feet at 6 seconds. 
.TUESDAY NIGHT...East southeast winds 7 to 10 knots. Seas to
3 feet in the evening, then to 2 feet or less. Wave Detail: South
southeast 3 feet at 6 seconds. 
.WEDNESDAY...Southeast winds to 10 knots. Seas to 2 feet or less.
Wave Detail: South 2 feet at 6 seconds. 
.WEDNESDAY NIGHT...East winds to 10 knots. Seas to 2 feet or
less. Wave Detail: South 2 feet at 6 seconds. 
.THURSDAY...East winds 10 to 15 knots, becoming 7 to 10 knots.
Seas to 2 feet or less. 
.FRIDAY...East southeast winds 7 to 10 knots, becoming variable
less than 10 knots. Seas to 2 feet or less.  

PHZ120-290215-
Pailolo Channel-
358 AM HST Mon Sep 28 2026

...SMALL CRAFT ADVISORY IN EFFECT THROUGH EARLY TUESDAY MORNING...

.TODAY...East winds 25 to 30 knots. Seas 5 to 8 feet. Wave
Detail: East 8 feet at 6 seconds and south southwest 3 feet at
12 seconds. 
.TONIGHT...East northeast winds 20 to 25 knots. Seas 5 to 7 feet,
subsiding to 3 to 5 feet after midnight. Wave Detail: East
northeast 6 feet at 6 seconds. 
.TUESDAY...East northeast winds 10 to 15 knots. Seas 3 to 5 feet.
Wave Detail: East 4 feet at 6 seconds. 
.TUESDAY NIGHT...East southeast winds 7 to 10 knots in the
evening, becoming variable less than 10 knots. Seas 3 to 5 feet.
Wave Detail: East southeast 3 feet at 6 seconds. Scattered
showers. 
.WEDNESDAY...East winds 7 to 10 knots. Seas 3 to 5 feet. Wave
Detail: Southeast 3 feet at 6 seconds. Isolated showers in the
morning. 
.WEDNESDAY NIGHT...East winds 10 to 15 knots. Seas 3 to 4 feet.
Wave Detail: Southeast 3 feet at 5 seconds. Isolated showers. 
.THURSDAY...East northeast winds 10 to 15 knots. Seas 3 to
4 feet. Wave Detail: East 3 feet at 5 seconds. Isolated showers
in the morning. 
.FRIDAY...East northeast winds 10 to 15 knots. Seas 3 to 4 feet.
Wave Detail: East 3 feet at 5 seconds. Scattered showers through
the day.  

PHZ121-290215-
Alenuihaha Channel-
358 AM HST Mon Sep 28 2026

...SMALL CRAFT ADVISORY IN EFFECT THROUGH EARLY TUESDAY MORNING...

.TODAY...East northeast winds 25 to 30 knots. Seas 9 to 12 feet,
subsiding to 7 to 10 feet this afternoon. Wave Detail: East
11 feet at 7 seconds and southwest 4 feet at 12 seconds. 
.TONIGHT...East winds 25 to 30 knots. Seas 6 to 9 feet. Wave
Detail: East 7 feet at 6 seconds and south southwest 4 feet at
12 seconds. Isolated showers. 
.TUESDAY...East winds 20 to 25 knots. Seas 5 to 8 feet. Wave
Detail: East 6 feet at 5 seconds and south southwest 4 feet at
16 seconds. Isolated showers in the afternoon. 
.TUESDAY NIGHT...East southeast winds 15 to 20 knots, easing to
10 to 15 knots after midnight. Seas 5 to 8 feet. Wave Detail:
Southeast 5 feet at 5 seconds, west northwest 4 feet at
11 seconds and south southwest 4 feet at 16 seconds. Scattered
showers. 
.WEDNESDAY...East southeast winds 10 to 15 knots, becoming east
15 to 20 knots in the afternoon. Seas 5 to 8 feet. Wave Detail:
Southeast 5 feet at 5 seconds, west northwest 4 feet at
10 seconds and south southwest 4 feet at 15 seconds. Scattered
showers. 
.WEDNESDAY NIGHT...East winds 15 to 20 knots. Seas 5 to 7 feet.
Wave Detail: South southeast 5 feet at 6 seconds and south
southwest 4 feet at 14 seconds. Scattered showers. 
.THURSDAY...East winds 15 to 20 knots. Seas 5 to 7 feet. Wave
Detail: East 4 feet at 5 seconds and south southwest 3 feet at
13 seconds. Scattered showers in the morning. Scattered showers
through the day. 
.FRIDAY...East winds 15 to 20 knots, easing to 10 to 15 knots
after midnight. Seas 4 to 5 feet. Wave Detail: East northeast
4 feet at 5 seconds and south southwest 3 feet at 13 seconds.
Isolated showers.  

PHZ122-290215-
Big Island Windward Waters-
358 AM HST Mon Sep 28 2026

...SMALL CRAFT ADVISORY IN EFFECT THROUGH EARLY TUESDAY MORNING...

.TODAY...East southeast winds 20 to 25 knots. Seas 5 to 7 feet.
Wave Detail: East 5 feet at 5 seconds, south southwest 4 feet at
13 seconds and north northwest 3 feet at 15 seconds. Isolated
showers this afternoon. 
.TONIGHT...East southeast winds 20 to 25 knots. Seas 4 to 5 feet.
Wave Detail: East northeast 4 feet at 4 seconds and south
southwest 3 feet at 12 seconds. Scattered showers. 
.TUESDAY...East southeast winds 20 to 25 knots, easing to 15 to
20 knots in the afternoon. Seas 3 to 5 feet. Wave Detail:
Southeast 4 feet at 4 seconds and south southwest 3 feet at
12 seconds. Isolated showers. 
.TUESDAY NIGHT...East southeast winds 15 to 20 knots. Seas 3 to
4 feet. Wave Detail: Southeast 4 feet at 4 seconds. Isolated
showers. 
.WEDNESDAY...East southeast winds 15 to 20 knots. Seas 3 to
4 feet. Wave Detail: Southeast 4 feet at 4 seconds. 
.WEDNESDAY NIGHT...East southeast winds 10 to 15 knots. Seas 3 to
4 feet. Wave Detail: Southeast 3 feet at 4 seconds. Isolated
showers. 
.THURSDAY...East winds 10 to 15 knots. Seas 3 to 4 feet. Wave
Detail: East southeast 3 feet at 4 seconds. Isolated showers
through the day. 
.FRIDAY...East winds 10 to 15 knots. Seas 3 to 5 feet. Wave
Detail: East 3 feet at 4 seconds. Isolated showers in the
morning. Isolated showers through the day.  

PHZ123-290215-
Big Island Leeward Waters-
358 AM HST Mon Sep 28 2026

...SMALL CRAFT ADVISORY IN EFFECT THROUGH EARLY TUESDAY MORNING...

.TODAY...West of the Big Island, northwest winds 10 to 15 knots,
becoming 7 to 10 knots this afternoon. Near South Point, east
winds 25 to 30 knots. Seas 6 to 9 feet. Wave Detail: East
southeast 8 feet at 6 seconds and south southwest 5 feet at
13 seconds. 
.TONIGHT...West of the Big Island, north winds 7 to 10 knots.
Near South Point, east winds to 25 knots, becoming 20 to 25 knots
after midnight. Seas 5 to 8 feet. Wave Detail: East southeast
6 feet at 6 seconds and south southwest 4 feet at 12 seconds. 
.TUESDAY...West of the Big Island, northwest winds 7 to 10 knots,
becoming southwest 15 to 20 knots in the afternoon. Near South
Point, east southeast winds 20 to 25 knots. Seas 5 to 7 feet.
Wave Detail: Southeast 5 feet at 6 seconds and south southwest
4 feet at 16 seconds. Isolated showers in the afternoon. 
.TUESDAY NIGHT...Winds east northeast winds 10 to 15 knots. Seas
5 to 8 feet. Wave Detail: Southeast 5 feet at 6 seconds, west
northwest 5 feet at 11 seconds and south southwest 4 feet at
16 seconds. Isolated showers. 
.WEDNESDAY...West of the Big Island, southwest winds 15 to
20 knots, rising to 20 to 25 knots in the afternoon. Near
Kawaihae, north northeast winds 7 to 10 knots. Seas 5 to 8 feet.
Wave Detail: West northwest 5 feet at 11 seconds, southeast
4 feet at 5 seconds and south southwest 4 feet at 15 seconds.
Isolated showers. 
.WEDNESDAY NIGHT...West of the Big Island, south southeast winds
15 to 20 knots, easing to 10 to 15 knots after midnight. Near
Kawaihae, east northeast winds 7 to 10 knots. Seas 5 to 8 feet.
Wave Detail: Southeast 5 feet at 5 seconds, south southwest
4 feet at 14 seconds and west northwest 3 feet at 9 seconds.
Scattered showers. 
.THURSDAY...West of the Big Island, north northeast winds 10 to
15 knots, backing to west southwest in the afternoon, backing to
south in the evening, veering to north northwest 7 to 10 knots
after midnight. Near South Point, east winds 15 to 20 knots,
rising to 20 to 25 knots in the afternoon, easing to 15 knots.
Seas 5 to 7 feet. Wave Detail: Southeast 4 feet at 5 seconds,
west northwest 3 feet at 9 seconds and south southwest 3 feet at
13 seconds. Scattered showers in the morning. Isolated showers in
the afternoon, then scattered showers through the day. 
.FRIDAY...West of the Big Island, winds variable less than
10 knots, becoming southwest 7 to 10 knots in the afternoon,
backing to south southeast. Near South Point, east winds to
15 knots, easing to 10 knots. Seas 3 to 5 feet. Wave Detail: East
southeast 3 feet at 4 seconds and south southwest 3 feet at
13 seconds. Isolated showers.  

PHZ124-290215-
Big Island Southeast Waters-
358 AM HST Mon Sep 28 2026

...SMALL CRAFT ADVISORY IN EFFECT THROUGH EARLY TUESDAY MORNING...

.TODAY...East northeast winds 20 to 25 knots. Seas 5 to 7 feet.
Wave Detail: East 5 feet at 5 seconds and south southwest 4 feet
at 13 seconds. Isolated showers this afternoon. 
.TONIGHT...East winds 15 to 20 knots. Seas 4 to 6 feet. Wave
Detail: East 4 feet at 4 seconds and south southwest 3 feet at
12 seconds. Scattered showers. 
.TUESDAY...East winds 10 to 15 knots. Seas 4 to 5 feet. Wave
Detail: East southeast 3 feet at 4 seconds, west northwest 3 feet
at 10 seconds and south southwest 3 feet at 16 seconds. Isolated
showers in the morning, then scattered showers in the afternoon. 
.TUESDAY NIGHT...East winds 10 to 15 knots. Seas 4 to 6 feet.
Wave Detail: West northwest 4 feet at 11 seconds, east southeast
3 feet at 4 seconds and south southwest 3 feet at 16 seconds.
Scattered showers. 
.WEDNESDAY...East winds 10 to 15 knots. Seas 4 to 6 feet. Wave
Detail: West northwest 4 feet at 11 seconds, east 3 feet at
4 seconds and south southwest 3 feet at 15 seconds. Isolated
showers. 
.WEDNESDAY NIGHT...East winds to 15 knots. Seas 3 to 5 feet. Wave
Detail: West northwest 3 feet at 9 seconds and south southwest
3 feet at 14 seconds. Isolated showers. 
.THURSDAY...East winds to 15 knots. Seas 3 to 5 feet. Wave
Detail: East northeast 3 feet at 4 seconds and west northwest
3 feet at 9 seconds. Isolated showers in the morning. Isolated
showers through the day. 
.FRIDAY...East winds 10 to 15 knots. Seas 3 to 5 feet. Wave
Detail: East 3 feet at 4 seconds. Isolated showers in the
morning. Scattered showers through the day.
```

---

### 5. Daily Climate Summary — HNL

| Field | Value |
|---|---|
| **Resource ID** | cli_daily_climate_summary_HNL |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLI&issuedby=HNL |
| **Collected** | 2026-09-27T22:56:38.603695-10:00 HST |

```text
508
CDHW40 PHFO 280227
CLIHNL

CLIMATE REPORT
NATIONAL WEATHER SERVICE HONOLULU HI
427 PM HST SUN SEP 27 2026

...................................

...THE HONOLULU CLIMATE SUMMARY FOR SEPTEMBER 27 2026...
VALID TODAY AS OF 0425 PM LOCAL TIME.

CLIMATE NORMAL PERIOD 1991 TO 2020
CLIMATE RECORD PERIOD 1940 TO 2026

WEATHER ITEM   OBSERVED TIME   RECORD YEAR NORMAL DEPARTURE LAST
                VALUE   (LST)  VALUE       VALUE  FROM      YEAR
                                                  NORMAL
...................................................................
TEMPERATURE (F)
 TODAY
  MAXIMUM         89    154 PM  93    1987  88      1       90
  MINIMUM         79    639 AM  68    1945  75      4       75
                                      1996
  AVERAGE         84                        81      3       83

PRECIPITATION (IN)
  TODAY            0.00          0.29 2000   0.02  -0.02      T
  MONTH TO DATE    0.32                      0.80  -0.48     0.71
  SINCE SEP 1      0.32                      0.80  -0.48     0.71
  SINCE JAN 1     22.35                     10.39  11.96     9.59

DEGREE DAYS
 HEATING
  TODAY            0                         0      0        0
  MONTH TO DATE    0                         0      0        0
  SINCE SEP 1      0                         0      0        0
  SINCE JUL 1      0                         0      0        0

 COOLING
  TODAY           19                        16      3       18
  MONTH TO DATE  491                       449     42      478
  SINCE SEP 1    491                       449     42      478
  SINCE JAN 1   3701                      3526    175     3963
...................................................................

WIND (MPH)
  HIGHEST WIND SPEED    39   HIGHEST WIND DIRECTION     E (70)
  HIGHEST GUST SPEED    53   HIGHEST GUST DIRECTION     E (70)
  AVERAGE WIND SPEED    22.9

SKY COVER
  POSSIBLE SUNSHINE  MM
  AVERAGE SKY COVER 0.3

WEATHER CONDITIONS
THE FOLLOWING WEATHER WAS RECORDED TODAY.
  NO SIGNIFICANT WEATHER WAS OBSERVED.

RELATIVE HUMIDITY (PERCENT)
 HIGHEST    65           600 AM
 LOWEST     47           100 PM
 AVERAGE    56

..........................................................

THE HONOLULU CLIMATE NORMALS FOR TOMORROW
                         NORMAL    RECORD    YEAR
 MAXIMUM TEMPERATURE (F)   88        91      1988
                                             1995
                                             1997
 MINIMUM TEMPERATURE (F)   75        68      1945

SUNRISE AND SUNSET
SEPTEMBER 27 2026.....SUNRISE   622 AM HST   SUNSET   623 PM HST
SEPTEMBER 28 2026.....SUNRISE   622 AM HST   SUNSET   622 PM HST

-  INDICATES NEGATIVE NUMBERS.
R  INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T  INDICATES TRACE AMOUNT.
```

---

### 6. Daily Climate Summary — ITO

| Field | Value |
|---|---|
| **Resource ID** | cli_daily_climate_summary_ITO |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLI&issuedby=ITO |
| **Collected** | 2026-09-27T22:59:09.092780-10:00 HST |

```text
524
CDHW43 PHFO 280227
CLIITO

CLIMATE REPORT
NATIONAL WEATHER SERVICE HONOLULU HI
427 PM HST SUN SEP 27 2026

...................................

...THE HILO/GEN.LYMAN FLD CLIMATE SUMMARY FOR SEPTEMBER 27 2026...
VALID TODAY AS OF 0425 PM LOCAL TIME.

CLIMATE NORMAL PERIOD 1991 TO 2020
CLIMATE RECORD PERIOD 1949 TO 2026

WEATHER ITEM   OBSERVED TIME   RECORD YEAR NORMAL DEPARTURE LAST
                VALUE   (LST)  VALUE       VALUE  FROM      YEAR
                                                  NORMAL
...................................................................
TEMPERATURE (F)
 TODAY
  MAXIMUM         83    359 PM  92    2019  83      0       84
  MINIMUM         71    539 AM  64    1950  70      1       71
  AVERAGE         77                        76      1       78

PRECIPITATION (IN)
  TODAY            1.49          5.82 1960   0.30   1.19     0.00
  MONTH TO DATE   16.18                      7.82   8.36     2.73
  SINCE SEP 1     16.18                      7.82   8.36     2.73
  SINCE JAN 1    124.42                     82.81  41.61    38.11

DEGREE DAYS
 HEATING
  TODAY            0                         0      0        0
  MONTH TO DATE    0                         0      0        0
  SINCE SEP 1      0                         0      0        0
  SINCE JUL 1      0                         0      0        0

 COOLING
  TODAY           12                        11      1       13
  MONTH TO DATE  355                       323     32      342
  SINCE SEP 1    355                       323     32      342
  SINCE JAN 1   2784                      2434    350     2843
...................................................................

WIND (MPH)
  HIGHEST WIND SPEED    15   HIGHEST WIND DIRECTION     E (90)
  HIGHEST GUST SPEED    20   HIGHEST GUST DIRECTION    SE (120)
  AVERAGE WIND SPEED     6.6

SKY COVER
  POSSIBLE SUNSHINE  MM
  AVERAGE SKY COVER 0.9

WEATHER CONDITIONS
THE FOLLOWING WEATHER WAS RECORDED TODAY.
  HEAVY RAIN
  RAIN
  LIGHT RAIN
  FOG

RELATIVE HUMIDITY (PERCENT)
 HIGHEST    97           200 AM
 LOWEST     63           300 PM
 AVERAGE    80

..........................................................

THE HILO/GEN.LYMAN FLD CLIMATE NORMALS FOR TOMORROW
                         NORMAL    RECORD    YEAR
 MAXIMUM TEMPERATURE (F)   83        90      2019
 MINIMUM TEMPERATURE (F)   70        64      1956

SUNRISE AND SUNSET
SEPTEMBER 27 2026.....SUNRISE   610 AM HST   SUNSET   612 PM HST
SEPTEMBER 28 2026.....SUNRISE   610 AM HST   SUNSET   611 PM HST

-  INDICATES NEGATIVE NUMBERS.
R  INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T  INDICATES TRACE AMOUNT.
```

---

### 7. Daily Climate Summary — LIH

| Field | Value |
|---|---|
| **Resource ID** | cli_daily_climate_summary_LIH |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLI&issuedby=LIH |
| **Collected** | 2026-09-27T22:57:38.472615-10:00 HST |

```text
540
CDHW41 PHFO 280227
CLILIH

CLIMATE REPORT
NATIONAL WEATHER SERVICE HONOLULU HI
427 PM HST SUN SEP 27 2026

...................................

...THE LIHUE CLIMATE SUMMARY FOR SEPTEMBER 27 2026...
VALID TODAY AS OF 0425 PM LOCAL TIME.

CLIMATE NORMAL PERIOD 1991 TO 2020
CLIMATE RECORD PERIOD 1950 TO 2026

WEATHER ITEM   OBSERVED TIME   RECORD YEAR NORMAL DEPARTURE LAST
                VALUE   (LST)  VALUE       VALUE  FROM      YEAR
                                                  NORMAL
...................................................................
TEMPERATURE (F)
 TODAY
  MAXIMUM         85    139 PM  88    1981  85      0       84
                                      2017
  MINIMUM         77    657 AM  66    1977  75      2       70
  AVERAGE         81                        80      1       77

PRECIPITATION (IN)
  TODAY            0.01          0.79 1987   0.07  -0.06     0.00
  MONTH TO DATE    3.12                      1.93   1.19     3.49
  SINCE SEP 1      3.12                      1.93   1.19     3.49
  SINCE JAN 1     42.91                     24.03  18.88    14.95

DEGREE DAYS
 HEATING
  TODAY            0                         0      0        0
  MONTH TO DATE    0                         0      0        0
  SINCE SEP 1      0                         0      0        0
  SINCE JUL 1      0                         0      0        0

 COOLING
  TODAY           16                        15      1       12
  MONTH TO DATE  408                       405      3      416
  SINCE SEP 1    408                       405      3      416
  SINCE JAN 1   3111                      3039     72     3354
...................................................................

WIND (MPH)
  HIGHEST WIND SPEED    29   HIGHEST WIND DIRECTION     E (70)
  HIGHEST GUST SPEED    38   HIGHEST GUST DIRECTION    NE (60)
  AVERAGE WIND SPEED    22.6

SKY COVER
  POSSIBLE SUNSHINE  MM
  AVERAGE SKY COVER 0.6

WEATHER CONDITIONS
THE FOLLOWING WEATHER WAS RECORDED TODAY.
  LIGHT RAIN

RELATIVE HUMIDITY (PERCENT)
 HIGHEST    84           600 AM
 LOWEST     63          1200 PM
 AVERAGE    74

..........................................................

THE LIHUE CLIMATE NORMALS FOR TOMORROW
                         NORMAL    RECORD    YEAR
 MAXIMUM TEMPERATURE (F)   85        89      1981
                                             2019
 MINIMUM TEMPERATURE (F)   75        66      1958
                                             1970

SUNRISE AND SUNSET
SEPTEMBER 27 2026.....SUNRISE   628 AM HST   SUNSET   628 PM HST
SEPTEMBER 28 2026.....SUNRISE   628 AM HST   SUNSET   628 PM HST

-  INDICATES NEGATIVE NUMBERS.
R  INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T  INDICATES TRACE AMOUNT.
```

---

### 8. Daily Climate Summary — OGG

| Field | Value |
|---|---|
| **Resource ID** | cli_daily_climate_summary_OGG |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLI&issuedby=OGG |
| **Collected** | 2026-09-27T22:58:39.185287-10:00 HST |

```text
556
CDHW42 PHFO 280227
CLIOGG

CLIMATE REPORT
NATIONAL WEATHER SERVICE HONOLULU HI
427 PM HST SUN SEP 27 2026

...................................

...THE KAHULUI/MAUI CLIMATE SUMMARY FOR SEPTEMBER 27 2026...
VALID TODAY AS OF 0425 PM LOCAL TIME.

CLIMATE NORMAL PERIOD 1991 TO 2020
CLIMATE RECORD PERIOD 1954 TO 2026

WEATHER ITEM   OBSERVED TIME   RECORD YEAR NORMAL DEPARTURE LAST
                VALUE   (LST)  VALUE       VALUE  FROM      YEAR
                                                  NORMAL
...................................................................
TEMPERATURE (F)
 TODAY
  MAXIMUM         89    228 PM  93    1972  90     -1       89
                                      1984
                                      2020
  MINIMUM         75    206 AM  60    1975  71      4       73
  AVERAGE         82                        80      2       81

PRECIPITATION (IN)
  TODAY            0.00          0.54 2000   0.02  -0.02     0.00
  MONTH TO DATE    0.60                      0.41   0.19     0.04
  SINCE SEP 1      0.60                      0.41   0.19     0.04
  SINCE JAN 1     30.28                     10.73  19.55     6.61

DEGREE DAYS
 HEATING
  TODAY            0                         0      0        0
  MONTH TO DATE    0                         0      0        0
  SINCE SEP 1      0                         0      0        0
  SINCE JUL 1      0                         0      0        0

 COOLING
  TODAY           17                        15      2       16
  MONTH TO DATE  440                       427     13      425
  SINCE SEP 1    440                       427     13      425
  SINCE JAN 1   3224                      3274    -50     3280
...................................................................

WIND (MPH)
  HIGHEST WIND SPEED    38   HIGHEST WIND DIRECTION     E (70)
  HIGHEST GUST SPEED    58   HIGHEST GUST DIRECTION     E (70)
  AVERAGE WIND SPEED    25.0

SKY COVER
  POSSIBLE SUNSHINE  MM
  AVERAGE SKY COVER 0.3

WEATHER CONDITIONS
THE FOLLOWING WEATHER WAS RECORDED TODAY.
  NO SIGNIFICANT WEATHER WAS OBSERVED.

RELATIVE HUMIDITY (PERCENT)
 HIGHEST    79           100 AM
 LOWEST     39           200 PM
 AVERAGE    59

..........................................................

THE KAHULUI/MAUI CLIMATE NORMALS FOR TOMORROW
                         NORMAL    RECORD    YEAR
 MAXIMUM TEMPERATURE (F)   90        93      2019
 MINIMUM TEMPERATURE (F)   71        63      1965
                                             2010

SUNRISE AND SUNSET
SEPTEMBER 27 2026.....SUNRISE   616 AM HST   SUNSET   617 PM HST
SEPTEMBER 28 2026.....SUNRISE   616 AM HST   SUNSET   616 PM HST

-  INDICATES NEGATIVE NUMBERS.
R  INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T  INDICATES TRACE AMOUNT.
```

---

### 9. Hawaii Rainfall Summary direct product

| Field | Value |
|---|---|
| **Resource ID** | hfo_rra_direct |
| **Official source** | https://forecast.weather.gov/product.php?issuedby=HFO&product=RRA&site=hfo |
| **Collected** | 2026-09-28T05:09:34.209613-10:00 HST |

```text
689
SRHW80 PHFO 281446
RRAHFO

Hawaii Rainfall Summary
National Weather Service Honolulu HI
445 AM HST Mon Sep 28 2026

:
.B HFO  0928 H  DH04 /DRH-03/PPT/DRH-06/PPQ/DRH-12/PPK/DRH-24/PPD
:
:Automated rain gage reports from around the State of Hawaii.
:These are provisional reports that have not been quality
:controlled.
:
:T=Trace Rainfall, M=Missing Data
:
:Precipitation totals ending  4 AM HST
:
:Island of Kauai                                   Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
:       Windward/Mauka Sites
MKAH1 : Makaha Ridge (RAWS)         :    0.00  /  0.00  /  0.00  /  0.00
PLRH1 : Puu Lua (RAWS)              :    0.00  /  0.00  /  0.00  /  0.00
WKRH1 : Waiakoali (USGS)            :    0.00  /  0.00  /  0.00  /  0.00
KLOH1 : Kilohana (USGS)             :    0.01  /  0.03  /  0.10  /  0.14
MCRH1 : Mohihi Crossing (USGS)      :    0.01  /  0.03  /  0.03  /  0.04
WLGH1 : Waialae (USGS)              :    0.07  /  0.10  /  0.10  /  0.10
LLMH1 : Lower Limahuli (UHM)        :    0.03  /  0.06  /  0.07  /  0.10
WNHH1 : Wainiha (12010)             :    0.05  /  0.05  /  0.07  /  0.07
WIPH1 : Waipa (UHM)                 :    0.03  /  0.05  /  0.09  /  0.17
HNIH1 : Hanalei (12009)             :    0.06  /  0.08  /  0.12  /  0.20
WLLH1 : Mount Waialeale (USGS)      :      M   /    M   /    M   /    M
PRIH1 : Princeville Airport (12011) :    0.01  /  0.02  /  0.03  /  0.03
CMGH1 : Common Ground (UHM)         :    0.02  /  0.04  /  0.05  /  0.09
HLIH1 : Hanalei (RAWS)              :    0.05  /  0.07  /  0.08  /  0.17
MLDH1 : Moloaa Dairy (RAWS)         :    0.00  /  0.00  /  0.00  /  0.00
ANHH1 : Anahola (12001)             :      M   /    M   /  0.00  /  0.01
KPIH1 : Kapahi (12003)              :    0.03  /  0.03  /  0.06  /  0.06
WLDH1 : N Wailua Ditch (USGS)       :    0.09  /  0.13  /  0.13  /  0.14
WUHH1 : Wailua (12005)              :    0.04  /  0.04  /  0.04  /  0.04
WIRH1 : Waiahi Rain Gage (USGS)     :    0.02  /  0.05  /  0.05  /  0.15
LIHH1 : Lihue Var. Stn. (12006)     :    0.00  /  0.03  /  0.03  /  0.06
HNMH1 : Hanamaulu (UHM)             :    0.01  /  0.09  /  0.09  /  0.23
HLI   : Lihue Airport (ASOS)        :      T   /    T   /  0.01  /  0.02
:       Leeward Sites
OMAH1 : Omao (12004)                :    0.00  /  0.00  /  0.00  /  0.01
LNTH1 : Lawai NTBG (UHM)            :    0.02  /  0.02  /  0.02  /  0.05
KHEH1 : Kalaheo (12008)             :    0.02  /  0.02  /  0.02  /  0.05
PAKH1 : Port Allen (HSOIS)          :    0.00  /  0.00  /  0.00  /  0.00
HNPH1 : Hanapepe (12002)            :    0.00  /  0.00  /  0.00  /  0.00
POPH1 : Puu Opae (RAWS)             :    0.00  /  0.00  /  0.00  /  0.00
WHGH1 : Waimea Heights (RAWS)       :    0.00  /  0.00  /  0.00  /  0.00
WMTH1 : Waimea Tank (12007)         :    0.00  /  0.00  /  0.00  /  0.00
MNRH1 : Mana (RAWS)                 :    0.00  /  0.00  /  0.00  /  0.00
:
:Island of Oahu                                    Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
:       Windward/Mauka Sites
KAHH1 : Kahuku (13027)              :    0.00  /  0.00  /  0.00  /  0.00
KTAH1 : Kahuku Training Area (RAWS) :    0.00  /  0.00  /  0.00  /  0.00
KFWH1 : Kii (RAWS)                  :    0.00  /  0.00  /  0.00  /  0.00
PUNH1 : Punaluu Pump (13013)        :    0.00  /  0.00  /  0.00  /  0.01
PNSH1 : Punaluu Stream (USGS)       :    0.01  /  0.02  /  0.02  /  0.02
KNRH1 : Kahana (USGS)               :    0.01  /  0.03  /  0.03  /  0.03
HAKH1 : Hakipuu Mauka (13004)       :    0.00  /  0.00  /  0.00  /  0.00
WPPH1 : Waihee Pump (13002)         :    0.00  /  0.00  /  0.00  /  0.05
WHSH1 : Waiahole (USGS)             :    0.00  /  0.00  /  0.00  /  0.00
OFRH1 : Oahu Forest NWR (USFWS)     :    0.00  /  0.00  /  0.00  /  0.00
AHUH1 : Ahuimanu Loop (13005)       :    0.00  /  0.00  /  0.00  /  0.00
HRRH1 : Heeia NERR (NOAA/NOS)       :    0.00  /  0.00  /  0.00  /  0.00
LULH1 : Luluku (13016)              :    0.00  /  0.00  /  0.00  /  0.00
NRSH1 : Nuuanu Res No. 1 (UHM)      :    0.00  /  0.00  /  0.00  /  0.00
KWIH1 : Kalawahine (UHM)            :    0.00  /  0.00  /  0.00  /  0.06
LYOH1 : Lyon (UHM)                  :    0.00  /  0.01  /  0.02  /  0.03
MNLH1 : Manoa Lyon Arboretum (13023):    0.00  /  0.00  /  0.00  /  0.02
STVH1 : St. Stephens (13006)        :    0.00  /  0.00  /  0.00  /  0.01
MAUH1 : Maunawili (13008)           :      M   /    M   /    M   /    M
OFSH1 : Olomana Fire Station (13009):    0.00  /  0.00  /  0.00  /  0.00
WMLH1 : Waimanalo (13011)           :    0.00  /  0.00  /  0.00  /  0.00
BELH1 : Bellows AFS (HSOIS)         :    0.00  /  0.00  /  0.00  /  0.00
KMHH1 : Kamehame (13012)            :    0.00  /  0.00  /  0.00  /  0.01
HAJH1 : Hawaii Kai Golf Crse (13015):    0.00  /  0.00  /  0.00  /  0.00
:       Leeward/Central Sites
KUXH1 : Kaluanui (UHM)              :    0.00  /  0.00  /  0.00  /  0.00
NIUH1 : Niu Valley (13001)          :    0.00  /  0.00  /  0.00  /  0.00
PFSH1 : Palolo Fire Station (13010) :    0.00  /  0.00  /  0.00  /  0.00
HNL   : Honolulu Airport (ASOS)             See note at bottom  :
MOAH1 : Moanalua (13003)            :    0.00  /  0.00  /  0.00  /  0.00
MOGH1 : Moanalua RG (USGS)          :    0.00  /  0.00  /  0.00  /  0.00
TNLH1 : Tunnel RG (USGS)            :    0.00  /  0.00  /  0.00  /  0.00
PACH1 : Palisades (13020)           :    0.00  /  0.00  /  0.00  /  0.00
WAWH1 : Waiawa C.F. (13025)         :    0.00  /  0.00  /  0.00  /  0.00
MITH1 : Mililani (13022)            :    0.00  /  0.00  /  0.00  /  0.00
SCBH1 : Schofield Barracks (RAWS)   :    0.00  /  0.00  /  0.00  /  0.00
SCEH1 : Schofield East (RAWS)       :    0.00  /  0.00  /  0.00  /  0.00
WAFH1 : Wheeler Airfield            :    0.00  /  0.00  /  0.00  /  0.00
POAH1 : Poamoho (13018)             :    0.00  /  0.00  /  0.00  /  0.00
KRGH1 : Kalahee Ridge (UHM)         :    0.00  /  0.00  /  0.00  /  0.00
KMRH1 : Kamananui Stream (USGS)     :    0.00  /  0.00  /  0.00  /  0.02
PPRH1 : Pupukea Road (USGS)         :    0.00  /  0.00  /  0.00  /  0.01
PMHH1 : Poamoho RG 1 (USGS)         :    0.01  /  0.02  /  0.03  /  0.03
DLGH1 : Dillingham (RAWS)           :    0.00  /  0.00  /  0.00  /  0.00
AALH1 : Kaala (UHM)                 :    0.00  /  0.00  /  0.00  /  0.00
PECH1 : Waipio (13019)              :    0.00  /  0.00  /  0.00  /  0.00
KUNH1 : Kunia Substation (13021)    :    0.00  /  0.00  /  0.00  /  0.00
HOFH1 : Honouliuli (RAWS)           :    0.00  /  0.00  /  0.00  /  0.00
PTWH1 : Ewa Beach USGS (13024)      :    0.00  /  0.00  /  0.00  /  0.00
HJR   : Kalaeloa Airport (ASOS)             See note at bottom  :
PLHH1 : Palehua (RAWS)              :    0.00  /  0.00  /  0.00  /  0.00
LUAH1 : Lualualei (13017)           :    0.00  /  0.00  /  0.00  /  0.00
WNVH1 : Waianae Valley (RAWS)       :    0.00  /  0.00  /  0.00  /  0.00
WBHH1 : Waianae Boat Harbor (HSOIS) :    0.00  /  0.00  /  0.00  /  0.00
WAIH1 : Waianae (13014)             :      M   /    M   /    M   /    M
MKHH1 : Makaha Stream (USGS)        :    0.00  /  0.00  /  0.00  /  0.00
MKRH1 : Makua Range (RAWS)          :    0.00  /  0.00  /  0.00  /  0.00
KKRH1 : Kuaokala (RAWS)             :    0.00  /  0.00  /  0.00  /  0.00
:
:Island of Molokai                                 Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
KOPH1 : Keopukaloa (UHM)            :    0.00  /  0.00  /  0.00  /  0.00
HOMH1 : Honolimaloo (UHM)           :    0.00  /  0.00  /  0.00  /  0.00
KMLH1 : Kamalo (14013)              :    0.00  /  0.00  /  0.00  /  0.00
MKPH1 : Makapulapai (RAWS)          :    0.00  /  0.00  /  0.00  /  0.00
PAFH1 : Puu Alii (RAWS)             :    0.00  /  0.00  /  0.00  /  0.00
MLKH1 : Molokai 1 (RAWS)            :      M   /    M   /    M   /    M
KACH1 : Kaunakakai Mauka (14004)    :    0.00  /  0.00  /  0.00  /  0.00
HMK   : Molokai Airport (ASOS)      :    0.00  /  0.00  /  0.00  /  0.00
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
WWKH1 : West Wailuaiki (USGS)       :    0.00  /  0.00  /  0.00  /  0.21
EBYH1 : EMI Baseyard (UHM)          :    0.00  /  0.00  /  0.00  /  0.02
AIKH1 : Haiku (14001)               :    0.00  /  0.00  /  0.00  /  0.00
HOG   : Kahului Airport (ASOS)      :    0.00  /  0.00  /  0.00  /  0.00
WUKH1 : Wailuku (14007)             :    0.00  /  0.00  /  0.00  /  0.00
KHKH1 : Kahakuloa (14002)           :    0.00  /  0.00  /  0.00  /  0.00
PKKH1 : Puu Kukui (USGS)            :    0.00  /  0.02  /  0.06  /  0.15
:       Leeward/Upcountry Sites
NKUH1 : Na Kula (RAWS)              :    0.00  /  0.00  /  0.00  /  0.00
KPNH1 : Kepuni (USGS)               :    0.00  /  0.00  /  0.00  /  0.00
PILH1 : Piiholo (UHM)               :    0.00  /  0.00  /  0.00  /  0.02
WKTH1 : Waikamoi Treeline (UHM)     :    0.00  /  0.00  /  0.00  /  0.02
PUKH1 : Pukalani (14006)            :    0.00  /  0.00  /  0.00  /  0.00
KBSH1 : Kula Branch Station (14008) :      M   /    M   /    M   /    M
KLGH1 : Kula Ag (UHM)               :    0.00  /  0.00  /  0.00  /  0.00
PHQH1 : Park HQ (UHM)               :    0.00  /  0.00  /  0.00  /  0.00
NNEH1 : Nene Nest (UHM)             :    0.00  /  0.00  /  0.00  /  0.00
SUMH1 : Summit (UHM)                :    0.00  /  0.00  /  0.00  /  0.00
KLFH1 : Kula 1 (RAWS)               :    0.00  /  0.00  /  0.00  /  0.00
KKNH1 : Kahikinui 1 (RAWS)          :    0.00  /  0.00  /  0.00  /  0.00
KMEH1 : Kamehamenui 1 (RAWS)        :    0.00  /  0.00  /  0.00  /  0.00
KKEH1 : Keokea (UHM)                :    0.00  /  0.00  /  0.00  /  0.00
ULUH1 : Ulupalakua (14003)          :    0.00  /  0.00  /  0.00  /  0.00
LPOH1 : Lipoa (UHM)                 :    0.00  /  0.00  /  0.00  /  0.00
KHIH1 : Kihei #2 (14009)            :      M   /    M   /    M   /  0.00
KPDH1 : Kealia Pond (USFWS)         :    0.00  /  0.00  /  0.00  /  0.00
WCCH1 : Waikapu Country Club (14005):    0.00  /  0.00  /  0.00  /  0.00
HULH1 : Hanaula (UHM)               :    0.00  /  0.00  /  0.00  /  0.00
OLUH1 : Olowalu (UHM)               :    0.00  /  0.00  /  0.00  /  0.00
LAHH1 : Lahainaluna (14011)         :    0.00  /  0.00  /  0.00  /  0.00
LWTH1 : Lahaina WTP (UHM)           :    0.00  /  0.00  /  0.00  /  0.00
HOOH1 : Honolua (UHM)               :    0.00  /  0.00  /  0.00  /  0.00
:
:Island of Hawaii                                  Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
:       Windward Sites
UPLH1 : Upolu Airport (HSOIS)       :    0.00  /  0.00  /  0.00  /  0.01
KMMH1 : Kaluamakani (UHM)           :    0.00  /  0.00  /  0.00  /  0.00
KWSH1 : Kawainui Stream (USGS)      :    0.00  /  0.00  /  0.00  /  0.27
KUUH1 : Kamuela Upper (15002)       :    0.00  /  0.00  /  0.00  /  0.02
KMUH1 : Kamuela (15005)             :    0.00  /  0.00  /  0.00  /  0.01
HNKH1 : Honokaa (15010)             :    0.00  /  0.00  /  0.00  /  0.01
PMLH1 : Puu Mali (RAWS)             :    0.00  /  0.00  /  0.00  /  0.00
WPNH1 : Waipunalei (UHM)            :      M   /    M   /    M   /  0.03
KNKH1 : Kanakaleonui (UHM)          :    0.00  /  0.00  /  0.00  /  0.08
LPHH1 : Laupahoehoe PD (15001)      :    0.00  /  0.00  /  0.00  /  0.07
LAUH1 : Laupahoehoe (UHM)           :      M   /    M   /    M   /  0.43
SPNH1 : Spencer (UHM)               :      M   /    M   /    M   /  0.05
HKUH1 : Hakalau (RAWS)              :    0.00  /  0.00  /  0.00  /  0.25
KLXH1 : Kulaimano (UHM)             :    0.00  /  0.00  /  0.00  /  0.11
NLIH1 : Honolii Stream (USGS)       :    0.00  /  0.00  /  0.00  /  0.87
SDQH1 : Saddle Quarry (USGS)        :    0.00  /  0.00  /  0.01  /  0.97
PIOH1 : Piihonua (UHM)              :    0.00  /  0.00  /  0.00  /  0.82
PIIH1 : Piihonua (15016)            :    0.00  /  0.00  /  0.01  /  0.02
IPIH1 : IPIF (UHM)                  :    0.00  /  0.00  /  0.00  /  0.24
WKAH1 : Waiakea Uka (15017)         :    0.00  /  0.00  /  0.00  /  0.28
WEXH1 : Waiakea Exp Stn (NOAA/CRN)  :    0.00  /  0.00  /  0.00  /  0.13
HTO   : Hilo Airport (ASOS)         :    0.00  /  0.00  /  0.00  /  0.51
PHAH1 : Pahoa (15015)               :    0.00  /  0.00  /  0.00  /  0.13
PAOH1 : Pahoa (UHM)                 :    0.00  /  0.00  /  0.00  /  0.03
MTVH1 : Mountain View (15014)       :    0.00  /  0.00  /  0.00  /  0.37
GLNH1 : Glenwood (15013)            :    0.00  /  0.00  /  0.00  /  0.84
:       Leeward Sites
MOBH1 : Mauna Loa Ob Stn (NOAA/CRN) :    0.00  /  0.00  /  0.00  /  0.00
NHKH1 : Nahuku (UHM)                :    0.00  /  0.00  /  0.00  /  0.53
KKUH1 : Keaumo (RAWS)               :    0.00  /  0.00  /  0.00  /  0.04
KMOH1 : Kealakomo (RAWS)            :    0.00  /  0.00  /  0.00  /  0.10
PLIH1 : Pali 2 (RAWS)               :    0.00  /  0.00  /  0.00  /  0.01
KPRH1 : Kapapala (RAWS)             :    0.00  /  0.00  /  0.00  /  0.03
KAYH1 : Kapapala Ranch (15003)      :    0.00  /  0.00  /  0.00  /  0.04
PPLH1 : Pahala (15004)              :    0.00  /  0.00  /  0.00  /  0.00
KIOH1 : Kaiholena (UHM)             :      M   /    M   /    M   /    M
NENH1 : Nene Cabin (RAWS)           :    0.00  /  0.00  /  0.00  /  0.05
SOPH1 : South Point (HSOIS)         :    0.00  /  0.00  /  0.00  /  0.65
LKHH1 : Lower Kahuku (RAWS)         :    0.00  /  0.00  /  0.01  /  0.26
KRCH1 : Kahuku Ranch (RAWS)         :    0.00  /  0.00  /  0.00  /  0.01
KOMH1 : Kona Hema (UHM)             :    0.00  /  0.00  /  0.00  /  0.03
PHRH1 : Puho CS (RAWS)              :    0.16  /  0.16  /  0.17  /  0.17
HAUH1 : Honaunau (15007)            :    0.00  /  0.03  /  0.70  /  0.73
KLEH1 : Kealakekua (15008)          :    0.00  /  0.07  /  0.13  /  0.13
WIHH1 : Waiaha Stream (15009)       :    0.01  /  0.06  /  0.46  /  0.47
KOUH1 : Keahuolu (UHM)              :    0.01  /  0.15  /  0.51  /  0.72
KHOH1 : Kaloko-Honokohau (RAWS)     :    0.00  /  0.00  /  0.00  /  0.00
HKO   : Kona Intl Airport (ASOS)    :    0.00  /  0.00  /  0.00  /  0.00
PLMH1 : Palamanui (UHM)             :    0.00  /  0.00  /  0.06  /  0.07
KIRH1 : Kiholo RG (USGS)            :    0.00  /  0.03  /  0.03  /  0.03
KPLH1 : Kaupulehu (RAWS)            :    0.00  /  0.08  /  0.08  /  0.08
PULH1 : Puuanahulu (RAWS)           :    0.00  /  0.00  /  0.00  /  0.00
MMLH1 : Mamalahoa (UHM)             :    0.00  /  0.00  /  0.00  /  0.00
PWWH1 : Puu Waawaa (RAWS)           :    0.00  /  0.00  /  0.00  /  0.00
PWAH1 : Puu Waawaa (UHM)            :    0.00  /  0.00  /  0.00  /  0.01
KIUH1 : Kaiaulu Puu Waawaa (UHM)    :    0.00  /  0.00  /  0.00  /  0.00
PKAH1 : Pohakuloa Kipuka Alala RAWS :    0.00  /  0.00  /  0.00  /  0.00
PTRH1 : Pohakuloa Range 17 (RAWS)   :    0.00  /  0.00  /  0.00  /  0.00
PKWH1 : Pohakuloa West (RAWS)       :    0.00  /  0.00  /  0.00  /  0.00
PKMH1 : Pohakuloa Keamuku (RAWS)    :    0.00  /  0.00  /  0.00  /  0.00
AHMH1 : Ahumoa (RAWS)               :    0.00  /  0.00  /  0.00  /  0.00
WHIH1 : Waikii (15011)              :    0.00  /  0.00  /  0.00  /  0.00
LLAH1 : Lalamilo (UHM)              :    0.00  /  0.00  /  0.00  /  0.00
WKVH1 : Waikoloa (RAWS)             :    0.00  /  0.00  /  0.00  /  0.00
PERH1 : Puhe CS (RAWS)              :    0.00  /  0.00  /  0.00  /  0.00
KHRH1 : Kohala Ranch (RAWS)         :    0.00  /  0.00  /  0.00  /  0.00
KASH1 : Kahua Ranch (15006)         :    0.00  /  0.00  /  0.00  /  0.05
KEHH1 : Kehena (UHM)                :    0.00  /  0.00  /  0.00  /  0.12
PLAH1 : Puuloa (UHM)                :    0.00  /  0.00  /  0.00  /  0.01
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
| **Collected** | 2026-09-28T05:18:39.185214-10:00 HST |

```text
                        
522
SXHW80 PHFO 280115
OMRHFO

SURF OBSERVATIONS
NATIONAL WEATHER SERVICE HONOLULU HI
315 PM HST SUN SEP 27 2026

FULL FACE SURF OBSERVATIONS ARE TAKEN BY COUNTY LIFE GUARDS AND
COOPERATIVE OBSERVERS AND RELAYED TO THE NATIONAL WEATHER SERVICE
FOR DISSEMINATION. THESE OBSERVATIONS ARE NOT QUALITY CONTROLLED.

HIZ003-004-029>031-280100-
KAUAI-

LOCATION        TIME   SURF HEIGHT DIR   PER                  REMARKS
KEE
HAENA        1200 PM           4-5  NE    10
HANALEI      1200 PM           2-4  NE    10
ANAHOLA      1000 AM           4-6   E    12
KEALIA       1000 AM           6-8   E    12
LYDGATE      1000 AM           4-7   E    12
POIPU        1000 AM           6-8  SE     8
SALT POND    1000 AM           6-8   S     8
KEKAHA       1000 AM           6-8   S     8
$$

HIZ006-007-009>011-032>036-280100-
OAHU-

LOCATION        TIME   SURF HEIGHT DIR PER         WIND      REMARKS
DIAMOND HEAD
SUNSET
WAIKIKI      1000 AM           4-5                            CANOES
SANDY BEACH  1000 AM           6-8                       SHORE BREAK
MAKAPUU      1000 AM          8-12
EHUKAI       1000 AM           1-2
MAKAHA       1000 AM           1-2
$$

HIZ015>018-022-045>050-280100-
MAUI-MOLOKAI-LANAI-KAHOOLAWE-

LOCATION        TIME   SURF HEIGHT   DIR         WIND      REMARKS
KANAHA       1045 AM           0-1    NE      E 15-25
BALDWIN SHOR 1045 AM           0-1     E         E 25
BALDWIN OUTE 1045 AM           2-3     E
HOOKIPA
KAMAOLE I
KAMAOLE III
HANAKAOO
FLEMING
$$

HIZ023-026>028-051>054-280100-
BIG ISLAND OF HAWAII-

LOCATION        TIME   SURF HEIGHT   DIR         WIND      REMARKS
RICHARDSONS  1045 AM           3-4    NE         NE 5      -DZ OVC
HONOLII
PUNALU`U
ISAAC HALE   1045 AM           5-7     E      E 10-20        SUNNY
HAPUNA
KAHALUU      1045 AM           3-5     S        VRB 5          P/C
MAGIC SANDS  1045 AM           2-3    SW         SW 7        SUNNY
KUA BAY
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
| **Collected** | 2026-09-27T23:54:05.017256-10:00 HST |

```text
210
FZPN40 PHFO 280933
HSFNP

HIGH SEAS FORECAST
NATIONAL WEATHER SERVICE HONOLULU HI
1100 UTC MON SEP 28 2026

SUPERSEDED BY NEXT ISSUANCE IN 6 HOURS

SEAS GIVEN AS SIGNIFICANT WAVE HEIGHT...WHICH IS THE AVERAGE HEIGHT
OF THE HIGHEST 1/3 OF THE WAVES. INDIVIDUAL WAVES MAY BE MORE THAN
TWICE THE SIGNIFICANT WAVE HEIGHT.

THIS HIGH SEAS FORECAST USES 1-MINUTE AVERAGE WINDS WHICH MAY BE
HIGHER THAN 10-MINUTE AVERAGE WINDS.

SECURITE

NORTH PACIFIC EQUATOR TO 30N BETWEEN 140W AND 180W

SYNOPSIS VALID 0600 UTC SEP 28 2026.
24 HOUR FORECAST VALID 0600 UTC SEP 29 2026.
48 HOUR FORECAST VALID 0600 UTC SEP 30 2026.

.WARNINGS.

...HURRICANE WARNING...
.HURRICANE NOLO NEAR 16.5N 161.3W 929 MB AT 0900 UTC SEP 28
MOVING WNW OR 290 DEG AT 10 KT. MAXIMUM SUSTAINED WINDS 135 KT
GUSTS 165 KT. TROPICAL STORM FORCE WINDS WITHIN 130 NM NE
QUADRANT...100 NM SE QUADRANT...80 NM SW QUADRANT AND 110 NM
NW QUADRANT. WINDS 20 TO 30 KT ELSEWHERE FROM 15N TO 21N BETWEEN
154W AND 166W. SEAS 4 M OR GREATER WITHIN 360 NM NE QUADRANT...
150 NM SE QUADRANT...180 NM SW QUADRANT AND 330 NM NW QUADRANT
WITH SEAS TO 10 M. SEAS 2.5 TO 3.5 M ELSEWHERE N OF 10N BETWEEN
153W AND 175W. SCATTERED TO NUMEROUS MODERATE TSTMS WITHIN 85 NM
FROM CENTER.
.24 HOUR FORECAST HURRICANE NOLO NEAR 19.2N 163.5W. MAXIMUM
SUSTAINED WINDS 135 KT GUSTS 165 KT. TROPICAL STORM FORCE WINDS
WITHIN 120 NM NE QUADRANT...110 NM SE QUADRANT...80 NM SW
QUADRANT...AND 100 NM NW QUADRANT. WINDS 20 TO 30 KT ELSEWHERE
FROM 17N TO 25N BETWEEN 160W AND 167W. SEAS 4 M OR GREATER FROM
17N TO 22N BETWEEN 160W AND 167W WITH SEAS TO 11 M. SEAS 2.5 TO
3.5 M ELSEWHERE FROM 13N TO 29N BETWEEN 155W AND 178W.
.48 HOUR FORECAST HURRICANE NOLO NEAR 22.4N 163.7W. MAXIMUM
SUSTAINED WINDS 95 KT GUSTS 115 KT. LITTLE CHANGE IN RADIUS OF
TROPICAL STORM FORCE WINDS. WINDS 20 TO 30 KT ELSEWHERE FROM 20N
TO 27N BETWEEN 158W AND 168W. SEAS 4 M OR GREATER FROM 20N TO 25N
BETWEEN 161W AND 166W WITH SEAS TO 9.5 M. SEAS 2.5 TO 3.5 M
ELSEWHERE FROM 15N TO 28N BETWEEN 157W AND 170W.

FORECAST WINDS IN AND NEAR ACTIVE TROPICAL CYCLONES SHOULD BE
USED WITH CAUTION DUE TO UNCERTAINTY IN FORECAST TRACK...SIZE AND
INTENSITY.

.SYNOPSIS AND FORECAST.

.24 HOUR FORECAST NEW TROUGH 24N167W TO 30N164W.
.48 HOUR FORECAST TROUGH 26N164W TO 30N162W.

.WINDS 20 TO 25 KT FROM 21N TO 27N W OF 152W...AND FROM 17N TO
26N E OF 147W. SEAS 2.5 TO 3 M FROM 12N TO 29N E OF 153W...AND
FROM 06N TO 12N E OF 146W.
.24 HOUR FORECAST WINDS 20 TO 25 KT FROM 17N TO 24N BETWEEN 155W
AND 160W. SEAS 2.5 TO 3 M FROM 16N TO 27N E OF 155W...AND FROM 07N
TO 13N E OF 143W.
.48 HOUR FORECAST WINDS 20 TO 25 KT N OF 29N BETWEEN 168W AND
175W. SEAS 2.5 TO 3 M FROM 14N TO 24N E OF 144W...AND N OF 29N
BETWEEN 171W AND 175W.

.WINDS 20 KT OR LESS AND SEAS 2.5 M OR LOWER OVER REMAINDER OF
FORECAST AREA.

.MONSOON TROUGH 14N140W TO 12N157W...AND 14N165W TO 11N172W TO
11N180. SCATTERED MODERATE TO ISOLATED STRONG TSTMS S OF TROUGH
FROM 00N TO 07N E OF 159W.

.FORECASTER CHAN. HONOLULU HI.
```

---

### 12. Hourly Wind/Precip Observations

| Field | Value |
|---|---|
| **Resource ID** | oso_hourly_obs |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=OSO&issuedby=HFO |
| **Collected** | 2026-09-27T23:40:58.617900-10:00 HST |

```text
204
SXHW50 PHFO 280926
OSOHFO

Hawaii Wind Data
National Weather Service Honolulu HI
1125 PM HST Sun Sep 27 2026

                            W I N D        D A T A
                            ----------------------
                                                                   IN KNOTS
 ID                Location              Date     Time     DIR    SPD   GUST
--------   -------------------------    -------  -(HST)-  ----   ----   ----
0000LLMH1  Lower Limahuli     Kauai     27Sep26   23:00    340      3      8
0000CMGH1  Common Ground      Kauai     27Sep26   23:00    120      5      9
0000HLIH1  Hanalei            Kauai     27Sep26   22:41    110      6     14
0000MLDH1  Moloaa Dairy       Kauai     27Sep26   22:45    120      6     14
0000HNMH1  Hanamaulu          Kauai     27Sep26   23:00     50      5     10
0000PHLI   Lihue              Kauai     27Sep26   23:00     60     15     25
0000NWWH1  Nawiliwili NOS     Kauai     27Sep26   23:06     60     16     19
0000POIH1  Poipu              Kauai                MSG    MSG    MSG    MSG
0000LNTH1  Lawai NTBG         Kauai     27Sep26   23:00     90     12     24
0000PAKH1  Port Allen         Kauai     27Sep26   23:00     90     16     27
0000MKAH1  Makaha Ridge       Kauai     27Sep26   23:11     30      3      9
0000MNRH1  Mana               Kauai     27Sep26   22:34     70      5     13
0000PHBK   Barking Sands      Kauai     27Sep26   23:00      0      0    MSG
0000PLRH1  Puu Lua            Kauai     27Sep26   22:35     70     14     24
0000POPH1  Puu Opae           Kauai     27Sep26   22:34     90     10     28
0000WHGH1  Waimea Heights     Kauai     27Sep26   22:35     30     12     27

0000KRGH1  Kalahee Ridge      Oahu      27Sep26   22:55     60      9     19
0000KAHH1  Kahuku             Oahu                 MSG    MSG    MSG    MSG
0000KTAH1  Kahuku Trng        Oahu      27Sep26   22:59    110      3     14
0000KFWH1  Kii                Oahu      27Sep26   22:45     90     16     24
0000OFRH1  Oahu Forest NWR    Oahu      27Sep26   22:36     90     12     37
0000KWMH1  Kaaawa Makai       Oahu      27Sep26   22:45     50      5      9
0000PHNG   Kaneohe MCBH       Oahu      27Sep26   23:12     80     12     25
0000MOKH1  Mokuoloe Is NOS    Oahu      27Sep26   23:06     90     11     16
0000BELH1  Bellows AFS        Oahu      27Sep26   23:15     70     15    MSG
0000KUXH1  Kaluanui           Oahu      27Sep26   23:00    160      5     18
0000LYOH1  Lyon               Oahu      27Sep26   22:55    290      3      8
0000NRSH1  Nuuanu Res No 1    Oahu      27Sep26   23:00     10      6     13
0000PHNL   Honolulu AP        Oahu      27Sep26   23:00     60     16     27
0000OOUH1  Honolulu Hbr NOS   Oahu      27Sep26   23:00     70      5     16
0000HOFH1  Honouliuli PHB     Oahu      27Sep26   22:41     60     14     21
0000SCBH1  Schofield Brks     Oahu      27Sep26   22:57     90      5     22
0000SCEH1  Schofield East     Oahu      27Sep26   22:58     90      8     17
0000HWLH1  HECO Wilikina      Oahu      27Sep26   23:10    110      4      7
0000PHJR   Kalaeloa           Oahu      27Sep26   23:00     80     12     21
0000HFHH1  HECO Farrington    Oahu      27Sep26   23:10     70     12     22
0000HPLH1  HECO Palehua       Oahu      27Sep26   23:10     80     14     24
0000HPDH1  HECO Palehua 2     Oahu      27Sep26   23:10     60     19     27
0000HPHH1  HECO Palehua 3     Oahu      27Sep26   23:10     60     13     24
0000HPRH1  HECO Paakea        Oahu      27Sep26   23:10     30      5     19
0000HLRH1  HECO Lualualei     Oahu      27Sep26   23:10     40      6     26
0000HWVH1  HECO Waianae Vly   Oahu                 MSG    MSG    MSG    MSG
0000PLHH1  Palehua            Oahu      27Sep26   22:36     50      0      0
0000WNVH1  Waianae Valley     Oahu      27Sep26   22:37     50     13     30
0000HHSH1  HECO Ala Hema St   Oahu      27Sep26   23:10     90     10     21
0000WBHH1  Waianae Harbor     Oahu                 MSG    MSG    MSG    MSG
0000HKRH1  HECO Kili Dr       Oahu      27Sep26   23:10     90      6     16
0000HMVH1  HECO Makaha Vly    Oahu      27Sep26   23:10    100      5     19
0000MKRH1  Makua Range        Oahu      27Sep26   22:58     80      8     18
0000KKRH1  Kuaokala           Oahu      27Sep26   22:36     30      7     23
0000AALH1  Kaala              Oahu      27Sep26   23:00    100      7     17
0000HFRH1  HECO Farrington2   Oahu      27Sep26   23:10     70      7     12
0000HFYH1  HECO Farrington3   Oahu      27Sep26   23:10     80     15     22
0000DLGH1  Dillingham         Oahu      27Sep26   22:49     80      3     10

0000MKPH1  Makapulapai        Molokai   27Sep26   23:15     90     23     38
0000PAFH1  Puu Alii           Molokai   27Sep26   23:22    300      3     16
0000HOMH1  Honolimaloo        Molokai   27Sep26   23:00    110      7     14
0000KOPH1  Keopukaloa         Molokai   27Sep26   23:00    130      8     15
0000MLKH1  Molokai 1          Molokai              MSG    MSG    MSG    MSG
0000MMPH1  MECO Makaena       Molokai   27Sep26   23:10    340      1      4
0000MKYH1  MECO Kalae Hwy     Molokai   27Sep26   23:10     30      7     10
0000PHMK   Molokai AP         Molokai   27Sep26   23:00     50     10     24
0000ANPH1  Anapuka            Molokai   27Sep26   23:00     80     11     19

0000LNIH1  Lanai 1            Lanai     27Sep26   22:37     60      0      0

0000KAOH1  Kaneloa            Kahoolawe            MSG    MSG    MSG    MSG

0000PHOG   Kahului AP         Maui      27Sep26   23:00     60     21     34
0000KLIH1  Kahului Hbr NOS    Maui      27Sep26   23:06    120      8     23
0000MHRH1  MECO Hansen Rd     Maui      27Sep26   23:10    210      4      7
0000MHKH1  MECO Haleakala Hwy Maui      27Sep26   23:10     70      5     10
0000MMKH1  MECO Makawao       Maui      27Sep26   23:10    150      5     10
0000MKTH1  MECO Kula 2        Maui      27Sep26   21:50    130      4      7
0000PILH1  Piiholo            Maui      27Sep26   23:00    130      4     15
0000EBYH1  EMI Baseyard       Maui      27Sep26   23:00    120      2      6
0000HNAH1  Hana               Maui                 MSG    MSG    MSG    MSG
0000NKUH1  Na Kula            Maui      27Sep26   22:35     70     23     44
0000AWAH1  Auwahi             Maui                 MSG    MSG    MSG    MSG
0000KLFH1  Kula 1             Maui      27Sep26   22:48     50      3      6
0000KKNH1  Kahikinui 1        Maui      27Sep26   22:34     70      5     16
0000KMEH1  Kamehamenui 1      Maui      27Sep26   22:48    120     23     32
0000SUMH1  Summit             Maui      27Sep26   23:00    100     16     22
0000NNEH1  Nene Nest          Maui      27Sep26   23:00    140      9     15
0000PHQH1  Park HQ            Maui      27Sep26   23:00    130     11     18
0000WKTH1  Waikamoi Treeline  Maui      27Sep26   23:00    170      6     18
0000MCTH1  MECO Crater Rd     Maui      27Sep26   23:10    120      3      8
0000KLGH1  Kula Ag            Maui      27Sep26   23:00    100      1      2
0000MWAH1  MECO Waipoli Rd    Maui      27Sep26   23:10    100      2      4
0000KKEH1  Keokea             Maui      27Sep26   23:00    130      2      3
0000MKUH1  MECO Kula          Maui      27Sep26   23:10     60      5      7
0000PHUH1  Pulehu             Maui      27Sep26   23:00    120      3      6
0000MNDH1  MECO Naalaea Rd    Maui      27Sep26   23:10    100      3      5
0000MURH1  MECO Ulupalakua    Maui      27Sep26   23:10     80      3      4
0000LPOH1  Lipoa              Maui      27Sep26   23:00    140      3      3
0000MVHH1  MECO Veterans Hwy  Maui      27Sep26   23:10      0      3      4
0000KPDH1  Kealia Pond        Maui      27Sep26   23:20     50      3      6
0000MMAH1  MECO Maalaea       Maui      27Sep26   23:20    350      8     15
00000P36   Maalaea Bay        Maui      27Sep26   22:15      0      0      0
0000HULH1  Hanaula            Maui      27Sep26   22:55     60      7     17
0000OLUH1  Olowalu            Maui      27Sep26   23:00     70      5     12
0000MMMH1  MECO Mamane Pl     Maui      27Sep26   23:10    290     12     17
0000MHOH1  MECO Honoapiilani  Maui      27Sep26   23:10    360     12     18
0000MHHH1  MECO Honoapiilani2 Maui      27Sep26   23:10    330      9     16
0000MKEH1  MECO Kealaloloa Rg Maui      27Sep26   23:20    340     10     19
0000MUGH1  MECO Ukumehame Gul Maui      27Sep26   23:10     10     11     21
0000MOOH1  MECO Olowalu       Maui      27Sep26   23:20     30      6     15
0000OLUH1  Olowalu            Maui      27Sep26   23:00     70      5     12
0000MLPH1  MECO Launiupoko    Maui      27Sep26   23:20     40      5      7
0000MLTH1  MECO Launiupoko 2  Maui      27Sep26   23:10     30      6     12
0000MLRH1  MECO Lahainaluna   Maui      27Sep26   20:50     80      5      6
0000LWTH1  Lahaina WTP        Maui      27Sep26   23:00    100      3      5
0000MKNH1  MECO Kaanapali     Maui      27Sep26   23:20     90      6      7
0000PHJH   Kapalua-W Maui     Maui                 MSG    MSG    MSG    MSG
0000HOOH1  Honolua            Maui      27Sep26   23:00     60      6     19

0000UPLH1  Upolu Airport      Hawaii    27Sep26   22:15     80     17     30
0000KMMH1  Kaluamakani        Hawaii    27Sep26   23:00    150      4      4
0000PMLH1  Puu Mali           Hawaii    27Sep26   23:00    200      3      5
0000KNKH1  Kanakaleonui       Hawaii    27Sep26   23:00    200      9     12
0000WPNH1  Waipunalei         Hawaii               MSG    MSG    MSG    MSG
0000LAUH1  Laupahoehoe        Hawaii               MSG    MSG    MSG    MSG
0000SPNH1  Spencer            Hawaii               MSG    MSG    MSG    MSG
0000HKUH1  Hakalau            Hawaii    27Sep26   22:45    200      3     10
0000KLXH1  Kulaimano          Hawaii    27Sep26   23:00    190      4      7
0000PIOH1  Piihonua           Hawaii    27Sep26   23:00    260      4      6
0000PHTO   Hilo AP            Hawaii    27Sep26   23:00    240      7    MSG
0000ILOH1  Hilo Hbr NOS       Hawaii    27Sep26   23:06    220      3      6
0000IPIH1  IPIF               Hawaii    27Sep26   23:00    230      2      5
0000WEXH1  Waiakea Exp Stn    Hawaii    27Sep26   23:00    MSG      0      3
0000KEUH1  Keaau              Hawaii    27Sep26   23:00    250      0      2
0000PAOH1  Pahoa              Hawaii    27Sep26   23:00    190      0      1
0000NHKH1  Nahuku             Hawaii    27Sep26   23:00     20     10     16
0000KKUH1  Keaumo             Hawaii    27Sep26   22:34    350      7     14
0000MOBH1  Mauna Loa Obs      Hawaii    27Sep26   23:00    MSG     10     15
0000PLIH1  Pali 2             Hawaii    27Sep26   23:01     20     11     17
0000KMOH1  Kealakomo          Hawaii    27Sep26   22:44     10     13     24
0000KPRH1  Kapapala           Hawaii    27Sep26   22:48     10      4      8
0000NENH1  Nene Cabin         Hawaii    27Sep26   23:23     60      8     15
0000KIOH1  Kaiholena          Hawaii    27Sep26   23:00    320      8     10
0000LKHH1  Lower Kahuku       Hawaii    27Sep26   23:23    350      3     15
0000SOPH1  South Point        Hawaii    27Sep26   23:00     70     17     23
0000KOMH1  Kona Hema          Hawaii    27Sep26   23:00      0      1      4
0000KRCH1  Kahuku Ranch       Hawaii    27Sep26   22:29     30      7     19
0000PHRH1  Puho CS            Hawaii    27Sep26   23:22     60      3      6
0000HLNH1  HELCO Lolo Ln      Hawaii    27Sep26   23:20    360      2      3
0000HHUH1  HELCO Hualalai Rd  Hawaii    27Sep26   23:20     10      2      4
0000KOUH1  Keahuolu           Hawaii    27Sep26   23:00     30      0      3
0000PHKO   Kona Intl AP       Hawaii    27Sep26   23:00    280     13    MSG
0000KHOH1  Kaloko-Honokohau   Hawaii    27Sep26   23:15    280      6     10
0000PLMH1  Palamanui          Hawaii    27Sep26   23:00    220      0      1
0000PWAH1  Puu Waawaa (UHM)   Hawaii    27Sep26   23:00    170      4      5
0000KIUH1  Kaiaulu Puu Waawaa Hawaii    27Sep26   23:00    300      9     11
0000KPLH1  Kaupulehu          Hawaii    27Sep26   22:36    260      3      5
0000PWWH1  Puu Waawaa         Hawaii    27Sep26   22:37    180      2      8
0000HMHH1  HELCO Mamalahoa 2  Hawaii    27Sep26   23:20    190      5      7
0000MMLH1  Mamalahoa          Hawaii    27Sep26   23:00    160      0      1
0000HMWH1  HELCO Mamalahoa 3  Hawaii    27Sep26   23:20    210      6      9
0000PULH1  Puuanahulu         Hawaii    27Sep26   22:37    130     13     30
0000AHMH1  Ahumoa             Hawaii    27Sep26   22:35     60      6      8
0000AIPH1  Aipaloa            Hawaii    27Sep26   23:00    130      7      9
0000HSRH1  HELCO Saddle Rd    Hawaii    27Sep26   23:20     50      6      7
0000HMYH1  HELCO Mamalahoa    Hawaii    27Sep26   23:20     80      4      9
0000HHCH1  HELCO Hokuloa UCC  Hawaii    27Sep26   23:20     90      8      9
0000HWRH1  HELCO Waikoloa Rd  Hawaii    27Sep26   23:20     70      9     13
0000HWXH1  HELCO Waikoloa 2   Hawaii    27Sep26   23:20    100     12     15
0000WKVH1  Waikoloa           Hawaii    27Sep26   22:35     70      6     14
0000HLOH1  HELCO Lalamilo     Hawaii    27Sep26   23:20     40     12     14
0000LLAH1  Lalamilo           Hawaii    27Sep26   23:00    350      2      7
0000HKWH1  HELCO Kawaihae Rd  Hawaii    27Sep26   23:20     20     16     23
0000PKAH1  PTA Kipuka Alala   Hawaii    27Sep26   22:55    120      5      8
0000PKWH1  PTA West           Hawaii    27Sep26   22:56    100     16     32
0000PKMH1  PTA Keamuku        Hawaii    27Sep26   22:50    110      0      0
0000PTRH1  PTA Range 17       Hawaii    27Sep26   22:49    140     22     31
0000PERH1  Puhe CS            Hawaii    27Sep26   22:24     70      3      6
0000KWHH1  Kawaihae NOS       Hawaii               MSG    MSG    MSG    MSG
0000HHKH1  HELCO Hulukupuna   Hawaii    27Sep26   23:20     60      5      7
0000PLAH1  Puuloa             Hawaii    27Sep26   23:00    320     13     22
0000HMLH1  HELCO Maluokalani  Hawaii               MSG    MSG    MSG    MSG
0000HKDH1  HELCO Ala Kahua    Hawaii    27Sep26   23:20    210      6      8
0000KHRH1  Kohala Ranch       Hawaii    27Sep26   22:35     60      5     10
0000KEHH1  Kehena             Hawaii    27Sep26   23:00    140      7     16
```

---

### 13. Monthly Climate Summary — HNL

| Field | Value |
|---|---|
| **Resource ID** | clm_monthly_climate_summary_HNL |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLM&issuedby=HNL |
| **Collected** | 2026-09-27T22:59:23.864727-10:00 HST |

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

WEATHER         OBSERVED          NORMAL  DEPART   LAST YEAR`S
                VALUE   DATE(S)   VALUE   FROM     VALUE DATE(S)
                                          NORMAL
................................................................
TEMPERATURE (F)
RECORD
 HIGH             95   08/31/2019
 LOW              25   08/02/2024
HIGHEST           90   08/09         89       1       92  08/11
                       08/11
                       08/22
LOWEST            74   08/19         75      -1       74  08/11
                       08/20
                                                          08/14
                                                          08/30
AVG. MAXIMUM    88.3               88.8    -0.5     89.2
AVG. MINIMUM    76.7               75.6     1.1     76.6
MEAN            82.5               82.2     0.3     82.9
DAYS MAX >= 93     0                                   0
DAYS MAX >= 90     6                                  13
DAYS MAX <= 80     0                                   0
DAYS MIN >= 72    31                                  31
DAYS MIN <= 60     0                                   0
DAYS MIN <= 55     0                                   0

PRECIPITATION (INCHES)
RECORD
 MAXIMUM        3.74   2004
 MINIMUM           T   2025
TOTALS          0.91               0.84    0.07        T
DAILY AVG.      0.03               0.03    0.00        T
DAYS >= .01        1                5.7    -4.7        0
DAYS >= .10        0                1.2    -1.2        0
DAYS >= .50        0                0.4    -0.4        0
DAYS >= 1.00       0                0.2    -0.2        0
GREATEST
 24 HR. TOTAL   0.86   08/15 TO 08/16                  T

DEGREE DAYS
HEATING TOTAL      0                  0       0        0
 SINCE 7/1         0                  0       0       MM
COOLING TOTAL    550                533      17      561
 SINCE 1/1      3210               3077     133       MM
................................................................

WIND (MPH)
AVERAGE WIND SPEED              12.5
HIGHEST WIND SPEED/DIRECTION    38/050    DATE  08/16
HIGHEST GUST SPEED/DIRECTION    53/060    DATE  08/16

SKY COVER
POSSIBLE SUNSHINE (PERCENT)   MM
AVERAGE SKY COVER           0.45
NUMBER OF DAYS FAIR           10
NUMBER OF DAYS PC             19
NUMBER OF DAYS CLOUDY          2

AVERAGE RH (PERCENT)     66

WEATHER CONDITIONS. NUMBER OF DAYS WITH
THUNDERSTORM             MM     MIXED PRECIP              MM
HEAVY RAIN                1     RAIN                       1
LIGHT RAIN               12     FREEZING RAIN             MM
LT FREEZING RAIN         MM     HAIL                      MM
HEAVY SNOW               MM     SNOW                      MM
LIGHT SNOW               MM     SLEET                     MM
FOG                       3     FOG W/VIS <= 1/4 MILE     MM
HAZE                     MM

-  INDICATES NEGATIVE NUMBERS.
R  INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T  INDICATES TRACE AMOUNT.
```

---

### 14. Monthly Climate Summary — ITO

| Field | Value |
|---|---|
| **Resource ID** | clm_monthly_climate_summary_ITO |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLM&issuedby=ITO |
| **Collected** | 2026-09-27T23:00:09.780072-10:00 HST |

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

WEATHER         OBSERVED          NORMAL  DEPART   LAST YEAR`S
                VALUE   DATE(S)   VALUE   FROM     VALUE DATE(S)
                                          NORMAL
................................................................
TEMPERATURE (F)
RECORD
 HIGH             93   08/15/1950
 LOW              63   08/01/1955
HIGHEST           87   08/21         83       4       88  08/11
LOWEST            70   08/30         69       1       67  08/24
AVG. MAXIMUM    83.7               82.9     0.8     84.9
AVG. MINIMUM    72.6               70.4     2.2     70.0
MEAN            78.2               76.6     1.6     77.5
DAYS MAX >= 93     0                                   0
DAYS MAX >= 90     0                                   0
DAYS MAX <= 80     2                                   2
DAYS MIN >= 72    20                                   6
DAYS MIN <= 60     0                                   0
DAYS MIN <= 55     0                                   0

PRECIPITATION (INCHES)
RECORD
 MAXIMUM       48.85   2018
 MINIMUM        2.06   2025
TOTALS         20.85              11.30    9.55     2.06
DAILY AVG.      0.67               0.36    0.31     0.05
DAYS >= .01       25               27.2    -2.2       19
DAYS >= .10       16               18.2    -2.2        5
DAYS >= .50        8                6.0     2.0        1
DAYS >= 1.00       3                2.2     0.8        0
GREATEST
 24 HR. TOTAL   9.24   08/15 TO 08/16               0.70

DEGREE DAYS
HEATING TOTAL      0                  0       0        0
 SINCE 7/1         0                  0       0       MM
COOLING TOTAL    416                361      55      393
 SINCE 1/1      2429               2111     318       MM
................................................................

WIND (MPH)
AVERAGE WIND SPEED              6.8
HIGHEST WIND SPEED/DIRECTION    39/090    DATE  08/15
HIGHEST GUST SPEED/DIRECTION    56/080    DATE  08/15

SKY COVER
POSSIBLE SUNSHINE (PERCENT)   MM
AVERAGE SKY COVER           0.78
NUMBER OF DAYS FAIR            1
NUMBER OF DAYS PC             11
NUMBER OF DAYS CLOUDY         19

AVERAGE RH (PERCENT)     81

WEATHER CONDITIONS. NUMBER OF DAYS WITH
THUNDERSTORM             MM     MIXED PRECIP              MM
HEAVY RAIN               15     RAIN                      15
LIGHT RAIN               27     FREEZING RAIN             MM
LT FREEZING RAIN         MM     HAIL                      MM
HEAVY SNOW               MM     SNOW                      MM
LIGHT SNOW               MM     SLEET                     MM
FOG                      25     FOG W/VIS <= 1/4 MILE     MM
HAZE                      8

-  INDICATES NEGATIVE NUMBERS.
R  INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T  INDICATES TRACE AMOUNT.
```

---

### 15. Monthly Climate Summary — LIH

| Field | Value |
|---|---|
| **Resource ID** | clm_monthly_climate_summary_LIH |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLM&issuedby=LIH |
| **Collected** | 2026-09-27T22:59:38.927207-10:00 HST |

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

WEATHER         OBSERVED          NORMAL  DEPART   LAST YEAR`S
                VALUE   DATE(S)   VALUE   FROM     VALUE DATE(S)
                                          NORMAL
................................................................
TEMPERATURE (F)
RECORD
 HIGH             91   08/31/2019
                       08/25/2019
                       09/19/1994
 LOW              59   08/27/2020
HIGHEST           87   08/13         85       2       88  08/16
LOWEST            72   08/07         75      -3       72  08/11
AVG. MAXIMUM    84.7               85.2    -0.5     86.6
AVG. MINIMUM    75.7               75.2     0.5     75.7
MEAN            80.2               80.2     0.0     81.2
DAYS MAX >= 93     0                                   0
DAYS MAX >= 90     0                                   0
DAYS MAX <= 80     1                                   0
DAYS MIN >= 72    31                                  31
DAYS MIN <= 60     0                                   0
DAYS MIN <= 55     0                                   0

PRECIPITATION (INCHES)
RECORD
 MAXIMUM        8.13   1959
 MINIMUM        0.44   2007
TOTALS          2.43               2.33    0.10     1.25
DAILY AVG.      0.08               0.08    0.00     0.04
DAYS >= .01       22               18.0     4.0       12
DAYS >= .10        4                5.3    -1.3        2
DAYS >= .50        1                0.9     0.1        1
DAYS >= 1.00       1                0.4     0.6        0
GREATEST
 24 HR. TOTAL   1.18   08/16 TO 08/17               0.83

DEGREE DAYS
HEATING TOTAL      0                  0       0        0
 SINCE 7/1         0                  0       0       MM
COOLING TOTAL    480                471       9      508
 SINCE 1/1      2703               2634      69       MM
................................................................

WIND (MPH)
AVERAGE WIND SPEED              14.6
HIGHEST WIND SPEED/DIRECTION    39/070    DATE  08/16
HIGHEST GUST SPEED/DIRECTION    53/070    DATE  08/16

SKY COVER
POSSIBLE SUNSHINE (PERCENT)   MM
AVERAGE SKY COVER           0.61
NUMBER OF DAYS FAIR            3
NUMBER OF DAYS PC             19
NUMBER OF DAYS CLOUDY          9

AVERAGE RH (PERCENT)     78

WEATHER CONDITIONS. NUMBER OF DAYS WITH
THUNDERSTORM             MM     MIXED PRECIP              MM
HEAVY RAIN                3     RAIN                       3
LIGHT RAIN               19     FREEZING RAIN             MM
LT FREEZING RAIN         MM     HAIL                      MM
HEAVY SNOW               MM     SNOW                      MM
LIGHT SNOW               MM     SLEET                     MM
FOG                      17     FOG W/VIS <= 1/4 MILE     MM
HAZE                     10

-  INDICATES NEGATIVE NUMBERS.
R  INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T  INDICATES TRACE AMOUNT.
```

---

### 16. Monthly Climate Summary — OGG

| Field | Value |
|---|---|
| **Resource ID** | clm_monthly_climate_summary_OGG |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=CLM&issuedby=OGG |
| **Collected** | 2026-09-27T22:59:53.943975-10:00 HST |

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

WEATHER         OBSERVED          NORMAL  DEPART   LAST YEAR`S
                VALUE   DATE(S)   VALUE   FROM     VALUE DATE(S)
                                          NORMAL
................................................................
TEMPERATURE (F)
RECORD
 HIGH             97   08/22/2015
                       08/31/1994
 LOW              60   08/30/2019
HIGHEST           90   08/11         88       2       92  08/16
                       08/21
                       08/24
                                                          08/23
                                                          08/27
LOWEST            70   08/20         71      -1       65  08/25
AVG. MAXIMUM    87.1               89.9    -2.8     89.5
AVG. MINIMUM    74.4               72.3     2.1     71.7
MEAN            80.8               81.1    -0.3     80.6
DAYS MAX >= 93     0                                   0
DAYS MAX >= 90     3                                  17
DAYS MAX <= 80     0                                   0
DAYS MIN >= 72    28                                  16
DAYS MIN <= 60     0                                   0
DAYS MIN <= 55     0                                   0

PRECIPITATION (INCHES)
RECORD
 MAXIMUM        1.93   2018
 MINIMUM        0.01   2025
TOTALS          1.47               0.53    0.94     0.01
DAILY AVG.      0.05               0.02    0.03     0.00
DAYS >= .01        5                7.4    -2.4        1
DAYS >= .10        3                1.3     1.7        0
DAYS >= .50        1                0.2     0.8        0
DAYS >= 1.00       0                0.0     0.0        0
GREATEST
 24 HR. TOTAL   1.20   08/15 TO 08/16               0.01

DEGREE DAYS
HEATING TOTAL      0                  0       0        0
 SINCE 7/1         0                  0       0       MM
COOLING TOTAL    400                499     -99      490
 SINCE 1/1      2784               2847     -63       MM
................................................................

WIND (MPH)
AVERAGE WIND SPEED              15.9
HIGHEST WIND SPEED/DIRECTION    38/050    DATE  08/15
HIGHEST GUST SPEED/DIRECTION    62/050    DATE  08/15

SKY COVER
POSSIBLE SUNSHINE (PERCENT)   MM
AVERAGE SKY COVER           0.40
NUMBER OF DAYS FAIR           15
NUMBER OF DAYS PC             14
NUMBER OF DAYS CLOUDY          2

AVERAGE RH (PERCENT)     73

WEATHER CONDITIONS. NUMBER OF DAYS WITH
THUNDERSTORM             MM     MIXED PRECIP              MM
HEAVY RAIN                1     RAIN                       2
LIGHT RAIN               15     FREEZING RAIN             MM
LT FREEZING RAIN         MM     HAIL                      MM
HEAVY SNOW               MM     SNOW                      MM
LIGHT SNOW               MM     SLEET                     MM
FOG                      12     FOG W/VIS <= 1/4 MILE     MM
HAZE                      2

-  INDICATES NEGATIVE NUMBERS.
R  INDICATES RECORD WAS SET OR TIED.
MM INDICATES DATA IS MISSING.
T  INDICATES TRACE AMOUNT.
```

---

### 17. NHC Atlantic Tropical Weather Outlook — 2 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_atlc_2day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=atlc&fdays=2 |
| **Collected** | 2026-09-28T05:06:18.527040-10:00 HST |

```text
733 ACCA62 KNHC 281118TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL800 AM EDT lunes 28 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Depresión Tropical Fay, ubicada al suroeste delas Azores.Atlántico Subtropical Central (AL91): Un área de baja presiónubicada al este-noreste de las Bermudas se está moviendo rápidamentehacia el este. Imágenes recientes de microondas sugieren que laactividad de aguaceros y tormentas está comenzando a mostrar signosde organización, aunque no está claro si el sistema ha desarrolladouna circulación bien definida dado su rápido movimiento de avance.Si bien las condiciones ambientales son actualmente solomarginalmente favorables, es probable que este sistema se conviertaen una depresión tropical o tormenta en el próximo día o dos, amedida que gire hacia el este-sureste y se ralentice sobre elAtlántico Subtropical central. Se anticipa que las condicionesambientales se vuelvan desfavorables para un mayor desarrollo afinales de esta semana.* Probabilidad de formación hasta 48 horas...alta...70 por ciento.* Probabilidad de formación hasta 7 días...alta...80 por ciento.$$Pronosticador Papin*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 18. NHC Atlantic Tropical Weather Outlook — 7 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_atlc_7day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=atlc&fdays=7 |
| **Collected** | 2026-09-28T05:07:18.533489-10:00 HST |

```text
733 ACCA62 KNHC 281118TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL800 AM EDT lunes 28 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Depresión Tropical Fay, ubicada al suroeste delas Azores.Atlántico Subtropical Central (AL91): Un área de baja presiónubicada al este-noreste de las Bermudas se está moviendo rápidamentehacia el este. Imágenes recientes de microondas sugieren que laactividad de aguaceros y tormentas está comenzando a mostrar signosde organización, aunque no está claro si el sistema ha desarrolladouna circulación bien definida dado su rápido movimiento de avance.Si bien las condiciones ambientales son actualmente solomarginalmente favorables, es probable que este sistema se conviertaen una depresión tropical o tormenta en el próximo día o dos, amedida que gire hacia el este-sureste y se ralentice sobre elAtlántico Subtropical central. Se anticipa que las condicionesambientales se vuelvan desfavorables para un mayor desarrollo afinales de esta semana.* Probabilidad de formación hasta 48 horas...alta...70 por ciento.* Probabilidad de formación hasta 7 días...alta...80 por ciento.$$Pronosticador Papin*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 19. NHC Central Pacific Tropical Weather Outlook — 2 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_cpac_2day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=cpac&fdays=2 |
| **Collected** | 2026-09-28T05:02:18.497047-10:00 HST |

```text
733 ACCA62 KNHC 281118TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL800 AM EDT lunes 28 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Depresión Tropical Fay, ubicada al suroeste delas Azores.Atlántico Subtropical Central (AL91): Un área de baja presiónubicada al este-noreste de las Bermudas se está moviendo rápidamentehacia el este. Imágenes recientes de microondas sugieren que laactividad de aguaceros y tormentas está comenzando a mostrar signosde organización, aunque no está claro si el sistema ha desarrolladouna circulación bien definida dado su rápido movimiento de avance.Si bien las condiciones ambientales son actualmente solomarginalmente favorables, es probable que este sistema se conviertaen una depresión tropical o tormenta en el próximo día o dos, amedida que gire hacia el este-sureste y se ralentice sobre elAtlántico Subtropical central. Se anticipa que las condicionesambientales se vuelvan desfavorables para un mayor desarrollo afinales de esta semana.* Probabilidad de formación hasta 48 horas...alta...70 por ciento.* Probabilidad de formación hasta 7 días...alta...80 por ciento.$$Pronosticador Papin*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 20. NHC Central Pacific Tropical Weather Outlook — 7 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_cpac_7day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=cpac&fdays=7 |
| **Collected** | 2026-09-28T05:03:18.612277-10:00 HST |

```text
733 ACCA62 KNHC 281118TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL800 AM EDT lunes 28 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Depresión Tropical Fay, ubicada al suroeste delas Azores.Atlántico Subtropical Central (AL91): Un área de baja presiónubicada al este-noreste de las Bermudas se está moviendo rápidamentehacia el este. Imágenes recientes de microondas sugieren que laactividad de aguaceros y tormentas está comenzando a mostrar signosde organización, aunque no está claro si el sistema ha desarrolladouna circulación bien definida dado su rápido movimiento de avance.Si bien las condiciones ambientales son actualmente solomarginalmente favorables, es probable que este sistema se conviertaen una depresión tropical o tormenta en el próximo día o dos, amedida que gire hacia el este-sureste y se ralentice sobre elAtlántico Subtropical central. Se anticipa que las condicionesambientales se vuelvan desfavorables para un mayor desarrollo afinales de esta semana.* Probabilidad de formación hasta 48 horas...alta...70 por ciento.* Probabilidad de formación hasta 7 días...alta...80 por ciento.$$Pronosticador Papin*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 21. NHC Eastern Pacific Tropical Weather Outlook — 2 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_epac_2day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=epac&fdays=2 |
| **Collected** | 2026-09-28T05:04:18.699384-10:00 HST |

```text
733 ACCA62 KNHC 281118TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL800 AM EDT lunes 28 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Depresión Tropical Fay, ubicada al suroeste delas Azores.Atlántico Subtropical Central (AL91): Un área de baja presiónubicada al este-noreste de las Bermudas se está moviendo rápidamentehacia el este. Imágenes recientes de microondas sugieren que laactividad de aguaceros y tormentas está comenzando a mostrar signosde organización, aunque no está claro si el sistema ha desarrolladouna circulación bien definida dado su rápido movimiento de avance.Si bien las condiciones ambientales son actualmente solomarginalmente favorables, es probable que este sistema se conviertaen una depresión tropical o tormenta en el próximo día o dos, amedida que gire hacia el este-sureste y se ralentice sobre elAtlántico Subtropical central. Se anticipa que las condicionesambientales se vuelvan desfavorables para un mayor desarrollo afinales de esta semana.* Probabilidad de formación hasta 48 horas...alta...70 por ciento.* Probabilidad de formación hasta 7 días...alta...80 por ciento.$$Pronosticador Papin*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 22. NHC Eastern Pacific Tropical Weather Outlook — 7 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_epac_7day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=epac&fdays=7 |
| **Collected** | 2026-09-28T05:05:18.390977-10:00 HST |

```text
733 ACCA62 KNHC 281118TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL800 AM EDT lunes 28 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Depresión Tropical Fay, ubicada al suroeste delas Azores.Atlántico Subtropical Central (AL91): Un área de baja presiónubicada al este-noreste de las Bermudas se está moviendo rápidamentehacia el este. Imágenes recientes de microondas sugieren que laactividad de aguaceros y tormentas está comenzando a mostrar signosde organización, aunque no está claro si el sistema ha desarrolladouna circulación bien definida dado su rápido movimiento de avance.Si bien las condiciones ambientales son actualmente solomarginalmente favorables, es probable que este sistema se conviertaen una depresión tropical o tormenta en el próximo día o dos, amedida que gire hacia el este-sureste y se ralentice sobre elAtlántico Subtropical central. Se anticipa que las condicionesambientales se vuelvan desfavorables para un mayor desarrollo afinales de esta semana.* Probabilidad de formación hasta 48 horas...alta...70 por ciento.* Probabilidad de formación hasta 7 días...alta...80 por ciento.$$Pronosticador Papin*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 23. NHC source index

| Field | Value |
|---|---|
| **Resource ID** | nhc_homepage |
| **Official source** | https://www.nhc.noaa.gov/ |
| **Collected** | 2026-09-28T05:25:18.541024-10:00 HST |

```text
Home

Mobile Site

Text Version

RSS

Local Forecast

NATIONAL HURRICANE CENTER and
CENTRAL PACIFIC HURRICANE CENTER

National Oceanic and Atmospheric Administration

Analysis & Forecasts

Tropical Cyclone Products

Tropical Weather Outlooks

Marine Products

Rip Currents Map

RSS Feeds

GIS Products

Alternate Formats

Tropical Cyclone Product Descriptions

Tropical Cyclone Product Examples

Marine Product Descriptions

Data & Tools

Satellite Imagery

Radar Imagery

Aircraft Reconnaissance

Tropical Analysis Tools

Experimental Products

Lat/Lon Distance Calculator

Blank Tracking Maps

Educational Resources

Be Prepared!
NWS Hurricane Prep Week

Outreach Documents

TC Videos

Rip Currents

Storm Surge

Watch/Warning Breakpoints

Climatology

Tropical Cyclone Names

Wind Scale

Records and Facts

Historical Hurricane Summaries

Forecast Models

NHC Publications

NHC Glossary

Acronyms

Frequent Questions

Archives

Tropical Cyclone Advisories

Tropical Weather Outlooks

Tropical Cyclone Reports and Season Summaries

Tropical Cyclone Forecast Verification

NHC News Archive

Other Archives: HURDAT, Track Maps, Marine Products, and more

About

National Hurricane Center

Central Pacific Hurricane Center

Library

Contact Us

Search

Search for

Search

Top News of the Day...
view past news

Last update Mon, 28 Sep 2026 15:23:45 UTC

NHC issuing advisories for the Atlantic on

TD Fay

and

TS Hanna

NHC issuing advisories for the Eastern Pacific on

Hurricane Polo

and

TS Rachel

NHC issuing advisories for the Central Pacific on

Hurricane Nolo

Marine warnings are in effect for the Eastern Pacific

Key messages regarding Hurricane Polo

(en Español: Mensajes Claves)

Key messages regarding Tropical Storm Rachel

(en Español: Mensajes Claves)

Graphical Tropical Weather Outlook (Static Images)

JavaScript is currently disabled in your browser or you are using an older browser that is incompatible with this map. To view the interactive map, please enable JavaScript or update your browser if possible. Direct links to the latest high-resolution forecast images are provided below:

View Atlantic 2-Day Outlook

View Atlantic 7-Day Outlook

View Eastern Pacific 2-Day Outlook

View Eastern Pacific 7-Day Outlook

View Central Pacific 2-Day Outlook

View Central Pacific 7-Day Outlook

Central Pacific

Pacific

Atlantic

2-Day Forecast

7-Day Forecast

Disturbances:

None

Disturbances:

None

Disturbances:

ALL

1

Disturbances:

ALL

1

Disturbances:

ALL

1

Disturbances:

ALL

1

Disturbances:

ALL

1

Disturbances:

ALL

1

Disturbances:

ALL

1

Disturbances:

ALL

1

View Full Graphical Tropical Weather Outlook
| Marine Products

Close (X)

View Storm Details

Eastern North Pacific
(East of 140°W)

Tropical Weather Outlook

(en Español*)

500 AM PDT Mon Sep 28 2026

Tropical Weather Discussion

1005 UTC Mon Sep 28 2026

Hurricane Polo

Satellite |
Buoys |
Grids |
Storm Archive

...POLO STILL A MAJOR HURRICANE AS IT APPROACHES THE BAJA CALIFORNIA PENINSULA...
...CONDITIONS TO SOON DETERIORATE AS LIFE-THREATENING WINDS AND FLASH FLOODS EXPECTED OVER PORTIONS OF BAJA CALIFORNIA SUR AND SONORA TODAY AND TUESDAY...

8:00 AM MST Mon Sep 28

Location: 24.2°N 113.5°W

Moving: NE at 10 mph

Min pressure: 958 mb

Max sustained: 115 mph

Public

Advisory

#32

800 AM MST

Forecast

Advisory

#32

1500 UTC

Forecast

Discussion

#32

800 AM MST

Wind Speed

Probabilities

#32

1500 UTC

Productos en español:

(más información)

Aviso

Publico

Pronóstico

Discusión

Wind Speed
Probabilities

Arrival Time
of Winds

Wind
History

Interactive
Cone

Warnings/Cone
Static Images

Warnings/Cone
Interactive Map

Experimental Cone
Static Images

Experimental Cone
Interactive Map

Warnings and
Surface Wind

Key
Messages

Mensajes
Claves

Rip
Currents

Rainfall
Potential

Tropical Storm Rachel

Satellite |
Buoys |
Grids |
Storm Archive

...RACHEL A LITTLE STRONGER AS IT MOVES WEST-NORTHWESTWARD...
...TROPICAL STORM WARNING ISSUED FOR A PORTION OF THE COAST OF SOUTHWESTERN MEXICO...

9:00 AM CST Mon Sep 28

Location: 13.8°N 101.2°W

Moving: WNW at 8 mph

Min pressure: 999 mb

Max sustained: 50 mph

Public

Advisory

#6

900 AM CST

Forecast

Advisory

#6

1500 UTC

Forecast

Discussion

#6

900 AM CST

Wind Speed

Probabilities

#6

1500 UTC

Productos en español:

(más información)

Aviso

Publico

Pronóstico

Discusión

Wind Speed
Probabilities

Arrival Time
of Winds

Wind
History

Interactive
Cone

Warnings/Cone
Static Images

Warnings/Cone
Interactive Map

Experimental Cone
Static Images

Experimental Cone
Interactive Map

Warnings and
Surface Wind

Key
Messages

Mensajes
Claves

Rip
Currents

Rainfall
Potential

Central North Pacific
(140°W to 180°)

Tropical Weather Outlook

(en Español*)

200 AM HST Mon Sep 28 2026

Hurricane Nolo

Satellite |
Buoys |
Grids |
Storm Archive

...HURRICANE WARNING ISSUED FOR A PORTION OF THE PAPAHANAUMOKUAKEA MARINE NATIONAL MONUMENT...

5:00 AM HST Mon Sep 28

Location: 17.1°N 162.3°W

Moving: WNW at 13 mph

Min pressure: 929 mb

Max sustained: 155 mph

Public

Advisory

#32

500 AM HST

Forecast

Advisory

#32

1500 UTC

Forecast

Discussion

#32

500 AM HST

Wind Speed

Probabilities

#32

1500 UTC

Productos en español:

(más información)

Aviso

Publico

Pronóstico

Discusión

Wind Speed
Probabilities

Arrival Time
of Winds

Wind
History

Interactive
Cone

Warnings/Cone
Static Images

Warnings/Cone
Interactive Map

Experimental Cone
Static Images

Experimental Cone
Interactive Map

Warnings and
Surface Wind

Atlantic - Caribbean Sea - Gulf of America

Tropical Weather Outlook

(en Español*)

800 AM EDT Mon Sep 28 2026

Tropical Weather Discussion

1215 UTC Mon Sep 28 2026

Tropical Depression Fay

Satellite |
Buoys |
Grids |
Storm Archive

...FAY MOVING SOUTH-SOUTHWESTWARD OVER THE CENTRAL ATLANTIC...

3:00 PM GMT Mon Sep 28

Location: 27.1°N 44.6°W

Moving: SSW at 9 mph

Min pressure: 1011 mb

Max sustained: 35 mph

Public

Advisory

#34

300 PM GMT

Forecast

Advisory

#34

1500 UTC

Forecast

Discussion

#34

300 PM GMT

Wind Speed

Probabilities

#34

1500 UTC

Productos en español:

(más información)

Aviso

Publico

Pronóstico

Discusión

Wind Speed
Probabilities

Arrival Time
of Winds

Wind
History

Interactive
Cone

Warnings/Cone
Static Images

Warnings/Cone
Interactive Map

Experimental Cone
Static Images

Experimental Cone
Interactive Map

Warnings and
Surface Wind

Rip
Currents

Tropical Storm Hanna

Satellite |
Buoys |
Grids |
Storm Archive

...TROPICAL STORM HANNA FORMS IN THE CENTRAL SUBTROPICAL ATLANTIC...

11:00 AM AST Mon Sep 28

Location: 36.6°N 50.4°W

Moving: E at 17 mph

Min pressure: 1006 mb

Max sustained: 45 mph

Public

Advisory

#1

1100 AM AST

Forecast

Advisory

#1

1500 UTC

Forecast

Discussion

#1

1100 AM AST

Wind Speed

Probabilities

#1

1500 UTC

Productos en español:

(más información)

Aviso

Publico

Pronóstico

Discusión

Wind Speed
Probabilities

Arrival Time
of Winds

Wind
History

Interactive
Cone

Warnings/Cone
Static Images

Warnings/Cone
Interactive Map

Experimental Cone
Static Images

Experimental Cone
Interactive Map

Warnings and
Surface Wind

Rip
Currents

Building Your Hurricane Knowledge Kit

‹

National Hurricane Center Track Forecast Cone (2026)

Building Your Hurricane "Knowledge" Kit: Storm Surge Warning

Building Your Hurricane "Knowledge" Kit: Potential Tropical Cyclones

Tropical Cyclone Names

Tropical Waves

Artificial Intelligence (AI) in Hurricane Forecasting

Building Your Hurricane "Knowledge" Kit: Tropical Weather Outlook

Building Your Hurricane "Knowledge" Kit: Time of Arrival

Building Your Hurricane "Knowledge" Kit: Wind Speed Probabilities

Building Your Hurricane "Knowledge" Kit: Saffir-Simpson Hurricane Wind Scale

Building Your Hurricane "Knowledge" Kit: Storm Surge Watch

National Hurricane Preparedness Week Preview: Assembling Your Hurricane "Knowledge" Kit

›

Quick Links and Additional Resources

Tropical Cyclone Forecasts

Tropical Cyclone Advisories

Tropical Weather Outlook

Audio/Podcasts

About Advisories

Marine Forecasts

Offshore Waters Forecasts

Gridded Forecasts

Graphicast

About Marine

Social Media

NHC on Facebook

NHC on X

NHC on YouTube

NHC Blog:
"Inside the Eye"

Hurricane Preparedness

Preparedness Guide

Hurricane Hazards

Watches and Warnings

Marine Safety

Ready.gov Hurricanes

Weather-Ready Nation

Emergency Management Offices

Research and Development

NOAA Hurricane Research Division

Hurricane and Ocean Testbed

Hurricane Forecast Improvement Program

Other Resources

Q & A with NHC

NHC/AOML Library Branch

NOAA: Hurricane FAQs

National Hurricane Operations Plan

WX4NHC Amateur Radio

NWS Forecast Offices

Weather Prediction Center

Storm Prediction Center

Ocean Prediction Center

Local Forecast Offices

Worldwide Tropical Cyclone Centers

Canadian Hurricane Centre

Joint Typhoon Warning Center

Other Tropical Cyclone Centers

WMO Severe Weather Info Centre

US Dept of Commerce

National Oceanic and Atmospheric Administration

National Hurricane Center

11691 SW 17th Street

Miami, FL, 33165

nhcwebmaster@noaa.gov

Central Pacific Hurricane Center

2525 Correa Rd

Suite 250

Honolulu, HI 96822

W-HFO.webmaster@noaa.gov

Disclaimer

Information Quality

Help

Glossary
```

---

### 24. NOAA solar calculation table

| Field | Value |
|---|---|
| **Resource ID** | solar_calculation_table |
| **Official source** | https://gml.noaa.gov/grad/solcalc/table.php?lat=21.3&lon=-157.85&year=2026 |
| **Collected** | 2026-09-27T22:57:55.728502-10:00 HST |

```text
Solar Calculator - NOAA Global Monitoring Laboratory

Skip to main content

An official website of the United States government Here's how you know

Official websites use .gov

A .gov website belongs to an official government organization in the United States.

Secure .gov websites use HTTPS

A lock () or https:// means you’ve safely connected to the .gov website. Share sensitive information only on official, secure websites.

Search

Search GML:

Global Monitoring Laboratory

Menu

Home

About

About GML
Science Reviews
Safety Program

Employment
Visiting
Contact Us

Intranet

People

Organization
Staff
Employee Spotlight

Research

Research Overview
Carbon Cycle Greenhouse Gases
Greenhouse gases and Ozone-depleting Substances
Ozone and Water Vapor
Global Radiation, Aerosols and Clouds
Publications
Calibration Facilities
WMO Central Calibration Laboratory
Central UV Calibration Facility
Broadband Solar Calibration Facility
World Dobson Ozone Calibration Centre

Observing Networks

Overview
Observations Overview
Measurement Sites
Field Campaigns

Atmospheric Baseline Observatories
Observatory Operations
Barrow, Alaska
Mauna Loa, Hawaii
American Samoa
South Pole

Observing Networks
Greenhouse Gas Reference Network
Halocarbons and Trace Gases
Surface Radiation
Federated Aerosol Network
Ozone
Water Vapor

Data & Products

Data
Data & Products Portal
Data Finder
ObsPack Data Products
Measurement Sites

Visualization & Tools

Data Viewer
South Pole Ozone Hole
Mauna Loa Apparent Transmission
Barrow Snow Melt Dates

Products
Greenhouse Gas Index
Ozone Depletion Index
Trends in CO2, CH4, N2O, SF6
Modeling

Information

News
Seminars
Education/Outreach
Student Opportunities
FAQ's
Publications

Webcams
South Pole Webcam
Mauna Loa Webcams
Barrow Webcam

Global Monitoring Annual Conference
GMAC Conference

Search

Search GML:

PDF Format

Sunrise Table for 2026

Location: Latitude 21.30000 Longitude -157.85000

Time Zone Offset: Pacific/Honolulu -10.0

All times are in local time. Cells with light green color indicate when daylight saving time is in effect.

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

Oct

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

Sunset Table for 2026

Location: Latitude 21.30000 Longitude -157.85000

Time Zone Offset: Pacific/Honolulu -10.0

All times are in local time. Cells with light green color indicate when daylight saving time is in effect.

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

Oct

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

Location: Latitude 21.30000 Longitude -157.85000

Time Zone Offset: Pacific/Honolulu -10.0

All times are in local time. Cells with light green color indicate when daylight saving time is in effect.

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

Oct

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

Global Monitoring Laboratory

» U.S. Department of Commerce

» National Oceanic & Atmospheric Administration

» NOAA Research
```

---

### 25. Offshore Forecast (40-240nm)

| Field | Value |
|---|---|
| **Resource ID** | off_offshore_forecast |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=OFF&issuedby=HFO |
| **Collected** | 2026-09-27T23:53:50.061534-10:00 HST |

```text
599
FZHW60 PHFO 280945
OFFHFO

Offshore Waters Forecast for Hawaii
National Weather Service Honolulu HI
1145 PM HST Sun Sep 27 2026

Hawaiian offshore waters beyond 40 nautical miles out to 240
nautical miles including the portion of the Papahanaumokuakea
Marine National Monument east of French Frigate Shoals

Seas given as significant wave height, which is the average height
of the highest 1/3 of the waves. Individual waves may be more than
twice the significant wave height.

PHZ105-281630-
1145 PM HST Sun Sep 27 2026

.Synopsis for the Hawaiian offshore waters...
The center of Hurricane Nolo will pass just outside of the far SW
offshore waters boundary as it turns toward the NW tonight and
Monday. Strong high pressure N of the area will maintain fresh to
strong trade winds outside of the Nolo wind field during this
time. Nolo will reenter far W offshore waters late Monday and
track N through Tuesday night. Nolo will then turn W and exit the
offshore waters by Thursday.

AT 1100 PM HST HURRICANE NOLO WAS CENTERED AT 16.5N 161.3W...MOVING
WNW AT 10 KT

NOLO FORECAST POSITIONS
800 AM HST MONDAY 17.5N 162.5W
800 PM HST MONDAY 19.2N 163.5W
800 AM HST TUESDAY 21.0N 163.7W
800 PM HST TUESDAY 22.4N 163.7W
800 AM HST WEDNESDAY 22.8N 163.9W
800 PM HST WEDNESDAY 23.0N 164.7W
800 PM HST THURSDAY 23.6N 166.9W
800 PM HST FRIDAY 24.0N 169.1W
800 PM HST SATURDAY 24.6N 174.0W
800 PM HST SUNDAY 26.3N 179.5W

PHZ180-281630-
Hawaiian Offshore Waters-
1145 PM HST Sun Sep 27 2026

...HURRICANE WARNING IN EFFECT...

.REST OF TONIGHT...Tropical storm conditions S of 20N W of 159W.
Elsewhere, E winds 15 to 30 kt and seas 9 to 14 ft. Isolated
thunderstorms near Hurricane Nolo.
.MONDAY...Hurricane conditions expected S of 22N W of 160W.
Elsewhere, E winds 15 to 30 kt, strongest W of 158W and seas 8 to
14 ft. Isolated thunderstorms near Hurricane Nolo.
.MONDAY NIGHT...Hurricane conditions expected S of 24N W of 161W.
Elsewhere NW half, E to SE winds 15 to 30 kt and seas 8 to 14 ft.
SE half, E to SE winds 10 to 15 kt and seas 7 to 8 ft. Isolated
thunderstorms near Hurricane Nolo.
.TUESDAY...Hurricane conditions expected S of 25N W of 161W.
Elsewhere NW half, E to SE winds 15 to 30 kt and seas 8 to 14 ft.
SE half, E to SE winds 10 to 15 kt and seas 6 to 8 ft. Isolated
thunderstorms near Hurricane Nolo.
.TUESDAY NIGHT...Hurricane conditions expected N of 20N W of
161W. Elsewhere NW half, E to SE winds 15 to 30 kt and seas 8 to 14 ft.
SE half, E to SE winds 10 to 15 kt and seas 6 to 8 ft. Isolated
thunderstorms near Hurricane Nolo.
.WEDNESDAY...Hurricane conditions possible W of 162W. Elsewhere NW
half, SE winds 15 to 30 kt and seas 8 to 12 ft. SE half, E to SE
winds 10 to 15 kt and seas 6 to 8 ft. Isolated thunderstorms near
Hurricane Nolo.
.THURSDAY...N of 20N W of 162W, SE winds 15 to 25 kt and seas 8
to 10 ft. Elsewhere, E to SE winds 10 to 15 kt and seas 5 to 8 ft.
.FRIDAY...NW half, SE winds 10 to 20 kt. SE half, E to SE winds
10 to 15 kt. Seas 5 to 7 ft.
```

---

### 26. Radar status/outage text messages

| Field | Value |
|---|---|
| **Resource ID** | ftm_radar_status |
| **Official source** | https://www.weather.gov/hfo/FTM |
| **Collected** | 2026-09-27T22:56:35.595779-10:00 HST |

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

### 27. State Forecast for Hawaii

| Field | Value |
|---|---|
| **Resource ID** | sfp_state_forecast |
| **Official source** | https://api.weather.gov/products/types/SFP/locations/HFO |
| **Collected** | 2026-09-28T04:52:20.638777-10:00 HST |

```text
000
FPHW60 PHFO 281447
SFPHFO

State Forecast for Hawaii
National Weather Service Honolulu HI
447 AM HST Mon Sep 28 2026

HIZ001-003-004-006-007-009>011-015>018-022-029>050-290415-
Kauai-Oahu-Maui-Molokai-Lanai-
447 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY FOR SOUTH FACING SHORES...

.TODAY...Sunny, breezy. Scattered showers windward and mountains.
Highs 87 to 92. East winds 15 to 25 mph. 
.TONIGHT...Mostly cloudy. Breezy. Isolated showers on Kauai. Lows
73 to 78. East winds 15 to 25 mph. 
.TUESDAY...Windward and mountains, occasional showers during the
day. Scattered showers at night. Leeward, numerous showers during
the day. Scattered showers at night. Highs 86 to 91. Lows 74 to
79. Southeast winds 15 to 20 mph. 
.WEDNESDAY...Mostly cloudy. On Kauai, numerous showers during the
day, then scattered showers at night. Oahu and Maui County,
scattered showers. Highs 85 to 90. Lows 73 to 78. East winds
15 to 20 mph. 
.THURSDAY...Mostly cloudy. On Kauai and Oahu, scattered showers
during the day, then isolated showers at night. Maui County,
isolated showers at night. Highs 84 to 89. Lows 73 to 78. East
winds around 15 mph. 
.FRIDAY...Mostly cloudy. Windward and mountains, scattered
showers. Leeward, isolated showers during the day. Scattered
showers at night. Highs 84 to 89. Lows 73 to 78. East winds
around 15 mph. 

HIZ023-026>028-051>054-290415-
Big Island of Hawaii-
447 AM HST Mon Sep 28 2026

...HIGH SURF ADVISORY FOR SOUTH AND WEST FACING SHORES...

.TODAY...Mostly sunny. Isolated showers. Highs 86 to 91. East
winds 15 to 20 mph. 
.TONIGHT...Partly cloudy. Lows 72 to 77. East winds around
15 mph. 
.TUESDAY...Mostly cloudy. Leeward, scattered showers during the
day. Windward, isolated showers during the day. Scattered showers
at night. Highs 85 to 90. Lows 72 to 77. Southeast winds around
15 mph. 
.WEDNESDAY...Mostly cloudy. Windward, isolated showers during the
day. Leeward, scattered showers during the day. Highs 85 to 90.
Lows 72 to 77. Variable winds to 15 mph. 
.THURSDAY...Mostly cloudy. Leeward, scattered showers during the
day. Windward, isolated showers at night. Highs 84 to 89. Lows
71 to 76. Northeast winds around 15 mph. 
.FRIDAY...Mostly cloudy. Windward, isolated showers during the
day, then scattered showers at night. Highs 83 to 88. Lows 71 to
76. Variable winds to 15 mph.
```

---

### 28. Statewide Surf Observations

| Field | Value |
|---|---|
| **Resource ID** | surfreports_statewide_observations |
| **Official source** | https://www.weather.gov/hfo/surfreports |
| **Collected** | Unknown HST |

```text
                        
522
SXHW80 PHFO 280115
OMRHFO

SURF OBSERVATIONS
NATIONAL WEATHER SERVICE HONOLULU HI
315 PM HST SUN SEP 27 2026

FULL FACE SURF OBSERVATIONS ARE TAKEN BY COUNTY LIFE GUARDS AND
COOPERATIVE OBSERVERS AND RELAYED TO THE NATIONAL WEATHER SERVICE
FOR DISSEMINATION. THESE OBSERVATIONS ARE NOT QUALITY CONTROLLED.

HIZ003-004-029>031-280100-
KAUAI-

LOCATION        TIME   SURF HEIGHT DIR   PER                  REMARKS
KEE
HAENA        1200 PM           4-5  NE    10
HANALEI      1200 PM           2-4  NE    10
ANAHOLA      1000 AM           4-6   E    12
KEALIA       1000 AM           6-8   E    12
LYDGATE      1000 AM           4-7   E    12
POIPU        1000 AM           6-8  SE     8
SALT POND    1000 AM           6-8   S     8
KEKAHA       1000 AM           6-8   S     8
$$

HIZ006-007-009>011-032>036-280100-
OAHU-

LOCATION        TIME   SURF HEIGHT DIR PER         WIND      REMARKS
DIAMOND HEAD
SUNSET
WAIKIKI      1000 AM           4-5                            CANOES
SANDY BEACH  1000 AM           6-8                       SHORE BREAK
MAKAPUU      1000 AM          8-12
EHUKAI       1000 AM           1-2
MAKAHA       1000 AM           1-2
$$

HIZ015>018-022-045>050-280100-
MAUI-MOLOKAI-LANAI-KAHOOLAWE-

LOCATION        TIME   SURF HEIGHT   DIR         WIND      REMARKS
KANAHA       1045 AM           0-1    NE      E 15-25
BALDWIN SHOR 1045 AM           0-1     E         E 25
BALDWIN OUTE 1045 AM           2-3     E
HOOKIPA
KAMAOLE I
KAMAOLE III
HANAKAOO
FLEMING
$$

HIZ023-026>028-051>054-280100-
BIG ISLAND OF HAWAII-

LOCATION        TIME   SURF HEIGHT   DIR         WIND      REMARKS
RICHARDSONS  1045 AM           3-4    NE         NE 5      -DZ OVC
HONOLII
PUNALU`U
ISAAC HALE   1045 AM           5-7     E      E 10-20        SUNNY
HAPUNA
KAHALUU      1045 AM           3-5     S        VRB 5          P/C
MAGIC SANDS  1045 AM           2-3    SW         SW 7        SUNNY
KUA BAY
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

### 29. Tsunami Bulletin product type reference

| Field | Value |
|---|---|
| **Resource ID** | hfo_tib_reference |
| **Official source** | https://forecast.weather.gov/product_types.php |
| **Collected** | 2026-09-28T05:18:22.183774-10:00 HST |

```text
National Weather Service

Toggle navigation

HOME

FORECAST

Local

Graphical

Aviation

Marine

Rivers and Lakes

Hurricanes

Severe Weather

Fire Weather

Sunrise/Sunset

Long Range Forecasts

Climate Prediction

Space Weather

PAST WEATHER

Past Weather

Astronomical Data

Certified Weather Data

SAFETY

INFORMATION

Wireless Emergency Alerts

Weather-Ready Nation

Brochures

Cooperative Observers

Daily Briefing

Damage/Fatality/Injury Statistics

Forecast Models

GIS Data Portal

NOAA Weather Radio

Publications

SKYWARN Storm Spotters

StormReady

TsunamiReady

Service Change Notices

EDUCATION

NEWS

SEARCH

Search For

NWS

All NOAA

ABOUT

About NWS

Organization

For NWS Employees

National Centers

Careers

Contact Us

Glossary

Social Media

NWS Transformation

NWS Weather Forecast Office Product Listing

Click on the product identifier or description to view products:

Product Identifier

Product Description

ABV

Rawinsonde Data Above 100 Millibars

ADA

Alarm/Alert Administrative Msg

ADM

Alert Administrative Message

ADR

NWS Administrative Message

ADV

Generic Space Environment Advisory

AFD

Area Forecast Discussion

AFM

Area Forecast Matrices

AFP

Area Forecast Product

AFW

Fire Weather Matrix

AGF

Agricultural Forecast

AGO

Agricultural Observations

ALT

Space Environment Alert

AQA

Air Quality Alert

AQI

Air Quality Index Statement

ASA

Air Stagnation Advisory

AVA

Avalanche Watch

AVG

Avalanche Weather Guidance

AVW

Avalanche Warning

AWO

Area Weather Outlook

AWS

Area Weather Summary

AWU

Area Weather Update

AWW

Airport Weather Warning

BLU

Blue Alert

BOY

Buoy Report

BRG

Coast Guard Observations

BRT

Hourly Roundup for Weather Radio

CAE

Child Abduction Emergency

CCF

Coded City Forecast

CDW

Civil Danger Warning

CEM

Civil Emergency Message

CF6

WFO Monthly/Daily Climate Data

CFP

Convective Forecast Product

CFW

Coastal Flood Warnings/Watches/Statements

CGR

Coast Guard Surface Report

CHG

Computer Hurricane Guidance

CLA

Climatological Report (Annual)

CLI

Climatological Report (Daily)

CLM

Climatological Report (Monthly)

CLQ

Climatological Report (Quarterly)

CLS

Climatological Report (Seasonal)

CLT

Climate Report

CMM

Coded Climatological Monthly Means

COD

Coded Analysis and Forecasts

CPF

Great Lakes Port Forecast

CUR

Routine Space Environment Products

CWA

Center (CWSU) Weather Advisory

CWF

Coastal Waters Forecast

CWS

Center (CWSU) Weather Statement

DAY

Routine Space Environment Product (Daily)

DDO

Daily Dispersion Outlook

DGT

Drought Information Statement

DMO

Practice/Demo Warning

DSA

Unnumbered Depression / Suspicious Area Advisory

DSM

ASOS Daily Summary

DSW

Dust Storm Warning and Dust Advisory

EFP

3 To 5 Day Extended Forecast

EOL

Average 6 To 10 Day Weather Outlook (Local)

EQI

Tsunami Bulletin

EQR

Earthquake Report

EQW

Earthquake Warning

ESF

Flood Potential Outlook

ESG

Extended Streamflow Guidance

ESP

Extended Streamflow Prediction

ESS

Water Supply Outlook

EVI

Evacuation Immediate

EWW

Extreme Wind Warning

FA0

Aviation Area Forecasts (Pacific)

FA1

Aviation Area Forecasts (Northeast)

FA2

Aviation Area Forecasts (Southeast)

FA3

Aviation Area Forecasts (North Central)

FA4

Aviation Area Forecasts (South Central)

FA5

Aviation Area Forecasts (Rocky Mountains)

FA6

Aviation Area Forecasts (West Coast)

FA7

Aviation Area Forecasts (Juneau, AK)

FA8

Aviation Area Forecasts (Anchorage, AK)

FA9

Aviation Area Forecasts (Fairbanks, AK)

FD0

24 Hr Fd Winds Aloft Fcst (45,000 and 53,000 Ft)

FD1

6 Hour Winds Aloft Forecast

FD2

12 Hour Winds Aloft Forecast

FD3

24 Hour Winds Aloft Forecast

FD4

Winds Aloft Forecast

FD5

Winds Aloft Forecast

FD6

Winds Aloft Forecast

FD7

Winds Aloft Forecast

FD8

6 Hour Fd Winds Aloft Fcst (45,000 and 53,000 Ft)

FD9

12 Hr Fd Winds Aloft Fcst (45,000 and 53,000 Ft)

FDI

Fire Danger Indices

FFA

Flash Flood Watch

FFG

Flash Flood Guidance

FFH

Headwater Guidance

FFS

Flash Flood Statement

FFW

Flash Flood Warning

FLN

National Flood Summary

FLS

Flood Statement

FLW

Flood Warning

FOF

Upper Wind Fallout Forecast

FRW

Fire Warning

FSH

Natl Marine Fisheries Administrative Service Message

FTM

WSR-88D Radar Outage Notification / Free Text Message

FTP

FOUS Prog Max/Min Temp/Pop Guidance

FWA

Fire Weather Administrative Message

FWD

Fire Weather Outlook Discussion

FWF

Routine Fire Wx Fcst (With/Without 6-10 Day Outlook)

FWL

Land Management Forecasts

FWM

Miscellaneous Fire Weather Product

FWN

Fire Weather Notification

FWO

Fire Weather Observation

FWS

Spot Forecast

FZL

Freezing Level Data (RADAT)

GLF

Great Lakes Forecast

GLS

Great Lakes Storm Summary

GRE

GREEN

HD1

RFC Derived QPF Data Product

HD2

RFC Derived QPF Data Product

HD3

RFC Derived QPF Data Product

HD4

RFC Derived QPF Data Product

HD7

RFC Derived QPF Data Product

HD8

RFC Derived QPF Data Product

HD9

RFC Derived QPF Data Product

HLS

Hurricane Local Statement

HMD

Hydrometeorological Discussion

HML

AHPS XML

HMW

Hazardous Materials Warning

HP1

RFC QPF Verification Product

HP2

RFC QPF Verification Product

HP3

RFC QPF Verification Product

HP4

RFC QPF Verification Product

HP5

RFC QPF Verification Product

HP6

RFC QPF Verification Product

HP7

RFC QPF Verification Product

HP8

RFC QPF Verification Product

HRR

Weather Roundup

HSF

High Seas Forecast

HWO

Hazardous Weather Outlook

HWR

Hourly Weather Roundup

HYD

Daily Hydrometeorological Products

HYM

Monthly Hydrometeorological Plain Language Product

ICE

Ice Forecast

IDM

Ice Drift Vectors

INI

ADMINISTR [NOUS51 KWBC]

IOB

Ice Observation

KPA

Keep Alive Message

LAE

Local Area Emergency

LCD

Preliminary Local Climatological Data

LCO

Local Cooperative Observation

LEW

Law Enforcement Warning

LFP

Local Forecast

LKE

Lake Stages

LLS

Low-Level Sounding

LOW

Low Temperatures

LSR

Local Storm Report

LTG

Lightning Data

MAN

Rawinsonde Observation Mandatory Levels

MAP

Mean Areal Precipitation

MAW

Amended Marine Forecast

MFM

Marine Forecast Matrix

MIM

Marine Interpretation Message

MIS

Miscellaneous Local Product

MOB

MOB Observations

MON

Routine Space Environment Product Issued Monthly

MRP

Techniques Development Laboratory Marine Product

MSM

ASOS Monthly Summary Message

MTR

METAR Formatted Surface Weather Observation

MTT

METAR Test Message

MVF

Marine Verification Coded Message

MWS

Marine Weather Statement

MWW

Marine Weather Message

NOU

Weather Reconnaisance Flights

NOW

Short Term Forecast

NOX

Data Mgt Message

NPW

Non-Precipitation Warnings / Watches / Advisories

NSH

Nearshore Marine Forecast

NUW

Nuclear Power Plant Warning

NWR

NOAA Weather Radio Forecast

OAV

Other Aviation Products

OBS

Observations

OFA

Offshore Aviation Area Forecast

OFF

Offshore Forecast

OMR

Other Marine Products

OPU

Other Public Products

OSO

Other Surface Observations

OSW

Ocean Surface Winds

OUA

Other Upper Air Data

OZF

Zone Forecast

PFM

Point Forecast Matrices

PFW

Fire Weather Point Forecast Matrices

PLS

Plain Language Ship Report

PMD

Prognostic Meteorological Discussion

PNS

Public Information Statement

POE

Probability of Exceed

PRB

Heat Index Forecast Tables

PRC

State Pilot Report Collective

PRE

Preliminary Forecasts

PSH

Post Storm Hurricane Report

PTS

Probabilistic Outlook Points

PWO

Public Severe Weather Outlook

PWS

Tropical Cyclone Probabilities

QPF

Quantitative Precipitation Forecast

QPS

Quantitative Precipitation Statement

RDF

Revised Digital Forecast

REC

Recreational Report

RER

Record Report

RET

EAS Activation Request

RFD

Rangeland Fire Danger Forecast

RFI

RFI Observation

RFR

Route Forecast

RFW

Red Flag Warning

RHW

Radiological Hazard Warning

RMT

Required Monthly Test

RNS

Rain Information Statement

RR1

Hydro-Met Data Report Part 1

RR2

Hydro-Met Data Report Part 2

RR3

Hydro-Met Data Report Part 3

RR4

Hydro-Met Data Report Part 4

RR5

Hydro-Met Data Report Part 5

RR6

Hydro-Met Data Report Part 6

RR7

Hydro-Met Data Report Part 7

RR8

Hydro-Met Data Report Part 8

RR9

Hydro-Met Data Report Part 9

RRA

Automated Hydrologic Observation Sta Report (AHOS)

RRM

Miscellaneous Hydrologic Data

RRS

HADS Data

RRY

ASOS SHEF Hourly Routine Test Message

RSD

Daily Snotel Data

RSM

Monthly Snotel Data

RTP

Regional Max/Min Temp and Precipitation Table

RVA

River Summary

RVD

Daily River Forecasts

RVF

River Forecast

RVI

River Ice Statement

RVM

Miscellaneous River Product

RVR

River Recreation Statement

RVS

River Statement

RWR

Regional Weather Roundup

RWS

Regional Weather Summary

RWT

Required Weekly Test

SAB

Special Avalanche Bulletin

SAF

Speci Agri Wx Fcst / Advisory / Flying Farmer Fcst Outlook

SAG

Snow Avalanche Guidance

SAT

APT Prediction

SAW

Prelim Notice of Watch & Cancellation Msg (Aviation)

SCC

Storm Summary

SCD

Supplementary Climatological Data (ASOS)

SCN

Soil Climate Analysis Network Data

SCP

Satellite Cloud Product

SCS

Selected Cities Summary

SDO

Supplementary Data Observation (ASOS)

SDS

Special Dispersion Statement

SEL

Severe Local Storm Watch and Watch Cancellation Msg

SEV

SPC Watch Point Information Message

SFP

State Forecast

SFT

Tabular State Forecast

SGL

Rawinsonde Observation Significant Levels

SHP

Surface Ship Report at Synoptic Time

SIG

International Sigmet / Convective Sigmet

SIM

Satellite Interpretation Message

SLS

Severe Local Storm Watch and Areal Outline

SMF

Smoke Management Weather Forecast

SMW

Special Marine Warning

SOO

SOO Product

SPE

Satellite Precipitation Estimates (TXUS20 KWBC)

SPF

Storm Strike Probability Bulletin (TPC)

SPS

Special Weather Statement

SPW

Shelter in Place Warning

SQW

Snow Squall Warning

SRD

Surf Discussion

SRF

Surf Forecast

SRG

Soaring Guidance

SSM

Main Synoptic Hour Surface Observation

STA

Network and Severe Weather Statistical Summaries

STD

Satellite Tropical Disturbance Summary

STO

Road Condition Reports (State Agencies)

STP

State Max/Min Temperature and Precipitation Table

STQ

Spot Forecast Request

SUM

Space Weather Message

SVR

Severe Thunderstorm Warning

SVS

Severe Weather Statement

SWO

Severe Storm Outlook Narrative (AC)

SWS

State Weather Summary

SYN

Regional Weather Synopsis

TAF

Terminal Aerodrome Forecast

TAP

Terminal Alerting Products

TAV

Travelers Forecast Table

TCA

Aviation Tropical Cyclone Advisory

TCD

Tropical Cyclone Discussion

TCE

Tropical Cyclone Position Estimate

TCM

Marine/Aviation Tropical Cyclone Advisory

TCP

Public Tropical Cyclone Advisory

TCS

Satellite Tropical Cyclone Summary

TCU

Tropical Cyclone Update

TCV

Tropical Cyclone Watch/Warning Break Points

TIB

Tsunami Bulletin

TID

Tide Report

TMA

Tsunami Tide/Seismic Message Acknowledgement

TOE

911 Telephone Outage Emergency

TOR

Tornado Warning

TPT

Temperature Precipitation Table (Natl and Intnl)

TSU

Tsunami Watch/Warning

TUV

Weather Bulletin

TVL

Travelers Forecast

TWB

Transcribed Weather Broadcast

TWD

Tropical Weather Discussion

TWO

Tropical Weather Outlook and Summary

TWS

Tropical Weather Summary

URN

Aircraft Reconnaissance

UVI

Ultraviolet Index

VAA

Volcanic Activity Advisory

VER

Forecast Verification Statistics

VFT

Terminal Aerodrome Forecast (TAF) Verification

VOW

Volcano Warning

WA0

Airmet (Pacific)

WA1

Airmet (Northeast)

WA2

Airmet (Southeast)

WA3

Airmet (North Central)

WA4

Airmet (South Central)

WA5

Airmet (Rocky Mountains)

WA6

Airmet (West Coast)

WA7

Airmet (Juneau, AK)

WA8

Airmet (Anchorage, AK)

WA9

Airmet (Fairbanks, AK)

WAR

Space Environment Warning

WAT

Space Environment Watch

WCN

Weather Watch Clearance Notification

WCR

Weekly Weather and Crop Report

WDA

Weekly Data for Agriculture

WDU

Warning Decision Update

WEK

Routine Space Environment Product Issued Weekly

WOU

Tornado/Severe Thunderstorm Watch

WS1

Sigmet (Northeast)

WS2

Sigmet (Southeast)

WS3

Sigmet (North Central)

WS4

Sigmet (South Central)

WS5

Sigmet (Rocky Mountains)

WS6

Sigmet (West Coast)

WST

Tropical Cyclone Sigmet

WSV

Volcanic Activity Sigmet

WSW

Winter Weather Warnings / Watches / Advisories

WWA

Watch Status Report

WWP

Severe Thunderstorm / Tornado Watch Probabilities

ZFP

Zone Forecast Product

US Dept of Commerce

National Oceanic and Atmospheric Administration

National Weather Service

1325 East West Highway

Silver Spring, MD 20910

Comments? Questions? Please Contact Us.

Disclaimer

Information Quality

Help

Glossary
```

---

_Generated automatically by the RootRecord weather reporting pipeline._
