# TY.DEALER.PROFITABILITY — Table Schema

> Source: `INSERTS/I_F.TY.DEALER.PROFITABILITY` in `TY_Parameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TY.DEAL.DESCRIPTION` | `TyDealerProfitability_Description` | TField |  | Specifies a meaningful description for grouping the dealers based on the FX activity assigned , specific to a company. Multivalued Language specific field. |
| 2 | `TY.DEAL.CATEGORY.CONS.COND` | `TyDealerProfitability_CategoryConsCond` | TField |  | Identifies the user defined field name defined in CONSOLIDATE.COND for the filename CATEG.ENTRY with fieldname as PL.CATEGORY. Validation Rules: No-input field. Defaulted by the system with the NAME defined in CONSOLIDATE.COND of PROFIT &amp; LOSS, where the FILE.NAME is CATEG.ENTRY &amp; FIELD.NAME is PL.CATEGORY |
| 3 | `TY.DEAL.DEPT.RVL.CONS.COND` | `TyDealerProfitability_DeptRvlConsCond` | TField |  | Identifies the user defined field name defined in CONSOLIDATE.COND for the filename CATEG.ENTRY with fieldname as ACCOUNT.OFFICER. Validation Rules: No-input field. Defaulted by the system with the NAME defined in CONSOLIDATE.COND of PROFIT &amp; LOSS, where the FILE.NAME is CATEG.ENTRY FIELD.NAME is ACCOUNT.OFFICER |
| 4 | `TY.DEAL.GROUP.NAME` | `TyDealerProfitability_GroupName` |  |  |  |
| 5 | `TY.DEAL.DEALER.ID` | `TyDealerProfitability_DealerId` |  |  |  |
| 6 | `TY.DEAL.DEBIT.CATEGORY` | `TyDealerProfitability_DebitCategory` |  |  |  |
| 7 | `TY.DEAL.CREDIT.CATEGORY` | `TyDealerProfitability_CreditCategory` |  |  |  |
| 8 | `TY.DEAL.DEPT.FOR.REVAL` | `TyDealerProfitability_DeptForReval` |  |  |  |
| 9 | `TY.DEAL.RESERVED.1` | `TyDealerProfitability_Reserved1` |  |  |  |
| 10 | `TY.DEAL.RESERVED.2` | `TyDealerProfitability_Reserved2` |  |  |  |
| 11 | `TY.DEAL.RESERVED.3` | `TyDealerProfitability_Reserved3` |  |  |  |
| 12 | `TY.DEAL.RESERVED.4` | `TyDealerProfitability_Reserved4` |  |  |  |
| 13 | `TY.DEAL.RESERVED.5` | `TyDealerProfitability_Reserved5` |  |  |  |
| 14 | `TY.DEAL.RESERVED.6` | `TyDealerProfitability_Reserved6` |  |  |  |
| 15 | `TY.DEAL.RESERVED.7` | `TyDealerProfitability_Reserved7` |  |  |  |
| 16 | `TY.DEAL.RESERVED.8` | `TyDealerProfitability_Reserved8` |  |  |  |
| 17 | `TY.DEAL.RESERVED.9` | `TyDealerProfitability_Reserved9` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 18 | `TY.DEAL.DEALER.CONS.COND` | `TyDealerProfitability_DealerConsCond` | TField |  | Identifies the user defined field name defined in CONSOLIDATE.COND for the filename CATEG.ENTRY with fieldname as DEALER.DESK. Validation Rules: No-input field. Defaulted by the system with the NAME defined in CONSOLIDATE.COND of PROFIT and LOSS, where the FILE.NAME is CATEG.ENTRY and FIELD.NAME is DEALER.DESK. |
| 19 | `TY.DEAL.LOCAL.REF` | `TyDealerProfitability_LocalRef` |  |  |  |
| 20 | `TY.DEAL.OVERRIDE` | `TyDealerProfitability_Override` |  |  |  |
| 21 | `TY.DEAL.RECORD.STATUS` | `TyDealerProfitability_RecordStatus` | String |  |  |
| 22 | `TY.DEAL.CURR.NO` | `TyDealerProfitability_CurrNo` | String |  |  |
| 23 | `TY.DEAL.INPUTTER` | `TyDealerProfitability_Inputter` |  |  |  |
| 24 | `TY.DEAL.DATE.TIME` | `TyDealerProfitability_DateTime` |  |  |  |
| 25 | `TY.DEAL.AUTHORISER` | `TyDealerProfitability_Authoriser` | String |  |  |
| 26 | `TY.DEAL.CO.CODE` | `TyDealerProfitability_CoCode` | String |  |  |
| 27 | `TY.DEAL.DEPT.CODE` | `TyDealerProfitability_DeptCode` | String |  |  |
| 28 | `TY.DEAL.AUDITOR.CODE` | `TyDealerProfitability_AuditorCode` | String |  |  |
| 29 | `TY.DEAL.AUDIT.DATE.TIME` | `TyDealerProfitability_AuditDateTime` | String |  |  |
