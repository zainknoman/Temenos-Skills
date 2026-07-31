# DD.RETURN — Table Schema

> Source: `INSERTS/I_F.DD.RETURN` in `DD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.RET.DD.ITEM.ID` | `DdReturn_DdItemId` | TField | Yes | Give the DD.ITEM id which should be Returned / Resubmitted. It must be an Item for which the funds have already been received. The STMT.ENTRY will be raised with the details as applicable for this ITEM. Validation Rules: Must be a record in DD.ITEM with status as 'CLAIMED.ITEM' Mandatory Field This is a No change field |
| 2 | `DD.RET.RET.REASON` | `DdReturn_RetReason` |  |  |  |
| 3 | `DD.RET.CLAIM.CONTENT` | `DdReturn_ClaimContent` |  |  |  |
| 4 | `DD.RET.RESUB.VAL.DATE` | `DdReturn_ResubValDate` | TField | Conditional | Specify the value date on which the DD.ITEM has to be resubmitted and same is used as the value date for the resubmit accounting. If the STATUS is blank , then the value of this field will default to Current Date + RESUB.DATE.PRD + CLAIM.DATE.PRD (both from DD.PARAMETER) The above defaulting will happen only when the RESUB.DATE.PRD field in DD.PARAMETER is input with valid value. To stop above defaulting mechanism even when RESUB.DATE.PRD is specified- set the DD.RESUBMIT as 'N' In case a user wishes to input his own value date for resubmission then he may do so after considering the setup of the clearing cycle in DD.PARAMETER. Ideally, the date given here must be greater than the current date + CLAIM.DATE.PRD field in DD.PARAMETER. Validation Rules: If DD.RESUBMIT is blank, this field is mandatory otherwise Optional If entered it must be greater than the current date. Up to 9 date characters (standard Date format) - type D |
| 5 | `DD.RET.CREATE.DATE` | `DdReturn_CreateDate` | TField |  | Date of creation of the DD.RETURN record is stored here Validation Rules: No input allowed Updated by System. |
| 6 | `DD.RET.STATUS` | `DdReturn_Status` | TField |  | Contains the status of the DD.RETURN record. When a DD.ITEM is returned without specifying the resubmission value date then the status is updated as "RETURNED.ITEM'. This record can be modified again for resubmission by giving the Resubmit value date. In case DD.ITEM is given along with resubmission value date, then the status is updated as "PROCESSED.ITEM". When status is set to "PROCESSED.ITEM", then changes are not allowed for this record. When a cancel Flag is set internally, And If DD.ITEM is in CLAIMSENT.ITEM status,then status of DD.RETURN would be updated as CANCEL.ITEM and respective DD.ITEM status would be marked as CONFIRMED.CANCELLED.ITEM. If DD.ITEM is in CLAIMED.ITEM status, then status of both DD.RETURN and DD.ITEM would be updated as RETURNED.ITEM. Validation Rules: No input field. Updated by the System either "RETURNED.ITEM' or 'PROCESSED.ITEM' or 'CANCEL.ITEM' |
| 7 | `DD.RET.STATUS.HIST` | `DdReturn_StatusHist` |  |  |  |
| 8 | `DD.RET.STATUS.DATE` | `DdReturn_StatusDate` |  |  |  |
| 9 | `DD.RET.DD.RESUBMIT` | `DdReturn_DdResubmit` | TField | Conditional | To stop defaulting RESUB.VAL.DATE field even when RESUB.DATE.PRD is specified in DD.PARAMEMTER- set this field as N. If the user does not wish to resubmit the item irrespective of presence or absence of the field RESUB.VAL.DATE, then this field should be set to 'N'. In such cases. STATUS of DD.RETURN shall be RETURNED.ITEM only. If blank, resubmission entries shall be raised and the DD.RETURN status will be updated to PROCESSED.ITEM. Validation Rules: Optional field- Valid values N or Null If blank, then resubmission entries will be raised and hence RESUB.VAL.DATE is mandatory. If the value is 'N' , then RESUB.VAL.DATE is Optional. |
| 10 | `DD.RET.REASON.CODE` | `DdReturn_ReasonCode` | TField | No | The actual reason code for the direct debit system rejection. Validation Rules: Optional Field |
| 11 | `DD.RET.LOCAL.REF` | `DdReturn_LocalRef` |  |  |  |
| 12 | `DD.RET.BULK.REFERENCE` | `DdReturn_BulkReference` | TField |  | This will be the Message Id of the pain.002 transaction. Validation Rules: 1-35 Alphanumeric character's |
| 13 | `DD.RET.REFUND.ORG.NAME` | `DdReturn_RefundOrgName` | TField |  | It Will store the Refund Originator Name which will identify that pain.002 is received following a Refund. Validation Rules: 1-70 Alphanumeric character's |
| 14 | `DD.RET.REPRESENT.FLG` | `DdReturn_RepresentationFlag` |  |  |  |
| 15 | `DD.RET.INT.REJECT` | `DdReturn_InternalReject` |  |  |  |
| 16 | `DD.RET.COMBINED.BULK.DD.RET` | `DdReturn_CombinedBulkDdRet` | TField |  | The field contains original DD.RETURN id with combined Bulk items. |
| 17 | `DD.RET.ERROR.REASON` | `DdReturn_ErrorReason` | TField |  | This fields contains the error message raised, while the bulk Item return process. |
| 18 | `DD.RET.CANCEL.FLAG` | `DdReturn_CancelFlag` | TField |  | Flag to mention whether to CANCEL the collection or not Yes - will indicate the DD.ITEM indicated in the DD.RETURN must be cancelled. Blank - indicates the DD.ITEM is rejected/returned (current functionality) |
| 19 | `DD.RET.STMT.NOS` | `DdReturn_StmtNos` |  |  |  |
| 20 | `DD.RET.OVERRIDE` | `DdReturn_Override` |  |  |  |
| 21 | `DD.RET.RECORD.STATUS` | `DdReturn_RecordStatus` | String |  |  |
| 22 | `DD.RET.CURR.NO` | `DdReturn_CurrNo` | String |  |  |
| 23 | `DD.RET.INPUTTER` | `DdReturn_Inputter` |  |  |  |
| 24 | `DD.RET.DATE.TIME` | `DdReturn_DateTime` |  |  |  |
| 25 | `DD.RET.AUTHORISER` | `DdReturn_Authoriser` | String |  |  |
| 26 | `DD.RET.CO.CODE` | `DdReturn_CoCode` | String |  |  |
| 27 | `DD.RET.DEPT.CODE` | `DdReturn_DeptCode` | String |  |  |
| 28 | `DD.RET.AUDITOR.CODE` | `DdReturn_AuditorCode` | String |  |  |
| 29 | `DD.RET.AUDIT.DATE.TIME` | `DdReturn_AuditDateTime` | String |  |  |
