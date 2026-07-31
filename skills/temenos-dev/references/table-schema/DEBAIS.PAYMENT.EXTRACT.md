# DEBAIS.PAYMENT.EXTRACT — Table Schema

> Source: `INSERTS/I_F.DEBAIS.PAYMENT.EXTRACT` in `DEBAIS_PaymentStatistics.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DEBAIS.EXTRACT.POSITION` | `DebaisPaymentExtract_Position` |  |  |  |
| 2 | `DEBAIS.EXTRACT.RESERVED.10` | `DebaisPaymentExtract_Reserved10` | TField |  | Reserved for Future Use. |
| 3 | `DEBAIS.EXTRACT.RESERVED.9` | `DebaisPaymentExtract_Reserved9` | TField |  | Reserved for Future Use. |
| 4 | `DEBAIS.EXTRACT.RESERVED.8` | `DebaisPaymentExtract_Reserved8` | TField |  | Reserved for Future Use. |
| 5 | `DEBAIS.EXTRACT.RESERVED.7` | `DebaisPaymentExtract_Reserved7` | TField |  | Reserved for Future Use. |
| 6 | `DEBAIS.EXTRACT.RESERVED.6` | `DebaisPaymentExtract_Reserved6` | TField |  | Reserved for Future Use. |
| 7 | `DEBAIS.EXTRACT.RESERVED.5` | `DebaisPaymentExtract_Reserved5` | TField |  | Reserved for Future Use. |
| 8 | `DEBAIS.EXTRACT.RESERVED.4` | `DebaisPaymentExtract_Reserved4` | TField |  | Reserved for Future Use. |
| 9 | `DEBAIS.EXTRACT.RESERVED.3` | `DebaisPaymentExtract_Reserved3` | TField |  | Reserved for Future Use. |
| 10 | `DEBAIS.EXTRACT.RESERVED.2` | `DebaisPaymentExtract_Reserved2` | TField |  | Reserved for Future Use. |
| 11 | `DEBAIS.EXTRACT.RESERVED.1` | `DebaisPaymentExtract_Reserved1` | TField |  | Reserved for Future Use. |
| 12 | `DEBAIS.EXTRACT.LOCAL.REF` | `DebaisPaymentExtract_LocalRef` |  |  |  |
| 13 | `DEBAIS.EXTRACT.OVERRIDE` | `DebaisPaymentExtract_Override` |  |  |  |
| 14 | `DEBAIS.EXTRACT.RECORD.STATUS` | `DebaisPaymentExtract_RecordStatus` | String |  |  |
| 15 | `DEBAIS.EXTRACT.CURR.NO` | `DebaisPaymentExtract_CurrNo` | String |  |  |
| 16 | `DEBAIS.EXTRACT.INPUTTER` | `DebaisPaymentExtract_Inputter` |  |  |  |
| 17 | `DEBAIS.EXTRACT.DATE.TIME` | `DebaisPaymentExtract_DateTime` |  |  |  |
| 18 | `DEBAIS.EXTRACT.AUTHORISER` | `DebaisPaymentExtract_Authoriser` | String |  |  |
| 19 | `DEBAIS.EXTRACT.CO.CODE` | `DebaisPaymentExtract_CoCode` | String |  |  |
| 20 | `DEBAIS.EXTRACT.DEPT.CODE` | `DebaisPaymentExtract_DeptCode` | String |  |  |
| 21 | `DEBAIS.EXTRACT.AUDITOR.CODE` | `DebaisPaymentExtract_AuditorCode` | String |  |  |
| 22 | `DEBAIS.EXTRACT.AUDIT.DATE.TIME` | `DebaisPaymentExtract_AuditDateTime` | String |  |  |
