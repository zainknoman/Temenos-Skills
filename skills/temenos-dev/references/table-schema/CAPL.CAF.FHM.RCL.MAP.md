# CAPL.CAF.FHM.RCL.MAP — Table Schema

> Source: `INSERTS/I_F.CAPL.CAF.FHM.RCL.MAP` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CRD.RCL.MAP.RCL.MAPPING` | `CaplCafFhmRclMap_RclMapping` | TField |  |  |
| 2 | `CRD.RCL.MAP.MIGRATION.DONE` | `CaplCafFhmRclMap_MigrationDone` | TField |  |  |
| 3 | `CRD.RCL.MAP.FLD.PERSIST` | `CaplCafFhmRclMap_FldPersist` | TField |  |  |
| 4 | `CRD.RCL.MAP.CARD.SIGNER` | `CaplCafFhmRclMap_CardSigner` | TField |  |  |
| 5 | `CRD.RCL.MAP.RESERVED.8` | `CaplCafFhmRclMap_Reserved8` | TField |  |  |
| 6 | `CRD.RCL.MAP.RESERVED.7` | `CaplCafFhmRclMap_Reserved7` | TField |  |  |
| 7 | `CRD.RCL.MAP.RESERVED.6` | `CaplCafFhmRclMap_Reserved6` | TField |  |  |
| 8 | `CRD.RCL.MAP.RESERVED.5` | `CaplCafFhmRclMap_Reserved5` | TField |  |  |
| 9 | `CRD.RCL.MAP.RESERVED.4` | `CaplCafFhmRclMap_Reserved4` | TField |  |  |
| 10 | `CRD.RCL.MAP.RESERVED.3` | `CaplCafFhmRclMap_Reserved3` | TField |  |  |
| 11 | `CRD.RCL.MAP.RESERVED.2` | `CaplCafFhmRclMap_Reserved2` | TField |  |  |
| 12 | `CRD.RCL.MAP.RESERVED.1` | `CaplCafFhmRclMap_Reserved1` | TField |  |  |
| 13 | `CRD.RCL.MAP.LOCAL.REF` | `CaplCafFhmRclMap_LocalRef` |  |  |  |
| 14 | `CRD.RCL.MAP.OVERRIDE` | `CaplCafFhmRclMap_Override` |  |  |  |
| 15 | `CRD.RCL.MAP.RECORD.STATUS` | `CaplCafFhmRclMap_RecordStatus` | String |  |  |
| 16 | `CRD.RCL.MAP.CURR.NO` | `CaplCafFhmRclMap_CurrNo` | String |  |  |
| 17 | `CRD.RCL.MAP.INPUTTER` | `CaplCafFhmRclMap_Inputter` |  |  |  |
| 18 | `CRD.RCL.MAP.DATE.TIME` | `CaplCafFhmRclMap_DateTime` |  |  |  |
| 19 | `CRD.RCL.MAP.AUTHORISER` | `CaplCafFhmRclMap_Authoriser` | String |  |  |
| 20 | `CRD.RCL.MAP.CO.CODE` | `CaplCafFhmRclMap_CoCode` | String |  |  |
| 21 | `CRD.RCL.MAP.DEPT.CODE` | `CaplCafFhmRclMap_DeptCode` | String |  |  |
| 22 | `CRD.RCL.MAP.AUDITOR.CODE` | `CaplCafFhmRclMap_AuditorCode` | String |  |  |
| 23 | `CRD.RCL.MAP.AUDIT.DATE.TIME` | `CaplCafFhmRclMap_AuditDateTime` | String |  |  |
