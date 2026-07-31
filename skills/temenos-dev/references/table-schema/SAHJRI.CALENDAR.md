# SAHJRI.CALENDAR — Table Schema

> Source: `INSERTS/I_F.SAHJRI.CALENDAR` in `SAHJRI_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HIJ.CAL.START.DATE.GREG` | `SahjriCalendar_StartDateGreg` | TField |  | Gregorian Start date of the Hijri Year |
| 2 | `HIJ.CAL.NO.OF.DAYS.1` | `SahjriCalendar_NoOfDays1` | TField |  | No Of Days in Muharam |
| 3 | `HIJ.CAL.NO.OF.DAYS.2` | `SahjriCalendar_NoOfDays2` | TField |  | No Of Days in Safar |
| 4 | `HIJ.CAL.NO.OF.DAYS.3` | `SahjriCalendar_NoOfDays3` | TField |  | No Of Days in Rabi-ul-Awwal |
| 5 | `HIJ.CAL.NO.OF.DAYS.4` | `SahjriCalendar_NoOfDays4` | TField |  | No of Days in Rabi-ul-Thani |
| 6 | `HIJ.CAL.NO.OF.DAYS.5` | `SahjriCalendar_NoOfDays5` | TField |  | No of Days in Jumada-l-Ula |
| 7 | `HIJ.CAL.NO.OF.DAYS.6` | `SahjriCalendar_NoOfDays6` | TField |  | No of Days in Jumada-th-Thaniyya |
| 8 | `HIJ.CAL.NO.OF.DAYS.7` | `SahjriCalendar_NoOfDays7` | TField |  | No of Days in Rajab (S) |
| 9 | `HIJ.CAL.NO.OF.DAYS.8` | `SahjriCalendar_NoOfDays8` | TField |  | No of Days in Shaaban |
| 10 | `HIJ.CAL.NO.OF.DAYS.9` | `SahjriCalendar_NoOfDays9` | TField |  | No of Days in Ramadhan |
| 11 | `HIJ.CAL.NO.OF.DAYS.10` | `SahjriCalendar_NoOfDays10` | TField |  | NO of Days in Shawwal |
| 12 | `HIJ.CAL.NO.OF.DAYS.11` | `SahjriCalendar_NoOfDays11` | TField |  | NO of Days in Dhul Qadah (S) |
| 13 | `HIJ.CAL.NO.OF.DAYS.12` | `SahjriCalendar_NoOfDays12` | TField |  | NO of Days in Dhul Hijja (S) |
| 14 | `HIJ.CAL.RESERVED.1` | `SahjriCalendar_Reserved1` | TField |  | This field is reserved for future use |
| 15 | `HIJ.CAL.RESERVED.2` | `SahjriCalendar_Reserved2` | TField |  | This field is reserved for future use |
| 16 | `HIJ.CAL.RESERVED.3` | `SahjriCalendar_Reserved3` | TField |  | This field is reserved for future use |
| 17 | `HIJ.CAL.RESERVED.4` | `SahjriCalendar_Reserved4` | TField |  | This field is reserved for future use |
| 18 | `HIJ.CAL.RESERVED.5` | `SahjriCalendar_Reserved5` | TField |  | This field is reserved for future use |
| 19 | `HIJ.CAL.RESERVED.6` | `SahjriCalendar_Reserved6` | TField |  | This field is reserved for future use |
| 20 | `HIJ.CAL.RESERVED.7` | `SahjriCalendar_Reserved7` | TField |  | This field is reserved for future use |
| 21 | `HIJ.CAL.RESERVED.8` | `SahjriCalendar_Reserved8` | TField |  | This field is reserved for future use |
| 22 | `HIJ.CAL.RESERVED.9` | `SahjriCalendar_Reserved9` | TField |  | This field is reserved for future use |
| 23 | `HIJ.CAL.RESERVED.10` | `SahjriCalendar_Reserved10` | TField |  | This field is reserved for future use |
| 24 | `HIJ.CAL.RESERVED.11` | `SahjriCalendar_Reserved11` | TField |  | This field is reserved for future use |
| 25 | `HIJ.CAL.RESERVED.12` | `SahjriCalendar_Reserved12` | TField |  | This field is reserved for future use |
| 26 | `HIJ.CAL.RESERVED.13` | `SahjriCalendar_Reserved13` | TField |  | This field is reserved for future use |
| 27 | `HIJ.CAL.RESERVED.14` | `SahjriCalendar_Reserved14` | TField |  | This field is reserved for future use |
| 28 | `HIJ.CAL.RESERVED.15` | `SahjriCalendar_Reserved15` | TField |  | This field is reserved for future use |
| 29 | `HIJ.CAL.LOCAL.REF` | `SahjriCalendar_LocalRef` |  |  |  |
| 30 | `HIJ.CAL.OVERRIDE` | `SahjriCalendar_Override` |  |  |  |
| 31 | `HIJ.CAL.RECORD.STATUS` | `SahjriCalendar_RecordStatus` | String |  |  |
| 32 | `HIJ.CAL.CURR.NO` | `SahjriCalendar_CurrNo` | String |  |  |
| 33 | `HIJ.CAL.INPUTTER` | `SahjriCalendar_Inputter` |  |  |  |
| 34 | `HIJ.CAL.DATE.TIME` | `SahjriCalendar_DateTime` |  |  |  |
| 35 | `HIJ.CAL.AUTHORISER` | `SahjriCalendar_Authoriser` | String |  |  |
| 36 | `HIJ.CAL.CO.CODE` | `SahjriCalendar_CoCode` | String |  |  |
| 37 | `HIJ.CAL.DEPT.CODE` | `SahjriCalendar_DeptCode` | String |  |  |
| 38 | `HIJ.CAL.AUDITOR.CODE` | `SahjriCalendar_AuditorCode` | String |  |  |
| 39 | `HIJ.CAL.AUDIT.DATE.TIME` | `SahjriCalendar_AuditDateTime` | String |  |  |
