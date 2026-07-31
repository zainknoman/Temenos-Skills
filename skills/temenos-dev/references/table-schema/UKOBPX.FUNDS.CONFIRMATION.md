# UKOBPX.FUNDS.CONFIRMATION — Table Schema

> Source: `INSERTS/I_F.UKOBPX.FUNDS.CONFIRMATION` in `UKOBPX_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UKFC.FUNDS.CONFIRMATION.ID` | `UkobpxFundsConfirmation_FundsConfirmationId` |  |  |  |
| 2 | `UKFC.ACCOUNT.NUMBER` | `UkobpxFundsConfirmation_AccountNumber` | TField |  | Field used for storing the Account Number. |
| 3 | `UKFC.FUNDS.AVAILABLE` | `UkobpxFundsConfirmation_FundsAvailable` |  |  |  |
| 4 | `UKFC.REFERENCE` | `UkobpxFundsConfirmation_Reference` |  |  |  |
| 5 | `UKFC.AMOUNT` | `UkobpxFundsConfirmation_Amount` |  |  |  |
| 6 | `UKFC.CURRENCY` | `UkobpxFundsConfirmation_Currency` |  |  |  |
| 7 | `UKFC.DEBTOR.ACC.SCHEME.NAME` | `UkobpxFundsConfirmation_DebtorAccSchemeName` | TField |  | Field used for storing the Currency. |
| 8 | `UKFC.DEBTOR.ACC.IDENTIFICATION` | `UkobpxFundsConfirmation_DebtorAccIdentification` | TField |  | Field used for storing debtor account identification. |
| 9 | `UKFC.DEBTOR.ACC.NAME` | `UkobpxFundsConfirmation_DebtorAccName` | TField |  | Field for determining the debtor name. |
| 10 | `UKFC.DEBTOR.ACC.SEC.IDENTIFICATION` | `UkobpxFundsConfirmation_DebtorAccSecIdentification` | TField |  | Field used for storing secondary identification of debtor. |
| 11 | `UKFC.EXPIRATION.DATE.TIME` | `UkobpxFundsConfirmation_ExpirationDateTime` |  |  |  |
| 12 | `UKFC.RESERVED.1` | `UkobpxFundsConfirmation_Reserved1` | TField |  |  |
| 13 | `UKFC.RESERVED.2` | `UkobpxFundsConfirmation_Reserved2` | TField |  |  |
| 14 | `UKFC.RESERVED.3` | `UkobpxFundsConfirmation_Reserved3` | TField |  |  |
| 15 | `UKFC.RESERVED.4` | `UkobpxFundsConfirmation_Reserved4` | TField |  |  |
| 16 | `UKFC.RESERVED.5` | `UkobpxFundsConfirmation_Reserved5` | TField |  |  |
| 17 | `UKFC.RESERVED.6` | `UkobpxFundsConfirmation_Reserved6` | TField |  |  |
| 18 | `UKFC.RESERVED.7` | `UkobpxFundsConfirmation_Reserved7` | TField |  |  |
| 19 | `UKFC.RESERVED.8` | `UkobpxFundsConfirmation_Reserved8` | TField |  |  |
| 20 | `UKFC.RESERVED.9` | `UkobpxFundsConfirmation_Reserved9` | TField |  |  |
| 21 | `UKFC.RESERVED.10` | `UkobpxFundsConfirmation_Reserved10` | TField |  |  |
| 22 | `UKFC.OVERRIDE` | `UkobpxFundsConfirmation_Override` |  |  |  |
| 23 | `UKFC.LOCAL.REF` | `UkobpxFundsConfirmation_LocalRef` |  |  |  |
| 24 | `UKFC.RECORD.STATUS` | `UkobpxFundsConfirmation_RecordStatus` | String |  |  |
| 25 | `UKFC.CURR.NO` | `UkobpxFundsConfirmation_CurrNo` | String |  |  |
| 26 | `UKFC.INPUTTER` | `UkobpxFundsConfirmation_Inputter` |  |  |  |
| 27 | `UKFC.DATE.TIME` | `UkobpxFundsConfirmation_DateTime` |  |  |  |
| 28 | `UKFC.AUTHORISER` | `UkobpxFundsConfirmation_Authoriser` | String |  |  |
| 29 | `UKFC.CO.CODE` | `UkobpxFundsConfirmation_CoCode` | String |  |  |
| 30 | `UKFC.DEPT.CODE` | `UkobpxFundsConfirmation_DeptCode` | String |  |  |
| 31 | `UKFC.AUDITOR.CODE` | `UkobpxFundsConfirmation_AuditorCode` | String |  |  |
| 32 | `UKFC.AUDIT.DATE.TIME` | `UkobpxFundsConfirmation_AuditDateTime` | String |  |  |
