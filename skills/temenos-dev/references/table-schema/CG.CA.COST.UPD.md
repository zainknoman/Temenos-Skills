# CG.CA.COST.UPD — Table Schema

> Source: `INSERTS/I_F.CG.CA.COST.UPD` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CA.COST.COST.BASE.ADJ` | `CgCaCostUpd_CostBaseAdj` |  |  |  |
| 2 | `CA.COST.RED.COST.BASE.ADJ` | `CgCaCostUpd_RedCostBaseAdj` |  |  |  |
| 3 | `CA.COST.COST.POS.ADJ` | `CgCaCostUpd_CostPosAdj` |  |  |  |
| 4 | `CA.COST.STATUS` | `CgCaCostUpd_Status` | TField |  | Informatory field to identify the type of update to this record. Allowed Options : INITIAL , FINAL |
| 5 | `CA.COST.SERVICE.STATUS` | `CgCaCostUpd_ServiceStatus` | TField |  | Field is to identify processing of this record by service : CG.COST.ADJUSTMENT . Update to this field is as below : ACTIVATED - Record is ready to be picked by service : CG.COST.ADJUSTMENT PROCESSING - Record is picked by service : CG.COST.ADJUSTMENT and is being processed. PROCESSED - Record is processed by service : CG.COST.ADJUSTMENT Validation Rules : NOINPUT Field |
| 6 | `CA.COST.RESERVED.09` | `CgCaCostUpd_Reserved09` |  |  |  |
| 7 | `CA.COST.RESERVED.08` | `CgCaCostUpd_Reserved08` | TField |  |  |
| 8 | `CA.COST.RESERVED.07` | `CgCaCostUpd_Reserved07` | TField |  |  |
| 9 | `CA.COST.RESERVED.06` | `CgCaCostUpd_Reserved06` | TField |  |  |
| 10 | `CA.COST.RESERVED.05` | `CgCaCostUpd_Reserved05` | TField |  |  |
| 11 | `CA.COST.RESERVED.04` | `CgCaCostUpd_Reserved04` | TField |  |  |
| 12 | `CA.COST.RESERVED.03` | `CgCaCostUpd_Reserved03` | TField |  |  |
| 13 | `CA.COST.RESERVED.02` | `CgCaCostUpd_Reserved02` | TField |  |  |
| 14 | `CA.COST.RESERVED.01` | `CgCaCostUpd_Reserved01` | TField |  |  |
| 15 | `CA.COST.LOCAL.REF` | `CgCaCostUpd_LocalRef` |  |  |  |
| 16 | `CA.COST.OVERRIDE` | `CgCaCostUpd_Override` |  |  |  |
| 17 | `CA.COST.RECORD.STATUS` | `CgCaCostUpd_RecordStatus` | String |  |  |
| 18 | `CA.COST.CURR.NO` | `CgCaCostUpd_CurrNo` | String |  |  |
| 19 | `CA.COST.INPUTTER` | `CgCaCostUpd_Inputter` |  |  |  |
| 20 | `CA.COST.DATE.TIME` | `CgCaCostUpd_DateTime` |  |  |  |
| 21 | `CA.COST.AUTHORISER` | `CgCaCostUpd_Authoriser` | String |  |  |
| 22 | `CA.COST.CO.CODE` | `CgCaCostUpd_CoCode` | String |  |  |
| 23 | `CA.COST.DEPT.CODE` | `CgCaCostUpd_DeptCode` | String |  |  |
| 24 | `CA.COST.AUDITOR.CODE` | `CgCaCostUpd_AuditorCode` | String |  |  |
| 25 | `CA.COST.AUDIT.DATE.TIME` | `CgCaCostUpd_AuditDateTime` | String |  |  |
| 26 | `CA.COST.STAPLED.SECURITY` | `CgCaCostUpd_StapledSecurity` |  |  |  |
| 27 | `CA.COST.DEFERRED.RATE` | `CgCaCostUpd_DeferredRate` |  |  |  |
