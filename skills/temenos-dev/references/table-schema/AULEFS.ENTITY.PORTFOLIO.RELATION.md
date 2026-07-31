# AULEFS.ENTITY.PORTFOLIO.RELATION — Table Schema

> Source: `INSERTS/I_F.AULEFS.ENTITY.PORTFOLIO.RELATION` in `AULEFS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ENTITY.RELATION.RESERVED.1` | `AulefsEntityPortfolioRelation_Reserved1` | TField |  |  |
| 2 | `ENTITY.RELATION.RESERVED.11` | `AulefsEntityPortfolioRelation_Reserved11` | TField |  |  |
| 3 | `ENTITY.RELATION.ASSOCIATED.PORTFOLIO` | `AulefsEntityPortfolioRelation_AssociatedPortfolio` |  |  |  |
| 4 | `ENTITY.RELATION.LOCAL.REF` | `AulefsEntityPortfolioRelation_LocalRef` |  |  |  |
| 5 | `ENTITY.RELATION.LEGAL.ENTITY` | `AulefsEntityPortfolioRelation_LegalEntity` | TField |  | Legal Entity of the Portfolio LE.PF.ID from SEC.ACC.MASTER is being stored in this field. |
| 6 | `ENTITY.RELATION.RESERVED.2` | `AulefsEntityPortfolioRelation_Reserved2` | TField |  |  |
| 7 | `ENTITY.RELATION.RESERVED.3` | `AulefsEntityPortfolioRelation_Reserved3` | TField |  |  |
| 8 | `ENTITY.RELATION.RESERVED.4` | `AulefsEntityPortfolioRelation_Reserved4` | TField |  |  |
| 9 | `ENTITY.RELATION.RESERVED.5` | `AulefsEntityPortfolioRelation_Reserved5` | TField |  |  |
| 10 | `ENTITY.RELATION.RESERVED.6` | `AulefsEntityPortfolioRelation_Reserved6` | TField |  |  |
| 11 | `ENTITY.RELATION.RESERVED.7` | `AulefsEntityPortfolioRelation_Reserved7` | TField |  |  |
| 12 | `ENTITY.RELATION.RESERVED.8` | `AulefsEntityPortfolioRelation_Reserved8` | TField |  |  |
| 13 | `ENTITY.RELATION.RESERVED.9` | `AulefsEntityPortfolioRelation_Reserved9` | TField |  |  |
| 14 | `ENTITY.RELATION.RESERVED.10` | `AulefsEntityPortfolioRelation_Reserved10` | TField |  |  |
