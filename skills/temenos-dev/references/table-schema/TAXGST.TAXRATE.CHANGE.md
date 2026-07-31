# TAXGST.TAXRATE.CHANGE — Table Schema

> Source: `INSERTS/I_F.TAXGST.TAXRATE.CHANGE` in `TAXGST_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TAXRATE.CHANGE.APPLICATION` | `TaxgstTaxrateChange_Application` |  |  |  |
| 2 | `TAXRATE.CHANGE.APP.OLD.TAX.CODE` | `TaxgstTaxrateChange_AppOldTaxCode` |  |  |  |
| 3 | `TAXRATE.CHANGE.APP.NEW.TAX.CODE` | `TaxgstTaxrateChange_AppNewTaxCode` |  |  |  |
| 4 | `TAXRATE.CHANGE.CONTRACT.ID` | `TaxgstTaxrateChange_ContractId` |  |  |  |
| 5 | `TAXRATE.CHANGE.CONT.OLD.TAX.CODE` | `TaxgstTaxrateChange_ContOldTaxCode` |  |  |  |
| 6 | `TAXRATE.CHANGE.CONT.NEW.TAX.CODE` | `TaxgstTaxrateChange_ContNewTaxCode` |  |  |  |
| 7 | `TAXRATE.CHANGE.ADJ.EFF.DATE` | `TaxgstTaxrateChange_AdjEffDate` | TField |  | Indicates the effective date for tax adjustment. |
| 8 | `TAXRATE.CHANGE.LOCAL.REF` | `TaxgstTaxrateChange_LocalRef` |  |  |  |
| 9 | `TAXRATE.CHANGE.RESERVED.10` | `TaxgstTaxrateChange_Reserved10` | TField |  |  |
| 10 | `TAXRATE.CHANGE.RESERVED.9` | `TaxgstTaxrateChange_Reserved9` | TField |  |  |
| 11 | `TAXRATE.CHANGE.RESERVED.8` | `TaxgstTaxrateChange_Reserved8` | TField |  |  |
| 12 | `TAXRATE.CHANGE.RESERVED.7` | `TaxgstTaxrateChange_Reserved7` | TField |  |  |
| 13 | `TAXRATE.CHANGE.RESERVED.6` | `TaxgstTaxrateChange_Reserved6` | TField |  |  |
| 14 | `TAXRATE.CHANGE.RESERVED.5` | `TaxgstTaxrateChange_Reserved5` | TField |  |  |
| 15 | `TAXRATE.CHANGE.RESERVED.4` | `TaxgstTaxrateChange_Reserved4` | TField |  |  |
| 16 | `TAXRATE.CHANGE.RESERVED.3` | `TaxgstTaxrateChange_Reserved3` | TField |  |  |
| 17 | `TAXRATE.CHANGE.RESERVED.2` | `TaxgstTaxrateChange_Reserved2` | TField |  |  |
| 18 | `TAXRATE.CHANGE.RESERVED.1` | `TaxgstTaxrateChange_Reserved1` | TField |  |  |
| 19 | `TAXRATE.CHANGE.RECORD.STATUS` | `TaxgstTaxrateChange_RecordStatus` | String |  |  |
| 20 | `TAXRATE.CHANGE.CURR.NO` | `TaxgstTaxrateChange_CurrNo` | String |  |  |
| 21 | `TAXRATE.CHANGE.INPUTTER` | `TaxgstTaxrateChange_Inputter` |  |  |  |
| 22 | `TAXRATE.CHANGE.DATE.TIME` | `TaxgstTaxrateChange_DateTime` |  |  |  |
| 23 | `TAXRATE.CHANGE.AUTHORISER` | `TaxgstTaxrateChange_Authoriser` | String |  |  |
| 24 | `TAXRATE.CHANGE.CO.CODE` | `TaxgstTaxrateChange_CoCode` | String |  |  |
| 25 | `TAXRATE.CHANGE.DEPT.CODE` | `TaxgstTaxrateChange_DeptCode` | String |  |  |
| 26 | `TAXRATE.CHANGE.AUDITOR.CODE` | `TaxgstTaxrateChange_AuditorCode` | String |  |  |
| 27 | `TAXRATE.CHANGE.AUDIT.DATE.TIME` | `TaxgstTaxrateChange_AuditDateTime` | String |  |  |
