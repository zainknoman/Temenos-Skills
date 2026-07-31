# PAYMENT.CATEG.PURPOSE — Table Schema

> Source: `INSERTS/I_F.PAYMENT.CATEG.PURPOSE` in `AC_StandingOrders.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PCP.SHORT.DESC` | `PaymentCategPurpose_ShortDesc` |  |  |  |
| 2 | `PCP.DEFINITION` | `PaymentCategPurpose_Definition` |  |  |  |
| 3 | `PCP.RESERVED.10` | `PaymentCategPurpose_Reserved10` | TField |  |  |
| 4 | `PCP.RESERVED.09` | `PaymentCategPurpose_Reserved09` | TField |  |  |
| 5 | `PCP.RESERVED.08` | `PaymentCategPurpose_Reserved08` | TField |  |  |
| 6 | `PCP.RESERVED.07` | `PaymentCategPurpose_Reserved07` | TField |  |  |
| 7 | `PCP.RESERVED.06` | `PaymentCategPurpose_Reserved06` | TField |  |  |
| 8 | `PCP.RESERVED.05` | `PaymentCategPurpose_Reserved05` | TField |  |  |
| 9 | `PCP.RESERVED.04` | `PaymentCategPurpose_Reserved04` | TField |  |  |
| 10 | `PCP.RESERVED.03` | `PaymentCategPurpose_Reserved03` | TField |  |  |
| 11 | `PCP.RESERVED.02` | `PaymentCategPurpose_Reserved02` | TField |  |  |
| 12 | `PCP.RESERVED.01` | `PaymentCategPurpose_Reserved01` | TField |  |  |
| 13 | `PCP.LOCAL.REF` | `PaymentCategPurpose_LocalRef` |  |  |  |
| 14 | `PCP.OVERRIDE` | `PaymentCategPurpose_Override` |  |  |  |
| 15 | `PCP.RECORD.STATUS` | `PaymentCategPurpose_RecordStatus` | String |  |  |
| 16 | `PCP.CURR.NO` | `PaymentCategPurpose_CurrNo` | String |  |  |
| 17 | `PCP.INPUTTER` | `PaymentCategPurpose_Inputter` |  |  |  |
| 18 | `PCP.DATE.TIME` | `PaymentCategPurpose_DateTime` |  |  |  |
| 19 | `PCP.AUTHORISER` | `PaymentCategPurpose_Authoriser` | String |  |  |
| 20 | `PCP.CO.CODE` | `PaymentCategPurpose_CoCode` | String |  |  |
| 21 | `PCP.DEPT.CODE` | `PaymentCategPurpose_DeptCode` | String |  |  |
| 22 | `PCP.AUDITOR.CODE` | `PaymentCategPurpose_AuditorCode` | String |  |  |
| 23 | `PCP.AUDIT.DATE.TIME` | `PaymentCategPurpose_AuditDateTime` | String |  |  |
