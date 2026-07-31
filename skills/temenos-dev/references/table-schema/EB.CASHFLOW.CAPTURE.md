# EB.CASHFLOW.CAPTURE — Table Schema

> Source: `INSERTS/I_F.EB.CASHFLOW.CAPTURE` in `CW_CashFlow.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IA.CCAP.CURRENCY` | `EbCashflowCapture_Currency` | TField |  | This field denotes the contract currency. Validation Rules: : No input field. A valid currency record of length 3. Will be updated by system only if the field POPULATE.CASHFLOW is set as "YES" |
| 2 | `IA.CCAP.INTEREST.BASIS` | `EbCashflowCapture_InterestBasis` | TField |  | This field denotes the INTEREST.BASIS of the underlying contract. Validation Rules: : No input field. Denotes a valid record in INTEREST.BASIS table. Alphanumeric up to length 3. Will be updated by system only if the field POPULATE.CASHFLOW is set as "YES" |
| 3 | `IA.CCAP.IAS.CLASSIFICATION` | `EbCashflowCapture_IasClassification` | TField | Yes | IFRS9 regulations requires a strict classification of financial assets and liabilities according to their purpose. IAS.CLASSIFICATION table holds various IFRS reporting classifications - AMC,FVOCI etc. This field denotes a valid IAS.CLASSIFICATION. Validation Rules: : Alphanumeric up to length 35. Mandatory field. |
| 4 | `IA.CCAP.IAS.SUB.TYPE` | `EbCashflowCapture_IasSubType` | TField | Yes | A valid IFRS.SUB.TYPE, under which the contract will be taken over into IFRS9. Validation Rules: : Mandatory field. Alphanumeric of length up to 35. |
| 5 | `IA.CCAP.EVENT.DATE` | `EbCashflowCapture_EventDate` |  |  |  |
| 6 | `IA.CCAP.EVENT.AMT` | `EbCashflowCapture_EventAmt` |  |  |  |
| 7 | `IA.CCAP.EXC.FROM.EIR` | `EbCashflowCapture_ExcFromEir` |  |  |  |
| 8 | `IA.CCAP.ACC.HEAD` | `EbCashflowCapture_AccHead` |  |  |  |
| 9 | `IA.CCAP.CONTRACT.RATE` | `EbCashflowCapture_ContractRate` | TField |  | This field denotes the Rate of the underlying contract. Validation Rules: : No input field. Standard T24 numeric field of length up to 35. Will be updated by system only if the field POPULATE.CASHFLOW is set as "YES" |
| 10 | `IA.CCAP.MARKET.KEY` | `EbCashflowCapture_MarketKey` | TField |  | This field denotes the market rate for the contract. This can either be a ID in PERIODIC.INTEREST table or the actual rate itself. Validation Rules: : Basic detail to build EB.CASHFLOW record. Field value will be updated in the respective application. Numeric of length up to 35. |
| 11 | `IA.CCAP.MARKET.MARGIN` | `EbCashflowCapture_MarketMargin` | TField | No | Flexibility is given to the user through the field MARKET.MARGIN to include margin as a percentage of the market rate in to the calculation of the fair value. Both positive and negative margin percentage can be inputted. For example if the market rate is 10%. With the positive margin of +0.50%, the net rate for the calculation will be 10.50% and with a negative margin of -0.50%, the net rate for the calculation will be 9.50%. Validation Rules: Optional input Field value will be updated in the respective application record. Numeric of length up to 35. |
| 12 | `IA.CCAP.MARGIN.OPERAND` | `EbCashflowCapture_MarginOperand` | TField | No | Indicates the operand to be used for arriving at the market rate using MARKET.MARGIN. Example: +/- Validation Rules: Optional input + if add operand is specified, then market.key will be added with market.margin to arrive at the final rate - if sub operand is specified, then market.key is subtracted from market.margin to arrive at the final rate |
| 13 | `IA.CCAP.EIR` | `EbCashflowCapture_Eir` | TField |  | This field will store the effective rate of interest of the contract. If EIR is input, the system populates the cash flow information and start the IFRS processing with the EIR input Validation Rules: : Either AMC or EIR must be inputted but not both. Basic detail to build EB.CASHFLOW record. Standard rate type field of length 16. |
| 14 | `IA.CCAP.AMC` | `EbCashflowCapture_Amc` | TField |  | This field denotes the Amortised cost amount used for the calculation of EIR. If AMC Balance is inputted then with that and all the future cash flows for the contract, the system will calculate the EIR. Validation Rules: : Either AMC or EIR must be inputted but not both. Basic detail to build EB.CASHFLOW record. Valid amount field of length up to 35. Negative amounts also allowed. |
| 15 | `IA.CCAP.RATE.FIX.DATE` | `EbCashflowCapture_RateFixDate` | TField |  | This field denotes the date from which the new rate, in case of a rate fixing contract, will be applicable. Validation Rules: System updated, no input field Standard T24 date of length 11 characters. |
| 16 | `IA.CCAP.OUTSTANDING.AMT` | `EbCashflowCapture_OutstandingAmt` | TField |  | This field denotes the outstanding amount to the bank as on the rate fix date. This field is mainly used for repricing, updated when IFRS.SUB.TYPE TERM is SHORT. When TERM is set as 'SHORT', the system will calculate the EIR only up to the next rate fixing date and income will be amortised over this period. Validation Rules: : No input field. System updated from the respective application. Numeric field of length up to 35. |
| 17 | `IA.CCAP.POPULATE.CASHFLOW` | `EbCashflowCapture_PopulateCashflow` | TField | Yes | If this field POPULATE.CASHFLOW is set as 'YES', system will get the static, rate and cash flow information and will populate it to EB.CASHFLOW.CAPTURE. If this field POPULATE.CASHFLOW is set as 'N', system expects the user to provide the cash flow information as well as the rate and static information. Validation Rules: : Mandatory input Yes or no field |
| 18 | `IA.CCAP.UPD.STATUS` | `EbCashflowCapture_UpdStatus` |  |  |  |
| 19 | `IA.CCAP.ACCRUAL.METHOD` | `EbCashflowCapture_AccrualMethod` | TField |  | Field denoting the accrual method followed by the underlying contract. This field will provide the link to the table EB.ACCRUAL.PARAM which determines how accruals are performed by the core accrual processing. Validation Rules: No input, system updated from corresponding application record. Alphanumeric of length up to 35. |
| 20 | `IA.CCAP.EXPECTED.END.DATE` | `EbCashflowCapture_ExpectedEndDate` | TField |  | When the field TERM is set as EXPECTED it means this is applicable for contracts with an expected term. Cashflow engine will consolidate the contractual cashflows to fit into the expected term for a set of cashflows required for the EIR calculation. All contractual cashflows beyond the expected life end (based on the Expected term and the Start date) will be consolidated under the expected life end. The system will calculate the EIR up to the expected life end date, and the Amortised cost will be calculated as the NPV of the cashflows till the Expected life end. Validation Rules: Valid T24 date of length 11 System updated, no input field |
| 21 | `IA.CCAP.CATEGORY` | `EbCashflowCapture_Category` | TField |  | This contains the CATEGORY of the Contract. Validation Rules: This is a NOINPUT field, system updated from respective application record Valid CATEGORY, numeric of length up to 5 characters. |
| 22 | `IA.CCAP.CONTRACT.TYPE` | `EbCashflowCapture_ContractType` | TField |  | To pass commitment flag for AA contracts. Specific to AA contracts,since AA contracts will be taken over via takeover activity, this field is no longer used. |
| 23 | `IA.CCAP.LOCAL.REF` | `EbCashflowCapture_LocalRef` |  |  |  |
| 24 | `IA.CCAP.OVERRIDE` | `EbCashflowCapture_Override` |  |  |  |
| 25 | `IA.CCAP.RECORD.STATUS` | `EbCashflowCapture_RecordStatus` | String |  |  |
| 26 | `IA.CCAP.CURR.NO` | `EbCashflowCapture_CurrNo` | String |  |  |
| 27 | `IA.CCAP.INPUTTER` | `EbCashflowCapture_Inputter` |  |  |  |
| 28 | `IA.CCAP.DATE.TIME` | `EbCashflowCapture_DateTime` |  |  |  |
| 29 | `IA.CCAP.AUTHORISER` | `EbCashflowCapture_Authoriser` | String |  |  |
| 30 | `IA.CCAP.CO.CODE` | `EbCashflowCapture_CoCode` | String |  |  |
| 31 | `IA.CCAP.DEPT.CODE` | `EbCashflowCapture_DeptCode` | String |  |  |
| 32 | `IA.CCAP.AUDITOR.CODE` | `EbCashflowCapture_AuditorCode` | String |  |  |
| 33 | `IA.CCAP.AUDIT.DATE.TIME` | `EbCashflowCapture_AuditDateTime` | String |  |  |
| 34 | `IA.CCAP.CALC.TYPE` | `EbCashflowCapture_CalcType` |  |  |  |
| 35 | `IA.CCAP.CALC.RATE` | `EbCashflowCapture_CalcRate` |  |  |  |
| 36 | `IA.CCAP.CALC.AMC` | `EbCashflowCapture_CalcAmc` |  |  |  |
