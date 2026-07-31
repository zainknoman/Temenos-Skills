# AM.PORT.TYPE — Table Schema

> Source: `INSERTS/I_F.AM.PORT.TYPE` in `AM_Group.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.PTY.DESCRIPTION` | `AmPortType_Description` |  |  |  |
| 2 | `AM.PTY.SHORT.NAME` | `AmPortType_ShortName` |  |  |  |
| 3 | `AM.PTY.TAX.WRAPPER` | `AmPortType_TaxWrapper` | TField |  | Indicates whether the specified portfolio type must maximise its benefits on tax. Validation Rules: Alphabetic Accepts only two values �Yes� and �No� |
| 4 | `AM.PTY.PRIORITY` | `AmPortType_Priority` | TField | Yes | Holds two numeric characters. No two portfolio types can have the same priority. Validation Rules: Numeric Mandatory field when TAX.WRAPPER field is set. |
| 5 | `AM.PTY.SUPPORT.MODEL` | `AmPortType_SupportModel` | TField | Yes | Accepts a valid id from the application INVESTMENT.PROGRAM. Validation Rules: Alpha numeric Mandatory field when TAX.WRAPPER field is set. |
| 6 | `AM.PTY.NOMINEE.CODE` | `AmPortType_NomineeCode` | TField |  | Accepts a valid nominee from the application NOMINEE.CODE. Sec open orders and bulk orders for the portfolio will be generated based on this Nominee code. Validation Rules: Alpha numeric |
| 7 | `AM.PTY.RESERVED.04` | `AmPortType_Reserved04` | TField |  |  |
| 8 | `AM.PTY.RESERVED.03` | `AmPortType_Reserved03` | TField |  |  |
| 9 | `AM.PTY.RESERVED.02` | `AmPortType_Reserved02` | TField |  |  |
| 10 | `AM.PTY.RESERVED.01` | `AmPortType_Reserved01` | TField |  |  |
| 11 | `AM.PTY.LOCAL.REF` | `AmPortType_LocalRef` |  |  |  |
| 12 | `AM.PTY.RECORD.STATUS` | `AmPortType_RecordStatus` | String |  |  |
| 13 | `AM.PTY.CURR.NO` | `AmPortType_CurrNo` | String |  |  |
| 14 | `AM.PTY.INPUTTER` | `AmPortType_Inputter` |  |  |  |
| 15 | `AM.PTY.DATE.TIME` | `AmPortType_DateTime` |  |  |  |
| 16 | `AM.PTY.AUTHORISER` | `AmPortType_Authoriser` | String |  |  |
| 17 | `AM.PTY.CO.CODE` | `AmPortType_CoCode` | String |  |  |
| 18 | `AM.PTY.DEPT.CODE` | `AmPortType_DeptCode` | String |  |  |
| 19 | `AM.PTY.AUDITOR.CODE` | `AmPortType_AuditorCode` | String |  |  |
| 20 | `AM.PTY.AUDIT.DATE.TIME` | `AmPortType_AuditDateTime` | String |  |  |
