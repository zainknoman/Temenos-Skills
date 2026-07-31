# CAMB.AML.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.AML.PARAM` in `CABASE_AMLInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.AML.DESCRIPTION` | `CambAmlParam_Description` |  |  |  |
| 2 | `CAMB.AML.CATEG.TXN.FLAG` | `CambAmlParam_CategTxnFlag` | TField |  | Reserved for future use. Not in use now. |
| 3 | `CAMB.AML.EXC.CATEG.CODE` | `CambAmlParam_ExcCategCode` |  |  |  |
| 4 | `CAMB.AML.TXN.CODE` | `CambAmlParam_TxnCode` |  |  |  |
| 5 | `CAMB.AML.TFS.TXN.CODE` | `CambAmlParam_TfsTxnCode` |  |  |  |
| 6 | `CAMB.AML.CCY.TO.TRACK` | `CambAmlParam_CcyToTrack` |  |  |  |
| 7 | `CAMB.AML.TIME.IN.HOUR` | `CambAmlParam_TimeInHour` | TField |  | Time limit between financial transactions to be considered for aggregation for LCTR reporting.Eg. 24Threshold of aggregation of CAD 10,000 within 24 hours will be considered for LCTR reporting. |
| 8 | `CAMB.AML.LIM.AMT.CAD` | `CambAmlParam_LimAmtCad` | TField |  | Field to define the threshold amount above which Cash transaction should be considered for LCTR ReportingEg. 10,000Single cash transactions of CAD 10,000 or multiple cash transactions aggreate to cad 10,000 wihin 24hrs will be considered for LCTR reporting. |
| 9 | `CAMB.AML.CUST.TYPE.PERS` | `CambAmlParam_CustTypePers` |  |  |  |
| 10 | `CAMB.AML.CUST.TYPE.NON.PERS` | `CambAmlParam_CustTypeNonPers` |  |  |  |
| 11 | `CAMB.AML.CONSOL.TXN.OTH` | `CambAmlParam_ConsolTxnOth` |  |  |  |
| 12 | `CAMB.AML.PERS.VERSION` | `CambAmlParam_PersVersion` |  |  |  |
| 13 | `CAMB.AML.NPERS.VERSION` | `CambAmlParam_NpersVersion` |  |  |  |
| 14 | `CAMB.AML.NOON.RATE.CCY.MKT` | `CambAmlParam_NoonRateCcyMkt` | TField |  | File to define the Noon rate currency market required for FCY to LCY conversion calculation.Validations - Valid record of CURRENCY.MARKETEg - 15. If any cash transaction with foreign currency is executed, the exchange rate for FCY to LCY conversion will be based on the rate defined in the record 15 &gt; CURRENCY.MARKET |
| 15 | `CAMB.AML.INTRF.FT.TXN.CODE` | `CambAmlParam_IntrfFtTxnCode` |  |  |  |
| 16 | `CAMB.AML.LCTR.SUPPORT.TXN` | `CambAmlParam_LctrSupportTxn` | TField |  | Field to indicate if the Supporting Tranaction should be updated in AML/LCTR form - in case of aggregration 24 hrs period.Valid inputs YES/ NOYES - all supporting transactions will be updated in LCTR/AML Form, that is considered for 24 Hrs period, and Total amount of All transactions is GT Threshold amount.NO - supporting transactions will NOT be updated in LCTR/AML Form, that is considered for 24 Hrs period, and Total amount of All transactions is GT Threshold amount. |
| 17 | `CAMB.AML.TFS.UNDERLY.TXN` | `CambAmlParam_TfsUnderlyTxn` | TField |  | Field to indicate if Underlying FT/TT reference to be updated in AML form for TFS transaction or not.Valid inputs YES/NOYES - underlying FT/TT transaction reference will be updated in AML form instead of TFS referenceNO - TFS reference will be updated in AML form instead ofunderlying FT/TT reference |
| 18 | `CAMB.AML.DAYS.MOVE.TO.HIST` | `CambAmlParam_DaysMoveToHist` | TField |  | field to define the Number of days after the LCTR extraction, the AML record (CAMB.AML.LOG) should be moved to history. |
| 19 | `CAMB.AML.INT.MAN.FT.TX.CDE` | `CambAmlParam_IntManFtTxCde` |  |  |  |
| 20 | `CAMB.AML.REL.ACCT` | `CambAmlParam_RelAcct` | TField |  | This field is used to indicate whether LCTR validation to be triggered for related customer or not.Valid Inputs : YES/NOIf set to 'YES', system will consider all related customer and account for validating LCTR functionality.If set to 'NO' , system will consider only own customer and account for validating LCTR |
| 21 | `CAMB.AML.EXCL.SINGLE.LCTR` | `CambAmlParam_ExclSingleLctr` | TField |  | This field is used to Indicate if cash transaction with Amount GT Threshold amount should be considered for aggreegation or not in 24 hrs period.Valid Inputs YES / NOYes Cash transaction of 10,000 or more will not be included as part consolidated amount calculation for 24 hrs period.No --&gt; Cash transaction of 10,000 or more will be included as part consolidated amount calculation for 24 hrs period. Comment no addressed. Hence chnaged |
| 22 | `CAMB.AML.NIT.DEP.TFS.CDE` | `CambAmlParam_NitDepTfsCde` |  |  |  |
| 23 | `CAMB.AML.TFS.TXN` | `CambAmlParam_TfsTxn` |  |  |  |
| 24 | `CAMB.AML.TT.TXN` | `CambAmlParam_TtTxn` |  |  |  |
| 25 | `CAMB.AML.FT.TXN` | `CambAmlParam_FtTxn` |  |  |  |
| 26 | `CAMB.AML.AML.AMOUNT` | `CambAmlParam_AmlAmount` |  |  |  |
| 27 | `CAMB.AML.CONDUCTOR.CIF.REQ` | `CambAmlParam_ConductorCifReq` |  |  |  |
| 28 | `CAMB.AML.RESERVED.5` | `CambAmlParam_Reserved5` |  |  |  |
| 29 | `CAMB.AML.RESERVED.4` | `CambAmlParam_Reserved4` |  |  |  |
| 30 | `CAMB.AML.CONDUCTOR.VERSION` | `CambAmlParam_ConductorVersion` | TField |  | Purpose of the field to define the version to populate the Conductor form.Example - CAMB.AML.LOG,CONDUCTORValid records VERSION |
| 31 | `CAMB.AML.PERSONAL.CONDUCTOR.TYPE` | `CambAmlParam_PersonalConductorType` |  |  |  |
| 32 | `CAMB.AML.CIF.PERSONAL` | `CambAmlParam_CifPersonal` | TField |  | Field to define the version in which the Customer record will be populated to create a Personal Conductor CIF.Valid records of VERSION. |
| 33 | `CAMB.AML.CIF.NPERSONAL` | `CambAmlParam_CifNpersonal` | TField |  | Field to define the version in which the Customer record will be populated to create a Non-Personal Conductor CIF.Valid records of VERSION |
| 34 | `CAMB.AML.AML.FUNCTION` | `CambAmlParam_AmlFunction` | TField | Yes | Purpose of the field to indicate the AML form used by the FI.Allowed inputs:LCTR / Conductor / BothLCTR: LCTR form will be populated for AML check.Conductor: Conductor form will be populated for AML check.Both: Both LCTR and Conductor validation will checked and if both matches, LCTR form will be populated.Mandatory field. |
| 35 | `CAMB.AML.RESERVED.3` | `CambAmlParam_Reserved3` | TField |  |  |
| 36 | `CAMB.AML.RESERVED.2` | `CambAmlParam_Reserved2` | TField |  |  |
| 37 | `CAMB.AML.RESERVED.1` | `CambAmlParam_Reserved1` | TField |  |  |
| 38 | `CAMB.AML.LOCAL.REF` | `CambAmlParam_LocalRef` |  |  |  |
| 39 | `CAMB.AML.RECORD.STATUS` | `CambAmlParam_RecordStatus` | String |  |  |
| 40 | `CAMB.AML.CURR.NO` | `CambAmlParam_CurrNo` | String |  |  |
| 41 | `CAMB.AML.INPUTTER` | `CambAmlParam_Inputter` |  |  |  |
| 42 | `CAMB.AML.DATE.TIME` | `CambAmlParam_DateTime` |  |  |  |
| 43 | `CAMB.AML.AUTHORISER` | `CambAmlParam_Authoriser` | String |  |  |
| 44 | `CAMB.AML.CO.CODE` | `CambAmlParam_CoCode` | String |  |  |
| 45 | `CAMB.AML.DEPT.CODE` | `CambAmlParam_DeptCode` | String |  |  |
| 46 | `CAMB.AML.AUDITOR.CODE` | `CambAmlParam_AuditorCode` | String |  |  |
| 47 | `CAMB.AML.AUDIT.DATE.TIME` | `CambAmlParam_AuditDateTime` | String |  |  |
