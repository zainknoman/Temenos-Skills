# AA.BUNDLE.HIERARCHY.DETAILS — Table Schema

> Source: `INSERTS/I_F.AA.BUNDLE.HIERARCHY.DETAILS` in `AA_BundleHierarchy.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.BHD.ACCOUNT.REF` | `AaBundleHierarchyDetails_AccountRef` |  |  |  |
| 2 | `AA.BHD.PARENT.ACCOUNT` | `AaBundleHierarchyDetails_ParentAccount` |  |  |  |
| 3 | `AA.BHD.LINK.TYPE` | `AaBundleHierarchyDetails_LinkType` |  |  |  |
| 4 | `AA.BHD.STATUS` | `AaBundleHierarchyDetails_Status` |  |  |  |
| 5 | `AA.BHD.ACCOUNT.ALIAS` | `AaBundleHierarchyDetails_AccountAlias` |  |  |  |
| 6 | `AA.BHD.ALT.REFERENCE` | `AaBundleHierarchyDetails_AltReference` |  |  |  |
| 7 | `AA.BHD.ACTIVITY.REF` | `AaBundleHierarchyDetails_ActivityRef` |  |  |  |
| 8 | `AA.BHD.ACTIVITY.STATUS` | `AaBundleHierarchyDetails_ActivityStatus` |  |  |  |
| 9 | `AA.BHD.LIVE.DATE` | `AaBundleHierarchyDetails_LiveDate` |  |  |  |
| 10 | `AA.BHD.NEW.BUNDLE.REF` | `AaBundleHierarchyDetails_NewBundleRef` |  |  |  |
| 11 | `AA.BHD.KEEP.BALANCE` | `AaBundleHierarchyDetails_KeepBalance` |  |  |  |
| 12 | `AA.BHD.RESERVED.13` | `AaBundleHierarchyDetails_Reserved13` |  |  |  |
| 13 | `AA.BHD.RESERVED.12` | `AaBundleHierarchyDetails_Reserved12` |  |  |  |
| 14 | `AA.BHD.ACC.LOCATION` | `AaBundleHierarchyDetails_AccLocation` |  |  |  |
