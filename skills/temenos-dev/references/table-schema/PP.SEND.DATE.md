# PP.SEND.DATE — Table Schema

> Source: `INSERTS/I_F.PP.SEND.DATE` in `PP_DateDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.SDT.StartDate` | `PpSendDate_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Autopopulated from the ID upon clicking Validate Button |
| 2 | `PP.SDT.EndDate` | `PpSendDate_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 3 | `PP.SDT.Ranking` | `PpSendDate_Ranking` |  |  |  |
| 4 | `PP.SDT.Channel` | `PpSendDate_Channel` |  |  |  |
| 5 | `PP.SDT.Source` | `PpSendDate_Source` |  |  |  |
| 6 | `PP.SDT.CurrencyGroup` | `PpSendDate_Currencygroup` |  |  |  |
| 7 | `PP.SDT.WarehouseFlag` | `PpSendDate_Warehouseflag` |  |  |  |
| 8 | `PP.SDT.Priority` | `PpSendDate_Priority` |  |  |  |
| 9 | `PP.SDT.CTRBTRIndicator` | `PpSendDate_Ctrbtrindicator` |  |  |  |
| 10 | `PP.SDT.SendDateBase` | `PpSendDate_Senddatebase` |  |  |  |
| 11 | `PP.SDT.SendDateOffset` | `PpSendDate_Senddateoffset` |  |  |  |
| 12 | `PP.SDT.CoverIndicator` | `PpSendDate_Coverindicator` |  |  |  |
| 13 | `PP.SDT.ReleaseOnSystemDate` | `PpSendDate_Releaseonsystemdate` |  |  |  |
| 14 | `PP.SDT.RESERVED.4` | `PpSendDate_Reserved4` | TField |  | Standard T24 field. Reserved for future use |
| 15 | `PP.SDT.RESERVED.3` | `PpSendDate_Reserved3` | TField |  | Standard T24 field. Reserved for future use |
| 16 | `PP.SDT.RESERVED.2` | `PpSendDate_Reserved2` | TField |  | Standard T24 field. Reserved for future use |
| 17 | `PP.SDT.RESERVED.1` | `PpSendDate_Reserved1` | TField |  | Standard T24 field. Reserved for future use |
| 18 | `PP.SDT.LOCAL.REF` | `PpSendDate_LocalRef` |  |  |  |
| 19 | `PP.SDT.OVERRIDE` | `PpSendDate_Override` |  |  |  |
| 20 | `PP.SDT.RECORD.STATUS` | `PpSendDate_RecordStatus` | String |  |  |
| 21 | `PP.SDT.CURR.NO` | `PpSendDate_CurrNo` | String |  |  |
| 22 | `PP.SDT.INPUTTER` | `PpSendDate_Inputter` |  |  |  |
| 23 | `PP.SDT.DATE.TIME` | `PpSendDate_DateTime` |  |  |  |
| 24 | `PP.SDT.AUTHORISER` | `PpSendDate_Authoriser` | String |  |  |
| 25 | `PP.SDT.CO.CODE` | `PpSendDate_CoCode` | String |  |  |
| 26 | `PP.SDT.DEPT.CODE` | `PpSendDate_DeptCode` | String |  |  |
| 27 | `PP.SDT.AUDITOR.CODE` | `PpSendDate_AuditorCode` | String |  |  |
| 28 | `PP.SDT.AUDIT.DATE.TIME` | `PpSendDate_AuditDateTime` | String |  |  |
