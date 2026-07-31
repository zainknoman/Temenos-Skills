# USLEND.PRINT.FORMAT — Table Schema

> Source: `INSERTS/I_F.USLEND.PRINT.FORMAT` in `USLEND_EscrowProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UPF.DESCRIPTION` | `UslendPrintFormat_Description` |  |  |  |
| 2 | `UPF.MESSAGE.TEXT` | `UslendPrintFormat_MessageText` |  |  |  |
| 3 | `UPF.RESERVED.20` | `UslendPrintFormat_Reserved20` | TField |  |  |
| 4 | `UPF.RESERVED.19` | `UslendPrintFormat_Reserved19` | TField |  |  |
| 5 | `UPF.RESERVED.18` | `UslendPrintFormat_Reserved18` | TField |  |  |
| 6 | `UPF.RESERVED.17` | `UslendPrintFormat_Reserved17` | TField |  |  |
| 7 | `UPF.RESERVED.16` | `UslendPrintFormat_Reserved16` | TField |  |  |
| 8 | `UPF.RESERVED.15` | `UslendPrintFormat_Reserved15` | TField |  |  |
| 9 | `UPF.RESERVED.14` | `UslendPrintFormat_Reserved14` | TField |  |  |
| 10 | `UPF.RESERVED.13` | `UslendPrintFormat_Reserved13` | TField |  |  |
| 11 | `UPF.RESERVED.12` | `UslendPrintFormat_Reserved12` | TField |  |  |
| 12 | `UPF.RESERVED.11` | `UslendPrintFormat_Reserved11` | TField |  |  |
| 13 | `UPF.RESERVED.10` | `UslendPrintFormat_Reserved10` | TField |  |  |
| 14 | `UPF.RESERVED.9` | `UslendPrintFormat_Reserved9` | TField |  |  |
| 15 | `UPF.RESERVED.8` | `UslendPrintFormat_Reserved8` | TField |  |  |
| 16 | `UPF.RESERVED.7` | `UslendPrintFormat_Reserved7` | TField |  |  |
| 17 | `UPF.RESERVED.6` | `UslendPrintFormat_Reserved6` | TField |  |  |
| 18 | `UPF.RESERVED.5` | `UslendPrintFormat_Reserved5` | TField |  |  |
| 19 | `UPF.RESERVED.4` | `UslendPrintFormat_Reserved4` | TField |  |  |
| 20 | `UPF.RESERVED.3` | `UslendPrintFormat_Reserved3` | TField |  |  |
| 21 | `UPF.RESERVED.2` | `UslendPrintFormat_Reserved2` | TField |  |  |
| 22 | `UPF.LOCAL.REF` | `UslendPrintFormat_LocalRef` |  |  |  |
| 23 | `UPF.RECORD.STATUS` | `UslendPrintFormat_RecordStatus` | String |  |  |
| 24 | `UPF.CURR.NO` | `UslendPrintFormat_CurrNo` | String |  |  |
| 25 | `UPF.INPUTTER` | `UslendPrintFormat_Inputter` |  |  |  |
| 26 | `UPF.DATE.TIME` | `UslendPrintFormat_DateTime` |  |  |  |
| 27 | `UPF.AUTHORISER` | `UslendPrintFormat_Authoriser` | String |  |  |
| 28 | `UPF.CO.CODE` | `UslendPrintFormat_CoCode` | String |  |  |
| 29 | `UPF.DEPT.CODE` | `UslendPrintFormat_DeptCode` | String |  |  |
| 30 | `UPF.AUDITOR.CODE` | `UslendPrintFormat_AuditorCode` | String |  |  |
| 31 | `UPF.AUDIT.DATE.TIME` | `UslendPrintFormat_AuditDateTime` | String |  |  |
