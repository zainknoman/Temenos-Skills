# SC.SETT.PENALTY.DAILY — Table Schema

> Source: `INSERTS/I_F.SC.SETT.PENALTY.DAILY` in `SC_SctSettlement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PEN.DAIL.DEPOSITORY` | `ScSettPenaltyDaily_Depository` | TField |  | This field holds the value from DEPOSITORY field from the corresponding transaction SEC.TRADE or SECURITY.TRANSFER for which the penalty details are received . This is the valid DEPOSITORY definition from CUSTOMER.SECURITY |
| 2 | `SC.PEN.DAIL.MATCH.DATE` | `ScSettPenaltyDaily_MatchDate` | TField |  | This field holds the date of receipt of MT548 match status (MTCH/MACH) This will be populated from SC.MT548.MATCH.QUEUE record when the penalty details are received from MT537 Validation: Standard T24 date field |
| 3 | `SC.PEN.DAIL.INW.DELIVERY.REF` | `ScSettPenaltyDaily_InwDeliveryRef` |  |  |  |
| 4 | `SC.PEN.DAIL.MSG.DATE` | `ScSettPenaltyDaily_MsgDate` |  |  |  |
| 5 | `SC.PEN.DAIL.PENALTY.TYPE` | `ScSettPenaltyDaily_PenaltyType` |  |  |  |
| 6 | `SC.PEN.DAIL.LMFP.COMM.REF` | `ScSettPenaltyDaily_LmfpCommRef` |  |  |  |
| 7 | `SC.PEN.DAIL.LMFP.RECD.DATE` | `ScSettPenaltyDaily_LmfpRecdDate` |  |  |  |
| 8 | `SC.PEN.DAIL.LMFP.RECD` | `ScSettPenaltyDaily_LmfpRecd` |  |  |  |
| 9 | `SC.PEN.DAIL.LMFP.SYS` | `ScSettPenaltyDaily_LmfpSys` |  |  |  |
| 10 | `SC.PEN.DAIL.SEFP.COMM.REF` | `ScSettPenaltyDaily_SefpCommRef` |  |  |  |
| 11 | `SC.PEN.DAIL.SEFP.RECD.DATE` | `ScSettPenaltyDaily_SefpRecdDate` |  |  |  |
| 12 | `SC.PEN.DAIL.SEFP.RECD` | `ScSettPenaltyDaily_SefpRecd` |  |  |  |
| 13 | `SC.PEN.DAIL.SEFP.SYS` | `ScSettPenaltyDaily_SefpSys` |  |  |  |
| 14 | `SC.PEN.DAIL.NET.LMFP.RECD` | `ScSettPenaltyDaily_NetLmfpRecd` | TField |  | This field holds sum of LMFP.RECD Automatically updated by the system when the penalty details are received via MT548 or MT537 swift message with PENA details Standard T24 Amount field |
| 15 | `SC.PEN.DAIL.NET.SEFP.RECD` | `ScSettPenaltyDaily_NetSefpRecd` | TField |  | This field holds sum of SEFP.RECD Automatically updated by the system when the penalty details are received via MT548 or MT537 swift message with PENA details Standard T24 Amount field |
| 16 | `SC.PEN.DAIL.NET.RECD.PENALTY` | `ScSettPenaltyDaily_NetRecdPenalty` | TField |  | This field holds the sum of NET.LMFP.RECD and NET.SEFP.RECD Automatically updated by the system when the penalty details are received via MT548 or MT537 swift message with PENA details Standard T24 Amount field |
| 17 | `SC.PEN.DAIL.NET.LMFP.SYS` | `ScSettPenaltyDaily_NetLmfpSys` | TField |  | This field holds the sum of LMFP.SYS Calculated and populated by system automatically during COB once the LMFP.SYS penalty amount is calculated and populated in SC.SETT.PENALTY.DAILY record Standard T24 Amount field |
| 18 | `SC.PEN.DAIL.NET.SEFP.SYS` | `ScSettPenaltyDaily_NetSefpSys` | TField |  | This field holds the sum of SEFP.SYS Calculated and populated by system automatically during COB once the SEFP.SYS penalty amount is calculated and populated in SC.SETT.PENALTY.DAILY record Standard T24 Amount field |
| 19 | `SC.PEN.DAIL.NET.SYS.PENALTY` | `ScSettPenaltyDaily_NetSysPenalty` | TField |  | This field holds the sum of NET.LMFP.SYS and NET.SEFP.SYS Standard T24 Amount field |
| 20 | `SC.PEN.DAIL.RESERVED20` | `ScSettPenaltyDaily_Reserved20` | TField |  |  |
| 21 | `SC.PEN.DAIL.RESERVED19` | `ScSettPenaltyDaily_Reserved19` | TField |  |  |
| 22 | `SC.PEN.DAIL.RESERVED18` | `ScSettPenaltyDaily_Reserved18` | TField |  |  |
| 23 | `SC.PEN.DAIL.RESERVED17` | `ScSettPenaltyDaily_Reserved17` | TField |  |  |
| 24 | `SC.PEN.DAIL.RESERVED16` | `ScSettPenaltyDaily_Reserved16` | TField |  |  |
| 25 | `SC.PEN.DAIL.RESERVED15` | `ScSettPenaltyDaily_Reserved15` | TField |  |  |
| 26 | `SC.PEN.DAIL.RESERVED14` | `ScSettPenaltyDaily_Reserved14` | TField |  |  |
| 27 | `SC.PEN.DAIL.RESERVED13` | `ScSettPenaltyDaily_Reserved13` | TField |  |  |
| 28 | `SC.PEN.DAIL.RESERVED12` | `ScSettPenaltyDaily_Reserved12` | TField |  |  |
| 29 | `SC.PEN.DAIL.RESERVED11` | `ScSettPenaltyDaily_Reserved11` | TField |  |  |
| 30 | `SC.PEN.DAIL.RESERVED10` | `ScSettPenaltyDaily_Reserved10` | TField |  |  |
| 31 | `SC.PEN.DAIL.RESERVED9` | `ScSettPenaltyDaily_Reserved9` | TField |  |  |
| 32 | `SC.PEN.DAIL.RESERVED8` | `ScSettPenaltyDaily_Reserved8` | TField |  |  |
| 33 | `SC.PEN.DAIL.RESERVED7` | `ScSettPenaltyDaily_Reserved7` | TField |  |  |
| 34 | `SC.PEN.DAIL.RESERVED6` | `ScSettPenaltyDaily_Reserved6` | TField |  |  |
| 35 | `SC.PEN.DAIL.RESERVED5` | `ScSettPenaltyDaily_Reserved5` | TField |  |  |
| 36 | `SC.PEN.DAIL.RESERVED4` | `ScSettPenaltyDaily_Reserved4` | TField |  |  |
| 37 | `SC.PEN.DAIL.RESERVED3` | `ScSettPenaltyDaily_Reserved3` | TField |  |  |
| 38 | `SC.PEN.DAIL.RESERVED2` | `ScSettPenaltyDaily_Reserved2` | TField |  |  |
| 39 | `SC.PEN.DAIL.RESERVED1` | `ScSettPenaltyDaily_Reserved1` | TField |  |  |
| 40 | `SC.PEN.DAIL.LOCAL.REF` | `ScSettPenaltyDaily_LocalRef` |  |  |  |
| 41 | `SC.PEN.DAIL.OVERRIDE` | `ScSettPenaltyDaily_Override` |  |  |  |
| 42 | `SC.PEN.DAIL.RECORD.STATUS` | `ScSettPenaltyDaily_RecordStatus` | String |  |  |
| 43 | `SC.PEN.DAIL.CURR.NO` | `ScSettPenaltyDaily_CurrNo` | String |  |  |
| 44 | `SC.PEN.DAIL.INPUTTER` | `ScSettPenaltyDaily_Inputter` |  |  |  |
| 45 | `SC.PEN.DAIL.DATE.TIME` | `ScSettPenaltyDaily_DateTime` |  |  |  |
| 46 | `SC.PEN.DAIL.AUTHORISER` | `ScSettPenaltyDaily_Authoriser` | String |  |  |
| 47 | `SC.PEN.DAIL.CO.CODE` | `ScSettPenaltyDaily_CoCode` | String |  |  |
| 48 | `SC.PEN.DAIL.DEPT.CODE` | `ScSettPenaltyDaily_DeptCode` | String |  |  |
| 49 | `SC.PEN.DAIL.AUDITOR.CODE` | `ScSettPenaltyDaily_AuditorCode` | String |  |  |
| 50 | `SC.PEN.DAIL.AUDIT.DATE.TIME` | `ScSettPenaltyDaily_AuditDateTime` | String |  |  |
