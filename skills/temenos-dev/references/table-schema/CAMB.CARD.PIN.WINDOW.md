# CAMB.CARD.PIN.WINDOW — Table Schema

> Source: `INSERTS/I_F.CAMB.CARD.PIN.WINDOW` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.CARD.PIN.PIN.WINDOW` | `CambCardPinWindow_PinWindow` | TField |  |  |
| 2 | `CAMB.CARD.PIN.RESERVED.1` | `CambCardPinWindow_Reserved1` | TField |  |  |
| 3 | `CAMB.CARD.PIN.RESERVED.2` | `CambCardPinWindow_Reserved2` | TField |  |  |
| 4 | `CAMB.CARD.PIN.LOCAL.REF` | `CambCardPinWindow_LocalRef` |  |  |  |
| 5 | `CAMB.CARD.PIN.OVERRIDE` | `CambCardPinWindow_Override` |  |  |  |
| 6 | `CAMB.CARD.PIN.RECORD.STATUS` | `CambCardPinWindow_RecordStatus` | String |  |  |
| 7 | `CAMB.CARD.PIN.CURR.NO` | `CambCardPinWindow_CurrNo` | String |  |  |
| 8 | `CAMB.CARD.PIN.INPUTTER` | `CambCardPinWindow_Inputter` |  |  |  |
| 9 | `CAMB.CARD.PIN.DATE.TIME` | `CambCardPinWindow_DateTime` |  |  |  |
| 10 | `CAMB.CARD.PIN.AUTHORISER` | `CambCardPinWindow_Authoriser` | String |  |  |
| 11 | `CAMB.CARD.PIN.CO.CODE` | `CambCardPinWindow_CoCode` | String |  |  |
| 12 | `CAMB.CARD.PIN.DEPT.CODE` | `CambCardPinWindow_DeptCode` | String |  |  |
| 13 | `CAMB.CARD.PIN.AUDITOR.CODE` | `CambCardPinWindow_AuditorCode` | String |  |  |
| 14 | `CAMB.CARD.PIN.AUDIT.DATE.TIME` | `CambCardPinWindow_AuditDateTime` | String |  |  |
