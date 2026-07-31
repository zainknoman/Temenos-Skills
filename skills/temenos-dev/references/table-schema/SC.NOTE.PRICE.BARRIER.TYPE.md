# SC.NOTE.PRICE.BARRIER.TYPE — Table Schema

> Source: `INSERTS/I_F.SC.NOTE.PRICE.BARRIER.TYPE` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PBT.DESCRIPTION` | `ScNotePriceBarrierType_Description` |  |  |  |
| 2 | `SC.PBT.RESERVED.10` | `ScNotePriceBarrierType_Reserved10` | TField |  |  |
| 3 | `SC.PBT.RESERVED.9` | `ScNotePriceBarrierType_Reserved9` | TField |  |  |
| 4 | `SC.PBT.RESERVED.8` | `ScNotePriceBarrierType_Reserved8` | TField |  |  |
| 5 | `SC.PBT.RESERVED.7` | `ScNotePriceBarrierType_Reserved7` | TField |  |  |
| 6 | `SC.PBT.RESERVED.6` | `ScNotePriceBarrierType_Reserved6` | TField |  |  |
| 7 | `SC.PBT.RESERVED.5` | `ScNotePriceBarrierType_Reserved5` | TField |  |  |
| 8 | `SC.PBT.RESERVED.4` | `ScNotePriceBarrierType_Reserved4` | TField |  |  |
| 9 | `SC.PBT.RESERVED.3` | `ScNotePriceBarrierType_Reserved3` | TField |  |  |
| 10 | `SC.PBT.RESERVED.2` | `ScNotePriceBarrierType_Reserved2` | TField |  |  |
| 11 | `SC.PBT.RESERVED.1` | `ScNotePriceBarrierType_Reserved1` | TField |  |  |
| 12 | `SC.PBT.LOCAL.REF` | `ScNotePriceBarrierType_LocalRef` |  |  |  |
| 13 | `SC.PBT.RECORD.STATUS` | `ScNotePriceBarrierType_RecordStatus` | String |  |  |
| 14 | `SC.PBT.CURR.NO` | `ScNotePriceBarrierType_CurrNo` | String |  |  |
| 15 | `SC.PBT.INPUTTER` | `ScNotePriceBarrierType_Inputter` |  |  |  |
| 16 | `SC.PBT.DATE.TIME` | `ScNotePriceBarrierType_DateTime` |  |  |  |
| 17 | `SC.PBT.AUTHORISER` | `ScNotePriceBarrierType_Authoriser` | String |  |  |
| 18 | `SC.PBT.CO.CODE` | `ScNotePriceBarrierType_CoCode` | String |  |  |
| 19 | `SC.PBT.DEPT.CODE` | `ScNotePriceBarrierType_DeptCode` | String |  |  |
| 20 | `SC.PBT.AUDITOR.CODE` | `ScNotePriceBarrierType_AuditorCode` | String |  |  |
| 21 | `SC.PBT.AUDIT.DATE.TIME` | `ScNotePriceBarrierType_AuditDateTime` | String |  |  |
