# FX.POSITION.TRANSFER.PARAM — Table Schema

> Source: `INSERTS/I_F.FX.POSITION.TRANSFER.PARAM` in `FX_PositionAndReval.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FX.POSITION.TRANSFER.PARAM.CONSOL.COMP` | `FxPositionTransferParam_ConsolComp` | TField |  | This field holds the company to where the position needs to be transferred. Validation Rules: Valid company id Valid branch under the same lead company. |
| 2 | `FX.POSITION.TRANSFER.PARAM.CREDIT.TXN.CODE` | `FxPositionTransferParam_CreditTxnCode` | TField |  | This field holds the credit transaction code. Validation Rules: Valid Transaction id. |
| 3 | `FX.POSITION.TRANSFER.PARAM.DEBIT.TXN.CODE` | `FxPositionTransferParam_DebitTxnCode` | TField |  | This field holds the debit transaction code. Validation Rules: Valid Transaction id. |
| 4 | `FX.POSITION.TRANSFER.PARAM.RESERVED.11` | `FxPositionTransferParam_Reserved11` |  |  |  |
| 5 | `FX.POSITION.TRANSFER.PARAM.RESERVED.10` | `FxPositionTransferParam_Reserved10` | TField |  |  |
| 6 | `FX.POSITION.TRANSFER.PARAM.RESERVED.9` | `FxPositionTransferParam_Reserved9` | TField |  |  |
| 7 | `FX.POSITION.TRANSFER.PARAM.RESERVED.8` | `FxPositionTransferParam_Reserved8` | TField |  |  |
| 8 | `FX.POSITION.TRANSFER.PARAM.RESERVED.7` | `FxPositionTransferParam_Reserved7` | TField |  |  |
| 9 | `FX.POSITION.TRANSFER.PARAM.RESERVED.6` | `FxPositionTransferParam_Reserved6` | TField |  |  |
| 10 | `FX.POSITION.TRANSFER.PARAM.RESERVED.5` | `FxPositionTransferParam_Reserved5` | TField |  |  |
| 11 | `FX.POSITION.TRANSFER.PARAM.RESERVED.4` | `FxPositionTransferParam_Reserved4` | TField |  |  |
| 12 | `FX.POSITION.TRANSFER.PARAM.RESERVED.3` | `FxPositionTransferParam_Reserved3` | TField |  |  |
| 13 | `FX.POSITION.TRANSFER.PARAM.RESERVED.2` | `FxPositionTransferParam_Reserved2` | TField |  |  |
| 14 | `FX.POSITION.TRANSFER.PARAM.RESERVED.1` | `FxPositionTransferParam_Reserved1` | TField |  |  |
| 15 | `FX.POSITION.TRANSFER.PARAM.LOCAL.REF` | `FxPositionTransferParam_LocalRef` |  |  |  |
| 16 | `FX.POSITION.TRANSFER.PARAM.OVERRIDE` | `FxPositionTransferParam_Override` |  |  |  |
| 17 | `FX.POSITION.TRANSFER.PARAM.RECORD.STATUS` | `FxPositionTransferParam_RecordStatus` | String |  |  |
| 18 | `FX.POSITION.TRANSFER.PARAM.CURR.NO` | `FxPositionTransferParam_CurrNo` | String |  |  |
| 19 | `FX.POSITION.TRANSFER.PARAM.INPUTTER` | `FxPositionTransferParam_Inputter` |  |  |  |
| 20 | `FX.POSITION.TRANSFER.PARAM.DATE.TIME` | `FxPositionTransferParam_DateTime` |  |  |  |
| 21 | `FX.POSITION.TRANSFER.PARAM.AUTHORISER` | `FxPositionTransferParam_Authoriser` | String |  |  |
| 22 | `FX.POSITION.TRANSFER.PARAM.CO.CODE` | `FxPositionTransferParam_CoCode` | String |  |  |
| 23 | `FX.POSITION.TRANSFER.PARAM.DEPT.CODE` | `FxPositionTransferParam_DeptCode` | String |  |  |
| 24 | `FX.POSITION.TRANSFER.PARAM.AUDITOR.CODE` | `FxPositionTransferParam_AuditorCode` | String |  |  |
| 25 | `FX.POSITION.TRANSFER.PARAM.AUDIT.DATE.TIME` | `FxPositionTransferParam_AuditDateTime` | String |  |  |
