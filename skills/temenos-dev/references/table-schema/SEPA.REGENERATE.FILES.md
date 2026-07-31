# SEPA.REGENERATE.FILES — Table Schema

> Source: `INSERTS/I_F.SEPA.REGENERATE.FILES` in `EP_OutwardProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.REGF.ORIG.BULKS` | `SepaRegenerateFiles_OrigBulks` | TField |  | Validation Rules: Up to 5 characters free text. No Input field |
| 2 | `SEP.REGF.ORIG.MSG.ID` | `SepaRegenerateFiles_OrigMsgId` |  |  |  |
| 3 | `SEP.REGF.ORIG.MSG.TYPE` | `SepaRegenerateFiles_OrigMsgType` |  |  |  |
| 4 | `SEP.REGF.ORIG.TRANS.CODE` | `SepaRegenerateFiles_OrigTransCode` |  |  |  |
| 5 | `SEP.REGF.ORIG.TOTAL.AMT` | `SepaRegenerateFiles_OrigTotalAmt` |  |  |  |
| 6 | `SEP.REGF.ORIG.NO.OF.TXN` | `SepaRegenerateFiles_OrigNoOfTxn` |  |  |  |
| 7 | `SEP.REGF.ORIG.TXN.ID` | `SepaRegenerateFiles_OrigTxnId` |  |  |  |
| 8 | `SEP.REGF.REGEN.TXN.ID` | `SepaRegenerateFiles_RegenTxnId` |  |  |  |
| 9 | `SEP.REGF.RESERVED6` | `SepaRegenerateFiles_Reserved6` | TField |  |  |
| 10 | `SEP.REGF.RESERVED5` | `SepaRegenerateFiles_Reserved5` | TField |  |  |
| 11 | `SEP.REGF.RESERVED4` | `SepaRegenerateFiles_Reserved4` | TField |  |  |
| 12 | `SEP.REGF.RESERVED3` | `SepaRegenerateFiles_Reserved3` | TField |  |  |
| 13 | `SEP.REGF.RESERVED2` | `SepaRegenerateFiles_Reserved2` | TField |  |  |
| 14 | `SEP.REGF.RESERVED1` | `SepaRegenerateFiles_Reserved1` | TField |  |  |
| 15 | `SEP.REGF.LOCAL.REF` | `SepaRegenerateFiles_LocalRef` |  |  |  |
| 16 | `SEP.REGF.OVERRIDE` | `SepaRegenerateFiles_Override` |  |  |  |
| 17 | `SEP.REGF.RECORD.STATUS` | `SepaRegenerateFiles_RecordStatus` | String |  |  |
| 18 | `SEP.REGF.CURR.NO` | `SepaRegenerateFiles_CurrNo` | String |  |  |
| 19 | `SEP.REGF.INPUTTER` | `SepaRegenerateFiles_Inputter` |  |  |  |
| 20 | `SEP.REGF.DATE.TIME` | `SepaRegenerateFiles_DateTime` |  |  |  |
| 21 | `SEP.REGF.AUTHORISER` | `SepaRegenerateFiles_Authoriser` | String |  |  |
| 22 | `SEP.REGF.CO.CODE` | `SepaRegenerateFiles_CoCode` | String |  |  |
| 23 | `SEP.REGF.DEPT.CODE` | `SepaRegenerateFiles_DeptCode` | String |  |  |
| 24 | `SEP.REGF.AUDITOR.CODE` | `SepaRegenerateFiles_AuditorCode` | String |  |  |
| 25 | `SEP.REGF.AUDIT.DATE.TIME` | `SepaRegenerateFiles_AuditDateTime` | String |  |  |
