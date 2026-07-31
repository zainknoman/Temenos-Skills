# EB.ENC.BROWSER — Table Schema

> Source: `INSERTS/I_F.EB.ENC.BROWSER` in `EB_Security.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.ENC.BRW.DESCRIPTION` | `EbEncBrowser_Description` |  |  |  |
| 2 | `EB.ENC.BRW.ORIGINAL.VALUE` | `EbEncBrowser_OriginalValue` |  |  |  |
| 3 | `EB.ENC.BRW.ENCRYPT.VALUE` | `EbEncBrowser_EncryptValue` |  |  |  |
| 4 | `EB.ENC.BRW.BROWSER.ENCODING` | `EbEncBrowser_BrowserEncoding` | TField |  | Allows the definition of the actual browser encoding value. |
| 5 | `EB.ENC.BRW.RESERVED.5` | `EbEncBrowser_Reserved5` | TField |  |  |
| 6 | `EB.ENC.BRW.RESERVED.4` | `EbEncBrowser_Reserved4` | TField |  |  |
| 7 | `EB.ENC.BRW.RESERVED.3` | `EbEncBrowser_Reserved3` | TField |  |  |
| 8 | `EB.ENC.BRW.RESERVED.2` | `EbEncBrowser_Reserved2` | TField |  |  |
| 9 | `EB.ENC.BRW.RESERVED.1` | `EbEncBrowser_Reserved1` | TField |  |  |
| 10 | `EB.ENC.BRW.LOCAL.REF` | `EbEncBrowser_LocalRef` |  |  |  |
| 11 | `EB.ENC.BRW.RECORD.STATUS` | `EbEncBrowser_RecordStatus` | String |  |  |
| 12 | `EB.ENC.BRW.CURR.NO` | `EbEncBrowser_CurrNo` | String |  |  |
| 13 | `EB.ENC.BRW.INPUTTER` | `EbEncBrowser_Inputter` |  |  |  |
| 14 | `EB.ENC.BRW.DATE.TIME` | `EbEncBrowser_DateTime` |  |  |  |
| 15 | `EB.ENC.BRW.AUTHORISER` | `EbEncBrowser_Authoriser` | String |  |  |
| 16 | `EB.ENC.BRW.CO.CODE` | `EbEncBrowser_CoCode` | String |  |  |
| 17 | `EB.ENC.BRW.DEPT.CODE` | `EbEncBrowser_DeptCode` | String |  |  |
| 18 | `EB.ENC.BRW.AUDITOR.CODE` | `EbEncBrowser_AuditorCode` | String |  |  |
| 19 | `EB.ENC.BRW.AUDIT.DATE.TIME` | `EbEncBrowser_AuditDateTime` | String |  |  |
