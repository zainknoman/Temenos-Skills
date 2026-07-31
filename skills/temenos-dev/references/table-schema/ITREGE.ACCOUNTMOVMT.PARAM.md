# ITREGE.ACCOUNTMOVMT.PARAM — Table Schema

> Source: `INSERTS/I_F.ITREGE.ACCOUNTMOVMT.PARAM` in `ITREGE_AccountMovements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACC.PARAM.AREA.CODE` | `ItregeAccountmovmtParam_AreaCode` | TField |  | This field stores the area code |
| 2 | `ACC.PARAM.SERVICE` | `ItregeAccountmovmtParam_Service` | TField |  | This field stores the service code |
| 3 | `ACC.PARAM.OPR.TYPE` | `ItregeAccountmovmtParam_OprType` | TField |  | This field stores the Operation Type� |
| 4 | `ACC.PARAM.CURR.TYPE` | `ItregeAccountmovmtParam_CurrType` | TField |  | This field stores the Currency Type� |
| 5 | `ACC.PARAM.EXCH.TYPE` | `ItregeAccountmovmtParam_ExchType` | TField |  | This field stores the Exchange code |
| 6 | `ACC.PARAM.MOVMT.SIGN` | `ItregeAccountmovmtParam_MovmtSign` | TField |  | This field stores the Movement sign |
| 7 | `ACC.PARAM.EXCHANGE` | `ItregeAccountmovmtParam_Exchange` | TField |  | This field stores the Exchange Value |
| 8 | `ACC.PARAM.EXCH.CURR.VALUE` | `ItregeAccountmovmtParam_ExchCurrValue` | TField |  | This field stores the Exchange Currency value |
| 9 | `ACC.PARAM.CTV.CURR.EXCH` | `ItregeAccountmovmtParam_CtvCurrExch` | TField |  | This field stores the Ctv currency Exchange value |
| 10 | `ACC.PARAM.DEPEND.PROVINCE` | `ItregeAccountmovmtParam_DependProvince` | TField |  | This field stores the Dependency Province |
| 11 | `ACC.PARAM.SETT.METHODS` | `ItregeAccountmovmtParam_SettMethods` | TField |  | This field stores the Settlement Methods |
| 12 | `ACC.PARAM.DEBIT.CAUSE` | `ItregeAccountmovmtParam_DebitCause` | TField |  | This field stores the Debit Cause |
| 13 | `ACC.PARAM.REPT.TYPE` | `ItregeAccountmovmtParam_ReptType` | TField |  | This field stores the Report Type |
| 14 | `ACC.PARAM.DOOR.TYPE` | `ItregeAccountmovmtParam_DoorType` | TField |  | This field stores the Door Type |
| 15 | `ACC.PARAM.TYPE.CURR.ACC.OPTN` | `ItregeAccountmovmtParam_TypeCurrAccOptn` | TField |  | This field stores the Type of current account operation |
| 16 | `ACC.PARAM.MOVEMENT.TYPE` | `ItregeAccountmovmtParam_MovementType` | TField |  | This field stores the Movement Type |
| 17 | `ACC.PARAM.RELAT.DURN` | `ItregeAccountmovmtParam_RelatDurn` | TField |  | This field stores the Relationship Duration |
| 18 | `ACC.PARAM.CUST.DEPEND.CODE` | `ItregeAccountmovmtParam_CustDependCode` | TField |  | This field stores the Customer Dependency code |
| 19 | `ACC.PARAM.ACCTNG.ENTY` | `ItregeAccountmovmtParam_AcctngEnty` | TField |  | This field stores the Accounting Entity |
| 20 | `ACC.PARAM.CUST.NAT` | `ItregeAccountmovmtParam_CustNat` | TField |  | This field stores the Customer Nation value |
| 21 | `ACC.PARAM.CUST.RES` | `ItregeAccountmovmtParam_CustRes` | TField |  | This field stores the Customer residence value, The value when the customer is a local resident |
| 22 | `ACC.PARAM.CUST.NON.RES` | `ItregeAccountmovmtParam_CustNonRes` | TField |  | This field stores the Customer Non-residence value, the value when the customer is not a local resident |
| 23 | `ACC.PARAM.INDIVIDUAL.SECTOR` | `ItregeAccountmovmtParam_IndividualSector` | TField |  | This field stores the Individual sector value, The value when the customer belongs to individual sector |
| 24 | `ACC.PARAM.BUSINESS.SECTOR` | `ItregeAccountmovmtParam_BusinessSector` | TField |  | This field stores the Business sector value, The value when the customer not belonging to individual sector |
| 25 | `ACC.PARAM.MOVMT.SIGN.1` | `ItregeAccountmovmtParam_MovmtSign1` | TField |  | This field stores the Account Expense Movement sign |
| 26 | `ACC.PARAM.CURRENCY` | `ItregeAccountmovmtParam_Currency` | TField |  | This field stores the Currency Value |
| 27 | `ACC.PARAM.RECORD.PROPERTY` | `ItregeAccountmovmtParam_RecordProperty` | TField |  | This field stores the Record Property Value |
| 28 | `ACC.PARAM.RECVNG.CHN` | `ItregeAccountmovmtParam_RecvngChn` | TField |  | This field stores the Receiving channel |
| 29 | `ACC.PARAM.ESERV.FUN.CODE` | `ItregeAccountmovmtParam_EservFunCode` | TField |  | This field stores the Eservice func code value |
| 30 | `ACC.PARAM.ACTIVITY` | `ItregeAccountmovmtParam_Activity` |  |  |  |
| 31 | `ACC.PARAM.INCOME.LOSS.MOVMT.TYPE` | `ItregeAccountmovmtParam_IncomeLossMovmtType` |  |  |  |
| 32 | `ACC.PARAM.DEBIT.CREDIT.TXN.SIGN` | `ItregeAccountmovmtParam_DebitCreditTxnSign` |  |  |  |
| 33 | `ACC.PARAM.DEBIT.CREDIT.MOVMT.TYPE` | `ItregeAccountmovmtParam_DebitCreditMovmtType` |  |  |  |
| 34 | `ACC.PARAM.FEE.CODE` | `ItregeAccountmovmtParam_FeeCode` |  |  |  |
| 35 | `ACC.PARAM.CHANNEL` | `ItregeAccountmovmtParam_Channel` |  |  |  |
| 36 | `ACC.PARAM.ACTOPN.RUN.DATE` | `ItregeAccountmovmtParam_ActopnRunDate` | TField |  | This field stores the Account Open Rerun date, Last four quarter values can be given |
| 37 | `ACC.PARAM.ACTEXP.RUN.DATE` | `ItregeAccountmovmtParam_ActexpRunDate` | TField |  | This field stores the Account Expense Rerun date, Last four quarter values can be given |
| 38 | `ACC.PARAM.ACTHOM.RUN.DATE` | `ItregeAccountmovmtParam_ActhomRunDate` | TField |  | This field stores the Home Bank Rerun date, Last two year values can be given |
| 39 | `ACC.PARAM.PL.ACCOUNT` | `ItregeAccountmovmtParam_PlAccount` |  |  |  |
| 40 | `ACC.PARAM.CATEGORY` | `ItregeAccountmovmtParam_Category` |  |  |  |
| 41 | `ACC.PARAM.MODE.IDENTIFICATION` | `ItregeAccountmovmtParam_ModeIdentification` | TField |  | This field refers to the identification mode |
| 42 | `ACC.PARAM.TECH.TYPE` | `ItregeAccountmovmtParam_TechType` | TField |  | This field refers to the technology type. It is usually connected via app from mobile device |
| 43 | `ACC.PARAM.TELEMATIC.TYPE` | `ItregeAccountmovmtParam_TelematicType` | TField |  | This field refers to the type of telematic services |
| 44 | `ACC.PARAM.IND.AISP` | `ItregeAccountmovmtParam_IndAisp` | TField |  | Holds the value of providers of account information service providers |
| 45 | `ACC.PARAM.UIC.DEVICE.LOC` | `ItregeAccountmovmtParam_UicDeviceLoc` | TField |  | This field refers to the UIC device location |
| 46 | `ACC.PARAM.ACCEXP.IGNORE.PL` | `ItregeAccountmovmtParam_AccexpIgnorePl` |  |  |  |
| 47 | `ACC.PARAM.RESERVED.2` | `ItregeAccountmovmtParam_Reserved2` | TField |  |  |
| 48 | `ACC.PARAM.RESERVED.1` | `ItregeAccountmovmtParam_Reserved1` | TField |  |  |
| 49 | `ACC.PARAM.OVERRIDE` | `ItregeAccountmovmtParam_Override` |  |  |  |
| 50 | `ACC.PARAM.RECORD.STATUS` | `ItregeAccountmovmtParam_RecordStatus` | String |  |  |
| 51 | `ACC.PARAM.CURR.NO` | `ItregeAccountmovmtParam_CurrNo` | String |  |  |
| 52 | `ACC.PARAM.INPUTTER` | `ItregeAccountmovmtParam_Inputter` |  |  |  |
| 53 | `ACC.PARAM.DATE.TIME` | `ItregeAccountmovmtParam_DateTime` |  |  |  |
| 54 | `ACC.PARAM.AUTHORISER` | `ItregeAccountmovmtParam_Authoriser` | String |  |  |
| 55 | `ACC.PARAM.CO.CODE` | `ItregeAccountmovmtParam_CoCode` | String |  |  |
| 56 | `ACC.PARAM.DEPT.CODE` | `ItregeAccountmovmtParam_DeptCode` | String |  |  |
| 57 | `ACC.PARAM.AUDITOR.CODE` | `ItregeAccountmovmtParam_AuditorCode` | String |  |  |
| 58 | `ACC.PARAM.AUDIT.DATE.TIME` | `ItregeAccountmovmtParam_AuditDateTime` | String |  |  |
| 59 | `ACC.PARAM.SCHEDULED.PROPERTY` | `ItregeAccountmovmtParam_ScheduledProperty` |  |  |  |
| 60 | `ACC.PARAM.TPH.FEE.TYPE` | `ItregeAccountmovmtParam_TphFeeType` |  |  |  |
| 61 | `ACC.PARAM.TPH.INCOME.LOSS.MOVMT.TYPE` | `ItregeAccountmovmtParam_TphIncomeLossMovmtType` |  |  |  |
| 62 | `ACC.PARAM.TPH.DEBIT.CREDIT.TXN.SIGN` | `ItregeAccountmovmtParam_TphDebitCreditTxnSign` |  |  |  |
| 63 | `ACC.PARAM.TPH.DEBIT.CREDIT.MOVMT.TYPE` | `ItregeAccountmovmtParam_TphDebitCreditMovmtType` |  |  |  |
| 64 | `ACC.PARAM.TPH.FEE.CODE` | `ItregeAccountmovmtParam_TphFeeCode` |  |  |  |
