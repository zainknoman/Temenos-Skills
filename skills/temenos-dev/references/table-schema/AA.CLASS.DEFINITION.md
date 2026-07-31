# AA.CLASS.DEFINITION — Table Schema

> Source: `INSERTS/I_F.AA.CLASS.DEFINITION` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CDF.SHORT.DESC` | `AaClassDefinition_ShortDesc` |  |  |  |
| 2 | `AA.CDF.FULL.DESC` | `AaClassDefinition_FullDesc` |  |  |  |
| 3 | `AA.CDF.TYPE` | `AaClassDefinition_Type` |  |  |  |
| 4 | `AA.CDF.CLASS.GROUP` | `AaClassDefinition_ClassGroup` | TField |  | This field can be used for grouping of products. The list of groups available can be defined in the EB.LOOKUP file for AA.PC.GROUP. Used for enquiry and display purposes for filtering out the required classes. |
| 5 | `AA.CDF.DEL.INFO.REQD` | `AaClassDefinition_DelInfoReqd` | TField |  | This field denotes whether delivery information is required for the property class. If this field is set to Y then delivery processing is done for the user defined class. |
| 6 | `AA.CDF.PRODUCT` | `AaClassDefinition_Product` | TField |  | A valid product code. The template created will belong to this product and the template name will be prefixed with this product |
| 7 | `AA.CDF.FIELD.NAME` | `AaClassDefinition_FieldName` |  |  |  |
| 8 | `AA.CDF.DESCRIPTION` | `AaClassDefinition_Description` |  |  |  |
| 9 | `AA.CDF.PROMPT.TEXT` | `AaClassDefinition_PromptText` |  |  |  |
| 10 | `AA.CDF.TOOL.TIP` | `AaClassDefinition_ToolTip` |  |  |  |
| 11 | `AA.CDF.CALCULATION` | `AaClassDefinition_Calculation` |  |  |  |
| 12 | `AA.CDF.AVAILABILITY` | `AaClassDefinition_Availability` |  |  |  |
| 13 | `AA.CDF.ACTIVITY.ID` | `AaClassDefinition_ActivityId` |  |  |  |
| 14 | `AA.CDF.ACTIVITY.FLD` | `AaClassDefinition_ActivityFld` |  |  |  |
| 15 | `AA.CDF.MAX.CHAR` | `AaClassDefinition_MaxChar` |  |  |  |
| 16 | `AA.CDF.MIN.CHAR` | `AaClassDefinition_MinChar` |  |  |  |
| 17 | `AA.CDF.DATA.TYPE` | `AaClassDefinition_DataType` |  |  |  |
| 18 | `AA.CDF.CCY.ACTIVITY` | `AaClassDefinition_CcyActivity` |  |  |  |
| 19 | `AA.CDF.CCY.ACT.FLD` | `AaClassDefinition_CcyActFld` |  |  |  |
| 20 | `AA.CDF.VETTING.TABLE` | `AaClassDefinition_VettingTable` |  |  |  |
| 21 | `AA.CDF.APPL.VET` | `AaClassDefinition_ApplVet` |  |  |  |
| 22 | `AA.CDF.APPL.ENRICH.FLD` | `AaClassDefinition_ApplEnrichFld` |  |  |  |
| 23 | `AA.CDF.DEF.VALUE` | `AaClassDefinition_DefValue` |  |  |  |
| 24 | `AA.CDF.FLD.PROPERTY` | `AaClassDefinition_FldProperty` |  |  |  |
| 25 | `AA.CDF.MASKING.FMT` | `AaClassDefinition_MaskingFmt` |  |  |  |
| 26 | `AA.CDF.VIRTUAL.TABLE` | `AaClassDefinition_VirtualTable` |  |  |  |
| 27 | `AA.CDF.SUB.ASSOC.CODE` | `AaClassDefinition_SubAssocCode` |  |  |  |
| 28 | `AA.CDF.REL.DATE.FIELD` | `AaClassDefinition_RelDateField` |  |  |  |
| 29 | `AA.CDF.REL.CURRENCY.FIELD` | `AaClassDefinition_RelCurrencyField` |  |  |  |
| 30 | `AA.CDF.FLD.PRODUCT` | `AaClassDefinition_FldProduct` |  |  |  |
| 31 | `AA.CDF.PHYSICAL.POSITION` | `AaClassDefinition_PhysicalPosition` |  |  |  |
| 32 | `AA.CDF.RESERVED11` | `AaClassDefinition_Reserved11` |  |  |  |
| 33 | `AA.CDF.PREFIX` | `AaClassDefinition_Prefix` | TField | Yes | The prefix needed to address all the fields defined in the dynamic application. Value entered here will become the prefix for this dynamic application with product. (e.g: if name given here is TEST and product is EB then prefix of the dynamic application becomes EB.TEST.fieldname). 1.Field can accept alpha numeric values 2.NOCHANGE field - can�t change the prefix of the insert file once the record being authorized 3.Mandatory field |
| 34 | `AA.CDF.FILE.TYPE` | `AaClassDefinition_FileType` | TField |  | Defines the type of the file. The allowed values are FIN, CUS and INT |
| 35 | `AA.CDF.LINK.TO.WFL` | `AaClassDefinition_LinkToWfl` | TField |  | Using this field the user can define whether the application should be linked to the workflow. If the value of this field is set to NO, then the record in the application cannot be kept on HOLD after first input |
| 36 | `AA.CDF.NS.OPERATION` | `AaClassDefinition_NsOperation` | TField |  | NS.OPERATION field will determine if this application will allow entry / modification during the close of business This field should allow only three input ALL,NEW and NOD ALL - Application alows NS operation NEW - Application allows NS operation for NEW id�s only NOD - Can be run Non Stop without the NS module installed |
| 37 | `AA.CDF.KEY.FIELD` | `AaClassDefinition_KeyField` | TField | Yes | Holds any one of the field name from the multi value set which field become an ID of the dynamic template. properties of that specified field is becomes the properties of the ID for dynamic template. 1.Corresponding field should accept the ALPHA, DATE, ALPHANUMERIC,NUMERIC and TEXT data types. 2.should be valid name from the FIELD.NAME multi value set 3.Non �Mandatory field |
| 38 | `AA.CDF.INSERT.LAYOUT` | `AaClassDefinition_InsertLayout` | TField | Yes | We can specify the location of the insert file. Insert file for the dynamic template will be created under the directory name specified here. If there is no mentioned directory present then T24 will automatically create that directory and place the insert file under the directory. 1.Non �Mandatory field |
| 39 | `AA.CDF.ADD.SPECIAL.FIELDS` | `AaClassDefinition_AddSpecialFields` |  |  |  |
| 40 | `AA.CDF.LOCAL.REF` | `AaClassDefinition_LocalRef` |  |  |  |
| 41 | `AA.CDF.CLASS.TYPE` | `AaClassDefinition_ClassType` | TField | Yes | This is mandatory field, where the user want to specify the class type in which the attributes should be created. System will use this data to create design, proof, catalog, simulation and instance level dynamic templates for the class definition. Validation Rules: 1. Valid entry from AA.CLASS.TYPE application. |
| 42 | `AA.CDF.RULE.NAME` | `AaClassDefinition_RuleName` |  |  |  |
| 43 | `AA.CDF.RULE` | `AaClassDefinition_Rule` |  |  |  |
| 44 | `AA.CDF.PGM.TYPE` | `AaClassDefinition_PgmType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 45 | `AA.CDF.RESERVED3` | `AaClassDefinition_Reserved3` | TField |  |  |
| 46 | `AA.CDF.RESERVED2` | `AaClassDefinition_Reserved2` | TField |  |  |
| 47 | `AA.CDF.OVERRIDE` | `AaClassDefinition_Override` |  |  |  |
| 48 | `AA.CDF.RECORD.STATUS` | `AaClassDefinition_RecordStatus` | String |  |  |
| 49 | `AA.CDF.CURR.NO` | `AaClassDefinition_CurrNo` | String |  |  |
| 50 | `AA.CDF.INPUTTER` | `AaClassDefinition_Inputter` |  |  |  |
| 51 | `AA.CDF.DATE.TIME` | `AaClassDefinition_DateTime` |  |  |  |
| 52 | `AA.CDF.AUTHORISER` | `AaClassDefinition_Authoriser` | String |  |  |
| 53 | `AA.CDF.CO.CODE` | `AaClassDefinition_CoCode` | String |  |  |
| 54 | `AA.CDF.DEPT.CODE` | `AaClassDefinition_DeptCode` | String |  |  |
| 55 | `AA.CDF.AUDITOR.CODE` | `AaClassDefinition_AuditorCode` | String |  |  |
| 56 | `AA.CDF.AUDIT.DATE.TIME` | `AaClassDefinition_AuditDateTime` | String |  |  |
| 57 | `AA.CDF.TABLE.OWNER` | `AaClassDefinition_TableOwner` | TField |  | Valid values are Core, Feature and Client To indicate if the table is released from Temenos or not |
| 58 | `AA.CDF.FIELD.OWNER` | `AaClassDefinition_FieldOwner` |  |  |  |
| 59 | `AA.CDF.PERSONAL.DATA` | `AaClassDefinition_PersonalData` |  |  |  |
| 60 | `AA.CDF.ATTRIBUTES` | `AaClassDefinition_Attributes` |  |  |  |
| 61 | `AA.CDF.PURPOSE` | `AaClassDefinition_Purpose` |  |  |  |
| 62 | `AA.CDF.ERASE.OPTION` | `AaClassDefinition_EraseOption` |  |  |  |
| 63 | `AA.CDF.ACCESSIBILITY` | `AaClassDefinition_Accessibility` |  |  |  |
