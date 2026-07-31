# AA.CLASS.APPL.CONDITION — Table Schema

> Source: `INSERTS/I_F.AA.CLASS.APPL.CONDITION` in `AA_IntegrationFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CAC.DESCRIPTION` | `AaClassApplCondition_Description` |  |  |  |
| 2 | `AA.CAC.TRANS.ELEMENT.NAME` | `AaClassApplCondition_TransElementName` |  |  |  |
| 3 | `AA.CAC.TRANS.APPLICATION.NAME` | `AaClassApplCondition_TransApplicationName` |  |  |  |
| 4 | `AA.CAC.TRANS.NAU.SUFFIX` | `AaClassApplCondition_TransNauSuffix` |  |  |  |
| 5 | `AA.CAC.RESERVED.11` | `AaClassApplCondition_Reserved11` | TField |  |  |
| 6 | `AA.CAC.RESERVED.10` | `AaClassApplCondition_Reserved10` | TField |  |  |
| 7 | `AA.CAC.RESERVED.9` | `AaClassApplCondition_Reserved9` | TField |  |  |
| 8 | `AA.CAC.STATIC.ELEMENT.NAME` | `AaClassApplCondition_StaticElementName` |  |  |  |
| 9 | `AA.CAC.STATIC.APPLICATION.NAME` | `AaClassApplCondition_StaticApplicationName` |  |  |  |
| 10 | `AA.CAC.STATIC.NAU.SUFFIX` | `AaClassApplCondition_StaticNauSuffix` |  |  |  |
| 11 | `AA.CAC.STATIC.KEY.HOOK.RTN` | `AaClassApplCondition_StaticKeyHookRtn` |  |  |  |
| 12 | `AA.CAC.RESERVED.7` | `AaClassApplCondition_Reserved7` | TField |  |  |
| 13 | `AA.CAC.RESERVED.6` | `AaClassApplCondition_Reserved6` | TField |  |  |
| 14 | `AA.CAC.MASTER.ELEMENT.NAME` | `AaClassApplCondition_MasterElementName` | TField |  | The element name for a master application(i.e. AA.ARRANGEMENT.ACTIVITY) will be used in IF to expose the details to the external system. Released and maintained by Temenos. |
| 15 | `AA.CAC.MASTER.APPLICATION.NAME` | `AaClassApplCondition_MasterApplicationName` | TField |  | T24 application which needs to map aginst the corresponding to the element. So the corresponding record will be captured while having an update to this table. Released and maintained by Temenos. This image only be extracted if the corresponding table is updated by this transaction. |
| 16 | `AA.CAC.MASTER.NAU.SUFFIX` | `AaClassApplCondition_MasterNauSuffix` | TField |  | T24 application prefix which holds the NAU records. Released and maintained by Temenos. So the corresponding record will be captured while having an update to this table. This image only be extracted if the corresponding table is updated by this transaction |
| 17 | `AA.CAC.CUSTOM.ELEMENT.NAME` | `AaClassApplCondition_CustomElementName` |  |  |  |
| 18 | `AA.CAC.CUSTOM.APPLICATION.NAME` | `AaClassApplCondition_CustomApplicationName` |  |  |  |
| 19 | `AA.CAC.CUSTOM.NAU.SUFFIX` | `AaClassApplCondition_CustomNauSuffix` |  |  |  |
| 20 | `AA.CAC.CUSTOM.DATA.COLLECTION.HOOK` | `AaClassApplCondition_CustomDataCollectionHook` |  |  |  |
| 21 | `AA.CAC.CUSTOM.ELEMENT.FILTER` | `AaClassApplCondition_CustomElementFilter` |  |  |  |
| 22 | `AA.CAC.OVERRIDE` | `AaClassApplCondition_Override` |  |  |  |
| 23 | `AA.CAC.RECORD.STATUS` | `AaClassApplCondition_RecordStatus` | String |  |  |
| 24 | `AA.CAC.CURR.NO` | `AaClassApplCondition_CurrNo` | String |  |  |
| 25 | `AA.CAC.INPUTTER` | `AaClassApplCondition_Inputter` |  |  |  |
| 26 | `AA.CAC.DATE.TIME` | `AaClassApplCondition_DateTime` |  |  |  |
| 27 | `AA.CAC.AUTHORISER` | `AaClassApplCondition_Authoriser` | String |  |  |
| 28 | `AA.CAC.CO.CODE` | `AaClassApplCondition_CoCode` | String |  |  |
| 29 | `AA.CAC.DEPT.CODE` | `AaClassApplCondition_DeptCode` | String |  |  |
| 30 | `AA.CAC.AUDITOR.CODE` | `AaClassApplCondition_AuditorCode` | String |  |  |
| 31 | `AA.CAC.AUDIT.DATE.TIME` | `AaClassApplCondition_AuditDateTime` | String |  |  |
