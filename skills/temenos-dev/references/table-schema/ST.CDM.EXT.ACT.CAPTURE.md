# ST.CDM.EXT.ACT.CAPTURE — Table Schema

> Source: `INSERTS/I_F.ST.CDM.EXT.ACT.CAPTURE` in `ST_DormancyMonitor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.EAC.CUSTOMER.ID` | `StCdmExtActCapture_CustomerId` | TField | Yes | External activity of this customer is to be captured. Only those customers with status as ACTIVE is considered for dormancy processing. Validation Rule: Should be a valid T24 Customer. This is a mandatory field. |
| 2 | `ST.EAC.DATE.OF.ACTIVITY` | `StCdmExtActCapture_DateOfActivity` | TField |  | Date on which this activity is captured in T24. Will be defaulted to current system date if not defined. |
| 3 | `ST.EAC.TIME.OF.ACTIVITY` | `StCdmExtActCapture_TimeOfActivity` | TField |  | Time at which this activity is captured in T24. Will be defaulted to current time based on the time zone. |
| 4 | `ST.EAC.RESET.DORMANCY` | `StCdmExtActCapture_ResetDormancy` | TField |  | Option to reset dormancy status for external products. If set , then dormancy status will be reset in ST.CDM.MONITOR, inline . Validation Rule: Allowed Values : Yes - Indicates customer is no more dormant. |
| 5 | `ST.EAC.UPDATE.LAST.ACTIVITY.DT` | `StCdmExtActCapture_UpdateLastActivityDt` | TField |  | If set, during dormancy reset system will capture the DATE.OF.ACTIVITY in LAST.ACTIVITY.DATE in ST.CDM.MONITOR. Applicable only if RESET.DORMANCY is set. Validation Rule: Allowed Values : Yes - Indicates to capture DATE.OF.ACTIVITY in LAST.ACTIVITY.DATE in ST.CDM.MONITOR. |
| 6 | `ST.EAC.ORG.SYSTEM.ID` | `StCdmExtActCapture_OrgSystemId` | TField |  | Field to capture the system ID of the external product. |
| 7 | `ST.EAC.EXTERNAL.ACTIVITY.REF` | `StCdmExtActCapture_ExternalActivityRef` | TField |  | This field captures the key for the activity of an external product. |
| 8 | `ST.EAC.ADDITIONAL.INFO` | `StCdmExtActCapture_AdditionalInfo` | TField |  | Addition information if required to be captured within T24. |
| 9 | `ST.EAC.LOCAL.REF` | `StCdmExtActCapture_LocalRef` |  |  |  |
| 10 | `ST.EAC.OVERRIDE` | `StCdmExtActCapture_Override` |  |  |  |
| 11 | `ST.EAC.RECORD.STATUS` | `StCdmExtActCapture_RecordStatus` | String |  |  |
| 12 | `ST.EAC.CURR.NO` | `StCdmExtActCapture_CurrNo` | String |  |  |
| 13 | `ST.EAC.INPUTTER` | `StCdmExtActCapture_Inputter` |  |  |  |
| 14 | `ST.EAC.DATE.TIME` | `StCdmExtActCapture_DateTime` |  |  |  |
| 15 | `ST.EAC.AUTHORISER` | `StCdmExtActCapture_Authoriser` | String |  |  |
| 16 | `ST.EAC.CO.CODE` | `StCdmExtActCapture_CoCode` | String |  |  |
| 17 | `ST.EAC.DEPT.CODE` | `StCdmExtActCapture_DeptCode` | String |  |  |
| 18 | `ST.EAC.AUDITOR.CODE` | `StCdmExtActCapture_AuditorCode` | String |  |  |
| 19 | `ST.EAC.AUDIT.DATE.TIME` | `StCdmExtActCapture_AuditDateTime` | String |  |  |
