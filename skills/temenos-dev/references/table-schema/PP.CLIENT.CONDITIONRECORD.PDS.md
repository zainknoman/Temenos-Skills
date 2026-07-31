# PP.CLIENT.CONDITIONRECORD.PDS — Table Schema

> Source: `INSERTS/I_F.PP.CLIENT.CONDITIONRECORD.PDS` in `PP_ClientConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CCR.CompanyID` | `PpClientConditionrecordPds_Companyid` | TField |  |  |
| 2 | `PP.CCR.ClientConditionProduct` | `PpClientConditionrecordPds_Clientconditionproduct` | TField |  |  |
| 3 | `PP.CCR.SourceProduct` | `PpClientConditionrecordPds_Sourceproduct` | TField |  |  |
| 4 | `PP.CCR.BusinessLine` | `PpClientConditionrecordPds_Businessline` | TField |  |  |
| 5 | `PP.CCR.ClientID` | `PpClientConditionrecordPds_Clientid` | TField |  |  |
| 6 | `PP.CCR.AccountNumber` | `PpClientConditionrecordPds_Accountnumber` | TField |  |  |
| 7 | `PP.CCR.AccountCurrency` | `PpClientConditionrecordPds_Accountcurrency` | TField |  |  |
| 8 | `PP.CCR.AccountCompanyID` | `PpClientConditionrecordPds_Accountcompanyid` | TField |  |  |
| 9 | `PP.CCR.StartDate` | `PpClientConditionrecordPds_Startdate` | TField |  |  |
| 10 | `PP.CCR.EndDate` | `PpClientConditionrecordPds_Enddate` | TField |  |  |
| 11 | `PP.CCR.LanguageID` | `PpClientConditionrecordPds_Languageid` | TField |  |  |
| 12 | `PP.CCR.DrStatementFormat` | `PpClientConditionrecordPds_Drstatementformat` | TField |  |  |
| 13 | `PP.CCR.CRStatementFormat` | `PpClientConditionrecordPds_Crstatementformat` | TField |  |  |
| 14 | `PP.CCR.BillingIndicator` | `PpClientConditionrecordPds_Billingindicator` | TField |  |  |
| 15 | `PP.CCR.ChargePostingSeparately` | `PpClientConditionrecordPds_Chargepostingseparately` | TField |  |  |
| 16 | `PP.CCR.ChargePostingDetail` | `PpClientConditionrecordPds_Chargepostingdetail` | TField |  |  |
| 17 | `PP.CCR.VatPrincipal` | `PpClientConditionrecordPds_Vatprincipal` | TField |  |  |
| 18 | `PP.CCR.VATOnCharge` | `PpClientConditionrecordPds_Vatoncharge` | TField |  |  |
| 19 | `PP.CCR.NonSTPIndicator` | `PpClientConditionrecordPds_Nonstpindicator` | TField |  |  |
| 20 | `PP.CCR.AdviceIndicator` | `PpClientConditionrecordPds_Adviceindicator` | TField |  |  |
| 21 | `PP.CCR.DebitCreditAdvice` | `PpClientConditionrecordPds_Debitcreditadvice` |  |  |  |
| 22 | `PP.CCR.SequenceNumber` | `PpClientConditionrecordPds_Sequencenumber` |  |  |  |
| 23 | `PP.CCR.DeliveryMethod` | `PpClientConditionrecordPds_Deliverymethod` |  |  |  |
| 24 | `PP.CCR.PhoneConfirmation` | `PpClientConditionrecordPds_Phoneconfirmation` |  |  |  |
| 25 | `PP.CCR.SMS` | `PpClientConditionrecordPds_Sms` |  |  |  |
| 26 | `PP.CCR.FAX` | `PpClientConditionrecordPds_Fax` |  |  |  |
| 27 | `PP.CCR.EmailID` | `PpClientConditionrecordPds_Emailid` |  |  |  |
| 28 | `PP.CCR.MailLine1` | `PpClientConditionrecordPds_Mailline1` |  |  |  |
| 29 | `PP.CCR.MailLine2` | `PpClientConditionrecordPds_Mailline2` |  |  |  |
| 30 | `PP.CCR.MailLine3` | `PpClientConditionrecordPds_Mailline3` |  |  |  |
| 31 | `PP.CCR.MailLine4` | `PpClientConditionrecordPds_Mailline4` |  |  |  |
| 32 | `PP.CCR.Swift` | `PpClientConditionrecordPds_Swift` |  |  |  |
| 33 | `PP.CCR.Attention` | `PpClientConditionrecordPds_Attention` |  |  |  |
| 34 | `PP.CCR.AdviceType` | `PpClientConditionrecordPds_Advicetype` |  |  |  |
| 35 | `PP.CCR.AdviceTxnLowerLimit` | `PpClientConditionrecordPds_Advicetxnlowerlimit` |  |  |  |
| 36 | `PP.CCR.FXDiscountIndicator` | `PpClientConditionrecordPds_Fxdiscountindicator` | TField |  |  |
| 37 | `PP.CCR.TransactionCurrency` | `PpClientConditionrecordPds_Transactioncurrency` |  |  |  |
| 38 | `PP.CCR.Discount` | `PpClientConditionrecordPds_Discount` |  |  |  |
| 39 | `PP.CCR.SeparatechargeAccountIndicator` | `PpClientConditionrecordPds_Separatechargeaccountindicator` | TField |  |  |
| 40 | `PP.CCR.DebitCreditIndicator` | `PpClientConditionrecordPds_Debitcreditindicator` |  |  |  |
| 41 | `PP.CCR.ChargeAccTransactionCCY` | `PpClientConditionrecordPds_Chargeacctransactionccy` |  |  |  |
| 42 | `PP.CCR.ChargeAccountCompanyID` | `PpClientConditionrecordPds_Chargeaccountcompanyid` |  |  |  |
| 43 | `PP.CCR.ChargeAccountCurrency` | `PpClientConditionrecordPds_Chargeaccountcurrency` |  |  |  |
| 44 | `PP.CCR.ChargeAccountNumber` | `PpClientConditionrecordPds_Chargeaccountnumber` |  |  |  |
| 45 | `PP.CCR.FXNonSTPIndicator` | `PpClientConditionrecordPds_Fxnonstpindicator` | TField |  |  |
| 46 | `PP.CCR.FXNonSTPAmount` | `PpClientConditionrecordPds_Fxnonstpamount` | TField |  |  |
| 47 | `PP.CCR.DebitSpecialInstructions` | `PpClientConditionrecordPds_Debitspecialinstructions` | TField |  |  |
| 48 | `PP.CCR.CreditSpecialInstructions` | `PpClientConditionrecordPds_Creditspecialinstructions` | TField |  |  |
| 49 | `PP.CCR.CurrencyCode` | `PpClientConditionrecordPds_Currencycode` |  |  |  |
| 50 | `PP.CCR.IncomingCutOffLeadTime` | `PpClientConditionrecordPds_Incomingcutoffleadtime` |  |  |  |
| 51 | `PP.CCR.OutgoingCutOffLeadTime` | `PpClientConditionrecordPds_Outgoingcutoffleadtime` |  |  |  |
| 52 | `PP.CCR.AccountSubstitution` | `PpClientConditionrecordPds_Accountsubstitution` | TField |  |  |
| 53 | `PP.CCR.ReleaseTime` | `PpClientConditionrecordPds_Releasetime` | TField |  |  |
| 54 | `PP.CCR.DebitFloat` | `PpClientConditionrecordPds_Debitfloat` | TField |  |  |
| 55 | `PP.CCR.CreditFloat` | `PpClientConditionrecordPds_Creditfloat` | TField |  |  |
| 56 | `PP.CCR.AuthoriserDateTime` | `PpClientConditionrecordPds_Authoriserdatetime` | TField |  |  |
| 57 | `PP.CCR.ThresholdAmount` | `PpClientConditionrecordPds_Thresholdamount` | TField |  |  |
| 58 | `PP.CCR.BatchACKNACKIndicator` | `PpClientConditionrecordPds_Batchacknackindicator` | TField |  |  |
| 59 | `PP.CCR.TranNACKIndicator` | `PpClientConditionrecordPds_Trannackindicator` | TField |  |  |
| 60 | `PP.CCR.BalanceCheckOnChgAct` | `PpClientConditionrecordPds_Balancecheckonchgact` | TField |  |  |
| 61 | `PP.CCR.InterimStatusIndicator` | `PpClientConditionrecordPds_Interimstatusindicator` | TField |  |  |
| 62 | `PP.CCR.CustomerStatusMessageType` | `PpClientConditionrecordPds_Customerstatusmessagetype` | TField |  |  |
| 63 | `PP.CCR.TaxId` | `PpClientConditionrecordPds_Taxid` | TField |  |  |
| 64 | `PP.CCR.TaxTypeId` | `PpClientConditionrecordPds_Taxtypeid` | TField |  |  |
| 65 | `PP.CCR.CustomerStatusReportRejects` | `PpClientConditionrecordPds_Customerstatusreportrejects` | TField |  |  |
| 66 | `PP.CCR.RESERVED.9` | `PpClientConditionrecordPds_Reserved9` | TField |  |  |
| 67 | `PP.CCR.RESERVED.8` | `PpClientConditionrecordPds_Reserved8` | TField |  |  |
| 68 | `PP.CCR.RESERVED.7` | `PpClientConditionrecordPds_Reserved7` | TField |  |  |
| 69 | `PP.CCR.RESERVED.6` | `PpClientConditionrecordPds_Reserved6` | TField |  |  |
| 70 | `PP.CCR.RESERVED.5` | `PpClientConditionrecordPds_Reserved5` | TField |  |  |
| 71 | `PP.CCR.RESERVED.4` | `PpClientConditionrecordPds_Reserved4` | TField |  |  |
| 72 | `PP.CCR.RESERVED.3` | `PpClientConditionrecordPds_Reserved3` | TField |  |  |
| 73 | `PP.CCR.RESERVED.2` | `PpClientConditionrecordPds_Reserved2` | TField |  |  |
| 74 | `PP.CCR.RESERVED.1` | `PpClientConditionrecordPds_Reserved1` | TField |  |  |
| 75 | `PP.CCR.LOCAL.REF` | `PpClientConditionrecordPds_LocalRef` |  |  |  |
| 76 | `PP.CCR.LinkID` | `PpClientConditionrecordPds_Linkid` | TField |  |  |
| 77 | `PP.CCR.OVERRIDE` | `PpClientConditionrecordPds_Override` |  |  |  |
| 78 | `PP.CCR.RECORD.STATUS` | `PpClientConditionrecordPds_RecordStatus` | String |  |  |
| 79 | `PP.CCR.CURR.NO` | `PpClientConditionrecordPds_CurrNo` | String |  |  |
| 80 | `PP.CCR.INPUTTER` | `PpClientConditionrecordPds_Inputter` |  |  |  |
| 81 | `PP.CCR.DATE.TIME` | `PpClientConditionrecordPds_DateTime` |  |  |  |
| 82 | `PP.CCR.AUTHORISER` | `PpClientConditionrecordPds_Authoriser` | String |  |  |
| 83 | `PP.CCR.CO.CODE` | `PpClientConditionrecordPds_CoCode` | String |  |  |
| 84 | `PP.CCR.DEPT.CODE` | `PpClientConditionrecordPds_DeptCode` | String |  |  |
| 85 | `PP.CCR.AUDITOR.CODE` | `PpClientConditionrecordPds_AuditorCode` | String |  |  |
| 86 | `PP.CCR.AUDIT.DATE.TIME` | `PpClientConditionrecordPds_AuditDateTime` | String |  |  |
