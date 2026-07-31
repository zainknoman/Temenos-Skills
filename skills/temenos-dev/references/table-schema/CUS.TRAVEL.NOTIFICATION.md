# CUS.TRAVEL.NOTIFICATION — Table Schema

> Source: `INSERTS/I_F.CUS.TRAVEL.NOTIFICATION` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CU.TN.CUSTOMER.ID` | `CusTravelNotification_CustomerId` | TField | Yes | Holds the customer's Id who is going to travel Validation Rules: Should be a valid T24 Customer(Mandatory input) |
| 2 | `CU.TN.TRAVEL.COUNTRY` | `CusTravelNotification_TravelCountry` |  |  |  |
| 3 | `CU.TN.VISIT.PERIOD.START` | `CusTravelNotification_VisitPeriodStart` |  |  |  |
| 4 | `CU.TN.VISIT.TIME.FROM` | `CusTravelNotification_VisitTimeFrom` |  |  |  |
| 5 | `CU.TN.VISIT.TIME.TO` | `CusTravelNotification_VisitTimeTo` |  |  |  |
| 6 | `CU.TN.VISIT.PERIOD.END` | `CusTravelNotification_VisitPeriodEnd` |  |  |  |
| 7 | `CU.TN.VISIT.PURPOSE` | `CusTravelNotification_VisitPurpose` |  |  |  |
| 8 | `CU.TN.CONTACT.DETAILS` | `CusTravelNotification_ContactDetails` |  |  |  |
| 9 | `CU.TN.ACCT.TO.BE.USED` | `CusTravelNotification_AcctToBeUsed` |  |  |  |
| 10 | `CU.TN.SCHEDULE.TYPE` | `CusTravelNotification_ScheduleType` |  |  |  |
| 11 | `CU.TN.TRAVEL.STATUS` | `CusTravelNotification_TravelStatus` |  |  |  |
| 12 | `CU.TN.ADDNL.INFO` | `CusTravelNotification_AddnlInfo` |  |  |  |
| 13 | `CU.TN.CANCEL.REQUEST` | `CusTravelNotification_CancelRequest` | TField |  | Indicates if the travel record is to be cancelled or not.If cancelled , the record will be moved to history Validation Rules: Options allowed are Yes,No(Default value is No) |
| 14 | `CU.TN.OVERALL.STATUS` | `CusTravelNotification_OverallStatus` | TField |  | Holds the overall status of the travel record. Expired records will be moved to history Validation Rules: Option allowed is Active,Expired(Default value is Active) |
| 15 | `CU.TN.RESERVED.10` | `CusTravelNotification_Reserved10` | TField |  |  |
| 16 | `CU.TN.RESERVED.09` | `CusTravelNotification_Reserved09` | TField |  |  |
| 17 | `CU.TN.RESERVED.08` | `CusTravelNotification_Reserved08` | TField |  |  |
| 18 | `CU.TN.RESERVED.07` | `CusTravelNotification_Reserved07` | TField |  |  |
| 19 | `CU.TN.RESERVED.06` | `CusTravelNotification_Reserved06` | TField |  |  |
| 20 | `CU.TN.RESERVED.05` | `CusTravelNotification_Reserved05` | TField |  |  |
| 21 | `CU.TN.RESERVED.04` | `CusTravelNotification_Reserved04` | TField |  |  |
| 22 | `CU.TN.RESERVED.03` | `CusTravelNotification_Reserved03` | TField |  |  |
| 23 | `CU.TN.RESERVED.02` | `CusTravelNotification_Reserved02` | TField |  |  |
| 24 | `CU.TN.RESERVED.01` | `CusTravelNotification_Reserved01` | TField |  |  |
| 25 | `CU.TN.LOCAL.REF` | `CusTravelNotification_LocalRef` |  |  |  |
| 26 | `CU.TN.OVERRIDE` | `CusTravelNotification_Override` |  |  |  |
| 27 | `CU.TN.RECORD.STATUS` | `CusTravelNotification_RecordStatus` | String |  |  |
| 28 | `CU.TN.CURR.NO` | `CusTravelNotification_CurrNo` | String |  |  |
| 29 | `CU.TN.INPUTTER` | `CusTravelNotification_Inputter` |  |  |  |
| 30 | `CU.TN.DATE.TIME` | `CusTravelNotification_DateTime` |  |  |  |
| 31 | `CU.TN.AUTHORISER` | `CusTravelNotification_Authoriser` | String |  |  |
| 32 | `CU.TN.CO.CODE` | `CusTravelNotification_CoCode` | String |  |  |
| 33 | `CU.TN.DEPT.CODE` | `CusTravelNotification_DeptCode` | String |  |  |
| 34 | `CU.TN.AUDITOR.CODE` | `CusTravelNotification_AuditorCode` | String |  |  |
| 35 | `CU.TN.AUDIT.DATE.TIME` | `CusTravelNotification_AuditDateTime` | String |  |  |
