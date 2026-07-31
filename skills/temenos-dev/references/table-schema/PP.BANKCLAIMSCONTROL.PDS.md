# PP.BANKCLAIMSCONTROL.PDS — Table Schema

> Source: `INSERTS/I_F.PP.BANKCLAIMSCONTROL.PDS` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.BCL.CompanyID` | `PpBankclaimscontrolPds_Companyid` |  |  |  |
| 2 | `PP.BCL.CorrespondentBIC` | `PpBankclaimscontrolPds_Correspondentbic` |  |  |  |
| 3 | `PP.BCL.CurrencyCode` | `PpBankclaimscontrolPds_Currencycode` |  |  |  |
| 4 | `PP.BCL.ClaimType` | `PpBankclaimscontrolPds_Claimtype` |  |  |  |
| 5 | `PP.BCL.ClaimTowards` | `PpBankclaimscontrolPds_Claimtowards` |  |  |  |
| 6 | `PP.BCL.ClaimBIC` | `PpBankclaimscontrolPds_Claimbic` |  |  |  |
| 7 | `PP.BCL.ClaimBasis` | `PpBankclaimscontrolPds_Claimbasis` |  |  |  |
| 8 | `PP.BCL.ClaimPeriod` | `PpBankclaimscontrolPds_Claimperiod` |  |  |  |
| 9 | `PP.BCL.ClaimTrigger` | `PpBankclaimscontrolPds_Claimtrigger` |  |  |  |
| 10 | `PP.BCL.IndividualGroupIndicator` | `PpBankclaimscontrolPds_Individualgroupindicator` |  |  |  |
| 11 | `PP.BCL.StartDate` | `PpBankclaimscontrolPds_Startdate` |  |  |  |
| 12 | `PP.BCL.EndDate` | `PpBankclaimscontrolPds_Enddate` |  |  |  |
| 13 | `PP.BCL.RESERVED.5` | `PpBankclaimscontrolPds_Reserved5` |  |  |  |
| 14 | `PP.BCL.RESERVED.4` | `PpBankclaimscontrolPds_Reserved4` |  |  |  |
| 15 | `PP.BCL.RESERVED.3` | `PpBankclaimscontrolPds_Reserved3` |  |  |  |
| 16 | `PP.BCL.RESERVED.2` | `PpBankclaimscontrolPds_Reserved2` |  |  |  |
| 17 | `PP.BCL.RESERVED.1` | `PpBankclaimscontrolPds_Reserved1` |  |  |  |
| 18 | `PP.BCL.LOCAL.REF` | `PpBankclaimscontrolPds_LocalRef` |  |  |  |
| 19 | `PP.BCL.LinkID` | `PpBankclaimscontrolPds_Linkid` |  |  |  |
| 20 | `PP.BCL.OVERRIDE` | `PpBankclaimscontrolPds_Override` |  |  |  |
| 21 | `PP.BCL.RECORD.STATUS` | `PpBankclaimscontrolPds_RecordStatus` |  |  |  |
| 22 | `PP.BCL.CURR.NO` | `PpBankclaimscontrolPds_CurrNo` |  |  |  |
| 23 | `PP.BCL.INPUTTER` | `PpBankclaimscontrolPds_Inputter` |  |  |  |
| 24 | `PP.BCL.DATE.TIME` | `PpBankclaimscontrolPds_DateTime` |  |  |  |
| 25 | `PP.BCL.AUTHORISER` | `PpBankclaimscontrolPds_Authoriser` |  |  |  |
| 26 | `PP.BCL.CO.CODE` | `PpBankclaimscontrolPds_CoCode` |  |  |  |
| 27 | `PP.BCL.DEPT.CODE` | `PpBankclaimscontrolPds_DeptCode` |  |  |  |
| 28 | `PP.BCL.AUDITOR.CODE` | `PpBankclaimscontrolPds_AuditorCode` |  |  |  |
| 29 | `PP.BCL.AUDIT.DATE.TIME` | `PpBankclaimscontrolPds_AuditDateTime` |  |  |  |
