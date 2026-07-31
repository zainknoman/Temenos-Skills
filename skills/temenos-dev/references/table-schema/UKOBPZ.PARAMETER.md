# UKOBPZ.PARAMETER — Table Schema

> Source: `INSERTS/I_F.UKOBPZ.PARAMETER` in `UKOBPZ_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OBIE.PARAM.PERSONAL.SECTOR.FROM` | `UkobpzParameter_PersonalSectorFrom` | TField |  | This field no longer in use |
| 2 | `OBIE.PARAM.PERSONAL.SECTOR.TO` | `UkobpzParameter_PersonalSectorTo` | TField |  | This field no longer in use |
| 3 | `OBIE.PARAM.BUSINESS.SECTOR.FROM` | `UkobpzParameter_BusinessSectorFrom` | TField |  | This field no longer in use |
| 4 | `OBIE.PARAM.BUSINESS.SECTOR.TO` | `UkobpzParameter_BusinessSectorTo` | TField |  | This field no longer in use |
| 5 | `OBIE.PARAM.ACCOUNT.SCHEME` | `UkobpzParameter_AccountScheme` | TField |  | Field to store the schema name.Free text field. |
| 6 | `OBIE.PARAM.ALT.ACCT.TYPE` | `UkobpzParameter_AltAcctType` | TField |  | Alternate Account Type from this field is used to fetch the Alternate Account from Account Application . |
| 7 | `OBIE.PARAM.BIC.SCHEME` | `UkobpzParameter_BicScheme` | TField |  | This Scheme Name helps us identify the content of the Identification field Field to store the Bic schema name |
| 8 | `OBIE.PARAM.TRANSACTION.PERIOD` | `UkobpzParameter_TransactionPeriod` | TField |  | Field to store default Transaction Period to fetch statement details |
| 9 | `OBIE.PARAM.DD.ACCOUNT.STATUS` | `UkobpzParameter_DdAccountStatus` |  |  |  |
| 10 | `OBIE.PARAM.DD.STATUS` | `UkobpzParameter_DdStatus` |  |  |  |
| 11 | `OBIE.PARAM.STO.ACCOUNT.STATUS` | `UkobpzParameter_StoAccountStatus` |  |  |  |
| 12 | `OBIE.PARAM.STO.STATUS` | `UkobpzParameter_StoStatus` |  |  |  |
| 13 | `OBIE.PARAM.BNF.ACCOUNT.STATUS` | `UkobpzParameter_BnfAccountStatus` |  |  |  |
| 14 | `OBIE.PARAM.BNF.STATUS` | `UkobpzParameter_BnfStatus` |  |  |  |
| 15 | `OBIE.PARAM.ACCT.TYPE` | `UkobpzParameter_AcctType` |  |  |  |
| 16 | `OBIE.PARAM.PRD.GRP` | `UkobpzParameter_PrdGrp` |  |  |  |
| 17 | `OBIE.PARAM.OVERRIDE` | `UkobpzParameter_Override` |  |  |  |
| 18 | `OBIE.PARAM.LOCAL.REF` | `UkobpzParameter_LocalRef` |  |  |  |
| 19 | `OBIE.PARAM.RECORD.STATUS` | `UkobpzParameter_RecordStatus` | String |  |  |
| 20 | `OBIE.PARAM.CURR.NO` | `UkobpzParameter_CurrNo` | String |  |  |
| 21 | `OBIE.PARAM.INPUTTER` | `UkobpzParameter_Inputter` |  |  |  |
| 22 | `OBIE.PARAM.DATE.TIME` | `UkobpzParameter_DateTime` |  |  |  |
| 23 | `OBIE.PARAM.AUTHORISER` | `UkobpzParameter_Authoriser` | String |  |  |
| 24 | `OBIE.PARAM.CO.CODE` | `UkobpzParameter_CoCode` | String |  |  |
| 25 | `OBIE.PARAM.DEPT.CODE` | `UkobpzParameter_DeptCode` | String |  |  |
| 26 | `OBIE.PARAM.AUDITOR.CODE` | `UkobpzParameter_AuditorCode` | String |  |  |
| 27 | `OBIE.PARAM.AUDIT.DATE.TIME` | `UkobpzParameter_AuditDateTime` | String |  |  |
