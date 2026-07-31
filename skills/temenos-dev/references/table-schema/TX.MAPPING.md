# TX.MAPPING — Table Schema

> Source: `INSERTS/I_F.TX.MAPPING` in `TX_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TE.MAP.DESCRIPTION` | `TxMapping_Description` | A (alphanumeric) |  | Description of the Tx Mapping record. Validations : 0 - 40 type A (alphanumeric) characters. |
| 2 | `TE.MAP.OUTPUT.STYLE` | `TxMapping_OutputStyle` | TField |  | Specifies the style in which data is sent or received from T24 for Tax engine processing. Validations : Should contain the following valid data CSV/T24/XML CSV - Sends data separated by Comma to a Unix file T24 - Sends the data to a T24 Work file. XML - Sends the data in XML format. (currently not supported) |
| 3 | `TE.MAP.HANDOFF.PATH` | `TxMapping_HandoffPath` | TField |  | Specifies the path for the output file. Validations : For CSV output style it contains the entire file path. The output record is created in the path specified. For T24 output style it contains the valid T24 work file name with a file control. |
| 4 | `TE.MAP.COMPLETE.STATUS` | `TxMapping_CompleteStatus` | TField |  | Specifies the position in the workfile where the Black box routine updates the status of tax engine processing. Validations : Numeric value of 2 characters length. |
| 5 | `TE.MAP.SCHEDULE` | `TxMapping_Schedule` | TField |  | This field specifies when the Tax processing is going to happen. Whether immediate or through phantom jobs. Validations : Should contains the following values, LAUNCH.AND.WAIT - This triggers the Tax engine processing immediately when the transaction is input. LAUNCH.AND.RETURN - Tax engine is not triggered immediately. It is carried over by the phantom jobs after the transaction is committed. Currently this is not supported |
| 6 | `TE.MAP.TRANSACTION.FILE` | `TxMapping_TransactionFile` | TField |  | Gives the Application for which the mapping belongs. Validations : Valid T24 application name with a valid PGM.FILE of TYPE = L/U/H |
| 7 | `TE.MAP.BLACK.BOX` | `TxMapping_BlackBox` | TField |  | The name of the Black box routine triggered for Tax processing. The routine can be a T24 or an external routine. Validations : The routine should have a valid PGM.FILE entry with TYPE = S if the Output style is 'T24'. |
| 8 | `TE.MAP.TAX.CCY.POS` | `TxMapping_TaxCcyPos` | TField |  | The position in the workfile where the Black box processing returns the Tax currency. Validations : Numeric value of 2 characters long. |
| 9 | `TE.MAP.TAX.AMT.POS` | `TxMapping_TaxAmtPos` | TField |  | The position in the workfile where the Black box processing returns the Tax amount. Validations : Numeric value of 2 characters long. |
| 10 | `TE.MAP.FILE.NAME` | `TxMapping_FileName` |  |  |  |
| 11 | `TE.MAP.RECORD.ID` | `TxMapping_RecordId` |  |  |  |
| 12 | `TE.MAP.CONVERSION` | `TxMapping_Conversion` |  |  |  |
| 13 | `TE.MAP.FROM.FIELD` | `TxMapping_FromField` |  |  |  |
| 14 | `TE.MAP.TO.FIELD` | `TxMapping_ToField` |  |  |  |
| 15 | `TE.MAP.FIELD.NAME` | `TxMapping_FieldName` |  |  |  |
| 16 | `TE.MAP.RET.FLD.POS` | `TxMapping_RetFldPos` |  |  |  |
| 17 | `TE.MAP.RET.FLD.CONV` | `TxMapping_RetFldConv` |  |  |  |
| 18 | `TE.MAP.ROUTINE` | `TxMapping_Routine` |  |  |  |
| 19 | `TE.MAP.RESERVED12` | `TxMapping_Reserved12` | TField |  |  |
| 20 | `TE.MAP.RESERVED11` | `TxMapping_Reserved11` | TField |  |  |
| 21 | `TE.MAP.RESERVED10` | `TxMapping_Reserved10` | TField |  |  |
| 22 | `TE.MAP.RESERVED9` | `TxMapping_Reserved9` | TField |  |  |
| 23 | `TE.MAP.RESERVED8` | `TxMapping_Reserved8` | TField |  |  |
| 24 | `TE.MAP.RESERVED7` | `TxMapping_Reserved7` | TField |  |  |
| 25 | `TE.MAP.LOCAL.REF` | `TxMapping_LocalRef` |  |  |  |
| 26 | `TE.MAP.OVERRIDE` | `TxMapping_Override` |  |  |  |
| 27 | `TE.MAP.RECORD.STATUS` | `TxMapping_RecordStatus` | String |  |  |
| 28 | `TE.MAP.CURR.NO` | `TxMapping_CurrNo` | String |  |  |
| 29 | `TE.MAP.INPUTTER` | `TxMapping_Inputter` |  |  |  |
| 30 | `TE.MAP.DATE.TIME` | `TxMapping_DateTime` |  |  |  |
| 31 | `TE.MAP.AUTHORISER` | `TxMapping_Authoriser` | String |  |  |
| 32 | `TE.MAP.CO.CODE` | `TxMapping_CoCode` | String |  |  |
| 33 | `TE.MAP.DEPT.CODE` | `TxMapping_DeptCode` | String |  |  |
| 34 | `TE.MAP.AUDITOR.CODE` | `TxMapping_AuditorCode` | String |  |  |
| 35 | `TE.MAP.AUDIT.DATE.TIME` | `TxMapping_AuditDateTime` | String |  |  |
