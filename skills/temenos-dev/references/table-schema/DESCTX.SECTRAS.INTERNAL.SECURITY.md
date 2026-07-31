# DESCTX.SECTRAS.INTERNAL.SECURITY — Table Schema

> Source: `INSERTS/I_F.DESCTX.SECTRAS.INTERNAL.SECURITY` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DESCTX.INT.SEC.SEC.PROD.TYPE` | `DesctxSectrasInternalSecurity_SecProdType` | TField |  | Security Product type. |
| 2 | `DESCTX.INT.SEC.VVT.INDICATOR` | `DesctxSectrasInternalSecurity_VvtIndicator` | TField |  | VVT indicator field |
| 3 | `DESCTX.INT.SEC.TAX.AGENT` | `DesctxSectrasInternalSecurity_TaxAgent` | TField |  | TAX agent field |
| 4 | `DESCTX.INT.SEC.INVEST.FUND.LIQ.IND` | `DesctxSectrasInternalSecurity_InvestFundLiqInd` | TField |  | Inverstment fund liquidation ind field |
| 5 | `DESCTX.INT.SEC.INVEST.FUND.LAW.IND` | `DesctxSectrasInternalSecurity_InvestFundLawInd` | TField |  | Inverstment fund law ind field |
| 6 | `DESCTX.INT.SEC.TRANSP.IND` | `DesctxSectrasInternalSecurity_TranspInd` | TField |  | Transparent ind field |
| 7 | `DESCTX.INT.SEC.REPL.VALUE.IND` | `DesctxSectrasInternalSecurity_ReplValueInd` | TField |  | REPL.VALUE ind field |
| 8 | `DESCTX.INT.SEC.EAV.IND` | `DesctxSectrasInternalSecurity_EavInd` | TField |  | EAV ind field |
| 9 | `DESCTX.INT.SEC.DOM.IND` | `DesctxSectrasInternalSecurity_DomInd` | TField |  | Domicile ind field |
| 10 | `DESCTX.INT.SEC.BID` | `DesctxSectrasInternalSecurity_Bid` | TField |  | Bid field |
| 11 | `DESCTX.INT.SEC.SKZ` | `DesctxSectrasInternalSecurity_Skz` | TField |  | Sort number field |
| 12 | `DESCTX.INT.SEC.FED.STATE.ISSUER` | `DesctxSectrasInternalSecurity_FedStateIssuer` | TField |  | Federal state issuer field |
| 13 | `DESCTX.INT.SEC.QUOTE.TYPE` | `DesctxSectrasInternalSecurity_QuoteType` | TField |  | Quote type field |
| 14 | `DESCTX.INT.SEC.ACCUM.IND` | `DesctxSectrasInternalSecurity_AccumInd` | TField |  | Accumulation ind field |
| 15 | `DESCTX.INT.SEC.TAX.DR.ACCT.IND` | `DesctxSectrasInternalSecurity_TaxDrAcctInd` | TField |  | Tax Debit account ind field |
| 16 | `DESCTX.INT.SEC.INTR.PERIOD.FROM` | `DesctxSectrasInternalSecurity_IntrPeriodFrom` | TField |  | Interest Period from field |
| 17 | `DESCTX.INT.SEC.INTR.PERIOD.TO` | `DesctxSectrasInternalSecurity_IntrPeriodTo` | TField |  | Interest Period to field |
| 18 | `DESCTX.INT.SEC.GRANDFATHERING.INDICATOR` | `DesctxSectrasInternalSecurity_GrandfatheringIndicator` | TField |  | Grandfathering indicator field |
| 19 | `DESCTX.INT.SEC.LOCAL.REF` | `DesctxSectrasInternalSecurity_LocalRef` |  |  |  |
| 20 | `DESCTX.INT.SEC.RESERVED.8` | `DesctxSectrasInternalSecurity_Reserved8` | TField |  |  |
| 21 | `DESCTX.INT.SEC.RESERVED.7` | `DesctxSectrasInternalSecurity_Reserved7` | TField |  |  |
| 22 | `DESCTX.INT.SEC.RESERVED.6` | `DesctxSectrasInternalSecurity_Reserved6` | TField |  |  |
| 23 | `DESCTX.INT.SEC.RESERVED.5` | `DesctxSectrasInternalSecurity_Reserved5` | TField |  |  |
| 24 | `DESCTX.INT.SEC.RESERVED.4` | `DesctxSectrasInternalSecurity_Reserved4` | TField |  |  |
| 25 | `DESCTX.INT.SEC.RESERVED.3` | `DesctxSectrasInternalSecurity_Reserved3` | TField |  |  |
| 26 | `DESCTX.INT.SEC.RESERVED.2` | `DesctxSectrasInternalSecurity_Reserved2` | TField |  |  |
| 27 | `DESCTX.INT.SEC.RESERVED.1` | `DesctxSectrasInternalSecurity_Reserved1` | TField |  |  |
| 28 | `DESCTX.INT.SEC.OVERRIDE` | `DesctxSectrasInternalSecurity_Override` |  |  |  |
| 29 | `DESCTX.INT.SEC.RECORD.STATUS` | `DesctxSectrasInternalSecurity_RecordStatus` | String |  |  |
| 30 | `DESCTX.INT.SEC.CURR.NO` | `DesctxSectrasInternalSecurity_CurrNo` | String |  |  |
| 31 | `DESCTX.INT.SEC.INPUTTER` | `DesctxSectrasInternalSecurity_Inputter` |  |  |  |
| 32 | `DESCTX.INT.SEC.DATE.TIME` | `DesctxSectrasInternalSecurity_DateTime` |  |  |  |
| 33 | `DESCTX.INT.SEC.AUTHORISER` | `DesctxSectrasInternalSecurity_Authoriser` | String |  |  |
| 34 | `DESCTX.INT.SEC.CO.CODE` | `DesctxSectrasInternalSecurity_CoCode` | String |  |  |
| 35 | `DESCTX.INT.SEC.DEPT.CODE` | `DesctxSectrasInternalSecurity_DeptCode` | String |  |  |
| 36 | `DESCTX.INT.SEC.AUDITOR.CODE` | `DesctxSectrasInternalSecurity_AuditorCode` | String |  |  |
| 37 | `DESCTX.INT.SEC.AUDIT.DATE.TIME` | `DesctxSectrasInternalSecurity_AuditDateTime` | String |  |  |
