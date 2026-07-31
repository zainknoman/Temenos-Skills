# AA.SDB.BOX — Table Schema

> Source: `INSERTS/I_F.AA.SDB.BOX` in `BX_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.BX.DESCRIPTION` | `AaSdbBox_Description` |  |  |  |
| 2 | `AA.BX.BOX.TYPE` | `AaSdbBox_BoxType` | TField |  | Specifies the Box type of the box record. |
| 3 | `AA.BX.ALTERNATE.ID` | `AaSdbBox_AlternateId` | TField |  | Holds the alternate ID of the box. Alphanumeric, linked to EB.ALTERNATE.KEY. This means user can access the record by using the alternate id saved in this field. Bank can specify id of record in their legacy system. |
| 4 | `AA.BX.LOCATION` | `AaSdbBox_Location` |  |  |  |
| 5 | `AA.BX.STATUS` | `AaSdbBox_Status` | TField |  | Indicates the current status of the Box. The field contains drop down options from AA.SDB.STATUS virtual table (EB.LOOKUP) where the user can define their own status. However the following system defined status are released. Available, Rented, Reserved and Maintenance. Validation Rules: If the status is changed manually by the user, then only the below status changes below are permitted. � Available -&gt; Maintenance / Reserved � Reserved -&gt; Available / Maintenance � Maintenance -&gt; Available / Reserved. |
| 6 | `AA.BX.ARRANGEMENT.ID` | `AaSdbBox_ArrangementId` | TField |  | Contains the Arrangement ID to which the box is linked. Vetting ARRANGEMENT.ID. The field is a No Input, System maintained field. It is Linked to the EB.ALTERNATE.KEY. This means the user will be able to access the record by using the alternate id. |
| 7 | `AA.BX.KEY.NO` | `AaSdbBox_KeyNo` |  |  |  |
| 8 | `AA.BX.LOCAL.REF` | `AaSdbBox_LocalRef` |  |  |  |
| 9 | `AA.BX.STATUS.REASON` | `AaSdbBox_StatusReason` | TField |  |  |
| 10 | `AA.BX.LAST.UPDATE.DATE` | `AaSdbBox_LastUpdateDate` | TField |  |  |
| 11 | `AA.BX.RESERVED3` | `AaSdbBox_Reserved3` | TField |  |  |
| 12 | `AA.BX.RESERVED2` | `AaSdbBox_Reserved2` | TField |  |  |
| 13 | `AA.BX.RESERVED1` | `AaSdbBox_Reserved1` | TField |  |  |
| 14 | `AA.BX.RECORD.STATUS` | `AaSdbBox_RecordStatus` | String |  |  |
| 15 | `AA.BX.CURR.NO` | `AaSdbBox_CurrNo` | String |  |  |
| 16 | `AA.BX.INPUTTER` | `AaSdbBox_Inputter` |  |  |  |
| 17 | `AA.BX.DATE.TIME` | `AaSdbBox_DateTime` |  |  |  |
| 18 | `AA.BX.AUTHORISER` | `AaSdbBox_Authoriser` | String |  |  |
| 19 | `AA.BX.CO.CODE` | `AaSdbBox_CoCode` | String |  |  |
| 20 | `AA.BX.DEPT.CODE` | `AaSdbBox_DeptCode` | String |  |  |
| 21 | `AA.BX.AUDITOR.CODE` | `AaSdbBox_AuditorCode` | String |  |  |
| 22 | `AA.BX.AUDIT.DATE.TIME` | `AaSdbBox_AuditDateTime` | String |  |  |
