# FS.GI.APP.FX.DEALING.CCY — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.FX.DEALING.CCY` in `FS_Dealing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.FX.DEALING.CCY.PARENT.REF.ID` | `FsGiAppFxDealingCcy_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.FX.DEALING.CCY.ORA.ROWID` | `FsGiAppFxDealingCcy_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.FX.DEALING.CCY.PARENT.ID.TYPE` | `FsGiAppFxDealingCcy_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.APP.FX.DEALING.CCY.PARENT.ID` | `FsGiAppFxDealingCcy_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.APP.FX.DEALING.CCY.SHARE.CLASS.CODE` | `FsGiAppFxDealingCcy_ShareClassCode` | TField |  | Fund share class code linked to dealing currency paramaterisation. Multifonds DB Column is TPART. |
| 6 | `FS.GI.APP.FX.DEALING.CCY.OPERATION.CODE` | `FsGiAppFxDealingCcy_OperationCode` | TField |  | Operation code allowed for the dealing currency. Multifonds DB Column is COPERATION. |
| 7 | `FS.GI.APP.FX.DEALING.CCY.PAYMENT.CURRENCY` | `FsGiAppFxDealingCcy_PaymentCurrency` | TField |  | Dealing currency (in 3 letter format &apos;USD&apos;) for the type of operation in the fund share class. Multifonds DB Column is CMON. |
| 8 | `FS.GI.APP.FX.DEALING.CCY.FUND.ID` | `FsGiAppFxDealingCcy_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 9 | `FS.GI.APP.FX.DEALING.CCY.CLASS.CURRENCY` | `FsGiAppFxDealingCcy_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 10 | `FS.GI.APP.FX.DEALING.CCY.RESERVED10` | `FsGiAppFxDealingCcy_Reserved10` | TField |  |  |
| 11 | `FS.GI.APP.FX.DEALING.CCY.RESERVED9` | `FsGiAppFxDealingCcy_Reserved9` | TField |  |  |
| 12 | `FS.GI.APP.FX.DEALING.CCY.RESERVED8` | `FsGiAppFxDealingCcy_Reserved8` | TField |  |  |
| 13 | `FS.GI.APP.FX.DEALING.CCY.RESERVED7` | `FsGiAppFxDealingCcy_Reserved7` | TField |  |  |
| 14 | `FS.GI.APP.FX.DEALING.CCY.RESERVED6` | `FsGiAppFxDealingCcy_Reserved6` | TField |  |  |
| 15 | `FS.GI.APP.FX.DEALING.CCY.RESERVED5` | `FsGiAppFxDealingCcy_Reserved5` | TField |  |  |
| 16 | `FS.GI.APP.FX.DEALING.CCY.RESERVED4` | `FsGiAppFxDealingCcy_Reserved4` | TField |  |  |
| 17 | `FS.GI.APP.FX.DEALING.CCY.RESERVED3` | `FsGiAppFxDealingCcy_Reserved3` | TField |  |  |
| 18 | `FS.GI.APP.FX.DEALING.CCY.RESERVED2` | `FsGiAppFxDealingCcy_Reserved2` | TField |  |  |
| 19 | `FS.GI.APP.FX.DEALING.CCY.RESERVED1` | `FsGiAppFxDealingCcy_Reserved1` | TField |  |  |
| 20 | `FS.GI.APP.FX.DEALING.CCY.LOCAL.REF` | `FsGiAppFxDealingCcy_LocalRef` |  |  |  |
| 21 | `FS.GI.APP.FX.DEALING.CCY.OVERRIDE` | `FsGiAppFxDealingCcy_Override` |  |  |  |
| 22 | `FS.GI.APP.FX.DEALING.CCY.RECORD.STATUS` | `FsGiAppFxDealingCcy_RecordStatus` | String |  |  |
| 23 | `FS.GI.APP.FX.DEALING.CCY.CURR.NO` | `FsGiAppFxDealingCcy_CurrNo` | String |  |  |
| 24 | `FS.GI.APP.FX.DEALING.CCY.INPUTTER` | `FsGiAppFxDealingCcy_Inputter` |  |  |  |
| 25 | `FS.GI.APP.FX.DEALING.CCY.DATE.TIME` | `FsGiAppFxDealingCcy_DateTime` |  |  |  |
| 26 | `FS.GI.APP.FX.DEALING.CCY.AUTHORISER` | `FsGiAppFxDealingCcy_Authoriser` | String |  |  |
| 27 | `FS.GI.APP.FX.DEALING.CCY.CO.CODE` | `FsGiAppFxDealingCcy_CoCode` | String |  |  |
| 28 | `FS.GI.APP.FX.DEALING.CCY.DEPT.CODE` | `FsGiAppFxDealingCcy_DeptCode` | String |  |  |
| 29 | `FS.GI.APP.FX.DEALING.CCY.AUDITOR.CODE` | `FsGiAppFxDealingCcy_AuditorCode` | String |  |  |
| 30 | `FS.GI.APP.FX.DEALING.CCY.AUDIT.DATE.TIME` | `FsGiAppFxDealingCcy_AuditDateTime` | String |  |  |
