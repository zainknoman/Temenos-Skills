# SC.WHT.SOURCE.LOCAL — Table Schema

> Source: `INSERTS/I_F.SC.WHT.SOURCE.LOCAL` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SL.FATCA.TAX.TYPE` | `ScWhtSourceLocal_FatcaTaxType` | TField |  |  |
| 2 | `SC.SL.CLASSIFICATION` | `ScWhtSourceLocal_Classification` | TField |  |  |
| 3 | `SC.SL.SOURCE.LOCAL` | `ScWhtSourceLocal_SourceLocal` |  |  |  |
| 4 | `SC.SL.INCOME.TYPE` | `ScWhtSourceLocal_IncomeType` |  |  |  |
| 5 | `SC.SL.INSTRUMENT` | `ScWhtSourceLocal_Instrument` |  |  |  |
| 6 | `SC.SL.DEPOSITORY` | `ScWhtSourceLocal_Depository` |  |  |  |
| 7 | `SC.SL.SUB.ACCOUNT` | `ScWhtSourceLocal_SubAccount` |  |  |  |
| 8 | `SC.SL.TAX.CODE` | `ScWhtSourceLocal_TaxCode` |  |  |  |
| 9 | `SC.SL.TAX.RATE` | `ScWhtSourceLocal_TaxRate` |  |  |  |
| 10 | `SC.SL.RESERVED.5` | `ScWhtSourceLocal_Reserved5` | TField |  |  |
| 11 | `SC.SL.RESERVED.4` | `ScWhtSourceLocal_Reserved4` | TField |  |  |
| 12 | `SC.SL.RESERVED.3` | `ScWhtSourceLocal_Reserved3` | TField |  |  |
| 13 | `SC.SL.RESERVED.2` | `ScWhtSourceLocal_Reserved2` | TField |  |  |
| 14 | `SC.SL.RESERVED.1` | `ScWhtSourceLocal_Reserved1` | TField |  |  |
| 15 | `SC.SL.LOCAL.REF` | `ScWhtSourceLocal_LocalRef` |  |  |  |
| 16 | `SC.SL.OVERRIDE` | `ScWhtSourceLocal_Override` |  |  |  |
| 17 | `SC.SL.RECORD.STATUS` | `ScWhtSourceLocal_RecordStatus` | String |  |  |
| 18 | `SC.SL.CURR.NO` | `ScWhtSourceLocal_CurrNo` | String |  |  |
| 19 | `SC.SL.INPUTTER` | `ScWhtSourceLocal_Inputter` |  |  |  |
| 20 | `SC.SL.DATE.TIME` | `ScWhtSourceLocal_DateTime` |  |  |  |
| 21 | `SC.SL.AUTHORISER` | `ScWhtSourceLocal_Authoriser` | String |  |  |
| 22 | `SC.SL.CO.CODE` | `ScWhtSourceLocal_CoCode` | String |  |  |
| 23 | `SC.SL.DEPT.CODE` | `ScWhtSourceLocal_DeptCode` | String |  |  |
| 24 | `SC.SL.AUDITOR.CODE` | `ScWhtSourceLocal_AuditorCode` | String |  |  |
| 25 | `SC.SL.AUDIT.DATE.TIME` | `ScWhtSourceLocal_AuditDateTime` | String |  |  |
