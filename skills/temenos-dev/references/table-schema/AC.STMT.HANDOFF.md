# AC.STMT.HANDOFF — Table Schema

> Source: `INSERTS/I_F.AC.STMT.HANDOFF` in `AC_AccountStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.STH.CARRIER.ADDR.NO` | `AcStmtHandoff_CarrierAddrNo` |  |  |  |
| 2 | `AC.STH.LANGUAGE` | `AcStmtHandoff_Language` |  |  |  |
| 3 | `AC.STH.COPIES` | `AcStmtHandoff_Copies` |  |  |  |
| 4 | `AC.STH.CUSTOMER` | `AcStmtHandoff_Customer` | TField |  | Identifies the Customer to whom the Account belongs. For internal accounts this will be null. Validation Rules: 1-10 numeric character Customer Code. Internal file - this is a NOINPUT field. |
| 5 | `AC.STH.SECTOR.CODE` | `AcStmtHandoff_SectorCode` | TField |  | Identifies the Sector Code relating to the Customer who owns the account. Not present for Internal accounts. Validation Rules: 1-4 numeric character Sector Code. (Internal file, No input) |
| 6 | `AC.STH.COMPANY.CODE` | `AcStmtHandoff_CompanyCode` | TField |  | Identifies the company producing the statement. Validation Rules: Company Id: CCGGGLLLL where CC is alphabetic country code. GGG is numeric company code. LLLL is local code. (Internal file, No input.) |
| 7 | `AC.STH.ACCOUNT.OFFICER` | `AcStmtHandoff_AccountOfficer` | TField |  | Identifies the Account Officer responsible for the account. This will contain the first OTHER.OFFICER from the Account record if specified, otherwise the ACCOUNT.OFFICER will be used. Validation Rules: 1-4 numeric character Account Officer code. (Internal file, No input.) |
| 8 | `AC.STH.CURRENCY` | `AcStmtHandoff_Currency` | TField |  | Identifies the Currency of the account. Validation Rules: 3 type SSS (uppercase alpha) characters. Internal file - this is a NOINPUT field. |
| 9 | `AC.STH.ACCT.CATEGORY` | `AcStmtHandoff_AcctCategory` | TField |  | Indicates the Category Code for the account. Validation Rules: 4-5 numeric character Category Code. Internal file - this is a NOINPUT field. |
| 10 | `AC.STH.ACCT.LIMIT.REF` | `AcStmtHandoff_AcctLimitRef` | TField | No | If the customer has a Credit Limit covering this account, this field identifies the type of Limit applicable to the Account and forms part of the key to the Limit record containing Credit Limit details. This field is also used to indicate Nostro accounts. Validation Rules: 3-9 numeric characters consisting of a 3-7 digit Limit Reference code and optionally, a 2 digit sequence number separated by '.'. Or 'NOSTRO' to denote a Nostro Account. (Internal file, No input.) |
| 11 | `AC.STH.STATEMENT.NO` | `AcStmtHandoff_StatementNo` | TField |  | Identifies the number of the statement to be printed. Validation Rules: 1-6 numeric character Statement Number. Internal file - this is a NOINPUT field. |
| 12 | `AC.STH.OPENING.DATE` | `AcStmtHandoff_OpeningDate` | TField |  | Identifies the start date of the statement period. This date is the date of the last statement. If this is the first statement produced there will be no value. Validation Rules: 8 numeric character date. (Internal file, No input.) |
| 13 | `AC.STH.OPENING.BALANCE` | `AcStmtHandoff_OpeningBalance` | TField |  | Contains the balance at the start of the statement period. This is the same as the closing balance for the last statement for that account. Validation Rules: Standard amount format. (Internal file, No input.) |
| 14 | `AC.STH.DESCRIPTIVE.STMT` | `AcStmtHandoff_DescriptiveStmt` | TField |  | Specifies whether or not the statement should include any customer narrative entered at the time contracts etc. are input. This is taken from the ACCOUNT STATEMENT record of the account. Validation Rules: Y(es) or N(o) (Internal file, No input.) |
| 15 | `AC.STH.PRINT.ERROR` | `AcStmtHandoff_PrintError` |  |  |  |
| 16 | `AC.STH.STMT.FREQU` | `AcStmtHandoff_StmtFrequ` | TField |  | Identifies the frequency of the statement to be printed. This will be the frequency code from the appropriate Statement Frequency field from the Account Staement record. Validation Rules: 1-5 type SS (uppercase alpha or numeric, first character alpha) characters. (Internal file, No input.) |
| 17 | `AC.STH.ACCT.TITLE.2` | `AcStmtHandoff_AcctTitle2` | A (alphanumeric) |  | Continuation of Account Title 1. This will be taken from the ACCT.TITLE.2 field on the account record. The ACCT.TITLE.2 is only complete when more details are entered than can be entered in ACCT.TITLE.1. Validation Rules: Up to 35 type A (alphanumeric) characters. Indicates the Category Code for the account. Internal file - this is a NOINPUT field. |
| 18 | `AC.STH.CONDITION.GROUP` | `AcStmtHandoff_ConditionGroup` | TField |  | Indicates the group of Accounts to which this Account belongs for the purpose of specifying rules for the calculation of interest and charges. The group is determined automatically on the basis of Customer and Account details as specified in the Account General Condition table (ACCT.GEN.CONDITION). This will be taken from the CONDITION.GROUP field on the account record. Validation Rules: 2 numeric characters. (Internal file, No input.) |
| 19 | `AC.STH.SHORT.TITLE` | `AcStmtHandoff_ShortTitle` | A (alphanumeric) |  | Specifies the abbreviated title of the Account. This will be taken from the SHORT TITLE field on the account record. Validation Rules: Up to 35 type A (alphanumeric) characters. (Internal file, No input.) |
| 20 | `AC.STH.TO.DATE` | `AcStmtHandoff_ToDate` | TField |  | Indicates the end date for entries on the statement. In a VALUE.DATED system, this date will be set the PERIOD.END date in the DATES record, as the statement will only include entries with a value date less than or equal to this date. In a non-value dated system, the statement will only include entries with a BOOKING.DATE up to and including the system date, so the date is set to the system run date. Validation Rules: 8 numeric character date. Internal file - this is a NOINPUT field. |
| 21 | `AC.STH.LIMIT.AMOUNT` | `AcStmtHandoff_LimitAmount` | TField |  | Contains the allocated amount for the limit record linked to the account. The amount is taken as the ONLINE.LIMIT amount for the lowest level record defined in the limit structure on the date the statment was produced. The amount is converted from the limit currency to the account currency where required. Validation Rules: Amount field in the currency of the account |
| 22 | `AC.STH.LIMIT.AVAIL` | `AcStmtHandoff_LimitAvail` | TField |  | Contains the amount of the limit record available on the date of statement production, for use when the account is linked to a limit. The available amount is calculated as the ONLINE.LIMIT less the TOTAL.OS and the value of the account balances linked to the limit. The value is taken from the lowest level limit in the structure where an amount has been defined, and is converted to the account currency where the limit currency differs. Validation Rules: Standard Amount field in the currency of the account. |
| 23 | `AC.STH.PENDING.ID` | `AcStmtHandoff_PendingId` |  |  |  |
| 24 | `AC.STH.TOTAL.PENDING` | `AcStmtHandoff_TotalPending` |  |  |  |
| 25 | `AC.STH.RECORD.STATUS` | `AcStmtHandoff_RecordStatus` | String |  |  |
| 26 | `AC.STH.CURR.NO` | `AcStmtHandoff_CurrNo` | String |  |  |
| 27 | `AC.STH.INPUTTER` | `AcStmtHandoff_Inputter` |  |  |  |
| 28 | `AC.STH.DATE.TIME` | `AcStmtHandoff_DateTime` |  |  |  |
| 29 | `AC.STH.AUTHORISER` | `AcStmtHandoff_Authoriser` | String |  |  |
| 30 | `AC.STH.CO.CODE` | `AcStmtHandoff_CoCode` | String |  |  |
| 31 | `AC.STH.DEPT.CODE` | `AcStmtHandoff_DeptCode` | String |  |  |
| 32 | `AC.STH.AUDITOR.CODE` | `AcStmtHandoff_AuditorCode` | String |  |  |
| 33 | `AC.STH.AUDIT.DATE.TIME` | `AcStmtHandoff_AuditDateTime` | String |  |  |
| 34 | `AC.STH.PRINT.STMT.TYPE` | `AcStmtHandoff_PrintStmtType` | TField |  | Allows configuration of a specific Statement Type for the Product so that different Summary or Statement pages could be configured based on Product type Validation Rules: Must be a valid PRINT.STATEMENT record |
| 35 | `AC.STH.STMT.ADD.ON` | `AcStmtHandoff_StmtAddOn` |  |  |  |
| 36 | `AC.STH.DETAILED.STATEMENT` | `AcStmtHandoff_DetailedStatement` | TField |  | Indicates if the Produced Statement should include details of the movements or just the Summary Information Validation Rules: YES or NO |
| 37 | `AC.STH.LEAD.OR.PARTCIPANT` | `AcStmtHandoff_LeadOrPartcipant` | TField |  | Determines whether the Account is a lead or partcipant If field value is 'L' , then it is a Lead Account If field value is 'P', then it is a Partcipant Account |
| 38 | `AC.STH.PARTCIPANT.ACCOUNT` | `AcStmtHandoff_PartcipantAccount` |  |  |  |
| 39 | `AC.STH.CLOSED.PARTCIPANT` | `AcStmtHandoff_ClosedPartcipant` |  |  |  |
| 40 | `AC.STH.PRINT.ATTR.NAME` | `AcStmtHandoff_PrintAttrName` |  |  |  |
| 41 | `AC.STH.PRINT.ATTR.VALUE` | `AcStmtHandoff_PrintAttrValue` |  |  |  |
| 42 | `AC.STH.ADDITIONAL.STMT` | `AcStmtHandoff_AdditionalStmt` | TField |  |  |
