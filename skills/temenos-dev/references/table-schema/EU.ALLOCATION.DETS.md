# EU.ALLOCATION.DETS — Table Schema

> Source: `INSERTS/I_F.EU.ALLOCATION.DETS` in `ET_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EU.ALD.CR.TXN.REF` | `EuAllocationDets_CrTxnRef` |  |  |  |
| 2 | `EU.ALD.CR.TXN.DATE` | `EuAllocationDets_CrTxnDate` |  |  |  |
| 3 | `EU.ALD.CR.NOMINAL` | `EuAllocationDets_CrNominal` |  |  |  |
| 4 | `EU.ALD.EU.TAX.BASE` | `EuAllocationDets_EuTaxBase` |  |  |  |
| 5 | `EU.ALD.EU.TAX.RATE` | `EuAllocationDets_EuTaxRate` |  |  |  |
| 6 | `EU.ALD.EU.TAX.SEC.CR` | `EuAllocationDets_EuTaxSecCr` |  |  |  |
| 7 | `EU.ALD.EU.TAX.ACC.CR` | `EuAllocationDets_EuTaxAccCr` |  |  |  |
| 8 | `EU.ALD.DR.TXN.REF` | `EuAllocationDets_DrTxnRef` |  |  |  |
| 9 | `EU.ALD.DR.TXN.CODE` | `EuAllocationDets_DrTxnCode` |  |  |  |
| 10 | `EU.ALD.DR.TXN.DATE` | `EuAllocationDets_DrTxnDate` |  |  |  |
| 11 | `EU.ALD.DR.TXN.TIME` | `EuAllocationDets_DrTxnTime` |  |  |  |
| 12 | `EU.ALD.DR.NOMINAL` | `EuAllocationDets_DrNominal` |  |  |  |
| 13 | `EU.ALD.HLD.PERIOD` | `EuAllocationDets_HldPeriod` |  |  |  |
| 14 | `EU.ALD.HLD.PD.INT` | `EuAllocationDets_HldPdInt` |  |  |  |
| 15 | `EU.ALD.HLD.PD.DISC` | `EuAllocationDets_HldPdDisc` |  |  |  |
| 16 | `EU.ALD.HLD.PD.DISCDAYS` | `EuAllocationDets_HldPdDiscdays` |  |  |  |
| 17 | `EU.ALD.NAV.OUT` | `EuAllocationDets_NavOut` |  |  |  |
| 18 | `EU.ALD.AVG.CAP.GAIN` | `EuAllocationDets_AvgCapGain` |  |  |  |
| 19 | `EU.ALD.CAP.GAIN` | `EuAllocationDets_CapGain` |  |  |  |
| 20 | `EU.ALD.INT.CTR.AVG` | `EuAllocationDets_IntCtrAvg` |  |  |  |
| 21 | `EU.ALD.INT.CTR.OUT` | `EuAllocationDets_IntCtrOut` |  |  |  |
| 22 | `EU.ALD.INT.CTR.GAIN` | `EuAllocationDets_IntCtrGain` |  |  |  |
| 23 | `EU.ALD.TAX.BASE.REV` | `EuAllocationDets_TaxBaseRev` |  |  |  |
| 24 | `EU.ALD.TAX.RATE.REV` | `EuAllocationDets_TaxRateRev` |  |  |  |
| 25 | `EU.ALD.TAX.REV.SEC.CCY` | `EuAllocationDets_TaxRevSecCcy` |  |  |  |
| 26 | `EU.ALD.INCR.TAX.SCCY` | `EuAllocationDets_IncrTaxSccy` |  |  |  |
| 27 | `EU.ALD.INCR.TAX.ACCY` | `EuAllocationDets_IncrTaxAccy` |  |  |  |
| 28 | `EU.ALD.MAN.TAX.SCCY` | `EuAllocationDets_ManTaxSccy` | TField |  | This field holds the manually calculated tax amount in security currency. |
| 29 | `EU.ALD.MAN.TAX.ACCY` | `EuAllocationDets_ManTaxAccy` | TField |  | This field holds the manually calculated tax amount in account currency. |
| 30 | `EU.ALD.JOINT.CUST.TAXID` | `EuAllocationDets_JointCustTaxid` |  |  |  |
| 31 | `EU.ALD.TAX.AMT.SPLIT` | `EuAllocationDets_TaxAmtSplit` |  |  |  |
