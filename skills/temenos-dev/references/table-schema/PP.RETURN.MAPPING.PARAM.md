# PP.RETURN.MAPPING.PARAM — Table Schema

> Source: `INSERTS/I_F.PP.RETURN.MAPPING.PARAM` in `PP_PaymentReturn.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.RMP.Application` | `PpReturnMappingParam_Application` |  |  |  |
| 2 | `PP.RMP.FieldName` | `PpReturnMappingParam_Fieldname` |  |  |  |
| 3 | `PP.RMP.FieldPosition` | `PpReturnMappingParam_Fieldposition` |  |  |  |
| 4 | `PP.RMP.LinkedAppl` | `PpReturnMappingParam_Linkedappl` |  |  |  |
| 5 | `PP.RMP.LinkedApplField` | `PpReturnMappingParam_Linkedapplfield` |  |  |  |
| 6 | `PP.RMP.LinkedApplFieldPosition` | `PpReturnMappingParam_Linkedapplfieldposition` |  |  |  |
| 7 | `PP.RMP.LinkedApplFieldValue` | `PpReturnMappingParam_Linkedapplfieldvalue` |  |  |  |
| 8 | `PP.RMP.Constant` | `PpReturnMappingParam_Constant` |  |  |  |
| 9 | `PP.RMP.OrigPmtAppl` | `PpReturnMappingParam_Origpmtappl` |  |  |  |
| 10 | `PP.RMP.OrigPmtApplField` | `PpReturnMappingParam_Origpmtapplfield` |  |  |  |
| 11 | `PP.RMP.OrigPmtApplFieldPosition` | `PpReturnMappingParam_Origpmtapplfieldposition` |  |  |  |
| 12 | `PP.RMP.OrigLinkedAppl` | `PpReturnMappingParam_Origlinkedappl` |  |  |  |
| 13 | `PP.RMP.OrigLinkedApplField` | `PpReturnMappingParam_Origlinkedapplfield` |  |  |  |
| 14 | `PP.RMP.OrigLinkedApplFieldPos` | `PpReturnMappingParam_Origlinkedapplfieldpos` |  |  |  |
| 15 | `PP.RMP.OrigLinkedApplFieldVal` | `PpReturnMappingParam_Origlinkedapplfieldval` |  |  |  |
| 16 | `PP.RMP.Routine` | `PpReturnMappingParam_Routine` | TField |  | This field can be used by regional/ L3 layer to define specific logic/ conditional mapping which should be applied for any of the fields for return/ reject payment. Routine can be written only if it is not possible to configure using the above mapping fields. Note that there are two arguments for this routine. First argument is an input aurgument which carries FTNumber of return transaction and second argument is an output argument which may contains error information. |
| 17 | `PP.RMP.RESERVED.10` | `PpReturnMappingParam_Reserved10` | TField |  |  |
| 18 | `PP.RMP.RESERVED.9` | `PpReturnMappingParam_Reserved9` | TField |  |  |
| 19 | `PP.RMP.RESERVED.8` | `PpReturnMappingParam_Reserved8` | TField |  |  |
| 20 | `PP.RMP.RESERVED.7` | `PpReturnMappingParam_Reserved7` | TField |  |  |
| 21 | `PP.RMP.RESERVED.6` | `PpReturnMappingParam_Reserved6` | TField |  |  |
| 22 | `PP.RMP.RESERVED.5` | `PpReturnMappingParam_Reserved5` | TField |  |  |
| 23 | `PP.RMP.RESERVED.4` | `PpReturnMappingParam_Reserved4` | TField |  |  |
| 24 | `PP.RMP.RESERVED.3` | `PpReturnMappingParam_Reserved3` | TField |  |  |
| 25 | `PP.RMP.RESERVED.2` | `PpReturnMappingParam_Reserved2` | TField |  |  |
| 26 | `PP.RMP.RESERVED.1` | `PpReturnMappingParam_Reserved1` | TField |  |  |
| 27 | `PP.RMP.RECORD.STATUS` | `PpReturnMappingParam_RecordStatus` | String |  |  |
| 28 | `PP.RMP.CURR.NO` | `PpReturnMappingParam_CurrNo` | String |  |  |
| 29 | `PP.RMP.INPUTTER` | `PpReturnMappingParam_Inputter` |  |  |  |
| 30 | `PP.RMP.DATE.TIME` | `PpReturnMappingParam_DateTime` |  |  |  |
| 31 | `PP.RMP.AUTHORISER` | `PpReturnMappingParam_Authoriser` | String |  |  |
| 32 | `PP.RMP.CO.CODE` | `PpReturnMappingParam_CoCode` | String |  |  |
| 33 | `PP.RMP.DEPT.CODE` | `PpReturnMappingParam_DeptCode` | String |  |  |
| 34 | `PP.RMP.AUDITOR.CODE` | `PpReturnMappingParam_AuditorCode` | String |  |  |
| 35 | `PP.RMP.AUDIT.DATE.TIME` | `PpReturnMappingParam_AuditDateTime` | String |  |  |
