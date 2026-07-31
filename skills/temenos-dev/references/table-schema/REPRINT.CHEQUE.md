# REPRINT.CHEQUE — Table Schema

> Source: `INSERTS/I_F.REPRINT.CHEQUE` in `CACQMG_ChequeManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RPT.CHQ.CHEQUE.NUMBER` | `ReprintCheque_ChequeNumber` | TField |  |  |
| 2 | `RPT.CHQ.ACCT.NUMBER` | `ReprintCheque_AcctNumber` | TField |  | Valid Account number for which the cheque is issued.Valid entry in ACCOUNT table. |
| 3 | `RPT.CHQ.CHQ.TYPE` | `ReprintCheque_ChqType` | TField |  | This field can be entered by the user or defaulted at version level during UI stage. Valid record from CHEQUE.TYPE table.Valid entry in CHEQUE.TYPE table. |
| 4 | `RPT.CHQ.LOCAL.REF` | `ReprintCheque_LocalRef` |  |  |  |
| 5 | `RPT.CHQ.RESERVED.10` | `ReprintCheque_Reserved10` | TField |  |  |
| 6 | `RPT.CHQ.RESERVED.9` | `ReprintCheque_Reserved9` | TField |  |  |
| 7 | `RPT.CHQ.RESERVED.8` | `ReprintCheque_Reserved8` | TField |  |  |
| 8 | `RPT.CHQ.RESERVED.7` | `ReprintCheque_Reserved7` | TField |  |  |
| 9 | `RPT.CHQ.RESERVED.6` | `ReprintCheque_Reserved6` | TField |  |  |
| 10 | `RPT.CHQ.RESERVED.5` | `ReprintCheque_Reserved5` | TField |  |  |
| 11 | `RPT.CHQ.RESERVED.4` | `ReprintCheque_Reserved4` | TField |  |  |
| 12 | `RPT.CHQ.RESERVED.3` | `ReprintCheque_Reserved3` | TField |  |  |
| 13 | `RPT.CHQ.RESERVED.2` | `ReprintCheque_Reserved2` | TField |  |  |
| 14 | `RPT.CHQ.RESERVED.1` | `ReprintCheque_Reserved1` | TField |  |  |
| 15 | `RPT.CHQ.OVERRIDE` | `ReprintCheque_Override` |  |  |  |
| 16 | `RPT.CHQ.RECORD.STATUS` | `ReprintCheque_RecordStatus` | String |  |  |
| 17 | `RPT.CHQ.CURR.NO` | `ReprintCheque_CurrNo` | String |  |  |
| 18 | `RPT.CHQ.INPUTTER` | `ReprintCheque_Inputter` |  |  |  |
| 19 | `RPT.CHQ.DATE.TIME` | `ReprintCheque_DateTime` |  |  |  |
| 20 | `RPT.CHQ.AUTHORISER` | `ReprintCheque_Authoriser` | String |  |  |
| 21 | `RPT.CHQ.CO.CODE` | `ReprintCheque_CoCode` | String |  |  |
| 22 | `RPT.CHQ.DEPT.CODE` | `ReprintCheque_DeptCode` | String |  |  |
| 23 | `RPT.CHQ.AUDITOR.CODE` | `ReprintCheque_AuditorCode` | String |  |  |
| 24 | `RPT.CHQ.AUDIT.DATE.TIME` | `ReprintCheque_AuditDateTime` | String |  |  |
