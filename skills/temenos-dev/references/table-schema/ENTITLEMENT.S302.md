# ENTITLEMENT.S302 — Table Schema

> Source: `INSERTS/I_F.ENTITLEMENT.S302` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ES.OPTION.B` | `EntitlementS302_OptionB` | TField |  | This field indicates that the customer has no holdings of acquirer stock after the merger event, ie., thecustomer has surrendered target stock, for cash consideration. User input field Allowed Values: Yes, Blank |
| 2 | `SC.ES.ACQ.STOCK.RECEIVED` | `EntitlementS302_AcqStockReceived` | TField |  | This field holds the quantity of acquirer shares received through merger Defaults from entitlement, can be amended by user |
| 3 | `SC.ES.ACQ.STOCK.BEFORE` | `EntitlementS302_AcqStockBefore` | TField |  | This field holds the quantity of Acquirer stock held before the merger User input field |
| 4 | `SC.ES.ACQ.STOCK.TOTAL` | `EntitlementS302_AcqStockTotal` | TField |  | This field holds the total share i.e., sum of ACQ.STOCK.RECEIVED and ACQ.STOCK.BEFORE No input field |
| 5 | `SC.ES.ACT.INTEREST` | `EntitlementS302_ActInterest` | TField |  | This field holds the actual interest Formula : 100*ACQ.STOCK.TOTAL/302W , where 302W is available in SC.EVENT.ADJUST |
| 6 | `SC.ES.TARGET.SEC.BEFORE` | `EntitlementS302_TargetSecBefore` | TField |  | This field holds the number of shares of event(target) security Defaults from entitlement, can be amended by user |
| 7 | `SC.ES.HYP.ACQ.SHARES` | `EntitlementS302_HypAcqShares` | TField |  | This field holds the hypothetical shares acquired after applying the ratio (HYP.CONV.OLD.RATIO andHYP.CONV.NEW.RATIO) specified in SC.EVENT.ADJUST No input field |
| 8 | `SC.ES.POT.INTEREST` | `EntitlementS302_PotInterest` | TField |  | This field holds the potential interest Formula : 100*HYP.ACQ.SHARES/302X , where 302X is available in SC.EVENT.ADJUST |
| 9 | `SC.ES.OPTION.A` | `EntitlementS302_OptionA` | TField |  | This field defaults to 'Yes', when potential interest is greater than actual interest Can be amended by the user Allowed values : Yes, Blank |
| 10 | `SC.ES.OPTION.C` | `EntitlementS302_OptionC` | TField |  | This field defaults to 'Yes', when actual interest is greater than or equal to potential interest Can be amended by the user Allowed values : Yes, Blank |
| 11 | `SC.ES.BASE.AMOUNT` | `EntitlementS302_BaseAmount` | TField |  | This field holds the amount on which tax is to be applied Defaults from INCOME.AMOUNT field of entitlement |
| 12 | `SC.ES.SOURCE.TAX.PERC` | `EntitlementS302_SourceTaxPerc` | TField |  | This field holds the source tax percentage Defaults from entitlement |
| 13 | `SC.ES.SOURCE.TAX.AMOUNT` | `EntitlementS302_SourceTaxAmount` | TField |  | This field holds the source tax amount calculated based on source tax percentage Defaults from entitlement |
| 14 | `SC.ES.NEW.TAX.RATE` | `EntitlementS302_NewTaxRate` | TField |  | This field defaults to 0, when option A or B is set to 'Yes'. Else the local tax rate computed based on QI taxsetup willget defaulted No input field |
| 15 | `SC.ES.NEW.TAX.AMOUNT` | `EntitlementS302_NewTaxAmount` | TField |  | This field holds the tax amount computed based on the new tax rate No input field |
| 16 | `SC.ES.ADJ.AMOUNT` | `EntitlementS302_AdjAmount` | TField |  | This field holds the difference between old and new tax amount No input field |
| 17 | `SC.ES.DOCUMENT.STATUS` | `EntitlementS302_DocumentStatus` | TField |  | This fields holds various statuses of the Document flow. The S302 form is received from the custodian and passed on to the customer. The customer has to provide hisresponses by FORM.SUBMIT.DATE specified in SC.EVENT.ADJUST. These responses are then submitted to the custodian andfinally the custodian acknowledges the submission of the form. This is an EB.LOOKUP field , various statuses of thedocument flow can be defined as required. User input field |
| 18 | `SC.ES.POST.STATUS` | `EntitlementS302_PostStatus` | TField |  | This field when set to 'Yes' indicates that , input processing is complete and the system can proceed withposting of the adjustment amounts User input field Allowed Values : Yes, Blank |
| 19 | `SC.ES.VALUE.DATE` | `EntitlementS302_ValueDate` | TField |  | This field holds the value date required for the Adjustment entry. User input field |
| 20 | `SC.ES.SYS.ELECTED.OPTION` | `EntitlementS302_SysElectedOption` | TField |  | This field holds the option elected based on the system calculation No input field |
| 21 | `SC.ES.SC.ADJ.TXN.UPDATE.ID` | `EntitlementS302_ScAdjTxnUpdateId` | TField |  | This field holds the id of SC.ADJ.TXN.UPDATE record created for this transaction |
| 22 | `SC.ES.FUNDS.TRANSFER.ID` | `EntitlementS302_FundsTransferId` | TField |  | This field holds the id of FUNDS.TRANSFER record created for this transaction |
| 23 | `SC.ES.TAX.EFF.DATE` | `EntitlementS302_TaxEffDate` | TField |  | This is input field If not manually given, tax effective date will be defaulted based on TXN.TAX.CODE parameterization Ex date, pay date or value date will be defaulted Validation Rules: Date can not be greater than today |
| 24 | `SC.ES.RESERVED.05` | `EntitlementS302_Reserved05` | TField |  |  |
| 25 | `SC.ES.RESERVED.04` | `EntitlementS302_Reserved04` | TField |  |  |
| 26 | `SC.ES.RESERVED.03` | `EntitlementS302_Reserved03` | TField |  |  |
| 27 | `SC.ES.RESERVED.02` | `EntitlementS302_Reserved02` | TField |  |  |
| 28 | `SC.ES.RESERVED.01` | `EntitlementS302_Reserved01` | TField |  |  |
| 29 | `SC.ES.LOCAL.REF` | `EntitlementS302_LocalRef` |  |  |  |
| 30 | `SC.ES.OVERRIDE` | `EntitlementS302_Override` |  |  |  |
| 31 | `SC.ES.RECORD.STATUS` | `EntitlementS302_RecordStatus` | String |  |  |
| 32 | `SC.ES.CURR.NO` | `EntitlementS302_CurrNo` | String |  |  |
| 33 | `SC.ES.INPUTTER` | `EntitlementS302_Inputter` |  |  |  |
| 34 | `SC.ES.DATE.TIME` | `EntitlementS302_DateTime` |  |  |  |
| 35 | `SC.ES.AUTHORISER` | `EntitlementS302_Authoriser` | String |  |  |
| 36 | `SC.ES.CO.CODE` | `EntitlementS302_CoCode` | String |  |  |
| 37 | `SC.ES.DEPT.CODE` | `EntitlementS302_DeptCode` | String |  |  |
| 38 | `SC.ES.AUDITOR.CODE` | `EntitlementS302_AuditorCode` | String |  |  |
| 39 | `SC.ES.AUDIT.DATE.TIME` | `EntitlementS302_AuditDateTime` | String |  |  |
| 40 | `SC.ES.NEW.MAN.TAX.AMOUNT` | `EntitlementS302_NewManTaxAmount` | TField |  | This field holds the tax amount amended by the user User input field |
