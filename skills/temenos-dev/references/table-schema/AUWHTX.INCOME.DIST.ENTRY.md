# AUWHTX.INCOME.DIST.ENTRY — Table Schema

> Source: `INSERTS/I_F.AUWHTX.INCOME.DIST.ENTRY` in `AUWHTX_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IDE.SECURITY.NO` | `AuwhtxIncomeDistEntry_SecurityNo` | TField |  | The security no for which the income distribution details are entered. |
| 2 | `IDE.EVENT.TYPE` | `AuwhtxIncomeDistEntry_EventType` | TField |  | The type of the event associated with the Diary. |
| 3 | `IDE.EX.DATE` | `AuwhtxIncomeDistEntry_ExDate` | TField |  | The Ex date of the corporate action event. |
| 4 | `IDE.PAY.DATE` | `AuwhtxIncomeDistEntry_PayDate` | TField |  | The Pay date of the corporate action event. |
| 5 | `IDE.VALUE.DATE` | `AuwhtxIncomeDistEntry_ValueDate` | TField |  | The Value date of the corporate action event. |
| 6 | `IDE.CURRENCY` | `AuwhtxIncomeDistEntry_Currency` | TField |  | The currency of the corporate action event. |
| 7 | `IDE.OPTION.DESC` | `AuwhtxIncomeDistEntry_OptionDesc` |  |  |  |
| 8 | `IDE.RATE.IN.DPU` | `AuwhtxIncomeDistEntry_RateInDpu` |  |  |  |
| 9 | `IDE.NO.TFN.COMPONENT` | `AuwhtxIncomeDistEntry_NoTfnComponent` |  |  |  |
| 10 | `IDE.NO.TFN.PCT` | `AuwhtxIncomeDistEntry_NoTfnPct` |  |  |  |
| 11 | `IDE.NON.RESIDENT.COMPONENT` | `AuwhtxIncomeDistEntry_NonResidentComponent` |  |  |  |
| 12 | `IDE.NON.RESIDENT.PCT` | `AuwhtxIncomeDistEntry_NonResidentPct` |  |  |  |
| 13 | `IDE.STATUS` | `AuwhtxIncomeDistEntry_Status` | TField |  | Status to be updated based on Entitlement authorisation Accrued, Partially Paid (after first Entitlement is authorised) and Fully Paid (After all Entitlements are authorised). |
| 14 | `IDE.UNALLOCATED.COMPONENT.PCT` | `AuwhtxIncomeDistEntry_UnallocatedComponentPct` | TField |  | This field indicates the unallocated component percentage of non-resident components. |
| 15 | `IDE.ADJ.ROUND.DIFF` | `AuwhtxIncomeDistEntry_AdjRoundDiff` | TField |  | This field indicates if the rounding difference should be adjusted against WHT component values. |
| 16 | `IDE.INCOME.EXCH.RATE` | `AuwhtxIncomeDistEntry_IncomeExchRate` | TField |  | The exchange rate used for calculating the foreign exchange gain or loss. This is relevant only in those corporate actions with multi-currency dividend where some entitlement holders opt for income in event currency while some opt for income in local currency |
| 17 | `IDE.RESERVED.4` | `AuwhtxIncomeDistEntry_Reserved4` | TField |  |  |
| 18 | `IDE.RESERVED.5` | `AuwhtxIncomeDistEntry_Reserved5` | TField |  |  |
| 19 | `IDE.RESERVED.6` | `AuwhtxIncomeDistEntry_Reserved6` | TField |  |  |
| 20 | `IDE.RESERVED.7` | `AuwhtxIncomeDistEntry_Reserved7` | TField |  |  |
| 21 | `IDE.RESERVED.8` | `AuwhtxIncomeDistEntry_Reserved8` | TField |  |  |
| 22 | `IDE.RESERVED.9` | `AuwhtxIncomeDistEntry_Reserved9` | TField |  |  |
| 23 | `IDE.RESERVED.10` | `AuwhtxIncomeDistEntry_Reserved10` | TField |  |  |
| 24 | `IDE.LOCAL.REF` | `AuwhtxIncomeDistEntry_LocalRef` |  |  |  |
| 25 | `IDE.OVERRIDE` | `AuwhtxIncomeDistEntry_Override` |  |  |  |
| 26 | `IDE.RECORD.STATUS` | `AuwhtxIncomeDistEntry_RecordStatus` | String |  |  |
| 27 | `IDE.CURR.NO` | `AuwhtxIncomeDistEntry_CurrNo` | String |  |  |
| 28 | `IDE.INPUTTER` | `AuwhtxIncomeDistEntry_Inputter` |  |  |  |
| 29 | `IDE.DATE.TIME` | `AuwhtxIncomeDistEntry_DateTime` |  |  |  |
| 30 | `IDE.AUTHORISER` | `AuwhtxIncomeDistEntry_Authoriser` | String |  |  |
| 31 | `IDE.CO.CODE` | `AuwhtxIncomeDistEntry_CoCode` | String |  |  |
| 32 | `IDE.DEPT.CODE` | `AuwhtxIncomeDistEntry_DeptCode` | String |  |  |
| 33 | `IDE.AUDITOR.CODE` | `AuwhtxIncomeDistEntry_AuditorCode` | String |  |  |
| 34 | `IDE.AUDIT.DATE.TIME` | `AuwhtxIncomeDistEntry_AuditDateTime` | String |  |  |
| 35 | `IDE.CHILD.SECURITY` | `AuwhtxIncomeDistEntry_ChildSecurity` | TField |  | The Child Security Master IDs of the Parent Diary Security Master. |
| 36 | `IDE.CHILD.INCOME.PERCENTAGE` | `AuwhtxIncomeDistEntry_ChildIncomePercentage` | TField |  | Percentage of income attributed to this child security master. |
