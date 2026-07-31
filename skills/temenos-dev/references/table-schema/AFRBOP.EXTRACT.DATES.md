# AFRBOP.EXTRACT.DATES — Table Schema

> Source: `INSERTS/I_F.AFRBOP.EXTRACT.DATES` in `AFRBOP_BalanceOfPayment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AFRBOP.DATES.START.DATE` | `AfrbopExtractDates_StartDate` | TField |  | Specifies the start date of the extraction period |
| 2 | `AFRBOP.DATES.END.DATE` | `AfrbopExtractDates_EndDate` | TField |  | Specifies the End date of the extraction period. |
| 3 | `AFRBOP.DATES.PREVIOUS.RUN.START` | `AfrbopExtractDates_PreviousRunStart` |  |  |  |
| 4 | `AFRBOP.DATES.PREVIOUS.RUN.END` | `AfrbopExtractDates_PreviousRunEnd` |  |  |  |
| 5 | `AFRBOP.DATES.LOCAL.REF` | `AfrbopExtractDates_LocalRef` |  |  |  |
| 6 | `AFRBOP.DATES.RESERVED.5` | `AfrbopExtractDates_Reserved5` | TField |  | This field is reserved for future use |
| 7 | `AFRBOP.DATES.RESERVED.4` | `AfrbopExtractDates_Reserved4` | TField |  | This field is reserved for future use |
| 8 | `AFRBOP.DATES.RESERVED.3` | `AfrbopExtractDates_Reserved3` | TField |  | This field is reserved for future use |
| 9 | `AFRBOP.DATES.RESERVED.2` | `AfrbopExtractDates_Reserved2` | TField |  | This field is reserved for future use |
| 10 | `AFRBOP.DATES.RESERVED.1` | `AfrbopExtractDates_Reserved1` | TField |  | This field is reserved for future use |
| 11 | `AFRBOP.DATES.OVERRIDE` | `AfrbopExtractDates_Override` |  |  |  |
| 12 | `AFRBOP.DATES.RECORD.STATUS` | `AfrbopExtractDates_RecordStatus` | String |  |  |
| 13 | `AFRBOP.DATES.CURR.NO` | `AfrbopExtractDates_CurrNo` | String |  |  |
| 14 | `AFRBOP.DATES.INPUTTER` | `AfrbopExtractDates_Inputter` |  |  |  |
| 15 | `AFRBOP.DATES.DATE.TIME` | `AfrbopExtractDates_DateTime` |  |  |  |
| 16 | `AFRBOP.DATES.AUTHORISER` | `AfrbopExtractDates_Authoriser` | String |  |  |
| 17 | `AFRBOP.DATES.CO.CODE` | `AfrbopExtractDates_CoCode` | String |  |  |
| 18 | `AFRBOP.DATES.DEPT.CODE` | `AfrbopExtractDates_DeptCode` | String |  |  |
| 19 | `AFRBOP.DATES.AUDITOR.CODE` | `AfrbopExtractDates_AuditorCode` | String |  |  |
| 20 | `AFRBOP.DATES.AUDIT.DATE.TIME` | `AfrbopExtractDates_AuditDateTime` | String |  |  |
