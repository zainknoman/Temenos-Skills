# SALBLK.SAL.BLOCK.PARAM — Table Schema

> Source: `INSERTS/I_F.SALBLK.SAL.BLOCK.PARAM` in `SALBLK_SalaryBlocking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SAL.BLK.PAR.DESCRIPTION` | `SalblkSalBlockParam_Description` |  |  |  |
| 2 | `SAL.BLK.PAR.OFS.SOURCE` | `SalblkSalBlockParam_OfsSource` | TField |  | This field identifies the ofs source record to be used while creating record in AC.LOCKED.EVENT. 1. A valid record must be present in OFS.SOURCE table. 2. OFS.SOURCE record used here must be of GLOBUS type. |
| 3 | `SAL.BLK.PAR.ACLK.VERSION` | `SalblkSalBlockParam_AclkVersion` | TField |  | This field is to identify that version to be used while posting the ofs message to create record in AC.LOCKED.EVENTS. A valid entry should be present in Version application. |
| 4 | `SAL.BLK.PAR.ACLK.DAYS` | `SalblkSalBlockParam_AclkDays` | TField |  | This field denotes the number of days to be taken to update the date on which lock should be released. ie, Field TO.DATE in AC.LOCKED.EVENTS should be updated with next payment date of Loan added with no. of days given in this field. |
| 5 | `SAL.BLK.PAR.CCY.MARKET` | `SalblkSalBlockParam_CcyMarket` | TField |  | This field is for future use. |
| 6 | `SAL.BLK.PAR.EMPLOYER.CUSTID` | `SalblkSalBlockParam_EmployerCustid` |  |  |  |
| 7 | `SAL.BLK.PAR.CATEGORY.CODE` | `SalblkSalBlockParam_CategoryCode` |  |  |  |
| 8 | `SAL.BLK.PAR.EXEMPT.PRODUCT` | `SalblkSalBlockParam_ExemptProduct` |  |  |  |
| 9 | `SAL.BLK.PAR.EMPLOYEE.CUSTID` | `SalblkSalBlockParam_EmployeeCustid` |  |  |  |
| 10 | `SAL.BLK.PAR.RELATION.CODE` | `SalblkSalBlockParam_RelationCode` |  |  |  |
| 11 | `SAL.BLK.PAR.LOCK.REASON` | `SalblkSalBlockParam_LockReason` | TField |  | This field stores the description of the field Description in AC.LOCKED.EVENTS. When entry gets created in AC.LOCKED.EVENTS for salary blocking then description field will be updated with LOCK.REASON |
| 12 | `SAL.BLK.PAR.LOCK.REV.VERSION` | `SalblkSalBlockParam_LockRevVersion` | TField |  | This field is to identify the version to be used while posting the ofs message to reverse records in AC.LOCKED.EVENTS. A valid entry should be present in Version application. |
| 13 | `SAL.BLK.PAR.LOCK.BATCH.NAME` | `SalblkSalBlockParam_LockBatchName` | TField |  | This field is to identify the service to be used while reversing records in AC.LOCKED.EVENTS through Domiciliation. A valid entry should be present in TSA.SERVICE application. |
| 14 | `SAL.BLK.PAR.SAL.MAX.PERIOD` | `SalblkSalBlockParam_SalMaxPeriod` | TField |  | This field will hold number of calendar days which will be used for checking for the maximum number of days forward before blocking a salary amount. ie, difference between the next instalment date and current system date is greater than the SAL.MAX.PERIOD then system should not place any lock. |
| 15 | `SAL.BLK.PAR.SETTLEMT.AC.OR.CUS` | `SalblkSalBlockParam_SettlemtAcOrCus` |  |  |  |
| 16 | `SAL.BLK.PAR.RESERVED.10` | `SalblkSalBlockParam_Reserved10` | TField |  |  |
| 17 | `SAL.BLK.PAR.RESERVED.9` | `SalblkSalBlockParam_Reserved9` | TField |  |  |
| 18 | `SAL.BLK.PAR.RESERVED.8` | `SalblkSalBlockParam_Reserved8` | TField |  |  |
| 19 | `SAL.BLK.PAR.RESERVED.7` | `SalblkSalBlockParam_Reserved7` | TField |  |  |
| 20 | `SAL.BLK.PAR.RESERVED.6` | `SalblkSalBlockParam_Reserved6` | TField |  |  |
| 21 | `SAL.BLK.PAR.RESERVED.5` | `SalblkSalBlockParam_Reserved5` | TField |  |  |
| 22 | `SAL.BLK.PAR.RESERVED.4` | `SalblkSalBlockParam_Reserved4` | TField |  |  |
| 23 | `SAL.BLK.PAR.RESERVED.3` | `SalblkSalBlockParam_Reserved3` | TField |  |  |
| 24 | `SAL.BLK.PAR.RESERVED.2` | `SalblkSalBlockParam_Reserved2` | TField |  |  |
| 25 | `SAL.BLK.PAR.RESERVED.1` | `SalblkSalBlockParam_Reserved1` | TField |  |  |
| 26 | `SAL.BLK.PAR.LOCAL.REF` | `SalblkSalBlockParam_LocalRef` |  |  |  |
| 27 | `SAL.BLK.PAR.OVERRIDE` | `SalblkSalBlockParam_Override` |  |  |  |
| 28 | `SAL.BLK.PAR.RECORD.STATUS` | `SalblkSalBlockParam_RecordStatus` | String |  |  |
| 29 | `SAL.BLK.PAR.CURR.NO` | `SalblkSalBlockParam_CurrNo` | String |  |  |
| 30 | `SAL.BLK.PAR.INPUTTER` | `SalblkSalBlockParam_Inputter` |  |  |  |
| 31 | `SAL.BLK.PAR.DATE.TIME` | `SalblkSalBlockParam_DateTime` |  |  |  |
| 32 | `SAL.BLK.PAR.AUTHORISER` | `SalblkSalBlockParam_Authoriser` | String |  |  |
| 33 | `SAL.BLK.PAR.CO.CODE` | `SalblkSalBlockParam_CoCode` | String |  |  |
| 34 | `SAL.BLK.PAR.DEPT.CODE` | `SalblkSalBlockParam_DeptCode` | String |  |  |
| 35 | `SAL.BLK.PAR.AUDITOR.CODE` | `SalblkSalBlockParam_AuditorCode` | String |  |  |
| 36 | `SAL.BLK.PAR.AUDIT.DATE.TIME` | `SalblkSalBlockParam_AuditDateTime` | String |  |  |
