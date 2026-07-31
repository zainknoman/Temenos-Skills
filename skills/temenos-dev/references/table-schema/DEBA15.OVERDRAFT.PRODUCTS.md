# DEBA15.OVERDRAFT.PRODUCTS — Table Schema

> Source: `INSERTS/I_F.DEBA15.OVERDRAFT.PRODUCTS` in `DEBA15_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OVRDFT.PROD.PRODUCT` | `Deba15OverdraftProducts_Product` |  |  |  |
| 2 | `OVRDFT.PROD.RESERVED.8` | `Deba15OverdraftProducts_Reserved8` | TField |  |  |
| 3 | `OVRDFT.PROD.RESERVED.7` | `Deba15OverdraftProducts_Reserved7` | TField |  |  |
| 4 | `OVRDFT.PROD.RESERVED.6` | `Deba15OverdraftProducts_Reserved6` | TField |  |  |
| 5 | `OVRDFT.PROD.RESERVED.5` | `Deba15OverdraftProducts_Reserved5` | TField |  |  |
| 6 | `OVRDFT.PROD.RESERVED.4` | `Deba15OverdraftProducts_Reserved4` | TField |  |  |
| 7 | `OVRDFT.PROD.RESERVED.3` | `Deba15OverdraftProducts_Reserved3` | TField |  |  |
| 8 | `OVRDFT.PROD.RESERVED.2` | `Deba15OverdraftProducts_Reserved2` | TField |  |  |
| 9 | `OVRDFT.PROD.RESERVED.1` | `Deba15OverdraftProducts_Reserved1` | TField |  |  |
| 10 | `OVRDFT.PROD.LOCAL.REF` | `Deba15OverdraftProducts_LocalRef` |  |  |  |
| 11 | `OVRDFT.PROD.OVERRIDE` | `Deba15OverdraftProducts_Override` |  |  |  |
| 12 | `OVRDFT.PROD.RECORD.STATUS` | `Deba15OverdraftProducts_RecordStatus` | String |  |  |
| 13 | `OVRDFT.PROD.CURR.NO` | `Deba15OverdraftProducts_CurrNo` | String |  |  |
| 14 | `OVRDFT.PROD.INPUTTER` | `Deba15OverdraftProducts_Inputter` |  |  |  |
| 15 | `OVRDFT.PROD.DATE.TIME` | `Deba15OverdraftProducts_DateTime` |  |  |  |
| 16 | `OVRDFT.PROD.AUTHORISER` | `Deba15OverdraftProducts_Authoriser` | String |  |  |
| 17 | `OVRDFT.PROD.CO.CODE` | `Deba15OverdraftProducts_CoCode` | String |  |  |
| 18 | `OVRDFT.PROD.DEPT.CODE` | `Deba15OverdraftProducts_DeptCode` | String |  |  |
| 19 | `OVRDFT.PROD.AUDITOR.CODE` | `Deba15OverdraftProducts_AuditorCode` | String |  |  |
| 20 | `OVRDFT.PROD.AUDIT.DATE.TIME` | `Deba15OverdraftProducts_AuditDateTime` | String |  |  |
