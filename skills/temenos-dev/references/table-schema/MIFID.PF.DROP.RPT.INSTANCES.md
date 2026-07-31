# MIFID.PF.DROP.RPT.INSTANCES — Table Schema

> Source: `INSERTS/I_F.MIFID.PF.DROP.RPT.INSTANCES` in `MIFDII_IRP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MIFID.PF.DROP.CURRENCY` | `MifidPfDropRptInstances_Currency` | TField |  | It hold currency code which get defaulted based on SEC.ACC.MASTER or AM.GROUP.PORT. Validation Rule: This is a NOINPUT field. |
| 2 | `MIFID.PF.DROP.DROP.DATE` | `MifidPfDropRptInstances_DropDate` |  |  |  |
| 3 | `MIFID.PF.DROP.DROP.PCT.RECORDED` | `MifidPfDropRptInstances_DropPctRecorded` |  |  |  |
| 4 | `MIFID.PF.DROP.PF.GRP.VALUE` | `MifidPfDropRptInstances_PfGrpValue` |  |  |  |
| 5 | `MIFID.PF.DROP.REJECT` | `MifidPfDropRptInstances_Reject` |  |  |  |
| 6 | `MIFID.PF.DROP.LOCAL.REF` | `MifidPfDropRptInstances_LocalRef` |  |  |  |
| 7 | `MIFID.PF.DROP.RESERVED.10` | `MifidPfDropRptInstances_Reserved10` | TField |  |  |
| 8 | `MIFID.PF.DROP.RESERVED.9` | `MifidPfDropRptInstances_Reserved9` | TField |  |  |
| 9 | `MIFID.PF.DROP.RESERVED.8` | `MifidPfDropRptInstances_Reserved8` | TField |  |  |
| 10 | `MIFID.PF.DROP.RESERVED.7` | `MifidPfDropRptInstances_Reserved7` | TField |  |  |
| 11 | `MIFID.PF.DROP.RESERVED.6` | `MifidPfDropRptInstances_Reserved6` | TField |  |  |
| 12 | `MIFID.PF.DROP.RESERVED.5` | `MifidPfDropRptInstances_Reserved5` | TField |  |  |
| 13 | `MIFID.PF.DROP.RESERVED.4` | `MifidPfDropRptInstances_Reserved4` | TField |  |  |
| 14 | `MIFID.PF.DROP.RESERVED.3` | `MifidPfDropRptInstances_Reserved3` | TField |  |  |
| 15 | `MIFID.PF.DROP.RESERVED.2` | `MifidPfDropRptInstances_Reserved2` | TField |  |  |
| 16 | `MIFID.PF.DROP.RESERVED.1` | `MifidPfDropRptInstances_Reserved1` | TField |  |  |
| 17 | `MIFID.PF.DROP.OVERRIDE` | `MifidPfDropRptInstances_Override` |  |  |  |
| 18 | `MIFID.PF.DROP.RECORD.STATUS` | `MifidPfDropRptInstances_RecordStatus` | String |  |  |
| 19 | `MIFID.PF.DROP.CURR.NO` | `MifidPfDropRptInstances_CurrNo` | String |  |  |
| 20 | `MIFID.PF.DROP.INPUTTER` | `MifidPfDropRptInstances_Inputter` |  |  |  |
| 21 | `MIFID.PF.DROP.DATE.TIME` | `MifidPfDropRptInstances_DateTime` |  |  |  |
| 22 | `MIFID.PF.DROP.AUTHORISER` | `MifidPfDropRptInstances_Authoriser` | String |  |  |
| 23 | `MIFID.PF.DROP.CO.CODE` | `MifidPfDropRptInstances_CoCode` | String |  |  |
| 24 | `MIFID.PF.DROP.DEPT.CODE` | `MifidPfDropRptInstances_DeptCode` | String |  |  |
| 25 | `MIFID.PF.DROP.AUDITOR.CODE` | `MifidPfDropRptInstances_AuditorCode` | String |  |  |
| 26 | `MIFID.PF.DROP.AUDIT.DATE.TIME` | `MifidPfDropRptInstances_AuditDateTime` | String |  |  |
