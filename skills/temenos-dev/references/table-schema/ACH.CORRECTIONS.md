# ACH.CORRECTIONS — Table Schema

> Source: `INSERTS/I_F.ACH.CORRECTIONS` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACH.CORR.PAYEE.AC` | `AchCorrections_PayeeAc` | TField |  | Field to capture the payee account number received in NOC |
| 2 | `ACH.CORR.RDFI` | `AchCorrections_Rdfi` | TField |  | Field to record the corrected routing number information received in NOC |
| 3 | `ACH.CORR.RDFI.NAME` | `AchCorrections_RdfiName` | TField |  | Field to record the corrected company name of the RDFI received in NOC |
| 4 | `ACH.CORR.TXN.CODE` | `AchCorrections_TxnCode` | TField |  | Field to hold the corrected transaction code received in NOC |
| 5 | `ACH.CORR.ACCT.TYPE` | `AchCorrections_AcctType` | TField |  | Field to hold the corrected payee account type transaction code received in NOC. Based on the transaction code, the underlying Account type defined in payee information record will be reviewed and updated |
| 6 | `ACH.CORR.PAYEE.NAME` | `AchCorrections_PayeeName` | TField |  | Field to hold corrected name of the payee as per the records in the payee�s financial institute as notified in NOC |
| 7 | `ACH.CORR.PAYEE.ID` | `AchCorrections_PayeeId` | TField |  | Field to hold the corrected Identification number of the Payee as received in NOC |
| 8 | `ACH.CORR.ACH.ENTRIES.ID` | `AchCorrections_AchEntriesId` | TField |  | Field to hold the original entry for which the notification of change was received |
| 9 | `ACH.CORR.ACH.ADDENDA.ID` | `AchCorrections_AchAddendaId` | TField |  | The addenda ID for the record where notification of change was received |
| 10 | `ACH.CORR.RESERVED.5` | `AchCorrections_Reserved5` | TField |  |  |
| 11 | `ACH.CORR.RESERVED.4` | `AchCorrections_Reserved4` | TField |  |  |
| 12 | `ACH.CORR.RESERVED.3` | `AchCorrections_Reserved3` | TField |  |  |
| 13 | `ACH.CORR.RESERVED.2` | `AchCorrections_Reserved2` | TField |  |  |
| 14 | `ACH.CORR.RESERVED.1` | `AchCorrections_Reserved1` | TField |  |  |
| 15 | `ACH.CORR.LOCAL.REF` | `AchCorrections_LocalRef` |  |  |  |
| 16 | `ACH.CORR.OVERRIDE` | `AchCorrections_Override` |  |  |  |
| 17 | `ACH.CORR.RECORD.STATUS` | `AchCorrections_RecordStatus` | String |  |  |
| 18 | `ACH.CORR.CURR.NO` | `AchCorrections_CurrNo` | String |  |  |
| 19 | `ACH.CORR.INPUTTER` | `AchCorrections_Inputter` |  |  |  |
| 20 | `ACH.CORR.DATE.TIME` | `AchCorrections_DateTime` |  |  |  |
| 21 | `ACH.CORR.AUTHORISER` | `AchCorrections_Authoriser` | String |  |  |
| 22 | `ACH.CORR.CO.CODE` | `AchCorrections_CoCode` | String |  |  |
| 23 | `ACH.CORR.DEPT.CODE` | `AchCorrections_DeptCode` | String |  |  |
| 24 | `ACH.CORR.AUDITOR.CODE` | `AchCorrections_AuditorCode` | String |  |  |
| 25 | `ACH.CORR.AUDIT.DATE.TIME` | `AchCorrections_AuditDateTime` | String |  |  |
