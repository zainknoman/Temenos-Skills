# FS.GA.UDF.OPTION.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.UDF.OPTION.TRANSACTION` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.UDF.OPTION.TRANSACTION.FUND.ID` | `FsGaUdfOptionTransaction_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.UDF.OPTION.TRANSACTION.USER.DEFINABLE.FIELDS.GROUP` | `FsGaUdfOptionTransaction_UserDefinableFieldsGroup` | TField |  | User definable Fields group code Multifonds DB Column is GRP_CODE. |
| 3 | `FS.GA.UDF.OPTION.TRANSACTION.UDF.CODE` | `FsGaUdfOptionTransaction_UdfCode` | TField |  | Udf code Multifonds DB Column is UDF_CODE. |
| 4 | `FS.GA.UDF.OPTION.TRANSACTION.OPTION.ID` | `FsGaUdfOptionTransaction_OptionId` | TField |  | Option Security ID Multifonds DB Column is NOPT. |
| 5 | `FS.GA.UDF.OPTION.TRANSACTION.TRANSACTION.NUMBER` | `FsGaUdfOptionTransaction_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 6 | `FS.GA.UDF.OPTION.TRANSACTION.EXTERNAL.REFERENCE` | `FsGaUdfOptionTransaction_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 7 | `FS.GA.UDF.OPTION.TRANSACTION.LOT.NUMBER` | `FsGaUdfOptionTransaction_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 8 | `FS.GA.UDF.OPTION.TRANSACTION.MANDATORY.OR.OPTIONAL` | `FsGaUdfOptionTransaction_MandatoryOrOptional` | TField | Conditional | User can input either M (Mandatory) or O (optional) Multifonds DB Column is MANDAT_OPT. |
| 9 | `FS.GA.UDF.OPTION.TRANSACTION.SHORT.CODE` | `FsGaUdfOptionTransaction_ShortCode` | TField |  | Short code in UDF screen Multifonds DB Column is SHORT_CODE. |
| 10 | `FS.GA.UDF.OPTION.TRANSACTION.LONGDESCRIPTION` | `FsGaUdfOptionTransaction_Longdescription` | TField |  | Detailed description Multifonds DB Column is LONG_DESC. |
| 11 | `FS.GA.UDF.OPTION.TRANSACTION.SESSION.NUMBER` | `FsGaUdfOptionTransaction_SessionNumber` | TField |  | Session Number Multifonds DB Column is NO_SESSION. |
| 12 | `FS.GA.UDF.OPTION.TRANSACTION.RESERVED10` | `FsGaUdfOptionTransaction_Reserved10` | TField |  |  |
| 13 | `FS.GA.UDF.OPTION.TRANSACTION.RESERVED9` | `FsGaUdfOptionTransaction_Reserved9` | TField |  |  |
| 14 | `FS.GA.UDF.OPTION.TRANSACTION.RESERVED8` | `FsGaUdfOptionTransaction_Reserved8` | TField |  |  |
| 15 | `FS.GA.UDF.OPTION.TRANSACTION.RESERVED7` | `FsGaUdfOptionTransaction_Reserved7` | TField |  |  |
| 16 | `FS.GA.UDF.OPTION.TRANSACTION.RESERVED6` | `FsGaUdfOptionTransaction_Reserved6` | TField |  |  |
| 17 | `FS.GA.UDF.OPTION.TRANSACTION.RESERVED5` | `FsGaUdfOptionTransaction_Reserved5` | TField |  |  |
| 18 | `FS.GA.UDF.OPTION.TRANSACTION.RESERVED4` | `FsGaUdfOptionTransaction_Reserved4` | TField |  |  |
| 19 | `FS.GA.UDF.OPTION.TRANSACTION.RESERVED3` | `FsGaUdfOptionTransaction_Reserved3` | TField |  |  |
| 20 | `FS.GA.UDF.OPTION.TRANSACTION.RESERVED2` | `FsGaUdfOptionTransaction_Reserved2` | TField |  |  |
| 21 | `FS.GA.UDF.OPTION.TRANSACTION.RESERVED1` | `FsGaUdfOptionTransaction_Reserved1` | TField |  |  |
| 22 | `FS.GA.UDF.OPTION.TRANSACTION.RECORD.STATUS` | `FsGaUdfOptionTransaction_RecordStatus` | String |  |  |
| 23 | `FS.GA.UDF.OPTION.TRANSACTION.CURR.NO` | `FsGaUdfOptionTransaction_CurrNo` | String |  |  |
| 24 | `FS.GA.UDF.OPTION.TRANSACTION.INPUTTER` | `FsGaUdfOptionTransaction_Inputter` |  |  |  |
| 25 | `FS.GA.UDF.OPTION.TRANSACTION.DATE.TIME` | `FsGaUdfOptionTransaction_DateTime` |  |  |  |
| 26 | `FS.GA.UDF.OPTION.TRANSACTION.AUTHORISER` | `FsGaUdfOptionTransaction_Authoriser` | String |  |  |
| 27 | `FS.GA.UDF.OPTION.TRANSACTION.CO.CODE` | `FsGaUdfOptionTransaction_CoCode` | String |  |  |
| 28 | `FS.GA.UDF.OPTION.TRANSACTION.DEPT.CODE` | `FsGaUdfOptionTransaction_DeptCode` | String |  |  |
| 29 | `FS.GA.UDF.OPTION.TRANSACTION.AUDITOR.CODE` | `FsGaUdfOptionTransaction_AuditorCode` | String |  |  |
| 30 | `FS.GA.UDF.OPTION.TRANSACTION.AUDIT.DATE.TIME` | `FsGaUdfOptionTransaction_AuditDateTime` | String |  |  |
