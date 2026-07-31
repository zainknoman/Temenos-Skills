# SFCONF.TRACKER.STATUS.REASON — Table Schema

> Source: `INSERTS/I_F.SFCONF.TRACKER.STATUS.REASON` in `SFCONF_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SFTR.DESCRIPTION` | `SfconfTrackerStatusReason_Description` | TField |  | Description of status and Reason code |
| 2 | `SFTR.TRACKER.STATUS` | `SfconfTrackerStatusReason_TrackerStatus` | TField | No | Confirmation tracker status corresponding to this status and reason code Validation Rules: Optional Field.Allowed Values are: SETTLED, TRANSFERRED, PENDING, REJECTED, NULL |
| 3 | `SFTR.STATUS.CODE` | `SfconfTrackerStatusReason_StatusCode` | TField |  | Status code to be sent in 199 message |
| 4 | `SFTR.REASON.CODE` | `SfconfTrackerStatusReason_ReasonCode` | TField |  | Reason code to be sent in 199 message |
| 5 | `SFTR.CONF.AMT.CCY` | `SfconfTrackerStatusReason_ConfAmtCcy` | TField |  | Indicates if Confirmed Amount and Currency must e captured for this Status Reason Code |
| 6 | `SFTR.RESERVED.10` | `SfconfTrackerStatusReason_Reserved10` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 7 | `SFTR.RESERVED.9` | `SfconfTrackerStatusReason_Reserved9` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 8 | `SFTR.RESERVED.8` | `SfconfTrackerStatusReason_Reserved8` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 9 | `SFTR.RESERVED.7` | `SfconfTrackerStatusReason_Reserved7` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 10 | `SFTR.RESERVED.6` | `SfconfTrackerStatusReason_Reserved6` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 11 | `SFTR.LOCAL.REF` | `SfconfTrackerStatusReason_LocalRef` |  |  |  |
| 12 | `SFTR.OVERRIDE` | `SfconfTrackerStatusReason_Override` |  |  |  |
| 13 | `SFTR.RECORD.STATUS` | `SfconfTrackerStatusReason_RecordStatus` | String |  |  |
| 14 | `SFTR.CURR.NO` | `SfconfTrackerStatusReason_CurrNo` | String |  |  |
| 15 | `SFTR.INPUTTER` | `SfconfTrackerStatusReason_Inputter` |  |  |  |
| 16 | `SFTR.DATE.TIME` | `SfconfTrackerStatusReason_DateTime` |  |  |  |
| 17 | `SFTR.AUTHORISER` | `SfconfTrackerStatusReason_Authoriser` | String |  |  |
| 18 | `SFTR.CO.CODE` | `SfconfTrackerStatusReason_CoCode` | String |  |  |
| 19 | `SFTR.DEPT.CODE` | `SfconfTrackerStatusReason_DeptCode` | String |  |  |
| 20 | `SFTR.AUDITOR.CODE` | `SfconfTrackerStatusReason_AuditorCode` | String |  |  |
| 21 | `SFTR.AUDIT.DATE.TIME` | `SfconfTrackerStatusReason_AuditDateTime` | String |  |  |
