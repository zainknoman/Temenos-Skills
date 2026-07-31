# DX.CO.EXT.XFER.MANUAL — Table Schema

> Source: `INSERTS/I_F.DX.CO.EXT.XFER.MANUAL` in `DX_Transfer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.COEXT.TRANS.ID` | `DxCoExtXferManual_TransId` | TField | Yes | Related DX.TRANSACTION ID Validation Rules: Mandatory input Upto 35 alphanumeric characters Must be a valid record in DX.TRANSACTION application |
| 2 | `DX.COEXT.LOTS.TRANSFER` | `DxCoExtXferManual_LotsTransfer` | TField |  | Specifies the number of lots to be transferred Validation Rules: Upto 35 alphanumeric values |
| 3 | `DX.COEXT.DEST.CUST` | `DxCoExtXferManual_DestCust` | TField |  | Specifies the external recipient customer reference number Validation Rules: Upto 10 numeric values Must be a valid record in CUSTOMER application |
| 4 | `DX.COEXT.DEST.PORTFOLIO` | `DxCoExtXferManual_DestPortfolio` | TField |  | Specifies the external recipient customer portfolio reference if any Validation Rules: Upto 18 alphanumeric characters |
| 5 | `DX.COEXT.DEST.CUST.PORT` | `DxCoExtXferManual_DestCustPort` | TField |  | Specifies the recipient customer or portfolio Validation Rules: Upto 10 numeric values Must be a valid record in CUSTOMER application |
| 6 | `DX.COEXT.CUST.CPARTY` | `DxCoExtXferManual_CustCparty` | TField |  | Specifies receiver counterparty Validation Rules: Upto 10 numeric values Must be a valid record in CUSTOMER application |
| 7 | `DX.COEXT.CUST.BNK.NME` | `DxCoExtXferManual_CustBnkNme` | TField |  | Specifies the receiver bank name Validation Rules: Upto 35 alphanumeric values |
| 8 | `DX.COEXT.CUST.BNK.ADD` | `DxCoExtXferManual_CustBnkAdd` | TField |  | Specifies the receiver bank address Validation Rules: Upto 35 alphanumeric values |
| 9 | `DX.COEXT.CUST.BNK.SORT.CDE` | `DxCoExtXferManual_CustBnkSortCde` | TField |  | Specifies the receiver bank sort code Validation Rules: Upto 35 alphanumeric values |
| 10 | `DX.COEXT.PRICE.TRADED` | `DxCoExtXferManual_PriceTraded` | TField |  | Specifies the price at which the trade is being done Validation Rules: Upto 19 numeric values |
| 11 | `DX.COEXT.FEE` | `DxCoExtXferManual_Fee` | TField |  | Set to YES if fee is required else set to NO Validation Rules: Upto 3 alphanumeric values Valid inputs are YES or NO |
| 12 | `DX.COEXT.ADVICE` | `DxCoExtXferManual_Advice` | TField |  | Set to YES if transfer advice is to be produced else set to NO Validation Rules: Upto 3 alphanumeric values Valid inputs are YES and NO |
| 13 | `DX.COEXT.CLOSEOUT.ID` | `DxCoExtXferManual_CloseoutId` |  |  |  |
| 14 | `DX.COEXT.RESERVED04` | `DxCoExtXferManual_Reserved04` | TField |  |  |
| 15 | `DX.COEXT.RESERVED03` | `DxCoExtXferManual_Reserved03` | TField |  |  |
| 16 | `DX.COEXT.LOCAL.REF` | `DxCoExtXferManual_LocalRef` |  |  |  |
| 17 | `DX.COEXT.UNAUTH.AUTH` | `DxCoExtXferManual_UnauthAuth` | TField |  | This field shows whether transfer is Authorised or Unauthorised |
| 18 | `DX.COEXT.OVERRIDE` | `DxCoExtXferManual_Override` |  |  |  |
| 19 | `DX.COEXT.RECORD.STATUS` | `DxCoExtXferManual_RecordStatus` | String |  |  |
| 20 | `DX.COEXT.CURR.NO` | `DxCoExtXferManual_CurrNo` | String |  |  |
| 21 | `DX.COEXT.INPUTTER` | `DxCoExtXferManual_Inputter` |  |  |  |
| 22 | `DX.COEXT.DATE.TIME` | `DxCoExtXferManual_DateTime` |  |  |  |
| 23 | `DX.COEXT.AUTHORISER` | `DxCoExtXferManual_Authoriser` | String |  |  |
| 24 | `DX.COEXT.CO.CODE` | `DxCoExtXferManual_CoCode` | String |  |  |
| 25 | `DX.COEXT.DEPT.CODE` | `DxCoExtXferManual_DeptCode` | String |  |  |
| 26 | `DX.COEXT.AUDITOR.CODE` | `DxCoExtXferManual_AuditorCode` | String |  |  |
| 27 | `DX.COEXT.AUDIT.DATE.TIME` | `DxCoExtXferManual_AuditDateTime` | String |  |  |
