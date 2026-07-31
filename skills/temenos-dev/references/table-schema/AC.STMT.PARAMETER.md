# AC.STMT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AC.STMT.PARAMETER` in `AC_AccountStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.STP.IF.NO.MOVEMENT` | `AcStmtParameter_IfNoMovement` | TField | Yes | Specifies the value for IF.NO.MOVEMENT in the default ACCOUNT.STATEMENT record for a newly opened account. Validation Rules: 'Y'(es),'N'(o) or NO.IF.0.BALANCE. Mandatory Input. |
| 2 | `AC.STP.DESCRIPT.STATEMENT` | `AcStmtParameter_DescriptStatement` | TField | Yes | Specifies the value for DESCRIPT.STATEMENT in the default ACCOUNT.STATEMENT record for a newly opened account. Validation Rules: 'Y'(es) or 'N'(o). Mandatory Input. |
| 3 | `AC.STP.INT.CLOSING.ADVICE` | `AcStmtParameter_IntClosingAdvice` | TField | Yes | Specifies the value for INT.CLOSING.ADVICE in the default ACCOUNT.STATEMENT record for a newly opened account. Validation Rules: 'Y'(es) or 'N'(o). Mandatory Input. |
| 4 | `AC.STP.INTEREST.SCALE` | `AcStmtParameter_InterestScale` | TField | Yes | Specifies the value for INTEREST.SCALE in the default ACCOUNT.STATEMENT record for a newly opened account. Validation Rules: 'Y'(es) or 'N'(o). Mandatory Input. |
| 5 | `AC.STP.TAX.ADVICE` | `AcStmtParameter_TaxAdvice` | TField | Yes | Specifies the value for TAX.ADVICE in the default ACCOUNT.STATEMENT record for a newly opened account. Validation Rules: 'Y'(es) or 'N'(o). Mandatory Input. |
| 6 | `AC.STP.MIN.MONTHS.STMT` | `AcStmtParameter_MinMonthsStmt` | TField |  | Specifies the value for MIN.MONTHS.STMT that controls the minimum frequency for statements to be produced in PRINT.ACCOUNT.STMT. The default of null is 6 months although you can specify no minimum frequency or any number of months between 1 and 9999. Validation Rules: NONE - No minimum frequency. 1-4 numeric characters. |
| 7 | `AC.STP.FIRST.STMT` | `AcStmtParameter_FirstStmt` | TField |  | Specifies whether a statement is required to be produced the first day if there has been no movements for the Account since being opened. Validation Rules: 1 alphabetic character. Y(es) or N(o). |
| 8 | `AC.STP.OTHER.OFFICER` | `AcStmtParameter_OtherOfficer` | TField | Yes | Specifies the value for deciding whether the alternative ACCOUNT.OFFICER will be printed in PRINT.ACCOUNT.STMT, if this field exists on the ACCOUNT record. Validation Rules: 'Y'(es) or 'NO' Mandatory input. Defaults to 'Y'es. |
| 9 | `AC.STP.FWD.MVMT.REQD` | `AcStmtParameter_FwdMvmtReqd` | TField |  | In a value dated accounting system (i.e. in ACCOUNT.PARAMETER, VALUE.DATED.ACCTING is YES) , if this field is Null or No, then real forward entries with a Value-Date equal to or less than the next statement date, booked during the statement period alone, will be reported in the statements. If it is desired that all the real forward entries irrespective of value date booked during the statement period, are to be printed in the next statement, then this field has to be made YES. Example: Last statement date-15.3.2002. Next Statement date-31.3.2002 Booking date- 16.3.2002-Value date-28.3.2002 Booking date- 20.3.2002-Value date-5.4.2002 If this field is NULL/NO then only the entry with value date 28.3.2002 will be reported in the next statement due on 31.3.2002. On the other hand if this field is YES then both the entries will be reported in the next statement due on 31.3.2002. Validation Rules: Allowed values NULL/NO/YES. Input allowed only when the field VALUE.DATED.ACCTING is YES in ACCOUNT.PARAMETER. NULL will not be allowed if this field already has the value NO/YES. |
| 10 | `AC.STP.SP.PB.CONS.MAX` | `AcStmtParameter_SpPbConsMax` | TField |  | Specifies the number of transactions after which Savings Bank Account entries are to be consolidated for Passbook printing. If the number of transactions during the day after last print in a Passbook Savings account exceeds the number specified in this field then the entries would be consolidated and printed as total of Debit and / or Credit entries. Validation Rules: Allows only a positive integer numeric value. |
| 11 | `AC.STP.PB.CONS.DR.TRANS` | `AcStmtParameter_PbConsDrTrans` | TField |  | Specifies a valid Debit transaction code to which the consolidated Passbook Debit entries refer to. Validation Rules: Allows only positive integer numeric values Must be a valid debit transaction code from the TRANSACTION table. |
| 12 | `AC.STP.PB.CONS.CR.TRANS` | `AcStmtParameter_PbConsCrTrans` | TField |  | Specifies a valid Credit transaction code to which the consolidated Passbook Credit entries refer to. Validation Rules: Allows only a valid positive numeric integer value. Must be a valid Credit transaction code from the TRANSACTION table. |
| 13 | `AC.STP.INT.STMT.AND.ADV` | `AcStmtParameter_IntStmtAndAdv` | TField |  | Indicates whether the interest statement and advice job should run. Possible values are "Y", "N" or "". If set to "Y", the interest statement and advice job should select and process the relevant records. |
| 14 | `AC.STP.EXT.SEPA.LINK.API` | `AcStmtParameter_ExtSepaLinkApi` | TField |  | A valid id of EB.API to hold the API that will return the link id to the EXTERNAL.SEPA.DETAILS table Validation Rules: If EP module is installed then only the value "GET.SEPA.DETAILS" is allowed. |
| 15 | `AC.STP.MESSAGE.TYPE` | `AcStmtParameter_MessageType` |  |  |  |
| 16 | `AC.STP.FILTER.RTN` | `AcStmtParameter_FilterRtn` |  |  |  |
| 17 | `AC.STP.CONSOLIDATE.RTN` | `AcStmtParameter_ConsolidateRtn` |  |  |  |
| 18 | `AC.STP.STMT.PRODUCE.RTN` | `AcStmtParameter_StmtProduceRtn` |  |  |  |
| 19 | `AC.STP.INCL.MASK.ENTRIES` | `AcStmtParameter_InclMaskEntries` |  |  |  |
| 20 | `AC.STP.CAMT.XSLT` | `AcStmtParameter_CamtXslt` |  |  |  |
| 21 | `AC.STP.INTRA.ENT.DAY` | `AcStmtParameter_IntraEntDay` | TField |  |  |
| 22 | `AC.STP.IX.MSG.CLASS` | `AcStmtParameter_IxMsgClass` |  |  |  |
| 23 | `AC.STP.IX.ADDTL.TAG.API` | `AcStmtParameter_IxAddtlTagApi` |  |  |  |
| 24 | `AC.STP.LOCAL.REF` | `AcStmtParameter_LocalRef` |  |  |  |
| 25 | `AC.STP.OVERRIDE` | `AcStmtParameter_Override` |  |  |  |
| 26 | `AC.STP.RECORD.STATUS` | `AcStmtParameter_RecordStatus` | String |  |  |
| 27 | `AC.STP.CURR.NO` | `AcStmtParameter_CurrNo` | String |  |  |
| 28 | `AC.STP.INPUTTER` | `AcStmtParameter_Inputter` |  |  |  |
| 29 | `AC.STP.DATE.TIME` | `AcStmtParameter_DateTime` |  |  |  |
| 30 | `AC.STP.AUTHORISER` | `AcStmtParameter_Authoriser` | String |  |  |
| 31 | `AC.STP.CO.CODE` | `AcStmtParameter_CoCode` | String |  |  |
| 32 | `AC.STP.DEPT.CODE` | `AcStmtParameter_DeptCode` | String |  |  |
| 33 | `AC.STP.AUDITOR.CODE` | `AcStmtParameter_AuditorCode` | String |  |  |
| 34 | `AC.STP.AUDIT.DATE.TIME` | `AcStmtParameter_AuditDateTime` | String |  |  |
| 35 | `AC.STP.USE.DATA.EVENTS` | `AcStmtParameter_UseDataEvents` | TField |  | This field is used to specify the configuration for streaming of Accounting data and production of CAMT statements. Valid options are: i) Statement through Services - This option is to setup CAMT statement generation through IX module using XML.TRANSFORMATION service. ii) Statement through Events and Microservice � This option is to setup CAMT statement generation through IZ module using streaming of data to the DATA.EVENTS table from where CAMT Microservice will consume the data and produce CAMT statement. iii) Both - If this option is set then CAMT Statement will be produced both through Services (option i) and through Events and Microservice (option ii) The default value for this field is "Statement through Services" if "IX" module is installed. If the field has no value and there is no Company specific definition in CO.USE.DATA.EVENTS field, then the CAMT statement will not be generated. Validation Rules: i) Option "Statement through Services" is allowed only if "IX" module is installed ii) Option "Statement through Events and Microservice" is allowed only if "IZ" module is installed iii) Option "BOTH" is allowed only if both the modules "IX" and "IZ" are installed |
| 36 | `AC.STP.DEFAULT.CAMT.FORMAT` | `AcStmtParameter_DefaultCamtFormat` |  |  |  |
| 37 | `AC.STP.SPLIT.MAXIMUM` | `AcStmtParameter_SplitMaximum` | TField |  | Allows to specify the number of Dates/Balances data in each ACCT.STMT.PRINT or ACCT.STMT2.PRINT record, beyond which data will be moved to other split sequencing records with record keys as ACCT.STMT.PRINT or ACCT.STMT2.PRINT master key and sequence number separated by underscore. Example: 100, 100_1, 100_2, ... for ACCT.STMT.PRINT and 100.3, 100.3_1, 100.3_2, ... for ACCT.STMT2.PRINT Validation Rules: Only Numeric Input Allowed between range 100 to 999 |
| 38 | `AC.STP.COMPANY.ID` | `AcStmtParameter_CompanyId` |  |  |  |
| 39 | `AC.STP.CO.USE.DATA.EVENTS` | `AcStmtParameter_CoUseDataEvents` |  |  |  |
| 40 | `AC.STP.RESERVED.5` | `AcStmtParameter_Reserved5` |  |  |  |
| 41 | `AC.STP.RESERVED.4` | `AcStmtParameter_Reserved4` |  |  |  |
| 42 | `AC.STP.RESERVED.3` | `AcStmtParameter_Reserved3` |  |  |  |
| 43 | `AC.STP.RESERVED.2` | `AcStmtParameter_Reserved2` |  |  |  |
| 44 | `AC.STP.RESERVED.1` | `AcStmtParameter_Reserved1` |  |  |  |
| 45 | `AC.STP.GEN.942.INDEPENDENTLY` | `AcStmtParameter_Gen942Independently` | TField |  | Indicates that the statement for the message type MT942 should be generated independently of MT941 (i.e. The entries for MT942 should not be filtered based on the last MT941). Valid options - YES_NULL If set to "YES" then during statement production for the message type MT942 the entries will be filtered based on the last MT942 statement. |
