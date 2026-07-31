# CNCUST.H.SAFE.BOP — Table Schema

> Source: `INSERTS/I_F.CNCUST.H.SAFE.BOP` in `CNCUST_SafeDeclaration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CNCUST.SAFE.QFII.IND` | `CncustHSafeBop_QfiiInd` | TField |  | This field stores the qualified institutional investor indicator |
| 2 | `CNCUST.SAFE.QFII.TYPE` | `CncustHSafeBop_QfiiType` | TField |  | This field stores the qualified institutional investor type |
| 3 | `CNCUST.SAFE.ACCT.TYPE` | `CncustHSafeBop_AcctType` | TField |  | This field stores the SAFE account type |
| 4 | `CNCUST.SAFE.LIMIT.TYPE` | `CncustHSafeBop_LimitType` | TField |  | This field stores the limit type |
| 5 | `CNCUST.SAFE.LIMIT.AMT` | `CncustHSafeBop_LimitAmt` | TField |  | This field stores the limit amount |
| 6 | `CNCUST.SAFE.APPROVAL.NO` | `CncustHSafeBop_ApprovalNo` | TField |  | This field stores the approval nummber |
| 7 | `CNCUST.SAFE.BOP.TXN.CODE` | `CncustHSafeBop_BopTxnCode` |  |  |  |
| 8 | `CNCUST.SAFE.BOP.TXN.AMT` | `CncustHSafeBop_BopTxnAmt` |  |  |  |
| 9 | `CNCUST.SAFE.BOP.TXN.REMARK` | `CncustHSafeBop_BopTxnRemark` |  |  |  |
| 10 | `CNCUST.SAFE.FX.PUR.CODE` | `CncustHSafeBop_FxPurCode` | TField |  | This field stores the foreign exchange purpose code |
| 11 | `CNCUST.SAFE.FX.PURPOSE` | `CncustHSafeBop_FxPurpose` | TField |  | This field stores the foreign exchange purpose |
| 12 | `CNCUST.SAFE.PAYMENT.MED` | `CncustHSafeBop_PaymentMed` | TField |  | This field stores the payment method |
| 13 | `CNCUST.SAFE.RCPT.PMT.TYPE` | `CncustHSafeBop_RcptPmtType` | TField |  | This field stores the receipt payment type |
| 14 | `CNCUST.SAFE.CONTRACT.NO` | `CncustHSafeBop_ContractNo` | TField |  | This field stores the contract number |
| 15 | `CNCUST.SAFE.INVOICE.NO` | `CncustHSafeBop_InvoiceNo` | TField |  | This field stores the invoice number |
| 16 | `CNCUST.SAFE.BOND.GOOD.FLAG` | `CncustHSafeBop_BondGoodFlag` | TField |  | This field stores the remittance of bonded goods |
| 17 | `CNCUST.SAFE.LOCAL.REF` | `CncustHSafeBop_LocalRef` |  |  |  |
| 18 | `CNCUST.SAFE.OVERRIDE` | `CncustHSafeBop_Override` |  |  |  |
| 19 | `CNCUST.SAFE.RECORD.STATUS` | `CncustHSafeBop_RecordStatus` | String |  |  |
| 20 | `CNCUST.SAFE.CURR.NO` | `CncustHSafeBop_CurrNo` | String |  |  |
| 21 | `CNCUST.SAFE.INPUTTER` | `CncustHSafeBop_Inputter` |  |  |  |
| 22 | `CNCUST.SAFE.DATE.TIME` | `CncustHSafeBop_DateTime` |  |  |  |
| 23 | `CNCUST.SAFE.AUTHORISER` | `CncustHSafeBop_Authoriser` | String |  |  |
| 24 | `CNCUST.SAFE.CO.CODE` | `CncustHSafeBop_CoCode` | String |  |  |
| 25 | `CNCUST.SAFE.DEPT.CODE` | `CncustHSafeBop_DeptCode` | String |  |  |
| 26 | `CNCUST.SAFE.AUDITOR.CODE` | `CncustHSafeBop_AuditorCode` | String |  |  |
| 27 | `CNCUST.SAFE.AUDIT.DATE.TIME` | `CncustHSafeBop_AuditDateTime` | String |  |  |
