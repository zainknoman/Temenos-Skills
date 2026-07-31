# FS.GA.CAP.FEE.EXPENSE — Table Schema

> Source: `INSERTS/I_F.FS.GA.CAP.FEE.EXPENSE` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GA.CAP.FEE.EXPENSE.FUND.ID` | `FsGaCapFeeExpense_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `GA.CAP.FEE.EXPENSE.FEE.CAP` | `FsGaCapFeeExpense_FeeCap` | TField |  | Fee Cap Multifonds DB Column is NOFRAIS_CAP. |
| 3 | `GA.CAP.FEE.EXPENSE.ADJUSTED.FEE` | `FsGaCapFeeExpense_AdjustedFee` | TField |  | Adjusted Fee Multifonds DB Column is NOFRAIS_ADJ. |
| 4 | `GA.CAP.FEE.EXPENSE.ORDER` | `FsGaCapFeeExpense_Order` | TField |  | The column Order allows defining an order in the fee adjustment. Only numerical characters have to be entered Multifonds DB Column is NORDER. |
| 5 | `GA.CAP.FEE.EXPENSE.GL.ACCOUNT` | `FsGaCapFeeExpense_GlAccount` | TField |  | Cash Account Number Multifonds DB Column is NRUBR. |
| 6 | `GA.CAP.FEE.EXPENSE.TYPE.OF.EXPENSES` | `FsGaCapFeeExpense_TypeOfExpenses` | TField |  | Type of expenses to be linked to CAP FEE, there are two options 1.Proportional Method and 2.Sequential Method Multifonds DB Column is TYP_EXP. |
| 7 | `GA.CAP.FEE.EXPENSE.PRO.PERCENTAGE` | `FsGaCapFeeExpense_ProPercentage` | TField |  | This field Automatically populated by the system based on the type as explained for the column "Type" Multifonds DB Column is PROPCT. |
| 8 | `GA.CAP.FEE.EXPENSE.FEE.NUMBER` | `FsGaCapFeeExpense_FeeNumber` | TField |  | Refers to the Charge ID linked to another NAV charges in order to put the adjustment into those accounts Multifonds DB Column is NOFRAIS_EXP. |
| 9 | `GA.CAP.FEE.EXPENSE.RESERVED10` | `FsGaCapFeeExpense_Reserved10` | TField |  |  |
| 10 | `GA.CAP.FEE.EXPENSE.RESERVED9` | `FsGaCapFeeExpense_Reserved9` | TField |  |  |
| 11 | `GA.CAP.FEE.EXPENSE.RESERVED8` | `FsGaCapFeeExpense_Reserved8` | TField |  |  |
| 12 | `GA.CAP.FEE.EXPENSE.RESERVED7` | `FsGaCapFeeExpense_Reserved7` | TField |  |  |
| 13 | `GA.CAP.FEE.EXPENSE.RESERVED6` | `FsGaCapFeeExpense_Reserved6` | TField |  |  |
| 14 | `GA.CAP.FEE.EXPENSE.RESERVED5` | `FsGaCapFeeExpense_Reserved5` | TField |  |  |
| 15 | `GA.CAP.FEE.EXPENSE.RESERVED4` | `FsGaCapFeeExpense_Reserved4` | TField |  |  |
| 16 | `GA.CAP.FEE.EXPENSE.RESERVED3` | `FsGaCapFeeExpense_Reserved3` | TField |  |  |
| 17 | `GA.CAP.FEE.EXPENSE.RESERVED2` | `FsGaCapFeeExpense_Reserved2` | TField |  |  |
| 18 | `GA.CAP.FEE.EXPENSE.RESERVED1` | `FsGaCapFeeExpense_Reserved1` | TField |  |  |
| 19 | `GA.CAP.FEE.EXPENSE.LOCAL.REF` | `FsGaCapFeeExpense_LocalRef` |  |  |  |
| 20 | `GA.CAP.FEE.EXPENSE.OVERRIDE` | `FsGaCapFeeExpense_Override` |  |  |  |
| 21 | `GA.CAP.FEE.EXPENSE.RECORD.STATUS` | `FsGaCapFeeExpense_RecordStatus` | String |  |  |
| 22 | `GA.CAP.FEE.EXPENSE.CURR.NO` | `FsGaCapFeeExpense_CurrNo` | String |  |  |
| 23 | `GA.CAP.FEE.EXPENSE.INPUTTER` | `FsGaCapFeeExpense_Inputter` |  |  |  |
| 24 | `GA.CAP.FEE.EXPENSE.DATE.TIME` | `FsGaCapFeeExpense_DateTime` |  |  |  |
| 25 | `GA.CAP.FEE.EXPENSE.AUTHORISER` | `FsGaCapFeeExpense_Authoriser` | String |  |  |
| 26 | `GA.CAP.FEE.EXPENSE.CO.CODE` | `FsGaCapFeeExpense_CoCode` | String |  |  |
| 27 | `GA.CAP.FEE.EXPENSE.DEPT.CODE` | `FsGaCapFeeExpense_DeptCode` | String |  |  |
| 28 | `GA.CAP.FEE.EXPENSE.AUDITOR.CODE` | `FsGaCapFeeExpense_AuditorCode` | String |  |  |
| 29 | `GA.CAP.FEE.EXPENSE.AUDIT.DATE.TIME` | `FsGaCapFeeExpense_AuditDateTime` | String |  |  |
