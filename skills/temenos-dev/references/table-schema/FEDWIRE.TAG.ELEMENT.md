# FEDWIRE.TAG.ELEMENT — Table Schema

> Source: `INSERTS/I_F.FEDWIRE.TAG.ELEMENT` in `USRTGS_Fedwire.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FWTE.DESC` | `FedwireTagElement_Desc` |  |  |  |
| 2 | `FWTE.SHORT.NAME` | `FedwireTagElement_ShortName` |  |  |  |
| 3 | `FWTE.REPORT.ELEMENT` | `FedwireTagElement_ReportElement` | TField | No | Field to denote whether the constructed element value should be updated in MESSAGE.TRACKER table. Possible values: YES NO Optional input. |
| 4 | `FWTE.REPORT.FIELD` | `FedwireTagElement_ReportField` | TField | No | Contains the field in MESSAGE.TRACKER table where the element value should be populated. Optional input. Input allowed only when REPORT.ELEMENT is YES |
| 5 | `FWTE.RESERVED.15` | `FedwireTagElement_Reserved15` |  |  |  |
| 6 | `FWTE.APPLICATION` | `FedwireTagElement_Application` |  |  |  |
| 7 | `FWTE.FIELD.NAME` | `FedwireTagElement_FieldName` |  |  |  |
| 8 | `FWTE.CONVERSION` | `FedwireTagElement_Conversion` |  |  |  |
| 9 | `FWTE.RESERVED.14` | `FedwireTagElement_Reserved14` |  |  |  |
| 10 | `FWTE.RESERVED.13` | `FedwireTagElement_Reserved13` |  |  |  |
| 11 | `FWTE.EDIT.PROPERTY` | `FedwireTagElement_EditProperty` |  |  |  |
| 12 | `FWTE.TAG` | `FedwireTagElement_Tag` |  |  |  |
| 13 | `FWTE.TAG.ELEMENT` | `FedwireTagElement_TagElement` |  |  |  |
| 14 | `FWTE.OPERAND` | `FedwireTagElement_Operand` |  |  |  |
| 15 | `FWTE.VALUE.FROM` | `FedwireTagElement_ValueFrom` |  |  |  |
| 16 | `FWTE.VALUE.TO` | `FedwireTagElement_ValueTo` |  |  |  |
| 17 | `FWTE.AND.OR` | `FedwireTagElement_AndOr` |  |  |  |
| 18 | `FWTE.RESERVED.12` | `FedwireTagElement_Reserved12` |  |  |  |
| 19 | `FWTE.RESERVED.11` | `FedwireTagElement_Reserved11` |  |  |  |
| 20 | `FWTE.RESERVED.10` | `FedwireTagElement_Reserved10` | TField |  |  |
| 21 | `FWTE.RESERVED.9` | `FedwireTagElement_Reserved9` | TField |  |  |
| 22 | `FWTE.RESERVED.8` | `FedwireTagElement_Reserved8` | TField |  |  |
| 23 | `FWTE.RESERVED.7` | `FedwireTagElement_Reserved7` | TField |  |  |
| 24 | `FWTE.RESERVED.6` | `FedwireTagElement_Reserved6` | TField |  |  |
| 25 | `FWTE.RESERVED.5` | `FedwireTagElement_Reserved5` | TField |  |  |
| 26 | `FWTE.RESERVED.4` | `FedwireTagElement_Reserved4` | TField |  |  |
| 27 | `FWTE.RESERVED.3` | `FedwireTagElement_Reserved3` | TField |  |  |
| 28 | `FWTE.RESERVED.2` | `FedwireTagElement_Reserved2` | TField |  |  |
| 29 | `FWTE.RESERVED.1` | `FedwireTagElement_Reserved1` | TField |  |  |
| 30 | `FWTE.OVERRIDE` | `FedwireTagElement_Override` |  |  |  |
| 31 | `FWTE.RECORD.STATUS` | `FedwireTagElement_RecordStatus` | String |  |  |
| 32 | `FWTE.CURR.NO` | `FedwireTagElement_CurrNo` | String |  |  |
| 33 | `FWTE.INPUTTER` | `FedwireTagElement_Inputter` |  |  |  |
| 34 | `FWTE.DATE.TIME` | `FedwireTagElement_DateTime` |  |  |  |
| 35 | `FWTE.AUTHORISER` | `FedwireTagElement_Authoriser` | String |  |  |
| 36 | `FWTE.CO.CODE` | `FedwireTagElement_CoCode` | String |  |  |
| 37 | `FWTE.DEPT.CODE` | `FedwireTagElement_DeptCode` | String |  |  |
| 38 | `FWTE.AUDITOR.CODE` | `FedwireTagElement_AuditorCode` | String |  |  |
| 39 | `FWTE.AUDIT.DATE.TIME` | `FedwireTagElement_AuditDateTime` | String |  |  |
