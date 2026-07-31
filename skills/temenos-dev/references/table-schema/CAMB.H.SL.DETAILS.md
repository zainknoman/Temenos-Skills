# CAMB.H.SL.DETAILS — Table Schema

> Source: `INSERTS/I_F.CAMB.H.SL.DETAILS` in `CASYLN_SyndicatedLending.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.H.SL.DETAILS.LOAN.ARR.ID` | `CambHSlDetails_LoanArrId` | TField |  | Field is used to identify the linkage between SL agreement and SL loan.Stores the SL loan arrangement ID.Validation - System update field, which is auto-populated when the Arrangement is created and linked to the Syndication ID.Valid id of AA.ARRANGEMENT table. |
| 2 | `CAMB.H.SL.DETAILS.LOAN.CCY` | `CambHSlDetails_LoanCcy` | TField |  | Field is used to define the Currency of the SL Loan.Must be a valid currency code in the CURRENCY file in T24.Validation - When a loan is linked to the SL agreement ID, error is thrown to the user if any mismatch in the currency.Eg. CAD |
| 3 | `CAMB.H.SL.DETAILS.CUSTOMER.ID` | `CambHSlDetails_CustomerId` | TField |  | Field is used to store the primary Borrower of the loan.Validation - Must be a valid ID in the CUSTOMER file in T24When a loan is linked to the SL agreement ID, error is thrown to the user if any mismatch in the primary owner. |
| 4 | `CAMB.H.SL.DETAILS.LOAN.AMT` | `CambHSlDetails_LoanAmt` | TField |  | Field is used to define the Loan Amount to be advanced to the Borrower.Validattion - When a loan is linked to the SL agreement ID, error is thrown to the user if any mismatch with loan amount and amount defined in this field. |
| 5 | `CAMB.H.SL.DETAILS.SYN.ST.DATE` | `CambHSlDetails_SynStDate` | TField |  | Field to store the Start Date of the Syndication.Valdiation - Must be the same as AA Loan Start Date at the Arrangement level.Date format field. |
| 6 | `CAMB.H.SL.DETAILS.SYN.MAT.DATE` | `CambHSlDetails_SynMatDate` | TField |  | Purpose of the field to store the Maturity Date of the Syndication.Validation - Must be the same as AA Loan Maturity Date at the Arrangement level.Date format field. |
| 7 | `CAMB.H.SL.DETAILS.OWN.AMT` | `CambHSlDetails_OwnAmt` | TField |  | Field is used to store the Own bank's amount (FI's acting as a lead banker) in the Syndicated loan.Validation - If field is blank, system updates the amount based on the percentage defined in OWN.PERC |
| 8 | `CAMB.H.SL.DETAILS.OWN.PERC` | `CambHSlDetails_OwnPerc` | TField |  | Field is used to store the Own bank's percentage (FI's acting as a lead banker) in the Syndicated loan..Validation - If field is blank, system updates the percentage based on the amount defined in OWN.AMT |
| 9 | `CAMB.H.SL.DETAILS.OWN.PAYOFF.PRTY` | `CambHSlDetails_OwnPayoffPrty` | TField |  |  |
| 10 | `CAMB.H.SL.DETAILS.OWN.PRIN.BAL` | `CambHSlDetails_OwnPrinBal` | TField |  | This field is used to hold the own FI Principal Balance.Based on the repayment towards loan, system updates the field. |
| 11 | `CAMB.H.SL.DETAILS.OWN.OLD.PERC` | `CambHSlDetails_OwnOldPerc` |  |  |  |
| 12 | `CAMB.H.SL.DETAILS.OWN.OLD.PERC.DATE` | `CambHSlDetails_OwnOldPercDate` |  |  |  |
| 13 | `CAMB.H.SL.DETAILS.DIFF.INT.RATE` | `CambHSlDetails_DiffIntRate` | TField | Yes | If set to YES - PART.INT.PERT field is mandatory, if PART.INT.TYPE field is not entered.If set to NO - PART.INT.PERT field should not allowed to define. |
| 14 | `CAMB.H.SL.DETAILS.OWN.INT.PERT` | `CambHSlDetails_OwnIntPert` | TField |  | This field is used to define the Own Bank's Interest percentage.To be defined only if Interest percentage is different for each participants and Lead Bank.Allowed characters 12Max Decimals allowed is 6 If SPF>SYSTEM - EXTENDED.PERC field is set to No andMax Decimals allowed is 9 If SPF>SYSTEM - EXTENDED.PERC field is set to Yes.Max Integers allowed is 8 |
| 15 | `CAMB.H.SL.DETAILS.OWN.INT.TYPE` | `CambHSlDetails_OwnIntType` | TField |  | This field is used to define whether the interest is Periodic or FLoating.Valid record of this field are:Periodic - PERIODIC.INTERESTFloating - BASIC.INTEREST |
| 16 | `CAMB.H.SL.DETAILS.OWN.INT.TYPE.RATE` | `CambHSlDetails_OwnIntTypeRate` | TField |  | This field is used to define the interest key, based on the value defined OWN.INT.TYPE Allowed values 2 numeric character.E.g. 10, 11 |
| 17 | `CAMB.H.SL.DETAILS.OWN.INT.TYPE.MARGIN.OPER` | `CambHSlDetails_OwnIntTypeMarginOper` | TField |  | This field is used to define the operator for the interest rate margin.Eg. ADD, SUB |
| 18 | `CAMB.H.SL.DETAILS.OWN.INT.TYPE.MARGIN` | `CambHSlDetails_OwnIntTypeMargin` | TField |  | This field is used to define the margin interest rate for the OWN.INT.TYPE.RATE field.Based on the value in this field the margin will be added or subtracted as per the operator specified.Allowed value 2 characters |
| 19 | `CAMB.H.SL.DETAILS.PART.ID` | `CambHSlDetails_PartId` |  |  |  |
| 20 | `CAMB.H.SL.DETAILS.PART.AMT` | `CambHSlDetails_PartAmt` |  |  |  |
| 21 | `CAMB.H.SL.DETAILS.DISB.PART.AMT` | `CambHSlDetails_DisbPartAmt` |  |  |  |
| 22 | `CAMB.H.SL.DETAILS.PART.PERC` | `CambHSlDetails_PartPerc` |  |  |  |
| 23 | `CAMB.H.SL.DETAILS.PART.INT.PERT` | `CambHSlDetails_PartIntPert` |  |  |  |
| 24 | `CAMB.H.SL.DETAILS.PART.VOSTRO.AC` | `CambHSlDetails_PartVostroAc` |  |  |  |
| 25 | `CAMB.H.SL.DETAILS.PART.BENE` | `CambHSlDetails_PartBene` |  |  |  |
| 26 | `CAMB.H.SL.DETAILS.PART.PO.PROD` | `CambHSlDetails_PartPoProd` |  |  |  |
| 27 | `CAMB.H.SL.DETAILS.PART.ARR.REF` | `CambHSlDetails_PartArrRef` |  |  |  |
| 28 | `CAMB.H.SL.DETAILS.PART.PRIN.BAL` | `CambHSlDetails_PartPrinBal` |  |  |  |
| 29 | `CAMB.H.SL.DETAILS.PART.INT.ACC.BAL` | `CambHSlDetails_PartIntAccBal` |  |  |  |
| 30 | `CAMB.H.SL.DETAILS.PART.PAYOFF.PRTY` | `CambHSlDetails_PartPayoffPrty` |  |  |  |
| 31 | `CAMB.H.SL.DETAILS.PART.OLD.PERC` | `CambHSlDetails_PartOldPerc` |  |  |  |
| 32 | `CAMB.H.SL.DETAILS.PART.OLD.PERC.DATE` | `CambHSlDetails_PartOldPercDate` |  |  |  |
| 33 | `CAMB.H.SL.DETAILS.PART.INT.TYPE` | `CambHSlDetails_PartIntType` |  |  |  |
| 34 | `CAMB.H.SL.DETAILS.PART.INT.TYPE.RATE` | `CambHSlDetails_PartIntTypeRate` |  |  |  |
| 35 | `CAMB.H.SL.DETAILS.PART.INT.TYPE.MARGIN.OPER` | `CambHSlDetails_PartIntTypeMarginOper` |  |  |  |
| 36 | `CAMB.H.SL.DETAILS.PART.INT.TYPE.MARGIN` | `CambHSlDetails_PartIntTypeMargin` |  |  |  |
| 37 | `CAMB.H.SL.DETAILS.SYN.STATUS` | `CambHSlDetails_SynStatus` | TField |  | Field is used to indicate the status of the Syndication agreement.Allowed inputs are 'ACTIVE', 'REQUEST.CLOSURE', 'CLOSED' &amp; PARTICIPATION.CHANGE.ACTIVE - Syndication agreement and loan is active.REQUEST.CLOSURE - When Syndication loan is in request closure status, this field is updated as 'Request Closure'CLOSED- When Syndication loan is in close status, this field is updated as 'Closed'PARTICIPATION CHANGE - status updated when there is a change in participant.System update field. |
| 38 | `CAMB.H.SL.DETAILS.SYN.STATUS.DATE` | `CambHSlDetails_SynStatusDate` | TField |  | This field is used to indicate the date on which the Syndication status get updated in SYN.STATUS field.System update field, every time there is a change in SYN.STATUS field. |
| 39 | `CAMB.H.SL.DETAILS.SYN.NEW.ID` | `CambHSlDetails_SynNewId` | TField |  | This field used to hold the id of the new syndication arrangement.When existing syndication is dissolved and new syndication arrangement is created, this field will become an inputtable.Validation - Applicable only when the field SYN.STATUS is PARTICIPATION.CHANGE |
| 40 | `CAMB.H.SL.DETAILS.LOCAL.REF` | `CambHSlDetails_LocalRef` |  |  |  |
| 41 | `CAMB.H.SL.DETAILS.OVERRIDE` | `CambHSlDetails_Override` |  |  |  |
| 42 | `CAMB.H.SL.DETAILS.RECORD.STATUS` | `CambHSlDetails_RecordStatus` | String |  |  |
| 43 | `CAMB.H.SL.DETAILS.CURR.NO` | `CambHSlDetails_CurrNo` | String |  |  |
| 44 | `CAMB.H.SL.DETAILS.INPUTTER` | `CambHSlDetails_Inputter` |  |  |  |
| 45 | `CAMB.H.SL.DETAILS.DATE.TIME` | `CambHSlDetails_DateTime` |  |  |  |
| 46 | `CAMB.H.SL.DETAILS.AUTHORISER` | `CambHSlDetails_Authoriser` | String |  |  |
| 47 | `CAMB.H.SL.DETAILS.CO.CODE` | `CambHSlDetails_CoCode` | String |  |  |
| 48 | `CAMB.H.SL.DETAILS.DEPT.CODE` | `CambHSlDetails_DeptCode` | String |  |  |
| 49 | `CAMB.H.SL.DETAILS.AUDITOR.CODE` | `CambHSlDetails_AuditorCode` | String |  |  |
| 50 | `CAMB.H.SL.DETAILS.AUDIT.DATE.TIME` | `CambHSlDetails_AuditDateTime` | String |  |  |
