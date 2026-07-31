# CANNEX.GIC.PRODUCT.PARAM — Table Schema

> Source: `INSERTS/I_F.CANNEX.GIC.PRODUCT.PARAM` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CANNEX.GIC.PROD.DESCRIPTION` | `CannexGicProductParam_Description` | TField |  | Description of the product |
| 2 | `CANNEX.GIC.PROD.REDEEMABLE` | `CannexGicProductParam_Redeemable` | TField |  | This field is used to define the Redeem ability of the product being purchased.Allowed values are:'Y' = Redeemable product.'N' = Non-redeemable product.'C' = Cashable product. |
| 3 | `CANNEX.GIC.PROD.NAME.TYPE` | `CannexGicProductParam_NameType` | TField |  | This Field value indicates what or who is contained in the name fields for the registered owner record.Valid entries are:'F' - Female'M' - Male'I' - Individual if gender unknown'C' - Company |
| 4 | `CANNEX.GIC.PROD.INT.COMPOUND` | `CannexGicProductParam_IntCompound` | TField |  |  |
| 5 | `CANNEX.GIC.PROD.INT.PAYMENT.FQU` | `CannexGicProductParam_IntPaymentFqu` | TField |  |  |
| 6 | `CANNEX.GIC.PROD.MIN.AMOUNT` | `CannexGicProductParam_MinAmount` | TField |  | This field will be used to compare the deposit amount from the incoming file received from Cannex against the product amount (start range).Validation:T24 AMOUNT field |
| 7 | `CANNEX.GIC.PROD.MAX.AMOUNT` | `CannexGicProductParam_MaxAmount` | TField |  | This field will be used to compare the deposit amount from the incoming file received from Cannex against the product amount (end range)Validation:T24 AMOUNT fieldNote: If the amount in the incoming file falls between the start range and end range, then it will satisfy the condition. |
| 8 | `CANNEX.GIC.PROD.INT.RATE.BROKER` | `CannexGicProductParam_IntRateBroker` | TField |  |  |
| 9 | `CANNEX.GIC.PROD.MATURE.INSTR` | `CannexGicProductParam_MatureInstr` | TField |  |  |
| 10 | `CANNEX.GIC.PROD.PAY.DATE.TYPE` | `CannexGicProductParam_PayDateType` | TField |  |  |
| 11 | `CANNEX.GIC.PROD.PAY.METHOD` | `CannexGicProductParam_PayMethod` | TField |  |  |
| 12 | `CANNEX.GIC.PROD.PAY.FREQ` | `CannexGicProductParam_PayFreq` | TField |  |  |
| 13 | `CANNEX.GIC.PROD.PAY.PROPERTY` | `CannexGicProductParam_PayProperty` | TField |  |  |
| 14 | `CANNEX.GIC.PROD.PROD.SEL.RTN` | `CannexGicProductParam_ProdSelRtn` | TField |  |  |
| 15 | `CANNEX.GIC.PROD.AGENT.SEL.RTN` | `CannexGicProductParam_AgentSelRtn` | TField |  |  |
| 16 | `CANNEX.GIC.PROD.AA.PROPERTY` | `CannexGicProductParam_AaProperty` |  |  |  |
| 17 | `CANNEX.GIC.PROD.AA.PROP.FIELD` | `CannexGicProductParam_AaPropField` |  |  |  |
| 18 | `CANNEX.GIC.PROD.MAP.FILE.NAME` | `CannexGicProductParam_MapFileName` |  |  |  |
| 19 | `CANNEX.GIC.PROD.MAP.FIELD.NAME` | `CannexGicProductParam_MapFieldName` |  |  |  |
| 20 | `CANNEX.GIC.PROD.CONCAT.KEY` | `CannexGicProductParam_ConcatKey` |  |  |  |
| 21 | `CANNEX.GIC.PROD.DEFAULT.COMM` | `CannexGicProductParam_DefaultComm` | TField |  | The purpose of this field is used to define, how the commission to be calculation.This field will have 2 optionsNone or File or CalcIf 'File' or 'None' is selected then the commission amount from the incoming file should be defaulted, else the T24 calculated amount using Agent will be defaulted. |
| 22 | `CANNEX.GIC.PROD.TERM.DAYS` | `CannexGicProductParam_TermDays` | TField | No | Field to indicate the number of days to maturity of the product.At least one of TERM-DAYS, TERM-MONTHS or TERM-YEARS must be &gt; 0.Note: This field is an optional field. If this field is define then unique product will be selected. If not then all the products will be selected. |
| 23 | `CANNEX.GIC.PROD.TERM.MONTHS` | `CannexGicProductParam_TermMonths` | TField |  |  |
| 24 | `CANNEX.GIC.PROD.TERM.YEARS` | `CannexGicProductParam_TermYears` | TField | No | Field is to indicate the number of days to maturity of the product.At least one of TERM-DAYS, TERM-MONTHS or TERM-YEARS must be &gt; 0.Note: This field is an optional field. If this field is define then unique product will be selected. If not then all the products will be selected. |
| 25 | `CANNEX.GIC.PROD.COMPANY.CODE` | `CannexGicProductParam_CompanyCode` | TField |  | This field will represent the Cannex company code. T24 company code can be identified by reading the CANNEX.GIC.ORD.PRO.PARAM&gt;ALLOWED.COMP.CODE field and identify the corresponding MNEMONIC.CODE.Validation:Entry must be a valid CANNEX financial institution company code. |
| 26 | `CANNEX.GIC.PROD.COMP.PROD.CODE` | `CannexGicProductParam_CompProdCode` | TField |  | The financial institution's code to further subdivide CANNEX' PRODUCT-CODE field into their own specific products. |
| 27 | `CANNEX.GIC.PROD.CASHABLE.TERM` | `CannexGicProductParam_CashableTerm` | TField |  | If the REDEEMABILITY-FLAG is a Cashable ('C') type then this field must have the number of days that the GIC is cashable in.The standard cashable terms are usually: 30, 60, 90, 120, 180, and 270. |
| 28 | `CANNEX.GIC.PROD.REGISTERED.FLAG` | `CannexGicProductParam_RegisteredFlag` | TField |  | Field is to define the registered flag.Allowed values are:'R' = the product is a registered (RRSP) product.'N' = the product is a non-registeredproduct.'T' = the product is a Tax Free Saving Account (TFSA). |
| 29 | `CANNEX.GIC.PROD.CHG.DEPCOMM.PROP` | `CannexGicProductParam_ChgDepcommProp` | TField |  |  |
| 30 | `CANNEX.GIC.PROD.CHG.UPFRONT.PROP` | `CannexGicProductParam_ChgUpfrontProp` | TField |  |  |
| 31 | `CANNEX.GIC.PROD.ACCR.BALANCE.TYPE` | `CannexGicProductParam_AccrBalanceType` |  |  |  |
| 32 | `CANNEX.GIC.PROD.CUR.BALANCE.TYPE` | `CannexGicProductParam_CurBalanceType` |  |  |  |
| 33 | `CANNEX.GIC.PROD.CURRENCY` | `CannexGicProductParam_Currency` |  |  |  |
| 34 | `CANNEX.GIC.PROD.COMMISSION.PRORATE` | `CannexGicProductParam_CommissionProrate` | TField |  | This will hold the value to identify if the commission rate needs to be calculated on prorate or no.Valid record from EB.LOOUPCNX.COMMISSION.PRORATE*YES |
| 35 | `CANNEX.GIC.PROD.NEG.VARIANCE` | `CannexGicProductParam_Reserved7` |  |  |  |
| 36 | `CANNEX.GIC.PROD.RESERVED.8` | `CannexGicProductParam_Reserved8` | TField |  |  |
| 37 | `CANNEX.GIC.PROD.RESERVED.9` | `CannexGicProductParam_Reserved9` | TField |  |  |
| 38 | `CANNEX.GIC.PROD.RESERVED.10` | `CannexGicProductParam_Reserved10` | TField |  |  |
| 39 | `CANNEX.GIC.PROD.LOCAL.REF` | `CannexGicProductParam_LocalRef` |  |  |  |
| 40 | `CANNEX.GIC.PROD.OVERRIDE` | `CannexGicProductParam_Override` |  |  |  |
| 41 | `CANNEX.GIC.PROD.RECORD.STATUS` | `CannexGicProductParam_RecordStatus` | String |  |  |
| 42 | `CANNEX.GIC.PROD.CURR.NO` | `CannexGicProductParam_CurrNo` | String |  |  |
| 43 | `CANNEX.GIC.PROD.INPUTTER` | `CannexGicProductParam_Inputter` |  |  |  |
| 44 | `CANNEX.GIC.PROD.DATE.TIME` | `CannexGicProductParam_DateTime` |  |  |  |
| 45 | `CANNEX.GIC.PROD.AUTHORISER` | `CannexGicProductParam_Authoriser` | String |  |  |
| 46 | `CANNEX.GIC.PROD.CO.CODE` | `CannexGicProductParam_CoCode` | String |  |  |
| 47 | `CANNEX.GIC.PROD.DEPT.CODE` | `CannexGicProductParam_DeptCode` | String |  |  |
| 48 | `CANNEX.GIC.PROD.AUDITOR.CODE` | `CannexGicProductParam_AuditorCode` | String |  |  |
| 49 | `CANNEX.GIC.PROD.AUDIT.DATE.TIME` | `CannexGicProductParam_AuditDateTime` | String |  |  |
