# CAPL.H.PROD.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.H.PROD.PARAM` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PROD.PARAM.SHORT.DESCRP` | `CaplHProdParam_ShortDescrp` |  |  |  |
| 2 | `PROD.PARAM.DESCRIPTION` | `CaplHProdParam_Description` |  |  |  |
| 3 | `PROD.PARAM.ALLOWER.FOR.INTF` | `CaplHProdParam_AllowerForIntf` |  |  |  |
| 4 | `PROD.PARAM.PROD.CATEG.GROUP` | `CaplHProdParam_ProdCategGroup` |  |  |  |
| 5 | `PROD.PARAM.MD.EXC.STO.FTTC` | `CaplHProdParam_MdExcStoFttc` |  |  |  |
| 6 | `PROD.PARAM.MD.CHQ.STP.VAL.FRQ` | `CaplHProdParam_MdChqStpValFrq` | TField |  | This field used to parameterise the frequency to be used for calculating the end date for the Stop payments initiated from MDI. If no value in this field then system will take M12 as default value for calculating the end date.Eg: M1 |
| 7 | `PROD.PARAM.MD.AA.INC.TXNS` | `CaplHProdParam_MdAaIncTxns` |  |  |  |
| 8 | `PROD.PARAM.MD.AA.EXC.RUNBAL` | `CaplHProdParam_MdAaExcRunbal` |  |  |  |
| 9 | `PROD.PARAM.T24.LIVE.DT` | `CaplHProdParam_T24LiveDt` | TField |  | This field used to define the date on which product goes live on t24. So based on that the running balance will be calculate for statements.Eg: 20161114 |
| 10 | `PROD.PARAM.STO.ACCT.FTTC` | `CaplHProdParam_StoAcctFttc` | TField |  | For future purpose |
| 11 | `PROD.PARAM.STO.AA.FTTC` | `CaplHProdParam_StoAaFttc` | TField |  | For future purpose |
| 12 | `PROD.PARAM.MAX.STMT.TXNS` | `CaplHProdParam_MaxStmtTxns` | TField |  | For future purpose |
| 13 | `PROD.PARAM.MAX.BM.STMT.TXNS` | `CaplHProdParam_MaxBmStmtTxns` | TField |  | For future purpose |
| 14 | `PROD.PARAM.RESERVED.1` | `CaplHProdParam_Reserved1` | TField |  |  |
| 15 | `PROD.PARAM.LOCAL.REF` | `CaplHProdParam_LocalRef` |  |  |  |
| 16 | `PROD.PARAM.OVERRIDE` | `CaplHProdParam_Override` |  |  |  |
| 17 | `PROD.PARAM.RECORD.STATUS` | `CaplHProdParam_RecordStatus` | String |  |  |
| 18 | `PROD.PARAM.CURR.NO` | `CaplHProdParam_CurrNo` | String |  |  |
| 19 | `PROD.PARAM.INPUTTER` | `CaplHProdParam_Inputter` |  |  |  |
| 20 | `PROD.PARAM.DATE.TIME` | `CaplHProdParam_DateTime` |  |  |  |
| 21 | `PROD.PARAM.AUTHORISER` | `CaplHProdParam_Authoriser` | String |  |  |
| 22 | `PROD.PARAM.CO.CODE` | `CaplHProdParam_CoCode` | String |  |  |
| 23 | `PROD.PARAM.DEPT.CODE` | `CaplHProdParam_DeptCode` | String |  |  |
| 24 | `PROD.PARAM.AUDITOR.CODE` | `CaplHProdParam_AuditorCode` | String |  |  |
| 25 | `PROD.PARAM.AUDIT.DATE.TIME` | `CaplHProdParam_AuditDateTime` | String |  |  |
