# EB.SIGNATORY.GROUP — Table Schema

> Source: `INSERTS/I_F.EB.SIGNATORY.GROUP` in `EB_Mandate.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SIG.GRP.DESCRIPTION` | `EbSignatoryGroup_Description` |  |  |  |
| 2 | `EB.SIG.GRP.SIGNATORY.CUSTOMER` | `EbSignatoryGroup_SignatoryCustomer` |  |  |  |
| 3 | `EB.SIG.GRP.START.DATE` | `EbSignatoryGroup_StartDate` |  |  |  |
| 4 | `EB.SIG.GRP.END.DATE` | `EbSignatoryGroup_EndDate` |  |  |  |
| 5 | `EB.SIG.GRP.RESERVED.10` | `EbSignatoryGroup_Reserved10` | TField |  |  |
| 6 | `EB.SIG.GRP.RESERVED.9` | `EbSignatoryGroup_Reserved9` | TField |  |  |
| 7 | `EB.SIG.GRP.RESERVED.8` | `EbSignatoryGroup_Reserved8` | TField |  |  |
| 8 | `EB.SIG.GRP.RESERVED.7` | `EbSignatoryGroup_Reserved7` | TField |  |  |
| 9 | `EB.SIG.GRP.RESERVED.6` | `EbSignatoryGroup_Reserved6` | TField |  |  |
| 10 | `EB.SIG.GRP.RESERVED.5` | `EbSignatoryGroup_Reserved5` | TField |  |  |
| 11 | `EB.SIG.GRP.RESERVED.4` | `EbSignatoryGroup_Reserved4` | TField |  |  |
| 12 | `EB.SIG.GRP.RESERVED.3` | `EbSignatoryGroup_Reserved3` | TField |  |  |
| 13 | `EB.SIG.GRP.RESERVED.2` | `EbSignatoryGroup_Reserved2` | TField |  |  |
| 14 | `EB.SIG.GRP.RESERVED.1` | `EbSignatoryGroup_Reserved1` | TField |  |  |
| 15 | `EB.SIG.GRP.LOCAL.REF` | `EbSignatoryGroup_LocalRef` |  |  |  |
| 16 | `EB.SIG.GRP.OVERRIDE` | `EbSignatoryGroup_Override` |  |  |  |
| 17 | `EB.SIG.GRP.RECORD.STATUS` | `EbSignatoryGroup_RecordStatus` | String |  |  |
| 18 | `EB.SIG.GRP.CURR.NO` | `EbSignatoryGroup_CurrNo` | String |  |  |
| 19 | `EB.SIG.GRP.INPUTTER` | `EbSignatoryGroup_Inputter` |  |  |  |
| 20 | `EB.SIG.GRP.DATE.TIME` | `EbSignatoryGroup_DateTime` |  |  |  |
| 21 | `EB.SIG.GRP.AUTHORISER` | `EbSignatoryGroup_Authoriser` | String |  |  |
| 22 | `EB.SIG.GRP.CO.CODE` | `EbSignatoryGroup_CoCode` | String |  |  |
| 23 | `EB.SIG.GRP.DEPT.CODE` | `EbSignatoryGroup_DeptCode` | String |  |  |
| 24 | `EB.SIG.GRP.AUDITOR.CODE` | `EbSignatoryGroup_AuditorCode` | String |  |  |
| 25 | `EB.SIG.GRP.AUDIT.DATE.TIME` | `EbSignatoryGroup_AuditDateTime` | String |  |  |
