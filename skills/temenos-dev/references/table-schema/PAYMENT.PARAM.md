# PAYMENT.PARAM — Table Schema

> Source: `INSERTS/I_F.PAYMENT.PARAM` in `CAEFPA_EFTPap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DEP.EXT.PO.PRODUCT` | `PaymentParam_PoProduct` |  |  |  |
| 2 | `DEP.EXT.FT.VERSION` | `PaymentParam_FtVersion` | TField |  | This field is used to define the FT version for raising the accounting entryCheckfile: VERSION |
| 3 | `DEP.EXT.OFS.SOURCE` | `PaymentParam_OfsSource` | TField |  | This field it used to define the OFS.SOURCE for raising the accounting entryCheckfile: OFS.SOURCE |
| 4 | `DEP.EXT.RESERVED.10` | `PaymentParam_Reserved10` | TField |  |  |
| 5 | `DEP.EXT.RESERVED.9` | `PaymentParam_Reserved9` | TField |  |  |
| 6 | `DEP.EXT.RESERVED.8` | `PaymentParam_Reserved8` | TField |  |  |
| 7 | `DEP.EXT.RESERVED.7` | `PaymentParam_Reserved7` | TField |  |  |
| 8 | `DEP.EXT.RESERVED.6` | `PaymentParam_Reserved6` | TField |  |  |
| 9 | `DEP.EXT.RESERVED.5` | `PaymentParam_Reserved5` | TField |  |  |
| 10 | `DEP.EXT.RESERVED.4` | `PaymentParam_Reserved4` | TField |  |  |
| 11 | `DEP.EXT.RESERVED.3` | `PaymentParam_Reserved3` | TField |  |  |
| 12 | `DEP.EXT.RESERVED.2` | `PaymentParam_Reserved2` | TField |  |  |
| 13 | `DEP.EXT.RESERVED.1` | `PaymentParam_Reserved1` | TField |  |  |
| 14 | `DEP.EXT.OVERRIDE` | `PaymentParam_Override` |  |  |  |
| 15 | `DEP.EXT.RECORD.STATUS` | `PaymentParam_RecordStatus` | String |  |  |
| 16 | `DEP.EXT.CURR.NO` | `PaymentParam_CurrNo` | String |  |  |
| 17 | `DEP.EXT.INPUTTER` | `PaymentParam_Inputter` |  |  |  |
| 18 | `DEP.EXT.DATE.TIME` | `PaymentParam_DateTime` |  |  |  |
| 19 | `DEP.EXT.AUTHORISER` | `PaymentParam_Authoriser` | String |  |  |
| 20 | `DEP.EXT.CO.CODE` | `PaymentParam_CoCode` | String |  |  |
| 21 | `DEP.EXT.DEPT.CODE` | `PaymentParam_DeptCode` | String |  |  |
| 22 | `DEP.EXT.AUDITOR.CODE` | `PaymentParam_AuditorCode` | String |  |  |
| 23 | `DEP.EXT.AUDIT.DATE.TIME` | `PaymentParam_AuditDateTime` | String |  |  |
