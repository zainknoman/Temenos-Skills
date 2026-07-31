# TCIB.ACCT.DETS — Table Schema

> Source: `INSERTS/I_F.TCIB.ACCT.DETS` in `CATCIB_TCIBOnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TCIB.ACCT.PRODUCT` | `TcibAcctDets_Product` | TField |  | To capture incoming AA product Id for creating the Account. |
| 2 | `TCIB.ACCT.CURRENCY` | `TcibAcctDets_Currency` | TField |  | To Capture incoming Currency Code |
| 3 | `TCIB.ACCT.EFFECTIVE.DATE` | `TcibAcctDets_EffectiveDate` | TField |  | To Capture the Effective Date of the Contract. |
| 4 | `TCIB.ACCT.INTENDED.USE` | `TcibAcctDets_IntendedUse` | TField |  | To Capture the Intended use of the Contract. |
| 5 | `TCIB.ACCT.INTENDED.USE.DESC` | `TcibAcctDets_IntendedUseDesc` | TField |  | To Capture additional Intended use desc if any |
| 6 | `TCIB.ACCT.THIRD.PARTY` | `TcibAcctDets_ThirdParty` | TField |  | Yes or No field to be captured to Indicate whether the created Account can be accessed by third party. |
| 7 | `TCIB.ACCT.PLAN.TYPE` | `TcibAcctDets_PlanType` | TField |  | To Capture the Plan Type for the Incoming Registered Account. |
| 8 | `TCIB.ACCT.ACTION.TYPE` | `TcibAcctDets_ActionType` | TField |  | To Capture the Action Type for the incoming Account. Valid options are NEWPLAN, LINK, CLOSE |
| 9 | `TCIB.ACCT.PORTFOLIO.ID` | `TcibAcctDets_PortfolioId` | TField |  | To capture the Plan Id the Account creation is to link for an existing Account. |
| 10 | `TCIB.ACCT.TERM` | `TcibAcctDets_Term` | TField |  | To capture the Term Details if the incoming Account is for Deposits. |
| 11 | `TCIB.ACCT.CHANGE.PERIOD` | `TcibAcctDets_ChangePeriod` | TField |  | Change Period to be captured if the Term has any change product to be done |
| 12 | `TCIB.ACCT.AMOUNT` | `TcibAcctDets_Amount` | TField |  | To Capture the Term Amount if the incoming Account is for Deposits |
| 13 | `TCIB.ACCT.PYMT.FREQUENCY` | `TcibAcctDets_PymtFrequency` | TField |  | To capture the Payment Frequency for Deposit Accounts |
| 14 | `TCIB.ACCT.MODE` | `TcibAcctDets_Mode` | TField |  | Possible values are SIMULATE or CREATE or EXECUTE |
| 15 | `TCIB.ACCT.SIM.REF` | `TcibAcctDets_SimRef` | TField |  | Simulation Reference to be captured |
| 16 | `TCIB.ACCT.DEP.RENEW` | `TcibAcctDets_DepRenew` | TField |  | Possible values are YES or NO |
| 17 | `TCIB.ACCT.ACCOUNT.ID` | `TcibAcctDets_AccountId` | TField |  | ACCOUNT.ID |
| 18 | `TCIB.ACCT.CUSTOMER.ID` | `TcibAcctDets_CustomerId` | TField |  |  |
| 19 | `TCIB.ACCT.ACCOUNT.NAME` | `TcibAcctDets_AccountName` | TField |  | To update nick name for the account to be created |
| 20 | `TCIB.ACCT.PAY.METHOD` | `TcibAcctDets_PayMethod` | TField |  | The Purpose of the field is to store the Payment Method which is used to create GIC Interest Option to Payment Schedule Property.Value in this field will be mapped to the GIC Payment Schedule for Interest property for field PAYMENT.METHODAllowed Inputs:PayCapitaliseValidations:Vetted to EB.LOOKUP of PAY.METHOD |
| 21 | `TCIB.ACCT.INTEREST.RATE` | `TcibAcctDets_InterestRate` | TField |  | Field to define the Interest rate of the account.Value given will be mapped to the fixed / floating / periodic rate.Allowed up to 2 decimals.Validation:Value given in this field will be compared to the account rate. Any difference will be updated to the margin of the Interest condition. |
| 22 | `TCIB.ACCT.PAYIN.ACCOUNT` | `TcibAcctDets_PayinAccount` | TField |  | Purpose of the field to define the account used for pay-in settlement instructions.Value given will be mapped to the field PAYIN.ACCOUNT in SETTLEMENT property.Valid records of ACCOUNT application. |
| 23 | `TCIB.ACCT.PAYOUT.ACCOUNT` | `TcibAcctDets_PayoutAccount` | TField |  | Purpose of the field to define the account used for pay-out settlement instructions.Value given will be mapped to the field PAYOUT.ACCOUNT in SETTLEMENT property.Valid records of ACCOUNT application |
| 24 | `TCIB.ACCT.PAYIN.BENEFICIARY` | `TcibAcctDets_PayinBeneficiary` | TField |  | Purpose of the field to define the beneficiary details used for pay-in settlement instructions.Value given will be mapped to the field PAYIN.BENEFICIARY in SETTLEMENT property.Validations:Records of BENEFICIARY application.Allowed only if PAYIN.ACCOUNT is blank. |
| 25 | `TCIB.ACCT.PAYOUT.BENEFICIARY` | `TcibAcctDets_PayoutBeneficiary` | TField |  | Purpose of the field to define the beneficiary details used for pay-out settlement instructions.Value given will be mapped to the field PAYOUT.BENEFICIARY in SETTLEMENT property.Validations:Records of BENEFICIARY application.Allowed only if PAYOUT.ACCOUNT is blank. |
| 26 | `TCIB.ACCT.PAYIN.PRODUCT` | `TcibAcctDets_PayinProduct` | TField | Yes | Purpose of the field to define the Payment Order Product details used for pay-in settlement instructions.Value given will be mapped to the field PAYIN.PO.PRODUCT in SETTLEMENT property.Validations:Records of PAYMENT.ORDER.PRODUCT application.Allowed only if PAYIN.ACCOUNT is blank.Mandatory if PAYIN.BENEFICIARY is inputted. |
| 27 | `TCIB.ACCT.PAYOUT.PRODUCT` | `TcibAcctDets_PayoutProduct` | TField | Yes | Purpose of the field to define the Payment Order Product details used for pay-out settlement instructions.Value given will be mapped to the field PAYIN.PO.PRODUCT in SETTLEMENT property.Validations:Records of PAYMENT.ORDER.PRODUCT application.Allowed only if PAYOUT.ACCOUNT is blank.Mandatory if PAYOUT.BENEFICIARY is inputted. |
| 28 | `TCIB.ACCT.PROPERTY` | `TcibAcctDets_Property` |  |  |  |
| 29 | `TCIB.ACCT.FIELD.NAME` | `TcibAcctDets_FieldName` |  |  |  |
| 30 | `TCIB.ACCT.FIELD.VALUE` | `TcibAcctDets_FieldValue` |  |  |  |
| 31 | `TCIB.ACCT.CLOSURE.REASON` | `TcibAcctDets_ClosureReason` | TField |  |  |
| 32 | `TCIB.ACCT.CLOSURE.NOTES` | `TcibAcctDets_ClosureNotes` |  |  |  |
| 33 | `TCIB.ACCT.RESERVED.3` | `TcibAcctDets_Reserved3` | TField |  |  |
| 34 | `TCIB.ACCT.RESERVED.4` | `TcibAcctDets_Reserved4` | TField |  |  |
| 35 | `TCIB.ACCT.RESERVED.5` | `TcibAcctDets_Reserved5` | TField |  |  |
| 36 | `TCIB.ACCT.RESERVED.6` | `TcibAcctDets_Reserved6` | TField |  |  |
| 37 | `TCIB.ACCT.RESERVED.7` | `TcibAcctDets_Reserved7` | TField |  |  |
| 38 | `TCIB.ACCT.RESERVED.8` | `TcibAcctDets_Reserved8` | TField |  |  |
| 39 | `TCIB.ACCT.RESERVED.9` | `TcibAcctDets_Reserved9` | TField |  |  |
| 40 | `TCIB.ACCT.RESERVED.10` | `TcibAcctDets_Reserved10` | TField |  |  |
| 41 | `TCIB.ACCT.OVERRIDE` | `TcibAcctDets_Override` |  |  |  |
| 42 | `TCIB.ACCT.RECORD.STATUS` | `TcibAcctDets_RecordStatus` | String |  |  |
| 43 | `TCIB.ACCT.CURR.NO` | `TcibAcctDets_CurrNo` | String |  |  |
| 44 | `TCIB.ACCT.INPUTTER` | `TcibAcctDets_Inputter` |  |  |  |
| 45 | `TCIB.ACCT.DATE.TIME` | `TcibAcctDets_DateTime` |  |  |  |
| 46 | `TCIB.ACCT.AUTHORISER` | `TcibAcctDets_Authoriser` | String |  |  |
| 47 | `TCIB.ACCT.CO.CODE` | `TcibAcctDets_CoCode` | String |  |  |
| 48 | `TCIB.ACCT.DEPT.CODE` | `TcibAcctDets_DeptCode` | String |  |  |
| 49 | `TCIB.ACCT.AUDITOR.CODE` | `TcibAcctDets_AuditorCode` | String |  |  |
| 50 | `TCIB.ACCT.AUDIT.DATE.TIME` | `TcibAcctDets_AuditDateTime` | String |  |  |
