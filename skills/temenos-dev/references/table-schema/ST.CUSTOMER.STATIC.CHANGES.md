# ST.CUSTOMER.STATIC.CHANGES — Table Schema

> Source: `INSERTS/I_F.ST.CUSTOMER.STATIC.CHANGES` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EXT.CUS.CHG.CUSTOMER.REF` | `StCustomerStaticChanges_CustomerRef` | TField |  |  |
| 2 | `EXT.CUS.CHG.EVENT.NAME` | `StCustomerStaticChanges_EventName` | TField |  |  |
| 3 | `EXT.CUS.CHG.EVENT.DATE` | `StCustomerStaticChanges_EventDate` | TField |  |  |
| 4 | `EXT.CUS.CHG.EVENT.TIME` | `StCustomerStaticChanges_EventTime` | TField |  |  |
| 5 | `EXT.CUS.CHG.RECORD.STATUS` | `StCustomerStaticChanges_RecordStatus` | String |  |  |
| 6 | `EXT.CUS.CHG.CURR.NO` | `StCustomerStaticChanges_CurrNo` | String |  |  |
| 7 | `EXT.CUS.CHG.INPUTTER` | `StCustomerStaticChanges_Inputter` |  |  |  |
| 8 | `EXT.CUS.CHG.DATE.TIME` | `StCustomerStaticChanges_DateTime` |  |  |  |
| 9 | `EXT.CUS.CHG.AUTHORISER` | `StCustomerStaticChanges_Authoriser` | String |  |  |
| 10 | `EXT.CUS.CHG.CO.CODE` | `StCustomerStaticChanges_CoCode` | String |  |  |
| 11 | `EXT.CUS.CHG.DEPT.CODE` | `StCustomerStaticChanges_DeptCode` | String |  |  |
| 12 | `EXT.CUS.CHG.AUDITOR.CODE` | `StCustomerStaticChanges_AuditorCode` | String |  |  |
| 13 | `EXT.CUS.CHG.AUDIT.DATE.TIME` | `StCustomerStaticChanges_AuditDateTime` | String |  |  |
