# SC.INCOME.RECLASSIFICATION — Table Schema

> Source: `INSERTS/I_F.SC.INCOME.RECLASSIFICATION` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.INC.RCL.SECURITY.CODE` | `ScIncomeReclassification_SecurityCode` | TField |  | This field will be used in selecting the applicable DIARY events. Validation Rules: Must be a valid SECURITY.MASTER record |
| 2 | `SC.INC.RCL.EVENT.TYPE` | `ScIncomeReclassification_EventType` | TField |  | This field will be used in selecting the applicable DIARY events. Validation Rules: Must be a valid DIARY.TYPE record |
| 3 | `SC.INC.RCL.DATE.TYPE` | `ScIncomeReclassification_DateType` | TField |  | All Diary ids with date (i.e, EX.DATE / PAY.DATE / VALUE.DATE) greater than the START.DATE and less than theEND.DATE would be fetched for reclassification processing Validation Rules: Allowed Values : EX.DATE , PAY.DATE , VALUE.DATE |
| 4 | `SC.INC.RCL.START.DATE` | `ScIncomeReclassification_StartDate` | TField |  | START.DATE and END.DATE are used together in the selection process. All DIARYs with EX.DATE/PAY.DATE/VALUE.DATE(as defined in the DATE.TYPE field) will be selected for reclassification processing. |
| 5 | `SC.INC.RCL.END.DATE` | `ScIncomeReclassification_EndDate` | TField |  | START.DATE and END.DATE are used together in the selection process. All DIARYs with EX.DATE/PAY.DATE/VALUE.DATE(as defined in the DATE.TYPE field) will be selected for reclassification processing. Validation Rules: Must be greater than start date |
| 6 | `SC.INC.RCL.DIARY.ID` | `ScIncomeReclassification_DiaryId` |  |  |  |
| 7 | `SC.INC.RCL.INCOME.CODE` | `ScIncomeReclassification_IncomeCode` |  |  |  |
| 8 | `SC.INC.RCL.INCOME.RATE` | `ScIncomeReclassification_IncomeRate` |  |  |  |
| 9 | `SC.INC.RCL.INCOME.PERC` | `ScIncomeReclassification_IncomePerc` |  |  |  |
| 10 | `SC.INC.RCL.TAXABLE` | `ScIncomeReclassification_Taxable` |  |  |  |
| 11 | `SC.INC.RCL.REPORTABLE` | `ScIncomeReclassification_Reportable` |  |  |  |
| 12 | `SC.INC.RCL.CONSOLIDATE.ENTRY` | `ScIncomeReclassification_ConsolidateEntry` | TField |  | This field indicates whether the entry has to be consolidated or not Validation Rules: Accepts : Yes, No When set to No, Individual entry per Entitlement will be created by creating a separate SC.ADJ.TXN.UPDATE recordfor each entitlement.. When set to Yes, the entry will be consolidated (the tax difference of all events will be consolidated) percustomer, by creating a single SC.ADJ.TXN.UPDATE record for all the entitlements of the customer. |
| 13 | `SC.INC.RCL.RESERVED.01` | `ScIncomeReclassification_Reserved01` | TField |  |  |
| 14 | `SC.INC.RCL.RESERVED.02` | `ScIncomeReclassification_Reserved02` | TField |  |  |
| 15 | `SC.INC.RCL.RESERVED.03` | `ScIncomeReclassification_Reserved03` | TField |  |  |
| 16 | `SC.INC.RCL.RESERVED.04` | `ScIncomeReclassification_Reserved04` | TField |  |  |
| 17 | `SC.INC.RCL.RESERVED.05` | `ScIncomeReclassification_Reserved05` | TField |  |  |
| 18 | `SC.INC.RCL.RESERVED.06` | `ScIncomeReclassification_Reserved06` | TField |  |  |
| 19 | `SC.INC.RCL.RESERVED.07` | `ScIncomeReclassification_Reserved07` | TField |  |  |
| 20 | `SC.INC.RCL.RESERVED.08` | `ScIncomeReclassification_Reserved08` | TField |  |  |
| 21 | `SC.INC.RCL.RESERVED.09` | `ScIncomeReclassification_Reserved09` | TField |  |  |
| 22 | `SC.INC.RCL.RESERVED.10` | `ScIncomeReclassification_Reserved10` | TField |  |  |
| 23 | `SC.INC.RCL.RESERVED.11` | `ScIncomeReclassification_Reserved11` | TField |  |  |
| 24 | `SC.INC.RCL.RESERVED.12` | `ScIncomeReclassification_Reserved12` | TField |  |  |
| 25 | `SC.INC.RCL.RESERVED.13` | `ScIncomeReclassification_Reserved13` | TField |  |  |
| 26 | `SC.INC.RCL.RESERVED.14` | `ScIncomeReclassification_Reserved14` | TField |  |  |
| 27 | `SC.INC.RCL.RESERVED.15` | `ScIncomeReclassification_Reserved15` | TField |  |  |
| 28 | `SC.INC.RCL.LOCAL.REF` | `ScIncomeReclassification_LocalRef` |  |  |  |
| 29 | `SC.INC.RCL.OVERRIDE` | `ScIncomeReclassification_Override` |  |  |  |
| 30 | `SC.INC.RCL.RECORD.STATUS` | `ScIncomeReclassification_RecordStatus` | String |  |  |
| 31 | `SC.INC.RCL.CURR.NO` | `ScIncomeReclassification_CurrNo` | String |  |  |
| 32 | `SC.INC.RCL.INPUTTER` | `ScIncomeReclassification_Inputter` |  |  |  |
| 33 | `SC.INC.RCL.DATE.TIME` | `ScIncomeReclassification_DateTime` |  |  |  |
| 34 | `SC.INC.RCL.AUTHORISER` | `ScIncomeReclassification_Authoriser` | String |  |  |
| 35 | `SC.INC.RCL.CO.CODE` | `ScIncomeReclassification_CoCode` | String |  |  |
| 36 | `SC.INC.RCL.DEPT.CODE` | `ScIncomeReclassification_DeptCode` | String |  |  |
| 37 | `SC.INC.RCL.AUDITOR.CODE` | `ScIncomeReclassification_AuditorCode` | String |  |  |
| 38 | `SC.INC.RCL.AUDIT.DATE.TIME` | `ScIncomeReclassification_AuditDateTime` | String |  |  |
| 39 | `SC.INC.RCL.TAX.EFF.DATE` | `ScIncomeReclassification_TaxEffDate` |  |  |  |
