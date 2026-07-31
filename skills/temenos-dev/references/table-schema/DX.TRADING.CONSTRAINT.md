# DX.TRADING.CONSTRAINT — Table Schema

> Source: `INSERTS/I_F.DX.TRADING.CONSTRAINT` in `DX_Constraints.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.TC.FIELD.NAME` | `DxTradingConstraint_FieldName` |  |  |  |
| 2 | `DX.TC.SEC.FIELD.NAME` | `DxTradingConstraint_SecFieldName` |  |  |  |
| 3 | `DX.TC.OPERATOR` | `DxTradingConstraint_Operator` |  |  |  |
| 4 | `DX.TC.FIELD.CONTENT` | `DxTradingConstraint_FieldContent` |  |  |  |
| 5 | `DX.TC.FIELD.TO` | `DxTradingConstraint_FieldTo` |  |  |  |
| 6 | `DX.TC.NARRATIVE` | `DxTradingConstraint_Narrative` |  |  |  |
| 7 | `DX.TC.MESSAGE.TYPE` | `DxTradingConstraint_MessageType` |  |  |  |
| 8 | `DX.TC.LOGIC` | `DxTradingConstraint_Logic` |  |  |  |
| 9 | `DX.TC.RESERVED.05` | `DxTradingConstraint_Reserved05` |  |  |  |
| 10 | `DX.TC.CONSTRAINT.TYPE` | `DxTradingConstraint_ConstraintType` | TField |  | This field controls the overall logic of the constraint. If the Constraint Type is 'Permission' and the conditions specified in the constraint are met, then the transaction is allowed to proceed; if the Constraint Type is 'Restriction' and the conditions specified in the constraint are not met, then the transaction is allowed to proceed; otherwise the relevant message type (i.e. error or override) will be generated with the corresponding narrative. The field can be set to 'Permission', 'Restriction' or simply left blank. If blank, 'Restriction' is assumed. |
| 11 | `DX.TC.RESERVED.03` | `DxTradingConstraint_Reserved03` | TField |  | Reserved For Future Use Validation Rules: No Input Field |
| 12 | `DX.TC.RESERVED.02` | `DxTradingConstraint_Reserved02` | TField |  | Reserved For Future Use Validation Rules: No Input Field |
| 13 | `DX.TC.RESERVED.01` | `DxTradingConstraint_Reserved01` | TField |  | Reserved For Future Use Validation Rules: No Input Field |
| 14 | `DX.TC.RECORD.STATUS` | `DxTradingConstraint_RecordStatus` | String |  |  |
| 15 | `DX.TC.CURR.NO` | `DxTradingConstraint_CurrNo` | String |  |  |
| 16 | `DX.TC.INPUTTER` | `DxTradingConstraint_Inputter` |  |  |  |
| 17 | `DX.TC.DATE.TIME` | `DxTradingConstraint_DateTime` |  |  |  |
| 18 | `DX.TC.AUTHORISER` | `DxTradingConstraint_Authoriser` | String |  |  |
| 19 | `DX.TC.CO.CODE` | `DxTradingConstraint_CoCode` | String |  |  |
| 20 | `DX.TC.DEPT.CODE` | `DxTradingConstraint_DeptCode` | String |  |  |
| 21 | `DX.TC.AUDITOR.CODE` | `DxTradingConstraint_AuditorCode` | String |  |  |
| 22 | `DX.TC.AUDIT.DATE.TIME` | `DxTradingConstraint_AuditDateTime` | String |  |  |
