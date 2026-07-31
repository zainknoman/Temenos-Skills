# QI.PARAMETER — Table Schema

> Source: `INSERTS/I_F.QI.PARAMETER` in `QI_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `QI.PAR.AUTO.CALC.QI.STATUS` | `QiParameter_AutoCalcQiStatus` | TField |  | Yes or Null denotes that the Customer QI status calculation by system is required.NO denotes that the customers' QI statuses will be manually fed into QCSI table either manually or through aninterface. The fields RULE.TYPE, RULE.NAME and QI.EXEMPT.CODE must have values if this field is set to YES Validation Rules: Allowed values are YES,NO and null Default value 'Null' |
| 2 | `QI.PAR.RULE.TYPE` | `QiParameter_RuleType` |  |  |  |
| 3 | `QI.PAR.RULE.NAME` | `QiParameter_RuleName` |  |  |  |
| 4 | `QI.PAR.CHAP.3.4.EXEMPT.CODES.API` | `QiParameter_Chap34ExemptCodesApi` | TField |  | Field reserved for future use |
| 5 | `QI.PAR.QI.EXEMPT.CODE` | `QiParameter_QiExemptCode` | TField | Yes | Field holds the value that considered for reporting purpose when the withholding tax is applied per FATCA and thecorresponding exemption code as per Chapter III. Validation Rules: This field becomes mandatory when AUTO.CALC.QI.STATUS field is set to YES. |
| 6 | `QI.PAR.QI.TAX.TYPE` | `QiParameter_QiTaxType` | TField |  | Field holds the TAX.TYPE record that is used in applying Withholding TAX on US income from QI perspective.The Security transactions that are taxed under this tax type are considered to be updated in the QI.USDB.TX.DETAILStable Validation Rules: Valid record in TAX.TYPE table |
| 7 | `QI.PAR.FATCA.TAX.TYPE` | `QiParameter_FatcaTaxType` | TField | Yes | Field holds the TAX.TYPE record that is used in applying Withholding TAX on US income from FATCA perspective.The Security transactions that are taxed under this tax type are considered to be updated in the QI.USDB.TX.DETAILStable. The field is mandatory to be input only if FA product is installed. Validation Rules: Valid record in TAX.TYPE table |
| 8 | `QI.PAR.US.DB.HIST.MVMT` | `QiParameter_UsDbHistMvmt` | TField |  | Fields hold the month and year or a local API for the cut-off date for movement to history |
| 9 | `QI.PAR.RECALC.TAX.TYPE` | `QiParameter_RecalcTaxType` | TField |  | Field holds the TAX.TYPE record that is used in applying Back-up withholding TAX on sale of US securities wherethe customer's QI status is 'US undocumented'. The Security transactions that are taxed under this tax type are considered to be updated in theQI.USDB.TX.DETAILS The Tax is applied on the entire sale proceeds of the transaction at the rate applicable for back-up withholdingand as configured. Validation Rules: Valid record in TAX.TYPE table |
| 10 | `QI.PAR.REQD.DOC.TYPE` | `QiParameter_ReqdDocType` |  |  |  |
| 11 | `QI.PAR.MRGR.DEF.TAX.IC` | `QiParameter_MrgrDefTaxIc` | TField |  | For events subject to S302 regulation of US IRS, the tax is withheld at source at the time of the event andsubsequently based on the response provided by each holder in the S302 form, the tax liability is calculated andthe refund, if any is processed. This field holds a default Income Code under which proceeds from such events are treated (as taxable) based onthe S302 option. Validation Rules: Must be a valid SC.INCOME.CODE and is defaulted with a 06 code if given as NULL. |
| 12 | `QI.PAR.MRGR.DEF.NON.TAX.IC` | `QiParameter_MrgrDefNonTaxIc` | TField |  | For events subject to S302 regulation of US IRS, the tax is withheld at source at the time of the event andsubsequently based on the response provided by each holder in the S302 form, the tax liability is calculated andthe refund, if any is processed. This field holds a default Income Code under which proceeds from such events are treated (as non-taxable) basedon the S302 option. Validation Rules: Must be a valid SC.INCOME.CODE and is defaulted with a 09 code if given as NULL. |
| 13 | `QI.PAR.RESERVED.16` | `QiParameter_Reserved16` | TField |  | Reserved for future use |
| 14 | `QI.PAR.RESERVED.15` | `QiParameter_Reserved15` | TField |  | Reserved for future use |
| 15 | `QI.PAR.RESERVED.14` | `QiParameter_Reserved14` | TField |  | Reserved for future use |
| 16 | `QI.PAR.RESERVED.13` | `QiParameter_Reserved13` | TField |  | Reserved for future use |
| 17 | `QI.PAR.RESERVED.12` | `QiParameter_Reserved12` | TField |  | Reserved for future use |
| 18 | `QI.PAR.RESERVED.11` | `QiParameter_Reserved11` | TField |  | Reserved for future use |
| 19 | `QI.PAR.RESERVED.10` | `QiParameter_Reserved10` | TField |  | Reserved for future use |
| 20 | `QI.PAR.RESERVED.09` | `QiParameter_Reserved09` | TField |  | Reserved for future use |
| 21 | `QI.PAR.RESERVED.08` | `QiParameter_Reserved08` | TField |  | Reserved for future use |
| 22 | `QI.PAR.RESERVED.07` | `QiParameter_Reserved07` | TField |  | Reserved for future use |
| 23 | `QI.PAR.RESERVED.06` | `QiParameter_Reserved06` | TField |  | Reserved for future use |
| 24 | `QI.PAR.RESERVED.05` | `QiParameter_Reserved05` | TField |  | Reserved for future use |
| 25 | `QI.PAR.RESERVED.04` | `QiParameter_Reserved04` | TField |  | Reserved for future use |
| 26 | `QI.PAR.RESERVED.03` | `QiParameter_Reserved03` | TField |  | Reserved for future use |
| 27 | `QI.PAR.RESERVED.02` | `QiParameter_Reserved02` | TField |  | Reserved for future use |
| 28 | `QI.PAR.RESERVED.01` | `QiParameter_Reserved01` | TField |  | Reserved for future use |
| 29 | `QI.PAR.LOCAL.REF` | `QiParameter_LocalRef` |  |  |  |
| 30 | `QI.PAR.OVERRIDE` | `QiParameter_Override` |  |  |  |
| 31 | `QI.PAR.RECORD.STATUS` | `QiParameter_RecordStatus` | String |  | Status of the record |
| 32 | `QI.PAR.CURR.NO` | `QiParameter_CurrNo` | String |  | Curr No |
| 33 | `QI.PAR.INPUTTER` | `QiParameter_Inputter` |  |  |  |
| 34 | `QI.PAR.DATE.TIME` | `QiParameter_DateTime` |  |  |  |
| 35 | `QI.PAR.AUTHORISER` | `QiParameter_Authoriser` | String |  | Authoriser |
| 36 | `QI.PAR.CO.CODE` | `QiParameter_CoCode` | String |  | Company code |
| 37 | `QI.PAR.DEPT.CODE` | `QiParameter_DeptCode` | String |  | Department code |
| 38 | `QI.PAR.AUDITOR.CODE` | `QiParameter_AuditorCode` | String |  | Auditor Code |
| 39 | `QI.PAR.AUDIT.DATE.TIME` | `QiParameter_AuditDateTime` | String |  | Audit Date and time |
