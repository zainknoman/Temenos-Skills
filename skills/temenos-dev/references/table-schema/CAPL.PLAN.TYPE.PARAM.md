# CAPL.PLAN.TYPE.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.PLAN.TYPE.PARAM` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.PTP.DESCRIPTION` | `CaplPlanTypeParam_Description` |  |  |  |
| 2 | `CAPL.PTP.WITHIN.PERIOD` | `CaplPlanTypeParam_WithinPeriod` | TField | Yes | Field is used to Specify the Month and Date for defining the allowed period. Allowed period is the period from death of date of the annuitant till December 31st of the next year.Validation : Format should be MMDD - validate first two digits should be 1 to 12 and the other two digits should be 1 to 31.Mandatory field.Eg. 1231 |
| 3 | `CAPL.PTP.WITHIN.PLUS` | `CaplPlanTypeParam_WithinPlus` | TField | Yes | Field is used to Specify the number of months to define the after allowed. After the allowed period is one year after the allowed period defined in field WITHIN.PERIOD.Format will be M12 - validate first digit should be 'M' and next two digit should be numeric.Mandatory field.Eg. M12 |
| 4 | `CAPL.PTP.RESIDENCE` | `CaplPlanTypeParam_Residence` | TField |  | Field to used to store the customer Residence to be considered for grouping the plansValidation - record from RESIDENCE |
| 5 | `CAPL.PTP.CONTR.TXN.NO` | `CaplPlanTypeParam_ContrTxnNo` | TField |  | Field is used to Define the Plan transaction code, that will be used for register plan contributions.Validations : Link to CAPL.PLAN.TXNS |
| 6 | `CAPL.PTP.CONTR.FT.TXN.CODE` | `CaplPlanTypeParam_ContrFtTxnCode` | TField | Yes | Field to store the T24 transaction code that will be used for register plan contributions.Validation : Link to FT.TXN.TYPE.CONDITION.Mandatory field. |
| 7 | `CAPL.PTP.REL.CODE.BENEFICIARY` | `CaplPlanTypeParam_RelCodeBeneficiary` |  |  |  |
| 8 | `CAPL.PTP.REL.CODE.SPOUSE` | `CaplPlanTypeParam_RelCodeSpouse` |  |  |  |
| 9 | `CAPL.PTP.FT.TXN.CODE.REV` | `CaplPlanTypeParam_FtTxnCodeRev` | TField | Yes | Field to store the transaction code will be used when reversing registered plans transactions.Link to FT.TXN.TYPE.CONDITION. Mandatory field. |
| 10 | `CAPL.PTP.REVE.CATEGORY` | `CaplPlanTypeParam_ReveCategory` | TField | Yes | Field is used to define the category that will be used to post the reversals. Usually the reversals are taken from teller account.Link to CATEGORY Table.Mandatory Field. |
| 11 | `CAPL.PTP.MIGRATION.DATE` | `CaplPlanTypeParam_MigrationDate` | TField | Yes | Field is used to store the Date on which the registered plans have been converted from the legacy system to T24. If the customer is deceased before this date, T24 will look into the file CAPL.USER.PLAN.VALUES that keeps the balances for the accounts and plans for those customers that were deceased before the migration.date but their holding are pending settlement.Mandatory Field. |
| 12 | `CAPL.PTP.REG.PLAN.TYP.CODE` | `CaplPlanTypeParam_RegPlanTypCode` | TField |  |  |
| 13 | `CAPL.PTP.IMPLEM.METHOD` | `CaplPlanTypeParam_ImplemMethod` |  |  |  |
| 14 | `CAPL.PTP.PRIORITY.PLAN.TYPE` | `CaplPlanTypeParam_PriorityPlanType` | TField |  |  |
| 15 | `CAPL.PTP.SAM.NEW.CREATE.VERSION` | `CaplPlanTypeParam_SamNewCreateVersion` | TField |  |  |
| 16 | `CAPL.PTP.SAM.LINK.CONV.VERSION` | `CaplPlanTypeParam_SamLinkConvVersion` | TField |  |  |
| 17 | `CAPL.PTP.SAM.B.CONV.VERSION` | `CaplPlanTypeParam_SamBConvVersion` | TField |  |  |
| 18 | `CAPL.PTP.SAM.B.PART.EXT.VERSION` | `CaplPlanTypeParam_SamBPartExtVersion` | TField |  |  |
| 19 | `CAPL.PTP.OFS.VERSION` | `CaplPlanTypeParam_OfsVersion` | TField |  |  |
| 20 | `CAPL.PTP.FT.VERSION` | `CaplPlanTypeParam_FtVersion` | TField |  |  |
| 21 | `CAPL.PTP.PAYOUT.ACTIVITY` | `CaplPlanTypeParam_PayoutActivity` | TField |  | If PAYOUT.ACTIVITY field is parameterised with a valid activity, then that activity will be triggered during payout.If PAYOUT.ACTIVITY field is not parameterised/blank, then BY default ACCOUNTS-SETTLE-PAYOFF will be triggered during payout.LINKED TO AA.ACTIVITY |
| 22 | `CAPL.PTP.UPGRADE.DATE` | `CaplPlanTypeParam_UpgradeDate` | TField |  | This field is used for the client who is upgrading from AC/AZ to AA. The date defined in this field is used to calculate plan values differently considering AC/AZ Versa AA. Note: This field needs to be inputted only by client who is migrating from AC/AZ to AA and not all upgrade clients. |
| 23 | `CAPL.PTP.RIF.CONV.CLR.FLDS` | `CaplPlanTypeParam_RifConvClrFlds` |  |  |  |
| 24 | `CAPL.PTP.RESERVED.4` | `CaplPlanTypeParam_Reserved4` |  |  |  |
| 25 | `CAPL.PTP.RESERVED.3` | `CaplPlanTypeParam_Reserved3` | TField |  |  |
| 26 | `CAPL.PTP.RESERVED.2` | `CaplPlanTypeParam_Reserved2` | TField |  |  |
| 27 | `CAPL.PTP.RESERVED.1` | `CaplPlanTypeParam_Reserved1` | TField |  |  |
| 28 | `CAPL.PTP.LOCAL.REF` | `CaplPlanTypeParam_LocalRef` |  |  |  |
| 29 | `CAPL.PTP.OVERRIDE` | `CaplPlanTypeParam_Override` |  |  |  |
| 30 | `CAPL.PTP.RECORD.STATUS` | `CaplPlanTypeParam_RecordStatus` | String |  |  |
| 31 | `CAPL.PTP.CURR.NO` | `CaplPlanTypeParam_CurrNo` | String |  |  |
| 32 | `CAPL.PTP.INPUTTER` | `CaplPlanTypeParam_Inputter` |  |  |  |
| 33 | `CAPL.PTP.DATE.TIME` | `CaplPlanTypeParam_DateTime` |  |  |  |
| 34 | `CAPL.PTP.AUTHORISER` | `CaplPlanTypeParam_Authoriser` | String |  |  |
| 35 | `CAPL.PTP.CO.CODE` | `CaplPlanTypeParam_CoCode` | String |  |  |
| 36 | `CAPL.PTP.DEPT.CODE` | `CaplPlanTypeParam_DeptCode` | String |  |  |
| 37 | `CAPL.PTP.AUDITOR.CODE` | `CaplPlanTypeParam_AuditorCode` | String |  |  |
| 38 | `CAPL.PTP.AUDIT.DATE.TIME` | `CaplPlanTypeParam_AuditDateTime` | String |  |  |
