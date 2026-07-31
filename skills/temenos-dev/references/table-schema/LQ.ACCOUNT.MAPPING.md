# LQ.ACCOUNT.MAPPING — Table Schema

> Source: `INSERTS/I_F.LQ.ACCOUNT.MAPPING` in `LQ_LiquidityManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LQ.ACC.INSTITUTION.IDENTIFICATION` | `LqAccountMapping_InstitutionIdentification` | TField |  | If it's a Liquidity Transfer it should be Receiving Institution. If it's a Liquidity Transfer Advice it should be Sending Institution. |
| 2 | `LQ.ACC.LIQUIDITY.TRANSACTION.TYPE` | `LqAccountMapping_LiquidityTransactionType` | TField |  | Determines if it's a Liquidity Transfer Advice or Liquidity Transfer. |
| 3 | `LQ.ACC.DEBIT.CREDIT.OPERATION` | `LqAccountMapping_DebitCreditOperation` | TField |  | Possible values are Debit or Credit. |
| 4 | `LQ.ACC.ADVICE.TYPE` | `LqAccountMapping_AdviceType` | TField |  | Indicates if the LTA is for a debit operation or credit operation. |
| 5 | `LQ.ACC.EXTERNAL.ACCOUNT.IDENTIFIER` | `LqAccountMapping_ExternalAccountIdentifier` | TField |  | Account Number held at ASI. |
| 6 | `LQ.ACC.ACCOUNT.COMPANY` | `LqAccountMapping_AccountCompany` | TField |  | When TPH is in embedded mode this can be defaulted based on Transact T24 company. When TPH is in standalone mode this can be defaulted based on PP.NON.CUSTOMER.ACCOUNTS table. |
| 7 | `LQ.ACC.ACCOUNT.CURRENCY` | `LqAccountMapping_AccountCurrency` | TField | Yes | Mandatory field. Account's currency should be keyed in by the user |
| 8 | `LQ.ACC.INTERNAL.ACCOUNT` | `LqAccountMapping_InternalAccount` | TField |  | Clearing or suspense account held maintained internally. |
| 9 | `LQ.ACC.EXTERNAL.ACCOUNT.NAME` | `LqAccountMapping_ExternalAccountName` | TField |  | Name of the account number received from ASI. |
| 10 | `LQ.ACC.ACCOUNT.RESIDING.SERVICE` | `LqAccountMapping_AccountResidingService` | TField |  | This field is to capture the service of the clearing system where the account lies. For example: CLM, RTGS, T2S, TIPS. |
| 11 | `LQ.ACC.BIC` | `LqAccountMapping_Bic` | TField |  | This field is to capture the BIC Code of the institution that holds the account. |
| 12 | `LQ.ACC.RESERVED.8` | `LqAccountMapping_Reserved8` |  |  |  |
| 13 | `LQ.ACC.RESERVED.7` | `LqAccountMapping_Reserved7` |  |  |  |
| 14 | `LQ.ACC.RESERVED.6` | `LqAccountMapping_Reserved6` | TField |  |  |
| 15 | `LQ.ACC.RESERVED.5` | `LqAccountMapping_Reserved5` | TField |  |  |
| 16 | `LQ.ACC.RESERVED.4` | `LqAccountMapping_Reserved4` | TField |  |  |
| 17 | `LQ.ACC.RESERVED.3` | `LqAccountMapping_Reserved3` | TField |  |  |
| 18 | `LQ.ACC.RESERVED.2` | `LqAccountMapping_Reserved2` | TField |  |  |
| 19 | `LQ.ACC.RESERVED.1` | `LqAccountMapping_Reserved1` | TField |  |  |
| 20 | `LQ.ACC.LOCAL.REF` | `LqAccountMapping_LocalRef` |  |  |  |
| 21 | `LQ.ACC.OVERRIDE` | `LqAccountMapping_Override` |  |  |  |
| 22 | `LQ.ACC.RECORD.STATUS` | `LqAccountMapping_RecordStatus` | String |  |  |
| 23 | `LQ.ACC.CURR.NO` | `LqAccountMapping_CurrNo` | String |  |  |
| 24 | `LQ.ACC.INPUTTER` | `LqAccountMapping_Inputter` |  |  |  |
| 25 | `LQ.ACC.DATE.TIME` | `LqAccountMapping_DateTime` |  |  |  |
| 26 | `LQ.ACC.AUTHORISER` | `LqAccountMapping_Authoriser` | String |  |  |
| 27 | `LQ.ACC.CO.CODE` | `LqAccountMapping_CoCode` | String |  |  |
| 28 | `LQ.ACC.DEPT.CODE` | `LqAccountMapping_DeptCode` | String |  |  |
| 29 | `LQ.ACC.AUDITOR.CODE` | `LqAccountMapping_AuditorCode` | String |  |  |
| 30 | `LQ.ACC.AUDIT.DATE.TIME` | `LqAccountMapping_AuditDateTime` | String |  |  |
