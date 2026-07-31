# UB.PAYEE.ACCT — Table Schema

> Source: `INSERTS/I_F.UB.PAYEE.ACCT` in `CAEBPS_EbillsInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UB.PA.PAYEE.NAME` | `UbPayeeAcct_PayeeName` |  |  |  |
| 2 | `UB.PA.PAYEE.OLD.NAME` | `UbPayeeAcct_PayeeOldName` |  |  |  |
| 3 | `UB.PA.FROM.DATE` | `UbPayeeAcct_FromDate` |  |  |  |
| 4 | `UB.PA.TO.DATE` | `UbPayeeAcct_ToDate` |  |  |  |
| 5 | `UB.PA.EXTERNAL.ID` | `UbPayeeAcct_ExternalId` |  |  |  |
| 6 | `UB.PA.RESERVED.10` | `UbPayeeAcct_Reserved10` | TField |  |  |
| 7 | `UB.PA.RESERVED.9` | `UbPayeeAcct_Reserved9` | TField |  |  |
| 8 | `UB.PA.RESERVED.8` | `UbPayeeAcct_Reserved8` | TField |  |  |
| 9 | `UB.PA.PAYEE.GROUP` | `UbPayeeAcct_PayeeGroup` | TField |  |  |
| 10 | `UB.PA.ACCT.NO` | `UbPayeeAcct_AcctNo` | TField |  |  |
| 11 | `UB.PA.INT.ACCT.NO` | `UbPayeeAcct_IntAcctNo` | TField |  |  |
| 12 | `UB.PA.ACTIVE` | `UbPayeeAcct_Active` | TField |  | Field is used to indicate whether the vendor is an active vendor or not.Allowed inputs: YES/NOBill payment is considered when this field is set to YES |
| 13 | `UB.PA.CAMB.VND.BUNDLE` | `UbPayeeAcct_CambVndBundle` | TField |  |  |
| 14 | `UB.PA.RESERVED.6` | `UbPayeeAcct_Reserved6` | TField |  |  |
| 15 | `UB.PA.CAMB.VENDOR.FEE` | `UbPayeeAcct_CambVendorFee` | TField |  | Field to indicate whether bill payment to the ID vendor is chargeabe or not.Allowed inputs: YES/NOYES- charges will be takenNo - Charge is not considered. |
| 16 | `UB.PA.CAMB.INT.AC.CAT` | `UbPayeeAcct_CambIntAcCat` | TField |  | Field to store the category to which the chargeS to be posted to.Based on the category defined, GL account will be formed.Applicable - when CAMB.VENDOR.FEE is set to YESValidation - record from CATEGORY table. |
| 17 | `UB.PA.COMM.TYPE` | `UbPayeeAcct_CommType` | TField |  | This field indicates the charge code for the charges to be applied.Validation - record of COMMISSION.TYPE |
| 18 | `UB.PA.OFS.ALLOWED` | `UbPayeeAcct_OfsAllowed` |  |  |  |
| 19 | `UB.PA.LOCAL.REF` | `UbPayeeAcct_LocalRef` |  |  |  |
| 20 | `UB.PA.PAPER.BILL` | `UbPayeeAcct_PaperBill` | TField |  | Field is used to indicate whether the vendor based bill payment is allowed for paper bills functionality.Allowed inputs : YES/NO |
| 21 | `UB.PA.VND.BUNDLE` | `UbPayeeAcct_VndBundle` | TField |  | This field is used to define the vendor details for papers bill functionality to be sent in the request message.Used as part narrative for the statement.Allowed upto 2 char. |
| 22 | `UB.PA.RESERVED.1` | `UbPayeeAcct_Reserved1` | TField |  |  |
| 23 | `UB.PA.OVERRIDE` | `UbPayeeAcct_Override` |  |  |  |
| 24 | `UB.PA.RECORD.STATUS` | `UbPayeeAcct_RecordStatus` | String |  |  |
| 25 | `UB.PA.CURR.NO` | `UbPayeeAcct_CurrNo` | String |  |  |
| 26 | `UB.PA.INPUTTER` | `UbPayeeAcct_Inputter` |  |  |  |
| 27 | `UB.PA.DATE.TIME` | `UbPayeeAcct_DateTime` |  |  |  |
| 28 | `UB.PA.AUTHORISER` | `UbPayeeAcct_Authoriser` | String |  |  |
| 29 | `UB.PA.CO.CODE` | `UbPayeeAcct_CoCode` | String |  |  |
| 30 | `UB.PA.DEPT.CODE` | `UbPayeeAcct_DeptCode` | String |  |  |
| 31 | `UB.PA.AUDITOR.CODE` | `UbPayeeAcct_AuditorCode` | String |  |  |
| 32 | `UB.PA.AUDIT.DATE.TIME` | `UbPayeeAcct_AuditDateTime` | String |  |  |
