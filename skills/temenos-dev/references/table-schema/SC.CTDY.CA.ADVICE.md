# SC.CTDY.CA.ADVICE — Table Schema

> Source: `INSERTS/I_F.SC.CTDY.CA.ADVICE` in `SC_SccEventNotification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CTDY.CA.IN.MT564.FUNC` | `ScCtdyCaAdvice_InMt564Func` |  |  |  |
| 2 | `SC.CTDY.CA.IN.MT564.STATUS` | `ScCtdyCaAdvice_InMt564Status` |  |  |  |
| 3 | `SC.CTDY.CA.IN.MT564.FUNC.STATUS` | `ScCtdyCaAdvice_InMt564FuncStatus` |  |  |  |
| 4 | `SC.CTDY.CA.SEND.MT564.CANC` | `ScCtdyCaAdvice_SendMt564Canc` | TField |  | This field indicates whether to generate MT564 message, when diary is reversed Validation Rules: Accepted Values : YES , BLANK |
| 5 | `SC.CTDY.CA.564.OUT.FUNC` | `ScCtdyCaAdvice_564OutFunc` |  |  |  |
| 6 | `SC.CTDY.CA.564.OUT.NB.OF.DAYS` | `ScCtdyCaAdvice_564OutNbOfDays` |  |  |  |
| 7 | `SC.CTDY.CA.564.OUT.PRI.AFT` | `ScCtdyCaAdvice_564OutPriAft` |  |  |  |
| 8 | `SC.CTDY.CA.564.OUT.SEL.DATE` | `ScCtdyCaAdvice_564OutSelDate` |  |  |  |
| 9 | `SC.CTDY.CA.RESERVED30` | `ScCtdyCaAdvice_Reserved30` | TField |  |  |
| 10 | `SC.CTDY.CA.RESERVED29` | `ScCtdyCaAdvice_Reserved29` | TField |  |  |
| 11 | `SC.CTDY.CA.RESERVED28` | `ScCtdyCaAdvice_Reserved28` | TField |  |  |
| 12 | `SC.CTDY.CA.RESERVED27` | `ScCtdyCaAdvice_Reserved27` | TField |  |  |
| 13 | `SC.CTDY.CA.RESERVED26` | `ScCtdyCaAdvice_Reserved26` | TField |  |  |
| 14 | `SC.CTDY.CA.RESERVED25` | `ScCtdyCaAdvice_Reserved25` | TField |  |  |
| 15 | `SC.CTDY.CA.RESERVED24` | `ScCtdyCaAdvice_Reserved24` | TField |  |  |
| 16 | `SC.CTDY.CA.RESERVED23` | `ScCtdyCaAdvice_Reserved23` | TField |  |  |
| 17 | `SC.CTDY.CA.RESERVED22` | `ScCtdyCaAdvice_Reserved22` | TField |  |  |
| 18 | `SC.CTDY.CA.RESERVED21` | `ScCtdyCaAdvice_Reserved21` | TField |  |  |
| 19 | `SC.CTDY.CA.RESERVED20` | `ScCtdyCaAdvice_Reserved20` | TField |  |  |
| 20 | `SC.CTDY.CA.RESERVED19` | `ScCtdyCaAdvice_Reserved19` | TField |  |  |
| 21 | `SC.CTDY.CA.RESERVED18` | `ScCtdyCaAdvice_Reserved18` | TField |  |  |
| 22 | `SC.CTDY.CA.RESERVED17` | `ScCtdyCaAdvice_Reserved17` | TField |  |  |
| 23 | `SC.CTDY.CA.RESERVED16` | `ScCtdyCaAdvice_Reserved16` | TField |  |  |
| 24 | `SC.CTDY.CA.RESERVED15` | `ScCtdyCaAdvice_Reserved15` | TField |  |  |
| 25 | `SC.CTDY.CA.RESERVED14` | `ScCtdyCaAdvice_Reserved14` | TField |  |  |
| 26 | `SC.CTDY.CA.RESERVED13` | `ScCtdyCaAdvice_Reserved13` | TField |  |  |
| 27 | `SC.CTDY.CA.RESERVED12` | `ScCtdyCaAdvice_Reserved12` | TField |  |  |
| 28 | `SC.CTDY.CA.RESERVED11` | `ScCtdyCaAdvice_Reserved11` | TField |  |  |
| 29 | `SC.CTDY.CA.RESERVED10` | `ScCtdyCaAdvice_Reserved10` | TField |  |  |
| 30 | `SC.CTDY.CA.RESERVED09` | `ScCtdyCaAdvice_Reserved09` | TField |  |  |
| 31 | `SC.CTDY.CA.RESERVED08` | `ScCtdyCaAdvice_Reserved08` | TField |  |  |
| 32 | `SC.CTDY.CA.RESERVED07` | `ScCtdyCaAdvice_Reserved07` | TField |  |  |
| 33 | `SC.CTDY.CA.RESERVED06` | `ScCtdyCaAdvice_Reserved06` | TField |  |  |
| 34 | `SC.CTDY.CA.RESERVED05` | `ScCtdyCaAdvice_Reserved05` | TField |  |  |
| 35 | `SC.CTDY.CA.RESERVED04` | `ScCtdyCaAdvice_Reserved04` | TField |  |  |
| 36 | `SC.CTDY.CA.RESERVED03` | `ScCtdyCaAdvice_Reserved03` | TField |  |  |
| 37 | `SC.CTDY.CA.RESERVED02` | `ScCtdyCaAdvice_Reserved02` | TField |  |  |
| 38 | `SC.CTDY.CA.RESERVED01` | `ScCtdyCaAdvice_Reserved01` | TField |  |  |
| 39 | `SC.CTDY.CA.LOCAL.REF` | `ScCtdyCaAdvice_LocalRef` |  |  |  |
| 40 | `SC.CTDY.CA.OVERRIDE` | `ScCtdyCaAdvice_Override` |  |  |  |
| 41 | `SC.CTDY.CA.RECORD.STATUS` | `ScCtdyCaAdvice_RecordStatus` | String |  |  |
| 42 | `SC.CTDY.CA.CURR.NO` | `ScCtdyCaAdvice_CurrNo` | String |  |  |
| 43 | `SC.CTDY.CA.INPUTTER` | `ScCtdyCaAdvice_Inputter` |  |  |  |
| 44 | `SC.CTDY.CA.DATE.TIME` | `ScCtdyCaAdvice_DateTime` |  |  |  |
| 45 | `SC.CTDY.CA.AUTHORISER` | `ScCtdyCaAdvice_Authoriser` | String |  |  |
| 46 | `SC.CTDY.CA.CO.CODE` | `ScCtdyCaAdvice_CoCode` | String |  |  |
| 47 | `SC.CTDY.CA.DEPT.CODE` | `ScCtdyCaAdvice_DeptCode` | String |  |  |
| 48 | `SC.CTDY.CA.AUDITOR.CODE` | `ScCtdyCaAdvice_AuditorCode` | String |  |  |
| 49 | `SC.CTDY.CA.AUDIT.DATE.TIME` | `ScCtdyCaAdvice_AuditDateTime` | String |  |  |
