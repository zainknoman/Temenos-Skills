# INLEND.LDPD.PARAMETER — Table Schema

> Source: `INSERTS/I_F.INLEND.LDPD.PARAMETER` in `INLEND_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.LDPD.PSA.CATEGORY` | `InlendLdpdParameter_PsaCategory` |  |  |  |
| 2 | `INLEND.LDPD.PSA.LIMIT` | `InlendLdpdParameter_PsaLimit` |  |  |  |
| 3 | `INLEND.LDPD.PSA.PNEL.RATE` | `InlendLdpdParameter_PsaPnelRate` |  |  |  |
| 4 | `INLEND.LDPD.PSA.SPREAD.RATE` | `InlendLdpdParameter_PsaSpreadRate` |  |  |  |
| 5 | `INLEND.LDPD.CATEGORY` | `InlendLdpdParameter_Category` |  |  |  |
| 6 | `INLEND.LDPD.NO.OF.ROLLOVER.ALLWD` | `InlendLdpdParameter_NoOfRolloverAllwd` |  |  |  |
| 7 | `INLEND.LDPD.SUSPENSE.CATEGORY` | `InlendLdpdParameter_SuspenseCategory` |  |  |  |
| 8 | `INLEND.LDPD.LAR.BOR.CATEGORY` | `InlendLdpdParameter_LarBorCategory` |  |  |  |
| 9 | `INLEND.LDPD.MINIMUM.TENOR` | `InlendLdpdParameter_MinimumTenor` |  |  |  |
| 10 | `INLEND.LDPD.ACCOUNT.IRREGULAR` | `InlendLdpdParameter_AccountIrregular` | TField |  | It will hold the no.of.days, post which the account will move to irregular status |
| 11 | `INLEND.LDPD.RESTRUCT.INT.ACCT` | `InlendLdpdParameter_RestructIntAcct` | TField |  | This internal account, used to adjust the proceeds while doing the restructuring of loan |
| 12 | `INLEND.LDPD.ASSET.CLASS` | `InlendLdpdParameter_AssetClass` |  |  |  |
| 13 | `INLEND.LDPD.OVERDUE.START.RANGE` | `InlendLdpdParameter_OverdueStartRange` |  |  |  |
| 14 | `INLEND.LDPD.RESERVED.1` | `InlendLdpdParameter_Reserved1` | TField |  |  |
| 15 | `INLEND.LDPD.LOCAL.REF` | `InlendLdpdParameter_LocalRef` |  |  |  |
| 16 | `INLEND.LDPD.OVERRIDE` | `InlendLdpdParameter_Override` |  |  |  |
| 17 | `INLEND.LDPD.RECORD.STATUS` | `InlendLdpdParameter_RecordStatus` | String |  |  |
| 18 | `INLEND.LDPD.CURR.NO` | `InlendLdpdParameter_CurrNo` | String |  |  |
| 19 | `INLEND.LDPD.INPUTTER` | `InlendLdpdParameter_Inputter` |  |  |  |
| 20 | `INLEND.LDPD.DATE.TIME` | `InlendLdpdParameter_DateTime` |  |  |  |
| 21 | `INLEND.LDPD.AUTHORISER` | `InlendLdpdParameter_Authoriser` | String |  |  |
| 22 | `INLEND.LDPD.CO.CODE` | `InlendLdpdParameter_CoCode` | String |  |  |
| 23 | `INLEND.LDPD.DEPT.CODE` | `InlendLdpdParameter_DeptCode` | String |  |  |
| 24 | `INLEND.LDPD.AUDITOR.CODE` | `InlendLdpdParameter_AuditorCode` | String |  |  |
| 25 | `INLEND.LDPD.AUDIT.DATE.TIME` | `InlendLdpdParameter_AuditDateTime` | String |  |  |
