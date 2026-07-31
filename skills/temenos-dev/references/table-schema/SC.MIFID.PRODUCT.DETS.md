# SC.MIFID.PRODUCT.DETS — Table Schema

> Source: `INSERTS/I_F.SC.MIFID.PRODUCT.DETS` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.MFDPRD.MGMT.FEE.RATE` | `ScMifidProductDets_MgmtFeeRate` | TField |  | This Field captures Management Fee Rate to be applied for Trailer Fee Calculation method Validation Rules: Value entered will be in terms of percentage |
| 2 | `SC.MFDPRD.CODE` | `ScMifidProductDets_Code` |  |  |  |
| 3 | `SC.MFDPRD.CATEGORY` | `ScMifidProductDets_Category` |  |  |  |
| 4 | `SC.MFDPRD.LABEL` | `ScMifidProductDets_Label` |  |  |  |
| 5 | `SC.MFDPRD.CURRENCY` | `ScMifidProductDets_Currency` |  |  |  |
| 6 | `SC.MFDPRD.AMOUNT` | `ScMifidProductDets_Amount` |  |  |  |
| 7 | `SC.MFDPRD.QUOTATION.CODE` | `ScMifidProductDets_QuotationCode` |  |  |  |
| 8 | `SC.MFDPRD.QUOTATION.LABEL` | `ScMifidProductDets_QuotationLabel` |  |  |  |
| 9 | `SC.MFDPRD.EX.ANTE.EX.POST` | `ScMifidProductDets_ExAnteExPost` |  |  |  |
| 10 | `SC.MFDPRD.CALCULATION.RULE` | `ScMifidProductDets_CalculationRule` |  |  |  |
| 11 | `SC.MFDPRD.BEGIN.DATE` | `ScMifidProductDets_BeginDate` |  |  |  |
| 12 | `SC.MFDPRD.MIN.RANGE` | `ScMifidProductDets_MinRange` |  |  |  |
| 13 | `SC.MFDPRD.MAX.RANGE` | `ScMifidProductDets_MaxRange` |  |  |  |
| 14 | `SC.MFDPRD.EXP.REQ` | `ScMifidProductDets_ExpReq` |  |  |  |
| 15 | `SC.MFDPRD.LOSS.TOLERANCE` | `ScMifidProductDets_LossTolerance` |  |  |  |
| 16 | `SC.MFDPRD.LIQUIDITY` | `ScMifidProductDets_Liquidity` |  |  |  |
| 17 | `SC.MFDPRD.OTHR.OBJECTIVES` | `ScMifidProductDets_OthrObjectives` |  |  |  |
| 18 | `SC.MFDPRD.DISTRIBUTION.STRTGY` | `ScMifidProductDets_DistributionStrtgy` |  |  |  |
| 19 | `SC.MFDPRD.RESERVED.20` | `ScMifidProductDets_Reserved20` |  |  |  |
| 20 | `SC.MFDPRD.RESERVED.19` | `ScMifidProductDets_Reserved19` |  |  |  |
| 21 | `SC.MFDPRD.RESERVED.18` | `ScMifidProductDets_Reserved18` |  |  |  |
| 22 | `SC.MFDPRD.RESERVED.17` | `ScMifidProductDets_Reserved17` |  |  |  |
| 23 | `SC.MFDPRD.RESERVED.16` | `ScMifidProductDets_Reserved16` |  |  |  |
| 24 | `SC.MFDPRD.RESERVED.15` | `ScMifidProductDets_Reserved15` |  |  |  |
| 25 | `SC.MFDPRD.RESERVED.14` | `ScMifidProductDets_Reserved14` |  |  |  |
| 26 | `SC.MFDPRD.RESERVED.13` | `ScMifidProductDets_Reserved13` | TField |  |  |
| 27 | `SC.MFDPRD.RESERVED.12` | `ScMifidProductDets_Reserved12` | TField |  |  |
| 28 | `SC.MFDPRD.RESERVED.11` | `ScMifidProductDets_Reserved11` | TField |  |  |
| 29 | `SC.MFDPRD.RESERVED.10` | `ScMifidProductDets_Reserved10` | TField |  |  |
| 30 | `SC.MFDPRD.RESERVED.09` | `ScMifidProductDets_Reserved09` | TField |  |  |
| 31 | `SC.MFDPRD.RESERVED.08` | `ScMifidProductDets_Reserved08` | TField |  |  |
| 32 | `SC.MFDPRD.RESERVED.07` | `ScMifidProductDets_Reserved07` | TField |  |  |
| 33 | `SC.MFDPRD.RESERVED.06` | `ScMifidProductDets_Reserved06` | TField |  |  |
| 34 | `SC.MFDPRD.RESERVED.05` | `ScMifidProductDets_Reserved05` | TField |  |  |
| 35 | `SC.MFDPRD.RESERVED.04` | `ScMifidProductDets_Reserved04` | TField |  |  |
| 36 | `SC.MFDPRD.RESERVED.03` | `ScMifidProductDets_Reserved03` | TField |  |  |
| 37 | `SC.MFDPRD.RESERVED.02` | `ScMifidProductDets_Reserved02` | TField |  |  |
| 38 | `SC.MFDPRD.RESERVED.01` | `ScMifidProductDets_Reserved01` | TField |  |  |
| 39 | `SC.MFDPRD.LOCAL.REF` | `ScMifidProductDets_LocalRef` |  |  |  |
| 40 | `SC.MFDPRD.OVERRIDE` | `ScMifidProductDets_Override` |  |  |  |
| 41 | `SC.MFDPRD.RECORD.STATUS` | `ScMifidProductDets_RecordStatus` | String |  |  |
| 42 | `SC.MFDPRD.CURR.NO` | `ScMifidProductDets_CurrNo` | String |  |  |
| 43 | `SC.MFDPRD.INPUTTER` | `ScMifidProductDets_Inputter` |  |  |  |
| 44 | `SC.MFDPRD.DATE.TIME` | `ScMifidProductDets_DateTime` |  |  |  |
| 45 | `SC.MFDPRD.AUTHORISER` | `ScMifidProductDets_Authoriser` | String |  |  |
| 46 | `SC.MFDPRD.CO.CODE` | `ScMifidProductDets_CoCode` | String |  |  |
| 47 | `SC.MFDPRD.DEPT.CODE` | `ScMifidProductDets_DeptCode` | String |  |  |
| 48 | `SC.MFDPRD.AUDITOR.CODE` | `ScMifidProductDets_AuditorCode` | String |  |  |
| 49 | `SC.MFDPRD.AUDIT.DATE.TIME` | `ScMifidProductDets_AuditDateTime` | String |  |  |
