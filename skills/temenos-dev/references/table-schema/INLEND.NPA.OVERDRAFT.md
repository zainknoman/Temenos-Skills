# INLEND.NPA.OVERDRAFT — Table Schema

> Source: `INSERTS/I_F.INLEND.NPA.OVERDRAFT` in `INLEND_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.OD.LAST.DEBIT.DATE` | `InlendNpaOverdraft_LastDebitDate` | TField |  | It denotes the date on which the Last debit transaction done for an account. |
| 2 | `INLEND.OD.LAST.CREDIT.DATE` | `InlendNpaOverdraft_LastCreditDate` | TField |  | It denotes the date on which the Last credit transaction done for an account. |
| 3 | `INLEND.OD.LAST.INT.CAP.DATE` | `InlendNpaOverdraft_LastIntCapDate` |  |  |  |
| 4 | `INLEND.OD.INT.CAP.AMOUNT` | `InlendNpaOverdraft_IntCapAmount` |  |  |  |
| 5 | `INLEND.OD.CREDIT.AMOUNT` | `InlendNpaOverdraft_CreditAmount` | TField |  | Cumulative sum of credit amount, Update during credit transaction. |
| 6 | `INLEND.OD.NPA.IRREGULAR` | `InlendNpaOverdraft_NpaIrregular` | TField |  | Flag used to state that account is under Npa Irregular, its update is based on the account's transaction. |
| 7 | `INLEND.OD.AGEING.DAYS` | `InlendNpaOverdraft_AgeingDays` | TField |  | Ageing Days will be calculated after interest capitalization till sufficient credit to realize the capitalized interest. |
| 8 | `INLEND.OD.NO.CR.AGEING.DAYS` | `InlendNpaOverdraft_NoCrAgeingDays` | TField |  | No Cr Ageing Days will be calculated after debit till any repayemnt or credit . |
| 9 | `INLEND.OD.UNREALISED.AMOUNT` | `InlendNpaOverdraft_UnrealisedAmount` | TField |  | The unrealised amount will be captured during repayment if only capitalised charge is available. |
| 10 | `INLEND.OD.RESERVED.7` | `InlendNpaOverdraft_Reserved7` | TField |  |  |
| 11 | `INLEND.OD.RESERVED.6` | `InlendNpaOverdraft_Reserved6` | TField |  |  |
| 12 | `INLEND.OD.RESERVED.5` | `InlendNpaOverdraft_Reserved5` | TField |  |  |
| 13 | `INLEND.OD.RESERVED.4` | `InlendNpaOverdraft_Reserved4` | TField |  |  |
| 14 | `INLEND.OD.RESERVED.3` | `InlendNpaOverdraft_Reserved3` | TField |  |  |
| 15 | `INLEND.OD.RESERVED.2` | `InlendNpaOverdraft_Reserved2` | TField |  |  |
| 16 | `INLEND.OD.RESERVED.1` | `InlendNpaOverdraft_Reserved1` | TField |  |  |
| 17 | `INLEND.OD.INT.PROPERTY` | `InlendNpaOverdraft_IntProperty` |  |  |  |
| 18 | `INLEND.OD.POS.ACC.INT` | `InlendNpaOverdraft_PosAccInt` |  |  |  |
| 19 | `INLEND.OD.SUSP.OVERDUE.INT` | `InlendNpaOverdraft_SuspOverdueInt` |  |  |  |
| 20 | `INLEND.OD.REGULARISED.INT` | `InlendNpaOverdraft_RegularisedInt` |  |  |  |
| 21 | `INLEND.OD.CHG.PROPERTY` | `InlendNpaOverdraft_ChgProperty` |  |  |  |
| 22 | `INLEND.OD.CHG.CAP.DATE` | `InlendNpaOverdraft_ChgCapDate` |  |  |  |
| 23 | `INLEND.OD.CHG.CAP.AMOUNT` | `InlendNpaOverdraft_ChgCapAmount` |  |  |  |
| 24 | `INLEND.OD.POS.CHARGE` | `InlendNpaOverdraft_PosCharge` |  |  |  |
| 25 | `INLEND.OD.SUSP.OVERDUE.CHRG` | `InlendNpaOverdraft_SuspOverdueChrg` |  |  |  |
| 26 | `INLEND.OD.REGULARISED.CHG` | `InlendNpaOverdraft_RegularisedChg` |  |  |  |
| 27 | `INLEND.OD.SUSPEND.CHARGE` | `InlendNpaOverdraft_SuspendCharge` |  |  |  |
| 28 | `INLEND.OD.SUSP.OVERDUEACC.INT` | `InlendNpaOverdraft_SuspOverdueaccInt` |  |  |  |
| 29 | `INLEND.OD.INT.REPAID.AMOUNT` | `InlendNpaOverdraft_IntRepaidAmount` |  |  |  |
