# EB.PROJECT.MANAGER — Table Schema

> Source: `INSERTS/I_F.EB.PROJECT.MANAGER` in `AA_ProductManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.PM.DESCRIPTION` | `EbProjectManager_Description` |  |  |  |
| 2 | `EB.PM.FULL.DESCRIPTION` | `EbProjectManager_FullDescription` |  |  |  |
| 3 | `EB.PM.PROJECT.TYPE` | `EbProjectManager_ProjectType` | TField |  | Describes the type of project, currently only supports AA, which means created within AA Product Builder |
| 4 | `EB.PM.USER` | `EbProjectManager_User` | TField |  | "Describes the USER who created the project System maintained field" |
| 5 | `EB.PM.ACTION` | `EbProjectManager_Action` | TField |  | "Describes the current action performed on the project, ADD - Amended recrods to the project, ie either added or deleted to the project DELETE - Entire project to be deleted COMMIT - Authorise the records that are in the project and are in held status ARCHIVE - Archive the project" |
| 6 | `EB.PM.RESERVED.15` | `EbProjectManager_Reserved15` | TField |  |  |
| 7 | `EB.PM.RESERVED.14` | `EbProjectManager_Reserved14` | TField |  |  |
| 8 | `EB.PM.RESERVED.13` | `EbProjectManager_Reserved13` | TField |  |  |
| 9 | `EB.PM.RESERVED.12` | `EbProjectManager_Reserved12` | TField |  |  |
| 10 | `EB.PM.RESERVED.11` | `EbProjectManager_Reserved11` | TField |  |  |
| 11 | `EB.PM.APPLICATION` | `EbProjectManager_Application` |  |  |  |
| 12 | `EB.PM.FUNCTION` | `EbProjectManager_Function` |  |  |  |
| 13 | `EB.PM.COMPANY.CODE` | `EbProjectManager_CompanyCode` |  |  |  |
| 14 | `EB.PM.RECORD.KEY` | `EbProjectManager_RecordKey` |  |  |  |
| 15 | `EB.PM.RESERVED.10` | `EbProjectManager_Reserved10` | TField |  |  |
| 16 | `EB.PM.RESERVED.9` | `EbProjectManager_Reserved9` | TField |  |  |
| 17 | `EB.PM.RESERVED.8` | `EbProjectManager_Reserved8` | TField |  |  |
| 18 | `EB.PM.RESERVED.7` | `EbProjectManager_Reserved7` | TField |  |  |
| 19 | `EB.PM.RESERVED.6` | `EbProjectManager_Reserved6` | TField |  |  |
| 20 | `EB.PM.LINKED.APPLICATION` | `EbProjectManager_LinkedApplication` |  |  |  |
| 21 | `EB.PM.LINKED.REC.COM` | `EbProjectManager_LinkedRecCom` |  |  |  |
| 22 | `EB.PM.LINKED.RECORDKEY` | `EbProjectManager_LinkedRecordkey` |  |  |  |
| 23 | `EB.PM.CREATION.DATE` | `EbProjectManager_CreationDate` | TField |  | "Describes the project creation date System maintained" |
| 24 | `EB.PM.LAST.UPDATE.DATE` | `EbProjectManager_LastUpdateDate` | TField |  | "Describes the date on which the project was last updated System maintained" |
| 25 | `EB.PM.COMMIT.MODE` | `EbProjectManager_CommitMode` | TField |  | This field will describes how the underlying project manager records defined in APPLICATION field of the EB.PROJECT.MANAGER is going to be created as part of product creation. It accepts two values Online � All the Application records defined in the project such as AA.PRD.DES.XXX, AA.PROPERTY,AA.BALANCE.TYPE etc. will be created online itself i.e. when committing the EB.PROJECT.MANAGER definition. Service � While authorizing the EB.PROJECT.MANAGER the record key will get updated in the service list file EB.PROJECT.MANAGER.SERVICE.LIST. Then EB.PROJECT.MANAGER.SERVICE will pick it up this key and create the Application records as part of service processing. |
| 26 | `EB.PM.PROCESS.KEY` | `EbProjectManager_ProcessKey` |  |  |  |
| 27 | `EB.PM.PROCESS.STATUS` | `EbProjectManager_ProcessStatus` |  |  |  |
| 28 | `EB.PM.PROCESS.ERROR` | `EbProjectManager_ProcessError` |  |  |  |
| 29 | `EB.PM.PROCESS.OVERRIDE` | `EbProjectManager_ProcessOverride` |  |  |  |
| 30 | `EB.PM.STATUS` | `EbProjectManager_Status` | TField |  | It is System populated field. This field describes the overall Status of the Project. It will accept two values. Completed � If all the underlying all project applications are created successfully then this field will get updated with Status as Completed. Error � If anyone of the underlying project application record creation failed then this field will get updated with the status as Error. |
| 31 | `EB.PM.RESERVED.5` | `EbProjectManager_Reserved5` | TField |  |  |
| 32 | `EB.PM.RESERVED.4` | `EbProjectManager_Reserved4` | TField |  |  |
| 33 | `EB.PM.RESERVED.3` | `EbProjectManager_Reserved3` | TField |  |  |
| 34 | `EB.PM.RESERVED.2` | `EbProjectManager_Reserved2` | TField |  |  |
| 35 | `EB.PM.OVERRIDE` | `EbProjectManager_Override` |  |  |  |
| 36 | `EB.PM.RECORD.STATUS` | `EbProjectManager_RecordStatus` | String |  |  |
| 37 | `EB.PM.CURR.NO` | `EbProjectManager_CurrNo` | String |  |  |
| 38 | `EB.PM.INPUTTER` | `EbProjectManager_Inputter` |  |  |  |
| 39 | `EB.PM.DATE.TIME` | `EbProjectManager_DateTime` |  |  |  |
| 40 | `EB.PM.AUTHORISER` | `EbProjectManager_Authoriser` | String |  |  |
| 41 | `EB.PM.CO.CODE` | `EbProjectManager_CoCode` | String |  |  |
| 42 | `EB.PM.DEPT.CODE` | `EbProjectManager_DeptCode` | String |  |  |
| 43 | `EB.PM.AUDITOR.CODE` | `EbProjectManager_AuditorCode` | String |  |  |
| 44 | `EB.PM.AUDIT.DATE.TIME` | `EbProjectManager_AuditDateTime` | String |  |  |
