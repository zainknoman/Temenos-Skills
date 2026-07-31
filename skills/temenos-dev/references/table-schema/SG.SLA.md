# SG.SLA — Table Schema

> Source: `INSERTS/I_F.SG.SLA` in `SG_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SG.SLA.DESCRIPTION` | `SgSla_Description` |  |  |  |
| 2 | `SG.SLA.ALLOWED.COMPANY` | `SgSla_AllowedCompany` |  |  |  |
| 3 | `SG.SLA.DURATION.TIME` | `SgSla_DurationTime` | TField |  | Indicates the expected duration time. Once the activity is started, this field is used to arrive at end time. Validation Rules: =============== a) Should accept Time like HH:MM:SS b) Value NONE is not supported |
| 4 | `SG.SLA.DURATION.DAY` | `SgSla_DurationDay` | TField |  | Accepts the number of days for processing. Validation Rules: =============== Input must be numeric |
| 5 | `SG.SLA.DUR.CAL.WORK` | `SgSla_DurCalWork` | TField |  | Indicates if the DURATION.DAY is to be calculated on Calender or Working days. Validation Rules: =============== Allowed Values: C or W If left blank system will consider the calculation based on 'C'(Calender). Input allowed only if DURATION.DAY is specified. Note: For Working days- the current (ID.COMPANY) will be used for holiday calculations. |
| 6 | `SG.SLA.SEND.DELIVERY` | `SgSla_SendDelivery` | TField |  | Indicates if delivery message to be raised in addition to marking the status as BREACHED or not Validation Rules: =============== Allowed Values: Yes or No Yes - Indicates that delivery message should be raised in addition to marking the status as BREACHED. No - Indicates that no delivery to be sent- just mark the status to BREACHED. If left blank, it will be treated as YES. |
| 7 | `SG.SLA.EB.ACTIVITY` | `SgSla_EbActivity` | TField |  | This field is used to specify EB.ACTIVITY table Id which is used to define and control the output of delivery messages. Validation Rules: If SEND.DELIVERY field is set as NO,input to this field is not Allowed If SEND.DELIVERY field is set as YES or NULL,input to this field is Allowed |
| 8 | `SG.SLA.RESERVED.10` | `SgSla_Reserved10` | TField |  | This field is reserved for future use Validation Rules: =============== NOINPUT field |
| 9 | `SG.SLA.RESERVED.9` | `SgSla_Reserved9` | TField |  |  |
| 10 | `SG.SLA.RESERVED.8` | `SgSla_Reserved8` | TField |  |  |
| 11 | `SG.SLA.RESERVED.7` | `SgSla_Reserved7` | TField |  |  |
| 12 | `SG.SLA.RESERVED.6` | `SgSla_Reserved6` | TField |  |  |
| 13 | `SG.SLA.RESERVED.5` | `SgSla_Reserved5` | TField |  |  |
| 14 | `SG.SLA.RESERVED.4` | `SgSla_Reserved4` | TField |  |  |
| 15 | `SG.SLA.RESERVED.3` | `SgSla_Reserved3` | TField |  |  |
| 16 | `SG.SLA.RESERVED.2` | `SgSla_Reserved2` | TField |  |  |
| 17 | `SG.SLA.RESERVED.1` | `SgSla_Reserved1` | TField |  |  |
| 18 | `SG.SLA.LOCAL.REF` | `SgSla_LocalRef` |  |  |  |
| 19 | `SG.SLA.OVERRIDE` | `SgSla_Override` |  |  |  |
| 20 | `SG.SLA.RECORD.STATUS` | `SgSla_RecordStatus` | String |  |  |
| 21 | `SG.SLA.CURR.NO` | `SgSla_CurrNo` | String |  |  |
| 22 | `SG.SLA.INPUTTER` | `SgSla_Inputter` |  |  |  |
| 23 | `SG.SLA.DATE.TIME` | `SgSla_DateTime` |  |  |  |
| 24 | `SG.SLA.AUTHORISER` | `SgSla_Authoriser` | String |  |  |
| 25 | `SG.SLA.CO.CODE` | `SgSla_CoCode` | String |  |  |
| 26 | `SG.SLA.DEPT.CODE` | `SgSla_DeptCode` | String |  |  |
| 27 | `SG.SLA.AUDITOR.CODE` | `SgSla_AuditorCode` | String |  |  |
| 28 | `SG.SLA.AUDIT.DATE.TIME` | `SgSla_AuditDateTime` | String |  |  |
