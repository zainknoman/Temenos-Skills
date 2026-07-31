# AC.XML.STMT.DATA — Table Schema

> Source: `INSERTS/I_F.AC.XML.STMT.DATA` in `IX_XmlStmtPrinting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IX.DATA.CUSTOMER.ID` | `AcXmlStmtData_CustomerId` | TField |  | CUSTOMER.ID The Customer Id of the Account for which CAMT is generated |
| 2 | `IX.DATA.ACCOUNT.IBAN` | `AcXmlStmtData_AccountIban` | TField |  | ACCOUNT.IBAN This field holds the IBAN id of the Account holder |
| 3 | `IX.DATA.ACCOUNT.NAME` | `AcXmlStmtData_AccountName` | TField |  | Account Name The Account title of the Account Holder |
| 4 | `IX.DATA.ACCOUNT.CURRENCY` | `AcXmlStmtData_AccountCurrency` | TField |  | ACCOUNT.CURRENCY The Currency of the Account |
| 5 | `IX.DATA.STMT.DATE` | `AcXmlStmtData_StmtDate` | TField |  | STMT.DATE The date of the Statement |
| 6 | `IX.DATA.STMT.FQU.TYPE` | `AcXmlStmtData_StmtFquType` | TField |  | STMT.FQU.TYPE The Frequency type of the Statement |
| 7 | `IX.DATA.LAST.STMT.NO` | `AcXmlStmtData_LastStmtNo` | TField |  | LAST.STMT.NO The Last Statement Number |
| 8 | `IX.DATA.OPEN.STMT.DATA` | `AcXmlStmtData_OpenStmtData` | TField |  |  |
| 9 | `IX.DATA.OPEN.STMT.BALANCE` | `AcXmlStmtData_OpenStmtBalance` | TField |  | OPEN.STMT.BALANCE The Opening Balance of the Statement, which will be the Closing balance of the previous statement |
| 10 | `IX.DATA.XML.STMT.TYPE` | `AcXmlStmtData_XmlStmtType` | TField |  | Type of XML Statement Value in this field can be CAMT052 or CAMT053 |
| 11 | `IX.DATA.CLOSING.CLEARED` | `AcXmlStmtData_ClosingCleared` | TField |  | CLOSING.CLEARED The Closing Cleared balance of the Statement |
| 12 | `IX.DATA.AVAILABLE.DATE` | `AcXmlStmtData_AvailableDate` |  |  |  |
| 13 | `IX.DATA.AVAILABLE.BALANCE` | `AcXmlStmtData_AvailableBalance` |  |  |  |
| 14 | `IX.DATA.LIMIT.AMOUNT` | `AcXmlStmtData_LimitAmount` | TField |  | LIMIT.AMOUNT The Available Limit amount at the time the Statement is being generated |
| 15 | `IX.DATA.STMT.PRINTED.ID` | `AcXmlStmtData_StmtPrintedId` | TField |  | STMT.PRINTED or STMT2.PRINTED id The link to the STMT.PRINTED/STMT2.PRINTED record |
| 16 | `IX.DATA.PERIOD.END.DATE` | `AcXmlStmtData_PeriodEndDate` | TField |  | Period End The Period end Date when the Statement is being generated |
| 17 | `IX.DATA.CO.CODE` | `AcXmlStmtData_CoCode` | String |  | CO.CODE The Company Code of the Account record |
| 18 | `IX.DATA.MESSAGE.STATUS` | `AcXmlStmtData_MessageStatus` | TField |  | Status of the CAMT message This field will be updated after the XML.TRANSFORMATION service Value can be "T24XML.GENERATED" or "CAMTXML.GENERATED" The value "CAMTXML.GENERATED" represents the successful generation of CAMT message |
| 19 | `IX.DATA.XML.MESSAGE` | `AcXmlStmtData_XmlMessage` |  |  |  |
| 20 | `IX.DATA.DE.STAT.REQ.ID` | `AcXmlStmtData_DeStatReqId` |  |  |  |
| 21 | `IX.DATA.HIST.ID` | `AcXmlStmtData_HistId` |  |  |  |
| 22 | `IX.DATA.CARRIER.ADDR.NO` | `AcXmlStmtData_CarrierAddrNo` |  |  |  |
| 23 | `IX.DATA.LANGUAGE` | `AcXmlStmtData_Language` |  |  |  |
| 24 | `IX.DATA.COPIES` | `AcXmlStmtData_Copies` |  |  |  |
| 25 | `IX.DATA.RECIPIENT.ID` | `AcXmlStmtData_RecipientId` |  |  |  |
| 26 | `IX.DATA.INVOKE.DELIVERY` | `AcXmlStmtData_InvokeDelivery` |  |  |  |
| 27 | `IX.DATA.RESERVED.4` | `AcXmlStmtData_Reserved4` |  |  |  |
| 28 | `IX.DATA.FWD.STMT.PRINTED` | `AcXmlStmtData_FwdStmtPrinted` | TField |  |  |
| 29 | `IX.DATA.STMT.NO` | `AcXmlStmtData_StmtNo` | TField |  |  |
| 30 | `IX.DATA.ONLINE.ACTUAL.BAL` | `AcXmlStmtData_OnlineActualBal` | TField |  |  |
| 31 | `IX.DATA.OTHER.DETAILS` | `AcXmlStmtData_OtherDetails` |  |  |  |
| 32 | `IX.DATA.AC.XML.STMT.ID` | `AcXmlStmtData_AcXmlStmtId` |  |  |  |
| 33 | `IX.DATA.CARRIER.ADDR` | `AcXmlStmtData_CarrierAddr` |  |  |  |
| 34 | `IX.DATA.LISTENER.ID` | `AcXmlStmtData_ListenerId` |  |  |  |
