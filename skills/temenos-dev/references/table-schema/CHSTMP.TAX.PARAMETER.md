# CHSTMP.TAX.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CHSTMP.TAX.PARAMETER` in `CHSTMP_SwissTaxStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TAXPARAM.CA.EVENT.TYPE` | `ChstmpTaxParameter_CaEventType` |  |  |  |
| 2 | `TAXPARAM.SWISS.TAX.CODE` | `ChstmpTaxParameter_SwissTaxCode` |  |  |  |
| 3 | `TAXPARAM.ZERO.TAX.CODE` | `ChstmpTaxParameter_ZeroTaxCode` |  |  |  |
| 4 | `TAXPARAM.FGN.TAX.CODE` | `ChstmpTaxParameter_FgnTaxCode` |  |  |  |
| 5 | `TAXPARAM.US.TAX.CODE` | `ChstmpTaxParameter_UsTaxCode` |  |  |  |
| 6 | `TAXPARAM.REDEEM.EVENT.TYPE` | `ChstmpTaxParameter_RedeemEventType` |  |  |  |
| 7 | `TAXPARAM.PRODUCT.NAME` | `ChstmpTaxParameter_ProductName` |  |  |  |
| 8 | `TAXPARAM.PROPERTY.NAME` | `ChstmpTaxParameter_PropertyName` |  |  |  |
| 9 | `TAXPARAM.FUND.ACCUMULATION` | `ChstmpTaxParameter_FundAccumulation` | TField |  | The keyword to identify the accumulated funds from CHSTMP.FISCAL.DATA template. |
| 10 | `TAXPARAM.FUND.DISTRIBUTION` | `ChstmpTaxParameter_FundDistribution` | TField |  | The keyword to identify the distributing funds from the CHSTMP.FISCAL.DATA template. |
| 11 | `TAXPARAM.LOCAL.REF` | `ChstmpTaxParameter_LocalRef` |  |  |  |
| 12 | `TAXPARAM.RESERVED.5` | `ChstmpTaxParameter_Reserved5` | TField |  |  |
| 13 | `TAXPARAM.RESERVED.4` | `ChstmpTaxParameter_Reserved4` | TField |  |  |
| 14 | `TAXPARAM.RESERVED.3` | `ChstmpTaxParameter_Reserved3` | TField |  |  |
| 15 | `TAXPARAM.RESERVED.2` | `ChstmpTaxParameter_Reserved2` | TField |  |  |
| 16 | `TAXPARAM.RESERVED.1` | `ChstmpTaxParameter_Reserved1` | TField |  |  |
| 17 | `TAXPARAM.OVERRIDE` | `ChstmpTaxParameter_Override` |  |  |  |
| 18 | `TAXPARAM.RECORD.STATUS` | `ChstmpTaxParameter_RecordStatus` | String |  |  |
| 19 | `TAXPARAM.CURR.NO` | `ChstmpTaxParameter_CurrNo` | String |  |  |
| 20 | `TAXPARAM.INPUTTER` | `ChstmpTaxParameter_Inputter` |  |  |  |
| 21 | `TAXPARAM.DATE.TIME` | `ChstmpTaxParameter_DateTime` |  |  |  |
| 22 | `TAXPARAM.AUTHORISER` | `ChstmpTaxParameter_Authoriser` | String |  |  |
| 23 | `TAXPARAM.CO.CODE` | `ChstmpTaxParameter_CoCode` | String |  |  |
| 24 | `TAXPARAM.DEPT.CODE` | `ChstmpTaxParameter_DeptCode` | String |  |  |
| 25 | `TAXPARAM.AUDITOR.CODE` | `ChstmpTaxParameter_AuditorCode` | String |  |  |
| 26 | `TAXPARAM.AUDIT.DATE.TIME` | `ChstmpTaxParameter_AuditDateTime` | String |  |  |
