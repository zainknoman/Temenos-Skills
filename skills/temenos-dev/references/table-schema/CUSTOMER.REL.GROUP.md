# CUSTOMER.REL.GROUP — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.REL.GROUP` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CUS.REL.GR.GROUP.NAME` | `CustomerRelGroup_GroupName` | TField | Yes | Identifies the name of the group. Validation Rules: Mandatory Input. Maximum 40 characters. |
| 2 | `CUS.REL.GR.CUSTOMER.NO` | `CustomerRelGroup_CustomerNo` | TField | No | Identifies the owner of the group. Validation Rules: Optional Input. Must be a valid record in customer table. |
| 3 | `CUS.REL.GR.CUSTOMER.NAME` | `CustomerRelGroup_CustomerName` |  |  |  |
| 4 | `CUS.REL.GR.LEGAL.ID` | `CustomerRelGroup_LegalId` |  |  |  |
| 5 | `CUS.REL.GR.LEGAL.DOC.NAME` | `CustomerRelGroup_LegalDocName` |  |  |  |
| 6 | `CUS.REL.GR.LOCAL.REF` | `CustomerRelGroup_LocalRef` |  |  |  |
| 7 | `CUS.REL.GR.RESERVED.15` | `CustomerRelGroup_Reserved15` | TField |  |  |
| 8 | `CUS.REL.GR.RESERVED.14` | `CustomerRelGroup_Reserved14` | TField |  |  |
| 9 | `CUS.REL.GR.RESERVED.13` | `CustomerRelGroup_Reserved13` | TField |  |  |
| 10 | `CUS.REL.GR.RESERVED.12` | `CustomerRelGroup_Reserved12` | TField |  |  |
| 11 | `CUS.REL.GR.RESERVED.11` | `CustomerRelGroup_Reserved11` | TField |  |  |
| 12 | `CUS.REL.GR.RESERVED.10` | `CustomerRelGroup_Reserved10` | TField |  |  |
| 13 | `CUS.REL.GR.RESERVED.9` | `CustomerRelGroup_Reserved9` | TField |  |  |
| 14 | `CUS.REL.GR.RESERVED.8` | `CustomerRelGroup_Reserved8` | TField |  |  |
| 15 | `CUS.REL.GR.RESERVED.7` | `CustomerRelGroup_Reserved7` | TField |  |  |
| 16 | `CUS.REL.GR.RESERVED.6` | `CustomerRelGroup_Reserved6` | TField |  |  |
| 17 | `CUS.REL.GR.RESERVED.5` | `CustomerRelGroup_Reserved5` | TField |  |  |
| 18 | `CUS.REL.GR.RESERVED.4` | `CustomerRelGroup_Reserved4` | TField |  |  |
| 19 | `CUS.REL.GR.RESERVED.3` | `CustomerRelGroup_Reserved3` | TField |  |  |
| 20 | `CUS.REL.GR.RESERVED.2` | `CustomerRelGroup_Reserved2` | TField |  |  |
| 21 | `CUS.REL.GR.RESERVED.1` | `CustomerRelGroup_Reserved1` | TField |  |  |
| 22 | `CUS.REL.GR.RECORD.STATUS` | `CustomerRelGroup_RecordStatus` | String |  |  |
| 23 | `CUS.REL.GR.CURR.NO` | `CustomerRelGroup_CurrNo` | String |  |  |
| 24 | `CUS.REL.GR.INPUTTER` | `CustomerRelGroup_Inputter` |  |  |  |
| 25 | `CUS.REL.GR.DATE.TIME` | `CustomerRelGroup_DateTime` |  |  |  |
| 26 | `CUS.REL.GR.AUTHORISER` | `CustomerRelGroup_Authoriser` | String |  |  |
| 27 | `CUS.REL.GR.CO.CODE` | `CustomerRelGroup_CoCode` | String |  |  |
| 28 | `CUS.REL.GR.DEPT.CODE` | `CustomerRelGroup_DeptCode` | String |  |  |
| 29 | `CUS.REL.GR.AUDITOR.CODE` | `CustomerRelGroup_AuditorCode` | String |  |  |
| 30 | `CUS.REL.GR.AUDIT.DATE.TIME` | `CustomerRelGroup_AuditDateTime` | String |  |  |
