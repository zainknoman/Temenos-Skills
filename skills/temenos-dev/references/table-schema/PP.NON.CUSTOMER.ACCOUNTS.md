# PP.NON.CUSTOMER.ACCOUNTS — Table Schema

> Source: `INSERTS/I_F.PP.NON.CUSTOMER.ACCOUNTS` in `PP_DebitPartyDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPNCA.AccountType` | `PpNonCustomerAccounts_Accounttype` | TField |  | This field indicates the type of the account in the DDAFollowing are the types used in TPS. Possible Values: N: Nostro I: Internal Account PL: Profit And Loss Account |
| 2 | `PPNCA.DepartmentCode` | `PpNonCustomerAccounts_Departmentcode` | TField |  | It is the account officer of the account or the depart code to which the entry belongs toIt will be part of the posting line entry ( department code) to the general ledger and will be useful in reporting. |
| 3 | `PPNCA.Name1` | `PpNonCustomerAccounts_Name1` | TField | Yes | validation: Mandatory. Name 1 of the account. |
| 4 | `PPNCA.Name2` | `PpNonCustomerAccounts_Name2` | TField |  | Name 2 of the account. |
| 5 | `PPNCA.AddressLine1` | `PpNonCustomerAccounts_Addressline1` | TField | Yes | validation: Mandatory. Street name of the bank/branch owning the account ( Address line 1). |
| 6 | `PPNCA.AddressLine2` | `PpNonCustomerAccounts_Addressline2` | TField |  | Street name of the bank/branch owning the account ( Address line 2). |
| 7 | `PPNCA.Town` | `PpNonCustomerAccounts_Town` | TField |  | Town Country of the bank /branch owning the account. |
| 8 | `PPNCA.PostalCode` | `PpNonCustomerAccounts_Postalcode` | TField |  | Postal Code of the bank/branch owning the account. |
| 9 | `PPNCA.Country` | `PpNonCustomerAccounts_Country` | TField | Yes | validation: Mandatory. Country of the bank/branch owning the account. |
| 10 | `PPNCA.Residence` | `PpNonCustomerAccounts_Residence` | TField | Yes | validation: Mandatory. Residency of the account owner . It will be used within TPH while calculating client charges,It can contain any ISO country code (e.g. BE,GB etc.) |
| 11 | `PPNCA.Language` | `PpNonCustomerAccounts_Language` | TField | Yes | validation: Mandatory. Valid Entry in T24 Language table (LANGUAGE). |
| 12 | `PPNCA.AccountDDASystem` | `PpNonCustomerAccounts_Accountddasystem` | TField | Yes | validation: Mandatory when core system is external or hybrid. This field indicates the system where the DDA of the account is located. |
| 13 | `PPNCA.RESERVED.10` | `PpNonCustomerAccounts_Reserved10` |  |  |  |
| 14 | `PPNCA.RESERVED.9` | `PpNonCustomerAccounts_Reserved9` | TField |  | Standard T24 String. No Input Field |
| 15 | `PPNCA.RESERVED.8` | `PpNonCustomerAccounts_Reserved8` | TField |  | Standard T24 String. No Input Field |
| 16 | `PPNCA.RESERVED.7` | `PpNonCustomerAccounts_Reserved7` | TField |  | Standard T24 String. No Input Field |
| 17 | `PPNCA.RESERVED.6` | `PpNonCustomerAccounts_Reserved6` | TField |  | Standard T24 String. No Input Field |
| 18 | `PPNCA.RESERVED.5` | `PpNonCustomerAccounts_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 19 | `PPNCA.RESERVED.4` | `PpNonCustomerAccounts_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 20 | `PPNCA.RESERVED.3` | `PpNonCustomerAccounts_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 21 | `PPNCA.RESERVED.2` | `PpNonCustomerAccounts_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 22 | `PPNCA.RESERVED.1` | `PpNonCustomerAccounts_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 23 | `PPNCA.LOCAL.REF` | `PpNonCustomerAccounts_LocalRef` |  |  |  |
| 24 | `PPNCA.OVERRIDE` | `PpNonCustomerAccounts_Override` |  |  |  |
| 25 | `PPNCA.RECORD.STATUS` | `PpNonCustomerAccounts_RecordStatus` | String |  |  |
| 26 | `PPNCA.CURR.NO` | `PpNonCustomerAccounts_CurrNo` | String |  |  |
| 27 | `PPNCA.INPUTTER` | `PpNonCustomerAccounts_Inputter` |  |  |  |
| 28 | `PPNCA.DATE.TIME` | `PpNonCustomerAccounts_DateTime` |  |  |  |
| 29 | `PPNCA.AUTHORISER` | `PpNonCustomerAccounts_Authoriser` | String |  |  |
| 30 | `PPNCA.CO.CODE` | `PpNonCustomerAccounts_CoCode` | String |  |  |
| 31 | `PPNCA.DEPT.CODE` | `PpNonCustomerAccounts_DeptCode` | String |  |  |
| 32 | `PPNCA.AUDITOR.CODE` | `PpNonCustomerAccounts_AuditorCode` | String |  |  |
| 33 | `PPNCA.AUDIT.DATE.TIME` | `PpNonCustomerAccounts_AuditDateTime` | String |  |  |
