# SC.DAILY.ACCRUAL.DETAIL — Table Schema

> Source: `INSERTS/I_F.SC.DAILY.ACCRUAL.DETAIL` in `SC_ScfSafeAdvDailyAccr.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SCDAD.SEC.ACC.NO` | `ScDailyAccrualDetail_SecAccNo` | TField |  | Security Account. The key to the portfolio on SEC.ACC.MASTER. |
| 2 | `SCDAD.CHG.TYPE` | `ScDailyAccrualDetail_ChgType` | TField |  | Charge type a record relates to. SC for Safekeeping, IC for Advisory, or DP for Depository. |
| 3 | `SCDAD.CHG.END.DATE` | `ScDailyAccrualDetail_ChgEndDate` | TField |  | The Charge Period End Date for the record. |
| 4 | `SCDAD.ASSET.ID` | `ScDailyAccrualDetail_AssetId` |  |  |  |
| 5 | `SCDAD.DEPOSITORY` | `ScDailyAccrualDetail_Depository` |  |  |  |
| 6 | `SCDAD.PRODUCT` | `ScDailyAccrualDetail_Product` |  |  |  |
| 7 | `SCDAD.EFF.DATE` | `ScDailyAccrualDetail_EffDate` |  |  |  |
| 8 | `SCDAD.CHG.SCALE` | `ScDailyAccrualDetail_ChgScale` |  |  |  |
| 9 | `SCDAD.CHG.FT.TYPE` | `ScDailyAccrualDetail_ChgFtType` |  |  |  |
| 10 | `SCDAD.CHG.RATE` | `ScDailyAccrualDetail_ChgRate` |  |  |  |
| 11 | `SCDAD.CHG.DAYS` | `ScDailyAccrualDetail_ChgDays` |  |  |  |
| 12 | `SCDAD.CHG.BASE.AMT` | `ScDailyAccrualDetail_ChgBaseAmt` |  |  |  |
| 13 | `SCDAD.CHG.LCY` | `ScDailyAccrualDetail_ChgLcy` |  |  |  |
| 14 | `SCDAD.CHG.AC.CCY` | `ScDailyAccrualDetail_ChgAcCcy` |  |  |  |
| 15 | `SCDAD.CHG.ACY` | `ScDailyAccrualDetail_ChgAcy` |  |  |  |
| 16 | `SCDAD.CHG.XRATE` | `ScDailyAccrualDetail_ChgXrate` |  |  |  |
| 17 | `SCDAD.SV.RES.5` | `ScDailyAccrualDetail_SvRes5` |  |  |  |
| 18 | `SCDAD.SV.RES.4` | `ScDailyAccrualDetail_SvRes4` |  |  |  |
| 19 | `SCDAD.SV.RES.3` | `ScDailyAccrualDetail_SvRes3` |  |  |  |
| 20 | `SCDAD.SV.RES.2` | `ScDailyAccrualDetail_SvRes2` |  |  |  |
| 21 | `SCDAD.SV.RES.1` | `ScDailyAccrualDetail_SvRes1` |  |  |  |
| 22 | `SCDAD.MV.RES.5` | `ScDailyAccrualDetail_MvRes5` |  |  |  |
| 23 | `SCDAD.MV.RES.4` | `ScDailyAccrualDetail_MvRes4` |  |  |  |
| 24 | `SCDAD.MV.RES.3` | `ScDailyAccrualDetail_MvRes3` |  |  |  |
| 25 | `SCDAD.MV.RES.2` | `ScDailyAccrualDetail_MvRes2` |  |  |  |
| 26 | `SCDAD.MV.RES.1` | `ScDailyAccrualDetail_MvRes1` |  |  |  |
| 27 | `SCDAD.SCND.EFF.DATE` | `ScDailyAccrualDetail_ScndEffDate` |  |  |  |
| 28 | `SCDAD.SCND.CHG.SCALE` | `ScDailyAccrualDetail_ScndChgScale` |  |  |  |
| 29 | `SCDAD.SCND.CHG.FT.TYPE` | `ScDailyAccrualDetail_ScndChgFtType` |  |  |  |
| 30 | `SCDAD.SCND.CHG.RATE` | `ScDailyAccrualDetail_ScndChgRate` |  |  |  |
| 31 | `SCDAD.SCND.CHG.DAYS` | `ScDailyAccrualDetail_ScndChgDays` |  |  |  |
| 32 | `SCDAD.SCND.CHG.BASE` | `ScDailyAccrualDetail_ScndChgBase` |  |  |  |
| 33 | `SCDAD.SCND.CHG.LCY` | `ScDailyAccrualDetail_ScndChgLcy` |  |  |  |
| 34 | `SCDAD.SCND.CHG.AC.CCY` | `ScDailyAccrualDetail_ScndChgAcCcy` |  |  |  |
| 35 | `SCDAD.SCND.CHG.ACY` | `ScDailyAccrualDetail_ScndChgAcy` |  |  |  |
| 36 | `SCDAD.SCND.CHG.XRATE` | `ScDailyAccrualDetail_ScndChgXrate` |  |  |  |
| 37 | `SCDAD.ANNUAL.MIN.LCY` | `ScDailyAccrualDetail_AnnualMinLcy` | TField |  | Where a minimum fee has been imposed, this field shows the annual minimum in local currency. Note that, in these circumstances, the calculation breakdown in the asset-based fields in this application relate to the original fee, prior to imposition of the minimum. |
| 38 | `SCDAD.ANNUAL.MAX.LCY` | `ScDailyAccrualDetail_AnnualMaxLcy` | TField |  | Where a maximum fee has been imposed, this field shows the annual maximum in local currency. Note that, in these circumstances, the calculation breakdown in the asset-based fields in this application relate to the original fee, prior to imposition of the maximum. |
| 39 | `SCDAD.ANNUAL.MIN.ACY` | `ScDailyAccrualDetail_AnnualMinAcy` | TField |  | Where a minimum fee has been imposed, this field shows the annual minimum in charge account currency. Note that, in these circumstances, the calculation breakdown in the asset-based fields in this application relate to the original fee, prior to imposition of the minimum. |
| 40 | `SCDAD.ANNUAL.MAX.ACY` | `ScDailyAccrualDetail_AnnualMaxAcy` | TField |  | Where a maximum fee has been imposed, this field shows the annual maximum in charge account currency. Note that, in these circumstances, the calculation breakdown in the asset-based fields in this application relate to the original fee, prior to imposition of the maximum. |
