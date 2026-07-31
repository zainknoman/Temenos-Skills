# SC.BUILD.UPFRONT.POSITION — Table Schema

> Source: `INSERTS/I_F.SC.BUILD.UPFRONT.POSITION` in `SC_SctOffMarketTrades.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.BUI.FUND.ID` | `ScBuildUpfrontPosition_FundId` | TField | Yes | This field will hold Original security for which the NAV is captured. Validation Rules: It should be valid security Master ID (Mandatory input) |
| 2 | `SC.BUI.NAV` | `ScBuildUpfrontPosition_Nav` | TField | Yes | This field holds the Price (Net Asset Value) for the Original security. The NAV is the execution price for the fund order placed. Validation Rules: Mandatory Input |
| 3 | `SC.BUI.SEC.TRADE.ID` | `ScBuildUpfrontPosition_SecTradeId` |  |  |  |
| 4 | `SC.BUI.UPFRONT.SEC` | `ScBuildUpfrontPosition_UpfrontSec` | TField |  | This fields gets defaulted with the value in the field UPFRONT.SEC from security master application pertaining to the security defined in FUND.ID Validation Rules: This is a NOINPUT field |
| 5 | `SC.BUI.BEGIN.DATE` | `ScBuildUpfrontPosition_BeginDate` | TField |  | This field will hold the Begin Date for auto selection of SEC.TRADEs. SEC.TRADEs with TRADE.DATE greater or equal to this date will be selected |
| 6 | `SC.BUI.END.DATE` | `ScBuildUpfrontPosition_EndDate` | TField |  | This field will hold the End Date for auto selection of SEC.TRADEs. SEC.TRADEs with TRADE.DATE lesser or equal to this date will be selected.If Blank, SEC.TRADEs with TRADE.DATE lesser or equal to TODAY will be selected Validation Rules: Valid Date Field |
| 7 | `SC.BUI.OLD.FUND.ID` | `ScBuildUpfrontPosition_OldFundId` | TField |  | Field to hold the Previous fund ID in case of Hedge Funds where Active Fund series has changed. If an Old Fund ID is given, then all trades in this Old fund id will be selected and position would be moved to the new fund Validation Rules: Must exist on SECURITY.MASTER table |
| 8 | `SC.BUI.RESERVED.1` | `ScBuildUpfrontPosition_Reserved1` | TField |  |  |
| 9 | `SC.BUI.LOCAL.REF` | `ScBuildUpfrontPosition_LocalRef` |  |  |  |
| 10 | `SC.BUI.RECORD.STATUS` | `ScBuildUpfrontPosition_RecordStatus` | String |  |  |
| 11 | `SC.BUI.CURR.NO` | `ScBuildUpfrontPosition_CurrNo` | String |  |  |
| 12 | `SC.BUI.INPUTTER` | `ScBuildUpfrontPosition_Inputter` |  |  |  |
| 13 | `SC.BUI.DATE.TIME` | `ScBuildUpfrontPosition_DateTime` |  |  |  |
| 14 | `SC.BUI.AUTHORISER` | `ScBuildUpfrontPosition_Authoriser` | String |  |  |
| 15 | `SC.BUI.CO.CODE` | `ScBuildUpfrontPosition_CoCode` | String |  |  |
| 16 | `SC.BUI.DEPT.CODE` | `ScBuildUpfrontPosition_DeptCode` | String |  |  |
| 17 | `SC.BUI.AUDITOR.CODE` | `ScBuildUpfrontPosition_AuditorCode` | String |  |  |
| 18 | `SC.BUI.AUDIT.DATE.TIME` | `ScBuildUpfrontPosition_AuditDateTime` | String |  |  |
