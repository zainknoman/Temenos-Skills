# PP.CHANNEL.CUTOFF.PDS — Table Schema

> Source: `INSERTS/I_F.PP.CHANNEL.CUTOFF.PDS` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.LCC.CompanyID` | `PpChannelCutoffPds_Companyid` | TField |  |  |
| 2 | `PP.LCC.ChannelName` | `PpChannelCutoffPds_Channelname` | TField |  |  |
| 3 | `PP.LCC.CurrencyCode` | `PpChannelCutoffPds_Currencycode` | TField |  |  |
| 4 | `PP.LCC.CTRBTRIndicator` | `PpChannelCutoffPds_Ctrbtrindicator` | TField |  |  |
| 5 | `PP.LCC.PaymentDirection` | `PpChannelCutoffPds_Paymentdirection` | TField |  |  |
| 6 | `PP.LCC.Priority` | `PpChannelCutoffPds_Priority` | TField |  |  |
| 7 | `PP.LCC.MessageType` | `PpChannelCutoffPds_Messagetype` | TField |  |  |
| 8 | `PP.LCC.Source` | `PpChannelCutoffPds_Source` | TField |  |  |
| 9 | `PP.LCC.CutoffTime` | `PpChannelCutoffPds_Cutofftime` | TField |  |  |
| 10 | `PP.LCC.CutoffTimeWithFX` | `PpChannelCutoffPds_Cutofftimewithfx` | TField |  |  |
| 11 | `PP.LCC.SettlementShift` | `PpChannelCutoffPds_Settlementshift` | TField |  |  |
| 12 | `PP.LCC.FXShift` | `PpChannelCutoffPds_Fxshift` | TField |  |  |
| 13 | `PP.LCC.CutoffShift` | `PpChannelCutoffPds_Cutoffshift` | TField |  |  |
| 14 | `PP.LCC.ASAPALAP` | `PpChannelCutoffPds_Asapalap` | TField |  |  |
| 15 | `PP.LCC.StartDate` | `PpChannelCutoffPds_Startdate` | TField |  |  |
| 16 | `PP.LCC.EndDate` | `PpChannelCutoffPds_Enddate` | TField |  |  |
| 17 | `PP.LCC.CPCurrencyCode` | `PpChannelCutoffPds_Cpcurrencycode` |  |  |  |
| 18 | `PP.LCC.CPFXShift` | `PpChannelCutoffPds_Cpfxshift` |  |  |  |
| 19 | `PP.LCC.CPCutoffTimeFX` | `PpChannelCutoffPds_Cpcutofftimefx` |  |  |  |
| 20 | `PP.LCC.RepairCutOffTime` | `PpChannelCutoffPds_Repaircutofftime` | TField |  |  |
| 21 | `PP.LCC.RepairCutOffTimeFX` | `PpChannelCutoffPds_Repaircutofftimefx` | TField |  |  |
| 22 | `PP.LCC.ClearingNatureCode` | `PpChannelCutoffPds_Clearingnaturecode` |  |  |  |
| 23 | `PP.LCC.MaxInstTimeOut` | `PpChannelCutoffPds_Maxinsttimeout` |  |  |  |
| 24 | `PP.LCC.RESERVED.1` | `PpChannelCutoffPds_Reserved1` |  |  |  |
| 25 | `PP.LCC.LOCAL.REF` | `PpChannelCutoffPds_LocalRef` |  |  |  |
| 26 | `PP.LCC.LinkID` | `PpChannelCutoffPds_Linkid` | TField |  |  |
| 27 | `PP.LCC.OVERRIDE` | `PpChannelCutoffPds_Override` |  |  |  |
| 28 | `PP.LCC.RECORD.STATUS` | `PpChannelCutoffPds_RecordStatus` | String |  |  |
| 29 | `PP.LCC.CURR.NO` | `PpChannelCutoffPds_CurrNo` | String |  |  |
| 30 | `PP.LCC.INPUTTER` | `PpChannelCutoffPds_Inputter` |  |  |  |
| 31 | `PP.LCC.DATE.TIME` | `PpChannelCutoffPds_DateTime` |  |  |  |
| 32 | `PP.LCC.AUTHORISER` | `PpChannelCutoffPds_Authoriser` | String |  |  |
| 33 | `PP.LCC.CO.CODE` | `PpChannelCutoffPds_CoCode` | String |  |  |
| 34 | `PP.LCC.DEPT.CODE` | `PpChannelCutoffPds_DeptCode` | String |  |  |
| 35 | `PP.LCC.AUDITOR.CODE` | `PpChannelCutoffPds_AuditorCode` | String |  |  |
| 36 | `PP.LCC.AUDIT.DATE.TIME` | `PpChannelCutoffPds_AuditDateTime` | String |  |  |
