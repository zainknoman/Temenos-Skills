# FEDWIRE.MESSAGE.SUBTYPE — Table Schema

> Source: `INSERTS/I_F.FEDWIRE.MESSAGE.SUBTYPE` in `USRTGS_Fedwire.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FWMST.DESC` | `FedwireMessageSubtype_Desc` |  |  |  |
| 2 | `FWMST.SHORT.NAME` | `FedwireMessageSubtype_ShortName` |  |  |  |
| 3 | `FWMST.RESERVED.10` | `FedwireMessageSubtype_Reserved10` | TField |  |  |
| 4 | `FWMST.RESERVED.9` | `FedwireMessageSubtype_Reserved9` | TField |  |  |
| 5 | `FWMST.RESERVED.8` | `FedwireMessageSubtype_Reserved8` | TField |  |  |
| 6 | `FWMST.RESERVED.7` | `FedwireMessageSubtype_Reserved7` | TField |  |  |
| 7 | `FWMST.RESERVED.6` | `FedwireMessageSubtype_Reserved6` | TField |  |  |
| 8 | `FWMST.RESERVED.5` | `FedwireMessageSubtype_Reserved5` | TField |  |  |
| 9 | `FWMST.RESERVED.4` | `FedwireMessageSubtype_Reserved4` | TField |  |  |
| 10 | `FWMST.RESERVED.3` | `FedwireMessageSubtype_Reserved3` | TField |  |  |
| 11 | `FWMST.RESERVED.2` | `FedwireMessageSubtype_Reserved2` | TField |  |  |
| 12 | `FWMST.RESERVED.1` | `FedwireMessageSubtype_Reserved1` | TField |  |  |
| 13 | `FWMST.RECORD.STATUS` | `FedwireMessageSubtype_RecordStatus` | String |  |  |
| 14 | `FWMST.CURR.NO` | `FedwireMessageSubtype_CurrNo` | String |  |  |
| 15 | `FWMST.INPUTTER` | `FedwireMessageSubtype_Inputter` |  |  |  |
| 16 | `FWMST.DATE.TIME` | `FedwireMessageSubtype_DateTime` |  |  |  |
| 17 | `FWMST.AUTHORISER` | `FedwireMessageSubtype_Authoriser` | String |  |  |
| 18 | `FWMST.CO.CODE` | `FedwireMessageSubtype_CoCode` | String |  |  |
| 19 | `FWMST.DEPT.CODE` | `FedwireMessageSubtype_DeptCode` | String |  |  |
| 20 | `FWMST.AUDITOR.CODE` | `FedwireMessageSubtype_AuditorCode` | String |  |  |
| 21 | `FWMST.AUDIT.DATE.TIME` | `FedwireMessageSubtype_AuditDateTime` | String |  |  |
