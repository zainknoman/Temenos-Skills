# EB.GC.ACTIVE — Table Schema

> Source: `INSERTS/I_F.EB.GC.ACTIVE` in `EB_Constraints.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.GCA.APP.PROCESSING` | `EbGcActive_AppProcessing` | TField | Yes | Controls Global Constraints processing at application level. If set to 'YES' and also enabled at company or system level, record validation for this application will include Global Constraints processing. If set to 'NO', constraints processing will not occur. Mandatory input. |
| 2 | `EB.GCA.APP.DIAG` | `EbGcActive_AppDiag` | TField | Yes | Controls diagnostics recording at application level. If set to 'ON' and diagnostics recording is also enabled at company or system level and a constraint is breached, a record is created in EB.GC.DIAGNOSTIC giving details of constraint breach. If set to 'OFF', no diagnostics recording will occur. Mandatory field |
| 3 | `EB.GCA.APP.DIAG.LIFE` | `EbGcActive_AppDiagLife` | TField | No | Sets diagnostic life at application level. EB.GC.DIAGNOSTIC record produced when constraint breached will then be removed from system after this number of days has elapsed. Overrides setting of DIAG.LIFE at System or Company level. Optional Field. |
| 4 | `EB.GCA.APP.METHOD` | `EbGcActive_AppMethod` | TField | No | Specifies whether only the most specific valid constraint (EB.GC.CONSTRAINT) found is processed or if all constraints are processed. Constraints processing attempts to read constraints in a specific order as determined by the PRECEDENCE of the key fields, if COM.METHOD is 'SINGLE', the constraints processing ends when a valid constraint is found; if COM.METHOD is 'CUMULATIVE', the constraints processing ends when all existing constraints have been processed. If set to SINGLE, the constraints processing picks up the most specific constraint with respect to the record and application being processed, and if it is valid (in terms of FIRST.VALID.DATE and LAST.VALID.DATE), tests the record against the rules specified in the constraint, and does not process any further constraints. If set to CUMULATIVE, all constraints which are valid are processed in turn, in each case testing the record against the rules specified in the constraint. Overrides setting of METHOD at System or Company level. Optional Field. |
| 5 | `EB.GCA.CONSTRAINT.COUNT` | `EbGcActive_ConstraintCount` | TField |  | System generated field showing the number of constraints which exist against this application for information purposes only. |
| 6 | `EB.GCA.SELECTION.ROUTINE` | `EbGcActive_SelectionRoutine` | TField | No | Valid API or local subroutine. Routine overrides the default method of selection of constraint keys, therefore settings of METHOD, field associations, and PRECEDENCE fields (in EB.GC.PARAMETER) may not have the desired result when a selection routine is used, as they will not have any effect on processing of constraints when a SELECTION.ROUTINE is specified here beyond those explicitly coded within the SELECTION.ROUTINE itself. Optional Field. |
| 7 | `EB.GCA.CUSTOMER.FILE` | `EbGcActive_CustomerFile` |  |  |  |
| 8 | `EB.GCA.CUSTOMER.KEY` | `EbGcActive_CustomerKey` |  |  |  |
| 9 | `EB.GCA.CUSTOMER.FLD` | `EbGcActive_CustomerFld` |  |  |  |
| 10 | `EB.GCA.PORTFOLIO.FILE` | `EbGcActive_PortfolioFile` |  |  |  |
| 11 | `EB.GCA.PORTFOLIO.KEY` | `EbGcActive_PortfolioKey` |  |  |  |
| 12 | `EB.GCA.PORTFOLIO.FLD` | `EbGcActive_PortfolioFld` |  |  |  |
| 13 | `EB.GCA.PORT.FLD.ASSOC` | `EbGcActive_PortFldAssoc` | TField | No | Where there is more than one CUSTOMER.FLD specified and the PORTFOLIO.FLD is linked to the CUSTOMER.FLD within the same multivalue set on the source application, this field should be set to 'CUSTOMER'. Optional Field. |
| 14 | `EB.GCA.ACCOUNT.FILE` | `EbGcActive_AccountFile` |  |  |  |
| 15 | `EB.GCA.ACCOUNT.KEY` | `EbGcActive_AccountKey` |  |  |  |
| 16 | `EB.GCA.ACCOUNT.FLD` | `EbGcActive_AccountFld` |  |  |  |
| 17 | `EB.GCA.ACCT.FLD.ASSOC` | `EbGcActive_AcctFldAssoc` | TField | No | Where there is more than one CUSTOMER.FLD specified and the ACCOUNT.FLD is linked to the CUSTOMER.FLD within the same multivalue set on the source application, this field should be set to 'CUSTOMER'. If set to 'CUSTOMER', PORT.FLD.ASSOC must also be set to 'CUSTOMER' Optional Field. |
| 18 | `EB.GCA.CURRENCY.FILE` | `EbGcActive_CurrencyFile` |  |  |  |
| 19 | `EB.GCA.CURRENCY.KEY` | `EbGcActive_CurrencyKey` |  |  |  |
| 20 | `EB.GCA.CURRENCY.FLD` | `EbGcActive_CurrencyFld` |  |  |  |
| 21 | `EB.GCA.CURR.FLD.ASSOC` | `EbGcActive_CurrFldAssoc` | TField | No | Where there is more than one CUSTOMER.FLD specified and the CURRENCY.FLD is linked to the CUSTOMER.FLD within the same multivalue set on the source application, this field should be set to 'CUSTOMER'. If set to 'CUSTOMER', both ACCT.FLD.ASSOC and PORT.FLD.ASSOC must also be set to 'CUSTOMER'. Optional Field. |
| 22 | `EB.GCA.TRANS.DATE.FLD` | `EbGcActive_TransDateFld` | TField | No | Maps location of transaction date field in application. Used by constraints processing to determine date of transaction and therefore whether a particular constraint applies or not based upon validity dates of the constraint. Optional Field. |
| 23 | `EB.GCA.GROUP` | `EbGcActive_Group` |  |  |  |
| 24 | `EB.GCA.VSET.LOOKUP.ID` | `EbGcActive_VsetLookupId` |  |  |  |
| 25 | `EB.GCA.VSET.LOOKUP.FIELD` | `EbGcActive_VsetLookupField` |  |  |  |
| 26 | `EB.GCA.VSET.DATA.FIELD` | `EbGcActive_VsetDataField` |  |  |  |
| 27 | `EB.GCA.RESERVED1` | `EbGcActive_Reserved1` | TField |  |  |
| 28 | `EB.GCA.LOCAL.REF` | `EbGcActive_LocalRef` |  |  |  |
| 29 | `EB.GCA.OVERRIDE` | `EbGcActive_Override` |  |  |  |
| 30 | `EB.GCA.RECORD.STATUS` | `EbGcActive_RecordStatus` | String |  |  |
| 31 | `EB.GCA.CURR.NO` | `EbGcActive_CurrNo` | String |  |  |
| 32 | `EB.GCA.INPUTTER` | `EbGcActive_Inputter` |  |  |  |
| 33 | `EB.GCA.DATE.TIME` | `EbGcActive_DateTime` |  |  |  |
| 34 | `EB.GCA.AUTHORISER` | `EbGcActive_Authoriser` | String |  |  |
| 35 | `EB.GCA.CO.CODE` | `EbGcActive_CoCode` | String |  |  |
| 36 | `EB.GCA.DEPT.CODE` | `EbGcActive_DeptCode` | String |  |  |
| 37 | `EB.GCA.AUDITOR.CODE` | `EbGcActive_AuditorCode` | String |  |  |
| 38 | `EB.GCA.AUDIT.DATE.TIME` | `EbGcActive_AuditDateTime` | String |  |  |
