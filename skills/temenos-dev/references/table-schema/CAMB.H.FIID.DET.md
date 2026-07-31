# CAMB.H.FIID.DET — Table Schema

> Source: `INSERTS/I_F.CAMB.H.FIID.DET` in `CAATMI_EverlinkATMInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CA.FIID.FIID.NO` | `CambHFiidDet_FiidNo` | TField |  |  |
| 2 | `CA.FIID.DPC.NUMBER` | `CambHFiidDet_DpcNumber` | TField |  |  |
| 3 | `CA.FIID.RESERVED.5` | `CambHFiidDet_Reserved5` | TField |  |  |
| 4 | `CA.FIID.RESERVED.4` | `CambHFiidDet_Reserved4` | TField |  |  |
| 5 | `CA.FIID.RESERVED.3` | `CambHFiidDet_Reserved3` | TField |  |  |
| 6 | `CA.FIID.RESERVED.2` | `CambHFiidDet_Reserved2` | TField |  |  |
| 7 | `CA.FIID.RESERVED.1` | `CambHFiidDet_Reserved1` | TField |  |  |
| 8 | `CA.FIID.LOCAL.REF` | `CambHFiidDet_LocalRef` |  |  |  |
| 9 | `CA.FIID.OVERRIDE` | `CambHFiidDet_Override` |  |  |  |
| 10 | `CA.FIID.RECORD.STATUS` | `CambHFiidDet_RecordStatus` | String |  |  |
| 11 | `CA.FIID.CURR.NO` | `CambHFiidDet_CurrNo` | String |  |  |
| 12 | `CA.FIID.INPUTTER` | `CambHFiidDet_Inputter` |  |  |  |
| 13 | `CA.FIID.DATE.TIME` | `CambHFiidDet_DateTime` |  |  |  |
| 14 | `CA.FIID.AUTHORISER` | `CambHFiidDet_Authoriser` | String |  |  |
| 15 | `CA.FIID.CO.CODE` | `CambHFiidDet_CoCode` | String |  |  |
| 16 | `CA.FIID.DEPT.CODE` | `CambHFiidDet_DeptCode` | String |  |  |
| 17 | `CA.FIID.AUDITOR.CODE` | `CambHFiidDet_AuditorCode` | String |  |  |
| 18 | `CA.FIID.AUDIT.DATE.TIME` | `CambHFiidDet_AuditDateTime` | String |  |  |
