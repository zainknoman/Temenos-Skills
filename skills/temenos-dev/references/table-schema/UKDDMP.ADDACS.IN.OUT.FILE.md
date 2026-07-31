# UKDDMP.ADDACS.IN.OUT.FILE — Table Schema

> Source: `INSERTS/I_F.UKDDMP.ADDACS.IN.OUT.FILE` in `UKDDMP_Lodgements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IN.OUT.ADDACS.FILE.DIRECTION` | `UkddmpAddacsInOutFile_FileDirection` | TField |  | This field contains direction of file either Inward or Outward |
| 2 | `IN.OUT.ADDACS.FILE.STATUS` | `UkddmpAddacsInOutFile_FileStatus` | TField |  | This field contains status of file |
| 3 | `IN.OUT.ADDACS.REASON.FOR.FAILURE` | `UkddmpAddacsInOutFile_ReasonForFailure` | TField |  | This field contains the reason for failure |
| 4 | `IN.OUT.ADDACS.FILE.TYPE` | `UkddmpAddacsInOutFile_FileType` | TField |  | This field contains the type of file either ADDACS or AUDDIS |
| 5 | `IN.OUT.ADDACS.CORRELATION.ID` | `UkddmpAddacsInOutFile_CorrelationId` | TField |  | This field conatins the DD mandate reference |
| 6 | `IN.OUT.ADDACS.HDR.LABEL.NAME` | `UkddmpAddacsInOutFile_HdrLabelName` | TField |  | This field contains the lable name |
| 7 | `IN.OUT.ADDACS.HDR.SERIAL.NO` | `UkddmpAddacsInOutFile_HdrSerialNo` | TField |  | This field contains the submission serial number |
| 8 | `IN.OUT.ADDACS.HDR.BANK.CODE.SUBMITTER` | `UkddmpAddacsInOutFile_HdrBankCodeSubmitter` | TField |  | This contains the bank code of the submitter |
| 9 | `IN.OUT.ADDACS.HDR.CENTER.NO` | `UkddmpAddacsInOutFile_HdrCenterNo` | TField |  | This contains the submitter centre number |
| 10 | `IN.OUT.ADDACS.HDR.BANK.CODE.PAYING.BANK` | `UkddmpAddacsInOutFile_HdrBankCodePayingBank` | TField |  | This field contains the bank code of paying bank |
| 11 | `IN.OUT.ADDACS.HDR.PROC.DAY` | `UkddmpAddacsInOutFile_HdrProcDay` | TField |  | This field contains the processing date in the format bYYDDD |
| 12 | `IN.OUT.ADDACS.HDR.WORK.CODE` | `UkddmpAddacsInOutFile_HdrWorkCode` | TField |  | This field contains the workcode |
| 13 | `IN.OUT.ADDACS.HDR.FILE.NUMBER` | `UkddmpAddacsInOutFile_HdrFileNumber` | TField |  | This field contains the file number |
| 14 | `IN.OUT.ADDACS.HDR.TEST.INDICATOR` | `UkddmpAddacsInOutFile_HdrTestIndicator` | TField |  | This field is a test indicator |
| 15 | `IN.OUT.ADDACS.DATA.SUN` | `UkddmpAddacsInOutFile_DataSun` | TField |  | This field contains the service user number of a direct debit originator. Corresponds to the value of CREDITOR.ID in DD.DDI |
| 16 | `IN.OUT.ADDACS.DATA.RECORD.TYPE` | `UkddmpAddacsInOutFile_DataRecordType` | TField |  | This field contains the record type. Value will be A |
| 17 | `IN.OUT.ADDACS.DATA.EFF.DATE` | `UkddmpAddacsInOutFile_DataEffDate` | TField |  | This field contains the advice effective date. |
| 18 | `IN.OUT.ADDACS.DATA.ADVICE.REF` | `UkddmpAddacsInOutFile_DataAdviceRef` | TField |  | This field contains the advice reference |
| 19 | `IN.OUT.ADDACS.DATA.ADVICE.PAYER` | `UkddmpAddacsInOutFile_DataAdvicePayer` | TField |  | This field contains the advice payer's name |
| 20 | `IN.OUT.ADDACS.DATA.ADVICE.PAY.ACC` | `UkddmpAddacsInOutFile_DataAdvicePayAcc` | TField |  | This field contains the advice payer's account number |
| 21 | `IN.OUT.ADDACS.DATA.ADVICE.PAY.SORT` | `UkddmpAddacsInOutFile_DataAdvicePaySort` | TField |  | This contains the advice payer's sorting code |
| 22 | `IN.OUT.ADDACS.DATA.ADVICE.DD` | `UkddmpAddacsInOutFile_DataAdviceDd` | TField |  | This has advice due date in the format byyddd |
| 23 | `IN.OUT.ADDACS.DATA.ADVICE.FQY` | `UkddmpAddacsInOutFile_DataAdviceFqy` | TField |  | Contains the advice payment frequency. Values can be D/W/F/M/B/Q/Y |
| 24 | `IN.OUT.ADDACS.DATA.ADV.PYMT` | `UkddmpAddacsInOutFile_DataAdvPymt` | TField |  | Contains the advice amount of payment. |
| 25 | `IN.OUT.ADDACS.DATA.ADV.REASON` | `UkddmpAddacsInOutFile_DataAdvReason` | TField |  | Contains the advice reason code |
| 26 | `IN.OUT.ADDACS.DATA.ADV.PAY.NAME` | `UkddmpAddacsInOutFile_DataAdvPayName` | TField |  | This field contains the advice payer's new name |
| 27 | `IN.OUT.ADDACS.DATA.ADV.PAYER.ACCNO` | `UkddmpAddacsInOutFile_DataAdvPayerAccno` | TField |  | This field contains the advice payer's new account number |
| 28 | `IN.OUT.ADDACS.DATA.ADV.PAYER.SORTCDE` | `UkddmpAddacsInOutFile_DataAdvPayerSortcde` | TField |  | This field contains the advice payer's new sorting code |
| 29 | `IN.OUT.ADDACS.DATA.ADV.NEWDATE` | `UkddmpAddacsInOutFile_DataAdvNewdate` | TField |  | This contains the advice new date |
| 30 | `IN.OUT.ADDACS.DATA.ADV.PAY.FQY` | `UkddmpAddacsInOutFile_DataAdvPayFqy` | TField |  | This contains the advice new payment frequency |
| 31 | `IN.OUT.ADDACS.DATA.NEW.PAYMENT` | `UkddmpAddacsInOutFile_DataNewPayment` | TField |  | This contains the new amount of payment |
| 32 | `IN.OUT.ADDACS.DATA.ADV.LAST.DATE` | `UkddmpAddacsInOutFile_DataAdvLastDate` | TField |  | Contains the advice last payment date |
| 33 | `IN.OUT.ADDACS.UTL.LABEL.NAME` | `UkddmpAddacsInOutFile_UtlLabelName` | TField |  | This field contains the label name |
| 34 | `IN.OUT.ADDACS.REJ.PROC.DATE` | `UkddmpAddacsInOutFile_RejProcDate` | TField |  | This field contains bacs processing date of original Ddi |
| 35 | `IN.OUT.ADDACS.REJ.ORIG.NAME` | `UkddmpAddacsInOutFile_RejOrigName` | TField |  | This field contains originator's name |
| 36 | `IN.OUT.ADDACS.REJ.TXN.CODE` | `UkddmpAddacsInOutFile_RejTxnCode` | TField |  | This field contains transaction code |
| 37 | `IN.OUT.ADDACS.REJ.ORIG.SORT.CODE` | `UkddmpAddacsInOutFile_RejOrigSortCode` | TField |  | This field contains orignator's sorting code |
| 38 | `IN.OUT.ADDACS.REJ.ORIG.ACC.NUMBER` | `UkddmpAddacsInOutFile_RejOrigAccNumber` | TField |  | This field contains originator's account number |
| 39 | `IN.OUT.ADDACS.REJ.ADVICE.NOTE` | `UkddmpAddacsInOutFile_RejAdviceNote` | TField |  | This field contains advice note |
| 40 | `IN.OUT.ADDACS.REJ.PAYER.ACC.TYPE` | `UkddmpAddacsInOutFile_RejPayerAccType` | TField |  | This field contains payer's account type |
| 41 | `IN.OUT.ADDACS.LOCAL.REF` | `UkddmpAddacsInOutFile_LocalRef` |  |  |  |
| 42 | `IN.OUT.ADDACS.RESERVED.1` | `UkddmpAddacsInOutFile_Reserved1` | TField |  | This field is reserved for future use. |
| 43 | `IN.OUT.ADDACS.RESERVED.2` | `UkddmpAddacsInOutFile_Reserved2` | TField |  | This field is reserved for future use. |
| 44 | `IN.OUT.ADDACS.RESERVED.3` | `UkddmpAddacsInOutFile_Reserved3` | TField |  | This field is reserved for future use. |
| 45 | `IN.OUT.ADDACS.RESERVED.4` | `UkddmpAddacsInOutFile_Reserved4` | TField |  | This field is reserved for future use. |
| 46 | `IN.OUT.ADDACS.RESERVED.5` | `UkddmpAddacsInOutFile_Reserved5` | TField |  | This field is reserved for future use. |
| 47 | `IN.OUT.ADDACS.RESERVED.6` | `UkddmpAddacsInOutFile_Reserved6` | TField |  | This field is reserved for future use. |
| 48 | `IN.OUT.ADDACS.RESERVED.7` | `UkddmpAddacsInOutFile_Reserved7` | TField |  | This field is reserved for future use. |
| 49 | `IN.OUT.ADDACS.RESERVED.8` | `UkddmpAddacsInOutFile_Reserved8` | TField |  | This field is reserved for future use. |
| 50 | `IN.OUT.ADDACS.RESERVED.9` | `UkddmpAddacsInOutFile_Reserved9` | TField |  | This field is reserved for future use. |
| 51 | `IN.OUT.ADDACS.RESERVED.10` | `UkddmpAddacsInOutFile_Reserved10` | TField |  | This field is reserved for future use. |
| 52 | `IN.OUT.ADDACS.OVERRIDE` | `UkddmpAddacsInOutFile_Override` |  |  |  |
| 53 | `IN.OUT.ADDACS.RECORD.STATUS` | `UkddmpAddacsInOutFile_RecordStatus` | String |  |  |
| 54 | `IN.OUT.ADDACS.CURR.NO` | `UkddmpAddacsInOutFile_CurrNo` | String |  |  |
| 55 | `IN.OUT.ADDACS.INPUTTER` | `UkddmpAddacsInOutFile_Inputter` |  |  |  |
| 56 | `IN.OUT.ADDACS.DATE.TIME` | `UkddmpAddacsInOutFile_DateTime` |  |  |  |
| 57 | `IN.OUT.ADDACS.AUTHORISER` | `UkddmpAddacsInOutFile_Authoriser` | String |  |  |
| 58 | `IN.OUT.ADDACS.CO.CODE` | `UkddmpAddacsInOutFile_CoCode` | String |  |  |
| 59 | `IN.OUT.ADDACS.DEPT.CODE` | `UkddmpAddacsInOutFile_DeptCode` | String |  |  |
| 60 | `IN.OUT.ADDACS.AUDITOR.CODE` | `UkddmpAddacsInOutFile_AuditorCode` | String |  |  |
| 61 | `IN.OUT.ADDACS.AUDIT.DATE.TIME` | `UkddmpAddacsInOutFile_AuditDateTime` | String |  |  |
