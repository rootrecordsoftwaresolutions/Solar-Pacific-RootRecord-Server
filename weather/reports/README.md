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
| Honolulu | Partly cloudy | 81°F | 68°F | 64% | Northeast 23 gusts to 39 | 29.91S |
| Lihue | Light rain | 78°F | 73°F | 84% | East 23 | 29.97S |
| Kahului | Mostly cloudy | 78°F | 71°F | 79% | Northeast 15 gusts to 26 | 29.91S |
| Hilo | Cloudy | 79°F | 72°F | 79% | East 12 | 29.91S |
| Kona | Cloudy | 81°F | 77°F | 88% | South 9 | 29.77S |

_Source: locally collected NWS-HFO Regional Weather Roundup (RWR). Values are °F._

---

## 🌦️ Live Hawaiʻi Statewide Weather Report

> **Automatically regenerated from the latest locally collected official weather products.**

| Status | Coverage | Updated | Sections |
|---|---|---|---:|
| 🟢 Active | Hawaiʻi statewide | 2026-09-26T02:06:21-10:00 HST | 29 |

The report below is generated from the same current product sections as `Hawaii_State_Weather_Report_current.md`.

---

### 1. 7-Day Zone Forecasts (all islands)

| Field | Value |
|---|---|
| **Resource ID** | zfp_zone_forecast |
| **Official source** | https://api.weather.gov/products/types/ZFP/locations/HFO |
| **Collected** | 2026-09-25T23:18:55.895065-10:00 HST |

