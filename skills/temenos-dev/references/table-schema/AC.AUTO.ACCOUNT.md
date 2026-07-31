# AC.AUTO.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.AC.AUTO.ACCOUNT` in `AC_AccountOpening.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.AUT.DESCRIPTION` | `AcAutoAccount_Description` | TField |  | AC.AUTO.ACCOUNT DESCRIPTION The Description fields describe the category for which parameters for automatic creation of sub-accounts are being set. Validation Rules: |
| 2 | `AC.AUT.NEW.NUMBER.RULE` | `AcAutoAccount_NewNumberRule` | TField |  | AC.AUTO.ACCOUNT NEW.NUMBER The NEW.NUMBER.RULE field indicates how the system should allocate the new account number for the sub-account. It can either contain the value NEXT, in which case the system will allocate the next id using the check digit rule defined in the COMPANY record, or the name of a routine that will return a new account number. Validation Rules: If not set to NEXT, the name of the subroutine to generate the next account number can be defined, the master account number will be set in the common variable COMI which will set the new account number on return from the routine |
| 3 | `AC.AUT.INHERITED.FIELD` | `AcAutoAccount_InheritedField` |  |  |  |
| 4 | `AC.AUT.FIELD.NAME` | `AcAutoAccount_FieldName` |  |  |  |
| 5 | `AC.AUT.FIELD.VALUE` | `AcAutoAccount_FieldValue` |  |  |  |
| 6 | `AC.AUT.CREATION.RTN` | `AcAutoAccount_CreationRtn` | S (subroutine) |  | AC.AUTO.ACCOUNT CREATION.RTN The CREATION.RTN field defines a routine to be called to perform any other operation associated with the creation of the sub account Validation Rules: must exist on PGM.FILE as type S (subroutine) program |
| 7 | `AC.AUT.EXCLUDE.SYS.ID` | `AcAutoAccount_ExcludeSysId` |  |  |  |
| 8 | `AC.AUT.EXCLUDE.TXN` | `AcAutoAccount_ExcludeTxn` |  |  |  |
| 9 | `AC.AUT.LOCAL.REF` | `AcAutoAccount_LocalRef` |  |  |  |
| 10 | `AC.AUT.INT.ACC.TYPE` | `AcAutoAccount_IntAccType` | TField |  | Determines the type of sub account key that is created for internal accounts. There are 2 options:- SUFFIX indicates that the suffix part of the key will be incremented by 1 for each sub account created. The SUFFIX can be defined as the 4 characters in positions 9 to 12 of the account key. If an account already exists for the key to be created then this number will be skipped. If the incremented number exceeds 9999 then it will be reset to 2. CATEG indicates that the CATEGORY part of the key will be incremented by 1 for each new sub account to be created. The CATEGORY can be defined as the 5 characters taking up positions 4 to 8. Again if an account already exists for the category to be created it number will be incremented. BUFFER option will be for future use. The reason for entering the CATEG option is that for some types of account the SUFFIX part of the key is significant, for example those accounts used in inter-company accounting, where the suffix in postions 9-12 indicates the company that is being posted to and therefore should not be changed. Sub accounts for the category defined in ACCOUNT.CLASS "INTERCO" must be set to use the CATEG option. The sub accounts created will retain the original category code of the master account in the account record. When intercompany accounting takes place sub account processing will take place if the master intercompany account being processed is set for sub account processing and it is locked by another user. |
| 11 | `AC.AUT.AA.INT.TXN.CNT` | `AcAutoAccount_AaIntTxnCnt` | TField |  | AC.AUTO.ACCOUNT Indicates whether the transaction count fields are updated on ACCT.ACTIVITY for internal accounts. Normally these fields are only used for charge calculations which do not affect internal accounts Validation rules YES indicates that transaction count fields are to be updated NO indicates that the transaction count fields are not updated |
| 12 | `AC.AUT.AA.INT.BAL.UPD` | `AcAutoAccount_AaIntBalUpd` | TField |  | AC.AUTO.ACCOUNT Indicates whether the balance fields are updated on ACCT.ACTIVITY for internal accounts. Normally these fields are only used for interest calculations which do not affect internal accounts Validation rules YES indicates that balance fields are to be updated NO indicates that the balance fields are not updated |
| 13 | `AC.AUT.USE.MAX.SUB.ACCT` | `AcAutoAccount_UseMaxSubAcct` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 14 | `AC.AUT.RESERVED.6` | `AcAutoAccount_Reserved6` |  |  |  |
| 15 | `AC.AUT.RESERVED.5` | `AcAutoAccount_Reserved5` |  |  |  |
| 16 | `AC.AUT.RESERVED.4` | `AcAutoAccount_Reserved4` | TField |  |  |
| 17 | `AC.AUT.RESERVED.3` | `AcAutoAccount_Reserved3` | TField |  |  |
| 18 | `AC.AUT.RESERVED.2` | `AcAutoAccount_Reserved2` | TField |  |  |
| 19 | `AC.AUT.RESERVED.1` | `AcAutoAccount_Reserved1` | TField |  |  |
| 20 | `AC.AUT.RECORD.STATUS` | `AcAutoAccount_RecordStatus` | String |  |  |
| 21 | `AC.AUT.CURR.NO` | `AcAutoAccount_CurrNo` | String |  |  |
| 22 | `AC.AUT.INPUTTER` | `AcAutoAccount_Inputter` |  |  |  |
| 23 | `AC.AUT.DATE.TIME` | `AcAutoAccount_DateTime` |  |  |  |
| 24 | `AC.AUT.AUTHORISER` | `AcAutoAccount_Authoriser` | String |  |  |
| 25 | `AC.AUT.CO.CODE` | `AcAutoAccount_CoCode` | String |  |  |
| 26 | `AC.AUT.DEPT.CODE` | `AcAutoAccount_DeptCode` | String |  |  |
| 27 | `AC.AUT.AUDITOR.CODE` | `AcAutoAccount_AuditorCode` | String |  |  |
| 28 | `AC.AUT.AUDIT.DATE.TIME` | `AcAutoAccount_AuditDateTime` | String |  |  |
