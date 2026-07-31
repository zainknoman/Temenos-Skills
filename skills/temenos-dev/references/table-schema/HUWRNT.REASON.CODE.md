# HUWRNT.REASON.CODE — Table Schema

> Source: `INSERTS/I_F.HUWRNT.REASON.CODE` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWRCO.EB.ERROR.ID` | `HuwrntReasonCode_EbErrorId` |  |  |  |
| 2 | `HUWRCO.INTERNAL.CODE` | `HuwrntReasonCode_InternalCode` |  |  |  |
| 3 | `HUWRCO.RESERVED.15` | `HuwrntReasonCode_Reserved15` | TField |  | Reserved for Future Use. |
| 4 | `HUWRCO.RESERVED.14` | `HuwrntReasonCode_Reserved14` | TField |  | Reserved for Future Use. |
| 5 | `HUWRCO.RESERVED.13` | `HuwrntReasonCode_Reserved13` | TField |  | Reserved for Future Use. |
| 6 | `HUWRCO.RESERVED.12` | `HuwrntReasonCode_Reserved12` | TField |  | Reserved for Future Use. |
| 7 | `HUWRCO.RESERVED.11` | `HuwrntReasonCode_Reserved11` | TField |  | Reserved for Future Use. |
| 8 | `HUWRCO.RESERVED.10` | `HuwrntReasonCode_Reserved10` | TField |  | Reserved for Future Use. |
| 9 | `HUWRCO.RESERVED.9` | `HuwrntReasonCode_Reserved9` | TField |  | Reserved for Future Use. |
| 10 | `HUWRCO.RESERVED.8` | `HuwrntReasonCode_Reserved8` | TField |  | Reserved for Future Use. |
| 11 | `HUWRCO.RESERVED.7` | `HuwrntReasonCode_Reserved7` | TField |  | Reserved for Future Use. |
| 12 | `HUWRCO.RESERVED.6` | `HuwrntReasonCode_Reserved6` | TField |  | Reserved for Future Use. |
| 13 | `HUWRCO.RESERVED.5` | `HuwrntReasonCode_Reserved5` | TField |  | Reserved for Future Use. |
| 14 | `HUWRCO.RESERVED.4` | `HuwrntReasonCode_Reserved4` | TField |  | Reserved for Future Use. |
| 15 | `HUWRCO.RESERVED.3` | `HuwrntReasonCode_Reserved3` | TField |  | Reserved for Future Use. |
| 16 | `HUWRCO.RESERVED.2` | `HuwrntReasonCode_Reserved2` | TField |  | Reserved for Future Use. |
| 17 | `HUWRCO.RESERVED.1` | `HuwrntReasonCode_Reserved1` | TField |  | Reserved for Future Use. |
| 18 | `HUWRCO.STMT.NOS` | `HuwrntReasonCode_StmtNos` |  |  |  |
| 19 | `HUWRCO.OVERRIDE` | `HuwrntReasonCode_Override` |  |  |  |
| 20 | `HUWRCO.RECORD.STATUS` | `HuwrntReasonCode_RecordStatus` | String |  |  |
| 21 | `HUWRCO.CURR.NO` | `HuwrntReasonCode_CurrNo` | String |  |  |
| 22 | `HUWRCO.INPUTTER` | `HuwrntReasonCode_Inputter` |  |  |  |
| 23 | `HUWRCO.DATE.TIME` | `HuwrntReasonCode_DateTime` |  |  |  |
| 24 | `HUWRCO.AUTHORISER` | `HuwrntReasonCode_Authoriser` | String |  |  |
| 25 | `HUWRCO.CO.CODE` | `HuwrntReasonCode_CoCode` | String |  |  |
| 26 | `HUWRCO.DEPT.CODE` | `HuwrntReasonCode_DeptCode` | String |  |  |
| 27 | `HUWRCO.AUDITOR.CODE` | `HuwrntReasonCode_AuditorCode` | String |  |  |
| 28 | `HUWRCO.AUDIT.DATE.TIME` | `HuwrntReasonCode_AuditDateTime` | String |  |  |
