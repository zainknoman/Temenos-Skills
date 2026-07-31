# ESDORM.CLAIMED.DORMANT.ACCTS — Table Schema

> Source: `INSERTS/I_F.ESDORM.CLAIMED.DORMANT.ACCTS` in `ESBASE_ClosedDormantAccounts.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESDORM.CLAIM.AMOUNT` | `EsdormClaimedDormantAccts_ClaimedDormantAcctsClaimAmount` |  |  |  |
| 2 | `ESDORM.VALUE.DATE` | `EsdormClaimedDormantAccts_ClaimedDormantAcctsValueDate` |  |  |  |
| 3 | `ESDORM.PAYMENT.REFERENCE` | `EsdormClaimedDormantAccts_ClaimedDormantAcctsPaymentReference` |  |  |  |
| 4 | `ESDORM.RESERVED.1` | `EsdormClaimedDormantAccts__Reserved1` |  |  |  |
| 5 | `ESDORM.RESERVED.2` | `EsdormClaimedDormantAccts_Reserved2` | TField |  |  |
| 6 | `ESDORM.RESERVED.3` | `EsdormClaimedDormantAccts_Reserved3` | TField |  |  |
| 7 | `ESDORM.RESERVED.4` | `EsdormClaimedDormantAccts_Reserved4` | TField |  |  |
| 8 | `ESDORM.RESERVED.5` | `EsdormClaimedDormantAccts_Reserved5` | TField |  |  |
| 9 | `ESDORM.RESERVED.6` | `EsdormClaimedDormantAccts_Reserved6` | TField |  |  |
| 10 | `ESDORM.RESERVED.7` | `EsdormClaimedDormantAccts_Reserved7` | TField |  |  |
| 11 | `ESDORM.RESERVED.8` | `EsdormClaimedDormantAccts_Reserved8` | TField |  |  |
| 12 | `ESDORM.RESERVED.9` | `EsdormClaimedDormantAccts_Reserved9` | TField |  |  |
| 13 | `ESDORM.RESERVED.10` | `EsdormClaimedDormantAccts_Reserved10` | TField |  |  |
| 14 | `ESDORM.RESERVED.11` | `EsdormClaimedDormantAccts_Reserved11` | TField |  |  |
| 15 | `ESDORM.RESERVED.12` | `EsdormClaimedDormantAccts_Reserved12` | TField |  |  |
| 16 | `ESDORM.RESERVED.13` | `EsdormClaimedDormantAccts_Reserved13` | TField |  |  |
| 17 | `ESDORM.RESERVED.14` | `EsdormClaimedDormantAccts_Reserved14` | TField |  |  |
| 18 | `ESDORM.RESERVED.15` | `EsdormClaimedDormantAccts_Reserved15` | TField |  |  |
| 19 | `ESDORM.OVERRIDE` | `EsdormClaimedDormantAccts_Override` |  |  |  |
| 20 | `ESDORM.RECORD.STATUS` | `EsdormClaimedDormantAccts_RecordStatus` | String |  |  |
| 21 | `ESDORM.CURR.NO` | `EsdormClaimedDormantAccts_CurrNo` | String |  |  |
| 22 | `ESDORM.INPUTTER` | `EsdormClaimedDormantAccts_Inputter` |  |  |  |
| 23 | `ESDORM.DATE.TIME` | `EsdormClaimedDormantAccts_DateTime` |  |  |  |
| 24 | `ESDORM.AUTHORISER` | `EsdormClaimedDormantAccts_Authoriser` | String |  |  |
| 25 | `ESDORM.CO.CODE` | `EsdormClaimedDormantAccts_CoCode` | String |  |  |
| 26 | `ESDORM.DEPT.CODE` | `EsdormClaimedDormantAccts_DeptCode` | String |  |  |
| 27 | `ESDORM.AUDITOR.CODE` | `EsdormClaimedDormantAccts_AuditorCode` | String |  |  |
| 28 | `ESDORM.AUDIT.DATE.TIME` | `EsdormClaimedDormantAccts_AuditDateTime` | String |  |  |
