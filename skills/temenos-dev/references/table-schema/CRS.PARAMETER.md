# CRS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CRS.PARAMETER` in `CD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CD.CP.EFFECTIVE.DATE` | `CrsParameter_EffectiveDate` | TField | Yes | Field to specify the effective date of the CRS regulation. Customers are identified as existing or new based on this date. Validation rules: This is a mandatory field. Any valid Date. Standard date format -(YYYYMMDD). |
| 2 | `CD.CP.PARTNG.JURIDICTION` | `CrsParameter_PartngJuridiction` |  |  |  |
| 3 | `CD.CP.TELEPHONE.CODE` | `CrsParameter_TelephoneCode` |  |  |  |
| 4 | `CD.CP.RESERVED.15` | `CrsParameter_Reserved15` |  |  |  |
| 5 | `CD.CP.RESERVED.14` | `CrsParameter_Reserved14` |  |  |  |
| 6 | `CD.CP.RESERVED.13` | `CrsParameter_Reserved13` |  |  |  |
| 7 | `CD.CP.INDICIA.CALC.RTN` | `CrsParameter_IndiciaCalcRtn` | TField |  | The logic to calculate the Indicia along with the reportable jurisdiction will be built into the API that is specified in this field. The CRS.GET.INDICIA api is provided with some default indicia determining logic. However, clients can replace this routine with locally customised logic (if required) If no routine is attached here, the INDICIA, REPORTABLE.JUR and CRS.STATUS fields in CRS.CUST.SUPP.INFO will not be calculated. Validation rules: Should be a valid EB.API record. |
| 8 | `CD.CP.CLOSE.REL.BAL.TYP` | `CrsParameter_CloseRelBalTyp` | TField |  | Field to decide whether the previous day customer balances should be calculated when the CRS.STATUS is changed to INACTIVE in CRS.CUST.SUPP.INFO table. By default system calculates balance aggregation every month end. If set as none or previous month, then system uses the default calculated balance. Validation rules: Allowed values are Null, PREVIOUS.MONTH, PREVIOUS.DAY. |
| 9 | `CD.CP.REPORTING.CCY` | `CrsParameter_ReportingCcy` | TField |  | Field to specify the reporting currency to be used for Balance aggregation process. If no value is specified, system calculates the aggregation balance in local currency of the corresponding company. Validation rules: Valid ID from CURRENCY table. |
| 10 | `CD.CP.INITIAL.AGGR.BUILT` | `CrsParameter_InitialAggrBuilt` | TField |  | Field to identify whether the initial balance aggregation process is performed for all the existing customers. System will update this field as 'YES', once the initial aggregation is completed. Validation rules: System updated field. No input |
| 11 | `CD.CP.AUTO.STATUS.UPDATE` | `CrsParameter_AutoStatusUpdate` | TField |  | This field indicates whether the indicia,Reportable jurisdiction and CRS Status to be auto updated by the system whenever participating jurisdictions or telephone code is changed. The COB job ST.UPDATE.INDICIA invokes the INDICIA.CALC.RTN to rebuild the status for all CRS customers. System will update this field as 'YES', once the initial aggregation is completed. Validation rules: System updated field. No input |
| 12 | `CD.CP.ACCOUNT.TYPE` | `CrsParameter_AccountType` |  |  |  |
| 13 | `CD.CP.ACCOUNT.SUB.TYPE` | `CrsParameter_AccountSubType` |  |  |  |
| 14 | `CD.CP.BAL.AMT.AGGR.FROM` | `CrsParameter_BalAmtAggrFrom` |  |  |  |
| 15 | `CD.CP.BAL.AMT.AGGR.TO` | `CrsParameter_BalAmtAggrTo` |  |  |  |
| 16 | `CD.CP.DUE.DILIGENCE.DATE` | `CrsParameter_DueDiligenceDate` |  |  |  |
| 17 | `CD.CP.REPORTING.DATE` | `CrsParameter_ReportingDate` |  |  |  |
| 18 | `CD.CP.RESERVED.12` | `CrsParameter_Reserved12` |  |  |  |
| 19 | `CD.CP.RESERVED.11` | `CrsParameter_Reserved11` |  |  |  |
| 20 | `CD.CP.RESERVED.10` | `CrsParameter_Reserved10` |  |  |  |
| 21 | `CD.CP.SC.GRACE.DAYS` | `CrsParameter_ScGraceDays` | TField |  | It indicates the maximum number of days within which the client is supposed to submit his Self-Certification Document. This field is used to calculate the CUT.OFF.DATE when the REQ.DATE is specified in CRS.CUST.SUPP.INFO. Validation rules: A valid number |
| 22 | `CD.CP.DORM.IDENT.APP` | `CrsParameter_DormIdentApp` | TField |  | This field allows the user to specify the application from which the Dormancy can be identified. Validation rules: Allowed applications either CUSTOMER or CRS.CUST.SUPP.INFO Allowed only when DEFLT.DORMANT is set. |
| 23 | `CD.CP.DORM.IDENT.FIELD` | `CrsParameter_DormIdentField` | TField |  | It defines from which field of an application the dormancy can be identified. Validation rules: Any valid field from the T24 application defined in DORM.IDENT.APP can be used. |
| 24 | `CD.CP.DORM.IDENT.OPERAND` | `CrsParameter_DormIdentOperand` | TField |  | It defines what operand has to be used to match the value with above defined field of application so that the dormancy can be identified. Validation rules: Only EQ operand can be used. |
| 25 | `CD.CP.DORM.IDENT.VALUE` | `CrsParameter_DormIdentValue` | TField |  | It defines what value has to be matched from the above defined field of application so that the dormancy can be identified. |
| 26 | `CD.CP.EIN` | `CrsParameter_Ein` | TField |  | This holds the identification number used by the sending tax administration to identify the Entity Account Holder. |
| 27 | `CD.CP.COUNTRY.RULE` | `CrsParameter_CountryRule` | TField | Yes | INDIVIDUAL or Blank - Standard OECD formatting. i.e. one XML output per customer Validation rules: If COUNTRY.RULE is INDIVIDUAL, then EB.TRANSFM.KEY should not be greater than One Value If COUNTRY.RULE is BULK, then EB.TRANSFM.KEY should not be greater than Two Values and the second multi value field should be mandatory input |
| 28 | `CD.CP.EB.TRANSFM.KEY` | `CrsParameter_EbTransfmKey` |  |  |  |
| 29 | `CD.CP.RESERVED.01` | `CrsParameter_Reserved01` | TField |  |  |
| 30 | `CD.CP.LOCAL.REF` | `CrsParameter_LocalRef` |  |  |  |
| 31 | `CD.CP.OVERRIDE` | `CrsParameter_Override` |  |  |  |
| 32 | `CD.CP.RECORD.STATUS` | `CrsParameter_RecordStatus` | String |  |  |
| 33 | `CD.CP.CURR.NO` | `CrsParameter_CurrNo` | String |  |  |
| 34 | `CD.CP.INPUTTER` | `CrsParameter_Inputter` |  |  |  |
| 35 | `CD.CP.DATE.TIME` | `CrsParameter_DateTime` |  |  |  |
| 36 | `CD.CP.AUTHORISER` | `CrsParameter_Authoriser` | String |  |  |
| 37 | `CD.CP.CO.CODE` | `CrsParameter_CoCode` | String |  |  |
| 38 | `CD.CP.DEPT.CODE` | `CrsParameter_DeptCode` | String |  |  |
| 39 | `CD.CP.AUDITOR.CODE` | `CrsParameter_AuditorCode` | String |  |  |
| 40 | `CD.CP.AUDIT.DATE.TIME` | `CrsParameter_AuditDateTime` | String |  |  |
| 41 | `CD.CP.TELE.CONT.TYPE` | `CrsParameter_TeleContType` |  |  |  |
| 42 | `CD.CP.POA.CODE` | `CrsParameter_PoaCode` |  |  |  |
| 43 | `CD.CP.INCARE.OF` | `CrsParameter_IncareOf` |  |  |  |
| 44 | `CD.CP.RULE.TYPE` | `CrsParameter_RuleType` |  |  |  |
| 45 | `CD.CP.RULE.ID` | `CrsParameter_RuleId` |  |  |  |
| 46 | `CD.CP.REQD.DOC.TYPE` | `CrsParameter_ReqdDocType` |  |  |  |
