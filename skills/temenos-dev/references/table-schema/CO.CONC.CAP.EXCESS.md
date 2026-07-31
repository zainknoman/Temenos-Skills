# CO.CONC.CAP.EXCESS — Table Schema

> Source: `INSERTS/I_F.CO.CONC.CAP.EXCESS` in `CO_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COCE.CONC.CAP.LEVEL` | `CoConcCapExcess_ConcCapLevel` |  |  |  |
| 2 | `COCE.CONC.CAP.DEFN` | `CoConcCapExcess_ConcCapDefn` |  |  |  |
| 3 | `COCE.COLLATERAL.ID` | `CoConcCapExcess_CollateralId` |  |  |  |
| 4 | `COCE.OLD.LEVEL` | `CoConcCapExcess_OldLevel` |  |  |  |
| 5 | `COCE.OLD.VALUE` | `CoConcCapExcess_OldValue` |  |  |  |
| 6 | `COCE.NEW.LEVEL` | `CoConcCapExcess_NewLevel` |  |  |  |
| 7 | `COCE.NEW.VALUE` | `CoConcCapExcess_NewValue` |  |  |  |
| 8 | `COCE.APPLIED.DATE` | `CoConcCapExcess_AppliedDate` |  |  |  |
| 9 | `COCE.APPLIED.TIME` | `CoConcCapExcess_AppliedTime` |  |  |  |
| 10 | `COCE.RESERVED.12` | `CoConcCapExcess_Reserved12` |  |  |  |
| 11 | `COCE.RESERVED.11` | `CoConcCapExcess_Reserved11` |  |  |  |
| 12 | `COCE.RESERVED.10` | `CoConcCapExcess_Reserved10` |  |  |  |
| 13 | `COCE.RESERVED.9` | `CoConcCapExcess_Reserved9` |  |  |  |
| 14 | `COCE.RESERVED.8` | `CoConcCapExcess_Reserved8` | TField |  |  |
| 15 | `COCE.RESERVED.7` | `CoConcCapExcess_Reserved7` | TField |  |  |
| 16 | `COCE.RESERVED.6` | `CoConcCapExcess_Reserved6` | TField |  |  |
| 17 | `COCE.RESERVED.5` | `CoConcCapExcess_Reserved5` | TField |  |  |
| 18 | `COCE.RESERVED.4` | `CoConcCapExcess_Reserved4` | TField |  |  |
| 19 | `COCE.RESERVED.3` | `CoConcCapExcess_Reserved3` | TField |  |  |
| 20 | `COCE.RESERVED.2` | `CoConcCapExcess_Reserved2` | TField |  |  |
| 21 | `COCE.RESERVED.1` | `CoConcCapExcess_Reserved1` | TField |  |  |
