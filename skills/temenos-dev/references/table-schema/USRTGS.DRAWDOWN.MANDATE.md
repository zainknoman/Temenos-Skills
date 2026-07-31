# USRTGS.DRAWDOWN.MANDATE — Table Schema

> Source: `INSERTS/I_F.USRTGS.DRAWDOWN.MANDATE` in `USRTGS_Fedwire.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FWDM.DEBIT.ACCOUNT.NUMBER` | `UsrtgsDrawdownMandate_DebitAccountNumber` | TField | Yes | Account number mandated for the drawdown request. It is a mandatory field. |
| 2 | `FWDM.DEBIT.ACCOUNT.NAME` | `UsrtgsDrawdownMandate_DebitAccountName` | TField |  | Account Title mandated for the drawdown request. |
| 3 | `FWDM.RECIPIENT.ACCOUNT.NUMBER` | `UsrtgsDrawdownMandate_RecipientAccountNumber` | TField | Yes | External account number to which the credit must be posted. It is a mandatory field. |
| 4 | `FWDM.MAXIMUM.AMOUNT` | `UsrtgsDrawdownMandate_MaximumAmount` | TField | Yes | The maximum amount permitted per drawdown request. It is a mandatory field. |
| 5 | `FWDM.DFI.NAME` | `UsrtgsDrawdownMandate_DfiName` | TField | Yes | Name of the receiving financial institute. It is a mandatory field. |
| 6 | `FWDM.ROUTING.NUMBER` | `UsrtgsDrawdownMandate_RoutingNumber` | TField | Yes | Routing number of the financial institute where the receiving account is held. It is a mandatory field. |
| 7 | `FWDM.RECIPIENT.NAME` | `UsrtgsDrawdownMandate_RecipientName` | TField | Yes | Name of the customer for whom the drawdown request will be sent. It is a mandatory field. |
| 8 | `FWDM.RECIPIENT.ACCOUNT.TYPE` | `UsrtgsDrawdownMandate_RecipientAccountType` | TField |  | Account type of the recipient account number, Checking, Savings or DDA. |
| 9 | `FWDM.RECIPIENT.ADDRESS` | `UsrtgsDrawdownMandate_RecipientAddress` | TField |  | Address of the customer raising the drawdown request. |
| 10 | `FWDM.DRAWDOWN.PURPOSE` | `UsrtgsDrawdownMandate_DrawdownPurpose` |  |  |  |
| 11 | `FWDM.EFFECTIVE.FROM` | `UsrtgsDrawdownMandate_EffectiveFrom` | TField | Yes | Captures the date from when the mandate is activated. It is a mandatory field. |
| 12 | `FWDM.EFFECTIVE.TO` | `UsrtgsDrawdownMandate_EffectiveTo` | TField | Yes | Captures the date until the mandate is active. It is a mandatory field. |
| 13 | `FWDM.LOCAL.REF` | `UsrtgsDrawdownMandate_LocalRef` |  |  |  |
| 14 | `FWDM.OVERRIDE` | `UsrtgsDrawdownMandate_Override` |  |  |  |
| 15 | `FWDM.RECORD.STATUS` | `UsrtgsDrawdownMandate_RecordStatus` | String |  |  |
| 16 | `FWDM.CURR.NO` | `UsrtgsDrawdownMandate_CurrNo` | String |  |  |
| 17 | `FWDM.INPUTTER` | `UsrtgsDrawdownMandate_Inputter` |  |  |  |
| 18 | `FWDM.DATE.TIME` | `UsrtgsDrawdownMandate_DateTime` |  |  |  |
| 19 | `FWDM.AUTHORISER` | `UsrtgsDrawdownMandate_Authoriser` | String |  |  |
| 20 | `FWDM.CO.CODE` | `UsrtgsDrawdownMandate_CoCode` | String |  |  |
| 21 | `FWDM.DEPT.CODE` | `UsrtgsDrawdownMandate_DeptCode` | String |  |  |
| 22 | `FWDM.AUDITOR.CODE` | `UsrtgsDrawdownMandate_AuditorCode` | String |  |  |
| 23 | `FWDM.AUDIT.DATE.TIME` | `UsrtgsDrawdownMandate_AuditDateTime` | String |  |  |
