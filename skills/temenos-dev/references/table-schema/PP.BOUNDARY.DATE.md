# PP.BOUNDARY.DATE — Table Schema

> Source: `INSERTS/I_F.PP.BOUNDARY.DATE` in `PP_DateDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.BOD.StartDate` | `PpBoundaryDate_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Autopopulated from the ID upon clicking Validate Button |
| 2 | `PP.BOD.EndDate` | `PpBoundaryDate_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 3 | `PP.BOD.Ranking` | `PpBoundaryDate_Ranking` |  |  |  |
| 4 | `PP.BOD.DateType` | `PpBoundaryDate_Datetype` |  |  |  |
| 5 | `PP.BOD.DueDateRelation` | `PpBoundaryDate_Duedaterelation` |  |  |  |
| 6 | `PP.BOD.BookDateRelation` | `PpBoundaryDate_Bookdaterelation` |  |  |  |
| 7 | `PP.BOD.CVDDateRelation` | `PpBoundaryDate_Cvddaterelation` |  |  |  |
| 8 | `PP.BOD.DVDDateRelation` | `PpBoundaryDate_Dvddaterelation` |  |  |  |
| 9 | `PP.BOD.PSDDateRelation` | `PpBoundaryDate_Psddaterelation` |  |  |  |
| 10 | `PP.BOD.CSDDateRelation` | `PpBoundaryDate_Csddaterelation` |  |  |  |
| 11 | `PP.BOD.PastAllowedDays` | `PpBoundaryDate_Pastalloweddays` |  |  |  |
| 12 | `PP.BOD.FutureAllowedDays` | `PpBoundaryDate_Futurealloweddays` |  |  |  |
| 13 | `PP.BOD.RESERVED.5` | `PpBoundaryDate_Reserved5` | TField |  | Standard T24 field. Reserved for future use |
| 14 | `PP.BOD.RESERVED.4` | `PpBoundaryDate_Reserved4` | TField |  | Standard T24 field. Reserved for future use |
| 15 | `PP.BOD.RESERVED.3` | `PpBoundaryDate_Reserved3` | TField |  | Standard T24 field. Reserved for future use |
| 16 | `PP.BOD.RESERVED.2` | `PpBoundaryDate_Reserved2` | TField |  | Standard T24 field. Reserved for future use |
| 17 | `PP.BOD.RESERVED.1` | `PpBoundaryDate_Reserved1` | TField |  | Standard T24 field. Reserved for future use |
| 18 | `PP.BOD.LOCAL.REF` | `PpBoundaryDate_LocalRef` |  |  |  |
| 19 | `PP.BOD.OVERRIDE` | `PpBoundaryDate_Override` |  |  |  |
| 20 | `PP.BOD.RECORD.STATUS` | `PpBoundaryDate_RecordStatus` | String |  |  |
| 21 | `PP.BOD.CURR.NO` | `PpBoundaryDate_CurrNo` | String |  |  |
| 22 | `PP.BOD.INPUTTER` | `PpBoundaryDate_Inputter` |  |  |  |
| 23 | `PP.BOD.DATE.TIME` | `PpBoundaryDate_DateTime` |  |  |  |
| 24 | `PP.BOD.AUTHORISER` | `PpBoundaryDate_Authoriser` | String |  |  |
| 25 | `PP.BOD.CO.CODE` | `PpBoundaryDate_CoCode` | String |  |  |
| 26 | `PP.BOD.DEPT.CODE` | `PpBoundaryDate_DeptCode` | String |  |  |
| 27 | `PP.BOD.AUDITOR.CODE` | `PpBoundaryDate_AuditorCode` | String |  |  |
| 28 | `PP.BOD.AUDIT.DATE.TIME` | `PpBoundaryDate_AuditDateTime` | String |  |  |
