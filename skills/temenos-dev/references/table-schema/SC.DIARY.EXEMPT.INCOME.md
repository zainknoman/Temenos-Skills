# SC.DIARY.EXEMPT.INCOME — Table Schema

> Source: `INSERTS/I_F.SC.DIARY.EXEMPT.INCOME` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.FA.FATCA.TAX.TYPE` | `ScDiaryExemptIncome_FatcaTaxType` | TField |  | The tax type to which the taxable income and exempt income, specified here, pertains to. validation rules: The field is automatically updated based on the TAX.TYPE specified in the ID and is a no input field. |
| 2 | `SC.FA.DIARY.ID` | `ScDiaryExemptIncome_DiaryId` | TField |  | The DIARY to which the taxable income and exempt income, specified here, pertains to. validation rules: The field is automatically updated based on the DIARY reference specified in the ID and is a no-input field. |
| 3 | `SC.FA.TAXABLE.INCOME` | `ScDiaryExemptIncome_TaxableIncome` | TField |  | The proportion of income that is subject to withholding is set in this field. By default, the entire income will be considered taxable. However, in order to cater to events where certain portion of income is not subject to tax (e.g. non-US source income in the case of distribution by funds), the taxable income is given here. validation rules: : Percentage not exceeding 100% |
| 4 | `SC.FA.CLIENT.ID` | `ScDiaryExemptIncome_ClientId` |  |  |  |
| 5 | `SC.FA.EXEMPT.AMT` | `ScDiaryExemptIncome_ExemptAmt` |  |  |  |
| 6 | `SC.FA.EXEMPT.PERC` | `ScDiaryExemptIncome_ExemptPerc` |  |  |  |
| 7 | `SC.FA.GROSS.OR.NET` | `ScDiaryExemptIncome_GrossOrNet` | TField |  | The field controls whether the reinvestment is to be on a gross basis (before application of withholding) or on net amount post the withholding. Example: ANC Corporation declares a dividend of $1.5 per share which can be reinvested in the stock at $10 per share. A client who holds 5000 shares of ANC will receive a dividend of $7500. If the income is subject to withholding, the net amount available for reinvestment will be $5250 (30% WHT) with which he can acquire 525 additional shares of ANC. If the field is set to GROSS, the reinvestment will be based on the gross amount (in the above example, $7500 will be reinvested) with the tax amount being deducted separately. validation rules: GROSS or NET with input only allowed for Reinvestment event (DIARY TYPE flag). The field cannot be set to GROSS if the DIARY RATE.TYPE is net. By default, the reinvestment will be on a gross basis. |
| 8 | `SC.FA.RESERVED.5` | `ScDiaryExemptIncome_Reserved5` | TField |  |  |
| 9 | `SC.FA.RESERVED.4` | `ScDiaryExemptIncome_Reserved4` | TField |  |  |
| 10 | `SC.FA.RESERVED.3` | `ScDiaryExemptIncome_Reserved3` | TField |  |  |
| 11 | `SC.FA.RESERVED.2` | `ScDiaryExemptIncome_Reserved2` | TField |  |  |
| 12 | `SC.FA.RESERVED.1` | `ScDiaryExemptIncome_Reserved1` | TField |  |  |
| 13 | `SC.FA.LOCAL.REF` | `ScDiaryExemptIncome_LocalRef` |  |  |  |
| 14 | `SC.FA.OVERRIDE` | `ScDiaryExemptIncome_Override` |  |  |  |
| 15 | `SC.FA.RECORD.STATUS` | `ScDiaryExemptIncome_RecordStatus` | String |  |  |
| 16 | `SC.FA.CURR.NO` | `ScDiaryExemptIncome_CurrNo` | String |  |  |
| 17 | `SC.FA.INPUTTER` | `ScDiaryExemptIncome_Inputter` |  |  |  |
| 18 | `SC.FA.DATE.TIME` | `ScDiaryExemptIncome_DateTime` |  |  |  |
| 19 | `SC.FA.AUTHORISER` | `ScDiaryExemptIncome_Authoriser` | String |  |  |
| 20 | `SC.FA.CO.CODE` | `ScDiaryExemptIncome_CoCode` | String |  |  |
| 21 | `SC.FA.DEPT.CODE` | `ScDiaryExemptIncome_DeptCode` | String |  |  |
| 22 | `SC.FA.AUDITOR.CODE` | `ScDiaryExemptIncome_AuditorCode` | String |  |  |
| 23 | `SC.FA.AUDIT.DATE.TIME` | `ScDiaryExemptIncome_AuditDateTime` | String |  |  |
