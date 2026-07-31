# PP.BANKCHARGES — Table Schema

> Source: `INSERTS/I_F.PP.BANKCHARGES` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.BCH.CompanyID` | `PpBankcharges_Companyid` | TField |  | This is a No-Input field which gets Auto-Populated on Clicking Validate button Example : BNK,GB1 |
| 2 | `PP.BCH.SendingOrReceivingBankCharge` | `PpBankcharges_Sendingorreceivingbankcharge` | TField |  | Specifies if the charge defined is to be considered as Sending Bank charge or Receiving bank charge. Possible Values: S - Sending Bank. R - Receiving Bank. |
| 3 | `PP.BCH.CorrespondentBIC` | `PpBankcharges_Correspondentbic` | TField |  | Holds the BIC of the sending bank. Validation Rules: 35 alphanumeric characters. Wildcard value '*' is allowed. |
| 4 | `PP.BCH.CTRBTRIndicator` | `PpBankcharges_Ctrbtrindicator` | TField |  | Specifies the type of transfer for which the charge is defined. Possible Values: C - Customer Transfer B - Bank Transfer |
| 5 | `PP.BCH.SLACode` | `PpBankcharges_Slacode` | TField |  | Indicates the code that relates to service level agreement with other banks. Validation Rules: Value links to field, 'SLAID' in PP.SLA.PER.CODEWORD table. |
| 6 | `PP.BCH.CurrencyCode` | `PpBankcharges_Currencycode` | TField |  | Indicates the code of the currency for which the charge is defined. Possible Values : Value links to field, 'CurrencyCode' in PP.CURRENCY. Wildcard value '*' is allowed. |
| 7 | `PP.BCH.CountryCodeDestination` | `PpBankcharges_Countrycodedestination` | TField |  | Holds the country code of the destination. Validation Rules: 2 alphanumeric characters. Value links to field, 'COUNTRY.CODE' in COUNTRY |
| 8 | `PP.BCH.StartDate` | `PpBankcharges_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Autopopulated from the ID upon clicking Validate Button |
| 9 | `PP.BCH.Include71GIndicator` | `PpBankcharges_Include71gindicator` | TField | Yes | Indicates if the payments hub needs to send 71G charges to the receiving bank or not. Possible values: Y - Yes.Charges are included in 71G tag N - No.Charges are not included in 71G tag. Vaidation Rules: Value to this field is mandatory if field, 'SendingOrReceivingBankCharge'is set as R. |
| 10 | `PP.BCH.CommonCurrency` | `PpBankcharges_Commoncurrency` | TField | Yes | Holds the Common Currency for all the fee types within a bank charge. Validation Rules: Mandatory field. 3 alphanumeric characters. Value links to field, 'CurrencyCode' in PP.CURRENCY |
| 11 | `PP.BCH.EndDate` | `PpBankcharges_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 12 | `PP.BCH.FeeType` | `PpBankcharges_Feetype` |  |  |  |
| 13 | `PP.BCH.Ranking` | `PpBankcharges_Ranking` |  |  |  |
| 14 | `PP.BCH.AlwaysApplyFlag` | `PpBankcharges_Alwaysapplyflag` |  |  |  |
| 15 | `PP.BCH.ApplyMeOnlyFlag` | `PpBankcharges_Applymeonlyflag` |  |  |  |
| 16 | `PP.BCH.PercentageVATOnCharge` | `PpBankcharges_Percentagevatoncharge` |  |  |  |
| 17 | `PP.BCH.FeeTierRangeLowerLimit` | `PpBankcharges_Feetierrangelowerlimit` |  |  |  |
| 18 | `PP.BCH.FixedChargeAmount` | `PpBankcharges_Fixedchargeamount` |  |  |  |
| 19 | `PP.BCH.PercentageVariableFee` | `PpBankcharges_Percentagevariablefee` |  |  |  |
| 20 | `PP.BCH.BaseChargeAmount` | `PpBankcharges_Basechargeamount` |  |  |  |
| 21 | `PP.BCH.ChargeDiscountAmount` | `PpBankcharges_Chargediscountamount` |  |  |  |
| 22 | `PP.BCH.ChargeRiseAmount` | `PpBankcharges_Chargeriseamount` |  |  |  |
| 23 | `PP.BCH.MinimumChargeAmount` | `PpBankcharges_Minimumchargeamount` |  |  |  |
| 24 | `PP.BCH.MaximumChargeAmount` | `PpBankcharges_Maximumchargeamount` |  |  |  |
| 25 | `PP.BCH.AuthoriserDateTime` | `PpBankcharges_Authoriserdatetime` | TField |  |  |
| 26 | `PP.BCH.RESERVED.5` | `PpBankcharges_Reserved5` | TField |  | Standard T24 field. Reserved for future use |
| 27 | `PP.BCH.RESERVED.4` | `PpBankcharges_Reserved4` | TField |  | Standard T24 field. Reserved for future use |
| 28 | `PP.BCH.RESERVED.3` | `PpBankcharges_Reserved3` | TField |  | Standard T24 field. Reserved for future use |
| 29 | `PP.BCH.RESERVED.2` | `PpBankcharges_Reserved2` | TField |  | Standard T24 field. Reserved for future use |
| 30 | `PP.BCH.RESERVED.1` | `PpBankcharges_Reserved1` | TField |  | Standard T24 field. Reserved for future use |
| 31 | `PP.BCH.LOCAL.REF` | `PpBankcharges_LocalRef` |  |  |  |
| 32 | `PP.BCH.LinkID` | `PpBankcharges_Linkid` | TField |  | Its a No-Input field Value is populated by concatenating all the Primary Keys |
| 33 | `PP.BCH.OVERRIDE` | `PpBankcharges_Override` |  |  |  |
| 34 | `PP.BCH.RECORD.STATUS` | `PpBankcharges_RecordStatus` | String |  |  |
| 35 | `PP.BCH.CURR.NO` | `PpBankcharges_CurrNo` | String |  |  |
| 36 | `PP.BCH.INPUTTER` | `PpBankcharges_Inputter` |  |  |  |
| 37 | `PP.BCH.DATE.TIME` | `PpBankcharges_DateTime` |  |  |  |
| 38 | `PP.BCH.AUTHORISER` | `PpBankcharges_Authoriser` | String |  |  |
| 39 | `PP.BCH.CO.CODE` | `PpBankcharges_CoCode` | String |  |  |
| 40 | `PP.BCH.DEPT.CODE` | `PpBankcharges_DeptCode` | String |  |  |
| 41 | `PP.BCH.AUDITOR.CODE` | `PpBankcharges_AuditorCode` | String |  |  |
| 42 | `PP.BCH.AUDIT.DATE.TIME` | `PpBankcharges_AuditDateTime` | String |  |  |
