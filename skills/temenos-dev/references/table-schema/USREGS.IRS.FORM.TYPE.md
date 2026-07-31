# USREGS.IRS.FORM.TYPE — Table Schema

> Source: `INSERTS/I_F.USREGS.IRS.FORM.TYPE` in `USREGS_YearEndTaxReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TX.TYPE.DESCRIPTION` | `UsregsIrsFormType_Description` |  |  |  |
| 2 | `TX.TYPE.MAP.FILE` | `UsregsIrsFormType_MapFile` |  |  |  |
| 3 | `TX.TYPE.SYSTEM.ID` | `UsregsIrsFormType_SystemId` |  |  |  |
| 4 | `TX.TYPE.ID.MAP.FLD` | `UsregsIrsFormType_IdMapFld` |  |  |  |
| 5 | `TX.TYPE.ID.ROUTINE` | `UsregsIrsFormType_IdRoutine` |  |  |  |
| 6 | `TX.TYPE.RESERVED.18` | `UsregsIrsFormType_Reserved18` | TField |  |  |
| 7 | `TX.TYPE.RESERVED.17` | `UsregsIrsFormType_Reserved17` | TField |  |  |
| 8 | `TX.TYPE.AMOUNT.TYPE` | `UsregsIrsFormType_AmountType` |  |  |  |
| 9 | `TX.TYPE.PAYMENT.AMOUNT.POS` | `UsregsIrsFormType_PaymentAmountPos` |  |  |  |
| 10 | `TX.TYPE.TXN.CODE` | `UsregsIrsFormType_TxnCode` |  |  |  |
| 11 | `TX.TYPE.TXN.SYS.ID` | `UsregsIrsFormType_TxnSysId` |  |  |  |
| 12 | `TX.TYPE.TXN.ROUTINE` | `UsregsIrsFormType_TxnRoutine` |  |  |  |
| 13 | `TX.TYPE.MAP.CODE` | `UsregsIrsFormType_MapCode` |  |  |  |
| 14 | `TX.TYPE.AMOUNT.CONVERSION` | `UsregsIrsFormType_AmountConversion` |  |  |  |
| 15 | `TX.TYPE.INC.CATEGORY` | `UsregsIrsFormType_IncCategory` |  |  |  |
| 16 | `TX.TYPE.CONDITION.RTN` | `UsregsIrsFormType_ConditionRtn` | TField |  | The application allows conditional reporting only based on category. If additional conditions needs to be done then this can be catered using the condition routine API. The condition routine is triggered before id mapping and transaction mapping. Max 35 Alphanumeric character |
| 17 | `TX.TYPE.INT.MIN.AMT` | `UsregsIrsFormType_IntMinAmt` | TField |  | Minimum Amount for which the transaction will be considered. AMOUNT field. Max 19 Numeric character |
| 18 | `TX.TYPE.EXC.RESIDENCE` | `UsregsIrsFormType_ExcResidence` | TField |  | Shows the residence details which are to be excluded from the IRS processing Max 4 Alpha character |
| 19 | `TX.TYPE.EXC.SECTOR` | `UsregsIrsFormType_ExcSector` |  |  |  |
| 20 | `TX.TYPE.TAX.CERT.TYPE` | `UsregsIrsFormType_TaxCertType` |  |  |  |
| 21 | `TX.TYPE.CERTIFIED.STATUS` | `UsregsIrsFormType_CertifiedStatus` |  |  |  |
| 22 | `TX.TYPE.VDATE.ADJUST` | `UsregsIrsFormType_VdateAdjust` |  |  |  |
| 23 | `TX.TYPE.VDAT.ADJ.TXN` | `UsregsIrsFormType_VdatAdjTxn` |  |  |  |
| 24 | `TX.TYPE.INC.RESIDENCE` | `UsregsIrsFormType_IncResidence` | TField |  |  |
| 25 | `TX.TYPE.ACCT.BASED.REPORTING` | `UsregsIrsFormType_AcctBasedReporting` | TField |  |  |
| 26 | `TX.TYPE.DATE.WISE.REPORTING` | `UsregsIrsFormType_DateWiseReporting` | TField |  |  |
| 27 | `TX.TYPE.MAP.OPTION` | `UsregsIrsFormType_MapOption` |  |  |  |
| 28 | `TX.TYPE.MAP.TXN.CODE` | `UsregsIrsFormType_MapTxnCode` |  |  |  |
| 29 | `TX.TYPE.ID.VARIANCE` | `UsregsIrsFormType_IdVariance` | TField |  | Configuration to indicate the 6th part of ID for IRS Tax details table Allowed options are below 1099R � 6th part of ID would be a combination of plan type and distribution code 5498 � 6th part of ID would the plan type. |
| 30 | `TX.TYPE.INC.SECTOR` | `UsregsIrsFormType_IncSector` |  |  |  |
| 31 | `TX.TYPE.RESERVED.5` | `UsregsIrsFormType_Reserved5` | TField |  |  |
| 32 | `TX.TYPE.RESERVED.4` | `UsregsIrsFormType_Reserved4` | TField |  |  |
| 33 | `TX.TYPE.RESERVED.3` | `UsregsIrsFormType_Reserved3` | TField |  |  |
| 34 | `TX.TYPE.RESERVED.2` | `UsregsIrsFormType_Reserved2` | TField |  |  |
| 35 | `TX.TYPE.RESERVED.1` | `UsregsIrsFormType_Reserved1` | TField |  |  |
| 36 | `TX.TYPE.OVERRIDE` | `UsregsIrsFormType_Override` |  |  |  |
| 37 | `TX.TYPE.RECORD.STATUS` | `UsregsIrsFormType_RecordStatus` | String |  |  |
| 38 | `TX.TYPE.CURR.NO` | `UsregsIrsFormType_CurrNo` | String |  |  |
| 39 | `TX.TYPE.INPUTTER` | `UsregsIrsFormType_Inputter` |  |  |  |
| 40 | `TX.TYPE.DATE.TIME` | `UsregsIrsFormType_DateTime` |  |  |  |
| 41 | `TX.TYPE.AUTHORISER` | `UsregsIrsFormType_Authoriser` | String |  |  |
| 42 | `TX.TYPE.CO.CODE` | `UsregsIrsFormType_CoCode` | String |  |  |
| 43 | `TX.TYPE.DEPT.CODE` | `UsregsIrsFormType_DeptCode` | String |  |  |
| 44 | `TX.TYPE.AUDITOR.CODE` | `UsregsIrsFormType_AuditorCode` | String |  |  |
| 45 | `TX.TYPE.AUDIT.DATE.TIME` | `UsregsIrsFormType_AuditDateTime` | String |  |  |
