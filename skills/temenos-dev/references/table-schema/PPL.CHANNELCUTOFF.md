# PPL.CHANNELCUTOFF — Table Schema

> Source: `INSERTS/I_F.PPL.CHANNELCUTOFF` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPLCC.ChannelCutOffID` | `PplChannelcutoff_Channelcutoffid` |  |  |  |
| 2 | `PPLCC.CompanyID` | `PplChannelcutoff_Companyid` |  |  |  |
| 3 | `PPLCC.ChannelName` | `PplChannelcutoff_Channelname` |  |  |  |
| 4 | `PPLCC.CurrencyCode` | `PplChannelcutoff_Currencycode` |  |  |  |
| 5 | `PPLCC.CTRBTRIndicator` | `PplChannelcutoff_Ctrbtrindicator` |  |  |  |
| 6 | `PPLCC.PaymentDirection` | `PplChannelcutoff_Paymentdirection` |  |  |  |
| 7 | `PPLCC.Priority` | `PplChannelcutoff_Priority` |  |  |  |
| 8 | `PPLCC.MessageType` | `PplChannelcutoff_Messagetype` |  |  |  |
| 9 | `PPLCC.Source` | `PplChannelcutoff_Source` |  |  |  |
| 10 | `PPLCC.StartDateChannelCutoff` | `PplChannelcutoff_Startdatechannelcutoff` |  |  |  |
| 11 | `PPLCC.CutoffTime` | `PplChannelcutoff_Cutofftime` |  |  |  |
| 12 | `PPLCC.CutoffTimeWithFX` | `PplChannelcutoff_Cutofftimewithfx` |  |  |  |
| 13 | `PPLCC.SettlementShift` | `PplChannelcutoff_Settlementshift` |  |  |  |
| 14 | `PPLCC.FXShift` | `PplChannelcutoff_Fxshift` |  |  |  |
| 15 | `PPLCC.CutoffShift` | `PplChannelcutoff_Cutoffshift` |  |  |  |
| 16 | `PPLCC.ASAPALAP` | `PplChannelcutoff_Asapalap` |  |  |  |
| 17 | `PPLCC.EndDateChannelCutoff` | `PplChannelcutoff_Enddatechannelcutoff` |  |  |  |
| 18 | `PPLCC.RACChannelCutoff` | `PplChannelcutoff_Racchannelcutoff` |  |  |  |
| 19 | `PPLCC.RSCChannelCutoff` | `PplChannelcutoff_Rscchannelcutoff` |  |  |  |
| 20 | `PPLCC.EntryUserID` | `PplChannelcutoff_Entryuserid` |  |  |  |
| 21 | `PPLCC.EntryDateTime` | `PplChannelcutoff_Entrydatetime` |  |  |  |
| 22 | `PPLCC.ApproverUserID` | `PplChannelcutoff_Approveruserid` |  |  |  |
| 23 | `PPLCC.ApprovedDateTime` | `PplChannelcutoff_Approveddatetime` |  |  |  |
