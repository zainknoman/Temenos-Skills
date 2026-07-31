# PP.LORO.NOSTRO.ACCOUNT.PDS — Table Schema

> Source: `INSERTS/I_F.PP.LORO.NOSTRO.ACCOUNT.PDS` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.LNA.CompanyID` | `PpLoroNostroAccountPds_Companyid` | TField |  |  |
| 2 | `PP.LNA.BICCode` | `PpLoroNostroAccountPds_Biccode` | TField |  |  |
| 3 | `PP.LNA.AccountNumberType` | `PpLoroNostroAccountPds_Accountnumbertype` | TField |  |  |
| 4 | `PP.LNA.AccountCurrency` | `PpLoroNostroAccountPds_Accountcurrency` | TField |  |  |
| 5 | `PP.LNA.StartDate` | `PpLoroNostroAccountPds_Startdate` | TField |  |  |
| 6 | `PP.LNA.EndDate` | `PpLoroNostroAccountPds_Enddate` | TField |  |  |
| 7 | `PP.LNA.AccountNumberCompanyID` | `PpLoroNostroAccountPds_Accountnumbercompanyid` |  |  |  |
| 8 | `PP.LNA.AccountNumber` | `PpLoroNostroAccountPds_Accountnumber` |  |  |  |
| 9 | `PP.LNA.OwningBIC` | `PpLoroNostroAccountPds_Owningbic` |  |  |  |
| 10 | `PP.LNA.PreferredDebitAccountNumber` | `PpLoroNostroAccountPds_Preferreddebitaccountnumber` |  |  |  |
| 11 | `PP.LNA.PreferredCreditAcctNumber` | `PpLoroNostroAccountPds_Preferredcreditacctnumber` |  |  |  |
| 12 | `PP.LNA.ChargesIndicator` | `PpLoroNostroAccountPds_Chargesindicator` |  |  |  |
| 13 | `PP.LNA.AccountNumberInHoldingBk` | `PpLoroNostroAccountPds_Accountnumberinholdingbk` |  |  |  |
| 14 | `PP.LNA.AccountShortName` | `PpLoroNostroAccountPds_Accountshortname` |  |  |  |
| 15 | `PP.LNA.DraftAccount` | `PpLoroNostroAccountPds_Draftaccount` |  |  |  |
| 16 | `PP.LNA.RESERVED.4` | `PpLoroNostroAccountPds_Reserved4` |  |  |  |
| 17 | `PP.LNA.RESERVED.3` | `PpLoroNostroAccountPds_Reserved3` |  |  |  |
| 18 | `PP.LNA.RESERVED.2` | `PpLoroNostroAccountPds_Reserved2` | TField |  |  |
| 19 | `PP.LNA.RESERVED.1` | `PpLoroNostroAccountPds_Reserved1` | TField |  |  |
| 20 | `PP.LNA.LOCAL.REF` | `PpLoroNostroAccountPds_LocalRef` |  |  |  |
| 21 | `PP.LNA.LinkID` | `PpLoroNostroAccountPds_Linkid` | TField |  |  |
| 22 | `PP.LNA.OVERRIDE` | `PpLoroNostroAccountPds_Override` |  |  |  |
| 23 | `PP.LNA.RECORD.STATUS` | `PpLoroNostroAccountPds_RecordStatus` | String |  |  |
| 24 | `PP.LNA.CURR.NO` | `PpLoroNostroAccountPds_CurrNo` | String |  |  |
| 25 | `PP.LNA.INPUTTER` | `PpLoroNostroAccountPds_Inputter` |  |  |  |
| 26 | `PP.LNA.DATE.TIME` | `PpLoroNostroAccountPds_DateTime` |  |  |  |
| 27 | `PP.LNA.AUTHORISER` | `PpLoroNostroAccountPds_Authoriser` | String |  |  |
| 28 | `PP.LNA.CO.CODE` | `PpLoroNostroAccountPds_CoCode` | String |  |  |
| 29 | `PP.LNA.DEPT.CODE` | `PpLoroNostroAccountPds_DeptCode` | String |  |  |
| 30 | `PP.LNA.AUDITOR.CODE` | `PpLoroNostroAccountPds_AuditorCode` | String |  |  |
| 31 | `PP.LNA.AUDIT.DATE.TIME` | `PpLoroNostroAccountPds_AuditDateTime` | String |  |  |
