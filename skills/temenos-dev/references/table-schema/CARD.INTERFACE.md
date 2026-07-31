# CARD.INTERFACE — Table Schema

> Source: `INSERTS/I_F.CARD.INTERFACE` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAD.SHORT.DESCRP` | `CardInterface_ShortDescrp` |  |  |  |
| 2 | `CAD.DESCRIPTION` | `CardInterface_Description` |  |  |  |
| 3 | `CAD.COMP.ID.REJ.AC` | `CardInterface_CompIdRejAc` |  |  |  |
| 4 | `CAD.REJ.SUS.AC.OUR` | `CardInterface_RejSusAcOur` |  |  |  |
| 5 | `CAD.REJ.SUS.AC.OTH` | `CardInterface_RejSusAcOth` |  |  |  |
| 6 | `CAD.FTP.ID` | `CardInterface_FtpId` | TField |  | Not in use |
| 7 | `CAD.EXTERNAL.ID` | `CardInterface_ExternalId` | TField |  | External IDReserved for future use. |
| 8 | `CAD.WD.ONL.TXN.LIMIT` | `CardInterface_WdOnlTxnLimit` | TField |  | Field is used to store the ONLINE withdrawal limits.Validations:Withdrawal Online Limit - only for ATM and POS txns.Note: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 9 | `CAD.WD.OFL.TXN.LIMIT` | `CardInterface_WdOflTxnLimit` | TField |  | Field to store Daily Online Limit - only for ATM and POS txns.Eg. 5000online limit is applicable to a maximum if CAD 5000 per day.Note: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 10 | `CAD.WD.ONL.DAY.LIMIT` | `CardInterface_WdOnlDayLimit` | TField |  | Field to store Daily Online Limit - only for ATM and POS txns.Eg. 5000online limit is applicable to a maximum if CAD 5000 per day.Note: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 11 | `CAD.WD.OFL.DAY.LIMIT` | `CardInterface_WdOflDayLimit` | TField |  | Field to store daily Offline Limit - only for ATM and POS txns.Eg. 4000Offline limit is applicable to a maximum if CAD 4000 per day.Note: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 12 | `CAD.DP.CS.THAMT.OUR` | `CardInterface_DpCsThamtOur` | TField |  | Field is used to store the amount to be considered as a Maximum amount of Cash Deposit in Our ATMValidations= defined limit allowed only for Own bank and not other banks.Applicable for ATMeg. 1000Note: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 13 | `CAD.DP.CS.THPCT.OUR` | `CardInterface_DpCsThpctOur` | TField |  | Field is used to store the Percentage to be considered as a Maximum Cash Deposit allowed in Our ATMValidations= defined limit allowed only for Own bank and not other banks.Applicable for ATMeg. 10Note: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 14 | `CAD.DP.CS.HDAYS.OUR` | `CardInterface_DpCsHdaysOur` | TField |  | Field to store the number of Day's to Hold Funds in own bank ATM and not other bank's ATM. Eg 5. Any deposit more than threshold in own bank's ATM will be placed on HOLD for 5 calender days.Note: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 15 | `CAD.DP.CS.TXN.ID.OUR` | `CardInterface_DpCsTxnIdOur` |  |  |  |
| 16 | `CAD.DP.CS.THAMT.OTH` | `CardInterface_DpCsThamtOth` | TField |  | Field is used to store the amount to be considered as a Maximum amount of Cash Deposit in other bank's ATMValidations= defined limit allowed only for other bank ATM'sApplicable for ATMeg. 1000Note: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 17 | `CAD.DP.CS.THPCT.OTH` | `CardInterface_DpCsThpctOth` | TField |  | Field is used to store the Percentage upto which to be considered for Cash Deposit allowed in other bank's ATMValidations= defined limit allowed only for other bank ATM'sApplicable for ATM.eg. 10Note: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 18 | `CAD.DP.CS.HDAYS.OTH` | `CardInterface_DpCsHdaysOth` | TField |  | "Field to store the number of Day's to Hold Funds if the cash deposit in other bank's ATM exceeds the limit. Eg 7. Any deposit more than threshold in Own bank's ATM will be placed on HOLD for 7 calender daysNote: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table."Note: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 19 | `CAD.DP.CS.TXN.ID.OTH` | `CardInterface_DpCsTxnIdOth` |  |  |  |
| 20 | `CAD.DP.CQ.THAMT.OUR` | `CardInterface_DpCqThamtOur` | TField |  | Field is used to store the amount to be considered as a Maximum amount for Cheque Deposit in Our ATMValidations= defined limit allowed only for Own bank and not other banks.Applicable for ATMeg. 1000Note: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 21 | `CAD.DP.CQ.THPCT.OUR` | `CardInterface_DpCqThpctOur` | TField |  | Field is used to store the percentage up to which to be considered for Cheque Deposit in Our ATMValidations= defined limit allowed only for Own bank and not other banks.Applicable for ATMeg. 10%Note: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 22 | `CAD.DP.CQ.HDAYS.OUR` | `CardInterface_DpCqHdaysOur` | TField |  | "Field to store the number of Day's to Hold Funds if the Cheque deposit in own bank's ATM exceeds the limit. Eg 7. Any deposit more than threshold in Own bank's ATM will be placed on HOLD for 7 calender days.Note: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 23 | `CAD.DP.CQ.TXN.ID.OUR` | `CardInterface_DpCqTxnIdOur` | TField |  |  |
| 24 | `CAD.DP.CQ.THAMT.OTH` | `CardInterface_DpCqThamtOth` | TField |  | field to store maximum withdrawal for Cheque Deposited at Other ATM.Note: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 25 | `CAD.DP.CQ.THPCT.OTH` | `CardInterface_DpCqThpctOth` | TField |  | Field to store the percentage upto which the Cash Withdrawal on Check deposits in Other ATM's are allowed.Eg. 5maximum upto 5 pct of withdrawal amount is allowed in other ATMNote: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 26 | `CAD.DP.CQ.HDAYS.OTH` | `CardInterface_DpCqHdaysOth` | TField |  | Field to store the number of Day's to Hold Funds if the Cheque deposit in other bank's ATM exceeds the limit. Eg 7. Any deposit more than threshold in Own bank's ATM will be placed on HOLD for 7 calender daysNote: Limits in CARD ISSUE gets defaulted from CARD.INTERFACE if record not available in CARD.LIM.DEF table. |
| 27 | `CAD.DP.CQ.TXN.ID.OTH` | `CardInterface_DpCqTxnIdOth` | TField |  | Transaction Code |
| 28 | `CAD.MAX.DEPOSIT.AMT` | `CardInterface_MaxDepositAmt` | TField |  | Field to indicate the maximum amount that can deposited via the ID channel.Example - ID= ATM, maximum deposit amount as 2,00,000.00.Then only up 200000.00 deposit is allowed via ATM. |
| 29 | `CAD.LOG.DETAIL` | `CardInterface_LogDetail` | TField |  | To define Interface logs to be updated based on different settings "FULL", "ERROR" and NULLNot in use now. |
| 30 | `CAD.LOCAL.REF` | `CardInterface_LocalRef` |  |  |  |
| 31 | `CAD.OVERRIDE` | `CardInterface_Override` |  |  |  |
| 32 | `CAD.HOLD.TYPE` | `CardInterface_HoldType` | TField |  | Field to indicate the Holds via channels to be placed based on Card based limits or Tier based limits.Allowed inputs - Card / Tier |
| 33 | `CAD.NO.PAC.REQ` | `CardInterface_NoPacReq` |  |  |  |
| 34 | `CAD.INST.DISC.RESET` | `CardInterface_InstDiscReset` | TField |  | To define Institution Disclaimer date. This is used to reset the disclaimer for the customer when the last disclaimer date is less than the parameterized one. Used for Online Banking |
| 35 | `CAD.APPROVAL.AMT` | `CardInterface_ApprovalAmt` | TField |  | Approval amount to be defined for tired holds. The amount specified here will be automatically available when customer deposits the transaction through ATM |
| 36 | `CAD.IMMEDIATE.STD.FLAG` | `CardInterface_ImmediateStdFlag` | TField |  | Flag to indicate whether the approval amount should be available for the current day or next day. If this is set to "NO" then amount will be available immediately after the deposit transaction, but if this is set to "YES" then amount will be available on the next business day |
| 37 | `CAD.LEVEL.DP.CS.AMT` | `CardInterface_LevelDpCsAmt` |  |  |  |
| 38 | `CAD.DEP.CS.HDAYS.OUR` | `CardInterface_DepCsHdaysOur` |  |  |  |
| 39 | `CAD.DEP.CS.HDAYS.OTH` | `CardInterface_DepCsHdaysOth` |  |  |  |
| 40 | `CAD.LEVEL.DP.CQ.AMT` | `CardInterface_LevelDpCqAmt` |  |  |  |
| 41 | `CAD.DEP.CQ.HDAYS.OUR` | `CardInterface_DepCqHdaysOur` |  |  |  |
| 42 | `CAD.DEP.CQ.HDAYS.OTH` | `CardInterface_DepCqHdaysOth` |  |  |  |
| 43 | `CAD.HOLD.CALENDER` | `CardInterface_HoldCalender` | TField |  |  |
| 44 | `CAD.TYPE.OF.DAY` | `CardInterface_TypeOfDay` | TField |  | To indicate what type of day to be considered.(C - Calendar date or W - Working day) |
| 45 | `CAD.MDSB.DISC.RESET` | `CardInterface_MdsbDiscReset` | TField |  | MDSB Disclaimer date reset, purpose of this field is, in case FI needs all the existing user in MDSB to resign the disclaimer page on a particular date (Like T24 go live date). If this is not required, setup date is past. |
| 46 | `CAD.MDSB.REMIN.FREQ` | `CardInterface_MdsbReminFreq` | TField |  | MDSB Disclaimer reminder frequency, in case user eligible for MDSB, but does not opt for it now and wants to remind after 6M.Valid Value: 1M, 1D, 1W, 1Y |
| 47 | `CAD.MDSB.MULTI.SIGN` | `CardInterface_MdsbMultiSign` |  |  |  |
| 48 | `CAD.MDSB.EXCLUDE` | `CardInterface_MdsbExclude` |  |  |  |
| 49 | `CAD.MDSB.REQUIRED` | `CardInterface_MdsbRequired` | TField |  | The possible values are Yes or No. Field to indicate if FI Opted for MDSB or not. |
| 50 | `CAD.MDSB.MANDATORY` | `CardInterface_MdsbMandatory` | TField | Yes | The possible values are Yes or No. High level setting if MDSB is mandatory for Business CIF or not. This can also be defined in CARD.ISSUE. CARD issue takes precedence over CARD INTERFACE setting |
| 51 | `CAD.MDSB.DUAL.SIGN` | `CardInterface_MdsbDualSign` | TField |  | The possible values are Yes or No. Field to indicate if FI required Dual sign features for MDSB or not. If not, by default the initiator approve the transaction no second level authoriser is required. |
| 52 | `CAD.MDSB.ALLOWED` | `CardInterface_MdsbAllowed` | TField |  | The possible values are Yes or No. Field to indicate if FI requires the MDSB.ALLOWED field to be set automatically to YES for Business CIF or not (Based on Cus type of customer) |
| 53 | `CAD.MIN.PAC.LENGTH` | `CardInterface_MinPacLength` | TField |  | Not in use. Minimum PAC length is defined in CAMB.MEM.DIR.PARAM |
| 54 | `CAD.MAX.PAC.LENGTH` | `CardInterface_MaxPacLength` | TField |  | Field to define the maximum PAC length to be considered for Channels. |
| 55 | `CAD.PAC.CHAR.TYPE` | `CardInterface_PacCharType` | TField |  |  |
| 56 | `CAD.RESERVED.3` | `CardInterface_Reserved3` | TField |  |  |
| 57 | `CAD.RESERVED.2` | `CardInterface_Reserved2` | TField |  |  |
| 58 | `CAD.RESERVED.1` | `CardInterface_Reserved1` | TField |  |  |
| 59 | `CAD.RECORD.STATUS` | `CardInterface_RecordStatus` | String |  |  |
| 60 | `CAD.CURR.NO` | `CardInterface_CurrNo` | String |  |  |
| 61 | `CAD.INPUTTER` | `CardInterface_Inputter` |  |  |  |
| 62 | `CAD.DATE.TIME` | `CardInterface_DateTime` |  |  |  |
| 63 | `CAD.AUTHORISER` | `CardInterface_Authoriser` | String |  |  |
| 64 | `CAD.CO.CODE` | `CardInterface_CoCode` | String |  |  |
| 65 | `CAD.DEPT.CODE` | `CardInterface_DeptCode` | String |  |  |
| 66 | `CAD.AUDITOR.CODE` | `CardInterface_AuditorCode` | String |  |  |
| 67 | `CAD.AUDIT.DATE.TIME` | `CardInterface_AuditDateTime` | String |  |  |
