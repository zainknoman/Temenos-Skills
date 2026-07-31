# HKBASE.LINK.GC — Table Schema

> Source: `INSERTS/I_F.HKBASE.LINK.GC` in `HKBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HK.LGC.GC.INDICATOR` | `HkbaseLinkGc_GcIndicator` | TField |  | This field indicates if existing Global Customer should be linked or new Global Customer should be created for this Customer. Validation Rule: Radio buttons showing New or Existing. |
| 2 | `HK.LGC.GLOBAL.CUSTOMER.ID` | `HkbaseLinkGc_GlobalCustomerId` | TField | Yes | Validation Rule: This field is mandatory only when GC.INDICATOR is "Existing". |
| 3 | `HK.LGC.RESERVED.1` | `HkbaseLinkGc_Reserved1` | TField |  | Reserved for future purpose. |
| 4 | `HK.LGC.RESERVED.2` | `HkbaseLinkGc_Reserved2` | TField |  | Reserved for future purpose. |
| 5 | `HK.LGC.RESERVED.3` | `HkbaseLinkGc_Reserved3` | TField |  | Reserved for future purpose. |
| 6 | `HK.LGC.RESERVED.4` | `HkbaseLinkGc_Reserved4` | TField |  | Reserved for future purpose. |
| 7 | `HK.LGC.RESERVED.5` | `HkbaseLinkGc_Reserved5` | TField |  | Reserved for future purpose. |
| 8 | `HK.LGC.RESERVED.6` | `HkbaseLinkGc_Reserved6` | TField |  | Reserved for future purpose. |
| 9 | `HK.LGC.RESERVED.7` | `HkbaseLinkGc_Reserved7` | TField |  | Reserved for future purpose. |
| 10 | `HK.LGC.RESERVED.8` | `HkbaseLinkGc_Reserved8` | TField |  | Reserved for future purpose. |
| 11 | `HK.LGC.RESERVED.9` | `HkbaseLinkGc_Reserved9` | TField |  | Reserved for future purpose. |
| 12 | `HK.LGC.RESERVED.10` | `HkbaseLinkGc_Reserved10` | TField |  | Reserved for future purpose. |
| 13 | `HK.LGC.LOCAL.REF` | `HkbaseLinkGc_LocalRef` |  |  |  |
| 14 | `HK.LGC.OVERRIDE` | `HkbaseLinkGc_Override` |  |  |  |
| 15 | `HK.LGC.RECORD.STATUS` | `HkbaseLinkGc_RecordStatus` | String |  |  |
| 16 | `HK.LGC.CURR.NO` | `HkbaseLinkGc_CurrNo` | String |  |  |
| 17 | `HK.LGC.INPUTTER` | `HkbaseLinkGc_Inputter` |  |  |  |
| 18 | `HK.LGC.DATE.TIME` | `HkbaseLinkGc_DateTime` |  |  |  |
| 19 | `HK.LGC.AUTHORISER` | `HkbaseLinkGc_Authoriser` | String |  |  |
| 20 | `HK.LGC.CO.CODE` | `HkbaseLinkGc_CoCode` | String |  |  |
| 21 | `HK.LGC.DEPT.CODE` | `HkbaseLinkGc_DeptCode` | String |  |  |
| 22 | `HK.LGC.AUDITOR.CODE` | `HkbaseLinkGc_AuditorCode` | String |  |  |
| 23 | `HK.LGC.AUDIT.DATE.TIME` | `HkbaseLinkGc_AuditDateTime` | String |  |  |
