# ACCT.INTERIM.CHG — Table Schema

> Source: `INSERTS/I_F.ACCT.INTERIM.CHG` in `IC_InterestAndCapitalisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.INCHG.ACCOUNT.NUMBER` | `AcctInterimChg_AccountNumber` |  |  |  |
| 2 | `AC.INCHG.RESERVED1` | `AcctInterimChg_Reserved1` |  |  |  |
| 3 | `AC.INCHG.IC.CHARGE.CODE` | `AcctInterimChg_IcChargeCode` |  |  |  |
| 4 | `AC.INCHG.CHG.PRODUCTS` | `AcctInterimChg_ChgProducts` |  |  |  |
| 5 | `AC.INCHG.RESERVED.10` | `AcctInterimChg_Reserved10` | TField |  |  |
| 6 | `AC.INCHG.RESERVED.9` | `AcctInterimChg_Reserved9` | TField |  |  |
| 7 | `AC.INCHG.RESERVED.8` | `AcctInterimChg_Reserved8` | TField |  |  |
| 8 | `AC.INCHG.RESERVED.7` | `AcctInterimChg_Reserved7` | TField |  |  |
| 9 | `AC.INCHG.RESERVED.6` | `AcctInterimChg_Reserved6` | TField |  |  |
| 10 | `AC.INCHG.RESERVED.5` | `AcctInterimChg_Reserved5` | TField |  |  |
| 11 | `AC.INCHG.RESERVED.4` | `AcctInterimChg_Reserved4` | TField |  |  |
| 12 | `AC.INCHG.RESERVED.3` | `AcctInterimChg_Reserved3` | TField |  |  |
| 13 | `AC.INCHG.LOCAL.REF` | `AcctInterimChg_LocalRef` |  |  |  |
| 14 | `AC.INCHG.OVERRIDE` | `AcctInterimChg_Override` |  |  |  |
| 15 | `AC.INCHG.RECORD.STATUS` | `AcctInterimChg_RecordStatus` | String |  |  |
| 16 | `AC.INCHG.CURR.NO` | `AcctInterimChg_CurrNo` | String |  |  |
| 17 | `AC.INCHG.INPUTTER` | `AcctInterimChg_Inputter` |  |  |  |
| 18 | `AC.INCHG.DATE.TIME` | `AcctInterimChg_DateTime` |  |  |  |
| 19 | `AC.INCHG.AUTHORISER` | `AcctInterimChg_Authoriser` | String |  |  |
| 20 | `AC.INCHG.CO.CODE` | `AcctInterimChg_CoCode` | String |  |  |
| 21 | `AC.INCHG.DEPT.CODE` | `AcctInterimChg_DeptCode` | String |  |  |
| 22 | `AC.INCHG.AUDITOR.CODE` | `AcctInterimChg_AuditorCode` | String |  |  |
| 23 | `AC.INCHG.AUDIT.DATE.TIME` | `AcctInterimChg_AuditDateTime` | String |  |  |
