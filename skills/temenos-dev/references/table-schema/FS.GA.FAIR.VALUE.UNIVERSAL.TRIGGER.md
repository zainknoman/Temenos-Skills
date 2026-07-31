# FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER — Table Schema

> Source: `INSERTS/I_F.FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.NAV.GROUP.CODE` | `FsGaFairValueUniversalTrigger_NavGroupCode` | TField |  | The NAV group code is the list of funds grouped together for NAV processing, reporting etc Multifonds DB Column is NAV_GROUP. |
| 2 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.FUND.ID` | `FsGaFairValueUniversalTrigger_FundId` |  |  |  |
| 3 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.INTERNAL.SECURITY.ID` | `FsGaFairValueUniversalTrigger_InternalSecurityId` |  |  |  |
| 4 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.TOLERANCE` | `FsGaFairValueUniversalTrigger_Tolerance` | TField |  | The tolerance will be the minimum change necessary to bring into effect. E.g, Tolerance for Fair value price or NAV / Fixed tolerance group or APS account rebalancing Multifonds DB Column is TOLERANCE. |
| 5 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.COEFFICIENT` | `FsGaFairValueUniversalTrigger_Coefficient` | TField |  | minimum confidence coefficient for a fair value price to be accepted and coefficient for equalisation Multifonds DB Column is COEFFICIENT. |
| 6 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.TYPE.OF.PRICE` | `FsGaFairValueUniversalTrigger_TypeOfPrice` |  |  |  |
| 7 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.PRICE.SOURCE` | `FsGaFairValueUniversalTrigger_PriceSource` |  |  |  |
| 8 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.OTHER.PROVIDER` | `FsGaFairValueUniversalTrigger_OtherProvider` | TField |  | Enter the sec price prov. Acc to the price sltn algorithm defined in the pricing rule, MF will attmpt to find a price from the pref prov before proceeding with the search for a price from the sec Prov Multifonds DB Column is CORC_2. |
| 9 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.FACTOR.PRICE` | `FsGaFairValueUniversalTrigger_FactorPrice` | TField |  | Factor price Multifonds DB Column is FAC_COURS. |
| 10 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.RESERVED10` | `FsGaFairValueUniversalTrigger_Reserved10` | TField |  |  |
| 11 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.RESERVED9` | `FsGaFairValueUniversalTrigger_Reserved9` | TField |  |  |
| 12 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.RESERVED8` | `FsGaFairValueUniversalTrigger_Reserved8` | TField |  |  |
| 13 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.RESERVED7` | `FsGaFairValueUniversalTrigger_Reserved7` | TField |  |  |
| 14 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.RESERVED6` | `FsGaFairValueUniversalTrigger_Reserved6` | TField |  |  |
| 15 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.RESERVED5` | `FsGaFairValueUniversalTrigger_Reserved5` | TField |  |  |
| 16 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.RESERVED4` | `FsGaFairValueUniversalTrigger_Reserved4` | TField |  |  |
| 17 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.RESERVED3` | `FsGaFairValueUniversalTrigger_Reserved3` | TField |  |  |
| 18 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.RESERVED2` | `FsGaFairValueUniversalTrigger_Reserved2` | TField |  |  |
| 19 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.RESERVED1` | `FsGaFairValueUniversalTrigger_Reserved1` | TField |  |  |
| 20 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.RECORD.STATUS` | `FsGaFairValueUniversalTrigger_RecordStatus` | String |  |  |
| 21 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.CURR.NO` | `FsGaFairValueUniversalTrigger_CurrNo` | String |  |  |
| 22 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.INPUTTER` | `FsGaFairValueUniversalTrigger_Inputter` |  |  |  |
| 23 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.DATE.TIME` | `FsGaFairValueUniversalTrigger_DateTime` |  |  |  |
| 24 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.AUTHORISER` | `FsGaFairValueUniversalTrigger_Authoriser` | String |  |  |
| 25 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.CO.CODE` | `FsGaFairValueUniversalTrigger_CoCode` | String |  |  |
| 26 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.DEPT.CODE` | `FsGaFairValueUniversalTrigger_DeptCode` | String |  |  |
| 27 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.AUDITOR.CODE` | `FsGaFairValueUniversalTrigger_AuditorCode` | String |  |  |
| 28 | `FS.GA.FAIR.VALUE.UNIVERSAL.TRIGGER.AUDIT.DATE.TIME` | `FsGaFairValueUniversalTrigger_AuditDateTime` | String |  |  |
