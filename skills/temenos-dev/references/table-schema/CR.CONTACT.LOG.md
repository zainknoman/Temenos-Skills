# CR.CONTACT.LOG — Table Schema

> Source: `INSERTS/I_F.CR.CONTACT.LOG` in `CR_Analytical.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CR.CONT.LOG.CONTACT.CLIENT` | `CrContactLog_ContactClient` | TField |  | Specifies the ID of the customer or a prospect customer who interacts with the bank. Validation Rules Input to this field is based on options in the field WALK.IN.CUSTOMER Can be a valid ID from the CUSTOMER or PERSON.ENTITY table. |
| 2 | `CR.CONT.LOG.CONTACT.TYPE` | `CrContactLog_ContactType` | TField |  | Defines the type of contact made between customer and bank. If the contact iscreated by T24 application then this field will be set to TRANSACTION.e.g EMAIL,LETTER,CALLCENTRE Validation Rules :Input must have an existing code on EB.LOOKUP table |
| 3 | `CR.CONT.LOG.CONTACT.STATUS` | `CrContactLog_ContactStatus` | TField |  | Identifies the status of the customer contact log. e.gNEW,CONFIRMED,PENDING Validation Rules :Input must have valid entry on EB.LOOKUP table |
| 4 | `CR.CONT.LOG.CONTACT.DESC` | `CrContactLog_ContactDesc` | TField | Yes | Descriptive information on customer interaction with the bank Validation Rules :Mandatory input. Input must be alphanumeric. |
| 5 | `CR.CONT.LOG.CONTACT.NOTES` | `CrContactLog_ContactNotes` |  |  |  |
| 6 | `CR.CONT.LOG.CONTACT.STAFF` | `CrContactLog_ContactStaff` |  |  |  |
| 7 | `CR.CONT.LOG.CONTACT.CHANNEL` | `CrContactLog_ContactChannel` | TField |  | Specifies the channel for communication between customer and bankDifferent types channels has been described below:Channel DescriptionBRANCH When the customer visits the bankCALLCENTER Marketed through call centerEMAIL Campaigned through emailIM Campaigned through instant messengerINTERNET Communicated through internetNONE No channel usedPERSONAL By meeting the customer personallyPOST Launched by mail serviceSKYPE Instant messenger serviceSMS By Short messaging serviceOTHER Channel not mentioned above Validation Rules :Input should have an entry on EB.LOOKUP table |
| 8 | `CR.CONT.LOG.CONTACT.DATE` | `CrContactLog_ContactDate` | TField |  | Stores the client contact date. System date will be defaulted. Validation Rules :Standard date format (YYYYMMDD) |
| 9 | `CR.CONT.LOG.CONTACT.TIME` | `CrContactLog_ContactTime` | TField |  | Stores the client contact time. System date will be defaulted. Validation Rules :Standard time format (hh:mm) |
| 10 | `CR.CONT.LOG.APPL.VERSION` | `CrContactLog_ApplVersion` | TField |  | Holds the T24 application version ID. This will be updated when the type of contactlog is TRANSACTION. Validation Rules :No input field |
| 11 | `CR.CONT.LOG.CONTRACT.ID` | `CrContactLog_ContractId` | TField |  | Stores the ID of T24 application. Record id of transaction created. |
| 12 | `CR.CONT.LOG.COMPANY.CODE` | `CrContactLog_CompanyCode` | TField |  | Company code where the client is having financial data. Company id will bedefaulted. Validation Rules :Input should have valid entry on company code |
| 13 | `CR.CONT.LOG.CONTACT.DIRECTION` | `CrContactLog_ContactDirection` | TField |  | Direction of contact initiation. Default value is INWARD. Validation Rules :Allowed values are INWARD OUTWARD |
| 14 | `CR.CONT.LOG.MOOD` | `CrContactLog_Mood` | TField | No | Defines the customers mood during the contact with the bank. Validation Rules :Optional input. Allowed values are HAPPY ANGRY |
| 15 | `CR.CONT.LOG.WALK.IN.CUSTOMER` | `CrContactLog_WalkInCustomer` | TField | Yes | Field to recognize whether a customer is a T24 customer or walk-in customer Validation Rules Mandatory field YES - Implies that the person is a Walk-in customer. NO - Implies that the person is a T24 customer, a valid CUSTOMER record exist for the person. NONE - Implies that a person is neither a T24 customer nor Walk-in customer |
| 16 | `CR.CONT.LOG.RESERVED.8` | `CrContactLog_Reserved8` |  |  |  |
| 17 | `CR.CONT.LOG.RESERVED.7` | `CrContactLog_Reserved7` |  |  |  |
| 18 | `CR.CONT.LOG.RESERVED.6` | `CrContactLog_Reserved6` |  |  |  |
| 19 | `CR.CONT.LOG.RESERVED.5` | `CrContactLog_Reserved5` | TField |  |  |
| 20 | `CR.CONT.LOG.RESERVED.4` | `CrContactLog_Reserved4` | TField |  |  |
| 21 | `CR.CONT.LOG.RESERVED.3` | `CrContactLog_Reserved3` | TField |  |  |
| 22 | `CR.CONT.LOG.RESERVED.2` | `CrContactLog_Reserved2` | TField |  |  |
| 23 | `CR.CONT.LOG.RESERVED.1` | `CrContactLog_Reserved1` | TField |  |  |
| 24 | `CR.CONT.LOG.LOCAL.REF` | `CrContactLog_LocalRef` |  |  |  |
| 25 | `CR.CONT.LOG.OVERRIDE` | `CrContactLog_Override` |  |  |  |
| 26 | `CR.CONT.LOG.RECORD.STATUS` | `CrContactLog_RecordStatus` | String |  |  |
| 27 | `CR.CONT.LOG.CURR.NO` | `CrContactLog_CurrNo` | String |  |  |
| 28 | `CR.CONT.LOG.INPUTTER` | `CrContactLog_Inputter` |  |  |  |
| 29 | `CR.CONT.LOG.DATE.TIME` | `CrContactLog_DateTime` |  |  |  |
| 30 | `CR.CONT.LOG.AUTHORISER` | `CrContactLog_Authoriser` | String |  |  |
| 31 | `CR.CONT.LOG.CO.CODE` | `CrContactLog_CoCode` | String |  |  |
| 32 | `CR.CONT.LOG.DEPT.CODE` | `CrContactLog_DeptCode` | String |  |  |
| 33 | `CR.CONT.LOG.AUDITOR.CODE` | `CrContactLog_AuditorCode` | String |  |  |
| 34 | `CR.CONT.LOG.AUDIT.DATE.TIME` | `CrContactLog_AuditDateTime` | String |  |  |
