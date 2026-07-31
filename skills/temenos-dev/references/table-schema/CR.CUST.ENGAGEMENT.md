# CR.CUST.ENGAGEMENT — Table Schema

> Source: `INSERTS/I_F.CR.CUST.ENGAGEMENT` in `CR_Analytical.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CR.CET.CUSTOMER` | `CrCustEngagement_Customer` | TField | Yes | Specifies the ID of the customer or a prospect customer who interacts with the bank. Validation Rules Mandatory field Can be a valid ID from the CUSTOMER table. |
| 2 | `CR.CET.LOCATION` | `CrCustEngagement_Location` | TField |  | The customer visits the bank company code. Validation Rules :Input must have valid entry on COMPANY table |
| 3 | `CR.CET.DATE` | `CrCustEngagement_Date` | TField |  | Stores the client contact date.If date is null,system date will be defaulted. Validation Rules :Standard date format (YYYYMMDD) |
| 4 | `CR.CET.TIME.IN` | `CrCustEngagement_TimeIn` | TField |  | Stores the Time client checked in. Validation Rules :Standard time format (hh:mm) |
| 5 | `CR.CET.TIME.OUT` | `CrCustEngagement_TimeOut` | TField |  | Stores the Time client checked out. Validation Rules :Standard time format (hh:mm) |
| 6 | `CR.CET.NOTES` | `CrCustEngagement_Notes` |  |  |  |
| 7 | `CR.CET.CHANNEL` | `CrCustEngagement_Channel` | TField |  | Specifies the channel for communication between customer and bankDifferent types channels has been described below:Channel DescriptionBRANCH When the customer visits the bankCALLCENTER Marketed through call centerEMAIL Campaigned through emailIM Campaigned through instant messengerINTERNET Communicated through internetNONE No channel usedPERSONAL By meeting the customer personallyPOST Launched by mail serviceSKYPE Instant messenger serviceSMS By Short messaging serviceOTHER Channel not mentioned above Validation Rules :Input should have an entry on EB.CHANNEL table |
| 8 | `CR.CET.IDENTIFIED` | `CrCustEngagement_Identified` | TField |  | Field to recognize whether a customer is a T24 customer or walk-in customer Validation Rules YES - Implies that the person is a T24 customer. |
| 9 | `CR.CET.EXTENSION` | `CrCustEngagement_Extension` | TField |  | If callcentre ? extension required (so phone records can be identified) Validation Rules :A maximum of 35 numeric characters may be entered. |
| 10 | `CR.CET.CHECKOUT.TYPE` | `CrCustEngagement_CheckoutType` | TField |  | Whether the client is checked out. Validation Rules USER - Client is checked out by User. SYSTEM - Client is checked out by System. |
| 11 | `CR.CET.COMMON.ACTIVITY` | `CrCustEngagement_CommonActivity` |  |  |  |
| 12 | `CR.CET.ASSIGNED.OFFICER` | `CrCustEngagement_AssignedOfficer` |  |  |  |
| 13 | `CR.CET.ASSIGNED.USER` | `CrCustEngagement_AssignedUser` |  |  |  |
| 14 | `CR.CET.ASS.OFF.ST.TIME` | `CrCustEngagement_AssOffStTime` |  |  |  |
| 15 | `CR.CET.ASS.OFF.END.TIME` | `CrCustEngagement_AssOffEndTime` |  |  |  |
| 16 | `CR.CET.ACTIONS` | `CrCustEngagement_Actions` |  |  |  |
| 17 | `CR.CET.RESERVED.04` | `CrCustEngagement_Reserved04` |  |  |  |
| 18 | `CR.CET.RESERVED.03` | `CrCustEngagement_Reserved03` |  |  |  |
| 19 | `CR.CET.RESERVED.02` | `CrCustEngagement_Reserved02` |  |  |  |
| 20 | `CR.CET.RESERVED.01` | `CrCustEngagement_Reserved01` |  |  |  |
| 21 | `CR.CET.RESERVED.09` | `CrCustEngagement_Reserved09` | TField |  |  |
| 22 | `CR.CET.RESERVED.08` | `CrCustEngagement_Reserved08` | TField |  |  |
| 23 | `CR.CET.RESERVED.07` | `CrCustEngagement_Reserved07` | TField |  |  |
| 24 | `CR.CET.RESERVED.06` | `CrCustEngagement_Reserved06` | TField |  |  |
| 25 | `CR.CET.RESERVED.05` | `CrCustEngagement_Reserved05` | TField |  |  |
| 26 | `CR.CET.LOCAL.REF` | `CrCustEngagement_LocalRef` |  |  |  |
| 27 | `CR.CET.OVERRIDE` | `CrCustEngagement_Override` |  |  |  |
| 28 | `CR.CET.RECORD.STATUS` | `CrCustEngagement_RecordStatus` | String |  |  |
| 29 | `CR.CET.CURR.NO` | `CrCustEngagement_CurrNo` | String |  |  |
| 30 | `CR.CET.INPUTTER` | `CrCustEngagement_Inputter` |  |  |  |
| 31 | `CR.CET.DATE.TIME` | `CrCustEngagement_DateTime` |  |  |  |
| 32 | `CR.CET.AUTHORISER` | `CrCustEngagement_Authoriser` | String |  |  |
| 33 | `CR.CET.CO.CODE` | `CrCustEngagement_CoCode` | String |  |  |
| 34 | `CR.CET.DEPT.CODE` | `CrCustEngagement_DeptCode` | String |  |  |
| 35 | `CR.CET.AUDITOR.CODE` | `CrCustEngagement_AuditorCode` | String |  |  |
| 36 | `CR.CET.AUDIT.DATE.TIME` | `CrCustEngagement_AuditDateTime` | String |  |  |
