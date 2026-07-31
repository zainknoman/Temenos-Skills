# PP.PROCESSING.SEQUENCE — Table Schema

> Source: `INSERTS/I_F.PP.PROCESSING.SEQUENCE` in `PP_InboundCodeWordService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.PSS.CompanyID` | `PpProcessingSequence_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.PSS.ProcessingSequenceDesc` | `PpProcessingSequence_Processingsequencedesc` |  |  |  |
| 3 | `PP.PSS.ProcessingSequenceRoutineName` | `PpProcessingSequence_Processingsequenceroutinename` | TField |  | Indicates the name of the routine that needs to be executed as part of the processing sequence. Example: InboundCodeWordService.setIPSYMT101ProcessFlags,InboundCodeWordService.setIPSYMT103ProcessFlags Validation Rules:Valid EB.API record of type 'Basic', if the hook is of JBCroutine 255 alphanumeric characters. Must be a valid routine. Specify either A jBC subroutine name The routine has six passed parameters and expected to update the processing sequence and decide whether to include the codeword for special processing or not. For java implementations: An EB.API record of type METHOD which implements an interface defined in the EB.API record PP.PROCESSING.SEQUENCE.RtnName.HOOK. This field currently supports the PaymentLifecycle.updateProcessSequence() method. The PaymentLifecycle class is in the com.temenos.t24.api.hook.payments package which is in PP_PaymentLifecycleHook.jar shipped with T24. |
| 4 | `PP.PSS.InboundProcessingSequenceFlag` | `PpProcessingSequence_Inboundprocessingsequenceflag` | TField |  | Indicates whether processing sequence is applicable for inbound code word processing. Possible values: Y - Yes N - No Blank |
| 5 | `PP.PSS.OutboundProcessingSequenceFlag` | `PpProcessingSequence_Outboundprocessingsequenceflag` | TField |  | Indicates whether processing sequence is applicable for outbound code word processing. Possible values: Y - Yes N - No Blank |
| 6 | `PP.PSS.RESERVED.5` | `PpProcessingSequence_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.PSS.RESERVED.4` | `PpProcessingSequence_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 8 | `PP.PSS.RESERVED.3` | `PpProcessingSequence_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 9 | `PP.PSS.RESERVED.2` | `PpProcessingSequence_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 10 | `PP.PSS.RESERVED.1` | `PpProcessingSequence_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 11 | `PP.PSS.LOCAL.REF` | `PpProcessingSequence_LocalRef` |  |  |  |
| 12 | `PP.PSS.OVERRIDE` | `PpProcessingSequence_Override` |  |  |  |
| 13 | `PP.PSS.RECORD.STATUS` | `PpProcessingSequence_RecordStatus` | String |  |  |
| 14 | `PP.PSS.CURR.NO` | `PpProcessingSequence_CurrNo` | String |  |  |
| 15 | `PP.PSS.INPUTTER` | `PpProcessingSequence_Inputter` |  |  |  |
| 16 | `PP.PSS.DATE.TIME` | `PpProcessingSequence_DateTime` |  |  |  |
| 17 | `PP.PSS.AUTHORISER` | `PpProcessingSequence_Authoriser` | String |  |  |
| 18 | `PP.PSS.CO.CODE` | `PpProcessingSequence_CoCode` | String |  |  |
| 19 | `PP.PSS.DEPT.CODE` | `PpProcessingSequence_DeptCode` | String |  |  |
| 20 | `PP.PSS.AUDITOR.CODE` | `PpProcessingSequence_AuditorCode` | String |  |  |
| 21 | `PP.PSS.AUDIT.DATE.TIME` | `PpProcessingSequence_AuditDateTime` | String |  |  |
