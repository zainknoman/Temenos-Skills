# RR.SNAPSHOT.RULE — Table Schema

> Source: `INSERTS/I_F.RR.SNAPSHOT.RULE` in `RR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RR.SNAP.CHILD.REQUIRED` | `RrSnapshotRule_SnapChildRequired` |  |  |  |
| 2 | `RR.SNAP.NO.OF.DAYS` | `RrSnapshotRule_SnapNoOfDays` |  |  |  |
| 3 | `RR.SNAP.SNAPSHOT.TYPE` | `RrSnapshotRule_SnapSnapshotType` |  |  |  |
| 4 | `RR.SNAP.FREQUENCY` | `RrSnapshotRule_SnapFrequency` |  |  |  |
| 5 | `RR.SNAP.REQ.DATES` | `RrSnapshotRule_SnapReqDates` |  |  |  |
| 6 | `RR.SNAP.COMPANY.CODE` | `RrSnapshotRule_SnapCompanyCode` |  |  |  |
| 7 | `RR.SNAP.COMPANY.MNEMONIC` | `RrSnapshotRule_SnapCompanyMnemonic` |  |  |  |
| 8 | `RR.SNAP.APPLICATION` | `RrSnapshotRule_SnapApplication` |  |  |  |
| 9 | `RR.SNAP.ORCLFILENAME` | `RrSnapshotRule_SnapOrclfilename` |  |  |  |
| 10 | `RR.SNAP.RESERVED.8` | `RrSnapshotRule_Reserved8` | TField |  |  |
| 11 | `RR.SNAP.RESERVED.7` | `RrSnapshotRule_Reserved7` | TField |  |  |
| 12 | `RR.SNAP.RESERVED.6` | `RrSnapshotRule_Reserved6` | TField |  |  |
| 13 | `RR.SNAP.RESERVED.5` | `RrSnapshotRule_Reserved5` | TField |  |  |
| 14 | `RR.SNAP.RESERVED.4` | `RrSnapshotRule_Reserved4` | TField |  |  |
| 15 | `RR.SNAP.RESERVED.3` | `RrSnapshotRule_Reserved3` | TField |  |  |
| 16 | `RR.SNAP.RESERVED.2` | `RrSnapshotRule_Reserved2` | TField |  |  |
| 17 | `RR.SNAP.RESERVED.1` | `RrSnapshotRule_Reserved1` | TField |  |  |
| 18 | `RR.SNAP.OVERRIDE` | `RrSnapshotRule_Override` |  |  |  |
| 19 | `RR.SNAP.RECORD.STATUS` | `RrSnapshotRule_RecordStatus` | String |  |  |
| 20 | `RR.SNAP.CURR.NO` | `RrSnapshotRule_CurrNo` | String |  |  |
| 21 | `RR.SNAP.INPUTTER` | `RrSnapshotRule_Inputter` |  |  |  |
| 22 | `RR.SNAP.DATE.TIME` | `RrSnapshotRule_DateTime` |  |  |  |
| 23 | `RR.SNAP.AUTHORISER` | `RrSnapshotRule_Authoriser` | String |  |  |
| 24 | `RR.SNAP.CO.CODE` | `RrSnapshotRule_CoCode` | String |  |  |
| 25 | `RR.SNAP.DEPT.CODE` | `RrSnapshotRule_DeptCode` | String |  |  |
| 26 | `RR.SNAP.AUDITOR.CODE` | `RrSnapshotRule_AuditorCode` | String |  |  |
| 27 | `RR.SNAP.AUDIT.DATE.TIME` | `RrSnapshotRule_AuditDateTime` | String |  |  |
