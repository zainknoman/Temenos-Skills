# EB.TAABS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.EB.TAABS.PARAMETER` in `EB_ProductConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.TPAR.OP.MODE` | `EbTaabsParameter_OpMode` | TField |  | Defines the TAABS operation mode. Allowed Values - "CAPTURE", "PACKAGE", "RELEASE" |
| 2 | `EB.TPAR.IGNORE.APP` | `EbTaabsParameter_IgnoreApp` |  |  |  |
| 3 | `EB.TPAR.IGNORE.VERSION` | `EbTaabsParameter_IgnoreVersion` |  |  |  |
| 4 | `EB.TPAR.IGNORE.USER` | `EbTaabsParameter_IgnoreUser` |  |  |  |
| 5 | `EB.TPAR.INCLUDE.SERVICE` | `EbTaabsParameter_IncludeService` |  |  |  |
| 6 | `EB.TPAR.CAPTURE.RTN` | `EbTaabsParameter_CaptureRtn` | TField |  | This field contains reference to EB.API application. The BASIC routine defined here would get the contents of the data captured in the transaction as input argument and could amend its contents so that the modified OFS String is updated inTAABS.MESSAGE.QUEUE. |
| 7 | `EB.TPAR.MAX.RECORD.PACK` | `EbTaabsParameter_MaxRecordPack` | TField |  | This field contains the maximum number of OFS Strings that could be accommodated in a single TAABS.PACKAGE record. The default value is 50 and 50 is the maximum value permitted as well. |
| 8 | `EB.TPAR.REL.USER` | `EbTaabsParameter_RelUser` | TField |  | This field contains reference to USER application. During the release of TAABS data this user if defined would supersede the actual USER captured in the OFS string. |
| 9 | `EB.TPAR.SINGLE.PACKAGE` | `EbTaabsParameter_SinglePackage` | TField |  |  |
| 10 | `EB.TPAR.SINGLE.PACK.NAME` | `EbTaabsParameter_SinglePackName` | TField |  |  |
| 11 | `EB.TPAR.RESERVED.8` | `EbTaabsParameter_Reserved8` | TField |  |  |
| 12 | `EB.TPAR.RESERVED.7` | `EbTaabsParameter_Reserved7` | TField |  |  |
| 13 | `EB.TPAR.RESERVED.6` | `EbTaabsParameter_Reserved6` | TField |  |  |
| 14 | `EB.TPAR.RESERVED.5` | `EbTaabsParameter_Reserved5` | TField |  |  |
| 15 | `EB.TPAR.RESERVED.4` | `EbTaabsParameter_Reserved4` | TField |  |  |
| 16 | `EB.TPAR.RESERVED.3` | `EbTaabsParameter_Reserved3` | TField |  |  |
| 17 | `EB.TPAR.RESERVED.2` | `EbTaabsParameter_Reserved2` | TField |  |  |
| 18 | `EB.TPAR.RESERVED.1` | `EbTaabsParameter_Reserved1` | TField |  |  |
| 19 | `EB.TPAR.LOCAL.REF` | `EbTaabsParameter_LocalRef` |  |  |  |
| 20 | `EB.TPAR.OVERRIDE` | `EbTaabsParameter_Override` |  |  |  |
| 21 | `EB.TPAR.RECORD.STATUS` | `EbTaabsParameter_RecordStatus` | String |  |  |
| 22 | `EB.TPAR.CURR.NO` | `EbTaabsParameter_CurrNo` | String |  |  |
| 23 | `EB.TPAR.INPUTTER` | `EbTaabsParameter_Inputter` |  |  |  |
| 24 | `EB.TPAR.DATE.TIME` | `EbTaabsParameter_DateTime` |  |  |  |
| 25 | `EB.TPAR.AUTHORISER` | `EbTaabsParameter_Authoriser` | String |  |  |
| 26 | `EB.TPAR.CO.CODE` | `EbTaabsParameter_CoCode` | String |  |  |
| 27 | `EB.TPAR.DEPT.CODE` | `EbTaabsParameter_DeptCode` | String |  |  |
| 28 | `EB.TPAR.AUDITOR.CODE` | `EbTaabsParameter_AuditorCode` | String |  |  |
| 29 | `EB.TPAR.AUDIT.DATE.TIME` | `EbTaabsParameter_AuditDateTime` | String |  |  |
