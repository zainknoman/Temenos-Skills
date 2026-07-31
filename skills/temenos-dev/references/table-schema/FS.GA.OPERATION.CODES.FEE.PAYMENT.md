# FS.GA.OPERATION.CODES.FEE.PAYMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.OPERATION.CODES.FEE.PAYMENT` in `FS_Equivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.PARENT.REF.ID` | `FsGaOperationCodesFeePayment_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.ORA.ROWID` | `FsGaOperationCodesFeePayment_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.OP.CODE` | `FsGaOperationCodesFeePayment_OpCode` | TField |  | Enter the operation code Multifonds DB Column is COPER_REPRISE. |
| 4 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.CHARGE.CODE` | `FsGaOperationCodesFeePayment_ChargeCode` | TField |  | Corresponds to Multifonds fee code or NAV charge number Multifonds DB Column is NOFRAIS. |
| 5 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.REPRISE.INT.ACCOUNT.NUMBER` | `FsGaOperationCodesFeePayment_RepriseIntAccountNumber` | TField |  | Enter account number as per the source system Multifonds DB Column is NRUBR_REP_INT. |
| 6 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.SOURCE.SUFFIX.NUMBER` | `FsGaOperationCodesFeePayment_SourceSuffixNumber` | TField |  | Enter the suffix number, if any, as used in the source system. Multifonds DB Column is NSUFF_REP_INT. |
| 7 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.GL.ACCOUNT` | `FsGaOperationCodesFeePayment_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 8 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.FUND.ID` | `FsGaOperationCodesFeePayment_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 9 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.RESERVED10` | `FsGaOperationCodesFeePayment_Reserved10` | TField |  |  |
| 10 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.RESERVED9` | `FsGaOperationCodesFeePayment_Reserved9` | TField |  |  |
| 11 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.RESERVED8` | `FsGaOperationCodesFeePayment_Reserved8` | TField |  |  |
| 12 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.RESERVED7` | `FsGaOperationCodesFeePayment_Reserved7` | TField |  |  |
| 13 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.RESERVED6` | `FsGaOperationCodesFeePayment_Reserved6` | TField |  |  |
| 14 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.RESERVED5` | `FsGaOperationCodesFeePayment_Reserved5` | TField |  |  |
| 15 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.RESERVED4` | `FsGaOperationCodesFeePayment_Reserved4` | TField |  |  |
| 16 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.RESERVED3` | `FsGaOperationCodesFeePayment_Reserved3` | TField |  |  |
| 17 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.RESERVED2` | `FsGaOperationCodesFeePayment_Reserved2` | TField |  |  |
| 18 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.RESERVED1` | `FsGaOperationCodesFeePayment_Reserved1` | TField |  |  |
| 19 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.LOCAL.REF` | `FsGaOperationCodesFeePayment_LocalRef` |  |  |  |
| 20 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.OVERRIDE` | `FsGaOperationCodesFeePayment_Override` |  |  |  |
| 21 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.RECORD.STATUS` | `FsGaOperationCodesFeePayment_RecordStatus` | String |  |  |
| 22 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.CURR.NO` | `FsGaOperationCodesFeePayment_CurrNo` | String |  |  |
| 23 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.INPUTTER` | `FsGaOperationCodesFeePayment_Inputter` |  |  |  |
| 24 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.DATE.TIME` | `FsGaOperationCodesFeePayment_DateTime` |  |  |  |
| 25 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.AUTHORISER` | `FsGaOperationCodesFeePayment_Authoriser` | String |  |  |
| 26 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.CO.CODE` | `FsGaOperationCodesFeePayment_CoCode` | String |  |  |
| 27 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.DEPT.CODE` | `FsGaOperationCodesFeePayment_DeptCode` | String |  |  |
| 28 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.AUDITOR.CODE` | `FsGaOperationCodesFeePayment_AuditorCode` | String |  |  |
| 29 | `FS.GA.OPERATION.CODES.FEE.PAYMENT.AUDIT.DATE.TIME` | `FsGaOperationCodesFeePayment_AuditDateTime` | String |  |  |
