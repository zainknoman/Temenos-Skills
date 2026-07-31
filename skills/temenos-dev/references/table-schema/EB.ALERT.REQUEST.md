# EB.ALERT.REQUEST — Table Schema

> Source: `INSERTS/I_F.EB.ALERT.REQUEST` in `EB_AlertProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.AR.EVENT` | `EbAlertRequest_Event` | TField |  | Identifies the event from TEC.ITEMS.A valid event from TEC.ITEMS should be specified in this field. These TEC.ITEMS are designed to define the conditions to trigger alerts. Validation Rules: This is a NOCHANGE field |
| 2 | `EB.AR.CONTRACT.REF` | `EbAlertRequest_ContractRef` | TField |  | Identifies the Account number,arrangement id or Portfolio No, subscribing to the alerts. |
| 3 | `EB.AR.ACCOUNT.OFFICER` | `EbAlertRequest_AccountOfficer` |  |  |  |
| 4 | `EB.AR.FIELD` | `EbAlertRequest_Field` |  |  |  |
| 5 | `EB.AR.FIELD.DESC` | `EbAlertRequest_FieldDesc` |  |  |  |
| 6 | `EB.AR.FIELD.NO` | `EbAlertRequest_FieldNo` |  |  |  |
| 7 | `EB.AR.OPERAND` | `EbAlertRequest_Operand` |  |  |  |
| 8 | `EB.AR.VALUE` | `EbAlertRequest_Value` |  |  |  |
| 9 | `EB.AR.SUBSCRIBE` | `EbAlertRequest_Subscribe` | TField | Yes | An alert is subscribed based on the value in this field. This field can be set to YES/NO Whether the customer/account officer has subscribed to or wants to unsubscribe from the event. By default set as YES. It is a mandatory field. Validation Rules: Accepted values to this field are YES/NO |
| 10 | `EB.AR.CUSTOMER` | `EbAlertRequest_Customer` | TField |  | Customer associated with the Account, Arrangement or Portfolio can be input. If no value is input,valid customer number gets defaulted from the Account, Arrangement or Portfolio Id specified in the field Contract Ref. |
| 11 | `EB.AR.EXT.USER.ID` | `EbAlertRequest_ExtUserId` | TField |  |  |
| 12 | `EB.AR.EXT.CUST.ID` | `EbAlertRequest_ExtCustId` | TField |  |  |
| 13 | `EB.AR.RESERVED.8` | `EbAlertRequest_Reserved8` | TField |  |  |
| 14 | `EB.AR.RESERVED.7` | `EbAlertRequest_Reserved7` | TField |  |  |
| 15 | `EB.AR.RESERVED.6` | `EbAlertRequest_Reserved6` | TField |  |  |
| 16 | `EB.AR.RESERVED.5` | `EbAlertRequest_Reserved5` | TField |  |  |
| 17 | `EB.AR.RESERVED.4` | `EbAlertRequest_Reserved4` | TField |  |  |
| 18 | `EB.AR.RESERVED.3` | `EbAlertRequest_Reserved3` | TField |  |  |
| 19 | `EB.AR.RESERVED.2` | `EbAlertRequest_Reserved2` | TField |  |  |
| 20 | `EB.AR.RESERVED.1` | `EbAlertRequest_Reserved1` | TField |  |  |
| 21 | `EB.AR.LOCAL.REF` | `EbAlertRequest_LocalRef` |  |  |  |
| 22 | `EB.AR.OVERRIDE` | `EbAlertRequest_Override` |  |  |  |
| 23 | `EB.AR.RECORD.STATUS` | `EbAlertRequest_RecordStatus` | String |  |  |
| 24 | `EB.AR.CURR.NO` | `EbAlertRequest_CurrNo` | String |  |  |
| 25 | `EB.AR.INPUTTER` | `EbAlertRequest_Inputter` |  |  |  |
| 26 | `EB.AR.DATE.TIME` | `EbAlertRequest_DateTime` |  |  |  |
| 27 | `EB.AR.AUTHORISER` | `EbAlertRequest_Authoriser` | String |  |  |
| 28 | `EB.AR.CO.CODE` | `EbAlertRequest_CoCode` | String |  |  |
| 29 | `EB.AR.DEPT.CODE` | `EbAlertRequest_DeptCode` | String |  |  |
| 30 | `EB.AR.AUDITOR.CODE` | `EbAlertRequest_AuditorCode` | String |  |  |
| 31 | `EB.AR.AUDIT.DATE.TIME` | `EbAlertRequest_AuditDateTime` | String |  |  |
