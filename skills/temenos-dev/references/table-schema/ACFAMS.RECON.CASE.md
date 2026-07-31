# ACFAMS.RECON.CASE — Table Schema

> Source: `INSERTS/I_F.ACFAMS.RECON.CASE` in `ACFAMS_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACFAMS.RECON.DESCRIPTION` | `AcfamsReconciliationCase_Description` |  |  |  |
| 2 | `ACFAMS.RECON.LEFT.SIDE.DATA.SOURCE` | `AcfamsReconciliationCase_LeftSideDataSource` |  |  |  |
| 3 | `ACFAMS.RECON.RIGHT.SIDE.DATA.SOURCE` | `AcfamsReconciliationCase_RightSideDataSource` |  |  |  |
| 4 | `ACFAMS.RECON.LEFT.SIDE.RETR.METHOD` | `AcfamsReconciliationCase_LeftSideRetrMethod` |  |  |  |
| 5 | `ACFAMS.RECON.RIGHT.SIDE.RETR.METHOD` | `AcfamsReconciliationCase_RightSideRetrMethod` |  |  |  |
| 6 | `ACFAMS.RECON.FULL.SELECTOR.METHOD` | `AcfamsReconciliationCase_FullSelectorMethod` |  |  |  |
| 7 | `ACFAMS.RECON.FULL.FILTER.METHOD` | `AcfamsReconciliationCase_FullFilterMethod` |  |  |  |
| 8 | `ACFAMS.RECON.DELTA.SELECTOR.METHOD` | `AcfamsReconciliationCase_DeltaSelectorMethod` |  |  |  |
| 9 | `ACFAMS.RECON.DELTA.FILTER.METHOD` | `AcfamsReconciliationCase_DeltaFilterMethod` |  |  |  |
| 10 | `ACFAMS.RECON.LAST.RECON.DATE.TIME` | `AcfamsReconciliationCase_LastReconDateTime` |  |  |  |
| 11 | `ACFAMS.RECON.RUN.SEQ.NUMBER` | `AcfamsReconciliationCase_RunSeqNumber` |  |  |  |
| 12 | `ACFAMS.RECON.RECON.MODE` | `AcfamsReconciliationCase_ReconMode` |  |  |  |
| 13 | `ACFAMS.RECON.PROCESS.CONTROL` | `AcfamsReconciliationCase_ProcessControl` |  |  |  |
| 14 | `ACFAMS.RECON.RECON.RECORD.MODE` | `AcfamsReconciliationCase_ReconRecordMode` |  |  |  |
| 15 | `ACFAMS.RECON.RETRY.ATTEMPTS` | `AcfamsReconciliationCase_RetryAttempts` |  |  |  |
| 16 | `ACFAMS.RECON.PURGE.PERIOD` | `AcfamsReconciliationCase_PurgePeriod` |  |  |  |
| 17 | `ACFAMS.RECON.IP.ADDRESS` | `AcfamsReconciliationCase_IpAddress` |  |  |  |
| 18 | `ACFAMS.RECON.PORT.NUMBER` | `AcfamsReconciliationCase_PortNumber` |  |  |  |
| 19 | `ACFAMS.RECON.MAX.NO.ID` | `AcfamsReconciliationCase_MaxNoId` |  |  |  |
| 20 | `ACFAMS.RECON.MAX.LIST.NO` | `AcfamsReconciliationCase_MaxListNo` |  |  |  |
| 21 | `ACFAMS.RECON.LAST.DELTA.RECON.DATE.TIME` | `AcfamsReconciliationCase_LastDeltaReconDateTime` |  |  |  |
| 22 | `ACFAMS.RECON.DATA.REFRESH.METHOD` | `AcfamsReconciliationCase_DataRefreshMethod` |  |  |  |
| 23 | `ACFAMS.RECON.PROTOCOL` | `AcfamsReconciliationCase_Protocol` |  |  |  |
| 24 | `ACFAMS.RECON.JWT.TOKEN.GENERATOR` | `AcfamsReconciliationCase_JwtTokenGenerator` |  |  |  |
| 25 | `ACFAMS.RECON.RECONCILE.URL` | `AcfamsReconciliationCase_ReconcileUrl` |  |  |  |
| 26 | `ACFAMS.RECON.DES.URL` | `AcfamsReconCase_DesUrl` | TField |  | Contains the URL path for DES Api , which will be called from Delta Selection. Example: http://localhost:13161/des/v1/events/entitydetails |
| 27 | `ACFAMS.RECON.LOCAL.REF` | `AcfamsReconciliationCase_LocalRef` |  |  |  |
| 28 | `ACFAMS.RECON.OVERRIDE` | `AcfamsReconciliationCase_Override` |  |  |  |
| 29 | `ACFAMS.RECON.RECORD.STATUS` | `AcfamsReconciliationCase_RecordStatus` |  |  |  |
| 30 | `ACFAMS.RECON.CURR.NO` | `AcfamsReconciliationCase_CurrNo` |  |  |  |
| 31 | `ACFAMS.RECON.INPUTTER` | `AcfamsReconciliationCase_Inputter` |  |  |  |
| 32 | `ACFAMS.RECON.DATE.TIME` | `AcfamsReconciliationCase_DateTime` |  |  |  |
| 33 | `ACFAMS.RECON.AUTHORISER` | `AcfamsReconciliationCase_Authoriser` |  |  |  |
| 34 | `ACFAMS.RECON.CO.CODE` | `AcfamsReconciliationCase_CoCode` |  |  |  |
| 35 | `ACFAMS.RECON.DEPT.CODE` | `AcfamsReconciliationCase_DeptCode` |  |  |  |
| 36 | `ACFAMS.RECON.AUDITOR.CODE` | `AcfamsReconciliationCase_AuditorCode` |  |  |  |
| 37 | `ACFAMS.RECON.AUDIT.DATE.TIME` | `AcfamsReconciliationCase_AuditDateTime` |  |  |  |
| 38 | `ACFAMS.RECON.DES.JWT.TOKEN.GENERATOR` | `AcfamsReconCase_DesJwtTokenGenerator` | TField |  |  |
| 39 | `ACFAMS.RECON.DES.PAGE.SIZE` | `AcfamsReconCase_DesPageSize` | TField |  | Defines the Number or size of Records that needs to be fetched while invoking DES.URL each time. User can define, or else by default Page size will be assumed as 1000 |
| 40 | `ACFAMS.RECON.PRODUCT.LINES` | `AcfamsReconCase_ProductLines` |  |  |  |
