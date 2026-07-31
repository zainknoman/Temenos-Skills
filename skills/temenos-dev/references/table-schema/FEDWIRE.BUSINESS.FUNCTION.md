# FEDWIRE.BUSINESS.FUNCTION — Table Schema

> Source: `INSERTS/I_F.FEDWIRE.BUSINESS.FUNCTION` in `USRTGS_Fedwire.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FWBF.DESC` | `FedwireBusinessFunction_Desc` |  |  |  |
| 2 | `FWBF.SHORT.NAME` | `FedwireBusinessFunction_ShortName` |  |  |  |
| 3 | `FWBF.TYPE.CODE` | `FedwireBusinessFunction_TypeCode` |  |  |  |
| 4 | `FWBF.SUBTYPE.CODE` | `FedwireBusinessFunction_SubtypeCode` |  |  |  |
| 5 | `FWBF.RESERVED.10` | `FedwireBusinessFunction_Reserved10` |  |  |  |
| 6 | `FWBF.RESERVED.9` | `FedwireBusinessFunction_Reserved9` |  |  |  |
| 7 | `FWBF.RESERVED.8` | `FedwireBusinessFunction_Reserved8` |  |  |  |
| 8 | `FWBF.RESERVED.7` | `FedwireBusinessFunction_Reserved7` | TField |  |  |
| 9 | `FWBF.RESERVED.6` | `FedwireBusinessFunction_Reserved6` | TField |  |  |
| 10 | `FWBF.RESERVED.5` | `FedwireBusinessFunction_Reserved5` | TField |  |  |
| 11 | `FWBF.RESERVED.4` | `FedwireBusinessFunction_Reserved4` | TField |  |  |
| 12 | `FWBF.RESERVED.3` | `FedwireBusinessFunction_Reserved3` | TField |  |  |
| 13 | `FWBF.RESERVED.2` | `FedwireBusinessFunction_Reserved2` | TField |  |  |
| 14 | `FWBF.RESERVED.1` | `FedwireBusinessFunction_Reserved1` | TField |  |  |
| 15 | `FWBF.RECORD.STATUS` | `FedwireBusinessFunction_RecordStatus` | String |  |  |
| 16 | `FWBF.CURR.NO` | `FedwireBusinessFunction_CurrNo` | String |  |  |
| 17 | `FWBF.INPUTTER` | `FedwireBusinessFunction_Inputter` |  |  |  |
| 18 | `FWBF.DATE.TIME` | `FedwireBusinessFunction_DateTime` |  |  |  |
| 19 | `FWBF.AUTHORISER` | `FedwireBusinessFunction_Authoriser` | String |  |  |
| 20 | `FWBF.CO.CODE` | `FedwireBusinessFunction_CoCode` | String |  |  |
| 21 | `FWBF.DEPT.CODE` | `FedwireBusinessFunction_DeptCode` | String |  |  |
| 22 | `FWBF.AUDITOR.CODE` | `FedwireBusinessFunction_AuditorCode` | String |  |  |
| 23 | `FWBF.AUDIT.DATE.TIME` | `FedwireBusinessFunction_AuditDateTime` | String |  |  |
