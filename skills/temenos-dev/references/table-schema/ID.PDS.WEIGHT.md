# ID.PDS.WEIGHT — Table Schema

> Source: `INSERTS/I_F.ID.PDS.WEIGHT` in `ID_PdsConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.WGT.DESCRIPTION` | `IdPdsWeight_Description` |  |  |  |
| 2 | `ID.WGT.AMOUNT.FROM` | `IdPdsWeight_AmountFrom` |  |  |  |
| 3 | `ID.WGT.AMOUNT.TO` | `IdPdsWeight_AmountTo` |  |  |  |
| 4 | `ID.WGT.WEIGHT` | `IdPdsWeight_Weight` |  |  |  |
| 5 | `ID.WGT.MUD.SHARE` | `IdPdsWeight_MudShare` |  |  |  |
| 6 | `ID.WGT.IRR.PERCENT` | `IdPdsWeight_IrrPercent` |  |  |  |
| 7 | `ID.WGT.PER.PERCENT` | `IdPdsWeight_PerPercent` |  |  |  |
| 8 | `ID.WGT.ACCRUAL.RATE` | `IdPdsWeight_AccrualRate` |  |  |  |
| 9 | `ID.WGT.UPDATE.RATE` | `IdPdsWeight_UpdateRate` |  |  |  |
| 10 | `ID.WGT.RESERVED.20` | `IdPdsWeight_Reserved20` |  |  |  |
| 11 | `ID.WGT.RESERVED.19` | `IdPdsWeight_Reserved19` |  |  |  |
| 12 | `ID.WGT.RESERVED.18` | `IdPdsWeight_Reserved18` |  |  |  |
| 13 | `ID.WGT.RESERVED.17` | `IdPdsWeight_Reserved17` |  |  |  |
| 14 | `ID.WGT.RESERVED.16` | `IdPdsWeight_Reserved16` |  |  |  |
| 15 | `ID.WGT.RESERVED.15` | `IdPdsWeight_Reserved15` |  |  |  |
| 16 | `ID.WGT.RESERVED.14` | `IdPdsWeight_Reserved14` |  |  |  |
| 17 | `ID.WGT.RESERVED.13` | `IdPdsWeight_Reserved13` |  |  |  |
| 18 | `ID.WGT.RESERVED.12` | `IdPdsWeight_Reserved12` |  |  |  |
| 19 | `ID.WGT.RESERVED.11` | `IdPdsWeight_Reserved11` |  |  |  |
| 20 | `ID.WGT.APPLY.AS.TIER.RATE` | `IdPdsWeight_ApplyAsTierRate` | TField |  | It is possible to define the profit rate as a tier rate with band or level conditions when creating the Mudaraba savings account. It can be set as "Yes" to default the accrual rate configured for different balance brackets. Validation: It cannot be set as "Yes" for "ALL.ALL" condition. It is not allowed to modify this field definition after authorization. |
| 21 | `ID.WGT.BAND.OR.LEVEL` | `IdPdsWeight_BandOrLevel` | TField |  | It indicates whether the tier definition of profit rates is applied by using band or level calculation method. Validation: It is not allowed to modify this field definition after authorization. |
| 22 | `ID.WGT.RESERVED.8` | `IdPdsWeight_Reserved8` |  |  |  |
| 23 | `ID.WGT.RESERVED.7` | `IdPdsWeight_Reserved7` | TField |  |  |
| 24 | `ID.WGT.RESERVED.6` | `IdPdsWeight_Reserved6` | TField |  |  |
| 25 | `ID.WGT.RESERVED.5` | `IdPdsWeight_Reserved5` | TField |  |  |
| 26 | `ID.WGT.RESERVED.4` | `IdPdsWeight_Reserved4` | TField |  |  |
| 27 | `ID.WGT.RESERVED.3` | `IdPdsWeight_Reserved3` | TField |  |  |
| 28 | `ID.WGT.RESERVED.2` | `IdPdsWeight_Reserved2` | TField |  |  |
| 29 | `ID.WGT.RESERVED.1` | `IdPdsWeight_Reserved1` | TField |  |  |
| 30 | `ID.WGT.LOCAL.REF` | `IdPdsWeight_LocalRef` |  |  |  |
| 31 | `ID.WGT.OVERRIDE` | `IdPdsWeight_Override` |  |  |  |
| 32 | `ID.WGT.RECORD.STATUS` | `IdPdsWeight_RecordStatus` | String |  |  |
| 33 | `ID.WGT.CURR.NO` | `IdPdsWeight_CurrNo` | String |  |  |
| 34 | `ID.WGT.INPUTTER` | `IdPdsWeight_Inputter` |  |  |  |
| 35 | `ID.WGT.DATE.TIME` | `IdPdsWeight_DateTime` |  |  |  |
| 36 | `ID.WGT.AUTHORISER` | `IdPdsWeight_Authoriser` | String |  |  |
| 37 | `ID.WGT.CO.CODE` | `IdPdsWeight_CoCode` | String |  |  |
| 38 | `ID.WGT.DEPT.CODE` | `IdPdsWeight_DeptCode` | String |  |  |
| 39 | `ID.WGT.AUDITOR.CODE` | `IdPdsWeight_AuditorCode` | String |  |  |
| 40 | `ID.WGT.AUDIT.DATE.TIME` | `IdPdsWeight_AuditDateTime` | String |  |  |
