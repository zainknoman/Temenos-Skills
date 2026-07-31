# EW.HOST.COMPARE.ONLINE — Table Schema

> Source: `INSERTS/I_F.EW.HOST.COMPARE.ONLINE` in `EW_HostCompare.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EW.HC.MISMATCH.REASON` | `EwHostCompareOnline_MismatchReason` | TField |  | This field holds the reason for mismatch. This will accept values QUANTITY or OTHER. Default will be QUANTITY |
| 2 | `EW.HC.STATUS` | `EwHostCompareOnline_Status` | TField |  | This will be blank. Once re-run is flagged and a fresh enquiry extract is triggered, this will be marked as "Completed" and the record will be deleted. |
| 3 | `EW.HC.RERUN` | `EwHostCompareOnline_Rerun` | TField |  | This field will allow input only in the "SYSTEM" record. This will accept "ALL" or "YES". If flagged to "ALL", system will launch the Host compare enquiry for all portfolios flagged as EXTRACT.REQDS in SAM. If flagged to "YES" it will launch for all portfolio records in this application. |
| 4 | `EW.HC.RESERVED15` | `EwHostCompareOnline_Reserved15` | TField |  |  |
| 5 | `EW.HC.RESERVED14` | `EwHostCompareOnline_Reserved14` | TField |  |  |
| 6 | `EW.HC.RESERVED13` | `EwHostCompareOnline_Reserved13` | TField |  |  |
| 7 | `EW.HC.RESERVED12` | `EwHostCompareOnline_Reserved12` | TField |  |  |
| 8 | `EW.HC.RESERVED11` | `EwHostCompareOnline_Reserved11` | TField |  |  |
| 9 | `EW.HC.RESERVED10` | `EwHostCompareOnline_Reserved10` | TField |  |  |
| 10 | `EW.HC.RESERVED9` | `EwHostCompareOnline_Reserved9` | TField |  |  |
| 11 | `EW.HC.RESERVED8` | `EwHostCompareOnline_Reserved8` | TField |  |  |
| 12 | `EW.HC.RESERVED7` | `EwHostCompareOnline_Reserved7` | TField |  |  |
| 13 | `EW.HC.RESERVED6` | `EwHostCompareOnline_Reserved6` | TField |  |  |
| 14 | `EW.HC.RESERVED5` | `EwHostCompareOnline_Reserved5` | TField |  |  |
| 15 | `EW.HC.RESERVED4` | `EwHostCompareOnline_Reserved4` | TField |  |  |
| 16 | `EW.HC.RESERVED3` | `EwHostCompareOnline_Reserved3` | TField |  |  |
| 17 | `EW.HC.RESERVED2` | `EwHostCompareOnline_Reserved2` | TField |  |  |
| 18 | `EW.HC.RESERVED1` | `EwHostCompareOnline_Reserved1` | TField |  |  |
| 19 | `EW.HC.LOCAL.REF` | `EwHostCompareOnline_LocalRef` |  |  |  |
| 20 | `EW.HC.STMT.NOS` | `EwHostCompareOnline_StmtNos` |  |  |  |
| 21 | `EW.HC.OVERRIDE` | `EwHostCompareOnline_Override` |  |  |  |
| 22 | `EW.HC.RECORD.STATUS` | `EwHostCompareOnline_RecordStatus` | String |  |  |
| 23 | `EW.HC.CURR.NO` | `EwHostCompareOnline_CurrNo` | String |  |  |
| 24 | `EW.HC.INPUTTER` | `EwHostCompareOnline_Inputter` |  |  |  |
| 25 | `EW.HC.DATE.TIME` | `EwHostCompareOnline_DateTime` |  |  |  |
| 26 | `EW.HC.AUTHORISER` | `EwHostCompareOnline_Authoriser` | String |  |  |
| 27 | `EW.HC.CO.CODE` | `EwHostCompareOnline_CoCode` | String |  |  |
| 28 | `EW.HC.DEPT.CODE` | `EwHostCompareOnline_DeptCode` | String |  |  |
| 29 | `EW.HC.AUDITOR.CODE` | `EwHostCompareOnline_AuditorCode` | String |  |  |
| 30 | `EW.HC.AUDIT.DATE.TIME` | `EwHostCompareOnline_AuditDateTime` | String |  |  |
