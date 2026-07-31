# CMBASE.BATCH.INTRF.PARAM — Table Schema

> Source: `INSERTS/I_F.CMBASE.BATCH.INTRF.PARAM` in `CMBASE_InterfaceBatchExtract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CMBASE.INTRF.MAIN.APPLICATION` | `CmbaseBatchIntrfParam_MainApplication` | TField |  | This field holds the application from which the records will be filtered for the extraction process. Vettingtable � FILE.CONTROL |
| 2 | `CMBASE.INTRF.REL.APPLICATION` | `CmbaseBatchIntrfParam_RelApplication` |  |  |  |
| 3 | `CMBASE.INTRF.REL.APPL.FIELD.INFO` | `CmbaseBatchIntrfParam_RelApplFieldInfo` |  |  |  |
| 4 | `CMBASE.INTRF.FILE.DIRECTORY` | `CmbaseBatchIntrfParam_FileDirectory` | TField |  | This field is required to mention the output file directory. |
| 5 | `CMBASE.INTRF.FILTER.API` | `CmbaseBatchIntrfParam_FilterApi` | TField |  | This field has vetting to - EB.API Attached routine should accept one argument. If the current argument passed to this routine not to be executed inthe batch extract, empty the incoming argument |
| 6 | `CMBASE.INTRF.OUTPUT.FILE.NAME` | `CmbaseBatchIntrfParam_OutputFileName` | TField |  |  |
| 7 | `CMBASE.INTRF.LOCAL.REF` | `CmbaseBatchIntrfParam_LocalRef` |  |  |  |
| 8 | `CMBASE.INTRF.ENABLE.BULK` | `CmbaseBatchIntrfParam_EnableBulk` | TField |  | This field is used to enable the bulking of the generated xml files |
| 9 | `CMBASE.INTRF.FILE.SEQUENCE.ID` | `CmbaseBatchIntrfParam_FileSequenceId` | TField |  | If this field is inputted, the value will be used during the bulking process to update the sequence number Format: Locking Record ID * Type of Sequence (A - Alphanumeric, N - Numeric) * Batch Common Variable or Constant Example: BATCH.EXTRACT*N*!TODAY BATCH.EXTRACT*A*202008 BATCH.EXTRACT*A*!COMPANY |
| 10 | `CMBASE.INTRF.RESERVED.3` | `CmbaseBatchIntrfParam_Reserved3` | TField |  | This field is reserved for future use |
| 11 | `CMBASE.INTRF.RESERVED.2` | `CmbaseBatchIntrfParam_Reserved2` | TField |  | This field is reserved for future use |
| 12 | `CMBASE.INTRF.RESERVED.1` | `CmbaseBatchIntrfParam_Reserved1` | TField |  | This field is reserved for future use |
| 13 | `CMBASE.INTRF.OVERRIDE` | `CmbaseBatchIntrfParam_Override` |  |  |  |
| 14 | `CMBASE.INTRF.RECORD.STATUS` | `CmbaseBatchIntrfParam_RecordStatus` | String |  |  |
| 15 | `CMBASE.INTRF.CURR.NO` | `CmbaseBatchIntrfParam_CurrNo` | String |  |  |
| 16 | `CMBASE.INTRF.INPUTTER` | `CmbaseBatchIntrfParam_Inputter` |  |  |  |
| 17 | `CMBASE.INTRF.DATE.TIME` | `CmbaseBatchIntrfParam_DateTime` |  |  |  |
| 18 | `CMBASE.INTRF.AUTHORISER` | `CmbaseBatchIntrfParam_Authoriser` | String |  |  |
| 19 | `CMBASE.INTRF.CO.CODE` | `CmbaseBatchIntrfParam_CoCode` | String |  |  |
| 20 | `CMBASE.INTRF.DEPT.CODE` | `CmbaseBatchIntrfParam_DeptCode` | String |  |  |
| 21 | `CMBASE.INTRF.AUDITOR.CODE` | `CmbaseBatchIntrfParam_AuditorCode` | String |  |  |
| 22 | `CMBASE.INTRF.AUDIT.DATE.TIME` | `CmbaseBatchIntrfParam_AuditDateTime` | String |  |  |
| 23 | `CMBASE.INTRF.MAIN.APPL.EXTRACT.FLDS` | `CmbaseBatchIntrfParam_MainApplExtractFlds` |  |  |  |
| 24 | `CMBASE.INTRF.REL.APPL.EXTRACT.FLDS` | `CmbaseBatchIntrfParam_RelApplExtractFlds` |  |  |  |
| 25 | `CMBASE.INTRF.REL.APPL.ID.FIELD` | `CmbaseBatchIntrfParam_RelApplIdField` |  |  |  |
| 26 | `CMBASE.INTRF.REL.APPL.ID.TRANSFORM` | `CmbaseBatchIntrfParam_RelApplIdTransform` |  |  |  |
| 27 | `CMBASE.INTRF.REL.APPL.ALIAS` | `CmbaseBatchIntrfParam_RelApplAlias` |  |  |  |
| 28 | `CMBASE.INTRF.SECONDARY.REL.APPL` | `CmbaseBatchIntrfParam_SecondaryRelAppl` |  |  |  |
