# CAMB.MICR.CLR.DETS — Table Schema

> Source: `INSERTS/I_F.CAMB.MICR.CLR.DETS` in `CACCPA_ClearingCPA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.MAP.DETS.DEBIT.ACCOUNT` | `CambMicrClrDets_DebitAccount` |  |  |  |
| 2 | `CAMB.MAP.DETS.CREDIT.ACCOUNT` | `CambMicrClrDets_CreditAccount` |  |  |  |
| 3 | `CAMB.MAP.DETS.MICR.ACCOUNT` | `CambMicrClrDets_MicrAccount` |  |  |  |
| 4 | `CAMB.MAP.DETS.TRANSIT` | `CambMicrClrDets_Transit` |  |  |  |
| 5 | `CAMB.MAP.DETS.CURRENCY` | `CambMicrClrDets_Currency` |  |  |  |
| 6 | `CAMB.MAP.DETS.FILE.CURRENCY` | `CambMicrClrDets_FileCurrency` |  |  |  |
| 7 | `CAMB.MAP.DETS.TXN.AMOUNT` | `CambMicrClrDets_TxnAmount` |  |  |  |
| 8 | `CAMB.MAP.DETS.CLEAR.FILE.AMT` | `CambMicrClrDets_ClearFileAmt` |  |  |  |
| 9 | `CAMB.MAP.DETS.PROCESSING.DATE` | `CambMicrClrDets_ProcessingDate` |  |  |  |
| 10 | `CAMB.MAP.DETS.VALUE.DATE` | `CambMicrClrDets_ValueDate` |  |  |  |
| 11 | `CAMB.MAP.DETS.FT.TXN.TYPE` | `CambMicrClrDets_FtTxnType` |  |  |  |
| 12 | `CAMB.MAP.DETS.CR.DR.FLAG` | `CambMicrClrDets_CrDrFlag` |  |  |  |
| 13 | `CAMB.MAP.DETS.CHEQUE.NUMBER` | `CambMicrClrDets_ChequeNumber` |  |  |  |
| 14 | `CAMB.MAP.DETS.SEQUENCE.NUMBER` | `CambMicrClrDets_SequenceNumber` |  |  |  |
| 15 | `CAMB.MAP.DETS.CLEAR.FILE.DATE` | `CambMicrClrDets_ClearFileDate` |  |  |  |
| 16 | `CAMB.MAP.DETS.TRACE.NO` | `CambMicrClrDets_TraceNo` |  |  |  |
| 17 | `CAMB.MAP.DETS.TXN.STATUS` | `CambMicrClrDets_TxnStatus` |  |  |  |
| 18 | `CAMB.MAP.DETS.TXN.COMMENT` | `CambMicrClrDets_TxnComment` |  |  |  |
| 19 | `CAMB.MAP.DETS.LARGE.TXN` | `CambMicrClrDets_LargeTxn` |  |  |  |
| 20 | `CAMB.MAP.DETS.REV.STATUS` | `CambMicrClrDets_RevStatus` |  |  |  |
| 21 | `CAMB.MAP.DETS.REVERSED.DATE` | `CambMicrClrDets_ReversedDate` |  |  |  |
| 22 | `CAMB.MAP.DETS.RESERVED.5` | `CambMicrClrDets_Reserved5` |  |  |  |
| 23 | `CAMB.MAP.DETS.RESERVED.4` | `CambMicrClrDets_Reserved4` |  |  |  |
| 24 | `CAMB.MAP.DETS.RESERVED.3` | `CambMicrClrDets_Reserved3` |  |  |  |
| 25 | `CAMB.MAP.DETS.RESERVED.2` | `CambMicrClrDets_Reserved2` |  |  |  |
| 26 | `CAMB.MAP.DETS.RESERVED.1` | `CambMicrClrDets_Reserved1` |  |  |  |
| 27 | `CAMB.MAP.DETS.LOCAL.REF` | `CambMicrClrDets_LocalRef` |  |  |  |
