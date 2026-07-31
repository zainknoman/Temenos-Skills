# SY.MASTER — Table Schema

> Source: `INSERTS/I_F.SY.MASTER` in `SY_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.SM.ASSET.CLASS` | `SyMaster_AssetClass` | TField | Yes | This field will hold the asset class of the underlying. Mandatory input Allowed values: EQUITY - For equity accumulator/decumulator contracts. FX - For FX accumulator/decumulator contracts |
| 2 | `SY.SM.MNEMONIC` | `SyMaster_Mnemonic` | TField | Yes | This field will hold the mnemonic, which would be an alternative easy means to reference the master. Like the ID, the Mnemonic must be unique across T24. Mandatory input |
| 3 | `SY.SM.UNDERLYING` | `SyMaster_Underlying` | TField | Yes | This field holds the underlying equity instrument. Validation Rules: NOCHANGE field This field will be made NOINPUT for FX related products ie. allowed to input only if ASSET.CLASS is set as EQUITY. Mandatory input when ASSET.CLASS is set as EQUITY. Must be the ID of a valid SECURITY.MASTER file record. |
| 4 | `SY.SM.CURRENCY1` | `SyMaster_Currency1` | TField | Yes | This field holds the first currency in the currency pair. Validation Rules: NOCHANGE field This field will be made NOINPUT for EQUITY related products ie. allowed to input only when ASSET.CLASS is set as FX. Mandatory input when ASSET.CLASS is set as FX . Must exist on Currency file. |
| 5 | `SY.SM.CURRENCY2` | `SyMaster_Currency2` | TField | Yes | This field holds the second currency in the currency pair. Validation Rules: NOCHANGE field This field will be made NOINPUT for EQUITY related products ie. allowed to input only when ASSET.CLASS is set as FX. Mandatory input when ASSET.CLASS is set as FX . Must exist on Currency file. |
| 6 | `SY.SM.SUB.ASSET.TYPE` | `SyMaster_SubAssetType` | TField |  | This field holds the Sub Asset type associated with this master. This will be used for reporting purposes. Validation Rules: NOCHANGE field Must exist on SUB.ASSET.TYPE file. |
| 7 | `SY.SM.RISK.COMPANY` | `SyMaster_RiskCompany` |  |  |  |
| 8 | `SY.SM.RISK.LEVEL` | `SyMaster_RiskLevel` |  |  |  |
| 9 | `SY.SM.DX.CONTRACT.CODE` | `SyMaster_DxContractCode` | TField |  |  |
| 10 | `SY.SM.RESERVED.19` | `SyMaster_Reserved19` | TField |  |  |
| 11 | `SY.SM.RESERVED.18` | `SyMaster_Reserved18` | TField |  |  |
| 12 | `SY.SM.RESERVED.17` | `SyMaster_Reserved17` | TField |  |  |
| 13 | `SY.SM.RESERVED.16` | `SyMaster_Reserved16` | TField |  |  |
| 14 | `SY.SM.RESERVED.15` | `SyMaster_Reserved15` | TField |  |  |
| 15 | `SY.SM.RESERVED.14` | `SyMaster_Reserved14` | TField |  |  |
| 16 | `SY.SM.RESERVED.13` | `SyMaster_Reserved13` | TField |  |  |
| 17 | `SY.SM.RESERVED.12` | `SyMaster_Reserved12` | TField |  |  |
| 18 | `SY.SM.RESERVED.11` | `SyMaster_Reserved11` | TField |  |  |
| 19 | `SY.SM.RESERVED.10` | `SyMaster_Reserved10` | TField |  |  |
| 20 | `SY.SM.RESERVED.09` | `SyMaster_Reserved09` | TField |  |  |
| 21 | `SY.SM.RESERVED.08` | `SyMaster_Reserved08` | TField |  |  |
| 22 | `SY.SM.RESERVED.07` | `SyMaster_Reserved07` | TField |  |  |
| 23 | `SY.SM.RESERVED.06` | `SyMaster_Reserved06` | TField |  |  |
| 24 | `SY.SM.RESERVED.05` | `SyMaster_Reserved05` | TField |  |  |
| 25 | `SY.SM.RESERVED.04` | `SyMaster_Reserved04` | TField |  |  |
| 26 | `SY.SM.RESERVED.03` | `SyMaster_Reserved03` | TField |  |  |
| 27 | `SY.SM.RESERVED.02` | `SyMaster_Reserved02` | TField |  |  |
| 28 | `SY.SM.RESERVED.01` | `SyMaster_Reserved01` | TField |  |  |
| 29 | `SY.SM.LOCAL.REF` | `SyMaster_LocalRef` |  |  |  |
| 30 | `SY.SM.OVERRIDE` | `SyMaster_Override` |  |  |  |
| 31 | `SY.SM.RECORD.STATUS` | `SyMaster_RecordStatus` | String |  |  |
| 32 | `SY.SM.CURR.NO` | `SyMaster_CurrNo` | String |  |  |
| 33 | `SY.SM.INPUTTER` | `SyMaster_Inputter` |  |  |  |
| 34 | `SY.SM.DATE.TIME` | `SyMaster_DateTime` |  |  |  |
| 35 | `SY.SM.AUTHORISER` | `SyMaster_Authoriser` | String |  |  |
| 36 | `SY.SM.CO.CODE` | `SyMaster_CoCode` | String |  |  |
| 37 | `SY.SM.DEPT.CODE` | `SyMaster_DeptCode` | String |  |  |
| 38 | `SY.SM.AUDITOR.CODE` | `SyMaster_AuditorCode` | String |  |  |
| 39 | `SY.SM.AUDIT.DATE.TIME` | `SyMaster_AuditDateTime` | String |  |  |
