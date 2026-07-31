# PP.AUTO.REPAIR.RETURNCODE — Table Schema

> Source: `INSERTS/I_F.PP.AUTO.REPAIR.RETURNCODE` in `PP_AutomatedRepairToolService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.ARC.ReturnCodeDescription` | `PpAutoRepairReturncode_Returncodedescription` | TField | Yes | Describes the return code. Validation Rules: Mandatory field. 128 alphanumeric characters. |
| 2 | `PP.ARC.SetBeneficiaryBICRepairedFlag` | `PpAutoRepairReturncode_Setbeneficiarybicrepairedflag` | TField |  | As part of the Auto repair functionality which enriches payment information, banks can opt for events/ errors that can be chargeable. This provision is available by this field. Possible values: "Y" - Yes. Return code will be considered for processing in the payments hub. "N" - No. Return code will not considered for processing in the payments hub. |
| 3 | `PP.ARC.LOCAL.REF` | `PpAutoRepairReturncode_LocalRef` |  |  |  |
| 4 | `PP.ARC.RESERVED.5` | `PpAutoRepairReturncode_Reserved5` | TField |  |  |
| 5 | `PP.ARC.RESERVED.4` | `PpAutoRepairReturncode_Reserved4` | TField |  |  |
| 6 | `PP.ARC.RESERVED.3` | `PpAutoRepairReturncode_Reserved3` | TField |  |  |
| 7 | `PP.ARC.RESERVED.2` | `PpAutoRepairReturncode_Reserved2` | TField |  |  |
| 8 | `PP.ARC.RESERVED.1` | `PpAutoRepairReturncode_Reserved1` | TField |  |  |
| 9 | `PP.ARC.OVERRIDE` | `PpAutoRepairReturncode_Override` |  |  |  |
| 10 | `PP.ARC.RECORD.STATUS` | `PpAutoRepairReturncode_RecordStatus` | String |  |  |
| 11 | `PP.ARC.CURR.NO` | `PpAutoRepairReturncode_CurrNo` | String |  |  |
| 12 | `PP.ARC.INPUTTER` | `PpAutoRepairReturncode_Inputter` |  |  |  |
| 13 | `PP.ARC.DATE.TIME` | `PpAutoRepairReturncode_DateTime` |  |  |  |
| 14 | `PP.ARC.AUTHORISER` | `PpAutoRepairReturncode_Authoriser` | String |  |  |
| 15 | `PP.ARC.CO.CODE` | `PpAutoRepairReturncode_CoCode` | String |  |  |
| 16 | `PP.ARC.DEPT.CODE` | `PpAutoRepairReturncode_DeptCode` | String |  |  |
| 17 | `PP.ARC.AUDITOR.CODE` | `PpAutoRepairReturncode_AuditorCode` | String |  |  |
| 18 | `PP.ARC.AUDIT.DATE.TIME` | `PpAutoRepairReturncode_AuditDateTime` | String |  |  |
