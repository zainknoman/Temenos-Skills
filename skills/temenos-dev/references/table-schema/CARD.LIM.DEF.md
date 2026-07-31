# CARD.LIM.DEF — Table Schema

> Source: `INSERTS/I_F.CARD.LIM.DEF` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CALI.WD.ONL.TXN.LIMIT` | `CardLimDef_WdOnlTxnLimit` | TField |  | Field to store the ONLINE withdrawal limits.Validations:Withdrawal Online Limit - only for ATM and POS txns. |
| 2 | `CALI.WD.OFL.TXN.LIMIT` | `CardLimDef_WdOflTxnLimit` | TField |  | Field to store the OFFLINE withdrawal limits.Validations:Withdrawal Offline Limit - only for ATM and POS txns. |
| 3 | `CALI.WD.ONL.DAY.LIMIT` | `CardLimDef_WdOnlDayLimit` | TField |  | Field to store Daily Online Limit - only for ATM and POS txns.Eg. 5000online limit is applicable to a maximum if CAD 5000 per day. |
| 4 | `CALI.WD.OFL.DAY.LIMIT` | `CardLimDef_WdOflDayLimit` | TField |  | Field to store daily Offline Limit - only for ATM and POS txns.Eg. 4000Offline limit is applicable to a maximum if CAD 4000 per day. |
| 5 | `CALI.DP.CS.THAMT.OUR` | `CardLimDef_DpCsThamtOur` | TField |  | Field is used to store the amount to be considered as a Maximum amount of Cash Deposit in Our ATMValidations= defined limit allowed only for Own bank and not other banks.Applicable for ATMeg. 1000 |
| 6 | `CALI.DP.CS.THPCT.OUR` | `CardLimDef_DpCsThpctOur` | TField |  | Field is used to store the Percentage to be considered as a Maximum Cash Deposit allowed in Our ATMValidations= defined limit allowed only for Own bank and not other banks.Applicable for ATMeg. 10 |
| 7 | `CALI.DP.CS.HDAYS.OUR` | `CardLimDef_DpCsHdaysOur` | TField |  | Field to store the number of Day's to Hold Funds in own bank ATM and not other bank's ATM. Eg 5. Any deposit more than threshold in own bank's ATM will be placed on HOLD for 5 calender days. |
| 8 | `CALI.DP.CS.THAMT.OTH` | `CardLimDef_DpCsThamtOth` | TField |  | Field is used to store the amount to be considered as a Maximum amount of Cash Deposit in other bank's ATMValidations= defined limit allowed only for other bank ATM'sApplicable for ATMeg. 1000 |
| 9 | `CALI.DP.CS.THPCT.OTH` | `CardLimDef_DpCsThpctOth` | TField |  | Field is used to store the Percentage upto which to be considered for Cash Deposit allowed in other bank's ATMValidations= defined limit allowed only for other bank ATM'sApplicable for ATM.eg. 10 |
| 10 | `CALI.DP.CS.HDAYS.OTH` | `CardLimDef_DpCsHdaysOth` | TField |  | Field to store the number of Day's to Hold Funds in other bank ATM. Eg 7. Any deposit more than threshold in other bank's ATM will be placed on HOLD for 7 calender days. |
| 11 | `CALI.DP.CQ.THAMT.OUR` | `CardLimDef_DpCqThamtOur` | TField |  | Field is used to store the amount to be considered as a Maximum amount for Cheque Deposit in Our ATMValidations= defined limit allowed only for Own bank and not other banks.Applicable for ATMeg. 1000 |
| 12 | `CALI.DP.CQ.THPCT.OUR` | `CardLimDef_DpCqThpctOur` | TField |  | Field is used to store the percentage up to which to be considered for Cheque Deposit in Our ATMValidations= defined limit allowed only for Own bank and not other banks.Applicable for ATMeg. 10% |
| 13 | `CALI.DP.CQ.HDAYS.OUR` | `CardLimDef_DpCqHdaysOur` | TField |  | Field to store the number of Day's to Hold Funds in own bank's ATM. Eg 7. Any deposit more than threshold in Own bank's ATM will be placed on HOLD for 7 calender days. |
| 14 | `CALI.DP.CQ.THAMT.OTH` | `CardLimDef_DpCqThamtOth` | TField |  | field to store maximum withdrawal for Cheque Deposited at Other ATM |
| 15 | `CALI.DP.CQ.THPCT.OTH` | `CardLimDef_DpCqThpctOth` | TField |  | Field to store the percentage upto which the Cash Withdrawal on Check deposits in Other ATM's are allowed.Eg. 5maximum upto 5 pct of withdrwal amount is allowed in other ATM |
| 16 | `CALI.DP.CQ.HDAYS.OTH` | `CardLimDef_DpCqHdaysOth` | TField |  | Field to store the number of Day's to Hold Funds in own bank's ATM for Cheque deposits. Eg 7. Any deposit more than threshold in other bank's ATM will be placed on HOLD for 7 calender days. |
| 17 | `CALI.CUS.FIELD` | `CardLimDef_CusField` |  |  |  |
| 18 | `CALI.CUS.INCL.VALUES` | `CardLimDef_CusInclValues` |  |  |  |
| 19 | `CALI.CUS.EXCL.VALUES` | `CardLimDef_CusExclValues` |  |  |  |
| 20 | `CALI.LOCAL.REF` | `CardLimDef_LocalRef` |  |  |  |
| 21 | `CALI.OVERRIDE` | `CardLimDef_Override` |  |  |  |
| 22 | `CALI.APPROVAL.AMT` | `CardLimDef_ApprovalAmt` | TField |  | Field to store the amount upto which the transactions allowed for the ID product for the defined channels. |
| 23 | `CALI.IMMEDIATE.STD.FLAG` | `CardLimDef_ImmediateStdFlag` | TField |  | Flag to indicate whether the approval amount should be available for the current day or next day. If this is set to "NO" then amount will be available immediately after the deposit transaction, but if this is set to "YES" then amount will be available on the next business day |
| 24 | `CALI.LEVEL.DP.CS.AMT` | `CardLimDef_LevelDpCsAmt` |  |  |  |
| 25 | `CALI.DEP.CS.HDAYS.OUR` | `CardLimDef_DepCsHdaysOur` |  |  |  |
| 26 | `CALI.DEP.CS.HDAYS.OTH` | `CardLimDef_DepCsHdaysOth` |  |  |  |
| 27 | `CALI.LEVEL.DP.CQ.AMT` | `CardLimDef_LevelDpCqAmt` |  |  |  |
| 28 | `CALI.DEP.CQ.HDAYS.OUR` | `CardLimDef_DepCqHdaysOur` |  |  |  |
| 29 | `CALI.DEP.CQ.HDAYS.OTH` | `CardLimDef_DepCqHdaysOth` |  |  |  |
| 30 | `CALI.POS.ADJ.ONLDAY.LIM` | `CardLimDef_PosAdjOnldayLim` | TField |  | Field to store online limit for POS transactions.Eg. 5000online limit is applicable to a maximum if CAD 5000 per day. |
| 31 | `CALI.POS.ADJ.OFFDAY.LIM` | `CardLimDef_PosAdjOffdayLim` | TField |  | Field to store offline limit for POS transactions.Eg. 2000 |
| 32 | `CALI.RESERVED.5` | `CardLimDef_Reserved5` | TField |  |  |
| 33 | `CALI.RESERVED.4` | `CardLimDef_Reserved4` | TField |  |  |
| 34 | `CALI.RESERVED.3` | `CardLimDef_Reserved3` | TField |  |  |
| 35 | `CALI.RESERVED.2` | `CardLimDef_Reserved2` | TField |  |  |
| 36 | `CALI.RESERVED.1` | `CardLimDef_Reserved1` | TField |  |  |
| 37 | `CALI.RECORD.STATUS` | `CardLimDef_RecordStatus` | String |  |  |
| 38 | `CALI.CURR.NO` | `CardLimDef_CurrNo` | String |  |  |
| 39 | `CALI.INPUTTER` | `CardLimDef_Inputter` |  |  |  |
| 40 | `CALI.DATE.TIME` | `CardLimDef_DateTime` |  |  |  |
| 41 | `CALI.AUTHORISER` | `CardLimDef_Authoriser` | String |  |  |
| 42 | `CALI.CO.CODE` | `CardLimDef_CoCode` | String |  |  |
| 43 | `CALI.DEPT.CODE` | `CardLimDef_DeptCode` | String |  |  |
| 44 | `CALI.AUDITOR.CODE` | `CardLimDef_AuditorCode` | String |  |  |
| 45 | `CALI.AUDIT.DATE.TIME` | `CardLimDef_AuditDateTime` | String |  |  |
