# FS.GA.COMPOSITE.OWNERSHIP.RATIO — Table Schema

> Source: `INSERTS/I_F.FS.GA.COMPOSITE.OWNERSHIP.RATIO` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COMPOSITE.OWNERSHIP.RATIO.NAV.GROUP` | `FsGaCompositeOwnershipRatio_NavGroup` | TField |  | Nav group Multifonds DB Column is NAV_GROUP. |
| 2 | `COMPOSITE.OWNERSHIP.RATIO.FUND.ID` | `FsGaCompositeOwnershipRatio_Fund` |  |  |  |
| 3 | `COMPOSITE.OWNERSHIP.RATIO.SHARE.TYPE` | `FsGaCompositeOwnershipRatio_ShareType` | TField |  | Share type Multifonds DB Column is TPARTS. |
| 4 | `COMPOSITE.OWNERSHIP.RATIO.DATE.NAV` | `FsGaCompositeOwnershipRatio_DateNav` | TField |  | Date Nav Multifonds DB Column is DATE_NAV. |
| 5 | `COMPOSITE.OWNERSHIP.RATIO.COMPOSITE.OWNERSHIP.RATIO` | `FsGaCompositeOwnershipRatio_CompositeOwnershipRatio` | TField |  | Composite ownership ratio Multifonds DB Column is COMP_OWN_RATIO. |
| 6 | `COMPOSITE.OWNERSHIP.RATIO.RECORD.STATUS` | `FsGaCompositeOwnershipRatio_RecordStatus` | String |  |  |
| 7 | `COMPOSITE.OWNERSHIP.RATIO.CURR.NO` | `FsGaCompositeOwnershipRatio_CurrNo` | String |  |  |
| 8 | `COMPOSITE.OWNERSHIP.RATIO.INPUTTER` | `FsGaCompositeOwnershipRatio_Inputter` |  |  |  |
| 9 | `COMPOSITE.OWNERSHIP.RATIO.DATE.TIME` | `FsGaCompositeOwnershipRatio_DateTime` |  |  |  |
| 10 | `COMPOSITE.OWNERSHIP.RATIO.AUTHORISER` | `FsGaCompositeOwnershipRatio_Authoriser` | String |  |  |
| 11 | `COMPOSITE.OWNERSHIP.RATIO.CO.CODE` | `FsGaCompositeOwnershipRatio_CoCode` | String |  |  |
| 12 | `COMPOSITE.OWNERSHIP.RATIO.DEPT.CODE` | `FsGaCompositeOwnershipRatio_DeptCode` | String |  |  |
| 13 | `COMPOSITE.OWNERSHIP.RATIO.AUDITOR.CODE` | `FsGaCompositeOwnershipRatio_AuditorCode` | String |  |  |
| 14 | `COMPOSITE.OWNERSHIP.RATIO.AUDIT.DATE.TIME` | `FsGaCompositeOwnershipRatio_AuditDateTime` | String |  |  |
