# PP.EXPOSURE.DATE — Table Schema

> Source: `INSERTS/I_F.PP.EXPOSURE.DATE` in `PP_DateDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.EXD.StartDate` | `PpExposureDate_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Autopopulated from the ID upon clicking Validate Button |
| 2 | `PP.EXD.EndDate` | `PpExposureDate_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 3 | `PP.EXD.Ranking` | `PpExposureDate_Ranking` |  |  |  |
| 4 | `PP.EXD.ProductCode` | `PpExposureDate_Productcode` |  |  |  |
| 5 | `PP.EXD.ExposureDateBase` | `PpExposureDate_Exposuredatebase` |  |  |  |
| 6 | `PP.EXD.OffsetDays` | `PpExposureDate_Offsetdays` |  |  |  |
| 7 | `PP.EXD.RESERVED.5` | `PpExposureDate_Reserved5` | TField |  | Standard T24 field. Reserved for future use |
| 8 | `PP.EXD.RESERVED.4` | `PpExposureDate_Reserved4` | TField |  | Standard T24 field. Reserved for future use |
| 9 | `PP.EXD.RESERVED.3` | `PpExposureDate_Reserved3` | TField |  | Standard T24 field. Reserved for future use |
| 10 | `PP.EXD.RESERVED.2` | `PpExposureDate_Reserved2` | TField |  | Standard T24 field. Reserved for future use |
| 11 | `PP.EXD.RESERVED.1` | `PpExposureDate_Reserved1` | TField |  | Standard T24 field. Reserved for future use |
| 12 | `PP.EXD.LOCAL.REF` | `PpExposureDate_LocalRef` |  |  |  |
| 13 | `PP.EXD.OVERRIDE` | `PpExposureDate_Override` |  |  |  |
| 14 | `PP.EXD.RECORD.STATUS` | `PpExposureDate_RecordStatus` | String |  |  |
| 15 | `PP.EXD.CURR.NO` | `PpExposureDate_CurrNo` | String |  |  |
| 16 | `PP.EXD.INPUTTER` | `PpExposureDate_Inputter` |  |  |  |
| 17 | `PP.EXD.DATE.TIME` | `PpExposureDate_DateTime` |  |  |  |
| 18 | `PP.EXD.AUTHORISER` | `PpExposureDate_Authoriser` | String |  |  |
| 19 | `PP.EXD.CO.CODE` | `PpExposureDate_CoCode` | String |  |  |
| 20 | `PP.EXD.DEPT.CODE` | `PpExposureDate_DeptCode` | String |  |  |
| 21 | `PP.EXD.AUDITOR.CODE` | `PpExposureDate_AuditorCode` | String |  |  |
| 22 | `PP.EXD.AUDIT.DATE.TIME` | `PpExposureDate_AuditDateTime` | String |  |  |
