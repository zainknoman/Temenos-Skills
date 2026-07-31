# CARD.ACCESS — Table Schema

> Source: `INSERTS/I_F.CARD.ACCESS` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAD.AC.CARD.STATUS` | `CardAccess_CardStatus` | TField |  | Card Status |
| 2 | `CAD.AC.DISCLAIMER.FLAG` | `CardAccess_DisclaimerFlag` | TField |  | Field is used to store the Disclaimer Date for Member Direct |
| 3 | `CAD.AC.CUSTOMER` | `CardAccess_Customer` | TField |  | Field is used to store the Customer No.Should be always inputted with CIF.Validations - Valid CUSTOMER record. |
| 4 | `CAD.AC.INTERFACE` | `CardAccess_Interface` |  |  |  |
| 5 | `CAD.AC.WD.ONL.TXN.LIMIT` | `CardAccess_WdOnlTxnLimit` |  |  |  |
| 6 | `CAD.AC.WD.OFL.TXN.LIMIT` | `CardAccess_WdOflTxnLimit` |  |  |  |
| 7 | `CAD.AC.WD.ONL.DAY.LIMIT` | `CardAccess_WdOnlDayLimit` |  |  |  |
| 8 | `CAD.AC.WD.OFL.DAY.LIMIT` | `CardAccess_WdOflDayLimit` |  |  |  |
| 9 | `CAD.AC.DP.CS.THAMT.OUR` | `CardAccess_DpCsThamtOur` |  |  |  |
| 10 | `CAD.AC.DP.CS.THPCT.OUR` | `CardAccess_DpCsThpctOur` |  |  |  |
| 11 | `CAD.AC.DP.CS.HDAYS.OUR` | `CardAccess_DpCsHdaysOur` |  |  |  |
| 12 | `CAD.AC.DP.CS.THAMT.OTH` | `CardAccess_DpCsThamtOth` |  |  |  |
| 13 | `CAD.AC.DP.CS.THPCT.OTH` | `CardAccess_DpCsThpctOth` |  |  |  |
| 14 | `CAD.AC.DP.CS.HDAYS.OTH` | `CardAccess_DpCsHdaysOth` |  |  |  |
| 15 | `CAD.AC.DP.CQ.THAMT.OUR` | `CardAccess_DpCqThamtOur` |  |  |  |
| 16 | `CAD.AC.DP.CQ.THPCT.OUR` | `CardAccess_DpCqThpctOur` |  |  |  |
| 17 | `CAD.AC.DP.CQ.HDAYS.OUR` | `CardAccess_DpCqHdaysOur` |  |  |  |
| 18 | `CAD.AC.DP.CQ.THAMT.OTH` | `CardAccess_DpCqThamtOth` |  |  |  |
| 19 | `CAD.AC.DP.CQ.THPCT.OTH` | `CardAccess_DpCqThpctOth` |  |  |  |
| 20 | `CAD.AC.DP.CQ.HDAYS.OTH` | `CardAccess_DpCqHdaysOth` |  |  |  |
| 21 | `CAD.AC.ACCOUNT` | `CardAccess_Account` |  |  |  |
| 22 | `CAD.AC.AC.PRIME.CUST` | `CardAccess_AcPrimeCust` |  |  |  |
| 23 | `CAD.AC.BI.FLAG` | `CardAccess_BiFlag` |  |  |  |
| 24 | `CAD.AC.MS.FLAG` | `CardAccess_MsFlag` |  |  |  |
| 25 | `CAD.AC.WD.FLAG` | `CardAccess_WdFlag` |  |  |  |
| 26 | `CAD.AC.DP.FLAG` | `CardAccess_DpFlag` |  |  |  |
| 27 | `CAD.AC.TI.FLAG` | `CardAccess_TiFlag` |  |  |  |
| 28 | `CAD.AC.TO.FLAG` | `CardAccess_ToFlag` |  |  |  |
| 29 | `CAD.AC.BP.FLAG` | `CardAccess_BpFlag` |  |  |  |
| 30 | `CAD.AC.PU.FLAG` | `CardAccess_PuFlag` |  |  |  |
| 31 | `CAD.AC.EN.FLAG` | `CardAccess_EnFlag` |  |  |  |
| 32 | `CAD.AC.IMT.FLAG` | `CardAccess_ImtFlag` |  |  |  |
| 33 | `CAD.AC.AC.STATUS` | `CardAccess_AcStatus` |  |  |  |
| 34 | `CAD.AC.M2M.FLAG` | `CardAccess_M2mFlag` |  |  |  |
| 35 | `CAD.AC.APPROVAL.AMT` | `CardAccess_ApprovalAmt` |  |  |  |
| 36 | `CAD.AC.IMMEDIATE.STD.FLAG` | `CardAccess_ImmediateStdFlag` |  |  |  |
| 37 | `CAD.AC.LEVEL.DP.CS.AMT` | `CardAccess_LevelDpCsAmt` |  |  |  |
| 38 | `CAD.AC.DEP.CS.HDAYS.OUR` | `CardAccess_DepCsHdaysOur` |  |  |  |
| 39 | `CAD.AC.DEP.CS.HDAYS.OTH` | `CardAccess_DepCsHdaysOth` |  |  |  |
| 40 | `CAD.AC.LEVEL.DP.CQ.AMT` | `CardAccess_LevelDpCqAmt` |  |  |  |
| 41 | `CAD.AC.DEP.CQ.HDAYS.OUR` | `CardAccess_DepCqHdaysOur` |  |  |  |
| 42 | `CAD.AC.DEP.CQ.HDAYS.OTH` | `CardAccess_DepCqHdaysOth` |  |  |  |
| 43 | `CAD.AC.FHM.UPD.DTE` | `CardAccess_FhmUpdDte` | TField |  | Field which Holds the date on which the FHM update date.Valid date format. |
| 44 | `CAD.AC.ONLINE.UPDATE` | `CardAccess_OnlineUpdate` |  |  |  |
| 45 | `CAD.AC.UPD.DATE.TIME` | `CardAccess_UpdDateTime` |  |  |  |
| 46 | `CAD.AC.TXN.DATE` | `CardAccess_TxnDate` |  |  |  |
| 47 | `CAD.AC.NO.OF.WTHDR` | `CardAccess_NoOfWthdr` |  |  |  |
| 48 | `CAD.AC.DEPOSIT.AMT` | `CardAccess_DepositAmt` |  |  |  |
| 49 | `CAD.AC.RESERVED.20` | `CardAccess_Reserved20` |  |  |  |
| 50 | `CAD.AC.CARD.SEQ` | `CardAccess_CardSeq` |  |  |  |
| 51 | `CAD.AC.CARD.EXP.DATE` | `CardAccess_CardExpDate` |  |  |  |
| 52 | `CAD.AC.CARD.FORMAT` | `CardAccess_CardFormat` |  |  |  |
| 53 | `CAD.AC.ORDER.STATUS` | `CardAccess_OrderStatus` | TField |  | Field which Holds the order status of the card.Applicable before the card is issed to the actual customer. |
| 54 | `CAD.AC.FHM.UPDATED` | `CardAccess_FhmUpdated` | TField |  | Field which Holds the FHM update Status.Allowed inputs : UPDATED / FAILEDUPDATED - Card record selected and sent to FHM |
| 55 | `CAD.AC.ISSUE.DATE` | `CardAccess_IssueDate` | TField |  |  |
| 56 | `CAD.AC.LIMIT.SCORE` | `CardAccess_LimitScore` | TField |  |  |
| 57 | `CAD.AC.POS.ADJ.ONLDAY.LIM` | `CardAccess_PosAdjOnldayLim` | TField |  |  |
| 58 | `CAD.AC.POS.ADJ.OFFDAY.LIM` | `CardAccess_PosAdjOffdayLim` | TField |  |  |
| 59 | `CAD.AC.MOBILE.ACCESS` | `CardAccess_MobileAccess` | TField |  |  |
| 60 | `CAD.AC.MOBILE.BLOCK` | `CardAccess_MobileBlock` | TField |  |  |
| 61 | `CAD.AC.REQUESTED.DATE` | `CardAccess_RequestedDate` | TField |  | Field which Holds the card requested date.Valid date format field. |
| 62 | `CAD.AC.ORDERED.DATE` | `CardAccess_OrderedDate` | TField |  | Field which Holds the card ordered date.Valid date format field. |
| 63 | `CAD.AC.ACTIVATED.DATE` | `CardAccess_ActivatedDate` | TField |  | Field which Holds the card activated date.Valid date format field. |
| 64 | `CAD.AC.EXPIRY.DATE` | `CardAccess_ExpiryDate` | TField |  | Field which Holds the card expiry date.Valid date format field. |
| 65 | `CAD.AC.PIN.WINDOW.EXPIRY` | `CardAccess_PinWindowExpiry` | TField |  | field which Holds the Expiry of PIN window Like 1 hour, 5 Hour etceg. 5 |
| 66 | `CAD.AC.LAST.ATM.TXN.DATE` | `CardAccess_LastAtmTxnDate` |  |  |  |
| 67 | `CAD.AC.LAST.ATM.TXN.AMT` | `CardAccess_LastAtmTxnAmt` |  |  |  |
| 68 | `CAD.AC.LAST.POS.TXN.DATE` | `CardAccess_LastPosTxnDate` |  |  |  |
| 69 | `CAD.AC.LAST.POS.TXN.AMT` | `CardAccess_LastPosTxnAmt` |  |  |  |
| 70 | `CAD.AC.LAST.MDI.TXN.DATE` | `CardAccess_LastMdiTxnDate` |  |  |  |
| 71 | `CAD.AC.LAST.MDI.TXN.AMT` | `CardAccess_LastMdiTxnAmt` |  |  |  |
| 72 | `CAD.AC.LAST.IVR.TXN.DATE` | `CardAccess_LastIvrTxnDate` |  |  |  |
| 73 | `CAD.AC.LAST.IVR.TXN.AMT` | `CardAccess_LastIvrTxnAmt` |  |  |  |
| 74 | `CAD.AC.LAST.ATM.USE.DATE` | `CardAccess_LastAtmUseDate` | TField |  | Field which Holds the last ATM usage date.Valid date format field. |
| 75 | `CAD.AC.LAST.POS.USE.DATE` | `CardAccess_LastPosUseDate` | TField |  | Field which Holds the last POS usage date.Valid date format field. |
| 76 | `CAD.AC.LAST.ONLINE.USE.DATE` | `CardAccess_LastOnlineUseDate` | TField |  | Field which Holds the last ONLINE usage date.Valid date format field. |
| 77 | `CAD.AC.LAST.MOBILE.USE.DATE` | `CardAccess_LastMobileUseDate` | TField |  | Field which Holds the last MOBILE banking usage date.Valid date format field. |
| 78 | `CAD.AC.LAST.IVR.USE.DATE` | `CardAccess_LastIvrUseDate` | TField |  |  |
| 79 | `CAD.AC.MDSB.DISC.DATE` | `CardAccess_MdsbDiscDate` | TField |  |  |
| 80 | `CAD.AC.MDSB.OPTED` | `CardAccess_MdsbOpted` | TField |  |  |
| 81 | `CAD.AC.MDSB.REMIND.DATE` | `CardAccess_MdsbRemindDate` | TField |  |  |
| 82 | `CAD.AC.NT.ACTIVE.DATE` | `CardAccess_NtActiveDate` | TField |  | Field which Holds the card activation date, which is activated after the Watch status.Applicable for the card moved to WATCH status.Valid date format field. |
| 83 | `CAD.AC.WATCH.DATE` | `CardAccess_WatchDate` | TField |  | field which Holds the date on which the card is moved to WATCH status.Valid date format field. |
| 84 | `CAD.AC.INTERAC.FLASH` | `CardAccess_InteracFlash` | TField |  | Field is Used to indicate whether the card is a flash card or notdefaulted from CARD.FORMATallowed inputs : YES / NOYES - Card with interac flash access and details part of CAF and FHMNo - Card is without interac flash access.Validation - Allowed to amend at card access level. If NO is defined at card format level, user will be thrown with a warning message that card is not enabled for flash access |
| 85 | `CAD.AC.DEF.ACCT.TYPE` | `CardAccess_DefAcctType` | TField |  | The Purpose of this field is to capture the default account type in CAF/FHM during the card issuance, modifications, re-issuance etc.Based on the value defined, the default account type, it will be reported in Full CAF, Partial CAF and FHM messagesValid values as 'C', 'S' and NoneC- Chequing AccountS - Savings Account.Validations:If C is selected, system validates any Chequing Account is available in the card, else warning will be thrown.If S is selected, system validates any Savings Account is available in the card, else warning will be thrown.If it is selected as C -then Default account type will be mapped as 20 in Full CAF,Partial CAF and FHM MessagesIf it is selected as S - Default account type will be mapped as 10 in Full CAF,Partial CAF and FHM MessagesIf it is selected as None- Default account type will be mapped based on CARD.ACCESS>EN.FLAG |
| 86 | `CAD.AC.RESERVED.9` | `CardAccess_Reserved9` |  |  |  |
| 87 | `CAD.AC.RESERVED.8` | `CardAccess_Reserved8` | TField |  |  |
| 88 | `CAD.AC.RESERVED.7` | `CardAccess_Reserved7` | TField |  |  |
| 89 | `CAD.AC.RESERVED.6` | `CardAccess_Reserved6` | TField |  |  |
| 90 | `CAD.AC.RESERVED.5` | `CardAccess_Reserved5` | TField |  |  |
| 91 | `CAD.AC.RESERVED.4` | `CardAccess_Reserved4` | TField |  |  |
| 92 | `CAD.AC.RESERVED.3` | `CardAccess_Reserved3` | TField |  |  |
| 93 | `CAD.AC.LOCAL.REF` | `CardAccess_LocalRef` |  |  |  |
| 94 | `CAD.AC.OVERRIDE` | `CardAccess_Override` |  |  |  |
| 95 | `CAD.AC.RECORD.STATUS` | `CardAccess_RecordStatus` | String |  |  |
| 96 | `CAD.AC.CURR.NO` | `CardAccess_CurrNo` | String |  |  |
| 97 | `CAD.AC.INPUTTER` | `CardAccess_Inputter` |  |  |  |
| 98 | `CAD.AC.DATE.TIME` | `CardAccess_DateTime` |  |  |  |
| 99 | `CAD.AC.AUTHORISER` | `CardAccess_Authoriser` | String |  |  |
| 100 | `CAD.AC.CO.CODE` | `CardAccess_CoCode` | String |  |  |
| 101 | `CAD.AC.DEPT.CODE` | `CardAccess_DeptCode` | String |  |  |
| 102 | `CAD.AC.AUDITOR.CODE` | `CardAccess_AuditorCode` | String |  |  |
| 103 | `CAD.AC.AUDIT.DATE.TIME` | `CardAccess_AuditDateTime` | String |  |  |
