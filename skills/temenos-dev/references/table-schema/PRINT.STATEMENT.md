# PRINT.STATEMENT — Table Schema

> Source: `INSERTS/I_F.PRINT.STATEMENT` in `AC_AccountStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACPS.DESCRIPTION` | `PrintStatement_Description` |  |  |  |
| 2 | `ACPS.SELECTION.FIELD` | `PrintStatement_SelectionField` |  |  |  |
| 3 | `ACPS.OPERAND` | `PrintStatement_Operand` |  |  |  |
| 4 | `ACPS.SELECTION` | `PrintStatement_Selection` |  |  |  |
| 5 | `ACPS.SORT.FIELD` | `PrintStatement_SortField` |  |  |  |
| 6 | `ACPS.CHARGE` | `PrintStatement_Charge` | TField | No | If statement charge details are NOT to be stored for this request then this field should be set to NO. Statement charge details, number of copies, sheets etc are stored in the file DE.SENT.PRINT which is used as the basis for statement charges (see STATEMENT.CHARGE). If you do not wish to record these details for this request, you may be reprinting the statement due to a printer wreck, then set this field to NO. Validation Rules: Y or NO Optional - default Y |
| 7 | `ACPS.REPRINT` | `PrintStatement_Reprint` | TField | No | Determines which file should be used in the selection process, AC.STMT.HANDOFF or AC.STMT.HANDOFF$HIS. When an account is due for a statement, defined by the statement frequency in ACCOUNT.STATEMENT, the necessary details to produce the statement are recorded in the file AC.STMT.HANDOFF. The key is the account number, statement date, frequency (1 or 2) and carrier (1 or 2). When the statement is actually printed, controlled by this application, PRINT.STATEMENT, the record is moved from AC.STMT.HANDOFF to the file AC.STMT.HANDOFF$HIS. Consequently, if the request is re-issued it will not select statements which have already been printed (see NUMBER.TO.BULK). If, however, you wish statements to be reprinted then this field should be set to "Y" and the statements will be selected from the AC.STMT.HANDOFF$HIS file. When reprinting your selection criteria should involve a statement date otherwise all statements will be reprinted. Validation Rules: Y or NO. OPTIONAL - default NO Y or NO. Default NO |
| 8 | `ACPS.FORMAT` | `PrintStatement_Format` | TField | Yes | The field facilitates the developer to format the statement ready for printing. The id of the enquiry record which controls the format of the statement. You can specify special formats for different requests - for example the nostro statements might be contain less transaction information than customer statements. Validation Rules: 1-32 Alphanumeric characters (Mandatory input) Must be a valid id on the ENQUIRY file. Must be a valid subroutine with PGM.FILE as a type 'S' and should be '@' prefix in the value or Must be a valid EB.API record of type METHOD which implements an interface defined in the EB.API record HOOK.ACPS.FORMAT.RTN. |
| 9 | `ACPS.REPORT.CONTROL.ID` | `PrintStatement_ReportControlId` | TField | Yes | The report control record which the controls the spooling of the statements. The report control record is used to determine the destination printer, the spooling format (number of lines per page etc) and whether the output should be stored for microfiching. Validation Rules: 4-35 Alphanumeric characters (Mandatory input) Must be a valid record on REPORT.CONTROL. |
| 10 | `ACPS.NUMBER.TO.BULK` | `PrintStatement_NumberToBulk` | TField | No | Determines the number of statements which will be bulked into a single spool job. Used to control the efficiency of the spooler when printing statements, the larger the number to bulk the fewer spool jobs (which can be useful in sites where there is a limitation). If ACCOUNT is specified then the statements will be batched by account. Also controls the number of statements which constitute a transaction for system recovery purposes. If the application aborts or the machine crashes then the number processed is the last complete bulk, i.e if the number to bulk is set to 100 and the machine crashes during the processing of number 145, when the request is re-issued processing will start from number 101. When executing the request online there is a limit of 500 writes which can be performed in one transaction. To determine the maximum number to bulk use the following table: Reprint Charge Maximum NO Y 160 Y Y 500 Y NO 9999 Validation Rules: 8 Numeric or ACCOUNT. Optional - default 100 Numeric in the range 1-9999 or equal ACCOUNT. Default 100 |
| 11 | `ACPS.PRINT.ROUTINE` | `PrintStatement_PrintRoutine` | TField |  | This field contains name of an external subroutine(exist on PGM.FILE as a type 'S') or an EB.API record of type METHOD which implements an interface defined in the EB.API record HOOK.ACPS.PRINT.RTN, written by the user that needs to be invoked as an alternative method of printing statements. AC.STMT.HANDOFF id, AC.STMT.HANDOFF record and account id will be passed to local routine. If entered then T24's own printing process will be ignored. Handling of AC.STMT.HANDOFF ids (whether to retain or delete) also to be handled locally. If EB.ERROR record with id 'AC-AC.STMT.HOOK.PRINT.RTN.INV' is available then core will pick the AC.STMT.HANFOFF ids and pass to local api in multi-threaded fashion. In this case local api should exists to accept 3 arguments. In case selection of records to be controlled locally then there should be no EB.ERROR record with id as AC-AC.STMT.HOOK.PRINT.RTN.INV. In this method the PRINT.STATEMENTRUN service will behave as single threaded service and local api will not accept any arguments. |
| 12 | `ACPS.CHARGE.ROUTINE` | `PrintStatement_ChargeRoutine` | TField |  | This field will contain the name of an external subroutine written by the user to apply an immediate charge to the account for which the statement is being reprinted. Validation Rules: The routine must exist on the system and have a valid VOC entry The routine must exist in the PGM.FILE as a subroutine i.e. TYPE = 'S' |
| 13 | `ACPS.NEXT.FORMAT.ENQ` | `PrintStatement_NextFormatEnq` |  |  |  |
| 14 | `ACPS.NEW.PAGE` | `PrintStatement_NewPage` |  |  |  |
| 15 | `ACPS.ALLOWED.ADDON` | `PrintStatement_AllowedAddon` |  |  |  |
| 16 | `ACPS.ADDON.NEW.PAGE` | `PrintStatement_AddonNewPage` |  |  |  |
| 17 | `ACPS.REFER.TO.PRODUCT` | `PrintStatement_ReferToProduct` | TField | No | When set to Yes, the Statement generation process would know to check with the Statement configuration for details of the appropriate Statement Type in the AccountStatement Validation Rules: Optional input, YES or NO Field This attribute would need to be set to “Yes�? in the SYSTEM definition and any other default definition used, to process Combined Statements |
| 18 | `ACPS.RESERVED.5` | `PrintStatement_Reserved5` | TField |  | Reserved for future use. |
| 19 | `ACPS.RESERVED.4` | `PrintStatement_Reserved4` | TField |  | Reserved for future use. |
| 20 | `ACPS.RESERVED.3` | `PrintStatement_Reserved3` | TField |  | Reserved for future use. |
| 21 | `ACPS.RESERVED.2` | `PrintStatement_Reserved2` | TField |  | Reserved for future use. |
| 22 | `ACPS.RESERVED.1` | `PrintStatement_Reserved1` | TField |  | Reserved for future use. |
| 23 | `ACPS.RESERVED.15` | `PrintStatement_Reserved15` | TField |  |  |
| 24 | `ACPS.RESERVED.14` | `PrintStatement_Reserved14` | TField |  |  |
| 25 | `ACPS.RESERVED.13` | `PrintStatement_Reserved13` | TField |  |  |
| 26 | `ACPS.RESERVED.12` | `PrintStatement_Reserved12` | TField |  |  |
| 27 | `ACPS.RESERVED.11` | `PrintStatement_Reserved11` | TField |  |  |
| 28 | `ACPS.RESERVED.10` | `PrintStatement_Reserved10` | TField |  |  |
| 29 | `ACPS.RESERVED.9` | `PrintStatement_Reserved9` | TField |  |  |
| 30 | `ACPS.LOCAL.REF` | `PrintStatement_LocalRef` |  |  |  |
| 31 | `ACPS.RECORD.STATUS` | `PrintStatement_RecordStatus` | String |  |  |
| 32 | `ACPS.CURR.NO` | `PrintStatement_CurrNo` | String |  |  |
| 33 | `ACPS.INPUTTER` | `PrintStatement_Inputter` |  |  |  |
| 34 | `ACPS.DATE.TIME` | `PrintStatement_DateTime` |  |  |  |
| 35 | `ACPS.AUTHORISER` | `PrintStatement_Authoriser` | String |  |  |
| 36 | `ACPS.CO.CODE` | `PrintStatement_CoCode` | String |  |  |
| 37 | `ACPS.DEPT.CODE` | `PrintStatement_DeptCode` | String |  |  |
| 38 | `ACPS.AUDITOR.CODE` | `PrintStatement_AuditorCode` | String |  |  |
| 39 | `ACPS.AUDIT.DATE.TIME` | `PrintStatement_AuditDateTime` | String |  |  |
