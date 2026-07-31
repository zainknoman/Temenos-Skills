# CLUSTER.ARC.GENERIC.REQUEST — Table Schema

> Source: `INSERTS/I_F.CLUSTER.ARC.GENERIC.REQUEST` in `PP_ArchivingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CLUSTER.ArchiveID` | `ClusterArcGenericRequest_Archiveid` |  |  |  |
| 2 | `CLUSTER.RECORD.STATUS` | `ClusterArcGenericRequest_RecordStatus` |  |  |  |
| 3 | `CLUSTER.CURR.NO` | `ClusterArcGenericRequest_CurrNo` |  |  |  |
| 4 | `CLUSTER.INPUTTER` | `ClusterArcGenericRequest_Inputter` |  |  |  |
| 5 | `CLUSTER.DATE.TIME` | `ClusterArcGenericRequest_DateTime` |  |  |  |
| 6 | `CLUSTER.AUTHORISER` | `ClusterArcGenericRequest_Authoriser` |  |  |  |
| 7 | `CLUSTER.CO.CODE` | `ClusterArcGenericRequest_CoCode` |  |  |  |
| 8 | `CLUSTER.DEPT.CODE` | `ClusterArcGenericRequest_DeptCode` |  |  |  |
| 9 | `CLUSTER.AUDITOR.CODE` | `ClusterArcGenericRequest_AuditorCode` |  |  |  |
| 10 | `CLUSTER.AUDIT.DATE.TIME` | `ClusterArcGenericRequest_AuditDateTime` |  |  |  |
