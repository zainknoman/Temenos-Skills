# DX.CO.XFER.MANUAL — Table Schema

> Source: `INSERTS/I_F.DX.CO.XFER.MANUAL` in `DX_Transfer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.COINT.TRANS.ID` | `DxCoXferManual_TransId` | TField |  | This specifies the related DX.TRANSACTION id Validation Rules: Upto 35 alphanumeric characters Must be a valid record in DX.TRANSACTION application |
| 2 | `DX.COINT.LOTS.TRANSFER` | `DxCoXferManual_LotsTransfer` | TField |  | Specifies the no. of lots to be transferred Validation Rules: Upto 35 numeric values |
| 3 | `DX.COINT.DEST.CUST` | `DxCoXferManual_DestCust` | TField |  | Specifies the internal recipient customer Validation Rules: Upto 10 numeric values Must be a valid record CUSTOMER application |
| 4 | `DX.COINT.DEST.PORTFOLIO` | `DxCoXferManual_DestPortfolio` | TField |  | Specifies the internal recipient Customer portfolio if any Validation Rules: Upto 18 aplhanumeric values |
| 5 | `DX.COINT.PRICE.TRADED` | `DxCoXferManual_PriceTraded` | TField |  | Price at which the trading is done Validation Rules: Upto 19 numeric values |
| 6 | `DX.COINT.FEE` | `DxCoXferManual_Fee` | TField |  | Set to YES if a fee is required else set to NO Validation Rules: Upto 3 alphanumeric values Valid inputs are YES and NO |
| 7 | `DX.COINT.ADVICE` | `DxCoXferManual_Advice` | TField |  | Specifies the external recipient customer reference number Validation Rules: Upto 10 numeric values Must be a valid record in CUSTOMER application |
| 8 | `DX.COINT.CLOSEOUT.ID` | `DxCoXferManual_CloseoutId` |  |  |  |
| 9 | `DX.COINT.RESERVED03` | `DxCoXferManual_Reserved03` | TField |  |  |
| 10 | `DX.COINT.RESERVED02` | `DxCoXferManual_Reserved02` | TField |  |  |
| 11 | `DX.COINT.RESERVED01` | `DxCoXferManual_Reserved01` | TField |  |  |
| 12 | `DX.COINT.LOCAL.REF` | `DxCoXferManual_LocalRef` |  |  |  |
| 13 | `DX.COINT.OVERRIDE` | `DxCoXferManual_Override` |  |  |  |
| 14 | `DX.COINT.RECORD.STATUS` | `DxCoXferManual_RecordStatus` | String |  |  |
| 15 | `DX.COINT.CURR.NO` | `DxCoXferManual_CurrNo` | String |  |  |
| 16 | `DX.COINT.INPUTTER` | `DxCoXferManual_Inputter` |  |  |  |
| 17 | `DX.COINT.DATE.TIME` | `DxCoXferManual_DateTime` |  |  |  |
| 18 | `DX.COINT.AUTHORISER` | `DxCoXferManual_Authoriser` | String |  |  |
| 19 | `DX.COINT.CO.CODE` | `DxCoXferManual_CoCode` | String |  |  |
| 20 | `DX.COINT.DEPT.CODE` | `DxCoXferManual_DeptCode` | String |  |  |
| 21 | `DX.COINT.AUDITOR.CODE` | `DxCoXferManual_AuditorCode` | String |  |  |
| 22 | `DX.COINT.AUDIT.DATE.TIME` | `DxCoXferManual_AuditDateTime` | String |  |  |
