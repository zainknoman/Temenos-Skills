# DESCTX.PORTFOLIO.FEEGROUP — Table Schema

> Source: `INSERTS/I_F.DESCTX.PORTFOLIO.FEEGROUP` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SECTRAS.FEEGRP.VALID.FROM.DATE` | `DesctxPortfolioFeegroup_ValidFromDate` |  |  |  |
| 2 | `SECTRAS.FEEGRP.FEE.GROUP` | `DesctxPortfolioFeegroup_FeeGroup` |  |  |  |
| 3 | `SECTRAS.FEEGRP.LOCAL.REF` | `DesctxPortfolioFeegroup_LocalRef` |  |  |  |
| 4 | `SECTRAS.FEEGRP.RESERVED.8` | `DesctxPortfolioFeegroup_Reserved8` | TField |  | This field is reserved for future use. |
| 5 | `SECTRAS.FEEGRP.RESERVED.7` | `DesctxPortfolioFeegroup_Reserved7` | TField |  | This field is reserved for future use. |
| 6 | `SECTRAS.FEEGRP.RESERVED.6` | `DesctxPortfolioFeegroup_Reserved6` | TField |  | This field is reserved for future use. |
| 7 | `SECTRAS.FEEGRP.RESERVED.5` | `DesctxPortfolioFeegroup_Reserved5` | TField |  | This field is reserved for future use. |
| 8 | `SECTRAS.FEEGRP.RESERVED.4` | `DesctxPortfolioFeegroup_Reserved4` | TField |  | This field is reserved for future use. |
| 9 | `SECTRAS.FEEGRP.RESERVED.3` | `DesctxPortfolioFeegroup_Reserved3` | TField |  | This field is reserved for future use. |
| 10 | `SECTRAS.FEEGRP.RESERVED.2` | `DesctxPortfolioFeegroup_Reserved2` | TField |  | This field is reserved for future use. |
| 11 | `SECTRAS.FEEGRP.RESERVED.1` | `DesctxPortfolioFeegroup_Reserved1` | TField |  | This field is reserved for future use. |
| 12 | `SECTRAS.FEEGRP.OVERRIDE` | `DesctxPortfolioFeegroup_Override` |  |  |  |
| 13 | `SECTRAS.FEEGRP.RECORD.STATUS` | `DesctxPortfolioFeegroup_RecordStatus` | String |  |  |
| 14 | `SECTRAS.FEEGRP.CURR.NO` | `DesctxPortfolioFeegroup_CurrNo` | String |  |  |
| 15 | `SECTRAS.FEEGRP.INPUTTER` | `DesctxPortfolioFeegroup_Inputter` |  |  |  |
| 16 | `SECTRAS.FEEGRP.DATE.TIME` | `DesctxPortfolioFeegroup_DateTime` |  |  |  |
| 17 | `SECTRAS.FEEGRP.AUTHORISER` | `DesctxPortfolioFeegroup_Authoriser` | String |  |  |
| 18 | `SECTRAS.FEEGRP.CO.CODE` | `DesctxPortfolioFeegroup_CoCode` | String |  |  |
| 19 | `SECTRAS.FEEGRP.DEPT.CODE` | `DesctxPortfolioFeegroup_DeptCode` | String |  |  |
| 20 | `SECTRAS.FEEGRP.AUDITOR.CODE` | `DesctxPortfolioFeegroup_AuditorCode` | String |  |  |
| 21 | `SECTRAS.FEEGRP.AUDIT.DATE.TIME` | `DesctxPortfolioFeegroup_AuditDateTime` | String |  |  |
