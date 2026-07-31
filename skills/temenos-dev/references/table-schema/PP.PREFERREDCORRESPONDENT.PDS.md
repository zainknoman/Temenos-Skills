# PP.PREFERREDCORRESPONDENT.PDS — Table Schema

> Source: `INSERTS/I_F.PP.PREFERREDCORRESPONDENT.PDS` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.PCT.CompanyID` | `PpPreferredcorrespondentPds_Companyid` | TField |  |  |
| 2 | `PP.PCT.DestinationCountryCode` | `PpPreferredcorrespondentPds_Destinationcountrycode` | TField |  |  |
| 3 | `PP.PCT.TransactionCurrency` | `PpPreferredcorrespondentPds_Transactioncurrency` | TField |  |  |
| 4 | `PP.PCT.RoutingProduct` | `PpPreferredcorrespondentPds_Routingproduct` | TField |  |  |
| 5 | `PP.PCT.StartDate` | `PpPreferredcorrespondentPds_Startdate` | TField |  |  |
| 6 | `PP.PCT.PrefCorrespondentIDType` | `PpPreferredcorrespondentPds_Prefcorrespondentidtype` | TField |  |  |
| 7 | `PP.PCT.PrefCorrespondentID` | `PpPreferredcorrespondentPds_Prefcorrespondentid` | TField |  |  |
| 8 | `PP.PCT.EndDate` | `PpPreferredcorrespondentPds_Enddate` | TField |  |  |
| 9 | `PP.PCT.RESERVED.5` | `PpPreferredcorrespondentPds_Reserved5` | TField |  |  |
| 10 | `PP.PCT.RESERVED.4` | `PpPreferredcorrespondentPds_Reserved4` | TField |  |  |
| 11 | `PP.PCT.RESERVED.3` | `PpPreferredcorrespondentPds_Reserved3` | TField |  |  |
| 12 | `PP.PCT.RESERVED.2` | `PpPreferredcorrespondentPds_Reserved2` | TField |  |  |
| 13 | `PP.PCT.RESERVED.1` | `PpPreferredcorrespondentPds_Reserved1` | TField |  |  |
| 14 | `PP.PCT.DefineQuota` | `PpPreferredcorrespondentPds_Definequota` | TField |  |  |
| 15 | `PP.PCT.CorrespondentIDType` | `PpPreferredcorrespondentPds_Correspondentidtype` |  |  |  |
| 16 | `PP.PCT.CorrespondentID` | `PpPreferredcorrespondentPds_Correspondentid` |  |  |  |
| 17 | `PP.PCT.MessageType` | `PpPreferredcorrespondentPds_Messagetype` |  |  |  |
| 18 | `PP.PCT.PercentageAllotted` | `PpPreferredcorrespondentPds_Percentageallotted` |  |  |  |
| 19 | `PP.PCT.CountAllotted` | `PpPreferredcorrespondentPds_Countallotted` |  |  |  |
| 20 | `PP.PCT.CountPriority` | `PpPreferredcorrespondentPds_Countpriority` |  |  |  |
| 21 | `PP.PCT.AmountFrom` | `PpPreferredcorrespondentPds_Amountfrom` |  |  |  |
| 22 | `PP.PCT.AmountTo` | `PpPreferredcorrespondentPds_Amountto` |  |  |  |
| 23 | `PP.PCT.QuotaAPI` | `PpPreferredcorrespondentPds_Quotaapi` | TField |  |  |
| 24 | `PP.PCT.ResetFrequency` | `PpPreferredcorrespondentPds_Resetfrequency` | TField |  |  |
| 25 | `PP.PCT.LOCAL.REF` | `PpPreferredcorrespondentPds_LocalRef` |  |  |  |
| 26 | `PP.PCT.LinkID` | `PpPreferredcorrespondentPds_Linkid` | TField |  |  |
| 27 | `PP.PCT.OVERRIDE` | `PpPreferredcorrespondentPds_Override` |  |  |  |
| 28 | `PP.PCT.RECORD.STATUS` | `PpPreferredcorrespondentPds_RecordStatus` | String |  |  |
| 29 | `PP.PCT.CURR.NO` | `PpPreferredcorrespondentPds_CurrNo` | String |  |  |
| 30 | `PP.PCT.INPUTTER` | `PpPreferredcorrespondentPds_Inputter` |  |  |  |
| 31 | `PP.PCT.DATE.TIME` | `PpPreferredcorrespondentPds_DateTime` |  |  |  |
| 32 | `PP.PCT.AUTHORISER` | `PpPreferredcorrespondentPds_Authoriser` | String |  |  |
| 33 | `PP.PCT.CO.CODE` | `PpPreferredcorrespondentPds_CoCode` | String |  |  |
| 34 | `PP.PCT.DEPT.CODE` | `PpPreferredcorrespondentPds_DeptCode` | String |  |  |
| 35 | `PP.PCT.AUDITOR.CODE` | `PpPreferredcorrespondentPds_AuditorCode` | String |  |  |
| 36 | `PP.PCT.AUDIT.DATE.TIME` | `PpPreferredcorrespondentPds_AuditDateTime` | String |  |  |
