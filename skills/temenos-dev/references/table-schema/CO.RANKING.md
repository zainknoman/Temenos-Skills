# CO.RANKING — Table Schema

> Source: `INSERTS/I_F.CO.RANKING` in `CO_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CO.RA.DESCRIPTION` | `CoRanking_Description` |  |  |  |
| 2 | `CO.RA.COLLATERAL.CODE` | `CoRanking_CollateralCode` |  |  |  |
| 3 | `CO.RA.EMERGING.MARKET` | `CoRanking_EmergingMarket` | TField |  | Used to determine if Emerging Market Securities should be used after Developed Market Securities. Validation Rules: 1. Valid values are YES_NO. |
| 4 | `CO.RA.POSITION.ORDER` | `CoRanking_PositionOrder` | TField |  | Order of securities where the ranking is equal. This can contain with VALUE or SECURITY. If this field is equal to VALUE then the securities will be assigned in Market �Value order if all other rules are equal. If this field is equal to SECURITY then the securities will be assigned in SECURITY.MASTER ID order if all other rules are equal. Validation Rules: 1. Valid values are VALUE_SECURITY.NO. |
| 5 | `CO.RA.RESERVED.16` | `CoRanking_Reserved16` | TField |  |  |
| 6 | `CO.RA.RESERVED.15` | `CoRanking_Reserved15` | TField |  |  |
| 7 | `CO.RA.RESERVED.14` | `CoRanking_Reserved14` | TField |  |  |
| 8 | `CO.RA.RESERVED.13` | `CoRanking_Reserved13` | TField |  |  |
| 9 | `CO.RA.RESERVED.12` | `CoRanking_Reserved12` | TField |  |  |
| 10 | `CO.RA.RESERVED.11` | `CoRanking_Reserved11` | TField |  |  |
| 11 | `CO.RA.RESERVED.10` | `CoRanking_Reserved10` | TField |  |  |
| 12 | `CO.RA.RESERVED.9` | `CoRanking_Reserved9` | TField |  |  |
| 13 | `CO.RA.RESERVED.8` | `CoRanking_Reserved8` | TField |  |  |
| 14 | `CO.RA.RESERVED.7` | `CoRanking_Reserved7` | TField |  |  |
| 15 | `CO.RA.RESERVED.6` | `CoRanking_Reserved6` | TField |  |  |
| 16 | `CO.RA.RESERVED.5` | `CoRanking_Reserved5` | TField |  |  |
| 17 | `CO.RA.RESERVED.4` | `CoRanking_Reserved4` | TField |  |  |
| 18 | `CO.RA.RESERVED.3` | `CoRanking_Reserved3` | TField |  |  |
| 19 | `CO.RA.RESERVED.2` | `CoRanking_Reserved2` | TField |  |  |
| 20 | `CO.RA.RESERVED.1` | `CoRanking_Reserved1` | TField |  |  |
| 21 | `CO.RA.LOCAL.REF` | `CoRanking_LocalRef` |  |  |  |
| 22 | `CO.RA.OVERRIDE` | `CoRanking_Override` |  |  |  |
| 23 | `CO.RA.RECORD.STATUS` | `CoRanking_RecordStatus` | String |  |  |
| 24 | `CO.RA.CURR.NO` | `CoRanking_CurrNo` | String |  |  |
| 25 | `CO.RA.INPUTTER` | `CoRanking_Inputter` |  |  |  |
| 26 | `CO.RA.DATE.TIME` | `CoRanking_DateTime` |  |  |  |
| 27 | `CO.RA.AUTHORISER` | `CoRanking_Authoriser` | String |  |  |
| 28 | `CO.RA.CO.CODE` | `CoRanking_CoCode` | String |  |  |
| 29 | `CO.RA.DEPT.CODE` | `CoRanking_DeptCode` | String |  |  |
| 30 | `CO.RA.AUDITOR.CODE` | `CoRanking_AuditorCode` | String |  |  |
| 31 | `CO.RA.AUDIT.DATE.TIME` | `CoRanking_AuditDateTime` | String |  |  |
