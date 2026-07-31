# PP.ERRORTYPES — Table Schema

> Source: `INSERTS/I_F.PP.ERRORTYPES` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.ERT.CompanyID` | `PpErrortypes_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.ERT.ErrorType` | `PpErrortypes_Errortype` | TField |  | Specifies whether the error belongs to type INFORMATION or WARNING. Possible values: F - FUNCTIONAL I - INFORMATION W - WARNING |
| 3 | `PP.ERT.ForceRepair` | `PpErrortypes_Forcerepair` | TField |  | If forcedRepair flag is set as 'Y' for an error code, the payment will be routed to repair. This field can take 'Y' or 'N' as values. |
| 4 | `PP.ERT.Importance` | `PpErrortypes_Importance` | TField |  | Indicator with integer values where highest priority will be given to the lowest value. |
| 5 | `PP.ERT.EbErrorOverrideId` | `PpErrortypes_Eberroroverrideid` |  |  |  |
| 6 | `PP.ERT.EbForceRepair` | `PpErrortypes_Ebforcerepair` |  |  |  |
| 7 | `PP.ERT.EbImportance` | `PpErrortypes_Ebimportance` |  |  |  |
| 8 | `PP.ERT.RESERVED.2` | `PpErrortypes_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 9 | `PP.ERT.RESERVED.1` | `PpErrortypes_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 10 | `PP.ERT.LOCAL.REF` | `PpErrortypes_LocalRef` |  |  |  |
| 11 | `PP.ERT.OVERRIDE` | `PpErrortypes_Override` |  |  |  |
| 12 | `PP.ERT.RECORD.STATUS` | `PpErrortypes_RecordStatus` | String |  |  |
| 13 | `PP.ERT.CURR.NO` | `PpErrortypes_CurrNo` | String |  |  |
| 14 | `PP.ERT.INPUTTER` | `PpErrortypes_Inputter` |  |  |  |
| 15 | `PP.ERT.DATE.TIME` | `PpErrortypes_DateTime` |  |  |  |
| 16 | `PP.ERT.AUTHORISER` | `PpErrortypes_Authoriser` | String |  |  |
| 17 | `PP.ERT.CO.CODE` | `PpErrortypes_CoCode` | String |  |  |
| 18 | `PP.ERT.DEPT.CODE` | `PpErrortypes_DeptCode` | String |  |  |
| 19 | `PP.ERT.AUDITOR.CODE` | `PpErrortypes_AuditorCode` | String |  |  |
| 20 | `PP.ERT.AUDIT.DATE.TIME` | `PpErrortypes_AuditDateTime` | String |  |  |
