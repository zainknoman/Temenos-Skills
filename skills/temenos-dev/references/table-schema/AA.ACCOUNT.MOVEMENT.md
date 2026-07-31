# AA.ACCOUNT.MOVEMENT — Table Schema

> Source: `INSERTS/I_F.AA.ACCOUNT.MOVEMENT` in `AA_Accounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.MVMT.BALANCE.TYPE` | `AaAccountMovement_BalanceType` |  |  |  |
| 2 | `AA.MVMT.NAU.VALUE.DATE` | `AaAccountMovement_NauValueDate` |  |  |  |
| 3 | `AA.MVMT.NAU.MOVEMENT` | `AaAccountMovement_NauMovement` |  |  |  |
| 4 | `AA.MVMT.NAU.CR.MOVEMENT` | `AaAccountMovement_NauCrMovement` |  |  |  |
| 5 | `AA.MVMT.NAU.DR.MOVEMENT` | `AaAccountMovement_NauDrMovement` |  |  |  |
| 6 | `AA.MVMT.FWD.VALUE.DATE` | `AaAccountMovement_FwdValueDate` |  |  |  |
| 7 | `AA.MVMT.FWD.MOVEMENT` | `AaAccountMovement_FwdMovement` |  |  |  |
| 8 | `AA.MVMT.FWD.CR.MOVEMENT` | `AaAccountMovement_FwdCrMovement` |  |  |  |
| 9 | `AA.MVMT.FWD.DR.MOVEMENT` | `AaAccountMovement_FwdDrMovement` |  |  |  |
| 10 | `AA.MVMT.ARR.ACTIVITY.ID` | `AaAccountMovement_ArrActivityId` |  |  |  |
| 11 | `AA.MVMT.ACT.BAL.TYPE` | `AaAccountMovement_ActBalType` |  |  |  |
| 12 | `AA.MVMT.ACT.NAU.MVMT` | `AaAccountMovement_ActNauMvmt` |  |  |  |
| 13 | `AA.MVMT.ACT.NAU.CR.MVMT` | `AaAccountMovement_ActNauCrMvmt` |  |  |  |
| 14 | `AA.MVMT.ACT.NAU.DR.MVMT` | `AaAccountMovement_ActNauDrMvmt` |  |  |  |
| 15 | `AA.MVMT.ACT.FWD.MVMT` | `AaAccountMovement_ActFwdMvmt` |  |  |  |
| 16 | `AA.MVMT.ACT.FWD.CR.MVMT` | `AaAccountMovement_ActFwdCrMvmt` |  |  |  |
| 17 | `AA.MVMT.ACT.FWD.DR.MVMT` | `AaAccountMovement_ActFwdDrMvmt` |  |  |  |
