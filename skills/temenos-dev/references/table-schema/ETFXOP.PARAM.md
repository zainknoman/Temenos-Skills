# ETFXOP.PARAM — Table Schema

> Source: `INSERTS/I_F.ETFXOP.PARAM` in `ETFXOP_RetentionAccounts.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ETFXOP.RA.PERCENTAGE.A` | `EtfxopParam_PercentageA` | TField |  | This will determine the percentage to be transferred to retention account A when an amount is deposited in the master account. |
| 2 | `ETFXOP.RA.RETENTION.DAYS.A` | `EtfxopParam_RetentionDaysA` | TField |  | This will determine the number of days funds will be retained in the retention account before being transferred to the liquidation account. Will be left blank in case the amount in Retention account A is to be retained for indefinite period. |
| 3 | `ETFXOP.RA.PERCENTAGE.B` | `EtfxopParam_PercentageB` | TField |  | This will determine the percentage to be transferred to retention account B when an amount is deposited in the master account. |
| 4 | `ETFXOP.RA.RETENTION.DAYS.B` | `EtfxopParam_RetentionDaysB` | TField |  | This will determine the number of days funds will be retained in the retention account before being transferred to the liquidation account. |
| 5 | `ETFXOP.RA.RETENTION.PRODUCT` | `EtfxopParam_RetentionProduct` | TField |  | This field will have the list of all the products from Account Product Line. The Retention accounts will be opened from the product parameterized. |
| 6 | `ETFXOP.RA.RESERVED.1` | `EtfxopParam_Reserved1` | TField |  |  |
| 7 | `ETFXOP.RA.RESERVED.2` | `EtfxopParam_Reserved2` | TField |  |  |
| 8 | `ETFXOP.RA.RESERVED.3` | `EtfxopParam_Reserved3` | TField |  |  |
| 9 | `ETFXOP.RA.RESERVED.4` | `EtfxopParam_Reserved4` | TField |  |  |
| 10 | `ETFXOP.RA.RESERVED.5` | `EtfxopParam_Reserved5` | TField |  |  |
| 11 | `ETFXOP.RA.RESERVED.6` | `EtfxopParam_Reserved6` | TField |  |  |
| 12 | `ETFXOP.RA.RESERVED.7` | `EtfxopParam_Reserved7` | TField |  |  |
| 13 | `ETFXOP.RA.RESERVED.8` | `EtfxopParam_Reserved8` | TField |  |  |
| 14 | `ETFXOP.RA.RESERVED.9` | `EtfxopParam_Reserved9` | TField |  |  |
| 15 | `ETFXOP.RA.RESERVED.10` | `EtfxopParam_Reserved10` | TField |  |  |
| 16 | `ETFXOP.RA.LOCAL.REF` | `EtfxopParam_LocalRef` |  |  |  |
| 17 | `ETFXOP.RA.OVERRIDE` | `EtfxopParam_Override` |  |  |  |
| 18 | `ETFXOP.RA.RECORD.STATUS` | `EtfxopParam_RecordStatus` | String |  |  |
| 19 | `ETFXOP.RA.CURR.NO` | `EtfxopParam_CurrNo` | String |  |  |
| 20 | `ETFXOP.RA.INPUTTER` | `EtfxopParam_Inputter` |  |  |  |
| 21 | `ETFXOP.RA.DATE.TIME` | `EtfxopParam_DateTime` |  |  |  |
| 22 | `ETFXOP.RA.AUTHORISER` | `EtfxopParam_Authoriser` | String |  |  |
| 23 | `ETFXOP.RA.CO.CODE` | `EtfxopParam_CoCode` | String |  |  |
| 24 | `ETFXOP.RA.DEPT.CODE` | `EtfxopParam_DeptCode` | String |  |  |
| 25 | `ETFXOP.RA.AUDITOR.CODE` | `EtfxopParam_AuditorCode` | String |  |  |
| 26 | `ETFXOP.RA.AUDIT.DATE.TIME` | `EtfxopParam_AuditDateTime` | String |  |  |
