# CG.PORTFOLIO.BUILD — Table Schema

> Source: `INSERTS/I_F.CG.PORTFOLIO.BUILD` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CGPRB.GRP.NAME` | `CgPortfolioBuild_GrpName` |  |  |  |
| 2 | `CGPRB.SECURITY.CCY` | `CgPortfolioBuild_SecurityCcy` |  |  |  |
| 3 | `CGPRB.LOSS.BF.YEAR` | `CgPortfolioBuild_LossBfYear` |  |  |  |
| 4 | `CGPRB.LT.LOSS.BF.AMT` | `CgPortfolioBuild_LtLossBfAmt` |  |  |  |
| 5 | `CGPRB.ST.LOSS.BF.AMT` | `CgPortfolioBuild_StLossBfAmt` |  |  |  |
| 6 | `CGPRB.STATUS` | `CgPortfolioBuild_Status` | TField |  | Field is to identify processing of this record by service : CG.PORTFOLIO.BUILD . Update to this field is as below : ACTIVATED - Record is ready to be picked by service : CG.PORTFOLIO.BUILD PROCESSED - Record is processed by service : CG.PORTFOLIO.BUILD Validation Rules : NOINPUT Field |
| 7 | `CGPRB.SELECTED.CNT` | `CgPortfolioBuild_SelectedCnt` | TField |  | Total No of CG.PORTFOLIO records that are updated through service : CG.PORTFOLIO.BUILD |
| 8 | `CGPRB.LAST.RUN` | `CgPortfolioBuild_LastRun` | TField |  | Latest Processing Date and Time of this record through service : CG.PORTFOLIO.BUILD |
| 9 | `CGPRB.RESERVED.30` | `CgPortfolioBuild_Reserved30` |  |  |  |
| 10 | `CGPRB.RESERVED.29` | `CgPortfolioBuild_Reserved29` |  |  |  |
| 11 | `CGPRB.RESERVED.28` | `CgPortfolioBuild_Reserved28` |  |  |  |
| 12 | `CGPRB.RESERVED.27` | `CgPortfolioBuild_Reserved27` |  |  |  |
| 13 | `CGPRB.RESERVED.26` | `CgPortfolioBuild_Reserved26` |  |  |  |
| 14 | `CGPRB.RESERVED.25` | `CgPortfolioBuild_Reserved25` |  |  |  |
| 15 | `CGPRB.RESERVED.24` | `CgPortfolioBuild_Reserved24` |  |  |  |
| 16 | `CGPRB.RESERVED.23` | `CgPortfolioBuild_Reserved23` |  |  |  |
| 17 | `CGPRB.RESERVED.22` | `CgPortfolioBuild_Reserved22` |  |  |  |
| 18 | `CGPRB.RESERVED.21` | `CgPortfolioBuild_Reserved21` |  |  |  |
| 19 | `CGPRB.RESERVED.20` | `CgPortfolioBuild_Reserved20` |  |  |  |
| 20 | `CGPRB.RESERVED.19` | `CgPortfolioBuild_Reserved19` |  |  |  |
| 21 | `CGPRB.RESERVED.18` | `CgPortfolioBuild_Reserved18` |  |  |  |
| 22 | `CGPRB.RESERVED.17` | `CgPortfolioBuild_Reserved17` |  |  |  |
| 23 | `CGPRB.RESERVED.16` | `CgPortfolioBuild_Reserved16` |  |  |  |
| 24 | `CGPRB.RESERVED.15` | `CgPortfolioBuild_Reserved15` |  |  |  |
| 25 | `CGPRB.RESERVED.14` | `CgPortfolioBuild_Reserved14` |  |  |  |
| 26 | `CGPRB.RESERVED.13` | `CgPortfolioBuild_Reserved13` |  |  |  |
| 27 | `CGPRB.RESERVED.12` | `CgPortfolioBuild_Reserved12` |  |  |  |
| 28 | `CGPRB.RESERVED.11` | `CgPortfolioBuild_Reserved11` |  |  |  |
| 29 | `CGPRB.RESERVED.10` | `CgPortfolioBuild_Reserved10` | TField |  |  |
| 30 | `CGPRB.RESERVED.9` | `CgPortfolioBuild_Reserved9` | TField |  |  |
| 31 | `CGPRB.RESERVED.8` | `CgPortfolioBuild_Reserved8` | TField |  |  |
| 32 | `CGPRB.RESERVED.7` | `CgPortfolioBuild_Reserved7` | TField |  |  |
| 33 | `CGPRB.RESERVED.6` | `CgPortfolioBuild_Reserved6` | TField |  |  |
| 34 | `CGPRB.RESERVED.5` | `CgPortfolioBuild_Reserved5` | TField |  |  |
| 35 | `CGPRB.RESERVED.4` | `CgPortfolioBuild_Reserved4` | TField |  |  |
| 36 | `CGPRB.RESERVED.3` | `CgPortfolioBuild_Reserved3` | TField |  |  |
| 37 | `CGPRB.RESERVED.2` | `CgPortfolioBuild_Reserved2` | TField |  |  |
| 38 | `CGPRB.RESERVED.1` | `CgPortfolioBuild_Reserved1` | TField |  |  |
| 39 | `CGPRB.LOCAL.REF` | `CgPortfolioBuild_LocalRef` |  |  |  |
| 40 | `CGPRB.OVERRIDE` | `CgPortfolioBuild_Override` |  |  |  |
| 41 | `CGPRB.RECORD.STATUS` | `CgPortfolioBuild_RecordStatus` | String |  |  |
| 42 | `CGPRB.CURR.NO` | `CgPortfolioBuild_CurrNo` | String |  |  |
| 43 | `CGPRB.INPUTTER` | `CgPortfolioBuild_Inputter` |  |  |  |
| 44 | `CGPRB.DATE.TIME` | `CgPortfolioBuild_DateTime` |  |  |  |
| 45 | `CGPRB.AUTHORISER` | `CgPortfolioBuild_Authoriser` | String |  |  |
| 46 | `CGPRB.CO.CODE` | `CgPortfolioBuild_CoCode` | String |  |  |
| 47 | `CGPRB.DEPT.CODE` | `CgPortfolioBuild_DeptCode` | String |  |  |
| 48 | `CGPRB.AUDITOR.CODE` | `CgPortfolioBuild_AuditorCode` | String |  |  |
| 49 | `CGPRB.AUDIT.DATE.TIME` | `CgPortfolioBuild_AuditDateTime` | String |  |  |
