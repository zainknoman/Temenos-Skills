# FS.PAYMENT.FREQUENCY — Table Schema

> Source: `INSERTS/I_F.FS.PAYMENT.FREQUENCY` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.PAYMENT.FREQUENCY.DESCRIPTION` | `FsPaymentFrequency_Description` |  |  |  |
| 2 | `FS.PAYMENT.FREQUENCY.FILTER.KEY` | `FsPaymentFrequency_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.PAYMENT.FREQUENCY.RECORD.ID` | `FsPaymentFrequency_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.PAYMENT.FREQUENCY.RESERVED10` | `FsPaymentFrequency_Reserved10` | TField |  |  |
| 5 | `FS.PAYMENT.FREQUENCY.RESERVED9` | `FsPaymentFrequency_Reserved9` | TField |  |  |
| 6 | `FS.PAYMENT.FREQUENCY.RESERVED8` | `FsPaymentFrequency_Reserved8` | TField |  |  |
| 7 | `FS.PAYMENT.FREQUENCY.RESERVED7` | `FsPaymentFrequency_Reserved7` | TField |  |  |
| 8 | `FS.PAYMENT.FREQUENCY.RESERVED6` | `FsPaymentFrequency_Reserved6` | TField |  |  |
| 9 | `FS.PAYMENT.FREQUENCY.RESERVED5` | `FsPaymentFrequency_Reserved5` | TField |  |  |
| 10 | `FS.PAYMENT.FREQUENCY.RESERVED4` | `FsPaymentFrequency_Reserved4` | TField |  |  |
| 11 | `FS.PAYMENT.FREQUENCY.RESERVED3` | `FsPaymentFrequency_Reserved3` | TField |  |  |
| 12 | `FS.PAYMENT.FREQUENCY.RESERVED2` | `FsPaymentFrequency_Reserved2` | TField |  |  |
| 13 | `FS.PAYMENT.FREQUENCY.RESERVED1` | `FsPaymentFrequency_Reserved1` | TField |  |  |
| 14 | `FS.PAYMENT.FREQUENCY.LOCAL.REF` | `FsPaymentFrequency_LocalRef` |  |  |  |
| 15 | `FS.PAYMENT.FREQUENCY.OVERRIDE` | `FsPaymentFrequency_Override` |  |  |  |
| 16 | `FS.PAYMENT.FREQUENCY.RECORD.STATUS` | `FsPaymentFrequency_RecordStatus` | String |  |  |
| 17 | `FS.PAYMENT.FREQUENCY.CURR.NO` | `FsPaymentFrequency_CurrNo` | String |  |  |
| 18 | `FS.PAYMENT.FREQUENCY.INPUTTER` | `FsPaymentFrequency_Inputter` |  |  |  |
| 19 | `FS.PAYMENT.FREQUENCY.DATE.TIME` | `FsPaymentFrequency_DateTime` |  |  |  |
| 20 | `FS.PAYMENT.FREQUENCY.AUTHORISER` | `FsPaymentFrequency_Authoriser` | String |  |  |
| 21 | `FS.PAYMENT.FREQUENCY.CO.CODE` | `FsPaymentFrequency_CoCode` | String |  |  |
| 22 | `FS.PAYMENT.FREQUENCY.DEPT.CODE` | `FsPaymentFrequency_DeptCode` | String |  |  |
| 23 | `FS.PAYMENT.FREQUENCY.AUDITOR.CODE` | `FsPaymentFrequency_AuditorCode` | String |  |  |
| 24 | `FS.PAYMENT.FREQUENCY.AUDIT.DATE.TIME` | `FsPaymentFrequency_AuditDateTime` | String |  |  |
