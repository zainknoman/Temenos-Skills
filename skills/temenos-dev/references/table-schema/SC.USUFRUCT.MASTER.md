# SC.USUFRUCT.MASTER — Table Schema

> Source: `INSERTS/I_F.SC.USUFRUCT.MASTER` in `SC_ScoPortfolioMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.USFR.USUFRUCT.STATUS` | `ScUsufructMaster_UsufructStatus` | TField | Yes | This ACTIVE/INACTIVE status of Usufruct Master When the status is set as INACTIVE, Usufruct arrangement will not be considered and income will be bookinto bare owner instead of usufructers. Validation Rules Mandatory Field |
| 2 | `SC.USFR.USUFRUCT.CUST` | `ScUsufructMaster_UsufructCust` |  |  |  |
| 3 | `SC.USFR.USUFRUCT.PERCENT` | `ScUsufructMaster_UsufructPercent` |  |  |  |
| 4 | `SC.USFR.USUFRUCT.ACCOUNT` | `ScUsufructMaster_UsufructAccount` |  |  |  |
| 5 | `SC.USFR.USUFRUCT.ACCT.CCY` | `ScUsufructMaster_UsufructAcctCcy` |  |  |  |
| 6 | `SC.USFR.MV.RESERVED05` | `ScUsufructMaster_MvReserved05` |  |  |  |
| 7 | `SC.USFR.MV.RESERVED04` | `ScUsufructMaster_MvReserved04` |  |  |  |
| 8 | `SC.USFR.MV.RESERVED03` | `ScUsufructMaster_MvReserved03` |  |  |  |
| 9 | `SC.USFR.MV.RESERVED02` | `ScUsufructMaster_MvReserved02` |  |  |  |
| 10 | `SC.USFR.MV.RESERVED01` | `ScUsufructMaster_MvReserved01` |  |  |  |
| 11 | `SC.USFR.RESERVED05` | `ScUsufructMaster_Reserved05` | TField |  |  |
| 12 | `SC.USFR.RESERVED04` | `ScUsufructMaster_Reserved04` | TField |  |  |
| 13 | `SC.USFR.RESERVED03` | `ScUsufructMaster_Reserved03` | TField |  |  |
| 14 | `SC.USFR.RESERVED02` | `ScUsufructMaster_Reserved02` | TField |  |  |
| 15 | `SC.USFR.RESERVED01` | `ScUsufructMaster_Reserved01` | TField |  |  |
| 16 | `SC.USFR.LOCAL.REF` | `ScUsufructMaster_LocalRef` |  |  |  |
| 17 | `SC.USFR.OVERRIDE` | `ScUsufructMaster_Override` |  |  |  |
| 18 | `SC.USFR.RECORD.STATUS` | `ScUsufructMaster_RecordStatus` | String |  |  |
| 19 | `SC.USFR.CURR.NO` | `ScUsufructMaster_CurrNo` | String |  |  |
| 20 | `SC.USFR.INPUTTER` | `ScUsufructMaster_Inputter` |  |  |  |
| 21 | `SC.USFR.DATE.TIME` | `ScUsufructMaster_DateTime` |  |  |  |
| 22 | `SC.USFR.AUTHORISER` | `ScUsufructMaster_Authoriser` | String |  |  |
| 23 | `SC.USFR.CO.CODE` | `ScUsufructMaster_CoCode` | String |  |  |
| 24 | `SC.USFR.DEPT.CODE` | `ScUsufructMaster_DeptCode` | String |  |  |
| 25 | `SC.USFR.AUDITOR.CODE` | `ScUsufructMaster_AuditorCode` | String |  |  |
| 26 | `SC.USFR.AUDIT.DATE.TIME` | `ScUsufructMaster_AuditDateTime` | String |  |  |
