# DC.BATCH.CONTROL — Table Schema

> Source: `INSERTS/I_F.DC.BATCH.CONTROL` in `DC_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DC.BAT.ITEMS.NOT.AUTH` | `DcBatchControl_ItemsNotAuth` |  |  |  |
| 2 | `DC.BAT.ITEMS.USED` | `DcBatchControl_ItemsUsed` |  |  |  |
| 3 | `DC.BAT.LCY.AMOUNT.DEBIT` | `DcBatchControl_LcyAmountDebit` | TField |  | The total of all debit amount transactions with in a batch in local currency |
| 4 | `DC.BAT.LCY.AMOUNT.CREDIT` | `DcBatchControl_LcyAmountCredit` | TField |  | The total of all credit amount transactions with in a batch in local currency Validation Rules: Rule 1 : NO INPUT Rule 2 : Amount from DATA.CAPTURE record |
| 5 | `DC.BAT.FCY.AMOUNT.DEBIT` | `DcBatchControl_FcyAmountDebit` | TField |  | The total of all debit amount transactions with in a batch in foreign currency |
| 6 | `DC.BAT.FCY.AMOUNT.CREDIT` | `DcBatchControl_FcyAmountCredit` | TField |  | The total of all credit amount transactions with in a batch in foreign currency |
| 7 | `DC.BAT.RECORD.STATUS` | `DcBatchControl_RecordStatus` | String |  |  |
| 8 | `DC.BAT.COMPANY` | `DcBatchControl_Company` | TField |  | This field specifies the company to which the DATA.CAPTURE belongs to. Validation Rules: Rule 1 : NO INPUT Rule 2 : ID.COMPANY OF THE DATA.CAPTURE RECORD |
| 9 | `DC.BAT.FLAG` | `DcBatchControl_Flag` | TField |  | SYSTEM updated field. Will hold either "ADJUST" OR "TRY.ADJ |
| 10 | `DC.BAT.ADJUST.AMOUNT` | `DcBatchControl_AdjustAmount` | TField |  | SYSTEM updated field. Will hold the adjustment amount. |
| 11 | `DC.BAT.ADJUST.ITEM` | `DcBatchControl_AdjustItem` | TField |  | SYSTEM updated field. Will hold the adjustment item. |
| 12 | `DC.BAT.ACCOUNTING.DATE` | `DcBatchControl_AccountingDate` | TField |  | This field will be populated by the system from DATA.CAPTURE application. This field specifies on which date accounting should take place. |
| 13 | `DC.BAT.UNBALANCED` | `DcBatchControl_Unbalanced` |  |  |  |
| 14 | `DC.BAT.NET.LCY` | `DcBatchControl_NetLcy` |  |  |  |
| 15 | `DC.BAT.NET.FCY` | `DcBatchControl_NetFcy` |  |  |  |
| 16 | `DC.BAT.ITEMS.ON.HOLD` | `DcBatchControl_ItemsOnHold` |  |  |  |
| 17 | `DC.BAT.CONTINGENT.ACCT` | `DcBatchControl_ContingentAcct` | TField |  | This field will be populated from DATA.CAPTURE record. Sets the value in this field based on CONTINGENT.ACCT in DATA.CAPTURE to identify the type of batch (contingent/non contingent). Validation Rules: Rule 1 : NO INPUT Rule 2 : Y or N |
| 18 | `DC.BAT.OVERRIDE.CLASS` | `DcBatchControl_OverrideClass` |  |  |  |
| 19 | `DC.BAT.INPUTTERS` | `DcBatchControl_Inputters` |  |  |  |
| 20 | `DC.BAT.POSITION.TYPE` | `DcBatchControl_PositionType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 21 | `DC.BAT.COMP.ID` | `DcBatchControl_CompId` |  |  |  |
| 22 | `DC.BAT.LCY.AMT.DR` | `DcBatchControl_LcyAmtDr` |  |  |  |
| 23 | `DC.BAT.LCY.AMT.CR` | `DcBatchControl_LcyAmtCr` |  |  |  |
| 24 | `DC.BAT.FCY.AMT.DR` | `DcBatchControl_FcyAmtDr` |  |  |  |
| 25 | `DC.BAT.FCY.AMT.CR` | `DcBatchControl_FcyAmtCr` |  |  |  |
| 26 | `DC.BAT.RESERVED06` | `DcBatchControl_Reserved06` | TField |  |  |
| 27 | `DC.BAT.RESERVED05` | `DcBatchControl_Reserved05` | TField |  |  |
| 28 | `DC.BAT.RESERVED04` | `DcBatchControl_Reserved04` | TField |  |  |
| 29 | `DC.BAT.RESERVED03` | `DcBatchControl_Reserved03` | TField |  |  |
| 30 | `DC.BAT.RESERVED02` | `DcBatchControl_Reserved02` | TField |  |  |
| 31 | `DC.BAT.RESERVED01` | `DcBatchControl_Reserved01` | TField |  |  |
