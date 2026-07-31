# ST.REGULATORY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ST.REGULATORY.PARAMETER` in `RT_Regulation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.RP.DESC` | `StRegulatoryParameter_Desc` |  |  |  |
| 2 | `ST.RP.CURR.RULE.BOOK` | `StRegulatoryParameter_CurrRuleBook` | TField |  | Field to hold the release of regulation. Used to turn on and off the new rules when the regulation changes Validation rules Allows values from 1950 to 2049. System doesn't allow to define the value which is present in PREV.RULE.BOOK field. Once the rule is defined and authorised, system doesn't allow to make this field to blank. |
| 3 | `ST.RP.PREV.RULE.BOOK` | `StRegulatoryParameter_PrevRuleBook` |  |  |  |
| 4 | `ST.RP.AUTO.CREATE.RECS` | `StRegulatoryParameter_AutoCreateRecs` | TField |  | Field to specify whether updation of indicias or automatic creation of Supplementary Info records are allowed during the Indicia service Validation Rules: Yes/ No field |
| 5 | `ST.RP.INDICIA.CUST.SELECT.API` | `StRegulatoryParameter_IndiciaCustSelectApi` | TField |  | Field to define the API that returns the customers to be processed in automatic creation of FATCA.CUSTOMER.SUPPLEMENTARY.INFO/CRS.CUST.SUPP.INFO service (based on the indicia) Validation Rules: Allowed values are Blank or RT.GET.INDICIA.CUST.LIST |
| 6 | `ST.RP.RESERVED.3` | `StRegulatoryParameter_Reserved3` | TField |  |  |
| 7 | `ST.RP.RESERVED.4` | `StRegulatoryParameter_Reserved4` | TField |  |  |
| 8 | `ST.RP.RESERVED.5` | `StRegulatoryParameter_Reserved5` | TField |  |  |
| 9 | `ST.RP.RESERVED.6` | `StRegulatoryParameter_Reserved6` | TField |  |  |
| 10 | `ST.RP.RESERVED.7` | `StRegulatoryParameter_Reserved7` | TField |  |  |
| 11 | `ST.RP.RESERVED.8` | `StRegulatoryParameter_Reserved8` | TField |  |  |
| 12 | `ST.RP.RESERVED.9` | `StRegulatoryParameter_Reserved9` | TField |  |  |
| 13 | `ST.RP.RESERVED.10` | `StRegulatoryParameter_Reserved10` | TField |  |  |
| 14 | `ST.RP.RESERVED.11` | `StRegulatoryParameter_Reserved11` | TField |  |  |
| 15 | `ST.RP.RESERVED.12` | `StRegulatoryParameter_Reserved12` | TField |  |  |
| 16 | `ST.RP.RESERVED.13` | `StRegulatoryParameter_Reserved13` | TField |  |  |
| 17 | `ST.RP.RESERVED.14` | `StRegulatoryParameter_Reserved14` | TField |  |  |
| 18 | `ST.RP.RESERVED.15` | `StRegulatoryParameter_Reserved15` | TField |  |  |
| 19 | `ST.RP.RESERVED.16` | `StRegulatoryParameter_Reserved16` | TField |  |  |
| 20 | `ST.RP.RESERVED.17` | `StRegulatoryParameter_Reserved17` | TField |  |  |
| 21 | `ST.RP.RESERVED.18` | `StRegulatoryParameter_Reserved18` | TField |  |  |
| 22 | `ST.RP.RESERVED.19` | `StRegulatoryParameter_Reserved19` | TField |  |  |
| 23 | `ST.RP.RESERVED.20` | `StRegulatoryParameter_Reserved20` | TField |  |  |
| 24 | `ST.RP.LOCAL.REF` | `StRegulatoryParameter_LocalRef` |  |  |  |
| 25 | `ST.RP.OVERRIDE` | `StRegulatoryParameter_Override` |  |  |  |
| 26 | `ST.RP.RECORD.STATUS` | `StRegulatoryParameter_RecordStatus` | String |  |  |
| 27 | `ST.RP.CURR.NO` | `StRegulatoryParameter_CurrNo` | String |  |  |
| 28 | `ST.RP.INPUTTER` | `StRegulatoryParameter_Inputter` |  |  |  |
| 29 | `ST.RP.DATE.TIME` | `StRegulatoryParameter_DateTime` |  |  |  |
| 30 | `ST.RP.AUTHORISER` | `StRegulatoryParameter_Authoriser` | String |  |  |
| 31 | `ST.RP.CO.CODE` | `StRegulatoryParameter_CoCode` | String |  |  |
| 32 | `ST.RP.DEPT.CODE` | `StRegulatoryParameter_DeptCode` | String |  |  |
| 33 | `ST.RP.AUDITOR.CODE` | `StRegulatoryParameter_AuditorCode` | String |  |  |
| 34 | `ST.RP.AUDIT.DATE.TIME` | `StRegulatoryParameter_AuditDateTime` | String |  |  |
