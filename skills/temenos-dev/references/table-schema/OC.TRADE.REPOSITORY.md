# OC.TRADE.REPOSITORY — Table Schema

> Source: `INSERTS/I_F.OC.TRADE.REPOSITORY` in `OC_Parameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OC.TR.REP.REPOSITORY.NAME` | `OcTradeRepository_RepositoryName` |  |  |  |
| 2 | `OC.TR.REP.REPOSITORY.LEI` | `OcTradeRepository_RepositoryLei` | TField | No | Denotes the legal entity identifier of the trade repository. Validation Rules: Upto 40 alphanumeric characters. Optional |
| 3 | `OC.TR.REP.CUSTOMER.ID` | `OcTradeRepository_CustomerId` | TField | No | Indicates whether the repository is a customer of the bank. Holds the T24 customer number. Validation Rules: Optional Field. If LEI is entered, the val should be validated against OC.CUSTOMER field value. |
| 4 | `OC.TR.REP.COUNTRY` | `OcTradeRepository_Country` | TField |  | Denotes the country of the the regulator . Validation Rules: Should be a valid country code. |
| 5 | `OC.TR.REP.GEOGRAPHICAL.BLOCK` | `OcTradeRepository_GeographicalBlock` | TField |  | Denotes the geographical block of the regulator . Validation Rules: Should be a valid record in geographical block . Defaulted with the geographical block value defined in COUNTRY. |
| 6 | `OC.TR.REP.INTERFACE` | `OcTradeRepository_Interface` | TField | No | Denotes the interface type. Optional. Reserved for future use. Validation Rules: Valid Values are Auto and Manual. |
| 7 | `OC.TR.REP.TR.ACC.REF` | `OcTradeRepository_TrAccRef` | TField | No | Reference of the T24 bank�s account maintained with the Trade repository. Validation Rules: Optional Upto 20 alphanumeric characters. |
| 8 | `OC.TR.REP.RESERVED10` | `OcTradeRepository_Reserved10` | TField |  |  |
| 9 | `OC.TR.REP.RESERVED9` | `OcTradeRepository_Reserved9` | TField |  |  |
| 10 | `OC.TR.REP.RESERVED8` | `OcTradeRepository_Reserved8` | TField |  |  |
| 11 | `OC.TR.REP.RESERVED7` | `OcTradeRepository_Reserved7` | TField |  |  |
| 12 | `OC.TR.REP.RESERVED6` | `OcTradeRepository_Reserved6` | TField |  |  |
| 13 | `OC.TR.REP.RESERVED5` | `OcTradeRepository_Reserved5` | TField |  |  |
| 14 | `OC.TR.REP.RESERVED4` | `OcTradeRepository_Reserved4` | TField |  |  |
| 15 | `OC.TR.REP.RESERVED3` | `OcTradeRepository_Reserved3` | TField |  |  |
| 16 | `OC.TR.REP.RESERVED2` | `OcTradeRepository_Reserved2` | TField |  |  |
| 17 | `OC.TR.REP.RESERVED1` | `OcTradeRepository_Reserved1` | TField |  |  |
| 18 | `OC.TR.REP.LOCAL.REF` | `OcTradeRepository_LocalRef` |  |  |  |
| 19 | `OC.TR.REP.RECORD.STATUS` | `OcTradeRepository_RecordStatus` | String |  |  |
| 20 | `OC.TR.REP.CURR.NO` | `OcTradeRepository_CurrNo` | String |  |  |
| 21 | `OC.TR.REP.INPUTTER` | `OcTradeRepository_Inputter` |  |  |  |
| 22 | `OC.TR.REP.DATE.TIME` | `OcTradeRepository_DateTime` |  |  |  |
| 23 | `OC.TR.REP.AUTHORISER` | `OcTradeRepository_Authoriser` | String |  |  |
| 24 | `OC.TR.REP.CO.CODE` | `OcTradeRepository_CoCode` | String |  |  |
| 25 | `OC.TR.REP.DEPT.CODE` | `OcTradeRepository_DeptCode` | String |  |  |
| 26 | `OC.TR.REP.AUDITOR.CODE` | `OcTradeRepository_AuditorCode` | String |  |  |
| 27 | `OC.TR.REP.AUDIT.DATE.TIME` | `OcTradeRepository_AuditDateTime` | String |  |  |
