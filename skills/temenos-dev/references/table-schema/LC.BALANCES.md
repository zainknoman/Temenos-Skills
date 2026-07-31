# LC.BALANCES — Table Schema

> Source: `INSERTS/I_F.LC.BALANCES` in `LC_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LC.BAL.CURRENCY` | `LcBalances_Currency` | TField |  | Indicates the currency of the LETTER.OF.CREDIT. Validation Rules: System updated field. Noinput field. |
| 2 | `LC.BAL.LC.INIT.AMOUNT` | `LcBalances_LcInitAmount` | TField |  | Indicates the original LC amount when LC was issued. Validation Rules: System updated field. Noinput field. |
| 3 | `LC.BAL.LC.OUTS.AMOUNT` | `LcBalances_LcOutsAmount` | TField |  | Indicates the current LC outstanding amount available for drawings.Whenever drawings is made under LC, the oustanding amount will be reduced. Validation Rules: System updated field. Noinput field. |
| 4 | `LC.BAL.CONFIRMATION.AMT` | `LcBalances_ConfirmationAmt` | TField |  | Indicates the amount of confirmation provided on total LC amount. Validation Rules: System updated field. Noinput field. |
| 5 | `LC.BAL.APPLICATION` | `LcBalances_Application` |  |  |  |
| 6 | `LC.BAL.AMT.MOVED` | `LcBalances_AmtMoved` |  |  |  |
| 7 | `LC.BAL.EFF.DATE` | `LcBalances_EffDate` |  |  |  |
| 8 | `LC.BAL.PARTICIPANT` | `LcBalances_Participant` |  |  |  |
| 9 | `LC.BAL.PART.SHARE` | `LcBalances_PartShare` |  |  |  |
| 10 | `LC.BAL.PART.AMOUNT` | `LcBalances_PartAmount` |  |  |  |
| 11 | `LC.BAL.PART.OUTS.AMT` | `LcBalances_PartOutsAmt` |  |  |  |
| 12 | `LC.BAL.LAST.BS.DATE` | `LcBalances_LastBsDate` | TField |  | Holds the date of last contingent BUY or SELL movement for Syndicated LC�s done through SL.BUY.SELL application. System maintained field. |
| 13 | `LC.BAL.DR.REFERENCE` | `LcBalances_DrReference` |  |  |  |
| 14 | `LC.BAL.INST.NO` | `LcBalances_InstNo` |  |  |  |
| 15 | `LC.BAL.INST.DATE` | `LcBalances_InstDate` |  |  |  |
| 16 | `LC.BAL.INST.AMT` | `LcBalances_InstAmt` |  |  |  |
| 17 | `LC.BAL.PROV.REL.AMT` | `LcBalances_ProvRelAmt` |  |  |  |
| 18 | `LC.BAL.COVER.AMT` | `LcBalances_CoverAmt` |  |  |  |
| 19 | `LC.BAL.PAYMENT.TYPE` | `LcBalances_PaymentType` |  |  |  |
| 20 | `LC.BAL.DISC.AMT` | `LcBalances_DiscAmt` |  |  |  |
| 21 | `LC.BAL.LOAD.AMT` | `LcBalances_LoadAmt` |  |  |  |
| 22 | `LC.BAL.INST.TM.BAND` | `LcBalances_InstTmBand` |  |  |  |
| 23 | `LC.BAL.CUS.VALUE.DATE` | `LcBalances_CusValueDate` |  |  |  |
| 24 | `LC.BAL.RESERVED2` | `LcBalances_Reserved2` |  |  |  |
| 25 | `LC.BAL.RESERVED1` | `LcBalances_Reserved1` |  |  |  |
| 26 | `LC.BAL.INST.PRC.DT` | `LcBalances_InstPrcDt` |  |  |  |
| 27 | `LC.BAL.AMD.NO` | `LcBalances_AmdNo` |  |  |  |
| 28 | `LC.BAL.AMD.AMT` | `LcBalances_AmdAmt` |  |  |  |
| 29 | `LC.BAL.AMD.DATE` | `LcBalances_AmdDate` |  |  |  |
| 30 | `LC.BAL.AMD.ADV.EXP.DT` | `LcBalances_AmdAdvExpDt` |  |  |  |
| 31 | `LC.BAL.AMD.STATUS` | `LcBalances_AmdStatus` |  |  |  |
| 32 | `LC.BAL.DRAW.TYPE` | `LcBalances_DrawType` |  |  |  |
| 33 | `LC.BAL.DRAW.CCY` | `LcBalances_DrawCcy` |  |  |  |
| 34 | `LC.BAL.DRAW.AMT` | `LcBalances_DrawAmt` |  |  |  |
| 35 | `LC.BAL.DRAW.REFERENCE` | `LcBalances_DrawReference` |  |  |  |
| 36 | `LC.BAL.DRAW.DATE` | `LcBalances_DrawDate` |  |  |  |
| 37 | `LC.BAL.OVER.DRAW.AMT` | `LcBalances_OverDrawAmt` |  |  |  |
