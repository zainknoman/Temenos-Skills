# PPT.COMPANYPROPERTIES — Table Schema

> Source: `INSERTS/I_F.PPT.COMPANYPROPERTIES` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCOP.CompanyID` | `PptCompanyproperties_Companyid` |  |  |  |
| 2 | `PPCOP.StartDateCompanyProperties` | `PptCompanyproperties_Startdatecompanyproperties` |  |  |  |
| 3 | `PPCOP.HomeCountryCode` | `PptCompanyproperties_Homecountrycode` |  |  |  |
| 4 | `PPCOP.HomeCurrencyCode` | `PptCompanyproperties_Homecurrencycode` |  |  |  |
| 5 | `PPCOP.ApplicationUserID` | `PptCompanyproperties_Applicationuserid` |  |  |  |
| 6 | `PPCOP.CompanyRegion` | `PptCompanyproperties_Companyregion` |  |  |  |
| 7 | `PPCOP.DealerDeskEnabled` | `PptCompanyproperties_Dealerdeskenabled` |  |  |  |
| 8 | `PPCOP.SODRunTime` | `PptCompanyproperties_Sodruntime` |  |  |  |
| 9 | `PPCOP.COBRunTime` | `PptCompanyproperties_Cobruntime` |  |  |  |
| 10 | `PPCOP.CompanyBIC` | `PptCompanyproperties_Companybic` |  |  |  |
| 11 | `PPCOP.DaysActivePayment` | `PptCompanyproperties_Daysactivepayment` |  |  |  |
| 12 | `PPCOP.DaysDuplicateCheck` | `PptCompanyproperties_Daysduplicatecheck` |  |  |  |
| 13 | `PPCOP.ClaimBeneficiaryBIC` | `PptCompanyproperties_Claimbeneficiarybic` |  |  |  |
| 14 | `PPCOP.MaximumClaimDays` | `PptCompanyproperties_Maximumclaimdays` |  |  |  |
| 15 | `PPCOP.AutoRepairWaitIntervalSeconds` | `PptCompanyproperties_Autorepairwaitintervalseconds` |  |  |  |
| 16 | `PPCOP.ScreenWaitIntervalSeconds` | `PptCompanyproperties_Screenwaitintervalseconds` |  |  |  |
| 17 | `PPCOP.DefaultClientID` | `PptCompanyproperties_Defaultclientid` |  |  |  |
| 18 | `PPCOP.DefaultLanguageID` | `PptCompanyproperties_Defaultlanguageid` |  |  |  |
| 19 | `PPCOP.NonSTPIndicator` | `PptCompanyproperties_Nonstpindicator` |  |  |  |
| 20 | `PPCOP.ThresholdNonSTPAmt` | `PptCompanyproperties_Thresholdnonstpamt` |  |  |  |
| 21 | `PPCOP.ThresholdAutoFXAmt` | `PptCompanyproperties_Thresholdautofxamt` |  |  |  |
| 22 | `PPCOP.FXTolerancePercentage` | `PptCompanyproperties_Fxtolerancepercentage` |  |  |  |
| 23 | `PPCOP.TimeZone` | `PptCompanyproperties_Timezone` |  |  |  |
| 24 | `PPCOP.DebitStatementFormatName` | `PptCompanyproperties_Debitstatementformatname` |  |  |  |
| 25 | `PPCOP.CreditStatementFormatName` | `PptCompanyproperties_Creditstatementformatname` |  |  |  |
| 26 | `PPCOP.OCPStatementFormatName` | `PptCompanyproperties_Ocpstatementformatname` |  |  |  |
| 27 | `PPCOP.TradeCurrency1` | `PptCompanyproperties_Tradecurrency1` |  |  |  |
| 28 | `PPCOP.TradeCurrency2` | `PptCompanyproperties_Tradecurrency2` |  |  |  |
| 29 | `PPCOP.TradeCurrency3` | `PptCompanyproperties_Tradecurrency3` |  |  |  |
| 30 | `PPCOP.ClaimsWaitIntervalSeconds` | `PptCompanyproperties_Claimswaitintervalseconds` |  |  |  |
| 31 | `PPCOP.DefaultCompanyIndicator` | `PptCompanyproperties_Defaultcompanyindicator` |  |  |  |
| 32 | `PPCOP.EndDateCompanyProperties` | `PptCompanyproperties_Enddatecompanyproperties` |  |  |  |
| 33 | `PPCOP.MapIBANIndicator` | `PptCompanyproperties_Mapibanindicator` |  |  |  |
| 34 | `PPCOP.ReversedPostingProduct` | `PptCompanyproperties_Reversedpostingproduct` |  |  |  |
| 35 | `PPCOP.ReversedSourceProduct` | `PptCompanyproperties_Reversedsourceproduct` |  |  |  |
| 36 | `PPCOP.ReversedFeeProduct` | `PptCompanyproperties_Reversedfeeproduct` |  |  |  |
| 37 | `PPCOP.DefaultRepairFee` | `PptCompanyproperties_Defaultrepairfee` |  |  |  |
| 38 | `PPCOP.BillingDeltaFull` | `PptCompanyproperties_Billingdeltafull` |  |  |  |
| 39 | `PPCOP.BillingPreviousProcessingDate` | `PptCompanyproperties_Billingpreviousprocessingdate` |  |  |  |
| 40 | `PPCOP.BICIBANCheck` | `PptCompanyproperties_Bicibancheck` |  |  |  |
| 41 | `PPCOP.BICuploadDeltaFull` | `PptCompanyproperties_Bicuploaddeltafull` |  |  |  |
| 42 | `PPCOP.BICuploadCutOverDate` | `PptCompanyproperties_Bicuploadcutoverdate` |  |  |  |
| 43 | `PPCOP.BICuploadJobOffsetDays` | `PptCompanyproperties_Bicuploadjoboffsetdays` |  |  |  |
| 44 | `PPCOP.BICuploadReport` | `PptCompanyproperties_Bicuploadreport` |  |  |  |
| 45 | `PPCOP.BICuploadSchedule` | `PptCompanyproperties_Bicuploadschedule` |  |  |  |
| 46 | `PPCOP.TriggerFileLocation` | `PptCompanyproperties_Triggerfilelocation` |  |  |  |
| 47 | `PPCOP.InsightDeliveryLocation` | `PptCompanyproperties_Insightdeliverylocation` |  |  |  |
| 48 | `PPCOP.InsightArchiveLocation` | `PptCompanyproperties_Insightarchivelocation` |  |  |  |
| 49 | `PPCOP.AMLDeliveryLocation` | `PptCompanyproperties_Amldeliverylocation` |  |  |  |
| 50 | `PPCOP.AMLArchiveLocation` | `PptCompanyproperties_Amlarchivelocation` |  |  |  |
| 51 | `PPCOP.BillingDeliveryLocation` | `PptCompanyproperties_Billingdeliverylocation` |  |  |  |
| 52 | `PPCOP.BillingArchiveLocation` | `PptCompanyproperties_Billingarchivelocation` |  |  |  |
| 53 | `PPCOP.ReportsDeliveryLocation` | `PptCompanyproperties_Reportsdeliverylocation` |  |  |  |
| 54 | `PPCOP.ReportsArchiveLocation` | `PptCompanyproperties_Reportsarchivelocation` |  |  |  |
| 55 | `PPCOP.BICUploadLocation` | `PptCompanyproperties_Bicuploadlocation` |  |  |  |
| 56 | `PPCOP.BICUploadArchiveLocation` | `PptCompanyproperties_Bicuploadarchivelocation` |  |  |  |
| 57 | `PPCOP.BICUploadReportLocation` | `PptCompanyproperties_Bicuploadreportlocation` |  |  |  |
| 58 | `PPCOP.BankDirFullFileNameFormat` | `PptCompanyproperties_Bankdirfullfilenameformat` |  |  |  |
| 59 | `PPCOP.BankDirDeltaFileNameFormat` | `PptCompanyproperties_Bankdirdeltafilenameformat` |  |  |  |
| 60 | `PPCOP.IbanPlusFullFileNameFormat` | `PptCompanyproperties_Ibanplusfullfilenameformat` |  |  |  |
| 61 | `PPCOP.IbanPlusDeltaFileNameFormat` | `PptCompanyproperties_Ibanplusdeltafilenameformat` |  |  |  |
| 62 | `PPCOP.RACCompanyProperties` | `PptCompanyproperties_Raccompanyproperties` |  |  |  |
| 63 | `PPCOP.RSCCompanyProperties` | `PptCompanyproperties_Rsccompanyproperties` |  |  |  |
| 64 | `PPCOP.EntryUserID` | `PptCompanyproperties_Entryuserid` |  |  |  |
| 65 | `PPCOP.EntryDateTime` | `PptCompanyproperties_Entrydatetime` |  |  |  |
| 66 | `PPCOP.ApproverUserID` | `PptCompanyproperties_Approveruserid` |  |  |  |
| 67 | `PPCOP.ApprovedDateTime` | `PptCompanyproperties_Approveddatetime` |  |  |  |
| 68 | `PPCOP.GLHomeCurrency` | `PptCompanyproperties_Glhomecurrency` |  |  |  |
| 69 | `PPCOP.MktExchMethod` | `PptCompanyproperties_Mktexchmethod` |  |  |  |
| 70 | `PPCOP.EnableFATFReg` | `PptCompanyproperties_Enablefatfreg` |  |  |  |
| 71 | `PPCOP.UpdateCashPosition` | `PptCompanyproperties_Updatecashposition` |  |  |  |
| 72 | `PPCOP.RateRequest` | `PptCompanyproperties_Raterequest` |  |  |  |
| 73 | `PPCOP.FXRateReqCutoff` | `PptCompanyproperties_Fxratereqcutoff` |  |  |  |
| 74 | `PPCOP.CurrencyMarket` | `PptCompanyproperties_Currencymarket` |  |  |  |
