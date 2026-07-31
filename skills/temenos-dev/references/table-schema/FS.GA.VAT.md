# FS.GA.VAT — Table Schema

> Source: `INSERTS/I_F.FS.GA.VAT` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.VAT.VALUE.ADDED.TAX.CODE` | `FsGaVat_ValueAddedTaxCode` |  |  |  |
| 2 | `FS.GA.VAT.VAT.PERCENTAGE` | `FsGaVat_VatPercentage` |  |  |  |
| 3 | `FS.GA.VAT.OPERATION.CODE` | `FsGaVat_TransactionType` |  |  |  |
| 4 | `FS.GA.VAT.TRANSACTION.FEES.CODE` | `FsGaVat_TransactionFeesCode` |  |  |  |
| 5 | `FS.GA.VAT.EFFECTIVE.DATE` | `FsGaVat_EffectiveDate` |  |  |  |
| 6 | `FS.GA.VAT.SETTLE.SEPARATELY` | `FsGaVat_SettleSeparately` |  |  |  |
| 7 | `FS.GA.VAT.RESERVED10` | `FsGaVat_Reserved10` |  |  |  |
| 8 | `FS.GA.VAT.RESERVED9` | `FsGaVat_Reserved9` |  |  |  |
| 9 | `FS.GA.VAT.RESERVED8` | `FsGaVat_Reserved8` |  |  |  |
| 10 | `FS.GA.VAT.RESERVED7` | `FsGaVat_Reserved7` |  |  |  |
| 11 | `FS.GA.VAT.RESERVED6` | `FsGaVat_Reserved6` |  |  |  |
| 12 | `FS.GA.VAT.RESERVED5` | `FsGaVat_Reserved5` |  |  |  |
| 13 | `FS.GA.VAT.RESERVED4` | `FsGaVat_Reserved4` |  |  |  |
| 14 | `FS.GA.VAT.RESERVED3` | `FsGaVat_Reserved3` |  |  |  |
| 15 | `FS.GA.VAT.RESERVED2` | `FsGaVat_Reserved2` |  |  |  |
| 16 | `FS.GA.VAT.RESERVED1` | `FsGaVat_Reserved1` |  |  |  |
| 17 | `FS.GA.VAT.RECORD.STATUS` | `FsGaVat_RecordStatus` |  |  |  |
| 18 | `FS.GA.VAT.CURR.NO` | `FsGaVat_CurrNo` |  |  |  |
| 19 | `FS.GA.VAT.INPUTTER` | `FsGaVat_Inputter` |  |  |  |
| 20 | `FS.GA.VAT.DATE.TIME` | `FsGaVat_DateTime` |  |  |  |
| 21 | `FS.GA.VAT.AUTHORISER` | `FsGaVat_Authoriser` |  |  |  |
| 22 | `FS.GA.VAT.CO.CODE` | `FsGaVat_CoCode` |  |  |  |
| 23 | `FS.GA.VAT.DEPT.CODE` | `FsGaVat_DeptCode` |  |  |  |
| 24 | `FS.GA.VAT.AUDITOR.CODE` | `FsGaVat_AuditorCode` |  |  |  |
| 25 | `FS.GA.VAT.AUDIT.DATE.TIME` | `FsGaVat_AuditDateTime` |  |  |  |
