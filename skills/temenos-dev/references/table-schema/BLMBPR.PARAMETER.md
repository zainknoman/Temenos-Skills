# BLMBPR.PARAMETER — Table Schema

> Source: `INSERTS/I_F.BLMBPR.PARAMETER` in `BLMBPR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BLMBPR.PARAM.UPDATE.CODE` | `BlmbprParameter_UpdateCode` | TField |  | This update code of a security identifies the Bloomberg update. Validation Rule: 1) This table must be linked to PRICE.UPDATE application |
| 2 | `BLMBPR.PARAM.CURR.CONVERSION` | `BlmbprParameter_CurrConversion` | TField | Yes | Specifies if the updated price should be converted to the currency it is held in, in GLOBUS if it is different from it. Has a value of Y or N. Mandatory input. |
| 3 | `BLMBPR.PARAM.EXCH.RATE.FIELD` | `BlmbprParameter_ExchRateField` | TField |  | Specifies the field in the file CURRENCY from where the exchange rate for currency must be taken. Must be no input if the above field is N. Must be a drop down list with the values REVAL.RATE and MID.REVAL.RATE. Validation Rule: 1) If the CURR CONVERSION field values is N , make this field as null value 1) If the CURR CONVERSION field values is Y , it will be drop down list with the values REVAL.RATE and MID.REVAL.RATE |
| 4 | `BLMBPR.PARAM.ASSET.TYPE.CODE` | `BlmbprParameter_AssetTypeCode` |  |  |  |
| 5 | `BLMBPR.PARAM.AT.PR.VAR.PCNT` | `BlmbprParameter_AtPrVarPcnt` |  |  |  |
| 6 | `BLMBPR.PARAM.AT.PR.FREQ.UPD` | `BlmbprParameter_AtPrFreqUpd` |  |  |  |
| 7 | `BLMBPR.PARAM.AT.PR.ORDER` | `BlmbprParameter_AtPrOrder` |  |  |  |
| 8 | `BLMBPR.PARAM.SUB.ASSET.TYPE` | `BlmbprParameter_SubAssetType` |  |  |  |
| 9 | `BLMBPR.PARAM.SAT.PR.VAR.PCNT` | `BlmbprParameter_SatPrVarPcnt` |  |  |  |
| 10 | `BLMBPR.PARAM.SAT.PR.FREQ.UPD` | `BlmbprParameter_SatPrFreqUpd` |  |  |  |
| 11 | `BLMBPR.PARAM.SAT.PR.ORDER` | `BlmbprParameter_SatPrOrder` |  |  |  |
| 12 | `BLMBPR.PARAM.ALT.SEC.ID` | `BlmbprParameter_AltSecId` |  |  |  |
| 13 | `BLMBPR.PARAM.BLOOMBERG.ID` | `BlmbprParameter_BloombergId` |  |  |  |
| 14 | `BLMBPR.PARAM.FEED.CCY` | `BlmbprParameter_FeedCcy` |  |  |  |
| 15 | `BLMBPR.PARAM.ACTUAL.CCY` | `BlmbprParameter_ActualCcy` |  |  |  |
| 16 | `BLMBPR.PARAM.MULT.FACTOR` | `BlmbprParameter_MultFactor` |  |  |  |
| 17 | `BLMBPR.PARAM.ALT.SEC.PARAM` | `BlmbprParameter_AltSecParam` | TField |  | This filed contains the parameter value to generate the outward file generation. This value present in the ALT.SECURITY.ID of the SM record. |
| 18 | `BLMBPR.PARAM.ALT.SEC.DUP.CHECK` | `BlmbprParameter_AltSecDupCheck` | TField |  | This field contain the value YES or NO. If we set field YES means then it will check the Duplicate value in the ALT.SECURITY.NO field of the SECURITY.MASTER record |
| 19 | `BLMBPR.PARAM.DATA.LICENSE.NO` | `BlmbprParameter_DataLicenseNo` | TField |  | This field to define the FIRMNAME used in Bloomberg |
| 20 | `BLMBPR.PARAM.LOGIN.ID` | `BlmbprParameter_LoginId` | TField |  | This field to define the login id used in Bloomberg |
| 21 | `BLMBPR.PARAM.USER.NUMBER` | `BlmbprParameter_UserNumber` | TField |  | This field to define the user name used in Bloomberg |
| 22 | `BLMBPR.PARAM.SERIAL.NUMBER` | `BlmbprParameter_SerialNumber` | TField |  | This field to define the Serial Number "SN" used in Bloomberg |
| 23 | `BLMBPR.PARAM.WORKSTATION.NO` | `BlmbprParameter_WorkstationNo` | TField |  | This field to define the Work station number "WS" used in Bloomberg |
| 24 | `BLMBPR.PARAM.LOCAL.REF` | `BlmbprParameter_LocalRef` |  |  |  |
| 25 | `BLMBPR.PARAM.OVERRIDE` | `BlmbprParameter_Override` |  |  |  |
| 26 | `BLMBPR.PARAM.RECORD.STATUS` | `BlmbprParameter_RecordStatus` | String |  |  |
| 27 | `BLMBPR.PARAM.CURR.NO` | `BlmbprParameter_CurrNo` | String |  |  |
| 28 | `BLMBPR.PARAM.INPUTTER` | `BlmbprParameter_Inputter` |  |  |  |
| 29 | `BLMBPR.PARAM.DATE.TIME` | `BlmbprParameter_DateTime` |  |  |  |
| 30 | `BLMBPR.PARAM.AUTHORISER` | `BlmbprParameter_Authoriser` | String |  |  |
| 31 | `BLMBPR.PARAM.CO.CODE` | `BlmbprParameter_CoCode` | String |  |  |
| 32 | `BLMBPR.PARAM.DEPT.CODE` | `BlmbprParameter_DeptCode` | String |  |  |
| 33 | `BLMBPR.PARAM.AUDITOR.CODE` | `BlmbprParameter_AuditorCode` | String |  |  |
| 34 | `BLMBPR.PARAM.AUDIT.DATE.TIME` | `BlmbprParameter_AuditDateTime` | String |  |  |
