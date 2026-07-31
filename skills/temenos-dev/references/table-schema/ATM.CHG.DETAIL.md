# ATM.CHG.DETAIL — Table Schema

> Source: `INSERTS/I_F.ATM.CHG.DETAIL` in `ATMFRM_Charges.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AT.CHG.CHARGE.DESC` | `AtmChgDetail_ChargeDesc` |  |  |  |
| 2 | `AT.CHG.SEPARATE.FT` | `AtmChgDetail_SeparateFt` |  |  |  |
| 3 | `AT.CHG.TRAN.MTI` | `AtmChgDetail_TranMti` |  |  |  |
| 4 | `AT.CHG.PROC.CODE` | `AtmChgDetail_ProcCode` |  |  |  |
| 5 | `AT.CHG.BIN.NO` | `AtmChgDetail_BinNo` |  |  |  |
| 6 | `AT.CHG.TXN.CCY` | `AtmChgDetail_TxnCcy` |  |  |  |
| 7 | `AT.CHG.SPLIT.CHG.ID` | `AtmChgDetail_SplitChgId` |  |  |  |
| 8 | `AT.CHG.CHG.AMT` | `AtmChgDetail_ChgAmt` |  |  |  |
| 9 | `AT.CHG.CHG.AMT.POSN` | `AtmChgDetail_ChgAmtPosn` |  |  |  |
| 10 | `AT.CHG.CHG.PERC` | `AtmChgDetail_ChgPerc` |  |  |  |
| 11 | `AT.CHG.CHARGE.TYPE` | `AtmChgDetail_ChargeType` |  |  |  |
| 12 | `AT.CHG.DR.ACCT.TYPE` | `AtmChgDetail_DrAcctType` |  |  |  |
| 13 | `AT.CHG.CHG.DR.ACCT` | `AtmChgDetail_ChgDrAcct` |  |  |  |
| 14 | `AT.CHG.CHG.CR.ACCT` | `AtmChgDetail_ChgCrAcct` |  |  |  |
| 15 | `AT.CHG.NETWORK.TYPE` | `AtmChgDetail_NetworkType` |  |  |  |
| 16 | `AT.CHG.TXN.LIMIT.AMT` | `AtmChgDetail_TxnLimitAmt` |  |  |  |
| 17 | `AT.CHG.FLD.POS.RTN` | `AtmChgDetail_AtChgFldPosRoutine` |  |  |  |
| 18 | `AT.CHG.CHG.CHANNEL` | `AtmChgDetail_AtmChgChgChannel` |  |  |  |
| 19 | `AT.CHG.LOCAL.REF` | `AtmChgDetail_LocalRef` |  |  |  |
| 20 | `AT.CHG.RESERVED.10` | `AtmChgDetail_Reserved10` | TField |  |  |
| 21 | `AT.CHG.RESERVED.9` | `AtmChgDetail_Reserved9` | TField |  |  |
| 22 | `AT.CHG.RESERVED.8` | `AtmChgDetail_Reserved8` | TField |  |  |
| 23 | `AT.CHG.RESERVED.7` | `AtmChgDetail_Reserved7` | TField |  |  |
| 24 | `AT.CHG.RESERVED.6` | `AtmChgDetail_Reserved6` | TField |  |  |
| 25 | `AT.CHG.RESERVED.5` | `AtmChgDetail_Reserved5` | TField |  |  |
