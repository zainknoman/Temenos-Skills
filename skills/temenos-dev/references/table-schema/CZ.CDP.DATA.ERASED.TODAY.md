# CZ.CDP.DATA.ERASED.TODAY — Table Schema

> Source: `INSERTS/I_F.CZ.CDP.DATA.ERASED.TODAY` in `CZ_ErasureProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CCDT.PARTY.ID` | `CzCdpDataErasedToday_PartyId` | TField |  | The identifier for the customer who has requested his/her financial institution to furnish the personal data details held about him/her with them. Defaulted from ID of this application |
| 2 | `CCDT.PARTY.APPLICATION` | `CzCdpDataErasedToday_PartyApplication` | TField |  | This field indicates the application to which the party belongs Identifier to indicate the type of relationship the requestor has maintained with the bank. Validation Rule: Valid application name This is currently supported for CUSTOMER application and so defaulted as "CUSTOMER" |
| 3 | `CCDT.ERASURE.DATE` | `CzCdpDataErasedToday_ErasureDate` | TField |  | This field indicates the date on which the erasure is happened. |
| 4 | `CCDT.TABLE.NAME` | `CzCdpDataErasedToday_TableName` | TField |  | This field indicates T24 table in relation to the customer ID which was part of the CDP.DATA.DEFINITION search Defaulted from ID of this application |
| 5 | `CCDT.FILE.TYPE` | `CzCdpDataErasedToday_FileType` | TField |  | This field indicates if the above erased contracts and their associated information are held in LIVE/HISTORY/ARCHIVE database. |
| 6 | `CCDT.RECORD.ID` | `CzCdpDataErasedToday_RecordId` |  |  |  |
| 7 | `CCDT.COMPANY.ID` | `CzCdpDataErasedToday_CompanyId` |  |  |  |
| 8 | `CCDT.FIELD.NAME` | `CzCdpDataErasedToday_FieldName` |  |  |  |
| 9 | `CCDT.PURPOSE` | `CzCdpDataErasedToday_Purpose` |  |  |  |
| 10 | `CCDT.ERASE.OPTION` | `CzCdpDataErasedToday_EraseOption` |  |  |  |
| 11 | `CCDT.NEW.FIELD.VALUE` | `CzCdpDataErasedToday_NewFieldValue` |  |  |  |
| 12 | `CCDT.REC.RESERVED.05` | `CzCdpDataErasedToday_RecReserved05` |  |  |  |
| 13 | `CCDT.REC.RESERVED.04` | `CzCdpDataErasedToday_RecReserved04` |  |  |  |
| 14 | `CCDT.REC.RESERVED.03` | `CzCdpDataErasedToday_RecReserved03` |  |  |  |
| 15 | `CCDT.REC.RESERVED.02` | `CzCdpDataErasedToday_RecReserved02` |  |  |  |
| 16 | `CCDT.REC.RESERVED.01` | `CzCdpDataErasedToday_RecReserved01` |  |  |  |
| 17 | `CCDT.IF.EVENTS.STATUS` | `CzCdpDataErasedToday_IfEventsStatus` | TField |  |  |
| 18 | `CCDT.RESERVED.09` | `CzCdpDataErasedToday_Reserved09` | TField |  |  |
| 19 | `CCDT.RESERVED.08` | `CzCdpDataErasedToday_Reserved08` | TField |  |  |
| 20 | `CCDT.RESERVED.07` | `CzCdpDataErasedToday_Reserved07` | TField |  |  |
| 21 | `CCDT.RESERVED.06` | `CzCdpDataErasedToday_Reserved06` | TField |  |  |
| 22 | `CCDT.RESERVED.05` | `CzCdpDataErasedToday_Reserved05` | TField |  |  |
| 23 | `CCDT.RESERVED.04` | `CzCdpDataErasedToday_Reserved04` | TField |  |  |
| 24 | `CCDT.RESERVED.03` | `CzCdpDataErasedToday_Reserved03` | TField |  |  |
| 25 | `CCDT.RESERVED.02` | `CzCdpDataErasedToday_Reserved02` | TField |  |  |
| 26 | `CCDT.RESERVED.01` | `CzCdpDataErasedToday_Reserved01` | TField |  |  |
