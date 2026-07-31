# IN.IBAN.STRUCTURE — Table Schema

> Source: `INSERTS/I_F.IN.IBAN.STRUCTURE` in `IN_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IN.IBAN.STR.TAG` | `InIbanStructure_Tag` | TField |  | A tag identifier. Validation Rules: Record Identifier : "IS" |
| 2 | `IN.IBAN.STR.MODIFICATION.FLAG` | `InIbanStructure_ModificationFlag` | TField |  | A flag which indicates whether there is a change in the record, since the last release of the IBAN structure file. Validation Rules: A - Addition since last IBAN structure file. D - Deletion since last IBAN structure file. U - Unchanged since last IBAN structure file. M - Modification since last IBAN structure file. E - Expired : Reserved for future use. |
| 3 | `IN.IBAN.STR.IBAN.COUNTRY.CODE` | `InIbanStructure_IbanCountryCode` | TField |  | Specifies the ISO Country code prefix in IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 4 | `IN.IBAN.STR.IB.COUNTRY.CDE.POS` | `InIbanStructure_IbCountryCdePos` | TField |  | Specifies the start position of country code in IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 5 | `IN.IBAN.STR.IB.COUNTRY.CDE.LEN` | `InIbanStructure_IbCountryCdeLen` | TField |  | Specifies the number of characters of country code in IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 6 | `IN.IBAN.STR.IB.CHK.DIGITS.POS` | `InIbanStructure_IbChkDigitsPos` | TField |  | Specifies the start position of check digit in IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 7 | `IN.IBAN.STR.IB.CHK.DIGITS.LEN` | `InIbanStructure_IbChkDigitsLen` | TField |  | Specifies the number of check digits in IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 8 | `IN.IBAN.STR.BNK.IDENTIFIER.POS` | `InIbanStructure_BnkIdentifierPos` | TField |  | Specifies the start position of Bank identifier in IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 9 | `IN.IBAN.STR.BNK.IDENTIFIER.LEN` | `InIbanStructure_BnkIdentifierLen` | TField |  | Specifies the number of characters of bank identifier in IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 10 | `IN.IBAN.STR.BR.IDENTIFIER.POS` | `InIbanStructure_BrIdentifierPos` | TField |  | Specifies the start position of branch identifier in IBAN (value will be nil if the branch identifier is not applied in the country's IBAN format). Validation Rules: A maximum of 35 characters can be entered. |
| 11 | `IN.IBAN.STR.BR.IDENTIFIER.LEN` | `InIbanStructure_BrIdentifierLen` | TField |  | Specifies the number of characters of branch identifier in IBAN (value will be 0 if the branch identifier is not applied in the country's IBAN format) Validation Rules: A maximum of 35 characters can be entered. |
| 12 | `IN.IBAN.STR.IB.NATIONAL.ID.LEN` | `InIbanStructure_IbNationalIdLen` | TField |  | Specifies the number of significant characters of National ID value that are used by SWIFT, to populate the IBAN NATIONAL ID, and that are sufficient to derive the IBAN BIC correctly. This number can be different from (that is, smaller than) the length of national bank/branch identifier that is defined in IBAN Registry. Validation Rules: A maximum of 35 characters can be entered. |
| 13 | `IN.IBAN.STR.AC.NUMBER.POS` | `InIbanStructure_AcNumberPos` | TField |  | Specifies the start position of domestic account number in IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 14 | `IN.IBAN.STR.AC.NUMBER.LEN` | `InIbanStructure_AcNumberLen` | TField |  | Specifies the number of characters of account number in IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 15 | `IN.IBAN.STR.IBAN.TOTAL.LEN` | `InIbanStructure_IbanTotalLen` | TField |  |  |
| 16 | `IN.IBAN.STR.BANK.ID.APPL` | `InIbanStructure_BankIdAppl` | TField |  | Specifies the application in which the bank identifier can be fetched to build IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 17 | `IN.IBAN.STR.BANK.ID.FIELD` | `InIbanStructure_BankIdField` | TField |  | Specifies the field of the above application, from where bank identifier can be fetched to build IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 18 | `IN.IBAN.STR.BRANCH.ID.APPL` | `InIbanStructure_BranchIdAppl` | TField |  | Specifies the application in which branch identifier can be fetched to build IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 19 | `IN.IBAN.STR.BRANCH.ID.FIELD` | `InIbanStructure_BranchIdField` | TField |  | Specifies the field of the above application, from where branch identifier can be fetched to build IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 20 | `IN.IBAN.STR.ACCT.NO.APPL` | `InIbanStructure_AcctNoAppl` | TField |  | Specifies the application in which account number can be fetched to build IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 21 | `IN.IBAN.STR.ACCT.NO.FIELD` | `InIbanStructure_AcctNoField` | TField |  | Specifies the field of the above application, from where account number can be fetched to build IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 22 | `IN.IBAN.STR.SEPA` | `InIbanStructure_Sepa` | TField |  | This flag indicates whether the IBAN is used in one of the SEPA schemes. YES if it does, NO if it does not Validation Rules: 3 Alpha characters |
| 23 | `IN.IBAN.STR.OPT.COMMENCE.DATE` | `InIbanStructure_OptCommenceDate` | TField | No | The date from which the IBAN structure is an optional requirement. Validation Rules: Valid Date |
| 24 | `IN.IBAN.STR.MAND.COMMENCE.DATE` | `InIbanStructure_MandCommenceDate` | TField | Conditional | The date from which the IBAN structure is a mandatory requirement. If no date is supplied/specified, the use of IBAN in the respective country is optional. Validation Rules: Valid Date |
| 25 | `IN.IBAN.STR.OTHER.COMP.POS` | `InIbanStructure_OtherCompPos` |  |  |  |
| 26 | `IN.IBAN.STR.OTHER.COMP.LEN` | `InIbanStructure_OtherCompLen` |  |  |  |
| 27 | `IN.IBAN.STR.LOC.IBAN.GEN.RTN` | `InIbanStructure_LocIbanGenRtn` | TField |  |  |
| 28 | `IN.IBAN.STR.LOC.IBAN.VAL.RTN` | `InIbanStructure_LocIbanValRtn` | TField |  |  |
| 29 | `IN.IBAN.STR.LOCAL.REF` | `InIbanStructure_LocalRef` |  |  |  |
| 30 | `IN.IBAN.STR.RESERVED.12` | `InIbanStructure_Reserved12` |  |  |  |
| 31 | `IN.IBAN.STR.RESERVED.11` | `InIbanStructure_Reserved11` |  |  |  |
| 32 | `IN.IBAN.STR.RESERVED.10` | `InIbanStructure_Reserved10` |  |  |  |
| 33 | `IN.IBAN.STR.RESERVED.9` | `InIbanStructure_Reserved9` |  |  |  |
| 34 | `IN.IBAN.STR.RESERVED.8` | `InIbanStructure_Reserved8` |  |  |  |
| 35 | `IN.IBAN.STR.RESERVED.7` | `InIbanStructure_Reserved7` |  |  |  |
| 36 | `IN.IBAN.STR.RESERVED.6` | `InIbanStructure_Reserved6` |  |  |  |
| 37 | `IN.IBAN.STR.RESERVED.5` | `InIbanStructure_Reserved5` |  |  |  |
| 38 | `IN.IBAN.STR.RESERVED.4` | `InIbanStructure_Reserved4` |  |  |  |
| 39 | `IN.IBAN.STR.RESERVED.3` | `InIbanStructure_Reserved3` |  |  |  |
| 40 | `IN.IBAN.STR.RESERVED.2` | `InIbanStructure_Reserved2` | TField |  |  |
| 41 | `IN.IBAN.STR.OVERRIDE` | `InIbanStructure_Override` |  |  |  |
| 42 | `IN.IBAN.STR.RECORD.STATUS` | `InIbanStructure_RecordStatus` | String |  |  |
| 43 | `IN.IBAN.STR.CURR.NO` | `InIbanStructure_CurrNo` | String |  |  |
| 44 | `IN.IBAN.STR.INPUTTER` | `InIbanStructure_Inputter` |  |  |  |
| 45 | `IN.IBAN.STR.DATE.TIME` | `InIbanStructure_DateTime` |  |  |  |
| 46 | `IN.IBAN.STR.AUTHORISER` | `InIbanStructure_Authoriser` | String |  |  |
| 47 | `IN.IBAN.STR.CO.CODE` | `InIbanStructure_CoCode` | String |  |  |
| 48 | `IN.IBAN.STR.DEPT.CODE` | `InIbanStructure_DeptCode` | String |  |  |
| 49 | `IN.IBAN.STR.AUDITOR.CODE` | `InIbanStructure_AuditorCode` | String |  |  |
| 50 | `IN.IBAN.STR.AUDIT.DATE.TIME` | `InIbanStructure_AuditDateTime` | String |  |  |
