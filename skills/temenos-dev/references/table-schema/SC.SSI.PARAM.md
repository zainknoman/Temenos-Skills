# SC.SSI.PARAM — Table Schema

> Source: `INSERTS/I_F.SC.SSI.PARAM` in `SC_SctTrading.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SSI.PARAM.STOCK.EXCHANGE` | `ScSsiParam_StockExchange` | TField |  | Numeric field and will accept priority number less than 5.It indicates what priority has been Assigned to fieldSTOCK.EXCHANGE When ISSUER field is inputted Priority can be given less than 6 |
| 2 | `SC.SSI.PARAM.PL.SETT` | `ScSsiParam_PlSett` | TField |  | Numeric field and will accept priority number less than 5.It indicates what priority has been Assigned to fieldPL.SETT When ISSUER field is inputted Priority can be given less than 6 |
| 3 | `SC.SSI.PARAM.SECURITY` | `ScSsiParam_Security` | TField |  | Numeric field and will accept priority number less than 5.It indicates what priority has been Assigned to fieldSECURITY When ISSUER field is inputted Priority can be given less than 6 |
| 4 | `SC.SSI.PARAM.ISIN.CTRY` | `ScSsiParam_IsinCtry` | TField |  | Numeric field and will accept priority number less than 5.It indicates what priority has been Assigned to fieldISIN.CTRY When ISSUER field is inputted Priority can be given less than 6 |
| 5 | `SC.SSI.PARAM.PRIORITY` | `ScSsiParam_Priority` |  |  |  |
| 6 | `SC.SSI.PARAM.LOCAL.REF` | `ScSsiParam_LocalRef` |  |  |  |
| 7 | `SC.SSI.PARAM.VALIDITY.CHECK` | `ScSsiParam_ValidityCheck` | TField |  | This field used to check Validity period in SSI with TradeDate Validation Rules: Allowed Values - Yes or Blank When this field is set as Yes, VALID.FROM, VALID.TO fields will be checked against TradeDate of the transaction |
| 8 | `SC.SSI.PARAM.PSET.TXN.DFLT` | `ScSsiParam_PsetTxnDflt` | TField |  | This field used to indicate whether the PSET should be determined automatically based on rules and default at thetransaction Validation Rules: Allowed Values - Yes, RULE.OR.SM or Blank When this field is set as Yes, PSET field will be auto determined based on PSET RULES and default at thetransaction When PSET.TXN.DEFAULT is RULE.OR.SM, system first tries to determine the PSET based on rule (SC.PSET.RULES) and defaults the same in the transaction.In case if no PSET is found based on the rules, the system will determine the SSI using the PL.SETT in SECURITY.MASTER and default the SSI in the Transact.The PSET updated in the SSI will therefore be populated as PSET in the Transaction.In case if PL.SETT is not defined in SECURITY.MASTER and the field SEC.DOMICILE.SSI is set, then the SECURITY.DOMICILE field in the respective SECURITY.MASTER record will be considered to determine the SSI.The PSET defined in the determined SSI will be populated as PSET in the transaction. |
| 9 | `SC.SSI.PARAM.CASH.SSI.PROCESS` | `ScSsiParam_CashSsiProcess` | TField |  | This field used to determine whether Cash SSI can be processed for the transaction Validation Rules: Allowed Values - Yes or Blank When this field is set as Yes, System checks the SC.CASH.SSI.INSTRUCT table for defaulting beneficiary details tothe transaction. |
| 10 | `SC.SSI.PARAM.CASH.SSI.PRIORITY` | `ScSsiParam_CashSsiPriority` |  |  |  |
| 11 | `SC.SSI.PARAM.CHECK.SETT.PARTY.RULES` | `ScSsiParam_CheckSettPartyRules` | TField |  |  |
| 12 | `SC.SSI.PARAM.RESERVED.05` | `ScSsiParam_Reserved05` |  |  |  |
| 13 | `SC.SSI.PARAM.RESERVED.04` | `ScSsiParam_Reserved04` | TField |  |  |
| 14 | `SC.SSI.PARAM.RESERVED.03` | `ScSsiParam_Reserved03` | TField |  |  |
| 15 | `SC.SSI.PARAM.RESERVED.02` | `ScSsiParam_Reserved02` | TField |  |  |
| 16 | `SC.SSI.PARAM.OVERRIDE` | `ScSsiParam_Override` |  |  |  |
| 17 | `SC.SSI.PARAM.RECORD.STATUS` | `ScSsiParam_RecordStatus` | String |  |  |
| 18 | `SC.SSI.PARAM.CURR.NO` | `ScSsiParam_CurrNo` | String |  |  |
| 19 | `SC.SSI.PARAM.INPUTTER` | `ScSsiParam_Inputter` |  |  |  |
| 20 | `SC.SSI.PARAM.DATE.TIME` | `ScSsiParam_DateTime` |  |  |  |
| 21 | `SC.SSI.PARAM.AUTHORISER` | `ScSsiParam_Authoriser` | String |  |  |
| 22 | `SC.SSI.PARAM.CO.CODE` | `ScSsiParam_CoCode` | String |  |  |
| 23 | `SC.SSI.PARAM.DEPT.CODE` | `ScSsiParam_DeptCode` | String |  |  |
| 24 | `SC.SSI.PARAM.AUDITOR.CODE` | `ScSsiParam_AuditorCode` | String |  |  |
| 25 | `SC.SSI.PARAM.AUDIT.DATE.TIME` | `ScSsiParam_AuditDateTime` | String |  |  |
| 26 | `SC.SSI.PARAM.ISSUER.GRP` | `ScSsiParam_IssuerGrp` | TField |  |  |
| 27 | `SC.SSI.PARAM.ISIN.GRP` | `ScSsiParam_IsinGrp` | TField |  | This field used to indicate whether the ISIN Group can be added as one of priority values of ASSET.SUB field Validation Rules: Yes � If set to Yes then the field ASSET.SUB will allow a valid ISIN group specified in the field SSI.ISIN.GRP. |
| 28 | `SC.SSI.PARAM.ALLOW.DUPLICATE` | `ScSsiParam_AllowDuplicate` | TField |  | This field used to create duplicate SSI for the same SSI combination. Validation Rules: Allowed Values - Yes or Blank |
