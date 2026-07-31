# PP.STANDINGSETTMNTINSTRUC — Table Schema

> Source: `INSERTS/I_F.PP.STANDINGSETTMNTINSTRUC` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.SSI.CompanyID` | `PpStandingsettmntinstruc_Companyid` |  |  |  |
| 2 | `PP.SSI.BankName` | `PpStandingsettmntinstruc_Bankname` |  |  |  |
| 3 | `PP.SSI.City` | `PpStandingsettmntinstruc_City` |  |  |  |
| 4 | `PP.SSI.CurrencyCorrespondentIDType` | `PpStandingsettmntinstruc_Currencycorrespondentidtype` |  |  |  |
| 5 | `PP.SSI.CurrencyCorrespondentID` | `PpStandingsettmntinstruc_Currencycorrespondentid` |  |  |  |
| 6 | `PP.SSI.OverrideThroughUpload` | `PpStandingsettmntinstruc_Overridethroughupload` | TField |  | If this field is �N� then it implies that the data entry will never be updated by the upload process. If set to �Y� then the data can be overridden by the upload process. |
| 7 | `PP.SSI.StartDate` | `PpStandingsettmntinstruc_Startdate` | TField |  | Specifies the date on which the record is to be considered active by the payments hub. |
| 8 | `PP.SSI.EndDate` | `PpStandingsettmntinstruc_Enddate` | TField |  | Specifies the date on which the record is to be considered inactive by the payments hub. |
| 9 | `PP.SSI.RESERVED.5` | `PpStandingsettmntinstruc_Reserved5` | TField |  |  |
| 10 | `PP.SSI.RESERVED.4` | `PpStandingsettmntinstruc_Reserved4` | TField |  |  |
| 11 | `PP.SSI.RESERVED.3` | `PpStandingsettmntinstruc_Reserved3` | TField |  |  |
| 12 | `PP.SSI.RESERVED.2` | `PpStandingsettmntinstruc_Reserved2` | TField |  |  |
| 13 | `PP.SSI.RESERVED.1` | `PpStandingsettmntinstruc_Reserved1` | TField |  |  |
| 14 | `PP.SSI.LOCAL.REF` | `PpStandingsettmntinstruc_LocalRef` |  |  |  |
| 15 | `PP.SSI.OVERRIDE` | `PpStandingsettmntinstruc_Override` |  |  |  |
| 16 | `PP.SSI.RECORD.STATUS` | `PpStandingsettmntinstruc_RecordStatus` | String |  |  |
| 17 | `PP.SSI.CURR.NO` | `PpStandingsettmntinstruc_CurrNo` | String |  |  |
| 18 | `PP.SSI.INPUTTER` | `PpStandingsettmntinstruc_Inputter` |  |  |  |
| 19 | `PP.SSI.DATE.TIME` | `PpStandingsettmntinstruc_DateTime` |  |  |  |
| 20 | `PP.SSI.AUTHORISER` | `PpStandingsettmntinstruc_Authoriser` | String |  |  |
| 21 | `PP.SSI.CO.CODE` | `PpStandingsettmntinstruc_CoCode` | String |  |  |
| 22 | `PP.SSI.DEPT.CODE` | `PpStandingsettmntinstruc_DeptCode` | String |  |  |
| 23 | `PP.SSI.AUDITOR.CODE` | `PpStandingsettmntinstruc_AuditorCode` | String |  |  |
| 24 | `PP.SSI.AUDIT.DATE.TIME` | `PpStandingsettmntinstruc_AuditDateTime` | String |  |  |
| 25 | `PP.SSI.CountryCode` | `PpStandingsettmntinstruc_CountryCode` |  |  |  |
| 26 | `PP.SSI.AssetCategory` | `PpStandingsettmntinstruc_AssetCategory` |  |  |  |
| 27 | `PP.SSI.AccountNumber` | `PpStandingsettmntinstruc_AccountNumber` |  |  |  |
| 28 | `PP.SSI.CountryCodeCorrespondent` | `PpStandingsettmntinstruc_CountryCodeCorrespondent` |  |  |  |
| 29 | `PP.SSI.PreferredFlag` | `PpStandingsettmntinstruc_PreferredFlag` |  |  |  |
| 30 | `PP.SSI.CorrespondentGroup` | `PpStandingsettmntinstruc_CorrespondentGroup` |  |  |  |
| 31 | `PP.SSI.GroupKeyOwner` | `PpStandingsettmntinstruc_GroupKeyOwner` |  |  |  |
| 32 | `PP.SSI.RecordKeyBDPOwner` | `PpStandingsettmntinstruc_RecordKeyBDPOwner` |  |  |  |
| 33 | `PP.SSI.EIDOwner` | `PpStandingsettmntinstruc_EIDOwner` |  |  |  |
| 34 | `PP.SSI.RecordKeyBDPCorrespondent` | `PpStandingsettmntinstruc_RecordKeyBDPCorrespondent` |  |  |  |
| 35 | `PP.SSI.EIDCorrespondent` | `PpStandingsettmntinstruc_EIDCorrespondent` |  |  |  |
