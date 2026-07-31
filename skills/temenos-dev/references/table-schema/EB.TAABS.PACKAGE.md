# EB.TAABS.PACKAGE — Table Schema

> Source: `INSERTS/I_F.EB.TAABS.PACKAGE` in `EB_ProductConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.TPAC.APPL.VERSION` | `EbTaabsPackage_ApplVersion` |  |  |  |
| 2 | `EB.TPAC.FUNCTION` | `EbTaabsPackage_Function` |  |  |  |
| 3 | `EB.TPAC.TXN.ID` | `EbTaabsPackage_TxnId` |  |  |  |
| 4 | `EB.TPAC.USER` | `EbTaabsPackage_User` |  |  |  |
| 5 | `EB.TPAC.USER.ROLE` | `EbTaabsPackage_UserRole` |  |  |  |
| 6 | `EB.TPAC.MSG.CAPTURED` | `EbTaabsPackage_MsgCaptured` |  |  |  |
| 7 | `EB.TPAC.MSG.RESPONSE` | `EbTaabsPackage_MsgResponse` |  |  |  |
| 8 | `EB.TPAC.COMMENTS` | `EbTaabsPackage_Comments` |  |  |  |
| 9 | `EB.TPAC.RESERVED.4` | `EbTaabsPackage_Reserved4` |  |  |  |
| 10 | `EB.TPAC.RESERVED.3` | `EbTaabsPackage_Reserved3` |  |  |  |
| 11 | `EB.TPAC.RESERVED.2` | `EbTaabsPackage_Reserved2` |  |  |  |
| 12 | `EB.TPAC.RESERVED.1` | `EbTaabsPackage_Reserved1` |  |  |  |
| 13 | `EB.TPAC.EXCL.FOR.RELEASE` | `EbTaabsPackage_ExclForRelease` |  |  |  |
| 14 | `EB.TPAC.PACKAGED.IND` | `EbTaabsPackage_PackagedInd` | TField |  | This field indicates a 'Y' if it has already been included into a package. |
| 15 | `EB.TPAC.RELEASE.DATE` | `EbTaabsPackage_ReleaseDate` | TField |  | This field indicates the date on which all the associated events captured in this record has been released into the target system. |
