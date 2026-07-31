# PP.CLEARING.FREQUENCY — Table Schema

> Source: `INSERTS/I_F.PP.CLEARING.FREQUENCY` in `PP_LocalClearingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCFQ.CutOff` | `PpClearingFrequency_Cutoff` |  |  |  |
| 2 | `PPCFQ.Status` | `PpClearingFrequency_Status` |  |  |  |
| 3 | `PPCFQ.RejectCutOff` | `PpClearingFrequency_Rejectcutoff` | TField |  | Specifies time on which Nostro settlement process with clearing house has to be started. This value will be used by Outward Mapping Framework to determine when the settlement process has to run. This Cutoff is used for both CT and DD Transactions. Both Inward and Outward Settlement process. |
| 4 | `PPCFQ.RejectStatus` | `PpClearingFrequency_Rejectstatus` | TField |  | Specifies status of the cutoff. Possible values: 1. READY - the Nostro settlement process for the cutoff is not processed 2. READY-&lt;date&gt; - the Nostro settlement process for the cutoff is not processed and will be processed only on the &lt;date&gt; given. 3. PROCESSING - the Nostro settlement process for the cutoff is in-progress 4. COMPLETED - the Nostro settlement process is completed The value is not editable by the user |
| 5 | `PPCFQ.ReleaseTime` | `PpClearingFrequency_Releasetime` |  |  |  |
| 6 | `PPCFQ.ReleaseStatus` | `PpClearingFrequency_Releasestatus` |  |  |  |
| 7 | `PPCFQ.RESERVED01` | `PpClearingFrequency_Reserved01` | TField |  |  |
| 8 | `PPCFQ.LOCAL.REF` | `PpClearingFrequency_LocalRef` |  |  |  |
| 9 | `PPCFQ.OVERRIDE` | `PpClearingFrequency_Override` |  |  |  |
| 10 | `PPCFQ.RECORD.STATUS` | `PpClearingFrequency_RecordStatus` | String |  |  |
| 11 | `PPCFQ.CURR.NO` | `PpClearingFrequency_CurrNo` | String |  |  |
| 12 | `PPCFQ.INPUTTER` | `PpClearingFrequency_Inputter` |  |  |  |
| 13 | `PPCFQ.DATE.TIME` | `PpClearingFrequency_DateTime` |  |  |  |
| 14 | `PPCFQ.AUTHORISER` | `PpClearingFrequency_Authoriser` | String |  |  |
| 15 | `PPCFQ.CO.CODE` | `PpClearingFrequency_CoCode` | String |  |  |
| 16 | `PPCFQ.DEPT.CODE` | `PpClearingFrequency_DeptCode` | String |  |  |
| 17 | `PPCFQ.AUDITOR.CODE` | `PpClearingFrequency_AuditorCode` | String |  |  |
| 18 | `PPCFQ.AUDIT.DATE.TIME` | `PpClearingFrequency_AuditDateTime` | String |  |  |
| 19 | `PPCFQ.MessageType` | `PpClearingFrequency_Messagetype` |  |  |  |
| 20 | `PPCFQ.ClearingNatureCode` | `PpClearingFrequency_Clearingnaturecode` |  |  |  |
| 21 | `PPCFQ.Currency` | `PpClearingFrequency_Currency` |  |  |  |
