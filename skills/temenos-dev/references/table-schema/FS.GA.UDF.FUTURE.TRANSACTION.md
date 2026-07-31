# FS.GA.UDF.FUTURE.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.UDF.FUTURE.TRANSACTION` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.UDF.FUTURE.TRANSACTION.FUND.ID` | `FsGaUdfFutureTransaction_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.UDF.FUTURE.TRANSACTION.USER.DEFINABLE.FIELDS.GROUP` | `FsGaUdfFutureTransaction_UserDefinableFieldsGroup` | TField |  | User definable Fields group code Multifonds DB Column is GRP_CODE. |
| 3 | `FS.GA.UDF.FUTURE.TRANSACTION.UDF.CODE` | `FsGaUdfFutureTransaction_UdfCode` | TField |  | Udf code Multifonds DB Column is UDF_CODE. |
| 4 | `FS.GA.UDF.FUTURE.TRANSACTION.FUTURE.ID.CODE` | `FsGaUdfFutureTransaction_FutureIdCode` | TField |  | Future, Security,Swap,Derivative,CFD ID Code Multifonds DB Column is NFUT. |
| 5 | `FS.GA.UDF.FUTURE.TRANSACTION.TRANSACTION.NUMBER` | `FsGaUdfFutureTransaction_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 6 | `FS.GA.UDF.FUTURE.TRANSACTION.EXTERNAL.REFERENCE` | `FsGaUdfFutureTransaction_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 7 | `FS.GA.UDF.FUTURE.TRANSACTION.LOT.NUMBER` | `FsGaUdfFutureTransaction_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 8 | `FS.GA.UDF.FUTURE.TRANSACTION.MANDATORY.OR.OPTIONAL` | `FsGaUdfFutureTransaction_MandatoryOrOptional` | TField | Conditional | User can input either M (Mandatory) or O (optional) Multifonds DB Column is MANDAT_OPT. |
| 9 | `FS.GA.UDF.FUTURE.TRANSACTION.SHORT.CODE` | `FsGaUdfFutureTransaction_ShortCode` | TField |  | Short code in UDF screen Multifonds DB Column is SHORT_CODE. |
| 10 | `FS.GA.UDF.FUTURE.TRANSACTION.LONGDESCRIPTION` | `FsGaUdfFutureTransaction_Longdescription` | TField |  | Detailed description Multifonds DB Column is LONG_DESC. |
| 11 | `FS.GA.UDF.FUTURE.TRANSACTION.SESSION.NUMBER` | `FsGaUdfFutureTransaction_SessionNumber` | TField |  | Session Number Multifonds DB Column is NO_SESSION. |
| 12 | `FS.GA.UDF.FUTURE.TRANSACTION.RESERVED10` | `FsGaUdfFutureTransaction_Reserved10` | TField |  |  |
| 13 | `FS.GA.UDF.FUTURE.TRANSACTION.RESERVED9` | `FsGaUdfFutureTransaction_Reserved9` | TField |  |  |
| 14 | `FS.GA.UDF.FUTURE.TRANSACTION.RESERVED8` | `FsGaUdfFutureTransaction_Reserved8` | TField |  |  |
| 15 | `FS.GA.UDF.FUTURE.TRANSACTION.RESERVED7` | `FsGaUdfFutureTransaction_Reserved7` | TField |  |  |
| 16 | `FS.GA.UDF.FUTURE.TRANSACTION.RESERVED6` | `FsGaUdfFutureTransaction_Reserved6` | TField |  |  |
| 17 | `FS.GA.UDF.FUTURE.TRANSACTION.RESERVED5` | `FsGaUdfFutureTransaction_Reserved5` | TField |  |  |
| 18 | `FS.GA.UDF.FUTURE.TRANSACTION.RESERVED4` | `FsGaUdfFutureTransaction_Reserved4` | TField |  |  |
| 19 | `FS.GA.UDF.FUTURE.TRANSACTION.RESERVED3` | `FsGaUdfFutureTransaction_Reserved3` | TField |  |  |
| 20 | `FS.GA.UDF.FUTURE.TRANSACTION.RESERVED2` | `FsGaUdfFutureTransaction_Reserved2` | TField |  |  |
| 21 | `FS.GA.UDF.FUTURE.TRANSACTION.RESERVED1` | `FsGaUdfFutureTransaction_Reserved1` | TField |  |  |
| 22 | `FS.GA.UDF.FUTURE.TRANSACTION.RECORD.STATUS` | `FsGaUdfFutureTransaction_RecordStatus` | String |  |  |
| 23 | `FS.GA.UDF.FUTURE.TRANSACTION.CURR.NO` | `FsGaUdfFutureTransaction_CurrNo` | String |  |  |
| 24 | `FS.GA.UDF.FUTURE.TRANSACTION.INPUTTER` | `FsGaUdfFutureTransaction_Inputter` |  |  |  |
| 25 | `FS.GA.UDF.FUTURE.TRANSACTION.DATE.TIME` | `FsGaUdfFutureTransaction_DateTime` |  |  |  |
| 26 | `FS.GA.UDF.FUTURE.TRANSACTION.AUTHORISER` | `FsGaUdfFutureTransaction_Authoriser` | String |  |  |
| 27 | `FS.GA.UDF.FUTURE.TRANSACTION.CO.CODE` | `FsGaUdfFutureTransaction_CoCode` | String |  |  |
| 28 | `FS.GA.UDF.FUTURE.TRANSACTION.DEPT.CODE` | `FsGaUdfFutureTransaction_DeptCode` | String |  |  |
| 29 | `FS.GA.UDF.FUTURE.TRANSACTION.AUDITOR.CODE` | `FsGaUdfFutureTransaction_AuditorCode` | String |  |  |
| 30 | `FS.GA.UDF.FUTURE.TRANSACTION.AUDIT.DATE.TIME` | `FsGaUdfFutureTransaction_AuditDateTime` | String |  |  |
