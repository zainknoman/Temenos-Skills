# LBNCDR.EXTRACT.PARAM — Table Schema

> Source: `INSERTS/I_F.LBNCDR.EXTRACT.PARAM` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.EXP.THRESHOLD.AMOUNT` | `LbncdrExtractParam_ThresholdAmount` | TField |  | Holds the Threshold amount beyond which the Customers data will be declared in the CDR extract with BDL or CBJ Validation Rules 20 AMT |
| 2 | `LBNCDR.EXP.THRESHOLD.CCY` | `LbncdrExtractParam_ThresholdCcy` | TField |  | Holds the valid record ID from the Currency table. Check file should be linked to CURRENCY table Validation Rules 3 A |
| 3 | `LBNCDR.EXP.LIMIT.REF.TO.EXC` | `LbncdrExtractParam_LimitRefToExc` |  |  |  |
| 4 | `LBNCDR.EXP.LIMIT.REF.EXC.FLD.COND` | `LbncdrExtractParam_LimitRefExcFldCond` |  |  |  |
| 5 | `LBNCDR.EXP.LIMIT.REF.EXC.COND.OPER` | `LbncdrExtractParam_LimitRefExcCondOper` |  |  |  |
| 6 | `LBNCDR.EXP.LIMIT.REF.EXC.COND.VAL` | `LbncdrExtractParam_LimitRefExcCondVal` |  |  |  |
| 7 | `LBNCDR.EXP.RETENTION.PERIOD` | `LbncdrExtractParam_RetentionPeriod` | TField |  | Hold the number of months value Validation Rules 2 A |
| 8 | `LBNCDR.EXP.LIAB.DECL.PRIORITY` | `LbncdrExtractParam_LiabDeclPriority` | TField |  | Hold the value HIGH.TO.LOW or LOW.TO.HIGH Validation Rules 10 N |
| 9 | `LBNCDR.EXP.NON.PERF.CLASS` | `LbncdrExtractParam_NonPerfClass` |  |  |  |
| 10 | `LBNCDR.EXP.NON.PERF.LN.TYP` | `LbncdrExtractParam_NonPerfLnTyp` |  |  |  |
| 11 | `LBNCDR.EXP.INW.PATH` | `LbncdrExtractParam_InwPath` | TField |  | Holds the Inward path, where the AVIS or UPDATE files are placed for T24 to process Validation Rules 100 ANY |
| 12 | `LBNCDR.EXP.OUT.PATH` | `LbncdrExtractParam_OutPath` | TField |  | Holds the Outward path where the T24 will finally place the CDR files generated Validation Rules 100 ANY |
| 13 | `LBNCDR.EXP.CRE.AMT.IN.HUND` | `LbncdrExtractParam_CreAmtInHund` | TField |  | Holds the value of 100,1000,10000,100000,10000000 Based on this configuration amount will be expressed in risk file Validation Rules 10 N |
| 14 | `LBNCDR.EXP.TOTAL.NO.OF.CLIENT` | `LbncdrExtractParam_TotalNoOfClient` | TField |  | Maximum no of clients reported in Risk file for a branch Validation Rules 3 N |
| 15 | `LBNCDR.EXP.SITUATION.DATE` | `LbncdrExtractParam_SituationDate` | TField |  | Holds the situation date for Risk generation file Validation Rules 8 D |
| 16 | `LBNCDR.EXP.SME.TURNOVER` | `LbncdrExtractParam_SmeTurnover` | TField |  | Hold the turnover amount based on which Small and medium enterprises are arrived Validation Rules 19 AMT |
| 17 | `LBNCDR.EXP.SME.BALANCE` | `LbncdrExtractParam_SmeBalance` | TField |  | Hold the Balance sheet amount based on which Small and medium enterprises are arrived Validation Rules 19 AMT |
| 18 | `LBNCDR.EXP.SME.TOT.EMP` | `LbncdrExtractParam_SmeTotEmp` | TField |  | Holds the no of employees based on which Small and medium enterprises are arrived Validation Rules 3 N |
| 19 | `LBNCDR.EXP.CORPCR.TURNOVER` | `LbncdrExtractParam_CorpcrTurnover` | TField |  | Hold the turnover amount based on which Corporate credits are arrived Validation Rules 19 AMT |
| 20 | `LBNCDR.EXP.CORPCR.BALANCE` | `LbncdrExtractParam_CorpcrBalance` | TField |  | Hold the Balance sheet amount based on which Corporate credits are arrived Validation Rules 19 AMT |
| 21 | `LBNCDR.EXP.CORPCR.TOT.EMP` | `LbncdrExtractParam_CorpcrTotEmp` | TField |  | Holds the no of employees based on which Corporate credits are arrived Validation Rules 3 N |
| 22 | `LBNCDR.EXP.ADDRESS.LOCATION.CO` | `LbncdrExtractParam_AddressLocationCo` | TField |  |  |
| 23 | `LBNCDR.EXP.CITY.VILLAGE` | `LbncdrExtractParam_CityVillage` | TField |  |  |
| 24 | `LBNCDR.EXP.LEGAL.FORM` | `LbncdrExtractParam_LegalForm` | TField |  |  |
| 25 | `LBNCDR.EXP.JUDICIAL.STATUS` | `LbncdrExtractParam_JudicialStatus` | TField |  |  |
| 26 | `LBNCDR.EXP.BANK.RATING` | `LbncdrExtractParam_BankRating` | TField |  |  |
| 27 | `LBNCDR.EXP.RECOVERY.COMPANY.CO` | `LbncdrExtractParam_RecoveryCompanyCo` | TField |  |  |
| 28 | `LBNCDR.EXP.COLLATERAL.TYPE` | `LbncdrExtractParam_CollateralType` | TField |  |  |
| 29 | `LBNCDR.EXP.AA.CONTINGENT.CATEG` | `LbncdrExtractParam_AaContingentCateg` | TField |  |  |
| 30 | `LBNCDR.EXP.LC.ACCEPT.CATEG` | `LbncdrExtractParam_LcAcceptCateg` | TField |  |  |
| 31 | `LBNCDR.EXP.BANK.NUMBER` | `LbncdrExtractParam_BankNumber` | TField |  |  |
| 32 | `LBNCDR.EXP.BANK.NAME` | `LbncdrExtractParam_BankName` | TField |  |  |
| 33 | `LBNCDR.EXP.TEMP.OUT.PATH` | `LbncdrExtractParam_TempOutPath` | TField |  |  |
| 34 | `LBNCDR.EXP.OLD.SITUATION.DATE` | `LbncdrExtractParam_OldSituationDate` | TField |  |  |
| 35 | `LBNCDR.EXP.GUR.COLL.TYPE` | `LbncdrExtractParam_GurCollType` | TField |  |  |
| 36 | `LBNCDR.EXP.PRODUCT.ID` | `LbncdrExtractParam_ProductId` | TField |  |  |
| 37 | `LBNCDR.EXP.RESERVED.1` | `LbncdrExtractParam_Reserved1` | TField |  |  |
| 38 | `LBNCDR.EXP.RESERVED.2` | `LbncdrExtractParam_Reserved2` | TField |  |  |
| 39 | `LBNCDR.EXP.RESERVED.3` | `LbncdrExtractParam_Reserved3` | TField |  |  |
| 40 | `LBNCDR.EXP.RESERVED.4` | `LbncdrExtractParam_Reserved4` | TField |  |  |
| 41 | `LBNCDR.EXP.RESERVED.5` | `LbncdrExtractParam_Reserved5` | TField |  |  |
| 42 | `LBNCDR.EXP.RESERVED.6` | `LbncdrExtractParam_Reserved6` | TField |  |  |
| 43 | `LBNCDR.EXP.RESERVED.7` | `LbncdrExtractParam_Reserved7` | TField |  |  |
| 44 | `LBNCDR.EXP.RESERVED.8` | `LbncdrExtractParam_Reserved8` | TField |  |  |
| 45 | `LBNCDR.EXP.LOCAL.REF` | `LbncdrExtractParam_LocalRef` |  |  |  |
| 46 | `LBNCDR.EXP.OVERRIDE` | `LbncdrExtractParam_Override` |  |  |  |
| 47 | `LBNCDR.EXP.RECORD.STATUS` | `LbncdrExtractParam_RecordStatus` | String |  |  |
| 48 | `LBNCDR.EXP.CURR.NO` | `LbncdrExtractParam_CurrNo` | String |  |  |
| 49 | `LBNCDR.EXP.INPUTTER` | `LbncdrExtractParam_Inputter` |  |  |  |
| 50 | `LBNCDR.EXP.DATE.TIME` | `LbncdrExtractParam_DateTime` |  |  |  |
| 51 | `LBNCDR.EXP.AUTHORISER` | `LbncdrExtractParam_Authoriser` | String |  |  |
| 52 | `LBNCDR.EXP.CO.CODE` | `LbncdrExtractParam_CoCode` | String |  |  |
| 53 | `LBNCDR.EXP.DEPT.CODE` | `LbncdrExtractParam_DeptCode` | String |  |  |
| 54 | `LBNCDR.EXP.AUDITOR.CODE` | `LbncdrExtractParam_AuditorCode` | String |  |  |
| 55 | `LBNCDR.EXP.AUDIT.DATE.TIME` | `LbncdrExtractParam_AuditDateTime` | String |  |  |
