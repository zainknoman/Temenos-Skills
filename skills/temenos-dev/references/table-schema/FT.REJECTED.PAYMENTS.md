# FT.REJECTED.PAYMENTS — Table Schema

> Source: `INSERTS/I_F.FT.REJECTED.PAYMENTS` in `HKDDPR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FT.REJECT.PAY.TRANSACTION.TYPE` | `FtRejectedPayments_TransactionType` | TField |  | Should be a valid record from FT.TXN.TYPE.CONDITION Vetted to FT.TXN.TYPE.CONDITION |
| 2 | `FT.REJECT.PAY.TRANSACTION.ACCOUNT` | `FtRejectedPayments_TransactionAccount` | TField |  | The transaction account for FUNDS.TRANSFER |
| 3 | `FT.REJECT.PAY.TRANSACTION.CURRENCY` | `FtRejectedPayments_TransactionCurrency` | TField |  | Currency of the transaction Vetted to CURRENCY table |
| 4 | `FT.REJECT.PAY.TRANSACTION.AMOUNT` | `FtRejectedPayments_TransactionAmount` | TField |  | Transaction amount |
| 5 | `FT.REJECT.PAY.TRANSACTION.DATE` | `FtRejectedPayments_TransactionDate` | TField |  |  |
| 6 | `FT.REJECT.PAY.REJECT.REASON` | `FtRejectedPayments_RejectReason` | TField |  | Reason for which the transaction is rejected. |
| 7 | `FT.REJECT.PAY.STATUS` | `FtRejectedPayments_Status` | TField |  | This field will be updated by the interface whenever the outward field for HKICL has been generated for returns of INWARD DIRECT CREDIT.In case this field is blank, then it means that the file has not been generated for the day. Validation Rules: Allowed values defined in EB.LOOKUP&gt;FT.ORIGIN.STATUS*(VALUES) |
| 8 | `FT.REJECT.PAY.REASON.CODE` | `FtRejectedPayments_ReasonCode` | TField |  | The reason code for putting the transaction on hold. Reason code configured in EB.ERROR and override appication. Validation Rules: Vetted to EB.LOOKUP>HKDDPR.REASON.CODE*(Code) |
| 9 | `FT.REJECT.PAY.RESERVED.9` | `FtRejectedPayments_Reserved9` | TField |  |  |
| 10 | `FT.REJECT.PAY.RESERVED.8` | `FtRejectedPayments_Reserved8` | TField |  |  |
| 11 | `FT.REJECT.PAY.RESERVED.7` | `FtRejectedPayments_Reserved7` | TField |  |  |
| 12 | `FT.REJECT.PAY.RESERVED.6` | `FtRejectedPayments_Reserved6` | TField |  |  |
| 13 | `FT.REJECT.PAY.RESERVED.5` | `FtRejectedPayments_Reserved5` | TField |  |  |
| 14 | `FT.REJECT.PAY.RESERVED.4` | `FtRejectedPayments_Reserved4` | TField |  |  |
| 15 | `FT.REJECT.PAY.RESERVED.3` | `FtRejectedPayments_Reserved3` | TField |  |  |
| 16 | `FT.REJECT.PAY.RESERVED.2` | `FtRejectedPayments_Reserved2` | TField |  |  |
| 17 | `FT.REJECT.PAY.RESERVED.1` | `FtRejectedPayments_Reserved1` | TField |  |  |
| 18 | `FT.REJECT.PAY.LOCAL.REF` | `FtRejectedPayments_LocalRef` |  |  |  |
| 19 | `FT.REJECT.PAY.OVERRIDE` | `FtRejectedPayments_Override` |  |  |  |
| 20 | `FT.REJECT.PAY.RECORD.STATUS` | `FtRejectedPayments_RecordStatus` | String |  |  |
| 21 | `FT.REJECT.PAY.CURR.NO` | `FtRejectedPayments_CurrNo` | String |  |  |
| 22 | `FT.REJECT.PAY.INPUTTER` | `FtRejectedPayments_Inputter` |  |  |  |
| 23 | `FT.REJECT.PAY.DATE.TIME` | `FtRejectedPayments_DateTime` |  |  |  |
| 24 | `FT.REJECT.PAY.AUTHORISER` | `FtRejectedPayments_Authoriser` | String |  |  |
| 25 | `FT.REJECT.PAY.CO.CODE` | `FtRejectedPayments_CoCode` | String |  |  |
| 26 | `FT.REJECT.PAY.DEPT.CODE` | `FtRejectedPayments_DeptCode` | String |  |  |
| 27 | `FT.REJECT.PAY.AUDITOR.CODE` | `FtRejectedPayments_AuditorCode` | String |  |  |
| 28 | `FT.REJECT.PAY.AUDIT.DATE.TIME` | `FtRejectedPayments_AuditDateTime` | String |  |  |
