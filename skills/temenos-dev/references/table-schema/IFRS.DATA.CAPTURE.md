# IFRS.DATA.CAPTURE — Table Schema

> Source: `INSERTS/I_F.IFRS.DATA.CAPTURE` in `IA_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IFDC.APPLICATION` | `IfrsDataCapture_Application` | TField | Yes | Application related to the contract Applications supported - AA.ARRANGEMENT,AZ.ACCOUNT,LD.LOANS.AND.DEPOSITS,ACCOUNT,BL.REGISTER,SL.LOANS,SC.TRADING.POSITION,MM.MONEY.MARKET,MG.MORTAGE. Validation Rules: Valid T24 Application Input is mandatory Applications - BL.REGISTER,ACCOUNT,MG.MORTGAGE are allowed only when I9 product is installed and IFRS.PARAMETER is configured in the company |
| 2 | `IFDC.CONTRACT.NUMBER` | `IfrsDataCapture_ContractNumber` | TField |  | The Contract Id for which there is a data capture. Validation Rules: Should be a valid Id for that application. |
| 3 | `IFDC.CURRENCY` | `IfrsDataCapture_Currency` | TField |  | A valid record from CURRENCY table of length 3. This field is populated from EB.CASHFLOW if record (for the contract) exists otherwise from EB.CONTRACT.BALANCES Validation Rules: No-Input Field |
| 4 | `IFDC.GROUP.ID` | `IfrsDataCapture_GroupId` | TField |  | Reserved for future use |
| 5 | `IFDC.OPERATION` | `IfrsDataCapture_Operation` | TField | Yes | This field provides the following options, IMPAIR, UNIMPAIR, IMPAIR.AMENDMENT, CLASSIFY, RECLASSIFY, TAKEOVER, CORRECTION, CHARGE-OFF and RESTORE. For IFRS 9 Compliance, the Operation STAGE.CHANGE will be there instead of IMPAIR and UNIMPAIR. STAGE.CHANGE: By using the STAGE.CHANGE operation by giving the stages in the field STAGE, can either impair or unimpair the Contract. If the stage is 3(Impair) IMPAIR: This operation is used to impair a contract. IMPAIR.AMENDMENT: This operation is used to amend an already impaired contract or a contract which has impair evidence. UNIMPAIR: This operation is used to reverse the impairment done on a contract. RECLASSIFY: This operation is used to re-classify the contract. New IAS.CLASSIFICATION and new IFRS.SUB.TYPE can be given. CORRECTION: This operation is used when a contract is wrongly classified and when a user want to reverse the previous classification. CHARGE-OFF: If RN not installed, This operation is used to reverse the already posted ifrs accounting and stop further ifrs accounting. RESTORE: This is allowed only when RN not installed. Upon doing this operation, the contract will no longer be considered as charged off and ifrs accounting will be continued. Below options are not currently enabled and reserved for future use. CLASSIFY: TAKEOVER: Validation Rules: : Input is Mandatory No Change Field |
| 6 | `IFDC.EFFECTIVE.DATE` | `IfrsDataCapture_EffectiveDate` | TField |  | This Field cannot be backdated or future dated. Only value allowed is TODAY Validation Rules: Today is not defaulted, if it is not inputted Input allowed only if the Operation is IMPAIR/RECLASSIFY Also this date should not be less than Contract's Value date |
| 7 | `IFDC.IMPAIRMENT.CODE` | `IfrsDataCapture_ImpairmentCode` |  |  |  |
| 8 | `IFDC.ACTION.NOTES` | `IfrsDataCapture_ActionNotes` |  |  |  |
| 9 | `IFDC.DEF.CASH.FLOW.METH` | `IfrsDataCapture_DefCashFlowMeth` | TField |  | Mode of input for cash flow, �MANUAL� : For manual input �CONTRACTUAL�: To load Contractual cash flow �EXPECTED�: To load the expected cashflow from EB.CASHFLOW record. Valid input only for Operations IMPAIR / STAGE.CHANGE to 3 and IMPAIR.AMENDMENT Validation Rules: Input allowed for Operation IMPAIR,IMPAIR.AMENDMENT only When DefCashflowMeth is chosen as Expected, and no cashflows / collateral details fetched from EB.CASHFLOW, then error is raised. When DefCashflowMeth is chosen as Manual, and no cashflows / collateral details given in IFDC, then error is raised. Contractual cashflow option is invalid for overdraft accounts(which does not have steady cashflows). Defaulted as MANUAL,if expected cashflow fields are input. |
| 10 | `IFDC.DEF.CFLOW.TYPE` | `IfrsDataCapture_DefCflowType` |  |  |  |
| 11 | `IFDC.DEF.CFLOW.PERC` | `IfrsDataCapture_DefCflowPerc` |  |  |  |
| 12 | `IFDC.EXP.CFLOW.DATE` | `IfrsDataCapture_ExpCflowDate` |  |  |  |
| 13 | `IFDC.EXP.CFLOW.TYPE` | `IfrsDataCapture_ExpCflowType` |  |  |  |
| 14 | `IFDC.EXP.CFLOW.AMT` | `IfrsDataCapture_ExpCflowAmt` |  |  |  |
| 15 | `IFDC.EXP.CFLOW.CCY` | `IfrsDataCapture_ExpCflowCcy` |  |  |  |
| 16 | `IFDC.EXP.AMOUNT` | `IfrsDataCapture_ExpAmount` |  |  |  |
| 17 | `IFDC.EXLD.FROM.EIR` | `IfrsDataCapture_ExldFromEir` |  |  |  |
| 18 | `IFDC.RESERVED.5` | `IfrsDataCapture_Reserved5` |  |  |  |
| 19 | `IFDC.RESERVED.4` | `IfrsDataCapture_Reserved4` |  |  |  |
| 20 | `IFDC.RESERVED.3` | `IfrsDataCapture_Reserved3` |  |  |  |
| 21 | `IFDC.RESERVED.2` | `IfrsDataCapture_Reserved2` |  |  |  |
| 22 | `IFDC.RESERVED.1` | `IfrsDataCapture_Reserved1` |  |  |  |
| 23 | `IFDC.COLLATERAL.ID` | `IfrsDataCapture_CollateralId` |  |  |  |
| 24 | `IFDC.COLLAT.PERCENT` | `IfrsDataCapture_CollatPercent` |  |  |  |
| 25 | `IFDC.COLL.EXPIRY.DAT` | `IfrsDataCapture_CollExpiryDat` |  |  |  |
| 26 | `IFDC.EXP.COLL.DATE` | `IfrsDataCapture_ExpCollDate` |  |  |  |
| 27 | `IFDC.EXP.COLL.AMT` | `IfrsDataCapture_ExpCollAmt` |  |  |  |
| 28 | `IFDC.FEED.OPTION` | `IfrsDataCapture_FeedOption` |  |  |  |
| 29 | `IFDC.RECOVERABLE.AMT` | `IfrsDataCapture_RecoverableAmt` |  |  |  |
| 30 | `IFDC.COLL.RATE.AMORT` | `IfrsDataCapture_CollRateAmort` |  |  |  |
| 31 | `IFDC.COLL.RATE.FV` | `IfrsDataCapture_CollRateFv` |  |  |  |
| 32 | `IFDC.IMP.LOSS.AMORT` | `IfrsDataCapture_ImpLossAmort` | TField |  | Field to denote the impairment loss, for contracts with steady cashflow - loss is calculated under AMORTISED COST method For overdraft accounts,loss will be calculated as the difference between contract balance and recoverable value. Contract balance is T24 book balance Recoverable value will be total of all the cash flows that the entity expects to receive, discounted at the EIR or discount rate and collateral value if available. Collateral can be discounted at EIR or Market rate based on setup in COLL.RATE.AMORT field. If recoverable value becomes greater than the book balance, since there is no loss in that case impairment processing will not be carried out and contract with marked as IMPAIR.EVIDENCE. Validation Rules: Standard amount field. No input field, system updated based on expected cashflows and collateral values specified. |
| 33 | `IFDC.IMP.LOSS.FV` | `IfrsDataCapture_ImpLossFv` | TField |  | Field to denote the impairment loss under the FAIRVALUE method. If collateral is specified, based on field COLL.RATE.FV collateral value will be considered for loss calculation. Standard amount field. No input field, system updated. |
| 34 | `IFDC.IMPAIR.ACCOUNTING` | `IfrsDataCapture_ImpairAccounting` | TField |  | Option field indicating, Y � indicates whether accounting entries are raised N � indicates whether accounting entries are not raised Validation Rules: No input Field |
| 35 | `IFDC.ACCT.RUN.OPTION` | `IfrsDataCapture_AcctRunOption` | TField | Yes | Options available are, ONLINE: Accounting raised online COB: Accounting raised during the next COB SCHEDULE: As per provisioning frequency Default value is ONLINE. Mandatory input |
| 36 | `IFDC.CURR.IAS.CLASS` | `IfrsDataCapture_CurrIasClass` | TField |  | System defaulted field when OPERATION is �RECLASSIFY/CORRECTION" No input field. Represents current IAS.CLASSIFICATION of the contract. |
| 37 | `IFDC.CURR.IAS.SUBTYPE` | `IfrsDataCapture_CurrIasSubtype` | TField |  | System defaulted field when OPERATION is �RECLASSIFY/CORRECTION" No input field. Represents the current IFRS.SUB.TYPE of the contract. |
| 38 | `IFDC.NEW.IAS.CLASS` | `IfrsDataCapture_NewIasClass` | TField | Yes | New IAS classification to which the contract will be reclassified. Validation Rules: A Valid key to IAS.CLASSIFICATION Input mandatory for OPERATION � �RECLASSIFY" and "CORRECTION", otherwise NOINPUT field |
| 39 | `IFDC.NEW.IAS.SUBTYPE` | `IfrsDataCapture_NewIasSubtype` | TField | Yes | New IAS subtype to which the contract will be reclassified. Validation Rules: A Valid key to IFRS.SUB.TYPE Input mandatory for OPERATION � �RECLASSIFY" and "CORRECTION", otherwise NOINPUT field |
| 40 | `IFDC.EIR` | `IfrsDataCapture_Eir` | TField |  | Reserved for future use. |
| 41 | `IFDC.CARRYING.AMOUNT` | `IfrsDataCapture_CarryingAmount` | TField |  | Reserved for future use. |
| 42 | `IFDC.MARKET.KEY` | `IfrsDataCapture_MarketKey` | TField | Yes | The new market rate or key to PERIODIC.INTEREST table. Validation Rules: Input allowed only when OPERATION is "RECLASSIFY","CORRECTION" and overdraft accounts For overdraft accounts, if rate is chosen as MARKET, then this field is mandatory. Valid input only for IMPAIR and IMPAIR.AMENDMENT operations. |
| 43 | `IFDC.MARKET.MARGIN` | `IfrsDataCapture_MarketMargin` | TField |  | Flexibility is given to the user through the field MARKET.MARGIN to include margin as a percentage of the market rate in to the calculation of the fair value. Both positive and negative margin percentage can be inputted. For example if the market rate is 10%. With the positive margin of +0.50%, the net rate for the calculation will be 10.50% and with a negative margin of -0.50%, the net rate for the calculation will be 9.50%. Validation Rules: The Margin to the Market rate, only allowed if MARKET.KEY is input |
| 44 | `IFDC.STATUS` | `IfrsDataCapture_Status` | TField |  | Reserved for future use |
| 45 | `IFDC.STAGE` | `IfrsDataCapture_Stage` | TField | Yes | The STAGE of the contract. For STAGE.CHANGE operation input in this field is mandatory. If the contact is already in STAGE 3 and if the STAGE is given as 1 or 2 then it is UNIMPAIR operation. If the contact is already in STAGE 1 or 2 and if the STAGE is given as 3 then it is IMPAIR operation. STAGE 1 to 2, 2 to 1 , 3 to 1, 3 to 2, 1 to 3, 2 to 3 all combinations possible Validation Rules: Input is mandatory if the OPERATION is STAGE.CHANGE Input not required if OPERATION is other than STAGE.CHANGE |
| 46 | `IFDC.LOAN.CLASSIFICATION` | `IfrsDataCapture_LoanClassification` | TField |  | Reserved for future use. |
| 47 | `IFDC.DISCOUNT.RATE` | `IfrsDataCapture_DiscountRate` | TField | Yes | This field is input for Stage Change(to impair an OD Account and Operating leases) and Impair Amendment Operation This field is used to capture the discount rate or default the applicable interest rate of an account / lease. This field is used for the purpose of discounting the future cashflows. Validation Rules: Mandatory Input for AA OverDraft Accounts if contract rate is not available. The value given in this field will take precendence over contract rate, for NPV Calculation of Expected Cashflows and Collateral if any given. Invalid Input for Contracts other than Overdraft AC, AA Accounts and Operating lease. |
| 48 | `IFDC.RESERVED.12` | `IfrsDataCapture_Reserved12` |  |  |  |
| 49 | `IFDC.RESERVED.11` | `IfrsDataCapture_Reserved11` | TField |  |  |
| 50 | `IFDC.RESERVED.10` | `IfrsDataCapture_Reserved10` | TField |  |  |
| 51 | `IFDC.RESERVED.9` | `IfrsDataCapture_Reserved9` | TField |  |  |
| 52 | `IFDC.RESERVED.8` | `IfrsDataCapture_Reserved8` | TField |  |  |
| 53 | `IFDC.RESERVED.7` | `IfrsDataCapture_Reserved7` | TField |  |  |
| 54 | `IFDC.LOCAL.REF` | `IfrsDataCapture_LocalRef` |  |  |  |
| 55 | `IFDC.STMT.NOS` | `IfrsDataCapture_StmtNos` |  |  |  |
| 56 | `IFDC.OVERRIDE` | `IfrsDataCapture_Override` |  |  |  |
| 57 | `IFDC.RECORD.STATUS` | `IfrsDataCapture_RecordStatus` | String |  |  |
| 58 | `IFDC.CURR.NO` | `IfrsDataCapture_CurrNo` | String |  |  |
| 59 | `IFDC.INPUTTER` | `IfrsDataCapture_Inputter` |  |  |  |
| 60 | `IFDC.DATE.TIME` | `IfrsDataCapture_DateTime` |  |  |  |
| 61 | `IFDC.AUTHORISER` | `IfrsDataCapture_Authoriser` | String |  |  |
| 62 | `IFDC.CO.CODE` | `IfrsDataCapture_CoCode` | String |  |  |
| 63 | `IFDC.DEPT.CODE` | `IfrsDataCapture_DeptCode` | String |  |  |
| 64 | `IFDC.AUDITOR.CODE` | `IfrsDataCapture_AuditorCode` | String |  |  |
| 65 | `IFDC.AUDIT.DATE.TIME` | `IfrsDataCapture_AuditDateTime` | String |  |  |
