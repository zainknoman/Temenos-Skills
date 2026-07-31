# EB.BROWSER.CUSTOMISE.MSG — Table Schema

> Source: `INSERTS/I_F.EB.BROWSER.CUSTOMISE.MSG` in `EB_Interface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.CMSG.DESCRIPTION` | `EbBrowserCustomiseMsg_Description` | TField |  | Standard T24 alphanumeric field. Text field which describes the record. Validation Rules: A maximum of 70 characters can be entered. |
| 2 | `EB.CMSG.HOOK.ROUTINE` | `EbBrowserCustomiseMsg_Hook.routine` |  |  |  |
| 3 | `EB.CMSG.RESERVED.20` | `EbBrowserCustomiseMsg_Reserved20` | TField |  |  |
| 4 | `EB.CMSG.RESERVED.19` | `EbBrowserCustomiseMsg_Reserved19` | TField |  |  |
| 5 | `EB.CMSG.RESERVED.18` | `EbBrowserCustomiseMsg_Reserved18` | TField |  |  |
| 6 | `EB.CMSG.RESERVED.17` | `EbBrowserCustomiseMsg_Reserved17` | TField |  |  |
| 7 | `EB.CMSG.RESERVED.16` | `EbBrowserCustomiseMsg_Reserved16` | TField |  |  |
| 8 | `EB.CMSG.RESERVED.15` | `EbBrowserCustomiseMsg_Reserved15` | TField |  |  |
| 9 | `EB.CMSG.RESERVED.14` | `EbBrowserCustomiseMsg_Reserved14` | TField |  |  |
| 10 | `EB.CMSG.RESERVED.13` | `EbBrowserCustomiseMsg_Reserved13` | TField |  |  |
| 11 | `EB.CMSG.RESERVED.12` | `EbBrowserCustomiseMsg_Reserved12` | TField |  |  |
| 12 | `EB.CMSG.RESERVED.11` | `EbBrowserCustomiseMsg_Reserved11` | TField |  |  |
| 13 | `EB.CMSG.RESERVED.10` | `EbBrowserCustomiseMsg_Reserved10` | TField |  |  |
| 14 | `EB.CMSG.RESERVED.9` | `EbBrowserCustomiseMsg_Reserved9` | TField |  |  |
| 15 | `EB.CMSG.RESERVED.8` | `EbBrowserCustomiseMsg_Reserved8` | TField |  |  |
| 16 | `EB.CMSG.RESERVED.7` | `EbBrowserCustomiseMsg_Reserved7` | TField |  |  |
| 17 | `EB.CMSG.RESERVED.6` | `EbBrowserCustomiseMsg_Reserved6` | TField |  |  |
| 18 | `EB.CMSG.RESERVED.5` | `EbBrowserCustomiseMsg_Reserved5` | TField |  |  |
| 19 | `EB.CMSG.RESERVED.4` | `EbBrowserCustomiseMsg_Reserved4` | TField |  |  |
| 20 | `EB.CMSG.RESERVED.3` | `EbBrowserCustomiseMsg_Reserved3` | TField |  |  |
| 21 | `EB.CMSG.RESERVED.2` | `EbBrowserCustomiseMsg_Reserved2` | TField |  |  |
| 22 | `EB.CMSG.OVERRIDE` | `EbBrowserCustomiseMsg_Override` |  |  |  |
| 23 | `EB.CMSG.RECORD.STATUS` | `EbBrowserCustomiseMsg_RecordStatus` | String |  |  |
| 24 | `EB.CMSG.CURR.NO` | `EbBrowserCustomiseMsg_CurrNo` | String |  |  |
| 25 | `EB.CMSG.INPUTTER` | `EbBrowserCustomiseMsg_Inputter` |  |  |  |
| 26 | `EB.CMSG.DATE.TIME` | `EbBrowserCustomiseMsg_DateTime` |  |  |  |
| 27 | `EB.CMSG.AUTHORISER` | `EbBrowserCustomiseMsg_Authoriser` | String |  |  |
| 28 | `EB.CMSG.CO.CODE` | `EbBrowserCustomiseMsg_CoCode` | String |  |  |
| 29 | `EB.CMSG.DEPT.CODE` | `EbBrowserCustomiseMsg_DeptCode` | String |  |  |
| 30 | `EB.CMSG.AUDITOR.CODE` | `EbBrowserCustomiseMsg_AuditorCode` | String |  |  |
| 31 | `EB.CMSG.AUDIT.DATE.TIME` | `EbBrowserCustomiseMsg_AuditDateTime` | String |  |  |
