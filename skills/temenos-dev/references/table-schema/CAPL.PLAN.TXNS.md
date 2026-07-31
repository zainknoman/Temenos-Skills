# CAPL.PLAN.TXNS — Table Schema

> Source: `INSERTS/I_F.CAPL.PLAN.TXNS` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.PTXN.DESCRIPTION` | `CaplPlanTxns_Description` |  |  |  |
| 2 | `CAPL.PTXN.SHORT.DESCR` | `CaplPlanTxns_ShortDescr` |  |  |  |
| 3 | `CAPL.PTXN.CAPL.TXN.CODE` | `CaplPlanTxns_CaplTxnCode` | TField |  | Field is used to store the CRA or legacy system transaction codes. Those codes can be used for mapping a transaction when raising entries for TAX purposes. Points to table CAPL.PLAN.TXN.TYPE |
| 4 | `CAPL.PTXN.DR.CR` | `CaplPlanTxns_DrCr` | TField |  | Field is used to indicate the debit / credit marker for the plan transactions.Allowed inputs : DR/CRDr - indicate as Debit transactionCr - indicate as Credit transaction |
| 5 | `CAPL.PTXN.PLAN.LOCKED` | `CaplPlanTxns_PlanLocked` | TField |  | Field is used to define whether this transaction is applicable to locked plans. In case that the PLAN.TYPE is multivalue and more than one plan is specified, this should be configured to specify if this transaction is applicable to Locked Plans.allowed inputs : YES / NO.Validation -If "Y" there should not be any plan non locked in field PLAN.TYPE. If "N" there should not be any locked in plans in the PLAN.TYPE. If "" any plan type can be entered in PLAN.TYPE |
| 6 | `CAPL.PTXN.PLAN.TYPE` | `CaplPlanTxns_PlanType` |  |  |  |
| 7 | `CAPL.PTXN.VALID.STAGE` | `CaplPlanTxns_ValidStage` | TField | Yes | This flag determines the stage (LIVE, WITHIN, AFTER) this transaction is applicable. It should be mandatory field.Allowed inputs: Value should be "ALIVE/WITHIN/AFTER"Validation -If "ALIVE" is specified. This transaction is allowed only when death date field in the CIF of the annuitant is empty. If "WITHIN" then this transaction is allowed only if the annuitant is deceased and the transaction is executed within the allowed period. The system would calculate the value of the plan as of DOD as well as at the settlement date. If "AFTER" the transaction is applicable only if the payout is done once the customer is deceased and after the allowed period. The system should calculate the value of the plan as of DOD, WITHIN, and at the time of settlement. |
| 8 | `CAPL.PTXN.TXN.CONTRIBUTION` | `CaplPlanTxns_TxnContribution` | TField |  | Determines if a transaction is a contribution.Value should be "YES/NO".Applicable - Allowed only if DR.CR field is "CR".Validation -If plan type is Locked i.e. PLAN.LOCKED is "YES" then input should not be allowed |
| 9 | `CAPL.PTXN.MINIMUM.IND` | `CaplPlanTxns_MinimumInd` | TField |  | Defines whether this transaction is used to pay minimum payments online. Applicable to RRIF plan groups only (not allowed if any of the plan.types in PLAN.TYPE is of group different from RRIF.Inputs : Value should be "YES/NO". Allowed only for RRIF plan groups |
| 10 | `CAPL.PTXN.PAYOUT.IND` | `CaplPlanTxns_PayoutInd` | TField |  | Defines if the transaction is used for plan payout. Using this transaction the system will have to recalculate the value of the plan including the interest. If there is a date of death in the annuitant the system should calculate the value of the portfolio as of date of death, within allowed period, after the allowed period.If there is no date of death in the annuitant CIF the system should calculate the value of portfolio as of settlement date. If this transaction is being used the system should ensure that no open other accounts/terms exist for this portfolio and all balances are transferred into the account that is being debited (settlement account is single settlement method is being used). Once this transaction is authorized the SAM field "PAYOUT.INDICATOR" should be set to "Y"allowed inputs : Value should be "YES/NO" |
| 11 | `CAPL.PTXN.RESERVED.21` | `CaplPlanTxns_Reserved21` | TField |  |  |
| 12 | `CAPL.PTXN.RESERVED.20` | `CaplPlanTxns_Reserved20` | TField |  |  |
| 13 | `CAPL.PTXN.YEARLY.MAX.AMT` | `CaplPlanTxns_YearlyMaxAmt` | TField |  | Defines the yearly max amount for this transaction type. It starts from January 1st of the current year. An override message will be raised if this amount is exceeded. |
| 14 | `CAPL.PTXN.LIFE.MAX.AMT` | `CaplPlanTxns_LifeMaxAmt` | TField |  | Defines the lifetime max amount for this transaction type. An override message will be raised if this amount is exceeded. No functionality is linked to this field right now. |
| 15 | `CAPL.PTXN.RESERVED.19` | `CaplPlanTxns_Reserved19` | TField |  |  |
| 16 | `CAPL.PTXN.RESERVED.18` | `CaplPlanTxns_Reserved18` | TField |  |  |
| 17 | `CAPL.PTXN.PROV.TAX.ALIVE` | `CaplPlanTxns_ProvTaxAlive` | TField | Yes | Define whether this transaction is taxable Y/N. Mandatory at the time of withdrawal done when annuitant is alive. It cannot be "Y" if the DR/CR is "CR"Value should be "YES/NO"Validaiton - IF DR.CR is CR then YES should not be allowed. |
| 18 | `CAPL.PTXN.PROV.TAX.DEATH` | `CaplPlanTxns_ProvTaxDeath` | TField |  | Defines if this transaction is taxable when the annuitant is deceased. Currently there are no taxes taken and it should be "N". The user specifies the taxes at the screen if customer chooses to have taxes. It can be "Y" only when the DR/CR is DR and PAYOUT.INDICATOR is "Y". For deceased annuitants T24 should look at the residency of the beneficiary(ies) to determine the tax rate.Value should be "YES/NO"Applicable - IF DR.CR is CR then YES should not be allowed. |
| 19 | `CAPL.PTXN.PROV.TAX.KEY` | `CaplPlanTxns_ProvTaxKey` | TField |  | Enter here the TAX.TYPE that applies for provincial Taxes. As per the configuration of the taxes in the section above T24 will return a rate for QC residents and zero for the rest of the provinces. See the configuration section for the taxes.Link to TAX.TYPE for provincial tax. |
| 20 | `CAPL.PTXN.PROV.FT.TXN.CODE` | `CaplPlanTxns_ProvFtTxnCode` | TField |  | T24 will post the provincial taxes as a separate FT transaction debiting the customer's account and crediting the tax account so it needs an FT.TXNS.TYPE.CONDITION.Link to FT.TXN.TYPE.CONDITION |
| 21 | `CAPL.PTXN.FED.TAX.ALIVE` | `CaplPlanTxns_FedTaxAlive` | TField | Yes | Define whether this transaction is federally taxable Y/N. Mandatory at the time of withdrawal done when annuitant is alive. The configuration of taxes allows returning a different rate based on the customer province. So for QC residents T24 would return a federal rate different from the other provinces. See the tax configuration section above.It cannot be "Y" if the DR/CR is "CR".inputs - Value should be "YES/NO".validation - IF DR.CR is CR then YES should not be allowed. |
| 22 | `CAPL.PTXN.FED.TAX.DEATH` | `CaplPlanTxns_FedTaxDeath` | TField |  | Defines if this transaction is taxable when the annuitant is deceased. Currently there are no taxes taken and it should be "N". The user specifies the taxes at the screen if customer chooses to have taxes. It can be "Y" only when the DR/CR is DR. For deceased annuitants T24 should look at the residency of the beneficiary (ies) to determine the tax rate. |
| 23 | `CAPL.PTXN.FED.TAX.KEY` | `CaplPlanTxns_FedTaxKey` | TField |  | Link to TAX.TYPE table for federal Tax. |
| 24 | `CAPL.PTXN.FED.FT.TXN.CODE` | `CaplPlanTxns_FedFtTxnCode` | TField |  |  |
| 25 | `CAPL.PTXN.NR.TAX.ALIVE` | `CaplPlanTxns_NrTaxAlive` | TField |  | Define whether NR taxes apply to this transaction for nonresidents.Value should be "YES/NO"IF DR.CR is CR then YES should not be allowed. |
| 26 | `CAPL.PTXN.NR.TAX.DEATH` | `CaplPlanTxns_NrTaxDeath` | TField |  | Defines if this transaction is taxable when the annuitant is deceased. Currently there are taxes taken and it should be "Y". The user can override the taxes at the screen if customer chooses to have different taxes. It can be "Y" only when the DR/CR is DR. For the value of plan until the DOD the residence of the annuitant is looked to define the residency. If the withdrawal is done after the DOD then the residence of the beneficiary should be looked to define the residency.Value should be "YES/NO"IF DR.CR is CR then YES should not be allowed. |
| 27 | `CAPL.PTXN.NR.TAX.KEY` | `CaplPlanTxns_NrTaxKey` | TField |  | Link to TAX.TYPE. Input allowed only the previous field(NR.TAX.DEATH) is "YES" |
| 28 | `CAPL.PTXN.NR.FT.TXN.CODE` | `CaplPlanTxns_NrFtTxnCode` | TField |  | Link to FT.TXN.TYPE.CONDITION |
| 29 | `CAPL.PTXN.RESERVED.17` | `CaplPlanTxns_Reserved17` | TField |  |  |
| 30 | `CAPL.PTXN.RESERVED.16` | `CaplPlanTxns_Reserved16` | TField |  |  |
| 31 | `CAPL.PTXN.RESERVED.15` | `CaplPlanTxns_Reserved15` | TField |  |  |
| 32 | `CAPL.PTXN.RESERVED.14` | `CaplPlanTxns_Reserved14` | TField |  |  |
| 33 | `CAPL.PTXN.TXN.RESIDENT.ANNUITANT` | `CaplPlanTxns_TxnResidentAnnuitant` | TField |  | If "Y" the transaction is allowed to annuitant CA residents only, If "N" the transaction is allowed to non-residents only, If " " it is allowed to both residents and nonresidents.Value should be "YES/NO/''" |
| 34 | `CAPL.PTXN.NR.CODE.ALIVE` | `CaplPlanTxns_NrCodeAlive` | TField |  | Defines the code for NR taxation slips based on the annuitants transactions up to the date of death. It looks at the residence status of the annuitant.NR code for alive annuitants |
| 35 | `CAPL.PTXN.NR.CODE.WITHIN` | `CaplPlanTxns_NrCodeWithin` | TField |  | Keeps the NR codes that should be printed on the NR slips if the payout is within the allowed period. It reflects the residence status of the beneficiaries and not the annuitant. |
| 36 | `CAPL.PTXN.NR.CODE.AFTER` | `CaplPlanTxns_NrCodeAfter` | TField |  | Keeps the NR codes that should be printed on the NR slips if the payout is done after the allowed period. It reflects the residence status of the beneficiaries and not the annuitant. |
| 37 | `CAPL.PTXN.NR.CODE.MIN` | `CaplPlanTxns_NrCodeMin` | TField |  | Keeps the NR codes that should be printed on the slips for NR slips. It reflects the residence status of the annuitant at the time of transaction. It should be input if the plan type belongs to plan group RRIF. |
| 38 | `CAPL.PTXN.NR.CODE.EXCESS` | `CaplPlanTxns_NrCodeExcess` | TField |  | Keeps the NR codes that should be printed on the slips for NR slips. It reflects the residence status of the annuitant at the time of transaction. It should be input if the plan type belongs to plan group RRIF. |
| 39 | `CAPL.PTXN.NR.EXEMPTION.CODE` | `CaplPlanTxns_NrExemptionCode` | TField |  | Keeps an exemption code in case the user has exempted the NR taxes. It is used to all withdrawal transactions to NR clients or in case of death payout to NR beneficiaries. |
| 40 | `CAPL.PTXN.RESERVED.13` | `CaplPlanTxns_Reserved13` | TField |  |  |
| 41 | `CAPL.PTXN.RESERVED.12` | `CaplPlanTxns_Reserved12` | TField |  |  |
| 42 | `CAPL.PTXN.TXN.CHARGE.TYPE` | `CaplPlanTxns_TxnChargeType` | TField |  | Links to FT.COMMISSION.TYPE and serve to configure any charges. Those charges are booked separately into the liquidation account |
| 43 | `CAPL.PTXN.CHARGE.FT.TXN.CODE` | `CaplPlanTxns_ChargeFtTxnCode` | TField | Yes | For registered plans T24 post charges as a separate FT transaction so it needs an FT.TXN.TYPE.CONDITION for this purpose.if TXN.CHARGE.TYPE is not null then this field should be Mandatory Link to FT.TXN.TYPE.CONDITION |
| 44 | `CAPL.PTXN.RESERVED.11` | `CaplPlanTxns_Reserved11` | TField |  |  |
| 45 | `CAPL.PTXN.RESERVED.10` | `CaplPlanTxns_Reserved10` | TField |  |  |
| 46 | `CAPL.PTXN.RESERVED.9` | `CaplPlanTxns_Reserved9` | TField |  |  |
| 47 | `CAPL.PTXN.CONTRA.RECIEPT.MSG` | `CaplPlanTxns_ContraRecieptMsg` | TField |  |  |
| 48 | `CAPL.PTXN.R2.PROVENANCE` | `CaplPlanTxns_R2Provenance` | TField |  | Keeps the message to be printed on relive 2 for this transaction. |
| 49 | `CAPL.PTXN.R2.MESSAGE` | `CaplPlanTxns_R2Message` | TField |  | Keeps the message to be printed on R2 for this type of transaction |
| 50 | `CAPL.PTXN.T4.MESSAGE` | `CaplPlanTxns_T4Message` | TField |  | Keeps the message to be printed |
| 51 | `CAPL.PTXN.CALC.DOD.VALUE` | `CaplPlanTxns_CalcDodValue` | TField |  | If the value as of DOD is to be computed then this flag should be "Y". For "ROP" txn this value should be "N" |
| 52 | `CAPL.PTXN.RECIPIENT.SIN.NO` | `CaplPlanTxns_RecipientSinNo` | TField |  | If the SIN number is required to be entered on the screen. It should be "YES" for MBR (Marriage Break Down) transaction code. |
| 53 | `CAPL.PTXN.TXN.VERSION` | `CaplPlanTxns_TxnVersion` |  |  |  |
| 54 | `CAPL.PTXN.TXN.MESSAGE` | `CaplPlanTxns_TxnMessage` |  |  |  |
| 55 | `CAPL.PTXN.ABS.SCHED.RATES` | `CaplPlanTxns_AbsSchedRates` | TField |  | Defines whether the Tax rate needs to be taken from CAPL.PLAN.SCHEDULES or from default TAX table. |
| 56 | `CAPL.PTXN.RESERVED.7` | `CaplPlanTxns_Reserved7` |  |  |  |
| 57 | `CAPL.PTXN.RESERVED.6` | `CaplPlanTxns_Reserved6` | TField |  |  |
| 58 | `CAPL.PTXN.RESERVED.5` | `CaplPlanTxns_Reserved5` | TField |  |  |
| 59 | `CAPL.PTXN.RESERVED.4` | `CaplPlanTxns_Reserved4` | TField |  |  |
| 60 | `CAPL.PTXN.RESERVED.3` | `CaplPlanTxns_Reserved3` | TField |  |  |
| 61 | `CAPL.PTXN.RESERVED.2` | `CaplPlanTxns_Reserved2` | TField |  |  |
| 62 | `CAPL.PTXN.RESERVED.1` | `CaplPlanTxns_Reserved1` | TField |  |  |
| 63 | `CAPL.PTXN.LOCAL.REF` | `CaplPlanTxns_LocalRef` |  |  |  |
| 64 | `CAPL.PTXN.OVERRIDE` | `CaplPlanTxns_Override` |  |  |  |
| 65 | `CAPL.PTXN.RECORD.STATUS` | `CaplPlanTxns_RecordStatus` | String |  |  |
| 66 | `CAPL.PTXN.CURR.NO` | `CaplPlanTxns_CurrNo` | String |  |  |
| 67 | `CAPL.PTXN.INPUTTER` | `CaplPlanTxns_Inputter` |  |  |  |
| 68 | `CAPL.PTXN.DATE.TIME` | `CaplPlanTxns_DateTime` |  |  |  |
| 69 | `CAPL.PTXN.AUTHORISER` | `CaplPlanTxns_Authoriser` | String |  |  |
| 70 | `CAPL.PTXN.CO.CODE` | `CaplPlanTxns_CoCode` | String |  |  |
| 71 | `CAPL.PTXN.DEPT.CODE` | `CaplPlanTxns_DeptCode` | String |  |  |
| 72 | `CAPL.PTXN.AUDITOR.CODE` | `CaplPlanTxns_AuditorCode` | String |  |  |
| 73 | `CAPL.PTXN.AUDIT.DATE.TIME` | `CaplPlanTxns_AuditDateTime` | String |  |  |
