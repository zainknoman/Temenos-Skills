# BRBASE.JD.INTERFACE.MAPPING — Table Schema

> Source: `INSERTS/I_F.BRBASE.JD.INTERFACE.MAPPING` in `BRBASE_InterfaceConnector.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MAP.PARAM.TABLE.NAME` | `BrbaseJdInterfaceMapping_TableName` | TField |  | Holds the application name. It should be a valid STANDARD.SELECTION record |
| 2 | `MAP.PARAM.PROCESS.HOLD` | `BrbaseJdInterfaceMapping_ProcessHold` | TField |  | Flag to indicate if the record should be processed to live or remain to unauthorized status. |
| 3 | `MAP.PARAM.DEFAULT.FIELDS` | `BrbaseJdInterfaceMapping_DefaultFields` | TField |  | Flag to indicate that the record has default field values. |
| 4 | `MAP.PARAM.TAG.NAME` | `BrbaseJdInterfaceMapping_TagName` |  |  |  |
| 5 | `MAP.PARAM.FIELD.MAP` | `BrbaseJdInterfaceMapping_FieldMap` |  |  |  |
| 6 | `MAP.PARAM.DEFAULT.VALUE` | `BrbaseJdInterfaceMapping_DefaultValue` |  |  |  |
| 7 | `MAP.PARAM.VALIDATION.TYPE` | `BrbaseJdInterfaceMapping_ValidationType` |  |  |  |
| 8 | `MAP.PARAM.CONVERSION.FIELD.MAP` | `BrbaseJdInterfaceMapping_ConversionFieldMap` |  |  |  |
| 9 | `MAP.PARAM.RESERVED.2` | `BrbaseJdInterfaceMapping_Reserved2` |  |  |  |
| 10 | `MAP.PARAM.RESERVED.3` | `BrbaseJdInterfaceMapping_Reserved3` |  |  |  |
| 11 | `MAP.PARAM.LOCAL.MULTISET` | `BrbaseJdInterfaceMapping_LocalMultiset` |  |  |  |
| 12 | `MAP.PARAM.ISPBIF.CODE` | `BrbaseJdInterfaceMapping_IspbifCode` |  |  |  |
| 13 | `MAP.PARAM.ISPBIF.DESCRIPTION` | `BrbaseJdInterfaceMapping_IspbifDescription` |  |  |  |
| 14 | `MAP.PARAM.NOSTRO.ACCOUNT` | `BrbaseJdInterfaceMapping_NostroAccount` |  |  |  |
| 15 | `MAP.PARAM.INTERNAL.ACCOUNT` | `BrbaseJdInterfaceMapping_InternalAccount` |  |  |  |
| 16 | `MAP.PARAM.RESERVED.4` | `BrbaseJdInterfaceMapping_Reserved4` |  |  |  |
| 17 | `MAP.PARAM.RESERVED.5` | `BrbaseJdInterfaceMapping_Reserved5` |  |  |  |
| 18 | `MAP.PARAM.RESERVED.6` | `BrbaseJdInterfaceMapping_Reserved6` |  |  |  |
| 19 | `MAP.PARAM.ISPBIF.TYPE` | `BrbaseJdInterfaceMapping_IspbifType` |  |  |  |
| 20 | `MAP.PARAM.NAMESPACE` | `BrbaseJdInterfaceMapping_Namespace` |  |  |  |
| 21 | `MAP.PARAM.URL` | `BrbaseJdInterfaceMapping_Url` |  |  |  |
| 22 | `MAP.PARAM.OPERATION` | `BrbaseJdInterfaceMapping_Operation` |  |  |  |
| 23 | `MAP.PARAM.TIMEOUT` | `BrbaseJdInterfaceMapping_Timeout` | TField |  | Contains timeout for the responses |
| 24 | `MAP.PARAM.XSLT.REQUEST` | `BrbaseJdInterfaceMapping_XsltRequest` |  |  |  |
| 25 | `MAP.PARAM.USER` | `BrbaseJdInterfaceMapping_User` | TField |  | Field to store the user of the service |
| 26 | `MAP.PARAM.PASSWORD` | `BrbaseJdInterfaceMapping_Password` | TField |  | Field to store the password of the user |
| 27 | `MAP.PARAM.FILE.CONTROL` | `BrbaseJdInterfaceMapping_FileControl` | TField |  | Contains the control number of the outgoing files. |
| 28 | `MAP.PARAM.SENDER.PARTICIPANT` | `BrbaseJdInterfaceMapping_SenderParticipant` | TField |  | Receiving Agency Number. |
| 29 | `MAP.PARAM.DV.SENDER.PARTICIPANT` | `BrbaseJdInterfaceMapping_DvSenderParticipant` | TField |  | Receiving Agency Number Verification Digit. |
| 30 | `MAP.PARAM.PROCESSOR` | `BrbaseJdInterfaceMapping_Processor` | TField |  | Contains the processor code. Constant equal to �001� |
| 31 | `MAP.PARAM.DV.PROCESSOR` | `BrbaseJdInterfaceMapping_DvProcessor` | TField |  | Contains the verification digit of the processor. Constant equal to �9� |
| 32 | `MAP.PARAM.SOURCE` | `BrbaseJdInterfaceMapping_Source` | TField |  | Holds the place of the Origin Code. |
| 33 | `MAP.PARAM.SHIPPING.INDICATOR` | `BrbaseJdInterfaceMapping_ShippingIndicator` | TField |  | Stores shipping indicator code. |
| 34 | `MAP.PARAM.FILE.VERSION` | `BrbaseJdInterfaceMapping_FileVersion` | TField |  | Stores the version for outgoing files. |
| 35 | `MAP.PARAM.PROCESSOR.PARTIAL` | `BrbaseJdInterfaceMapping_ProcessorPartial` | TField |  | Holds the processor partial number where file was generated. |
| 36 | `MAP.PARAM.END.FLAG` | `BrbaseJdInterfaceMapping_EndFlag` | TField |  | Stores the end of processing indicator. Constant equal to: - �FIM� in the last partial - � � in the other cases. |
| 37 | `MAP.PARAM.RECIPIENT.PARTICIPANT` | `BrbaseJdInterfaceMapping_RecipientParticipant` | TField |  | Code of the financial institution that receives the file. |
| 38 | `MAP.PARAM.FILE.SOURCE` | `BrbaseJdInterfaceMapping_FileSource` | TField |  | Contains the source file code. |
| 39 | `MAP.PARAM.REPROC.INDICATOR` | `BrbaseJdInterfaceMapping_ReprocIndicator` | TField |  | File reprocessing indicator. |
| 40 | `MAP.PARAM.FILE.VALUE` | `BrbaseJdInterfaceMapping_FileValue` | TField |  | Field used to store the total amount of records file detail. |
| 41 | `MAP.PARAM.FILE.PRODUCT.CODE` | `BrbaseJdInterfaceMapping_FileProductCode` |  |  |  |
| 42 | `MAP.PARAM.RESERVED.7` | `BrbaseJdInterfaceMapping_Reserved7` |  |  |  |
| 43 | `MAP.PARAM.RESERVED.8` | `BrbaseJdInterfaceMapping_Reserved8` |  |  |  |
| 44 | `MAP.PARAM.RESERVED.9` | `BrbaseJdInterfaceMapping_Reserved9` |  |  |  |
| 45 | `MAP.PARAM.FILE.PRODUCT.DESCRIPTION` | `BrbaseJdInterfaceMapping_FileProductDescription` |  |  |  |
| 46 | `MAP.PARAM.RESERVED.10` | `BrbaseJdInterfaceMapping_Reserved10` | TField |  | Field for future use. |
| 47 | `MAP.PARAM.RESERVED.11` | `BrbaseJdInterfaceMapping_Reserved11` | TField |  | Field for future use. |
| 48 | `MAP.PARAM.RESERVED.12` | `BrbaseJdInterfaceMapping_Reserved12` | TField |  | Field for future use. |
| 49 | `MAP.PARAM.RESERVED.13` | `BrbaseJdInterfaceMapping_Reserved13` | TField |  | Field for future use. |
| 50 | `MAP.PARAM.RESERVED.14` | `BrbaseJdInterfaceMapping_Reserved14` | TField |  | Field for future use. |
| 51 | `MAP.PARAM.RESERVED.15` | `BrbaseJdInterfaceMapping_Reserved15` | TField |  | Field for future use. |
| 52 | `MAP.PARAM.RESERVED.16` | `BrbaseJdInterfaceMapping_Reserved16` | TField |  | Field for future use. |
| 53 | `MAP.PARAM.RESERVED.17` | `BrbaseJdInterfaceMapping_Reserved17` | TField |  | Field for future use. |
| 54 | `MAP.PARAM.RESERVED.18` | `BrbaseJdInterfaceMapping_Reserved18` | TField |  | Field for future use. |
| 55 | `MAP.PARAM.RESERVED.19` | `BrbaseJdInterfaceMapping_Reserved19` | TField |  | Field for future use. |
| 56 | `MAP.PARAM.RESERVED.20` | `BrbaseJdInterfaceMapping_Reserved20` | TField |  | Field for future use. |
| 57 | `MAP.PARAM.LOCAL.REF` | `BrbaseJdInterfaceMapping_LocalRef` |  |  |  |
| 58 | `MAP.PARAM.OVERRIDE` | `BrbaseJdInterfaceMapping_Override` |  |  |  |
| 59 | `MAP.PARAM.RECORD.STATUS` | `BrbaseJdInterfaceMapping_RecordStatus` | String |  |  |
| 60 | `MAP.PARAM.CURR.NO` | `BrbaseJdInterfaceMapping_CurrNo` | String |  |  |
| 61 | `MAP.PARAM.INPUTTER` | `BrbaseJdInterfaceMapping_Inputter` |  |  |  |
| 62 | `MAP.PARAM.DATE.TIME` | `BrbaseJdInterfaceMapping_DateTime` |  |  |  |
| 63 | `MAP.PARAM.AUTHORISER` | `BrbaseJdInterfaceMapping_Authoriser` | String |  |  |
| 64 | `MAP.PARAM.CO.CODE` | `BrbaseJdInterfaceMapping_CoCode` | String |  |  |
| 65 | `MAP.PARAM.DEPT.CODE` | `BrbaseJdInterfaceMapping_DeptCode` | String |  |  |
| 66 | `MAP.PARAM.AUDITOR.CODE` | `BrbaseJdInterfaceMapping_AuditorCode` | String |  |  |
| 67 | `MAP.PARAM.AUDIT.DATE.TIME` | `BrbaseJdInterfaceMapping_AuditDateTime` | String |  |  |
