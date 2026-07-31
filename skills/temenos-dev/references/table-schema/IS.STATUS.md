# IS.STATUS — Table Schema

> Source: `INSERTS/I_F.IS.STATUS` in `IS_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.STA.APPROVAL` | `IsStatus_Approval` | TField |  | Denotes if Approval Accounting has to be raised when the contract transits through this status. |
| 2 | `IS.STA.REV.APPROVAL` | `IsStatus_RevApproval` | TField |  | Denotes if Reversal of Approval Accounting has to be raised when the contract transits through this status. |
| 3 | `IS.STA.PURCHASE` | `IsStatus_Purchase` | TField |  | Denotes if Purchase Accounting has to be raised when the contract transits through this status. |
| 4 | `IS.STA.COST` | `IsStatus_Cost` | TField |  | Denotes if Cost Accounting has to be raised when the contract transits through this status. |
| 5 | `IS.STA.DOWN.PAYMENT` | `IsStatus_DownPayment` | TField |  | Denotes if Down Payment Accounting has to be raised when the contract transits through this status. |
| 6 | `IS.STA.RETURN.COM.TO.BROKER` | `IsStatus_ReturnComToBroker` | TField |  | This field will be used to set the flag to raise accounting entries for Return Commodity to Broker |
| 7 | `IS.STA.SELL.COM.TO.SELL.BROKER` | `IsStatus_SellComToSellBroker` | TField |  | This field will be used to set the flag to raise the accounting entries for Sell Commodity to Sell Broker |
| 8 | `IS.STA.BROKER.SETTLEMENT` | `IsStatus_BrokerSettlement` | TField |  | This field will be used to set the flag to raise accounting entries for Broker Settlement |
| 9 | `IS.STA.RESALE` | `IsStatus_Resale` | TField |  | This is used to control Accounting entries generated when resale transactions are posted |
| 10 | `IS.STA.LOCAL.REF` | `IsStatus_LocalRef` |  |  |  |
| 11 | `IS.STA.OVERRIDE` | `IsStatus_Override` |  |  |  |
| 12 | `IS.STA.RECORD.STATUS` | `IsStatus_RecordStatus` | String |  |  |
| 13 | `IS.STA.CURR.NO` | `IsStatus_CurrNo` | String |  |  |
| 14 | `IS.STA.INPUTTER` | `IsStatus_Inputter` |  |  |  |
| 15 | `IS.STA.DATE.TIME` | `IsStatus_DateTime` |  |  |  |
| 16 | `IS.STA.AUTHORISER` | `IsStatus_Authoriser` | String |  |  |
| 17 | `IS.STA.CO.CODE` | `IsStatus_CoCode` | String |  |  |
| 18 | `IS.STA.DEPT.CODE` | `IsStatus_DeptCode` | String |  |  |
| 19 | `IS.STA.AUDITOR.CODE` | `IsStatus_AuditorCode` | String |  |  |
| 20 | `IS.STA.AUDIT.DATE.TIME` | `IsStatus_AuditDateTime` | String |  |  |
