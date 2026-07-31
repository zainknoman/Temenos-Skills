# PP.CLIENTCHARGES.PDS — Table Schema

> Source: `INSERTS/I_F.PP.CLIENTCHARGES.PDS` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CC.CompanyID` | `PpClientchargesPds_Companyid` | TField |  |  |
| 2 | `PP.CC.FeeProduct` | `PpClientchargesPds_Feeproduct` | TField |  |  |
| 3 | `PP.CC.SourceProduct` | `PpClientchargesPds_Sourceproduct` | TField |  |  |
| 4 | `PP.CC.BusinessLine` | `PpClientchargesPds_Businessline` | TField |  |  |
| 5 | `PP.CC.ClientID` | `PpClientchargesPds_Clientid` | TField |  |  |
| 6 | `PP.CC.CustomerAccountNumberCompID` | `PpClientchargesPds_Customeraccountnumbercompid` | TField |  |  |
| 7 | `PP.CC.CustomerAccountNumber` | `PpClientchargesPds_Customeraccountnumber` | TField |  |  |
| 8 | `PP.CC.CustomerAccountCurrency` | `PpClientchargesPds_Customeraccountcurrency` | TField |  |  |
| 9 | `PP.CC.ResidencyStatus` | `PpClientchargesPds_Residencystatus` | TField |  |  |
| 10 | `PP.CC.StartDate` | `PpClientchargesPds_Startdate` | TField |  |  |
| 11 | `PP.CC.CommonCurrency` | `PpClientchargesPds_Commoncurrency` | TField |  |  |
| 12 | `PP.CC.EndDate` | `PpClientchargesPds_Enddate` | TField |  |  |
| 13 | `PP.CC.FeeType` | `PpClientchargesPds_Feetype` |  |  |  |
| 14 | `PP.CC.Ranking` | `PpClientchargesPds_Ranking` |  |  |  |
| 15 | `PP.CC.AlwaysApplyFlag` | `PpClientchargesPds_Alwaysapplyflag` |  |  |  |
| 16 | `PP.CC.ApplyMeOnlyFlag` | `PpClientchargesPds_Applymeonlyflag` |  |  |  |
| 17 | `PP.CC.PercentageVATOnCharge` | `PpClientchargesPds_Percentagevatoncharge` |  |  |  |
| 18 | `PP.CC.FeeTierRangeLowerLimit` | `PpClientchargesPds_Feetierrangelowerlimit` |  |  |  |
| 19 | `PP.CC.FixedChargeAmount` | `PpClientchargesPds_Fixedchargeamount` |  |  |  |
| 20 | `PP.CC.PercentageVariableFee` | `PpClientchargesPds_Percentagevariablefee` |  |  |  |
| 21 | `PP.CC.BaseChargeAmount` | `PpClientchargesPds_Basechargeamount` |  |  |  |
| 22 | `PP.CC.ChargeDiscountAmount` | `PpClientchargesPds_Chargediscountamount` |  |  |  |
| 23 | `PP.CC.ChargeRiseAmount` | `PpClientchargesPds_Chargeriseamount` |  |  |  |
| 24 | `PP.CC.MinimumChargeAmount` | `PpClientchargesPds_Minimumchargeamount` |  |  |  |
| 25 | `PP.CC.MaximumChargeAmount` | `PpClientchargesPds_Maximumchargeamount` |  |  |  |
| 26 | `PP.CC.FixedChargeAmountFX` | `PpClientchargesPds_Fixedchargeamountfx` |  |  |  |
| 27 | `PP.CC.PercentageVariableFeeFX` | `PpClientchargesPds_Percentagevariablefeefx` |  |  |  |
| 28 | `PP.CC.BaseChargeAmountFX` | `PpClientchargesPds_Basechargeamountfx` |  |  |  |
| 29 | `PP.CC.ChargeDiscountAmountFX` | `PpClientchargesPds_Chargediscountamountfx` |  |  |  |
| 30 | `PP.CC.ChargeRiseAmountFX` | `PpClientchargesPds_Chargeriseamountfx` |  |  |  |
| 31 | `PP.CC.AuthoriserDateTime` | `PpClientchargesPds_Authoriserdatetime` | TField |  |  |
| 32 | `PP.CC.RESERVED.10` | `PpClientchargesPds_Reserved10` | TField |  |  |
| 33 | `PP.CC.RESERVED.9` | `PpClientchargesPds_Reserved9` | TField |  |  |
| 34 | `PP.CC.RESERVED.8` | `PpClientchargesPds_Reserved8` | TField |  |  |
| 35 | `PP.CC.RESERVED.7` | `PpClientchargesPds_Reserved7` | TField |  |  |
| 36 | `PP.CC.RESERVED.6` | `PpClientchargesPds_Reserved6` | TField |  |  |
| 37 | `PP.CC.RESERVED.5` | `PpClientchargesPds_Reserved5` | TField |  |  |
| 38 | `PP.CC.RESERVED.4` | `PpClientchargesPds_Reserved4` | TField |  |  |
| 39 | `PP.CC.RESERVED.3` | `PpClientchargesPds_Reserved3` | TField |  |  |
| 40 | `PP.CC.RESERVED.2` | `PpClientchargesPds_Reserved2` | TField |  |  |
| 41 | `PP.CC.RESERVED.1` | `PpClientchargesPds_Reserved1` | TField |  |  |
| 42 | `PP.CC.LOCAL.REF` | `PpClientchargesPds_LocalRef` |  |  |  |
| 43 | `PP.CC.LinkID` | `PpClientchargesPds_Linkid` | TField |  |  |
| 44 | `PP.CC.OVERRIDE` | `PpClientchargesPds_Override` |  |  |  |
| 45 | `PP.CC.RECORD.STATUS` | `PpClientchargesPds_RecordStatus` | String |  |  |
| 46 | `PP.CC.CURR.NO` | `PpClientchargesPds_CurrNo` | String |  |  |
| 47 | `PP.CC.INPUTTER` | `PpClientchargesPds_Inputter` |  |  |  |
| 48 | `PP.CC.DATE.TIME` | `PpClientchargesPds_DateTime` |  |  |  |
| 49 | `PP.CC.AUTHORISER` | `PpClientchargesPds_Authoriser` | String |  |  |
| 50 | `PP.CC.CO.CODE` | `PpClientchargesPds_CoCode` | String |  |  |
| 51 | `PP.CC.DEPT.CODE` | `PpClientchargesPds_DeptCode` | String |  |  |
| 52 | `PP.CC.AUDITOR.CODE` | `PpClientchargesPds_AuditorCode` | String |  |  |
| 53 | `PP.CC.AUDIT.DATE.TIME` | `PpClientchargesPds_AuditDateTime` | String |  |  |
