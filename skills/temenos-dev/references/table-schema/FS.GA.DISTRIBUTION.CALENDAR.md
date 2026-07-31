# FS.GA.DISTRIBUTION.CALENDAR — Table Schema

> Source: `INSERTS/I_F.FS.GA.DISTRIBUTION.CALENDAR` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.DISTRIBUTION.CALENDAR.DISTRIBUTION.CALENDAR` | `FsGaDistributionCalendar_DistributionCalendar` | TField |  | Distribution Calendar Multifonds DB Column is DIST_CAL. |
| 2 | `FS.GA.DISTRIBUTION.CALENDAR.EVENT.START.DATE` | `FsGaDistributionCalendar_EventStartDate` | TField |  | Start date of the event ex. Start date of distribution Multifonds DB Column is START_DATE. |
| 3 | `FS.GA.DISTRIBUTION.CALENDAR.END.DATE` | `FsGaDistributionCalendar_EndDate` | TField |  | This field is used for the calculation of management expense ratio (MER) at the share class level. It refers to the date upto which a share class is in existence for MER reporting. Multifonds DB Column is END_DATE. |
| 4 | `FS.GA.DISTRIBUTION.CALENDAR.PAYMENT.DATE` | `FsGaDistributionCalendar_PaymentDate` | TField |  | Payment date of the event ex. Payment date of distribution Multifonds DB Column is PAY_DATE. |
| 5 | `FS.GA.DISTRIBUTION.CALENDAR.RECORD.STATUS` | `FsGaDistributionCalendar_RecordStatus` | String |  |  |
| 6 | `FS.GA.DISTRIBUTION.CALENDAR.CURR.NO` | `FsGaDistributionCalendar_CurrNo` | String |  |  |
| 7 | `FS.GA.DISTRIBUTION.CALENDAR.INPUTTER` | `FsGaDistributionCalendar_Inputter` |  |  |  |
| 8 | `FS.GA.DISTRIBUTION.CALENDAR.DATE.TIME` | `FsGaDistributionCalendar_DateTime` |  |  |  |
| 9 | `FS.GA.DISTRIBUTION.CALENDAR.AUTHORISER` | `FsGaDistributionCalendar_Authoriser` | String |  |  |
| 10 | `FS.GA.DISTRIBUTION.CALENDAR.CO.CODE` | `FsGaDistributionCalendar_CoCode` | String |  |  |
| 11 | `FS.GA.DISTRIBUTION.CALENDAR.DEPT.CODE` | `FsGaDistributionCalendar_DeptCode` | String |  |  |
| 12 | `FS.GA.DISTRIBUTION.CALENDAR.AUDITOR.CODE` | `FsGaDistributionCalendar_AuditorCode` | String |  |  |
| 13 | `FS.GA.DISTRIBUTION.CALENDAR.AUDIT.DATE.TIME` | `FsGaDistributionCalendar_AuditDateTime` | String |  |  |
