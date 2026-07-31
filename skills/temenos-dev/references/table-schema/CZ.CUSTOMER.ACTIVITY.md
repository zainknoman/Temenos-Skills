# CZ.CUSTOMER.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.CZ.CUSTOMER.ACTIVITY` in `CZ_CustomerActivity.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CA.CUSTOMER.START.DATE` | `CzCustomerActivity_CustomerStartDate` | TField |  | Date Customer was created |
| 2 | `CA.CUSTOMER.ACTIVITY.STATUS` | `CzCustomerActivity_CustomerActivityStatus` | TField |  | The status of the Customer Allowed values are ACTIVE,INACTIVE,ERASURE.IN.PROGRESS,ERASED Active: when there are still active contracts for customer Inactive: When all contracts for customer are completed Erasure in Progress: When customer is inactive and erasure process has started but not personal data has been erased Erased: When all personal data for customer has been erased Awtng.Ext.Status: When customer is inactive and is waiting for external system's response |
| 3 | `CA.INACTIVE.SINCE.DATE` | `CzCustomerActivity_InactiveSinceDate` | TField |  | Date on which Customer became inactive |
| 4 | `CA.ACTIVE.CONTRACT.APPLN` | `CzCustomerActivity_ActiveContractAppln` |  |  |  |
| 5 | `CA.ACTIVE.CONTRACT.ID` | `CzCustomerActivity_ActiveContractId` |  |  |  |
| 6 | `CA.ACTIVE.CONTRACT.CO.CODE` | `CzCustomerActivity_ActiveContractCoCode` |  |  |  |
| 7 | `CA.CONTRACT.CREATION.DATE` | `CzCustomerActivity_ContractCreationDate` |  |  |  |
| 8 | `CA.ACTIVE.CONTRACT.LINK` | `CzCustomerActivity_ActiveContractLink` |  |  |  |
| 9 | `CA.ACT.RESERVED.05` | `CzCustomerActivity_ActReserved05` |  |  |  |
| 10 | `CA.ACT.RESERVED.04` | `CzCustomerActivity_ActReserved04` |  |  |  |
| 11 | `CA.ACT.RESERVED.03` | `CzCustomerActivity_ActReserved03` |  |  |  |
| 12 | `CA.ACT.RESERVED.02` | `CzCustomerActivity_ActReserved02` |  |  |  |
| 13 | `CA.ACT.RESERVED.01` | `CzCustomerActivity_ActReserved01` |  |  |  |
| 14 | `CA.COMPLETED.CONTRACT.APPLN` | `CzCustomerActivity_CompletedContractAppln` |  |  |  |
| 15 | `CA.COMPLETED.CONTRACT.ID` | `CzCustomerActivity_CompletedContractId` |  |  |  |
| 16 | `CA.COMPLETED.CONTRACT.CO.CODE` | `CzCustomerActivity_CompletedContractCoCode` |  |  |  |
| 17 | `CA.CONTRACT.END.DATE` | `CzCustomerActivity_ContractEndDate` |  |  |  |
| 18 | `CA.COMPLETE.CONTRACT.LINK` | `CzCustomerActivity_CompleteContractLink` |  |  |  |
| 19 | `CA.CONTRACT.ERASURE.DETAILS` | `CzCustomerActivity_ContractErasureDetails` |  |  |  |
| 20 | `CA.COM.RESERVED.04` | `CzCustomerActivity_ComReserved04` |  |  |  |
| 21 | `CA.COM.RESERVED.03` | `CzCustomerActivity_ComReserved03` |  |  |  |
| 22 | `CA.COM.RESERVED.02` | `CzCustomerActivity_ComReserved02` |  |  |  |
| 23 | `CA.COM.RESERVED.01` | `CzCustomerActivity_ComReserved01` |  |  |  |
| 24 | `CA.OTHER.LINKED.APPLN` | `CzCustomerActivity_OtherLinkedAppln` |  |  |  |
| 25 | `CA.OTHER.LINKED.RECORD` | `CzCustomerActivity_OtherLinkedRecord` |  |  |  |
| 26 | `CA.OTHER.LINKED.CO.CODE` | `CzCustomerActivity_OtherLinkedCoCode` |  |  |  |
| 27 | `CA.OTHER.LINKED.REC.STATUS` | `CzCustomerActivity_OtherLinkedRecStatus` |  |  |  |
| 28 | `CA.OTR.LINKED.CONT.ERASURE.DETS` | `CzCustomerActivity_OtrLinkedContErasureDets` |  |  |  |
| 29 | `CA.CDP.ELIGIBLE` | `CzCustomerActivity_CdpEligible` | TField |  | Allowed values are YES/NO/BLANK. Yes indicates customer qualified for Customer Data Protection. No / Null indicates means customer is not qualified for Customer Data Protection. This value is updated by the system everytime when a Customer/party application record is authorised and it requires the service ST.BUILD.CUS.ACTIVITY to be running in parallel. If the CDP eligibility condition defined in CZ.CDP.PARAMETER is met, the Customer is marked as YES otherwise as NO. |
| 30 | `CA.DO.NOT.ERASE` | `CzCustomerActivity_DoNotErase` | TField |  | It will be checked by the Erasure process to ignore data erasure if set to YES This will be updated by the CUSTOMER.ACTIVITY.CAPTURE application Allowed values are YES/NO/BLANK Yes indicates do not erase the customer record No indicates customer record may be erased |
| 31 | `CA.ERASE.COMMENTS` | `CzCustomerActivity_EraseComments` |  |  |  |
| 32 | `CA.EXTERNAL.EOR.DATE` | `CzCustomerActivity_ExternalEorDate` | TField |  | It will be used to determine if a customer is Active, even if all contracts in T24 are completed the customer becomes INACTIVE, only when the EXTERNAL.EOR.DATE is passed Input field by user, must be date format. Field is to hold the oldest maturity date of external contracts This will be updated by the CUSTOMER.ACTIVITY.CAPTURE application |
| 33 | `CA.PURPOSE` | `CzCustomerActivity_Purpose` |  |  |  |
| 34 | `CA.ERASURE.DATE` | `CzCustomerActivity_ErasureDate` |  |  |  |
| 35 | `CA.ERASURE.STATUS` | `CzCustomerActivity_ErasureStatus` |  |  |  |
| 36 | `CA.RET.PERIOD.USED` | `CzCustomerActivity_RetPeriodUsed` |  |  |  |
| 37 | `CA.PUR.RESERVED.05` | `CzCustomerActivity_PurReserved05` |  |  |  |
| 38 | `CA.PUR.RESERVED.04` | `CzCustomerActivity_PurReserved04` |  |  |  |
| 39 | `CA.PUR.RESERVED.03` | `CzCustomerActivity_PurReserved03` |  |  |  |
| 40 | `CA.PUR.RESERVED.02` | `CzCustomerActivity_PurReserved02` |  |  |  |
| 41 | `CA.PUR.RESERVED.01` | `CzCustomerActivity_PurReserved01` |  |  |  |
| 42 | `CA.PDD.TAKEOVER.DATE` | `CzCustomerActivity_PddTakeoverDate` | TField |  | This will be updated by the takeover process and will be used for back patching to update the Customer Activity |
| 43 | `CA.REC.SPLIT` | `CzCustomerActivity_RecSplit` | TField |  | To record the number of splits for the master record if more than 100 contracts |
| 44 | `CA.ACTIVITY.MOVED` | `CzCustomerActivity_ActivityMoved` | TField |  | This will be updated when the CZ customer activity related informations are moved to ST Customer Activity. When the field value is YES, the customer activity informations are moved to ST customer activity table. |
| 45 | `CA.DELINK.CONT.APPLN` | `CzCustomerActivity_DelinkContAppln` |  |  |  |
| 46 | `CA.DELINK.CONT.ID` | `CzCustomerActivity_DelinkContId` |  |  |  |
| 47 | `CA.DELINK.CONT.CO.CODE` | `CzCustomerActivity_DelinkContCoCode` |  |  |  |
| 48 | `CA.DELINK.CONT.START.DATE` | `CzCustomerActivity_DelinkContStartDate` |  |  |  |
| 49 | `CA.DELINK.CONT.END.DATE` | `CzCustomerActivity_DelinkContEndDate` |  |  |  |
| 50 | `CA.DELINK.CONT.LINK` | `CzCustomerActivity_DelinkContLink` |  |  |  |
| 51 | `CA.DELINK.RESERVED.02` | `CzCustomerActivity_DelinkReserved02` |  |  |  |
| 52 | `CA.DELINK.RESERVED.01` | `CzCustomerActivity_DelinkReserved01` |  |  |  |
| 53 | `CA.RESERVED.02` | `CzCustomerActivity_Reserved02` | TField |  |  |
| 54 | `CA.RESERVED.01` | `CzCustomerActivity_Reserved01` | TField |  |  |
