# CG.PORTFOLIO.CALC — Table Schema

> Source: `INSERTS/I_F.CG.PORTFOLIO.CALC` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.CPC.SELECTION.ID` | `CgPortfolioCalc_SelectionId` |  |  |  |
| 2 | `CG.CPC.SEC.CCY` | `CgPortfolioCalc_SecCcy` |  |  |  |
| 3 | `CG.CPC.EXCH.RATE.LCY` | `CgPortfolioCalc_ExchRateLcy` |  |  |  |
| 4 | `CG.CPC.STATUS` | `CgPortfolioCalc_Status` | TField |  | Field shows that the record has been processed or not. Possible Values: PROCESSED, ACTIVATED Validation Rules: This is a NOINPUT, system generated field. Field value shows ACTIVATED once we authorise the CG.PORTFOLIO.CALC record by mentioning the security currency for which recalculation needs to be performed Field value shows PROCESSED after the recalculation is performed. |
| 5 | `CG.CPC.NO.OF.REC.SELCTD` | `CgPortfolioCalc_NoOfRecSelctd` | TField |  | This field will hold number of records that got selected for recalculation. Updated by the Service SC.RECALC.EXCH.CG.PORT after recalculation Validation Rules: This is a NOINPUT, system generated field. |
| 6 | `CG.CPC.RESERVED1` | `CgPortfolioCalc_Reserved1` | TField |  |  |
| 7 | `CG.CPC.RESERVED2` | `CgPortfolioCalc_Reserved2` | TField |  |  |
| 8 | `CG.CPC.RESERVED3` | `CgPortfolioCalc_Reserved3` | TField |  |  |
| 9 | `CG.CPC.RESERVED4` | `CgPortfolioCalc_Reserved4` | TField |  |  |
| 10 | `CG.CPC.RESERVED5` | `CgPortfolioCalc_Reserved5` | TField |  |  |
| 11 | `CG.CPC.RESERVED6` | `CgPortfolioCalc_Reserved6` | TField |  |  |
| 12 | `CG.CPC.RESERVED7` | `CgPortfolioCalc_Reserved7` | TField |  |  |
| 13 | `CG.CPC.RESERVED8` | `CgPortfolioCalc_Reserved8` | TField |  |  |
| 14 | `CG.CPC.RESERVED9` | `CgPortfolioCalc_Reserved9` | TField |  |  |
| 15 | `CG.CPC.RESERVED10` | `CgPortfolioCalc_Reserved10` | TField |  |  |
| 16 | `CG.CPC.RESERVED11` | `CgPortfolioCalc_Reserved11` | TField |  |  |
| 17 | `CG.CPC.RESERVED12` | `CgPortfolioCalc_Reserved12` | TField |  |  |
| 18 | `CG.CPC.RESERVED13` | `CgPortfolioCalc_Reserved13` | TField |  |  |
| 19 | `CG.CPC.RESERVED14` | `CgPortfolioCalc_Reserved14` | TField |  |  |
| 20 | `CG.CPC.RESERVED15` | `CgPortfolioCalc_Reserved15` | TField |  |  |
| 21 | `CG.CPC.RESERVED16` | `CgPortfolioCalc_Reserved16` | TField |  |  |
| 22 | `CG.CPC.RESERVED17` | `CgPortfolioCalc_Reserved17` | TField |  |  |
| 23 | `CG.CPC.RESERVED18` | `CgPortfolioCalc_Reserved18` | TField |  |  |
| 24 | `CG.CPC.RESERVED19` | `CgPortfolioCalc_Reserved19` | TField |  |  |
| 25 | `CG.CPC.RESERVED20` | `CgPortfolioCalc_Reserved20` | TField |  |  |
| 26 | `CG.CPC.LOCAL.REF` | `CgPortfolioCalc_LocalRef` |  |  |  |
| 27 | `CG.CPC.OVERRIDE` | `CgPortfolioCalc_Override` |  |  |  |
| 28 | `CG.CPC.RECORD.STATUS` | `CgPortfolioCalc_RecordStatus` | String |  |  |
| 29 | `CG.CPC.CURR.NO` | `CgPortfolioCalc_CurrNo` | String |  |  |
| 30 | `CG.CPC.INPUTTER` | `CgPortfolioCalc_Inputter` |  |  |  |
| 31 | `CG.CPC.DATE.TIME` | `CgPortfolioCalc_DateTime` |  |  |  |
| 32 | `CG.CPC.AUTHORISER` | `CgPortfolioCalc_Authoriser` | String |  |  |
| 33 | `CG.CPC.CO.CODE` | `CgPortfolioCalc_CoCode` | String |  |  |
| 34 | `CG.CPC.DEPT.CODE` | `CgPortfolioCalc_DeptCode` | String |  |  |
| 35 | `CG.CPC.AUDITOR.CODE` | `CgPortfolioCalc_AuditorCode` | String |  |  |
| 36 | `CG.CPC.AUDIT.DATE.TIME` | `CgPortfolioCalc_AuditDateTime` | String |  |  |
