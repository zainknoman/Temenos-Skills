# AA.POOL.ORCHESTRATION.DETAILS — Table Schema

> Source: `INSERTS/I_F.AA.POOL.ORCHESTRATION.DETAILS` in `AA_BundleHierarchy.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.POD.ACCOUNT.REF` | `AaPoolOrchestrationDetails_AccountRef` |  |  |  |
| 2 | `AA.POD.ACCOUNT.ALIAS` | `AaPoolOrchestrationDetails_AccountAlias` |  |  |  |
| 3 | `AA.POD.SHORT.NAME` | `AaPoolOrchestrationDetails_ShortName` |  |  |  |
| 4 | `AA.POD.CUSTOMER` | `AaPoolOrchestrationDetails_Customer` |  |  |  |
| 5 | `AA.POD.ACC.COMPANY` | `AaPoolOrchestrationDetails_AccCompany` |  |  |  |
| 6 | `AA.POD.ACC.CURRENCY` | `AaPoolOrchestrationDetails_AccCurrency` |  |  |  |
| 7 | `AA.POD.ACC.PRODUCT` | `AaPoolOrchestrationDetails_AccProduct` |  |  |  |
| 8 | `AA.POD.ALT.REFERENCE` | `AaPoolOrchestrationDetails_AltReference` |  |  |  |
| 9 | `AA.POD.RESERVED.4` | `AaPoolOrchestrationDetails_Reserved4` |  |  |  |
| 10 | `AA.POD.RESERVED.3` | `AaPoolOrchestrationDetails_Reserved3` |  |  |  |
| 11 | `AA.POD.NEW.BUNDLE.REF` | `AaPoolOrchestrationDetails_NewBundleRef` |  |  |  |
| 12 | `AA.POD.PARENT.ACCOUNT` | `AaPoolOrchestrationDetails_ParentAccount` |  |  |  |
| 13 | `AA.POD.LINK.TYPE` | `AaPoolOrchestrationDetails_LinkType` |  |  |  |
| 14 | `AA.POD.KEEP.BALANCE` | `AaPoolOrchestrationDetails_KeepBalance` |  |  |  |
| 15 | `AA.POD.LIVE.DATE` | `AaPoolOrchestrationDetails_LiveDate` |  |  |  |
| 16 | `AA.POD.ACTIVITY.REF` | `AaPoolOrchestrationDetails_ActivityRef` |  |  |  |
| 17 | `AA.POD.STATUS` | `AaPoolOrchestrationDetails_Status` |  |  |  |
| 18 | `AA.POD.ACC.LOCATION` | `AaPoolOrchestrationDetails_AccLocation` |  |  |  |
| 19 | `AA.POD.ACC.SEQUENCE` | `AaPoolOrchestrationDetails_AccSequence` |  |  |  |
| 20 | `AA.POD.CANCEL.RESTRUCTURE` | `AaPoolOrchestrationDetails_CancelRestructure` |  |  |  |
| 21 | `AA.POD.RESERVED.6` | `AaPoolOrchestrationDetails_Reserved6` |  |  |  |
| 22 | `AA.POD.ERR.SOURCE` | `AaPoolOrchestrationDetails_ErrSource` |  |  |  |
| 23 | `AA.POD.ERR.MESSAGE` | `AaPoolOrchestrationDetails_ErrMessage` |  |  |  |
| 24 | `AA.POD.OVERALL.STATUS` | `AaPoolOrchestrationDetails_OverallStatus` | TField |  | Contains either of two values Completed with error - when the pool orchestration service service has completed with error Completed Successfully - when the pool orchestration has completed without any errors |