```text
000
FPHW50 PHFO 260856
ZFPHFO

Zone Forecast Product for Hawaii
National Weather Service Honolulu HI
1056 PM HST Fri Sep 25 2026

HIZ001-262315-
Niihau-
1056 PM HST Fri Sep 25 2026

...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT...Mostly cloudy. Breezy. Lows 72 to 78. East
winds 10 to 20 mph. 
.SATURDAY...Breezy. Partly sunny with isolated showers. Highs
81 to 87. Northeast winds 10 to 25 mph. Chance of rain
20 percent. 
.SATURDAY NIGHT...Partly cloudy. Windy. Lows 72 to 78. East winds
10 to 30 mph. 
.SUNDAY...Mostly sunny. Windy. Highs 81 to 87. East winds 15 to
35 mph increasing to 25 to 35 mph in the afternoon. Gusts up to
55 mph. 
.SUNDAY NIGHT...Partly cloudy in the evening then becoming mostly
cloudy. Windy. Lows 72 to 78. East winds 20 to 30 mph. 
.MONDAY...Partly sunny. Windy. Highs 81 to 87. East winds 20 to
35 mph. Gusts up to 50 mph increasing to 60 mph in the afternoon.
.MONDAY NIGHT...Windy. Mostly cloudy with isolated showers. Lows
72 to 78. East winds 20 to 30 mph with gusts to 50 mph. Chance of
rain 20 percent. 
.TUESDAY...Windy. Mostly cloudy with scattered showers. Highs
80 to 86. East winds 20 to 30 mph with gusts to 50 mph. Chance of
rain 40 percent. 
.TUESDAY NIGHT...Windy. Mostly cloudy with scattered showers.
Lows 72 to 78. East winds 20 to 35 mph. Gusts up to 50 mph
increasing to 60 mph after midnight. Chance of rain 40 percent. 
.WEDNESDAY...Windy. Mostly cloudy with scattered showers. Highs
80 to 86. Southeast winds 25 to 35 mph. Chance of rain
30 percent. 
.WEDNESDAY NIGHT...Windy. Mostly cloudy with scattered showers.
Lows 71 to 78. Southeast winds 20 to 30 mph. Chance of rain
30 percent. 
.THURSDAY...Mostly sunny. Windy. Scattered showers in the
morning, then isolated showers in the afternoon. Highs 80 to 85.
Southeast winds 20 to 35 mph with gusts to 55 mph. Chance of rain
30 percent. 
.THURSDAY NIGHT...Windy. Partly cloudy with scattered showers.
Lows 71 to 77. South winds 15 to 30 mph. Chance of rain
30 percent. 
.FRIDAY...Windy. Partly sunny with scattered showers. Highs 79 to
85. Southeast winds 10 to 30 mph. Chance of rain 40 percent. 

HIZ029-262315-
Kauai North-
Including Princeville, Hanalei, Na Pali State Park
1056 PM HST Fri Sep 25 2026

...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT...Breezy. Mostly cloudy with scattered showers.
Lows 67 to 76. East winds up to 20 mph increasing to 10 to 20 mph
after midnight. Chance of rain 50 percent. 
.SATURDAY...Breezy. Mostly cloudy with scattered showers. Highs
70 to 87. East winds up to 20 mph increasing to 10 to 25 mph in
the afternoon. Chance of rain 50 percent. 
.SATURDAY NIGHT...Windy. Mostly cloudy with isolated showers.
Lows 66 to 76. East winds 10 to 30 mph. Gusts up to 50 mph after
midnight. Chance of rain 20 percent. 
.SUNDAY...Partly sunny. Windy. Isolated showers in the morning.
Highs 71 to 88. East winds 10 to 30 mph. Chance of rain
20 percent. 
.SUNDAY NIGHT...Mostly cloudy. Breezy. Lows 67 to 76. East winds
10 to 25 mph. 
.MONDAY...Mostly cloudy. Breezy. Highs 72 to 89. East winds 10 to
20 mph. 
.MONDAY NIGHT...Mostly cloudy. Breezy. Lows 67 to 76. East winds
10 to 20 mph. 
.TUESDAY...Mostly cloudy. Isolated showers in the afternoon.
Highs 72 to 88. East winds 10 to 15 mph. Chance of rain
20 percent. 
.TUESDAY NIGHT...Mostly cloudy with isolated showers. Lows 67 to
76. East winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY...Mostly cloudy. Breezy. Scattered showers in the
morning, then isolated showers in the afternoon. Highs 71 to 87.
East winds 10 to 20 mph. Chance of rain 30 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with isolated showers. Lows
66 to 75. Southeast winds 10 to 15 mph. Chance of rain
20 percent. 
.THURSDAY...Mostly sunny with isolated showers. Highs 71 to 87.
Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows 66 to
75. Southeast winds up to 15 mph. Chance of rain 20 percent. 
.FRIDAY...Mostly sunny with isolated showers. Highs 71 to 87.
East winds up to 10 mph. Chance of rain 20 percent. 

HIZ030-262315-
Kauai East-
Including Lihue, Kapaa, Anahola
1056 PM HST Fri Sep 25 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST SUNDAY...
...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT...Breezy. Mostly cloudy with scattered showers.
Lows 68 to 77. Northeast winds 10 to 20 mph. Chance of rain
50 percent. 
.SATURDAY...Windy. Mostly cloudy with scattered showers. Highs
78 to 86. Northeast winds 10 to 30 mph. Chance of rain
50 percent. 
.SATURDAY NIGHT...Windy. Mostly cloudy with isolated showers.
Lows 68 to 78. Northeast winds 10 to 30 mph. Chance of rain
20 percent. 
.SUNDAY...Windy. Partly sunny with isolated showers. Highs 78 to
86. East winds 10 to 30 mph with gusts to 50 mph. Chance of rain
20 percent. 
.SUNDAY NIGHT...Mostly cloudy. Breezy. Isolated showers in the
evening, then scattered showers after midnight. Lows 68 to 77.
East winds 10 to 25 mph with gusts to 45 mph. Chance of rain
30 percent. 
.MONDAY...Mostly cloudy. Breezy. Scattered showers in the
morning, then isolated showers in the afternoon. Highs 78 to 86.
East winds 10 to 20 mph. Chance of rain 30 percent. 
.MONDAY NIGHT...Mostly cloudy with isolated showers. Lows 68 to
78. East winds 10 to 15 mph. Chance of rain 20 percent. 
.TUESDAY...Mostly cloudy. Isolated showers in the morning, then
scattered showers in the afternoon. Highs 78 to 86. East winds
10 to 15 mph. Chance of rain 30 percent. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows 68 to
77. East winds 10 to 15 mph. Chance of rain 40 percent. 
.WEDNESDAY...Mostly cloudy with scattered showers. Highs 77 to
85. East winds 10 to 15 mph. Chance of rain 40 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Breezy. Scattered showers in
the evening, then isolated showers after midnight. Lows 67 to 77.
Southeast winds 10 to 20 mph. Chance of rain 30 percent. 
.THURSDAY...Partly sunny with isolated showers. Highs 77 to 86.
Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows 67 to
77. Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny with scattered showers. Highs 78 to 86.
Southeast winds up to 10 mph. Chance of rain 40 percent. 

HIZ031-262315-
Kauai South-
Including Poipu, Kalaheo, Koloa
1056 PM HST Fri Sep 25 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST SUNDAY...
...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT...Breezy. Mostly cloudy with scattered showers.
Lows 72 to 78. Northeast winds 15 to 25 mph. Chance of rain
50 percent. 
.SATURDAY...Windy. Mostly cloudy with scattered showers. Highs
80 to 89. Northeast winds 15 to 30 mph. Chance of rain
50 percent. 
.SATURDAY NIGHT...Mostly cloudy. Windy. Isolated showers after
midnight. Lows 72 to 78. Northeast winds 20 to 30 mph with gusts
to 50 mph. Chance of rain 20 percent. 
.SUNDAY...Partly sunny. Windy. Isolated showers in the morning.
Highs 80 to 89. East winds 20 to 30 mph with gusts to 55 mph.
Chance of rain 20 percent. 
.SUNDAY NIGHT...Mostly cloudy. Windy. Isolated showers after
midnight. Lows 72 to 78. East winds 20 to 30 mph with gusts to
50 mph. Chance of rain 20 percent. 
.MONDAY...Mostly cloudy. Windy. Isolated showers in the morning.
Highs 81 to 89. East winds 15 to 30 mph. Chance of rain
20 percent. 
.MONDAY NIGHT...Mostly cloudy. Breezy. Isolated showers after
midnight. Lows 72 to 78. East winds 15 to 25 mph. Chance of rain
20 percent. 
.TUESDAY...Mostly cloudy. Breezy. Isolated showers in the
morning, then scattered showers in the afternoon. Highs 80 to 89.
East winds 15 to 20 mph. Chance of rain 30 percent. 
.TUESDAY NIGHT...Breezy. Mostly cloudy with scattered showers.
Lows 72 to 77. East winds 15 to 20 mph. Chance of rain
40 percent. 
.WEDNESDAY...Breezy. Mostly cloudy with scattered showers. Highs
79 to 88. East winds 15 to 25 mph. Chance of rain 40 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Breezy. Scattered showers in
the evening, then isolated showers after midnight. Lows 71 to 77.
Southeast winds 15 to 25 mph. Chance of rain 30 percent. 
.THURSDAY...Breezy. Partly sunny with scattered showers. Highs
79 to 89. Southeast winds 15 to 20 mph. Chance of rain
30 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows 71 to
77. Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny with scattered showers. Highs 79 to 89.
East winds 10 to 15 mph. Chance of rain 40 percent. 

HIZ003-262315-
Kauai Southwest-
Including Waimea, Waimea Canyon State Park, Hanapepe, Kekaha, 
Barking Sands
1056 PM HST Fri Sep 25 2026

...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT...Mostly cloudy with isolated showers. Lows
around 76 near the shore to around 66 above 3000 feet. East winds
up to 15 mph. Chance of rain 20 percent. 
.SATURDAY...Windy. Mostly cloudy with isolated showers. Highs
86 to 91 near the shore to around 77 above 3000 feet. East winds
up to 30 mph. Chance of rain 20 percent. 
.SATURDAY NIGHT...Mostly cloudy. Windy. Lows around 75 near the
shore to around 66 above 3000 feet. East winds up to 30 mph. 
.SUNDAY...Partly sunny in the morning then becoming mostly sunny.
Windy. Highs 77 to 90. East winds 10 to 30 mph with gusts to
55 mph. 
.SUNDAY NIGHT...Mostly cloudy. Breezy. Lows 65 to 77. East winds
10 to 25 mph with gusts to 45 mph. 
.MONDAY...Mostly cloudy. Breezy. Highs 77 to 91. East winds 10 to
25 mph with gusts to 50 mph. 
.MONDAY NIGHT...Mostly cloudy. Breezy. Lows 65 to 77. East winds
10 to 20 mph. 
.TUESDAY...Mostly cloudy. Breezy. Isolated showers in the
morning, then scattered showers in the afternoon. Highs 77 to 90.
East winds 10 to 20 mph. Chance of rain 30 percent. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows 65 to
77. East winds 10 to 15 mph. Chance of rain 30 percent. 
.WEDNESDAY...Breezy. Mostly cloudy with scattered showers. Highs
76 to 89. East winds 10 to 20 mph. Chance of rain 30 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Breezy. Scattered showers in
the evening, then isolated showers after midnight. Lows 64 to 76.
Southeast winds 10 to 20 mph. Chance of rain 30 percent. 
.THURSDAY...Partly sunny in the morning then becoming mostly
sunny. Breezy. Isolated showers. Highs 76 to 89. Southeast winds
10 to 20 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows 64 to
76. Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny with scattered showers. Highs 76 to 90.
Southeast winds around 10 mph. Chance of rain 30 percent. 

HIZ004-262315-
Kauai Mountains-
Including Kokee State Park
1056 PM HST Fri Sep 25 2026

...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT...Windy. Mostly cloudy with scattered showers.
Lows around 71 in the valleys to around 63 above 4000 feet. East
winds 10 to 30 mph with gusts to 50 mph. Chance of rain
50 percent. 
.SATURDAY...Windy. Mostly cloudy with scattered showers. Highs
74 to 82 in the valleys to around 68 above 4000 feet. East winds
10 to 30 mph. Chance of rain 50 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with isolated showers. Lows around 71 in the valleys to
around 63 above 4000 feet. East winds 10 to 35 mph with gusts to
60 mph increasing to 10 to 45 mph with gusts to 80 mph after
midnight. Chance of rain 20 percent. 
.SUNDAY... Tropical storm conditions possible. Partly sunny with
isolated showers. Highs 66 to 82. East winds 15 to 45 mph with
gusts to 80 mph. Chance of rain 20 percent. 
.SUNDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy. Isolated showers after midnight. Lows 62 to 73. East
winds 10 to 45 mph with gusts to 75 mph. Chance of rain
20 percent. 
.MONDAY... Tropical storm conditions possible. Mostly cloudy.
Isolated showers in the morning. Highs 66 to 83. East winds 10 to
45 mph. Gusts up to 75 mph decreasing to 65 mph in the afternoon.
Chance of rain 20 percent. 
.MONDAY NIGHT...Mostly cloudy. Windy. Isolated showers after
midnight. Lows 62 to 73. East winds 10 to 35 mph with gusts to
60 mph. Chance of rain 20 percent. 
.TUESDAY...Mostly cloudy. Windy. Isolated showers in the morning,
then scattered showers in the afternoon. Highs 66 to 83. East
winds 10 to 30 mph. Chance of rain 30 percent. 
.TUESDAY NIGHT...Windy. Mostly cloudy with scattered showers.
Lows 62 to 73. East winds 10 to 30 mph with gusts to 50 mph.
Chance of rain 30 percent. 
.WEDNESDAY...Windy. Mostly cloudy with scattered showers. Highs
65 to 81. East winds 10 to 30 mph. Chance of rain 30 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Windy. Scattered showers in the
evening, then isolated showers after midnight. Lows 61 to 72.
Southeast winds 10 to 35 mph with gusts to 55 mph. Chance of rain
30 percent. 
.THURSDAY...Breezy. Partly sunny with isolated showers. Highs
66 to 82. Southeast winds 10 to 25 mph. Gusts up to 45 mph in the
morning. Chance of rain 20 percent. 
.THURSDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Breezy. Isolated showers. Lows 61 to 72. Southeast
winds 10 to 20 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny with scattered showers. Highs 66 to 83.
Southeast winds 10 to 15 mph. Chance of rain 30 percent. 

HIZ032-262315-
East Honolulu-
Including Hawaii Kai, Aina Haina, Kahala
1056 PM HST Fri Sep 25 2026

...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT...Windy. Mostly cloudy with isolated showers.
Lows around 78. Northeast winds 25 to 30 mph. Chance of rain
20 percent. 
.SATURDAY...Windy. Mostly cloudy with scattered showers. Highs
81 to 88. East winds 25 to 35 mph. Chance of rain 40 percent. 
.SATURDAY NIGHT...Mostly cloudy. Windy. Lows around 78. Northeast
winds 30 to 35 mph shifting to the east 15 to 35 mph after
midnight. 
.SUNDAY...Partly sunny. Breezy. Highs 81 to 88. East winds 15 to
20 mph. 
.SUNDAY NIGHT...Partly cloudy in the evening then becoming mostly
cloudy. Breezy. Lows around 78. East winds 10 to 20 mph. 
.MONDAY...Partly sunny. Breezy. Highs 82 to 88. East winds 10 to
20 mph. 
.MONDAY NIGHT...Mostly cloudy. Lows around 78. East winds 10 to
15 mph. 
.TUESDAY...Partly sunny in the morning, then mostly sunny with
isolated showers in the afternoon. Highs 82 to 88. East winds
10 to 15 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Isolated showers. Lows around 77. East winds 10 to
15 mph. Chance of rain 20 percent. 
.WEDNESDAY...Partly sunny with isolated showers. Highs 81 to 87.
East winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Isolated showers. Lows around 77. Southeast winds
10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY...Mostly sunny with isolated showers. Highs 81 to 87.
Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows
around 77. Southeast winds around 10 mph. Chance of rain
20 percent. 
.FRIDAY...Partly sunny with scattered showers. Highs 81 to 88.
Light winds becoming east around 10 mph in the afternoon. Chance
of rain 30 percent. 

HIZ033-262315-
Honolulu Metro-
Including Honolulu, Waikiki
1056 PM HST Fri Sep 25 2026

...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT...Breezy. Mostly cloudy with isolated showers.
Lows around 78. East winds 20 to 25 mph. Chance of rain
20 percent. 
.SATURDAY...Windy. Partly sunny with scattered showers. Highs
83 to 88. East winds 25 to 30 mph. Chance of rain 50 percent. 
.SATURDAY NIGHT...Windy. Mostly cloudy with isolated showers.
Lows around 77. East winds 25 to 30 mph decreasing to 15 to
30 mph after midnight. Chance of rain 20 percent. 
.SUNDAY...Partly sunny. Breezy. Isolated showers in the morning.
Highs 83 to 88. East winds 15 to 20 mph. Chance of rain
20 percent. 
.SUNDAY NIGHT...Mostly cloudy. Breezy. Lows around 78. East winds
10 to 20 mph. 
.MONDAY...Partly sunny. Highs 84 to 89. East winds 10 to 15 mph. 
.MONDAY NIGHT...Mostly cloudy. Lows around 77. East winds 10 to
15 mph. 
.TUESDAY...Mostly cloudy in the morning, then mostly sunny with
isolated showers in the afternoon. Highs 84 to 89. East winds
10 to 15 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy with isolated showers. Lows around
77. East winds around 10 mph. Chance of rain 20 percent. 
.WEDNESDAY...Partly sunny with isolated showers. Highs 83 to 88.
East winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Isolated showers. Lows around 77. Southeast winds
10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY...Mostly sunny with isolated showers. Highs 83 to 88.
Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows
around 77. Southeast winds around 10 mph in the evening becoming
light. Chance of rain 20 percent. 
.FRIDAY...Partly sunny with scattered showers. Highs 84 to 89.
Light winds becoming east around 10 mph in the afternoon. Chance
of rain 40 percent. 

HIZ034-262315-
Ewa Plain-
Including Kapolei
1056 PM HST Fri Sep 25 2026

...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT...Breezy. Mostly cloudy with isolated showers.
Lows around 77. East winds 10 to 25 mph. Chance of rain
20 percent. 
.SATURDAY...Partly sunny. Windy. Scattered showers until late
afternoon, then isolated showers late in the afternoon. Highs
83 to 89. East winds 15 to 30 mph. Chance of rain 40 percent. 
.SATURDAY NIGHT...Mostly cloudy. Windy. Isolated showers after
midnight. Lows around 77. East winds 15 to 30 mph. Chance of rain
20 percent. 
.SUNDAY...Partly sunny. Windy. Isolated showers in the morning.
Highs 83 to 89. East winds 15 to 30 mph. Chance of rain
20 percent. 
.SUNDAY NIGHT...Mostly cloudy. Breezy. Lows around 77. East winds
15 to 20 mph. 
.MONDAY...Mostly sunny. Breezy. Highs 84 to 90. East winds 15 to
20 mph. Gusts up to 40 mph in the afternoon. 
.MONDAY NIGHT...Mostly cloudy. Lows around 77. East winds 10 to
15 mph. 
.TUESDAY...Partly sunny. Isolated showers in the afternoon. Highs
84 to 90. East winds 10 to 15 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy with isolated showers. Lows around
76. East winds around 10 mph. Chance of rain 20 percent. 
.WEDNESDAY...Breezy. Partly sunny with isolated showers. Highs
83 to 89. East winds 15 to 20 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Isolated showers. Lows around 76. Southeast winds
10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY...Mostly sunny with isolated showers. Highs 83 to 89.
Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows
around 76. Southeast winds around 10 mph in the evening becoming
light. Chance of rain 20 percent. 
.FRIDAY...Partly sunny with scattered showers. Highs 84 to 89.
Light winds becoming southeast around 10 mph in the afternoon.
Chance of rain 40 percent. 

HIZ006-262315-
Waianae Coast-
Including Nanakuli, Waianae, Makaha
1056 PM HST Fri Sep 25 2026

...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT...Mostly cloudy. Windy. Lows 72 to 79. East
winds up to 30 mph with gusts to 50 mph. 
.SATURDAY...Partly sunny. Windy. Scattered showers until late
afternoon, then isolated showers late in the afternoon. Highs
84 to 92. East winds 15 to 35 mph. Chance of rain 30 percent. 
.SATURDAY NIGHT...Mostly cloudy. Windy. Isolated showers after
midnight. Lows 72 to 79. East winds 10 to 35 mph with gusts to
55 mph. Chance of rain 20 percent. 
.SUNDAY...Partly sunny. Windy. Isolated showers in the morning.
Highs 85 to 92. East winds 10 to 30 mph. Chance of rain
20 percent. 
.SUNDAY NIGHT...Mostly cloudy. Breezy. Lows 72 to 79. East winds
10 to 20 mph. 
.MONDAY...Mostly sunny. Breezy. Highs 86 to 93. East winds 10 to
20 mph. 
.MONDAY NIGHT...Mostly cloudy. Lows 72 to 79. East winds up to
15 mph. 
.TUESDAY...Partly sunny. Highs 85 to 93. East winds up to 10 mph.
.TUESDAY NIGHT...Mostly cloudy with isolated showers. Lows 71 to
78. East winds up to 10 mph. Chance of rain 20 percent. 
.WEDNESDAY...Partly sunny with isolated showers. Highs 84 to 91.
Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Isolated showers. Lows 71 to 78. Southeast winds
10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY...Mostly sunny with isolated showers. Highs 84 to 91.
Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows 71 to
78. Southeast winds around 10 mph in the evening becoming light.
Chance of rain 20 percent. 
.FRIDAY...Partly sunny in the morning then becoming mostly sunny.
Scattered showers. Highs 84 to 91. Light winds becoming southeast
up to 10 mph in the afternoon. Chance of rain 40 percent. 

HIZ007-262315-
Oahu North Shore-
Including Waialua, Haleiwa, Pupukea
1056 PM HST Fri Sep 25 2026

...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT...Windy. Mostly cloudy with scattered showers.
Lows 71 to 78. East winds 10 to 30 mph with gusts to 50 mph.
Chance of rain 50 percent. 
.SATURDAY...Windy. Mostly cloudy with scattered showers. Highs
79 to 86. East winds 15 to 30 mph. Chance of rain 50 percent. 
.SATURDAY NIGHT...Windy. Mostly cloudy with isolated showers.
Lows 72 to 78. East winds 10 to 30 mph with gusts to 55 mph.
Chance of rain 20 percent. 
.SUNDAY...Partly sunny. Windy. Isolated showers in the morning.
Highs 80 to 87. East winds 10 to 30 mph. Chance of rain
20 percent. 
.SUNDAY NIGHT...Mostly cloudy. Breezy. Lows 72 to 78. East winds
10 to 20 mph. 
.MONDAY...Partly sunny. Breezy. Highs 80 to 88. East winds 10 to
20 mph. 
.MONDAY NIGHT...Mostly cloudy. Lows 71 to 78. East winds 10 to
15 mph. 
.TUESDAY...Partly sunny. Isolated showers in the afternoon. Highs
80 to 88. East winds 10 to 15 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy with isolated showers. Lows 71 to
77. East winds 10 to 15 mph decreasing to up to 15 mph after
midnight. Chance of rain 20 percent. 
.WEDNESDAY...Partly sunny with isolated showers. Highs 79 to 87.
East winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Isolated showers. Lows 71 to 77. Southeast winds
10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY...Mostly sunny with isolated showers. Highs 80 to 87.
Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows 70 to
77. Southeast winds up to 10 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny in the morning then becoming mostly sunny.
Scattered showers. Highs 81 to 88. Light winds becoming east
around 10 mph in the afternoon. Chance of rain 30 percent. 

HIZ035-262315-
Koolau Windward-
Including Kahuku, Laie, Punaluu, Kahaluu, Ahuimanu
1056 PM HST Fri Sep 25 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST SUNDAY...
...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT...Windy. Mostly cloudy with scattered showers.
Lows 70 to 80. East winds 15 to 30 mph with gusts to 50 mph.
Chance of rain 50 percent. 
.SATURDAY...Mostly cloudy. Windy. Numerous showers in the
morning, then scattered showers in the afternoon. Highs 74 to 85.
East winds 25 to 30 mph. Chance of rain 70 percent. 
.SATURDAY NIGHT...Windy. Mostly cloudy with isolated showers.
Lows 70 to 80. East winds 25 to 35 mph decreasing to 15 to 35 mph
after midnight. Gusts up to 60 mph. Chance of rain 20 percent. 
.SUNDAY...Windy. Partly sunny with isolated showers. Highs 74 to
86. East winds 15 to 35 mph with gusts to 60 mph. Chance of rain
20 percent. 
.SUNDAY NIGHT...Windy. Mostly cloudy with isolated showers. Lows
70 to 80. East winds 15 to 30 mph with gusts to 60 mph. Chance of
rain 20 percent. 
.MONDAY...Partly sunny. Windy. Isolated showers in the morning.
Highs 75 to 86. East winds 10 to 30 mph. Gusts up to 55 mph
decreasing to 45 mph in the afternoon. Chance of rain 20 percent.
.MONDAY NIGHT...Mostly cloudy. Breezy. Isolated showers after
midnight. Lows 70 to 79. East winds 10 to 25 mph with gusts to
45 mph. Chance of rain 20 percent. 
.TUESDAY...Breezy. Mostly cloudy with isolated showers. Highs
75 to 86. East winds 10 to 20 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Breezy. Mostly cloudy with isolated showers.
Lows 69 to 79. East winds 10 to 20 mph. Chance of rain
20 percent. 
.WEDNESDAY...Breezy. Partly sunny with isolated showers. Highs
74 to 85. East winds 10 to 20 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Breezy. Mostly cloudy with isolated showers.
Lows 69 to 79. Southeast winds 10 to 20 mph. Chance of rain
20 percent. 
.THURSDAY...Partly sunny in the morning then becoming mostly
sunny. Breezy. Isolated showers. Highs 75 to 85. Southeast winds
10 to 20 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Isolated showers. Lows 69 to 78. Southeast winds
10 to 15 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny with scattered showers. Highs 76 to 86.
East winds around 10 mph. Chance of rain 40 percent. 

HIZ036-262315-
Koolau Leeward-
Including Nuuanu, Manoa, Palolo
1056 PM HST Fri Sep 25 2026

...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT... Tropical storm conditions possible. Mostly
cloudy with scattered showers. Lows 68 to 77. Northeast winds
25 to 40 mph. Gusts up to 60 mph late in the evening. Chance of
rain 50 percent. 
.SATURDAY... Tropical storm conditions possible. Mostly cloudy.
Scattered showers early in the morning, then numerous showers
late in the morning. Scattered showers in the afternoon. Highs
71 to 86. East winds 25 to 40 mph. Chance of rain 70 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with isolated showers. Lows 68 to 77. Northeast winds
25 to 40 mph shifting to the east 15 to 40 mph after midnight.
Gusts up to 60 mph. Chance of rain 20 percent. 
.SUNDAY...Windy. Partly sunny with isolated showers. Highs 72 to
86. East winds 15 to 30 mph with gusts to 60 mph. Chance of rain
20 percent. 
.SUNDAY NIGHT...Breezy. Mostly cloudy with isolated showers. Lows
69 to 77. East winds 10 to 25 mph with gusts to 50 mph. Chance of
rain 20 percent. 
.MONDAY...Partly sunny. Breezy. Isolated showers in the morning.
Highs 73 to 86. East winds 10 to 25 mph with gusts to 50 mph.
Chance of rain 20 percent. 
.MONDAY NIGHT...Mostly cloudy. Breezy. Lows 68 to 77. East winds
10 to 20 mph. 
.TUESDAY...Partly sunny with isolated showers. Highs 73 to 86.
East winds 10 to 15 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Breezy. Mostly cloudy with isolated showers.
Lows 68 to 77. East winds 10 to 20 mph. Chance of rain
20 percent. 
.WEDNESDAY...Breezy. Partly sunny with isolated showers. Highs
72 to 86. East winds 10 to 20 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Breezy. Mostly cloudy with isolated showers.
Lows 67 to 76. Southeast winds 10 to 20 mph. Chance of rain
20 percent. 
.THURSDAY...Partly sunny in the morning then becoming mostly
sunny. Breezy. Isolated showers. Highs 72 to 86. Southeast winds
10 to 20 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows 67 to
76. Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny with scattered showers. Highs 73 to 86.
East winds up to 10 mph. Chance of rain 40 percent. 

HIZ009-262315-
Olomana-
Including Kailua, Kaneohe, Waimanalo
1056 PM HST Fri Sep 25 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST SUNDAY...
...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT...Breezy. Mostly cloudy with scattered showers.
Lows 73 to 79. East winds 15 to 25 mph with gusts to 45 mph.
Chance of rain 50 percent. 
.SATURDAY...Windy. Mostly cloudy with scattered showers. Highs
78 to 84. East winds 20 to 30 mph. Chance of rain 50 percent. 
.SATURDAY NIGHT...Windy. Mostly cloudy with isolated showers.
Lows 73 to 78. East winds 25 to 30 mph decreasing to 15 to 30 mph
after midnight. Gusts up to 50 mph. Chance of rain 20 percent. 
.SUNDAY...Windy. Partly sunny with isolated showers. Highs 78 to
85. East winds 15 to 30 mph. Chance of rain 20 percent. 
.SUNDAY NIGHT...Partly cloudy in the evening then becoming mostly
cloudy. Breezy. Lows 73 to 78. East winds 10 to 20 mph. 
.MONDAY...Partly sunny. Breezy. Highs 79 to 85. East winds 10 to
20 mph. 
.MONDAY NIGHT...Mostly cloudy. Lows 73 to 78. East winds 10 to
15 mph. 
.TUESDAY...Partly sunny with isolated showers. Highs 79 to 85.
East winds 10 to 15 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy with isolated showers. Lows 73 to
78. East winds around 10 mph. Chance of rain 20 percent. 
.WEDNESDAY...Partly sunny with isolated showers. Highs 78 to 84.
East winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with isolated showers. Lows
72 to 78. Southeast winds 10 to 15 mph. Chance of rain
20 percent. 
.THURSDAY...Partly sunny in the morning then becoming mostly
sunny. Isolated showers. Highs 78 to 85. Southeast winds 10 to
15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows 72 to
78. Southeast winds up to 10 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny with scattered showers. Highs 78 to 85.
Light winds. Chance of rain 40 percent. 

HIZ010-262315-
Central Oahu-
Including Mililani, Wahiawa, Pearl City
1056 PM HST Fri Sep 25 2026

...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT...Windy. Mostly cloudy with scattered showers.
Lows 71 to 76. East winds 10 to 30 mph with gusts to 50 mph.
Chance of rain 50 percent. 
.SATURDAY...Windy. Mostly cloudy with scattered showers. Highs
77 to 85. East winds 15 to 35 mph. Chance of rain 50 percent. 
.SATURDAY NIGHT...Windy. Mostly cloudy with isolated showers.
Lows around 73. East winds 15 to 35 mph. Chance of rain
20 percent. 
.SUNDAY...Partly sunny. Windy. Isolated showers in the morning.
Highs 78 to 86. East winds 15 to 30 mph. Chance of rain
20 percent. 
.SUNDAY NIGHT...Mostly cloudy. Breezy. Lows 71 to 76. East winds
10 to 20 mph. 
.MONDAY...Partly sunny. Breezy. Highs 79 to 87. East winds 10 to
20 mph. 
.MONDAY NIGHT...Mostly cloudy. Lows 71 to 76. East winds 10 to
15 mph. 
.TUESDAY...Mostly cloudy. Isolated showers in the afternoon.
Highs 79 to 87. East winds 10 to 15 mph. Chance of rain
20 percent. 
.TUESDAY NIGHT...Mostly cloudy with isolated showers. Lows 70 to
75. East winds around 10 mph. Chance of rain 20 percent. 
.WEDNESDAY...Partly sunny with isolated showers. Highs 78 to 85.
Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with isolated showers. Lows
70 to 75. Southeast winds 10 to 15 mph. Chance of rain
20 percent. 
.THURSDAY...Partly sunny with isolated showers. Highs 79 to 86.
Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Isolated showers. Lows around 72. Southeast winds
around 10 mph in the evening becoming light. Chance of rain
20 percent. 
.FRIDAY...Partly sunny with scattered showers. Highs 80 to 86.
Light winds becoming southeast around 10 mph in the afternoon.
Chance of rain 40 percent. 

HIZ011-262315-
Waianae Mountains-
Including Makakilo
1056 PM HST Fri Sep 25 2026

...WIND ADVISORY IN EFFECT FROM 6 AM SATURDAY TO 6 PM HST
SUNDAY...

.REST OF TONIGHT... Tropical storm conditions possible. Mostly
cloudy. Lows 67 to 77. East winds 20 to 40 mph. 
.SATURDAY... Tropical storm conditions possible. Mostly cloudy
with scattered showers. Highs 76 to 91. East winds 30 to 45 mph.
Chance of rain 40 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy. Isolated showers after midnight. Lows 66 to 76. East
winds 30 to 45 mph decreasing to 20 to 45 mph after midnight.
Chance of rain 20 percent. 
.SUNDAY...Partly sunny. Windy. Isolated showers in the morning.
Highs 77 to 91. East winds 20 to 30 mph with gusts to 50 mph.
Chance of rain 20 percent. 
.SUNDAY NIGHT...Mostly cloudy. Windy. Lows 67 to 76. East winds
10 to 30 mph. 
.MONDAY...Partly sunny in the morning then becoming mostly sunny.
Breezy. Highs 78 to 93. East winds 10 to 25 mph. 
.MONDAY NIGHT...Mostly cloudy. Breezy. Lows 67 to 76. East winds
10 to 20 mph. 
.TUESDAY...Partly sunny. Highs 77 to 92. East winds 10 to 15 mph.
.TUESDAY NIGHT...Mostly cloudy with isolated showers. Lows 67 to
76. East winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY...Breezy. Partly sunny with isolated showers. Highs
76 to 91. Southeast winds 10 to 20 mph. Chance of rain
20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Isolated showers. Lows 66 to 75. Southeast winds
10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY...Breezy. Mostly sunny with isolated showers. Highs
76 to 91. Southeast winds 10 to 20 mph. Chance of rain
20 percent. 
.THURSDAY NIGHT...Partly cloudy with isolated showers. Lows 66 to
75. Southeast winds around 10 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny in the morning then becoming mostly sunny.
Scattered showers. Highs 76 to 91. Southeast winds around 10 mph.
Chance of rain 30 percent. 

HIZ037-262315-
Molokai Windward-
Including Kalaupapa, Halawa Valley
1056 PM HST Fri Sep 25 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST SUNDAY...
...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible. Cloudy
with scattered showers and isolated thunderstorms. Locally heavy
rainfall possible. Lows 62 to 77. East winds 20 to 30 mph with
gusts to 50 mph. Chance of rain 50 percent. 
.SATURDAY... Tropical storm conditions possible. Mostly cloudy
with scattered showers and isolated thunderstorms. Locally heavy
rainfall possible. Highs 68 to 83. East winds 25 to 35 mph.
Chance of rain 50 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with isolated showers. Lows 61 to 77. East winds 25 to
40 mph with gusts to 60 mph increasing to 30 to 50 mph with gusts
to 75 mph after midnight. Chance of rain 20 percent. 
.SUNDAY... Tropical storm conditions possible. Partly sunny.
Isolated showers in the morning. Highs 68 to 84. East winds 30 to
50 mph with gusts to 80 mph. Chance of rain 20 percent. 
.SUNDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy. Lows 62 to 77. East winds 25 to 45 mph with gusts to
70 mph. 
.MONDAY... Tropical storm conditions possible. Partly sunny.
Highs 69 to 84. East winds 20 to 40 mph with gusts to 60 mph. 
.MONDAY NIGHT...Mostly cloudy. Windy. Lows 62 to 77. East winds
15 to 30 mph. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Breezy. Highs 69 to 84. East winds 15 to 25 mph. 
.TUESDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Breezy. Lows 62 to 77. East winds 15 to 25 mph. 
.WEDNESDAY...Windy. Partly sunny with isolated showers. Highs
68 to 84. East winds 15 to 30 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Windy. Partly cloudy with isolated showers.
Lows 61 to 77. East winds 15 to 30 mph. Chance of rain
20 percent. 
.THURSDAY...Mostly sunny. Breezy. Highs 68 to 84. East winds
15 to 20 mph. 
.THURSDAY NIGHT...Partly cloudy. Breezy. Lows 61 to 77. Southeast
winds 10 to 20 mph. 
.FRIDAY...Mostly sunny with isolated showers in the morning, then
partly sunny with scattered showers in the afternoon. Highs 69 to
84. East winds 10 to 15 mph. Chance of rain 30 percent. 

HIZ038-262315-
Molokai Southeast-
Including Pukoo
1056 PM HST Fri Sep 25 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST SUNDAY...
...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible. Cloudy
with scattered showers and isolated thunderstorms. Locally heavy
rainfall possible. Lows 62 to 78. East winds 25 to 35 mph. Gusts
up to 55 mph late in the evening. Chance of rain 40 percent. 
.SATURDAY... Tropical storm conditions expected. Mostly cloudy
with scattered showers and isolated thunderstorms. Locally heavy
rainfall possible. Highs 67 to 84. East winds 30 to 45 mph.
Chance of rain 50 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with isolated showers. Lows 62 to 77. East winds 25 to
45 mph. Gusts up to 80 mph after midnight. Chance of rain
20 percent. 
.SUNDAY... Tropical storm conditions possible. Partly sunny.
Highs 67 to 84. East winds 20 to 50 mph with gusts to 85 mph. 
.SUNDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy. Lows 62 to 78. East winds 15 to 40 mph with gusts to
75 mph. 
.MONDAY...Mostly sunny in the morning then becoming partly sunny.
Windy. Highs 68 to 85. East winds 15 to 35 mph. Gusts up to
60 mph in the morning. 
.MONDAY NIGHT...Mostly cloudy. Windy. Lows 62 to 78. East winds
15 to 30 mph decreasing to 10 to 20 mph after midnight. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Breezy. Highs 68 to 85. East winds 15 to 25 mph. 
.TUESDAY NIGHT...Partly cloudy. Breezy. Lows 62 to 78. East winds
10 to 25 mph. 
.WEDNESDAY...Partly sunny. Windy. Isolated showers in the
afternoon. Highs 67 to 84. East winds 15 to 30 mph. Chance of
rain 20 percent. 
.WEDNESDAY NIGHT...Partly cloudy. Windy. Isolated showers in the
evening. Lows 62 to 77. East winds 10 to 30 mph. Chance of rain
20 percent. 
.THURSDAY...Mostly sunny. Breezy. Highs 67 to 84. Southeast winds
10 to 20 mph. 
.THURSDAY NIGHT...Partly cloudy. Breezy. Lows 62 to 77. Southeast
winds 10 to 20 mph. 
.FRIDAY...Mostly sunny with isolated showers in the morning, then
partly sunny with scattered showers in the afternoon. Highs 67 to
85. East winds around 10 mph. Chance of rain 30 percent. 

HIZ039-262315-
Molokai North-
Including Hoolehua
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions expected. Mostly
cloudy with scattered showers and isolated thunderstorms. Locally
heavy rainfall possible. Lows 67 to 79. East winds 25 to 40 mph.
Gusts up to 60 mph late in the evening. Chance of rain
40 percent. 
.SATURDAY... Tropical storm conditions expected. Mostly cloudy.
Scattered showers and isolated thunderstorms until late
afternoon, then isolated showers and thunderstorms late in the
afternoon. Locally heavy rainfall possible. Highs 73 to 85. East
winds 30 to 45 mph. Chance of rain 40 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy. Isolated showers in the evening. Lows 67 to 78. East
winds 30 to 45 mph. Gusts up to 70 mph after midnight. Chance of
rain 20 percent. 
.SUNDAY... Tropical storm conditions possible. Partly sunny.
Highs 74 to 85. East winds 35 to 45 mph with gusts to 70 mph. 
.SUNDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy in the evening then becoming partly cloudy. Lows 68 to 79.
East winds 25 to 40 mph with gusts to 60 mph. 
.MONDAY...Partly sunny. Windy. Highs 75 to 87. East winds 25 to
35 mph with gusts to 55 mph. 
.MONDAY NIGHT...Mostly cloudy. Windy. Lows 67 to 79. East winds
15 to 30 mph. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Breezy. Highs 75 to 87. East winds 20 to 25 mph. 
.TUESDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Breezy. Lows 67 to 78. East winds 15 to 25 mph. 
.WEDNESDAY...Windy. Partly sunny with isolated showers. Highs
74 to 85. East winds 20 to 30 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Breezy. Mostly cloudy with isolated showers in
the evening, then partly cloudy after midnight. Lows 67 to 78.
East winds 15 to 25 mph. Chance of rain 20 percent. 
.THURSDAY...Mostly sunny. Breezy. Highs 74 to 85. Southeast winds
20 to 25 mph. 
.THURSDAY NIGHT...Partly cloudy. Breezy. Lows 67 to 78. Southeast
winds 10 to 20 mph. 
.FRIDAY...Breezy. Mostly sunny with isolated showers in the
morning, then partly sunny with scattered showers in the
afternoon. Highs 74 to 86. East winds 10 to 20 mph. Chance of
rain 30 percent. 

HIZ040-262315-
Molokai West-
Including Kepuhi
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible. Mostly
cloudy with scattered showers and isolated thunderstorms. Locally
heavy rainfall possible. Lows around 77. East winds 20 to 35 mph.
Gusts up to 60 mph late in the evening. Chance of rain
30 percent. 
.SATURDAY... Tropical storm conditions expected. Mostly cloudy.
Scattered showers and isolated thunderstorms in the morning, then
isolated showers and thunderstorms in the afternoon. Locally
heavy rainfall possible. Highs 81 to 88. East winds 25 to 40 mph.
Chance of rain 30 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy. Lows around 77. East winds 25 to 40 mph with gusts to
60 mph. 
.SUNDAY... Tropical storm conditions possible. Partly sunny.
Highs 82 to 88. East winds 25 to 40 mph with gusts to 60 mph. 
.SUNDAY NIGHT...Partly cloudy. Windy. Lows around 77. East winds
15 to 35 mph. 
.MONDAY...Partly sunny. Windy. Highs 83 to 89. East winds 15 to
30 mph. 
.MONDAY NIGHT...Mostly cloudy. Breezy. Lows around 77. East winds
10 to 25 mph. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Breezy. Highs 82 to 88. East winds 10 to 20 mph. 
.TUESDAY NIGHT...Partly cloudy. Breezy. Lows around 77. East
winds 10 to 20 mph. 
.WEDNESDAY...Breezy. Partly sunny with isolated showers. Highs
81 to 88. East winds 15 to 25 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Breezy. Isolated showers. Lows around 76.
Southeast winds 15 to 25 mph. Chance of rain 20 percent. 
.THURSDAY...Mostly sunny. Breezy. Highs 81 to 87. Southeast winds
15 to 20 mph. 
.THURSDAY NIGHT...Partly cloudy. Breezy. Lows around 76.
Southeast winds 10 to 20 mph. 
.FRIDAY...Partly sunny with scattered showers in the morning,
then mostly sunny with isolated showers in the afternoon. Highs
81 to 87. East winds 10 to 15 mph. Chance of rain 30 percent. 

HIZ041-262315-
Molokai Leeward South-
Including Kaunakakai, Maunaloa
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible. Mostly
cloudy with scattered showers and isolated thunderstorms. Locally
heavy rainfall possible. Lows 64 to 78. East winds 10 to 35 mph.
Chance of rain 40 percent. 
.SATURDAY... Tropical storm conditions expected. Mostly cloudy.
Scattered showers and isolated thunderstorms until late
afternoon, then isolated showers and thunderstorms late in the
afternoon. Locally heavy rainfall possible. Highs 70 to 89. East
winds 15 to 40 mph. Chance of rain 40 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy. Isolated showers in the evening. Lows 64 to 78. East
winds 10 to 40 mph with gusts to 60 mph. Chance of rain
20 percent. 
.SUNDAY...Partly sunny. Windy. Highs 71 to 90. East winds 15 to
35 mph with gusts to 60 mph. 
.SUNDAY NIGHT...Mostly cloudy in the evening then becoming partly
cloudy. Windy. Lows 64 to 78. East winds 10 to 30 mph with gusts
to 55 mph. 
.MONDAY...Mostly sunny in the morning then becoming partly sunny.
Breezy. Highs 72 to 91. East winds 10 to 25 mph. 
.MONDAY NIGHT...Mostly cloudy. Breezy. Lows 64 to 78. East winds
10 to 20 mph. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Highs 72 to 90. East winds 10 to 15 mph. 
.TUESDAY NIGHT...Partly cloudy. Lows 64 to 78. East winds 10 to
15 mph. 
.WEDNESDAY...Breezy. Partly sunny with isolated showers. Highs
71 to 90. East winds 10 to 20 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Breezy. Isolated showers. Lows 64 to 77. East
winds 10 to 20 mph. Chance of rain 20 percent. 
.THURSDAY...Mostly sunny. Breezy. Highs 71 to 90. Southeast winds
10 to 20 mph. 
.THURSDAY NIGHT...Partly cloudy. Lows 63 to 77. Southeast winds
up to 15 mph. 
.FRIDAY...Mostly sunny with isolated showers in the morning, then
partly sunny with scattered showers in the afternoon. Highs 71 to
90. East winds up to 10 mph. Chance of rain 30 percent. 

HIZ042-262315-
Lanai Windward-
Including Shipwreck Beach
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible. Mostly
cloudy with scattered showers and isolated thunderstorms. Locally
heavy rainfall possible. Lows 67 to 77. Northeast winds 10 to
35 mph. Chance of rain 30 percent. 
.SATURDAY... Tropical storm conditions expected. Mostly cloudy.
Scattered showers and isolated thunderstorms early in the
morning, then isolated showers and thunderstorms in the late
morning and afternoon. Locally heavy rainfall possible. Highs
78 to 85. Northeast winds 15 to 40 mph. Chance of rain
30 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy in the evening then becoming partly cloudy. Lows 67 to 77.
Northeast winds 10 to 40 mph with gusts to 60 mph increasing to
10 to 55 mph with gusts to 80 mph after midnight. 
.SUNDAY... Tropical storm conditions possible. Mostly sunny.
Highs 78 to 85. East winds 30 to 50 mph with gusts to 80 mph. 
.SUNDAY NIGHT... Tropical storm conditions possible. Partly
cloudy. Lows 68 to 78. Northeast winds 20 to 45 mph shifting to
the east 20 to 35 mph after midnight. 
.MONDAY...Mostly sunny in the morning then becoming partly sunny.
Windy. Highs 79 to 86. Northeast winds 15 to 30 mph. 
.MONDAY NIGHT...Mostly cloudy. Breezy. Lows 67 to 78. Northeast
winds 10 to 20 mph. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Breezy. Highs 78 to 86. Northeast winds 10 to 25 mph. 
.TUESDAY NIGHT...Partly cloudy. Breezy. Lows 67 to 77. East winds
10 to 20 mph. 
.WEDNESDAY...Partly sunny. Windy. Highs 77 to 85. East winds
15 to 30 mph with gusts to 50 mph. 
.WEDNESDAY NIGHT...Partly cloudy. Windy. Lows 67 to 77. East
winds 15 to 30 mph. Gusts up to 50 mph in the evening. 
.THURSDAY...Mostly sunny. Breezy. Highs 77 to 85. Southeast winds
15 to 25 mph with gusts to 45 mph. 
.THURSDAY NIGHT...Partly cloudy. Breezy. Lows 67 to 77. Southeast
winds 10 to 20 mph. 
.FRIDAY...Mostly sunny with isolated showers. Highs 77 to 85.
East winds up to 10 mph increasing to 10 to 15 mph in the
afternoon. Chance of rain 20 percent. 

HIZ043-262315-
Lanai Leeward-
Including Kaumalapau Harbor
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible. Mostly
cloudy with isolated showers and thunderstorms. Locally heavy
rainfall possible. Lows 73 to 79. Northeast winds 15 to 35 mph.
Chance of rain 20 percent. 
.SATURDAY... Tropical storm conditions expected. Mostly cloudy
with isolated showers and thunderstorms. Locally heavy rainfall
possible. Highs 81 to 88. Northeast winds 15 to 40 mph. Chance of
rain 20 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy in the evening then becoming partly cloudy. Lows 72 to 78.
Northeast winds 20 to 40 mph with gusts to 60 mph increasing to
20 to 50 mph with gusts to 85 mph after midnight. 
.SUNDAY... Tropical storm conditions possible. Mostly sunny.
Highs 81 to 88. East winds 15 to 50 mph with gusts to 80 mph. 
.SUNDAY NIGHT...Partly cloudy. Windy. Lows 73 to 79. East winds
10 to 35 mph with gusts to 65 mph. 
.MONDAY...Mostly sunny in the morning then becoming partly sunny.
Windy. Highs 82 to 88. Northeast winds 10 to 30 mph. 
.MONDAY NIGHT...Mostly cloudy. Breezy. Lows 73 to 78. Northeast
winds 10 to 20 mph. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Breezy. Highs 81 to 87. East winds 10 to 20 mph. 
.TUESDAY NIGHT...Partly cloudy. Breezy. Lows 72 to 78. East winds
10 to 20 mph. 
.WEDNESDAY...Mostly sunny. Windy. Isolated showers in the
afternoon. Highs 81 to 87. Southeast winds 15 to 30 mph with
gusts to 50 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Partly cloudy. Windy. Isolated showers in the
evening. Lows 72 to 78. Southeast winds 15 to 30 mph. Gusts up to
50 mph in the evening. Chance of rain 20 percent. 
.THURSDAY...Mostly sunny. Windy. Highs 80 to 86. Southeast winds
15 to 30 mph. 
.THURSDAY NIGHT...Partly cloudy. Breezy. Lows 72 to 77. Southeast
winds 10 to 20 mph. 
.FRIDAY...Mostly sunny. Scattered showers in the morning, then
isolated showers in the afternoon. Highs 80 to 86. East winds
10 to 15 mph. Chance of rain 30 percent. 

HIZ044-262315-
Lanai South-
Including Manele
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT...Breezy. Mostly cloudy with scattered showers
and isolated thunderstorms. Locally heavy rainfall possible. Lows
around 77. Northeast winds 10 to 20 mph. Chance of rain
30 percent. 
.SATURDAY...Breezy. Mostly cloudy with isolated showers and
thunderstorms. Locally heavy rainfall possible. Highs around 83.
Northeast winds 10 to 25 mph. Chance of rain 20 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy in the evening then becoming partly cloudy. Lows around
76. Northeast winds 10 to 25 mph increasing to 10 to 40 mph with
gusts to 70 mph after midnight. 
.SUNDAY... Tropical storm conditions possible. Mostly sunny in
the morning then becoming partly sunny. Highs around 83. East
winds 20 to 40 mph. Gusts up to 70 mph decreasing to 60 mph in
the afternoon. 
.SUNDAY NIGHT...Mostly cloudy in the evening then becoming partly
cloudy. Breezy. Lows 74 to 79. Northeast winds 10 to 20 mph. 
.MONDAY...Mostly sunny in the morning then becoming partly sunny.
Breezy. Highs around 83. East winds 10 to 20 mph. 
.MONDAY NIGHT...Mostly cloudy. Lows 74 to 79. Northeast winds
10 to 15 mph. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Highs around 82. East winds 10 to 15 mph. 
.TUESDAY NIGHT...Partly cloudy. Breezy. Lows 74 to 79. East winds
around 10 mph increasing to 15 to 20 mph after midnight. 
.WEDNESDAY...Partly sunny. Breezy. Isolated showers in the
afternoon. Highs 79 to 84. Southeast winds 15 to 20 mph. Chance
of rain 20 percent. 
.WEDNESDAY NIGHT...Partly cloudy. Breezy. Isolated showers in the
evening. Lows around 76. Southeast winds 15 to 25 mph. Chance of
rain 20 percent. 
.THURSDAY...Mostly sunny. Breezy. Highs around 81. Southeast
winds 15 to 25 mph. 
.THURSDAY NIGHT...Partly cloudy. Lows 73 to 78. Southeast winds
10 to 15 mph. 
.FRIDAY...Mostly sunny. Scattered showers in the morning, then
isolated showers in the afternoon. Highs around 81. Southeast
winds 10 to 15 mph. Chance of rain 30 percent. 

HIZ015-262315-
Lanai Mauka-
Including Lanai City
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions expected. Cloudy
with scattered showers and isolated thunderstorms. Locally heavy
rainfall possible. Lows 69 to 75. Northeast winds 15 to 40 mph.
Chance of rain 30 percent. 
.SATURDAY... Tropical storm conditions expected. Mostly cloudy.
Isolated showers and thunderstorms until late afternoon, then
scattered showers and isolated thunderstorms late in the
afternoon. Locally heavy rainfall possible. Highs 74 to 84.
Northeast winds 15 to 40 mph. Chance of rain 30 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy in the evening then becoming partly cloudy. Lows 69 to 74.
Northeast winds 15 to 40 mph with gusts to 60 mph increasing to
15 to 50 mph with gusts to 85 mph after midnight. 
.SUNDAY... Tropical storm conditions possible. Mostly sunny.
Highs 74 to 84. Northeast winds 25 to 50 mph. Gusts up to 85 mph
decreasing to 75 mph in the afternoon. 
.SUNDAY NIGHT...Partly cloudy. Windy. Lows 69 to 74. East winds
15 to 30 mph. 
.MONDAY...Mostly sunny in the morning then becoming partly sunny.
Breezy. Highs 75 to 84. Northeast winds 10 to 25 mph with gusts
to 45 mph. 
.MONDAY NIGHT...Mostly cloudy. Lows 69 to 74. Northeast winds
10 to 15 mph. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Breezy. Highs 74 to 83. East winds 10 to 20 mph. 
.TUESDAY NIGHT...Partly cloudy. Lows 69 to 74. East winds 10 to
15 mph. 
.WEDNESDAY...Partly sunny. Windy. Highs 73 to 82. Southeast winds
15 to 30 mph. 
.WEDNESDAY NIGHT...Partly cloudy. Breezy. Lows 69 to 74.
Southeast winds 15 to 25 mph. 
.THURSDAY...Mostly sunny in the morning then becoming partly
sunny. Breezy. Highs 73 to 82. Southeast winds 20 to 25 mph. 
.THURSDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Lows around 71. Southeast winds 10 to 15 mph. 
.FRIDAY...Mostly sunny with isolated showers. Highs 73 to 82.
East winds 10 to 15 mph. Chance of rain 20 percent. 

HIZ016-262315-
Kahoolawe-
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible. Mostly
cloudy with scattered showers and isolated thunderstorms. Locally
heavy rainfall possible. Lows 72 to 78. Northeast winds 15 to
30 mph with gusts to 50 mph. Chance of rain 40 percent. 
.SATURDAY... Tropical storm conditions expected. Mostly cloudy
with scattered showers and isolated thunderstorms. Locally heavy
rainfall possible. Highs 81 to 87. East winds 20 to 45 mph.
Chance of rain 40 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy in the evening then becoming partly cloudy. Lows 72 to 77.
East winds 20 to 50 mph. Gusts up to 75 mph after midnight. 
.SUNDAY... Tropical storm conditions possible. Mostly sunny in
the morning then becoming partly sunny. Highs 81 to 87. East
winds 25 to 45 mph with gusts to 70 mph increasing to 25 to
55 mph with gusts to 80 mph in the afternoon. 
.SUNDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy in the evening then becoming partly cloudy. Lows 72 to 77.
East winds 25 to 55 mph with gusts to 80 mph decreasing to 20 to
45 mph with gusts to 70 mph after midnight. 
.MONDAY... Tropical storm conditions possible. Mostly sunny in
the morning then becoming partly sunny. Highs 81 to 87. East
winds 15 to 35 mph increasing to 25 to 40 mph in the afternoon.
Gusts up to 60 mph. 
.MONDAY NIGHT...Mostly cloudy. Windy. Lows 72 to 78. East winds
10 to 30 mph with gusts to 50 mph. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Windy. Highs 80 to 87. East winds 15 to 30 mph. 
.TUESDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Windy. Lows 72 to 77. East winds 15 to 30 mph. 
.WEDNESDAY...Windy. Partly sunny in the morning, then mostly
sunny with isolated showers in the afternoon. Highs 80 to 86.
East winds 25 to 30 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Windy. Partly cloudy with isolated showers.
Lows 71 to 77. East winds 20 to 30 mph decreasing to 15 to 20 mph
after midnight. Chance of rain 20 percent. 
.THURSDAY...Mostly sunny. Breezy. Isolated showers in the
morning. Highs 79 to 85. Southeast winds 15 to 25 mph. Chance of
rain 20 percent. 
.THURSDAY NIGHT...Partly cloudy. Breezy. Lows 71 to 77. Southeast
winds 10 to 20 mph. 
.FRIDAY...Partly sunny in the morning then becoming mostly sunny.
Breezy. Scattered showers. Highs 79 to 85. East winds 10 to
20 mph. Chance of rain 30 percent. 

HIZ017-262315-
Maui Windward West-
Including Wailuku
1056 PM HST Fri Sep 25 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST SUNDAY...
...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible. Cloudy
with scattered showers and isolated thunderstorms. Locally heavy
rainfall possible. Lows 70 to 76 makai to around 61 mauka. East
winds 15 to 35 mph. Gusts up to 60 mph late in the evening.
Chance of rain 50 percent. 
.SATURDAY... Tropical storm conditions expected. Mostly cloudy
with scattered showers and isolated thunderstorms. Locally heavy
rainfall possible. Highs around 81 makai to around 64 mauka. East
winds 15 to 40 mph. Chance of rain 50 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with isolated showers. Lows 69 to 76 makai to around
60 mauka. East winds 15 to 50 mph. Gusts up to 90 mph after
midnight. Chance of rain 20 percent. 
.SUNDAY... Tropical storm conditions possible. Partly sunny.
Highs 64 to 86. East winds 25 to 50 mph with gusts to 90 mph. 
.SUNDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy. Lows 61 to 77. East winds 15 to 40 mph with gusts to
70 mph. 
.MONDAY...Partly sunny. Windy. Highs 65 to 87. East winds 10 to
30 mph with gusts to 60 mph. 
.MONDAY NIGHT...Mostly cloudy. Breezy. Lows 61 to 77. East winds
10 to 25 mph with gusts to 45 mph decreasing to 10 to 15 mph
after midnight. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Breezy. Highs 65 to 87. East winds 10 to 20 mph. 
.TUESDAY NIGHT...Mostly cloudy. Breezy. Lows 60 to 76. East winds
10 to 20 mph. 
.WEDNESDAY...Partly sunny. Breezy. Highs 64 to 86. East winds
10 to 25 mph. 
.WEDNESDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Breezy. Lows 60 to 76. East winds 10 to 25 mph. 
.THURSDAY...Mostly sunny. Breezy. Highs 64 to 86. Southeast winds
10 to 20 mph. 
.THURSDAY NIGHT...Partly cloudy. Lows 60 to 76. Southeast winds
10 to 15 mph. 
.FRIDAY...Mostly sunny with isolated showers. Highs 64 to 86.
Light winds becoming east up to 10 mph in the afternoon. Chance
of rain 20 percent. 

HIZ018-262315-
Maui Leeward West-
Including Lahaina, Kaanapali
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible. Mostly
cloudy with scattered showers and isolated thunderstorms. Locally
heavy rainfall possible. Lows 72 to 79. Northeast winds up to
35 mph increasing to 15 to 35 mph after midnight. Gusts up to
55 mph. Chance of rain 40 percent. 
.SATURDAY... Tropical storm conditions expected. Mostly cloudy
with scattered showers and isolated thunderstorms. Locally heavy
rainfall possible. Highs 79 to 87. Northeast winds 20 to 40 mph.
Chance of rain 40 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with isolated showers. Lows 71 to 78. Northeast winds
15 to 40 mph with gusts to 60 mph. Chance of rain 20 percent. 
.SUNDAY...Partly sunny. Windy. Highs 79 to 87. East winds 15 to
30 mph with gusts to 60 mph. 
.SUNDAY NIGHT...Mostly cloudy. Breezy. Lows 72 to 78. East winds
10 to 25 mph with gusts to 45 mph. 
.MONDAY...Partly sunny. Breezy. Highs 81 to 89. East winds 10 to
20 mph. 
.MONDAY NIGHT...Mostly cloudy. Lows 71 to 78. East winds 10 to
15 mph. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Highs 81 to 88. East winds up to 15 mph increasing to
10 to 15 mph in the afternoon. 
.TUESDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Lows 71 to 78. East winds up to 15 mph. 
.WEDNESDAY...Partly sunny. Breezy. Highs 80 to 87. East winds
10 to 20 mph. 
.WEDNESDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Lows 71 to 77. East winds 10 to 15 mph. 
.THURSDAY...Mostly sunny. Highs 80 to 87. Southeast winds 10 to
15 mph. 
.THURSDAY NIGHT...Partly cloudy. Lows 71 to 77. Southeast winds
up to 10 mph. 
.FRIDAY...Mostly sunny with isolated showers. Highs 80 to 87.
Light winds becoming east up to 10 mph in the afternoon. Chance
of rain 20 percent. 

HIZ045-262315-
Maui Central Valley North-
Including Kahului
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible. Mostly
cloudy with scattered showers and isolated thunderstorms. Locally
heavy rainfall possible. Lows around 75. Northeast winds 15 to
30 mph. Chance of rain 50 percent. 
.SATURDAY... Tropical storm conditions possible. Mostly cloudy
with scattered showers and isolated thunderstorms. Locally heavy
rainfall possible. Highs 81 to 88. Northeast winds 25 to 30 mph.
Chance of rain 50 percent. 
.SATURDAY NIGHT...Windy. Mostly cloudy with isolated showers.
Lows around 74. Northeast winds 20 to 30 mph with gusts to
55 mph. Chance of rain 20 percent. 
.SUNDAY...Windy. Partly sunny with isolated showers. Highs 82 to
88. East winds 30 to 35 mph. Chance of rain 20 percent. 
.SUNDAY NIGHT...Breezy. Mostly cloudy with isolated showers. Lows
71 to 76. East winds 10 to 25 mph. Chance of rain 20 percent. 
.MONDAY...Partly sunny. Windy. Highs 83 to 89. East winds 10 to
20 mph increasing to 15 to 30 mph in the afternoon. 
.MONDAY NIGHT...Mostly cloudy. Breezy. Lows 71 to 76. East winds
10 to 20 mph. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Breezy. Highs 82 to 89. East winds 15 to 25 mph. 
.TUESDAY NIGHT...Partly cloudy in the evening then becoming
mostly cloudy. Lows 71 to 76. East winds 10 to 15 mph. 
.WEDNESDAY...Partly sunny. Breezy. Highs 82 to 88. East winds
15 to 25 mph. 
.WEDNESDAY NIGHT...Mostly cloudy. Lows around 73. East winds
10 to 15 mph. 
.THURSDAY...Mostly sunny in the morning then becoming partly
sunny. Breezy. Highs 82 to 88. East winds 15 to 20 mph. 
.THURSDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Lows around 73. Southeast winds 10 to 15 mph. 
.FRIDAY...Mostly sunny with isolated showers. Highs 82 to 88.
Light winds becoming northeast 10 to 15 mph in the afternoon.
Chance of rain 20 percent. 

HIZ046-262315-
Maui Central Valley South-
Including Maalaea
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible. Mostly
cloudy with scattered showers and isolated thunderstorms. Locally
heavy rainfall possible. Lows 73 to 82. Northeast winds 10 to
35 mph. Chance of rain 30 percent. 
.SATURDAY... Tropical storm conditions possible. Mostly cloudy.
Scattered showers and isolated thunderstorms in the morning, then
isolated showers and thunderstorms in the afternoon. Locally
heavy rainfall possible. Highs around 88. Northeast winds 30 to
35 mph. Chance of rain 30 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with isolated showers. Lows 72 to 81. Northeast winds
30 to 35 mph with gusts to 60 mph becoming 20 to 40 mph with
gusts to 80 mph after midnight. Chance of rain 20 percent. 
.SUNDAY... Tropical storm conditions possible. Partly sunny.
Highs 86 to 91. Northeast winds 20 to 40 mph shifting to the east
30 to 40 mph in the afternoon. Gusts up to 80 mph. 
.SUNDAY NIGHT...Mostly cloudy. Windy. Lows 72 to 81. East winds
10 to 30 mph with gusts to 60 mph. 
.MONDAY...Partly sunny. Windy. Highs 87 to 92. East winds 10 to
25 mph increasing to 20 to 30 mph in the afternoon. Gusts up to
50 mph. 
.MONDAY NIGHT...Mostly cloudy. Breezy. Lows 71 to 81. East winds
10 to 20 mph. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Breezy. Highs around 89. East winds 10 to 20 mph. 
.TUESDAY NIGHT...Mostly cloudy. Lows 72 to 81. East winds 10 to
15 mph. 
.WEDNESDAY...Partly sunny. Breezy. Highs 86 to 91. East winds
15 to 25 mph. 
.WEDNESDAY NIGHT...Mostly cloudy. Breezy. Lows 72 to 80. East
winds 10 to 20 mph. 
.THURSDAY...Mostly sunny in the morning then becoming partly
sunny. Breezy. Highs around 88. Southeast winds 15 to 20 mph. 
.THURSDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Lows 71 to 80. Southeast winds 10 to 15 mph. 
.FRIDAY...Mostly sunny with isolated showers. Highs around 88.
East winds up to 10 mph increasing to 10 to 15 mph in the
afternoon. Chance of rain 20 percent. 

HIZ047-262315-
Windward Haleakala-
Including Haiku, Makawao, Hana
1056 PM HST Fri Sep 25 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST SUNDAY...
...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible. Cloudy
with numerous showers and isolated thunderstorms. Locally heavy
rainfall possible. Lows around 74 near the shore to around
59 near 5000 feet. East winds 15 to 30 mph with gusts to 50 mph.
Chance of rain 70 percent. 
.SATURDAY... Tropical storm conditions possible. Occasional
showers in the morning. Isolated thunderstorms through the day.
Numerous showers in the afternoon. Locally heavy rainfall
possible. Highs around 81 near the shore to around 66 near
5000 feet. East winds 15 to 35 mph. Chance of rain near
100 percent. 
.SATURDAY NIGHT...Windy. Mostly cloudy with scattered showers.
Lows 71 to 76 near the shore to around 57 near 5000 feet. East
winds 15 to 35 mph with gusts to 60 mph. Chance of rain
50 percent. 
.SUNDAY...Windy. Mostly cloudy with scattered showers. Highs
65 to 83. East winds 15 to 30 mph with gusts to 55 mph. Chance of
rain 40 percent. 
.SUNDAY NIGHT...Breezy. Mostly cloudy with isolated showers. Lows
57 to 76. East winds 10 to 25 mph with gusts to 45 mph. Chance of
rain 20 percent. 
.MONDAY...Partly sunny. Breezy. Highs 67 to 85. East winds 10 to
25 mph with gusts to 45 mph. 
.MONDAY NIGHT...Mostly cloudy. Breezy. Isolated showers after
midnight. Lows 57 to 76. East winds 10 to 20 mph. Chance of rain
20 percent. 
.TUESDAY...Mostly cloudy in the morning then becoming mostly
sunny. Breezy. Isolated showers. Highs 67 to 84. East winds 10 to
20 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy with isolated showers. Lows 57 to
76. East winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY...Breezy. Partly sunny with isolated showers. Highs
66 to 84. East winds 10 to 20 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Breezy. Mostly cloudy with isolated showers.
Lows 57 to 76. East winds 10 to 20 mph. Chance of rain
20 percent. 
.THURSDAY...Partly sunny with isolated showers. Highs 66 to 83.
East winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Mostly cloudy. Lows 57 to 76. Southeast winds
around 10 mph. 
.FRIDAY...Mostly sunny with isolated showers. Highs 66 to 83.
East winds up to 10 mph. Chance of rain 20 percent. 

HIZ048-262315-
Kipahulu-
Including Hamoa
1056 PM HST Fri Sep 25 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST SUNDAY...
...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT...Breezy. Cloudy with numerous showers and
isolated thunderstorms. Locally heavy rainfall possible. Lows
65 to 77. Northeast winds 15 to 25 mph. Chance of rain
70 percent. 
.SATURDAY... Tropical storm conditions possible. Mostly cloudy.
Occasional showers in the morning. Isolated thunderstorms through
the day. Numerous showers in the afternoon. Locally heavy
rainfall possible. Highs 68 to 84. Northeast winds 15 to 30 mph.
Chance of rain 90 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with scattered showers. Lows 64 to 76. Northeast winds
15 to 30 mph increasing to east 15 to 55 mph with gusts to 90 mph
after midnight. Chance of rain 50 percent. 
.SUNDAY... Tropical storm conditions possible. Mostly cloudy with
scattered showers. Highs 69 to 84. East winds 25 to 55 mph with
gusts to 90 mph. Chance of rain 40 percent. 
.SUNDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with isolated showers. Lows 65 to 77. East winds 20 to
50 mph with gusts to 80 mph. Chance of rain 20 percent. 
.MONDAY... Tropical storm conditions possible. Mostly cloudy.
Highs 70 to 84. East winds 20 to 45 mph with gusts to 70 mph. 
.MONDAY NIGHT...Mostly cloudy. Windy. Isolated showers after
midnight. Lows 65 to 77. East winds 15 to 35 mph with gusts to
55 mph. Chance of rain 20 percent. 
.TUESDAY...Windy. Partly sunny with isolated showers. Highs 69 to
83. East winds 15 to 30 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Windy. Mostly cloudy with isolated showers. Lows
65 to 76. East winds 10 to 30 mph. Gusts up to 50 mph after
midnight. Chance of rain 20 percent. 
.WEDNESDAY...Windy. Partly sunny with isolated showers. Highs
69 to 83. East winds 15 to 35 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Windy. Mostly cloudy with isolated showers.
Lows 65 to 76. East winds 15 to 30 mph. Chance of rain
20 percent. 
.THURSDAY...Breezy. Partly sunny with isolated showers. Highs
69 to 83. Southeast winds 15 to 25 mph. Chance of rain
20 percent. 
.THURSDAY NIGHT...Mostly cloudy. Breezy. Lows 65 to 76. Southeast
winds 10 to 25 mph. 
.FRIDAY...Mostly sunny with isolated showers. Highs 69 to 84.
East winds 10 to 15 mph. Chance of rain 20 percent. 

HIZ049-262315-
South Maui/Upcountry-
Including Kihei, Makena, Pukalani, Kula, Ulupalakua
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT...Mostly cloudy with isolated showers and
thunderstorms. Locally heavy rainfall possible. Lows around
75 near the shore to around 61 near 4000 feet. East winds up to
15 mph. Chance of rain 20 percent. 
.SATURDAY...Mostly cloudy. Isolated showers and thunderstorms in
the morning, then scattered showers and isolated thunderstorms in
the afternoon. Locally heavy rainfall possible. Highs around
88 near the shore to around 74 near 4000 feet. East winds up to
15 mph shifting to the south in the afternoon. Gusts up to
40 mph. Chance of rain 50 percent. 
.SATURDAY NIGHT...Breezy. Mostly cloudy with isolated showers.
Lows around 74 near the shore to around 60 near 4000 feet. East
winds up to 20 mph with gusts to 45 mph. Chance of rain
20 percent. 
.SUNDAY...Partly sunny. Breezy. Isolated showers in the morning.
Highs 71 to 90. East winds 10 to 25 mph. Chance of rain
20 percent. 
.SUNDAY NIGHT...Mostly cloudy. Lows 57 to 77. East winds 10 to
15 mph. 
.MONDAY...Partly sunny. Breezy. Highs 72 to 91. East winds 10 to
20 mph. Gusts up to 40 mph. 
.MONDAY NIGHT...Mostly cloudy. Lows 57 to 77. East winds 10 to
15 mph. Gusts up to 35 mph. 
.TUESDAY...Partly sunny in the morning then becoming mostly
sunny. Highs 71 to 90. East winds 10 to 15 mph. 
.TUESDAY NIGHT...Mostly cloudy. Lows 57 to 76. East winds around
10 mph. 
.WEDNESDAY...Partly sunny. Highs 70 to 89. East winds 10 to
15 mph. 
.WEDNESDAY NIGHT...Mostly cloudy. Lows 57 to 76. East winds
around 10 mph. 
.THURSDAY...Mostly sunny in the morning then becoming partly
sunny. Highs 70 to 89. Southeast winds 10 to 15 mph. 
.THURSDAY NIGHT...Mostly cloudy. Lows 57 to 76. Southeast winds
up to 10 mph in the evening becoming light. 
.FRIDAY...Mostly sunny with isolated showers. Highs 70 to 89.
Light winds becoming east up to 10 mph in the afternoon. Chance
of rain 20 percent. 

HIZ050-262315-
South Haleakala-
Including Kipahulu, Kaupo
1056 PM HST Fri Sep 25 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST SUNDAY...
...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible. Cloudy
with scattered showers and isolated thunderstorms. Locally heavy
rainfall possible. Lows 59 to 77. East winds 10 to 35 mph. Gusts
up to 55 mph late in the evening. Chance of rain 50 percent. 
.SATURDAY... Tropical storm conditions expected. Mostly cloudy
with scattered showers and isolated thunderstorms. Locally heavy
rainfall possible. Highs 75 to 87. East winds 20 to 40 mph.
Chance of rain 50 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with scattered showers. Lows 58 to 77. East winds 20 to
45 mph increasing to 20 to 55 mph with gusts to 85 mph after
midnight. Chance of rain 50 percent. 
.SUNDAY... Tropical storm conditions possible. Partly sunny.
Scattered showers in the morning, then isolated showers in the
afternoon. Highs 76 to 87. East winds 20 to 55 mph with gusts to
85 mph. Chance of rain 30 percent. 
.SUNDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with isolated showers. Lows 59 to 77. East winds 20 to
50 mph with gusts to 80 mph. Chance of rain 20 percent. 
.MONDAY... Tropical storm conditions possible. Partly sunny.
Highs 77 to 88. East winds 20 to 50 mph with gusts to 80 mph. 
.MONDAY NIGHT...Mostly cloudy. Windy. Lows 59 to 77. East winds
15 to 30 mph with gusts to 50 mph. 
.TUESDAY...Breezy. Partly sunny in the morning, then mostly sunny
with isolated showers in the afternoon. Highs 76 to 86. East
winds 15 to 25 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Breezy. Mostly cloudy with isolated showers.
Lows 58 to 76. East winds 15 to 25 mph. Gusts up to 45 mph after
midnight. Chance of rain 20 percent. 
.WEDNESDAY...Breezy. Partly sunny with isolated showers. Highs
75 to 86. East winds 15 to 25 mph with gusts to 45 mph. Chance of
rain 20 percent. 
.WEDNESDAY NIGHT...Breezy. Mostly cloudy with isolated showers.
Lows 58 to 76. East winds 15 to 25 mph with gusts to 45 mph.
Chance of rain 20 percent. 
.THURSDAY...Breezy. Partly sunny with isolated showers. Highs
75 to 85. East winds 10 to 25 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Mostly cloudy. Lows 58 to 76. East winds 10 to
15 mph. 
.FRIDAY...Mostly sunny with isolated showers. Highs 75 to 85.
East winds 10 to 15 mph. Chance of rain 20 percent. 

HIZ022-262315-
Haleakala Summit-
Including Haleakala National Park Above 6000 feet
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT...Breezy. Cloudy with scattered showers and
isolated thunderstorms. Locally heavy rainfall possible. Lows
around 56 at the visitor center to around 52 at the summit. East
winds 10 to 25 mph. Chance of rain 50 percent. 
.SATURDAY... Tropical storm conditions possible. Scattered
showers and isolated thunderstorms early in the morning, then
occasional showers and isolated thunderstorms in the late morning
and afternoon. Locally heavy rainfall possible. Highs around
63 at the visitor center to around 72 at the summit. East winds
10 to 30 mph decreasing to up to 30 mph in the afternoon. Chance
of rain near 100 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with scattered showers. Lows around 55 at the visitor
center to around 51 at the summit. East winds 10 to 30 mph
increasing to 15 to 45 mph with gusts to 75 mph after midnight.
Chance of rain 50 percent. 
.SUNDAY... Tropical storm conditions possible. Mostly cloudy.
Scattered showers in the morning, then isolated showers in the
afternoon. Highs 60 to 80. East winds 15 to 45 mph with gusts to
75 mph. Chance of rain 40 percent. 
.SUNDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with isolated showers. Lows 48 to 65. East winds 15 to
45 mph with gusts to 65 mph. Chance of rain 20 percent. 
.MONDAY... Tropical storm conditions possible. Partly sunny.
Highs 62 to 82. East winds 10 to 40 mph with gusts to 60 mph
decreasing to 10 to 30 mph in the afternoon. 
.MONDAY NIGHT...Mostly cloudy. Breezy. Lows 48 to 65. East winds
10 to 25 mph. 
.TUESDAY...Partly sunny. Isolated showers in the afternoon. Highs
61 to 82. East winds 10 to 15 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Breezy. Mostly cloudy with isolated showers.
Lows 49 to 66. East winds 10 to 20 mph. Chance of rain
20 percent. 
.WEDNESDAY...Mostly cloudy with isolated showers. Highs 61 to 81.
East winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Breezy. Isolated showers after
midnight. Lows 48 to 64. East winds 10 to 20 mph. Chance of rain
20 percent. 
.THURSDAY...Mostly cloudy with isolated showers. Highs 60 to 81.
East winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Mostly cloudy. Lows 48 to 64. Southeast winds
up to 10 mph. 
.FRIDAY...Mostly sunny with isolated showers. Highs 61 to 82.
Light winds. Chance of rain 20 percent. 

HIZ023-262315-
Kona-
Including Kailua-Kona, Kealakekua, Milolii
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WARNING IN EFFECT...
...HURRICANE WATCH IN EFFECT...

.REST OF TONIGHT...Cloudy with scattered showers and isolated
thunderstorms. Locally heavy rainfall possible. Lows 71 to
77 near the shore to around 61 near 5000 feet. Light winds.
Chance of rain 50 percent. 
.SATURDAY...Mostly cloudy. Scattered showers and isolated
thunderstorms until late afternoon, then numerous showers and
isolated thunderstorms late in the afternoon. Locally heavy
rainfall possible. Highs 86 to 92 near the shore to around
72 near 5000 feet. Light winds becoming southwest up to 10 mph in
the afternoon. Chance of rain 70 percent. 
.SATURDAY NIGHT...Mostly cloudy. Scattered showers in the
evening, then isolated showers after midnight. Lows 71 to 78 near
the shore to around 59 near 5000 feet. Southwest winds up to
10 mph shifting to the east after midnight. Gusts up to 30 mph.
Chance of rain 40 percent. 
.SUNDAY...Partly sunny with isolated showers. Highs 71 to 92.
East winds 10 to 15 mph shifting to the west in the afternoon.
Chance of rain 20 percent. 
.SUNDAY NIGHT...Mostly cloudy with isolated showers. Lows 56 to
80. East winds up to 10 mph. Chance of rain 20 percent. 
.MONDAY...Partly sunny with isolated showers. Highs 70 to 90.
East winds around 10 mph shifting to the southwest in the
afternoon. Gusts up to 30 mph. Chance of rain 20 percent. 
.MONDAY NIGHT...Mostly cloudy. Isolated showers in the evening.
Lows 56 to 79. East winds up to 10 mph. Chance of rain
20 percent. 
.TUESDAY...Mostly cloudy. Isolated showers in the afternoon.
Highs 69 to 90. West winds up to 10 mph. Chance of rain
20 percent. 
.TUESDAY NIGHT...Mostly cloudy with isolated showers. Lows 55 to
79. East winds up to 10 mph. Chance of rain 20 percent. 
.WEDNESDAY...Partly sunny with isolated showers. Highs 69 to 90.
Southwest winds up to 10 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with isolated showers. Lows
54 to 79. East winds around 10 mph. Chance of rain 20 percent. 
.THURSDAY...Partly sunny. Highs 68 to 90. South winds around
10 mph. 
.THURSDAY NIGHT...Mostly cloudy. Lows 54 to 79. Southeast winds
up to 10 mph in the evening becoming light. 
.FRIDAY...Mostly sunny with isolated showers. Highs 69 to 90.
Light winds becoming southwest up to 10 mph in the afternoon.
Chance of rain 20 percent. 

HIZ051-262315-
Big Island South-
Including Ocean View
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WARNING IN EFFECT...
...HURRICANE WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions expected with
hurricane conditions possible. Cloudy with numerous showers and
isolated thunderstorms. Locally heavy rainfall possible. Lows
around 78 near the shore to around 63 near 5000 feet. Northeast
winds 10 to 40 mph with gusts to 60 mph. Chance of rain
70 percent. 
.SATURDAY... Tropical storm conditions expected with hurricane
conditions possible. Mostly cloudy. Numerous showers and isolated
thunderstorms early in the morning, then occasional showers and
isolated thunderstorms in the late morning and afternoon. Locally
heavy rainfall possible. Highs around 85 near the shore to around
70 near 5000 feet. Northeast winds 10 to 45 mph decreasing to up
to 40 mph in the afternoon. Chance of rain 90 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with scattered showers. Lows around 77 near the shore to
around 62 near 5000 feet. East winds 15 to 45 mph. Chance of rain
50 percent. 
.SUNDAY... Tropical storm conditions possible. Partly sunny with
isolated showers. Highs 70 to 86. East winds 20 to 40 mph with
gusts to 60 mph. Chance of rain 20 percent. 
.SUNDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with isolated showers. Lows 60 to 80. East winds 15 to
30 mph with gusts to 50 mph increasing to 20 to 40 mph with gusts
to 60 mph after midnight. Chance of rain 20 percent. 
.MONDAY...Windy. Partly sunny with isolated showers. Highs 70 to
87. East winds 15 to 35 mph. Gusts up to 60 mph decreasing to
50 mph in the afternoon. Chance of rain 20 percent. 
.MONDAY NIGHT...Windy. Mostly cloudy with isolated showers. Lows
60 to 79. East winds 15 to 30 mph. Chance of rain 20 percent. 
.TUESDAY...Breezy. Partly sunny with isolated showers. Highs
69 to 86. East winds 10 to 25 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Breezy. Mostly cloudy with isolated showers.
Lows 60 to 79. East winds 15 to 20 mph. Chance of rain
20 percent. 
.WEDNESDAY...Breezy. Partly sunny with isolated showers. Highs
68 to 85. East winds 10 to 25 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Breezy. Mostly cloudy with isolated showers.
Lows 60 to 79. East winds 10 to 20 mph. Chance of rain
20 percent. 
.THURSDAY...Breezy. Mostly cloudy with isolated showers. Highs
68 to 85. East winds 10 to 20 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Mostly cloudy with isolated showers. Lows 60 to
79. East winds 10 to 15 mph. Chance of rain 20 percent. 
.FRIDAY...Mostly sunny with isolated showers. Highs 69 to 85.
East winds 10 to 15 mph. Chance of rain 20 percent. 

HIZ052-262315-
Big Island Southeast-
Including South Point, Pahala
1056 PM HST Fri Sep 25 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST SUNDAY...
...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WARNING IN EFFECT...
...HURRICANE WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible.
Occasional showers and isolated thunderstorms. Locally heavy
rainfall possible. Lows 72 to 77 near the shore to 60 to 65 near
4000 feet. Northeast winds 20 to 35 mph with gusts to 55 mph.
Chance of rain near 100 percent. 
.SATURDAY... Tropical storm conditions possible. Occasional
showers and isolated thunderstorms. Locally heavy rainfall
possible. Highs 80 to 87 near the shore to 68 to 73 near
4000 feet. Northeast winds 15 to 35 mph. Chance of rain near
100 percent. 
.SATURDAY NIGHT...Windy. Mostly cloudy with scattered showers.
Lows 70 to 76 near the shore to 57 to 63 near 4000 feet.
Northeast winds 15 to 35 mph with gusts to 60 mph. Chance of rain
50 percent. 
.SUNDAY...Mostly cloudy. Windy. Scattered showers in the morning,
then isolated showers in the afternoon. Highs 67 to 87. Northeast
winds 15 to 35 mph with gusts to 60 mph. Chance of rain
50 percent. 
.SUNDAY NIGHT...Breezy. Mostly cloudy with isolated showers. Lows
57 to 78. Northeast winds 10 to 25 mph with gusts to 55 mph.
Chance of rain 20 percent. 
.MONDAY...Breezy. Partly sunny with isolated showers. Highs 69 to
89. East winds 10 to 20 mph with gusts to 45 mph. Chance of rain
20 percent. 
.MONDAY NIGHT...Mostly cloudy with isolated showers. Lows 58 to
78. Northeast winds 10 to 15 mph decreasing to up to 15 mph after
midnight. Chance of rain 20 percent. 
.TUESDAY...Mostly cloudy with isolated showers. Highs 69 to 88.
East winds 10 to 15 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows 58 to
78. East winds up to 15 mph. Chance of rain 40 percent. 
.WEDNESDAY...Partly sunny. Scattered showers in the morning, then
isolated showers in the afternoon. Highs 68 to 87. East winds
10 to 15 mph. Chance of rain 40 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with isolated showers. Lows
57 to 78. East winds up to 15 mph. Chance of rain 20 percent. 
.THURSDAY...Mostly cloudy with isolated showers. Highs 68 to 88.
Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Mostly cloudy with isolated showers. Lows 57 to
78. East winds up to 10 mph. Chance of rain 20 percent. 
.FRIDAY...Partly sunny in the morning then becoming mostly sunny.
Scattered showers. Highs 69 to 89. East winds up to 10 mph.
Chance of rain 40 percent. 

HIZ053-262315-
Big Island East-
Including Hilo, Volcano, Pahoa, Mountain View, Laupahoehoe
1056 PM HST Fri Sep 25 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST SUNDAY...
...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WARNING IN EFFECT...
...HURRICANE WATCH IN EFFECT...

.REST OF TONIGHT...Breezy. Occasional showers and isolated
thunderstorms. Locally heavy rainfall possible. Lows 68 to
76 near the shore to around 62 at 4000 feet. Northeast winds
10 to 25 mph. Chance of rain near 100 percent. 
.SATURDAY...Breezy. Occasional showers and isolated
thunderstorms. Locally heavy rainfall possible. Highs 78 to
84 near the shore to 63 to 68 at 4000 feet. Northeast winds 10 to
20 mph. Chance of rain near 100 percent. 
.SATURDAY NIGHT...Cloudy and breezy. Occasional showers in the
evening, then numerous showers after midnight. Lows 67 to 75 near
the shore to 57 to 62 at 4000 feet. East winds up to 20 mph.
Chance of rain 90 percent. 
.SUNDAY...Mostly cloudy. Breezy. Numerous showers in the morning,
then scattered showers in the afternoon. Highs 64 to 85. East
winds 10 to 20 mph. Chance of rain 70 percent. 
.SUNDAY NIGHT...Mostly cloudy with isolated showers. Lows 55 to
78. East winds up to 15 mph. Chance of rain 20 percent. 
.MONDAY...Mostly cloudy with isolated showers. Highs 67 to 85.
Southeast winds up to 15 mph shifting to the east in the
afternoon. Chance of rain 20 percent. 
.MONDAY NIGHT...Mostly cloudy with scattered showers. Lows 56 to
78. South winds up to 15 mph. Chance of rain 40 percent. 
.TUESDAY...Partly sunny with scattered showers. Highs 66 to 85.
Southeast winds around 10 mph. Chance of rain 40 percent. 
.TUESDAY NIGHT...Mostly cloudy with scattered showers. Lows 56 to
78. Southeast winds up to 10 mph. Chance of rain 40 percent. 
.WEDNESDAY...Mostly cloudy. Scattered showers in the morning,
then isolated showers in the afternoon. Highs 66 to 84. Southeast
winds 10 to 15 mph. Chance of rain 40 percent. 
.WEDNESDAY NIGHT...Mostly cloudy with isolated showers. Lows
56 to 78. Southeast winds 10 to 15 mph. Chance of rain
20 percent. 
.THURSDAY...Mostly cloudy with isolated showers. Highs 66 to 84.
Southeast winds 10 to 15 mph. Chance of rain 20 percent. 
.THURSDAY NIGHT...Mostly cloudy with isolated showers. Lows 56 to
78. Southeast winds up to 10 mph. Chance of rain 20 percent. 
.FRIDAY...Mostly sunny. Scattered showers in the morning, then
isolated showers in the afternoon. Highs 66 to 85. Light winds
becoming east around 10 mph in the afternoon. Chance of rain
40 percent. 

HIZ054-262315-
Big Island North-
Including Honokaa, Kamuela, Waipio Valley, Hawi
1056 PM HST Fri Sep 25 2026

...HIGH SURF ADVISORY IN EFFECT UNTIL 6 PM HST SUNDAY...
...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WARNING IN EFFECT...
...HURRICANE WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions expected with
hurricane conditions possible. Cloudy with numerous showers and
isolated thunderstorms. Locally heavy rainfall possible. Lows
68 to 75 near the shore to 62 to 70 near 3000 feet. East winds
20 to 40 mph. Gusts up to 65 mph late in the evening. Chance of
rain 70 percent. 
.SATURDAY... Tropical storm conditions expected with hurricane
conditions possible. Mostly cloudy with numerous showers and
isolated thunderstorms. Locally heavy rainfall possible. Highs
63 to 84. East winds 15 to 40 mph. Chance of rain 70 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with scattered showers. Lows 67 to 75 near the shore to
61 to 69 near 3000 feet. East winds 10 to 40 mph. Gusts up to
60 mph increasing to 80 mph after midnight. Chance of rain
50 percent. 
.SUNDAY...Partly sunny. Windy. Isolated showers in the morning.
Highs 65 to 85. East winds 10 to 35 mph with gusts to 75 mph.
Chance of rain 20 percent. 
.SUNDAY NIGHT...Mostly cloudy. Breezy. Lows 55 to 76. East winds
10 to 25 mph with gusts to 50 mph. 
.MONDAY...Partly sunny. Breezy. Isolated showers in the
afternoon. Highs 67 to 86. East winds 10 to 20 mph. Chance of
rain 20 percent. 
.MONDAY NIGHT...Mostly cloudy. Isolated showers in the evening.
Lows 56 to 76. Southeast winds 10 to 15 mph. Chance of rain
20 percent. 
.TUESDAY...Partly sunny in the morning, then mostly sunny with
isolated showers in the afternoon. Highs 66 to 85. East winds
10 to 15 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Partly cloudy with isolated showers in the
evening, then mostly cloudy after midnight. Lows 56 to 76.
Southeast winds around 10 mph. Chance of rain 20 percent. 
.WEDNESDAY...Partly sunny. Isolated showers in the afternoon.
Highs 66 to 85. East winds 10 to 15 mph. Chance of rain
20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Isolated showers in the
evening. Lows 55 to 75. Southeast winds around 10 mph. Chance of
rain 20 percent. 
.THURSDAY...Partly sunny. Isolated showers in the afternoon.
Highs 65 to 84. East winds around 10 mph. Chance of rain
20 percent. 
.THURSDAY NIGHT...Mostly cloudy with isolated showers in the
evening, then partly cloudy after midnight. Lows 55 to 75.
Southeast winds around 10 mph in the evening becoming light.
Chance of rain 20 percent. 
.FRIDAY...Mostly sunny. Isolated showers in the afternoon. Highs
65 to 84. Light winds becoming east around 10 mph in the
afternoon. Chance of rain 20 percent. 

HIZ026-262315-
Kohala-
Including Kawaihae, Waikoloa, Waikii, Puuanahulu
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WARNING IN EFFECT...
...HURRICANE WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions expected with
hurricane conditions possible. Cloudy with scattered showers and
isolated thunderstorms. Locally heavy rainfall possible. Lows
73 to 78 near the shore to 59 to 64 above 4000 feet. East winds
up to 40 mph with gusts to 65 mph. Chance of rain 50 percent. 
.SATURDAY... Tropical storm conditions expected with hurricane
conditions possible. Mostly cloudy. Isolated showers and
thunderstorms in the morning, then scattered showers and isolated
thunderstorms in the afternoon. Locally heavy rainfall possible.
Highs 84 to 91 near the shore to around 72 above 4000 feet. East
winds up to 40 mph with gusts to 60 mph. Chance of rain
50 percent. 
.SATURDAY NIGHT... Tropical storm conditions possible. Mostly
cloudy with isolated showers. Lows 72 to 78 near the shore to
57 to 63 above 4000 feet. East winds up to 45 mph. Chance of rain
20 percent. 
.SUNDAY...Partly sunny. Windy. Isolated showers in the morning.
Highs 70 to 92. Northeast winds 10 to 35 mph with gusts to
60 mph. Chance of rain 20 percent. 
.SUNDAY NIGHT...Mostly cloudy. Breezy. Lows 56 to 77. East winds
10 to 20 mph. 
.MONDAY...Partly sunny. Highs 69 to 93. East winds 10 to 15 mph
shifting to the northwest in the afternoon. 
.MONDAY NIGHT...Mostly cloudy. Lows 56 to 77. Southeast winds
around 10 mph in the evening becoming light. 
.TUESDAY...Partly sunny. Isolated showers in the afternoon. Highs
68 to 92. Northwest winds up to 10 mph. Chance of rain
20 percent. 
.TUESDAY NIGHT...Mostly cloudy. Isolated showers in the evening.
Lows 56 to 77. Light winds becoming east around 10 mph after
midnight. Chance of rain 20 percent. 
.WEDNESDAY...Partly sunny. Highs 68 to 91. Northwest winds 10 to
15 mph. 
.WEDNESDAY NIGHT...Mostly cloudy. Isolated showers in the
evening. Lows 55 to 77. Southeast winds around 10 mph. Chance of
rain 20 percent. 
.THURSDAY...Partly sunny. Highs 68 to 91. Northwest winds 10 to
15 mph. 
.THURSDAY NIGHT...Mostly cloudy in the evening then becoming
partly cloudy. Lows 55 to 77. South winds up to 10 mph in the
evening becoming light. 
.FRIDAY...Mostly sunny with isolated showers. Highs 68 to 90.
Light winds becoming northwest up to 15 mph in the afternoon.
Chance of rain 20 percent. 

HIZ027-262315-
Big Island Interior-
Including Bradshaw Field, Saddle Road Above 5000 feet
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WARNING IN EFFECT...
...HURRICANE WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions possible. Cloudy
with numerous showers and isolated thunderstorms. Locally heavy
rainfall possible. Lows 58 to 63 near 5000 feet to 52 to 58 near
8000 feet. East winds up to 35 mph. Gusts up to 60 mph late in
the evening. Chance of rain 70 percent. 
.SATURDAY... Tropical storm conditions possible. Occasional
showers and isolated thunderstorms. Locally heavy rainfall
possible. Highs 63 to 76 near 5000 feet to 58 to 65 near
8000 feet. East winds up to 30 mph. Chance of rain near
100 percent. 
.SATURDAY NIGHT...Windy. Mostly cloudy with scattered showers.
Lows 55 to 61 near 5000 feet to 50 to 55 near 8000 feet. East
winds up to 30 mph with gusts to 50 mph. Chance of rain
50 percent. 
.SUNDAY...Mostly cloudy. Windy. Scattered showers in the morning,
then isolated showers in the afternoon. Highs 59 to 77. East
winds 10 to 30 mph with gusts to 50 mph. Chance of rain
50 percent. 
.SUNDAY NIGHT...Mostly cloudy. Breezy. Isolated showers in the
evening. Lows 49 to 60. East winds 10 to 25 mph with gusts to
50 mph. Chance of rain 20 percent. 
.MONDAY...Partly sunny. Breezy. Isolated showers in the
afternoon. Highs 61 to 77. East winds 10 to 20 mph. Chance of
rain 20 percent. 
.MONDAY NIGHT...Mostly cloudy. Isolated showers in the evening.
Lows 50 to 60. East winds 10 to 15 mph. Chance of rain
20 percent. 
.TUESDAY...Mostly cloudy with isolated showers. Highs 60 to 76.
Southeast winds around 10 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy with isolated showers. Lows 50 to
60. Southeast winds around 10 mph. Chance of rain 20 percent. 
.WEDNESDAY...Mostly cloudy with isolated showers. Highs 60 to 75.
South winds 10 to 15 mph. Chance of rain 20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Isolated showers in the
evening. Lows 49 to 60. Southeast winds 10 to 15 mph. Chance of
rain 20 percent. 
.THURSDAY...Mostly cloudy. Highs 60 to 75. South winds around
10 mph. 
.THURSDAY NIGHT...Mostly cloudy. Lows 49 to 60. Southeast winds
up to 10 mph. 
.FRIDAY...Mostly sunny with isolated showers. Highs 60 to 75.
Light winds becoming south around 10 mph in the afternoon. Chance
of rain 20 percent. 

HIZ028-262315-
Big Island Summits-
Including Mauna Loa and Mauna Kea Above 8000 feet
1056 PM HST Fri Sep 25 2026

...FLOOD WATCH IN EFFECT THROUGH SATURDAY AFTERNOON...
...TROPICAL STORM WARNING IN EFFECT...
...HURRICANE WATCH IN EFFECT...

.REST OF TONIGHT... Tropical storm conditions expected with
hurricane conditions possible. Cloudy with numerous showers and
isolated thunderstorms. Locally heavy rainfall possible. Lows
around 46 at the visitor information station to around 40 near
the summits. East winds up to 50 mph with gusts to 70 mph. Chance
of rain 70 percent. 
.SATURDAY... Tropical storm conditions expected with hurricane
conditions possible. Cloudy. Numerous showers and isolated
thunderstorms early in the morning, then occasional showers and
isolated thunderstorms in the late morning and afternoon. Locally
heavy rainfall possible. Highs around 61 at the visitor
information station to around 52 near the summits. East winds up
to 40 mph with gusts to 60 mph. Chance of rain 90 percent. 
.SATURDAY NIGHT...Mostly cloudy. Windy. Scattered showers in the
evening, then isolated showers after midnight. Lows around 46 at
the visitor information station to around 40 near the summits.
East winds up to 35 mph. Chance of rain 50 percent. 
.SUNDAY...Mostly cloudy. Breezy. Isolated showers in the morning.
Highs 50 to 73. East winds 10 to 25 mph with gusts to 45 mph.
Chance of rain 20 percent. 
.SUNDAY NIGHT...Mostly cloudy. Breezy. Lows 39 to 54. East winds
10 to 20 mph. 
.MONDAY...Partly sunny. Isolated showers in the afternoon. Highs
50 to 73. Southeast winds around 10 mph becoming up to 15 mph in
the afternoon. Chance of rain 20 percent. 
.MONDAY NIGHT...Mostly cloudy. Isolated showers in the evening.
Lows 40 to 55. Light winds. Chance of rain 20 percent. 
.TUESDAY...Mostly cloudy with isolated showers. Highs 49 to 72.
Southwest winds up to 10 mph. Chance of rain 20 percent. 
.TUESDAY NIGHT...Mostly cloudy. Isolated showers in the evening.
Lows 39 to 55. Southeast winds up to 10 mph shifting to the
southwest around 10 mph after midnight. Chance of rain
20 percent. 
.WEDNESDAY...Mostly cloudy. Isolated showers in the afternoon.
Highs 49 to 71. Southwest winds around 10 mph. Chance of rain
20 percent. 
.WEDNESDAY NIGHT...Mostly cloudy. Isolated showers in the
evening. Lows 39 to 54. Southeast winds around 10 mph shifting to
the southwest after midnight. Chance of rain 20 percent. 
.THURSDAY...Mostly cloudy. Highs 50 to 71. Southwest winds up to
10 mph. 
.THURSDAY NIGHT...Mostly cloudy. Lows 40 to 54. Southeast winds
up to 10 mph in the evening becoming light. 
.FRIDAY...Mostly sunny. Isolated showers in the afternoon. Highs
51 to 71. Light winds becoming southeast up to 10 mph in the
afternoon. Chance of rain 20 percent.
```

