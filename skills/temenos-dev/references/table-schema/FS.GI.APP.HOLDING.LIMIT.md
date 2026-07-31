# FS.GI.APP.HOLDING.LIMIT — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.HOLDING.LIMIT` in `FS_InvestmentRestrictions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.HOLDING.LIMIT.PARENT.REF.ID` | `FsGiAppHoldingLimit_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.HOLDING.LIMIT.ORA.ROWID` | `FsGiAppHoldingLimit_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.HOLDING.LIMIT.PARENT.TYPE` | `FsGiAppHoldingLimit_ParentType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.APP.HOLDING.LIMIT.PARENT.TYPE.ID` | `FsGiAppHoldingLimit_ParentTypeId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.APP.HOLDING.LIMIT.LEGAL.ENTITY.ID` | `FsGiAppHoldingLimit_LegalEntityId` | TField |  | Legal entity linked to the holding limit check. Multifonds DB Column is NTFC. |
| 6 | `FS.GI.APP.HOLDING.LIMIT.TA.FUND.ID` | `FsGiAppHoldingLimit_TaFundId` | TField |  | Fund linked to the holding limit check. Multifonds DB Column is NPTF. |
| 7 | `FS.GI.APP.HOLDING.LIMIT.SHARE.CLASS.CODE` | `FsGiAppHoldingLimit_ShareClassCode` | TField |  | Fund share class linked to the holding limit check. Multifonds DB Column is TPART. |
| 8 | `FS.GI.APP.HOLDING.LIMIT.LIMIT.CURRENCY` | `FsGiAppHoldingLimit_LimitCurrency` | TField |  | The currency (in 3 letter format eg: EUR) of the holding limit check. Multifonds DB Column is CMON_LIMIT. |
| 9 | `FS.GI.APP.HOLDING.LIMIT.MINIMUM.HOLDING.AMOUNT` | `FsGiAppHoldingLimit_MinimumHoldingAmount` | TField |  | The minimum holding amount to be maintained in the fund share class Multifonds DB Column is MIN_HOLD_AMOUNT. |
| 10 | `FS.GI.APP.HOLDING.LIMIT.MINIMUM.HOLDING.QUANTITY` | `FsGiAppHoldingLimit_MinimumHoldingQuantity` | TField |  | The minimum holding quantity to be maintained in the fund share Class Multifonds DB Column is MIN_HOLD_QUANTITY. |
| 11 | `FS.GI.APP.HOLDING.LIMIT.PERSON.TYPE` | `FsGiAppHoldingLimit_PersonType` | TField |  | The person type for which the holidng limit has to be defined Multifonds DB Column is TYPE_PERSON. |
| 12 | `FS.GI.APP.HOLDING.LIMIT.HOLDING.LIMIT.ID` | `FsGiAppHoldingLimit_HoldingLimitId` | TField |  | Unique internal holding limit identifier. Multifonds DB Column is INTERNAL_ID. |
| 13 | `FS.GI.APP.HOLDING.LIMIT.FUND.ID` | `FsGiAppHoldingLimit_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 14 | `FS.GI.APP.HOLDING.LIMIT.CLASS.CURRENCY` | `FsGiAppHoldingLimit_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 15 | `FS.GI.APP.HOLDING.LIMIT.RESERVED10` | `FsGiAppHoldingLimit_Reserved10` | TField |  |  |
| 16 | `FS.GI.APP.HOLDING.LIMIT.RESERVED9` | `FsGiAppHoldingLimit_Reserved9` | TField |  |  |
| 17 | `FS.GI.APP.HOLDING.LIMIT.RESERVED8` | `FsGiAppHoldingLimit_Reserved8` | TField |  |  |
| 18 | `FS.GI.APP.HOLDING.LIMIT.RESERVED7` | `FsGiAppHoldingLimit_Reserved7` | TField |  |  |
| 19 | `FS.GI.APP.HOLDING.LIMIT.RESERVED6` | `FsGiAppHoldingLimit_Reserved6` | TField |  |  |
| 20 | `FS.GI.APP.HOLDING.LIMIT.RESERVED5` | `FsGiAppHoldingLimit_Reserved5` | TField |  |  |
| 21 | `FS.GI.APP.HOLDING.LIMIT.RESERVED4` | `FsGiAppHoldingLimit_Reserved4` | TField |  |  |
| 22 | `FS.GI.APP.HOLDING.LIMIT.RESERVED3` | `FsGiAppHoldingLimit_Reserved3` | TField |  |  |
| 23 | `FS.GI.APP.HOLDING.LIMIT.RESERVED2` | `FsGiAppHoldingLimit_Reserved2` | TField |  |  |
| 24 | `FS.GI.APP.HOLDING.LIMIT.RESERVED1` | `FsGiAppHoldingLimit_Reserved1` | TField |  |  |
| 25 | `FS.GI.APP.HOLDING.LIMIT.LOCAL.REF` | `FsGiAppHoldingLimit_LocalRef` |  |  |  |
| 26 | `FS.GI.APP.HOLDING.LIMIT.OVERRIDE` | `FsGiAppHoldingLimit_Override` |  |  |  |
| 27 | `FS.GI.APP.HOLDING.LIMIT.RECORD.STATUS` | `FsGiAppHoldingLimit_RecordStatus` | String |  |  |
| 28 | `FS.GI.APP.HOLDING.LIMIT.CURR.NO` | `FsGiAppHoldingLimit_CurrNo` | String |  |  |
| 29 | `FS.GI.APP.HOLDING.LIMIT.INPUTTER` | `FsGiAppHoldingLimit_Inputter` |  |  |  |
| 30 | `FS.GI.APP.HOLDING.LIMIT.DATE.TIME` | `FsGiAppHoldingLimit_DateTime` |  |  |  |
| 31 | `FS.GI.APP.HOLDING.LIMIT.AUTHORISER` | `FsGiAppHoldingLimit_Authoriser` | String |  |  |
| 32 | `FS.GI.APP.HOLDING.LIMIT.CO.CODE` | `FsGiAppHoldingLimit_CoCode` | String |  |  |
| 33 | `FS.GI.APP.HOLDING.LIMIT.DEPT.CODE` | `FsGiAppHoldingLimit_DeptCode` | String |  |  |
| 34 | `FS.GI.APP.HOLDING.LIMIT.AUDITOR.CODE` | `FsGiAppHoldingLimit_AuditorCode` | String |  |  |
| 35 | `FS.GI.APP.HOLDING.LIMIT.AUDIT.DATE.TIME` | `FsGiAppHoldingLimit_AuditDateTime` | String |  |  |
