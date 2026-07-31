# SACUIN.ALERT.AND.PR.DETAILS — Table Schema

> Source: `INSERTS/I_F.SACUIN.ALERT.AND.PR.DETAILS` in `SACUIN_CustomerIdExpiry.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SACUIN.ALERT.LEGAL.ID.EXP.DT` | `SacuinAlertAndPrDetails_LegalIdExpDt` | TField |  | The expiry date of the Legal ID. |
| 2 | `SACUIN.ALERT.ALRT.DAYS.BEF.EXP` | `SacuinAlertAndPrDetails_AlrtDaysBefExp` | TField |  | The number of days before the legal ID expiry date, where the alert should be triggered. |
| 3 | `SACUIN.ALERT.ALRT.DAYS.AFT.EXP` | `SacuinAlertAndPrDetails_AlrtDaysAftExp` | TField |  | The no.of days after the legal ID expiry date, where the alert should be triggered. |
| 4 | `SACUIN.ALERT.PR.DAYS.BEF.EXP` | `SacuinAlertAndPrDetails_PrDaysBefExp` | TField |  | The no.of days before the legal ID expiry date, where the posting restriction should be applied at customer level. |
| 5 | `SACUIN.ALERT.PR.TYPE.BEF.EXP` | `SacuinAlertAndPrDetails_PrTypeBefExp` | TField |  | The posting restriction type, which should be imposed, should be mentioned in this field. |
| 6 | `SACUIN.ALERT.PR.DAYS.AFT.EXP` | `SacuinAlertAndPrDetails_PrDaysAftExp` | TField |  | The no.of days after the legal ID expiry date, where the posting restriction should be applied at customer level. |
| 7 | `SACUIN.ALERT.PR.TYPE.AFT.EXP` | `SacuinAlertAndPrDetails_PrTypeAftExp` | TField |  | The posting restriction type, which should be imposed, should be mentioned in this field. |
| 8 | `SACUIN.ALERT.PR.TYPE.OTHR.DOC` | `SacuinAlertAndPrDetails_PrTypeOthrDoc` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 9 | `SACUIN.ALERT.SAUDI.NATIONAL.ID` | `SacuinAlertAndPrDetails_SaudiNationalId` |  |  |  |
| 10 | `SACUIN.ALERT.TARGET` | `SacuinAlertAndPrDetails_Target` |  |  |  |
| 11 | `SACUIN.ALERT.OTHR.ALRT.DAYS.BEF.EXP` | `SacuinAlertAndPrDetails_OthrAlrtDaysBefExp` | TField |  | The no.of days before the legal ID expiry date, where the alert should be triggered. |
| 12 | `SACUIN.ALERT.OTHR.ALRT.DAYS.AFT.EXP` | `SacuinAlertAndPrDetails_OthrAlrtDaysAftExp` | TField |  | The no.of days after the legal ID expiry date, where the alert should be triggered. |
| 13 | `SACUIN.ALERT.OTHR.PR.DAYS.BEF.EXP` | `SacuinAlertAndPrDetails_OthrPrDaysBefExp` | TField |  | The no.of days before the legal ID expiry date, where the posting restriction should be applied at customer level. |
| 14 | `SACUIN.ALERT.OTHR.PR.TYPE.BEF.EXP` | `SacuinAlertAndPrDetails_OthrPrTypeBefExp` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 15 | `SACUIN.ALERT.OTHR.PR.TYPE.ON.EXP` | `SacuinAlertAndPrDetails_OthrPrTypeOnExp` | TField |  | The posting restriction type which should be imposed on the Legal Id expiry date should be mentioned in this field. |
| 16 | `SACUIN.ALERT.OTHR.UNCL.DAYS.AFT.EXP` | `SacuinAlertAndPrDetails_OthrUnclDaysAftExp` | TField |  | The no.of days after the legal ID expiry date, where the accounts should be moved to unclaimed status. |
| 17 | `SACUIN.ALERT.SPL.ALRT.DAYS.BEF.EXP` | `SacuinAlertAndPrDetails_SplAlrtDaysBefExp` | TField |  | The no.of days before the legal ID expiry date, where the alert should be triggered. |
| 18 | `SACUIN.ALERT.SPL.ALRT.DAYS.AFT.EXP` | `SacuinAlertAndPrDetails_SplAlrtDaysAftExp` | TField |  | The no.of days after the legal ID expiry date, where the alert should be triggered. |
| 19 | `SACUIN.ALERT.SPL.PR.DAYS.BEF.EXP` | `SacuinAlertAndPrDetails_SplPrDaysBefExp` | TField |  | The no.of days before the legal ID expiry date, where the posting restriction should be applied at customer level. |
| 20 | `SACUIN.ALERT.SPL.PR.TYPE.BEF.EXP` | `SacuinAlertAndPrDetails_SplPrTypeBefExp` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 21 | `SACUIN.ALERT.SPL.GR1.DAYS.AFT.EXP` | `SacuinAlertAndPrDetails_SplGr1DaysAftExp` | TField |  | The no.of days after the first grace period of the legal ID expiry date, where the posting restriction should be applied at customer level. |
| 22 | `SACUIN.ALERT.SPL.PR.TYPE.AFT.GR1` | `SacuinAlertAndPrDetails_SplPrTypeAftGr1` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 23 | `SACUIN.ALERT.SPL.GR2.DAYS.AFT.EXP` | `SacuinAlertAndPrDetails_SplGr2DaysAftExp` | TField |  | The no.of days after the second grace period of the legal ID expiry date, where the posting restriction should be applied at customer level. |
| 24 | `SACUIN.ALERT.SPL.PR.TYPE.AFT.GR2` | `SacuinAlertAndPrDetails_SplPrTypeAftGr2` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 25 | `SACUIN.ALERT.MINOR.AGE.YRS` | `SacuinAlertAndPrDetails_MinorAgeYrs` | TField |  | The no. of years at which the minor age will be expired. |
| 26 | `SACUIN.ALERT.MINOR.ALRT.DAYS.BEF.EXP` | `SacuinAlertAndPrDetails_MinorAlrtDaysBefExp` | TField |  | The no.of days before the minor age expiry date, where the alert should be triggered. |
| 27 | `SACUIN.ALERT.MINOR.PR.TYPE.AGE.EXP` | `SacuinAlertAndPrDetails_MinorPrTypeAgeExp` | TField |  | The posting restriction type which should be imposed on the minor age expiry should be mentioned in this field. |
| 28 | `SACUIN.ALERT.MINOR.GR.DAYS.AFT.EXP` | `SacuinAlertAndPrDetails_MinorGrDaysAftExp` | TField |  | The no.of days after the minor age expiry date, after which the posting restriction will be imposed. |
| 29 | `SACUIN.ALERT.MINOR.PR.TYPE.AFT.GR` | `SacuinAlertAndPrDetails_MinorPrTypeAftGr` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 30 | `SACUIN.ALERT.CUS.INFO.EXP.YRS` | `SacuinAlertAndPrDetails_CusInfoExpYrs` | TField |  | The no. of years at which the customer info. will get expired. |
| 31 | `SACUIN.ALERT.CUS.ALRT.DAYS.BEF.EXP` | `SacuinAlertAndPrDetails_CusAlrtDaysBefExp` | TField |  | The no of days before the customer info expiry the alert should be triggered |
| 32 | `SACUIN.ALERT.OTHR.CUS.INFO.EXP.YRS` | `SacuinAlertAndPrDetails_OthrCusInfoExpYrs` | TField |  | The no. of years at which the customer info. will get expired. |
| 33 | `SACUIN.ALERT.CUS.INFO.BEF.EXP.DAYS` | `SacuinAlertAndPrDetails_CusInfoBefExpDays` | TField |  | The no.of days before the customer info expiry date, where the posting restriction should be imposed. |
| 34 | `SACUIN.ALERT.CUS.INFO.PR.BEF.EXP` | `SacuinAlertAndPrDetails_CusInfoPrBefExp` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 35 | `SACUIN.ALERT.CUS.INFO.AFT.EXP.DAYS` | `SacuinAlertAndPrDetails_CusInfoAftExpDays` | TField |  | The no.of days after the customer info expiry date, where the posting restriction should be imposed. |
| 36 | `SACUIN.ALERT.CUS.INFO.PR.AFT.EXP` | `SacuinAlertAndPrDetails_CusInfoPrAftExp` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
