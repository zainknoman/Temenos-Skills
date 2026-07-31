# SC.GROUP.POS.ASSET — Table Schema

> Source: `INSERTS/I_F.SC.GROUP.POS.ASSET` in `SC_ScvValuationUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.GPA.APPLICATION` | `ScGroupPosAsset_Application` |  |  |  |
| 2 | `SC.GPA.SECURITY.NO` | `ScGroupPosAsset_SecurityNo` |  |  |  |
| 3 | `SC.GPA.SECURITY.CCY` | `ScGroupPosAsset_SecurityCcy` |  |  |  |
| 4 | `SC.GPA.NO.NOMINAL` | `ScGroupPosAsset_NoNominal` |  |  |  |
| 5 | `SC.GPA.ESTIMATION` | `ScGroupPosAsset_Estimation` |  |  |  |
| 6 | `SC.GPA.MARGIN.VALUE` | `ScGroupPosAsset_MarginValue` |  |  |  |
| 7 | `SC.GPA.TOT.UNRL.MKT` | `ScGroupPosAsset_TotUnrlMkt` |  |  |  |
| 8 | `SC.GPA.TOT.UNRL.CCY` | `ScGroupPosAsset_TotUnrlCcy` |  |  |  |
| 9 | `SC.GPA.TOP.UP.MARGIN.AMT` | `ScGroupPosAsset_TopUpMarginAmt` |  |  |  |
| 10 | `SC.GPA.SELL.OUT.MARGN.AMT` | `ScGroupPosAsset_SellOutMargnAmt` |  |  |  |
| 11 | `SC.GPA.INIT.MGN.VALUE` | `ScGroupPosAsset_InitMgnValue` |  |  |  |
| 12 | `SC.GPA.MV.MARGIN.AMT` | `ScGroupPosAsset_MvMarginAmt` |  |  |  |
| 13 | `SC.GPA.EQ.MARGIN.AMT` | `ScGroupPosAsset_EqMarginAmt` |  |  |  |
| 14 | `SC.GPA.SECOND.MRKT.VALUE` | `ScGroupPosAsset_SecondMrktValue` |  |  |  |
| 15 | `SC.GPA.DEPOSITORY` | `ScGroupPosAsset_Depository` |  |  |  |
| 16 | `SC.GPA.INDEX` | `ScGroupPosAsset_Index` |  |  |  |
| 17 | `SC.GPA.SOURCE.ID` | `ScGroupPosAsset_SourceId` |  |  |  |
| 18 | `SC.GPA.ACCRUED.INT` | `ScGroupPosAsset_AccruedInt` |  |  |  |
| 19 | `SC.GPA.ACCR.DIV` | `ScGroupPosAsset_AccrDiv` |  |  |  |
| 20 | `SC.GPA.RESERVED.15` | `ScGroupPosAsset_Reserved15` |  |  |  |
| 21 | `SC.GPA.RESERVED.14` | `ScGroupPosAsset_Reserved14` |  |  |  |
| 22 | `SC.GPA.RESERVED.13` | `ScGroupPosAsset_Reserved13` |  |  |  |
| 23 | `SC.GPA.RESERVED.12` | `ScGroupPosAsset_Reserved12` |  |  |  |
| 24 | `SC.GPA.RESERVED.11` | `ScGroupPosAsset_Reserved11` |  |  |  |
| 25 | `SC.GPA.MASTER.PORTFOLIO` | `ScGroupPosAsset_MasterPortfolio` | TField |  | Id of the master portfolio |
| 26 | `SC.GPA.RESERVED.10` | `ScGroupPosAsset_Reserved10` | TField |  |  |
| 27 | `SC.GPA.RESERVED.9` | `ScGroupPosAsset_Reserved9` | TField |  |  |
| 28 | `SC.GPA.RESERVED.8` | `ScGroupPosAsset_Reserved8` | TField |  |  |
| 29 | `SC.GPA.RESERVED.7` | `ScGroupPosAsset_Reserved7` | TField |  |  |
| 30 | `SC.GPA.RESERVED.6` | `ScGroupPosAsset_Reserved6` | TField |  |  |
| 31 | `SC.GPA.RESERVED.5` | `ScGroupPosAsset_Reserved5` | TField |  |  |
| 32 | `SC.GPA.RESERVED.4` | `ScGroupPosAsset_Reserved4` | TField |  |  |
| 33 | `SC.GPA.RESERVED.3` | `ScGroupPosAsset_Reserved3` | TField |  |  |
| 34 | `SC.GPA.RESERVED.2` | `ScGroupPosAsset_Reserved2` | TField |  |  |
| 35 | `SC.GPA.RESERVED.1` | `ScGroupPosAsset_Reserved1` | TField |  |  |
