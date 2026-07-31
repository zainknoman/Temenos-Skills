# ACH.CORPORATE.INFO — Table Schema

> Source: `INSERTS/I_F.ACH.CORPORATE.INFO` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACH.CORP.CUSTOMER.ID` | `AchCorporateInfo_CustomerId` | TField |  | 10 positions�A field within T24 by which all bank Customers are uniquely identified. 10 digit numeric. |
| 2 | `ACH.CORP.ORIGINATOR.ID` | `AchCorporateInfo_OriginatorId` | TField |  | 10 positions - This field uniquely identifies each Corporate Customer as an ACH participant to the T24 bank. |
| 3 | `ACH.CORP.CORPORATE.TYPE` | `AchCorporateInfo_CorporateType` | TField |  | When an Originator ID is created the Corporate Type field will be populated with a value of �Originator"". |
| 4 | `ACH.CORP.ENTRIES.BY.COMPANY` | `AchCorporateInfo_EntriesByCompany` | TField |  | Check box - Flag used to determine if the entries are made using the Offset DR and Offset CR account number at the Originator Level or at the Company Level. Blank = Entries by Originator Check box checked = Entires by Company |
| 5 | `ACH.CORP.OFFSET.CR.ACCT` | `AchCorporateInfo_OffsetCrAcct` | TField |  | Used to offset and balance the Debit amount of ACH Batches received from Clients or used to offset Debits created with the ad hoc batch entry. Field required when Entries by company is set to ""Blank"". |
| 6 | `ACH.CORP.OFFSET.DR.ACCT` | `AchCorporateInfo_OffsetDrAcct` | TField |  | Used to offset and balance the Credit amount of ACH Batches received from Clients or used to offset Credits created with the ad hoc batch entry. Field required when Entries by company is set to ""Blank"". |
| 7 | `ACH.CORP.ALLOW.SEC.CODE` | `AchCorporateInfo_AllowSecCode` |  |  |  |
| 8 | `ACH.CORP.RISK.MGMT` | `AchCorporateInfo_RiskMgmt` | TField |  | Future Use |
| 9 | `ACH.CORP.AGGR.DEBIT.DAYS` | `AchCorporateInfo_AggrDebitDays` | TField |  | Future Use |
| 10 | `ACH.CORP.AGGR.CREDIT.DAYS` | `AchCorporateInfo_AggrCreditDays` | TField |  | Future Use |
| 11 | `ACH.CORP.AGGR.DEBIT.AMT` | `AchCorporateInfo_AggrDebitAmt` | TField |  | Future Use |
| 12 | `ACH.CORP.AGGR.CREDIT.AMT` | `AchCorporateInfo_AggrCreditAmt` | TField |  | Future Use |
| 13 | `ACH.CORP.DAILY.DEBIT.TOTAL` | `AchCorporateInfo_DailyDebitTotal` | TField |  | The total amount of ACH debits that can be originated for a day would be defined in this field. The total of all the debits batches originated by the corporate originator for an effective date is compared against this amount. When the cumulative total of all the debited batches originated for that effective date is more than the amount defined here , the credit batch that breaches this limit would have the status updated as LIMIT.BREACHED when the batch is processed by the either the ACH.UPLOAD.WAREHOUSE service or the ACH.CUPTURE.UPLOAD service. Validation An error would be raised if the field is updated if the value in the field corporate type is 'company' |
| 14 | `ACH.CORP.DAILY.CREDIT.TOTAL` | `AchCorporateInfo_DailyCreditTotal` | TField |  | The total amount of ACH credits that can be originated for a day would be defined in this field. The total of all the credit batches originated by the corporate originator for an effective date is compared against this amount. When the cumulative total of all the credit batches originated for that effective date is more than the amount defined here , the credit batch that breaches this limit would have the status updated as LIMIT.BREACHED when the batch is processed by the either the ACH.UPLOAD.WAREHOUSE service or the ACH.CAPTURE.UPLOAD service. Validation - An error would be raised if the field is updated if the value in the field corporate type is 'company' |
| 15 | `ACH.CORP.TXNS.DEBIT.LIMIT` | `AchCorporateInfo_TxnsDebitLimit` | TField |  | Future Use |
| 16 | `ACH.CORP.TXNS.CREDIT.LIMIT` | `AchCorporateInfo_TxnsCreditLimit` | TField |  | Future Use |
| 17 | `ACH.CORP.PREFUND.HOLD` | `AchCorporateInfo_PrefundHold` | TField |  | Account Holds and Prefunding of Originated ACH Credit Files are risk mitigation tools available to assist in preventing losses associated with ACH Origination. The Account Hold option will place a memo post hold on the Originator account at the time the ACH credit file or batch is submitted to T24. The Prefunding option will post a debit adjustment to the Originator account at the time the ACH credit file or batch is submitted to T24. |
| 18 | `ACH.CORP.RETRY.PAYMENTS` | `AchCorporateInfo_RetryPayments` | TField |  | To �Opt In� for Retry Payments functionality select a non-blank value. Valid values are: None (Null) = the default value and is equivalent to �Opt Out�. 0 = do not retry payments 1 = retry payments 1 time 2 = retry payments 2 times |
| 19 | `ACH.CORP.SAME.DAY` | `AchCorporateInfo_SameDay` | TField |  | Same day ACH flag will allow a Corporate Originator to originate same ACH batches that will be settled with RDFI on the same business day provided the effective date is less than or equal to current business date and the batch is sent in the same day distribution time set by Fed.If the flag is not enabled the ACH batch for the originator is not processed in the same day distribution window provided by FED as per the NACHA guidelines.The batch would be sent to the Fed only after the same day final distribution cutoff for a corporate that has not signed up for same day processing and has sent a batch with effective date equal or less than current business date. Validation : The only allowed value is YES. If the value in the field CORPORATE.TYPE = COMPANY and there is a value of 'YES' in this field then raise the error EB-INVALID.DEF.SAME.DAY |
| 20 | `ACH.CORP.CHARGE.ACCOUNT` | `AchCorporateInfo_ChargeAccount` | TField |  | Define the account which would be debited by the DDA system for ACH activity.Corporate Customer can havethis field defined and it should be an Arrangement account held by the Corporate Customer. Validation : If the value in the field CORPORATE.TYPE is COMPANY then Value cannot be defined in this Charge Account Field. |
| 21 | `ACH.CORP.PREFUND.DAYS` | `AchCorporateInfo_PrefundDays` | TField |  | Required field if the Account Hold / Prefunding option is input. Input can be between 1 to 99 |
| 22 | `ACH.CORP.RESERVED.14` | `AchCorporateInfo_Reserved14` | TField |  | Reserved Field |
| 23 | `ACH.CORP.RESERVED.13` | `AchCorporateInfo_Reserved13` | TField |  | Reserved Field |
| 24 | `ACH.CORP.RESERVED.12` | `AchCorporateInfo_Reserved12` | TField |  | Reserved Field |
| 25 | `ACH.CORP.RESERVED.11` | `AchCorporateInfo_Reserved11` | TField |  | Reserved Field |
| 26 | `ACH.CORP.RESERVED.10` | `AchCorporateInfo_Reserved10` | TField |  | Reserved Field |
| 27 | `ACH.CORP.RESERVED.9` | `AchCorporateInfo_Reserved9` | TField |  | Reserved Field |
| 28 | `ACH.CORP.RESERVED.8` | `AchCorporateInfo_Reserved8` | TField |  | Reserved Field |
| 29 | `ACH.CORP.RESERVED.7` | `AchCorporateInfo_Reserved7` | TField |  | Reserved Field |
| 30 | `ACH.CORP.RESERVED.6` | `AchCorporateInfo_Reserved6` | TField |  | Reserved Field |
| 31 | `ACH.CORP.RESERVED.5` | `AchCorporateInfo_Reserved5` | TField |  | Reserved Field |
| 32 | `ACH.CORP.RESERVED.4` | `AchCorporateInfo_Reserved4` | TField |  | Reserved Field |
| 33 | `ACH.CORP.RESERVED.3` | `AchCorporateInfo_Reserved3` | TField |  | Reserved Field |
| 34 | `ACH.CORP.RESERVED.2` | `AchCorporateInfo_Reserved2` | TField |  | Reserved Field |
| 35 | `ACH.CORP.RESERVED.1` | `AchCorporateInfo_Reserved1` | TField |  | Reserved Field |
| 36 | `ACH.CORP.LOCAL.REF` | `AchCorporateInfo_LocalRef` |  |  |  |
| 37 | `ACH.CORP.OVERRIDE` | `AchCorporateInfo_Override` |  |  |  |
| 38 | `ACH.CORP.RECORD.STATUS` | `AchCorporateInfo_RecordStatus` | String |  |  |
| 39 | `ACH.CORP.CURR.NO` | `AchCorporateInfo_CurrNo` | String |  |  |
| 40 | `ACH.CORP.INPUTTER` | `AchCorporateInfo_Inputter` |  |  |  |
| 41 | `ACH.CORP.DATE.TIME` | `AchCorporateInfo_DateTime` |  |  |  |
| 42 | `ACH.CORP.AUTHORISER` | `AchCorporateInfo_Authoriser` | String |  |  |
| 43 | `ACH.CORP.CO.CODE` | `AchCorporateInfo_CoCode` | String |  |  |
| 44 | `ACH.CORP.DEPT.CODE` | `AchCorporateInfo_DeptCode` | String |  |  |
| 45 | `ACH.CORP.AUDITOR.CODE` | `AchCorporateInfo_AuditorCode` | String |  |  |
| 46 | `ACH.CORP.AUDIT.DATE.TIME` | `AchCorporateInfo_AuditDateTime` | String |  |  |
