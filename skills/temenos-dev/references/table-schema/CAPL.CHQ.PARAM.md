# CAPL.CHQ.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.CHQ.PARAM` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.CHQP.PAYMENT.TYPE` | `CaplChqParam_PaymentType` |  |  |  |
| 2 | `CAPL.CHQP.CHEQUE.TYPE` | `CaplChqParam_ChequeType` |  |  |  |
| 3 | `CAPL.CHQP.PROCESSING.TYPE` | `CaplChqParam_ProcessingType` |  |  |  |
| 4 | `CAPL.CHQP.RESERVED.11` | `CaplChqParam_Reserved11` | TField |  |  |
| 5 | `CAPL.CHQP.RESERVED.10` | `CaplChqParam_Reserved10` | TField |  |  |
| 6 | `CAPL.CHQP.RESERVED.9` | `CaplChqParam_Reserved9` | TField |  |  |
| 7 | `CAPL.CHQP.RESERVED.8` | `CaplChqParam_Reserved8` | TField |  |  |
| 8 | `CAPL.CHQP.RESERVED.7` | `CaplChqParam_Reserved7` | TField |  |  |
| 9 | `CAPL.CHQP.RESERVED.6` | `CaplChqParam_Reserved6` | TField |  |  |
| 10 | `CAPL.CHQP.GIT.INTERFACE.CHQ` | `CaplChqParam_GitInterfaceChq` |  |  |  |
| 11 | `CAPL.CHQP.GIT.INTERFACE.EFT` | `CaplChqParam_GitInterfaceEft` |  |  |  |
| 12 | `CAPL.CHQP.DE.MAPPING` | `CaplChqParam_DeMapping` |  |  |  |
| 13 | `CAPL.CHQP.DEAL.SLIP` | `CaplChqParam_DealSlip` |  |  |  |
| 14 | `CAPL.CHQP.RP.PO.BENE` | `CaplChqParam_RpPoBene` | TField |  |  |
| 15 | `CAPL.CHQP.RP.PO.PRODUCT` | `CaplChqParam_RpPoProduct` | TField |  |  |
| 16 | `CAPL.CHQP.RP.PO.OFS.SOURCE` | `CaplChqParam_RpPoOfsSource` | TField |  |  |
| 17 | `CAPL.CHQP.RP.PO.VERSION` | `CaplChqParam_RpPoVersion` | TField |  |  |
| 18 | `CAPL.CHQP.RESERVED.1` | `CaplChqParam_Reserved1` | TField |  |  |
| 19 | `CAPL.CHQP.LOCAL.REF` | `CaplChqParam_LocalRef` |  |  |  |
| 20 | `CAPL.CHQP.OVERRIDE` | `CaplChqParam_Override` |  |  |  |
| 21 | `CAPL.CHQP.RECORD.STATUS` | `CaplChqParam_RecordStatus` | String |  |  |
| 22 | `CAPL.CHQP.CURR.NO` | `CaplChqParam_CurrNo` | String |  |  |
| 23 | `CAPL.CHQP.INPUTTER` | `CaplChqParam_Inputter` |  |  |  |
| 24 | `CAPL.CHQP.DATE.TIME` | `CaplChqParam_DateTime` |  |  |  |
| 25 | `CAPL.CHQP.AUTHORISER` | `CaplChqParam_Authoriser` | String |  |  |
| 26 | `CAPL.CHQP.CO.CODE` | `CaplChqParam_CoCode` | String |  |  |
| 27 | `CAPL.CHQP.DEPT.CODE` | `CaplChqParam_DeptCode` | String |  |  |
| 28 | `CAPL.CHQP.AUDITOR.CODE` | `CaplChqParam_AuditorCode` | String |  |  |
| 29 | `CAPL.CHQP.AUDIT.DATE.TIME` | `CaplChqParam_AuditDateTime` | String |  |  |