---

### 2. AIRMETs

| Field | Value |
|---|---|
| **Resource ID** | wa0_airmets |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=WA0&issuedby=HI |
| **Collected** | 2026-09-25T23:57:43.043270-10:00 HST |

```text
670
WAHW31 PHFO 260953 AAA
WA0HI

HNLS WA 261000
AIRMET SIERRA UPDATE 1 FOR IFR VALID UNTIL 261600
.
AIRMET MTN OBSC...KAUAI OAHU MOLOKAI LANAI MAUI
N THROUGH E SECTIONS.
TEMPO MTN OBSC ABV 025 EXP DUE TO CLD AND SHRA.
COND CONT BEYOND 1600Z.
.
AIRMET IFR...BIG ISLAND
UPOLU POINT TO CAPE KUMUKAHI TO SOUTH CAPE.
TEMPO CEILING BLW 015 AND/OR VIS BLW 4SM SHRA.
COND CONT BEYOND 1600Z.

=HNLT WA 260952 AMD
AIRMET TANGO UPDATE 2 FOR TURB VALID UNTIL 261600
.
AIRMET TURB...HI
OVER AND IMT S THRU W OF MTN.
TEMPO MOD TURB EXP BLW 090.
COND CONT BEYOND 1600Z.
.
AIRMET STG SFC WND...BIG ISLAND MAUI MOLOKAI LANAI
ENTIRE AREA.
STG SFC WND GREATER THAN 30 KT EXP DUE TO HURRICANE
NOLO.
COND CONT BEYOND 1600Z.

=HNLZ WA 261000
AIRMET ZULU UPDATE 1 FOR ICE AND FZLVL VALID UNTIL 261600
.
NO SIGNIFICANT ICE EXP.
.
FZLVL...159 PHLI SLOPING TO 167 PHTO.
```

