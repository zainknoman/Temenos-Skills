# SC.WHT.ADJ.PARAM — Table Schema

> Source: `INSERTS/I_F.SC.WHT.ADJ.PARAM` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.WAP.ADJ.SOURCE` | `ScWhtAdjParam_AdjSource` | TField | Yes | Mandatory field.If the withholding is at source (meaning by the custodian and not the bank) this field will determine whether any adjustment of tax for over or under withheld is possible(YES/NO).Defaulted to YES. |
| 2 | `SC.WAP.REIMBURSE.CAT` | `ScWhtAdjParam_ReimburseCat` | TField |  | If the field is set then the field REIMB.TAX.ACCT.CAT in SC.ADJ.TXN.UPDATE application will be update with thiscategory as default. |
| 3 | `SC.WAP.FT.VERSION` | `ScWhtAdjParam_FtVersion` | TField |  | Version used to create a FUNDS.TRANSFER record through OFS after authorising SC.ADJ.TXN.UPDATE record. |
| 4 | `SC.WAP.FT.TXN.TYPE` | `ScWhtAdjParam_FtTxnType` | TField | Yes | Mandatory field. Default TXN.TYPE for the FUNDS.TRANSFER record after authorising SC.ADJ.TXN.UPDATE record. |
| 5 | `SC.WAP.FT.OFS.SOURCE` | `ScWhtAdjParam_FtOfsSource` | TField |  | OFS.SOURCE record used to create a FUNDS.TRANSFER record through OFS after authorising SC.ADJ.TXN.UPDATE record. |
| 6 | `SC.WAP.OFS.SOURCE` | `ScWhtAdjParam_OfsSource` |  |  |  |
| 7 | `SC.WAP.OFS.VERSION` | `ScWhtAdjParam_OfsVersion` |  |  |  |
| 8 | `SC.WAP.RESERVED.8` | `ScWhtAdjParam_Reserved8` | TField |  |  |
| 9 | `SC.WAP.RESERVED.7` | `ScWhtAdjParam_Reserved7` | TField |  |  |
| 10 | `SC.WAP.RESERVED.6` | `ScWhtAdjParam_Reserved6` | TField |  |  |
| 11 | `SC.WAP.RESERVED.5` | `ScWhtAdjParam_Reserved5` | TField |  |  |
| 12 | `SC.WAP.RESERVED.4` | `ScWhtAdjParam_Reserved4` | TField |  |  |
| 13 | `SC.WAP.RESERVED.3` | `ScWhtAdjParam_Reserved3` | TField |  |  |
| 14 | `SC.WAP.RESERVED.2` | `ScWhtAdjParam_Reserved2` | TField |  |  |
| 15 | `SC.WAP.RESERVED.1` | `ScWhtAdjParam_Reserved1` | TField |  |  |
| 16 | `SC.WAP.LOCAL.REF` | `ScWhtAdjParam_LocalRef` |  |  |  |
| 17 | `SC.WAP.OVERRIDE` | `ScWhtAdjParam_Override` |  |  |  |
| 18 | `SC.WAP.RECORD.STATUS` | `ScWhtAdjParam_RecordStatus` | String |  |  |
| 19 | `SC.WAP.CURR.NO` | `ScWhtAdjParam_CurrNo` | String |  |  |
| 20 | `SC.WAP.INPUTTER` | `ScWhtAdjParam_Inputter` |  |  |  |
| 21 | `SC.WAP.DATE.TIME` | `ScWhtAdjParam_DateTime` |  |  |  |
| 22 | `SC.WAP.AUTHORISER` | `ScWhtAdjParam_Authoriser` | String |  |  |
| 23 | `SC.WAP.CO.CODE` | `ScWhtAdjParam_CoCode` | String |  |  |
| 24 | `SC.WAP.DEPT.CODE` | `ScWhtAdjParam_DeptCode` | String |  |  |
| 25 | `SC.WAP.AUDITOR.CODE` | `ScWhtAdjParam_AuditorCode` | String |  |  |
| 26 | `SC.WAP.AUDIT.DATE.TIME` | `ScWhtAdjParam_AuditDateTime` | String |  |  |
