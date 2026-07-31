# ACFAMS.SYNC.ERROR — Table Schema

> Source: `INSERTS/I_F.ACFAMS.SYNC.ERROR` in `ACFAMS_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACFAMS.SYNER.RESERVATION.KEY` | `AcfamsSyncError_ReservationKey` |  |  |  |
| 2 | `ACFAMS.SYNER.AC.INWARD.ID` | `AcfamsSyncError_AcInwardId` |  |  |  |
| 3 | `ACFAMS.SYNER.ERROR.MESSAGE` | `AcfamsSyncError_ErrorMessage` |  |  |  |
| 4 | `ACFAMS.SYNER.STATUS` | `AcfamsSyncError_Status` |  |  |  |
| 5 | `ACFAMS.SYNER.RESERV.KEY.RESERV5` | `AcfamsSyncError_ReservKeyReserv5` |  |  |  |
| 6 | `ACFAMS.SYNER.RESERV.KEY.RESERV4` | `AcfamsSyncError_ReservKeyReserv4` |  |  |  |
| 7 | `ACFAMS.SYNER.RESERV.KEY.RESERV3` | `AcfamsSyncError_ReservKeyReserv3` |  |  |  |
| 8 | `ACFAMS.SYNER.RESERV.KEY.RESERV2` | `AcfamsSyncError_ReservKeyReserv2` |  |  |  |
| 9 | `ACFAMS.SYNER.RESERV.KEY.RESERV1` | `AcfamsSyncError_ReservKeyReserv1` |  |  |  |
| 10 | `ACFAMS.SYNER.ER.BLOCK.ERR` | `AcfamsSyncError_ErBlockErr` | TField |  | The error message |
| 11 | `ACFAMS.SYNER.RESOLVED` | `AcfamsSyncError_Resolved` | TField |  | Have all the errors been fixed.FIXED or null. When marked as FIXED, the Account FA Status will be cleared. |
| 12 | `ACFAMS.SYNER.ER.BLOCK.STATUS` | `AcfamsSyncError_ErBlockStatus` | TField |  |  |
| 13 | `ACFAMS.SYNER.RESERVED.18` | `AcfamsSyncError_Reserved18` | TField |  |  |
| 14 | `ACFAMS.SYNER.RESERVED.17` | `AcfamsSyncError_Reserved17` | TField |  |  |
| 15 | `ACFAMS.SYNER.RESERVED.16` | `AcfamsSyncError_Reserved16` | TField |  |  |
| 16 | `ACFAMS.SYNER.RESERVED.15` | `AcfamsSyncError_Reserved15` | TField |  |  |
| 17 | `ACFAMS.SYNER.RESERVED.14` | `AcfamsSyncError_Reserved14` | TField |  |  |
| 18 | `ACFAMS.SYNER.RESERVED.13` | `AcfamsSyncError_Reserved13` | TField |  |  |
| 19 | `ACFAMS.SYNER.RESERVED.12` | `AcfamsSyncError_Reserved12` | TField |  |  |
| 20 | `ACFAMS.SYNER.RESERVED.11` | `AcfamsSyncError_Reserved11` | TField |  |  |
| 21 | `ACFAMS.SYNER.RESERVED.10` | `AcfamsSyncError_Reserved10` | TField |  |  |
| 22 | `ACFAMS.SYNER.RESERVED.9` | `AcfamsSyncError_Reserved9` | TField |  |  |
| 23 | `ACFAMS.SYNER.RESERVED.8` | `AcfamsSyncError_Reserved8` | TField |  |  |
| 24 | `ACFAMS.SYNER.RESERVED.7` | `AcfamsSyncError_Reserved7` | TField |  |  |
| 25 | `ACFAMS.SYNER.RESERVED.6` | `AcfamsSyncError_Reserved6` | TField |  |  |
| 26 | `ACFAMS.SYNER.RESERVED.5` | `AcfamsSyncError_Reserved5` | TField |  |  |
| 27 | `ACFAMS.SYNER.RESERVED.4` | `AcfamsSyncError_Reserved4` | TField |  |  |
| 28 | `ACFAMS.SYNER.RESERVED.3` | `AcfamsSyncError_Reserved3` | TField |  |  |
| 29 | `ACFAMS.SYNER.RESERVED.2` | `AcfamsSyncError_Reserved2` | TField |  |  |
| 30 | `ACFAMS.SYNER.RESERVED.1` | `AcfamsSyncError_Reserved1` | TField |  |  |
| 31 | `ACFAMS.SYNER.LOCAL.REF` | `AcfamsSyncError_LocalRef` |  |  |  |
| 32 | `ACFAMS.SYNER.OVERRIDE` | `AcfamsSyncError_Override` |  |  |  |
| 33 | `ACFAMS.SYNER.RECORD.STATUS` | `AcfamsSyncError_RecordStatus` | String |  |  |
| 34 | `ACFAMS.SYNER.CURR.NO` | `AcfamsSyncError_CurrNo` | String |  |  |
| 35 | `ACFAMS.SYNER.INPUTTER` | `AcfamsSyncError_Inputter` |  |  |  |
| 36 | `ACFAMS.SYNER.DATE.TIME` | `AcfamsSyncError_DateTime` |  |  |  |
| 37 | `ACFAMS.SYNER.AUTHORISER` | `AcfamsSyncError_Authoriser` | String |  |  |
| 38 | `ACFAMS.SYNER.CO.CODE` | `AcfamsSyncError_CoCode` | String |  |  |
| 39 | `ACFAMS.SYNER.DEPT.CODE` | `AcfamsSyncError_DeptCode` | String |  |  |
| 40 | `ACFAMS.SYNER.AUDITOR.CODE` | `AcfamsSyncError_AuditorCode` | String |  |  |
| 41 | `ACFAMS.SYNER.AUDIT.DATE.TIME` | `AcfamsSyncError_AuditDateTime` | String |  |  |
