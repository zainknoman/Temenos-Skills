# AUWHTX.IDC.YEAR.END.TAX.PROFILE — Table Schema

> Source: `INSERTS/I_F.AUWHTX.IDC.YEAR.END.TAX.PROFILE` in `AUWHTX_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IDC.TAX.DIARY.ID` | `AuwhtxIdcYearEndTaxProfile_DiaryId` |  |  |  |
| 2 | `IDC.TAX.APPL.CUSTOMER.TYPE` | `AuwhtxIdcYearEndTaxProfile_ApplCustomerType` | TField |  | This field holds, ALL or Residents or Non-Residents. This field value is defaulted to ALL, but can be changed. The Year End component would need to be separately specified for residents and non residents in situations when some components are applicable for residents while some components like NANE are applicable only for non residents. |
| 3 | `IDC.TAX.SECURITY.NO` | `AuwhtxIdcYearEndTaxProfile_SecurityNo` | TField |  | This field a NOINPUT field. This field holds the value of the SECURITY.NO of the Diary. |
| 4 | `IDC.TAX.YEAR.END.TAX.TYPE` | `AuwhtxIdcYearEndTaxProfile_YearEndTaxType` | TField |  | The Year End Tax type as to if it is an interim or final. |
| 5 | `IDC.TAX.ENTITLEMENT.BASE` | `AuwhtxIdcYearEndTaxProfile_EntitlementBase` | TField |  | TThis field indicates if the total sum of all the Cash components entered in the Year end profile should be matched with a value provided in the field Percentage to be matched. |
| 6 | `IDC.TAX.PERCENTAGE.TO.MATCHED` | `AuwhtxIdcYearEndTaxProfile_PercentageToMatched` | TField |  | The percentage which should be matched with the sum of total cash components entered. |
| 7 | `IDC.TAX.SURPLUS.DEFICIT.PERCENTAGE` | `AuwhtxIdcYearEndTaxProfile_SurplusDeficitPercentage` | TField |  | This field a NOINPUT field. The surplus or deficit in terms of sum of cash components should be updated here. |
| 8 | `IDC.TAX.TOTAL.AMT` | `AuwhtxIdcYearEndTaxProfile_TotalAmt` | TField |  | This field holds The total amount of all the Diary records selected should be calculated here. |
| 9 | `IDC.TAX.TAX.YEAR.END` | `AuwhtxIdcYearEndTaxProfile_TaxYearEnd` | TField |  | The tax year end associated with this record. Year to be defaulted from Company table. |
| 10 | `IDC.TAX.COMPONENT` | `AuwhtxIdcYearEndTaxProfile_Component` |  |  |  |
| 11 | `IDC.TAX.COMPONENT.PERCENTAGE` | `AuwhtxIdcYearEndTaxProfile_ComponentPercentage` |  |  |  |
| 12 | `IDC.TAX.INCOME.EXCH.RATE` | `AuwhtxIdcYearEndTaxProfile_IncomeExchRate` | TField |  | The exchange rate used for calculating the foreign exchange gain or loss. This is relevant only in those corporate actions with multi-currency dividend where some entitlement holders opt for income in event currency while some opt for income in local currency. |
| 13 | `IDC.TAX.CALC.FX.GAIN.LOSS` | `AuwhtxIdcYearEndTaxProfile_CalcFxGainLoss` | TField |  | Indicates if the Fx loss or gain should be calculated based on the rate. Allowed Yes only if INCOME.EXCH.RATE is populated (manually/by the system) |
| 14 | `IDC.TAX.FX.GAIN.LOSS.PER.UNIT` | `AuwhtxIdcYearEndTaxProfile_FxGainLossPerUnit` | TField |  | This is the exchange rate differential used to calculate the fx_gain_or_loss. |
| 15 | `IDC.TAX.FITO.APPLICABLE` | `AuwhtxIdcYearEndTaxProfile_FitoApplicable` | TField |  | This indicates if the FITO is applicable for the event. |
| 16 | `IDC.TAX.FITO.COMPONENT` | `AuwhtxIdcYearEndTaxProfile_FitoComponent` | TField |  | This field indicates the FITO component. |
| 17 | `IDC.TAX.RESERVED.6` | `AuwhtxIdcYearEndTaxProfile_Reserved6` | TField |  |  |
| 18 | `IDC.TAX.RESERVED.7` | `AuwhtxIdcYearEndTaxProfile_Reserved7` | TField |  |  |
| 19 | `IDC.TAX.RESERVED.8` | `AuwhtxIdcYearEndTaxProfile_Reserved8` | TField |  |  |
| 20 | `IDC.TAX.RESERVED.9` | `AuwhtxIdcYearEndTaxProfile_Reserved9` | TField |  |  |
| 21 | `IDC.TAX.RESERVED.10` | `AuwhtxIdcYearEndTaxProfile_Reserved10` | TField |  |  |
| 22 | `IDC.TAX.LOCAL.REF` | `AuwhtxIdcYearEndTaxProfile_LocalRef` |  |  |  |
| 23 | `IDC.TAX.OVERRIDE` | `AuwhtxIdcYearEndTaxProfile_Override` |  |  |  |
| 24 | `IDC.TAX.RECORD.STATUS` | `AuwhtxIdcYearEndTaxProfile_RecordStatus` | String |  |  |
| 25 | `IDC.TAX.CURR.NO` | `AuwhtxIdcYearEndTaxProfile_CurrNo` | String |  |  |
| 26 | `IDC.TAX.INPUTTER` | `AuwhtxIdcYearEndTaxProfile_Inputter` |  |  |  |
| 27 | `IDC.TAX.DATE.TIME` | `AuwhtxIdcYearEndTaxProfile_DateTime` |  |  |  |
| 28 | `IDC.TAX.AUTHORISER` | `AuwhtxIdcYearEndTaxProfile_Authoriser` | String |  |  |
| 29 | `IDC.TAX.CO.CODE` | `AuwhtxIdcYearEndTaxProfile_CoCode` | String |  |  |
| 30 | `IDC.TAX.DEPT.CODE` | `AuwhtxIdcYearEndTaxProfile_DeptCode` | String |  |  |
| 31 | `IDC.TAX.AUDITOR.CODE` | `AuwhtxIdcYearEndTaxProfile_AuditorCode` | String |  |  |
| 32 | `IDC.TAX.AUDIT.DATE.TIME` | `AuwhtxIdcYearEndTaxProfile_AuditDateTime` | String |  |  |
| 33 | `IDC.TAX.CHILD.SECURITY` | `AuwhtxIdcYearEndTaxProfile_ChildSecurity` |  |  |  |
| 34 | `IDC.TAX.CHILD.INCOME.PERCENTAGE` | `AuwhtxIdcYearEndTaxProfile_ChildIncomePercentage` |  |  |  |
| 35 | `IDC.TAX.NEW.CHILD.SECURITY` | `AuwhtxIdcYearEndTaxProfile_NewChildSecurity` | TField |  | The Child Security Master ID of the Parent Diary Security Master. |
