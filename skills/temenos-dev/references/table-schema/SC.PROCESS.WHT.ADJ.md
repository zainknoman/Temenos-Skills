# SC.PROCESS.WHT.ADJ — Table Schema

> Source: `INSERTS/I_F.SC.PROCESS.WHT.ADJ` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PWA.TAX.TYPE` | `ScProcessWhtAdj_TaxType` | TField |  | Valid TAX.TYPE id to which adjustment needs to be made. validation rules: Madatory field. |
| 2 | `SC.PWA.CLIENT.ID` | `ScProcessWhtAdj_ClientId` | TField | Yes | Valid customer id. Used to get the entitlements records for the customer. validation rules: Mandatory field if the TXN.ID is not given. |
| 3 | `SC.PWA.DATE.TYPE` | `ScProcessWhtAdj_DateType` | TField | Yes | Entitlements will be selected for adjustment based on the field.Valid options are EX.DATE,PAY.DATE,VALUE.DATE. Based on the option elected start and end date check will be performed on ENTITLEMENT application on the field specified in this option validation rules: Mandatory field if the TXN.ID is not given. |
| 4 | `SC.PWA.START.DATE` | `ScProcessWhtAdj_StartDate` | TField | Yes | Transactions greater than and equal to this date will be considered for adjustment.if the start date is not specified, the start date will be assumed to be the start of the calendar year.if the security and depository details are not given, all the taxable transactions for the given date range will be selected. validation rules: Mandatory field if the TXN.ID is not given. |
| 5 | `SC.PWA.END.DATE` | `ScProcessWhtAdj_EndDate` | TField | Yes | Transactions less than and equal to this date will be considered for adjustment.If the end date is not specified, the end date will be assumed to be today. If the security and depository details are not given, all the taxable transactions for the given date range will be selected. validation rules: Mandatory field if the TXN.ID is not given. |
| 6 | `SC.PWA.TXN.ID` | `ScProcessWhtAdj_TxnId` | TField |  | Entitlement id for the adjustment. If the transaction ID is specified, the adjustments will be processed only for that transaction.No other details are considered. validation rules: Check whether the customer is given in CLIENT.ID field if the value exist then it is validated against the customer of the entitlement. |
| 7 | `SC.PWA.SECURITY.NO` | `ScProcessWhtAdj_SecurityNo` | TField | Yes | Security which needs to be considered for the adjustment. If this field is given then the ENTITLEMENTS of the securities will be considered for the adjustment. validation rules: Non mandatory field. |
| 8 | `SC.PWA.DEPOSITORY` | `ScProcessWhtAdj_Depository` |  |  |  |
| 9 | `SC.PWA.SUB.ACCOUNT` | `ScProcessWhtAdj_SubAccount` |  |  |  |
| 10 | `SC.PWA.OVER.UNDER` | `ScProcessWhtAdj_OverUnder` | TField | Yes | Over or Under depending on whether the adjustment is for over withholding or under withholding. validation rules: Mandatory field. |
| 11 | `SC.PWA.SATU.ID` | `ScProcessWhtAdj_SatuId` | TField |  | Id of the record SC.ADJ.TXN.UPDATE created after running the service SC.WHT.ADJUSTMENT.SERVICE.No input field and populated by system. |
| 12 | `SC.PWA.RESERVED.5` | `ScProcessWhtAdj_Reserved5` | TField |  |  |
| 13 | `SC.PWA.RESERVED.4` | `ScProcessWhtAdj_Reserved4` | TField |  |  |
| 14 | `SC.PWA.RESERVED.3` | `ScProcessWhtAdj_Reserved3` | TField |  |  |
| 15 | `SC.PWA.RESERVED.2` | `ScProcessWhtAdj_Reserved2` | TField |  |  |
| 16 | `SC.PWA.RESERVED.1` | `ScProcessWhtAdj_Reserved1` | TField |  |  |
| 17 | `SC.PWA.LOCAL.REF` | `ScProcessWhtAdj_LocalRef` |  |  |  |
| 18 | `SC.PWA.OVERRIDE` | `ScProcessWhtAdj_Override` |  |  |  |
| 19 | `SC.PWA.RECORD.STATUS` | `ScProcessWhtAdj_RecordStatus` | String |  |  |
| 20 | `SC.PWA.CURR.NO` | `ScProcessWhtAdj_CurrNo` | String |  |  |
| 21 | `SC.PWA.INPUTTER` | `ScProcessWhtAdj_Inputter` |  |  |  |
| 22 | `SC.PWA.DATE.TIME` | `ScProcessWhtAdj_DateTime` |  |  |  |
| 23 | `SC.PWA.AUTHORISER` | `ScProcessWhtAdj_Authoriser` | String |  |  |
| 24 | `SC.PWA.CO.CODE` | `ScProcessWhtAdj_CoCode` | String |  |  |
| 25 | `SC.PWA.DEPT.CODE` | `ScProcessWhtAdj_DeptCode` | String |  |  |
| 26 | `SC.PWA.AUDITOR.CODE` | `ScProcessWhtAdj_AuditorCode` | String |  |  |
| 27 | `SC.PWA.AUDIT.DATE.TIME` | `ScProcessWhtAdj_AuditDateTime` | String |  |  |
