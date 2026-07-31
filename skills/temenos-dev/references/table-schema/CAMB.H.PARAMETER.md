# CAMB.H.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CAMB.H.PARAMETER` in `CABASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CCS.PARAM.LOC.COV.AMT` | `CambHParameter_LocCovAmt` | TField |  | Field to define the threshold amount for LOC Insurance type.Amount field. Allowed up to 20 digits.Eg.10,000Insurance for LOC type of insurance can be provided upto maximum of 10,000 |
| 2 | `CCS.PARAM.OB.COV.AMT` | `CambHParameter_ObCovAmt` | TField |  | Field to define the threshold amount for OB Insurance type.Amount field. Allowed up to 20 digits.Eg.5,000Insurance for LOC type of insurance can be provided upto maximum of 5,000 |
| 3 | `CCS.PARAM.AGE.TYPE` | `CambHParameter_AgeType` |  |  |  |
| 4 | `CCS.PARAM.FROM.AGE` | `CambHParameter_FromAge` |  |  |  |
| 5 | `CCS.PARAM.TO.AGE` | `CambHParameter_ToAge` |  |  |  |
| 6 | `CCS.PARAM.HRS.PER.WEEK` | `CambHParameter_HrsPerWeek` | TField |  | Minimum working hour's for a customer to be eligible for REX loans is parameterised here.Allowed up to 2 digits numeric. Considered in Hours.Eg 20. |
| 7 | `CCS.PARAM.EQUIFAX.EXT.DAYS` | `CambHParameter_EquifaxExtDays` | TField |  | Purpose of the field to define the number of days after which the new report for Equifax to be generated and reported.Example - 180C |
| 8 | `CCS.PARAM.NEXT.LOC.EXT.DATE` | `CambHParameter_NextLocExtDate` | TField |  |  |
| 9 | `CCS.PARAM.TRANSIT.NO` | `CambHParameter_TransitNo` | TField |  |  |
| 10 | `CCS.PARAM.GAP.OR.INTF` | `CambHParameter_GapOrIntf` |  |  |  |
| 11 | `CCS.PARAM.APPLICATION` | `CambHParameter_Application` |  |  |  |
| 12 | `CCS.PARAM.VERSION` | `CambHParameter_Version` |  |  |  |
| 13 | `CCS.PARAM.FUNCTION` | `CambHParameter_Function` |  |  |  |
| 14 | `CCS.PARAM.OPERATION` | `CambHParameter_Operation` |  |  |  |
| 15 | `CCS.PARAM.OFS.SOURCE` | `CambHParameter_OfsSource` |  |  |  |
| 16 | `CCS.PARAM.TXN.TYPE` | `CambHParameter_TxnType` |  |  |  |
| 17 | `CCS.PARAM.COMPANY` | `CambHParameter_Company` |  |  |  |
| 18 | `CCS.PARAM.EQUIFAX.REQ.PATH` | `CambHParameter_EquifaxReqPath` | TField |  | Purpose of the field to store the path where the request Message for equifax to be stored. Used for download the Equifax report |
| 19 | `CCS.PARAM.EQUIFAX.RES.PATH` | `CambHParameter_EquifaxResPath` | TField |  |  |
| 20 | `CCS.PARAM.CERT.NAME` | `CambHParameter_CertName` | TField |  | Field to store the prefix for the Certificate Number generation for LOC Insurance should be parameterised here. |
| 21 | `CCS.PARAM.EXT.COST.CENTER` | `CambHParameter_ExtCostCenter` | TField |  |  |
| 22 | `CCS.PARAM.EXC.INS.CATEG` | `CambHParameter_ExcInsCateg` |  |  |  |
| 23 | `CCS.PARAM.OB.INS.MIN.AMT` | `CambHParameter_ObInsMinAmt` | TField |  | Field not in use. |
| 24 | `CCS.PARAM.OB.INS.AGE` | `CambHParameter_ObInsAge` | TField |  | Field not in use. |
| 25 | `CCS.PARAM.LOC.INS.TRF.VER` | `CambHParameter_LocInsTrfVer` | TField |  | The Purpose of this field is used to define the OFS version to be used for LOC insurance transfer. Valid record of VERSION table.Ex. CAPL.H.INSURANCE.PRODUCT,TRANSFER |
| 26 | `CCS.PARAM.LOC.INS.OFS` | `CambHParameter_LocInsOfs` | TField |  | The purpose of this field is used to define the OFS.SOURCE, which is to be used for transfer of insurance product. Valid record from OFS.SOURCE table. |
| 27 | `CCS.PARAM.RESERVED.5` | `CambHParameter_Reserved5` |  |  |  |
| 28 | `CCS.PARAM.RESERVED.4` | `CambHParameter_Reserved4` | TField |  |  |
| 29 | `CCS.PARAM.RESERVED.3` | `CambHParameter_Reserved3` | TField |  |  |
| 30 | `CCS.PARAM.RESERVED.2` | `CambHParameter_Reserved2` | TField |  |  |
| 31 | `CCS.PARAM.RESERVED.1` | `CambHParameter_Reserved1` | TField |  |  |
| 32 | `CCS.PARAM.LOCAL.REF` | `CambHParameter_LocalRef` |  |  |  |
| 33 | `CCS.PARAM.STMT.NOS` | `CambHParameter_StmtNos` |  |  |  |
| 34 | `CCS.PARAM.OVERRIDE` | `CambHParameter_Override` |  |  |  |
| 35 | `CCS.PARAM.RECORD.STATUS` | `CambHParameter_RecordStatus` | String |  |  |
| 36 | `CCS.PARAM.CURR.NO` | `CambHParameter_CurrNo` | String |  |  |
| 37 | `CCS.PARAM.INPUTTER` | `CambHParameter_Inputter` |  |  |  |
| 38 | `CCS.PARAM.DATE.TIME` | `CambHParameter_DateTime` |  |  |  |
| 39 | `CCS.PARAM.AUTHORISER` | `CambHParameter_Authoriser` | String |  |  |
| 40 | `CCS.PARAM.CO.CODE` | `CambHParameter_CoCode` | String |  |  |
| 41 | `CCS.PARAM.DEPT.CODE` | `CambHParameter_DeptCode` | String |  |  |
| 42 | `CCS.PARAM.AUDITOR.CODE` | `CambHParameter_AuditorCode` | String |  |  |
| 43 | `CCS.PARAM.AUDIT.DATE.TIME` | `CambHParameter_AuditDateTime` | String |  |  |
