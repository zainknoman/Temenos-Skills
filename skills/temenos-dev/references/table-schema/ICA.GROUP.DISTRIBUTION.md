# ICA.GROUP.DISTRIBUTION — Table Schema

> Source: `INSERTS/I_F.ICA.GROUP.DISTRIBUTION` in `IC_OtherInterest.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ICA.DIS.MAX.PROC.LEVEL` | `IcaGroupDistribution_MaxProcLevel` | TField |  | MAX.PROC.LEVEL This field stores the highest number of links (or levels) between this account and the top of the ICA hierarchies it has been a member of. An ICA hierarchy consists of linked groups of accounts, each group has a main account to which sub accounts are linked. A main account in one group can be a sub account in another group. The main account of the highest level group is the top account. In order to calculate ICA group interest the combined balances of all in the group are used. If a group contains sub accounts which are themselves main accounts of lower level groups then group interest is calculated using the group balances of the lower level group of which the sub account is the main account rather than the balance of the sub account itself. The balances of each group are combined into special ACCT.ACTIVITY records, which contain the combined balances for the whole group. This scenario requires that the lowest level groups in the hierarchy are processed first so that their combined balances are available for the group interest calculations of the higher level groups. The structure of the ICA hierarchy can also change with time as group links can be moved from one level to another or even to different hierarchies. The MAX.PROC.LEVEL field is used to store the lowest level that a group has been, (in fact the highest number of links between it and the top of a hierarchy) in order that the ICA group interest processing takes place in the correct order. Validation Rules: Numeric field |
| 2 | `ICA.DIS.INTEREST.CALC` | `IcaGroupDistribution_InterestCalc` | TField |  | INTEREST.CALC Indicates the capitalisation interest calculations to perform. Each character in the 6 character field means the following Validation Rules: 6 character alphabetic field |
| 3 | `ICA.DIS.START.DATE.DR` | `IcaGroupDistribution_StartDateDr` | TField |  | START.DATE.DR Indicates the start date for the debit capitalisation period Validation Rules: Date |
| 4 | `ICA.DIS.START.DATE.DR2` | `IcaGroupDistribution_StartDateDr2` | TField |  | START.DATE.DR2 Indicates the start date for the debit 2 capitalisation period Validation Rules: Date |
| 5 | `ICA.DIS.START.DATE.CR` | `IcaGroupDistribution_StartDateCr` | TField |  | START.DATE.CR Indicates the start date for the credit capitalisation period Validation Rules: Date |
| 6 | `ICA.DIS.START.DATE.CR2` | `IcaGroupDistribution_StartDateCr2` | TField |  | START.DATE.CR2 Indicates the start date for the credit 2 capitalisation period Validation Rules: Date |
| 7 | `ICA.DIS.END.DATE` | `IcaGroupDistribution_EndDate` | TField |  | END.DATE Indicates the end date of the current capitalisation period for the main account in the group. I.e. when it was capitalised. Validation Rules: Date |
| 8 | `ICA.DIS.MAIN.ACCTY.KEY` | `IcaGroupDistribution_MainAcctyKey` |  |  |  |
| 9 | `ICA.DIS.PARTIAL.ACCOUNT` | `IcaGroupDistribution_PartialAccount` |  |  |  |
| 10 | `ICA.DIS.PART.ACCTYS` | `IcaGroupDistribution_PartAcctys` |  |  |  |
| 11 | `ICA.DIS.PART.STMTCR` | `IcaGroupDistribution_PartStmtcr` |  |  |  |
| 12 | `ICA.DIS.PART.STMTC2` | `IcaGroupDistribution_PartStmtc2` |  |  |  |
| 13 | `ICA.DIS.PART.STMTDR` | `IcaGroupDistribution_PartStmtdr` |  |  |  |
| 14 | `ICA.DIS.PART.STMTD2` | `IcaGroupDistribution_PartStmtd2` |  |  |  |
| 15 | `ICA.DIS.RUN.DATE` | `IcaGroupDistribution_RunDate` | TField |  | RUN.DATE Contains the system end of day date indicating when the group calculation was actually performed. Validation Rules: Date |
| 16 | `ICA.DIS.OLDEST.DATE` | `IcaGroupDistribution_OldestDate` | TField |  | The oldest start date for this capitalisation period |
