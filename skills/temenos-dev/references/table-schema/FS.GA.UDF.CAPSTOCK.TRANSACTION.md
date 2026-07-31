# FS.GA.UDF.CAPSTOCK.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.UDF.CAPSTOCK.TRANSACTION` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.FUND.ID` | `FsGaUdfCapstockTransaction_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.USER.DEFINABLE.FIELDS.GROUP` | `FsGaUdfCapstockTransaction_UserDefinableFieldsGroup` | TField |  | User definable Fields group code Multifonds DB Column is GRP_CODE. |
| 3 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.UDF.CODE` | `FsGaUdfCapstockTransaction_UdfCode` | TField |  | Udf code Multifonds DB Column is UDF_CODE. |
| 4 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.SHARE.CLASS.CODE` | `FsGaUdfCapstockTransaction_ShareClassCode` | TField |  | Share class Multifonds DB Column is TPARTS. |
| 5 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.TRANSACTION.NUMBER` | `FsGaUdfCapstockTransaction_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 6 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.EXTERNAL.REFERENCE` | `FsGaUdfCapstockTransaction_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 7 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.MANDATORY.OR.OPTIONAL` | `FsGaUdfCapstockTransaction_MandatoryOrOptional` | TField | Conditional | User can input either M (Mandatory) or O (optional) Multifonds DB Column is MANDAT_OPT. |
| 8 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.SHORT.CODE` | `FsGaUdfCapstockTransaction_ShortCode` | TField |  | Short code in UDF screen Multifonds DB Column is SHORT_CODE. |
| 9 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.LONGDESCRIPTION` | `FsGaUdfCapstockTransaction_Longdescription` | TField |  | Detailed description Multifonds DB Column is LONG_DESC. |
| 10 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.SESSION.NUMBER` | `FsGaUdfCapstockTransaction_SessionNumber` | TField |  | Session Number Multifonds DB Column is NO_SESSION. |
| 11 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.RESERVED10` | `FsGaUdfCapstockTransaction_Reserved10` | TField |  |  |
| 12 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.RESERVED9` | `FsGaUdfCapstockTransaction_Reserved9` | TField |  |  |
| 13 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.RESERVED8` | `FsGaUdfCapstockTransaction_Reserved8` | TField |  |  |
| 14 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.RESERVED7` | `FsGaUdfCapstockTransaction_Reserved7` | TField |  |  |
| 15 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.RESERVED6` | `FsGaUdfCapstockTransaction_Reserved6` | TField |  |  |
| 16 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.RESERVED5` | `FsGaUdfCapstockTransaction_Reserved5` | TField |  |  |
| 17 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.RESERVED4` | `FsGaUdfCapstockTransaction_Reserved4` | TField |  |  |
| 18 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.RESERVED3` | `FsGaUdfCapstockTransaction_Reserved3` | TField |  |  |
| 19 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.RESERVED2` | `FsGaUdfCapstockTransaction_Reserved2` | TField |  |  |
| 20 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.RESERVED1` | `FsGaUdfCapstockTransaction_Reserved1` | TField |  |  |
| 21 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.RECORD.STATUS` | `FsGaUdfCapstockTransaction_RecordStatus` | String |  |  |
| 22 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.CURR.NO` | `FsGaUdfCapstockTransaction_CurrNo` | String |  |  |
| 23 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.INPUTTER` | `FsGaUdfCapstockTransaction_Inputter` |  |  |  |
| 24 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.DATE.TIME` | `FsGaUdfCapstockTransaction_DateTime` |  |  |  |
| 25 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.AUTHORISER` | `FsGaUdfCapstockTransaction_Authoriser` | String |  |  |
| 26 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.CO.CODE` | `FsGaUdfCapstockTransaction_CoCode` | String |  |  |
| 27 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.DEPT.CODE` | `FsGaUdfCapstockTransaction_DeptCode` | String |  |  |
| 28 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.AUDITOR.CODE` | `FsGaUdfCapstockTransaction_AuditorCode` | String |  |  |
| 29 | `FS.GA.UDF.CAPSTOCK.TRANSACTION.AUDIT.DATE.TIME` | `FsGaUdfCapstockTransaction_AuditDateTime` | String |  |  |
