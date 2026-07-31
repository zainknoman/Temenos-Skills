# SC.SM.TAX.CONFIG — Table Schema

> Source: `INSERTS/I_F.SC.SM.TAX.CONFIG` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SMTAXCNF.SM.ATTRIBUTE` | `ScSmTaxConfig_SmAttribute` |  |  |  |
| 2 | `SC.SMTAXCNF.ATTRIBUTE.OPERAND` | `ScSmTaxConfig_AttributeOperand` |  |  |  |
| 3 | `SC.SMTAXCNF.ATTRIBUTE.VALUE` | `ScSmTaxConfig_AttributeValue` |  |  |  |
| 4 | `SC.SMTAXCNF.SC.TAX.CODE` | `ScSmTaxConfig_ScTaxCode` |  |  |  |
| 5 | `SC.SMTAXCNF.COUPON.TAX.CODE` | `ScSmTaxConfig_CouponTaxCode` |  |  |  |
| 6 | `SC.SMTAXCNF.TXN.TAX.CODE` | `ScSmTaxConfig_TxnTaxCode` |  |  |  |
| 7 | `SC.SMTAXCNF.RESERVED.15` | `ScSmTaxConfig_Reserved15` |  |  |  |
| 8 | `SC.SMTAXCNF.RESERVED.14` | `ScSmTaxConfig_Reserved14` | TField |  |  |
| 9 | `SC.SMTAXCNF.RESERVED.13` | `ScSmTaxConfig_Reserved13` | TField |  |  |
| 10 | `SC.SMTAXCNF.RESERVED.12` | `ScSmTaxConfig_Reserved12` | TField |  |  |
| 11 | `SC.SMTAXCNF.RESERVED.11` | `ScSmTaxConfig_Reserved11` | TField |  |  |
| 12 | `SC.SMTAXCNF.RESERVED.10` | `ScSmTaxConfig_Reserved10` | TField |  |  |
| 13 | `SC.SMTAXCNF.RESERVED.09` | `ScSmTaxConfig_Reserved09` | TField |  |  |
| 14 | `SC.SMTAXCNF.RESERVED.08` | `ScSmTaxConfig_Reserved08` | TField |  |  |
| 15 | `SC.SMTAXCNF.RESERVED.07` | `ScSmTaxConfig_Reserved07` | TField |  |  |
| 16 | `SC.SMTAXCNF.RESERVED.06` | `ScSmTaxConfig_Reserved06` | TField |  |  |
| 17 | `SC.SMTAXCNF.RESERVED.05` | `ScSmTaxConfig_Reserved05` | TField |  |  |
| 18 | `SC.SMTAXCNF.RESERVED.04` | `ScSmTaxConfig_Reserved04` | TField |  |  |
| 19 | `SC.SMTAXCNF.RESERVED.03` | `ScSmTaxConfig_Reserved03` | TField |  |  |
| 20 | `SC.SMTAXCNF.RESERVED.02` | `ScSmTaxConfig_Reserved02` | TField |  |  |
| 21 | `SC.SMTAXCNF.RESERVED.01` | `ScSmTaxConfig_Reserved01` | TField |  |  |
| 22 | `SC.SMTAXCNF.LOCAL.REF` | `ScSmTaxConfig_LocalRef` |  |  |  |
| 23 | `SC.SMTAXCNF.STMT.NOS` | `ScSmTaxConfig_StmtNos` |  |  |  |
| 24 | `SC.SMTAXCNF.OVERRIDE` | `ScSmTaxConfig_Override` |  |  |  |
| 25 | `SC.SMTAXCNF.RECORD.STATUS` | `ScSmTaxConfig_RecordStatus` | String |  |  |
| 26 | `SC.SMTAXCNF.CURR.NO` | `ScSmTaxConfig_CurrNo` | String |  |  |
| 27 | `SC.SMTAXCNF.INPUTTER` | `ScSmTaxConfig_Inputter` |  |  |  |
| 28 | `SC.SMTAXCNF.DATE.TIME` | `ScSmTaxConfig_DateTime` |  |  |  |
| 29 | `SC.SMTAXCNF.AUTHORISER` | `ScSmTaxConfig_Authoriser` | String |  |  |
| 30 | `SC.SMTAXCNF.CO.CODE` | `ScSmTaxConfig_CoCode` | String |  |  |
| 31 | `SC.SMTAXCNF.DEPT.CODE` | `ScSmTaxConfig_DeptCode` | String |  |  |
| 32 | `SC.SMTAXCNF.AUDITOR.CODE` | `ScSmTaxConfig_AuditorCode` | String |  |  |
| 33 | `SC.SMTAXCNF.AUDIT.DATE.TIME` | `ScSmTaxConfig_AuditDateTime` | String |  |  |
