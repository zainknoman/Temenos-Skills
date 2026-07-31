# ACCOUNT.STATEMENT — Table Schema

> Source: `INSERTS/I_F.ACCOUNT.STATEMENT` in `AC_AccountStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.STA.STMT.FQU.1` | `AccountStatement_StmtFqu1` |  |  |  |
| 2 | `AC.STA.SPECIAL.STATEMENT` | `AccountStatement_SpecialStatement` |  |  |  |
| 3 | `AC.STA.IF.NO.MOVEMENT` | `AccountStatement_IfNoMovement` | TField | No | Specifies whether or not Cycle 1 Statements should be printed if there have been no movements over the Account since the last statement. If this field contains 'Y', statements will be produced on the dates specified, regardless of whether or not there have been any movements. If there are no movements since last Statement, a value of NO in this field will suppress statements unless the minimum period (specified in the field MIN.MONTHS.STMT in AC.STMT.PARAMETER) has been exceeded. If the field contains 'NO' and MIN.MONTHS.STMT value is NONE, statements will only be produced when the account moves in the period since the last statement. An account statement can be produced automtatically on the first Statement date to serve as confirmation of opening the account. The value of FIRST.STMT on AC.STMT.PARAMETER will determine whether the first statement is to be printed even when no movement has taken place. This field cannot be input if the account has a passbook. When Account Statement records are generated automatically on Account opening, this field is set to the value defined in AC.STMT.PARAMETER if present, otherwise the field is set to 'NO', but it can subsequently be amended manually if required. Note: This field has no effect on the production of Special Statements (see SPECIAL.STATEMENT). Validation Rules: Y(es) or N(o). (Optional input. Default is NO.) |
| 4 | `AC.STA.DESCRIPT.STATEMENT` | `AccountStatement_DescriptStatement` | TField | No | Specifies whether or not statements should include any Customer Narrative entered at the time contracts etc. are input. Some of the transaction processing systems within T24 include the facility to enter one or more lines of Customer Narrative, each 34 characters long. If this field contains 'Y', the Customer Narrative may be printed on Account Statements, in addition to the standard Transaction Narrative (possibly including a Reference) as defined in the TRANSACTION table and DE.TRANSLATION table. When Account Statement records are generated automatically on Account opening, this field is set to the value defined in AC.STMT.PARAMETER if present, otherwise the field is set to 'NO', but it can subsequently be amended manually if required. This field cannot be input if the account has a passbook. Note: (i) Details of format, address(es) and copies are specified within the Delivery system. (ii) If a single line of Customer Narrative is entered and it is not translatable (i.e. does not start with '::'), it is used for the Additional Narrative in SWIFT statements, regardless of whether this field contains 'Y' or 'NO'. If this field contains 'NO' the single line of Customer Narrative replaces the standard narrative for printing on Account Statements. Validation Rules: Y(es) or N(o). (Optional input. Default is NO.) |
| 5 | `AC.STA.INT.CLOSING.ADVICE` | `AccountStatement_IntClosingAdvice` | TField | No | Specifies whether or not an advice should be produced when interest and charges are applied. When Account Statement records are generated automatically on Account opening, this field is set to the value defined in AC.STMT.PARAMETER if present, otherwise the field is set to 'NO', but it can subsequently be amended manually if required. Note: Details of format, address(es) and copies are specified within the Delivery system. Validation Rules: Y(es) or N(o). (Optional input. Default is NO.) |
| 6 | `AC.STA.INTEREST.SCALE` | `AccountStatement_InterestScale` | TField | No | Specifies whether or not a detailed interest statement (scale) should be produced whenever interest is applied. When Account Statement records are generated automatically on Account opening, this field is set to the value defined in AC.STMT.PARAMETER if present, otherwise the field is set to 'NO', but it can subsequently be amended manually if required. Note: Details of format, address(es) and copies are specified within the Delivery system. Validation Rules: Y(es) or N(o). (Optional input. Default is NO.) |
| 7 | `AC.STA.TAX.ADVICE` | `AccountStatement_TaxAdvice` | TField | No | Reserved for future use. Once requirements for Tax Advices have been defined (a local requirement), this field will specify whether or not an advice should be produced. When Account Statement records are generated automatically on Account opening, this field is set to the value defined in AC.STMT.PARAMETER if present, otherwise the field is set to 'NO', but it can subsequently be amended manually if required. Note: (i) Requirements for Tax Advices must be defined as a local requirement. At present this field has no effect. (ii) Details of format, address(es) and copies must be specified within the Delivery system. Validation Rules: Y(es) or N(o). (Optional input. Default is NO.) |
| 8 | `AC.STA.CURRENCY` | `AccountStatement_Currency` | TField |  | Holds the currency of the account. Validation Rules: 3 alphabetic characters. This is a NOINPUT field. |
| 9 | `AC.STA.FQU1.LAST.DATE` | `AccountStatement_Fqu1LastDate` | TField |  | Holds the date when the last Cycle 1 statements was produced. Validation Rules: This is a NOINPUT field. |
| 10 | `AC.STA.FQU1.LAST.BALANCE` | `AccountStatement_Fqu1LastBalance` | TField |  | Holds the 'balance brought forward' from the last Cycle 1 statement OR the last balance on the passbook. Validation Rules: 19 Amount characters. This is a NOINPUT field. |
| 11 | `AC.STA.LAST.STATEMENT.NO` | `AccountStatement_LastStatementNo` | TField |  | Hold the last statement number for Cycle 1 Statements, sequentially allocated, produced. The Statement numbers for each cycle is independently maintained starting with 1 for the cycle. Validation Rules: 5 numeric characters. This is a NOINPUT field. |
| 12 | `AC.STA.SWIFT.STMT.TYPE` | `AccountStatement_SwiftStmtType` |  |  |  |
| 13 | `AC.STA.STMT.FQU.2` | `AccountStatement_StmtFqu2` |  |  |  |
| 14 | `AC.STA.FREQ.NO` | `AccountStatement_FreqNo` |  |  |  |
| 15 | `AC.STA.SPL.STMT.FQU2` | `AccountStatement_SplStmtFqu2` |  |  |  |
| 16 | `AC.STA.IF.NO.MVMT.FQU2` | `AccountStatement_IfNoMvmtFqu2` |  |  |  |
| 17 | `AC.STA.FQU2.LAST.DATE` | `AccountStatement_Fqu2LastDate` |  |  |  |
| 18 | `AC.STA.FQU2.LAST.BAL` | `AccountStatement_Fqu2LastBal` |  |  |  |
| 19 | `AC.STA.LAST.STMT2.NO` | `AccountStatement_LastStmt2No` |  |  |  |
| 20 | `AC.STA.SW.STMT2.TYP` | `AccountStatement_SwStmt2Typ` |  |  |  |
| 21 | `AC.STA.PASSBOOK.NEXTLINE` | `AccountStatement_PassbookNextline` | TField |  | Holds the next passbook page and line to print on. Validation Rules: 5 Alphanumeric characters in the format: PAGE.LINE e.g. 2.11 This is a NOINPUT field. |
| 22 | `AC.STA.STATEMENT.DATE` | `AccountStatement_StatementDate` |  |  |  |
| 23 | `AC.STA.DELIVERY.REF` | `AccountStatement_DeliveryRef` |  |  |  |
| 24 | `AC.STA.LOCAL.REF` | `AccountStatement_LocalRef` |  |  |  |
| 25 | `AC.STA.MESSAGE.TIME` | `AccountStatement_MessageTime` |  |  |  |
| 26 | `AC.STA.DR.FLOOR.LIMIT` | `AccountStatement_DrFloorLimit` | TField | No | Used in conjunction with the MT942 fields. This value is used for the floor limit indicator for the debit transaction on the Interim Transaction Report, and is used to exclude smaller entries from the message details. On this message when only one value is used, the floor limit applies to both debit and credit amounts. If left blank then a value of zero is used which means all entries are detailed. Where a value entered is 100,000 (for a USD Account) then only entries where the amount is greater than USD 100,000 (debit or credit) are detailed. Smaller entries are only included in the entry totals and count. Incase a value entered in this field as 100,000 (for a USD Account) and in next field (Cr.Floor.Limit) 500,000 is given, then only debit entries where the amount is grater than USD 100,000 &amp; credit entries greater than USD500,000 are detailed. Smaller entries are only included in the entry totals and count. Validation Rules: Optional Input Input allowed only MESSAGE.TYPE = 942 &amp; SEND.MSG.TYPE ="Y" or when XML.STMT.TYPE is CAMT052 -Otherwise input not allowed |
| 27 | `AC.STA.CR.FLOOR.LIMIT` | `AccountStatement_CrFloorLimit` | TField | No | Used in conjunction with the MT942 fields. This value is used for the floor limit indicator for the credit transaction on the Interim Transaction Report, and is used to exclude smaller entries from the message details. On this message when only one value is used in the DR.FLOOR.LIMIT, the floor limit applies to both debit and credit amounts. If left blank then a value of zero is used which means all entries are detailed. Incase a value entered in this field as 500,000 (for a USD Account) and in previous field (Dr.Floor.Limit) 100,000 is given, then only debit entries where the amount is grater than USD 100,000 &amp; credit entries greater than USD500,000 are detailed. Smaller entries are only included in the entry totals and count. Amount entered here should not be same as DR.FLOOR.LIMIT- ie In DR.FLOOR.LIMIT &amp; CR.FLOOR.LIMIT cannot be mentioned as 10000. Validation Rules: Optional Input Input allowed only when or when XML.STMT.TYPE is CAMT052 or MESSAGE.TYPE = 942 &amp; SEND.MSG.TYPE ="Y" -Otherwise input not allowed |
| 28 | `AC.STA.MESSAGE.TYPE` | `AccountStatement_MessageType` |  |  |  |
| 29 | `AC.STA.SEND.MSG.TYPE` | `AccountStatement_SendMsgType` |  |  |  |
| 30 | `AC.STA.LAST.MT942.STMT.NO` | `AccountStatement_LastMt942StmtNo` | TField |  | The statement number on the last MT942 message sent. This value is incremented on the generation of each MT942 and is reset to zero on the 31 December each year. The first new messages sent on or after 1st Janauary will begin with 1 as per the requirements on S.W.I.F.T. |
| 31 | `AC.STA.PRINT.STMT` | `AccountStatement_PrintStmt` | TField |  | Yes or Null indicates that the statements will be printed as normal. No indicates that statements will be bypassed. Validation Rules: Yes, No or Null. |
| 32 | `AC.STA.PASSBOOK.ID` | `AccountStatement_PassbookId` | TField |  | ACCOUNT. STATEMENT PASSBOOK. ID This field will take the Teller. Passbook. id or any other id as input by the user. The id of course should have been defined in Teller. Passbook application. By default the input in this field would be "System" unless input otherwise. Validation Rules: |
| 33 | `AC.STA.CONS.SB.PASSBOOK` | `AccountStatement_ConsSbPassbook` | TField |  | Specifies whether consolidation of entries must happen for a Passbook Savings Account. If the number of transactions during the day after last print in a Passbook Savings account exceeds the number specified in AC.STMT.PARAMETER in field SB.PB.CONS.MAX then the entries would be consolidated and printed as total of Debit and / or Credit entries in the Passbook. Validation Rules: Accepts only the Alpha "YES' or a NULL as a valid input. If input as "YES" consolidation of entries would happen. Input "YES" would be accepted only if the account category is a savings bank account as classified in table ACCOUNT.CLASS. The account should be a Passbook account as defined in the ACCOUNT table in field PASSBOOK as "Y". |
| 34 | `AC.STA.LAST.MT941.DATE` | `AccountStatement_LastMt941Date` | TField |  | Holds the date as reported in the last MT941 in field 62F. This field is updated only when a MT941 statements generated through inward MT920 processing. When MT941 generated through Inward processing of MT920, the Last date and balance details available here &amp; the last date and balance as available for frequency 1 are compared and whichever is earlier is taken for tag 60F (opening date &amp; opening balance) in MT941 and transaction done after the latest date is taken for processing. The Outward delivery reference related to this statement is available in the respective statement request. Validation Rules: Valid Date format. This is a NO INPUT field-Update by System. Applicable only for MT941 generated through inward MT920 processing. |
| 35 | `AC.STA.LAST.MT941.BAL` | `AccountStatement_LastMt941Bal` | TField |  | Holds the balance as reported in the last MT941 in field 62F for the date as available in the previous field. This field is updated only when a MT941 statements generated through inward MT920 processing. When MT941 generated through Inward processing of MT920, the Last date and balance details available here &amp; the last date and balance as available for frequency 1 are compared and whichever is earlier is taken for tag 60F (opening date &amp; opening balance) in MT941 and all transaction done after the latest statement date is taken for processing. Validation Rules: 19 Amount characters. This is a NOINPUT field. Applicable only for MT941 generated through inward MT920 processing. |
| 36 | `AC.STA.LAST.MT941.STMT.NO` | `AccountStatement_LastMt941StmtNo` | TField |  | The statement number on the last MT941 message sent. This value is incremented on the generation of each MT941. This field is updated only when a MT941 statements generated through inward MT920 processing. |
| 37 | `AC.STA.XML.STMT.TYPE` | `AccountStatement_XmlStmtType` |  |  |  |
| 38 | `AC.STA.CYCLE.NO` | `AccountStatement_CycleNo` |  |  |  |
| 39 | `AC.STA.NEW.STMT.NO` | `AccountStatement_NewStmtNo` |  |  |  |
| 40 | `AC.STA.RESERVED.7` | `AccountStatement_Reserved7` |  |  |  |
| 41 | `AC.STA.INTRA.EFFECTIVE.DATE` | `AccountStatement_IntraEffectiveDate` | TField |  |  |
| 42 | `AC.STA.MANAGED.BY.AA` | `AccountStatement_ManagedByAa` | TField | No | Field to indicate that the record is managed by AA arrangement and any change has to be triggered using an AA Activity. Updated by system when an arrangement has Statement property setup. Validation Rules: This is a NOINPUT field Optional values with YES or NULL |
| 43 | `AC.STA.LAST.INTRADAY.MESSAGE` | `AccountStatement_LastIntradayMessage` |  |  |  |
| 44 | `AC.STA.LAST.INTRADAY.PROCESSED` | `AccountStatement_LastIntradayProcessed` |  |  |  |
| 45 | `AC.STA.RESERVED.2` | `AccountStatement_Reserved2` | TField |  |  |
| 46 | `AC.STA.RESERVED.1` | `AccountStatement_Reserved1` | TField |  |  |
| 47 | `AC.STA.RESERVED.20` | `AccountStatement_Reserved20` | TField |  |  |
| 48 | `AC.STA.RESERVED.19` | `AccountStatement_Reserved19` | TField |  |  |
| 49 | `AC.STA.RESERVED.18` | `AccountStatement_Reserved18` | TField |  |  |
| 50 | `AC.STA.RESERVED.17` | `AccountStatement_Reserved17` | TField |  |  |
| 51 | `AC.STA.RESERVED.16` | `AccountStatement_Reserved16` | TField |  |  |
| 52 | `AC.STA.RESERVED.15` | `AccountStatement_Reserved15` | TField |  |  |
| 53 | `AC.STA.RESERVED.14` | `AccountStatement_Reserved14` | TField |  |  |
| 54 | `AC.STA.RESERVED.13` | `AccountStatement_Reserved13` | TField |  |  |
| 55 | `AC.STA.RESERVED.12` | `AccountStatement_Reserved12` | TField |  |  |
| 56 | `AC.STA.RESERVED.11` | `AccountStatement_Reserved11` | TField |  |  |
| 57 | `AC.STA.RESERVED.10` | `AccountStatement_Reserved10` | TField |  |  |
| 58 | `AC.STA.RESERVED.9` | `AccountStatement_Reserved9` | TField |  |  |
| 59 | `AC.STA.RESERVED.8` | `AccountStatement_Reserved8` | TField |  |  |
| 60 | `AC.STA.RESERVED.6` | `AccountStatement_Reserved6` | TField |  |  |
| 61 | `AC.STA.RESERVED.5` | `AccountStatement_Reserved5` | TField |  |  |
| 62 | `AC.STA.RESERVED.4` | `AccountStatement_Reserved4` | TField |  |  |
| 63 | `AC.STA.RESERVED.3` | `AccountStatement_Reserved3` | TField |  |  |
| 64 | `AC.STA.OVERRIDE` | `AccountStatement_Override` |  |  |  |
| 65 | `AC.STA.RECORD.STATUS` | `AccountStatement_RecordStatus` | String |  |  |
| 66 | `AC.STA.CURR.NO` | `AccountStatement_CurrNo` | String |  |  |
| 67 | `AC.STA.INPUTTER` | `AccountStatement_Inputter` |  |  |  |
| 68 | `AC.STA.DATE.TIME` | `AccountStatement_DateTime` |  |  |  |
| 69 | `AC.STA.AUTHORISER` | `AccountStatement_Authoriser` | String |  |  |
| 70 | `AC.STA.CO.CODE` | `AccountStatement_CoCode` | String |  |  |
| 71 | `AC.STA.DEPT.CODE` | `AccountStatement_DeptCode` | String |  |  |
| 72 | `AC.STA.AUDITOR.CODE` | `AccountStatement_AuditorCode` | String |  |  |
| 73 | `AC.STA.AUDIT.DATE.TIME` | `AccountStatement_AuditDateTime` | String |  |  |
| 74 | `AC.STA.FOLLOW.SPECIAL` | `AccountStatement_FollowSpecial` | TField | No | Indicator to follow only Special statement dates and ignore Frequency 1 Validation Rules: YES or NO (Optional input) If set to YES, then StmtFqu1 cannot be multivalued. And When StmtFqu1 date is less than all the SpecialStatement Dates then the StmtFqu1 is updated with the Greatest SpecialStatement Date cycled with StmtFqu1 field frequency |
| 75 | `AC.STA.FQU1.IF.NO.SPECIAL` | `AccountStatement_Fqu1IfNoSpecial` | TField | No | Indicator to follow the If No movement for Special statement dates in Frequency 1 set Validation Rules: YES, NO or NO.IF.0.BALANCE (Optional input) |
| 76 | `AC.STA.FQU1.PRINT.STMT.TYPE` | `AccountStatement_Fqu1PrintStmtType` | TField |  | Allows configuration of a specific Statement Type for the Product. So that different Summary or Statement pages could be configured based on Product type in Frequency 1 set Validation Rules: Must be a valid PRINT.STATEMENT record |
| 77 | `AC.STA.FQU1.STMT.ADD.ON` | `AccountStatement_Fqu1StmtAddOn` |  |  |  |
| 78 | `AC.STA.FQU1.DETAILED.STATEMENT` | `AccountStatement_Fqu1DetailedStmt` |  |  |  |
| 79 | `AC.STA.FQU1.LEAD.ACCOUNT` | `AccountStatement_Fqu1LeadAccount` | TField |  | Holds the reference to the Lead Account of a Combined Statement in Frequency 1 set When a Combined Statement is defined and committed, the system would synchronise the Statement frequency of the Participant accounts with that of the Lead Account. Along with that, it will also update this attribute with the Lead Account reference Validation Rules: Must be a valid Account record. This field is inputtable for only AA |
| 80 | `AC.STA.FQU1.PARTCIPANT.ACCOUNT` | `AccountStatement_Fqu1PartcipantAccount` |  |  |  |
| 81 | `AC.STA.FQU1.CLOSED.PARTCIPANT` | `AccountStatement_Fqu1ClosedPartcipant` |  |  |  |
| 82 | `AC.STA.FQU1.PRINT.ATTR.NAME` | `AccountStatement_Fqu1PrintAttrName` |  |  |  |
| 83 | `AC.STA.FQU1.PRINT.ATTR.VALUE` | `AccountStatement_Fqu1PrintAttrValue` |  |  |  |
| 84 | `AC.STA.FQU2.IF.NO.SPECIAL` | `AccountStatement_Fqu2IfNoSpecial` |  |  |  |
| 85 | `AC.STA.FQU2.PRINT.STMT.TYPE` | `AccountStatement_Fqu2PrintStmtType` |  |  |  |
| 86 | `AC.STA.FQU2.STMT.ADD.ON` | `AccountStatement_Fqu2StmtAddOn` |  |  |  |
| 87 | `AC.STA.FQU2.DETAILED.STATEMENT` | `AccountStatement_Fqu2DetailedSummStmt` |  |  |  |
| 88 | `AC.STA.FQU2.LEAD.ACCOUNT` | `AccountStatement_Fqu2LeadAccount` |  |  |  |
| 89 | `AC.STA.FQU2.PARTCIPANT.ACCOUNT` | `AccountStatement_Fqu2PartcipantAccount` |  |  |  |
| 90 | `AC.STA.FQU2.CLOSED.PARTCIPANT` | `AccountStatement_Fqu2ClosedPartcipant` |  |  |  |
| 91 | `AC.STA.FQU2.PRINT.ATTR.NAME` | `AccountStatement_Fqu2PrintAttrName` |  |  |  |
| 92 | `AC.STA.FQU2.PRINT.ATTR.VALUE` | `AccountStatement_Fqu2PrintAttrValue` |  |  |  |
