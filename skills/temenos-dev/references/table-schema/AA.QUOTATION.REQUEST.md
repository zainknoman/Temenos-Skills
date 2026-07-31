# AA.QUOTATION.REQUEST — Table Schema

> Source: `INSERTS/I_F.AA.QUOTATION.REQUEST` in `AA_Quotation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.QR.DEFINITION` | `AaQuotationRequest_Definition` | TField |  | This field defines that type of the quotation for the customer. Validation Rules 1. It should be valid record from AA.QUOTATION.TYPE. 2. It should be a published definition |
| 2 | `AA.QR.VERSION` | `AaQuotationRequest_Version` | TField |  | Version of AA.QUOTATION.TYPE that needs to be used for processing the quotation |
| 3 | `AA.QR.ACTIVITY` | `AaQuotationRequest_Activity` | TField | Yes | This field defines the Activity to be processed against the Quotation. The activity may be a user activity or a system generated activity. The business functionality of the activity would be defined in the action routines which are defined in ACTIVITY.ACTION or ACTION fields. Validation Rules 1. Input is mandatory in this field. 2. It must be a valid record in AA.CLASS.TYPE.ACTIVITY and valid evidence activity. 3. The very first activity for quotation would be NEW-QUOTATION.REQUEST. |
| 4 | `AA.QR.EFFECTIVE.DATE` | `AaQuotationRequest_EffectiveDate` | TField |  | Effective date when the quotation was requested |
| 5 | `AA.QR.CLASS.INSTANCE` | `AaQuotationRequest_ClassInstance` |  |  |  |
| 6 | `AA.QR.INSTANCE.KEY` | `AaQuotationRequest_InstanceKey` |  |  |  |
| 7 | `AA.QR.INSTANCE.STATUS` | `AaQuotationRequest_InstanceStatus` |  |  |  |
| 8 | `AA.QR.STD.RESERVE8` | `AaQuotationRequest_StdReserve8` | TField |  | Reserved field for future purpose |
| 9 | `AA.QR.STD.RESERVE7` | `AaQuotationRequest_StdReserve7` | TField |  | Reserved field for future purpose |
| 10 | `AA.QR.STD.RESERVE6` | `AaQuotationRequest_StdReserve6` | TField |  | Reserved field for future purpose |
| 11 | `AA.QR.CUSTOMER` | `AaQuotationRequest_Customer` |  |  |  |
| 12 | `AA.QR.CUSTOMER.ROLE` | `AaQuotationRequest_CustomerRole` |  |  |  |
| 13 | `AA.QR.TO.CLASS.INSTANCE` | `AaQuotationRequest_ToClassInstance` |  |  |  |
| 14 | `AA.QR.TO.FIELD` | `AaQuotationRequest_ToField` |  |  |  |
| 15 | `AA.QR.TO.VALUE` | `AaQuotationRequest_ToValue` |  |  |  |
| 16 | `AA.QR.LAST.ACTIVITY` | `AaQuotationRequest_LastActivity` | TField |  | Details of last activity performed on the current record. |
| 17 | `AA.QR.STD.RESERVE4` | `AaQuotationRequest_StdReserve4` | TField |  | Reserved field for future purpose |
| 18 | `AA.QR.STD.RESERVE3` | `AaQuotationRequest_StdReserve3` | TField |  | Reserved field for future purpose |
| 19 | `AA.QR.STD.RESERVE2` | `AaQuotationRequest_StdReserve2` | TField |  | Reserved field for future purpose |
| 20 | `AA.QR.STD.RESERVE1` | `AaQuotationRequest_StdReserve1` | TField |  | Reserved field for future purpose |
| 21 | `AA.QR.NOTES` | `AaQuotationRequest_Notes` |  |  |  |
| 22 | `AA.QR.APPLICATION` | `AaQuotationRequest_Application` | TField |  | It is a valid record from the OA.APPLICATION table. If the user gives input this field then the system will link the current quotation Request along with Application. And the Linked quotation details will get updated in the OA.APPLICATION.STATUS record. |
| 23 | `AA.QR.PURPOSE` | `AaQuotationRequest_Purpose` |  |  |  |
| 24 | `AA.QR.RESERVED.3` | `AaQuotationRequest_Reserved3` | TField |  |  |
| 25 | `AA.QR.RESERVED.2` | `AaQuotationRequest_Reserved2` | TField |  |  |
| 26 | `AA.QR.RESERVED.1` | `AaQuotationRequest_Reserved1` | TField |  |  |
| 27 | `AA.QR.LOCAL.REF` | `AaQuotationRequest_LocalRef` |  |  |  |
| 28 | `AA.QR.STMT.NOS` | `AaQuotationRequest_StmtNos` |  |  |  |
| 29 | `AA.QR.OVERRIDE` | `AaQuotationRequest_Override` |  |  |  |
| 30 | `AA.QR.RECORD.STATUS` | `AaQuotationRequest_RecordStatus` | String |  |  |
| 31 | `AA.QR.CURR.NO` | `AaQuotationRequest_CurrNo` | String |  |  |
| 32 | `AA.QR.INPUTTER` | `AaQuotationRequest_Inputter` |  |  |  |
| 33 | `AA.QR.DATE.TIME` | `AaQuotationRequest_DateTime` |  |  |  |
| 34 | `AA.QR.AUTHORISER` | `AaQuotationRequest_Authoriser` | String |  |  |
| 35 | `AA.QR.CO.CODE` | `AaQuotationRequest_CoCode` | String |  |  |
| 36 | `AA.QR.DEPT.CODE` | `AaQuotationRequest_DeptCode` | String |  |  |
| 37 | `AA.QR.AUDITOR.CODE` | `AaQuotationRequest_AuditorCode` | String |  |  |
| 38 | `AA.QR.AUDIT.DATE.TIME` | `AaQuotationRequest_AuditDateTime` | String |  |  |
