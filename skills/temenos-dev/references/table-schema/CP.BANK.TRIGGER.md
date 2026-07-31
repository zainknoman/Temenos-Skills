# CP.BANK.TRIGGER — Table Schema

> Source: `INSERTS/I_F.CP.BANK.TRIGGER` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.BT.NAME` | `CpBankTrigger_Name` | TField | Yes | This field stores the name assigned to a trigger by the Digital Engagement Admin user.In the Administration User Agent Interface, the Admin user will be able to type in the name of the trigger.When the Admin user saves the trigger definition the name of the trigger is stored in this field. Validation Rules: Mandatory field, any 50 characters. |
| 2 | `CP.BT.DESCRIPTION` | `CpBankTrigger_Description` |  |  |  |
| 3 | `CP.BT.TYPE` | `CpBankTrigger_Type` | TField | Yes | This field stores the type of the trigger.The Admin user can choose a type of event depending of the source from which the event is passed in the Campaign Engine.This will be a predefined list of event types.The Admin role will be able to pick one of the values from the list to define the type of the new bank event. Validation Rules: Mandatory field. |
| 4 | `CP.BT.EVENT.NAME` | `CpBankTrigger_EventName` | TField | Yes | This field stores the Bank Event name associated to the bank trigger.This name is displayed in the Campaign Management User Agent Interface for the Marketing users. Validation Rules: Mandatory field, any 50 characters. |
| 5 | `CP.BT.BLOB` | `CpBankTrigger_Blob` |  |  |  |
| 6 | `CP.BT.STATUS.CODE` | `CpBankTrigger_StatusCode` | TField |  | This field stores the value of the field STATUS.CODE from CP.ENTITY.WORKFLOW table. Validation Rules: Any 100 characters. |
| 7 | `CP.BT.ORIGINAL.ID` | `CpBankTrigger_OriginalId` | TField |  | The solution allows versioning for BankTrigger.For every version of a BankTrigger we need to store the ID of the original one.This field stores the original ID of a BankTrigger. |
| 8 | `CP.BT.LAST.UPDATE` | `CpBankTrigger_LastUpdate` | TField |  | This field stores the date of the last comment made for this record. |
| 9 | `CP.BT.IS.VISIBLE` | `CpBankTrigger_IsVisible` | TField |  | This field stores "Y" or "N" values.This field indicates whether or not a bank trigger can be used for new campaigns. |
| 10 | `CP.BT.OWNER` | `CpBankTrigger_Owner` | TField |  | The user who defines the bank trigger Links to the ID of USER table |
| 11 | `CP.BT.SUSPEND.REASON.ID` | `CpBankTrigger_SuspendReasonId` | TField |  | This field stores the SUSPEND.REASON record ID. If this field has a SUSPEND.REASON ID -> the record has suspended values on it. It can't be used until they are approved or removed from the record. |
| 12 | `CP.BT.WORKFLOW.ID` | `CpBankTrigger_WorkflowId` | TField |  | This field stores the Workflow record ID. |
| 13 | `CP.BT.CUSTOMER.SOURCE` | `CpBankTrigger_CustomerSource` | TField |  | This field stores the source where a customer is registered: Internal (T24) or External (other core banking system) |
| 14 | `CP.BT.RESERVED.28` | `CpBankTrigger_Reserved28` | TField |  |  |
| 15 | `CP.BT.RESERVED.27` | `CpBankTrigger_Reserved27` | TField |  |  |
| 16 | `CP.BT.RESERVED.26` | `CpBankTrigger_Reserved26` | TField |  |  |
| 17 | `CP.BT.RESERVED.25` | `CpBankTrigger_Reserved25` | TField |  |  |
| 18 | `CP.BT.RESERVED.24` | `CpBankTrigger_Reserved24` | TField |  |  |
| 19 | `CP.BT.RESERVED.23` | `CpBankTrigger_Reserved23` | TField |  |  |
| 20 | `CP.BT.RESERVED.22` | `CpBankTrigger_Reserved22` | TField |  |  |
| 21 | `CP.BT.RESERVED.21` | `CpBankTrigger_Reserved21` | TField |  |  |
| 22 | `CP.BT.RESERVED.20` | `CpBankTrigger_Reserved20` | TField |  |  |
| 23 | `CP.BT.RESERVED.19` | `CpBankTrigger_Reserved19` | TField |  |  |
| 24 | `CP.BT.RESERVED.18` | `CpBankTrigger_Reserved18` | TField |  |  |
| 25 | `CP.BT.RESERVED.17` | `CpBankTrigger_Reserved17` | TField |  |  |
| 26 | `CP.BT.RESERVED.16` | `CpBankTrigger_Reserved16` | TField |  |  |
| 27 | `CP.BT.RESERVED.15` | `CpBankTrigger_Reserved15` | TField |  |  |
| 28 | `CP.BT.RESERVED.14` | `CpBankTrigger_Reserved14` | TField |  |  |
| 29 | `CP.BT.RESERVED.13` | `CpBankTrigger_Reserved13` | TField |  |  |
| 30 | `CP.BT.RESERVED.12` | `CpBankTrigger_Reserved12` | TField |  |  |
| 31 | `CP.BT.RESERVED.11` | `CpBankTrigger_Reserved11` | TField |  |  |
| 32 | `CP.BT.RESERVED.10` | `CpBankTrigger_Reserved10` | TField |  |  |
| 33 | `CP.BT.RESERVED.9` | `CpBankTrigger_Reserved9` | TField |  |  |
| 34 | `CP.BT.RESERVED.8` | `CpBankTrigger_Reserved8` | TField |  |  |
| 35 | `CP.BT.RESERVED.7` | `CpBankTrigger_Reserved7` | TField |  |  |
| 36 | `CP.BT.RESERVED.6` | `CpBankTrigger_Reserved6` | TField |  |  |
| 37 | `CP.BT.RESERVED.5` | `CpBankTrigger_Reserved5` | TField |  |  |
| 38 | `CP.BT.RESERVED.4` | `CpBankTrigger_Reserved4` | TField |  |  |
| 39 | `CP.BT.RESERVED.3` | `CpBankTrigger_Reserved3` | TField |  |  |
| 40 | `CP.BT.RESERVED.2` | `CpBankTrigger_Reserved2` | TField |  |  |
| 41 | `CP.BT.RESERVED.1` | `CpBankTrigger_Reserved1` | TField |  |  |
| 42 | `CP.BT.LOCAL.REF` | `CpBankTrigger_LocalRef` |  |  |  |
| 43 | `CP.BT.OVERRIDE` | `CpBankTrigger_Override` |  |  |  |
| 44 | `CP.BT.RECORD.STATUS` | `CpBankTrigger_RecordStatus` | String |  |  |
| 45 | `CP.BT.CURR.NO` | `CpBankTrigger_CurrNo` | String |  |  |
| 46 | `CP.BT.INPUTTER` | `CpBankTrigger_Inputter` |  |  |  |
| 47 | `CP.BT.DATE.TIME` | `CpBankTrigger_DateTime` |  |  |  |
| 48 | `CP.BT.AUTHORISER` | `CpBankTrigger_Authoriser` | String |  |  |
| 49 | `CP.BT.CO.CODE` | `CpBankTrigger_CoCode` | String |  |  |
| 50 | `CP.BT.DEPT.CODE` | `CpBankTrigger_DeptCode` | String |  |  |
| 51 | `CP.BT.AUDITOR.CODE` | `CpBankTrigger_AuditorCode` | String |  |  |
| 52 | `CP.BT.AUDIT.DATE.TIME` | `CpBankTrigger_AuditDateTime` | String |  |  |
