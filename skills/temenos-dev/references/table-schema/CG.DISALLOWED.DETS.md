# CG.DISALLOWED.DETS — Table Schema

> Source: `INSERTS/I_F.CG.DISALLOWED.DETS` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.DADET.PUR.TXN.ID` | `CgDisallowedDets_PurTxnId` |  |  |  |
| 2 | `CG.DADET.PUR.TAX.LOT.ID` | `CgDisallowedDets_PurTaxLotId` |  |  |  |
| 3 | `CG.DADET.DISALLOWED.NOM` | `CgDisallowedDets_DisallowedNom` |  |  |  |
| 4 | `CG.DADET.DISALLOWED.LOSS` | `CgDisallowedDets_DisallowedLoss` |  |  |  |
| 5 | `CG.DADET.REPLACEMENT.BASE` | `CgDisallowedDets_ReplacementBase` |  |  |  |
| 6 | `CG.DADET.REPLACEMENT.TXN` | `CgDisallowedDets_ReplacementTxn` |  |  |  |
