# HKBASE.OTHER.ACCOUNTS — Table Schema

> Source: `INSERTS/I_F.HKBASE.OTHER.ACCOUNTS` in `HKBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HK.OTH.CUSTOMER.NO` | `HkbaseOtherAccounts_CustomerNo` | TField |  | T24 Customer ID of Primary customer in External AccountWill be same as the Customer ID as in the @ ID. |
| 2 | `HK.OTH.EXT.ACC.OPEN.DATE` | `HkbaseOtherAccounts_ExtAccOpenDate` | TField |  | The open date of External Account. |
| 3 | `HK.OTH.EXT.ACC.CLOSE.DATE` | `HkbaseOtherAccounts_ExtAccCloseDate` | TField |  | The close date of External Account. |
| 4 | `HK.OTH.LOCAL.REF` | `HkbaseOtherAccounts_LocalRef` |  |  |  |
| 5 | `HK.OTH.RESERVED.1` | `HkbaseOtherAccounts_Reserved1` | TField |  | Reserved for future purpose. |
| 6 | `HK.OTH.RESERVED.2` | `HkbaseOtherAccounts_Reserved2` | TField |  | Reserved for future purpose. |
| 7 | `HK.OTH.RESERVED.3` | `HkbaseOtherAccounts_Reserved3` | TField |  | Reserved for future purpose. |
| 8 | `HK.OTH.RESERVED.4` | `HkbaseOtherAccounts_Reserved4` | TField |  | Reserved for future purpose. |
| 9 | `HK.OTH.RESERVED.5` | `HkbaseOtherAccounts_Reserved5` | TField |  | Reserved for future purpose. |
| 10 | `HK.OTH.RESERVED.6` | `HkbaseOtherAccounts_Reserved6` | TField |  | Reserved for future purpose. |
| 11 | `HK.OTH.RESERVED.7` | `HkbaseOtherAccounts_Reserved7` | TField |  | Reserved for future purpose. |
| 12 | `HK.OTH.RESERVED.8` | `HkbaseOtherAccounts_Reserved8` | TField |  | Reserved for future purpose. |
| 13 | `HK.OTH.RESERVED.9` | `HkbaseOtherAccounts_Reserved9` | TField |  | Reserved for future purpose. |
| 14 | `HK.OTH.RESERVED.10` | `HkbaseOtherAccounts_Reserved10` | TField |  | Reserved for future purpose. |
| 15 | `HK.OTH.OVERRIDE` | `HkbaseOtherAccounts_Override` |  |  |  |
| 16 | `HK.OTH.RECORD.STATUS` | `HkbaseOtherAccounts_RecordStatus` | String |  |  |
| 17 | `HK.OTH.CURR.NO` | `HkbaseOtherAccounts_CurrNo` | String |  |  |
| 18 | `HK.OTH.INPUTTER` | `HkbaseOtherAccounts_Inputter` |  |  |  |
| 19 | `HK.OTH.DATE.TIME` | `HkbaseOtherAccounts_DateTime` |  |  |  |
| 20 | `HK.OTH.AUTHORISER` | `HkbaseOtherAccounts_Authoriser` | String |  |  |
| 21 | `HK.OTH.CO.CODE` | `HkbaseOtherAccounts_CoCode` | String |  |  |
| 22 | `HK.OTH.DEPT.CODE` | `HkbaseOtherAccounts_DeptCode` | String |  |  |
| 23 | `HK.OTH.AUDITOR.CODE` | `HkbaseOtherAccounts_AuditorCode` | String |  |  |
| 24 | `HK.OTH.AUDIT.DATE.TIME` | `HkbaseOtherAccounts_AuditDateTime` | String |  |  |
