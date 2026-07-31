# CAREGS.CDIC.FORGN.BRANCH.HOLD.INST — Table Schema

> Source: `INSERTS/I_F.CAREGS.CDIC.FORGN.BRANCH.HOLD.INST` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.FORG.INST.MI.CLEARING.ACCT` | `CaregsCdicForgnBranchHoldInst_MiClearingAcct` |  |  |  |
| 2 | `CDIC.FORG.INST.DESCRIPTION` | `CaregsCdicForgnBranchHoldInst_Description` |  |  |  |
| 3 | `CDIC.FORG.INST.PERCENTAGE.HOLD` | `CaregsCdicForgnBranchHoldInst_PercentageHold` |  |  |  |
| 4 | `CDIC.FORG.INST.LOCAL.REF` | `CaregsCdicForgnBranchHoldInst_LocalRef` |  |  |  |
| 5 | `CDIC.FORG.INST.RECORD.STATUS` | `CaregsCdicForgnBranchHoldInst_RecordStatus` | String |  |  |
| 6 | `CDIC.FORG.INST.CURR.NO` | `CaregsCdicForgnBranchHoldInst_CurrNo` | String |  |  |
| 7 | `CDIC.FORG.INST.INPUTTER` | `CaregsCdicForgnBranchHoldInst_Inputter` |  |  |  |
| 8 | `CDIC.FORG.INST.DATE.TIME` | `CaregsCdicForgnBranchHoldInst_DateTime` |  |  |  |
| 9 | `CDIC.FORG.INST.AUTHORISER` | `CaregsCdicForgnBranchHoldInst_Authoriser` | String |  |  |
| 10 | `CDIC.FORG.INST.CO.CODE` | `CaregsCdicForgnBranchHoldInst_CoCode` | String |  |  |
| 11 | `CDIC.FORG.INST.DEPT.CODE` | `CaregsCdicForgnBranchHoldInst_DeptCode` | String |  |  |
| 12 | `CDIC.FORG.INST.AUDITOR.CODE` | `CaregsCdicForgnBranchHoldInst_AuditorCode` | String |  |  |
| 13 | `CDIC.FORG.INST.AUDIT.DATE.TIME` | `CaregsCdicForgnBranchHoldInst_AuditDateTime` | String |  |  |
