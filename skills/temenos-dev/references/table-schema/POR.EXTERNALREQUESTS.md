# POR.EXTERNALREQUESTS — Table Schema

> Source: `INSERTS/I_F.POR.EXTERNALREQUESTS` in `PP_PaymentWorkflowService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPEXR.PendingResponse` | `PorExternalrequests_Pendingresponse` | TField |  |  |
| 2 | `PPEXR.ProcessingCompanyCode` | `PorExternalrequests_Processingcompanycode` | TField |  | Indicates the company ID for which the record is created. |
| 3 | `PPEXR.RequestType` | `PorExternalrequests_Requesttype` |  |  |  |
| 4 | `PPEXR.UniqueReference` | `PorExternalrequests_Uniquereference` |  |  |  |
| 5 | `PPEXR.UserOperation` | `PorExternalrequests_Useroperation` |  |  |  |
| 6 | `PPEXR.SentDateTime` | `PorExternalrequests_Sentdatetime` |  |  |  |
| 7 | `PPEXR.ReceivedDateTime` | `PorExternalrequests_Receiveddatetime` |  |  |  |
| 8 | `PPEXR.DuplicateMessageSent` | `PorExternalrequests_Duplicatemessagesent` |  |  |  |
| 9 | `PPEXR.RequestStatus` | `PorExternalrequests_Requeststatus` |  |  |  |
| 10 | `PPEXR.DebitCreditIndicator` | `PorExternalrequests_Debitcreditindicator` |  |  |  |
| 11 | `PPEXR.BBANAccountNumber` | `PorExternalrequests_Bbanaccountnumber` |  |  |  |
| 12 | `PPEXR.IBANAccountNumber` | `PorExternalrequests_Ibanaccountnumber` |  |  |  |
| 13 | `PPEXR.DDASystem` | `PorExternalrequests_Ddasystem` |  |  |  |
| 14 | `PPEXR.AccountCompany` | `PorExternalrequests_Accountcompany` |  |  |  |
| 15 | `PPEXR.AccountNumber` | `PorExternalrequests_Accountnumber` |  |  |  |
| 16 | `PPEXR.AccountCurrency` | `PorExternalrequests_Accountcurrency` |  |  |  |
| 17 | `PPEXR.AccountStatus` | `PorExternalrequests_Accountstatus` |  |  |  |
| 18 | `PPEXR.AccountType` | `PorExternalrequests_Accounttype` |  |  |  |
| 19 | `PPEXR.RelatedIBAN` | `PorExternalrequests_Relatediban` |  |  |  |
| 20 | `PPEXR.CustomerID` | `PorExternalrequests_Customerid` |  |  |  |
| 21 | `PPEXR.Name1` | `PorExternalrequests_Name1` |  |  |  |
| 22 | `PPEXR.Name2` | `PorExternalrequests_Name2` |  |  |  |
| 23 | `PPEXR.Street` | `PorExternalrequests_Street` |  |  |  |
| 24 | `PPEXR.Address` | `PorExternalrequests_Address` |  |  |  |
| 25 | `PPEXR.TownCountry` | `PorExternalrequests_Towncountry` |  |  |  |
| 26 | `PPEXR.PostalCode` | `PorExternalrequests_Postalcode` |  |  |  |
| 27 | `PPEXR.Country` | `PorExternalrequests_Country` |  |  |  |
| 28 | `PPEXR.PreferredLanguage` | `PorExternalrequests_Preferredlanguage` |  |  |  |
| 29 | `PPEXR.Sector` | `PorExternalrequests_Sector` |  |  |  |
| 30 | `PPEXR.AccountOfficer` | `PorExternalrequests_Accountofficer` |  |  |  |
| 31 | `PPEXR.BusinessLine` | `PorExternalrequests_Businessline` |  |  |  |
| 32 | `PPEXR.Residence` | `PorExternalrequests_Residence` |  |  |  |
| 33 | `PPEXR.EmailID` | `PorExternalrequests_Emailid` |  |  |  |
| 34 | `PPEXR.CustomerPhoneNumber` | `PorExternalrequests_Customerphonenumber` |  |  |  |
| 35 | `PPEXR.BICCode` | `PorExternalrequests_Biccode` |  |  |  |
| 36 | `PPEXR.ReservationAmount` | `PorExternalrequests_Reservationamount` |  |  |  |
| 37 | `PPEXR.ReservationRequestDate` | `PorExternalrequests_Reservationrequestdate` |  |  |  |
| 38 | `PPEXR.TransactionAmount` | `PorExternalrequests_Transactionamount` |  |  |  |
| 39 | `PPEXR.TransactionCurrency` | `PorExternalrequests_Transactioncurrency` |  |  |  |
| 40 | `PPEXR.BookingCode` | `PorExternalrequests_Bookingcode` |  |  |  |
| 41 | `PPEXR.OldReserAccCompany` | `PorExternalrequests_Oldreseracccompany` |  |  |  |
| 42 | `PPEXR.OldReserAccNumber` | `PorExternalrequests_Oldreseraccnumber` |  |  |  |
| 43 | `PPEXR.OldReserAccCurrency` | `PorExternalrequests_Oldreseracccurrency` |  |  |  |
| 44 | `PPEXR.OldReservationReference` | `PorExternalrequests_Oldreservationreference` |  |  |  |
| 45 | `PPEXR.OldReservationDate` | `PorExternalrequests_Oldreservationdate` |  |  |  |
| 46 | `PPEXR.ChannelCutofftime` | `PorExternalrequests_Channelcutofftime` |  |  |  |
| 47 | `PPEXR.ManualAuthorisationFlag` | `PorExternalrequests_Manualauthorisationflag` |  |  |  |
| 48 | `PPEXR.ReservationResponseStatus` | `PorExternalrequests_Reservationresponsestatus` |  |  |  |
| 49 | `PPEXR.ReservationReference` | `PorExternalrequests_Reservationreference` |  |  |  |
| 50 | `PPEXR.ReopenMandateFlag` | `PorExternalrequests_Reopenmandateflag` |  |  |  |
| 51 | `PPEXR.MandateLimitUpdateFlag` | `PorExternalrequests_Mandatelimitupdateflag` |  |  |  |
| 52 | `PPEXR.SettlementDate` | `PorExternalrequests_Settlementdate` |  |  |  |
| 53 | `PPEXR.CancelMandateFlag` | `PorExternalrequests_Cancelmandateflag` |  |  |  |
| 54 | `PPEXR.AmendFlag` | `PorExternalrequests_Amendflag` |  |  |  |
| 55 | `PPEXR.UpdateColDateFlag` | `PorExternalrequests_Updatecoldateflag` |  |  |  |
| 56 | `PPEXR.AutoRegisterFlag` | `PorExternalrequests_Autoregisterflag` |  |  |  |
| 57 | `PPEXR.MandateLimitCheckFlag` | `PorExternalrequests_Mandatelimitcheckflag` |  |  |  |
| 58 | `PPEXR.CreditorRestrictionFlag` | `PorExternalrequests_Creditorrestrictionflag` |  |  |  |
| 59 | `PPEXR.DebtorAccountNumber` | `PorExternalrequests_Debtoraccountnumber` |  |  |  |
| 60 | `PPEXR.DebtorBankBIC` | `PorExternalrequests_Debtorbankbic` |  |  |  |
| 61 | `PPEXR.DebtorBankNCC` | `PorExternalrequests_Debtorbankncc` |  |  |  |
| 62 | `PPEXR.TransactionType` | `PorExternalrequests_Transactiontype` |  |  |  |
| 63 | `PPEXR.MandateAutoRegistered` | `PorExternalrequests_Mandateautoregistered` |  |  |  |
| 64 | `PPEXR.ActionFlag` | `PorExternalrequests_Actionflag` |  |  |  |
| 65 | `PPEXR.ForceFlag` | `PorExternalrequests_Forceflag` |  |  |  |
| 66 | `PPEXR.PostingReferenceIDS` | `PorExternalrequests_Postingreferenceids` |  |  |  |
| 67 | `PPEXR.BankSpecifc` | `PorExternalrequests_Bankspecifc` |  |  |  |
| 68 | `PPEXR.Result` | `PorExternalrequests_Result` |  |  |  |
| 69 | `PPEXR.RejectedReason` | `PorExternalrequests_Rejectedreason` |  |  |  |
| 70 | `PPEXR.InformationalMessages` | `PorExternalrequests_Informationalmessages` |  |  |  |
| 71 | `PPEXR.ErrorCode` | `PorExternalrequests_Errorcode` |  |  |  |
| 72 | `PPEXR.ErrorDescription` | `PorExternalrequests_Errordescription` |  |  |  |
| 73 | `PPEXR.AMLAction` | `PorExternalrequests_Amlaction` |  |  |  |
| 74 | `PPEXR.ManualAuthRequired` | `PorExternalrequests_Manualauthrequired` |  |  |  |
| 75 | `PPEXR.CutOffDate` | `PorExternalrequests_Cutoffdate` |  |  |  |
| 76 | `PPEXR.RESERVED.7` | `PorExternalrequests_Reserved7` | TField |  |  |
| 77 | `PPEXR.RESERVED.6` | `PorExternalrequests_Reserved6` | TField |  |  |
| 78 | `PPEXR.RESERVED.5` | `PorExternalrequests_Reserved5` | TField |  |  |
| 79 | `PPEXR.RESERVED.4` | `PorExternalrequests_Reserved4` | TField |  |  |
| 80 | `PPEXR.RESERVED.3` | `PorExternalrequests_Reserved3` | TField |  |  |
| 81 | `PPEXR.RESERVED.2` | `PorExternalrequests_Reserved2` | TField |  |  |
| 82 | `PPEXR.RESERVED.1` | `PorExternalrequests_Reserved1` | TField |  |  |
| 83 | `PPEXR.LOCAL.REF` | `PorExternalrequests_LocalRef` |  |  |  |
| 84 | `PPEXR.OVERRIDE` | `PorExternalrequests_Override` |  |  |  |
| 85 | `PPEXR.RECORD.STATUS` | `PorExternalrequests_RecordStatus` | String |  |  |
| 86 | `PPEXR.CURR.NO` | `PorExternalrequests_CurrNo` | String |  |  |
| 87 | `PPEXR.INPUTTER` | `PorExternalrequests_Inputter` |  |  |  |
| 88 | `PPEXR.DATE.TIME` | `PorExternalrequests_DateTime` |  |  |  |
| 89 | `PPEXR.AUTHORISER` | `PorExternalrequests_Authoriser` | String |  |  |
| 90 | `PPEXR.CO.CODE` | `PorExternalrequests_CoCode` | String |  |  |
| 91 | `PPEXR.DEPT.CODE` | `PorExternalrequests_DeptCode` | String |  |  |
| 92 | `PPEXR.AUDITOR.CODE` | `PorExternalrequests_AuditorCode` | String |  |  |
| 93 | `PPEXR.AUDIT.DATE.TIME` | `PorExternalrequests_AuditDateTime` | String |  |  |
