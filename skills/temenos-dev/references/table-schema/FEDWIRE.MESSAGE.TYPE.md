# FEDWIRE.MESSAGE.TYPE — Table Schema

> Source: `INSERTS/I_F.FEDWIRE.MESSAGE.TYPE` in `USRTGS_Fedwire.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FWMT.DESC` | `FedwireMessageType_Desc` |  |  |  |
| 2 | `FWMT.SHORT.NAME` | `FedwireMessageType_ShortName` |  |  |  |
| 3 | `FWMT.RESERVED.10` | `FedwireMessageType_Reserved10` | TField |  |  |
| 4 | `FWMT.RESERVED.9` | `FedwireMessageType_Reserved9` | TField |  |  |
| 5 | `FWMT.RESERVED.8` | `FedwireMessageType_Reserved8` | TField |  |  |
| 6 | `FWMT.RESERVED.7` | `FedwireMessageType_Reserved7` | TField |  |  |
| 7 | `FWMT.RESERVED.6` | `FedwireMessageType_Reserved6` | TField |  |  |
| 8 | `FWMT.RESERVED.5` | `FedwireMessageType_Reserved5` | TField |  |  |
| 9 | `FWMT.RESERVED.4` | `FedwireMessageType_Reserved4` | TField |  |  |
| 10 | `FWMT.RESERVED.3` | `FedwireMessageType_Reserved3` | TField |  |  |
| 11 | `FWMT.RESERVED.2` | `FedwireMessageType_Reserved2` | TField |  |  |
| 12 | `FWMT.RESERVED.1` | `FedwireMessageType_Reserved1` | TField |  |  |
| 13 | `FWMT.RECORD.STATUS` | `FedwireMessageType_RecordStatus` | String |  |  |
| 14 | `FWMT.CURR.NO` | `FedwireMessageType_CurrNo` | String |  |  |
| 15 | `FWMT.INPUTTER` | `FedwireMessageType_Inputter` |  |  |  |
| 16 | `FWMT.DATE.TIME` | `FedwireMessageType_DateTime` |  |  |  |
| 17 | `FWMT.AUTHORISER` | `FedwireMessageType_Authoriser` | String |  |  |
| 18 | `FWMT.CO.CODE` | `FedwireMessageType_CoCode` | String |  |  |
| 19 | `FWMT.DEPT.CODE` | `FedwireMessageType_DeptCode` | String |  |  |
| 20 | `FWMT.AUDITOR.CODE` | `FedwireMessageType_AuditorCode` | String |  |  |
| 21 | `FWMT.AUDIT.DATE.TIME` | `FedwireMessageType_AuditDateTime` | String |  |  |
