# EB.TABLE.DEFINITION — Table Schema

> Source: `INSERTS/I_F.EB.TABLE.DEFINITION` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DYN.ACT.ACT.DESC` | `EbTableDefinition_ActDesc` |  |  |  |
| 2 | `DYN.ACT.PRODUCT` | `EbTableDefinition_Product` | TField |  | A valid product code. The template created will belong to this product and the template name will be prefixedwith this product |
| 3 | `DYN.ACT.FIELD.NAME` | `EbTableDefinition_FieldName` |  |  |  |
| 4 | `DYN.ACT.DESCRIPTION` | `EbTableDefinition_Description` |  |  |  |
| 5 | `DYN.ACT.PROMPT.TEXT` | `EbTableDefinition_PromptText` |  |  |  |
| 6 | `DYN.ACT.TOOL.TIP` | `EbTableDefinition_ToolTip` |  |  |  |
| 7 | `DYN.ACT.CALCULATION` | `EbTableDefinition_Calculation` |  |  |  |
| 8 | `DYN.ACT.AVAILABILITY` | `EbTableDefinition_Availability` |  |  |  |
| 9 | `DYN.ACT.ACTIVITY.ID` | `EbTableDefinition_ActivityId` |  |  |  |
| 10 | `DYN.ACT.ACTIVITY.FLD` | `EbTableDefinition_ActivityFld` |  |  |  |
| 11 | `DYN.ACT.MAX.CHAR` | `EbTableDefinition_MaxChar` |  |  |  |
| 12 | `DYN.ACT.MIN.CHAR` | `EbTableDefinition_MinChar` |  |  |  |
| 13 | `DYN.ACT.DATA.TYPE` | `EbTableDefinition_DataType` |  |  |  |
| 14 | `DYN.ACT.CCY.ACTIVITY` | `EbTableDefinition_CcyActivity` |  |  |  |
| 15 | `DYN.ACT.CCY.ACT.FLD` | `EbTableDefinition_CcyActFld` |  |  |  |
| 16 | `DYN.ACT.VETTING.TABLE` | `EbTableDefinition_VettingTable` |  |  |  |
| 17 | `DYN.ACT.APPL.VET` | `EbTableDefinition_ApplVet` |  |  |  |
| 18 | `DYN.ACT.APPL.ENRICH.FLD` | `EbTableDefinition_ApplEnrichFld` |  |  |  |
| 19 | `DYN.ACT.DEF.VALUE` | `EbTableDefinition_DefValue` |  |  |  |
| 20 | `DYN.ACT.FLD.PROPERTY` | `EbTableDefinition_FldProperty` |  |  |  |
| 21 | `DYN.ACT.MASKING.FMT` | `EbTableDefinition_MaskingFmt` |  |  |  |
| 22 | `DYN.ACT.VIRTUAL.TABLE` | `EbTableDefinition_VirtualTable` |  |  |  |
| 23 | `DYN.ACT.SUB.ASSOC.CODE` | `EbTableDefinition_SubAssocCode` |  |  |  |
| 24 | `DYN.ACT.REL.DATE.FIELD` | `EbTableDefinition_RelDateField` |  |  |  |
| 25 | `DYN.ACT.REL.CURRENCY.FIELD` | `EbTableDefinition_RelCurrencyField` |  |  |  |
| 26 | `DYN.ACT.FLD.PRODUCT` | `EbTableDefinition_FldProduct` |  |  |  |
| 27 | `DYN.ACT.PHYSICAL.POSITION` | `EbTableDefinition_PhysicalPosition` |  |  |  |
| 28 | `DYN.ACT.RESERVED11` | `EbTableDefinition_Reserved11` |  |  |  |
| 29 | `DYN.ACT.PREFIX` | `EbTableDefinition_Prefix` | TField | Yes | The prefix needed to address all the fields defined in the dynamic application. Value entered here will becomethe prefix for this dynamic application with product. (e.g: if name given here is TEST and product is EB thenprefix of the dynamic application becomes EB.TEST.fieldname). Validation Rules: : 1.Field can accept alpha numeric values 2.NOCHANGE field - cant change the prefix of the insert file once the record being authorized 3.Mandatory field |
| 30 | `DYN.ACT.FILE.TYPE` | `EbTableDefinition_FileType` | TField |  | Defines the type of the file. The allowed values are FIN, CUS and INT |
| 31 | `DYN.ACT.LINK.TO.WFL` | `EbTableDefinition_LinkToWfl` | TField |  | Using this field the user can define whether the application should be linked to the workflow. If the value ofthis field is set to NO, then the record in the application cannot be kept on HOLD after first input |
| 32 | `DYN.ACT.NS.OPERATION` | `EbTableDefinition_NsOperation` | TField |  | NS.OPERATION field will determine if this application will allow entry / modification during the close ofbusiness This field should allow only three input ALL,NEW and NOD ALL - Application alows NS operation NEW - Application allows NS operation for NEW ids only NOD - Can be run Non Stop without the NS module installed |
| 33 | `DYN.ACT.KEY.FIELD` | `EbTableDefinition_KeyField` | TField | Yes | Holds any one of the field name from the multi value set which field become an ID of the dynamic template.properties of that specified field is becomes the properties of the ID for dynamic template. Validation Rules: 1.Corresponding field should accept the ALPHA, DATE, ALPHANUMERIC,NUMERIC and TEXT data types. 2.should be valid name from the FIELD.NAME multi value set 3.Non Mandatory field |
| 34 | `DYN.ACT.INSERT.LAYOUT` | `EbTableDefinition_InsertLayout` | TField | Yes | We can specify the location of the insert file. Insert file for the dynamic template will be created under thedirectory name specified here. If there is no mentioned directory present then T24 will automatically create that directory and place the insertfile under the directory. Validation Rules: 1.Non Mandatory field |
| 35 | `DYN.ACT.ADD.SPECIAL.FIELDS` | `EbTableDefinition_AddSpecialFields` |  |  |  |
| 36 | `DYN.ACT.LOCAL.REF` | `EbTableDefinition_LocalRef` |  |  |  |
| 37 | `DYN.ACT.CLASS.TYPE` | `EbTableDefinition_ClassType` | TField |  | This field is used only when the EB.TABLE.DEFINITION defines an AA.CLASS.DEFINITION application , otherwise ithas no effect. In the case of Class Definition the ID of EB.TABLE.DEFINITION will have format PRODUCT.CODE plus a start *Followed by CLASS.NAME.The system will use this value to create design, proof,catalog,simulation and instance leveldynamic templates for theclass definition Exact names of class definition templates being created is retrieved by refering to fieldsPREFIX.DESIGN,PREFIX.PROOF, PREFIX.CATALOG , PREFIX.INSTANCE and PREFIX.SIMULATION respectively and concatenatingthe Product code , the prefix and the class Name. Examples: 1.If the ID of EB.TABLE.DEFINITION is OA*BASIC.DETAILS and prefixes for AA.CLASS.TYPE were DES, PRF, CAT, DATAand SIM for PREFIX.DESIGN, PREFIX.PROOF, PREFIX.CATALOG , PREFIX.INSTANCE and PREFIX.SIMULATION respectively thefive applications created after authorisation of EB.TABLE.DEFINITION would be OA.DES.BASIC.DETAILS,OA.PRF.BASIC.DETAILS, OA.CAT.BASIC.DETAILS, OA.DATA.BASIC.DETAILS and OA.SIM.BASIC.DETAILS respectively Validation Rules: 1.Should be the ID of a valid AA.CLASS.TYPE |
| 38 | `DYN.ACT.RULE.NAME` | `EbTableDefinition_RuleName` |  |  |  |
| 39 | `DYN.ACT.RULE` | `EbTableDefinition_Rule` |  |  |  |
| 40 | `DYN.ACT.PGM.TYPE` | `EbTableDefinition_PgmType` | TField |  | Valid values are U,L For 'U' type only Live and Unauthorized files are created For 'L' type only Live files will be created Default value is 'H' No Change |
| 41 | `DYN.ACT.RESERVED3` | `EbTableDefinition_Reserved3` | TField |  |  |
| 42 | `DYN.ACT.RESERVED2` | `EbTableDefinition_Reserved2` | TField |  |  |
| 43 | `DYN.ACT.OVERRIDE` | `EbTableDefinition_Override` |  |  |  |
| 44 | `DYN.ACT.RECORD.STATUS` | `EbTableDefinition_RecordStatus` | String |  |  |
| 45 | `DYN.ACT.CURR.NO` | `EbTableDefinition_CurrNo` | String |  |  |
| 46 | `DYN.ACT.INPUTTER` | `EbTableDefinition_Inputter` |  |  |  |
| 47 | `DYN.ACT.DATE.TIME` | `EbTableDefinition_DateTime` |  |  |  |
| 48 | `DYN.ACT.AUTHORISER` | `EbTableDefinition_Authoriser` | String |  |  |
| 49 | `DYN.ACT.CO.CODE` | `EbTableDefinition_CoCode` | String |  |  |
| 50 | `DYN.ACT.DEPT.CODE` | `EbTableDefinition_DeptCode` | String |  |  |
| 51 | `DYN.ACT.AUDITOR.CODE` | `EbTableDefinition_AuditorCode` | String |  |  |
| 52 | `DYN.ACT.AUDIT.DATE.TIME` | `EbTableDefinition_AuditDateTime` | String |  |  |
| 53 | `DYN.ACT.TABLE.OWNER` | `EbTableDefinition_TableOwner` | TField |  | Valid values are Core, Feature and Client To indicate if the table is released from Temenos or not |
| 54 | `DYN.ACT.FIELD.OWNER` | `EbTableDefinition_FieldOwner` |  |  |  |
| 55 | `DYN.ACT.PERSONAL.DATA` | `EbTableDefinition_PersonalData` |  |  |  |
| 56 | `DYN.ACT.ATTRIBUTES` | `EbTableDefinition_Attributes` |  |  |  |
| 57 | `DYN.ACT.PURPOSE` | `EbTableDefinition_Purpose` |  |  |  |
| 58 | `DYN.ACT.ERASE.OPTION` | `EbTableDefinition_EraseOption` |  |  |  |
| 59 | `DYN.ACT.ACCESSIBILITY` | `EbTableDefinition_Accessibility` |  |  |  |
