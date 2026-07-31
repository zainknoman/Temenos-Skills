# CAMB.POSTING.LIMIT.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.POSTING.LIMIT.PARAM` in `CABASE_UserSecurity.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.PST.DESCRIPTION` | `CambPostingLimitParam_Description` | TField |  | To define the description for parameter table. |
| 2 | `CAMB.PST.LENDING.APPLICATIONS` | `CambPostingLimitParam_LendingApplications` |  |  |  |
| 3 | `CAMB.PST.CATEG.OPERAND` | `CambPostingLimitParam_CategOperand` |  |  |  |
| 4 | `CAMB.PST.FROM` | `CambPostingLimitParam_From` |  |  |  |
| 5 | `CAMB.PST.TO` | `CambPostingLimitParam_To` |  |  |  |
| 6 | `CAMB.PST.ROLE` | `CambPostingLimitParam_Role` |  |  |  |
| 7 | `CAMB.PST.MAX.LENDING.LIMIT` | `CambPostingLimitParam_MaxLendingLimit` |  |  |  |
| 8 | `CAMB.PST.MAX.GL.LIMIT` | `CambPostingLimitParam_MaxGlLimit` |  |  |  |
| 9 | `CAMB.PST.MAX.OTHERS.LIMIT` | `CambPostingLimitParam_MaxOthersLimit` |  |  |  |
| 10 | `CAMB.PST.LEND.OVR.CLASS` | `CambPostingLimitParam_LendOvrClass` | TField |  |  |
| 11 | `CAMB.PST.OTHERS.OVR.CLASS` | `CambPostingLimitParam_OthersOvrClass` | TField |  |  |
| 12 | `CAMB.PST.OTHERS.GL.CLASS` | `CambPostingLimitParam_OthersGlClass` | TField |  |  |
| 13 | `CAMB.PST.LOCAL.REF` | `CambPostingLimitParam_LocalRef` |  |  |  |
| 14 | `CAMB.PST.OVERRIDE` | `CambPostingLimitParam_Override` |  |  |  |
| 15 | `CAMB.PST.CLASS.DETAILS.LENDING` | `CambPostingLimitParam_ClassDetailsLending` | TField |  |  |
| 16 | `CAMB.PST.CLASS.DETAILS.OTHERS` | `CambPostingLimitParam_ClassDetailsOthers` | TField |  |  |
| 17 | `CAMB.PST.CLASS.DETAILS.GL` | `CambPostingLimitParam_ClassDetailsGl` | TField |  | This field is used to define the override class for GL Account transactions.Linked to OVERRIDE.CLASS.DETAILS for Non-lending GL , The data value are defined in amount range limit for userE.g.Classification = I100Comparison = EQData = 25000 |
| 18 | `CAMB.PST.APPLN` | `CambPostingLimitParam_Appln` |  |  |  |
| 19 | `CAMB.PST.ACCT.FIELD` | `CambPostingLimitParam_AcctField` |  |  |  |
| 20 | `CAMB.PST.AMT.FIELD` | `CambPostingLimitParam_AmtField` |  |  |  |
| 21 | `CAMB.PST.RESERVED5` | `CambPostingLimitParam_Reserved5` |  |  |  |
| 22 | `CAMB.PST.RESERVED4` | `CambPostingLimitParam_Reserved4` |  |  |  |
| 23 | `CAMB.PST.RESERVED3` | `CambPostingLimitParam_Reserved3` |  |  |  |
| 24 | `CAMB.PST.RESERVED2` | `CambPostingLimitParam_Reserved2` |  |  |  |
| 25 | `CAMB.PST.RESERVED1` | `CambPostingLimitParam_Reserved1` |  |  |  |
| 26 | `CAMB.PST.RESERVED.5` | `CambPostingLimitParam_Reserved5` |  |  |  |
| 27 | `CAMB.PST.RESERVED.4` | `CambPostingLimitParam_Reserved4` |  |  |  |
| 28 | `CAMB.PST.RESERVED.3` | `CambPostingLimitParam_Reserved3` |  |  |  |
| 29 | `CAMB.PST.RESERVED.2` | `CambPostingLimitParam_Reserved2` |  |  |  |
| 30 | `CAMB.PST.RESERVED.1` | `CambPostingLimitParam_Reserved1` |  |  |  |
| 31 | `CAMB.PST.RECORD.STATUS` | `CambPostingLimitParam_RecordStatus` | String |  |  |
| 32 | `CAMB.PST.CURR.NO` | `CambPostingLimitParam_CurrNo` | String |  |  |
| 33 | `CAMB.PST.INPUTTER` | `CambPostingLimitParam_Inputter` |  |  |  |
| 34 | `CAMB.PST.DATE.TIME` | `CambPostingLimitParam_DateTime` |  |  |  |
| 35 | `CAMB.PST.AUTHORISER` | `CambPostingLimitParam_Authoriser` | String |  |  |
| 36 | `CAMB.PST.CO.CODE` | `CambPostingLimitParam_CoCode` | String |  |  |
| 37 | `CAMB.PST.DEPT.CODE` | `CambPostingLimitParam_DeptCode` | String |  |  |
| 38 | `CAMB.PST.AUDITOR.CODE` | `CambPostingLimitParam_AuditorCode` | String |  |  |
| 39 | `CAMB.PST.AUDIT.DATE.TIME` | `CambPostingLimitParam_AuditDateTime` | String |  |  |
