# FS.GI.FUND.MIN.DIVIDEND.PAYMENT — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.MIN.DIVIDEND.PAYMENT` in `FS_Dealing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.PARENT.REF.ID` | `FsGiFundMinDividendPayment_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.ORA.ROWID` | `FsGiFundMinDividendPayment_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.TA.FUND.ID` | `FsGiFundMinDividendPayment_TaFundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.CURRENCY` | `FsGiFundMinDividendPayment_Currency` | TField |  | Currency code(in 3 letter format eg: EUR) of the fund. Multifonds DB Column is CMON. |
| 5 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.SHARE.CLASS.CODE` | `FsGiFundMinDividendPayment_ShareClassCode` | TField |  | Fund share class. Multifonds DB Column is TPART. |
| 6 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.COUNTRY` | `FsGiFundMinDividendPayment_Country` | TField |  | Country code (in 2 letter format eg: LU). Multifonds DB Column is CPAYS. |
| 7 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.MIN.DIVIDEND.AMOUNT` | `FsGiFundMinDividendPayment_MinDividendAmount` | TField |  | Minimum dividend amount in selected currency. Multifonds DB Column is MNT_MIN. |
| 8 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.INTERNAL.ID` | `FsGiFundMinDividendPayment_InternalId` | TField |  | Unique internal identifier for the record. Multifonds DB Column is INTERNAL_ID. |
| 9 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.FUND.ID` | `FsGiFundMinDividendPayment_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 10 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.CLASS.CURRENCY` | `FsGiFundMinDividendPayment_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 11 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.RESERVED10` | `FsGiFundMinDividendPayment_Reserved10` | TField |  |  |
| 12 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.RESERVED9` | `FsGiFundMinDividendPayment_Reserved9` | TField |  |  |
| 13 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.RESERVED8` | `FsGiFundMinDividendPayment_Reserved8` | TField |  |  |
| 14 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.RESERVED7` | `FsGiFundMinDividendPayment_Reserved7` | TField |  |  |
| 15 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.RESERVED6` | `FsGiFundMinDividendPayment_Reserved6` | TField |  |  |
| 16 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.RESERVED5` | `FsGiFundMinDividendPayment_Reserved5` | TField |  |  |
| 17 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.RESERVED4` | `FsGiFundMinDividendPayment_Reserved4` | TField |  |  |
| 18 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.RESERVED3` | `FsGiFundMinDividendPayment_Reserved3` | TField |  |  |
| 19 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.RESERVED2` | `FsGiFundMinDividendPayment_Reserved2` | TField |  |  |
| 20 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.RESERVED1` | `FsGiFundMinDividendPayment_Reserved1` | TField |  |  |
| 21 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.LOCAL.REF` | `FsGiFundMinDividendPayment_LocalRef` |  |  |  |
| 22 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.OVERRIDE` | `FsGiFundMinDividendPayment_Override` |  |  |  |
| 23 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.RECORD.STATUS` | `FsGiFundMinDividendPayment_RecordStatus` | String |  |  |
| 24 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.CURR.NO` | `FsGiFundMinDividendPayment_CurrNo` | String |  |  |
| 25 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.INPUTTER` | `FsGiFundMinDividendPayment_Inputter` |  |  |  |
| 26 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.DATE.TIME` | `FsGiFundMinDividendPayment_DateTime` |  |  |  |
| 27 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.AUTHORISER` | `FsGiFundMinDividendPayment_Authoriser` | String |  |  |
| 28 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.CO.CODE` | `FsGiFundMinDividendPayment_CoCode` | String |  |  |
| 29 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.DEPT.CODE` | `FsGiFundMinDividendPayment_DeptCode` | String |  |  |
| 30 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.AUDITOR.CODE` | `FsGiFundMinDividendPayment_AuditorCode` | String |  |  |
| 31 | `FS.GI.FUND.MIN.DIVIDEND.PAYMENT.AUDIT.DATE.TIME` | `FsGiFundMinDividendPayment_AuditDateTime` | String |  |  |
