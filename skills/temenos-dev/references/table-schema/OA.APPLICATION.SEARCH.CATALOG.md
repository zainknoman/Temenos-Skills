# OA.APPLICATION.SEARCH.CATALOG — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION.SEARCH.CATALOG` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.ASC.DESCRIPTION` | `OaApplicationSearchCatalog_Description` |  |  |  |
| 2 | `OA.ASC.FULL.DESCRIPTION` | `OaApplicationSearchCatalog_FullDescription` |  |  |  |
| 3 | `OA.ASC.RESERVED.10` | `OaApplicationSearchCatalog_Reserved10` | TField |  |  |
| 4 | `OA.ASC.RESERVED.9` | `OaApplicationSearchCatalog_Reserved9` | TField |  |  |
| 5 | `OA.ASC.RESERVED.8` | `OaApplicationSearchCatalog_Reserved8` | TField |  |  |
| 6 | `OA.ASC.ENQ.CRITERIA.NAME` | `OaApplicationSearchCatalog_EnqCriteriaName` |  |  |  |
| 7 | `OA.ASC.CRITERIA.DESCRIPTION` | `OaApplicationSearchCatalog_CriteriaDescription` |  |  |  |
| 8 | `OA.ASC.DATA.OBJECT` | `OaApplicationSearchCatalog_DataObject` |  |  |  |
| 9 | `OA.ASC.APPLICATION.NAME` | `OaApplicationSearchCatalog_ApplicationName` |  |  |  |
| 10 | `OA.ASC.SYS.ATTRIBUTE` | `OaApplicationSearchCatalog_SysAttribute` |  |  |  |
| 11 | `OA.ASC.SYS.ATTRIBUTE.POSITION` | `OaApplicationSearchCatalog_SysAttributePosition` |  |  |  |
| 12 | `OA.ASC.SEARCH.ATTRIBUTE` | `OaApplicationSearchCatalog_SearchAttribute` |  |  |  |
| 13 | `OA.ASC.STATUS.CODES` | `OaApplicationSearchCatalog_StatusCodes` |  |  |  |
| 14 | `OA.ASC.RESERVED.7` | `OaApplicationSearchCatalog_Reserved7` | TField |  |  |
| 15 | `OA.ASC.RESERVED.6` | `OaApplicationSearchCatalog_Reserved6` | TField |  |  |
| 16 | `OA.ASC.RESERVED.5` | `OaApplicationSearchCatalog_Reserved5` | TField |  |  |
| 17 | `OA.ASC.RESERVED.4` | `OaApplicationSearchCatalog_Reserved4` | TField |  |  |
| 18 | `OA.ASC.RESERVED.3` | `OaApplicationSearchCatalog_Reserved3` | TField |  |  |
| 19 | `OA.ASC.RESERVED.2` | `OaApplicationSearchCatalog_Reserved2` | TField |  |  |
| 20 | `OA.ASC.RESERVED.1` | `OaApplicationSearchCatalog_Reserved1` | TField |  |  |
| 21 | `OA.ASC.ACTION` | `OaApplicationSearchCatalog_Action` | TField |  | Option PUBLISH would be allowed in this field and authorization of the record with this option would trigger publishing of this record. |
| 22 | `OA.ASC.PUBLISH.STATUS` | `OaApplicationSearchCatalog_PublishStatus` | TField |  | Noinput, System maintained field - indicating the status of publish action. |
| 23 | `OA.ASC.PUBLISH.DATE` | `OaApplicationSearchCatalog_PublishDate` | TField |  | Noinput, System maintained field - indicating the last published date of this record. |
| 24 | `OA.ASC.REFERENCE` | `OaApplicationSearchCatalog_Reference` | TField |  | Indicates the First part of the @ID - System maintained, Noinput field. |
| 25 | `OA.ASC.VERSION` | `OaApplicationSearchCatalog_Version` | TField |  | Indicates the second part of the @ID - System maintained, Noinput field. |
