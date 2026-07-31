# PP.BALANCE.CHECK.REQUIRED — Table Schema

> Source: `INSERTS/I_F.PP.BALANCE.CHECK.REQUIRED` in `PP_BalanceCheckService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.BCR.CompanyID` | `PpBalanceCheckRequired_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.BCR.Ranking` | `PpBalanceCheckRequired_Ranking` | TField | Yes | Specifies the order (sequence) of the record in the application. Based on the value, a record is prioritised in such a way that, it is given higher preference for selection under peeling logic applied in the payments hub. Validation Rules: Mandatory field. 9 numeric characters. |
| 3 | `PP.BCR.OriginatingSource` | `PpBalanceCheckRequired_Originatingsource` | TField | Yes | Specifies the name of the source from where the payment is originated. Example: SWIFT, BACS. Validation Rules: Mandatory fields. 10 alphanumeric characters. |
| 4 | `PP.BCR.AccountType` | `PpBalanceCheckRequired_Accounttype` | TField |  | Specifies the type of account for which balance check is to be performed or skipped. Possible values: C - Client N - Nostro V - Vostro/Loro I - Suspense/Internal PL - P&amp;L Account |
| 5 | `PP.BCR.IncomingMessageType` | `PpBalanceCheckRequired_Incomingmessagetype` | TField | Yes | Holds the type of the incoming message type. Example: MT101, MT202. Validation Rules: Mandatory fields. 10 alphanumeric characters. |
| 6 | `PP.BCR.ClearingNatureCode` | `PpBalanceCheckRequired_Clearingnaturecode` | TField | Yes | Holds the code used to identify the nature of the clearing payment. Validation Rules: Mandatory field. 20 alphanumeric character. |
| 7 | `PP.BCR.BalanceCheckRequiredFlag` | `PpBalanceCheckRequired_Balancecheckrequiredflag` | TField |  | Indicates if balance is to be checked by the payments hub for a payment of the defined characteristics. Possible Values: "Y" - Yes "N" - No A value of "Y" implies that the balance check is required for the payment. A value of "N" implies that the balance check is not required for the payment. |
| 8 | `PP.BCR.SettlementTransactionIndicator` | `PpBalanceCheckRequired_Settlementtransactionindicator` | TField |  | Indicates whether the payment is a settlement transaction or not. Possible values: Y - Yes Blank - No A value of 'Y' indicates the transaction is a settlement transaction. Blank value indicates the transaction is not a settlement transaction. |
| 9 | `PP.BCR.ReserveWithCharges` | `PpBalanceCheckRequired_Reservewithcharges` | TField |  | Denotes whether balance reservation needs to be done with charges or only for transaction amount |
| 10 | `PP.BCR.HoldBalForFutureProcessingDt` | `PpBalanceCheckRequired_Holdbalforfutureprocessingdt` | TField |  |  |
| 11 | `PP.BCR.OERepairReservation` | `PpBalanceCheckRequired_Oerepairreservation` | TField |  | Denotes balance reservation needs to be done at the Submit Stage for Order Entry or at the Authorisation stage for Order Entry. Not Valid. Possible Values: Submit Authorise STP.It will be used for TPS Standalone. |
| 12 | `PP.BCR.ApprovalCode` | `PpBalanceCheckRequired_Approvalcode` |  |  |  |
| 13 | `PP.BCR.Action` | `PpBalanceCheckRequired_Action` |  |  |  |
| 14 | `PP.BCR.LOCAL.REF` | `PpBalanceCheckRequired_LocalRef` |  |  |  |
| 15 | `PP.BCR.OVERRIDE` | `PpBalanceCheckRequired_Override` |  |  |  |
| 16 | `PP.BCR.RECORD.STATUS` | `PpBalanceCheckRequired_RecordStatus` | String |  |  |
| 17 | `PP.BCR.CURR.NO` | `PpBalanceCheckRequired_CurrNo` | String |  |  |
| 18 | `PP.BCR.INPUTTER` | `PpBalanceCheckRequired_Inputter` |  |  |  |
| 19 | `PP.BCR.DATE.TIME` | `PpBalanceCheckRequired_DateTime` |  |  |  |
| 20 | `PP.BCR.AUTHORISER` | `PpBalanceCheckRequired_Authoriser` | String |  |  |
| 21 | `PP.BCR.CO.CODE` | `PpBalanceCheckRequired_CoCode` | String |  |  |
| 22 | `PP.BCR.DEPT.CODE` | `PpBalanceCheckRequired_DeptCode` | String |  |  |
| 23 | `PP.BCR.AUDITOR.CODE` | `PpBalanceCheckRequired_AuditorCode` | String |  |  |
| 24 | `PP.BCR.AUDIT.DATE.TIME` | `PpBalanceCheckRequired_AuditDateTime` | String |  |  |
| 25 | `PP.BCR.BalanceCheckTimeOutAction` | `PpBalanceCheckRequired_Balancechecktimeoutaction` | TField |  | Indicates the action that must be performed when a pending fund check request has exceeded the configured time out Options possible are Cancel,Continue,Repair or blank. Blank option implies cancel Values cannot be defined in this field if the value in BalanceCheckRequiredFlag field is set to 'N' |
| 26 | `PP.BCR.RecyclerRetryUntilDate` | `PpBalanceCheckRequired_Recyclerretryuntildate` | TField | Yes | This field indicates the date till which the Recyler should try for Funds. If defined, TPH will pass the date and channel Cut Off Time to create ACFA record Allowed Values are CVD, DVD, DUE, RCVD, RCLD, RED,SEND Where, CVD - Credit Value Date DVD - Debit Value Date DUE - Processing Date RCVD - Requested Credit Value Date RCLD - Requested Collection Date RED - Requested Execution Date SEND - Payment Send Date Validation: Non mandatory field Can be defined only when Balance Check with Charges is enabled, otherwise error is raised |
