# FATCA.FCSI.AMENDMENTS — Table Schema

> Source: `INSERTS/I_F.FATCA.FCSI.AMENDMENTS` in `FA_CustomerIdentification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FA.FA.EFFECTIVE.DATE` | `FatcaFcsiAmendments_EffectiveDate` |  |  |  |
| 2 | `FA.FA.FATCA.STATUS` | `FatcaFcsiAmendments_FatcaStatus` |  |  |  |
| 3 | `FA.FA.FCSI.CURR.NO` | `FatcaFcsiAmendments_FcsiCurrNo` |  |  |  |
| 4 | `FA.FA.COI.CURR.NO` | `FatcaFcsiAmendments_CoiCurrNo` |  |  |  |
| 5 | `FA.FA.DATE` | `FatcaFcsiAmendments_Date` |  |  |  |
| 6 | `FA.FA.EX.JOINT.CUST.ID` | `FatcaFcsiAmendments_ExJointCustId` |  |  |  |
| 7 | `FA.FA.RELATION.CODE` | `FatcaFcsiAmendments_RelationCode` |  |  |  |
| 8 | `FA.FA.EX.JOINT.CURR.NO` | `FatcaFcsiAmendments_ExJointCurrNo` |  |  |  |
