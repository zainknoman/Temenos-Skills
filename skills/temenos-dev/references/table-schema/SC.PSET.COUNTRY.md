# SC.PSET.COUNTRY — Table Schema

> Source: `INSERTS/I_F.SC.PSET.COUNTRY` in `SC_SctTrading.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PSC.CLEARING.CODE` | `ScPsetCountry_ClearingCode` | TField |  | This Field will be defaulted from ID It is a NO INPUT field |
| 2 | `SC.PSC.CUSTODIAN.TYPE` | `ScPsetCountry_CustodianType` | TField |  | This Field will be defaulted from ID It is a NO INPUT field |
| 3 | `SC.PSC.PRIORITY` | `ScPsetCountry_Priority` |  |  |  |
| 4 | `SC.PSC.RESERVED.10` | `ScPsetCountry_Reserved10` | TField |  |  |
| 5 | `SC.PSC.RESERVED.9` | `ScPsetCountry_Reserved9` | TField |  |  |
| 6 | `SC.PSC.RESERVED.8` | `ScPsetCountry_Reserved8` | TField |  |  |
| 7 | `SC.PSC.RESERVED.7` | `ScPsetCountry_Reserved7` | TField |  |  |
| 8 | `SC.PSC.RESERVED.6` | `ScPsetCountry_Reserved6` | TField |  |  |
| 9 | `SC.PSC.RESERVED.5` | `ScPsetCountry_Reserved5` | TField |  |  |
| 10 | `SC.PSC.RESERVED.4` | `ScPsetCountry_Reserved4` | TField |  |  |
| 11 | `SC.PSC.RESERVED.3` | `ScPsetCountry_Reserved3` | TField |  |  |
| 12 | `SC.PSC.RESERVED.2` | `ScPsetCountry_Reserved2` | TField |  |  |
| 13 | `SC.PSC.RESERVED.1` | `ScPsetCountry_Reserved1` | TField |  |  |
| 14 | `SC.PSC.LOCAL.REF` | `ScPsetCountry_LocalRef` |  |  |  |
| 15 | `SC.PSC.OVERRIDE` | `ScPsetCountry_Override` |  |  |  |
| 16 | `SC.PSC.RECORD.STATUS` | `ScPsetCountry_RecordStatus` | String |  |  |
| 17 | `SC.PSC.CURR.NO` | `ScPsetCountry_CurrNo` | String |  |  |
| 18 | `SC.PSC.INPUTTER` | `ScPsetCountry_Inputter` |  |  |  |
| 19 | `SC.PSC.DATE.TIME` | `ScPsetCountry_DateTime` |  |  |  |
| 20 | `SC.PSC.AUTHORISER` | `ScPsetCountry_Authoriser` | String |  |  |
| 21 | `SC.PSC.CO.CODE` | `ScPsetCountry_CoCode` | String |  |  |
| 22 | `SC.PSC.DEPT.CODE` | `ScPsetCountry_DeptCode` | String |  |  |
| 23 | `SC.PSC.AUDITOR.CODE` | `ScPsetCountry_AuditorCode` | String |  |  |
| 24 | `SC.PSC.AUDIT.DATE.TIME` | `ScPsetCountry_AuditDateTime` | String |  |  |
