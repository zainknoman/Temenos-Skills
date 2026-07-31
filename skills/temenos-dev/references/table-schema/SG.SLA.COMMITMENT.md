# SG.SLA.COMMITMENT — Table Schema

> Source: `INSERTS/I_F.SG.SLA.COMMITMENT` in `SG_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SG.SLA.COMMITMENT.SG.SLA.KEY` | `SgSlaCommitment_SgSlaKey` | TField | Yes | It should be Key to SG.SLA application Validation Rules: =============== Mandatory Input. Must be valid record from SG.SLA application |
| 2 | `SG.SLA.COMMITMENT.CUSTOMER` | `SgSlaCommitment_Customer` | TField |  | Customer for whom service is to be rendered. Validation Rules: =============== Must be a valid record from CUSTOMER application |
| 3 | `SG.SLA.COMMITMENT.COMPANY` | `SgSlaCommitment_Company` | TField |  | Company for which the SLA Monitoring is sought. Validation Rules: =============== Should be valid record from COMAPNY application |
| 4 | `SG.SLA.COMMITMENT.DAO.ID` | `SgSlaCommitment_DaoId` | TField |  | Department account officer for whom alert to be sent. Validation Rules: =============== Must be a valid record from DEPT.ACCT.OFFICER application. |
| 5 | `SG.SLA.COMMITMENT.USER` | `SgSlaCommitment_User` | TField |  | User responsible for file being created. Validation Rules: =============== Must be a valid record from the USER application. |
| 6 | `SG.SLA.COMMITMENT.OPERATOR` | `SgSlaCommitment_Operator` | TField |  | Operator of the process Validation Rules: =============== Must be a valid record from the USER application |
| 7 | `SG.SLA.COMMITMENT.SOURCE.APPLICATION` | `SgSlaCommitment_SourceApplication` | TField |  | Source application which creates the file, Say PW.PROCESS, PW.ACTIVITY.TXN Validation Rules: =============== Must be a valid record from the PGM.FILE application |
| 8 | `SG.SLA.COMMITMENT.START.DATE` | `SgSlaCommitment_StartDate` | TField |  | Date of start of activity/process |
| 9 | `SG.SLA.COMMITMENT.START.TIME` | `SgSlaCommitment_StartTime` | TField |  | Start time of activity/process |
| 10 | `SG.SLA.COMMITMENT.DUE.DATE` | `SgSlaCommitment_DueDate` | TField |  | Expected Due date is calculated by considering metrics definition in SG.SLA |
| 11 | `SG.SLA.COMMITMENT.DUE.TIME` | `SgSlaCommitment_DueTime` | TField |  | Expected Due time is calculated by considering metrics definition in SG.SLA |
| 12 | `SG.SLA.COMMITMENT.END.DATE` | `SgSlaCommitment_EndDate` | TField |  | Date of Actual end of activity/process |
| 13 | `SG.SLA.COMMITMENT.END.TIME` | `SgSlaCommitment_EndTime` | TField |  | END time of activity/process |
| 14 | `SG.SLA.COMMITMENT.STATUS` | `SgSlaCommitment_Status` | TField |  | Can be BREACHED or REVERSED |
| 15 | `SG.SLA.COMMITMENT.PREV.STATUS` | `SgSlaCommitment_PrevStatus` |  |  |  |
| 16 | `SG.SLA.COMMITMENT.STATUS.DATE` | `SgSlaCommitment_StatusDate` |  |  |  |
| 17 | `SG.SLA.COMMITMENT.DELIVERY.REF` | `SgSlaCommitment_DeliveryRef` | TField |  | Key to Delivery message generated. |
| 18 | `SG.SLA.COMMITMENT.RESERVED.10` | `SgSlaCommitment_Reserved10` | TField |  | This field is reserved for future use Validation Rules: =============== NOINPUT field |
| 19 | `SG.SLA.COMMITMENT.RESERVED.9` | `SgSlaCommitment_Reserved9` | TField |  | This field is reserved for future use Validation Rules: =============== NOINPUT field |
| 20 | `SG.SLA.COMMITMENT.RESERVED.8` | `SgSlaCommitment_Reserved8` | TField |  | This field is reserved for future use Validation Rules: =============== NOINPUT field |
| 21 | `SG.SLA.COMMITMENT.RESERVED.7` | `SgSlaCommitment_Reserved7` | TField |  | This field is reserved for future use Validation Rules: =============== NOINPUT field |
| 22 | `SG.SLA.COMMITMENT.RESERVED.6` | `SgSlaCommitment_Reserved6` | TField |  | This field is reserved for future use Validation Rules: =============== NOINPUT field |
| 23 | `SG.SLA.COMMITMENT.RESERVED.5` | `SgSlaCommitment_Reserved5` | TField |  | This field is reserved for future use Validation Rules: =============== NOINPUT field |
| 24 | `SG.SLA.COMMITMENT.RESERVED.4` | `SgSlaCommitment_Reserved4` | TField |  | This field is reserved for future use Validation Rules: =============== NOINPUT field |
| 25 | `SG.SLA.COMMITMENT.RESERVED.3` | `SgSlaCommitment_Reserved3` | TField |  | This field is reserved for future use Validation Rules: =============== NOINPUT field |
| 26 | `SG.SLA.COMMITMENT.RESERVED.2` | `SgSlaCommitment_Reserved2` | TField |  | This field is reserved for future use Validation Rules: =============== NOINPUT field |
| 27 | `SG.SLA.COMMITMENT.RESERVED.1` | `SgSlaCommitment_Reserved1` | TField |  | This field is reserved for future use Validation Rules: =============== NOINPUT field |
