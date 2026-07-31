# ATM.CHG.TABLE — Table Schema

> Source: `INSERTS/I_F.ATM.CHG.TABLE` in `ATMFRM_Charges.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ATM.CHG.DESCRIPTION` | `AtmChgTable_Description` |  |  |  |
| 2 | `ATM.CHG.CHG.CHANNEL` | `AtmChgTable_ChgChannel` |  |  |  |
| 3 | `ATM.CHG.FLD.POS.RTN` | `AtmChgTable_FldPosRtn` |  |  |  |
| 4 | `ATM.CHG.CHG.ID.RULE` | `AtmChgTable_ChgIdRule` |  |  |  |
| 5 | `ATM.CHG.CHARGE.DESC` | `AtmChgTable_ChargeDesc` |  |  |  |
| 6 | `ATM.CHG.SEPARATE.FT` | `AtmChgTable_SeparateFt` |  |  |  |
| 7 | `ATM.CHG.TRAN.MTI` | `AtmChgTable_TranMti` |  |  |  |
| 8 | `ATM.CHG.PROC.CODE` | `AtmChgTable_ProcCode` |  |  |  |
| 9 | `ATM.CHG.BIN.NO` | `AtmChgTable_BinNo` |  |  |  |
| 10 | `ATM.CHG.TXN.CCY` | `AtmChgTable_TxnCcy` |  |  |  |
| 11 | `ATM.CHG.SPLIT.CHG.ID` | `AtmChgTable_SplitChgId` |  |  |  |
| 12 | `ATM.CHG.CHG.AMT` | `AtmChgTable_ChgAmt` |  |  |  |
| 13 | `ATM.CHG.CHG.AMT.POSN` | `AtmChgTable_ChgAmtPosn` |  |  |  |
| 14 | `ATM.CHG.CHG.PERC` | `AtmChgTable_ChgPerc` |  |  |  |
| 15 | `ATM.CHG.CHARGE.TYPE` | `AtmChgTable_ChargeType` |  |  |  |
| 16 | `ATM.CHG.DR.ACCT.TYPE` | `AtmChgTable_DrAcctType` |  |  |  |
| 17 | `ATM.CHG.CHG.DR.ACCT` | `AtmChgTable_ChgDrAcct` |  |  |  |
| 18 | `ATM.CHG.CHG.CR.ACCT` | `AtmChgTable_ChgCrAcct` |  |  |  |
| 19 | `ATM.CHG.NETWORK.TYPE` | `AtmChgTable_NetworkType` |  |  |  |
| 20 | `ATM.CHG.TXN.LIMIT.AMT` | `AtmChgTable_TxnLimitAmt` |  |  |  |
| 21 | `ATM.CHG.RESERVED.14` | `AtmChgTable_Reserved14` |  |  |  |
| 22 | `ATM.CHG.RESERVED.13` | `AtmChgTable_Reserved13` |  |  |  |
| 23 | `ATM.CHG.RESERVED.12` | `AtmChgTable_Reserved12` |  |  |  |
| 24 | `ATM.CHG.CHG.VERSION` | `AtmChgTable_ChgVersion` | TField |  |  |
| 25 | `ATM.CHG.CHG.CODE` | `AtmChgTable_ChgCode` | TField |  |  |
| 26 | `ATM.CHG.RESERVATION.CHARGES.API` | `AtmChgTable_ReservationChargesApi` | TField |  |  |
| 27 | `ATM.CHG.NON.FIN.CHARGE` | `AtmChgTable_NonFinCharge` | TField |  |  |
| 28 | `ATM.CHG.RESERVED.9` | `AtmChgTable_Reserved9` | TField |  |  |
| 29 | `ATM.CHG.RESERVED.8` | `AtmChgTable_Reserved8` | TField |  |  |
| 30 | `ATM.CHG.RESERVED.7` | `AtmChgTable_Reserved7` | TField |  |  |
| 31 | `ATM.CHG.RESERVED.6` | `AtmChgTable_Reserved6` | TField |  |  |
| 32 | `ATM.CHG.LOCAL.REF` | `AtmChgTable_LocalRef` |  |  |  |
| 33 | `ATM.CHG.RESERVED.5` | `AtmChgTable_Reserved5` | TField |  |  |
| 34 | `ATM.CHG.RESERVED.4` | `AtmChgTable_Reserved4` | TField |  |  |
| 35 | `ATM.CHG.RESERVED.3` | `AtmChgTable_Reserved3` | TField |  |  |
| 36 | `ATM.CHG.RESERVED.2` | `AtmChgTable_Reserved2` | TField |  |  |
| 37 | `ATM.CHG.RESERVED.1` | `AtmChgTable_Reserved1` | TField |  |  |
| 38 | `ATM.CHG.RECORD.STATUS` | `AtmChgTable_RecordStatus` | String |  |  |
| 39 | `ATM.CHG.CURR.NO` | `AtmChgTable_CurrNo` | String |  |  |
| 40 | `ATM.CHG.INPUTTER` | `AtmChgTable_Inputter` |  |  |  |
| 41 | `ATM.CHG.DATE.TIME` | `AtmChgTable_DateTime` |  |  |  |
| 42 | `ATM.CHG.AUTHORISER` | `AtmChgTable_Authoriser` | String |  |  |
| 43 | `ATM.CHG.CO.CODE` | `AtmChgTable_CoCode` | String |  |  |
| 44 | `ATM.CHG.DEPT.CODE` | `AtmChgTable_DeptCode` | String |  |  |
| 45 | `ATM.CHG.AUDITOR.CODE` | `AtmChgTable_AuditorCode` | String |  |  |
| 46 | `ATM.CHG.AUDIT.DATE.TIME` | `AtmChgTable_AuditDateTime` | String |  |  |
