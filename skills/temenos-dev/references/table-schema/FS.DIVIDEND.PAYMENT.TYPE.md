# FS.DIVIDEND.PAYMENT.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.DIVIDEND.PAYMENT.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.DIVIDEND.PAYMENT.TYPE.DESCRIPTION` | `FsDividendPaymentType_Description` |  |  |  |
| 2 | `FS.DIVIDEND.PAYMENT.TYPE.FILTER.KEY` | `FsDividendPaymentType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.DIVIDEND.PAYMENT.TYPE.RECORD.ID` | `FsDividendPaymentType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.DIVIDEND.PAYMENT.TYPE.RESERVED10` | `FsDividendPaymentType_Reserved10` | TField |  |  |
| 5 | `FS.DIVIDEND.PAYMENT.TYPE.RESERVED9` | `FsDividendPaymentType_Reserved9` | TField |  |  |
| 6 | `FS.DIVIDEND.PAYMENT.TYPE.RESERVED8` | `FsDividendPaymentType_Reserved8` | TField |  |  |
| 7 | `FS.DIVIDEND.PAYMENT.TYPE.RESERVED7` | `FsDividendPaymentType_Reserved7` | TField |  |  |
| 8 | `FS.DIVIDEND.PAYMENT.TYPE.RESERVED6` | `FsDividendPaymentType_Reserved6` | TField |  |  |
| 9 | `FS.DIVIDEND.PAYMENT.TYPE.RESERVED5` | `FsDividendPaymentType_Reserved5` | TField |  |  |
| 10 | `FS.DIVIDEND.PAYMENT.TYPE.RESERVED4` | `FsDividendPaymentType_Reserved4` | TField |  |  |
| 11 | `FS.DIVIDEND.PAYMENT.TYPE.RESERVED3` | `FsDividendPaymentType_Reserved3` | TField |  |  |
| 12 | `FS.DIVIDEND.PAYMENT.TYPE.RESERVED2` | `FsDividendPaymentType_Reserved2` | TField |  |  |
| 13 | `FS.DIVIDEND.PAYMENT.TYPE.RESERVED1` | `FsDividendPaymentType_Reserved1` | TField |  |  |
| 14 | `FS.DIVIDEND.PAYMENT.TYPE.LOCAL.REF` | `FsDividendPaymentType_LocalRef` |  |  |  |
| 15 | `FS.DIVIDEND.PAYMENT.TYPE.OVERRIDE` | `FsDividendPaymentType_Override` |  |  |  |
| 16 | `FS.DIVIDEND.PAYMENT.TYPE.RECORD.STATUS` | `FsDividendPaymentType_RecordStatus` | String |  |  |
| 17 | `FS.DIVIDEND.PAYMENT.TYPE.CURR.NO` | `FsDividendPaymentType_CurrNo` | String |  |  |
| 18 | `FS.DIVIDEND.PAYMENT.TYPE.INPUTTER` | `FsDividendPaymentType_Inputter` |  |  |  |
| 19 | `FS.DIVIDEND.PAYMENT.TYPE.DATE.TIME` | `FsDividendPaymentType_DateTime` |  |  |  |
| 20 | `FS.DIVIDEND.PAYMENT.TYPE.AUTHORISER` | `FsDividendPaymentType_Authoriser` | String |  |  |
| 21 | `FS.DIVIDEND.PAYMENT.TYPE.CO.CODE` | `FsDividendPaymentType_CoCode` | String |  |  |
| 22 | `FS.DIVIDEND.PAYMENT.TYPE.DEPT.CODE` | `FsDividendPaymentType_DeptCode` | String |  |  |
| 23 | `FS.DIVIDEND.PAYMENT.TYPE.AUDITOR.CODE` | `FsDividendPaymentType_AuditorCode` | String |  |  |
| 24 | `FS.DIVIDEND.PAYMENT.TYPE.AUDIT.DATE.TIME` | `FsDividendPaymentType_AuditDateTime` | String |  |  |
