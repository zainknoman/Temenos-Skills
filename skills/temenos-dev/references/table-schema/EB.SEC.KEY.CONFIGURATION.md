# EB.SEC.KEY.CONFIGURATION — Table Schema

> Source: `INSERTS/I_F.EB.SEC.KEY.CONFIGURATION` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEC.KEY.KEYSTORE.NAME` | `EbSecKeyConfiguration_KeystoreName` |  |  |  |
| 2 | `SEC.KEY.KEYSTORE.ENCRYPTED.PASSWD` | `EbSecKeyConfiguration_KeystoreEncryptedPasswd` |  |  |  |
| 3 | `SEC.KEY.ENTRY.NAME` | `EbSecKeyConfiguration_EntryName` |  |  |  |
| 4 | `SEC.KEY.ENTRY.GENERATED.PASSWORD` | `EbSecKeyConfiguration_EntryGeneratedPassword` |  |  |  |
| 5 | `SEC.KEY.ENTRY.TYPE` | `EbSecKeyConfiguration_EntryType` |  |  |  |
| 6 | `SEC.KEY.RESERVED.1` | `EbSecKeyConfiguration_Reserved1` |  |  |  |
| 7 | `SEC.KEY.RESERVED.2` | `EbSecKeyConfiguration_Reserved2` |  |  |  |
| 8 | `SEC.KEY.RESERVED.3` | `EbSecKeyConfiguration_Reserved3` |  |  |  |
| 9 | `SEC.KEY.RESERVED.4` | `EbSecKeyConfiguration_Reserved4` |  |  |  |
| 10 | `SEC.KEY.OPERATION` | `EbSecKeyConfiguration_Operation` |  |  |  |
| 11 | `SEC.KEY.GRACE` | `EbSecKeyConfiguration_Grace` |  |  |  |
| 12 | `SEC.KEY.KEY.EXPIRY.WARN` | `EbSecKeyConfiguration_KeyExpiryWarn` | TField |  |  |
| 13 | `SEC.KEY.RESERVED.6` | `EbSecKeyConfiguration_Reserved6` | TField |  |  |
| 14 | `SEC.KEY.RESERVED.7` | `EbSecKeyConfiguration_Reserved7` | TField |  |  |
| 15 | `SEC.KEY.RESERVED.8` | `EbSecKeyConfiguration_Reserved8` | TField |  |  |
| 16 | `SEC.KEY.RESERVED.9` | `EbSecKeyConfiguration_Reserved9` | TField |  |  |
| 17 | `SEC.KEY.RESERVED.10` | `EbSecKeyConfiguration_Reserved10` | TField |  |  |
| 18 | `SEC.KEY.OVERRIDE` | `EbSecKeyConfiguration_Override` |  |  |  |
| 19 | `SEC.KEY.RECORD.STATUS` | `EbSecKeyConfiguration_RecordStatus` | String |  |  |
| 20 | `SEC.KEY.CURR.NO` | `EbSecKeyConfiguration_CurrNo` | String |  |  |
| 21 | `SEC.KEY.INPUTTER` | `EbSecKeyConfiguration_Inputter` |  |  |  |
| 22 | `SEC.KEY.DATE.TIME` | `EbSecKeyConfiguration_DateTime` |  |  |  |
| 23 | `SEC.KEY.AUTHORISER` | `EbSecKeyConfiguration_Authoriser` | String |  |  |
| 24 | `SEC.KEY.CO.CODE` | `EbSecKeyConfiguration_CoCode` | String |  |  |
| 25 | `SEC.KEY.DEPT.CODE` | `EbSecKeyConfiguration_DeptCode` | String |  |  |
| 26 | `SEC.KEY.AUDITOR.CODE` | `EbSecKeyConfiguration_AuditorCode` | String |  |  |
| 27 | `SEC.KEY.AUDIT.DATE.TIME` | `EbSecKeyConfiguration_AuditDateTime` | String |  |  |