---

### 3. Area Forecast Discussion

| Field | Value |
|---|---|
| **Resource ID** | afd_area_forecast_discussion |
| **Official source** | https://api.weather.gov/products/types/AFD/locations/HFO |
| **Collected** | 2026-09-25T23:47:25.162514-10:00 HST |

```text
000
FXHW60 PHFO 260902
AFDHFO

Area Forecast Discussion
National Weather Service Honolulu HI
1102 PM HST Fri Sep 25 2026

.SYNOPSIS...
Hurricane Nolo continues to slowly move to the north towards the
Big Island, and is expected to make a turn to the west tonight.
Moisture on the north side of Nolo will interact with the terrain
of the Big Island and Maui, and could lead to significant flash
flooding, particularly on the windward and southeast portions of
the Big Island. Localized strong and gusty winds are possible
statewide, with the highest winds expected on the Big Island due
to the proximity to Nolo.

.UPDATE...
Forecast winds for the first 24 hours have been updated to 
reflect the latest forecast guidance from the National Hurricane 
Center. With little change in the track and intensity, little 
change from the previous forecast. Hurricane Nolo has remained 
nearly stationary about 145 miles south of South Point on the Big 
Island. Gusts in excess of 50 mph have been reported over the Big 
Island and Maui in the last couple of hours. Some of the outer- 
most rainbands have been moving over the Big Island southeast 
slopes. Nolo is expected to begin its turn to the west over the 
next several hours. 

.AVIATION...
Issued at 918 PM HST Fri Sep 25 2026

Gusty trade winds continue across the islands with gusts peaking
between 25 to 35 knots. Gusts up to 40 knots are most likely at
the windiest sites. Winds may ease slightly overnight but kept 
the stronger winds as prevailing given continued trade shower 
activity and Hurricane Nolo to the south of the Big Island. 
Locally stronger winds are possible from Molokai south to the Big 
Island due to Hurricane Nolo. High resolution guidance suggests 
gusts reaching potentially as high as 45 to 50 knots Saturday 
afternoon and continuing through the end of the TAF period. North 
of Molokai, occasional trade showers continue across windward and 
mauka areas while heavier showers remain closer to the Big Island.
Moderate to heavy rain is expected to continue impacting the Big 
Island as Hurricane Nolo remains just to its south. Occasional 
moderate to heavy showers from Hurricane Nolo will extend up 
through Molokai. Reductions in visibility and ceiling heights are 
expected during heavier showers with MVFR to IFR conditions 
likely. 

AIRMET Sierra has been issued for IFR conditions across eastern
Big Island, and will likely remain in effect through tonight.
Additionally, AIRMET Sierra remains in effect for tempo mountain
obscuration for eastern Kauai, Oahu, Molokai, and Maui through
tonight.

AIRMET Tango remains in effect for moderate turbulence downwind of
island terrain due to breezy trade winds. Expect this to continue
through the forecast period. It is possible that an AIRMET for 
sustained 30 kt winds will be needed for the Big Island by 
Saturday as Nolo passes to the south.

TC SIGMET Oscar series covers Hurricane Nolo, and interests should
continue to monitor for updates to this SIGMET.

.MARINE...
Issued at 918 PM HST Fri Sep 25 2026

Hurricane Warnings around the Big Island and Tropical Storm 
Warnings around Maui County remain in effect as Hurricane Nolo
inches northward. A Gale Watch is in effect for the remaining
waters through Sunday. Nolo is still forecast to turn west well 
before reaching the Big Island or adjacent nearshore waters, but 
strong winds and high seas can nonetheless be expected well away
from the storm itself. 

South to southeast fresh swell emanating from Nolo will spread 
west across the southern nearshore waters as the system tracks 
west through early next week. The High Surf Advisory (HSA) for E 
and SE facing shores of the Big Island, Maui, and Molokai remains 
in effect and has been extended through Sunday. In addition, an 
HSA is now in effect for Kauai, Oahu, and Niihau beginning tonight
due to strengthening trades. A small, long period NW swell fills 
in this weekend in maintenance of elevated surf along exposed 
shorelines into early next week. 

.FIRE WEATHER...
Issued at 918 PM HST Fri Sep 25 2026

Winds will steadily increase as Hurricane Nolo moves closer. Very
strong winds are possible on the Big Island, though heavy rainfall
will likely mitigate fire danger over most areas. From Kauai to 
Maui County, rainfall over the last month has led to some 
improvement in fuels, but the gusty trade winds will produce 
moderate fire weather conditions over drier leeward areas through 
the weekend. Drier conditions are expected early next week, 
although winds will diminish substantially as pressure gradient 
weakens.

.PREV DISCUSSION...
Issued at 918 PM HST Fri Sep 25 2026

High-level cloudiness with light showers prevailed across the Big 
Island this afternoon as Hurricane Nolo continues to move slowly 
north-northeast. The rest of the islands remained relatively quiet, 
aside from breeze conditions throughout the day.

Latest radar imagery shows rainbands associated with Nolo inching 
closer to the Big Island. These bands are expected to move through 
tonight into Saturday morning, producing periods of heavy rainfall 
that could lead to flash flooding and dangerous mudslides.

The latest National Hurricane Center track still indicates Nolo will 
make its closest approach late tonight before turning westward. 
Although forecast precipitation amounts for the state have been 
adjusted slightly downward, rainfall totals remain high enough to 
cause life-threatreninh flooding,especially across the Big Island. 
Other impacts are summarized in the marine and aviation sections.

Impacts from Nolo will worsen through tomorrow morning and persist 
through Saturday night. A slow improvement in weather conditions is 
expected on Sunday as Nolo moves away from the area.

By the middle of next week, troughing will draw Nolo north or 
northeastward to the west of Kauai. Toward the end of next week, 
light south-to-southeast wind flow is expected to prevail as the 
pressure gradient over the state weakens substantially. 

.HFO WATCHES/WARNINGS/ADVISORIES...
Wind Advisory from 6 AM Saturday to 6 PM HST Sunday for Central 
Oahu-East Honolulu-Ewa Plain-Honolulu Metro-Kauai East-Kauai 
Mountains-Kauai North-Kauai South-Kauai Southwest-Koolau Leeward-
Koolau Windward-Niihau-Oahu North Shore-Olomana-Waianae Coast-
Waianae Mountains.

High Surf Advisory until 6 PM HST Sunday for Big Island East-Big 
Island North-Big Island Southeast-Kauai East-Kauai South-
Kipahulu-Koolau Windward-Maui Windward West-Molokai Southeast-
Molokai Windward-Olomana-South Haleakala-Windward Haleakala.

Flood Watch through Saturday afternoon for Big Island East-Big 
Island Interior-Big Island North-Big Island South-Big Island 
Southeast-Big Island Summits-Haleakala Summit-Kahoolawe-Kipahulu-
Kohala-Kona-Lanai Leeward-Lanai Mauka-Lanai South-Lanai Windward-
Maui Central Valley North-Maui Central Valley South-Maui Leeward 
West-Maui Windward West-Molokai Leeward South-Molokai North-
Molokai Southeast-Molokai West-Molokai Windward-South Haleakala-
South Maui/Upcountry-Windward Haleakala.

Tropical Storm Watch for Haleakala Summit-Kahoolawe-Kipahulu-
Lanai Leeward-Lanai Mauka-Lanai South-Lanai Windward-Maui 
Central Valley North-Maui Central Valley South-Maui Leeward West-
Maui Windward West-Molokai Leeward South-Molokai North-Molokai 
Southeast-Molokai West-Molokai Windward-South Haleakala-South 
Maui/Upcountry-Windward Haleakala. 

Hurricane Watch for Big Island East-Big Island Interior-Big 
Island North-Big Island South-Big Island Southeast-Big Island 
Summits-Kohala-Kona. 

Tropical Storm Warning for Big Island East-Big Island Interior-
Big Island North-Big Island South-Big Island Southeast-Big 
Island Summits-Kohala-Kona. 

Tropical Storm Watch for Kaiwi Channel-Maalaea Bay-Maui County 
Leeward Waters-Maui County Windward Waters-Pailolo Channel. 

Hurricane Watch for Alenuihaha Channel-Big Island Leeward Waters-
Big Island Southeast Waters-Big Island Windward Waters. 

Tropical Storm Warning for Alenuihaha Channel-Big Island Leeward 
Waters-Big Island Southeast Waters-Big Island Windward Waters. 

Small Craft Advisory until 6 PM HST Saturday for Kauai Channel-
Kauai Leeward Waters-Kauai Northwest Waters-Kauai Windward 
Waters-Oahu Leeward Waters-Oahu Windward Waters.

Gale Watch from 6 AM HST Saturday through Sunday afternoon for 
Kauai Channel-Kauai Leeward Waters-Kauai Northwest Waters-Kauai 
Windward Waters-Oahu Leeward Waters-Oahu Windward Waters.

DISCUSSION...Castro
AVIATION...Kennedy
MARINE...JVC
FIRE WEATHER...Castro
UPDATE...M Ballard
```

