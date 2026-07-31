# PM.PC.PARAM — Table Schema

> Source: `INSERTS/I_F.PM.PC.PARAM` in `PM_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PM.PC.PAR.POSN.TYPE` | `PmPcParam_PosnType` |  |  |  |
| 2 | `PM.PC.PAR.TRAN.CODE.START` | `PmPcParam_TranCodeStart` |  |  |  |
| 3 | `PM.PC.PAR.TRAN.CODE.END` | `PmPcParam_TranCodeEnd` |  |  |  |
| 4 | `PM.PC.PAR.ACC.MVMT.CHAR` | `PmPcParam_AccMvmtChar` |  |  |  |
| 5 | `PM.PC.PAR.REAL.FX.CLASS` | `PmPcParam_RealFxClass` | TField | No | For applications linked to PM through generic interface (Applications in modules other than FR, FX, LD, MM, ND, SC, SW), this field specifies the PM Module FX position movements created by real accounting entries. Validation Rules: Optional field. Should be the ID of a valid record of PM.POSN.CLASS. First 2 characters should match with that of the ID value. Value not allowed if the record ID is PD. |
| 6 | `PM.PC.PAR.FWD.FX.CLASS` | `PmPcParam_FwdFxClass` | TField | Conditional | For applications linked to PM through generic interface (Applications in modules other than FR, FX, LD, MM, ND, SC, SW), this field specifies the FX position movements created by forward (cash-flow) accounting entries. Validation Rules: Optional field. Should be the ID of a valid record of PM.POSN.CLASS. First 2 characters should match with that of the ID value. Value Mandatory if the field FWD.FX.PRG.CNT has a value. Input not allowed in records with ID as DC, PD or TT. |
| 7 | `PM.PC.PAR.FWD.FX.PRG.CNT` | `PmPcParam_FwdFxPrgCnt` | TField | Yes | For applications linked to PM through generic interface (Applications in modules other than FR, FX, LD, MM, ND, SC, SW),this field specifies whether FX position movements for forward (cash-flow) accounting movements need to be generated in PM.TRAN.ACTIVITY or not. Validation Rules: Value allowed only if FWD.FX.CLASS is specified. Valid values are APPLIC, NO and YES. NO - No FX forward position details would be generated. YES - FX forward position details would be generated. APPLIC - Application will determine whether the Forward position movement details need to be generated. Mandatory field and cannot be set NONE, when FWD.FX.CLASS is specified. |
| 8 | `PM.PC.PAR.RESERVED.4` | `PmPcParam_Reserved4` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 1 characters may be entered. This is a NOINPUT field. |
| 9 | `PM.PC.PAR.RESERVED.3` | `PmPcParam_Reserved3` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 1 characters may be entered. This is a NOINPUT field. |
| 10 | `PM.PC.PAR.RESERVED.2` | `PmPcParam_Reserved2` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 1 characters may be entered. This is a NOINPUT field. |
| 11 | `PM.PC.PAR.RESERVED.1` | `PmPcParam_Reserved1` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 1 characters may be entered. This is a NOINPUT field. |
| 12 | `PM.PC.PAR.RECORD.STATUS` | `PmPcParam_RecordStatus` | String |  |  |
| 13 | `PM.PC.PAR.CURR.NO` | `PmPcParam_CurrNo` | String |  |  |
| 14 | `PM.PC.PAR.INPUTTER` | `PmPcParam_Inputter` |  |  |  |
| 15 | `PM.PC.PAR.DATE.TIME` | `PmPcParam_DateTime` |  |  |  |
| 16 | `PM.PC.PAR.AUTHORISER` | `PmPcParam_Authoriser` | String |  |  |
| 17 | `PM.PC.PAR.CO.CODE` | `PmPcParam_CoCode` | String |  |  |
| 18 | `PM.PC.PAR.DEPT.CODE` | `PmPcParam_DeptCode` | String |  |  |
| 19 | `PM.PC.PAR.AUDITOR.CODE` | `PmPcParam_AuditorCode` | String |  |  |
| 20 | `PM.PC.PAR.AUDIT.DATE.TIME` | `PmPcParam_AuditDateTime` | String |  |  |
