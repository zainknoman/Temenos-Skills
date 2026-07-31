# ACH.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.ACH.EXCEPTION` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACH.EXC.ACCOUNT.NO` | `AchException_AccountNo` | TField |  | The account number used for transaction posting. |
| 2 | `ACH.EXC.TXN.AMOUNT` | `AchException_TxnAmount` | TField |  | To store the ACH transaction amount. |
| 3 | `ACH.EXC.RESERVED.26` | `AchException_Reserved26` | TField |  |  |
| 4 | `ACH.EXC.RESERVED.25` | `AchException_Reserved25` | TField |  |  |
| 5 | `ACH.EXC.RESERVED.24` | `AchException_Reserved24` | TField |  |  |
| 6 | `ACH.EXC.EXCEPTION.TYPE` | `AchException_ExceptionType` | TField |  | Valid exception types are NSF, RETURNED, DISHONORED, CONTESTED and OTHERS. |
| 7 | `ACH.EXC.EXCEPTION.MSG` | `AchException_ExceptionMsg` | TField |  | OFS failed error message recorded in this field. |
| 8 | `ACH.EXC.RESERVED.23` | `AchException_Reserved23` | TField |  |  |
| 9 | `ACH.EXC.RESERVED.22` | `AchException_Reserved22` | TField |  |  |
| 10 | `ACH.EXC.RESERVED.21` | `AchException_Reserved21` | TField |  |  |
| 11 | `ACH.EXC.ACCOUNT.OFFICER` | `AchException_AccountOfficer` | TField |  | Not Used |
| 12 | `ACH.EXC.APPLICATION` | `AchException_Application` | TField |  | Not Used |
| 13 | `ACH.EXC.APPLICATION.REF` | `AchException_ApplicationRef` | TField |  | Application transaction id into which entries posted |
| 14 | `ACH.EXC.RESERVED.20` | `AchException_Reserved20` | TField |  |  |
| 15 | `ACH.EXC.RESERVED.19` | `AchException_Reserved19` | TField |  |  |
| 16 | `ACH.EXC.RESERVED.18` | `AchException_Reserved18` | TField |  |  |
| 17 | `ACH.EXC.RESERVED.17` | `AchException_Reserved17` | TField |  |  |
| 18 | `ACH.EXC.RESERVED.16` | `AchException_Reserved16` | TField |  |  |
| 19 | `ACH.EXC.STATUS` | `AchException_Status` | TField |  | To store the ACH transaction status. |
| 20 | `ACH.EXC.RETURN.CODE` | `AchException_ReturnCode` | TField |  | To store the ACH return code. |
| 21 | `ACH.EXC.DATE.OF.DEATH` | `AchException_DateOfDeath` | TField |  | Date of death of ACH transaction customer |
| 22 | `ACH.EXC.ADDENDA.INFO` | `AchException_AddendaInfo` | TField |  | To store the ACH addenda information of the corresponding entries. |
| 23 | `ACH.EXC.REMARKS` | `AchException_Remarks` |  |  |  |
| 24 | `ACH.EXC.RESERVED.15` | `AchException_Reserved15` | TField |  |  |
| 25 | `ACH.EXC.RESERVED.14` | `AchException_Reserved14` | TField |  |  |
| 26 | `ACH.EXC.RESERVED.13` | `AchException_Reserved13` | TField |  |  |
| 27 | `ACH.EXC.RESERVED.12` | `AchException_Reserved12` | TField |  |  |
| 28 | `ACH.EXC.RESERVED.11` | `AchException_Reserved11` | TField |  |  |
| 29 | `ACH.EXC.RESERVED.10` | `AchException_Reserved10` | TField |  |  |
| 30 | `ACH.EXC.RESERVED.9` | `AchException_Reserved9` | TField |  |  |
| 31 | `ACH.EXC.RESERVED.8` | `AchException_Reserved8` | TField |  |  |
| 32 | `ACH.EXC.RESERVED.7` | `AchException_Reserved7` | TField |  |  |
| 33 | `ACH.EXC.RESERVED.6` | `AchException_Reserved6` | TField |  |  |
| 34 | `ACH.EXC.RESERVED.5` | `AchException_Reserved5` | TField |  |  |
| 35 | `ACH.EXC.RESERVED.4` | `AchException_Reserved4` | TField |  |  |
| 36 | `ACH.EXC.RESERVED.3` | `AchException_Reserved3` | TField |  |  |
| 37 | `ACH.EXC.RESERVED.2` | `AchException_Reserved2` | TField |  |  |
| 38 | `ACH.EXC.RESERVED.1` | `AchException_Reserved1` | TField |  |  |
| 39 | `ACH.EXC.LOCAL.REF` | `AchException_LocalRef` |  |  |  |
| 40 | `ACH.EXC.OVERRIDE` | `AchException_Override` |  |  |  |
| 41 | `ACH.EXC.RECORD.STATUS` | `AchException_RecordStatus` | String |  |  |
| 42 | `ACH.EXC.CURR.NO` | `AchException_CurrNo` | String |  |  |
| 43 | `ACH.EXC.INPUTTER` | `AchException_Inputter` |  |  |  |
| 44 | `ACH.EXC.DATE.TIME` | `AchException_DateTime` |  |  |  |
| 45 | `ACH.EXC.AUTHORISER` | `AchException_Authoriser` | String |  |  |
| 46 | `ACH.EXC.CO.CODE` | `AchException_CoCode` | String |  |  |
| 47 | `ACH.EXC.DEPT.CODE` | `AchException_DeptCode` | String |  |  |
| 48 | `ACH.EXC.AUDITOR.CODE` | `AchException_AuditorCode` | String |  |  |
| 49 | `ACH.EXC.AUDIT.DATE.TIME` | `AchException_AuditDateTime` | String |  |  |
