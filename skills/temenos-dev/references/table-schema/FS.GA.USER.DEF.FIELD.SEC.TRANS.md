# FS.GA.USER.DEF.FIELD.SEC.TRANS — Table Schema

> Source: `INSERTS/I_F.FS.GA.USER.DEF.FIELD.SEC.TRANS` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.FUND.ID` | `FsGaUserDefFieldSecTrans_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.USER.DEFINABLE.FIELDS.GROUP` | `FsGaUserDefFieldSecTrans_UserDefinableFieldsGroup` | TField |  | User definable Fields group code Multifonds DB Column is GRP_CODE. |
| 3 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.UDF.CODE` | `FsGaUserDefFieldSecTrans_UdfCode` | TField |  | Udf code Multifonds DB Column is UDF_CODE. |
| 4 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.INTERNAL.SECURITY.ID` | `FsGaUserDefFieldSecTrans_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 5 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.TRANSACTION.NUMBER` | `FsGaUserDefFieldSecTrans_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 6 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.EXTERNAL.REFERENCE` | `FsGaUserDefFieldSecTrans_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 7 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.LOT.NUMBER` | `FsGaUserDefFieldSecTrans_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 8 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.MANDATORY.OR.OPTIONAL` | `FsGaUserDefFieldSecTrans_MandatoryOrOptional` | TField | Conditional | User can input either M (Mandatory) or O (optional) Multifonds DB Column is MANDAT_OPT. |
| 9 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.SHORT.CODE` | `FsGaUserDefFieldSecTrans_ShortCode` | TField |  | Short code in UDF screen Multifonds DB Column is SHORT_CODE. |
| 10 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.LONGDESCRIPTION` | `FsGaUserDefFieldSecTrans_Longdescription` | TField |  | Detailed description Multifonds DB Column is LONG_DESC. |
| 11 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.SESSION.NUMBER` | `FsGaUserDefFieldSecTrans_SessionNumber` | TField |  | Session Number Multifonds DB Column is NO_SESSION. |
| 12 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.SERVICE.CODE` | `FsGaUserDefFieldSecTrans_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 13 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.RESERVED10` | `FsGaUserDefFieldSecTrans_Reserved10` | TField |  |  |
| 14 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.RESERVED9` | `FsGaUserDefFieldSecTrans_Reserved9` | TField |  |  |
| 15 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.RESERVED8` | `FsGaUserDefFieldSecTrans_Reserved8` | TField |  |  |
| 16 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.RESERVED7` | `FsGaUserDefFieldSecTrans_Reserved7` | TField |  |  |
| 17 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.RESERVED6` | `FsGaUserDefFieldSecTrans_Reserved6` | TField |  |  |
| 18 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.RESERVED5` | `FsGaUserDefFieldSecTrans_Reserved5` | TField |  |  |
| 19 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.RESERVED4` | `FsGaUserDefFieldSecTrans_Reserved4` | TField |  |  |
| 20 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.RESERVED3` | `FsGaUserDefFieldSecTrans_Reserved3` | TField |  |  |
| 21 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.RESERVED2` | `FsGaUserDefFieldSecTrans_Reserved2` | TField |  |  |
| 22 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.RESERVED1` | `FsGaUserDefFieldSecTrans_Reserved1` | TField |  |  |
| 23 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.RECORD.STATUS` | `FsGaUserDefFieldSecTrans_RecordStatus` | String |  |  |
| 24 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.CURR.NO` | `FsGaUserDefFieldSecTrans_CurrNo` | String |  |  |
| 25 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.INPUTTER` | `FsGaUserDefFieldSecTrans_Inputter` |  |  |  |
| 26 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.DATE.TIME` | `FsGaUserDefFieldSecTrans_DateTime` |  |  |  |
| 27 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.AUTHORISER` | `FsGaUserDefFieldSecTrans_Authoriser` | String |  |  |
| 28 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.CO.CODE` | `FsGaUserDefFieldSecTrans_CoCode` | String |  |  |
| 29 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.DEPT.CODE` | `FsGaUserDefFieldSecTrans_DeptCode` | String |  |  |
| 30 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.AUDITOR.CODE` | `FsGaUserDefFieldSecTrans_AuditorCode` | String |  |  |
| 31 | `FS.GA.USER.DEF.FIELD.SEC.TRANS.AUDIT.DATE.TIME` | `FsGaUserDefFieldSecTrans_AuditDateTime` | String |  |  |
