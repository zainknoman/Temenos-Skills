# PP.NODA.LIST — Table Schema

> Source: `INSERTS/I_F.PP.NODA.LIST` in `PP_DebitAuthorityService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.NOD.CompanyID` | `PpNodaList_Companyid` | TField |  | This is a No-Input field which gets Auto-Populated on Clicking Validate button Example : BNK,GB1 |
| 2 | `PP.NOD.StartDate` | `PpNodaList_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Autopopulated from the ID upon clicking Validate Button |
| 3 | `PP.NOD.EndDate` | `PpNodaList_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 4 | `PP.NOD.LinkID` | `PpNodaList_Linkid` | TField |  | Its a No-Input field Value is populated by concatenating all the Primary Keys |
| 5 | `PP.NOD.RESERVED.5` | `PpNodaList_Reserved5` | TField |  | Standard T24 field. Reserved for future use |
| 6 | `PP.NOD.RESERVED.4` | `PpNodaList_Reserved4` | TField |  | Standard T24 field. Reserved for future use |
| 7 | `PP.NOD.RESERVED.3` | `PpNodaList_Reserved3` | TField |  | Standard T24 field. Reserved for future use |
| 8 | `PP.NOD.RESERVED.2` | `PpNodaList_Reserved2` | TField |  | Standard T24 field. Reserved for future use |
| 9 | `PP.NOD.RESERVED.1` | `PpNodaList_Reserved1` | TField |  | Standard T24 field. Reserved for future use |
| 10 | `PP.NOD.LOCAL.REF` | `PpNodaList_LocalRef` |  |  |  |
| 11 | `PP.NOD.OVERRIDE` | `PpNodaList_Override` |  |  |  |
| 12 | `PP.NOD.RECORD.STATUS` | `PpNodaList_RecordStatus` | String |  |  |
| 13 | `PP.NOD.CURR.NO` | `PpNodaList_CurrNo` | String |  |  |
| 14 | `PP.NOD.INPUTTER` | `PpNodaList_Inputter` |  |  |  |
| 15 | `PP.NOD.DATE.TIME` | `PpNodaList_DateTime` |  |  |  |
| 16 | `PP.NOD.AUTHORISER` | `PpNodaList_Authoriser` | String |  |  |
| 17 | `PP.NOD.CO.CODE` | `PpNodaList_CoCode` | String |  |  |
| 18 | `PP.NOD.DEPT.CODE` | `PpNodaList_DeptCode` | String |  |  |
| 19 | `PP.NOD.AUDITOR.CODE` | `PpNodaList_AuditorCode` | String |  |  |
| 20 | `PP.NOD.AUDIT.DATE.TIME` | `PpNodaList_AuditDateTime` | String |  |  |
