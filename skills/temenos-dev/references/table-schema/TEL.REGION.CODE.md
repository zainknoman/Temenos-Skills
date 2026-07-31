# TEL.REGION.CODE — Table Schema

> Source: `INSERTS/I_F.TEL.REGION.CODE` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TEL.REG.COD.DESCRIPTION` | `TelRegionCode_Description` |  |  |  |
| 2 | `TEL.REG.COD.REGION.COUNTRY` | `TelRegionCode_RegionCountry` | TField | Yes | Field holds the country which country, the region belongs to. Validation Rules: valid record in COUNTRY table Mandatory to input |
| 3 | `TEL.REG.COD.RESERVED.20` | `TelRegionCode_Reserved20` | TField |  | Reserved for future use |
| 4 | `TEL.REG.COD.RESERVED.19` | `TelRegionCode_Reserved19` | TField |  | Reserved for future use |
| 5 | `TEL.REG.COD.RESERVED.18` | `TelRegionCode_Reserved18` | TField |  | Reserved for future use |
| 6 | `TEL.REG.COD.RESERVED.17` | `TelRegionCode_Reserved17` | TField |  | Reserved for future use |
| 7 | `TEL.REG.COD.RESERVED.16` | `TelRegionCode_Reserved16` | TField |  | Reserved for future use |
| 8 | `TEL.REG.COD.RESERVED.15` | `TelRegionCode_Reserved15` | TField |  | Reserved for future use |
| 9 | `TEL.REG.COD.RESERVED.14` | `TelRegionCode_Reserved14` | TField |  | Reserved for future use |
| 10 | `TEL.REG.COD.RESERVED.13` | `TelRegionCode_Reserved13` | TField |  | Reserved for future use |
| 11 | `TEL.REG.COD.RESERVED.12` | `TelRegionCode_Reserved12` | TField |  | Reserved for future use |
| 12 | `TEL.REG.COD.RESERVED.11` | `TelRegionCode_Reserved11` | TField |  | Reserved for future use |
| 13 | `TEL.REG.COD.RESERVED.10` | `TelRegionCode_Reserved10` | TField |  | Reserved for future use |
| 14 | `TEL.REG.COD.RESERVED.9` | `TelRegionCode_Reserved9` | TField |  | Reserved for future use |
| 15 | `TEL.REG.COD.RESERVED.8` | `TelRegionCode_Reserved8` | TField |  | Reserved for future use |
| 16 | `TEL.REG.COD.RESERVED.7` | `TelRegionCode_Reserved7` | TField |  | Reserved for future use |
| 17 | `TEL.REG.COD.RESERVED.6` | `TelRegionCode_Reserved6` | TField |  | Reserved for future use |
| 18 | `TEL.REG.COD.RESERVED.5` | `TelRegionCode_Reserved5` | TField |  | Reserved for future use |
| 19 | `TEL.REG.COD.RESERVED.4` | `TelRegionCode_Reserved4` | TField |  | Reserved for future use |
| 20 | `TEL.REG.COD.RESERVED.3` | `TelRegionCode_Reserved3` | TField |  | Reserved for future use |
| 21 | `TEL.REG.COD.RESERVED.2` | `TelRegionCode_Reserved2` | TField |  | Reserved for future use |
| 22 | `TEL.REG.COD.RESERVED.1` | `TelRegionCode_Reserved1` | TField |  | Reserved for future use |
| 23 | `TEL.REG.COD.LOCAL.REF` | `TelRegionCode_LocalRef` |  |  |  |
| 24 | `TEL.REG.COD.OVERRIDE` | `TelRegionCode_Override` |  |  |  |
| 25 | `TEL.REG.COD.RECORD.STATUS` | `TelRegionCode_RecordStatus` | String |  | Status of the record |
| 26 | `TEL.REG.COD.CURR.NO` | `TelRegionCode_CurrNo` | String |  | Curr No |
| 27 | `TEL.REG.COD.INPUTTER` | `TelRegionCode_Inputter` |  |  |  |
| 28 | `TEL.REG.COD.DATE.TIME` | `TelRegionCode_DateTime` |  |  |  |
| 29 | `TEL.REG.COD.AUTHORISER` | `TelRegionCode_Authoriser` | String |  | Authoriser |
| 30 | `TEL.REG.COD.CO.CODE` | `TelRegionCode_CoCode` | String |  | Company code |
| 31 | `TEL.REG.COD.DEPT.CODE` | `TelRegionCode_DeptCode` | String |  | Department code |
| 32 | `TEL.REG.COD.AUDITOR.CODE` | `TelRegionCode_AuditorCode` | String |  | Auditor Code |
| 33 | `TEL.REG.COD.AUDIT.DATE.TIME` | `TelRegionCode_AuditDateTime` | String |  | Audit Date and time |
