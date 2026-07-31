# SC.SETT.PEN.PARTY — Table Schema

> Source: `INSERTS/I_F.SC.SETT.PEN.PARTY` in `SC_SctSettlement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PEN.PAR.INW.DELIVERY.REF` | `ScSettPenParty_InwDeliveryRef` |  |  |  |
| 2 | `SC.PEN.PAR.COUNTERPARTY` | `ScSettPenParty_Counterparty` |  |  |  |
| 3 | `SC.PEN.PAR.LMFP.COMM.REF` | `ScSettPenParty_LmfpCommRef` |  |  |  |
| 4 | `SC.PEN.PAR.NET.LMFP.RECD` | `ScSettPenParty_NetLmfpRecd` |  |  |  |
| 5 | `SC.PEN.PAR.NET.LMFP.SYS` | `ScSettPenParty_NetLmfpSys` |  |  |  |
| 6 | `SC.PEN.PAR.LMFP.TRANS.REF` | `ScSettPenParty_LmfpTransRef` |  |  |  |
| 7 | `SC.PEN.PAR.SEFP.COMM.REF` | `ScSettPenParty_SefpCommRef` |  |  |  |
| 8 | `SC.PEN.PAR.NET.SEFP.RECD` | `ScSettPenParty_NetSefpRecd` |  |  |  |
| 9 | `SC.PEN.PAR.NET.SEFP.SYS` | `ScSettPenParty_NetSefpSys` |  |  |  |
| 10 | `SC.PEN.PAR.SEFP.TRANS.REF` | `ScSettPenParty_SefpTransRef` |  |  |  |
| 11 | `SC.PEN.PAR.NET.PEN.CPY.RECD` | `ScSettPenParty_NetPenCpyRecd` |  |  |  |
| 12 | `SC.PEN.PAR.NET.PEN.CPY.SYS` | `ScSettPenParty_NetPenCpySys` |  |  |  |
| 13 | `SC.PEN.PAR.NET.MONTHLY.PENALTY.RECD` | `ScSettPenParty_NetMonthlyPenaltyRecd` | TField |  | This field holds the system calcualted penalty amount for the associated SEFP.RECD.DATE Standard T24 Amount field This field is mapped from 19A tag of PENACUR block with Qualifier GBNT Format of this tag is :19A:GBNT//USD100,00 |
| 14 | `SC.PEN.PAR.NET.MONTHLY.PENALTY.SYS` | `ScSettPenParty_NetMonthlyPenaltySys` | TField |  | This field holds sum of NET.PEN.CPY.SYS Standard T24 Amount field |
| 15 | `SC.PEN.PAR.POST.SETT.PENALTY` | `ScSettPenParty_PostSettPenalty` | TField |  | This field is to trigger the posting of accounting entries for the penalty amount Allowed value Y |
| 16 | `SC.PEN.PAR.NET.MONTHLY.PENALTY.POST` | `ScSettPenParty_NetMonthlyPenaltyPost` | TField |  | This field holds the amount defaulted from NET.MONTHLY.PENALTY.RECD during the accounting entries posting, the amount from this field will be passed to the accounting entries Standard T24 Amount field |
| 17 | `SC.PEN.PAR.RESERVED20` | `ScSettPenParty_Reserved20` | TField |  |  |
| 18 | `SC.PEN.PAR.RESERVED19` | `ScSettPenParty_Reserved19` | TField |  |  |
| 19 | `SC.PEN.PAR.RESERVED18` | `ScSettPenParty_Reserved18` | TField |  |  |
| 20 | `SC.PEN.PAR.RESERVED17` | `ScSettPenParty_Reserved17` | TField |  |  |
| 21 | `SC.PEN.PAR.RESERVED16` | `ScSettPenParty_Reserved16` | TField |  |  |
| 22 | `SC.PEN.PAR.RESERVED15` | `ScSettPenParty_Reserved15` | TField |  |  |
| 23 | `SC.PEN.PAR.RESERVED14` | `ScSettPenParty_Reserved14` | TField |  |  |
| 24 | `SC.PEN.PAR.RESERVED13` | `ScSettPenParty_Reserved13` | TField |  |  |
| 25 | `SC.PEN.PAR.RESERVED12` | `ScSettPenParty_Reserved12` | TField |  |  |
| 26 | `SC.PEN.PAR.RESERVED11` | `ScSettPenParty_Reserved11` | TField |  |  |
| 27 | `SC.PEN.PAR.RESERVED10` | `ScSettPenParty_Reserved10` | TField |  |  |
| 28 | `SC.PEN.PAR.RESERVED9` | `ScSettPenParty_Reserved9` | TField |  |  |
| 29 | `SC.PEN.PAR.RESERVED8` | `ScSettPenParty_Reserved8` | TField |  |  |
| 30 | `SC.PEN.PAR.RESERVED7` | `ScSettPenParty_Reserved7` | TField |  |  |
| 31 | `SC.PEN.PAR.RESERVED6` | `ScSettPenParty_Reserved6` | TField |  |  |
| 32 | `SC.PEN.PAR.RESERVED5` | `ScSettPenParty_Reserved5` | TField |  |  |
| 33 | `SC.PEN.PAR.RESERVED4` | `ScSettPenParty_Reserved4` | TField |  |  |
| 34 | `SC.PEN.PAR.RESERVED3` | `ScSettPenParty_Reserved3` | TField |  |  |
| 35 | `SC.PEN.PAR.RESERVED2` | `ScSettPenParty_Reserved2` | TField |  |  |
| 36 | `SC.PEN.PAR.RESERVED1` | `ScSettPenParty_Reserved1` | TField |  |  |
| 37 | `SC.PEN.PAR.LOCAL.REF` | `ScSettPenParty_LocalRef` |  |  |  |
| 38 | `SC.PEN.PAR.STMT.NOS` | `ScSettPenParty_StmtNos` |  |  |  |
| 39 | `SC.PEN.PAR.OVERRIDE` | `ScSettPenParty_Override` |  |  |  |
| 40 | `SC.PEN.PAR.RECORD.STATUS` | `ScSettPenParty_RecordStatus` | String |  |  |
| 41 | `SC.PEN.PAR.CURR.NO` | `ScSettPenParty_CurrNo` | String |  |  |
| 42 | `SC.PEN.PAR.INPUTTER` | `ScSettPenParty_Inputter` |  |  |  |
| 43 | `SC.PEN.PAR.DATE.TIME` | `ScSettPenParty_DateTime` |  |  |  |
| 44 | `SC.PEN.PAR.AUTHORISER` | `ScSettPenParty_Authoriser` | String |  |  |
| 45 | `SC.PEN.PAR.CO.CODE` | `ScSettPenParty_CoCode` | String |  |  |
| 46 | `SC.PEN.PAR.DEPT.CODE` | `ScSettPenParty_DeptCode` | String |  |  |
| 47 | `SC.PEN.PAR.AUDITOR.CODE` | `ScSettPenParty_AuditorCode` | String |  |  |
| 48 | `SC.PEN.PAR.AUDIT.DATE.TIME` | `ScSettPenParty_AuditDateTime` | String |  |  |
