# IL.ENTITY — Table Schema

> Source: `INSERTS/I_F.IL.ENTITY` in `IL_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IL.ENT.ENTITY.NAME` | `IlEntity_EntityName` | TField | Yes | This field holds the name of the entity. Validation Rules: Standard T24 alphanumeric field. Mandatory field and accepts upto 35 alphanumeric characters. If the ID holds a valid transact company then it defaults the company name from the company table. |
| 2 | `IL.ENT.ENTITY.DESCRIPTION` | `IlEntity_EntityDescription` |  |  |  |
| 3 | `IL.ENT.BASE.CURRENCY` | `IlEntity_BaseCurrency` | TField | Yes | This field holds the local currency of the entity in ISO currency code. Validation Rules: Mandatory field. Must be a valid currency in the CURRENCY table. If the ID holds valid transact company, then default the local currency from the company table. User cannot change the value after the record is authorised. |
| 4 | `IL.ENT.ENTITY.BIC` | `IlEntity_EntityBic` | TField | Yes | This field holds the BIC of the entity. This will be used in the SWIFT messages. Validation Rules: Mandatory field. Should be 8 or 11 alphanumeric characters. User cannot change the value after the record is authorised. If RD/DE module is installed, then validate the BIC against the RD.CENTRAL.BANK.DIR/DE.BIC table. If not, system will validate the alphanumeric condition. If BIC is not validated as per the standard, then system will raise an override. |
| 5 | `IL.ENT.COUNTRY` | `IlEntity_Country` | TField | Yes | This field holds the country code of the entity. Validation Rules: Mandatory Field. User cannot change the value after the record is authorised. If the ID holds valid transact company, then default the local country from the company table. |
| 6 | `IL.ENT.GEO.BLOCK` | `IlEntity_GeoBlock` | TField | Yes | This field holds the geographic block of the entity. Validation Rules: Mandatory Field. User cannot change the value after the record is authorised. Must be a valid code in the GEOGRAPHIC.BLOCK table. The value will be defaulted from the GEOGRAPHIC.BLOCK table based on the IL.ENTITY country given. |
| 7 | `IL.ENT.MASTER.ENTITY` | `IlEntity_MasterEntity` | TField | Yes | This field defines if the entity is the master entity where consolidated liquidity will be monitored. There will be only one master entity. Validation Rules: Mandatory field and NoChange Field. Accepts YES or NO. If Master entity is marked as YES, then System will not allow to input PARENT.ENTITY. Only one Master Entity will be allowed. |
| 8 | `IL.ENT.PARENT.ENTITY` | `IlEntity_ParentEntity` | TField |  | This field defines the parent entity to which the liquidity will be consolidated. This will establish the parent-child hierarchy of entities. Validation Rules: If Master entity is marked as YES, then System will not allow to input PARENT.ENTITY. Valid record in IL.ENTITY table. System will throw an error if the selected entity is not a master entity. |
| 9 | `IL.ENT.RESERVED.10` | `IlEntity_Reserved10` | TField |  |  |
| 10 | `IL.ENT.RESERVED.9` | `IlEntity_Reserved9` | TField |  |  |
| 11 | `IL.ENT.RESERVED.8` | `IlEntity_Reserved8` | TField |  |  |
| 12 | `IL.ENT.RESERVED.7` | `IlEntity_Reserved7` | TField |  |  |
| 13 | `IL.ENT.RESERVED.6` | `IlEntity_Reserved6` | TField |  |  |
| 14 | `IL.ENT.RESERVED.5` | `IlEntity_Reserved5` | TField |  |  |
| 15 | `IL.ENT.RESERVED.4` | `IlEntity_Reserved4` | TField |  |  |
| 16 | `IL.ENT.RESERVED.3` | `IlEntity_Reserved3` | TField |  |  |
| 17 | `IL.ENT.RESERVED.2` | `IlEntity_Reserved2` | TField |  |  |
| 18 | `IL.ENT.RESERVED.1` | `IlEntity_Reserved1` | TField |  |  |
| 19 | `IL.ENT.LOCAL.REF` | `IlEntity_LocalRef` |  |  |  |
| 20 | `IL.ENT.OVERRIDE` | `IlEntity_Override` |  |  |  |
| 21 | `IL.ENT.RECORD.STATUS` | `IlEntity_RecordStatus` | String |  |  |
| 22 | `IL.ENT.CURR.NO` | `IlEntity_CurrNo` | String |  |  |
| 23 | `IL.ENT.INPUTTER` | `IlEntity_Inputter` |  |  |  |
| 24 | `IL.ENT.DATE.TIME` | `IlEntity_DateTime` |  |  |  |
| 25 | `IL.ENT.AUTHORISER` | `IlEntity_Authoriser` | String |  |  |
| 26 | `IL.ENT.CO.CODE` | `IlEntity_CoCode` | String |  |  |
| 27 | `IL.ENT.DEPT.CODE` | `IlEntity_DeptCode` | String |  |  |
| 28 | `IL.ENT.AUDITOR.CODE` | `IlEntity_AuditorCode` | String |  |  |
| 29 | `IL.ENT.AUDIT.DATE.TIME` | `IlEntity_AuditDateTime` | String |  |  |
