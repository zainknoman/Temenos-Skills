# ST.CUSTOMER.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.ST.CUSTOMER.ACTIVITY` in `ST_CustomerActivity.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.CA.CUSTOMER.START.DATE` | `StCustomerActivity_CustomerStartDate` | TField |  | Date Customer was created |
| 2 | `ST.CA.RESERVED1` | `StCustomerActivity_Reserved1` | TField |  |  |
| 3 | `ST.CA.RESERVED2` | `StCustomerActivity_Reserved2` | TField |  |  |
| 4 | `ST.CA.ACTIVE.CONTRACT.APPLN` | `StCustomerActivity_ActiveContractAppln` |  |  |  |
| 5 | `ST.CA.ACTIVE.CONTRACT.ID` | `StCustomerActivity_ActiveContractId` |  |  |  |
| 6 | `ST.CA.ACTIVE.CONTRACT.CO.CODE` | `StCustomerActivity_ActiveContractCoCode` |  |  |  |
| 7 | `ST.CA.CONTRACT.CREATION.DATE` | `StCustomerActivity_ContractCreationDate` |  |  |  |
| 8 | `ST.CA.ACTIVE.CONTRACT.LINK` | `StCustomerActivity_ActiveContractLink` |  |  |  |
| 9 | `ST.CA.ACTIVE.CONTRACT.CATEG` | `StCustomerActivity_ActiveContractCateg` |  |  |  |
| 10 | `ST.CA.ACT.RESERVED.09` | `StCustomerActivity_ActReserved09` |  |  |  |
| 11 | `ST.CA.ACT.RESERVED.08` | `StCustomerActivity_ActReserved08` |  |  |  |
| 12 | `ST.CA.ACT.RESERVED.07` | `StCustomerActivity_ActReserved07` |  |  |  |
| 13 | `ST.CA.ACT.RESERVED.06` | `StCustomerActivity_ActReserved06` |  |  |  |
| 14 | `ST.CA.ACT.RESERVED.05` | `StCustomerActivity_ActReserved05` |  |  |  |
| 15 | `ST.CA.ACT.RESERVED.04` | `StCustomerActivity_ActReserved04` |  |  |  |
| 16 | `ST.CA.ACT.RESERVED.03` | `StCustomerActivity_ActReserved03` |  |  |  |
| 17 | `ST.CA.ACT.RESERVED.02` | `StCustomerActivity_ActReserved02` |  |  |  |
| 18 | `ST.CA.ACT.RESERVED.01` | `StCustomerActivity_ActReserved01` |  |  |  |
| 19 | `ST.CA.COMPLETED.CONTRACT.APPLN` | `StCustomerActivity_CompletedContractAppln` |  |  |  |
| 20 | `ST.CA.COMPLETED.CONTRACT.ID` | `StCustomerActivity_CompletedContractId` |  |  |  |
| 21 | `ST.CA.COMPLETED.CONTRACT.CO.CODE` | `StCustomerActivity_CompletedContractCoCode` |  |  |  |
| 22 | `ST.CA.CONTRACT.END.DATE` | `StCustomerActivity_ContractEndDate` |  |  |  |
| 23 | `ST.CA.COMPLETE.CONTRACT.LINK` | `StCustomerActivity_CompleteContractLink` |  |  |  |
| 24 | `ST.CA.CONTRACT.ERASURE.DETAILS` | `StCustomerActivity_ContractErasureDetails` |  |  |  |
| 25 | `ST.CA.COMPLETED.CONTRACT.CATEG` | `StCustomerActivity_CompletedContractCateg` |  |  |  |
| 26 | `ST.CA.COM.RESERVED.08` | `StCustomerActivity_ComReserved08` |  |  |  |
| 27 | `ST.CA.COM.RESERVED.07` | `StCustomerActivity_ComReserved07` |  |  |  |
| 28 | `ST.CA.COM.RESERVED.06` | `StCustomerActivity_ComReserved06` |  |  |  |
| 29 | `ST.CA.COM.RESERVED.05` | `StCustomerActivity_ComReserved05` |  |  |  |
| 30 | `ST.CA.COM.RESERVED.04` | `StCustomerActivity_ComReserved04` |  |  |  |
| 31 | `ST.CA.COM.RESERVED.03` | `StCustomerActivity_ComReserved03` |  |  |  |
| 32 | `ST.CA.COM.RESERVED.02` | `StCustomerActivity_ComReserved02` |  |  |  |
| 33 | `ST.CA.COM.RESERVED.01` | `StCustomerActivity_ComReserved01` |  |  |  |
| 34 | `ST.CA.OTHER.LINKED.APPLN` | `StCustomerActivity_OtherLinkedAppln` |  |  |  |
| 35 | `ST.CA.OTHER.LINKED.RECORD` | `StCustomerActivity_OtherLinkedRecord` |  |  |  |
| 36 | `ST.CA.OTHER.LINKED.CO.CODE` | `StCustomerActivity_OtherLinkedCoCode` |  |  |  |
| 37 | `ST.CA.OTHER.LINKED.REC.STATUS` | `StCustomerActivity_OtherLinkedRecStatus` |  |  |  |
| 38 | `ST.CA.OTR.LINKED.CONT.ERASURE.DETS` | `StCustomerActivity_OtrLinkedContErasureDets` |  |  |  |
| 39 | `ST.CA.OTR.RESERVED.09` | `StCustomerActivity_OtrReserved09` |  |  |  |
| 40 | `ST.CA.OTR.RESERVED.08` | `StCustomerActivity_OtrReserved08` |  |  |  |
| 41 | `ST.CA.OTR.RESERVED.07` | `StCustomerActivity_OtrReserved07` |  |  |  |
| 42 | `ST.CA.OTR.RESERVED.06` | `StCustomerActivity_OtrReserved06` |  |  |  |
| 43 | `ST.CA.OTR.RESERVED.05` | `StCustomerActivity_OtrReserved05` |  |  |  |
| 44 | `ST.CA.OTR.RESERVED.04` | `StCustomerActivity_OtrReserved04` |  |  |  |
| 45 | `ST.CA.OTR.RESERVED.03` | `StCustomerActivity_OtrReserved03` |  |  |  |
| 46 | `ST.CA.OTR.RESERVED.02` | `StCustomerActivity_OtrReserved02` |  |  |  |
| 47 | `ST.CA.OTR.RESERVED.01` | `StCustomerActivity_OtrReserved01` |  |  |  |
| 48 | `ST.CA.PDD.TAKEOVER.DATE` | `StCustomerActivity_PddTakeoverDate` | TField |  | This will be updated by the takeover process and will be used for back patching to update the Customer Activity |
| 49 | `ST.CA.REC.SPLIT` | `StCustomerActivity_RecSplit` | TField |  | To record the number of splits for the master record if more than 100 contracts |
| 50 | `ST.CA.DELINK.CONT.APPLN` | `StCustomerActivity_DelinkContAppln` |  |  |  |
| 51 | `ST.CA.DELINK.CONT.ID` | `StCustomerActivity_DelinkContId` |  |  |  |
| 52 | `ST.CA.DELINK.CONT.CO.CODE` | `StCustomerActivity_DelinkContCoCode` |  |  |  |
| 53 | `ST.CA.DELINK.CONT.START.DATE` | `StCustomerActivity_DelinkStartDate` |  |  |  |
| 54 | `ST.CA.DELINK.CONT.END.DATE` | `StCustomerActivity_DelinkEndDate` |  |  |  |
| 55 | `ST.CA.DELINK.CONT.LINK` | `StCustomerActivity_DelinkContLink` |  |  |  |
| 56 | `ST.CA.DELINK.CONT.CATEG` | `StCustomerActivity_DelinkContCateg` |  |  |  |
| 57 | `ST.CA.DELINK.RESERVED.01` | `StCustomerActivity_DelinkReserved01` |  |  |  |
| 58 | `ST.CA.RESERVED.03` | `StCustomerActivity_Reserved03` | TField |  |  |
| 59 | `ST.CA.RESERVED.02` | `StCustomerActivity_Reserved02` | TField |  |  |
| 60 | `ST.CA.RESERVED.01` | `StCustomerActivity_Reserved01` | TField |  |  |
