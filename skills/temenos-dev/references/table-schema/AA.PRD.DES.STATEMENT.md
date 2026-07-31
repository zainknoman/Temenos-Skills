# AA.PRD.DES.STATEMENT — Table Schema

> Source: `INSERTS/I_F.AA.PRD.DES.STATEMENT` in `AA_Statement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.STMT.DESCRIPTION` | `AaPrdDesStatement_Description` |  |  |  |
| 2 | `AA.STMT.FULL.DESCRIPTION` | `AaPrdDesStatement_FullDescription` | TField |  | NEW Validation Rules: NEW |
| 3 | `AA.STMT.STMT.FQU.1` | `AaPrdDesStatement_StmtFqu1` |  |  |  |
| 4 | `AA.STMT.SPECIAL.STATEMENT` | `AaPrdDesStatement_SpecialStatement` |  |  |  |
| 5 | `AA.STMT.IF.NO.MOVEMENT` | `AaPrdDesStatement_IfNoMovement` | TField | No | Specifies whether or not Cycle1 Statements should be printed if there have been no movements over the Account since the last statement. If this field contains 'YES', statements will be produced on the dates specified, regardless of whether or not there have been any movements. If there are no movements since last Statement, a value of NO in this field will suppress statements unless the minimum period (specified in the field MIN.MONTHS.STMT in AC.STMT.PARAMETER) has been exceeded. If the field contains 'NO' and MIN.MONTHS.STMT value is NONE, statements will only be produced when the account moves in the period since the last statement. An account statement can be produced automtatically on the first Statement date to serve as confirmation of opening the account. The value of FIRST.STMT on AC.STMT.PARAMETER will determine whether the first statement is to be printed even when no movement has taken place. This field cannot be input if the account has a passbook. When Account Statement records are generated automatically on Account opening, this field is set to the value defined in AC.STMT.PARAMETER if present, otherwise the field is set to 'NO', but it can subsequently be amended manually if required. The option NO.IF.0.BALANCE is used to suppress if there are no balance movements Note: This field has no effect on the production of Special Statements (see SPECIAL.STATEMENT). Validation Rules: YES or NO or NO.IF.0.BALANCE. (Optional input. Default is NO.) |
| 6 | `AA.STMT.DESCRIPT.STATEMENT` | `AaPrdDesStatement_DescriptStatement` | TField | No | Specifies whether or not statements should include any Customer Narrative entered at the time contracts etc. are input. Some of the transaction processing systems within T24 include the facility to enter one or more lines of Customer Narrative, each 34 characters long. If this field contains 'Y', the Customer Narrative may be printed on Account Statements, in addition to the standard Transaction Narrative (possibly including a Reference) as defined in the TRANSACTION table and DE.TRANSLATION table. When Account Statement records are generated automatically on Account opening, this field is set to the value defined in AC.STMT.PARAMETER if present, otherwise the field is set to 'NO', but it can subsequently be amended manually if required. This field cannot be input if the account has a passbook. Note: (i) Details of format, address(es) and copies are specified within the Delivery system. (ii) If a single line of Customer Narrative is entered and it is not translatable (i.e. does not start with '::'), it is used for the Additional Narrative in SWIFT statements, regardless of whether this field contains 'Y' or 'NO'. If this field contains 'NO' the single line of Customer Narrative replaces the standard narrative for printing on Account Statements. Validation Rules: Y(es) or N(o). (Optional input. Default is NO.) |
| 7 | `AA.STMT.INT.CLOSING.ADVICE` | `AaPrdDesStatement_IntClosingAdvice` | TField | No | Specifies whether or not an advice should be produced when interest and charges are applied. When Account Statement records are generated automatically on Account opening, this field is set to the value defined in AC.STMT.PARAMETER if present, otherwise the field is set to 'NO', but it can subsequently be amended manually if required. Note: Details of format, address(es) and copies are specified within the Delivery system. Validation Rules: Y(es) or N(o). (Optional input. Default is NO.) |
| 8 | `AA.STMT.INTEREST.SCALE` | `AaPrdDesStatement_InterestScale` | TField | No | Specifies whether or not a detailed interest statement (scale) should be produced whenever interest is applied. When Account Statement records are generated automatically on Account opening, this field is set to the value defined in AC.STMT.PARAMETER if present, otherwise the field is set to 'NO', but it can subsequently be amended manually if required. Note: Details of format, address(es) and copies are specified within the Delivery system. Validation Rules: Y(es) or N(o). (Optional input. Default is NO.) |
| 9 | `AA.STMT.TAX.ADVICE` | `AaPrdDesStatement_TaxAdvice` | TField | No | Reserved for future use. Once requirements for Tax Advices have been defined (a local requirement), this field will specify whether or not an advice should be produced. When Account Statement records are generated automatically on Account opening, this field is set to the value defined in AC.STMT.PARAMETER if present, otherwise the field is set to 'NO', but it can subsequently be amended manually if required. Note: (i) Requirements for Tax Advices must be defined as a local requirement. At present this field has no effect. (ii) Details of format, address(es) and copies must be specified within the Delivery system. Validation Rules: Y(es) or N(o). (Optional input. Default is NO.) |
| 10 | `AA.STMT.SWIFT.STMT.TYPE` | `AaPrdDesStatement_SwiftStmtType` |  |  |  |
| 11 | `AA.STMT.STMT.FQU.2` | `AaPrdDesStatement_StmtFqu2` |  |  |  |
| 12 | `AA.STMT.FREQ.NO` | `AaPrdDesStatement_FreqNo` |  |  |  |
| 13 | `AA.STMT.SPL.STMT.FQU2` | `AaPrdDesStatement_SplStmtFqu2` |  |  |  |
| 14 | `AA.STMT.IF.NO.MVMT.FQU2` | `AaPrdDesStatement_IfNoMvmtFqu2` |  |  |  |
| 15 | `AA.STMT.SW.STMT2.TYP` | `AaPrdDesStatement_SwStmt2Typ` |  |  |  |
| 16 | `AA.STMT.MESSAGE.TIME` | `AaPrdDesStatement_MessageTime` |  |  |  |
| 17 | `AA.STMT.DR.FLOOR.LIMIT` | `AaPrdDesStatement_DrFloorLimit` | TField | No | Used in conjunction with the MT942 fields. This value is used for the floor limit indicator for the debit transaction on the Interim Transaction Report, and is used to exclude smaller entries from the message details. On this message when only one value is used, the floor limit applies to both debit and credit amounts. If left blank then a value of zero is used which means all entries are detailed. Where a value entered is 100,000 (for a USD Account) then only entries where the amount is greater than USD 100,000 (debit or credit) are detailed. Smaller entries are only included in the entry totals and count. Incase a value entered in this field as 100,000 (for a USD Account) and in next field (Cr.Floor.Limit) 500,000 is given, then only debit entries where the amount is grater than USD 100,000 &amp; credit entries greater than USD500,000 are detailed. Smaller entries are only included in the entry totals and count. Validation Rules: Optional Input Input allowed only MESSAGE.TYPE = 942 &amp; SEND.MSG.TYPE ="Y" or when XML.STMT.TYPE is CAMT052 -Otherwise input not allowed |
| 18 | `AA.STMT.CR.FLOOR.LIMIT` | `AaPrdDesStatement_CrFloorLimit` | TField | No | Used in conjunction with the MT942 fields. This value is used for the floor limit indicator for the credit transaction on the Interim Transaction Report, and is used to exclude smaller entries from the message details. On this message when only one value is used in the DR.FLOOR.LIMIT, the floor limit applies to both debit and credit amounts. If left blank then a value of zero is used which means all entries are detailed. Incase a value entered in this field as 500,000 (for a USD Account) and in previous field (Dr.Floor.Limit) 100,000 is given, then only debit entries where the amount is grater than USD 100,000 &amp; credit entries greater than USD500,000 are detailed. Smaller entries are only included in the entry totals and count. Amount entered here should not be same as DR.FLOOR.LIMIT- ie In DR.FLOOR.LIMIT &amp; CR.FLOOR.LIMIT cannot be mentioned as 10000. Validation Rules: Optional Input Input allowed only when or when XML.STMT.TYPE is CAMT052 or MESSAGE.TYPE = 942 &amp; SEND.MSG.TYPE ="Y" -Otherwise input not allowed |
| 19 | `AA.STMT.MESSAGE.TYPE` | `AaPrdDesStatement_MessageType` |  |  |  |
| 20 | `AA.STMT.SEND.MSG.TYPE` | `AaPrdDesStatement_SendMsgType` |  |  |  |
| 21 | `AA.STMT.PRINT.STMT` | `AaPrdDesStatement_PrintStmt` | TField |  | This field is inputtable only for Internal Accounts. Yes or Null indicates that the statements will be printed as normal. No indicates that statements will be bypassed. Validation Rules: Yes, No or Null. |
| 22 | `AA.STMT.CONS.SB.PASSBOOK` | `AaPrdDesStatement_ConsSbPassbook` | TField |  | Specifies whether consolidation of entries must happen for a Passbook Savings Account. If the number of transactions during the day after last print in a Passbook Savings account exceeds the number specified in AC.STMT.PARAMETER in field SB.PB.CONS.MAX then the entries would be consolidated and printed as total of Debit and / or Credit entries in the Passbook. Validation Rules: Accepts only the Alpha "YES' or a NULL as a valid input. If input as "YES" consolidation of entries would happen. Input "YES" would be accepted only if the account category is a savings bank account as classified in table ACCOUNT.CLASS. The account should be a Passbook account as defined in the ACCOUNT table in field PASSBOOK as "Y". |
| 23 | `AA.STMT.CYCLE.NO` | `AaPrdDesStatement_CycleNo` |  |  |  |
| 24 | `AA.STMT.NEW.STMT.NO` | `AaPrdDesStatement_NewStmtNo` |  |  |  |
| 25 | `AA.STMT.RESERVED.7` | `AaPrdDesStatement_Reserved7` |  |  |  |
| 26 | `AA.STMT.INTRA.EFFECTIVE.DATE` | `AaPrdDesStatement_IntraEffectiveDate` | TField |  |  |
| 27 | `AA.STMT.RATE.INFO.RTN` | `AaPrdDesStatement_RateInfoRtn` | A (alphanumeric) |  | Defines the Subroutine routine name to execute for converting the Interest rate.Up to 35 type A (alphanumeric) characters. Validation Rules: Must be a valid EB.API ID. |
| 28 | `AA.STMT.STMT.INFO.PROPERTY` | `AaPrdDesStatement_StmtInfoProperty` |  |  |  |
| 29 | `AA.STMT.INT.STMT.NAME` | `AaPrdDesStatement_IntStmtName` |  |  |  |
| 30 | `AA.STMT.INT.STMT.PROPERTY` | `AaPrdDesStatement_IntStmtProperty` |  |  |  |
| 31 | `AA.STMT.INT.STMT.FREQ` | `AaPrdDesStatement_IntStmtFreq` |  |  |  |
| 32 | `AA.STMT.RESERVED.6` | `AaPrdDesStatement_Reserved6` |  |  |  |
| 33 | `AA.STMT.RESERVED.5` | `AaPrdDesStatement_Reserved5` |  |  |  |
| 34 | `AA.STMT.RESERVED.4` | `AaPrdDesStatement_Reserved4` |  |  |  |
| 35 | `AA.STMT.RESERVED.3` | `AaPrdDesStatement_Reserved3` |  |  |  |
| 36 | `AA.STMT.RESERVED.2` | `AaPrdDesStatement_Reserved2` |  |  |  |
| 37 | `AA.STMT.RESERVED.1` | `AaPrdDesStatement_Reserved1` |  |  |  |
| 38 | `AA.STMT.LOCAL.REF` | `AaPrdDesStatement_LocalRef` |  |  |  |
| 39 | `AA.STMT.PR.ATTRIBUTE` | `AaPrdDesStatement_PrAttribute` |  |  |  |
| 40 | `AA.STMT.PR.VALUE` | `AaPrdDesStatement_PrValue` |  |  |  |
| 41 | `AA.STMT.PR.BRK.RES` | `AaPrdDesStatement_PrBrkRes` |  |  |  |
| 42 | `AA.STMT.PR.BRK.MSG` | `AaPrdDesStatement_PrBrkMsg` |  |  |  |
| 43 | `AA.STMT.PR.BRK.CHARGE` | `AaPrdDesStatement_PrBrkCharge` |  |  |  |
| 44 | `AA.STMT.PR.RESERVED.3` | `AaPrdDesStatement_PrReserved3` |  |  |  |
| 45 | `AA.STMT.PR.RESERVED.2` | `AaPrdDesStatement_PrReserved2` |  |  |  |
| 46 | `AA.STMT.PR.RESERVED.1` | `AaPrdDesStatement_PrReserved1` |  |  |  |
| 47 | `AA.STMT.PR.APP.METHOD` | `AaPrdDesStatement_PrAppMethod` |  |  |  |
| 48 | `AA.STMT.PR.APP.PERIOD` | `AaPrdDesStatement_PrAppPeriod` |  |  |  |
| 49 | `AA.STMT.SYS.RESERVE7` | `AaPrdDesStatement_SysReserve7` | TField |  |  |
| 50 | `AA.STMT.SYS.RESERVE6` | `AaPrdDesStatement_SysReserve6` | TField |  |  |
| 51 | `AA.STMT.OWNING.COMPANY` | `AaPrdDesStatement_OwningCompany` |  |  |  |
| 52 | `AA.STMT.SYS.RESERVE4` | `AaPrdDesStatement_SysReserve4` |  |  |  |
| 53 | `AA.STMT.SYS.RESERVE3` | `AaPrdDesStatement_SysReserve3` | TField |  | System field - reserved for future use |
| 54 | `AA.STMT.SYS.RESERVE2` | `AaPrdDesStatement_SysReserve2` | TField |  | System field - reserved for future use |
| 55 | `AA.STMT.SYS.RESERVE1` | `AaPrdDesStatement_SysReserve1` | TField |  | System field - reserved for future use |
| 56 | `AA.STMT.DEFAULT.ATTR.OPTION` | `AaPrdDesStatement_DefaultAttrOption` | TField | No | Optional field - Allowed Values are RESETTING and NON-RESETTING. RESETTING - During any Renewal Activities (for eg : change.product, rollover or reset) the property conditions will be reset from the product. NON-RESETTING - During any Renewal Activities property conditions will be maintained from the Arrangement level. Leaving the field blank sets NON-RESETTING as the default option. |
| 57 | `AA.STMT.DEFAULT.NEGOTIABLE` | `AaPrdDesStatement_DefaultNegotiable` | TField | Yes | Defines whether all attributes (fields) can be negotiable or not. This field is Mandatory Valid options are YES and NO |
| 58 | `AA.STMT.NR.ATTRIBUTE` | `AaPrdDesStatement_NrAttribute` |  |  |  |
| 59 | `AA.STMT.NR.OPTIONS` | `AaPrdDesStatement_NrOptions` |  |  |  |
| 60 | `AA.STMT.NR.RESERVED2` | `AaPrdDesStatement_NrReserved2` |  |  |  |
| 61 | `AA.STMT.NR.RESERVED1` | `AaPrdDesStatement_NrReserved1` |  |  |  |
| 62 | `AA.STMT.NR.STD.COMP` | `AaPrdDesStatement_NrStdComp` |  |  |  |
| 63 | `AA.STMT.NR.TYPE` | `AaPrdDesStatement_NrType` |  |  |  |
| 64 | `AA.STMT.NR.VALUE` | `AaPrdDesStatement_NrValue` |  |  |  |
| 65 | `AA.STMT.NR.MESSAGE` | `AaPrdDesStatement_NrMessage` |  |  |  |
| 66 | `AA.STMT.CHANGED.FIELDS` | `AaPrdDesStatement_ChangedFields` |  |  |  |
| 67 | `AA.STMT.NEGOTIATED.FLDS` | `AaPrdDesStatement_NegotiatedFlds` |  |  |  |
| 68 | `AA.STMT.ID.COMP.1` | `AaPrdDesStatement_IdComp1` | TField |  | Contains the arrangement number, extracted from the first component of the id Not applicable at product level System updated field no input allowed |
| 69 | `AA.STMT.ID.COMP.2` | `AaPrdDesStatement_IdComp2` | TField |  | The action that was triggered on the arrangement property The action is taken from ACTIVITY.CLASS record of the underlying AA.ARRANGEMENT.ACTIVITY request that caused the record to be modified. |
| 70 | `AA.STMT.ID.COMP.3` | `AaPrdDesStatement_IdComp3` | TField |  | Contains the effective date of the property condition Not applicable at product level System updated field no input allowed |
| 71 | `AA.STMT.ID.COMP.4` | `AaPrdDesStatement_IdComp4` | TField |  | Reserved for future use Not applicable at product level System field no input allowed |
| 72 | `AA.STMT.ID.COMP.5` | `AaPrdDesStatement_IdComp5` | TField |  | Reserved for future use Not applicable at product level System field no input allowed |
| 73 | `AA.STMT.ID.COMP.6` | `AaPrdDesStatement_IdComp6` | TField |  | Reserved for future use Not applicable at product level System field no input allowed |
| 74 | `AA.STMT.RESERVED2.ID` | `AaPrdDesStatement_Reserved2Id` | TField |  |  |
| 75 | `AA.STMT.TARGET.PRODUCT` | `AaPrdDesStatement_TargetProduct` | TField |  | This field denotes the target classic product of the given property class The already existing T24 products are mapped using AA infrastructure These are called classic products These products are mapped to different property clases |
| 76 | `AA.STMT.STMT.NOS` | `AaPrdDesStatement_StmtNos` |  |  |  |
| 77 | `AA.STMT.OVERRIDE` | `AaPrdDesStatement_Override` |  |  |  |
| 78 | `AA.STMT.RECORD.STATUS` | `AaPrdDesStatement_RecordStatus` | String |  |  |
| 79 | `AA.STMT.CURR.NO` | `AaPrdDesStatement_CurrNo` | String |  |  |
| 80 | `AA.STMT.INPUTTER` | `AaPrdDesStatement_Inputter` |  |  |  |
| 81 | `AA.STMT.DATE.TIME` | `AaPrdDesStatement_DateTime` |  |  |  |
| 82 | `AA.STMT.AUTHORISER` | `AaPrdDesStatement_Authoriser` | String |  |  |
| 83 | `AA.STMT.CO.CODE` | `AaPrdDesStatement_CoCode` | String |  |  |
| 84 | `AA.STMT.DEPT.CODE` | `AaPrdDesStatement_DeptCode` | String |  |  |
| 85 | `AA.STMT.AUDITOR.CODE` | `AaPrdDesStatement_AuditorCode` | String |  |  |
| 86 | `AA.STMT.AUDIT.DATE.TIME` | `AaPrdDesStatement_AuditDateTime` | String |  |  |
