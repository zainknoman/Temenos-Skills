# LMSCOL.COLLECTION.NOTES — Table Schema

> Source: `INSERTS/I_F.LMSCOL.COLLECTION.NOTES` in `LMSCOL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LMS.NT.CUSTOMER.ID` | `LmscolCollectionNotes_CustomerId` | TField |  | Customer Number. |
| 2 | `LMS.NT.ACCOUNT.ID` | `LmscolCollectionNotes_AccountId` | TField |  | Account Number. |
| 3 | `LMS.NT.TYPE` | `LmscolCollectionNotes_Type` | TField |  | Defines the type of contact made between customer and collection agency. Values are fetched from LMSCL.NOTE.TYPE eblookup table |
| 4 | `LMS.NT.PLACEMENT.DATE` | `LmscolCollectionNotes_PlacementDate` | TField |  | Contains the date on which the comment was created in infinity. |
| 5 | `LMS.NT.PLACEMENT.TIME` | `LmscolCollectionNotes_PlacementTime` | TField |  | Contains the time stamp on which the comment was created in infinity. |
| 6 | `LMS.NT.USER.ID` | `LmscolCollectionNotes_UserId` | TField |  | Contains the user who created the note in infinity. |
| 7 | `LMS.NT.LAST.MODIFIED.DATE` | `LmscolCollectionNotes_LastModifiedDate` | TField |  | Contains the date on which the comment was last modified in infinity. |
| 8 | `LMS.NT.EXPIRATION.DATE` | `LmscolCollectionNotes_ExpirationDate` | TField |  | Contains the date on which the comment is schedule to expire. |
| 9 | `LMS.NT.NOTES` | `LmscolCollectionNotes_Notes` |  |  |  |
| 10 | `LMS.NT.RESERVED.10` | `LmscolCollectionNotes_Reserved10` | TField |  |  |
| 11 | `LMS.NT.RESERVED.9` | `LmscolCollectionNotes_Reserved9` | TField |  |  |
| 12 | `LMS.NT.RESERVED.8` | `LmscolCollectionNotes_Reserved8` | TField |  |  |
| 13 | `LMS.NT.RESERVED.7` | `LmscolCollectionNotes_Reserved7` | TField |  |  |
| 14 | `LMS.NT.RESERVED.6` | `LmscolCollectionNotes_Reserved6` | TField |  |  |
| 15 | `LMS.NT.RESERVED.5` | `LmscolCollectionNotes_Reserved5` | TField |  |  |
| 16 | `LMS.NT.RESERVED.4` | `LmscolCollectionNotes_Reserved4` | TField |  |  |
| 17 | `LMS.NT.RESERVED.3` | `LmscolCollectionNotes_Reserved3` | TField |  |  |
| 18 | `LMS.NT.RESERVED.2` | `LmscolCollectionNotes_Reserved2` | TField |  |  |
| 19 | `LMS.NT.RESERVED.1` | `LmscolCollectionNotes_Reserved1` | TField |  |  |
| 20 | `LMS.NT.RECORD.STATUS` | `LmscolCollectionNotes_RecordStatus` | String |  |  |
| 21 | `LMS.NT.CURR.NO` | `LmscolCollectionNotes_CurrNo` | String |  |  |
| 22 | `LMS.NT.INPUTTER` | `LmscolCollectionNotes_Inputter` |  |  |  |
| 23 | `LMS.NT.DATE.TIME` | `LmscolCollectionNotes_DateTime` |  |  |  |
| 24 | `LMS.NT.AUTHORISER` | `LmscolCollectionNotes_Authoriser` | String |  |  |
| 25 | `LMS.NT.CO.CODE` | `LmscolCollectionNotes_CoCode` | String |  |  |
| 26 | `LMS.NT.DEPT.CODE` | `LmscolCollectionNotes_DeptCode` | String |  |  |
| 27 | `LMS.NT.AUDITOR.CODE` | `LmscolCollectionNotes_AuditorCode` | String |  |  |
| 28 | `LMS.NT.AUDIT.DATE.TIME` | `LmscolCollectionNotes_AuditDateTime` | String |  |  |
