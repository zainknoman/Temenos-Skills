# TNCUIN.POSTAL.CODE — Table Schema

> Source: `INSERTS/I_F.TNCUIN.POSTAL.CODE` in `TNCUIN_CustomerCRM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNCUIN.POST.DESCRIPTION` | `TncuinPostalCode_Description` |  |  |  |
| 2 | `TNCUIN.POST.DELEGATES` | `TncuinPostalCode_Delegates` |  |  |  |
| 3 | `TNCUIN.POST.POSTAL.CODE` | `TncuinPostalCode_PostalCode` |  |  |  |
| 4 | `TNCUIN.POST.LOCAL.REF` | `TncuinPostalCode_LocalRef` |  |  |  |
| 5 | `TNCUIN.POST.RESERVED.5` | `TncuinPostalCode_Reserved5` | TField |  |  |
| 6 | `TNCUIN.POST.RESERVED.4` | `TncuinPostalCode_Reserved4` | TField |  |  |
| 7 | `TNCUIN.POST.RESERVED.3` | `TncuinPostalCode_Reserved3` | TField |  |  |
| 8 | `TNCUIN.POST.RESERVED.2` | `TncuinPostalCode_Reserved2` | TField |  |  |
| 9 | `TNCUIN.POST.RESERVED.1` | `TncuinPostalCode_Reserved1` | TField |  |  |
| 10 | `TNCUIN.POST.OVERRIDE` | `TncuinPostalCode_Override` |  |  |  |
| 11 | `TNCUIN.POST.RECORD.STATUS` | `TncuinPostalCode_RecordStatus` | String |  |  |
| 12 | `TNCUIN.POST.CURR.NO` | `TncuinPostalCode_CurrNo` | String |  |  |
| 13 | `TNCUIN.POST.INPUTTER` | `TncuinPostalCode_Inputter` |  |  |  |
| 14 | `TNCUIN.POST.DATE.TIME` | `TncuinPostalCode_DateTime` |  |  |  |
| 15 | `TNCUIN.POST.AUTHORISER` | `TncuinPostalCode_Authoriser` | String |  |  |
| 16 | `TNCUIN.POST.CO.CODE` | `TncuinPostalCode_CoCode` | String |  |  |
| 17 | `TNCUIN.POST.DEPT.CODE` | `TncuinPostalCode_DeptCode` | String |  |  |
| 18 | `TNCUIN.POST.AUDITOR.CODE` | `TncuinPostalCode_AuditorCode` | String |  |  |
| 19 | `TNCUIN.POST.AUDIT.DATE.TIME` | `TncuinPostalCode_AuditDateTime` | String |  |  |
