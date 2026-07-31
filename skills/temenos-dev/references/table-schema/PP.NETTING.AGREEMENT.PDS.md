# PP.NETTING.AGREEMENT.PDS — Table Schema

> Source: `INSERTS/I_F.PP.NETTING.AGREEMENT.PDS` in `PP_DebitAuthorityService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.NTA.CompanyID` | `PpNettingAgreementPds_Companyid` | TField |  |  |
| 2 | `PP.NTA.IncomingMessageType` | `PpNettingAgreementPds_Incomingmessagetype` | TField |  |  |
| 3 | `PP.NTA.SendingBank` | `PpNettingAgreementPds_Sendingbank` | TField |  |  |
| 4 | `PP.NTA.DebitAccountLine` | `PpNettingAgreementPds_Debitaccountline` | TField |  |  |
| 5 | `PP.NTA.DebitPartyLine1` | `PpNettingAgreementPds_Debitpartyline1` | TField |  |  |
| 6 | `PP.NTA.StartDate` | `PpNettingAgreementPds_Startdate` | TField |  |  |
| 7 | `PP.NTA.EndDate` | `PpNettingAgreementPds_Enddate` | TField |  |  |
| 8 | `PP.NTA.SUBMITTER.ID` | `PpNettingAgreementPds_SubmitterId` | TField |  |  |
| 9 | `PP.NTA.SERVICE.TYPE` | `PpNettingAgreementPds_ServiceType` |  |  |  |
| 10 | `PP.NTA.BatchBooking` | `PpNettingAgreementPds_Batchbooking` | TField |  |  |
| 11 | `PP.NTA.CustStatusRptOnSettlement` | `PpNettingAgreementPds_Custstatusrptonsettlement` | TField |  |  |
| 12 | `PP.NTA.CustomerStatusReportRejects` | `PpNettingAgreementPds_Customerstatusreportrejects` | TField |  |  |
| 13 | `PP.NTA.LOCAL.REF` | `PpNettingAgreementPds_LocalRef` |  |  |  |
| 14 | `PP.NTA.LinkID` | `PpNettingAgreementPds_Linkid` | TField |  |  |
| 15 | `PP.NTA.OVERRIDE` | `PpNettingAgreementPds_Override` |  |  |  |
| 16 | `PP.NTA.RECORD.STATUS` | `PpNettingAgreementPds_RecordStatus` | String |  |  |
| 17 | `PP.NTA.CURR.NO` | `PpNettingAgreementPds_CurrNo` | String |  |  |
| 18 | `PP.NTA.INPUTTER` | `PpNettingAgreementPds_Inputter` |  |  |  |
| 19 | `PP.NTA.DATE.TIME` | `PpNettingAgreementPds_DateTime` |  |  |  |
| 20 | `PP.NTA.AUTHORISER` | `PpNettingAgreementPds_Authoriser` | String |  |  |
| 21 | `PP.NTA.CO.CODE` | `PpNettingAgreementPds_CoCode` | String |  |  |
| 22 | `PP.NTA.DEPT.CODE` | `PpNettingAgreementPds_DeptCode` | String |  |  |
| 23 | `PP.NTA.AUDITOR.CODE` | `PpNettingAgreementPds_AuditorCode` | String |  |  |
| 24 | `PP.NTA.AUDIT.DATE.TIME` | `PpNettingAgreementPds_AuditDateTime` | String |  |  |
| 25 | `PP.NTA.CustomerStatusReportReturns` | `PpNettingAgreementPds_Customerstatusreportreturns` | TField |  |  |
| 26 | `PP.NTA.StatusReportMessageType` | `PpNettingAgreementPds_Statusreportmessagetype` | TField |  |  |
| 27 | `PP.NTA.FileACKMessageType` | `PpNettingAgreementPds_Fileackmessagetype` | TField |  |  |
| 28 | `PP.NTA.FileACKRequired` | `PpNettingAgreementPds_Fileackrequired` | TField |  |  |
| 29 | `PP.NTA.BulkCurrency` | `PpNettingAgreementPds_Bulkcurrency` | TField |  |  |
| 30 | `PP.NTA.DaysInPastAllowed` | `PpNettingAgreementPds_Daysinpastallowed` | TField |  |  |
| 31 | `PP.NTA.ConsolidateRejects` | `PpNettingAgreementPds_Consolidaterejects` | TField |  |  |
| 32 | `PP.NTA.MaxAllowedDaysForReversal` | `PpNettingAgreementPds_Maxalloweddaysforreversal` | TField |  |  |
| 33 | `PP.NTA.CollectionRetryDays` | `PpNettingAgreementPds_Collectionretrydays` | TField |  |  |
| 34 | `PP.NTA.MaxReturnDaysBookDD` | `PpNettingAgreementPds_Maxreturndaysbookdd` | TField |  |  |
| 35 | `PP.NTA.MaxRefundDaysBookDDAuth` | `PpNettingAgreementPds_Maxrefunddaysbookddauth` | TField |  |  |
| 36 | `PP.NTA.MaxRefundDaysBookDDUnauth` | `PpNettingAgreementPds_Maxrefunddaysbookddunauth` | TField |  |  |
