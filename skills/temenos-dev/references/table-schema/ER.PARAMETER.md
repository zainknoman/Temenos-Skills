# ER.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ER.PARAMETER` in `ER_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ER.PAR.ACCOUNT.ID` | `ErParameter_AccountId` |  |  |  |
| 2 | `ER.PAR.AC.RET.DAYS` | `ErParameter_AcRetDays` |  |  |  |
| 3 | `ER.PAR.AC.OVER.DAYS` | `ErParameter_AcOverDays` |  |  |  |
| 4 | `ER.PAR.CATEGORY` | `ErParameter_Category` |  |  |  |
| 5 | `ER.PAR.EXP.FUNDS.TYPE` | `ErParameter_ExpFundsType` |  |  |  |
| 6 | `ER.PAR.EXP.TYPE.DESC` | `ErParameter_ExpTypeDesc` |  |  |  |
| 7 | `ER.PAR.EXP.TYPE.CR.DR` | `ErParameter_ExpTypeCrDr` |  |  |  |
| 8 | `ER.PAR.PAY.FUNDS.TYPE` | `ErParameter_PayFundsType` |  |  |  |
| 9 | `ER.PAR.PAY.TYPE.DESC` | `ErParameter_PayTypeDesc` |  |  |  |
| 10 | `ER.PAR.PAY.TYPE.CR.DR` | `ErParameter_PayTypeCrDr` |  |  |  |
| 11 | `ER.PAR.ACCT.BAL.FIELD` | `ErParameter_AcctBalField` |  |  |  |
| 12 | `ER.PAR.AUTO.PAR.MATCH` | `ErParameter_AutoParMatch` |  |  |  |
| 13 | `ER.PAR.MATCH.FIELD` | `ErParameter_MatchField` |  |  |  |
| 14 | `ER.PAR.TOLERANCE` | `ErParameter_Tolerance` |  |  |  |
| 15 | `ER.PAR.RETENTION.DAYS` | `ErParameter_RetentionDays` | TField |  | This field determines how long (in days) matched items remain on the live file before being transferred to the history file. This will be the system wide default for all accounts entered above unless they have the AC.RET.DAYS set. Validation Rules: The number of days is the working days and not the calendar days. |
| 16 | `ER.PAR.OVERDUE.DAYS` | `ErParameter_OverdueDays` | TField |  | This field determines how long (in days) unmatched items remain on the live file until being deleted. This will be the system wide default for all accounts entered above unless they have the AC.OVER.DAYS set. Validation Rules: The number of days is the working days and not the calendar days No Input field for ID = "COVER" |
| 17 | `ER.PAR.CCY.MKT` | `ErParameter_CcyMkt` | TField | No | Specify the Currency Market from which the Exchange rate to be taken for updating Correspondent Limit. When a limit is specified in ER.COVER.LIMIT for a Currency and an Incoming MT103 is processed with Debit Currency other than the Limit Currency, then the Limit currency amount is arrived using the Exchange rate applicable for the Currency Market as specified here. Validation Rules: Optional field-Default value is "1" Value entered should be a record in CURRENCY.MARKET. Input allowed only for ID = "COVER" - Otherwise No input field. |
| 18 | `ER.PAR.REQUEST.ADV.DAYS` | `ErParameter_RequestAdvDays` | TField | Yes | In AC.EXPECTED.RECS, when RC (Received Cover) is not available, EC (Expected Cover) record is created for Inward MT103 messages during Correspodent Cover Limit processing . Whenever RC is received , same is matched with EC. Incase the EC record remains unmatched from Date.Entered for more than the days specified here, then MT195 (Queries) is sent to the Sender of MT103 for clarification about the message with tag 75 as "'/2/". Incase Request.Query details given in the respective AC.EXPECTED.RECS, then same is used in tag 75 of MT195. Validation Rules: Mandatory Input for ID = "COVER" otherwise Not allowed 1-2 Numeric Characters denoting the working days. |
| 19 | `ER.PAR.CANCEL.ADV.DAYS` | `ErParameter_CancelAdvDays` | TField | Yes | In AC.EXPECTED.RECS, when RC (Received Cover) is not available, EC (Expected Cover) record is created for Inward MT103 messages during Correspodent Cover Limit processing . Whenever RC is received , same is matched with EC. Incase the EC record remains unmatched from Date.Entered for more than the days specified here, then MT195 (Queries) is sent to the Sender of MT103 for Cancellation of the message(MT103) with tag 75 as "'/36/". The EC record is cancelled from AC.EXPETED.RECS application. Incase Cancel.Query details given in the respective AC.EXPECTED.RECS, then same is used in tag 75 of MT195. Validation Rules: Mandatory Input for ID = "COVER" - Otherwise Not allowed. 1-2 Numeric Characters denoting the working days. No of days entered here should be more than REQUEST.ADV.DAYS as specified in previous field. |
| 20 | `ER.PAR.FWD.FUNDS.TYPES` | `ErParameter_FwdFundsTypes` |  |  |  |
| 21 | `ER.PAR.FWD.DB.TXN.CODE` | `ErParameter_FwdDbTxnCode` |  |  |  |
| 22 | `ER.PAR.FWD.CR.TXN.CODE` | `ErParameter_FwdCrTxnCode` |  |  |  |
| 23 | `ER.PAR.RESERVED6` | `ErParameter_Reserved6` | TField |  |  |
| 24 | `ER.PAR.RESERVED5` | `ErParameter_Reserved5` | TField |  |  |
| 25 | `ER.PAR.RESERVED4` | `ErParameter_Reserved4` | TField |  |  |
| 26 | `ER.PAR.RESERVED3` | `ErParameter_Reserved3` | TField |  |  |
| 27 | `ER.PAR.RESERVED2` | `ErParameter_Reserved2` | TField |  |  |
| 28 | `ER.PAR.RESERVED1` | `ErParameter_Reserved1` | TField |  |  |
| 29 | `ER.PAR.RECORD.STATUS` | `ErParameter_RecordStatus` | String |  |  |
| 30 | `ER.PAR.CURR.NO` | `ErParameter_CurrNo` | String |  |  |
| 31 | `ER.PAR.INPUTTER` | `ErParameter_Inputter` |  |  |  |
| 32 | `ER.PAR.DATE.TIME` | `ErParameter_DateTime` |  |  |  |
| 33 | `ER.PAR.AUTHORISER` | `ErParameter_Authoriser` | String |  |  |
| 34 | `ER.PAR.CO.CODE` | `ErParameter_CoCode` | String |  |  |
| 35 | `ER.PAR.DEPT.CODE` | `ErParameter_DeptCode` | String |  |  |
| 36 | `ER.PAR.AUDITOR.CODE` | `ErParameter_AuditorCode` | String |  |  |
| 37 | `ER.PAR.AUDIT.DATE.TIME` | `ErParameter_AuditDateTime` | String |  |  |
