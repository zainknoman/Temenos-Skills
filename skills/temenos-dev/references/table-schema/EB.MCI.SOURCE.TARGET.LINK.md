# EB.MCI.SOURCE.TARGET.LINK — Table Schema

> Source: `INSERTS/I_F.EB.MCI.SOURCE.TARGET.LINK` in `EI_MCI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.MCI.ST.LINK.TABLE` | `EbMciSourceTargetLink_LinkTable` | TField | Yes | The T24 Table where the Source Record ID is the Key to the record Either LINK.TABLE or LINK.API is mandatory |
| 2 | `EB.MCI.ST.LINK.FIELD` | `EbMciSourceTargetLink_LinkField` | TField |  | The field in the table specified in Link Table, that holds the key to the Target Record. If there is a CheckFile defined for this field then this must be the same as target table as specified in the id. |
| 3 | `EB.MCI.ST.LINK.API` | `EbMciSourceTargetLink_LinkApi` | TField | Yes | If there is no formal Link between a Source and Target record, this API can be used. This API will be called for each Source Record e.g; Customer and it is expected to return the applicable list of Target Record IDs e.g; AA.ARRANGEMENT IDs Either LINK.TABLE or LINK.API is mandatory |
| 4 | `EB.MCI.ST.RESERVED.5` | `EbMciSourceTargetLink_Reserved5` | TField |  |  |
| 5 | `EB.MCI.ST.RESERVED.4` | `EbMciSourceTargetLink_Reserved4` | TField |  |  |
| 6 | `EB.MCI.ST.RESERVED.3` | `EbMciSourceTargetLink_Reserved3` | TField |  |  |
| 7 | `EB.MCI.ST.RESERVED.2` | `EbMciSourceTargetLink_Reserved2` | TField |  |  |
| 8 | `EB.MCI.ST.RESERVED.1` | `EbMciSourceTargetLink_Reserved1` | TField |  |  |
| 9 | `EB.MCI.ST.LOCAL.REF` | `EbMciSourceTargetLink_LocalRef` |  |  |  |
| 10 | `EB.MCI.ST.OVERRIDE` | `EbMciSourceTargetLink_Override` |  |  |  |
| 11 | `EB.MCI.ST.RECORD.STATUS` | `EbMciSourceTargetLink_RecordStatus` | String |  |  |
| 12 | `EB.MCI.ST.CURR.NO` | `EbMciSourceTargetLink_CurrNo` | String |  |  |
| 13 | `EB.MCI.ST.INPUTTER` | `EbMciSourceTargetLink_Inputter` |  |  |  |
| 14 | `EB.MCI.ST.DATE.TIME` | `EbMciSourceTargetLink_DateTime` |  |  |  |
| 15 | `EB.MCI.ST.AUTHORISER` | `EbMciSourceTargetLink_Authoriser` | String |  |  |
| 16 | `EB.MCI.ST.CO.CODE` | `EbMciSourceTargetLink_CoCode` | String |  |  |
| 17 | `EB.MCI.ST.DEPT.CODE` | `EbMciSourceTargetLink_DeptCode` | String |  |  |
| 18 | `EB.MCI.ST.AUDITOR.CODE` | `EbMciSourceTargetLink_AuditorCode` | String |  |  |
| 19 | `EB.MCI.ST.AUDIT.DATE.TIME` | `EbMciSourceTargetLink_AuditDateTime` | String |  |  |
