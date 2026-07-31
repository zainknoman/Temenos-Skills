# PAYMENT.PURPOSE.CODE — Table Schema

> Source: `INSERTS/I_F.PAYMENT.PURPOSE.CODE` in `AC_StandingOrders.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPC.SHORT.DESC` | `PaymentPurposeCode_ShortDesc` |  |  |  |
| 2 | `PPC.CLASSIFICATION` | `PaymentPurposeCode_Classification` |  |  |  |
| 3 | `PPC.DEFINITION` | `PaymentPurposeCode_Definition` |  |  |  |
| 4 | `PPC.RESERVED.10` | `PaymentPurposeCode_Reserved10` | TField |  |  |
| 5 | `PPC.RESERVED.09` | `PaymentPurposeCode_Reserved09` | TField |  |  |
| 6 | `PPC.RESERVED.08` | `PaymentPurposeCode_Reserved08` | TField |  |  |
| 7 | `PPC.RESERVED.07` | `PaymentPurposeCode_Reserved07` | TField |  |  |
| 8 | `PPC.RESERVED.06` | `PaymentPurposeCode_Reserved06` | TField |  |  |
| 9 | `PPC.RESERVED.05` | `PaymentPurposeCode_Reserved05` | TField |  |  |
| 10 | `PPC.RESERVED.04` | `PaymentPurposeCode_Reserved04` | TField |  |  |
| 11 | `PPC.RESERVED.03` | `PaymentPurposeCode_Reserved03` | TField |  |  |
| 12 | `PPC.RESERVED.02` | `PaymentPurposeCode_Reserved02` | TField |  |  |
| 13 | `PPC.RESERVED.01` | `PaymentPurposeCode_Reserved01` | TField |  |  |
| 14 | `PPC.LOCAL.REF` | `PaymentPurposeCode_LocalRef` |  |  |  |
| 15 | `PPC.OVERRIDE` | `PaymentPurposeCode_Override` |  |  |  |
| 16 | `PPC.RECORD.STATUS` | `PaymentPurposeCode_RecordStatus` | String |  |  |
| 17 | `PPC.CURR.NO` | `PaymentPurposeCode_CurrNo` | String |  |  |
| 18 | `PPC.INPUTTER` | `PaymentPurposeCode_Inputter` |  |  |  |
| 19 | `PPC.DATE.TIME` | `PaymentPurposeCode_DateTime` |  |  |  |
| 20 | `PPC.AUTHORISER` | `PaymentPurposeCode_Authoriser` | String |  |  |
| 21 | `PPC.CO.CODE` | `PaymentPurposeCode_CoCode` | String |  |  |
| 22 | `PPC.DEPT.CODE` | `PaymentPurposeCode_DeptCode` | String |  |  |
| 23 | `PPC.AUDITOR.CODE` | `PaymentPurposeCode_AuditorCode` | String |  |  |
| 24 | `PPC.AUDIT.DATE.TIME` | `PaymentPurposeCode_AuditDateTime` | String |  |  |
