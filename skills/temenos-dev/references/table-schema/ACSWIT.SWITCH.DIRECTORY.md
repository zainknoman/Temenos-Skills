# ACSWIT.SWITCH.DIRECTORY — Table Schema

> Source: `INSERTS/I_F.ACSWIT.SWITCH.DIRECTORY` in `ACSWIT_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACSWIT.DIR.OLD.BIC` | `AcswitSwitchDirectory_OldBic` | TField |  | This field records the BIC of the old bank from which the user is switching. |
| 2 | `ACSWIT.DIR.NEW.IBAN` | `AcswitSwitchDirectory_NewIban` | TField | Yes | Record the IBAN of the account to which the customer wants to switch to. Mandatory field |
| 3 | `ACSWIT.DIR.NEW.BIC` | `AcswitSwitchDirectory_NewBic` | TField | Yes | This field record the BIC of the new bank to which the user is switching. Mandatory field |
| 4 | `ACSWIT.DIR.DATE.EFFECTIVE` | `AcswitSwitchDirectory_DateEffective` | TField |  | The field denotes the working day on which the switch will become active or has already become active. |
| 5 | `ACSWIT.DIR.EXPIRATION.DATE` | `AcswitSwitchDirectory_ExpirationDate` | TField |  | This date represents the first workday on which the switch will not be active anymore. This field will hold the expiry date of when the Switch record will expire. This will usually be effective date + 13 months. |
| 6 | `ACSWIT.DIR.ACTIVE` | `AcswitSwitchDirectory_Active` | TField |  | The value in this field represents the status of the Switch Instruction. The field accepts the value "Active" or "Inactive" . If in the the OVST file, the active tag has a value 1, the interface logic updating this file must update thevalue in this field as "Active". If in the OVST file, the active tag has a value 2, the interface logic updating this field must update the valuein this field as "Inactive". |
| 7 | `ACSWIT.DIR.CREATION.DATE` | `AcswitSwitchDirectory_CreationDate` | TField |  | Date of creation of this instruction from the file |
| 8 | `ACSWIT.DIR.RESERVED.10` | `AcswitSwitchDirectory_Reserved10` | TField |  |  |
| 9 | `ACSWIT.DIR.RESERVED.9` | `AcswitSwitchDirectory_Reserved9` | TField |  |  |
| 10 | `ACSWIT.DIR.RESERVED.8` | `AcswitSwitchDirectory_Reserved8` | TField |  |  |
| 11 | `ACSWIT.DIR.RESERVED.7` | `AcswitSwitchDirectory_Reserved7` | TField |  |  |
| 12 | `ACSWIT.DIR.RESERVED.6` | `AcswitSwitchDirectory_Reserved6` | TField |  |  |
| 13 | `ACSWIT.DIR.RESERVED.5` | `AcswitSwitchDirectory_Reserved5` | TField |  |  |
| 14 | `ACSWIT.DIR.RESERVED.4` | `AcswitSwitchDirectory_Reserved4` | TField |  |  |
| 15 | `ACSWIT.DIR.RESERVED.3` | `AcswitSwitchDirectory_Reserved3` | TField |  |  |
| 16 | `ACSWIT.DIR.RESERVED.2` | `AcswitSwitchDirectory_Reserved2` | TField |  |  |
| 17 | `ACSWIT.DIR.RESERVED.1` | `AcswitSwitchDirectory_Reserved1` | TField |  |  |
| 18 | `ACSWIT.DIR.LOCAL.REF` | `AcswitSwitchDirectory_LocalRef` |  |  |  |
| 19 | `ACSWIT.DIR.OVERRIDE` | `AcswitSwitchDirectory_Override` |  |  |  |
| 20 | `ACSWIT.DIR.RECORD.STATUS` | `AcswitSwitchDirectory_RecordStatus` | String |  |  |
| 21 | `ACSWIT.DIR.CURR.NO` | `AcswitSwitchDirectory_CurrNo` | String |  |  |
| 22 | `ACSWIT.DIR.INPUTTER` | `AcswitSwitchDirectory_Inputter` |  |  |  |
| 23 | `ACSWIT.DIR.DATE.TIME` | `AcswitSwitchDirectory_DateTime` |  |  |  |
| 24 | `ACSWIT.DIR.AUTHORISER` | `AcswitSwitchDirectory_Authoriser` | String |  |  |
| 25 | `ACSWIT.DIR.CO.CODE` | `AcswitSwitchDirectory_CoCode` | String |  |  |
| 26 | `ACSWIT.DIR.DEPT.CODE` | `AcswitSwitchDirectory_DeptCode` | String |  |  |
| 27 | `ACSWIT.DIR.AUDITOR.CODE` | `AcswitSwitchDirectory_AuditorCode` | String |  |  |
| 28 | `ACSWIT.DIR.AUDIT.DATE.TIME` | `AcswitSwitchDirectory_AuditDateTime` | String |  |  |
