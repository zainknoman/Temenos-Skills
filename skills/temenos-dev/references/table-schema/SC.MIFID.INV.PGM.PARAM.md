# SC.MIFID.INV.PGM.PARAM — Table Schema

> Source: `INSERTS/I_F.SC.MIFID.INV.PGM.PARAM` in `SC_Mifid.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.MIFIDINV.SCORE.ID` | `ScMifidInvPgmParam_ScoreId` |  |  |  |
| 2 | `SC.MIFIDINV.MIN.SCORE.POINTS` | `ScMifidInvPgmParam_MinScorePoints` |  |  |  |
| 3 | `SC.MIFIDINV.MAX.SCORE.POINTS` | `ScMifidInvPgmParam_MaxScorePoints` |  |  |  |
| 4 | `SC.MIFIDINV.APP.FIELD` | `ScMifidInvPgmParam_AppField` |  |  |  |
| 5 | `SC.MIFIDINV.OPERAND` | `ScMifidInvPgmParam_Operand` |  |  |  |
| 6 | `SC.MIFIDINV.VALUE` | `ScMifidInvPgmParam_Value` |  |  |  |
| 7 | `SC.MIFIDINV.POINTS` | `ScMifidInvPgmParam_Points` |  |  |  |
| 8 | `SC.MIFIDINV.POINTS.OPERAND` | `ScMifidInvPgmParam_PointsOperand` |  |  |  |
| 9 | `SC.MIFIDINV.ELIGIBLE.POINTS` | `ScMifidInvPgmParam_EligiblePoints` |  |  |  |
| 10 | `SC.MIFIDINV.ELIGIBLE.INVEST.PROGRAM` | `ScMifidInvPgmParam_EligibleInvestProgram` |  |  |  |
| 11 | `SC.MIFIDINV.DEFAULT.INVEST.PROGRAM` | `ScMifidInvPgmParam_DefaultInvestProgram` | TField |  | This field specifies investment program to be defaulted in SEC.ACC.MASTER if system fails to determine eligible investment program Validation Rules: valid record from INVESTMENT.PROGRAM |
| 12 | `SC.MIFIDINV.RESERVED1` | `ScMifidInvPgmParam_Reserved1` | TField |  |  |
| 13 | `SC.MIFIDINV.RESERVED2` | `ScMifidInvPgmParam_Reserved2` | TField |  |  |
| 14 | `SC.MIFIDINV.RESERVED3` | `ScMifidInvPgmParam_Reserved3` | TField |  |  |
| 15 | `SC.MIFIDINV.RESERVED4` | `ScMifidInvPgmParam_Reserved4` | TField |  |  |
| 16 | `SC.MIFIDINV.RESERVED5` | `ScMifidInvPgmParam_Reserved5` | TField |  |  |
| 17 | `SC.MIFIDINV.RESERVED6` | `ScMifidInvPgmParam_Reserved6` | TField |  |  |
| 18 | `SC.MIFIDINV.RESERVED7` | `ScMifidInvPgmParam_Reserved7` | TField |  |  |
| 19 | `SC.MIFIDINV.RESERVED8` | `ScMifidInvPgmParam_Reserved8` | TField |  |  |
| 20 | `SC.MIFIDINV.RESERVED9` | `ScMifidInvPgmParam_Reserved9` | TField |  |  |
| 21 | `SC.MIFIDINV.RESERVED10` | `ScMifidInvPgmParam_Reserved10` | TField |  |  |
| 22 | `SC.MIFIDINV.RESERVED11` | `ScMifidInvPgmParam_Reserved11` | TField |  |  |
| 23 | `SC.MIFIDINV.RESERVED12` | `ScMifidInvPgmParam_Reserved12` | TField |  |  |
| 24 | `SC.MIFIDINV.RESERVED13` | `ScMifidInvPgmParam_Reserved13` | TField |  |  |
| 25 | `SC.MIFIDINV.RESERVED14` | `ScMifidInvPgmParam_Reserved14` | TField |  |  |
| 26 | `SC.MIFIDINV.RESERVED15` | `ScMifidInvPgmParam_Reserved15` | TField |  |  |
| 27 | `SC.MIFIDINV.RESERVED16` | `ScMifidInvPgmParam_Reserved16` | TField |  |  |
| 28 | `SC.MIFIDINV.RESERVED17` | `ScMifidInvPgmParam_Reserved17` | TField |  |  |
| 29 | `SC.MIFIDINV.RESERVED18` | `ScMifidInvPgmParam_Reserved18` | TField |  |  |
| 30 | `SC.MIFIDINV.RESERVED19` | `ScMifidInvPgmParam_Reserved19` | TField |  |  |
| 31 | `SC.MIFIDINV.RESERVED20` | `ScMifidInvPgmParam_Reserved20` | TField |  |  |
| 32 | `SC.MIFIDINV.LOCAL.REF` | `ScMifidInvPgmParam_LocalRef` |  |  |  |
| 33 | `SC.MIFIDINV.OVERRIDE` | `ScMifidInvPgmParam_Override` |  |  |  |
| 34 | `SC.MIFIDINV.RECORD.STATUS` | `ScMifidInvPgmParam_RecordStatus` | String |  |  |
| 35 | `SC.MIFIDINV.CURR.NO` | `ScMifidInvPgmParam_CurrNo` | String |  |  |
| 36 | `SC.MIFIDINV.INPUTTER` | `ScMifidInvPgmParam_Inputter` |  |  |  |
| 37 | `SC.MIFIDINV.DATE.TIME` | `ScMifidInvPgmParam_DateTime` |  |  |  |
| 38 | `SC.MIFIDINV.AUTHORISER` | `ScMifidInvPgmParam_Authoriser` | String |  |  |
| 39 | `SC.MIFIDINV.CO.CODE` | `ScMifidInvPgmParam_CoCode` | String |  |  |
| 40 | `SC.MIFIDINV.DEPT.CODE` | `ScMifidInvPgmParam_DeptCode` | String |  |  |
| 41 | `SC.MIFIDINV.AUDITOR.CODE` | `ScMifidInvPgmParam_AuditorCode` | String |  |  |
| 42 | `SC.MIFIDINV.AUDIT.DATE.TIME` | `ScMifidInvPgmParam_AuditDateTime` | String |  |  |
