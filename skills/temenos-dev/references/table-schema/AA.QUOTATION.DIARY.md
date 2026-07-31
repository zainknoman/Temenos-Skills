# AA.QUOTATION.DIARY — Table Schema

> Source: `INSERTS/I_F.AA.QUOTATION.DIARY` in `AA_Quotation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.QDR.STATUS` | `AaQuotationDiary_Status` | TField |  | The status of the Application. Could hold 3 values: ACTIVE - Application is in progress INACTIVE - Application began, but no activity has happened for a long time. The time is controlled by a parameter in AA.ORIGINATION.PARAMETER table. COMPLETE - Application reached its logical end. READY.FOR.ARCHIVE - Indicates the record has crossed its threshold of inactivity or completion and is ready to be picked by Archival service. |
| 2 | `AA.QDR.STATUS.DATE` | `AaQuotationDiary_StatusDate` | TField |  | The date on which the above status was updated. Would be useful to know when the system moved to READY.FOR.ARCHIVE status so that the same can be compared against the RETENTION.PERIOD stated in the ARCHIVE record. Would also be a useful indicator on how long has it remained in this status. |
| 3 | `AA.QDR.RESERVED.17` | `AaQuotationDiary_Reserved17` | TField |  |  |
| 4 | `AA.QDR.RESERVED.16` | `AaQuotationDiary_Reserved16` | TField |  |  |
| 5 | `AA.QDR.RESERVED.15` | `AaQuotationDiary_Reserved15` | TField |  |  |
| 6 | `AA.QDR.ACTIVITY` | `AaQuotationDiary_Activity` |  |  |  |
| 7 | `AA.QDR.RESERVED.14` | `AaQuotationDiary_Reserved14` |  |  |  |
| 8 | `AA.QDR.RESERVED.13` | `AaQuotationDiary_Reserved13` |  |  |  |
| 9 | `AA.QDR.RESERVED.12` | `AaQuotationDiary_Reserved12` |  |  |  |
| 10 | `AA.QDR.DATE` | `AaQuotationDiary_Date` |  |  |  |
| 11 | `AA.QDR.TIME` | `AaQuotationDiary_Time` |  |  |  |
| 12 | `AA.QDR.USER` | `AaQuotationDiary_User` |  |  |  |
| 13 | `AA.QDR.OFS.SOURCE` | `AaQuotationDiary_OfsSource` |  |  |  |
| 14 | `AA.QDR.ACTIVITY.STATUS` | `AaQuotationDiary_ActivityStatus` |  |  |  |
| 15 | `AA.QDR.APPLICATION` | `AaQuotationDiary_Application` |  |  |  |
| 16 | `AA.QDR.REFERENCE` | `AaQuotationDiary_Reference` |  |  |  |
| 17 | `AA.QDR.DEFINITION` | `AaQuotationDiary_Definition` |  |  |  |
| 18 | `AA.QDR.RESERVED.11` | `AaQuotationDiary_Reserved11` |  |  |  |
| 19 | `AA.QDR.RESERVED.10` | `AaQuotationDiary_Reserved10` |  |  |  |
| 20 | `AA.QDR.RESERVED.9` | `AaQuotationDiary_Reserved9` |  |  |  |
| 21 | `AA.QDR.RESERVED.8` | `AaQuotationDiary_Reserved8` |  |  |  |
| 22 | `AA.QDR.RESERVED.7` | `AaQuotationDiary_Reserved7` |  |  |  |
| 23 | `AA.QDR.RESERVED.6` | `AaQuotationDiary_Reserved6` | TField |  |  |
| 24 | `AA.QDR.RESERVED.5` | `AaQuotationDiary_Reserved5` | TField |  |  |
| 25 | `AA.QDR.RESERVED.4` | `AaQuotationDiary_Reserved4` | TField |  |  |
| 26 | `AA.QDR.RESERVED.3` | `AaQuotationDiary_Reserved3` | TField |  |  |
| 27 | `AA.QDR.RESERVED.2` | `AaQuotationDiary_Reserved2` | TField |  |  |
| 28 | `AA.QDR.RESERVED.1` | `AaQuotationDiary_Reserved1` | TField |  |  |
