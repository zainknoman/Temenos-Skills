# PP.CONTRACT.PDS — Table Schema

> Source: `INSERTS/I_F.PP.CONTRACT.PDS` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CN.CompanyID` | `PpContractPds_Companyid` | TField |  |  |
| 2 | `PP.CN.StartDate` | `PpContractPds_Startdate` | TField |  |  |
| 3 | `PP.CN.BusinessLine` | `PpContractPds_Businessline` | TField |  |  |
| 4 | `PP.CN.ContractType` | `PpContractPds_Contracttype` | TField |  |  |
| 5 | `PP.CN.RoutingProduct` | `PpContractPds_Routingproduct` | TField |  |  |
| 6 | `PP.CN.PartyIDType` | `PpContractPds_Partyidtype` | TField |  |  |
| 7 | `PP.CN.PartyID` | `PpContractPds_Partyid` | TField |  |  |
| 8 | `PP.CN.Destination` | `PpContractPds_Destination` | TField |  |  |
| 9 | `PP.CN.EndDate` | `PpContractPds_Enddate` | TField |  |  |
| 10 | `PP.CN.Ranking` | `PpContractPds_Ranking` |  |  |  |
| 11 | `PP.CN.SLACode` | `PpContractPds_Slacode` |  |  |  |
| 12 | `PP.CN.Priority` | `PpContractPds_Priority` |  |  |  |
| 13 | `PP.CN.CurrencyCode` | `PpContractPds_Currencycode` |  |  |  |
| 14 | `PP.CN.TransactionLowerLimit` | `PpContractPds_Transactionlowerlimit` |  |  |  |
| 15 | `PP.CN.TransactionUpperLimit` | `PpContractPds_Transactionupperlimit` |  |  |  |
| 16 | `PP.CN.ChargeOption` | `PpContractPds_Chargeoption` |  |  |  |
| 17 | `PP.CN.OptionRanking` | `PpContractPds_Optionranking` |  |  |  |
| 18 | `PP.CN.RSOption` | `PpContractPds_Rsoption` |  |  |  |
| 19 | `PP.CN.RSPartyIDType` | `PpContractPds_Rspartyidtype` |  |  |  |
| 20 | `PP.CN.RSPartyID` | `PpContractPds_Rspartyid` |  |  |  |
| 21 | `PP.CN.AccountCompany` | `PpContractPds_Accountcompany` |  |  |  |
| 22 | `PP.CN.AccountCurrency` | `PpContractPds_Accountcurrency` |  |  |  |
| 23 | `PP.CN.AccountNumber` | `PpContractPds_Accountnumber` |  |  |  |
| 24 | `PP.CN.MessageChannel` | `PpContractPds_Messagechannel` |  |  |  |
| 25 | `PP.CN.CoverIndicator` | `PpContractPds_Coverindicator` |  |  |  |
| 26 | `PP.CN.LeadTime` | `PpContractPds_Leadtime` |  |  |  |
| 27 | `PP.CN.AlternativeForCutoff` | `PpContractPds_Alternativeforcutoff` |  |  |  |
| 28 | `PP.CN.AlternativeForRS` | `PpContractPds_Alternativeforrs` |  |  |  |
| 29 | `PP.CN.AuthoriserDateTime` | `PpContractPds_Authoriserdatetime` | TField |  |  |
| 30 | `PP.CN.RESERVED.5` | `PpContractPds_Reserved5` | TField |  |  |
| 31 | `PP.CN.RESERVED.4` | `PpContractPds_Reserved4` | TField |  |  |
| 32 | `PP.CN.RESERVED.3` | `PpContractPds_Reserved3` | TField |  |  |
| 33 | `PP.CN.RESERVED.2` | `PpContractPds_Reserved2` | TField |  |  |
| 34 | `PP.CN.RESERVED.1` | `PpContractPds_Reserved1` | TField |  |  |
| 35 | `PP.CN.LOCAL.REF` | `PpContractPds_LocalRef` |  |  |  |
| 36 | `PP.CN.LinkID` | `PpContractPds_Linkid` | TField |  |  |
| 37 | `PP.CN.OVERRIDE` | `PpContractPds_Override` |  |  |  |
| 38 | `PP.CN.RECORD.STATUS` | `PpContractPds_RecordStatus` | String |  |  |
| 39 | `PP.CN.CURR.NO` | `PpContractPds_CurrNo` | String |  |  |
| 40 | `PP.CN.INPUTTER` | `PpContractPds_Inputter` |  |  |  |
| 41 | `PP.CN.DATE.TIME` | `PpContractPds_DateTime` |  |  |  |
| 42 | `PP.CN.AUTHORISER` | `PpContractPds_Authoriser` | String |  |  |
| 43 | `PP.CN.CO.CODE` | `PpContractPds_CoCode` | String |  |  |
| 44 | `PP.CN.DEPT.CODE` | `PpContractPds_DeptCode` | String |  |  |
| 45 | `PP.CN.AUDITOR.CODE` | `PpContractPds_AuditorCode` | String |  |  |
| 46 | `PP.CN.AUDIT.DATE.TIME` | `PpContractPds_AuditDateTime` | String |  |  |
