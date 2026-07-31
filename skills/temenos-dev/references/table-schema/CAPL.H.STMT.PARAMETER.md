# CAPL.H.STMT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CAPL.H.STMT.PARAMETER` in `CABASE_CustomerStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.STMT.PARM.FREQUENCY.TYPE` | `CaplHStmtParameter_FrequencyType` |  |  |  |
| 2 | `CAPL.STMT.PARM.FREQUENCY` | `CaplHStmtParameter_Frequency` |  |  |  |
| 3 | `CAPL.STMT.PARM.STMT.MESSAGE.ID` | `CaplHStmtParameter_StmtMessageId` | TField |  | This field is used to store the statement message id.Allowed input must be Valid DE.MESSAGE ID.E.g 950 |
| 4 | `CAPL.STMT.PARM.CLOSED.ACCOUNTS` | `CaplHStmtParameter_ClosedAccounts` | TField |  | This field is used to decide if the accounts that are closed in a specific statement period are to be shown as a part of the statement.Allowed inputs are Yes / No.If Yes closed account will be shown in statement.If No closed account will not be shown in statement. |
| 5 | `CAPL.STMT.PARM.PASSBOOK.STMT` | `CaplHStmtParameter_PassbookStmt` | TField |  | The purpose of the field is to decide if there are accounts with passbook, are to be considered for statements. Thisfield must be set to YES.Allowed values are Yes / No.If Yes should be considered.If No should not be considered. |
| 6 | `CAPL.STMT.PARM.RETAIN.STMT.PRD` | `CaplHStmtParameter_RetainStmtPrd` |  |  |  |
| 7 | `CAPL.STMT.PARM.PRODUCT.FILES` | `CaplHStmtParameter_ProductFiles` |  |  |  |
| 8 | `CAPL.STMT.PARM.NAME.ORDER.1` | `CaplHStmtParameter_NameOrder1` | TField |  | Field is used to define the name that must appear first in the statement.Valid ID from EB.ROLE table |
| 9 | `CAPL.STMT.PARM.NAME.ORDER.2` | `CaplHStmtParameter_NameOrder2` | TField |  | Field is used to define the name that must appear second in the statement.Valid ID from EB.ROLE table |
| 10 | `CAPL.STMT.PARM.ENQUIRY.REPORT` | `CaplHStmtParameter_EnquiryReport` | TField |  | This field is used to define the enquiry report ID that will contain the enquiry name to display the account statement details.Valid record from ENQUIRY.REPORT table. |
| 11 | `CAPL.STMT.PARM.COPY.COMMAND` | `CaplHStmtParameter_CopyCommand` | TField |  | The copy command in the current operating system. For e.g. in Windows it will be "DOS /c COPY" |
| 12 | `CAPL.STMT.PARM.SOURCE.DIR.PATH` | `CaplHStmtParameter_SourceDirPath` |  |  |  |
| 13 | `CAPL.STMT.PARM.TARGET.DIR.PATH` | `CaplHStmtParameter_TargetDirPath` |  |  |  |
| 14 | `CAPL.STMT.PARM.MEMBER.STMT.FILE` | `CaplHStmtParameter_MemberStmtFile` |  |  |  |
| 15 | `CAPL.STMT.PARM.LOCAL.REF` | `CaplHStmtParameter_LocalRef` |  |  |  |
| 16 | `CAPL.STMT.PARM.DAYS.BF.MATY` | `CaplHStmtParameter_DaysBfMaty` | TField |  | This field holds the working days before maturity to display the message in statement.Free text field with max length of 2 numeric character. |
| 17 | `CAPL.STMT.PARM.VALID.ACTIVITY` | `CaplHStmtParameter_ValidActivity` |  |  |  |
| 18 | `CAPL.STMT.PARM.STMT.SORT` | `CaplHStmtParameter_StmtSort` | TField |  | Purpose of the field to define the sorting option of the transactions in Customer Statements. Applicable values- Booking date- Value dateBased on the values defined, sorting of transactions are made.Booking date - ordered by booking date.Value date - ordered by Value date. |
| 19 | `CAPL.STMT.PARM.LENDING.BAL.FMT` | `CaplHStmtParameter_LendingBalFmt` | TField |  | This field is used to display the balance type to be displayed as per the value mentioned. Format.Possible values are:ABS - Report lending balances as absolute values.ACTUAL -Report loan outstanding with Negative sign as T24, Report UNC with Positive sign as T24.CONVERTED - Reports lending balances as T24 Balances Multiplied by -1, hence outstanding balances will be reported as Absolute (With no sign), and UNC with Negative sign. |
| 20 | `CAPL.STMT.PARM.ESC.BAL.TYPE` | `CaplHStmtParameter_EscBalType` |  |  |  |
| 21 | `CAPL.STMT.PARM.ESC.INT.TXN.CDE` | `CaplHStmtParameter_EscIntTxnCde` |  |  |  |
| 22 | `CAPL.STMT.PARM.ESC.MUN.TXN.CDE` | `CaplHStmtParameter_EscMunTxnCde` |  |  |  |
| 23 | `CAPL.STMT.PARM.SKIP.PAY.ACT` | `CaplHStmtParameter_SkipPayAct` |  |  |  |
| 24 | `CAPL.STMT.PARM.INT.RATE.CHG.ACT` | `CaplHStmtParameter_IntRateChgAct` |  |  |  |
| 25 | `CAPL.STMT.PARM.INT.ADJUST.ACT` | `CaplHStmtParameter_IntAdjustAct` |  |  |  |
| 26 | `CAPL.STMT.PARM.ESC.INT.TXN.PYMT` | `CaplHStmtParameter_EscIntTxnPymt` |  |  |  |
| 27 | `CAPL.STMT.PARM.CHG.EXC.BAL.TYPE` | `CaplHStmtParameter_ChgExcBalType` |  |  |  |
| 28 | `CAPL.STMT.PARM.ADDR.RTN` | `CaplHStmtParameter_AddrRtn` | TField |  | User can define their routine with the below argument condition Argument1 is input argument and will have the Customer Number. Argument2 is input argument and will have the Customer Name'@'DE.ADDRESS type. Aruguent3 is input argument and will have the Customer record. Aruguent4 is output argument and the this should have the address details in an array. |
| 29 | `CAPL.STMT.PARM.REPORT.CUST` | `CaplHStmtParameter_ReportCust` | TField |  | The purpose of the field is to display customer number as per the value mentionedPossible values are:ACCT.CUST/NONE- Account Customer will be displayed as customer numberOWNER.CONT-Displays the owner as customer number whose role is 'FIRST' |
| 30 | `CAPL.STMT.PARM.LEN.STMT.FORMAT` | `CaplHStmtParameter_LenStmtFormat` | TField |  | The field is used to specify the format used for generating lending statement entries.Possible values are:NONE - Multiple entry formatOLD - To display consolidated entries |
| 31 | `CAPL.STMT.PARM.EXC.DEP.ACTIVITY` | `CaplHStmtParameter_ExcDepActivity` |  |  |  |
| 32 | `CAPL.STMT.PARM.SNAP.STMT.TEXT` | `CaplHStmtParameter_SnapStmtText` |  |  |  |
| 33 | `CAPL.STMT.PARM.ACCT.LIST.OPTION` | `CaplHStmtParameter_AcctListOption` | TField |  | The field is used to specify the accounts to be fetched.Possible values are:MEMBERSHIP - accounts specific to membershipALL.ACCOUNTS - accounts of cif and cif attached as owner to membership |
| 34 | `CAPL.STMT.PARM.INCLUDE.CHARGE.TXN` | `CaplHStmtParameter_IncludeChargeTxn` | TField |  | The field is used to specify that whether we need to include the Lending Charge Property Class or notYES - Lending charge property class will be included for the Account StatementNO - Lending charge property class will not be included for the Account Statement |
| 35 | `CAPL.STMT.PARM.RESERVED.3` | `CaplHStmtParameter_Reserved3` | TField |  |  |
| 36 | `CAPL.STMT.PARM.RESERVED.2` | `CaplHStmtParameter_Reserved2` | TField |  |  |
| 37 | `CAPL.STMT.PARM.RESERVED.1` | `CaplHStmtParameter_Reserved1` | TField |  |  |
| 38 | `CAPL.STMT.PARM.OVERRIDE` | `CaplHStmtParameter_Override` |  |  |  |
| 39 | `CAPL.STMT.PARM.RECORD.STATUS` | `CaplHStmtParameter_RecordStatus` | String |  |  |
| 40 | `CAPL.STMT.PARM.CURR.NO` | `CaplHStmtParameter_CurrNo` | String |  |  |
| 41 | `CAPL.STMT.PARM.INPUTTER` | `CaplHStmtParameter_Inputter` |  |  |  |
| 42 | `CAPL.STMT.PARM.DATE.TIME` | `CaplHStmtParameter_DateTime` |  |  |  |
| 43 | `CAPL.STMT.PARM.AUTHORISER` | `CaplHStmtParameter_Authoriser` | String |  |  |
| 44 | `CAPL.STMT.PARM.CO.CODE` | `CaplHStmtParameter_CoCode` | String |  |  |
| 45 | `CAPL.STMT.PARM.DEPT.CODE` | `CaplHStmtParameter_DeptCode` | String |  |  |
| 46 | `CAPL.STMT.PARM.AUDITOR.CODE` | `CaplHStmtParameter_AuditorCode` | String |  |  |
| 47 | `CAPL.STMT.PARM.AUDIT.DATE.TIME` | `CaplHStmtParameter_AuditDateTime` | String |  |  |
