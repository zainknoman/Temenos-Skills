# ILCOPM.COLLATERAL.POSITIONS — Table Schema

> Source: `INSERTS/I_F.ILCOPM.COLLATERAL.POSITIONS` in `ILCOPM_CollateralPosition.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COLL.POS.PORTFOLIO` | `IlcopmCollateralPositions_Portfolio` | TField |  | Portfolio number. |
| 2 | `COLL.POS.SECURITY.NO` | `IlcopmCollateralPositions_SecurityNo` | TField |  | Security Number. |
| 3 | `COLL.POS.SECURITY.CURRENCY` | `IlcopmCollateralPositions_SecurityCurrency` | TField |  | Security currency. |
| 4 | `COLL.POS.COLLATERAL.AMOUNT` | `IlcopmCollateralPositions_CollateralAmount` |  |  |  |
| 5 | `COLL.POS.COLLATERAL.NOMINALS` | `IlcopmCollateralPositions_CollateralNominals` |  |  |  |
| 6 | `COLL.POS.TARGET.DEPOSITORY` | `IlcopmCollateralPositions_TargetDepository` |  |  |  |
| 7 | `COLL.POS.UNMARKED.NOMINALS` | `IlcopmCollateralPositions_UnmarkedNominals` |  |  |  |
| 8 | `COLL.POS.UNMARKED.AMOUNT` | `IlcopmCollateralPositions_UnmarkedAmount` |  |  |  |
| 9 | `COLL.POS.LOCAL.REF` | `IlcopmCollateralPositions_LocalRef` |  |  |  |
| 10 | `COLL.POS.OVERRIDE` | `IlcopmCollateralPositions_Override` |  |  |  |
| 11 | `COLL.POS.RECORD.STATUS` | `IlcopmCollateralPositions_RecordStatus` | String |  |  |
| 12 | `COLL.POS.CURR.NO` | `IlcopmCollateralPositions_CurrNo` | String |  |  |
| 13 | `COLL.POS.INPUTTER` | `IlcopmCollateralPositions_Inputter` |  |  |  |
| 14 | `COLL.POS.DATE.TIME` | `IlcopmCollateralPositions_DateTime` |  |  |  |
| 15 | `COLL.POS.AUTHORISER` | `IlcopmCollateralPositions_Authoriser` | String |  |  |
| 16 | `COLL.POS.CO.CODE` | `IlcopmCollateralPositions_CoCode` | String |  |  |
| 17 | `COLL.POS.DEPT.CODE` | `IlcopmCollateralPositions_DeptCode` | String |  |  |
| 18 | `COLL.POS.AUDITOR.CODE` | `IlcopmCollateralPositions_AuditorCode` | String |  |  |
| 19 | `COLL.POS.AUDIT.DATE.TIME` | `IlcopmCollateralPositions_AuditDateTime` | String |  |  |
| 20 | `COLL.POS.SOURCE.POSITION` | `IlcopmCollateralPositions_SourcePosition` |  |  |  |
| 21 | `COLL.POS.TARGET.SUB.ACCOUNT` | `IlcopmCollateralPositions_TargetSubAccount` |  |  |  |
| 22 | `COLL.POS.SECURITY.POSITION.ID` | `IlcopmCollateralPositions_SecurityPositionId` | TField |  | values of SECURITY.POSITION for the collateral id |
| 23 | `COLL.POS.TRF.NOT.APPLICABLE` | `IlcopmCollateralPositions_TrfNotApplicable` | TField |  | Field to determine whether the position transfer should happen or not. |
