# SZ.INDUSTRY.ECONOMIC.CODES — Table Schema

> Source: `INSERTS/I_F.SZ.INDUSTRY.ECONOMIC.CODES` in `SZ_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SZ.IEC.INDUSTRY.CODE.DESC` | `SzIndustryEconomicCodes_IndustryCodeDesc` |  |  |  |
| 2 | `SZ.IEC.INDUSTRY` | `SzIndustryEconomicCodes_Industry` | TField |  | Temenos Industry code as held in TRANSACT Validation: Must be a relevant code in INDUSTRY table |
| 3 | `SZ.IEC.RESERVED.74` | `SzIndustryEconomicCodes_Reserved74` | TField |  |  |
| 4 | `SZ.IEC.RESERVED.73` | `SzIndustryEconomicCodes_Reserved73` | TField |  |  |
| 5 | `SZ.IEC.RESERVED.72` | `SzIndustryEconomicCodes_Reserved72` | TField |  |  |
| 6 | `SZ.IEC.RESERVED.71` | `SzIndustryEconomicCodes_Reserved71` | TField |  |  |
| 7 | `SZ.IEC.RESERVED.70` | `SzIndustryEconomicCodes_Reserved70` | TField |  |  |
| 8 | `SZ.IEC.RESERVED.69` | `SzIndustryEconomicCodes_Reserved69` | TField |  |  |
| 9 | `SZ.IEC.RESERVED.68` | `SzIndustryEconomicCodes_Reserved68` | TField |  |  |
| 10 | `SZ.IEC.RESERVED.67` | `SzIndustryEconomicCodes_Reserved67` | TField |  |  |
| 11 | `SZ.IEC.RESERVED.66` | `SzIndustryEconomicCodes_Reserved66` | TField |  |  |
| 12 | `SZ.IEC.RESERVED.65` | `SzIndustryEconomicCodes_Reserved65` | TField |  |  |
| 13 | `SZ.IEC.RESERVED.64` | `SzIndustryEconomicCodes_Reserved64` | TField |  |  |
| 14 | `SZ.IEC.RESERVED.63` | `SzIndustryEconomicCodes_Reserved63` | TField |  |  |
| 15 | `SZ.IEC.RESERVED.62` | `SzIndustryEconomicCodes_Reserved62` | TField |  |  |
| 16 | `SZ.IEC.RESERVED.61` | `SzIndustryEconomicCodes_Reserved61` | TField |  |  |
| 17 | `SZ.IEC.RESERVED.60` | `SzIndustryEconomicCodes_Reserved60` | TField |  |  |
| 18 | `SZ.IEC.RESERVED.59` | `SzIndustryEconomicCodes_Reserved59` | TField |  |  |
| 19 | `SZ.IEC.RESERVED.58` | `SzIndustryEconomicCodes_Reserved58` | TField |  |  |
| 20 | `SZ.IEC.RESERVED.57` | `SzIndustryEconomicCodes_Reserved57` | TField |  |  |
| 21 | `SZ.IEC.RESERVED.56` | `SzIndustryEconomicCodes_Reserved56` | TField |  |  |
| 22 | `SZ.IEC.RESERVED.55` | `SzIndustryEconomicCodes_Reserved55` | TField |  |  |
| 23 | `SZ.IEC.RESERVED.54` | `SzIndustryEconomicCodes_Reserved54` | TField |  |  |
| 24 | `SZ.IEC.RESERVED.53` | `SzIndustryEconomicCodes_Reserved53` | TField |  |  |
| 25 | `SZ.IEC.RESERVED.52` | `SzIndustryEconomicCodes_Reserved52` | TField |  |  |
| 26 | `SZ.IEC.RESERVED.51` | `SzIndustryEconomicCodes_Reserved51` | TField |  |  |
| 27 | `SZ.IEC.RESERVED.50` | `SzIndustryEconomicCodes_Reserved50` | TField |  |  |
| 28 | `SZ.IEC.RESERVED.49` | `SzIndustryEconomicCodes_Reserved49` | TField |  |  |
| 29 | `SZ.IEC.RESERVED.48` | `SzIndustryEconomicCodes_Reserved48` | TField |  |  |
| 30 | `SZ.IEC.RESERVED.47` | `SzIndustryEconomicCodes_Reserved47` | TField |  |  |
| 31 | `SZ.IEC.RESERVED.46` | `SzIndustryEconomicCodes_Reserved46` | TField |  |  |
| 32 | `SZ.IEC.RESERVED.45` | `SzIndustryEconomicCodes_Reserved45` | TField |  |  |
| 33 | `SZ.IEC.RESERVED.44` | `SzIndustryEconomicCodes_Reserved44` | TField |  |  |
| 34 | `SZ.IEC.RESERVED.43` | `SzIndustryEconomicCodes_Reserved43` | TField |  |  |
| 35 | `SZ.IEC.RESERVED.42` | `SzIndustryEconomicCodes_Reserved42` | TField |  |  |
| 36 | `SZ.IEC.RESERVED.41` | `SzIndustryEconomicCodes_Reserved41` | TField |  |  |
| 37 | `SZ.IEC.RESERVED.40` | `SzIndustryEconomicCodes_Reserved40` | TField |  |  |
| 38 | `SZ.IEC.RESERVED.39` | `SzIndustryEconomicCodes_Reserved39` | TField |  |  |
| 39 | `SZ.IEC.RESERVED.38` | `SzIndustryEconomicCodes_Reserved38` | TField |  |  |
| 40 | `SZ.IEC.RESERVED.37` | `SzIndustryEconomicCodes_Reserved37` | TField |  |  |
| 41 | `SZ.IEC.RESERVED.36` | `SzIndustryEconomicCodes_Reserved36` | TField |  |  |
| 42 | `SZ.IEC.RESERVED.35` | `SzIndustryEconomicCodes_Reserved35` | TField |  |  |
| 43 | `SZ.IEC.RESERVED.34` | `SzIndustryEconomicCodes_Reserved34` | TField |  |  |
| 44 | `SZ.IEC.RESERVED.33` | `SzIndustryEconomicCodes_Reserved33` | TField |  |  |
| 45 | `SZ.IEC.RESERVED.32` | `SzIndustryEconomicCodes_Reserved32` | TField |  |  |
| 46 | `SZ.IEC.RESERVED.31` | `SzIndustryEconomicCodes_Reserved31` | TField |  |  |
| 47 | `SZ.IEC.RESERVED.30` | `SzIndustryEconomicCodes_Reserved30` | TField |  |  |
| 48 | `SZ.IEC.RESERVED.29` | `SzIndustryEconomicCodes_Reserved29` | TField |  |  |
| 49 | `SZ.IEC.RESERVED.28` | `SzIndustryEconomicCodes_Reserved28` | TField |  |  |
| 50 | `SZ.IEC.RESERVED.27` | `SzIndustryEconomicCodes_Reserved27` | TField |  |  |
| 51 | `SZ.IEC.RESERVED.26` | `SzIndustryEconomicCodes_Reserved26` | TField |  |  |
| 52 | `SZ.IEC.RESERVED.25` | `SzIndustryEconomicCodes_Reserved25` | TField |  |  |
| 53 | `SZ.IEC.RESERVED.24` | `SzIndustryEconomicCodes_Reserved24` | TField |  |  |
| 54 | `SZ.IEC.RESERVED.23` | `SzIndustryEconomicCodes_Reserved23` | TField |  |  |
| 55 | `SZ.IEC.RESERVED.22` | `SzIndustryEconomicCodes_Reserved22` | TField |  |  |
| 56 | `SZ.IEC.RESERVED.21` | `SzIndustryEconomicCodes_Reserved21` | TField |  |  |
| 57 | `SZ.IEC.RESERVED.20` | `SzIndustryEconomicCodes_Reserved20` | TField |  |  |
| 58 | `SZ.IEC.RESERVED.19` | `SzIndustryEconomicCodes_Reserved19` | TField |  |  |
| 59 | `SZ.IEC.RESERVED.18` | `SzIndustryEconomicCodes_Reserved18` | TField |  |  |
| 60 | `SZ.IEC.RESERVED.17` | `SzIndustryEconomicCodes_Reserved17` | TField |  |  |
| 61 | `SZ.IEC.RESERVED.16` | `SzIndustryEconomicCodes_Reserved16` | TField |  |  |
| 62 | `SZ.IEC.RESERVED.15` | `SzIndustryEconomicCodes_Reserved15` | TField |  |  |
| 63 | `SZ.IEC.RESERVED.14` | `SzIndustryEconomicCodes_Reserved14` | TField |  |  |
| 64 | `SZ.IEC.RESERVED.13` | `SzIndustryEconomicCodes_Reserved13` | TField |  |  |
| 65 | `SZ.IEC.RESERVED.12` | `SzIndustryEconomicCodes_Reserved12` | TField |  |  |
| 66 | `SZ.IEC.RESERVED.11` | `SzIndustryEconomicCodes_Reserved11` | TField |  |  |
| 67 | `SZ.IEC.RESERVED.10` | `SzIndustryEconomicCodes_Reserved10` | TField |  |  |
| 68 | `SZ.IEC.RESERVED.09` | `SzIndustryEconomicCodes_Reserved09` | TField |  |  |
| 69 | `SZ.IEC.RESERVED.08` | `SzIndustryEconomicCodes_Reserved08` | TField |  |  |
| 70 | `SZ.IEC.RESERVED.07` | `SzIndustryEconomicCodes_Reserved07` | TField |  |  |
| 71 | `SZ.IEC.RESERVED.06` | `SzIndustryEconomicCodes_Reserved06` | TField |  |  |
| 72 | `SZ.IEC.RESERVED.05` | `SzIndustryEconomicCodes_Reserved05` | TField |  |  |
| 73 | `SZ.IEC.RESERVED.04` | `SzIndustryEconomicCodes_Reserved04` | TField |  |  |
| 74 | `SZ.IEC.RESERVED.03` | `SzIndustryEconomicCodes_Reserved03` | TField |  |  |
| 75 | `SZ.IEC.RESERVED.02` | `SzIndustryEconomicCodes_Reserved02` | TField |  |  |
| 76 | `SZ.IEC.RESERVED.01` | `SzIndustryEconomicCodes_Reserved01` | TField |  |  |
| 77 | `SZ.IEC.LOCAL.REF` | `SzIndustryEconomicCodes_LocalRef` |  |  |  |
| 78 | `SZ.IEC.OVERRIDE` | `SzIndustryEconomicCodes_Override` |  |  |  |
| 79 | `SZ.IEC.RECORD.STATUS` | `SzIndustryEconomicCodes_RecordStatus` | String |  |  |
| 80 | `SZ.IEC.CURR.NO` | `SzIndustryEconomicCodes_CurrNo` | String |  |  |
| 81 | `SZ.IEC.INPUTTER` | `SzIndustryEconomicCodes_Inputter` |  |  |  |
| 82 | `SZ.IEC.DATE.TIME` | `SzIndustryEconomicCodes_DateTime` |  |  |  |
| 83 | `SZ.IEC.AUTHORISER` | `SzIndustryEconomicCodes_Authoriser` | String |  |  |
| 84 | `SZ.IEC.CO.CODE` | `SzIndustryEconomicCodes_CoCode` | String |  |  |
| 85 | `SZ.IEC.DEPT.CODE` | `SzIndustryEconomicCodes_DeptCode` | String |  |  |
| 86 | `SZ.IEC.AUDITOR.CODE` | `SzIndustryEconomicCodes_AuditorCode` | String |  |  |
| 87 | `SZ.IEC.AUDIT.DATE.TIME` | `SzIndustryEconomicCodes_AuditDateTime` | String |  |  |
