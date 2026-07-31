# LC.ACCOUNT.BALANCES — Table Schema

> Source: `INSERTS/I_F.LC.ACCOUNT.BALANCES` in `LC_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LCAC.CURRENCY` | `LcAccountBalances_Currency` | TField |  | Identifies the currency of the Letter of Credit contract. This item is taken from the parent Letter of Credit file from the LC.CURRENCY field. Validation Rules: CCY (Currency code e.g. GBP must be 3). System Generated. The field will be calculated by the system and no operator input will be allowed. |
| 2 | `LCAC.ISSUE.DATE` | `LcAccountBalances_IssueDate` | TField |  | Identifies the issue date of the Letter of Credit contract. The item is taken from the parent Letter of Credit file from the ISSUE.DATE field. Validation Rules: Standard date format. System generated. The field will be calculated by the system and no operator input will be allowed. |
| 3 | `LCAC.EXPIRY.DATE` | `LcAccountBalances_ExpiryDate` | TField |  | Identifies the expiry date of the Letter of Credit contract. This item is taken from the parent Letter of Credit file from the EXPIRY.DATE field. Validation Rules: Standard date format. System generated. The field will be calculated by the system and no operator input will be allowed. |
| 4 | `LCAC.LC.AMOUNT` | `LcAccountBalances_LcAmount` | TField |  | Identifies the amount of the Letter of Credit contract. The item is taken from the parent Letter of Credit file from the LC.AMOUNT field. Validation Rules: Standard amount format. System generated. The field will be calculated by the system and no operator input will be allowed. |
| 5 | `LCAC.CHRG.AMT.DUE` | `LcAccountBalances_ChrgAmtDue` |  |  |  |
| 6 | `LCAC.CHRG.DATE.DUE` | `LcAccountBalances_ChrgDateDue` |  |  |  |
| 7 | `LCAC.CHRG.CODE` | `LcAccountBalances_ChrgCode` |  |  |  |
| 8 | `LCAC.CHRG.CCY` | `LcAccountBalances_ChrgCcy` |  |  |  |
| 9 | `LCAC.PARTY.CHRG` | `LcAccountBalances_PartyChrg` |  |  |  |
| 10 | `LCAC.CHRG.REL.DRAW` | `LcAccountBalances_ChrgRelDraw` |  |  |  |
| 11 | `LCAC.AMT.REC` | `LcAccountBalances_AmtRec` |  |  |  |
| 12 | `LCAC.CHG.PAID.IN.ADV` | `LcAccountBalances_ChgPaidInAdv` |  |  |  |
| 13 | `LCAC.AMORT.AMOUNT` | `LcAccountBalances_AmortAmount` |  |  |  |
| 14 | `LCAC.NO.OF.MTHS.LEFT` | `LcAccountBalances_NoOfMthsLeft` |  |  |  |
| 15 | `LCAC.AMORT.ORIGN.MTH` | `LcAccountBalances_AmortOrignMth` |  |  |  |
| 16 | `LCAC.AMORT.AMT.TO.DT` | `LcAccountBalances_AmortAmtToDt` |  |  |  |
| 17 | `LCAC.AMRT.AMT.DTE.LC` | `LcAccountBalances_AmrtAmtDteLc` |  |  |  |
| 18 | `LCAC.CHRG.ACC.AMT` | `LcAccountBalances_ChrgAccAmt` |  |  |  |
| 19 | `LCAC.CHRG.LCCY.AMT` | `LcAccountBalances_ChrgLccyAmt` |  |  |  |
| 20 | `LCAC.CHRG.STATUS` | `LcAccountBalances_ChrgStatus` |  |  |  |
| 21 | `LCAC.INST.CHARGE` | `LcAccountBalances_InstCharge` |  |  |  |
| 22 | `LCAC.CHARGE.INST.NO` | `LcAccountBalances_ChargeInstNo` |  |  |  |
| 23 | `LCAC.REFUND.OPTION` | `LcAccountBalances_RefundOption` |  |  |  |
| 24 | `LCAC.REFUND.DESC` | `LcAccountBalances_RefundDesc` |  |  |  |
| 25 | `LCAC.REFUND.AMT` | `LcAccountBalances_RefundAmt` |  |  |  |
| 26 | `LCAC.REAL.RF.AMT` | `LcAccountBalances_RealRfAmt` |  |  |  |
| 27 | `LCAC.UNREAL.RF.AMT` | `LcAccountBalances_UnrealRfAmt` |  |  |  |
| 28 | `LCAC.CLAIM.STLE.AMT` | `LcAccountBalances_ClaimStleAmt` |  |  |  |
| 29 | `LCAC.SETTLE.AC.FROM` | `LcAccountBalances_SettleAcFrom` |  |  |  |
| 30 | `LCAC.CLAIM.DIFF.AMT` | `LcAccountBalances_ClaimDiffAmt` |  |  |  |
| 31 | `LCAC.CLAIM.DIFF.ACC` | `LcAccountBalances_ClaimDiffAcc` |  |  |  |
| 32 | `LCAC.RESERVED11` | `LcAccountBalances_Reserved11` |  |  |  |
| 33 | `LCAC.RESERVED12` | `LcAccountBalances_Reserved12` |  |  |  |
| 34 | `LCAC.RESERVED13` | `LcAccountBalances_Reserved13` |  |  |  |
| 35 | `LCAC.DATE.RECEIVED` | `LcAccountBalances_DateReceived` |  |  |  |
| 36 | `LCAC.CHRG.XCHG.RATE` | `LcAccountBalances_ChrgXchgRate` |  |  |  |
| 37 | `LCAC.CHRG.PERC.RATE` | `LcAccountBalances_ChrgPercRate` |  |  |  |
| 38 | `LCAC.CHRG.PERIOD` | `LcAccountBalances_ChrgPeriod` |  |  |  |
| 39 | `LCAC.PARTICIPANT` | `LcAccountBalances_Participant` |  |  |  |
| 40 | `LCAC.PART.SHARE` | `LcAccountBalances_PartShare` |  |  |  |
| 41 | `LCAC.PART.CHG.AMT` | `LcAccountBalances_PartChgAmt` |  |  |  |
| 42 | `LCAC.TF.REFERENCE` | `LcAccountBalances_TfReference` |  |  |  |
| 43 | `LCAC.TAX.CODE` | `LcAccountBalances_TaxCode` |  |  |  |
| 44 | `LCAC.TAX.CODE.CCY` | `LcAccountBalances_TaxCodeCcy` |  |  |  |
| 45 | `LCAC.TAX.AMT` | `LcAccountBalances_TaxAmt` |  |  |  |
| 46 | `LCAC.TAX.PARTY.CHRG` | `LcAccountBalances_TaxPartyChrg` |  |  |  |
| 47 | `LCAC.TAX.REL.DRAW` | `LcAccountBalances_TaxRelDraw` |  |  |  |
| 48 | `LCAC.TAX.ACC.AMT` | `LcAccountBalances_TaxAccAmt` |  |  |  |
| 49 | `LCAC.TAX.LCCY.AMT` | `LcAccountBalances_TaxLccyAmt` |  |  |  |
| 50 | `LCAC.TAX.CHRG.STATUS` | `LcAccountBalances_TaxChrgStatus` |  |  |  |
| 51 | `LCAC.TAX.DR.ACCT` | `LcAccountBalances_TaxDrAcct` |  |  |  |
| 52 | `LCAC.PART.ID` | `LcAccountBalances_PartId` |  |  |  |
| 53 | `LCAC.PART.TAX.AMT` | `LcAccountBalances_PartTaxAmt` |  |  |  |
| 54 | `LCAC.CHG.CODE` | `LcAccountBalances_ChgCode` |  |  |  |
| 55 | `LCAC.TAX.DATE` | `LcAccountBalances_TaxDate` |  |  |  |
| 56 | `LCAC.CONSOL.KEY` | `LcAccountBalances_ConsolKey` |  |  |  |
| 57 | `LCAC.CONFIRM.FLAT.CODE` | `LcAccountBalances_ConfirmFlatCode` | TField |  | A number generated automatically by the system which identifies either a statement entry or a category entry in respect of these charges. The system will automatically insert a number into this field and this number may refer to a statement entry or a category entry depending on the value contained in the corresponding multivalue fields. Validation Rules: Internal multivalue field. The field will be calculated by the system and no operator input will be allowed. |
| 58 | `LCAC.CONFIRM.FLAT.CHG` | `LcAccountBalances_ConfirmFlatChg` | TField |  | Contains all the override messages which the user agreed to during input of the Drawing. The field will be updated by the system and no operator input will be allowed. During the validation of a Letters of Credit/Documentary Collection, the system may provide the user with a series of screen messages to indicate an anomaly, for instance, that the expiry date of the L/C exceeds the issue date by more than 1 year. In the event that the user confirms the override, the full text of the actual override message will be stored, for reference purposes only, in this multivalued field. For example, if the user inputs an expiry date that is more than 1 year greater than the issue date, then when the L/C if validated a warning bell will sould and a message will appear at the foot of the screen which reads: 'EXPIRY DATE EXCEEDS ISSUE DATE BY 1 YEAR' This will draw the users attention to the override entry(s). After checking and making only necessary amendments the user then approves the transaction. Validation Rules: Internal multivalue field. |
| 59 | `LCAC.CON.START.PERD` | `LcAccountBalances_ConStartPerd` |  |  |  |
| 60 | `LCAC.CON.END.PERIOD` | `LcAccountBalances_ConEndPeriod` |  |  |  |
| 61 | `LCAC.CON.PRIN.AMT` | `LcAccountBalances_ConPrinAmt` |  |  |  |
| 62 | `LCAC.CON.COMM.TODATE` | `LcAccountBalances_ConCommTodate` |  |  |  |
| 63 | `LCAC.CON.COMM.PCT` | `LcAccountBalances_ConCommPct` |  |  |  |
| 64 | `LCAC.CON.PARTY.CHRG` | `LcAccountBalances_ConPartyChrg` |  |  |  |
| 65 | `LCAC.CON.REL.DRAW` | `LcAccountBalances_ConRelDraw` |  |  |  |
| 66 | `LCAC.CONFIRM.STATUS` | `LcAccountBalances_ConfirmStatus` |  |  |  |
| 67 | `LCAC.CON.COMM.CODE` | `LcAccountBalances_ConCommCode` |  |  |  |
| 68 | `LCAC.CON.SET.AC.FR` | `LcAccountBalances_ConSetAcFr` |  |  |  |
| 69 | `LCAC.OPEN.FLAT.CODE` | `LcAccountBalances_OpenFlatCode` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 11 characters may be entered. This is a NOINPUT field. |
| 70 | `LCAC.OPEN.FLAT.CHG` | `LcAccountBalances_OpenFlatChg` | TField |  | Validation Rules: A maximum of 19 characters may be entered. This is a NOINPUT field. |
| 71 | `LCAC.OPN.START.PERD` | `LcAccountBalances_OpnStartPerd` |  |  |  |
| 72 | `LCAC.OPN.END.PERIOD` | `LcAccountBalances_OpnEndPeriod` |  |  |  |
| 73 | `LCAC.OPN.PRIN.AMT` | `LcAccountBalances_OpnPrinAmt` |  |  |  |
| 74 | `LCAC.OPN.COMM.TODATE` | `LcAccountBalances_OpnCommTodate` |  |  |  |
| 75 | `LCAC.OPN.COMM.PCT` | `LcAccountBalances_OpnCommPct` |  |  |  |
| 76 | `LCAC.OPN.PARTY.CHRG` | `LcAccountBalances_OpnPartyChrg` |  |  |  |
| 77 | `LCAC.OPN.REL.DRAW` | `LcAccountBalances_OpnRelDraw` |  |  |  |
| 78 | `LCAC.OPEN.STATUS` | `LcAccountBalances_OpenStatus` |  |  |  |
| 79 | `LCAC.OPN.COMM.CODE` | `LcAccountBalances_OpnCommCode` |  |  |  |
| 80 | `LCAC.OPN.SET.AC.FR` | `LcAccountBalances_OpnSetAcFr` |  |  |  |
| 81 | `LCAC.ACCR.CYCLE.COMM` | `LcAccountBalances_AccrCycleComm` | TField |  | Validation Rules: A maximum of 19 characters may be entered. This is a NOINPUT field. |
| 82 | `LCAC.LOCAL.REF` | `LcAccountBalances_LocalRef` |  |  |  |
| 83 | `LCAC.DELIVERY.REF` | `LcAccountBalances_DeliveryRef` |  |  |  |
| 84 | `LCAC.EB.ADV.NO` | `LcAccountBalances_EbAdvNo` |  |  |  |
| 85 | `LCAC.MESSAGE.TYPE` | `LcAccountBalances_MessageType` |  |  |  |
| 86 | `LCAC.MSG.CLASS.NO` | `LcAccountBalances_MsgClassNo` |  |  |  |
| 87 | `LCAC.OVR.CARRIER` | `LcAccountBalances_OvrCarrier` |  |  |  |
| 88 | `LCAC.ADDRESSEE` | `LcAccountBalances_Addressee` |  |  |  |
| 89 | `LCAC.SEND.MESSAGE` | `LcAccountBalances_SendMessage` |  |  |  |
| 90 | `LCAC.RESERVED3` | `LcAccountBalances_Reserved3` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 91 | `LCAC.RESERVED4` | `LcAccountBalances_Reserved4` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 92 | `LCAC.RESERVED5` | `LcAccountBalances_Reserved5` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 93 | `LCAC.STMT.NO` | `LcAccountBalances_StmtNo` |  |  |  |
| 94 | `LCAC.OVERRIDE` | `LcAccountBalances_Override` |  |  |  |
| 95 | `LCAC.RECORD.STATUS` | `LcAccountBalances_RecordStatus` | String |  |  |
| 96 | `LCAC.CURR.NO` | `LcAccountBalances_CurrNo` | String |  |  |
| 97 | `LCAC.INPUTTER` | `LcAccountBalances_Inputter` |  |  |  |
| 98 | `LCAC.DATE.TIME` | `LcAccountBalances_DateTime` |  |  |  |
| 99 | `LCAC.AUTHORISER` | `LcAccountBalances_Authoriser` | String |  |  |
| 100 | `LCAC.CO.CODE` | `LcAccountBalances_CoCode` | String |  |  |
| 101 | `LCAC.DEPT.CODE` | `LcAccountBalances_DeptCode` | String |  |  |
| 102 | `LCAC.AUDITOR.CODE` | `LcAccountBalances_AuditorCode` | String |  |  |
| 103 | `LCAC.AUDIT.DATE.TIME` | `LcAccountBalances_AuditDateTime` | String |  |  |
