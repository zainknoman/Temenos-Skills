# BL.BATCH — Table Schema

> Source: `INSERTS/I_F.BL.BATCH` in `BL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BL.BAT.DESCRIPTION` | `BlBatch_Description` |  |  |  |
| 2 | `BL.BAT.BILL.REG.ID` | `BlBatch_BillRegId` |  |  |  |
| 3 | `BL.BAT.BILL.BAT.ID` | `BlBatch_BillBatId` |  |  |  |
| 4 | `BL.BAT.BA.BL.REG.ID` | `BlBatch_BaBlRegId` |  |  |  |
| 5 | `BL.BAT.NO.OF.BILLS` | `BlBatch_NoOfBills` | TField |  | This is a no input field. This field is automatically updated with the number of bills attached to this batch when the Batch is committed. Validation Rules: Numeric |
| 6 | `BL.BAT.CURRENCY` | `BlBatch_Currency` |  |  |  |
| 7 | `BL.BAT.AMOUNT` | `BlBatch_Amount` |  |  |  |
| 8 | `BL.BAT.CHG.CODE` | `BlBatch_ChgCode` |  |  |  |
| 9 | `BL.BAT.CHG.CCY` | `BlBatch_ChgCcy` |  |  |  |
| 10 | `BL.BAT.CHG.AMT` | `BlBatch_ChgAmt` |  |  |  |
| 11 | `BL.BAT.LINKED.BB.ID` | `BlBatch_LinkedBbId` | TField |  | For future use |
| 12 | `BL.BAT.TRANS.REF` | `BlBatch_TransRef` |  |  |  |
| 13 | `BL.BAT.USR.STATUS` | `BlBatch_UsrStatus` | TField |  | The status of the Batch as given by the User defined in BL.STATUS application. For example 1.Received by the Customer 2.Sent to Head Office 3. Received at Head Office 4.Sent to Domicile branch If the status number is mentioned in this column, a Report on the Status of all bills with similar status or different statuses shall be generated. This will help tracking the movement of the Bill. Validation Rules: (1-8) Numeric Characters. Once keyed in, the enrichment as defined in BL.STATUS appears |
| 14 | `BL.BAT.BATCH.DATE` | `BlBatch_BatchDate` | TField |  | The date on which the status of the Bill is updated by the user. Default would be the current business date. Validation Rules: Standard T24 date format |
| 15 | `BL.BAT.SYS.STATUS` | `BlBatch_SysStatus` | TField |  | This is a No Input field. Updated based on the system status of BL.BATCH Validation Rules: Valid value "CUR" or "MAT" |
| 16 | `BL.BAT.MAX.AVAIL.AMT` | `BlBatch_MaxAvailAmt` | TField |  | This field specifies the sum of all maximum available amounts BL.REGISTERs for disbursement in a BL.BATCH record.Maximum amount available for disbursement will be calculated as MAX.AVAIL.AMT = AMOUNT(of BL.REGISTER) � (AMOUNT * RET.MARGIN/100) This field denotes maximum amount that can be disbursed out of a BL.BATCH record. It is the sum of all MAX.AVAIL.AMOUNT of all BL.REGISTER records attached in the batch Validation Rules: System maintained field Standard T24 Amount Field Specified in currency of BL.BATCH |
| 17 | `BL.BAT.AVAILED.AMOUNT` | `BlBatch_AvailedAmount` | TField |  |  |
| 18 | `BL.BAT.AVAILABLE.AMOUNT` | `BlBatch_AvailableAmount` | TField |  |  |
| 19 | `BL.BAT.DISBURSE.AMOUNT` | `BlBatch_DisburseAmount` | TField |  |  |
| 20 | `BL.BAT.RESERVED.6` | `BlBatch_Reserved6` | TField |  |  |
| 21 | `BL.BAT.RESERVED.5` | `BlBatch_Reserved5` | TField |  |  |
| 22 | `BL.BAT.RESERVED.4` | `BlBatch_Reserved4` | TField |  |  |
| 23 | `BL.BAT.RESERVED.3` | `BlBatch_Reserved3` | TField |  |  |
| 24 | `BL.BAT.RESERVED.2` | `BlBatch_Reserved2` | TField |  |  |
| 25 | `BL.BAT.RESERVED.1` | `BlBatch_Reserved1` | TField |  |  |
| 26 | `BL.BAT.LOCAL.REF` | `BlBatch_LocalRef` |  |  |  |
| 27 | `BL.BAT.OVERRIDE` | `BlBatch_Override` |  |  |  |
| 28 | `BL.BAT.RECORD.STATUS` | `BlBatch_RecordStatus` | String |  |  |
| 29 | `BL.BAT.CURR.NO` | `BlBatch_CurrNo` | String |  |  |
| 30 | `BL.BAT.INPUTTER` | `BlBatch_Inputter` |  |  |  |
| 31 | `BL.BAT.DATE.TIME` | `BlBatch_DateTime` |  |  |  |
| 32 | `BL.BAT.AUTHORISER` | `BlBatch_Authoriser` | String |  |  |
| 33 | `BL.BAT.CO.CODE` | `BlBatch_CoCode` | String |  |  |
| 34 | `BL.BAT.DEPT.CODE` | `BlBatch_DeptCode` | String |  |  |
| 35 | `BL.BAT.AUDITOR.CODE` | `BlBatch_AuditorCode` | String |  |  |
| 36 | `BL.BAT.AUDIT.DATE.TIME` | `BlBatch_AuditDateTime` | String |  |  |
