# IRS.FIRE.FILE.REQUEST — Table Schema

> Source: `INSERTS/I_F.IRS.FIRE.FILE.REQUEST` in `USREGS_YearEndTaxReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IRS.REQ.YEAR` | `IrsFireFileRequest_Year` | TField |  | The financial year for which IRS file extraction has to be executed. Only prior years allowed for corrections This will support file extraction upto 7 years; if user give year older than 7 years prior then system raise error. Max 4 numeric values |
| 2 | `IRS.REQ.FORM.TYPE` | `IrsFireFileRequest_FormType` |  |  |  |
| 3 | `IRS.REQ.FILE.TYPE` | `IrsFireFileRequest_FileType` | TField |  | The type of filing has to be defined here. The values available are Original, 1-Step and 2-Step. Original - The original file generation will include all tax data for requested financial year 1-Step - The 1-Step correction will include the tax data which got updated for amount corrections. 2-Step - The 2-Step correction will include the tax data for the customer level changes like name, TIN number. |
| 4 | `IRS.REQ.STATE` | `IrsFireFileRequest_State` | TField |  | This filed has to be used only when required to generate IRS file for a specific state which is not participating in the CF/SF program. A seprate file will get generated for the requested state. It must be a valid recod in US.STATE table. |
| 5 | `IRS.REQ.STATUS` | `IrsFireFileRequest_Status` | TField |  | The status of the submitted request will get updated in this field. Pending - The request just submitted and yet to process. Processing - System picked the request and processing. Completed - The request has been processed and file got generated. |
| 6 | `IRS.REQ.RESERVED.15` | `IrsFireFileRequest_Reserved15` | TField |  |  |
| 7 | `IRS.REQ.RESERVED.14` | `IrsFireFileRequest_Reserved14` | TField |  |  |
| 8 | `IRS.REQ.RESERVED.13` | `IrsFireFileRequest_Reserved13` | TField |  |  |
| 9 | `IRS.REQ.RESERVED.12` | `IrsFireFileRequest_Reserved12` | TField |  |  |
| 10 | `IRS.REQ.RESERVED.11` | `IrsFireFileRequest_Reserved11` | TField |  |  |
| 11 | `IRS.REQ.RESERVED.10` | `IrsFireFileRequest_Reserved10` | TField |  |  |
| 12 | `IRS.REQ.RESERVED.9` | `IrsFireFileRequest_Reserved9` | TField |  |  |
| 13 | `IRS.REQ.RESERVED.8` | `IrsFireFileRequest_Reserved8` | TField |  |  |
| 14 | `IRS.REQ.RESERVED.7` | `IrsFireFileRequest_Reserved7` | TField |  |  |
| 15 | `IRS.REQ.RESERVED.6` | `IrsFireFileRequest_Reserved6` | TField |  |  |
| 16 | `IRS.REQ.RESERVED.5` | `IrsFireFileRequest_Reserved5` | TField |  |  |
| 17 | `IRS.REQ.RESERVED.4` | `IrsFireFileRequest_Reserved4` | TField |  |  |
| 18 | `IRS.REQ.RESERVED.3` | `IrsFireFileRequest_Reserved3` | TField |  |  |
| 19 | `IRS.REQ.RESERVED.2` | `IrsFireFileRequest_Reserved2` | TField |  |  |
| 20 | `IRS.REQ.RESERVED.1` | `IrsFireFileRequest_Reserved1` | TField |  |  |
| 21 | `IRS.REQ.LOCAL.REF` | `IrsFireFileRequest_LocalRef` |  |  |  |
| 22 | `IRS.REQ.OVERRIDE` | `IrsFireFileRequest_Override` |  |  |  |
| 23 | `IRS.REQ.RECORD.STATUS` | `IrsFireFileRequest_RecordStatus` | String |  |  |
| 24 | `IRS.REQ.CURR.NO` | `IrsFireFileRequest_CurrNo` | String |  |  |
| 25 | `IRS.REQ.INPUTTER` | `IrsFireFileRequest_Inputter` |  |  |  |
| 26 | `IRS.REQ.DATE.TIME` | `IrsFireFileRequest_DateTime` |  |  |  |
| 27 | `IRS.REQ.AUTHORISER` | `IrsFireFileRequest_Authoriser` | String |  |  |
| 28 | `IRS.REQ.CO.CODE` | `IrsFireFileRequest_CoCode` | String |  |  |
| 29 | `IRS.REQ.DEPT.CODE` | `IrsFireFileRequest_DeptCode` | String |  |  |
| 30 | `IRS.REQ.AUDITOR.CODE` | `IrsFireFileRequest_AuditorCode` | String |  |  |
| 31 | `IRS.REQ.AUDIT.DATE.TIME` | `IrsFireFileRequest_AuditDateTime` | String |  |  |