---

### 4. Coastal Waters Forecast (within 40nm)

| Field | Value |
|---|---|
| **Resource ID** | cwf_coastal_waters |
| **Official source** | https://api.weather.gov/products/types/CWF/locations/HFO |
| **Collected** | 2026-09-25T23:51:25.083629-10:00 HST |

```text
000
FZHW50 PHFO 260911
CWFHFO

Coastal Waters Forecast
National Weather Service Honolulu HI
1111 PM HST Fri Sep 25 2026

Hawaiian coastal waters within 40 nautical miles including the
Hawaiian Islands Humpback Whale National Marine Sanctuary.

PHZ100-262215-
1111 PM HST Fri Sep 25 2026

.Synopsis for Hawaiian coastal waters...
Strong winds and hazardous seas will accompany Hurricane Nolo as
it advances westward across area waters through the weekend, then
turns northwest early next week. 

PHZ110-262215-
Kauai Northwest Waters-
1111 PM HST Fri Sep 25 2026

...GALE WATCH IN EFFECT FROM 6 AM HST SATURDAY THROUGH SUNDAY
AFTERNOON...

.REST OF TONIGHT...East northeast winds to 25 knots. Seas 8 to
10 feet. Wave Detail: East 9 feet at 9 seconds and north
northeast 3 feet at 18 seconds. Scattered showers. 
.SATURDAY...East northeast winds 20 to 25 knots, rising to 25 to
30 knots in the afternoon. Seas 10 to 11 feet. Wave Detail: East
10 feet at 9 seconds and north northwest 3 feet at 17 seconds.
Scattered showers. 
.SATURDAY NIGHT...East northeast winds 25 to 30 knots. Seas 11 to
14 feet. Wave Detail: East 13 feet at 9 seconds and north
northwest 4 feet at 15 seconds. Isolated showers. 
.SUNDAY...Tropical storm conditions possible. East northeast
winds 25 to 35 knots. Seas 12 to 14 feet. Wave Detail: East
13 feet at 9 seconds and north northeast 4 feet at 13 seconds.
Scattered showers. 
.SUNDAY NIGHT...East winds 25 to 30 knots. Seas 11 to 13 feet.
Wave Detail: East 12 feet at 9 seconds, north northeast 4 feet at
12 seconds and south 4 feet at 13 seconds. Scattered showers. 
.MONDAY...East winds 20 to 25 knots. Seas 10 to 13 feet. Wave
Detail: East 11 feet at 8 seconds, south 5 feet at 12 seconds and
north 4 feet at 12 seconds. Scattered showers. 
.MONDAY NIGHT...East winds 20 to 25 knots. Seas 9 to 12 feet,
subsiding to 9 to 10 feet after midnight. Wave Detail: East
10 feet at 8 seconds, south southwest 5 feet at 11 seconds and
north northwest 3 feet at 12 seconds. Scattered showers. 
.TUESDAY...East winds 15 to 20 knots, becoming east southeast
20 to 25 knots after midnight. Seas 7 to 10 feet. Wave Detail:
East 8 feet at 7 seconds, south southwest 5 feet at 11 seconds
and north northwest 3 feet at 11 seconds. Scattered showers. 
.WEDNESDAY...East southeast winds 20 to 25 knots. Seas 7 to
8 feet. Wave Detail: East 7 feet at 7 seconds and southwest
5 feet at 9 seconds. Scattered showers.  

PHZ111-262215-
Kauai Windward Waters-
1111 PM HST Fri Sep 25 2026

...GALE WATCH IN EFFECT FROM 6 AM HST SATURDAY THROUGH SUNDAY
AFTERNOON...

.REST OF TONIGHT...East northeast winds to 25 knots. Seas 9 to
11 feet. Wave Detail: East southeast 10 feet at 9 seconds and
north northeast 3 feet at 18 seconds. Scattered showers. 
.SATURDAY...East northeast winds 20 to 25 knots. Gusts up to
35 knots in the afternoon. Seas 10 to 13 feet. Wave Detail: East
southeast 12 feet at 9 seconds and north northwest 3 feet at
17 seconds. Scattered showers. 
.SATURDAY NIGHT...East northeast winds 25 to 30 knots. Seas 13 to
14 feet. Wave Detail: East southeast 13 feet at 10 seconds and
northwest 3 feet at 15 seconds. Scattered showers, mainly in the
evening. 
.SUNDAY...East winds 25 to 30 knots. Seas 13 to 14 feet. Wave
Detail: East southeast 13 feet at 9 seconds and north northeast
3 feet at 13 seconds. Scattered showers. 
.SUNDAY NIGHT...East winds 25 to 30 knots. Seas 12 to 14 feet.
Wave Detail: East southeast 12 feet at 9 seconds, south 5 feet at
13 seconds and north northeast 3 feet at 12 seconds. Scattered
showers. 
.MONDAY...East winds 20 to 25 knots. Seas 11 to 14 feet. Wave
Detail: East southeast 12 feet at 9 seconds, south 6 feet at
11 seconds and north northwest 3 feet at 14 seconds. Scattered
showers. 
.MONDAY NIGHT...East winds 20 to 25 knots. Seas 10 to 13 feet,
subsiding to 10 to 11 feet after midnight. Wave Detail: East
southeast 11 feet at 8 seconds, south southwest 6 feet at
11 seconds and north northwest 3 feet at 12 seconds. Scattered
showers. 
.TUESDAY...East winds to 20 knots. Seas 8 to 11 feet. Wave
Detail: East southeast 8 feet at 8 seconds and south southwest
5 feet at 9 seconds. Scattered showers. 
.WEDNESDAY...East southeast winds 20 to 25 knots. Seas 7 to
8 feet. Wave Detail: East 7 feet at 7 seconds and south southwest
4 feet at 15 seconds. Scattered showers.  

PHZ112-262215-
Kauai Leeward Waters-
1111 PM HST Fri Sep 25 2026

...GALE WATCH IN EFFECT FROM 6 AM HST SATURDAY THROUGH SUNDAY
AFTERNOON...

.REST OF TONIGHT...East northeast winds 20 to 25 knots. Seas 8 to
11 feet. Wave Detail: East southeast 10 feet at 9 seconds and
north northeast 3 feet at 18 seconds. Scattered showers. 
.SATURDAY...East northeast winds 20 to 25 knots, rising to 25 to
30 knots in the afternoon. Seas 9 to 13 feet. Wave Detail: East
southeast 12 feet at 9 seconds and north 3 feet at 17 seconds.
Scattered showers. 
.SATURDAY NIGHT...Tropical storm conditions possible. East
northeast winds 25 to 35 knots. Seas 12 to 16 feet. Wave Detail:
East 15 feet at 10 seconds, north northwest 3 feet at 15 seconds
and south southwest 3 feet at 15 seconds. Isolated showers. 
.SUNDAY...Tropical storm conditions possible. East northeast
winds 25 to 35 knots, rising to 30 to 40 knots in the afternoon.
Seas 12 to 15 feet. Wave Detail: East 15 feet at 10 seconds and
north 3 feet at 13 seconds. Isolated showers. 
.SUNDAY NIGHT...Tropical storm conditions possible. East winds
25 to 35 knots. Seas 11 to 15 feet. Wave Detail: East 14 feet at
9 seconds, south 5 feet at 13 seconds and north 3 feet at
16 seconds. Scattered showers. 
.MONDAY...East winds 25 to 30 knots. Seas 11 to 14 feet. Wave
Detail: East southeast 12 feet at 9 seconds, south 6 feet at
11 seconds and north northwest 3 feet at 14 seconds. Scattered
showers. 
.MONDAY NIGHT...East winds 25 to 30 knots, easing to 20 to
25 knots after midnight. Seas 10 to 13 feet, subsiding to 9 to
11 feet after midnight. Wave Detail: East southeast 11 feet at
8 seconds, south southwest 6 feet at 11 seconds and north
northwest 3 feet at 12 seconds. Scattered showers. 
.TUESDAY...East winds 20 to 25 knots, becoming east southeast
25 to 30 knots. Seas 7 to 10 feet. Wave Detail: Southeast 8 feet
at 7 seconds and south southwest 5 feet at 10 seconds. Scattered
showers. 
.WEDNESDAY...Southeast winds 25 to 30 knots. Seas 6 to 8 feet.
Wave Detail: East 7 feet at 7 seconds and southwest 5 feet at
9 seconds. Scattered showers.  

PHZ113-262215-
Kauai Channel-
1111 PM HST Fri Sep 25 2026

...GALE WATCH IN EFFECT FROM 6 AM HST SATURDAY THROUGH SUNDAY
AFTERNOON...

.REST OF TONIGHT...East northeast winds to 25 knots. Seas 10 to
12 feet. Wave Detail: East 11 feet at 9 seconds and north
northeast 3 feet at 18 seconds. Scattered showers. 
.SATURDAY...East northeast winds 25 to 30 knots. Seas 11 to
13 feet. Wave Detail: East 12 feet at 9 seconds and north
northeast 3 feet at 17 seconds. Scattered showers. 
.SATURDAY NIGHT...East northeast winds 25 to 30 knots. Seas 13 to
15 feet. Wave Detail: East northeast 14 feet at 9 seconds, north
northeast 3 feet at 15 seconds and south southwest 3 feet at
15 seconds. Isolated showers. 
.SUNDAY...East northeast winds 25 to 30 knots. Seas 13 to
14 feet. Wave Detail: East northeast 14 feet at 9 seconds and
north northeast 3 feet at 13 seconds. Isolated showers. 
.SUNDAY NIGHT...East northeast winds 25 to 30 knots. Seas 11 to
14 feet. Wave Detail: East 13 feet at 9 seconds, south 5 feet at
13 seconds and north northeast 3 feet at 16 seconds. Isolated
showers. 
.MONDAY...East winds 20 to 25 knots. Seas 10 to 13 feet. Wave
Detail: East 11 feet at 8 seconds, south southwest 6 feet at
11 seconds and north 3 feet at 15 seconds. Isolated showers. 
.MONDAY NIGHT...East winds 20 to 25 knots, easing to 15 to
20 knots after midnight. Seas 9 to 12 feet. Wave Detail: East
southeast 10 feet at 8 seconds, south southwest 6 feet at
11 seconds and north 3 feet at 12 seconds. Scattered showers. 
.TUESDAY...East southeast winds 15 to 20 knots. Seas 7 to
10 feet. Wave Detail: East southeast 7 feet at 7 seconds and
southwest 5 feet at 9 seconds. Scattered showers. 
.WEDNESDAY...Southeast winds 15 to 20 knots. Seas 6 to 7 feet.
Wave Detail: East 6 feet at 7 seconds and south 5 feet at
15 seconds. Scattered showers.  

PHZ114-262215-
Oahu Windward Waters-
1111 PM HST Fri Sep 25 2026

...GALE WATCH IN EFFECT FROM 6 AM HST SATURDAY THROUGH SUNDAY
AFTERNOON...

.REST OF TONIGHT...East northeast winds 25 to 30 knots. Seas
10 to 12 feet. Wave Detail: East 12 feet at 9 seconds and north
northeast 3 feet at 18 seconds. Scattered showers. 
.SATURDAY...East northeast winds 25 to 30 knots. Seas 11 to
13 feet. Wave Detail: East southeast 13 feet at 9 seconds and
north northwest 3 feet at 17 seconds. Scattered showers. 
.SATURDAY NIGHT...Tropical storm conditions possible. East
northeast winds 25 to 30 knots, veering to east 30 to 35 knots
after midnight. Seas 13 to 14 feet. Wave Detail: East 14 feet at
9 seconds and northwest 3 feet at 15 seconds. Isolated showers. 
.SUNDAY...Tropical storm conditions possible. East winds 30 to
35 knots. Seas 13 to 14 feet. Wave Detail: East southeast 13 feet
at 9 seconds and north northeast 3 feet at 14 seconds. Isolated
showers. 
.SUNDAY NIGHT...East winds 25 to 30 knots. Seas 11 to 13 feet.
Wave Detail: East southeast 12 feet at 9 seconds, south 4 feet at
13 seconds and north 3 feet at 16 seconds. Scattered showers. 
.MONDAY...East winds 25 to 30 knots. Seas 11 to 13 feet. Wave
Detail: East southeast 12 feet at 8 seconds, south southwest
5 feet at 12 seconds and north northwest 3 feet at 15 seconds.
Scattered showers in the morning. Isolated showers in the
afternoon. 
.MONDAY NIGHT...East winds 20 to 25 knots. Seas 9 to 12 feet.
Wave Detail: East southeast 11 feet at 8 seconds, south southwest
5 feet at 11 seconds and north northwest 3 feet at 13 seconds.
Isolated showers. 
.TUESDAY...East southeast winds to 20 knots. Seas 7 to 10 feet.
Wave Detail: East southeast 8 feet at 7 seconds and south
southwest 4 feet at 9 seconds. Isolated showers through the
night, then scattered showers through the day. 
.WEDNESDAY...East southeast winds 20 to 25 knots. Seas 6 to
7 feet. Wave Detail: East 7 feet at 7 seconds and south southwest
3 feet at 15 seconds. Scattered showers.  

PHZ115-262215-
Oahu Leeward Waters-
1111 PM HST Fri Sep 25 2026

...GALE WATCH IN EFFECT FROM 6 AM HST SATURDAY THROUGH SUNDAY
AFTERNOON...

.REST OF TONIGHT...East northeast winds 25 to 30 knots. Seas 9 to
13 feet. Wave Detail: East southeast 13 feet at 9 seconds.
Isolated showers. 
.SATURDAY...East northeast winds 25 to 30 knots. Seas 9 to
13 feet. Wave Detail: East 13 feet at 9 seconds. Scattered
showers with isolated thunderstorms. 
.SATURDAY NIGHT...East northeast winds to 30 knots. Seas 11 to
15 feet. Wave Detail: East 14 feet at 9 seconds. Isolated showers
after midnight. 
.SUNDAY...East northeast winds 25 to 30 knots, easing to 20 to
25 knots in the afternoon. Seas 10 to 14 feet. Wave Detail: East
13 feet at 9 seconds and south 3 feet at 14 seconds. Isolated
showers in the morning. 
.SUNDAY NIGHT...East northeast winds 20 to 25 knots. Gusts up to
35 knots in the evening. Seas 9 to 12 feet. Wave Detail: East
southeast 11 feet at 9 seconds and south 5 feet at 13 seconds.
Isolated showers after midnight. 
.MONDAY...East winds 15 to 20 knots, easing to 10 to 15 knots in
the afternoon. Seas 9 to 11 feet. Wave Detail: East southeast
10 feet at 9 seconds and south southwest 5 feet at 11 seconds.
Isolated showers in the morning. 
.MONDAY NIGHT...East winds 10 to 15 knots. Seas 8 to 10 feet.
Wave Detail: Southeast 8 feet at 8 seconds and south southwest
5 feet at 11 seconds. Isolated showers. 
.TUESDAY...East southeast winds 10 to 15 knots. Seas 7 to
10 feet. Wave Detail: Southeast 6 feet at 7 seconds and southwest
5 feet at 8 seconds. Isolated showers in the morning, then
scattered showers. 
.WEDNESDAY...Southeast winds 10 to 15 knots, rising to 15 to
20 knots. Seas 6 to 7 feet. Wave Detail: Southeast 5 feet at
6 seconds and south southwest 5 feet at 15 seconds. Scattered
showers.  

Winds and seas higher in and near tstms.

PHZ116-262215-
Kaiwi Channel-
1111 PM HST Fri Sep 25 2026

...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT...Tropical storm conditions possible. East
northeast winds 25 to 30 knots. Seas 10 to 13 feet. Wave Detail:
East northeast 13 feet at 8 seconds and north northeast 3 feet at
11 seconds. Isolated showers and thunderstorms. 
.SATURDAY...Tropical storm conditions expected. East northeast
winds 30 to 35 knots. Seas 11 to 14 feet. Wave Detail: East
northeast 14 feet at 9 seconds and north northeast 3 feet at
17 seconds. Scattered showers with isolated thunderstorms. 
.SATURDAY NIGHT...Tropical storm conditions possible. East
northeast winds 30 to 35 knots, becoming 25 to 35 knots after
midnight. Seas 12 to 14 feet. Wave Detail: East northeast 14 feet
at 9 seconds and north northeast 3 feet at 15 seconds. 
.SUNDAY...Tropical storm conditions possible. East northeast
winds 25 to 35 knots. Seas 11 to 14 feet. Wave Detail: East
14 feet at 9 seconds, south 4 feet at 14 seconds and north
northeast 3 feet at 13 seconds. Isolated showers. 
.SUNDAY NIGHT...East winds 25 to 30 knots. Seas 10 to 14 feet.
Wave Detail: East 12 feet at 8 seconds, south 5 feet at
11 seconds and north 3 feet at 16 seconds. 
.MONDAY...East winds 25 to 30 knots, easing to 20 to 25 knots in
the afternoon. Seas 9 to 13 feet. Wave Detail: East 11 feet at
8 seconds, south southwest 5 feet at 10 seconds and north 3 feet
at 15 seconds. 
.MONDAY NIGHT...East winds 20 to 25 knots. Gusts up to 35 knots
in the evening. Seas 9 to 12 feet. Wave Detail: East 10 feet at
8 seconds, south southwest 5 feet at 10 seconds and north 3 feet
at 13 seconds. 
.TUESDAY...East winds 15 to 20 knots. Seas 6 to 9 feet. Wave
Detail: East southeast 8 feet at 7 seconds and southwest 5 feet
at 8 seconds. Isolated showers. 
.WEDNESDAY...East southeast winds 15 to 20 knots. Seas 5 to
7 feet. Wave Detail: East 7 feet at 6 seconds and south southwest
4 feet at 15 seconds. Isolated showers.  

Winds and seas higher in and near tstms.

PHZ117-262215-
Maui County Windward Waters-
1111 PM HST Fri Sep 25 2026

...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT...Tropical storm conditions possible. East winds
25 to 30 knots. Seas 10 to 12 feet. Wave Detail: East 12 feet at
8 seconds and north northeast 3 feet at 18 seconds. Scattered
heavy showers with isolated thunderstorms. 
.SATURDAY...Tropical storm conditions expected. East winds 25 to
35 knots. Seas 12 to 13 feet. Wave Detail: East 13 feet at
8 seconds and northwest 3 feet at 18 seconds. Scattered heavy
showers with isolated thunderstorms. 
.SATURDAY NIGHT...Tropical storm conditions possible. East winds
25 to 35 knots, rising to 30 to 40 knots after midnight. Seas
12 to 14 feet. Wave Detail: East northeast 14 feet at 8 seconds
and northwest 3 feet at 15 seconds. Isolated showers. 
.SUNDAY...Tropical storm conditions possible. East winds 30 to
40 knots. Seas 11 to 13 feet. Wave Detail: East 13 feet at
8 seconds and north northwest 3 feet at 14 seconds. Scattered
showers. 
.SUNDAY NIGHT...Tropical storm conditions possible. East winds
25 to 35 knots. Seas 10 to 12 feet. Wave Detail: East southeast
12 feet at 8 seconds and north northwest 3 feet at 17 seconds.
Scattered showers. 
.MONDAY...East winds 25 to 30 knots. Seas 10 to 11 feet. Wave
Detail: East southeast 11 feet at 8 seconds and north northwest
3 feet at 15 seconds. Scattered showers in the morning. Isolated
showers in the afternoon. 
.MONDAY NIGHT...East southeast winds 20 to 25 knots. Seas 8 to
10 feet. Wave Detail: East southeast 10 feet at 7 seconds and
north northwest 3 feet at 13 seconds. Isolated showers. 
.TUESDAY...East southeast winds 20 to 25 knots. Seas 6 to 9 feet.
Wave Detail: East southeast 8 feet at 7 seconds and north
northwest 3 feet at 12 seconds. Isolated showers. 
.WEDNESDAY...East southeast winds 20 to 25 knots. Seas 6 to
7 feet. Wave Detail: East southeast 6 feet at 6 seconds. Isolated
showers, then scattered showers after midnight.  

Winds and seas higher in and near tstms.

PHZ118-262215-
Maui County Leeward Waters-
1111 PM HST Fri Sep 25 2026

...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT...Tropical storm conditions possible. East
northeast winds 25 to 30 knots. Seas 9 to 13 feet. Wave Detail:
East 13 feet at 7 seconds. Scattered heavy showers with isolated
thunderstorms. 
.SATURDAY...Tropical storm conditions expected. East northeast
winds 25 to 35 knots. Seas 9 to 13 feet. Wave Detail: East
13 feet at 7 seconds. Scattered heavy showers with isolated
thunderstorms. 
.SATURDAY NIGHT...Tropical storm conditions possible. East
northeast winds 25 to 35 knots. Seas 11 to 15 feet. Wave Detail:
East 15 feet at 8 seconds. 
.SUNDAY...Tropical storm conditions possible. East northeast
winds 25 to 35 knots. Seas 10 to 14 feet. Wave Detail: East
13 feet at 8 seconds and south 4 feet at 14 seconds. 
.SUNDAY NIGHT...Tropical storm conditions possible. East
northeast winds 30 to 40 knots. Seas 9 to 13 feet. Wave Detail:
East southeast 11 feet at 8 seconds and south 5 feet at
11 seconds. 
.MONDAY...East winds 25 to 30 knots, easing to 20 to 25 knots in
the afternoon. Seas 8 to 11 feet. Wave Detail: East southeast
10 feet at 9 seconds and south southwest 5 feet at 10 seconds. 
.MONDAY NIGHT...East winds 25 to 30 knots, easing to 20 to
25 knots after midnight. Seas 7 to 10 feet. Wave Detail: East
southeast 9 feet at 8 seconds and south southwest 5 feet at
10 seconds. Isolated showers after midnight. 
.TUESDAY...East southeast winds 15 to 20 knots. Seas 5 to 8 feet.
Wave Detail: Southeast 6 feet at 7 seconds and southwest 4 feet
at 16 seconds. Isolated showers through the night. Scattered
showers through the day. 
.WEDNESDAY...East southeast winds 15 to 20 knots, rising to 20 to
25 knots in the evening, easing to 15 to 20 knots after midnight.
Seas 4 to 6 feet. Wave Detail: East southeast 6 feet at 6 seconds
and south southwest 4 feet at 15 seconds. Scattered showers in
the morning, then isolated showers through the night. Scattered
showers after midnight.  

Winds and seas higher in and near tstms.

PHZ119-262215-
Maalaea Bay-
1111 PM HST Fri Sep 25 2026

...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT...Tropical storm conditions expected. North
northeast winds to 40 knots. Seas 3 to 5 feet. Wave Detail: North
5 feet at 4 seconds. Scattered heavy showers with isolated
thunderstorms. 
.SATURDAY...Tropical storm conditions expected. North winds to
40 knots. Seas 3 to 5 feet. Wave Detail: North northeast 5 feet
at 5 seconds. Scattered heavy showers in the morning. Isolated
thunderstorms. Isolated heavy showers in the afternoon. 
.SATURDAY NIGHT...Tropical storm conditions possible. North
northeast winds 30 to 40 knots. Seas 3 to 5 feet. Wave Detail:
East northeast 5 feet at 5 seconds. 
.SUNDAY...East northeast winds 25 to 30 knots. Seas 3 to 5 feet.
Wave Detail: East northeast 5 feet at 5 seconds and south 4 feet
at 9 seconds. 
.SUNDAY NIGHT...East northeast winds 20 to 25 knots, easing to
15 to 20 knots after midnight. Seas 3 to 5 feet. Wave Detail:
Northeast 5 feet at 4 seconds and south 4 feet at 10 seconds. 
.MONDAY...East winds 15 to 20 knots. Seas 3 to 4 feet. Wave
Detail: East 4 feet at 4 seconds and south southwest 4 feet at
10 seconds. 
.MONDAY NIGHT...East northeast winds 10 to 15 knots. Seas 3 to
4 feet. Wave Detail: South southeast 4 feet at 6 seconds and
south southwest 3 feet at 9 seconds. 
.TUESDAY...East winds to 10 knots. Seas to 3 feet. Wave Detail:
South southeast 3 feet at 5 seconds. 
.WEDNESDAY...East winds 10 to 15 knots. Seas to 3 feet.  

Winds and seas higher in and near tstms.

PHZ120-262215-
Pailolo Channel-
1111 PM HST Fri Sep 25 2026

...TROPICAL STORM WATCH IN EFFECT...

.REST OF TONIGHT...Tropical storm conditions expected. East
northeast winds 35 to 40 knots. Seas 8 to 11 feet. Wave Detail:
East 10 feet at 7 seconds. Scattered heavy showers with isolated
thunderstorms. 
.SATURDAY...Tropical storm conditions expected. East northeast
winds 35 to 40 knots. Seas 9 to 12 feet. Wave Detail: East
10 feet at 7 seconds. Scattered heavy showers in the morning.
Isolated thunderstorms. Isolated heavy showers in the afternoon. 
.SATURDAY NIGHT...Tropical storm conditions possible. East
northeast winds 35 to 45 knots. Seas 9 to 12 feet. Wave Detail:
East northeast 11 feet at 7 seconds. Isolated showers. 
.SUNDAY...Tropical storm conditions possible. East northeast
winds 30 to 40 knots. Seas 8 to 11 feet. Wave Detail: East
northeast 9 feet at 7 seconds and south 3 feet at 14 seconds. 
.SUNDAY NIGHT...Tropical storm conditions possible. East
northeast winds 30 to 40 knots, easing to 25 to 30 knots after
midnight. Seas 8 to 11 feet. Wave Detail: East 8 feet at
6 seconds and south 4 feet at 10 seconds. 
.MONDAY...East northeast winds 15 to 20 knots. Seas 6 to 9 feet.
Wave Detail: East 6 feet at 8 seconds and south southwest 4 feet
at 10 seconds. 
.MONDAY NIGHT...East northeast winds 10 to 15 knots. Seas 5 to
7 feet. Wave Detail: East 6 feet at 7 seconds and south southwest
3 feet at 10 seconds. 
.TUESDAY...East winds 10 to 15 knots. Seas 4 to 6 feet. Wave
Detail: East 4 feet at 6 seconds. 
.WEDNESDAY...East winds 10 to 15 knots. Seas 3 to 4 feet. Wave
Detail: East 4 feet at 6 seconds. Isolated showers through the
night.  

Winds and seas higher in and near tstms.

PHZ121-262215-
Alenuihaha Channel-
1111 PM HST Fri Sep 25 2026

...TROPICAL STORM WARNING IN EFFECT...
...HURRICANE WATCH IN EFFECT...

.REST OF TONIGHT...Tropical storm conditions expected with
hurricane conditions possible. East northeast winds 35 to
40 knots. Seas 12 to 16 feet. Wave Detail: East northeast 15 feet
at 8 seconds. Scattered heavy showers with isolated
thunderstorms. 
.SATURDAY...Tropical storm conditions expected with hurricane
conditions possible. East northeast winds 35 to 40 knots. Seas
12 to 16 feet. Wave Detail: East northeast 15 feet at 8 seconds.
Scattered heavy showers with isolated thunderstorms. 
.SATURDAY NIGHT...Tropical storm conditions possible. East
northeast winds 35 to 40 knots, rising to 40 to 50 knots after
midnight. Seas 12 to 16 feet. Wave Detail: East northeast 16 feet
at 8 seconds and south southwest 3 feet at 15 seconds. Scattered
showers. 
.SUNDAY...Tropical storm conditions possible. East northeast
winds 40 to 50 knots. Seas 12 to 16 feet. Wave Detail: East
northeast 16 feet at 8 seconds and south 4 feet at 14 seconds.
Isolated showers. 
.SUNDAY NIGHT...Tropical storm conditions possible. East winds
40 to 50 knots. Seas 11 to 15 feet. Wave Detail: East northeast
14 feet at 8 seconds and south southwest 5 feet at 10 seconds.
Isolated showers. 
.MONDAY...Tropical storm conditions possible. 
.MONDAY NIGHT...Tropical storm conditions possible. Isolated
showers. 
.TUESDAY...East winds 20 to 25 knots, easing to 15 to 20 knots
after midnight. Seas 6 to 9 feet. Wave Detail: East northeast
7 feet at 6 seconds and south southwest 4 feet at 16 seconds.
Isolated showers. 
.WEDNESDAY...East winds 15 to 20 knots, rising to 20 to 25 knots
in the afternoon and evening, easing to 15 to 20 knots after
midnight. Seas 5 to 7 feet. Wave Detail: East northeast 6 feet at
6 seconds and south southwest 4 feet at 15 seconds. Isolated
showers.  

Winds and seas higher in and near tstms.

PHZ122-262215-
Big Island Windward Waters-
1111 PM HST Fri Sep 25 2026

...TROPICAL STORM WARNING IN EFFECT...
...HURRICANE WATCH IN EFFECT...

.REST OF TONIGHT...Tropical storm conditions possible. East
northeast winds 25 to 30 knots. Seas 10 to 13 feet. Wave Detail:
Northeast 12 feet at 7 seconds and south 5 feet at 10 seconds.
Occasional heavy showers with isolated thunderstorms. 
.SATURDAY...Tropical storm conditions possible. East northeast
winds 25 to 30 knots. Seas 12 to 14 feet. Wave Detail: Northeast
12 feet at 8 seconds, south 4 feet at 9 seconds and north
northeast 3 feet at 18 seconds. Occasional heavy showers with
isolated thunderstorms. 
.SATURDAY NIGHT...East winds 25 to 30 knots. Seas 11 to 13 feet,
subsiding to 9 to 12 feet after midnight. Wave Detail: Northeast
12 feet at 7 seconds, south 5 feet at 9 seconds and north
northeast 3 feet at 15 seconds. Numerous showers, mainly in the
evening. 
.SUNDAY...Tropical storm conditions possible. East winds 25 to
35 knots. Seas 9 to 12 feet. Wave Detail: Northeast 11 feet at
7 seconds, south southwest 5 feet at 8 seconds and north
northeast 3 feet at 14 seconds. Scattered showers. 
.SUNDAY NIGHT...East winds 25 to 30 knots. Seas 7 to 10 feet.
Wave Detail: East northeast 9 feet at 6 seconds, south southwest
4 feet at 14 seconds and north 3 feet at 18 seconds. Scattered
showers, mainly in the evening. 
.MONDAY...East southeast winds 20 to 25 knots. Gusts up to
35 knots in the morning. Seas 6 to 9 feet. Wave Detail: East
southeast 8 feet at 6 seconds, south southwest 4 feet at
9 seconds and north northwest 3 feet at 16 seconds. Isolated
showers. 
.MONDAY NIGHT...East southeast winds 15 to 20 knots, rising to
20 to 25 knots after midnight. Seas 6 to 9 feet. Wave Detail:
East southeast 7 feet at 6 seconds, south southwest 4 feet at
12 seconds and north northwest 3 feet at 13 seconds. Scattered
showers. 
.TUESDAY...East southeast winds 15 to 20 knots. Seas 5 to 8 feet.
Wave Detail: Southeast 6 feet at 5 seconds, south southwest
4 feet at 15 seconds and north northwest 3 feet at 12 seconds.
Scattered showers. 
.WEDNESDAY...East southeast winds 15 to 20 knots. Seas 6 to
7 feet. Wave Detail: Southeast 5 feet at 5 seconds and south
southwest 3 feet at 15 seconds. Scattered showers.  

Winds and seas higher in and near tstms.

PHZ123-262215-
Big Island Leeward Waters-
1111 PM HST Fri Sep 25 2026

...TROPICAL STORM WARNING IN EFFECT...
...HURRICANE WATCH IN EFFECT...

.REST OF TONIGHT...Tropical storm conditions expected with
hurricane conditions possible. Northeast winds 30 to 35 knots.
Seas 10 to 14 feet. Wave Detail: Northeast 14 feet at 9 seconds.
Occasional heavy showers with isolated thunderstorms. 
.SATURDAY...Tropical storm conditions expected with hurricane
conditions possible. East northeast winds 30 to 35 knots. Seas
12 to 16 feet. Wave Detail: East northeast 16 feet at 9 seconds.
Occasional heavy showers with isolated thunderstorms. 
.SATURDAY NIGHT...Tropical storm conditions possible. East
northeast winds 25 to 35 knots. Seas 12 to 16 feet. Wave Detail:
East northeast 16 feet at 9 seconds and south 4 feet at
15 seconds. Scattered showers. 
.SUNDAY...Tropical storm conditions possible. East northeast
winds 25 to 35 knots, rising to 30 to 40 knots in the afternoon.
Seas 10 to 14 feet. Wave Detail: East northeast 14 feet at
8 seconds and south 5 feet at 14 seconds. Scattered showers,
mainly in the morning. 
.SUNDAY NIGHT...Tropical storm conditions possible. East winds
30 to 35 knots. Seas 9 to 13 feet, subsiding to 8 to 11 feet
after midnight. Wave Detail: East 11 feet at 7 seconds and south
southwest 5 feet at 10 seconds. Isolated showers. 
.MONDAY...Tropical storm conditions possible. Isolated showers. 
.MONDAY NIGHT...Southeast winds 25 to 30 knots, backing to east
20 to 25 knots after midnight. Seas 7 to 10 feet. Wave Detail:
Southeast 9 feet at 7 seconds and southwest 5 feet at 10 seconds.
Isolated showers. 
.TUESDAY...East southeast winds 20 to 25 knots. Seas 6 to 9 feet.
Wave Detail: East southeast 5 feet at 5 seconds and south
southwest 4 feet at 16 seconds. Isolated showers in the morning,
then scattered showers. 
.WEDNESDAY...Southeast winds 20 to 25 knots, rising to 25 to
30 knots in the afternoon and evening, backing to east southeast
20 to 25 knots after midnight. Seas 5 to 7 feet. Wave Detail:
East 4 feet at 5 seconds and south 4 feet at 15 seconds.
Scattered showers.  

Winds and seas higher in and near tstms.

PHZ124-262215-
Big Island Southeast Waters-
1111 PM HST Fri Sep 25 2026

...TROPICAL STORM WARNING IN EFFECT...
...HURRICANE WATCH IN EFFECT...

.REST OF TONIGHT...Tropical storm conditions with hurricane
conditions possible. East northeast winds 35 to 40 knots. Seas
15 to 18 feet. Wave Detail: East 17 feet at 9 seconds and south
4 feet at 10 seconds. Occasional heavy showers with isolated
thunderstorms. 
.SATURDAY...Tropical storm conditions expected with hurricane
conditions possible. East northeast winds 30 to 40 knots. Seas
15 to 19 feet. Wave Detail: East southeast 18 feet at 9 seconds
and south 4 feet at 16 seconds. Occasional heavy showers with
isolated thunderstorms. 
.SATURDAY NIGHT...Tropical storm conditions possible. East
northeast winds 30 to 35 knots. Seas 12 to 17 feet. Wave Detail:
East 16 feet at 8 seconds and south 4 feet at 9 seconds.
Occasional showers. 
.SUNDAY...Tropical storm conditions possible. East northeast
winds 30 to 35 knots. Seas 10 to 14 feet. Wave Detail: Northeast
12 feet at 7 seconds and south 5 feet at 8 seconds. Numerous
showers, mainly in the morning. 
.SUNDAY NIGHT...East northeast winds 25 to 30 knots. Seas 9 to
12 feet. Wave Detail: East northeast 10 feet at 7 seconds and
south southwest 5 feet at 10 seconds. Scattered showers. 
.MONDAY...East northeast winds 20 to 25 knots. Gusts up to
35 knots in the morning. Seas 7 to 10 feet. Wave Detail: East
southeast 8 feet at 6 seconds and south southwest 5 feet at
10 seconds. Scattered showers. 
.MONDAY NIGHT...East winds 20 to 25 knots, easing to 15 to
20 knots after midnight. Seas 6 to 9 feet, subsiding to 6 to
7 feet after midnight. Wave Detail: East 7 feet at 6 seconds and
south southwest 4 feet at 11 seconds. Scattered showers. 
.TUESDAY...East winds 15 to 20 knots. Seas 5 to 7 feet. Wave
Detail: East 4 feet at 5 seconds and south southwest 4 feet at
16 seconds. Scattered showers. 
.WEDNESDAY...East winds to 15 knots. Seas 6 to 7 feet. Wave
Detail: East 4 feet at 5 seconds and south southwest 4 feet at
15 seconds. Scattered showers.  

Winds and seas higher in and near tstms.
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
| **Collected** | 2026-09-26T01:59:38.490689-10:00 HST |

```text
771
SRHW80 PHFO 261146
RRAHFO

