# FS.GI.APP.MIN.DIV.PAYMENT — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.MIN.DIV.PAYMENT` in `FS_InvestorAccountStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.MIN.DIV.PAYMENT.PARENT.REF.ID` | `FsGiAppMinDivPayment_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.MIN.DIV.PAYMENT.ORA.ROWID` | `FsGiAppMinDivPayment_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.MIN.DIV.PAYMENT.PARENT.ID.TYPE` | `FsGiAppMinDivPayment_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.APP.MIN.DIV.PAYMENT.PARENT.ID` | `FsGiAppMinDivPayment_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.APP.MIN.DIV.PAYMENT.LEGAL.ENTITY.ID` | `FsGiAppMinDivPayment_LegalEntityId` | TField |  | Legal Entity internal identifier. Multifonds DB Column is NTFC. |
| 6 | `FS.GI.APP.MIN.DIV.PAYMENT.TA.FUND.ID` | `FsGiAppMinDivPayment_TaFundId` | TField |  | Fund internal identifier. Multifonds DB Column is NPTF. |
| 7 | `FS.GI.APP.MIN.DIV.PAYMENT.SHARE.CLASS.CODE` | `FsGiAppMinDivPayment_ShareClassCode` | TField |  | Fund share class internal identifier. Multifonds DB Column is TPART. |
| 8 | `FS.GI.APP.MIN.DIV.PAYMENT.COUNTRY` | `FsGiAppMinDivPayment_Country` | TField |  | The Country code (in 2 letter format eg: LU). Multifonds DB Column is CPAYS. |
| 9 | `FS.GI.APP.MIN.DIV.PAYMENT.MINIMUM.PAYMENT.AMOUNT` | `FsGiAppMinDivPayment_MinimumPaymentAmount` | TField |  | The minimum dividend amount that needs to be considered for payout Multifonds DB Column is PAYMENT_AMT. |
| 10 | `FS.GI.APP.MIN.DIV.PAYMENT.PAYMENT.CURRENCY` | `FsGiAppMinDivPayment_PaymentCurrency` | TField |  | The currency code(in 3 letter format eg: EUR) of the minimum dividend payment amount. Multifonds DB Column is CMON. |
| 11 | `FS.GI.APP.MIN.DIV.PAYMENT.MIN.DIV.PAY.ID` | `FsGiAppMinDivPayment_MinDivPayId` | TField |  | Unique internal minimum dividend payment identifier. Multifonds DB Column is INTERNAL_ID. |
| 12 | `FS.GI.APP.MIN.DIV.PAYMENT.FUND.ID` | `FsGiAppMinDivPayment_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 13 | `FS.GI.APP.MIN.DIV.PAYMENT.CLASS.CURRENCY` | `FsGiAppMinDivPayment_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 14 | `FS.GI.APP.MIN.DIV.PAYMENT.RESERVED10` | `FsGiAppMinDivPayment_Reserved10` | TField |  |  |
| 15 | `FS.GI.APP.MIN.DIV.PAYMENT.RESERVED9` | `FsGiAppMinDivPayment_Reserved9` | TField |  |  |
| 16 | `FS.GI.APP.MIN.DIV.PAYMENT.RESERVED8` | `FsGiAppMinDivPayment_Reserved8` | TField |  |  |
| 17 | `FS.GI.APP.MIN.DIV.PAYMENT.RESERVED7` | `FsGiAppMinDivPayment_Reserved7` | TField |  |  |
| 18 | `FS.GI.APP.MIN.DIV.PAYMENT.RESERVED6` | `FsGiAppMinDivPayment_Reserved6` | TField |  |  |
| 19 | `FS.GI.APP.MIN.DIV.PAYMENT.RESERVED5` | `FsGiAppMinDivPayment_Reserved5` | TField |  |  |
| 20 | `FS.GI.APP.MIN.DIV.PAYMENT.RESERVED4` | `FsGiAppMinDivPayment_Reserved4` | TField |  |  |
| 21 | `FS.GI.APP.MIN.DIV.PAYMENT.RESERVED3` | `FsGiAppMinDivPayment_Reserved3` | TField |  |  |
| 22 | `FS.GI.APP.MIN.DIV.PAYMENT.RESERVED2` | `FsGiAppMinDivPayment_Reserved2` | TField |  |  |
| 23 | `FS.GI.APP.MIN.DIV.PAYMENT.RESERVED1` | `FsGiAppMinDivPayment_Reserved1` | TField |  |  |
| 24 | `FS.GI.APP.MIN.DIV.PAYMENT.LOCAL.REF` | `FsGiAppMinDivPayment_LocalRef` |  |  |  |
| 25 | `FS.GI.APP.MIN.DIV.PAYMENT.OVERRIDE` | `FsGiAppMinDivPayment_Override` |  |  |  |
| 26 | `FS.GI.APP.MIN.DIV.PAYMENT.RECORD.STATUS` | `FsGiAppMinDivPayment_RecordStatus` | String |  |  |
| 27 | `FS.GI.APP.MIN.DIV.PAYMENT.CURR.NO` | `FsGiAppMinDivPayment_CurrNo` | String |  |  |
| 28 | `FS.GI.APP.MIN.DIV.PAYMENT.INPUTTER` | `FsGiAppMinDivPayment_Inputter` |  |  |  |
| 29 | `FS.GI.APP.MIN.DIV.PAYMENT.DATE.TIME` | `FsGiAppMinDivPayment_DateTime` |  |  |  |
| 30 | `FS.GI.APP.MIN.DIV.PAYMENT.AUTHORISER` | `FsGiAppMinDivPayment_Authoriser` | String |  |  |
| 31 | `FS.GI.APP.MIN.DIV.PAYMENT.CO.CODE` | `FsGiAppMinDivPayment_CoCode` | String |  |  |
| 32 | `FS.GI.APP.MIN.DIV.PAYMENT.DEPT.CODE` | `FsGiAppMinDivPayment_DeptCode` | String |  |  |
| 33 | `FS.GI.APP.MIN.DIV.PAYMENT.AUDITOR.CODE` | `FsGiAppMinDivPayment_AuditorCode` | String |  |  |
| 34 | `FS.GI.APP.MIN.DIV.PAYMENT.AUDIT.DATE.TIME` | `FsGiAppMinDivPayment_AuditDateTime` | String |  |  |
