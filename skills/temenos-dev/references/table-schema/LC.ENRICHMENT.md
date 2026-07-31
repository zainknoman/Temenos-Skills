# LC.ENRICHMENT — Table Schema

> Source: `INSERTS/I_F.LC.ENRICHMENT` in `LC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TF.ME.OPERATION` | `LcEnrichment_Operation` |  |  |  |
| 2 | `TF.ME.REVOCABLE` | `LcEnrichment_Revocable` |  |  |  |
| 3 | `TF.ME.UCP.IND` | `LcEnrichment_UcpInd` |  |  |  |
| 4 | `TF.ME.PART.SHIP` | `LcEnrichment_PartShip` |  |  |  |
| 5 | `TF.ME.TRANSSHIP` | `LcEnrichment_Transship` |  |  |  |
| 6 | `TF.ME.REIMBURSE` | `LcEnrichment_Reimburse` |  |  |  |
| 7 | `TF.ME.CHARGES.FROM` | `LcEnrichment_ChargesFrom` |  |  |  |
| 8 | `TF.ME.PARTY.CHRGD` | `LcEnrichment_PartyChrgd` |  |  |  |
| 9 | `TF.ME.CHRG.STATUS` | `LcEnrichment_ChrgStatus` |  |  |  |
| 10 | `TF.ME.DRAWING.TYPE` | `LcEnrichment_DrawingType` |  |  |  |
| 11 | `TF.ME.PAY.METHOD` | `LcEnrichment_PayMethod` |  |  |  |
| 12 | `TF.ME.COLL.REPLY` | `LcEnrichment_CollReply` |  |  |  |
| 13 | `TF.ME.CHRG.PERIOD` | `LcEnrichment_ChrgPeriod` |  |  |  |
| 14 | `TF.ME.IMP.EXP` | `LcEnrichment_ImpExp` |  |  |  |
| 15 | `TF.ME.PAY.TYPE` | `LcEnrichment_PayType` |  |  |  |
| 16 | `TF.ME.INCO.TERMS` | `LcEnrichment_IncoTerms` |  |  |  |
| 17 | `TF.ME.RECORD.STATUS` | `LcEnrichment_RecordStatus` | String |  |  |
| 18 | `TF.ME.CURR.NO` | `LcEnrichment_CurrNo` | String |  |  |
| 19 | `TF.ME.INPUTTER` | `LcEnrichment_Inputter` |  |  |  |
| 20 | `TF.ME.DATE.TIME` | `LcEnrichment_DateTime` |  |  |  |
| 21 | `TF.ME.AUTHORISER` | `LcEnrichment_Authoriser` | String |  |  |
| 22 | `TF.ME.CO.CODE` | `LcEnrichment_CoCode` | String |  |  |
| 23 | `TF.ME.DEPT.CODE` | `LcEnrichment_DeptCode` | String |  |  |
| 24 | `TF.ME.AUDITOR.CODE` | `LcEnrichment_AuditorCode` | String |  |  |
| 25 | `TF.ME.AUDIT.DATE.TIME` | `LcEnrichment_AuditDateTime` | String |  |  |
