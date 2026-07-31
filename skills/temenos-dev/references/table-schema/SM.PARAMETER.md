# SM.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SM.PARAMETER` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SM.PARAM.PRICE.QUAL.FORMAT` | `SmParameter_PriceQualFormat` | TField |  | Defines the validation to be applied to the fields CUM.INDICATE and EX.INDICATE. Used by SECURITY.MASTER to decide if the PRICE.QUAL.MARK field is to be in Swift format. Validation Rules: Must be SWIFT or blank |
| 2 | `SM.PARAM.CUM.INDICATE` | `SmParameter_CumIndicate` |  |  |  |
| 3 | `SM.PARAM.EX.INDICATE` | `SmParameter_ExIndicate` |  |  |  |
| 4 | `SM.PARAM.ALT.INDEX.DUP` | `SmParameter_AltIndexDup` | TField |  | This field controls the level of duplication allowed in the fields I.S.I.N., EUROCLEAR.NO, CEDEL.NO, SEDOL.NO, SWISS.NO and CUSIP.NO which can be defined as alternate indexes. If the field is set to blank or 001 then duplication of the index keys will be allowed but only one security with a suffix of -000 will be allowed per index key. For example 100147-000 and 100147-001 could share the same I.S.I.N. code but 100147-000 and 100148-000 cannot. If the field is set to NO then a one to one relationship between the SECURITY.MASTER key and the alternate index key must exist. No duplication will be allowed in any of the fields. If the field is set to YES the no checking will be performed on the index keys and they may be used any number of times on any number of SECURITY.MASTER records. If the field is set to OVERRIDE then an override message will be produced if the key is already used and acceptance will allow duplication. |
| 5 | `SM.PARAM.ISIN.VALIDATION` | `SmParameter_IsinValidation` | TField |  | Determines whether the ISIN code entered through the SECURITY.MASTER application is validated. If YES then the check digit must be as calculated by system. |
| 6 | `SM.PARAM.MAINT.AM.TSDATA` | `SmParameter_MaintAmTsdata` | TField |  | If AM is installed, this field determines whether the table AM.TSDATA is maintained or not. This field has no functionality if AM is not installed. |
| 7 | `SM.PARAM.ALPHA.KEY` | `SmParameter_AlphaKey` | TField |  | Enables the input of alphanumeric characters in the SECURITY.MASTER ID. Based on the format specified in the field SECURITY.FORMAT of the SC.PARAMETER, the setting of this field does not perform the formatting of SECURITY.MASTER reference. |
| 8 | `SM.PARAM.ALT.INDEX.CHECK` | `SmParameter_AltIndexCheck` | TField |  | This field is Set to Yes or Null |
| 9 | `SM.PARAM.SEC.DOMICILE.SSI` | `SmParameter_SecDomicileSsi` | TField |  | Allowed value is YES to say that SECURITY.DOMICILE field in SECURITY.MASTER will be considered for search in PL.SETT field of SC.SETT.INSTRUCT if PL.SETT is not defined in SECURITY.MASTER. |
| 10 | `SM.PARAM.MAINT.TIME.SERIES` | `SmParameter_MaintTimeSeries` | TField |  | This field will be set for recording the unit accruals and yield on a daily basis. The values will be recorded in SC.SEC.TIME.SERIES. Any backdated price change or back dated interest rate change done after the first recording will be considered. Validation Rules: Will accept the values YES and NULL. |
| 11 | `SM.PARAM.NONSHARED.SM` | `SmParameter_NonsharedSm` | TField |  |  |
| 12 | `SM.PARAM.RESERVED02` | `SmParameter_Reserved02` | TField |  |  |
| 13 | `SM.PARAM.RESERVED01` | `SmParameter_Reserved01` | TField |  |  |
| 14 | `SM.PARAM.LOCAL.REF` | `SmParameter_LocalRef` |  |  |  |
| 15 | `SM.PARAM.OVERRIDE` | `SmParameter_Override` |  |  |  |
| 16 | `SM.PARAM.RECORD.STATUS` | `SmParameter_RecordStatus` | String |  |  |
| 17 | `SM.PARAM.CURR.NO` | `SmParameter_CurrNo` | String |  |  |
| 18 | `SM.PARAM.INPUTTER` | `SmParameter_Inputter` |  |  |  |
| 19 | `SM.PARAM.DATE.TIME` | `SmParameter_DateTime` |  |  |  |
| 20 | `SM.PARAM.AUTHORISER` | `SmParameter_Authoriser` | String |  |  |
| 21 | `SM.PARAM.CO.CODE` | `SmParameter_CoCode` | String |  |  |
| 22 | `SM.PARAM.DEPT.CODE` | `SmParameter_DeptCode` | String |  |  |
| 23 | `SM.PARAM.AUDITOR.CODE` | `SmParameter_AuditorCode` | String |  |  |
| 24 | `SM.PARAM.AUDIT.DATE.TIME` | `SmParameter_AuditDateTime` | String |  |  |
