# ACSWIT.ACCOUNT.SWITCH — Table Schema

> Source: `INSERTS/I_F.ACSWIT.ACCOUNT.SWITCH` in `ACSWIT_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACSWIT.ACC.ACCOUNT.NUMBER` | `AcswitAccountSwitch_AccountNumber` | TField | Yes | Captures transact account number for which switch out or switch in instruction is captured. Whether the t24account is switching in or out can be identified by SWITCH.INDICATOR field Validation Rules: Has to be a valid account record Mandatory field |
| 2 | `ACSWIT.ACC.NEW.IBAN` | `AcswitAccountSwitch_NewIban` | TField |  | Captures the IBAN of the account to which the customer wants to switch to Validation Rules: Has to be a valid IBAN record |
| 3 | `ACSWIT.ACC.NEW.ACCOUNT` | `AcswitAccountSwitch_NewAccount` | TField |  | Captures the new account number to which the customer wants to switch to. Incase of transact Account switchingin, this field and ACCOUNT.NUMBER field holds the same account. |
| 4 | `ACSWIT.ACC.NEW.BIC` | `AcswitAccountSwitch_NewBic` | TField |  | This field will store the BIC of the new bank to which the user is switching. Validation Rules: Has to be a valid BIC record |
| 5 | `ACSWIT.ACC.NEW.CLR.BANK.CODE` | `AcswitAccountSwitch_NewClrBankCode` | TField |  | Captures the new clearing bank code to which the user is switching |
| 6 | `ACSWIT.ACC.REQUEST.DATE` | `AcswitAccountSwitch_RequestDate` | TField |  | Field to hold the date on which the switching instruction is captured for the customer as requested by him. When the record is created and authorised manually, the field is auto populated with the current business date. When updating the record automatically from ACSWIT.SWITCH.DIRECTORY, the value in this field is mapped from itsCREATION.DATE field. |
| 7 | `ACSWIT.ACC.STATUS` | `AcswitAccountSwitch_Status` | TField |  | Field to indicate the status of the Switch. The status can be: Created - indicates that a switch directory is created but not activated Active - indicates an active instruction and is auto populated if an active switch directory exists Cancelled - indicates a cancelled instruction and is auto populated when Cancel Instruction is set as YES or whenthe instruction is Expired Expired - indicates an expired instruction when an active switch has reached or crossed the Expiry Date |
| 8 | `ACSWIT.ACC.CANCEL.INSTRUCTION` | `AcswitAccountSwitch_CancelInstruction` | TField |  | This field will give the user, the ability to cancel the switching process based on the request date and thevalidity parameterized. Validation Rules: It is a YES or NO field |
| 9 | `ACSWIT.ACC.CANCEL.DATE` | `AcswitAccountSwitch_CancelDate` | TField |  | Displays the date on which the instruction has been cancelled. It is updated with the current business date when the instruction is being authorised after the CancelInstruction field is set to Yes. Validation Rules: It is defaulted to today when CANCEL.INSTRUCTION is set as YES |
| 10 | `ACSWIT.ACC.EXPIRY.DATE` | `AcswitAccountSwitch_ExpiryDate` | TField |  | Field to hold the Expiry Date of the Account Switch. When the record is updated automatically from ACSWIT.SWITCH.DIRECTORY, the field is mapped with the ExpirationDate from the Directory table. When the record is created and authorised manually, the user can input Expiry Date or if the field is left blank,the system will derive the date based on the Effective Date and Validity Period (i.e Effective Date + ValidityPeriod (number. of days or months set up in ACSWIT.PARAMETER) |
| 11 | `ACSWIT.ACC.OLD.IBAN` | `AcswitAccountSwitch_OldIban` | TField |  | Record the IBAN of the account to which the customer wants to switch out. |
| 12 | `ACSWIT.ACC.OLD.BIC` | `AcswitAccountSwitch_OldBic` | TField |  | This field records the BIC of the old bank from which the user is switching. |
| 13 | `ACSWIT.ACC.EFFECTIVE.DATE` | `AcswitAccountSwitch_EffectiveDate` | TField |  | The workday on which the switch is to becomes active or became active. |
| 14 | `ACSWIT.ACC.ALERT.DATE` | `AcswitAccountSwitch_AlertDate` | TField |  | Date that an alert must be raised by the bank to inform the Bank's customer that his Bank Account Switch servicewill end on the Expiry Date. This Date is defaulted as EXPIRY.DATE �? Days defined in the Switch parameter(alert trigger) |
| 15 | `ACSWIT.ACC.ALERT.STATUS` | `AcswitAccountSwitch_AlertStatus` | TField |  | None(while creating record), Pending(on system reaching alert date), Sent(While alert is being sent). |
| 16 | `ACSWIT.ACC.LOCAL.REF` | `AcswitAccountSwitch_LocalRef` |  |  |  |
| 17 | `ACSWIT.ACC.OVERRIDE` | `AcswitAccountSwitch_Override` |  |  |  |
| 18 | `ACSWIT.ACC.RECORD.STATUS` | `AcswitAccountSwitch_RecordStatus` | String |  |  |
| 19 | `ACSWIT.ACC.CURR.NO` | `AcswitAccountSwitch_CurrNo` | String |  |  |
| 20 | `ACSWIT.ACC.INPUTTER` | `AcswitAccountSwitch_Inputter` |  |  |  |
| 21 | `ACSWIT.ACC.DATE.TIME` | `AcswitAccountSwitch_DateTime` |  |  |  |
| 22 | `ACSWIT.ACC.AUTHORISER` | `AcswitAccountSwitch_Authoriser` | String |  |  |
| 23 | `ACSWIT.ACC.CO.CODE` | `AcswitAccountSwitch_CoCode` | String |  |  |
| 24 | `ACSWIT.ACC.DEPT.CODE` | `AcswitAccountSwitch_DeptCode` | String |  |  |
| 25 | `ACSWIT.ACC.AUDITOR.CODE` | `AcswitAccountSwitch_AuditorCode` | String |  |  |
| 26 | `ACSWIT.ACC.AUDIT.DATE.TIME` | `AcswitAccountSwitch_AuditDateTime` | String |  |  |
| 27 | `ACSWIT.ACC.SWITCH.INDICATOR` | `AcswitAccountSwitch_SwitchIndicator` | TField |  | Flag to represent transact account is switching in or out. Validation Rules: If the Sync flag is either set as No or None in ACSWIT.PARAMETER, then user has to manually input the Indicatorflag Accepts the values "In"/"Out". Value IN indicates that the New IBAN Account is T24 bank's account Value OUT indicates that the Old IBAN Account is T24 bank's account |
