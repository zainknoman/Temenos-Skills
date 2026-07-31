# TXRECT.RECTIFICATION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.TXRECT.RECTIFICATION.PARAMETER` in `TXRECT_TaxRectificationTool.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TXRECT.REC.PAR.RO.TYPE` | `TxrectRectificationParameter_RoType` |  |  |  |
| 2 | `TXRECT.REC.PAR.TAX.TYPE` | `TxrectRectificationParameter_TaxType` |  |  |  |
| 3 | `TXRECT.REC.PAR.INTERNAL.TAX.ACCT.CATEG` | `TxrectRectificationParameter_InternalTaxAcctCateg` |  |  |  |
| 4 | `TXRECT.REC.PAR.CUST.ACCT.CLOSE.CCY` | `TxrectRectificationParameter_CustAcctCloseCcy` |  |  |  |
| 5 | `TXRECT.REC.PAR.CUST.ACCT.CLOSE.CATEG` | `TxrectRectificationParameter_CustAcctCloseCateg` |  |  |  |
| 6 | `TXRECT.REC.PAR.FT.COMMISSION.TYPE` | `TxrectRectificationParameter_FtCommissionType` | TField |  | Holds the FT Commission Type that needs to be applied for Tax reclaim |
| 7 | `TXRECT.REC.PAR.RESERVED.4` | `TxrectRectificationParameter_Reserved4` |  |  |  |
| 8 | `TXRECT.REC.PAR.RESERVED.3` | `TxrectRectificationParameter_Reserved3` | TField |  | Reserved field for future use |
| 9 | `TXRECT.REC.PAR.RESERVED.2` | `TxrectRectificationParameter_Reserved2` | TField |  | Reserved field for future use |
| 10 | `TXRECT.REC.PAR.RESERVED.1` | `TxrectRectificationParameter_Reserved1` | TField |  | Reserved field for future use |
| 11 | `TXRECT.REC.PAR.LOCAL.REF` | `TxrectRectificationParameter_LocalRef` |  |  |  |
| 12 | `TXRECT.REC.PAR.OVERRIDE` | `TxrectRectificationParameter_Override` |  |  |  |
| 13 | `TXRECT.REC.PAR.RECORD.STATUS` | `TxrectRectificationParameter_RecordStatus` | String |  |  |
| 14 | `TXRECT.REC.PAR.CURR.NO` | `TxrectRectificationParameter_CurrNo` | String |  |  |
| 15 | `TXRECT.REC.PAR.INPUTTER` | `TxrectRectificationParameter_Inputter` |  |  |  |
| 16 | `TXRECT.REC.PAR.DATE.TIME` | `TxrectRectificationParameter_DateTime` |  |  |  |
| 17 | `TXRECT.REC.PAR.AUTHORISER` | `TxrectRectificationParameter_Authoriser` | String |  |  |
| 18 | `TXRECT.REC.PAR.CO.CODE` | `TxrectRectificationParameter_CoCode` | String |  |  |
| 19 | `TXRECT.REC.PAR.DEPT.CODE` | `TxrectRectificationParameter_DeptCode` | String |  |  |
| 20 | `TXRECT.REC.PAR.AUDITOR.CODE` | `TxrectRectificationParameter_AuditorCode` | String |  |  |
| 21 | `TXRECT.REC.PAR.AUDIT.DATE.TIME` | `TxrectRectificationParameter_AuditDateTime` | String |  |  |
