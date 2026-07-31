# PP.CLEARING.SETTING.PDS — Table Schema

> Source: `INSERTS/I_F.PP.CLEARING.SETTING.PDS` in `PP_LocalClearingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CGS.CompanyID` | `PpClearingSettingPds_Companyid` | TField |  |  |
| 2 | `PP.CGS.ClearingID` | `PpClearingSettingPds_Clearingid` | TField |  |  |
| 3 | `PP.CGS.ClearingCurrency` | `PpClearingSettingPds_Clearingcurrency` | TField |  |  |
| 4 | `PP.CGS.ClearingNatureCode` | `PpClearingSettingPds_Clearingnaturecode` | TField |  |  |
| 5 | `PP.CGS.MessageDirection` | `PpClearingSettingPds_Messagedirection` | TField |  |  |
| 6 | `PP.CGS.MessagePaymentType` | `PpClearingSettingPds_Messagepaymenttype` | TField |  |  |
| 7 | `PP.CGS.StartDate` | `PpClearingSettingPds_Startdate` | TField |  |  |
| 8 | `PP.CGS.ClearingAccountCompany` | `PpClearingSettingPds_Clearingaccountcompany` | TField |  |  |
| 9 | `PP.CGS.ClearingAccountNumber` | `PpClearingSettingPds_Clearingaccountnumber` | TField |  |  |
| 10 | `PP.CGS.ClearingAccountCurrency` | `PpClearingSettingPds_Clearingaccountcurrency` | TField |  |  |
| 11 | `PP.CGS.SuspenseAccountCompany` | `PpClearingSettingPds_Suspenseaccountcompany` |  |  |  |
| 12 | `PP.CGS.SuspenseAccountNumber` | `PpClearingSettingPds_Suspenseaccountnumber` |  |  |  |
| 13 | `PP.CGS.SuspenseAccountCurrency` | `PpClearingSettingPds_Suspenseaccountcurrency` |  |  |  |
| 14 | `PP.CGS.SettlementBookingIndicator` | `PpClearingSettingPds_Settlementbookingindicator` | TField |  |  |
| 15 | `PP.CGS.ManualVerificationIndicator` | `PpClearingSettingPds_Manualverificationindicator` | TField |  |  |
| 16 | `PP.CGS.SettlementShift` | `PpClearingSettingPds_Settlementshift` | TField |  |  |
| 17 | `PP.CGS.ScheduledForReleaseIndicator` | `PpClearingSettingPds_Scheduledforreleaseindicator` | TField |  |  |
| 18 | `PP.CGS.EndDate` | `PpClearingSettingPds_Enddate` | TField |  |  |
| 19 | `PP.CGS.ValidationRequired` | `PpClearingSettingPds_Validationrequired` | TField |  |  |
| 20 | `PP.CGS.Ranking` | `PpClearingSettingPds_Ranking` |  |  |  |
| 21 | `PP.CGS.ValidateAPI` | `PpClearingSettingPds_Validateapi` |  |  |  |
| 22 | `PP.CGS.AutomatedReturnIndicator` | `PpClearingSettingPds_Automatedreturnindicator` | TField |  |  |
| 23 | `PP.CGS.CreateReturnBookingIndicator` | `PpClearingSettingPds_Createreturnbookingindicator` | TField |  |  |
| 24 | `PP.CGS.CreateReturnMessageIndicator` | `PpClearingSettingPds_Createreturnmessageindicator` | TField |  |  |
| 25 | `PP.CGS.ReturnSuspenseAccountCompany` | `PpClearingSettingPds_Returnsuspenseaccountcompany` |  |  |  |
| 26 | `PP.CGS.ReturnSuspenseAccountNumber` | `PpClearingSettingPds_Returnsuspenseaccountnumber` |  |  |  |
| 27 | `PP.CGS.ReturnSuspenseAccountCurrency` | `PpClearingSettingPds_Returnsuspenseaccountcurrency` |  |  |  |
| 28 | `PP.CGS.CreateRejectMessageIndicator` | `PpClearingSettingPds_Createrejectmessageindicator` | TField |  |  |
| 29 | `PP.CGS.AcceptanceDays` | `PpClearingSettingPds_Acceptancedays` | TField |  |  |
| 30 | `PP.CGS.ClearingTransactionType` | `PpClearingSettingPds_Clearingtransactiontype` | TField |  |  |
| 31 | `PP.CGS.AuthRefundAllowedDays` | `PpClearingSettingPds_Authrefundalloweddays` | TField |  |  |
| 32 | `PP.CGS.UnAuthRefundAllowedDays` | `PpClearingSettingPds_Unauthrefundalloweddays` | TField |  |  |
| 33 | `PP.CGS.ImposeReturnValueDate` | `PpClearingSettingPds_Imposereturnvaluedate` | TField |  |  |
| 34 | `PP.CGS.MandateVerificationIndicator` | `PpClearingSettingPds_Mandateverificationindicator` | TField |  |  |
| 35 | `PP.CGS.AutoRegisterMandateIndicator` | `PpClearingSettingPds_Autoregistermandateindicator` | TField |  |  |
| 36 | `PP.CGS.MandateAmendmentIndicator` | `PpClearingSettingPds_Mandateamendmentindicator` | TField |  |  |
| 37 | `PP.CGS.MandateLimitCheckIndicator` | `PpClearingSettingPds_Mandatelimitcheckindicator` | TField |  |  |
| 38 | `PP.CGS.CrdRestrictionCheckIndicator` | `PpClearingSettingPds_Crdrestrictioncheckindicator` | TField |  |  |
| 39 | `PP.CGS.MaxInstTimeOut` | `PpClearingSettingPds_Maxinsttimeout` | TField |  |  |
| 40 | `PP.CGS.AutoNegativeCancelReqResponse` | `PpClearingSettingPds_Autonegativecancelreqresponse` | TField |  |  |
| 41 | `PP.CGS.OriginalTrnLookUpCriteriaAPI` | `PpClearingSettingPds_Originaltrnlookupcriteriaapi` | TField |  |  |
| 42 | `PP.CGS.SuspenseAccountNumberContra` | `PpClearingSettingPds_Suspenseaccountnumbercontra` |  |  |  |
| 43 | `PP.CGS.SuspenseAccNumberContraCcy` | `PpClearingSettingPds_Suspenseaccnumbercontraccy` |  |  |  |
| 44 | `PP.CGS.SuspenseAccNumberContraCmpy` | `PpClearingSettingPds_Suspenseaccnumbercontracmpy` |  |  |  |
| 45 | `PP.CGS.ChequesAutoClear` | `PpClearingSettingPds_Chequesautoclear` | TField |  |  |
| 46 | `PP.CGS.AcceptanceDaysCustInitCanclReq` | `PpClearingSettingPds_Acceptancedayscustinitcanclreq` | TField |  |  |
| 47 | `PP.CGS.CancellationOverdueDays` | `PpClearingSettingPds_Cancellationoverduedays` | TField |  |  |
| 48 | `PP.CGS.RESERVED.8` | `PpClearingSettingPds_Reserved8` | TField |  |  |
| 49 | `PP.CGS.RESERVED.7` | `PpClearingSettingPds_Reserved7` | TField |  |  |
| 50 | `PP.CGS.RESERVED.6` | `PpClearingSettingPds_Reserved6` | TField |  |  |
| 51 | `PP.CGS.RESERVED.5` | `PpClearingSettingPds_Reserved5` | TField |  |  |
| 52 | `PP.CGS.RESERVED.4` | `PpClearingSettingPds_Reserved4` | TField |  |  |
| 53 | `PP.CGS.RESERVED.3` | `PpClearingSettingPds_Reserved3` | TField |  |  |
| 54 | `PP.CGS.RESERVED.2` | `PpClearingSettingPds_Reserved2` | TField |  |  |
| 55 | `PP.CGS.RESERVED.1` | `PpClearingSettingPds_Reserved1` | TField |  |  |
| 56 | `PP.CGS.LOCAL.REF` | `PpClearingSettingPds_LocalRef` |  |  |  |
| 57 | `PP.CGS.LinkID` | `PpClearingSettingPds_Linkid` | TField |  |  |
| 58 | `PP.CGS.OVERRIDE` | `PpClearingSettingPds_Override` |  |  |  |
| 59 | `PP.CGS.RECORD.STATUS` | `PpClearingSettingPds_RecordStatus` | String |  |  |
| 60 | `PP.CGS.CURR.NO` | `PpClearingSettingPds_CurrNo` | String |  |  |
| 61 | `PP.CGS.INPUTTER` | `PpClearingSettingPds_Inputter` |  |  |  |
| 62 | `PP.CGS.DATE.TIME` | `PpClearingSettingPds_DateTime` |  |  |  |
| 63 | `PP.CGS.AUTHORISER` | `PpClearingSettingPds_Authoriser` | String |  |  |
| 64 | `PP.CGS.CO.CODE` | `PpClearingSettingPds_CoCode` | String |  |  |
| 65 | `PP.CGS.DEPT.CODE` | `PpClearingSettingPds_DeptCode` | String |  |  |
| 66 | `PP.CGS.AUDITOR.CODE` | `PpClearingSettingPds_AuditorCode` | String |  |  |
| 67 | `PP.CGS.AUDIT.DATE.TIME` | `PpClearingSettingPds_AuditDateTime` | String |  |  |
