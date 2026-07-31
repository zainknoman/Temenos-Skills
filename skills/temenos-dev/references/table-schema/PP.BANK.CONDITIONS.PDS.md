# PP.BANK.CONDITIONS.PDS — Table Schema

> Source: `INSERTS/I_F.PP.BANK.CONDITIONS.PDS` in `PP_BankConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.BC.CompanyID` | `PpBankConditionsPds_Companyid` | TField |  |  |
| 2 | `PP.BC.CorrespondentBIC` | `PpBankConditionsPds_Correspondentbic` | TField |  |  |
| 3 | `PP.BC.SLAID` | `PpBankConditionsPds_Slaid` | TField |  |  |
| 4 | `PP.BC.CurrencyCode` | `PpBankConditionsPds_Currencycode` | TField |  |  |
| 5 | `PP.BC.StartDate` | `PpBankConditionsPds_Startdate` | TField |  |  |
| 6 | `PP.BC.CTRNonSTPIndicator` | `PpBankConditionsPds_Ctrnonstpindicator` | TField |  |  |
| 7 | `PP.BC.CreditInstruction` | `PpBankConditionsPds_Creditinstruction` | TField |  |  |
| 8 | `PP.BC.BTRNonSTPIndicator` | `PpBankConditionsPds_Btrnonstpindicator` | TField |  |  |
| 9 | `PP.BC.DebitInstruction` | `PpBankConditionsPds_Debitinstruction` | TField |  |  |
| 10 | `PP.BC.WareHouseFlag` | `PpBankConditionsPds_Warehouseflag` | TField |  |  |
| 11 | `PP.BC.WareHouseReleaseTime` | `PpBankConditionsPds_Warehousereleasetime` | TField |  |  |
| 12 | `PP.BC.PSDECChargeCompliant` | `PpBankConditionsPds_Psdecchargecompliant` | TField |  |  |
| 13 | `PP.BC.LanguageID` | `PpBankConditionsPds_Languageid` | TField |  |  |
| 14 | `PP.BC.CreditStmtFormatName` | `PpBankConditionsPds_Creditstmtformatname` | TField |  |  |
| 15 | `PP.BC.DebitStmtFormatName` | `PpBankConditionsPds_Debitstmtformatname` | TField |  |  |
| 16 | `PP.BC.FXSpread` | `PpBankConditionsPds_Fxspread` | TField |  |  |
| 17 | `PP.BC.EndDate` | `PpBankConditionsPds_Enddate` | TField |  |  |
| 18 | `PP.BC.ChargeAccountIndicator` | `PpBankConditionsPds_Chargeaccountindicator` | TField |  |  |
| 19 | `PP.BC.TransactionCurrency` | `PpBankConditionsPds_Transactioncurrency` |  |  |  |
| 20 | `PP.BC.ChargeAccountCompanyID` | `PpBankConditionsPds_Chargeaccountcompanyid` |  |  |  |
| 21 | `PP.BC.ChargeAccountNumber` | `PpBankConditionsPds_Chargeaccountnumber` |  |  |  |
| 22 | `PP.BC.ChargeAccountCurrency` | `PpBankConditionsPds_Chargeaccountcurrency` |  |  |  |
| 23 | `PP.BC.AdviceIndicator` | `PpBankConditionsPds_Adviceindicator` | TField |  |  |
| 24 | `PP.BC.SequenceNumber` | `PpBankConditionsPds_Sequencenumber` |  |  |  |
| 25 | `PP.BC.DebitCreditAdvice` | `PpBankConditionsPds_Debitcreditadvice` |  |  |  |
| 26 | `PP.BC.CTRBTRIndicator` | `PpBankConditionsPds_Ctrbtrindicator` |  |  |  |
| 27 | `PP.BC.InitiatedByOthers` | `PpBankConditionsPds_Initiatedbyothers` |  |  |  |
| 28 | `PP.BC.AmountCurreny` | `PpBankConditionsPds_Amountcurreny` |  |  |  |
| 29 | `PP.BC.FromAmount` | `PpBankConditionsPds_Fromamount` |  |  |  |
| 30 | `PP.BC.ToAmount` | `PpBankConditionsPds_Toamount` |  |  |  |
| 31 | `PP.BC.DeliveryMethod` | `PpBankConditionsPds_Deliverymethod` |  |  |  |
| 32 | `PP.BC.Telephonenumber` | `PpBankConditionsPds_Telephonenumber` |  |  |  |
| 33 | `PP.BC.EmailID` | `PpBankConditionsPds_Emailid` |  |  |  |
| 34 | `PP.BC.BICAddress` | `PpBankConditionsPds_Bicaddress` |  |  |  |
| 35 | `PP.BC.SMSNumber` | `PpBankConditionsPds_Smsnumber` |  |  |  |
| 36 | `PP.BC.FaxNumber` | `PpBankConditionsPds_Faxnumber` |  |  |  |
| 37 | `PP.BC.PostName` | `PpBankConditionsPds_Postname` |  |  |  |
| 38 | `PP.BC.PostAddress1` | `PpBankConditionsPds_Postaddress1` |  |  |  |
| 39 | `PP.BC.PostAddress2` | `PpBankConditionsPds_Postaddress2` |  |  |  |
| 40 | `PP.BC.PostAddress3` | `PpBankConditionsPds_Postaddress3` |  |  |  |
| 41 | `PP.BC.Attention` | `PpBankConditionsPds_Attention` |  |  |  |
| 42 | `PP.BC.AllowSpecialCharacterSet` | `PpBankConditionsPds_Allowspecialcharacterset` | TField |  |  |
| 43 | `PP.BC.CodePageSet` | `PpBankConditionsPds_Codepageset` | TField |  |  |
| 44 | `PP.BC.TranAckNackIndicator` | `PpBankConditionsPds_Tranacknackindicator` | TField |  |  |
| 45 | `PP.BC.InterimStatusIndicator` | `PpBankConditionsPds_Interimstatusindicator` | TField |  |  |
| 46 | `PP.BC.CustomerStatusMessageType` | `PpBankConditionsPds_Customerstatusmessagetype` | TField |  |  |
| 47 | `PP.BC.LOCAL.REF` | `PpBankConditionsPds_LocalRef` |  |  |  |
| 48 | `PP.BC.LinkID` | `PpBankConditionsPds_Linkid` | TField |  |  |
| 49 | `PP.BC.OVERRIDE` | `PpBankConditionsPds_Override` |  |  |  |
| 50 | `PP.BC.RECORD.STATUS` | `PpBankConditionsPds_RecordStatus` | String |  |  |
| 51 | `PP.BC.CURR.NO` | `PpBankConditionsPds_CurrNo` | String |  |  |
| 52 | `PP.BC.INPUTTER` | `PpBankConditionsPds_Inputter` |  |  |  |
| 53 | `PP.BC.DATE.TIME` | `PpBankConditionsPds_DateTime` |  |  |  |
| 54 | `PP.BC.AUTHORISER` | `PpBankConditionsPds_Authoriser` | String |  |  |
| 55 | `PP.BC.CO.CODE` | `PpBankConditionsPds_CoCode` | String |  |  |
| 56 | `PP.BC.DEPT.CODE` | `PpBankConditionsPds_DeptCode` | String |  |  |
| 57 | `PP.BC.AUDITOR.CODE` | `PpBankConditionsPds_AuditorCode` | String |  |  |
| 58 | `PP.BC.AUDIT.DATE.TIME` | `PpBankConditionsPds_AuditDateTime` | String |  |  |
| 59 | `PP.BC.MT210MatchRequired` | `PpBankConditionsPds_Mt210matchrequired` | TField |  |  |
| 60 | `PP.BC.GPILeadTime` | `PpBankConditionsPds_Gpileadtime` | TField |  |  |
