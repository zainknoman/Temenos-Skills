# ARACCT.REDEEM.ARRANGEMENTS — Table Schema

> Source: `INSERTS/I_F.ARACCT.REDEEM.ARRANGEMENTS` in `ARACCT_EarlyRedeemDepositUVA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REDEEM.ARR.ARRANGEMENT.ID` | `AracctRedeemArrangements_ArrangementId` |  |  |  |
| 2 | `REDEEM.ARR.RESERVED.10` | `AracctRedeemArrangements_Reserved10` | TField |  |  |
| 3 | `REDEEM.ARR.RESERVED.9` | `AracctRedeemArrangements_Reserved9` | TField |  |  |
| 4 | `REDEEM.ARR.RESERVED.8` | `AracctRedeemArrangements_Reserved8` | TField |  |  |
| 5 | `REDEEM.ARR.RESERVED.7` | `AracctRedeemArrangements_Reserved7` | TField |  |  |
| 6 | `REDEEM.ARR.RESERVED.6` | `AracctRedeemArrangements_Reserved6` | TField |  |  |
| 7 | `REDEEM.ARR.RESERVED.5` | `AracctRedeemArrangements_Reserved5` | TField |  |  |
| 8 | `REDEEM.ARR.RESERVED.4` | `AracctRedeemArrangements_Reserved4` | TField |  |  |
| 9 | `REDEEM.ARR.RESERVED.3` | `AracctRedeemArrangements_Reserved3` | TField |  |  |
| 10 | `REDEEM.ARR.RESERVED.2` | `AracctRedeemArrangements_Reserved2` | TField |  |  |
| 11 | `REDEEM.ARR.RESERVED.1` | `AracctRedeemArrangements_Reserved1` | TField |  |  |
| 12 | `REDEEM.ARR.LOCAL.REF` | `AracctRedeemArrangements_LocalRef` |  |  |  |
