# CZ.CUSTOMER.ACTIVITY.CAPTURE — Table Schema

> Source: `INSERTS/I_F.CZ.CUSTOMER.ACTIVITY.CAPTURE` in `CZ_CustomerActivity.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAC.PARTY.ID` | `CzCustomerActivityCapture_PartyId` | TField |  | Valid Id to the application mentioned in PARTY.APPLICATION field |
| 2 | `CAC.PARTY.APPLICATION` | `CzCustomerActivityCapture_PartyApplication` | TField | Yes | Defines the party application to which the party Id belongs to. The field is defaulted with a value of CUSTOMER. In higher releases where Customer activity and CDP processing functionality enhanced for PERSON.ENTITY as well, the field is allowed input with options CUSTOMER or PERSON.ENTITY. It is mandatory that for a proper processing, user must ensure that this field is set with the appropriate party application relevant to the application being configured Options field |
| 3 | `CAC.DO.NOT.ERASE` | `CzCustomerActivityCapture_DoNotErase` | TField |  | It will be checked by the Erasure process to ignore data erasure if set to YES Allowed values are YES/NO/BLANK Yes indicates do not erase the customer record No indicates customer record may be erased |
| 4 | `CAC.ERASE.COMMENTS` | `CzCustomerActivityCapture_EraseComments` |  |  |  |
| 5 | `CAC.EXTERNAL.EOR.DATE` | `CzCustomerActivityCapture_ExternalEorDate` | TField |  | The field is used to capture the External End Of Relationship date for a Customer. If a Customer has active contracts outside Transact and if the Customer data has to be retained until that EOR date then this field shall be used. Even if all the contracts for a Customer within Transact is marked completed and if there is an EOR date, then the customer will be marked as ACTIVE until the EOR date is passed. There is no flag as such to remove an existing EOR date from CZ.CUSTOMER.ACTIVITY and hence if you want to remove the EOR date and mark the customer as inactive, a back dated capture can be input which will overwrite the existing EOR date and initiate the inactivity and therefore the CDP erasure processing for the Customer. Validation Rules: The field accepts a valid date |
| 6 | `CAC.EXT.SYSTEM` | `CzCustomerActivityCapture_ExtSystem` |  |  |  |
| 7 | `CAC.EXT.STATUS` | `CzCustomerActivityCapture_ExtStatus` |  |  |  |
| 8 | `CAC.EXT.RESERVED.04` | `CzCustomerActivityCapture_ExtReserved04` |  |  |  |
| 9 | `CAC.EXT.RESERVED.03` | `CzCustomerActivityCapture_ExtReserved03` |  |  |  |
| 10 | `CAC.EXT.RESERVED.02` | `CzCustomerActivityCapture_ExtReserved02` |  |  |  |
| 11 | `CAC.EXT.RESERVED.01` | `CzCustomerActivityCapture_ExtReserved01` |  |  |  |
| 12 | `CAC.CUST.STATUS.RECHECK` | `CzCustomerActivityCapture_CustStatusRecheck` | TField |  | Field to indicate that the CZ.CUSTOMER.ACTIVITY.CAPTURE is created to re-check the customer status in external systems before starting the erasure process. Manual input of this field is not allowed. |
| 13 | `CAC.RESERVED.04` | `CzCustomerActivityCapture_Reserved04` | TField |  |  |
| 14 | `CAC.RESERVED.03` | `CzCustomerActivityCapture_Reserved03` | TField |  |  |
| 15 | `CAC.RESERVED.02` | `CzCustomerActivityCapture_Reserved02` | TField |  |  |
| 16 | `CAC.RESERVED.01` | `CzCustomerActivityCapture_Reserved01` | TField |  |  |
| 17 | `CAC.LOCAL.REF` | `CzCustomerActivityCapture_LocalRef` |  |  |  |
| 18 | `CAC.RECORD.STATUS` | `CzCustomerActivityCapture_RecordStatus` | String |  |  |
| 19 | `CAC.CURR.NO` | `CzCustomerActivityCapture_CurrNo` | String |  |  |
| 20 | `CAC.INPUTTER` | `CzCustomerActivityCapture_Inputter` |  |  |  |
| 21 | `CAC.DATE.TIME` | `CzCustomerActivityCapture_DateTime` |  |  |  |
| 22 | `CAC.AUTHORISER` | `CzCustomerActivityCapture_Authoriser` | String |  |  |
| 23 | `CAC.CO.CODE` | `CzCustomerActivityCapture_CoCode` | String |  |  |
| 24 | `CAC.DEPT.CODE` | `CzCustomerActivityCapture_DeptCode` | String |  |  |
| 25 | `CAC.AUDITOR.CODE` | `CzCustomerActivityCapture_AuditorCode` | String |  |  |
| 26 | `CAC.AUDIT.DATE.TIME` | `CzCustomerActivityCapture_AuditDateTime` | String |  |  |
