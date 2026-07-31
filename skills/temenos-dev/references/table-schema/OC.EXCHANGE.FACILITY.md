# OC.EXCHANGE.FACILITY — Table Schema

> Source: `INSERTS/I_F.OC.EXCHANGE.FACILITY` in `OC_Parameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OC.EXCH.FAC.EXCHANGE.NAME` | `OcExchangeFacility_ExchangeName` |  |  |  |
| 2 | `OC.EXCH.FAC.EXCHANGE.LEI` | `OcExchangeFacility_ExchangeLei` | TField | No | Denotes the legal entity identifier of the exchange facility platform. Validation Rules: Optional field. Upto 50 alphanumeric characters |
| 3 | `OC.EXCH.FAC.INTERFACE` | `OcExchangeFacility_Interface` | TField | No | denotes how the deals done on a Swap Exchange Facility (SEF), or Trading Platform are read into T24. If interface is Auto then there is a straight through interface available between SEF and T24 i.e. there is no manual capture of trade required in T24, if �Manual� then Bank user has to manually capture the trade details in T24. Reserved for future use. Validation Rules: Optional field Valid Values are Auto and Manual. |
| 4 | `OC.EXCH.FAC.RESERVED10` | `OcExchangeFacility_Reserved10` | TField |  |  |
| 5 | `OC.EXCH.FAC.RESERVED9` | `OcExchangeFacility_Reserved9` | TField |  |  |
| 6 | `OC.EXCH.FAC.RESERVED8` | `OcExchangeFacility_Reserved8` | TField |  |  |
| 7 | `OC.EXCH.FAC.RESERVED7` | `OcExchangeFacility_Reserved7` | TField |  |  |
| 8 | `OC.EXCH.FAC.RESERVED6` | `OcExchangeFacility_Reserved6` | TField |  |  |
| 9 | `OC.EXCH.FAC.RESERVED5` | `OcExchangeFacility_Reserved5` | TField |  |  |
| 10 | `OC.EXCH.FAC.RESERVED4` | `OcExchangeFacility_Reserved4` | TField |  |  |
| 11 | `OC.EXCH.FAC.RESERVED3` | `OcExchangeFacility_Reserved3` | TField |  |  |
| 12 | `OC.EXCH.FAC.RESERVED2` | `OcExchangeFacility_Reserved2` | TField |  |  |
| 13 | `OC.EXCH.FAC.RESERVED1` | `OcExchangeFacility_Reserved1` | TField |  |  |
| 14 | `OC.EXCH.FAC.LOCAL.REF` | `OcExchangeFacility_LocalRef` |  |  |  |
| 15 | `OC.EXCH.FAC.RECORD.STATUS` | `OcExchangeFacility_RecordStatus` | String |  |  |
| 16 | `OC.EXCH.FAC.CURR.NO` | `OcExchangeFacility_CurrNo` | String |  |  |
| 17 | `OC.EXCH.FAC.INPUTTER` | `OcExchangeFacility_Inputter` |  |  |  |
| 18 | `OC.EXCH.FAC.DATE.TIME` | `OcExchangeFacility_DateTime` |  |  |  |
| 19 | `OC.EXCH.FAC.AUTHORISER` | `OcExchangeFacility_Authoriser` | String |  |  |
| 20 | `OC.EXCH.FAC.CO.CODE` | `OcExchangeFacility_CoCode` | String |  |  |
| 21 | `OC.EXCH.FAC.DEPT.CODE` | `OcExchangeFacility_DeptCode` | String |  |  |
| 22 | `OC.EXCH.FAC.AUDITOR.CODE` | `OcExchangeFacility_AuditorCode` | String |  |  |
| 23 | `OC.EXCH.FAC.AUDIT.DATE.TIME` | `OcExchangeFacility_AuditDateTime` | String |  |  |
