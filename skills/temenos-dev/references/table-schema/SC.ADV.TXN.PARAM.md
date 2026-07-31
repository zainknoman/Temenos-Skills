# SC.ADV.TXN.PARAM — Table Schema

> Source: `INSERTS/I_F.SC.ADV.TXN.PARAM` in `SC_ScfAdvisoryFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ATP.TXN.FEE.EXC.MODULE` | `ScAdvTxnParam_TxnFeeExcModule` |  |  |  |
| 2 | `SC.ATP.TXN.FEE.EXC.APP` | `ScAdvTxnParam_TxnFeeExcApp` |  |  |  |
| 3 | `SC.ATP.EXC.TXN.API` | `ScAdvTxnParam_ExcTxnApi` |  |  |  |
| 4 | `SC.ATP.MV.RESERVED.03` | `ScAdvTxnParam_MvReserved03` |  |  |  |
| 5 | `SC.ATP.MV.RESERVED.02` | `ScAdvTxnParam_MvReserved02` |  |  |  |
| 6 | `SC.ATP.MV.RESERVED.01` | `ScAdvTxnParam_MvReserved01` |  |  |  |
| 7 | `SC.ATP.TXN.FEE.EXC.FLD` | `ScAdvTxnParam_TxnFeeExcFld` |  |  |  |
| 8 | `SC.ATP.TXN.FEE.FLD.OPE` | `ScAdvTxnParam_TxnFeeFldOpe` |  |  |  |
| 9 | `SC.ATP.TXN.FEE.EXC.VALUE` | `ScAdvTxnParam_TxnFeeExcValue` |  |  |  |
| 10 | `SC.ATP.SV.RESERVED.03` | `ScAdvTxnParam_SvReserved03` |  |  |  |
| 11 | `SC.ATP.SV.RESERVED.02` | `ScAdvTxnParam_SvReserved02` |  |  |  |
| 12 | `SC.ATP.SV.RESERVED.01` | `ScAdvTxnParam_SvReserved01` |  |  |  |
| 13 | `SC.ATP.INCL.REV.TXNS` | `ScAdvTxnParam_InclRevTxns` | TField |  | This field indicates whether the Reversed transactions needs to be included for Advisoryfees calculation. Default value will be null which indicates Reversed transactions will not be included in Transaction count Validation Rule Only 'Y' will be accepted |
| 14 | `SC.ATP.TXN.COUNT.BASIS` | `ScAdvTxnParam_TxnCountBasis` | TField | Yes | This field defines the method for counting the transaction.Accepted values will be TRADE or INPUT. TRADE - Only transactions for the current period (Transaction date or trade date in current period) will beincluded for the transaction count. There will be no back-value calculations based on previous period transactionsinput during the current period. INPUT - The transactions count will be based on when the transaction is input (irrespective of transaction dateor trade date). Validation Rule Mandatory Field |
| 15 | `SC.ATP.RESERVED.05` | `ScAdvTxnParam_Reserved05` | TField |  |  |
| 16 | `SC.ATP.RESERVED.04` | `ScAdvTxnParam_Reserved04` | TField |  |  |
| 17 | `SC.ATP.RESERVED.03` | `ScAdvTxnParam_Reserved03` | TField |  |  |
| 18 | `SC.ATP.RESERVED.02` | `ScAdvTxnParam_Reserved02` | TField |  |  |
| 19 | `SC.ATP.RESERVED.01` | `ScAdvTxnParam_Reserved01` | TField |  |  |
| 20 | `SC.ATP.LOCAL.REF` | `ScAdvTxnParam_LocalRef` |  |  |  |
| 21 | `SC.ATP.OVERRIDE` | `ScAdvTxnParam_Override` |  |  |  |
| 22 | `SC.ATP.RECORD.STATUS` | `ScAdvTxnParam_RecordStatus` | String |  |  |
| 23 | `SC.ATP.CURR.NO` | `ScAdvTxnParam_CurrNo` | String |  |  |
| 24 | `SC.ATP.INPUTTER` | `ScAdvTxnParam_Inputter` |  |  |  |
| 25 | `SC.ATP.DATE.TIME` | `ScAdvTxnParam_DateTime` |  |  |  |
| 26 | `SC.ATP.AUTHORISER` | `ScAdvTxnParam_Authoriser` | String |  |  |
| 27 | `SC.ATP.CO.CODE` | `ScAdvTxnParam_CoCode` | String |  |  |
| 28 | `SC.ATP.DEPT.CODE` | `ScAdvTxnParam_DeptCode` | String |  |  |
| 29 | `SC.ATP.AUDITOR.CODE` | `ScAdvTxnParam_AuditorCode` | String |  |  |
| 30 | `SC.ATP.AUDIT.DATE.TIME` | `ScAdvTxnParam_AuditDateTime` | String |  |  |
