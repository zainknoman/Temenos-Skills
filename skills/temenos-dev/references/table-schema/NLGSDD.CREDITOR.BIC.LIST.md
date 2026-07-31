# NLGSDD.CREDITOR.BIC.LIST — Table Schema

> Source: `INSERTS/I_F.NLGSDD.CREDITOR.BIC.LIST` in `NLGSDD_Governmentorder.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NLGSDD.BANK.NAME` | `NlgsddCreditorBicList_BankName` | TField |  | Specifies the name of Financial Institution or Bank |
| 2 | `NLGSDD.BANK.IDENTIFIER` | `NlgsddCreditorBicList_BankIdentifier` | TField |  | Specifies the Bank Identifier |
| 3 | `NLGSDD.LOCAL.REF` | `NlgsddCreditorBicList_LocalRef` |  |  |  |
| 4 | `NLGSDD.RESERVED.5` | `NlgsddCreditorBicList_Reserved5` | TField |  | Reserved field for future use. |
| 5 | `NLGSDD.RESERVED.4` | `NlgsddCreditorBicList_Reserved4` | TField |  | Reserved field for future use. |
| 6 | `NLGSDD.RESERVED.3` | `NlgsddCreditorBicList_Reserved3` | TField |  | Reserved field for future use. |
| 7 | `NLGSDD.RESERVED.2` | `NlgsddCreditorBicList_Reserved2` | TField |  | Reserved field for future use. |
| 8 | `NLGSDD.RESERVED.1` | `NlgsddCreditorBicList_Reserved1` | TField |  | Reserved field for future use. |
| 9 | `NLGSDD.OVERRIDE` | `NlgsddCreditorBicList_Override` |  |  |  |
| 10 | `NLGSDD.RECORD.STATUS` | `NlgsddCreditorBicList_RecordStatus` | String |  |  |
| 11 | `NLGSDD.CURR.NO` | `NlgsddCreditorBicList_CurrNo` | String |  |  |
| 12 | `NLGSDD.INPUTTER` | `NlgsddCreditorBicList_Inputter` |  |  |  |
| 13 | `NLGSDD.DATE.TIME` | `NlgsddCreditorBicList_DateTime` |  |  |  |
| 14 | `NLGSDD.AUTHORISER` | `NlgsddCreditorBicList_Authoriser` | String |  |  |
| 15 | `NLGSDD.CO.CODE` | `NlgsddCreditorBicList_CoCode` | String |  |  |
| 16 | `NLGSDD.DEPT.CODE` | `NlgsddCreditorBicList_DeptCode` | String |  |  |
| 17 | `NLGSDD.AUDITOR.CODE` | `NlgsddCreditorBicList_AuditorCode` | String |  |  |
| 18 | `NLGSDD.AUDIT.DATE.TIME` | `NlgsddCreditorBicList_AuditDateTime` | String |  |  |
