# PP.NO.RMA — Table Schema

> Source: `INSERTS/I_F.PP.NO.RMA` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.NOR.CompanyID` | `PpNoRma_Companyid` | TField |  | This is a No-Input field which gets Auto-Populated on Clicking Validate button Example : BNK,GB1 |
| 2 | `PP.NOR.StartDate` | `PpNoRma_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Autopopulated from the ID upon clicking Validate Button |
| 3 | `PP.NOR.EndDate` | `PpNoRma_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date,the record will be set as Inactive by the payments hub. |
| 4 | `PP.NOR.LinkID` | `PpNoRma_Linkid` | TField |  | Its a No-Input field Value is populated by concatenating all the Primary Keys |
| 5 | `PP.NOR.RESERVED.5` | `PpNoRma_Reserved5` | TField |  | Standard T24 field. Reserved for future use |
| 6 | `PP.NOR.RESERVED.4` | `PpNoRma_Reserved4` | TField |  | Standard T24 field. Reserved for future use |
| 7 | `PP.NOR.RESERVED.3` | `PpNoRma_Reserved3` | TField |  | Standard T24 field. Reserved for future use |
| 8 | `PP.NOR.RESERVED.2` | `PpNoRma_Reserved2` | TField |  | Standard T24 field. Reserved for future use |
| 9 | `PP.NOR.RESERVED.1` | `PpNoRma_Reserved1` | TField |  | Standard T24 field. Reserved for future use |
| 10 | `PP.NOR.LOCAL.REF` | `PpNoRma_LocalRef` |  |  |  |
| 11 | `PP.NOR.OVERRIDE` | `PpNoRma_Override` |  |  |  |
| 12 | `PP.NOR.RECORD.STATUS` | `PpNoRma_RecordStatus` | String |  |  |
| 13 | `PP.NOR.CURR.NO` | `PpNoRma_CurrNo` | String |  |  |
| 14 | `PP.NOR.INPUTTER` | `PpNoRma_Inputter` |  |  |  |
| 15 | `PP.NOR.DATE.TIME` | `PpNoRma_DateTime` |  |  |  |
| 16 | `PP.NOR.AUTHORISER` | `PpNoRma_Authoriser` | String |  |  |
| 17 | `PP.NOR.CO.CODE` | `PpNoRma_CoCode` | String |  |  |
| 18 | `PP.NOR.DEPT.CODE` | `PpNoRma_DeptCode` | String |  |  |
| 19 | `PP.NOR.AUDITOR.CODE` | `PpNoRma_AuditorCode` | String |  |  |
| 20 | `PP.NOR.AUDIT.DATE.TIME` | `PpNoRma_AuditDateTime` | String |  |  |
