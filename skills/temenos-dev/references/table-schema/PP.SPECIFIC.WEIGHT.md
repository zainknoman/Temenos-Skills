# PP.SPECIFIC.WEIGHT — Table Schema

> Source: `INSERTS/I_F.PP.SPECIFIC.WEIGHT` in `PP_WeightAssignmentService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.SPW.CompanyID` | `PpSpecificWeight_Companyid` | TField |  | Indicates the Financial Table Descriptive(FTD) company for which the record is created. This is NoInput field It gets autopopulated after validation Example : BNK,GB1 |
| 2 | `PP.SPW.Ranking` | `PpSpecificWeight_Ranking` | TField | Yes | Specifies the order (sequence) of the record in the application. Based on the value, a record is prioritised in such a way that, it is given higher preference for selection under peeling logic applied in the payments hub. Validation Rules: Mandatory field. 9 numeric characters. |
| 3 | `PP.SPW.SpecificWeightCode` | `PpSpecificWeight_Specificweightcode` | TField | Yes | The specific weight code that needs to be applied based on the originating source, message type and ranking. Validation Rules: Mandatory field. 3 alphanumeric characters. |
| 4 | `PP.SPW.WeightDescription` | `PpSpecificWeight_Weightdescription` | TField |  | Describes the specific weight code defined. Validation Rules: 128 alphanumeric chracters. |
| 5 | `PP.SPW.WeightCode` | `PpSpecificWeight_Weightcode` | TField |  | Indicates the weight code for which a specific weight code is defined. Possible values: H - High M - Medium L - Light |
| 6 | `PP.SPW.AutoRepairInstanceName` | `PpSpecificWeight_Autorepairinstancename` | TField |  | Indicates the instance to be used for Auto Repair of a payment. |
| 7 | `PP.SPW.StartDate` | `PpSpecificWeight_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Validation Rules: No Input Field If the start date is given in ID then the start date gets populated from the id Or else start date gets populated from the field TODAY in the table DATES |
| 8 | `PP.SPW.EndDate` | `PpSpecificWeight_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 9 | `PP.SPW.RESERVED.5` | `PpSpecificWeight_Reserved5` | TField |  |  |
| 10 | `PP.SPW.RESERVED.4` | `PpSpecificWeight_Reserved4` | TField |  |  |
| 11 | `PP.SPW.RESERVED.3` | `PpSpecificWeight_Reserved3` | TField |  |  |
| 12 | `PP.SPW.RESERVED.2` | `PpSpecificWeight_Reserved2` | TField |  |  |
| 13 | `PP.SPW.RESERVED.1` | `PpSpecificWeight_Reserved1` | TField |  |  |
| 14 | `PP.SPW.LOCAL.REF` | `PpSpecificWeight_LocalRef` |  |  |  |
| 15 | `PP.SPW.OVERRIDE` | `PpSpecificWeight_Override` |  |  |  |
| 16 | `PP.SPW.RECORD.STATUS` | `PpSpecificWeight_RecordStatus` | String |  |  |
| 17 | `PP.SPW.CURR.NO` | `PpSpecificWeight_CurrNo` | String |  |  |
| 18 | `PP.SPW.INPUTTER` | `PpSpecificWeight_Inputter` |  |  |  |
| 19 | `PP.SPW.DATE.TIME` | `PpSpecificWeight_DateTime` |  |  |  |
| 20 | `PP.SPW.AUTHORISER` | `PpSpecificWeight_Authoriser` | String |  |  |
| 21 | `PP.SPW.CO.CODE` | `PpSpecificWeight_CoCode` | String |  |  |
| 22 | `PP.SPW.DEPT.CODE` | `PpSpecificWeight_DeptCode` | String |  |  |
| 23 | `PP.SPW.AUDITOR.CODE` | `PpSpecificWeight_AuditorCode` | String |  |  |
| 24 | `PP.SPW.AUDIT.DATE.TIME` | `PpSpecificWeight_AuditDateTime` | String |  |  |
