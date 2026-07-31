# USRETL.CHECK.CLEARING.PARAMETER — Table Schema

> Source: `INSERTS/I_F.USRETL.CHECK.CLEARING.PARAMETER` in `USRETL_CheckCollection.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USCCP.FED.NOSTRO.ACCOUNT` | `UsretlCheckClearingParameter_FedNostroAccount` | TField |  | Federal Reserve Bank Nostro Account Number maintained in Transact for the financial lead company. Account entered in this field must exist in NOSTRO.ACCOUNT table |
| 2 | `USCCP.APPLY.REGCC` | `UsretlCheckClearingParameter_ApplyRegcc` | TField |  | Indicator to denote RegCC is applicable to all entry posting from Remote Deposit Capture. Allowed values: YES - Denotes that REGCC exposure ladder will be applied for credit transctions posted using AC.ENTRY.PARAM-RDC NO - Denotes that REGCC exposure ladder will NOT be applied for credit transctions posted using AC.ENTRY.PARAM-RDC |
| 3 | `USCCP.GOV.ROUTING.NO` | `UsretlCheckClearingParameter_GovRoutingNo` |  |  |  |
| 4 | `USCCP.ONUS.ROUTING.NO` | `UsretlCheckClearingParameter_OnusRoutingNo` |  |  |  |
| 5 | `USCCP.CUTOFF.TIME` | `UsretlCheckClearingParameter_CutoffTime` | TField |  | Specifies the time during the day after which value date of the check deposit has to shifted as per CUTOFF.SHIFT. Prior to check deposit transaction posting, starting from midnight 00:00 hours until current time in local time zone configured in COMPANY - TIME.ZONE is converted into CUTOFF.TIME.ZONE and if the calculated time exceeds CUTOFF.TIME, value date is shifted. Time format is HH:MM, 24 hour clock format. |
| 6 | `USCCP.CUTOFF.TIME.ZONE` | `UsretlCheckClearingParameter_CutoffTimeZone` | TField |  | Specifies Time zone associated with CUTOFF.TIME. It is based on timezone used by Unix and other systems in the form of "Area/Location". Must be a valid entry in EB.TIME.ZONES table. Area is a continent or ocean name Location is the city, island, or other regional name |
| 7 | `USCCP.CUTOFF.SHIFT` | `UsretlCheckClearingParameter_CutoffShift` | TField |  | Specifies the number of working days shift to apply on current Transact Business Date, this will be the value date of check deposited after CUTOFF.TIME with CUTOFF.TIME.ZONE in consideration. |
| 8 | `USCCP.SETTLEMENT.SHIFT` | `UsretlCheckClearingParameter_SettlementShift` | TField |  | Specifies the number of working days shift to Value date of settlement entry between RDC suspense account and FED.NOSTRO.ACCT during COB. |
| 9 | `USCCP.IN.CLG.FILE.PATH` | `UsretlCheckClearingParameter_InClgFilePath` | TField |  | UD directory path where CHECK21 Inward Clearing file will be placed for USCK21.CLEARING.FILE.PROCESS batch process to refer. Field inout is required only when USCK21 product is installed. |
| 10 | `USCCP.IN.RETURNS.FILE.PATH` | `UsretlCheckClearingParameter_InReturnsFilePath` | TField |  | UD directory path where CHECK21 Inward Returns file will be placed for USCK21.CLEARING.FILE.PROCESS batch process to refer. Field input is required only when USCK21 product is installed. |
| 11 | `USCCP.ARCHIVE.PATH` | `UsretlCheckClearingParameter_ArchivePath` | TField |  | UD directory path where CHECK21 Inward Clearing and Inward Returns file will be archived once processed by USCK21.CLEARING.FILE.PROCESS batch process. Field input is required only when USCK21 product is installed. |
| 12 | `USCCP.OUT.EXCEPTION.FILE.PATH` | `UsretlCheckClearingParameter_OutExceptionFilePath` | TField |  | UD directory path where CHECK21 exception items that matches the Expiry Date (calculated from Received Clearing Date + Expiry Days) are captured in Outward exception file that will be placed by USCK21.EXCEPTION.FILE.PROCESS batch process. Field input is required only when USCK21 product is installed. |
| 13 | `USCCP.EXCEPTION.TXN.CODE` | `UsretlCheckClearingParameter_ExceptionTxnCode` |  |  |  |
| 14 | `USCCP.EXPIRY.DAYS` | `UsretlCheckClearingParameter_ExpiryDays` | TField |  | The number entered in this field represents the number of working days after which an item will be reported in Outward CHECK21 exception file. Scenario: EXPIRY.DAYS = 2 (working days) Inward Clearing Item received date - 9/01/2020 Expiry Date calculated = 09/01/2020 + 2 working days i.e. 09/03/2020 CHECK21 -USCK21.CLEARING.FILE.PROCESS batch process for items parked in exception queue contains EXPIRY.DATE = 09/03/2020 in USRETL.CHECK.COLLECTION. |
| 15 | `USCCP.RESERVED.10` | `UsretlCheckClearingParameter_Reserved10` |  |  |  |
| 16 | `USCCP.RESERVED.9` | `UsretlCheckClearingParameter_Reserved9` | TField |  |  |
| 17 | `USCCP.RESERVED.8` | `UsretlCheckClearingParameter_Reserved8` | TField |  |  |
| 18 | `USCCP.RESERVED.7` | `UsretlCheckClearingParameter_Reserved7` | TField |  |  |
| 19 | `USCCP.RESERVED.6` | `UsretlCheckClearingParameter_Reserved6` | TField |  |  |
| 20 | `USCCP.RESERVED.5` | `UsretlCheckClearingParameter_Reserved5` | TField |  |  |
| 21 | `USCCP.RESERVED.4` | `UsretlCheckClearingParameter_Reserved4` | TField |  |  |
| 22 | `USCCP.RESERVED.3` | `UsretlCheckClearingParameter_Reserved3` | TField |  |  |
| 23 | `USCCP.RESERVED.2` | `UsretlCheckClearingParameter_Reserved2` | TField |  |  |
| 24 | `USCCP.RESERVED.1` | `UsretlCheckClearingParameter_Reserved1` | TField |  |  |
| 25 | `USCCP.RECORD.STATUS` | `UsretlCheckClearingParameter_RecordStatus` | String |  |  |
| 26 | `USCCP.CURR.NO` | `UsretlCheckClearingParameter_CurrNo` | String |  |  |
| 27 | `USCCP.INPUTTER` | `UsretlCheckClearingParameter_Inputter` |  |  |  |
| 28 | `USCCP.DATE.TIME` | `UsretlCheckClearingParameter_DateTime` |  |  |  |
| 29 | `USCCP.AUTHORISER` | `UsretlCheckClearingParameter_Authoriser` | String |  |  |
| 30 | `USCCP.CO.CODE` | `UsretlCheckClearingParameter_CoCode` | String |  |  |
| 31 | `USCCP.DEPT.CODE` | `UsretlCheckClearingParameter_DeptCode` | String |  |  |
| 32 | `USCCP.AUDITOR.CODE` | `UsretlCheckClearingParameter_AuditorCode` | String |  |  |
| 33 | `USCCP.AUDIT.DATE.TIME` | `UsretlCheckClearingParameter_AuditDateTime` | String |  |  |
