# AUWHTX.YEAR.END.COMPONENT.VALUES — Table Schema

> Source: `INSERTS/I_F.AUWHTX.YEAR.END.COMPONENT.VALUES` in `AUWHTX_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `YEAREND.VALUE.CURRENCY` | `AuwhtxYearEndComponentValues_Currency` | TField |  | This field contains the Currency of the Entitlement |
| 2 | `YEAREND.VALUE.COMPONENT` | `AuwhtxYearEndComponentValues_Component` |  |  |  |
| 3 | `YEAREND.VALUE.VALUE` | `AuwhtxYearEndComponentValues_Value` |  |  |  |
| 4 | `YEAREND.VALUE.VALUE.LCY` | `AuwhtxYearEndComponentValues_ValueLcy` |  |  |  |
| 5 | `YEAREND.VALUE.LOCAL.REF` | `AuwhtxYearEndComponentValues_LocalRef` |  |  |  |
| 6 | `YEAREND.VALUE.CASH.COMP.BAL` | `AuwhtxYearEndComponentValues_CashCompBal` | TField |  | To record any surplus or deficit in the cash component in year end tax profile. |
| 7 | `YEAREND.VALUE.YR.END.COMP.TYPE` | `AuwhtxYearEndComponentValues_YrEndCompType` | TField |  |  |
| 8 | `YEAREND.VALUE.YEAR.END.PROFILE.ID` | `AuwhtxYearEndComponentValues_YearEndProfileId` | TField |  |  |
| 9 | `YEAREND.VALUE.TOTAL.INCOME` | `AuwhtxYearEndComponentValues_TotalIncome` | TField |  | The total income is derived by applying the CHILD.INCOME.PCT on the Entitlement Income Amount. All the component percentages are applied on this amount. |
| 10 | `YEAREND.VALUE.RESERVED.5` | `AuwhtxYearEndComponentValues_Reserved5` | TField |  |  |
| 11 | `YEAREND.VALUE.RESERVED.6` | `AuwhtxYearEndComponentValues_Reserved6` | TField |  |  |
| 12 | `YEAREND.VALUE.RESERVED.7` | `AuwhtxYearEndComponentValues_Reserved7` | TField |  |  |
| 13 | `YEAREND.VALUE.RESERVED.8` | `AuwhtxYearEndComponentValues_Reserved8` | TField |  |  |
| 14 | `YEAREND.VALUE.RESERVED.9` | `AuwhtxYearEndComponentValues_Reserved9` | TField |  |  |
| 15 | `YEAREND.VALUE.RESERVED.10` | `AuwhtxYearEndComponentValues_Reserved10` | TField |  |  |
| 16 | `YEAREND.VALUE.OVERRIDE` | `AuwhtxYearEndComponentValues_Override` |  |  |  |
| 17 | `YEAREND.VALUE.RECORD.STATUS` | `AuwhtxYearEndComponentValues_RecordStatus` | String |  |  |
| 18 | `YEAREND.VALUE.CURR.NO` | `AuwhtxYearEndComponentValues_CurrNo` | String |  |  |
| 19 | `YEAREND.VALUE.INPUTTER` | `AuwhtxYearEndComponentValues_Inputter` |  |  |  |
| 20 | `YEAREND.VALUE.DATE.TIME` | `AuwhtxYearEndComponentValues_DateTime` |  |  |  |
| 21 | `YEAREND.VALUE.AUTHORISER` | `AuwhtxYearEndComponentValues_Authoriser` | String |  |  |
| 22 | `YEAREND.VALUE.CO.CODE` | `AuwhtxYearEndComponentValues_CoCode` | String |  |  |
| 23 | `YEAREND.VALUE.DEPT.CODE` | `AuwhtxYearEndComponentValues_DeptCode` | String |  |  |
| 24 | `YEAREND.VALUE.AUDITOR.CODE` | `AuwhtxYearEndComponentValues_AuditorCode` | String |  |  |
| 25 | `YEAREND.VALUE.AUDIT.DATE.TIME` | `AuwhtxYearEndComponentValues_AuditDateTime` | String |  |  |
