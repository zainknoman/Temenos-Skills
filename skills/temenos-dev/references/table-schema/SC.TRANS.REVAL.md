# SC.TRANS.REVAL — Table Schema

> Source: `INSERTS/I_F.SC.TRANS.REVAL` in `SC_SctDealerBook.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.RVL.TRANS.REF` | `ScTransReval_TransRef` | TField |  |  |
| 2 | `SC.RVL.TRANS.TYPE` | `ScTransReval_TransType` | TField |  |  |
| 3 | `SC.RVL.VALUE.DATE` | `ScTransReval_ValueDate` | TField |  |  |
| 4 | `SC.RVL.TRD.NOMINAL` | `ScTransReval_TrdNominal` | TField |  |  |
| 5 | `SC.RVL.COST.OF.POSN` | `ScTransReval_CostOfPosn` | TField |  |  |
| 6 | `SC.RVL.AVAILABLE.NOM` | `ScTransReval_AvailableNom` | TField |  |  |
| 7 | `SC.RVL.REVALUATION.PRICE` | `ScTransReval_RevaluationPrice` | TField |  |  |
| 8 | `SC.RVL.REVALUATION.DATE` | `ScTransReval_RevaluationDate` | TField |  |  |
| 9 | `SC.RVL.REVAL.UNREAL.PL` | `ScTransReval_RevalUnrealPl` | TField |  |  |
| 10 | `SC.RVL.REVAL.UNREAL.P.LCY` | `ScTransReval_RevalUnrealPLcy` | TField |  |  |
| 11 | `SC.RVL.UNREAL.PL.CATEG` | `ScTransReval_UnrealPlCateg` | TField |  |  |
| 12 | `SC.RVL.SUSP.CATEG` | `ScTransReval_SuspCateg` | TField |  |  |
| 13 | `SC.RVL.STATEMENT.NO` | `ScTransReval_StatementNo` |  |  |  |
| 14 | `SC.RVL.ALLC.TRANS.REF` | `ScTransReval_AllcTransRef` |  |  |  |
| 15 | `SC.RVL.ALLC.TRANS.NOM` | `ScTransReval_AllcTransNom` |  |  |  |
