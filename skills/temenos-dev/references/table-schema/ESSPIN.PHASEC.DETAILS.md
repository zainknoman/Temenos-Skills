# ESSPIN.PHASEC.DETAILS — Table Schema

> Source: `INSERTS/I_F.ESSPIN.PHASEC.DETAILS` in `ESSPIN_EmbargoInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESSPIN.CCC.CODE` | `EsspinPhasecDetails_CccCode` |  |  |  |
| 2 | `ESSPIN.ACCOUNT.NO` | `EsspinPhasecDetails_AccountNo` |  |  |  |
| 3 | `ESSPIN.LOCKED.EVENT.ID` | `EsspinPhasecDetails_LockedEventId` |  |  |  |
| 4 | `ESSPIN.LOCKED.AMOUNT` | `EsspinPhasecDetails_LockedAmount` |  |  |  |
| 5 | `ESSPIN.BLOCK.EXE.DATE` | `EsspinPhasecDetails_BlockExeDate` |  |  |  |
| 6 | `ESSPIN.BLOCK.PERIOD.DATE` | `EsspinPhasecDetails_BlockPeriodDate` |  |  |  |
| 7 | `ESSPIN.TRANS.HEADER.FIELD.NO` | `EsspinPhasecDetails_TransHeaderFieldNo` |  |  |  |
| 8 | `ESSPIN.TRANS.HEADER.ERROR.CODE` | `EsspinPhasecDetails_TransHeaderErrorCode` |  |  |  |
| 9 | `ESSPIN.CREDITOR.HEADER.FIELD.NO` | `EsspinPhasecDetails_CreditorHeaderFieldNo` |  |  |  |
| 10 | `ESSPIN.CREDITOR.HEADER.ERROR.CODE` | `EsspinPhasecDetails_CreditorHeaderErrorCode` |  |  |  |
| 11 | `ESSPIN.RECORD.FIELD.NO` | `EsspinPhasecDetails_RecordFieldNo` |  |  |  |
| 12 | `ESSPIN.RECORD.ERROR.CODE` | `EsspinPhasecDetails_RecordErrorCode` |  |  |  |
| 13 | `ESSPIN.CREDITOR.FOOTER.FIELD.NO` | `EsspinPhasecDetails_CreditorFooterFieldNo` |  |  |  |
| 14 | `ESSPIN.CREDITOR.FOOTER.ERROR.CODE` | `EsspinPhasecDetails_CreditorFooterErrorCode` |  |  |  |
| 15 | `ESSPIN.TRANS.FOOTER.FIELD.NO` | `EsspinPhasecDetails_TransFooterFieldNo` |  |  |  |
| 16 | `ESSPIN.TRANS.FOOTER.ERROR.CODE` | `EsspinPhasecDetails_TransFooterErrorCode` |  |  |  |
| 17 | `ESSPIN.USER.DECISION` | `EsspinPhasecDetails_UserDecision` | TField |  | Holds Value of Accepted or Rejected |
| 18 | `ESSPIN.LOCAL.REF` | `EsspinPhasecDetails_LocalRef` |  |  |  |
| 19 | `ESSPIN.RESERVED.1` | `EsspinPhasecDetails_Reserved1` | TField |  |  |
| 20 | `ESSPIN.RESERVED.2` | `EsspinPhasecDetails_Reserved2` | TField |  |  |
| 21 | `ESSPIN.RESERVED.3` | `EsspinPhasecDetails_Reserved3` | TField |  |  |
| 22 | `ESSPIN.RESERVED.4` | `EsspinPhasecDetails_Reserved4` | TField |  |  |
| 23 | `ESSPIN.RESERVED.5` | `EsspinPhasecDetails_Reserved5` | TField |  |  |
| 24 | `ESSPIN.RESERVED.6` | `EsspinPhasecDetails_Reserved6` | TField |  |  |
| 25 | `ESSPIN.RESERVED.7` | `EsspinPhasecDetails_Reserved7` | TField |  |  |
| 26 | `ESSPIN.RESERVED.8` | `EsspinPhasecDetails_Reserved8` | TField |  |  |
| 27 | `ESSPIN.RESERVED.9` | `EsspinPhasecDetails_Reserved9` | TField |  |  |
| 28 | `ESSPIN.RESERVED.10` | `EsspinPhasecDetails_Reserved10` | TField |  |  |
| 29 | `ESSPIN.RESERVED.11` | `EsspinPhasecDetails_Reserved11` | TField |  |  |
| 30 | `ESSPIN.RESERVED.12` | `EsspinPhasecDetails_Reserved12` | TField |  |  |
| 31 | `ESSPIN.RESERVED.13` | `EsspinPhasecDetails_Reserved13` | TField |  |  |
| 32 | `ESSPIN.RESERVED.14` | `EsspinPhasecDetails_Reserved14` | TField |  |  |
| 33 | `ESSPIN.RESERVED.15` | `EsspinPhasecDetails_Reserved15` | TField |  |  |
| 34 | `ESSPIN.OVERRIDE` | `EsspinPhasecDetails_Override` |  |  |  |
| 35 | `ESSPIN.RECORD.STATUS` | `EsspinPhasecDetails_RecordStatus` | String |  |  |
| 36 | `ESSPIN.CURR.NO` | `EsspinPhasecDetails_CurrNo` | String |  |  |
| 37 | `ESSPIN.INPUTTER` | `EsspinPhasecDetails_Inputter` |  |  |  |
| 38 | `ESSPIN.DATE.TIME` | `EsspinPhasecDetails_DateTime` |  |  |  |
| 39 | `ESSPIN.AUTHORISER` | `EsspinPhasecDetails_Authoriser` | String |  |  |
| 40 | `ESSPIN.CO.CODE` | `EsspinPhasecDetails_CoCode` | String |  |  |
| 41 | `ESSPIN.DEPT.CODE` | `EsspinPhasecDetails_DeptCode` | String |  |  |
| 42 | `ESSPIN.AUDITOR.CODE` | `EsspinPhasecDetails_AuditorCode` | String |  |  |
| 43 | `ESSPIN.AUDIT.DATE.TIME` | `EsspinPhasecDetails_AuditDateTime` | String |  |  |
