# CNDEPO.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CNDEPO.PARAMETER` in `CNDEPO_RetailDeposit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CNDEPO.PARAMETER.PRODUCT.NAME` | `CndepoParameter_ProductName` |  |  |  |
| 2 | `CNDEPO.PARAMETER.MIN.BALANCE.FCCY` | `CndepoParameter_MinBalanceFccy` |  |  |  |
| 3 | `CNDEPO.PARAMETER.MIN.BALANCE.LCCY` | `CndepoParameter_MinBalanceLccy` |  |  |  |
| 4 | `CNDEPO.PARAMETER.INTEREST.TYPE` | `CndepoParameter_InterestType` |  |  |  |
| 5 | `CNDEPO.PARAMETER.INTEREST.INDEX` | `CndepoParameter_InterestIndex` |  |  |  |
| 6 | `CNDEPO.PARAMETER.CURRENCY.MARKET` | `CndepoParameter_CurrencyMarket` | TField |  | To configure currency market for conversion. |
| 7 | `CNDEPO.PARAMETER.LOCAL.REF` | `CndepoParameter_LocalRef` |  |  |  |
| 8 | `CNDEPO.PARAMETER.ACCOUNT.PAY.FREQ` | `CndepoParameter_AccountPayFreq` | TField |  | Specifies the interest capitalization frequency for account products. |
| 9 | `CNDEPO.PARAMETER.CONTRACT.OWNER.ROLES` | `CndepoParameter_ContractOwnerRoles` |  |  |  |
| 10 | `CNDEPO.PARAMETER.RESERVED.5` | `CndepoParameter_Reserved5` | TField |  | Reserved for future use. |
| 11 | `CNDEPO.PARAMETER.RESERVED.6` | `CndepoParameter_Reserved6` | TField |  | Reserved for future use. |
| 12 | `CNDEPO.PARAMETER.RESERVED.7` | `CndepoParameter_Reserved7` | TField |  | Reserved for future use. |
| 13 | `CNDEPO.PARAMETER.RESERVED.8` | `CndepoParameter_Reserved8` | TField |  | Reserved for future use. |
| 14 | `CNDEPO.PARAMETER.RESERVED.9` | `CndepoParameter_Reserved9` | TField |  | Reserved for future use. |
| 15 | `CNDEPO.PARAMETER.RESERVED.10` | `CndepoParameter_Reserved10` | TField |  | Reserved for future use. |
| 16 | `CNDEPO.PARAMETER.RESERVED.11` | `CndepoParameter_Reserved11` | TField |  |  |
| 17 | `CNDEPO.PARAMETER.RESERVED.12` | `CndepoParameter_Reserved12` | TField |  |  |
| 18 | `CNDEPO.PARAMETER.RESERVED.13` | `CndepoParameter_Reserved13` | TField |  | Reserved for future use. |
| 19 | `CNDEPO.PARAMETER.RESERVED.14` | `CndepoParameter_Reserved14` | TField |  | Reserved for future use. |
| 20 | `CNDEPO.PARAMETER.OVERRIDE` | `CndepoParameter_Override` |  |  |  |
| 21 | `CNDEPO.PARAMETER.RECORD.STATUS` | `CndepoParameter_RecordStatus` | String |  |  |
| 22 | `CNDEPO.PARAMETER.CURR.NO` | `CndepoParameter_CurrNo` | String |  |  |
| 23 | `CNDEPO.PARAMETER.INPUTTER` | `CndepoParameter_Inputter` |  |  |  |
| 24 | `CNDEPO.PARAMETER.DATE.TIME` | `CndepoParameter_DateTime` |  |  |  |
| 25 | `CNDEPO.PARAMETER.AUTHORISER` | `CndepoParameter_Authoriser` | String |  |  |
| 26 | `CNDEPO.PARAMETER.CO.CODE` | `CndepoParameter_CoCode` | String |  |  |
| 27 | `CNDEPO.PARAMETER.DEPT.CODE` | `CndepoParameter_DeptCode` | String |  |  |
| 28 | `CNDEPO.PARAMETER.AUDITOR.CODE` | `CndepoParameter_AuditorCode` | String |  |  |
| 29 | `CNDEPO.PARAMETER.AUDIT.DATE.TIME` | `CndepoParameter_AuditDateTime` | String |  |  |
| 30 | `CNDEPO.PARAMETER.INTEREST.PROPERTY` | `CndepoParameter_InterestProperty` |  |  |  |
| 31 | `CNDEPO.PARAMETER.EXPIRY.CHANGE.TO.PRODUCT` | `CndepoParameter_ExpiryChangeToProduct` |  |  |  |
