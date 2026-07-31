# SC.ESG.INDICATOR — Table Schema

> Source: `INSERTS/I_F.SC.ESG.INDICATOR` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ESGI.DESCRIPTION` | `ScEsgIndicator_Description` |  |  |  |
| 2 | `SC.ESGI.STATIC.FIELD.NAME` | `ScEsgIndicator_StaticFieldName` | TField |  | This field specifies Field name used in SM.ESG.SCORES Applicable only if Static Indicators / Fields are directly provided If inputted INDICATOR.CATEGORY,ESG.PILLAR,DATA.TYPE,LOOKUP.TABLE are hardcoded |
| 3 | `SC.ESGI.INDICATOR.CATEGORY` | `ScEsgIndicator_IndicatorCategory` | TField | Yes | This field specifies Category of indicator Allowed values areA) RatingB) ControversiesC) ScreeningD) SDGE) ClassificationF) Eu TaxonomyG) SFDR Adverse Impact It is a mandatory field. |
| 4 | `SC.ESGI.E.S.G.PILLAR` | `ScEsgIndicator_ESGPillar` | TField |  | This field specifies Pillar for indicator Allowed values areA) EnvironmentB) SocialC)Governance |
| 5 | `SC.ESGI.DATA.TYPE` | `ScEsgIndicator_DataType` | TField | Yes | This field specifies DataType accepted by indicators Allowed data types as below.A) Numeric - Allows NumbersB) Text - applicable only when static field name is CONTROVERSY.OVERALL.SUMMARYC) Alpha Numeric - Allows Numbers as well as AlphabetsD) Lookup - Refers to dynamic dropdown based on EB.LOOKUPE) YesOrNo - Accepts either Yes / NoF) Date - Hold a valid date format It is a mandatory field. |
| 6 | `SC.ESGI.LOOKUP.TABLE` | `ScEsgIndicator_LookupTable` | TField |  | This field specifies Prefix ID used in EB.LOOKUP when Data Type is defined as Lookup. For ex : If EB.LOOKUP records are OVERALL.RATING*1 , OVERALL.RATING*2 etc.. , then this field is expected to be updated as OVERALL.RATING |
| 7 | `SC.ESGI.OTHER.ATTR` | `ScEsgIndicator_OtherAttr` |  |  |  |
| 8 | `SC.ESGI.OTHER.ATTR.VAL` | `ScEsgIndicator_OtherAttrVal` |  |  |  |
| 9 | `SC.ESGI.RESERVED.01` | `ScEsgIndicator_Reserved01` | TField |  |  |
| 10 | `SC.ESGI.RESERVED.02` | `ScEsgIndicator_Reserved02` | TField |  |  |
| 11 | `SC.ESGI.RESERVED.03` | `ScEsgIndicator_Reserved03` | TField |  |  |
| 12 | `SC.ESGI.RESERVED.04` | `ScEsgIndicator_Reserved04` | TField |  |  |
| 13 | `SC.ESGI.RESERVED.05` | `ScEsgIndicator_Reserved05` | TField |  |  |
| 14 | `SC.ESGI.LOCAL.REF` | `ScEsgIndicator_LocalRef` |  |  |  |
| 15 | `SC.ESGI.OVERRIDE` | `ScEsgIndicator_Override` |  |  |  |
| 16 | `SC.ESGI.RECORD.STATUS` | `ScEsgIndicator_RecordStatus` | String |  |  |
| 17 | `SC.ESGI.CURR.NO` | `ScEsgIndicator_CurrNo` | String |  |  |
| 18 | `SC.ESGI.INPUTTER` | `ScEsgIndicator_Inputter` |  |  |  |
| 19 | `SC.ESGI.DATE.TIME` | `ScEsgIndicator_DateTime` |  |  |  |
| 20 | `SC.ESGI.AUTHORISER` | `ScEsgIndicator_Authoriser` | String |  |  |
| 21 | `SC.ESGI.CO.CODE` | `ScEsgIndicator_CoCode` | String |  |  |
| 22 | `SC.ESGI.DEPT.CODE` | `ScEsgIndicator_DeptCode` | String |  |  |
| 23 | `SC.ESGI.AUDITOR.CODE` | `ScEsgIndicator_AuditorCode` | String |  |  |
| 24 | `SC.ESGI.AUDIT.DATE.TIME` | `ScEsgIndicator_AuditDateTime` | String |  |  |
