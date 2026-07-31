# AUWHTX.INCOME.WHT.DETAILS — Table Schema

> Source: `INSERTS/I_F.AUWHTX.INCOME.WHT.DETAILS` in `AUWHTX_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IDC.WHT.CURRENCY` | `AuwhtxIncomeWhtDetails_Currency` | TField |  | Identifies the Currency of the Security. It is a No Input Field. |
| 2 | `IDC.WHT.TAX.COMPONENT.TYPE` | `AuwhtxIncomeWhtDetails_TaxComponentType` | TField |  | The type of tax component. It is a No Input Field. It will have Value as NONRESIDENTTAX, NOTFNTAX or RESIDENTWITHTFN. |
| 3 | `IDC.WHT.COMPONENT` | `AuwhtxIncomeWhtDetails_Component` |  |  |  |
| 4 | `IDC.WHT.VALUE` | `AuwhtxIncomeWhtDetails_Value` |  |  |  |
| 5 | `IDC.WHT.TOTAL` | `AuwhtxIncomeWhtDetails_Total` | TField |  | The total value of all the Components. |
| 6 | `IDC.WHT.LOCAL.REF` | `AuwhtxIncomeWhtDetails_LocalRef` |  |  |  |
| 7 | `IDC.WHT.RND.ADJ.COMPONENT` | `AuwhtxIncomeWhtDetails_RndAdjComponent` | TField |  |  |
| 8 | `IDC.WHT.RND.ADJ.AMT` | `AuwhtxIncomeWhtDetails_RndAdjAmt` | TField |  |  |
| 9 | `IDC.WHT.TOTAL.COMPONENT.VALUE.LCY` | `AuwhtxIncomeWhtDetails_TotalComponentValueLcy` | TField |  | Total component value in local currency of the company. |
| 10 | `IDC.WHT.TOTAL.WHT.VALUE.LCY` | `AuwhtxIncomeWhtDetails_TotalWhtValueLcy` | TField |  | Total withholding tax value in local currency of the company. |
| 11 | `IDC.WHT.RESERVED.5` | `AuwhtxIncomeWhtDetails_Reserved5` | TField |  |  |
| 12 | `IDC.WHT.RESERVED.6` | `AuwhtxIncomeWhtDetails_Reserved6` | TField |  |  |
| 13 | `IDC.WHT.RESERVED.7` | `AuwhtxIncomeWhtDetails_Reserved7` | TField |  |  |
| 14 | `IDC.WHT.RESERVED.8` | `AuwhtxIncomeWhtDetails_Reserved8` | TField |  |  |
| 15 | `IDC.WHT.RESERVED.9` | `AuwhtxIncomeWhtDetails_Reserved9` | TField |  |  |
| 16 | `IDC.WHT.RESERVED.10` | `AuwhtxIncomeWhtDetails_Reserved10` | TField |  |  |
| 17 | `IDC.WHT.OVERRIDE` | `AuwhtxIncomeWhtDetails_Override` |  |  |  |
| 18 | `IDC.WHT.RECORD.STATUS` | `AuwhtxIncomeWhtDetails_RecordStatus` | String |  |  |
| 19 | `IDC.WHT.CURR.NO` | `AuwhtxIncomeWhtDetails_CurrNo` | String |  |  |
| 20 | `IDC.WHT.INPUTTER` | `AuwhtxIncomeWhtDetails_Inputter` |  |  |  |
| 21 | `IDC.WHT.DATE.TIME` | `AuwhtxIncomeWhtDetails_DateTime` |  |  |  |
| 22 | `IDC.WHT.AUTHORISER` | `AuwhtxIncomeWhtDetails_Authoriser` | String |  |  |
| 23 | `IDC.WHT.CO.CODE` | `AuwhtxIncomeWhtDetails_CoCode` | String |  |  |
| 24 | `IDC.WHT.DEPT.CODE` | `AuwhtxIncomeWhtDetails_DeptCode` | String |  |  |
| 25 | `IDC.WHT.AUDITOR.CODE` | `AuwhtxIncomeWhtDetails_AuditorCode` | String |  |  |
| 26 | `IDC.WHT.AUDIT.DATE.TIME` | `AuwhtxIncomeWhtDetails_AuditDateTime` | String |  |  |
| 27 | `IDC.WHT.PORTFOLIO.ID` | `AuwhtxIncomeWhtDetails_PortfolioId` | TField |  | The Portfolio ID of the Customer. It is a No Input Field. |
| 28 | `IDC.WHT.TAX.RESIDENCE` | `AuwhtxIncomeWhtDetails_TaxResidence` | TField |  | The Residence of the Customer defaulted from SEC.ACC.MASTER. It is a No Input Field. |
| 29 | `IDC.WHT.INCOME.AMOUNT` | `AuwhtxIncomeWhtDetails_IncomeAmount` | TField |  | The Entitlement Amount. It is a No Input Field. |
| 30 | `IDC.WHT.TAX.AMOUNT` | `AuwhtxIncomeWhtDetails_TaxAmount` | TField |  | The Tax Amount which is defaulted from either the Local Tax Amount or Source Tax Amount from Entitlement. It is a No Input Field. |
| 31 | `IDC.WHT.ENTITLE.AUTHORISED` | `AuwhtxIncomeWhtDetails_EntitleAuthorised` | TField |  | This field Indicates if the respective Entitlement Record is authorised or not. It is a No Input Field. It will be checked in once the Entitlement record gets authorised. |
| 32 | `IDC.WHT.SYS.VALUE` | `AuwhtxIncomeWhtDetails_SysValue` |  |  |  |
| 33 | `IDC.WHT.WHT.RATE` | `AuwhtxIncomeWhtDetails_WhtRate` |  |  |  |
| 34 | `IDC.WHT.WHT.VALUE` | `AuwhtxIncomeWhtDetails_WhtValue` |  |  |  |
| 35 | `IDC.WHT.SYS.WHT.VALUE` | `AuwhtxIncomeWhtDetails_SysWhtValue` |  |  |  |
| 36 | `IDC.WHT.UNALLOCATED.NR.AMT` | `AuwhtxIncomeWhtDetails_UnallocatedNrAmt` | TField |  | The value of the unallocated Non Resident component. It is a No Input Field. |
| 37 | `IDC.WHT.WHT.ADJ.AMOUNT` | `AuwhtxIncomeWhtDetails_WhtAdjAmount` | TField |  | The Withholding Adjusted Amount. |
| 38 | `IDC.WHT.SYS.WHT.ADJ.AMOUNT` | `AuwhtxIncomeWhtDetails_SysWhtAdjAmount` | TField |  | The system calculated Withholding Adjusted Amount. |
| 39 | `IDC.WHT.TOTAL.WHT.VALUE` | `AuwhtxIncomeWhtDetails_TotalWhtValue` | TField |  | The total of all the WHT Values and WHT Adj Amount. |
| 40 | `IDC.WHT.STATUS.INDICATOR` | `AuwhtxIncomeWhtDetails_StatusIndicator` | TField |  | This field indicates the Status of the respective Entitlement Record. It is a No Input Field. It will have Value as Deleted, Reversed or None. |
| 41 | `IDC.WHT.SYS.CALC.WHT` | `AuwhtxIncomeWhtDetails_SysCalcWht` | TField |  | The field stores the system calculated withholding tax amount. It is a No Input Field. |
| 42 | `IDC.WHT.COMPONENT.VALUE.LCY` | `AuwhtxIncomeWhtDetails_ComponentValueLcy` |  |  |  |
| 43 | `IDC.WHT.WHT.VALUE.LCY` | `AuwhtxIncomeWhtDetails_WhtValueLcy` |  |  |  |
