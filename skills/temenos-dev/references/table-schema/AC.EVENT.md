# AC.EVENT — Table Schema

> Source: `INSERTS/I_F.AC.EVENT` in `AC_SoftAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.EV.DESCRIPTION` | `AcEvent_Description` | TField |  | Description of the event. |
| 2 | `AC.EV.FULL.DESCRIPTION` | `AcEvent_FullDescription` |  |  |  |
| 3 | `AC.EV.CREDIT.PREFIX` | `AcEvent_CreditPrefix` | TField |  |  |
| 4 | `AC.EV.DEBIT.PREFIX` | `AcEvent_DebitPrefix` | TField |  |  |
| 5 | `AC.EV.RESERVED.3` | `AcEvent_Reserved3` | TField |  |  |
| 6 | `AC.EV.RESERVED.2` | `AcEvent_Reserved2` | TField |  |  |
| 7 | `AC.EV.RESERVED.1` | `AcEvent_Reserved1` | TField |  |  |
| 8 | `AC.EV.LOCAL.REF` | `AcEvent_LocalRef` |  |  |  |
| 9 | `AC.EV.RECORD.STATUS` | `AcEvent_RecordStatus` | String |  |  |
| 10 | `AC.EV.CURR.NO` | `AcEvent_CurrNo` | String |  |  |
| 11 | `AC.EV.INPUTTER` | `AcEvent_Inputter` |  |  |  |
| 12 | `AC.EV.DATE.TIME` | `AcEvent_DateTime` |  |  |  |
| 13 | `AC.EV.AUTHORISER` | `AcEvent_Authoriser` | String |  |  |
| 14 | `AC.EV.CO.CODE` | `AcEvent_CoCode` | String |  |  |
| 15 | `AC.EV.DEPT.CODE` | `AcEvent_DeptCode` | String |  |  |
| 16 | `AC.EV.AUDITOR.CODE` | `AcEvent_AuditorCode` | String |  |  |
| 17 | `AC.EV.AUDIT.DATE.TIME` | `AcEvent_AuditDateTime` | String |  |  |
