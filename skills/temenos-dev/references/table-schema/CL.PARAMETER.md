# CL.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CL.PARAMETER` in `CL_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.PARAM.PTP.CODE` | `ClParameter_PtpCode` | TField |  |  |
| 2 | `CL.PARAM.KPTP.CODE` | `ClParameter_KptpCode` | TField |  |  |
| 3 | `CL.PARAM.BPTP.CODE` | `ClParameter_BptpCode` | TField |  |  |
| 4 | `CL.PARAM.PPTP.CODE` | `ClParameter_PptpCode` | TField |  |  |
| 5 | `CL.PARAM.PTP.PERCENTAGE` | `ClParameter_PtpPercentage` | TField |  |  |
| 6 | `CL.PARAM.PTP.GRACE.PRD` | `ClParameter_PtpGracePrd` | TField |  |  |
| 7 | `CL.PARAM.PPTPB.CODE` | `ClParameter_PptpbCode` | TField |  |  |
| 8 | `CL.PARAM.SPAY.CODE` | `ClParameter_SpayCode` | TField |  |  |
| 9 | `CL.PARAM.APAY.CODE` | `ClParameter_ApayCode` | TField |  |  |
| 10 | `CL.PARAM.ASAL.CODE` | `ClParameter_AsalCode` | TField |  |  |
| 11 | `CL.PARAM.IPTP.CODE` | `ClParameter_IptpCode` | TField |  |  |
| 12 | `CL.PARAM.RPTP.CODE` | `ClParameter_RptpCode` | TField |  |  |
| 13 | `CL.PARAM.CATEGORY.FROM` | `ClParameter_CategoryFrom` |  |  |  |
| 14 | `CL.PARAM.CATEGORY.TO` | `ClParameter_CategoryTo` |  |  |  |
| 15 | `CL.PARAM.COMPANY` | `ClParameter_Company` |  |  |  |
| 16 | `CL.PARAM.INACTIVES.NOTES` | `ClParameter_InactivesNotes` | TField |  |  |
| 17 | `CL.PARAM.HIST.NOTES` | `ClParameter_HistNotes` | TField |  |  |
| 18 | `CL.PARAM.AA.OD.BALANCE` | `ClParameter_AaOdBalance` | TField |  |  |
| 19 | `CL.PARAM.AA.OS.BALANCE` | `ClParameter_AaOsBalance` | TField |  |  |
| 20 | `CL.PARAM.LOCAL.REF` | `ClParameter_LocalRef` |  |  |  |
| 21 | `CL.PARAM.RESERVED.11` | `ClParameter_Reserved11` |  |  |  |
| 22 | `CL.PARAM.RESERVED.10` | `ClParameter_Reserved10` | TField |  |  |
| 23 | `CL.PARAM.RESERVED.9` | `ClParameter_Reserved9` | TField |  |  |
| 24 | `CL.PARAM.RESERVED.8` | `ClParameter_Reserved8` | TField |  |  |
| 25 | `CL.PARAM.RESERVED.7` | `ClParameter_Reserved7` | TField |  |  |
| 26 | `CL.PARAM.RESERVED.6` | `ClParameter_Reserved6` | TField |  |  |
| 27 | `CL.PARAM.RESERVED.5` | `ClParameter_Reserved5` | TField |  |  |
| 28 | `CL.PARAM.RESERVED.4` | `ClParameter_Reserved4` | TField |  |  |
| 29 | `CL.PARAM.RESERVED.3` | `ClParameter_Reserved3` | TField |  |  |
| 30 | `CL.PARAM.RESERVED.2` | `ClParameter_Reserved2` | TField |  |  |
| 31 | `CL.PARAM.RESERVED.1` | `ClParameter_Reserved1` | TField |  |  |
| 32 | `CL.PARAM.RECORD.STATUS` | `ClParameter_RecordStatus` | String |  |  |
| 33 | `CL.PARAM.CURR.NO` | `ClParameter_CurrNo` | String |  |  |
| 34 | `CL.PARAM.INPUTTER` | `ClParameter_Inputter` |  |  |  |
| 35 | `CL.PARAM.DATE.TIME` | `ClParameter_DateTime` |  |  |  |
| 36 | `CL.PARAM.AUTHORISER` | `ClParameter_Authoriser` | String |  |  |
| 37 | `CL.PARAM.CO.CODE` | `ClParameter_CoCode` | String |  |  |
| 38 | `CL.PARAM.DEPT.CODE` | `ClParameter_DeptCode` | String |  |  |
| 39 | `CL.PARAM.AUDITOR.CODE` | `ClParameter_AuditorCode` | String |  |  |
| 40 | `CL.PARAM.AUDIT.DATE.TIME` | `ClParameter_AuditDateTime` | String |  |  |
| 41 | `CL.PARAM.CAT.OVD.BAL.TYPE` | `ClParameter_CatOvdBalType` |  |  |  |
| 42 | `CL.PARAM.CAT.OS.BAL.TYPE` | `ClParameter_CatOsBalType` |  |  |  |
| 43 | `CL.PARAM.CONVERT.RATE` | `ClParameter_ConvertRate` | TField |  |  |
