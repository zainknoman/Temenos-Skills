# SC.SETT.PARTY.TAGS — Table Schema

> Source: `INSERTS/I_F.SC.SETT.PARTY.TAGS` in `SC_SctSettlement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SETTPTY.DEPO.BIC` | `ScSettPartyTags_DepoBic` | TField |  | This field holds the BIC code of Receiver The receiver of the swift message would be the Bank's custodian Validation Rules: Defaulted from id, Input not allowed |
| 2 | `SC.SETTPTY.PSET` | `ScSettPartyTags_Pset` | TField |  | This field holds the PSET value Validation Rules: Defaulted from id, Input not allowed |
| 3 | `SC.SETTPTY.RULE.NAME` | `ScSettPartyTags_RuleName` |  |  |  |
| 4 | `SC.SETTPTY.REAG` | `ScSettPartyTags_Reag` |  |  |  |
| 5 | `SC.SETTPTY.REAG.AC` | `ScSettPartyTags_ReagAc` |  |  |  |
| 6 | `SC.SETTPTY.DEAG` | `ScSettPartyTags_Deag` |  |  |  |
| 7 | `SC.SETTPTY.DEAG.AC` | `ScSettPartyTags_DeagAc` |  |  |  |
| 8 | `SC.SETTPTY.RECU` | `ScSettPartyTags_Recu` |  |  |  |
| 9 | `SC.SETTPTY.RECU.AC` | `ScSettPartyTags_RecuAc` |  |  |  |
| 10 | `SC.SETTPTY.DECU` | `ScSettPartyTags_Decu` |  |  |  |
| 11 | `SC.SETTPTY.DECU.AC` | `ScSettPartyTags_DecuAc` |  |  |  |
| 12 | `SC.SETTPTY.BUYR` | `ScSettPartyTags_Buyr` |  |  |  |
| 13 | `SC.SETTPTY.BUYR.AC` | `ScSettPartyTags_BuyrAc` |  |  |  |
| 14 | `SC.SETTPTY.SELL` | `ScSettPartyTags_Sell` |  |  |  |
| 15 | `SC.SETTPTY.SELL.AC` | `ScSettPartyTags_SellAc` |  |  |  |
| 16 | `SC.SETTPTY.RESERVED1` | `ScSettPartyTags_Reserved1` | TField |  |  |
| 17 | `SC.SETTPTY.RESERVED2` | `ScSettPartyTags_Reserved2` | TField |  |  |
| 18 | `SC.SETTPTY.RESERVED3` | `ScSettPartyTags_Reserved3` | TField |  |  |
| 19 | `SC.SETTPTY.RESERVED4` | `ScSettPartyTags_Reserved4` | TField |  |  |
| 20 | `SC.SETTPTY.RESERVED5` | `ScSettPartyTags_Reserved5` | TField |  |  |
| 21 | `SC.SETTPTY.RESERVED6` | `ScSettPartyTags_Reserved6` | TField |  |  |
| 22 | `SC.SETTPTY.RESERVED7` | `ScSettPartyTags_Reserved7` | TField |  |  |
| 23 | `SC.SETTPTY.RESERVED8` | `ScSettPartyTags_Reserved8` | TField |  |  |
| 24 | `SC.SETTPTY.RESERVED9` | `ScSettPartyTags_Reserved9` | TField |  |  |
| 25 | `SC.SETTPTY.RESERVED10` | `ScSettPartyTags_Reserved10` | TField |  |  |
| 26 | `SC.SETTPTY.RESERVED11` | `ScSettPartyTags_Reserved11` | TField |  |  |
| 27 | `SC.SETTPTY.RESERVED12` | `ScSettPartyTags_Reserved12` | TField |  |  |
| 28 | `SC.SETTPTY.RESERVED13` | `ScSettPartyTags_Reserved13` | TField |  |  |
| 29 | `SC.SETTPTY.RESERVED14` | `ScSettPartyTags_Reserved14` | TField |  |  |
| 30 | `SC.SETTPTY.RESERVED15` | `ScSettPartyTags_Reserved15` | TField |  |  |
| 31 | `SC.SETTPTY.RESERVED16` | `ScSettPartyTags_Reserved16` | TField |  |  |
| 32 | `SC.SETTPTY.RESERVED17` | `ScSettPartyTags_Reserved17` | TField |  |  |
| 33 | `SC.SETTPTY.RESERVED18` | `ScSettPartyTags_Reserved18` | TField |  |  |
| 34 | `SC.SETTPTY.RESERVED19` | `ScSettPartyTags_Reserved19` | TField |  |  |
| 35 | `SC.SETTPTY.RESERVED20` | `ScSettPartyTags_Reserved20` | TField |  |  |
| 36 | `SC.SETTPTY.LOCAL.REF` | `ScSettPartyTags_LocalRef` |  |  |  |
| 37 | `SC.SETTPTY.OVERRIDE` | `ScSettPartyTags_Override` |  |  |  |
| 38 | `SC.SETTPTY.RECORD.STATUS` | `ScSettPartyTags_RecordStatus` | String |  |  |
| 39 | `SC.SETTPTY.CURR.NO` | `ScSettPartyTags_CurrNo` | String |  |  |
| 40 | `SC.SETTPTY.INPUTTER` | `ScSettPartyTags_Inputter` |  |  |  |
| 41 | `SC.SETTPTY.DATE.TIME` | `ScSettPartyTags_DateTime` |  |  |  |
| 42 | `SC.SETTPTY.AUTHORISER` | `ScSettPartyTags_Authoriser` | String |  |  |
| 43 | `SC.SETTPTY.CO.CODE` | `ScSettPartyTags_CoCode` | String |  |  |
| 44 | `SC.SETTPTY.DEPT.CODE` | `ScSettPartyTags_DeptCode` | String |  |  |
| 45 | `SC.SETTPTY.AUDITOR.CODE` | `ScSettPartyTags_AuditorCode` | String |  |  |
| 46 | `SC.SETTPTY.AUDIT.DATE.TIME` | `ScSettPartyTags_AuditDateTime` | String |  |  |
