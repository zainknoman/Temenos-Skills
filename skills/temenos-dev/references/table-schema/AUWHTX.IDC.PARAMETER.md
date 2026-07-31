# AUWHTX.IDC.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AUWHTX.IDC.PARAMETER` in `AUWHTX_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IDC.PARAM.DESCRIPTION` | `AuwhtxIdcParameter_Description` | TField |  | Full description of the component. |
| 2 | `IDC.PARAM.TAX.COMPONENT.TYPE` | `AuwhtxIdcParameter_TaxComponentType` | TField |  | The type of tax component. Vetted to EB.LOOKUP with ID as AUWHTX.COMPONENT.TYPE |
| 3 | `IDC.PARAM.NR.TAX.COMPONENT.TYPE` | `AuwhtxIdcParameter_NrTaxComponentType` | TField |  | The type of non-resident tax component type. (Allowed input only if Component Type is Non Resident Tax). Defaulted to None. Allowed to change only if Component Type is "Non Resident Tax" Vetted to EB.LOOKUP with ID as AUWHTX.NR.COMPONENT.TYPE |
| 4 | `IDC.PARAM.RESIDENT.TAX.TREATMENT` | `AuwhtxIdcParameter_ResidentTaxTreatment` | TField |  | The resident tax treatment if the Component type is "No TFN Tax". Vetted to EB.LOOKUP with ID as AUWHTX.TAX.TREATMENT |
| 5 | `IDC.PARAM.RESIDENT.WHT.PCT` | `AuwhtxIdcParameter_ResidentWhtPct` |  |  |  |
| 6 | `IDC.PARAM.NR.RESIDENT.TAX.TREATMENT` | `AuwhtxIdcParameter_NrResidentTaxTreatment` | TField |  | The non resident tax treatment if the Component type is "NON Resident Tax". Vetted to EB.LOOKUP with ID as AUWHTX.NR.TAX.TREATMENT |
| 7 | `IDC.PARAM.NR.RESIDENT.WHT.PCT` | `AuwhtxIdcParameter_NrResidentWhtPct` |  |  |  |
| 8 | `IDC.PARAM.ACCOUNTING.COST.BASE.ADJ` | `AuwhtxIdcParameter_AccountingCostBaseAdj` | TField |  | This indicates if the accounting cost base adjustment is required. Default value is None. Changing this is permitted only if Component Type is "Year End Tax Profile" Vetted to EB.LOOKUP with ID as AUWHTX.ACCOUNTING.COST.BASE.ADJ |
| 9 | `IDC.PARAM.COST.BASE.ADJUSTMENT.TYPE` | `AuwhtxIdcParameter_CostBaseAdjustmentType` | TField |  | This indicates the type of cost base adjustment required. This is by default the Tax cost base. Default value is None. Changing this is permitted only if Component Type is "Year End Tax Profile" Vetted to EB.LOOKUP with ID as AUWHTX.COST.BASE.ADJUSTMENT.TYPE |
| 10 | `IDC.PARAM.COST.BASE.SIGN` | `AuwhtxIdcParameter_CostBaseSign` | TField |  | This indicates the sign of the cost base to be applied. Vetted to EB.LOOKUP with ID as AUWHTX.COST.BASE.SIGN |
| 11 | `IDC.PARAM.IDC.CATEGORY` | `AuwhtxIdcParameter_IdcCategory` | TField |  | The type of category such as Cash, Non Cash etc. Applicable only for Year End Components Vetted to EB.LOOKUP with ID as AUWHTX.IDC.CATEGORY |
| 12 | `IDC.PARAM.LOCAL.REF` | `AuwhtxIdcParameter_LocalRef` |  |  |  |
| 13 | `IDC.PARAM.RESERVED.1` | `AuwhtxIdcParameter_Reserved1` | TField |  |  |
| 14 | `IDC.PARAM.RESERVED.2` | `AuwhtxIdcParameter_Reserved2` | TField |  |  |
| 15 | `IDC.PARAM.RESERVED.3` | `AuwhtxIdcParameter_Reserved3` | TField |  |  |
| 16 | `IDC.PARAM.RESERVED.4` | `AuwhtxIdcParameter_Reserved4` | TField |  |  |
| 17 | `IDC.PARAM.RESERVED.5` | `AuwhtxIdcParameter_Reserved5` | TField |  |  |
| 18 | `IDC.PARAM.RESERVED.6` | `AuwhtxIdcParameter_Reserved6` | TField |  |  |
| 19 | `IDC.PARAM.RESERVED.7` | `AuwhtxIdcParameter_Reserved7` | TField |  |  |
| 20 | `IDC.PARAM.RESERVED.8` | `AuwhtxIdcParameter_Reserved8` | TField |  |  |
| 21 | `IDC.PARAM.RESERVED.9` | `AuwhtxIdcParameter_Reserved9` | TField |  |  |
| 22 | `IDC.PARAM.RESERVED.10` | `AuwhtxIdcParameter_Reserved10` | TField |  |  |
| 23 | `IDC.PARAM.OVERRIDE` | `AuwhtxIdcParameter_Override` |  |  |  |
| 24 | `IDC.PARAM.RECORD.STATUS` | `AuwhtxIdcParameter_RecordStatus` | String |  |  |
| 25 | `IDC.PARAM.CURR.NO` | `AuwhtxIdcParameter_CurrNo` | String |  |  |
| 26 | `IDC.PARAM.INPUTTER` | `AuwhtxIdcParameter_Inputter` |  |  |  |
| 27 | `IDC.PARAM.DATE.TIME` | `AuwhtxIdcParameter_DateTime` |  |  |  |
| 28 | `IDC.PARAM.AUTHORISER` | `AuwhtxIdcParameter_Authoriser` | String |  |  |
| 29 | `IDC.PARAM.CO.CODE` | `AuwhtxIdcParameter_CoCode` | String |  |  |
| 30 | `IDC.PARAM.DEPT.CODE` | `AuwhtxIdcParameter_DeptCode` | String |  |  |
| 31 | `IDC.PARAM.AUDITOR.CODE` | `AuwhtxIdcParameter_AuditorCode` | String |  |  |
| 32 | `IDC.PARAM.AUDIT.DATE.TIME` | `AuwhtxIdcParameter_AuditDateTime` | String |  |  |
