# CAREGS.CDIC.ACCT.TYPE.CODES — Table Schema

> Source: `INSERTS/I_F.CAREGS.CDIC.ACCT.TYPE.CODES` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.ACCT.CODES.MI.ACCT.TYPE` | `CaregsCdicAcctTypeCodes_MiAcctType` | TField |  | Field to define the default MI account type for the corresponding id Account type code to be reported in 0239 Account type tableExample:SA_1MT_2CA_3 |
| 2 | `CDIC.ACCT.CODES.ACCT.TYPE.DES` | `CaregsCdicAcctTypeCodes_AcctTypeDes` | TField |  | Field to define the default MI account type Description for the corresponding ID Account type code to be reported in 0239 Account type tableExample:Suspense Account.Mortgage tax account.Clearing Account (acss clearing) |
| 3 | `CDIC.ACCT.CODES.AA.PRODUCT` | `CaregsCdicAcctTypeCodes_AaProduct` |  |  |  |
| 4 | `CDIC.ACCT.CODES.AA.PRODUCT.GROUP` | `CaregsCdicAcctTypeCodes_AaProductGroup` |  |  |  |
| 5 | `CDIC.ACCT.CODES.AGC` | `CaregsCdicAcctTypeCodes_Agc` |  |  |  |
| 6 | `CDIC.ACCT.CODES.CATEGORY` | `CaregsCdicAcctTypeCodes_Category` |  |  |  |
| 7 | `CDIC.ACCT.CODES.ACCT` | `CaregsCdicAcctTypeCodes_Acct` |  |  |  |
| 8 | `CDIC.ACCT.CODES.RESERVED.1` | `CaregsCdicAcctTypeCodes_Reserved1` | TField |  |  |
| 9 | `CDIC.ACCT.CODES.RESERVED.2` | `CaregsCdicAcctTypeCodes_Reserved2` | TField |  |  |
| 10 | `CDIC.ACCT.CODES.RESERVED.3` | `CaregsCdicAcctTypeCodes_Reserved3` | TField |  |  |
| 11 | `CDIC.ACCT.CODES.RESERVED.4` | `CaregsCdicAcctTypeCodes_Reserved4` | TField |  |  |
| 12 | `CDIC.ACCT.CODES.RESERVED.5` | `CaregsCdicAcctTypeCodes_Reserved5` | TField |  |  |
| 13 | `CDIC.ACCT.CODES.RECORD.STATUS` | `CaregsCdicAcctTypeCodes_RecordStatus` | String |  |  |
| 14 | `CDIC.ACCT.CODES.CURR.NO` | `CaregsCdicAcctTypeCodes_CurrNo` | String |  |  |
| 15 | `CDIC.ACCT.CODES.INPUTTER` | `CaregsCdicAcctTypeCodes_Inputter` |  |  |  |
| 16 | `CDIC.ACCT.CODES.DATE.TIME` | `CaregsCdicAcctTypeCodes_DateTime` |  |  |  |
| 17 | `CDIC.ACCT.CODES.AUTHORISER` | `CaregsCdicAcctTypeCodes_Authoriser` | String |  |  |
| 18 | `CDIC.ACCT.CODES.CO.CODE` | `CaregsCdicAcctTypeCodes_CoCode` | String |  |  |
| 19 | `CDIC.ACCT.CODES.DEPT.CODE` | `CaregsCdicAcctTypeCodes_DeptCode` | String |  |  |
| 20 | `CDIC.ACCT.CODES.AUDITOR.CODE` | `CaregsCdicAcctTypeCodes_AuditorCode` | String |  |  |
| 21 | `CDIC.ACCT.CODES.AUDIT.DATE.TIME` | `CaregsCdicAcctTypeCodes_AuditDateTime` | String |  |  |