Hawaii Rainfall Summary
National Weather Service Honolulu HI
145 AM HST Sat Sep 26 2026

:
.B HFO  0926 H  DH01 /DRH-03/PPT/DRH-06/PPQ/DRH-12/PPK/DRH-24/PPD
:
:Automated rain gage reports from around the State of Hawaii.
:These are provisional reports that have not been quality
:controlled.
:
:T=Trace Rainfall, M=Missing Data
:
:Precipitation totals ending  1 AM HST
:
:Island of Kauai                                   Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
:       Windward/Mauka Sites
MKAH1 : Makaha Ridge (RAWS)         :    0.01  /  0.01  /  0.01  /  0.01
PLRH1 : Puu Lua (RAWS)              :    0.02  /  0.09  /  0.09  /  0.09
WKRH1 : Waiakoali (USGS)            :    0.17  /  0.48  /  0.68  /  0.72
KLOH1 : Kilohana (USGS)             :    0.35  /  1.08  /  1.75  /  2.39
MCRH1 : Mohihi Crossing (USGS)      :    0.14  /  0.48  /  0.64  /  0.70
WLGH1 : Waialae (USGS)              :    0.12  /  0.26  /  0.27  /  0.27
LLMH1 : Lower Limahuli (UHM)        :    0.03  /  0.24  /  0.32  /  0.36
WNHH1 : Wainiha (12010)             :    0.14  /  0.41  /  0.46  /  0.55
WIPH1 : Waipa (UHM)                 :    0.09  /  0.24  /  0.38  /  0.48
HNIH1 : Hanalei (12009)             :    0.06  /  0.26  /  0.36  /  0.44
WLLH1 : Mount Waialeale (USGS)      :      M   /    M   /    M   /    M
PRIH1 : Princeville Airport (12011) :    0.00  /  0.06  /  0.10  /  0.12
CMGH1 : Common Ground (UHM)         :    0.03  /  0.11  /  0.20  /  0.22
HLIH1 : Hanalei (RAWS)              :    0.04  /  0.27  /  0.39  /  0.42
MLDH1 : Moloaa Dairy (RAWS)         :    0.00  /  0.00  /  0.00  /  0.00
ANHH1 : Anahola (12001)             :    0.01  /  0.05  /  0.05  /  0.05
KPIH1 : Kapahi (12003)              :    0.02  /  0.29  /  0.34  /  0.36
WLDH1 : N Wailua Ditch (USGS)       :    0.21  /  0.61  /  0.65  /  0.71
WUHH1 : Wailua (12005)              :    0.09  /  0.40  /  0.47  /  0.53
WIRH1 : Waiahi Rain Gage (USGS)     :    0.08  /  0.41  /  0.51  /  0.66
LIHH1 : Lihue Var. Stn. (12006)     :    0.01  /  0.15  /  0.30  /  0.34
HNMH1 : Hanamaulu (UHM)             :    0.12  /  0.30  /  0.47  /  0.52
HLI   : Lihue Airport (ASOS)        :    0.01  /  0.01  /  0.05  /  0.07
:       Leeward Sites
OMAH1 : Omao (12004)                :    0.11  /  0.23  /  0.30  /  0.33
LNTH1 : Lawai NTBG (UHM)            :    0.05  /  0.16  /  0.21  /  0.22
KHEH1 : Kalaheo (12008)             :    0.09  /  0.15  /  0.20  /  0.21
PAKH1 : Port Allen (HSOIS)          :    0.02  /  0.03  /  0.03  /  0.03
HNPH1 : Hanapepe (12002)            :    0.06  /  0.11  /  0.11  /  0.11
POPH1 : Puu Opae (RAWS)             :    0.01  /  0.01  /  0.01  /  0.01
WHGH1 : Waimea Heights (RAWS)       :    0.00  /  0.01  /  0.01  /  0.01
WMTH1 : Waimea Tank (12007)         :    0.01  /  0.01  /  0.01  /  0.01
MNRH1 : Mana (RAWS)                 :    0.00  /  0.00  /  0.00  /  0.00
:
:Island of Oahu                                    Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
:       Windward/Mauka Sites
KAHH1 : Kahuku (13027)              :    0.01  /  0.04  /  0.04  /  0.04
KTAH1 : Kahuku Training Area (RAWS) :    0.00  /  0.00  /  0.00  /  0.00
KFWH1 : Kii (RAWS)                  :    0.00  /  0.00  /  0.00  /  0.00
PUNH1 : Punaluu Pump (13013)        :    0.00  /  0.03  /  0.08  /  0.17
PNSH1 : Punaluu Stream (USGS)       :    0.05  /  0.13  /  0.20  /  0.36
KNRH1 : Kahana (USGS)               :    0.01  /  0.03  /  0.09  /  0.34
HAKH1 : Hakipuu Mauka (13004)       :    0.01  /  0.03  /  0.04  /  0.34
WPPH1 : Waihee Pump (13002)         :    0.04  /  0.04  /  0.08  /  0.15
WHSH1 : Waiahole (USGS)             :    0.02  /  0.03  /  0.07  /  0.13
OFRH1 : Oahu Forest NWR (USFWS)     :    0.06  /  0.11  /  0.12  /  0.20
AHUH1 : Ahuimanu Loop (13005)       :    0.00  /  0.01  /  0.04  /  0.07
HRRH1 : Heeia NERR (NOAA/NOS)       :    0.00  /  0.00  /  0.05  /  0.12
LULH1 : Luluku (13016)              :    0.00  /  0.00  /  0.00  /  0.00
NRSH1 : Nuuanu Res No. 1 (UHM)      :    0.00  /  0.01  /  0.01  /  0.08
KWIH1 : Kalawahine (UHM)            :    0.00  /  0.00  /  0.01  /  0.17
LYOH1 : Lyon (UHM)                  :    0.00  /  0.01  /  0.01  /  0.26
MNLH1 : Manoa Lyon Arboretum (13023):    0.00  /  0.01  /  0.02  /  0.25
STVH1 : St. Stephens (13006)        :    0.00  /  0.00  /  0.02  /  0.16
MAUH1 : Maunawili (13008)           :      M   /    M   /    M   /    M
OFSH1 : Olomana Fire Station (13009):    0.00  /  0.00  /  0.00  /  0.04
WMLH1 : Waimanalo (13011)           :    0.00  /  0.00  /  0.00  /  0.06
BELH1 : Bellows AFS (HSOIS)         :    0.00  /  0.00  /  0.00  /  0.00
KMHH1 : Kamehame (13012)            :    0.01  /  0.01  /  0.01  /  0.09
HAJH1 : Hawaii Kai Golf Crse (13015):    0.00  /  0.00  /  0.00  /  0.17
:       Leeward/Central Sites
KUXH1 : Kaluanui (UHM)              :    0.00  /  0.00  /  0.01  /  0.13
NIUH1 : Niu Valley (13001)          :    0.00  /  0.00  /  0.00  /  0.24
PFSH1 : Palolo Fire Station (13010) :    0.00  /  0.00  /  0.00  /  0.14
HNL   : Honolulu Airport (ASOS)             See note at bottom  :
MOAH1 : Moanalua (13003)            :    0.00  /  0.01  /  0.02  /  0.09
MOGH1 : Moanalua RG (USGS)          :    0.00  /  0.00  /  0.15  /  0.33
TNLH1 : Tunnel RG (USGS)            :    0.00  /  0.02  /  0.14  /  0.39
PACH1 : Palisades (13020)           :    0.07  /  0.11  /  0.13  /  0.16
WAWH1 : Waiawa C.F. (13025)         :    0.07  /  0.13  /  0.14  /  0.15
MITH1 : Mililani (13022)            :    0.02  /  0.05  /  0.06  /  0.06
SCBH1 : Schofield Barracks (RAWS)   :      M   /    M   /  0.00  /  0.00
SCEH1 : Schofield East (RAWS)       :      M   /    M   /    M   /    M
WAFH1 : Wheeler Airfield            :    0.13  /  0.30  /  0.30  /  0.30
POAH1 : Poamoho (13018)             :    0.00  /  0.02  /  0.02  /  0.02
KRGH1 : Kalahee Ridge (UHM)         :    0.14  /  0.29  /  0.31  /  0.34
KMRH1 : Kamananui Stream (USGS)     :    0.29  /  0.40  /  0.48  /  0.58
PPRH1 : Pupukea Road (USGS)         :    0.07  /  0.14  /  0.21  /  0.29
PMHH1 : Poamoho RG 1 (USGS)         :    0.04  /  0.07  /  0.14  /  0.44
DLGH1 : Dillingham (RAWS)           :    0.00  /  0.01  /  0.01  /  0.01
AALH1 : Kaala (UHM)                 :    0.03  /  0.10  /  0.23  /  0.38
PECH1 : Waipio (13019)              :    0.00  /  0.00  /  0.00  /  0.00
KUNH1 : Kunia Substation (13021)    :    0.00  /  0.00  /  0.00  /  0.00
HOFH1 : Honouliuli (RAWS)           :    0.00  /  0.00  /  0.00  /  0.00
PTWH1 : Ewa Beach USGS (13024)      :    0.00  /  0.00  /  0.00  /  0.00
HJR   : Kalaeloa Airport (ASOS)             See note at bottom  :
PLHH1 : Palehua (RAWS)              :    0.01  /  0.01  /  0.02  /  0.03
LUAH1 : Lualualei (13017)           :    0.00  /  0.00  /  0.00  /  0.00
WNVH1 : Waianae Valley (RAWS)       :    0.00  /  0.00  /  0.00  /  0.00
WBHH1 : Waianae Boat Harbor (HSOIS) :    0.00  /  0.00  /  0.00  /  0.00
WAIH1 : Waianae (13014)             :      M   /    M   /    M   /    M
MKHH1 : Makaha Stream (USGS)        :    0.00  /  0.00  /  0.00  /  0.01
MKRH1 : Makua Range (RAWS)          :    0.00  /  0.00  /  0.00  /  0.00
KKRH1 : Kuaokala (RAWS)             :    0.01  /  0.01  /  0.01  /  0.01
:
:Island of Molokai                                 Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
KOPH1 : Keopukaloa (UHM)            :    0.00  /  0.01  /  0.01  /  0.01
HOMH1 : Honolimaloo (UHM)           :    0.00  /  0.02  /  0.06  /  0.12
KMLH1 : Kamalo (14013)              :    0.00  /  0.01  /  0.01  /  0.01
MKPH1 : Makapulapai (RAWS)          :    0.00  /  0.00  /  0.00  /  0.02
PAFH1 : Puu Alii (RAWS)             :    0.06  /  0.21  /  0.25  /  0.73
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
WWKH1 : West Wailuaiki (USGS)       :    0.16  /  0.55  /  1.06  /  2.12
EBYH1 : EMI Baseyard (UHM)          :    0.00  /  0.00  /  0.04  /  0.27
AIKH1 : Haiku (14001)               :    0.01  /  0.01  /  0.02  /  0.09
HOG   : Kahului Airport (ASOS)      :      T   /    T   /    T   /    T
WUKH1 : Wailuku (14007)             :    0.00  /  0.00  /  0.00  /  0.00
KHKH1 : Kahakuloa (14002)           :    0.00  /  0.00  /  0.00  /  0.00
PKKH1 : Puu Kukui (USGS)            :    0.37  /  0.54  /  0.62  /  2.83
:       Leeward/Upcountry Sites
NKUH1 : Na Kula (RAWS)              :    0.00  /  0.00  /  0.00  /  0.00
KPNH1 : Kepuni (USGS)               :    0.00  /  0.00  /  0.00  /  0.00
PILH1 : Piiholo (UHM)               :    0.37  /  0.60  /  0.66  /  0.78
WKTH1 : Waikamoi Treeline (UHM)     :    0.34  /  0.67  /  0.88  /  1.19
PUKH1 : Pukalani (14006)            :    0.10  /  0.15  /  0.15  /  0.15
KBSH1 : Kula Branch Station (14008) :      M   /    M   /    M   /    M
KLGH1 : Kula Ag (UHM)               :    0.00  /  0.00  /  0.00  /  0.00
PHQH1 : Park HQ (UHM)               :    0.12  /  0.20  /  0.23  /  0.23
NNEH1 : Nene Nest (UHM)             :    0.11  /  0.18  /  0.21  /  0.21
SUMH1 : Summit (UHM)                :    0.00  /  0.00  /  0.00  /  0.00
KLFH1 : Kula 1 (RAWS)               :    0.00  /  0.00  /  0.00  /  0.00
KKNH1 : Kahikinui 1 (RAWS)          :    0.00  /  0.00  /  0.00  /  0.00
KMEH1 : Kamehamenui 1 (RAWS)        :    0.00  /  0.00  /  0.00  /  0.00
KKEH1 : Keokea (UHM)                :    0.00  /  0.00  /  0.00  /  0.00
ULUH1 : Ulupalakua (14003)          :    0.00  /  0.00  /  0.00  /  0.00
LPOH1 : Lipoa (UHM)                 :    0.00  /  0.00  /  0.00  /  0.00
KHIH1 : Kihei #2 (14009)            :      M   /    M   /    M   /    M
KPDH1 : Kealia Pond (USFWS)         :    0.00  /  0.00  /  0.00  /  0.00
WCCH1 : Waikapu Country Club (14005):    0.00  /  0.00  /  0.00  /  0.00
HULH1 : Hanaula (UHM)               :    0.02  /  0.03  /  0.03  /  0.13
OLUH1 : Olowalu (UHM)               :    0.00  /  0.00  /  0.00  /  0.02
LAHH1 : Lahainaluna (14011)         :    0.00  /  0.00  /  0.00  /  0.00
LWTH1 : Lahaina WTP (UHM)           :    0.00  /  0.00  /  0.00  /  0.00
HOOH1 : Honolua (UHM)               :    0.01  /  0.01  /  0.01  /  0.06
:
:Island of Hawaii                                  Inches
:ID     Location                         3-Hr    6-Hr   12-Hr   24-Hr
:       Windward Sites
UPLH1 : Upolu Airport (HSOIS)       :    0.00  /  0.00  /  0.07  /  0.20
KMMH1 : Kaluamakani (UHM)           :    0.00  /  0.03  /  0.33  /  0.33
KWSH1 : Kawainui Stream (USGS)      :    1.04  /  2.16  /  3.78  /  5.33
KUUH1 : Kamuela Upper (15002)       :    0.19  /  0.51  /  1.14  /  1.77
KMUH1 : Kamuela (15005)             :    0.23  /  0.47  /  0.84  /  0.90
HNKH1 : Honokaa (15010)             :    0.74  /  1.74  /  2.88  /  3.43
PMLH1 : Puu Mali (RAWS)             :    0.06  /  0.21  /  0.62  /  0.63
WPNH1 : Waipunalei (UHM)            :      M   /    M   /    M   /    M
KNKH1 : Kanakaleonui (UHM)          :    0.49  /  1.46  /  3.28  /  3.53
LPHH1 : Laupahoehoe PD (15001)      :    0.30  /  0.30  /  1.24  /  1.96
LAUH1 : Laupahoehoe (UHM)           :    0.97  /  2.48  /  6.01  /  7.07
SPNH1 : Spencer (UHM)               :    0.93  /  1.05  /  2.29  /  3.94
HKUH1 : Hakalau (RAWS)              :    0.57  /  1.59  /  3.38  /  3.72
KLXH1 : Kulaimano (UHM)             :    0.02  /  0.02  /  0.37  /  1.02
NLIH1 : Honolii Stream (USGS)       :    0.15  /  0.30  /  1.09  /  2.19
SDQH1 : Saddle Quarry (USGS)        :    1.00  /  1.92  /  3.50  /  4.17
PIOH1 : Piihonua (UHM)              :    0.99  /  1.68  /  2.61  /  3.93
PIIH1 : Piihonua (15016)            :    0.00  /  0.01  /  0.01  /  0.03
IPIH1 : IPIF (UHM)                  :    0.00  /  0.01  /  0.39  /  1.33
WKAH1 : Waiakea Uka (15017)         :    0.12  /  0.25  /  0.57  /  1.65
WEXH1 : Waiakea Exp Stn (NOAA/CRN)  :    0.01  /  0.01  /  0.26  /  0.78
HTO   : Hilo Airport (ASOS)         :    0.00  /  0.00  /  0.08  /  1.01
PHAH1 : Pahoa (15015)               :    0.00  /  0.01  /  0.54  /  1.60
PAOH1 : Pahoa (UHM)                 :    0.01  /  0.01  /  0.46  /  1.36
MTVH1 : Mountain View (15014)       :    0.04  /  0.20  /  0.92  /  2.23
GLNH1 : Glenwood (15013)            :    0.67  /  1.62  /  2.92  /  4.14
:       Leeward Sites
MOBH1 : Mauna Loa Ob Stn (NOAA/CRN) :    0.04  /  0.23  /  0.72  /  0.75
NHKH1 : Nahuku (UHM)                :    0.65  /  1.51  /  3.00  /  3.63
KKUH1 : Keaumo (RAWS)               :    0.30  /  0.77  /  1.64  /  1.66
KMOH1 : Kealakomo (RAWS)            :    0.10  /  0.13  /  0.30  /  0.33
PLIH1 : Pali 2 (RAWS)               :    0.05  /  0.17  /  0.28  /  0.28
KPRH1 : Kapapala (RAWS)             :    0.00  /  0.00  /  0.02  /  0.04
KAYH1 : Kapapala Ranch (15003)      :    0.00  /  0.00  /  0.00  /  0.00
PPLH1 : Pahala (15004)              :    0.02  /  0.05  /  0.11  /  0.18
KIOH1 : Kaiholena (UHM)             :      M   /    M   /    M   /    M
NENH1 : Nene Cabin (RAWS)           :    0.03  /  0.06  /  0.75  /  0.76
SOPH1 : South Point (HSOIS)         :    0.07  /  0.33  /  0.50  /  0.51
LKHH1 : Lower Kahuku (RAWS)         :    0.10  /  0.30  /  0.96  /  0.97
KRCH1 : Kahuku Ranch (RAWS)         :    0.00  /  0.00  /  0.01  /  0.01
KOMH1 : Kona Hema (UHM)             :    0.00  /  0.00  /  0.01  /  0.02
PHRH1 : Puho CS (RAWS)              :    0.00  /  0.00  /  0.00  /  0.00
HAUH1 : Honaunau (15007)            :    0.00  /  0.00  /  0.01  /  0.02
KLEH1 : Kealakekua (15008)          :    0.00  /  0.00  /  0.00  /  0.02
WIHH1 : Waiaha Stream (15009)       :    0.00  /  0.00  /  0.01  /  0.01
KOUH1 : Keahuolu (UHM)              :    0.00  /  0.00  /  0.01  /  0.01
KHOH1 : Kaloko-Honokohau (RAWS)     :    0.00  /  0.00  /  0.00  /  0.00
HKO   : Kona Intl Airport (ASOS)    :    0.00  /  0.00  /  0.00  /  0.00
PLMH1 : Palamanui (UHM)             :    0.00  /  0.00  /  0.00  /  0.01
KIRH1 : Kiholo RG (USGS)            :    0.00  /  0.00  /  0.00  /  0.00
KPLH1 : Kaupulehu (RAWS)            :    0.00  /  0.00  /  0.00  /  0.00
PULH1 : Puuanahulu (RAWS)           :    0.00  /  0.00  /  0.00  /  0.00
MMLH1 : Mamalahoa (UHM)             :    0.00  /  0.00  /  0.00  /  0.00
PWWH1 : Puu Waawaa (RAWS)           :    0.00  /  0.00  /  0.00  /  0.00
PWAH1 : Puu Waawaa (UHM)            :    0.01  /  0.01  /  0.01  /  0.01
KIUH1 : Kaiaulu Puu Waawaa (UHM)    :    0.00  /  0.00  /  0.00  /  0.00
PKAH1 : Pohakuloa Kipuka Alala RAWS :    0.00  /  0.00  /  0.00  /  0.00
PTRH1 : Pohakuloa Range 17 (RAWS)   :    0.00  /  0.00  /  0.00  /  0.00
PKWH1 : Pohakuloa West (RAWS)       :    0.00  /  0.00  /  0.00  /  0.00
PKMH1 : Pohakuloa Keamuku (RAWS)    :    0.00  /  0.00  /  0.00  /  0.00
AHMH1 : Ahumoa (RAWS)               :    0.00  /  0.00  /  0.00  /  0.00
WHIH1 : Waikii (15011)              :    0.00  /  0.00  /  0.00  /  0.00
LLAH1 : Lalamilo (UHM)              :    0.03  /  0.12  /  0.24  /  0.31
WKVH1 : Waikoloa (RAWS)             :    0.00  /  0.00  /  0.00  /  0.00
PERH1 : Puhe CS (RAWS)              :    0.00  /  0.00  /  0.00  /  0.00
KHRH1 : Kohala Ranch (RAWS)         :    0.00  /  0.00  /  0.00  /  0.00
KASH1 : Kahua Ranch (15006)         :    0.29  /  0.58  /  0.88  /  1.08
KEHH1 : Kehena (UHM)                :    0.63  /  1.32  /  2.45  /  3.27
PLAH1 : Puuloa (UHM)                :    0.21  /  0.51  /  0.79  /  0.79
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
| **Collected** | 2026-09-26T01:59:41.571061-10:00 HST |

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
| **Collected** | 2026-09-26T00:30:35.265615-10:00 HST |

