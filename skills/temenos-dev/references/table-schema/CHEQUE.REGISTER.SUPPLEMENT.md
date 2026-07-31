# CHEQUE.REGISTER.SUPPLEMENT — Table Schema

> Source: `INSERTS/I_F.CHEQUE.REGISTER.SUPPLEMENT` in `CQ_ChqSubmit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CC.CRS.STATUS` | `ChequeRegisterSupplement_Status` | TField |  | This field holds the status of the draft/cheque. Validation Rules: Allows any of the following values: ISSUED, PRESENTED, CLEARED, CLEARED-PARTIAL, EXCEPTION, UNKNOWN, CANCELLED, STOPPED and RETURNED or EXPIRED. |
| 2 | `CC.CRS.CURRENCY` | `ChequeRegisterSupplement_Currency` | TField |  | This field holds the currency of the draft/cheque. Validation Rules: Allows valid currency from CURRENCY table. |
| 3 | `CC.CRS.AMOUNT` | `ChequeRegisterSupplement_Amount` | TField |  | This field holds the draft/cheque amount. Validation Rules: Allows 1-14 characters (plus a decimal point). (Standard Amount format) - type AMT |
| 4 | `CC.CRS.PAYEE.NAME` | `ChequeRegisterSupplement_PayeeName` |  |  |  |
| 5 | `CC.CRS.ISSUE.DATE` | `ChequeRegisterSupplement_IssueDate` | TField |  | This field holds the issue date of draft/cheque. Validation Rules: Standard T24 Date field. |
| 6 | `CC.CRS.UPDATED.BY` | `ChequeRegisterSupplement_UpdatedBy` | TField |  | Value of this field indicates whether the supplement is updated manually or by the system. Validation Rules: NOINPUT field. Holds the value SYSTEM or MANUAL. |
| 7 | `CC.CRS.ORIGIN` | `ChequeRegisterSupplement_Origin` | TField |  | This field displays the application name through which the draft is issued. Validation Rules: NOINPUT field. |
| 8 | `CC.CRS.ORIGIN.REF` | `ChequeRegisterSupplement_OriginRef` | TField |  | This field displays the transaction reference of the originating application. Validation Rules: NOINPUT field. |
| 9 | `CC.CRS.DATE.PRESENTED` | `ChequeRegisterSupplement_DatePresented` |  |  |  |
| 10 | `CC.CRS.DATE.STOPPED` | `ChequeRegisterSupplement_DateStopped` | TField |  | This field displays a date when the cheque/draft is stopped. Validation Rules: NOINPUT field. |
| 11 | `CC.CRS.PAYM.STOP.TYPE` | `ChequeRegisterSupplement_PaymStopType` | TField |  | This field gets updated when supplement is updated from the field PAYMENT.STOP . It displays a reason for Payment Stop request. Validation Rules: NOINPUT field. |
| 12 | `CC.CRS.AMOUNT.FROM` | `ChequeRegisterSupplement_AmountFrom` | TField |  | This field displays the amount from when the Payment Stop is effective. Validation Rules: NOINPUT field. |
| 13 | `CC.CRS.AMOUNT.TO` | `ChequeRegisterSupplement_AmountTo` | TField |  | This field displays the amount until when the Payment Stop is effective. Validation Rules: NOINPUT field. |
| 14 | `CC.CRS.BENEFICIARY` | `ChequeRegisterSupplement_Beneficiary` | TField |  | This field displays the payee's name. Validation Rules: NOINPUT field. |
| 15 | `CC.CRS.REMARKS` | `ChequeRegisterSupplement_Remarks` |  |  |  |
| 16 | `CC.CRS.PS.CURR.NO` | `ChequeRegisterSupplement_PsCurrNo` |  |  |  |
| 17 | `CC.CRS.REPRESENTED.COUNT` | `ChequeRegisterSupplement_RepresentedCount` | TField |  | This field displays the number of times the cheque is presented. Validation Rules: NOINPUT field. |
| 18 | `CC.CRS.ID.COMP1` | `ChequeRegisterSupplement_IdComp1` | TField |  | This field displays the cheque type of draft/cheque. Validation Rules: NOINPUT field. |
| 19 | `CC.CRS.ID.COMP2` | `ChequeRegisterSupplement_IdComp2` | TField |  | This field displays the account number of draft/cheque. Validation Rules: NOINPUT field. |
| 20 | `CC.CRS.ID.COMP3` | `ChequeRegisterSupplement_IdComp3` | TField |  | This field displays the cheque number of draft/cheque. Validation Rules: NOINPUT field. |
| 21 | `CC.CRS.DRAWER.ACCOUNT` | `ChequeRegisterSupplement_DrawerAccount` | TField |  | Account number of the customer who has originally issued the cheque.In case of the draft, the account number will be of the customer who had asked the bank to issue the draft. Valid T24 Account that is not CLOSED Validation Rules: Valid T24 Account |
| 22 | `CC.CRS.RETURN.COUNT` | `ChequeRegisterSupplement_ReturnCount` | TField |  | Number of times the cheque has been returned. Validation Rules: NOINPUT field. |
| 23 | `CC.CRS.PART.CLEARED.DATE` | `ChequeRegisterSupplement_PartClearedDate` |  |  |  |
| 24 | `CC.CRS.PART.CLEARED.AMOUNT` | `ChequeRegisterSupplement_PartClearedAmount` |  |  |  |
| 25 | `CC.CRS.RESERVED.6` | `ChequeRegisterSupplement_Reserved6` | TField |  |  |
| 26 | `CC.CRS.RESERVED.5` | `ChequeRegisterSupplement_Reserved5` | TField |  |  |
| 27 | `CC.CRS.RESERVED.4` | `ChequeRegisterSupplement_Reserved4` | TField |  |  |
| 28 | `CC.CRS.RESERVED.3` | `ChequeRegisterSupplement_Reserved3` | TField |  |  |
| 29 | `CC.CRS.RESERVED.2` | `ChequeRegisterSupplement_Reserved2` | TField |  |  |
| 30 | `CC.CRS.RESERVED.1` | `ChequeRegisterSupplement_Reserved1` | TField |  |  |
| 31 | `CC.CRS.LOCAL.REF` | `ChequeRegisterSupplement_LocalRef` |  |  |  |
| 32 | `CC.CRS.STMT.NOS` | `ChequeRegisterSupplement_StmtNos` |  |  |  |
| 33 | `CC.CRS.OVERRIDE` | `ChequeRegisterSupplement_Override` |  |  |  |
| 34 | `CC.CRS.RECORD.STATUS` | `ChequeRegisterSupplement_RecordStatus` | String |  |  |
| 35 | `CC.CRS.CURR.NO` | `ChequeRegisterSupplement_CurrNo` | String |  |  |
| 36 | `CC.CRS.INPUTTER` | `ChequeRegisterSupplement_Inputter` |  |  |  |
| 37 | `CC.CRS.DATE.TIME` | `ChequeRegisterSupplement_DateTime` |  |  |  |
| 38 | `CC.CRS.AUTHORISER` | `ChequeRegisterSupplement_Authoriser` | String |  |  |
| 39 | `CC.CRS.CO.CODE` | `ChequeRegisterSupplement_CoCode` | String |  |  |
| 40 | `CC.CRS.DEPT.CODE` | `ChequeRegisterSupplement_DeptCode` | String |  |  |
| 41 | `CC.CRS.AUDITOR.CODE` | `ChequeRegisterSupplement_AuditorCode` | String |  |  |
| 42 | `CC.CRS.AUDIT.DATE.TIME` | `ChequeRegisterSupplement_AuditDateTime` | String |  |  |
