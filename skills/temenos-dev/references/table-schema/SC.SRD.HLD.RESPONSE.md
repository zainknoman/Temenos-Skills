# SC.SRD.HLD.RESPONSE — Table Schema

> Source: `INSERTS/I_F.SC.SRD.HLD.RESPONSE` in `SC_ScSrdEventCapture.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SRP.RESERVED1` | `ScSrdHldResponse_Reserved1` | TField |  |  |
| 2 | `SC.SRP.SECURITY.NO` | `ScSrdHldResponse_SecurityNo` |  |  |  |
| 3 | `SC.SRP.DEPOSITORY` | `ScSrdHldResponse_Depository` | TField |  | Field holds the Depository number where the shares are held |
| 4 | `SC.SRP.SUB.ACCOUNT` | `ScSrdHldResponse_SubAccount` | TField |  | Field holds the sub account of the depository |
| 5 | `SC.SRP.NOMINAL` | `ScSrdHldResponse_Nominal` | TField |  | Field denotes the Portfolio Holding as on Record Date without considering unsettled nominals |
| 6 | `SC.SRP.INITIAL.HLDING.DATE` | `ScSrdHldResponse_InitialHldingDate` | TField |  | Field denotes the initial purchase date of the shares |
| 7 | `SC.SRP.BELOW.THRESHOLD` | `ScSrdHldResponse_BelowThreshold` | TField |  | Field indicates if the NOMINAL is below the threshold quantity |
| 8 | `SC.SRP.CUSTOMER.NO` | `ScSrdHldResponse_CustomerNo` | TField |  |  |
| 9 | `SC.SRP.I.S.I.N` | `ScSrdHldResponse_ISIN` | TField |  | Field holds the ISIN for which the event is taking place. |
| 10 | `SC.SRP.RESERVED3` | `ScSrdHldResponse_Reserved3` | TField |  |  |
| 11 | `SC.SRP.RESERVED4` | `ScSrdHldResponse_Reserved4` | TField |  |  |
| 12 | `SC.SRP.RESERVED5` | `ScSrdHldResponse_Reserved5` | TField |  |  |
| 13 | `SC.SRP.RESERVED6` | `ScSrdHldResponse_Reserved6` | TField |  |  |
| 14 | `SC.SRP.RESERVED7` | `ScSrdHldResponse_Reserved7` | TField |  |  |
| 15 | `SC.SRP.RESERVED8` | `ScSrdHldResponse_Reserved8` | TField |  |  |
| 16 | `SC.SRP.RESERVED9` | `ScSrdHldResponse_Reserved9` | TField |  |  |
| 17 | `SC.SRP.RESERVED10` | `ScSrdHldResponse_Reserved10` | TField |  |  |
| 18 | `SC.SRP.RESERVED11` | `ScSrdHldResponse_Reserved11` | TField |  |  |
| 19 | `SC.SRP.RESERVED12` | `ScSrdHldResponse_Reserved12` | TField |  |  |
| 20 | `SC.SRP.RESERVED13` | `ScSrdHldResponse_Reserved13` | TField |  |  |
| 21 | `SC.SRP.RESERVED14` | `ScSrdHldResponse_Reserved14` | TField |  |  |
| 22 | `SC.SRP.RESERVED15` | `ScSrdHldResponse_Reserved15` | TField |  |  |
| 23 | `SC.SRP.RESERVED16` | `ScSrdHldResponse_Reserved16` | TField |  |  |
| 24 | `SC.SRP.RESERVED17` | `ScSrdHldResponse_Reserved17` | TField |  |  |
| 25 | `SC.SRP.RESERVED18` | `ScSrdHldResponse_Reserved18` | TField |  |  |
| 26 | `SC.SRP.RESERVED19` | `ScSrdHldResponse_Reserved19` | TField |  |  |
| 27 | `SC.SRP.RESERVED20` | `ScSrdHldResponse_Reserved20` | TField |  |  |
| 28 | `SC.SRP.RESERVED21` | `ScSrdHldResponse_Reserved21` | TField |  |  |
| 29 | `SC.SRP.RESERVED22` | `ScSrdHldResponse_Reserved22` | TField |  |  |
| 30 | `SC.SRP.RESERVED23` | `ScSrdHldResponse_Reserved23` | TField |  |  |
| 31 | `SC.SRP.RESERVED24` | `ScSrdHldResponse_Reserved24` | TField |  |  |
| 32 | `SC.SRP.RESERVED25` | `ScSrdHldResponse_Reserved25` | TField |  |  |
| 33 | `SC.SRP.RESERVED26` | `ScSrdHldResponse_Reserved26` | TField |  |  |
| 34 | `SC.SRP.RESERVED27` | `ScSrdHldResponse_Reserved27` | TField |  |  |
| 35 | `SC.SRP.RESERVED28` | `ScSrdHldResponse_Reserved28` | TField |  |  |
| 36 | `SC.SRP.RESERVED29` | `ScSrdHldResponse_Reserved29` | TField |  |  |
| 37 | `SC.SRP.RESERVED30` | `ScSrdHldResponse_Reserved30` | TField |  |  |
| 38 | `SC.SRP.LOCAL.REF` | `ScSrdHldResponse_LocalRef` |  |  |  |
| 39 | `SC.SRP.OVERRIDE` | `ScSrdHldResponse_Override` |  |  |  |
| 40 | `SC.SRP.RECORD.STATUS` | `ScSrdHldResponse_RecordStatus` | String |  |  |
| 41 | `SC.SRP.CURR.NO` | `ScSrdHldResponse_CurrNo` | String |  |  |
| 42 | `SC.SRP.INPUTTER` | `ScSrdHldResponse_Inputter` |  |  |  |
| 43 | `SC.SRP.DATE.TIME` | `ScSrdHldResponse_DateTime` |  |  |  |
| 44 | `SC.SRP.AUTHORISER` | `ScSrdHldResponse_Authoriser` | String |  |  |
| 45 | `SC.SRP.CO.CODE` | `ScSrdHldResponse_CoCode` | String |  |  |
| 46 | `SC.SRP.DEPT.CODE` | `ScSrdHldResponse_DeptCode` | String |  |  |
| 47 | `SC.SRP.AUDITOR.CODE` | `ScSrdHldResponse_AuditorCode` | String |  |  |
| 48 | `SC.SRP.AUDIT.DATE.TIME` | `ScSrdHldResponse_AuditDateTime` | String |  |  |