```text
088
FZPN40 PHFO 261021
HSFNP

HIGH SEAS FORECAST
NATIONAL WEATHER SERVICE HONOLULU HI
1100 UTC SAT SEP 26 2026

SUPERSEDED BY NEXT ISSUANCE IN 6 HOURS

SEAS GIVEN AS SIGNIFICANT WAVE HEIGHT...WHICH IS THE AVERAGE HEIGHT
OF THE HIGHEST 1/3 OF THE WAVES. INDIVIDUAL WAVES MAY BE MORE THAN
TWICE THE SIGNIFICANT WAVE HEIGHT.

THIS HIGH SEAS FORECAST USES 1-MINUTE AVERAGE WINDS WHICH MAY BE
HIGHER THAN 10-MINUTE AVERAGE WINDS.

SECURITE

NORTH PACIFIC EQUATOR TO 30N BETWEEN 140W AND 180W

SYNOPSIS VALID 0600 UTC SEP 26 2026.
24 HOUR FORECAST VALID 0600 UTC SEP 27 2026.
48 HOUR FORECAST VALID 0600 UTC SEP 28 2026.

.WARNINGS.

...HURRICANE WARNING...
.HURRICANE NOLO NEAR 16.9N 155.3W 975 MB AT 0900 UTC SEP 26
AND QUASI STATIONARY. MAXIMUM SUSTAINED WINDS 90 KT GUSTS 110 KT.
TROPICAL STORM FORCE WINDS WITHIN 120 NM N SEMICIRCLE AND 100 NM
S SEMICIRCLE. WINDS 20 TO 30 KT ELSEWHERE FROM 14N TO 27N BETWEEN
150W AND 160W. SEAS 4 M OR GREATER WITHIN 180 NM S SEMICIRCLE...
210 NM NE QUADRANT AND 150 NM NW QUADRANT WITH SEAS TO 8.5 M. SEAS
2.5 TO 3.5 M ELSEWHERE FROM 11N TO 26N BETWEEN 150W AND 160W.
SCATTERED TO NUMEROUS MODERATE TSTMS WITHIN 100 NM SW SEMICIRCLE
AND 60 NM NE SEMICIRCLE FROM CENTER.
.24 HOUR FORECAST HURRICANE NOLO NEAR 16.8N 156.9W. MAXIMUM
SUSTAINED WINDS 105 KT GUSTS 130 KT. TROPICAL STORM FORCE WINDS
WITHIN 80 NM S SEMICIRCLE...140 NM NE QUADRANT AND 110 NM NW
QUADRANT. WINDS 20 TO 30 KT ELSEWHERE FROM 14N TO 27N BETWEEN 150W
AND 161W. SEAS 4 M OR GREATER FROM 15N TO 20N BETWEEN 154W AND
159W WITH SEAS TO 9.5 M. SEAS 2.5 TO 3.5 M ELSEWHERE FROM 12N TO
29N BETWEEN 150W AND 163W.
.48 HOUR FORECAST HURRICANE NOLO NEAR 17.2N 160.6W. MAXIMUM
SUSTAINED WINDS 120 KT GUSTS 145 KT. TROPICAL STORM FORCE WINDS
WITHIN 150 NM NE QUADRANT...90 NM SE QUADRANT...70 NM SW QUADRANT
AND 100 NM NW QUADRANT. WINDS 20 TO 30 KT ELSEWHERE FROM 15N TO
26N BETWEEN 154W AND 163W. SEAS 4 M OR GREATER FROM 14N TO 19N
BETWEEN 157W AND 164W WITH SEAS TO 10.5 M. SEAS 2.5 TO 3.5 M
ELSEWHERE FROM 10N TO 30N BETWEEN 155W AND 170W.

FORECAST WINDS IN AND NEAR ACTIVE TROPICAL CYCLONES SHOULD BE
USED WITH CAUTION DUE TO UNCERTAINTY IN FORECAST TRACK...SIZE
AND INTENSITY.

.SYNOPSIS AND FORECAST.

.LOW 1011 MB 09N177W NEARLY STATIONARY. ISOLATED MODERATE TSTMS N
OF LOW WITHIN 50 NM OF 12N177W.
.24 HOUR FORECAST LOW ABSORBED BY MONSOON TROUGH.

.TROUGH 18N175W TO 22N174W TO 27N171W MOVING W 10 KT.
.24 HOUR FORECAST TROUGH 19N179W TO 23N179W TO 27N178W.
.48 HOUR FORECAST TROUGH MOVED W OF AREA.

.WINDS 20 TO 25 KT FROM 19N TO 26N BETWEEN 140W AND 150W...AND
FROM 21N TO 26N BETWEEN 160W AND 166W. SEAS 2.5 TO 3 M FROM 15N TO
25N BETWEEN 140W AND 150W...AND FROM 14N TO 26N BETWEEN 160W AND
165W.
.24 HOUR FORECAST WINDS 20 TO 25 KT FROM 15N TO 27N BETWEEN 140W
AND 150W...AND 20 TO 30 KT FROM 18N TO 27N BETWEEN 161W AND 167W.
SEAS 2.5 TO 3 M FROM 13N TO 26N BETWEEN 140W AND 150W...AND FROM
16N TO 30N BETWEEN 163W AND 170W.
.48 HOUR FORECAST WINDS 20 TO 25 KT FROM 15N TO 26N BETWEEN 140W
AND 154W...AND FROM 18N TO 26N BETWEEN 163W AND 171W. SEAS 2.5 TO
3 M FROM 13N TO 28N BETWEEN 140W AND 155W...AND FROM 18N TO 29N
BETWEEN 170W AND 174W.

.24 HOUR FORECAST NEW LOW 1008 MB NEAR 12N140W. WINDS 20 TO 25 KT
FROM 08N TO 13N E OF 142W. SEAS 2.5 TO 3 M FROM 09N TO 12N E OF
144W.
.48 HOUR FORECAST LOW 1007 MB NEAR 13N142W. WINDS 20 TO 25 KT
FROM 07N TO 09N E OF 144W. SEAS 2.5 TO 3 M FROM 07N TO 12N E OF
145W.

.WINDS 20 KT OR LESS AND SEAS BELOW 2.5 M OVER REMAINDER OF
FORECAST AREA.

.MONSOON TROUGH 14N140W TO 16N150W...AND 14N166W TO LOW MENTIONED
ABOVE TO 10N180W. SCATTERED MODERATE TSTMS WITHIN 50 NM OF TROUGH
BETWEEN 140W AND 144W...AND S OF TROUGH FROM 00N TO 09N BETWEEN
160W AND 176W. SCATTERED MODERATE TO STRONG TSTMS S OF TROUGH
FROM 02N TO 11N E OF 145W.

.FORECASTER CHAN. HONOLULU HI.
```

