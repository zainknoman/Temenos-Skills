# DD.ITEM — Table Schema

> Source: `INSERTS/I_F.DD.ITEM` in `DD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.ITEM.DIRECTION` | `DdItem_Direction` | TField |  | Contains the Direction of the Claim. Defaults from the mandate which relates to this item (DD.DDI) |
| 2 | `DD.ITEM.MANDATE.REF` | `DdItem_MandateRef` | TField |  | This contains the underlying Mandate reference. When combining the DD.ITEM claims this field is used as part of the criteria for matching. |
| 3 | `DD.ITEM.ORIG.ENTRY.ID` | `DdItem_OrigEntryId` | TField |  | This is the forward Statement entry id through which the DD.ITEM was created. Other required details for this file such as Contract reference, Amount,Value date, Booking Date,Our reference, Their reference etc are taken from this Forward.entry. |
| 4 | `DD.ITEM.CREATE.DATE` | `DdItem_CreateDate` | TField |  | This is the date on which the DD.ITEM is created. ie. System.Date |
| 5 | `DD.ITEM.CONTRACT.REF` | `DdItem_ContractRef` | TField |  | This is the contract id which is linked to this DD.ITEM. The contract reference can be either MG id incase the DD.DDI is linked to MORTGAGE contract or DD.DDI id for standalone DD. |
| 6 | `DD.ITEM.ACCOUNT.NO` | `DdItem_AccountNo` | TField |  | This is the T24 account number for the mandate received and refers to the account where the claim amount to be credited. |
| 7 | `DD.ITEM.CURRENCY` | `DdItem_Currency` | TField |  | Contains the Currency of the Account. |
| 8 | `DD.ITEM.AMOUNT` | `DdItem_Amount` | TField |  | This has the Direct Debit Claim amount and this has to be mapped to outward claim file for the amount to be claimed. This amount is updated from the STMT.ENTRY local currency amount for which the DD.ITEM is created. |
| 9 | `DD.ITEM.THEIR.REFERENCE` | `DdItem_TheirReference` | TField |  | Their reference as available in the forward STMT.ENTRY is populated here. |
| 10 | `DD.ITEM.OUR.REFERENCE` | `DdItem_OurReference` | TField |  | Our reference as available in the STMT.ENTRY is updated here. |
| 11 | `DD.ITEM.ACCOUNT.OFFICER` | `DdItem_AccountOfficer` | TField |  | Account Officer populated in STMT.ENTRY is defaulted here. |
| 12 | `DD.ITEM.VALUE.DATE` | `DdItem_ValueDate` | TField |  | This contains the value date of the claim or the date on which the amount to be claimed. This is updated from the value date as available in STMT.ENTRY. Number of days as given in Claim.Date.Prd is deducted from this value date to determine the file generation date and file is generated on that day with the file date as this Value date. The claim accounting will be raised on this value date. |
| 13 | `DD.ITEM.BOOKING.DATE` | `DdItem_BookingDate` | TField |  | The is the date on which the STMT.ENTRY is created. |
| 14 | `DD.ITEM.CLAIM.DATE` | `DdItem_ClaimDate` | TField |  | Claim accounting is generated on the value date and this contains the date on which the claim entry is raised. |
| 15 | `DD.ITEM.CURRENCY.MARKET` | `DdItem_CurrencyMarket` | TField |  | The Currency market as available in the STMT.ENTRY is updated here. |
| 16 | `DD.ITEM.ORIG.DD.ITEM.ID` | `DdItem_OrigDdItemId` | TField |  | When a DD.ITEM is resubmitted, the new DD.ITEM created will have the original DD.ITEM reference id recorded here. |
| 17 | `DD.ITEM.RESUB.DD.ID` | `DdItem_ResubDdId` |  |  |  |
| 18 | `DD.ITEM.REASON.CODE` | `DdItem_ReasonCode` | TField |  | Reason code as applicable for the Status is updated here. The reason codes is defaulted from DD.REASON.CODES as applicable for the Status and Clearing system is defaulted here. |
| 19 | `DD.ITEM.STATUS` | `DdItem_Status` | TField |  | The status related to DD.ITEM which can only be updated by the System. |
| 20 | `DD.ITEM.STATUS.HIST` | `DdItem_StatusHist` |  |  |  |
| 21 | `DD.ITEM.STATUS.DATE` | `DdItem_StatusDate` |  |  |  |
| 22 | `DD.ITEM.MATURE.DATE` | `DdItem_MatureDate` | TField |  | Date on which the last claim is made, taken from the mandate (DD.DDI) when processing the last item. |
| 23 | `DD.ITEM.OUTPUT.REC.ID` | `DdItem_OutputRecId` | TField |  | The id of the claim fiel that this DD.ITEM has been included in. |
| 24 | `DD.ITEM.PARAM.ID` | `DdItem_ParamId` | TField |  | The id of the DD.PARAMETER which was used in the creation process of this record. |
| 25 | `DD.ITEM.REASON.CODE.ID` | `DdItem_ReasonCodeId` | TField |  | The record id of the DD.REASON.CODES which is used to provide enrichment for the REASON.CODE field since the codes themselves are usually too brief to enable a visual understanding of their meaning. |
| 26 | `DD.ITEM.REQUEST.TYPE` | `DdItem_RequestType` | TField |  | This field will have the value as INTERNAL, when a DD.ITEM is created for an internal DD.DDI. That is, when the REQUEST.TYPE field in DD.DDI is INTERNAL. No Input field. Update by System. |
| 27 | `DD.ITEM.SUSP.FT.ID` | `DdItem_SuspFtId` | TField |  | This field holds the ID of the FT, which is generated during the suspense processing on CLAIM date. No Input field. Update by System. |
| 28 | `DD.ITEM.AMEND.INDICATOR` | `DdItem_AmendIndicator` | TField |  |  |
| 29 | `DD.ITEM.RESUBMIT.NO` | `DdItem_ResubmitNo` | TField |  | This will store the resubmit counter where : 0 - will indicate a new DD Collection 1 - collection has been resubmitted once 2 - collection has been resubmitted twice etc.. |
| 30 | `DD.ITEM.MANDATE.VER.NO` | `DdItem_MandateVerNo` | TField |  | This will be populated with the DD.DDI version number. This will be used when displaying the DD Collection details to user having in mind that the DD.DDI can be amended during the life of the mandate. |
| 31 | `DD.ITEM.DELIVERY.REF.ID` | `DdItem_DeliveryRefId` |  |  |  |
| 32 | `DD.ITEM.BULK.REFERENCE.VALUE` | `DdItem_BulkReferenceValue` |  |  |  |
| 33 | `DD.ITEM.SEQUENCE` | `DdItem_Sequence` | TField |  | This will indicate the sequence of the DD collection and will be set by core to FRST or RCUR LAST will only be set for standalone mandates when they reach the termination date ( if not cancelled before). The Sequence Determination Routine can be used by L2/L3 layer to update the value populated by core in order to accommodate with clearing/customer requirements.Noinput field, updated by system. |
| 34 | `DD.ITEM.REPRESENT.FLG` | `DdItem_RepresentationFlag` |  |  |  |
| 35 | `DD.ITEM.TPH.REFERENCE` | `DdItem_TphReference` | TField |  | To update the TPH reference in which the DD collection message was mapped. If the OUTWARD.FORAMT is TPH only this field will get updated. |
| 36 | `DD.ITEM.COMBINE.FLAG` | `DdItem_CombineFlag` | TField |  | The values which indicates the respective DD.ITEM is Combined or individual items. 1. CombinedItem - means the item is individual one. 2. CombinedBulk - means the item contains bulk to process the files. |
| 37 | `DD.ITEM.RELATED.COMBINED.ITEMS` | `DdItem_RelatedCombiedItems` |  |  |  |
| 38 | `DD.ITEM.COMBINED.BULK.REF` | `DdItem_CombinedBulkRef` | TField |  | The fields combined bulk reference Id. |
| 39 | `DD.ITEM.CONTRACT.REFERENCE` | `DdItem_ContractReference` |  |  |  |
| 40 | `DD.ITEM.RESERVED01` | `DdItem_Reserved01` | TField |  |  |
| 41 | `DD.ITEM.STMT.NOS` | `DdItem_StmtNos` |  |  |  |
| 42 | `DD.ITEM.OVERRIDE` | `DdItem_Override` |  |  |  |
