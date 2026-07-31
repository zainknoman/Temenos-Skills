# CAPL.H.GEN.TFSA.SLIP — Table Schema

> Source: `INSERTS/I_F.CAPL.H.GEN.TFSA.SLIP` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.TFSA.GEN.SLIP.YEAR` | `CaplHGenTfsaSlip_SlipYear` | TField |  | This field is to indicate the slip year for the TFSA account.Valid year to be defined here. |
| 2 | `CAPL.TFSA.GEN.SEL.CRITERIA` | `CaplHGenTfsaSlip_SelCriteria` |  |  |  |
| 3 | `CAPL.TFSA.GEN.ACTION` | `CaplHGenTfsaSlip_Action` | TField |  | This field is to defien the action type for the tax slip generation.Allowed values are:GENERATEXML-ORIGINALXML-AMENDXML-CANCELXML-P.ORIGINALXML-P.AMENDXML-P.CANCEL |
| 4 | `CAPL.TFSA.GEN.RUN.MODE` | `CaplHGenTfsaSlip_RunMode` | TField |  | The purpose of this field is to denote the run mode, whether the slip to be generated thoruhg online or service.Allowed values are Online/Service |
| 5 | `CAPL.TFSA.GEN.RESERVED.10` | `CaplHGenTfsaSlip_Reserved10` |  |  |  |
| 6 | `CAPL.TFSA.GEN.RESERVED.9` | `CaplHGenTfsaSlip_Reserved9` |  |  |  |
| 7 | `CAPL.TFSA.GEN.RESERVED.8` | `CaplHGenTfsaSlip_Reserved8` | TField |  |  |
| 8 | `CAPL.TFSA.GEN.RESERVED.7` | `CaplHGenTfsaSlip_Reserved7` | TField |  |  |
| 9 | `CAPL.TFSA.GEN.RESERVED.6` | `CaplHGenTfsaSlip_Reserved6` | TField |  |  |
| 10 | `CAPL.TFSA.GEN.RESERVED.5` | `CaplHGenTfsaSlip_Reserved5` | TField |  |  |
| 11 | `CAPL.TFSA.GEN.RESERVED.4` | `CaplHGenTfsaSlip_Reserved4` | TField |  |  |
| 12 | `CAPL.TFSA.GEN.RESERVED.3` | `CaplHGenTfsaSlip_Reserved3` | TField |  |  |
| 13 | `CAPL.TFSA.GEN.RESERVED.2` | `CaplHGenTfsaSlip_Reserved2` | TField |  |  |
| 14 | `CAPL.TFSA.GEN.RESERVED.1` | `CaplHGenTfsaSlip_Reserved1` | TField |  |  |
| 15 | `CAPL.TFSA.GEN.LOCAL.REF` | `CaplHGenTfsaSlip_LocalRef` |  |  |  |
| 16 | `CAPL.TFSA.GEN.OVERRIDE` | `CaplHGenTfsaSlip_Override` |  |  |  |
| 17 | `CAPL.TFSA.GEN.RECORD.STATUS` | `CaplHGenTfsaSlip_RecordStatus` | String |  |  |
| 18 | `CAPL.TFSA.GEN.CURR.NO` | `CaplHGenTfsaSlip_CurrNo` | String |  |  |
| 19 | `CAPL.TFSA.GEN.INPUTTER` | `CaplHGenTfsaSlip_Inputter` |  |  |  |
| 20 | `CAPL.TFSA.GEN.DATE.TIME` | `CaplHGenTfsaSlip_DateTime` |  |  |  |
| 21 | `CAPL.TFSA.GEN.AUTHORISER` | `CaplHGenTfsaSlip_Authoriser` | String |  |  |
| 22 | `CAPL.TFSA.GEN.CO.CODE` | `CaplHGenTfsaSlip_CoCode` | String |  |  |
| 23 | `CAPL.TFSA.GEN.DEPT.CODE` | `CaplHGenTfsaSlip_DeptCode` | String |  |  |
| 24 | `CAPL.TFSA.GEN.AUDITOR.CODE` | `CaplHGenTfsaSlip_AuditorCode` | String |  |  |
| 25 | `CAPL.TFSA.GEN.AUDIT.DATE.TIME` | `CaplHGenTfsaSlip_AuditDateTime` | String |  |  |
