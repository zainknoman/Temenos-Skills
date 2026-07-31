# FICOLL.ASSET.DETAILS — Table Schema

> Source: `INSERTS/I_F.FICOLL.ASSET.DETAILS` in `FICOLL_Collateral.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FICOLL.ASSET.ASSET.TYPE` | `FicollAssetDetails_AssetType` | TField |  | A drop down option field to store the collateral type of the underlying asset. Validation Rules: Should be of type Ship / Vehicle / Aircraft / Floating charges / Deeds.These are valid entries from COLLATERAL.TYPE application. |
| 2 | `FICOLL.ASSET.CURRENCY` | `FicollAssetDetails_Currency` | TField | No | The currency in which the Asset details are expressed.If no input is given, defaults to local currency. Validation Rules: 3 alphanumeric characters, a valid code from the currency table.Optional Input. |
| 3 | `FICOLL.ASSET.COST.OF.ASSET` | `FicollAssetDetails_CostOfAsset` | TField | Yes | Stores the purchase or Nominal value of the Asset. Validation Rules: Up to 19 digit numeric , inclusive decimal point(amount format).Mandatory user-input field. |
| 4 | `FICOLL.ASSET.CURRENT.VALUE` | `FicollAssetDetails_CurrentValue` | TField | Yes | Stores the Execution value of the asset.This value is used for all calculations related to the asset and is the real valueof the asset. Validation Rules: Up to 19 digit numeric , inclusive decimal point(amount format).Mandatory user-input field. |
| 5 | `FICOLL.ASSET.LOCAL.REF` | `FicollAssetDetails_LocalRef` |  |  |  |
| 6 | `FICOLL.ASSET.OVERRIDE` | `FicollAssetDetails_Override` |  |  |  |
| 7 | `FICOLL.ASSET.RECORD.STATUS` | `FicollAssetDetails_RecordStatus` | String |  |  |
| 8 | `FICOLL.ASSET.CURR.NO` | `FicollAssetDetails_CurrNo` | String |  |  |
| 9 | `FICOLL.ASSET.INPUTTER` | `FicollAssetDetails_Inputter` |  |  |  |
| 10 | `FICOLL.ASSET.DATE.TIME` | `FicollAssetDetails_DateTime` |  |  |  |
| 11 | `FICOLL.ASSET.AUTHORISER` | `FicollAssetDetails_Authoriser` | String |  |  |
| 12 | `FICOLL.ASSET.CO.CODE` | `FicollAssetDetails_CoCode` | String |  |  |
| 13 | `FICOLL.ASSET.DEPT.CODE` | `FicollAssetDetails_DeptCode` | String |  |  |
| 14 | `FICOLL.ASSET.AUDITOR.CODE` | `FicollAssetDetails_AuditorCode` | String |  |  |
| 15 | `FICOLL.ASSET.AUDIT.DATE.TIME` | `FicollAssetDetails_AuditDateTime` | String |  |  |
