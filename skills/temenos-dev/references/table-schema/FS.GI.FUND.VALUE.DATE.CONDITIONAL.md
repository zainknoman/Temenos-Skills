# FS.GI.FUND.VALUE.DATE.CONDITIONAL — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.VALUE.DATE.CONDITIONAL` in `FS_FundDealing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.PARENT.REF.ID` | `FsGiFundValueDateConditional_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.ORA.ROWID` | `FsGiFundValueDateConditional_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.LEVEL.CODE` | `FsGiFundValueDateConditional_LevelCode` | TField |  | Level at which the holiday is defined (MF Fund, TA Fund, etc.). For examle: 0003 - TFC, 0004 a MF Fund ID, 0006 a TA Fund ID. Multifonds DB Column is LEVEL_CODE. |
| 4 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.LEVEL.CODE.ID` | `FsGiFundValueDateConditional_LevelCodeId` | TField |  | ID of the level code. Multifonds DB Column is CODE_ID. |
| 5 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.TA.FUND.ID` | `FsGiFundValueDateConditional_TaFundId` | TField |  | TA Fund ID. Multifonds DB Column is NPTF. |
| 6 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.SHARE.CLASS.CODE` | `FsGiFundValueDateConditional_ShareClassCode` | TField |  | Share Class ID if the value date conditioning is share class specific. Multifonds DB Column is TPART. |
| 7 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.OPERATION.CODE` | `FsGiFundValueDateConditional_OperationCode` | TField |  | Operation code for which value date setup is applicable. Multifonds DB Column is COPERATION. |
| 8 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.COND.VD.HOLIDAY.FUND.COUNTRY` | `FsGiFundValueDateConditional_CondVdHolidayFundCountry` | TField |  | Holiday in the country of the MF Fund. Multifonds DB Column is HOL_CON_MF. |
| 9 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.COND.VD.HOLIDAY.PAY.CURRENCY` | `FsGiFundValueDateConditional_CondVdHolidayPayCurrency` | TField |  | Holiday in payment currency. Multifonds DB Column is HOL_PAY_CCY. |
| 10 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.COND.VD.HOLIDAY.QUOT.CURRENCY` | `FsGiFundValueDateConditional_CondVdHolidayQuotCurrency` | TField |  | Holiday in quotation currency(TA Fund). Multifonds DB Column is HOL_QTN_CCY. |
| 11 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.COND.VD.HOLIDAY.REF.CURRENCY` | `FsGiFundValueDateConditional_CondVdHolidayRefCurrency` | TField |  | Holiday in reference currency(MF Fund). Multifonds DB Column is HOL_REF_CCY. |
| 12 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.COND.VD.CLOSED.WEEKENDS` | `FsGiFundValueDateConditional_CondVdClosedWeekends` | TField |  | Flag to indicate closed week ends. Multifonds DB Column is WEEK_END_CLOSE. |
| 13 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.REGISTER.VALUE.DATE.CODE` | `FsGiFundValueDateConditional_RegisterValueDateCode` | TField |  | Register Value Date Code. Multifonds DB Column is REG_VALDT_CODE. |
| 14 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.GROUP.ID` | `FsGiFundValueDateConditional_GroupId` | TField |  | Fund group ID. Multifonds DB Column is GRP_ID. |
| 15 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.TEMPLATE` | `FsGiFundValueDateConditional_Template` | TField |  | Template ID. Multifonds DB Column is TEMPLATE_ID. |
| 16 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.VALUE.DATE.FLAG` | `FsGiFundValueDateConditional_ValueDateFlag` | TField |  | Flag to indicate value date defined. Multifonds DB Column is FLG_VALUE_DATE. |
| 17 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.FUND.ID` | `FsGiFundValueDateConditional_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 18 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.CLASS.CURRENCY` | `FsGiFundValueDateConditional_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 19 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.RESERVED10` | `FsGiFundValueDateConditional_Reserved10` | TField |  |  |
| 20 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.RESERVED9` | `FsGiFundValueDateConditional_Reserved9` | TField |  |  |
| 21 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.RESERVED8` | `FsGiFundValueDateConditional_Reserved8` | TField |  |  |
| 22 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.RESERVED7` | `FsGiFundValueDateConditional_Reserved7` | TField |  |  |
| 23 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.RESERVED6` | `FsGiFundValueDateConditional_Reserved6` | TField |  |  |
| 24 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.RESERVED5` | `FsGiFundValueDateConditional_Reserved5` | TField |  |  |
| 25 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.RESERVED4` | `FsGiFundValueDateConditional_Reserved4` | TField |  |  |
| 26 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.RESERVED3` | `FsGiFundValueDateConditional_Reserved3` | TField |  |  |
| 27 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.RESERVED2` | `FsGiFundValueDateConditional_Reserved2` | TField |  |  |
| 28 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.RESERVED1` | `FsGiFundValueDateConditional_Reserved1` | TField |  |  |
| 29 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.LOCAL.REF` | `FsGiFundValueDateConditional_LocalRef` |  |  |  |
| 30 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.OVERRIDE` | `FsGiFundValueDateConditional_Override` |  |  |  |
| 31 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.RECORD.STATUS` | `FsGiFundValueDateConditional_RecordStatus` | String |  |  |
| 32 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.CURR.NO` | `FsGiFundValueDateConditional_CurrNo` | String |  |  |
| 33 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.INPUTTER` | `FsGiFundValueDateConditional_Inputter` |  |  |  |
| 34 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.DATE.TIME` | `FsGiFundValueDateConditional_DateTime` |  |  |  |
| 35 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.AUTHORISER` | `FsGiFundValueDateConditional_Authoriser` | String |  |  |
| 36 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.CO.CODE` | `FsGiFundValueDateConditional_CoCode` | String |  |  |
| 37 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.DEPT.CODE` | `FsGiFundValueDateConditional_DeptCode` | String |  |  |
| 38 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.AUDITOR.CODE` | `FsGiFundValueDateConditional_AuditorCode` | String |  |  |
| 39 | `FS.GI.FUND.VALUE.DATE.CONDITIONAL.AUDIT.DATE.TIME` | `FsGiFundValueDateConditional_AuditDateTime` | String |  |  |
