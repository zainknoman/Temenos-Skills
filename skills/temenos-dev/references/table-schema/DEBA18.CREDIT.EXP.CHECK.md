# DEBA18.CREDIT.EXP.CHECK — Table Schema

> Source: `INSERTS/I_F.DEBA18.CREDIT.EXP.CHECK` in `DEBA18_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DEBA18.START.CATEGORY` | `Deba18CreditExpCheck_StartCategory` | TField |  | Reserved for future use. |
| 2 | `DEBA18.CATEGORY.OPERATOR` | `Deba18CreditExpCheck_CategoryOperator` | TField |  | Reserved for future use. |
| 3 | `DEBA18.END.CATEGORY` | `Deba18CreditExpCheck_EndCategory` | TField |  | Reserved for future use. |
| 4 | `DEBA18.CUSTOMER.ID` | `Deba18CreditExpCheck_CustomerId` | TField |  |  |
| 5 | `DEBA18.CUSTOMER.GROUP` | `Deba18CreditExpCheck_CustomerGroup` | TField |  | Reserved for future use. |
| 6 | `DEBA18.START.SECTOR` | `Deba18CreditExpCheck_StartSector` | TField |  | Reserved for future use. |
| 7 | `DEBA18.END.SECTOR` | `Deba18CreditExpCheck_EndSector` | TField |  | Reserved for future use. |
| 8 | `DEBA18.SERVICE.CONTROL` | `Deba18CreditExpCheck_ServiceControl` | TField |  | Reserved for future use. |
| 9 | `DEBA18.RESERVED.10` | `Deba18CreditExpCheck_Reserved10` | TField |  | Reserved for Future Use. |
| 10 | `DEBA18.RESERVED.9` | `Deba18CreditExpCheck_Reserved9` | TField |  | Reserved for Future Use. |
| 11 | `DEBA18.RESERVED.8` | `Deba18CreditExpCheck_Reserved8` | TField |  | Reserved for Future Use. |
| 12 | `DEBA18.RESERVED.7` | `Deba18CreditExpCheck_Reserved7` | TField |  | Reserved for Future Use. |
| 13 | `DEBA18.RESERVED.6` | `Deba18CreditExpCheck_Reserved6` | TField |  | Reserved for Future Use. |
| 14 | `DEBA18.RESERVED.5` | `Deba18CreditExpCheck_Reserved5` | TField |  | Reserved for Future Use. |
| 15 | `DEBA18.RESERVED.4` | `Deba18CreditExpCheck_Reserved4` | TField |  | Reserved for Future Use. |
| 16 | `DEBA18.RESERVED.3` | `Deba18CreditExpCheck_Reserved3` | TField |  | Reserved for Future Use. |
| 17 | `DEBA18.RESERVED.2` | `Deba18CreditExpCheck_Reserved2` | TField |  | Reserved for Future Use. |
| 18 | `DEBA18.RESERVED.1` | `Deba18CreditExpCheck_Reserved1` | TField |  | Reserved for Future Use. |
| 19 | `DEBA18.LOCAL.REF` | `Deba18CreditExpCheck_LocalRef` |  |  |  |
| 20 | `DEBA18.OVERRIDE` | `Deba18CreditExpCheck_Override` |  |  |  |
| 21 | `DEBA18.RECORD.STATUS` | `Deba18CreditExpCheck_RecordStatus` | String |  |  |
| 22 | `DEBA18.CURR.NO` | `Deba18CreditExpCheck_CurrNo` | String |  |  |
| 23 | `DEBA18.INPUTTER` | `Deba18CreditExpCheck_Inputter` |  |  |  |
| 24 | `DEBA18.DATE.TIME` | `Deba18CreditExpCheck_DateTime` |  |  |  |
| 25 | `DEBA18.AUTHORISER` | `Deba18CreditExpCheck_Authoriser` | String |  |  |
| 26 | `DEBA18.CO.CODE` | `Deba18CreditExpCheck_CoCode` | String |  |  |
| 27 | `DEBA18.DEPT.CODE` | `Deba18CreditExpCheck_DeptCode` | String |  |  |
| 28 | `DEBA18.AUDITOR.CODE` | `Deba18CreditExpCheck_AuditorCode` | String |  |  |
| 29 | `DEBA18.AUDIT.DATE.TIME` | `Deba18CreditExpCheck_AuditDateTime` | String |  |  |
