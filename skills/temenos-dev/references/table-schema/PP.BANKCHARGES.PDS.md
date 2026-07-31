# PP.BANKCHARGES.PDS — Table Schema

> Source: `INSERTS/I_F.PP.BANKCHARGES.PDS` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.BCH.CompanyID` | `PpBankchargesPds_Companyid` |  |  |  |
| 2 | `PP.BCH.SendingOrReceivingBankCharge` | `PpBankchargesPds_Sendingorreceivingbankcharge` |  |  |  |
| 3 | `PP.BCH.CorrespondentBIC` | `PpBankchargesPds_Correspondentbic` |  |  |  |
| 4 | `PP.BCH.CTRBTRIndicator` | `PpBankchargesPds_Ctrbtrindicator` |  |  |  |
| 5 | `PP.BCH.SLACode` | `PpBankchargesPds_Slacode` |  |  |  |
| 6 | `PP.BCH.CurrencyCode` | `PpBankchargesPds_Currencycode` |  |  |  |
| 7 | `PP.BCH.CountryCodeDestination` | `PpBankchargesPds_Countrycodedestination` |  |  |  |
| 8 | `PP.BCH.StartDate` | `PpBankchargesPds_Startdate` |  |  |  |
| 9 | `PP.BCH.Include71GIndicator` | `PpBankchargesPds_Include71gindicator` |  |  |  |
| 10 | `PP.BCH.CommonCurrency` | `PpBankchargesPds_Commoncurrency` |  |  |  |
| 11 | `PP.BCH.EndDate` | `PpBankchargesPds_Enddate` |  |  |  |
| 12 | `PP.BCH.FeeType` | `PpBankchargesPds_Feetype` |  |  |  |
| 13 | `PP.BCH.Ranking` | `PpBankchargesPds_Ranking` |  |  |  |
| 14 | `PP.BCH.AlwaysApplyFlag` | `PpBankchargesPds_Alwaysapplyflag` |  |  |  |
| 15 | `PP.BCH.ApplyMeOnlyFlag` | `PpBankchargesPds_Applymeonlyflag` |  |  |  |
| 16 | `PP.BCH.PercentageVATOnCharge` | `PpBankchargesPds_Percentagevatoncharge` |  |  |  |
| 17 | `PP.BCH.FeeTierRangeLowerLimit` | `PpBankchargesPds_Feetierrangelowerlimit` |  |  |  |
| 18 | `PP.BCH.FixedChargeAmount` | `PpBankchargesPds_Fixedchargeamount` |  |  |  |
| 19 | `PP.BCH.PercentageVariableFee` | `PpBankchargesPds_Percentagevariablefee` |  |  |  |
| 20 | `PP.BCH.BaseChargeAmount` | `PpBankchargesPds_Basechargeamount` |  |  |  |
| 21 | `PP.BCH.ChargeDiscountAmount` | `PpBankchargesPds_Chargediscountamount` |  |  |  |
| 22 | `PP.BCH.ChargeRiseAmount` | `PpBankchargesPds_Chargeriseamount` |  |  |  |
| 23 | `PP.BCH.MinimumChargeAmount` | `PpBankchargesPds_Minimumchargeamount` |  |  |  |
| 24 | `PP.BCH.MaximumChargeAmount` | `PpBankchargesPds_Maximumchargeamount` |  |  |  |
| 25 | `PP.BCH.AuthoriserDateTime` | `PpBankchargesPds_Authoriserdatetime` |  |  |  |
| 26 | `PP.BCH.RESERVED.5` | `PpBankchargesPds_Reserved5` |  |  |  |
| 27 | `PP.BCH.RESERVED.4` | `PpBankchargesPds_Reserved4` |  |  |  |
| 28 | `PP.BCH.RESERVED.3` | `PpBankchargesPds_Reserved3` |  |  |  |
| 29 | `PP.BCH.RESERVED.2` | `PpBankchargesPds_Reserved2` |  |  |  |
| 30 | `PP.BCH.RESERVED.1` | `PpBankchargesPds_Reserved1` |  |  |  |
| 31 | `PP.BCH.LOCAL.REF` | `PpBankchargesPds_LocalRef` |  |  |  |
| 32 | `PP.BCH.LinkID` | `PpBankchargesPds_Linkid` |  |  |  |
| 33 | `PP.BCH.OVERRIDE` | `PpBankchargesPds_Override` |  |  |  |
| 34 | `PP.BCH.RECORD.STATUS` | `PpBankchargesPds_RecordStatus` |  |  |  |
| 35 | `PP.BCH.CURR.NO` | `PpBankchargesPds_CurrNo` |  |  |  |
| 36 | `PP.BCH.INPUTTER` | `PpBankchargesPds_Inputter` |  |  |  |
| 37 | `PP.BCH.DATE.TIME` | `PpBankchargesPds_DateTime` |  |  |  |
| 38 | `PP.BCH.AUTHORISER` | `PpBankchargesPds_Authoriser` |  |  |  |
| 39 | `PP.BCH.CO.CODE` | `PpBankchargesPds_CoCode` |  |  |  |
| 40 | `PP.BCH.DEPT.CODE` | `PpBankchargesPds_DeptCode` |  |  |  |
| 41 | `PP.BCH.AUDITOR.CODE` | `PpBankchargesPds_AuditorCode` |  |  |  |
| 42 | `PP.BCH.AUDIT.DATE.TIME` | `PpBankchargesPds_AuditDateTime` |  |  |  |
