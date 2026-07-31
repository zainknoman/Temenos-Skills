# NORACC.PARAMETER — Table Schema

> Source: `INSERTS/I_F.NORACC.PARAMETER` in `NORACC_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NORACCPARAM.PRENOTICE.DAYS` | `NoraccParameter_PrenoticeDays` | TField |  | Prenotice days common to all the properties can be configured |
| 2 | `NORACCPARAM.ADVICE.INDICATOR` | `NoraccParameter_AdviceIndicator` |  |  |  |
| 3 | `NORACCPARAM.PROPERTY.NAME` | `NoraccParameter_PropertyName` |  |  |  |
| 4 | `NORACCPARAM.FREE.TEXT` | `NoraccParameter_FreeText` |  |  |  |
| 5 | `NORACCPARAM.STO.TYPE` | `NoraccParameter_StoType` |  |  |  |
| 6 | `NORACCPARAM.PAYMENT.STO.TRAN.CODE` | `NoraccParameter_PaymentStoTranCode` |  |  |  |
| 7 | `NORACCPARAM.PAYMENT.STO.BANK.CUS.INDICATOR` | `NoraccParameter_PaymentStoBankCusIndicator` |  |  |  |
| 8 | `NORACCPARAM.PAYMENT.STO.TEXT` | `NoraccParameter_PaymentStoText` |  |  |  |
| 9 | `NORACCPARAM.RESERVED.5` | `NoraccParameter_Reserved5` | TField |  |  |
| 10 | `NORACCPARAM.RESERVED.4` | `NoraccParameter_Reserved4` | TField |  |  |
| 11 | `NORACCPARAM.RESERVED.3` | `NoraccParameter_Reserved3` | TField |  |  |
| 12 | `NORACCPARAM.RESERVED.2` | `NoraccParameter_Reserved2` | TField |  |  |
| 13 | `NORACCPARAM.RESERVED.1` | `NoraccParameter_Reserved1` | TField |  |  |
| 14 | `NORACCPARAM.RECORD.STATUS` | `NoraccParameter_RecordStatus` | String |  |  |
| 15 | `NORACCPARAM.CURR.NO` | `NoraccParameter_CurrNo` | String |  |  |
| 16 | `NORACCPARAM.INPUTTER` | `NoraccParameter_Inputter` |  |  |  |
| 17 | `NORACCPARAM.DATE.TIME` | `NoraccParameter_DateTime` |  |  |  |
| 18 | `NORACCPARAM.AUTHORISER` | `NoraccParameter_Authoriser` | String |  |  |
| 19 | `NORACCPARAM.CO.CODE` | `NoraccParameter_CoCode` | String |  |  |
| 20 | `NORACCPARAM.DEPT.CODE` | `NoraccParameter_DeptCode` | String |  |  |
| 21 | `NORACCPARAM.AUDITOR.CODE` | `NoraccParameter_AuditorCode` | String |  |  |
| 22 | `NORACCPARAM.AUDIT.DATE.TIME` | `NoraccParameter_AuditDateTime` | String |  |  |
