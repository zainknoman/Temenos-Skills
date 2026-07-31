# RE.CONSOL.SPEC.ENTRY — Table Schema

> Source: `INSERTS/I_F.RE.CONSOL.SPEC.ENTRY` in `AC_EntryCreation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RE.CSE.DEAL.NUMBER` | `ReConsolSpecEntry_DealNumber` | TField | Yes | Standard T24 alphanumeric field. Validation Rules: Mandatory presence. Either a standard transaction reference or a system created key. Examples such as: For a standard contract reference MM0512312345 or MMREVAL for a system revaluation or NET-R!AC.1.TR.GBP.1001.N.1..3300.US.2540.US.....50000.!DR!GBP!AC!381!20010615!!!1!!2!20010614!!1!1001 for systems where entries are consolidated (AC.CONSOLIDATE.COND) |
| 2 | `RE.CSE.COMPANY.CODE` | `ReConsolSpecEntry_CompanyCode` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 11 characters. Key to an entry on the COMPANY file. |
| 3 | `RE.CSE.AMOUNT.LCY` | `ReConsolSpecEntry_AmountLcy` | TField |  | Validation Rules: A maximum of 19 characters. |
| 4 | `RE.CSE.TRANSACTION.CODE` | `ReConsolSpecEntry_TransactionCode` | TField | Yes | Standard T24 alphanumeric field. Validation Rules: Mandatory presence. A maximum of 3 characters. Key to an entry on the RE.TXN.CODE file. |
| 5 | `RE.CSE.CONSOL.KEY.TYPE` | `ReConsolSpecEntry_ConsolKeyType` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 65 characters. |
| 6 | `RE.CSE.NARRATIVE` | `ReConsolSpecEntry_Narrative` |  |  |  |
| 7 | `RE.CSE.PL.CATEGORY` | `ReConsolSpecEntry_PlCategory` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 6 characters. |
| 8 | `RE.CSE.CUSTOMER.ID` | `ReConsolSpecEntry_CustomerId` | TField |  | Standard T24 customer field. Validation Rules: A maximum of 10. Key to a valid entry on the CUSTOMER file. |
| 9 | `RE.CSE.ACCOUNT.OFFICER` | `ReConsolSpecEntry_AccountOfficer` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 4 characters. |
| 10 | `RE.CSE.PRODUCT.CATEGORY` | `ReConsolSpecEntry_ProductCategory` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 6 characters. Key to an entry on the CATEGORY file. |
| 11 | `RE.CSE.VALUE.DATE` | `ReConsolSpecEntry_ValueDate` | TField |  | Standard T24 date field. Validation Rules: A maximum of 11 characters. |
| 12 | `RE.CSE.CURRENCY` | `ReConsolSpecEntry_Currency` | TField |  | Standard T24 currency field. Validation Rules: A maximum of 3 characters. Key to an entry on the CURRENCY file. |
| 13 | `RE.CSE.AMOUNT.FCY` | `ReConsolSpecEntry_AmountFcy` | TField |  | Validation Rules: A maximum of 19 characters. |
| 14 | `RE.CSE.EXCHANGE.RATE` | `ReConsolSpecEntry_ExchangeRate` | TField |  | Standard T24 rate field. Validation Rules: A maximum of 11 characters. |
| 15 | `RE.CSE.NEGOTIATED.REF.NUM` | `ReConsolSpecEntry_NegotiatedRefNum` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 5. |
| 16 | `RE.CSE.POSITION.TYPE` | `ReConsolSpecEntry_PositionType` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 2 characters. Key to an entry on the FX.POS.TYPE file. |
| 17 | `RE.CSE.OUR.REFERENCE` | `ReConsolSpecEntry_OurReference` | TField |  | Validation Rules: A maximum of 16 characters. |
| 18 | `RE.CSE.REVERSAL.MARKER` | `ReConsolSpecEntry_ReversalMarker` | TField |  | Validation Rules: A maximum of 1 characters. The following values are permitted: R or blank |
| 19 | `RE.CSE.EXPOSURE.DATE` | `ReConsolSpecEntry_ExposureDate` | TField |  | Standard T24 date field. Validation Rules: A maximum of 11 characters. |
| 20 | `RE.CSE.CURRENCY.MARKET` | `ReConsolSpecEntry_CurrencyMarket` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 1 characters. Key to an entry on the CURRENCY.MARKET file. |
| 21 | `RE.CSE.LOCAL.REF` | `ReConsolSpecEntry_LocalRef` |  |  |  |
| 22 | `RE.CSE.DEPARTMENT.CODE` | `ReConsolSpecEntry_DepartmentCode` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 4 characters. key to an entry on the DEPT.ACCT.OFFICER file. |
| 23 | `RE.CSE.TRANS.REFERENCE` | `ReConsolSpecEntry_TransReference` | TField |  | Validation Rules: A maximum of 25 characters. |
| 24 | `RE.CSE.SYSTEM.ID` | `ReConsolSpecEntry_SystemId` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 4 characters. Key to an entry on the EB.SYSTEM.ID file. |
| 25 | `RE.CSE.BOOKING.DATE` | `ReConsolSpecEntry_BookingDate` | TField |  | Standard T24 date field. Validation Rules: A maximum of 11 characters. |
| 26 | `RE.CSE.STMT.NO` | `ReConsolSpecEntry_StmtNo` |  |  |  |
| 27 | `RE.CSE.OVERRIDE` | `ReConsolSpecEntry_Override` |  |  |  |
| 28 | `RE.CSE.RECORD.STATUS` | `ReConsolSpecEntry_RecordStatus` | String |  | It's the Current status of the contract. Validation Rule: Valid Record Status Live table - No input field |
| 29 | `RE.CSE.CURR.NO` | `ReConsolSpecEntry_CurrNo` | String |  | It's the Curr number of the contract. Validation Rule: Numeric value Live table - No input field |
| 30 | `RE.CSE.INPUTTER` | `ReConsolSpecEntry_Inputter` |  |  |  |
| 31 | `RE.CSE.DATE.TIME` | `ReConsolSpecEntry_DateTime` |  |  |  |
| 32 | `RE.CSE.AUTHORISER` | `ReConsolSpecEntry_Authoriser` | String |  | It denotes the Authoriser of the contract. Validation Rule: Vaild user ID Live table - No input field |
| 33 | `RE.CSE.ORIG.LOCAL.EQUIV` | `ReConsolSpecEntry_OrigLocalEquiv` | TField |  | This field holds the local currency amount of the entry before EU conversion. Validation rule: Numeric Character (Standard Amount Field). Live Table. No Input. |
| 34 | `RE.CSE.AA.ITEM.REF` | `ReConsolSpecEntry_AaItemRef` | TField |  | Specifies the AA related reference value. Validation Rule: Alpha numeric. Live Table. No Input. |
| 35 | `RE.CSE.PROCESSING.DATE` | `ReConsolSpecEntry_ProcessingDate` | TField |  | Date on which the special entry will update the general ledger. Standard T24 date field. Validation Rules: A maximum of 11 characters. |
| 36 | `RE.CSE.RESERVED.10` | `ReConsolSpecEntry_Reserved10` | TField |  | Reserved field for future use. Validation Rule: Live table. No Input |
| 37 | `RE.CSE.RESERVED.9` | `ReConsolSpecEntry_Reserved9` | TField |  | Reserved field for future use. Validation Rule: Live table. No Input |
| 38 | `RE.CSE.RESERVED.8` | `ReConsolSpecEntry_Reserved8` | TField |  | Reserved field for future use. Validation Rule: Live table. No Input |
| 39 | `RE.CSE.RESERVED.7` | `ReConsolSpecEntry_Reserved7` | TField |  | Reserved field for future use. Validation Rule: Live table. No Input |
| 40 | `RE.CSE.RESERVED.6` | `ReConsolSpecEntry_Reserved6` | TField |  | Reserved field for future use. Validation Rule: Live table. No Input |
| 41 | `RE.CSE.RESERVED.5` | `ReConsolSpecEntry_Reserved5` | TField |  | Reserved field for future use. Validation Rule: Live table. No Input |
| 42 | `RE.CSE.RESERVED.4` | `ReConsolSpecEntry_Reserved4` | TField |  | Reserved field for future use. Validation Rule: Live table. No Input |
| 43 | `RE.CSE.RESERVED.3` | `ReConsolSpecEntry_Reserved3` | TField |  | Reserved field for future use. Validation Rule: Live table. No Input |
| 44 | `RE.CSE.RESERVED.2` | `ReConsolSpecEntry_Reserved2` | TField |  | Reserved field for future use. Validation Rule: Live table. No Input |
| 45 | `RE.CSE.RESERVED.1` | `ReConsolSpecEntry_Reserved1` | TField |  | Reserved field for future use. Validation Rule: Live table. No Input |
| 46 | `RE.CSE.ADD.DETAIL.NAME` | `ReConsolSpecEntry_AddDetailName` |  |  |  |
| 47 | `RE.CSE.ADD.DETAIL.VALUE` | `ReConsolSpecEntry_AddDetailValue` |  |  |  |
| 48 | `RE.CSE.SOFT.ACCTNG.DTLS` | `ReConsolSpecEntry_SoftAcctngDtls` | TField |  |  |
| 49 | `RE.CSE.NET.PARAM` | `ReConsolSpecEntry_NetParam` | TField |  | Holds the Netting parameter ID. Validation Rule: Alpha Numeric. Must be a record in AC.CONSOLIDATE.COND table. Live table. No Input |
| 50 | `RE.CSE.TDGL.DETAILS` | `ReConsolSpecEntry_TdglDetails` |  |  |  |
| 51 | `RE.CSE.BANK.SORT.CDE` | `ReConsolSpecEntry_ReCseBankSortCde` |  |  |  |
| 52 | `RE.CSE.CHEQUE.NUMBER` | `ReConsolSpecEntry_ReCseChequeNumber` |  |  |  |
| 53 | `RE.CSE.CHQ.COLL.ID` | `ReConsolSpecEntry_ReCseChqCollId` |  |  |  |
| 54 | `RE.CSE.CHQ.TYPE` | `ReConsolSpecEntry_ReCseChqType` |  |  |  |
| 55 | `RE.CSE.CONTRACT.BAL.ID` | `ReConsolSpecEntry_ReCseContractBalId` |  |  |  |
| 56 | `RE.CSE.BALANCE.TYPE` | `ReConsolSpecEntry_ReCseBalanceType` |  |  |  |
