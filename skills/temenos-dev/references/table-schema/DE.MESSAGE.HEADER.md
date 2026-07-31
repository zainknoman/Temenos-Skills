# DE.MESSAGE.HEADER — Table Schema

> Source: `INSERTS/I_F.DE.MESSAGE.HEADER` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.MH.DESCRIPTION` | `DeMessageHeader_Description` | TField | Yes | Header description. Validation Rules&#58; Alphanumeric field. A maximum of 35 characters can be entered. Mandatory input. |
| 2 | `DE.MH.SCHEMA.ID` | `DeMessageHeader_SchemaId` | TField |  | Schema Id example&#58; head.001.01.02. Currently not used. |
| 3 | `DE.MH.HEADER.TYPE` | `DeMessageHeader_HeaderType` | TField |  | Identifies the type of the Header. Validation Rules&#58; Options field. Valid options&#58; Technical&#44; Business |
| 4 | `DE.MH.HEADER.VERSION` | `DeMessageHeader_HeaderVersion` | TField |  | Identifies the version of the Header. |
| 5 | `DE.MH.BUSINESS.METADATA` | `DeMessageHeader_BusinessMetadata` |  |  |  |
| 6 | `DE.MH.GENERIC.METADATA` | `DeMessageHeader_GenericMetadata` |  |  |  |
| 7 | `DE.MH.LCL.HDR.ELEMENT.API` | `DeMessageHeader_LclHdrElementApi` | TField |  | In this field can attach an api to define the additional local header elements required to be added for therespective message header. The api attached must be defined with EB.API. The arguments will be as follows: In Arguments: DeOHeaderRec - The array of DE.O.HEADER record with whatever possible values arrived DeMsgHeaderId - The ID of DE.MESSAGE.HEADER record ReservedIn - Reserved in argument for future In/Out arguments: GeneMetaData - The Generic meta data name:value pairs delimited by @SM arrived by core delivery system Out arguments: ReservedOut - Reserved out argument for future Where the GenMetaData must be send as TagName:Value pair and must be delimited by @SM. Validation Rules&#58; Must be a valid record from EB.API. Note: The values in, GeneMatadata will be passed as per the core based on the configuration, the local elementsshould locate the meta data names and update the values. Should not duplicate the meta data. Business meta data cannot be updated by the local routine Any meta data that has configured as part of Business Meta data, the same meta data should not be enhanced inlocal routine even as part of generic meta data |
| 8 | `DE.MH.CREATE.DATE.TIME.FORMAT` | `DeMessageHeader_CreateDateTimeFormat` | TField |  | Indicates the format of the CreateDateTime metadata. Valid options:ZULU, LOCALTIMEUTCOFFSET |
| 9 | `DE.MH.RESERVED.12` | `DeMessageHeader_Reserved12` | TField |  |  |
| 10 | `DE.MH.RESERVED.11` | `DeMessageHeader_Reserved11` | TField |  |  |
| 11 | `DE.MH.RESERVED.10` | `DeMessageHeader_Reserved10` | TField |  |  |
| 12 | `DE.MH.RESERVED.9` | `DeMessageHeader_Reserved9` | TField |  |  |
| 13 | `DE.MH.RESERVED.8` | `DeMessageHeader_Reserved8` | TField |  |  |
| 14 | `DE.MH.RESERVED.7` | `DeMessageHeader_Reserved7` | TField |  |  |
| 15 | `DE.MH.RESERVED.6` | `DeMessageHeader_Reserved6` | TField |  |  |
| 16 | `DE.MH.RESERVED.5` | `DeMessageHeader_Reserved5` | TField |  |  |
| 17 | `DE.MH.RESERVED.4` | `DeMessageHeader_Reserved4` | TField |  |  |
| 18 | `DE.MH.RESERVED.3` | `DeMessageHeader_Reserved3` | TField |  |  |
| 19 | `DE.MH.RESERVED.2` | `DeMessageHeader_Reserved2` | TField |  |  |
| 20 | `DE.MH.RESERVED.1` | `DeMessageHeader_Reserved1` | TField |  |  |
| 21 | `DE.MH.LOCAL.REF` | `DeMessageHeader_LocalRef` |  |  |  |
| 22 | `DE.MH.OVERRIDE` | `DeMessageHeader_Override` |  |  |  |
| 23 | `DE.MH.RECORD.STATUS` | `DeMessageHeader_RecordStatus` | String |  |  |
| 24 | `DE.MH.CURR.NO` | `DeMessageHeader_CurrNo` | String |  |  |
| 25 | `DE.MH.INPUTTER` | `DeMessageHeader_Inputter` |  |  |  |
| 26 | `DE.MH.DATE.TIME` | `DeMessageHeader_DateTime` |  |  |  |
| 27 | `DE.MH.AUTHORISER` | `DeMessageHeader_Authoriser` | String |  |  |
| 28 | `DE.MH.CO.CODE` | `DeMessageHeader_CoCode` | String |  |  |
| 29 | `DE.MH.DEPT.CODE` | `DeMessageHeader_DeptCode` | String |  |  |
| 30 | `DE.MH.AUDITOR.CODE` | `DeMessageHeader_AuditorCode` | String |  |  |
| 31 | `DE.MH.AUDIT.DATE.TIME` | `DeMessageHeader_AuditDateTime` | String |  |  |
| 32 | `DE.MH.BUS.META.IS.MANDATORY` | `DeMessageHeader_BusMetaIsMandatory` |  |  |  |
| 33 | `DE.MH.GEN.META.IS.MANDATORY` | `DeMessageHeader_GenMetaIsMandatory` |  |  |  |
