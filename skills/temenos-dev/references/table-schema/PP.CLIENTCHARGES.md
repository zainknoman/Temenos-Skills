# PP.CLIENTCHARGES — Table Schema

> Source: `INSERTS/I_F.PP.CLIENTCHARGES` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CC.CompanyID` | `PpClientcharges_Companyid` | TField |  | This is a No-Input field which gets Auto-Populated on Clicking Validate button Example : BNK,GB1 |
| 2 | `PP.CC.FeeProduct` | `PpClientcharges_Feeproduct` | TField |  | Holds a valid FeePoduct. Fee product would be an output when a payment product is successfully determined. Can be wildcarded. |
| 3 | `PP.CC.SourceProduct` | `PpClientcharges_Sourceproduct` | TField |  | Bank may receive payments from variety of sources, it could be from Internet banking channel or Trade platform or the payment could have been initiated by the Cash pool engine. We may not want to take charges for payments originating from certain sources or apply preferential charges. E.g. A bank has introduced a new channel for the client initiated payment and want to move the clients from old channel to new channel; based on the source we can increase the Fee for payments initiated through the old channel; which will mean that client would not want to pay more charges to use the old channel and rather would try to move to new channel at the earliest This field specifies the source group from where payment has been originated. Soucre group is a group of payment sources Can be wildcarded Should be a valid value in PP.SourceProductGroup table |
| 4 | `PP.CC.BusinessLine` | `PpClientcharges_Businessline` | TField |  | This is the business line or the customer group to which the customer belongs. Each business line or customer group can have specific objectives from the perspective of fees being collected. Accordingly, a bank might want to price charges differently across different business lines or customer groups. When EnableCustGrouping in PP.COMPANY.PROPERTIES is set as "Yes", this holds the Customer Group ID from PP.GEN.CONDITION. When PP.COMPANY.PROPERTIES is blank, this field holds the Customer Target Validation Rules: 1. This field can be wildcarded (*). |
| 5 | `PP.CC.ClientID` | `PpClientcharges_Clientid` | TField |  | Customer ID as in the DDA Can be wildcarded as well. Wildcard denotes that this definition is not client specific but a common one |
| 6 | `PP.CC.CustomerAccountNumberCompID` | `PpClientcharges_Customeraccountnumbercompid` | TField |  | This is the owning company of the account specified in field Customer Account Number. Can be wild carded |
| 7 | `PP.CC.CustomerAccountNumber` | `PpClientcharges_Customeraccountnumber` | TField |  | Indicates the account number of the account which is either the credit or the debit account in the payment If specific charges need to be applied based on the account used in the payment, this field can be used Should be a valid account in the DDA system or can be wild carded |
| 8 | `PP.CC.CustomerAccountCurrency` | `PpClientcharges_Customeraccountcurrency` | TField |  | Indicates 3 character ISO currency code of the account which is either the credit or the debit account currency in the payment If specific charges need to be applied based on the account's currency, this field can be used Should be a valid value in PP_CURRENCY or can be wild carded |
| 9 | `PP.CC.ResidencyStatus` | `PpClientcharges_Residencystatus` | TField |  | In most of the countries there is a Value Added Tax (VAT) imposed by government which is levied on the payment or on the charges which are taken by the Bank. This tax amount goes to the government and all Banks within that country need to follow those regulations. It need not be applied on all the cases and one of the factor which influences whether we take the VAT or not depends if ordering party or beneficiary customer is a resident of that country or not. Possible Values: RR, RN, NR or NN First character denotes the residency status of the ordering party (OrderingPartyResidencyFlag) and second character denotes the residency status of beneficiary party (BeneficiaryPartyResidencyFlag) Can be wildcarded |
| 10 | `PP.CC.StartDate` | `PpClientcharges_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Autopopulated from the ID upon clicking Validate Button |
| 11 | `PP.CC.CommonCurrency` | `PpClientcharges_Commoncurrency` | TField |  | Multiple fee can be defined for a single correspondent bank. This fields holds the currency in which the fee will be charged. Should be a valid value in PP.CURRENCY |
| 12 | `PP.CC.EndDate` | `PpClientcharges_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 13 | `PP.CC.FeeType` | `PpClientcharges_Feetype` |  |  |  |
| 14 | `PP.CC.Ranking` | `PpClientcharges_Ranking` |  |  |  |
| 15 | `PP.CC.AlwaysApplyFlag` | `PpClientcharges_Alwaysapplyflag` |  |  |  |
| 16 | `PP.CC.ApplyMeOnlyFlag` | `PpClientcharges_Applymeonlyflag` |  |  |  |
| 17 | `PP.CC.PercentageVATOnCharge` | `PpClientcharges_Percentagevatoncharge` |  |  |  |
| 18 | `PP.CC.FeeTierRangeLowerLimit` | `PpClientcharges_Feetierrangelowerlimit` |  |  |  |
| 19 | `PP.CC.FixedChargeAmount` | `PpClientcharges_Fixedchargeamount` |  |  |  |
| 20 | `PP.CC.PercentageVariableFee` | `PpClientcharges_Percentagevariablefee` |  |  |  |
| 21 | `PP.CC.BaseChargeAmount` | `PpClientcharges_Basechargeamount` |  |  |  |
| 22 | `PP.CC.ChargeDiscountAmount` | `PpClientcharges_Chargediscountamount` |  |  |  |
| 23 | `PP.CC.ChargeRiseAmount` | `PpClientcharges_Chargeriseamount` |  |  |  |
| 24 | `PP.CC.MinimumChargeAmount` | `PpClientcharges_Minimumchargeamount` |  |  |  |
| 25 | `PP.CC.MaximumChargeAmount` | `PpClientcharges_Maximumchargeamount` |  |  |  |
| 26 | `PP.CC.FixedChargeAmountFX` | `PpClientcharges_Fixedchargeamountfx` |  |  |  |
| 27 | `PP.CC.PercentageVariableFeeFX` | `PpClientcharges_Percentagevariablefeefx` |  |  |  |
| 28 | `PP.CC.BaseChargeAmountFX` | `PpClientcharges_Basechargeamountfx` |  |  |  |
| 29 | `PP.CC.ChargeDiscountAmountFX` | `PpClientcharges_Chargediscountamountfx` |  |  |  |
| 30 | `PP.CC.ChargeRiseAmountFX` | `PpClientcharges_Chargeriseamountfx` |  |  |  |
| 31 | `PP.CC.AuthoriserDateTime` | `PpClientcharges_Authoriserdatetime` | TField |  |  |
| 32 | `PP.CC.RESERVED.10` | `PpClientcharges_Reserved10` | TField |  |  |
| 33 | `PP.CC.RESERVED.9` | `PpClientcharges_Reserved9` | TField |  |  |
| 34 | `PP.CC.RESERVED.8` | `PpClientcharges_Reserved8` | TField |  |  |
| 35 | `PP.CC.RESERVED.7` | `PpClientcharges_Reserved7` | TField |  |  |
| 36 | `PP.CC.RESERVED.6` | `PpClientcharges_Reserved6` | TField |  |  |
| 37 | `PP.CC.RESERVED.5` | `PpClientcharges_Reserved5` | TField |  | Standard T24 field. Reserved for future use |
| 38 | `PP.CC.RESERVED.4` | `PpClientcharges_Reserved4` | TField |  | Standard T24 field. Reserved for future use |
| 39 | `PP.CC.RESERVED.3` | `PpClientcharges_Reserved3` | TField |  | Standard T24 field. Reserved for future use |
| 40 | `PP.CC.RESERVED.2` | `PpClientcharges_Reserved2` | TField |  | Standard T24 field. Reserved for future use |
| 41 | `PP.CC.RESERVED.1` | `PpClientcharges_Reserved1` | TField |  | Standard T24 field. Reserved for future use |
| 42 | `PP.CC.LOCAL.REF` | `PpClientcharges_LocalRef` |  |  |  |
| 43 | `PP.CC.LinkID` | `PpClientcharges_Linkid` | TField |  | Its a No-Input field Value is populated by concatenating all the Primary Keys |
| 44 | `PP.CC.OVERRIDE` | `PpClientcharges_Override` |  |  |  |
| 45 | `PP.CC.RECORD.STATUS` | `PpClientcharges_RecordStatus` | String |  |  |
| 46 | `PP.CC.CURR.NO` | `PpClientcharges_CurrNo` | String |  |  |
| 47 | `PP.CC.INPUTTER` | `PpClientcharges_Inputter` |  |  |  |
| 48 | `PP.CC.DATE.TIME` | `PpClientcharges_DateTime` |  |  |  |
| 49 | `PP.CC.AUTHORISER` | `PpClientcharges_Authoriser` | String |  |  |
| 50 | `PP.CC.CO.CODE` | `PpClientcharges_CoCode` | String |  |  |
| 51 | `PP.CC.DEPT.CODE` | `PpClientcharges_DeptCode` | String |  |  |
| 52 | `PP.CC.AUDITOR.CODE` | `PpClientcharges_AuditorCode` | String |  |  |
| 53 | `PP.CC.AUDIT.DATE.TIME` | `PpClientcharges_AuditDateTime` | String |  |  |
