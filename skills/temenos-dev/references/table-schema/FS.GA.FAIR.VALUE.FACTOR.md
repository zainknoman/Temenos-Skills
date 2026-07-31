# FS.GA.FAIR.VALUE.FACTOR — Table Schema

> Source: `INSERTS/I_F.FS.GA.FAIR.VALUE.FACTOR` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FAIR.VALUE.FACTOR.INTERNAL.SECURITY.ID` | `FsGaFairValueFactor_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 2 | `FS.GA.FAIR.VALUE.FACTOR.PRICE.DATE` | `FsGaFairValueFactor_PriceDate` | TField |  | Date of the Price or Ex rate used in NAV Multifonds DB Column is DATE_COURS. |
| 3 | `FS.GA.FAIR.VALUE.FACTOR.PRICE.IN.LOCAL.CURRENCY` | `FsGaFairValueFactor_PriceInLocalCurrency` | TField |  | It reflects Price, Market Price,security price.effective unit price Multifonds DB Column is COURS. |
| 4 | `FS.GA.FAIR.VALUE.FACTOR.FACTOR` | `FsGaFairValueFactor_Factor` | TField |  | Factor for Mortgage backed instruments, also used in CMV securities and Fair value pricing. This also finds use as a mark up or down value in case of other features Multifonds DB Column is FACTOR. |
| 5 | `FS.GA.FAIR.VALUE.FACTOR.COEFFICIENT` | `FsGaFairValueFactor_Coefficient` | TField |  | minimum confidence coefficient for a fair value price to be accepted and coefficient for equalisation Multifonds DB Column is COEFFICIENT. |
| 6 | `FS.GA.FAIR.VALUE.FACTOR.PRICE.SOURCE` | `FsGaFairValueFactor_PriceSource` | TField |  | Provider code like Telekers, Reuters etc Multifonds DB Column is CORC. |
| 7 | `FS.GA.FAIR.VALUE.FACTOR.PROVIDER.ID` | `FsGaFairValueFactor_ProviderId` | TField |  | Relates to Identifier codes of security,Provider,Thirdparty and industry etc Multifonds DB Column is ID_CODE. |
| 8 | `FS.GA.FAIR.VALUE.FACTOR.SEC.TYPE` | `FsGaFairValueFactor_SecType` | TField |  | Allows user to define security type Multifonds DB Column is SEC_TYPE. |
| 9 | `FS.GA.FAIR.VALUE.FACTOR.RESERVED10` | `FsGaFairValueFactor_Reserved10` | TField |  |  |
| 10 | `FS.GA.FAIR.VALUE.FACTOR.RESERVED9` | `FsGaFairValueFactor_Reserved9` | TField |  |  |
| 11 | `FS.GA.FAIR.VALUE.FACTOR.RESERVED8` | `FsGaFairValueFactor_Reserved8` | TField |  |  |
| 12 | `FS.GA.FAIR.VALUE.FACTOR.RESERVED7` | `FsGaFairValueFactor_Reserved7` | TField |  |  |
| 13 | `FS.GA.FAIR.VALUE.FACTOR.RESERVED6` | `FsGaFairValueFactor_Reserved6` | TField |  |  |
| 14 | `FS.GA.FAIR.VALUE.FACTOR.RESERVED5` | `FsGaFairValueFactor_Reserved5` | TField |  |  |
| 15 | `FS.GA.FAIR.VALUE.FACTOR.RESERVED4` | `FsGaFairValueFactor_Reserved4` | TField |  |  |
| 16 | `FS.GA.FAIR.VALUE.FACTOR.RESERVED3` | `FsGaFairValueFactor_Reserved3` | TField |  |  |
| 17 | `FS.GA.FAIR.VALUE.FACTOR.RESERVED2` | `FsGaFairValueFactor_Reserved2` | TField |  |  |
| 18 | `FS.GA.FAIR.VALUE.FACTOR.RESERVED1` | `FsGaFairValueFactor_Reserved1` | TField |  |  |
| 19 | `FS.GA.FAIR.VALUE.FACTOR.RECORD.STATUS` | `FsGaFairValueFactor_RecordStatus` | String |  |  |
| 20 | `FS.GA.FAIR.VALUE.FACTOR.CURR.NO` | `FsGaFairValueFactor_CurrNo` | String |  |  |
| 21 | `FS.GA.FAIR.VALUE.FACTOR.INPUTTER` | `FsGaFairValueFactor_Inputter` |  |  |  |
| 22 | `FS.GA.FAIR.VALUE.FACTOR.DATE.TIME` | `FsGaFairValueFactor_DateTime` |  |  |  |
| 23 | `FS.GA.FAIR.VALUE.FACTOR.AUTHORISER` | `FsGaFairValueFactor_Authoriser` | String |  |  |
| 24 | `FS.GA.FAIR.VALUE.FACTOR.CO.CODE` | `FsGaFairValueFactor_CoCode` | String |  |  |
| 25 | `FS.GA.FAIR.VALUE.FACTOR.DEPT.CODE` | `FsGaFairValueFactor_DeptCode` | String |  |  |
| 26 | `FS.GA.FAIR.VALUE.FACTOR.AUDITOR.CODE` | `FsGaFairValueFactor_AuditorCode` | String |  |  |
| 27 | `FS.GA.FAIR.VALUE.FACTOR.AUDIT.DATE.TIME` | `FsGaFairValueFactor_AuditDateTime` | String |  |  |