---

### 12. Hourly Wind/Precip Observations

| Field | Value |
|---|---|
| **Resource ID** | oso_hourly_obs |
| **Official source** | https://forecast.weather.gov/product.php?site=HFO&product=OSO&issuedby=HFO |
| **Collected** | 2026-09-26T00:54:01.929301-10:00 HST |

```text
583
SXHW50 PHFO 260044
OSOHFO

Hawaii Wind Data
National Weather Service Honolulu HI
243 PM HST Fri Sep 25 2026

W I N D D A T A
----------------------
IN KNOTS
ID Location Date Time DIR SPD GUST
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
0000PAKH1 Port Allen Kauai 25Sep26 14:00 80 17 29
0000MKAH1 Makaha Ridge Kauai 25Sep26 14:11 60 4 15
0000MNRH1 Mana Kauai 25Sep26 14:34 250 4 11
0000PHBK Barking Sands Kauai 25Sep26 14:00 240 6 MSG
0000PLRH1 Puu Lua Kauai 25Sep26 14:35 90 7 18
0000POPH1 Puu Opae Kauai 25Sep26 14:34 200 4 20
0000WHGH1 Waimea Heights Kauai 25Sep26 14:35 30 6 10

0000KRGH1 Kalahee Ridge Oahu 25Sep26 14:10 40 8 20
0000KAHH1 Kahuku Oahu MSG MSG MSG MSG
0000KTAH1 Kahuku Trng Oahu 25Sep26 13:59 100 3 22
0000KFWH1 Kii Oahu 25Sep26 13:45 70 15 23
0000OFRH1 Oahu Forest NWR Oahu 25Sep26 14:36 80 27 44
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
0000SCEH1 Schofield East Oahu MSG MSG MSG MSG
0000HWLH1 HECO Wilikina Oahu 25Sep26 14:30 30 4 10
0000PHJR Kalaeloa Oahu 25Sep26 14:18 50 9 25
0000HFHH1 HECO Farrington Oahu 25Sep26 14:30 70 11 22
0000HPLH1 HECO Palehua Oahu 25Sep26 14:30 60 10 22
0000HPDH1 HECO Palehua 2 Oahu 25Sep26 14:30 60 17 25
0000HPHH1 HECO Palehua 3 Oahu 25Sep26 14:30 50 9 19
0000HPRH1 HECO Paakea Oahu 25Sep26 14:30 30 9 25
0000HLRH1 HECO Lualualei Oahu 25Sep26 14:30 50 11 22
0000HWVH1 HECO Waianae Vly Oahu 25Sep26 14:30 10 7 17
0000PLHH1 Palehua Oahu 25Sep26 14:36 50 0 0
0000WNVH1 Waianae Valley Oahu 25Sep26 14:37 60 8 30
0000HHSH1 HECO Ala Hema St Oahu 25Sep26 14:30 90 6 12
0000WBHH1 Waianae Harbor Oahu MSG MSG MSG MSG
0000HKRH1 HECO Kili Dr Oahu 25Sep26 14:30 340 8 16
0000HMVH1 HECO Makaha Vly Oahu 25Sep26 14:30 340 8 20
0000MKRH1 Makua Range Oahu 25Sep26 13:58 70 14 29
0000KKRH1 Kuaokala Oahu 25Sep26 14:36 30 14 36
0000AALH1 Kaala Oahu 25Sep26 14:15 60 6 13
0000HFRH1 HECO Farrington2 Oahu 25Sep26 14:30 60 7 15
0000HFYH1 HECO Farrington3 Oahu 25Sep26 14:30 70 17 23
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
0000SUMH1 Summit Maui 25Sep26 14:15 80 7 10
0000NNEH1 Nene Nest Maui 25Sep26 14:15 130 2 5
0000PHQH1 Park HQ Maui 25Sep26 14:15 70 2 8
0000WKTH1 Waikamoi Treeline Maui 25Sep26 14:15 130 4 10
0000MCTH1 MECO Crater Rd Maui 25Sep26 14:30 300 2 4
0000KLGH1 Kula Ag Maui 25Sep26 14:15 280 3 7
0000MWAH1 MECO Waipoli Rd Maui 25Sep26 14:30 270 2 5
0000KKEH1 Keokea Maui 25Sep26 14:15 290 2 5
0000MKUH1 MECO Kula Maui 25Sep26 14:30 200 5 9
0000PHUH1 Pulehu Maui 25Sep26 14:15 220 5 11
0000MNDH1 MECO Naalaea Rd Maui 25Sep26 14:30 210 5 9
0000MURH1 MECO Ulupalakua Maui 25Sep26 14:30 180 9 15
0000LPOH1 Lipoa Maui 25Sep26 14:15 190 8 15
0000MVHH1 MECO Veterans Hwy Maui 25Sep26 14:30 330 20 29
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

0000UPLH1 Upolu Airport Hawaii 25Sep26 14:15 90 15 23
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
0000WEXH1 Waiakea Exp Stn Hawaii 25Sep26 14:00 MSG 1 4
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
0000SOPH1 South Point Hawaii 25Sep26 14:00 60 14 24
0000KOMH1 Kona Hema Hawaii 25Sep26 14:15 230 4 5
0000KRCH1 Kahuku Ranch Hawaii 25Sep26 14:29 300 4 12
0000PHRH1 Puho CS Hawaii 25Sep26 14:22 290 3 7
0000HLNH1 HELCO Lolo Ln Hawaii 25Sep26 14:30 270 2 4
0000HHUH1 HELCO Hualalai Rd Hawaii 25Sep26 14:30 280 2 5
0000KOUH1 Keahuolu Hawaii 25Sep26 14:15 270 2 3
0000PHKO Kona Intl AP Hawaii 25Sep26 14:00 230 7 MSG
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
0000PKWH1 PTA West Hawaii 25Sep26 13:56 320 7 15
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
| **Collected** | 2026-09-26T02:04:20.716491-10:00 HST |

```text
172 ACCA62 KNHC 261200TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL800 AM EDT sábado 26 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Tormenta Tropical Gonzalo, ubicada justo aleste-noreste de las Islas de Cabo Verde, y sobre la DepresiónTropical Fay, ubicada al oeste-suroeste de las Azores.No se espera la formación de ciclones tropicales durante lospróximos 7 días.$$Pronosticador Katz*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 18. NHC Atlantic Tropical Weather Outlook — 7 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_atlc_7day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=atlc&fdays=7 |
| **Collected** | 2026-09-26T02:05:20.693263-10:00 HST |

```text
172 ACCA62 KNHC 261200TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL800 AM EDT sábado 26 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Tormenta Tropical Gonzalo, ubicada justo aleste-noreste de las Islas de Cabo Verde, y sobre la DepresiónTropical Fay, ubicada al oeste-suroeste de las Azores.No se espera la formación de ciclones tropicales durante lospróximos 7 días.$$Pronosticador Katz*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 19. NHC Central Pacific Tropical Weather Outlook — 2 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_cpac_2day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=cpac&fdays=2 |
| **Collected** | 2026-09-26T02:00:22.045852-10:00 HST |

```text
033 ACCA62 KNHC 261143TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL800 AM EDT sábado 26 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Tormenta Tropical Gonzalo, ubicada justo aleste-noreste de las Islas de Cabo Verde, y sobre la TormentaTropical Fay, ubicada al oeste-suroeste de las Azores.No se espera la formación de ciclones tropicales durante lospróximos 7 días.$$Pronosticador Katz*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 20. NHC Central Pacific Tropical Weather Outlook — 7 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_cpac_7day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=cpac&fdays=7 |
| **Collected** | 2026-09-26T02:01:20.538462-10:00 HST |

```text
172 ACCA62 KNHC 261200TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL800 AM EDT sábado 26 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Tormenta Tropical Gonzalo, ubicada justo aleste-noreste de las Islas de Cabo Verde, y sobre la DepresiónTropical Fay, ubicada al oeste-suroeste de las Azores.No se espera la formación de ciclones tropicales durante lospróximos 7 días.$$Pronosticador Katz*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 21. NHC Eastern Pacific Tropical Weather Outlook — 2 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_epac_2day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=epac&fdays=2 |
| **Collected** | 2026-09-26T02:02:20.943218-10:00 HST |

```text
172 ACCA62 KNHC 261200TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL800 AM EDT sábado 26 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Tormenta Tropical Gonzalo, ubicada justo aleste-noreste de las Islas de Cabo Verde, y sobre la DepresiónTropical Fay, ubicada al oeste-suroeste de las Azores.No se espera la formación de ciclones tropicales durante lospróximos 7 días.$$Pronosticador Katz*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 22. NHC Eastern Pacific Tropical Weather Outlook — 7 day

| Field | Value |
|---|---|
| **Resource ID** | nhc_gtwo_epac_7day |
| **Official source** | https://www.nhc.noaa.gov/gtwo.php?basin=epac&fdays=7 |
| **Collected** | 2026-09-26T02:03:20.649046-10:00 HST |

```text
172 ACCA62 KNHC 261200TWOSATPerspectiva de tiempo tropicalCentro Nacional de Huracanes del SNM Miami FL800 AM EDT sábado 26 de septiembre de 2026Para el Atlántico Norte...Mar Caribe y el Golfo de AméricaSistemas activos: El Centro Nacional de Huracanes está emitiendoadvertencias sobre la Tormenta Tropical Gonzalo, ubicada justo aleste-noreste de las Islas de Cabo Verde, y sobre la DepresiónTropical Fay, ubicada al oeste-suroeste de las Azores.No se espera la formación de ciclones tropicales durante lospróximos 7 días.$$Pronosticador Katz*** Este producto ha sido procesado automáticamente utilizando unprograma de traducción y puede contener omisiones y errores. ElServicio Nacional de Meteorología no puede garantizar la precisióndel texto convertido. De haber alguna duda, el texto en inglés essiempre la versión autorizada. ***
```

---

### 23. NHC source index

| Field | Value |
|---|---|
| **Resource ID** | nhc_homepage |
| **Official source** | https://www.nhc.noaa.gov/ |
| **Collected** | 2026-09-26T02:06:20.745184-10:00 HST |

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

Last update Sat, 26 Sep 2026 12:00:28 UTC

NHC issuing advisories for the Atlantic on

TD Fay

and

TS Gonzalo

NHC issuing advisories for the Eastern Pacific on

Hurricane Odalys

and

Hurricane Polo

NHC issuing advisories for the Central Pacific on

Hurricane Nolo

Marine warnings are in effect for the Eastern Pacific

Key messages regarding Hurricane Polo

(en Español: Mensajes Claves)

Key messages regarding Hurricane Nolo

(en Español: Mensajes Claves)

Local info on Nolo:
Honolulu

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

2

Disturbances:

ALL

1

2

Disturbances:

ALL

1

2

Disturbances:

ALL

1

2

Disturbances:

ALL

1

2

Disturbances:

ALL

1

2

Disturbances:

ALL

1

2

Disturbances:

ALL

1

2

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

Central North Pacific
(140°W to 180°)

Tropical Weather Outlook

(en Español*)

200 AM HST Sat Sep 26 2026

Hurricane Nolo

Satellite |
Buoys |
Grids |
Storm Archive

...NOLO STILL NEARLY STATIONARY SOUTH OF THE BIG ISLAND OF HAWAII...
...EXPECTED TO STRENGTHEN DURING THE NEXT COUPLE OF DAYS WHILE REMAINING WELL SOUTH OF THE HAWAIIAN ISLANDS...

2:00 AM HST Sat Sep 26

Location: 16.9°N 155.3°W

Moving: Stationary

Min pressure: 975 mb

Max sustained: 105 mph

Public

Advisory

#23A

200 AM HST

Forecast

Advisory

#23

0900 UTC

Forecast

Discussion

#23

1100 PM HST

Wind Speed

Probabilities

#23

0900 UTC

NWS Local

Products

1115 PM HST

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

Peak
Surge

Rainfall
Potential

Atlantic - Caribbean Sea - Gulf of America

Tropical Weather Outlook

(en Español*)

800 AM EDT Sat Sep 26 2026

Tropical Weather Discussion

1215 UTC Sat Sep 26 2026

Tropical Storm Gonzalo

Satellite |
Buoys |
Grids |
Storm Archive

...GONZALO STILL A TROPICAL STORM AS IT MOVES AWAY FROM THE CABO VERDE ISLANDS...

8:00 AM CVT Sat Sep 26

Location: 17.6°N 23.0°W

Moving: N at 9 mph

Min pressure: 1002 mb

Max sustained: 45 mph

Public

Advisory

#6

800 AM CVT

Forecast

Advisory

#6

0900 UTC

Forecast

Discussion

#6

800 AM CVT

Wind Speed

Probabilities

#6

0900 UTC

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

Tropical Depression Fay

Satellite |
Buoys |
Grids |
Storm Archive

...FAY WEAKENS TO A TROPICAL DEPRESSION ONCE AGAIN...

9:00 AM GMT Sat Sep 26

Location: 29.7°N 43.7°W

Moving: WSW at 3 mph

Min pressure: 1009 mb

Max sustained: 35 mph

Public

Advisory

#25

900 AM GMT

Forecast

Advisory

#25

0900 UTC

Forecast

Discussion

#25

900 AM GMT

Wind Speed

Probabilities

#25

0900 UTC

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

Eastern North Pacific
(East of 140°W)

Tropical Weather Outlook

(en Español*)

500 AM PDT Sat Sep 26 2026

Tropical Weather Discussion

1005 UTC Sat Sep 26 2026

Hurricane Polo

Satellite |
Buoys |
Grids |
Storm Archive

...POLO MOVING WEST-NORTHWESTWARD AS AN EXTREMELY DANGEROUS CATEGORY 5 HURRICANE...
...EXPECTED TO MAKE LANDFALL IN BAJA CALIFORNIA SUR ON MONDAY AS A POWERFUL HURRICANE...

5:00 AM MST Sat Sep 26

Location: 17.7°N 111.5°W

Moving: WNW at 10 mph

Min pressure: 922 mb

Max sustained: 160 mph

Public

Advisory

#23A

500 AM MST

Forecast

Advisory

#23

0900 UTC

Forecast

Discussion

#23

200 AM MST

Wind Speed

Probabilities

#23

0900 UTC

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

Hurricane Odalys

Satellite |
Buoys |
Grids |
Storm Archive

...ODALYS BEGINS WEAKENING AS IT CONTINUES TRACKING NORTHWARD...

2:00 AM PDT Sat Sep 26

Location: 19.1°N 123.7°W

Moving: N at 5 mph

Min pressure: 951 mb

Max sustained: 115 mph

Public

Advisory

#26

200 AM PDT

Forecast

Advisory

#26

0900 UTC

Forecast

Discussion

#26

200 AM PDT

Wind Speed

Probabilities

#26

0900 UTC

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
| **Collected** | 2026-09-25T20:03:50.351846-10:00 HST |

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
| **Collected** | 2026-09-25T23:16:41.129828-10:00 HST |

```text
442
FZHW60 PHFO 260909
OFFHFO

Offshore Waters Forecast for Hawaii
National Weather Service Honolulu HI
1109 PM HST Fri Sep 25 2026

Hawaiian offshore waters beyond 40 nautical miles out to 240
nautical miles including the portion of the Papahanaumokuakea
Marine National Monument east of French Frigate Shoals

Seas given as significant wave height, which is the average height
of the highest 1/3 of the waves. Individual waves may be more than
twice the significant wave height.

PHZ105-261630-
1109 PM HST Fri Sep 25 2026

.Synopsis for the Hawaiian offshore waters...
Strong winds and hazardous seas will accompany Hurricane Nolo as
it advances west across area waters through this weekend, then
turns northwest early next week and weakens to a tropical storm by
Wednesday.

AT 1100 PM HST HURRICANE NOLO WAS CENTERED AT 16.9N
155.3W...NEARLY STATIONARY

NOLO FORECAST POSITIONS
800 AM HST SATURDAY 17.0N 155.7W
800 PM HST SATURDAY 16.8N 156.9W
800 AM HST SUNDAY 16.8N 158.7W
800 PM HST SUNDAY 17.2N 160.6W
800 AM HST MONDAY 18.4N 162.3W
800 PM HST MONDAY 20.1N 163.4W
800 PM HST TUESDAY 22.9N 165.0W
800 PM HST MONDAY 23.3N 167.2W
800 PM HST TUESDAY 23.5N 170.0W
800 PM HST WEDNESDAY 23.5N 173.0W

PHZ180-261630-
Hawaiian Offshore Waters-
1109 PM HST Fri Sep 25 2026

...HURRICANE WARNING IN EFFECT...

.REST OF TONIGHT...Hurricane conditions expected S of 19N.
Elsewhere, NE to E winds 15 to 25 kt. Seas 9 to 16 ft. Isolated
thunderstorms S of 19N.
.SATURDAY...Hurricane conditions expected S of 19N. Elsewhere, NE
to E winds 20 to 30 kt. Seas 9 to 15 ft. Isolated thunderstorms
S of 19N.
.SATURDAY NIGHT...Hurricane conditions expected S of 19N. Elsewhere,
NE to E winds 20 to 30 kt. Seas 11 to 15 ft. Isolated
thunderstorms S of 19N.
.SUNDAY...Hurricane conditions expected S of 20N. Elsewhere, E
winds 20 to 30 kt. Seas 10 to 14 ft. Isolated thunderstorms S of
20N.
.SUNDAY NIGHT...Hurricane conditions possible SW waters.
Elsewhere, E winds 15 to 25 kt. Seas 9 to 14 ft. Isolated
thunderstorms SW waters.
.MONDAY...Hurricane conditions possible W of 160W. Elsewhere, E
to SE winds 15 to 25 kt. Seas 8 to 14 ft. Isolated thunderstorms W
of 160W.
.TUESDAY...Hurricane conditions possible W of 161W. Elsewhere, E
to SE winds 10 to 20 kt. Seas 6 to 13 ft. Isolated thunderstorms
W of 161W.
.WEDNESDAY...Tropical storm conditions possible W of 162W.
Elsewhere, E to SE winds 10 to 20 kt. Seas 6 to 10 ft. Isolated
thunderstorms W of 162W.
```

---

### 26. Radar status/outage text messages

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

### 27. State Forecast for Hawaii

| Field | Value |
|---|---|
| **Resource ID** | sfp_state_forecast |
| **Official source** | https://api.weather.gov/products/types/SFP/locations/HFO |
| **Collected** | 2026-09-25T21:37:10.649570-10:00 HST |

```text
000
FPHW60 PHFO 260259
SFPHFO

State Forecast for Hawaii
National Weather Service Honolulu HI
459 PM HST Fri Sep 25 2026

HIZ001-003-004-006-007-009>011-015>018-022-029>050-261615-
Kauai-Oahu-Maui-Molokai-Lanai-
459 PM HST Fri Sep 25 2026

...FLOOD WATCH FOR MOLOKAI LANAI KAHOOLAWE AND MAUI...
...HIGH SURF ADVISORY FOR KAUAI OAHU MOLOKAI AND MAUI...
...TROPICAL STORM WATCH FOR MOLOKAI LANAI KAHOOLAWE AND MAUI...
...WIND ADVISORY FOR NIIHAU KAUAI AND OAHU...

.TONIGHT...Mostly cloudy. Windy. Scattered showers on Kauai.
scattered showers and isolated thunderstorms Oahu and Maui
County. Locally heavy rainfall possible. Lows 75 to 80. East
winds 20 to 35 mph with gusts to 60 mph. 
.SATURDAY...Mostly cloudy. Very windy. Scattered showers on
Kauai. scattered showers and isolated thunderstorms Oahu and Maui
County. Locally heavy rainfall possible. Highs 85 to 90. East
winds 25 to 40 mph with gusts to 60 mph. 
.SATURDAY NIGHT...Mostly cloudy. Very windy. On Kauai and Oahu,
isolated showers. Maui County, scattered showers in the evening.
Isolated showers after midnight. Lows 74 to 79. East winds 30 to
45 mph with gusts to 65 mph. 
.SUNDAY...Mostly cloudy. Very windy. On Kauai and Oahu, isolated
showers. Maui County, scattered showers during the day. Isolated
showers at night. Highs 85 to 90. Lows 74 to 79. East winds 30 to
45 mph with gusts to 75 mph. 
.MONDAY...Mostly cloudy. Windy. Isolated showers windward and
mountains. Highs 86 to 91. Lows 74 to 79. East winds 20 to
35 mph. 
.TUESDAY...Mostly cloudy. Breezy. Windward and mountains,
isolated showers. Leeward, scattered showers during the day.
Isolated showers at night. Highs 86 to 91. Lows 74 to 79. East
winds 15 to 25 mph. 
.WEDNESDAY...Mostly cloudy. Breezy. On Kauai, scattered showers
during the day, then isolated showers at night. Oahu and Maui
County, isolated showers. Highs 84 to 89. Lows 73 to 78. East
winds 15 to 25 mph. 

HIZ023-026>028-051>054-261615-
Big Island of Hawaii-
459 PM HST Fri Sep 25 2026

...FLOOD WATCH...
...HIGH SURF ADVISORY...
...HURRICANE WATCH...
...TROPICAL STORM WARNING...

.TONIGHT...Very windy. Occasional showers and isolated
thunderstorms windward. scattered showers and isolated
thunderstorms leeward. Locally heavy rainfall possible. Lows
73 to 78. Northeast winds 30 to 45 mph with gusts to 70 mph. 
.SATURDAY...Very windy. Windward, occasional showers and isolated
thunderstorms. Leeward, scattered showers and isolated
thunderstorms through the day. Locally heavy rainfall possible.
Highs 85 to 90. East winds 30 to 45 mph with gusts to 75 mph. 
.SATURDAY NIGHT...Mostly cloudy. Very windy. Windward, occasional
showers. Leeward, scattered showers in the evening, then isolated
showers after midnight. Lows 72 to 77. East winds 30 to 45 mph
with gusts to 80 mph. 
.SUNDAY...Mostly cloudy. Very windy. Windward, scattered showers
during the day, then isolated showers at night. Leeward, isolated
showers. Highs 85 to 90. Lows 73 to 78. East winds 25 to 40 mph
with gusts to 65 mph. 
.MONDAY...Mostly cloudy. Windward, isolated showers during the
day. Scattered showers at night. Leeward, isolated showers. Highs
86 to 91. Lows 72 to 77. East winds 15 to 20 mph. 
.TUESDAY...Mostly cloudy. Scattered showers windward. isolated
showers leeward. Highs 85 to 90. Lows 72 to 77. Southeast winds
around 15 mph. 
.WEDNESDAY...Mostly cloudy. Isolated showers. Highs 84 to 89.
Lows 72 to 77. Southeast winds around 15 mph.
```

---

### 28. Statewide Surf Observations

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

### 29. Tsunami Bulletin product type reference

| Field | Value |
|---|---|
| **Resource ID** | hfo_tib_reference |
| **Official source** | https://forecast.weather.gov/product_types.php |
| **Collected** | 2026-09-26T01:59:23.986726-10:00 HST |

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

Brochures

Weather-Ready Nation

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
