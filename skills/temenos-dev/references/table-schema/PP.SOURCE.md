# PP.SOURCE — Table Schema

> Source: `INSERTS/I_F.PP.SOURCE` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.SR.ChannelName` | `PpSource_Channelname` | TField |  | Relates to the channel through which messages from a source can be received. Validation Rules: 10 alphanumeric characters.The field links to field 'ChannelName' in PP.CHANNEL |
| 2 | `PP.SR.SourceProduct` | `PpSource_Sourceproduct` | TField |  | Indicates the group to which the source belongs. Validation Rules: 10 alphabetic characters. The value links to field 'SourceProduct' in PP.SOURCEPRODUCTGROUP. |
| 3 | `PP.SR.SourceDescription` | `PpSource_Sourcedescription` |  |  |  |
| 4 | `PP.SR.SourcePDGroup` | `PpSource_Sourcepdgroup` | TField | Yes | Indicates the group to which the source belongs. This field is used exclusively in Product Determination process in payments hub. Validation Rules: Mandatory field. 10 alphabetic characters. The value links to field 'SourceProduct' in PPT.SOURCEPRODUCTGROUP. |
| 5 | `PP.SR.SourceType` | `PpSource_Sourcetype` | TField | Yes | This field indicates if the source is a client channel, a non-client channel or internal channel This field Contains the Values Blank,C,NC,I Blank C - Client NC - Non Client I - Internal Validation Rules: Mandatory field when SenderType is Blank |
| 6 | `PP.SR.StatusReportFilenameAPI` | `PpSource_Statusreportfilenameapi` | TField |  |  |
| 7 | `PP.SR.SenderType` | `PpSource_Sendertype` | TField | Yes | This field indicates that this record is for Indirect Participant This field contains the value 'Blank' or 'IP' Validation Rules: Mandatory field when SoureType is Blank Applicable Only for PH module.If PH is not installed, values will be made blank/ default functionality will be applicable during payment processing |
| 8 | `PP.SR.RepeatResponse` | `PpSource_Repeatresponse` | TField |  | This field can be set as 'Y' if an immediate Clearing Status response needs to be sent for a repeat payment received from Clearing. Validation Rules: Dropdown. Allowed values 'Y' Or Blank |
| 9 | `PP.SR.ActionOnNACK` | `PpSource_Actiononnack` | TField |  | To configure if automatic reversal to be performed when negative technical acknowledgement is received. Dropdown.Allowed Values Blank,Cancel |
| 10 | `PP.SR.LOCAL.REF` | `PpSource_LocalRef` |  |  |  |
| 11 | `PP.SR.OVERRIDE` | `PpSource_Override` |  |  |  |
| 12 | `PP.SR.RECORD.STATUS` | `PpSource_RecordStatus` | String |  |  |
| 13 | `PP.SR.CURR.NO` | `PpSource_CurrNo` | String |  |  |
| 14 | `PP.SR.INPUTTER` | `PpSource_Inputter` |  |  |  |
| 15 | `PP.SR.DATE.TIME` | `PpSource_DateTime` |  |  |  |
| 16 | `PP.SR.AUTHORISER` | `PpSource_Authoriser` | String |  |  |
| 17 | `PP.SR.CO.CODE` | `PpSource_CoCode` | String |  |  |
| 18 | `PP.SR.DEPT.CODE` | `PpSource_DeptCode` | String |  |  |
| 19 | `PP.SR.AUDITOR.CODE` | `PpSource_AuditorCode` | String |  |  |
| 20 | `PP.SR.AUDIT.DATE.TIME` | `PpSource_AuditDateTime` | String |  |  |
