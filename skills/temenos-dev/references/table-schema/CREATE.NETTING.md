# CREATE.NETTING — Table Schema

> Source: `INSERTS/I_F.CREATE.NETTING` in `AC_PaymentNetting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.CN.CURRENCY` | `CreateNetting_Currency` | TField | No | Identifies the currency of transactions used is association with VALUE.DATE and COUNTERPARTY as selection criteria. Will be used to select transactions for propagation to the NETTING file for agreement. Validation Rules: Optional input. |
| 2 | `AC.CN.COUNTERPARTY` | `CreateNetting_Counterparty` | TField | Yes | Identifies the Counterparty of transactions used is association with VALUE.DATE and CURRENCY as selection criteria. Will be used to select transactions for propagation to the NETTING file for agreement. Validation Rules: Mandatory input for Non-CLS deals. Not allowed if CLS.SETTLEMENT is set to YES. |
| 3 | `AC.CN.VALUE.DATE` | `CreateNetting_ValueDate` | TField | No | Identifies the value date of transactions used in association with CURRENCY and COUNTERPARTY as selection criteria. The value date represents the start of a range of value dates that will be used to select transactions for propagation to the NETTING file. The parameter NETTING.PARAMETERS - DAYS.AHEAD will be summed with this date to provide the final value date in the range. Validation Rules: Optional input. |
| 4 | `AC.CN.SYSTEM.ID` | `CreateNetting_SystemId` |  |  |  |
| 5 | `AC.CN.SEND.CORR.BK` | `CreateNetting_SendCorrBk` | TField |  | Identifies the Sender Correspondent Bank (tag 53) in Funds transfer application and details entered here along with COUNTERPARTY, SYSTEM.ID, REC.CORR.BANK,VALUE.DATE, CURRENCY and OPERATION.CODE is be used to select transactions for propagation to the NETTING file to generate MT102 and MT203. To create netting for Forex application CURRENCY,COUNTERPARTY, and VALUE.DATE is alone used to for selection Criteria and Input in this field not allowed. Validation Rules: Input allowed only when SYSTEM.ID = FT |
| 6 | `AC.CN.REC.CORR.BK` | `CreateNetting_RecCorrBk` | TField |  | Identifies the Receiver Correspondent Bank (tag 54) in Funds transfer application and details entered here along with COUNTERPARTY, SYSTEM.ID, SEND.CORR.BANK, VALUE.DATE, CURRENCY and OPERATION.CODE is be used to select transactions for propagation to the NETTING file to generate MT102 and MT203. To create netting for Forex application CURRENCY, COUNTERPARTY, and VALUE.DATE is alone used to for selection Criteria and Input in this field not allowed. Validation Rules: Input allowed only when SYSTEM.ID = FT |
| 7 | `AC.CN.MSG.TYPE` | `CreateNetting_MsgType` | TField |  | This field will hold the message type for which netting to be done. Validation Rules: Valid Swift Message Type as defined in DE.MESSAGE. This field if valid only if System.Id has value 'FT' Now the allowed message type are 102 and 203 |
| 8 | `AC.CN.OPERATION.CODE` | `CreateNetting_OperationCode` | TField | Conditional | When CHQB is given in this field, the system will try to net payments, which have been instructed to be paid by CHEQUE to beneficiary. When CREDIT is given, the credit transfers should be processed according to the netting agreement between sender and receiver. Validation Rules: Optional Input Valid values are CREDIT and CHQB Mandatory for MSG.TYPE 102 |
| 9 | `AC.CN.CLS.SETTLEMENT` | `CreateNetting_ClsSettlement` | TField | No | This field is used to define if the Payments to be Netted is for Multilateral Netting or Bilateral Netting i.e. CLS or Non-CLS settlements. Value YES in this field indicates the Multilateral Netting. Value NO or blank in this field indicates the Bilateral Netting. Validation Rules: Allowed values are YES or NO (Optional Input). |
| 10 | `AC.CN.RECORD.STATUS` | `CreateNetting_RecordStatus` | String |  |  |
| 11 | `AC.CN.CURR.NO` | `CreateNetting_CurrNo` | String |  |  |
| 12 | `AC.CN.INPUTTER` | `CreateNetting_Inputter` |  |  |  |
| 13 | `AC.CN.DATE.TIME` | `CreateNetting_DateTime` |  |  |  |
| 14 | `AC.CN.AUTHORISER` | `CreateNetting_Authoriser` | String |  |  |
| 15 | `AC.CN.CO.CODE` | `CreateNetting_CoCode` | String |  |  |
| 16 | `AC.CN.DEPT.CODE` | `CreateNetting_DeptCode` | String |  |  |
| 17 | `AC.CN.AUDITOR.CODE` | `CreateNetting_AuditorCode` | String |  |  |
| 18 | `AC.CN.AUDIT.DATE.TIME` | `CreateNetting_AuditDateTime` | String |  |  |
