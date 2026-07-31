# FS.GI.DIST.PAY.PROCESS.EXCEP — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.PAY.PROCESS.EXCEP` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.PAY.PROCESS.EXCEP.PARENT.REF.ID` | `FsGiDistPayProcessExcep_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.PAY.PROCESS.EXCEP.ORA.ROWID` | `FsGiDistPayProcessExcep_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.PAY.PROCESS.EXCEP.PARENT.ID.TYPE` | `FsGiDistPayProcessExcep_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.PAY.PROCESS.EXCEP.PARENT.ID` | `FsGiDistPayProcessExcep_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.PAY.PROCESS.EXCEP.PAYMENT.TYPE` | `FsGiDistPayProcessExcep_PaymentType` | TField |  | Payment type code. Multifonds DB Column is TA_PAYMENT. |
| 6 | `FS.GI.DIST.PAY.PROCESS.EXCEP.PAYMENT.PROCESS` | `FsGiDistPayProcessExcep_PaymentProcess` | TField |  | Payment process code. Multifonds DB Column is TA_PAYPROC. |
| 7 | `FS.GI.DIST.PAY.PROCESS.EXCEP.PAYMENT.CCY` | `FsGiDistPayProcessExcep_PaymentCcy` | TField |  | Payment currency code(in 3 letter format). Multifonds DB Column is PAY_CMON. |
| 8 | `FS.GI.DIST.PAY.PROCESS.EXCEP.FUND.ID` | `FsGiDistPayProcessExcep_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 9 | `FS.GI.DIST.PAY.PROCESS.EXCEP.CLASS.CURRENCY` | `FsGiDistPayProcessExcep_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 10 | `FS.GI.DIST.PAY.PROCESS.EXCEP.RESERVED10` | `FsGiDistPayProcessExcep_Reserved10` | TField |  |  |
| 11 | `FS.GI.DIST.PAY.PROCESS.EXCEP.RESERVED9` | `FsGiDistPayProcessExcep_Reserved9` | TField |  |  |
| 12 | `FS.GI.DIST.PAY.PROCESS.EXCEP.RESERVED8` | `FsGiDistPayProcessExcep_Reserved8` | TField |  |  |
| 13 | `FS.GI.DIST.PAY.PROCESS.EXCEP.RESERVED7` | `FsGiDistPayProcessExcep_Reserved7` | TField |  |  |
| 14 | `FS.GI.DIST.PAY.PROCESS.EXCEP.RESERVED6` | `FsGiDistPayProcessExcep_Reserved6` | TField |  |  |
| 15 | `FS.GI.DIST.PAY.PROCESS.EXCEP.RESERVED5` | `FsGiDistPayProcessExcep_Reserved5` | TField |  |  |
| 16 | `FS.GI.DIST.PAY.PROCESS.EXCEP.RESERVED4` | `FsGiDistPayProcessExcep_Reserved4` | TField |  |  |
| 17 | `FS.GI.DIST.PAY.PROCESS.EXCEP.RESERVED3` | `FsGiDistPayProcessExcep_Reserved3` | TField |  |  |
| 18 | `FS.GI.DIST.PAY.PROCESS.EXCEP.RESERVED2` | `FsGiDistPayProcessExcep_Reserved2` | TField |  |  |
| 19 | `FS.GI.DIST.PAY.PROCESS.EXCEP.RESERVED1` | `FsGiDistPayProcessExcep_Reserved1` | TField |  |  |
| 20 | `FS.GI.DIST.PAY.PROCESS.EXCEP.LOCAL.REF` | `FsGiDistPayProcessExcep_LocalRef` |  |  |  |
| 21 | `FS.GI.DIST.PAY.PROCESS.EXCEP.OVERRIDE` | `FsGiDistPayProcessExcep_Override` |  |  |  |
| 22 | `FS.GI.DIST.PAY.PROCESS.EXCEP.RECORD.STATUS` | `FsGiDistPayProcessExcep_RecordStatus` | String |  |  |
| 23 | `FS.GI.DIST.PAY.PROCESS.EXCEP.CURR.NO` | `FsGiDistPayProcessExcep_CurrNo` | String |  |  |
| 24 | `FS.GI.DIST.PAY.PROCESS.EXCEP.INPUTTER` | `FsGiDistPayProcessExcep_Inputter` |  |  |  |
| 25 | `FS.GI.DIST.PAY.PROCESS.EXCEP.DATE.TIME` | `FsGiDistPayProcessExcep_DateTime` |  |  |  |
| 26 | `FS.GI.DIST.PAY.PROCESS.EXCEP.AUTHORISER` | `FsGiDistPayProcessExcep_Authoriser` | String |  |  |
| 27 | `FS.GI.DIST.PAY.PROCESS.EXCEP.CO.CODE` | `FsGiDistPayProcessExcep_CoCode` | String |  |  |
| 28 | `FS.GI.DIST.PAY.PROCESS.EXCEP.DEPT.CODE` | `FsGiDistPayProcessExcep_DeptCode` | String |  |  |
| 29 | `FS.GI.DIST.PAY.PROCESS.EXCEP.AUDITOR.CODE` | `FsGiDistPayProcessExcep_AuditorCode` | String |  |  |
| 30 | `FS.GI.DIST.PAY.PROCESS.EXCEP.AUDIT.DATE.TIME` | `FsGiDistPayProcessExcep_AuditDateTime` | String |  |  |
