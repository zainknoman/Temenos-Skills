# SABASE.CUSTOMER.PARAM — Table Schema

> Source: `INSERTS/I_F.SABASE.CUSTOMER.PARAM` in `SABASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SABASE.PARAM.ALRT.DAYS.BEF.EXP` | `SabaseCustomerParam_AlrtDaysBefExp` | TField |  | The number of days before the legal ID expiry date, where the alert should be triggered. |
| 2 | `SABASE.PARAM.ALRT.DAYS.AFT.EXP` | `SabaseCustomerParam_AlrtDaysAftExp` | TField |  | The no.of days after the legal ID expiry date, where the alert should be triggered. |
| 3 | `SABASE.PARAM.PR.DAYS.BEF.EXP` | `SabaseCustomerParam_PrDaysBefExp` | TField |  | The no.of days before the legal ID expiry date, where the posting restriction should be applied at customer level. |
| 4 | `SABASE.PARAM.PR.TYPE.BEF.EXP` | `SabaseCustomerParam_PrTypeBefExp` | TField |  | The posting restriction type, which should be imposed, should be mentioned in this field. |
| 5 | `SABASE.PARAM.PR.DAYS.AFT.EXP` | `SabaseCustomerParam_PrDaysAftExp` | TField |  | The no.of days after the legal ID expiry date, where the posting restriction should be applied at customer level. |
| 6 | `SABASE.PARAM.PR.TYPE.AFT.EXP` | `SabaseCustomerParam_PrTypeAftExp` | TField |  | The posting restriction type, which should be imposed, should be mentioned in this field. |
| 7 | `SABASE.PARAM.PR.TYPE.OTHR.DOC` | `SabaseCustomerParam_PrTypeOthrDoc` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 8 | `SABASE.PARAM.SAUDI.NATIONAL.ID` | `SabaseCustomerParam_SaudiNationalId` |  |  |  |
| 9 | `SABASE.PARAM.TARGET` | `SabaseCustomerParam_Target` |  |  |  |
| 10 | `SABASE.PARAM.OTHR.ALRT.DAYS.BEF.EXP` | `SabaseCustomerParam_OthrAlrtDaysBefExp` | TField |  | The no.of days before the legal ID expiry date, where the alert should be triggered. |
| 11 | `SABASE.PARAM.OTHR.ALRT.DAYS.AFT.EXP` | `SabaseCustomerParam_OthrAlrtDaysAftExp` | TField |  | The no.of days after the legal ID expiry date, where the alert should be triggered. |
| 12 | `SABASE.PARAM.OTHR.PR.DAYS.BEF.EXP` | `SabaseCustomerParam_OthrPrDaysBefExp` | TField |  | The no.of days before the legal ID expiry date, where the posting restriction should be applied at customer level. |
| 13 | `SABASE.PARAM.OTHR.PR.TYPE.BEF.EXP` | `SabaseCustomerParam_OthrPrTypeBefExp` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 14 | `SABASE.PARAM.OTHR.PR.TYPE.ON.EXP` | `SabaseCustomerParam_OthrPrTypeOnExp` | TField |  | The posting restriction type which should be imposed on the Legal Id expiry date should be mentioned in this field. |
| 15 | `SABASE.PARAM.OTHR.UNCL.DAYS.AFT.EXP` | `SabaseCustomerParam_OthrUnclDaysAftExp` | TField |  | The no.of days after the legal ID expiry date, where the accounts should be moved to unclaimed status. |
| 16 | `SABASE.PARAM.SPL.ALRT.DAYS.BEF.EXP` | `SabaseCustomerParam_SplAlrtDaysBefExp` | TField |  | The no.of days before the legal ID expiry date, where the alert should be triggered. |
| 17 | `SABASE.PARAM.SPL.ALRT.DAYS.AFT.EXP` | `SabaseCustomerParam_SplAlrtDaysAftExp` | TField |  | The no.of days after the legal ID expiry date, where the alert should be triggered. |
| 18 | `SABASE.PARAM.SPL.PR.DAYS.BEF.EXP` | `SabaseCustomerParam_SplPrDaysBefExp` | TField |  | The no.of days before the legal ID expiry date, where the posting restriction should be applied at customer level. |
| 19 | `SABASE.PARAM.SPL.PR.TYPE.BEF.EXP` | `SabaseCustomerParam_SplPrTypeBefExp` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 20 | `SABASE.PARAM.SPL.GR1.DAYS.AFT.EXP` | `SabaseCustomerParam_SplGr1DaysAftExp` | TField |  | The no.of days after the first grace period of the legal ID expiry date, where the posting restriction should be applied at customer level. |
| 21 | `SABASE.PARAM.SPL.PR.TYPE.AFT.GR1` | `SabaseCustomerParam_SplPrTypeAftGr1` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 22 | `SABASE.PARAM.SPL.GR2.DAYS.AFT.EXP` | `SabaseCustomerParam_SplGr2DaysAftExp` | TField |  | The no.of days after the second grace period of the legal ID expiry date, where the posting restriction should be applied at customer level. |
| 23 | `SABASE.PARAM.SPL.PR.TYPE.AFT.GR2` | `SabaseCustomerParam_SplPrTypeAftGr2` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 24 | `SABASE.PARAM.MINOR.AGE.YRS` | `SabaseCustomerParam_MinorAgeYrs` | TField |  | The no. of years at which the minor age will be expired. |
| 25 | `SABASE.PARAM.MINOR.ALRT.DAYS.BEF.EXP` | `SabaseCustomerParam_MinorAlrtDaysBefExp` | TField |  | The no.of days before the minor age expiry date, where the alert should be triggered. |
| 26 | `SABASE.PARAM.MINOR.PR.TYPE.AGE.EXP` | `SabaseCustomerParam_MinorPrTypeAgeExp` | TField |  | The posting restriction type which should be imposed on the minor age expiry should be mentioned in this field. |
| 27 | `SABASE.PARAM.MINOR.GR.DAYS.AFT.EXP` | `SabaseCustomerParam_MinorGrDaysAftExp` | TField |  | The no.of days after the minor age expiry date, after which the posting restriction will be imposed. |
| 28 | `SABASE.PARAM.MINOR.PR.TYPE.AFT.GR` | `SabaseCustomerParam_MinorPrTypeAftGr` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 29 | `SABASE.PARAM.CUS.INFO.EXP.YRS` | `SabaseCustomerParam_CusInfoExpYrs` | TField |  | The no. of years at which the customer info. will get expired. |
| 30 | `SABASE.PARAM.CUS.ALRT.DAYS.BEF.EXP` | `SabaseCustomerParam_CusAlrtDaysBefExp` | TField |  | The no of days before the customer info expiry the alert should be triggered |
| 31 | `SABASE.PARAM.OTHR.CUS.INFO.EXP.YRS` | `SabaseCustomerParam_OthrCusInfoExpYrs` | TField |  | The no. of years at which the customer info. will get expired. |
| 32 | `SABASE.PARAM.CUS.INFO.BEF.EXP.DAYS` | `SabaseCustomerParam_CusInfoBefExpDays` | TField |  | The no.of days before the customer info expiry date, where the posting restriction should be imposed. |
| 33 | `SABASE.PARAM.CUS.INFO.PR.BEF.EXP` | `SabaseCustomerParam_CusInfoPrBefExp` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 34 | `SABASE.PARAM.CUS.INFO.AFT.EXP.DAYS` | `SabaseCustomerParam_CusInfoAftExpDays` | TField |  | The no.of days after the customer info expiry date, where the posting restriction should be imposed. |
| 35 | `SABASE.PARAM.CUS.INFO.PR.AFT.EXP` | `SabaseCustomerParam_CusInfoPrAftExp` | TField |  | The posting restriction type which should be imposed should be mentioned in this field. |
| 36 | `SABASE.PARAM.GUARD.REL.CODE` | `SabaseCustomerParam_GuardRelCode` |  |  |  |
| 37 | `SABASE.PARAM.SECTOR` | `SabaseCustomerParam_Sector` |  |  |  |
| 38 | `SABASE.PARAM.MAX.POA.ALLOWED` | `SabaseCustomerParam_MaxPoaAllowed` |  |  |  |
| 39 | `SABASE.PARAM.CUSTOMER.ROLE` | `SabaseCustomerParam_CustomerRole` | TField |  | Reserved for future use |
| 40 | `SABASE.PARAM.SPL.STO.TYPE` | `SabaseCustomerParam_SplStoType` |  |  |  |
| 41 | `SABASE.PARAM.EXCLUDED.STO.TYPE` | `SabaseCustomerParam_ExcludedStoType` |  |  |  |
| 42 | `SABASE.PARAM.ARABIC.LANGUAGE.CODE` | `SabaseCustomerParam_ArabicLanguageCode` | TField |  | This field will the language code of Arabic and it is vetted from LANGUAGE table |
| 43 | `SABASE.PARAM.DEFAULT.LANGUAGE.CODE` | `SabaseCustomerParam_DefaultLanguageCode` | TField |  | This field will the language code of default language other than Arabic and it is vetted from LANGUAGE table |
| 44 | `SABASE.PARAM.RESERVED.3` | `SabaseCustomerParam_Reserved3` | TField |  |  |
| 45 | `SABASE.PARAM.RESERVED.2` | `SabaseCustomerParam_Reserved2` | TField |  |  |
| 46 | `SABASE.PARAM.RESERVED.1` | `SabaseCustomerParam_Reserved1` | TField |  |  |
| 47 | `SABASE.PARAM.LOCAL.REF` | `SabaseCustomerParam_LocalRef` |  |  |  |
| 48 | `SABASE.PARAM.OVERRIDE` | `SabaseCustomerParam_Override` |  |  |  |
| 49 | `SABASE.PARAM.RECORD.STATUS` | `SabaseCustomerParam_RecordStatus` | String |  |  |
| 50 | `SABASE.PARAM.CURR.NO` | `SabaseCustomerParam_CurrNo` | String |  |  |
| 51 | `SABASE.PARAM.INPUTTER` | `SabaseCustomerParam_Inputter` |  |  |  |
| 52 | `SABASE.PARAM.DATE.TIME` | `SabaseCustomerParam_DateTime` |  |  |  |
| 53 | `SABASE.PARAM.AUTHORISER` | `SabaseCustomerParam_Authoriser` | String |  |  |
| 54 | `SABASE.PARAM.CO.CODE` | `SabaseCustomerParam_CoCode` | String |  |  |
| 55 | `SABASE.PARAM.DEPT.CODE` | `SabaseCustomerParam_DeptCode` | String |  |  |
| 56 | `SABASE.PARAM.AUDITOR.CODE` | `SabaseCustomerParam_AuditorCode` | String |  |  |
| 57 | `SABASE.PARAM.AUDIT.DATE.TIME` | `SabaseCustomerParam_AuditDateTime` | String |  |  |
