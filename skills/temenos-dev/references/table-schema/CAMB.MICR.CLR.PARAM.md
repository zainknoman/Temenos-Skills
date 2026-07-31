# CAMB.MICR.CLR.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.MICR.CLR.PARAM` in `CACCPA_ClearingCPA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.MICR.CURRENCY` | `CambMicrClrParam_Currency` |  |  |  |
| 2 | `CAMB.MICR.THRESHOLD.AMT` | `CambMicrClrParam_ThresholdAmt` |  |  |  |
| 3 | `CAMB.MICR.SEQUENCE.NO` | `CambMicrClrParam_SequenceNo` | TField |  | Purpose of the field to store the sequence number of incoming processed file.Once the clearing file is processed, this field gets incremented by 1.Validation: Sequence in this field should be less than the sequence in the incoming file.Allowed upto 15digits.eg. 0005When the incoming file with sequence as 0006 is processed and completed, the value in this field will gets incremented to 0006. |
| 4 | `CAMB.MICR.DATA.FILE.DIR` | `CambMicrClrParam_DataFileDir` | TField |  | Directory name where the extracted files to be placed.This can be load or extract location. |
| 5 | `CAMB.MICR.DATA.FILENAME` | `CambMicrClrParam_DataFilename` | TField |  | This field will have the name of the clearing file extracted.User need to configure their own clearing items (CAMB.MICR.CLR.MAP records) in the data part of the required clearing batch records listed below.The exact file name to be Parameterized in this field. |
| 6 | `CAMB.MICR.LOG.DIR` | `CambMicrClrParam_LogDir` | TField |  | Field will hold the valid directory name where log files have to be placed.When the clearing file is executed the failed transactions which are not processed will be part of this log file.Eg. MD.IN.LOG |
| 7 | `CAMB.MICR.LOG.FILENAME` | `CambMicrClrParam_LogFilename` | TField |  | Field which holds the log file name which is placed in the path mentioned in LOG.DIReg.CMB-MICR-CAD |
| 8 | `CAMB.MICR.PRE.PROCESS` | `CambMicrClrParam_PreProcess` |  |  |  |
| 9 | `CAMB.MICR.POST.PROCESS` | `CambMicrClrParam_PostProcess` |  |  |  |
| 10 | `CAMB.MICR.PROCESS.DEPENDENCY` | `CambMicrClrParam_ProcessDependency` |  |  |  |
| 11 | `CAMB.MICR.DEPENDENCY.FLAG` | `CambMicrClrParam_DependencyFlag` | TField |  | Purpose of the field to determine the output of the validation set in PROCESS.DEPENDENCEY field to override of not.Allowed inputs: Override / Blank.If set to override - Any process dependency failure will get override and clearing process will be continued. |
| 12 | `CAMB.MICR.REVERSAL.SEQ.NO` | `CambMicrClrParam_ReversalSeqNo` | TField |  | Purpose of the field to store the sequence number of file to be reversed in case of duplications.Eg. 0002All the clearing transactions for the specific seq no 0002 will be reversed in this instance. |
| 13 | `CAMB.MICR.REV.PROCESS.DATE` | `CambMicrClrParam_RevProcessDate` | TField |  | field used to store the reversal process date to be used for reversing the clearing file. (reversing the posted transactions)Note: it's a T24 DATE on which the file is to be reversed.To be inputted manually.Valid date format field. |
| 14 | `CAMB.MICR.VALUE.DATE` | `CambMicrClrParam_ValueDate` | TField |  | This field will have transaction posting date(value date). It should default last working date when the user opens the record.Validation: System validates the date in this field for processing the clearing transactions. |
| 15 | `CAMB.MICR.OFS.SOURCE` | `CambMicrClrParam_OfsSource` | TField |  | Field is used to define the OFS source to be used for clearing. Valid record of OFS.SOURCE |
| 16 | `CAMB.MICR.MICR.VERSION` | `CambMicrClrParam_MicrVersion` | TField |  | Field to used to define the version to be used for posting the clearing transactions. Valid record of VERSION |
| 17 | `CAMB.MICR.HEADER.MAPPING` | `CambMicrClrParam_HeaderMapping` | TField |  | Field to define the valid DFE record used to Header details. Valid record of DFE.MAPPING |
| 18 | `CAMB.MICR.RECORD.MAPPING` | `CambMicrClrParam_RecordMapping` | TField |  | Field to define the valid DFE record used to record details. Valid record of DFE.MAPPING |
| 19 | `CAMB.MICR.RESERVED.6` | `CambMicrClrParam_Reserved6` | TField |  |  |
| 20 | `CAMB.MICR.RESERVED.5` | `CambMicrClrParam_Reserved5` | TField |  |  |
| 21 | `CAMB.MICR.RESERVED.4` | `CambMicrClrParam_Reserved4` | TField |  |  |
| 22 | `CAMB.MICR.RESERVED.3` | `CambMicrClrParam_Reserved3` | TField |  |  |
| 23 | `CAMB.MICR.RESERVED.2` | `CambMicrClrParam_Reserved2` | TField |  |  |
| 24 | `CAMB.MICR.RESERVED.1` | `CambMicrClrParam_Reserved1` | TField |  |  |
| 25 | `CAMB.MICR.LOCAL.REF` | `CambMicrClrParam_LocalRef` |  |  |  |
| 26 | `CAMB.MICR.OVERRIDE` | `CambMicrClrParam_Override` |  |  |  |
| 27 | `CAMB.MICR.RECORD.STATUS` | `CambMicrClrParam_RecordStatus` | String |  |  |
| 28 | `CAMB.MICR.CURR.NO` | `CambMicrClrParam_CurrNo` | String |  |  |
| 29 | `CAMB.MICR.INPUTTER` | `CambMicrClrParam_Inputter` |  |  |  |
| 30 | `CAMB.MICR.DATE.TIME` | `CambMicrClrParam_DateTime` |  |  |  |
| 31 | `CAMB.MICR.AUTHORISER` | `CambMicrClrParam_Authoriser` | String |  |  |
| 32 | `CAMB.MICR.CO.CODE` | `CambMicrClrParam_CoCode` | String |  |  |
| 33 | `CAMB.MICR.DEPT.CODE` | `CambMicrClrParam_DeptCode` | String |  |  |
| 34 | `CAMB.MICR.AUDITOR.CODE` | `CambMicrClrParam_AuditorCode` | String |  |  |
| 35 | `CAMB.MICR.AUDIT.DATE.TIME` | `CambMicrClrParam_AuditDateTime` | String |  |  |
