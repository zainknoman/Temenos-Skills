# PM.DX.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PM.DX.PARAMETER` in `DX_PositionManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PM.DX.PARAM.DESCRIPTION` | `PmDxParameter_Description` |  |  |  |
| 2 | `PM.DX.PARAM.UPDATE.CAS` | `PmDxParameter_UpdateCas` | TField |  | This field specifies whether the CAS position movements for the COMMISSIONS involved in the DX trade should be captured in Position Management. When this field is set to �YES�, the CAS movements for all the types of DX trades (both futures and options) will be captured in Position Management. Validation Rules: : Values allowed are "Yes" or "Null". |
| 3 | `PM.DX.PARAM.REAL.FX.CLASS` | `PmDxParameter_RealFxClass` | TField |  | This field specifies the valid position class ID to capture FX spot position movements for CAS positions captured in PM. Input allowed only when the UPDATE.CAS is set to "YES". Validation Rules: : Input must be a valid PM.POSN.CLASS record id. The first two characters of the position class should be �DX�. |
| 4 | `PM.DX.PARAM.FWD.FX.PRG.CNT` | `PmDxParameter_FwdFxPrgCnt` | TField |  | This field specifies whether the FX forward position movements for the CAS positions should be captured in PM.When the field is set to �YES�, a valid PM.POSN.CLASS id should be defined in field FWD.FX.CLASS, which will be used to capture the FX forward positions. Input allowed only when the UPDATE.CAS is set to YES. Validation Rules: : Options are "Yes" or "No". Input allowed only when the UPDATE.CAS is set to YES. |
| 5 | `PM.DX.PARAM.FWD.FX.CLASS` | `PmDxParameter_FwdFxClass` | TField |  | This field specifies the valid position class ID to capture FX forward position movements for CAS positions captured in PM. Input allowed only when FWD.FX.PRG.CNT field is set to "YES". Validation Rules: : Input must be a valid PM.POSN.CLASS record id. The first two characters of the position class should be �DX�. |
| 6 | `PM.DX.PARAM.FIN.INT.RT.FUT` | `PmDxParameter_FinIntRtFut` |  |  |  |
| 7 | `PM.DX.PARAM.INT.RT.START.CLS` | `PmDxParameter_IntRtStartCls` |  |  |  |
| 8 | `PM.DX.PARAM.INT.RT.END.CLS` | `PmDxParameter_IntRtEndCls` |  |  |  |
| 9 | `PM.DX.PARAM.FIN.BOND.FUT` | `PmDxParameter_FinBondFut` |  |  |  |
| 10 | `PM.DX.PARAM.BOND.START.CLS` | `PmDxParameter_BondStartCls` |  |  |  |
| 11 | `PM.DX.PARAM.BOND.END.CLS` | `PmDxParameter_BondEndCls` |  |  |  |
| 12 | `PM.DX.PARAM.FIN.CCY.FUT` | `PmDxParameter_FinCcyFut` |  |  |  |
| 13 | `PM.DX.PARAM.CCY.POSN.CLS` | `PmDxParameter_CcyPosnCls` |  |  |  |
| 14 | `PM.DX.PARAM.TRADE.GAP` | `PmDxParameter_TradeGap` | TField |  | If set to Yes, Financial Futures i.e Interest, Bond and Currency futures done for Trading purpose are also updated in Postion Management (PM) besides the Hedge Trades , both being Own book trades. Set to Null, only Hedge Trades are considered PM Updation. Validation Rules: : Options are "Yes" or "null". |
| 15 | `PM.DX.PARAM.RESERVED.1` | `PmDxParameter_Reserved1` | TField |  |  |
| 16 | `PM.DX.PARAM.RESERVED.2` | `PmDxParameter_Reserved2` | TField |  |  |
| 17 | `PM.DX.PARAM.RESERVED.3` | `PmDxParameter_Reserved3` | TField |  |  |
| 18 | `PM.DX.PARAM.RESERVED.4` | `PmDxParameter_Reserved4` | TField |  |  |
| 19 | `PM.DX.PARAM.RESERVED.5` | `PmDxParameter_Reserved5` | TField |  |  |
| 20 | `PM.DX.PARAM.RECORD.STATUS` | `PmDxParameter_RecordStatus` | String |  |  |
| 21 | `PM.DX.PARAM.CURR.NO` | `PmDxParameter_CurrNo` | String |  |  |
| 22 | `PM.DX.PARAM.INPUTTER` | `PmDxParameter_Inputter` |  |  |  |
| 23 | `PM.DX.PARAM.DATE.TIME` | `PmDxParameter_DateTime` |  |  |  |
| 24 | `PM.DX.PARAM.AUTHORISER` | `PmDxParameter_Authoriser` | String |  |  |
| 25 | `PM.DX.PARAM.CO.CODE` | `PmDxParameter_CoCode` | String |  |  |
| 26 | `PM.DX.PARAM.DEPT.CODE` | `PmDxParameter_DeptCode` | String |  |  |
| 27 | `PM.DX.PARAM.AUDITOR.CODE` | `PmDxParameter_AuditorCode` | String |  |  |
| 28 | `PM.DX.PARAM.AUDIT.DATE.TIME` | `PmDxParameter_AuditDateTime` | String |  |  |
