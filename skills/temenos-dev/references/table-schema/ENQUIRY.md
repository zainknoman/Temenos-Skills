# ENQUIRY — Table Schema

> Source: `INSERTS/I_F.ENQUIRY` in `EB_Reports.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ENQ.PAGE.SIZE` | `Enquiry_PageSize` | TField | Yes | Standard T24 alphanumeric field. Validation Rules: Mandatory input. A maximum of 5 characters may be entered. These co-ordinates define the screen page which will be used by the enquiry. These co-ordinates represent the variable portion of the screen used to display the enquiry pages. Hence it is cleared prior to output of a page. It does not restrict the enquiry from addressing other areas of the screen, but it should be noted that these areas are not refreshed automatically by moving from one page to the next. Typically the page is used for line details leaving the remainder of the screen available for headings etc. Validation Rules: XX,YY where XX defines the first line of the page and YY the last. Must be numeric, in the range 0 - 999, and be separated by a ','. (Mandatory input) |
| 2 | `ENQ.FILE.NAME` | `Enquiry_FileName` | A (alphanumeric) | Yes | This is the main file to be accessed/displayed by the enquiry system. This specifies the main file to be processed. The file must be a valid entry on F.FILE.CONTROL and should not contain the 'F.' or 'FXXX.' prefix. Validation Rules: 35 type A (alphanumeric) characters. (Mandatory input) |
| 3 | `ENQ.FIXED.SELECTION` | `Enquiry_FixedSelection` |  |  |  |
| 4 | `ENQ.FIXED.SORT` | `Enquiry_FixedSort` |  |  |  |
| 5 | `ENQ.OPEN.BRACKET` | `Enquiry_OpenBracket` |  |  |  |
| 6 | `ENQ.SELECTION.FLDS` | `Enquiry_SelectionFlds` |  |  |  |
| 7 | `ENQ.SEL.LABEL` | `Enquiry_SelLabel` |  |  |  |
| 8 | `ENQ.SEL.FLD.OPER` | `Enquiry_SelFldOper` |  |  |  |
| 9 | `ENQ.REQUIRED.SEL` | `Enquiry_RequiredSel` |  |  |  |
| 10 | `ENQ.CLOSE.BRACKET` | `Enquiry_CloseBracket` |  |  |  |
| 11 | `ENQ.REL.NEXT.FIELD` | `Enquiry_RelNextField` |  |  |  |
| 12 | `ENQ.BUILD.ROUTINE` | `Enquiry_BuildRoutine` |  |  |  |
| 13 | `ENQ.HEADER` | `Enquiry_Header` |  |  |  |
| 14 | `ENQ.FIELD.NAME` | `Enquiry_FieldName` |  |  |  |
| 15 | `ENQ.OPERATION` | `Enquiry_Operation` |  |  |  |
| 16 | `ENQ.COLUMN` | `Enquiry_Column` |  |  |  |
| 17 | `ENQ.LENGTH.MASK` | `Enquiry_LengthMask` |  |  |  |
| 18 | `ENQ.CONVERSION` | `Enquiry_Conversion` |  |  |  |
| 19 | `ENQ.COMMENTS` | `Enquiry_Comments` |  |  |  |
| 20 | `ENQ.TYPE` | `Enquiry_Type` |  |  |  |
| 21 | `ENQ.DISPLAY.BREAK` | `Enquiry_DisplayBreak` |  |  |  |
| 22 | `ENQ.FIELD.LBL` | `Enquiry_FieldLbl` |  |  |  |
| 23 | `ENQ.FIELD.DISP.TYPE` | `Enquiry_FieldDispType` |  |  |  |
| 24 | `ENQ.SECTION` | `Enquiry_Section` |  |  |  |
| 25 | `ENQ.ATTRIBS` | `Enquiry_Attribs` |  |  |  |
| 26 | `ENQ.TARGET.FIELD` | `Enquiry_TargetField` |  |  |  |
| 27 | `ENQ.COL.WIDTH` | `Enquiry_ColWidth` |  |  |  |
| 28 | `ENQ.RESERVED7` | `Enquiry_Reserved7` |  |  |  |
| 29 | `ENQ.RESERVED6` | `Enquiry_Reserved6` |  |  |  |
| 30 | `ENQ.RESERVED5` | `Enquiry_Reserved5` |  |  |  |
| 31 | `ENQ.RESERVED4` | `Enquiry_Reserved4` |  |  |  |
| 32 | `ENQ.RESERVED3` | `Enquiry_Reserved3` |  |  |  |
| 33 | `ENQ.RESERVED2` | `Enquiry_Reserved2` |  |  |  |
| 34 | `ENQ.RESERVED1` | `Enquiry_Reserved1` |  |  |  |
| 35 | `ENQ.SINGLE.MULTI` | `Enquiry_SingleMulti` |  |  |  |
| 36 | `ENQ.ENQUIRY.NAME` | `Enquiry_EnquiryName` |  |  |  |
| 37 | `ENQ.SEL.CRIT` | `Enquiry_SelCrit` |  |  |  |
| 38 | `ENQ.LABEL.FIELD` | `Enquiry_LabelField` |  |  |  |
| 39 | `ENQ.NXT.DESC` | `Enquiry_NxtDesc` |  |  |  |
| 40 | `ENQ.PAGE.FIELDS` | `Enquiry_PageFields` | TField |  | Internal field used for processing of the enquiry. Validation Rules: Internal field. |
| 41 | `ENQ.STATIC.FIELDS` | `Enquiry_StaticFields` | TField |  | Internal field used for processing of the enquiry. Validation Rules: Internal field. |
| 42 | `ENQ.MULTI.FIELDS` | `Enquiry_MultiFields` | TField |  | Internal field used for processing of the enquiry. Validation Rules: Internal field. |
| 43 | `ENQ.BREAK.FIELDS` | `Enquiry_BreakFields` | TField |  | Internal field used for processing of the enquiry. Validation Rules: Internal field. |
| 44 | `ENQ.PROCESS.BREAKS` | `Enquiry_ProcessBreaks` | TField |  | Internal field used for processing of the enquiry. Validation Rules: Internal field. |
| 45 | `ENQ.TOTAL.FIELDS` | `Enquiry_TotalFields` | TField |  | Internal field used for processing of the enquiry. Validation Rules: Internal field. |
| 46 | `ENQ.NEXT.LVL.FLDS` | `Enquiry_NextLvlFlds` | TField |  | Standard T24 numeric field. Validation Rules: A maximum of 20 characters may be entered. This is a NOINPUT field. |
| 47 | `ENQ.INHERIT.SOURCE` | `Enquiry_InheritSource` | TField |  | Merging parent enquiry details to Current enquiry and fetching details in singleshot and also it supports Multilevel inheritance. Example ENQUIRY A has the INHERIT.SOURCE set to ENQUIRY B, ENQUIRY B has its INHERIT.SOURCE set to ENQUIRY C, ENQUIRY C has its INHERIT.SOURCE set to ENQUIRY D. This will be supported Inherit Feature will be available after R21 AMR release for Browser request. Validation Rules: Input allowed only when the Id of the current enquiry is an API type and also this field allows only API type enquiry. Current and parent enquiry FILE.NAME should be same otherwise throws an error. |
| 48 | `ENQ.SMS.APPLICATION` | `Enquiry_SmsApplication` |  |  |  |
| 49 | `ENQ.SMS.ID` | `Enquiry_SmsId` |  |  |  |
| 50 | `ENQ.SMS.ABORT` | `Enquiry_SmsAbort` | TField | No | Flag to indicate if the enquiry is to be aborted when the first SMS violation is recorded. The enquiry system will read and SMS verify all records it selects. This can be very time consuming if all the records fail the SMS checks. Consequently this flag enables the enquiry to abort at the first SMS violation encountered. Validation Rules: Can be either Y or No. (Optional Input). |
| 51 | `ENQ.USE.FIELD.NUMBERS` | `Enquiry_UseFieldNumbers` | TField | No | Specifies whether field numbers entered in the OPERATION field should not be converted to the relevant field name. Some enquiries may use a specified FILE.NAME for selection purposes, however a work record is constructed using a conversion routine in the body of the enquiry. Enquiry will usually attampt to convert a field number entered in the OPERATION field to the correct field name for the FILE.NAME, so that the enquiry is compatible with future file layout changes. However where the conversion routine builds a work record, this layout is fixed and should not be converted to the field name, as the layout may be entirely different. In order to suppress the conversion of the number entered in OPERATION to a name, a value of Y should be entered in this field. This will leave the field OPERATION as entered. Null and NO are treated in the same way. Validation Rules: Optional Field. May be Y or NO. |
| 52 | `ENQ.CUSTOMER.NO.FLD` | `Enquiry_CustomerNoFld` | TField | No | Indicates the defined field which contains the value of the customer number, to be used for purposes of spooling. When the Enquiry is used to produce a report from the ENQUIRY.REPORT module, the value in the nominated field will be passed to the Report Control system for each spooled record. The report Control System will then be able to determine whether the report generated is to be spooled or held for the customer. Note that the field nominated should not be extracted on a page break as the previous value may be extracted. Validation Rules: Up to 18 'A' alphanumeric characters. (Optional Input) The field must be defines as a FIELD NAME. |
| 53 | `ENQ.ACCOUNT.NO.FLD` | `Enquiry_AccountNoFld` | TField | No | Indicates the defined field which contains the value of the account number, to be used for purposes of spooling. When enquiry is used to produce a report from the ENQUIRY.REPORT module, the value in the nominated field will be passed to the Report Control system for each spooled record. The report control system will then be able to determine whether output for the report and the specified account is to be spooled or held. In order for the full definition of DE.PRODUCT records for Held Customer output to be utilised, a CUSTOMER.FLD.NO should be defined with this field. Note that the field nominated should not be extracted on a page break, as the previous value may be used. Validation Rules: Up to 18 'A' alphanumeric characters. (Optional input) Must be defined as a FIELD NAME. |
| 54 | `ENQ.SPOOL.BRK.FLD` | `Enquiry_SpoolBrkFld` |  |  |  |
| 55 | `ENQ.DESCRIPT` | `Enquiry_Descript` |  |  |  |
| 56 | `ENQ.ATTRIBUTES` | `Enquiry_Attributes` |  |  |  |
| 57 | `ENQ.PRODUCT` | `Enquiry_Product` | TField |  | Defines the Application / Product to which this Enquiry belongs eg: FX, MM etc. Validation Rules: Standard T24 alphanumeric field. A maximum of 5 characters may be entered. Must be the key to a valid entry on the EB.PRODUCT file. |
| 58 | `ENQ.SHORT.DESC` | `Enquiry_ShortDesc` |  |  |  |
| 59 | `ENQ.REAL.TIME.FILES` | `Enquiry_RealTimeFiles` |  |  |  |
| 60 | `ENQ.COMPANY.SELECT` | `Enquiry_CompanySelect` | TField | No | This field is used in a multi branch system to control enquiry access to financial level data. Multi branch indicates that the MB product is installed, the term Multi Book can also be used. This product basically allows financial level data to be stored in the same database table for all companies, as opposed to Multi Company where the data is stored in a separate table for each company. If this field is set to ALL then records will be selected for all companies, with the current SMS restrictions being applied to what the user can actually access. If this field is left blank then the data selected will be restricted to the current company. Validation Rules: Optional input of ALL in a system with the MB product installed |
| 61 | `ENQ.COMP.FOR.ENQ` | `Enquiry_CompForEnq` |  |  |  |
| 62 | `ENQ.TARGET.APPLICATION` | `Enquiry_TargetApplication` | TField |  | Applies to application enquiries (see ATTRIBUTES/APPLICATION.ENQUIRY). Specifies the application to be operated on by the enquiry. |
| 63 | `ENQ.ENQUIRY.GRAPH.ID` | `Enquiry_EnquiryGraphId` |  |  |  |
| 64 | `ENQ.TOOL.ID` | `Enquiry_ToolId` |  |  |  |
| 65 | `ENQ.TOOL.TEXT` | `Enquiry_ToolText` |  |  |  |
| 66 | `ENQ.TOOL.ITEM` | `Enquiry_ToolItem` |  |  |  |
| 67 | `ENQ.EXPOSE` | `Enquiry_Expose` | TField |  | Field that specifies whether the ENQUIRY should be exposed or not Validation Rules: 1. Length of 3 characters 2. Options are 'YES', 'NO', '' 3. No-input if 'PW' is not installed in the COMPANY |
| 68 | `ENQ.SERVICE` | `Enquiry_Service` |  |  |  |
| 69 | `ENQ.ACTIVITY` | `Enquiry_Activity` | TField | Yes | Field that contains the ID of a PW.ACTIVITY record. It may be an existing record. If the record is not present, then upon authorising the ENQUIRY, a new record is created. The ID of the new PW.ACTIVITY record created through the ENQUIRY will have prefix 'WS.' Validation Rules: 1. Length of 35 alphanumeric characters 2. If EXPOSE is set to 'YES', then this field is mandatory 3. No-input if EXPOSE is not set to 'YES' The following validations/processing is done based on the fields SERVICE and ACTIVITY. If both SERVICE and ACTIVITY do not exist, then a new activity is created in PW.ACTIVITY, with the TARGET field mapped to the Enquiry and a new record is created in EB.SERVICE with the activity added to it. If the SERVICE is existing EB.SERVICE and ACTIVITY does not exist in PW.ACTIVITY,a new activity is created in PW.ACTIVITY and the same is appended to the EB.SERVICE record. If SERVICE does not exist and ACTIVITY exists, a check is done to ensure that the activity relates to this Enquiry, i.e. the TARGET field in PW.ACTIVITY is mapped correctly, otherwise an error message is thrown. Then, a new EB.SERVICE record is created with the activity added to it. If both SERVICE and ACTIVITY exists and the activity relates to the Enquiry, a check is done to ensure that the EB.SERVICE does not contain the ACTIVITY.ID already.Otherwise an error message is thrown. Finally,EB.SERVICE is updated with the activity appended to it. |
| 70 | `ENQ.EXPOSE.DESC` | `Enquiry_ExposeDesc` | TField | Yes | Description of the exposed ENQUIRY.This would be updated in the DESCRIPTION fields of both PW.ACTIVITY and EB.SERVICE,when they are newly created from the ENQUIRY Validation Rules: 1. Length of 35 alphanumeric characters 2. If EXPOSE is set to 'YES', then this field is mandatory 3. No-input if EXPOSE is not set to 'YES' |
| 71 | `ENQ.TOOLBAR` | `Enquiry_Toolbar` | TField |  | Allows a custom toolbar to be displayed when enquiry results are displayed. This toolbar takes precedence over defined tool items. Validation Rules: Must be a valid BROWSER.TOOLBAR record. |
| 72 | `ENQ.FILE.VERSION` | `Enquiry_FileVersion` |  |  |  |
| 73 | `ENQ.POPUP.DROPDOWN.FLD` | `Enquiry_PopupDropdownFld` |  |  |  |
| 74 | `ENQ.NO.MANDATORY.SELECTION` | `Enquiry_NoMandatorySelection` | TField | Conditional | An optional field. Allows to input values in either REQUIRED.SEL or NO.MANDATORY.SELECTION While designing an enquiry, if the field NO.MANDATORY.SELECTION is input with a value, then the field REQUIRED.SEL values should be removed. If the value is not input in the field SELECTION.FLDS then the system disallows to input in the field NO.MANDATORY.SELECTION Validations: Optional field Numeric field |
| 75 | `ENQ.OVERRIDE` | `Enquiry_Override` |  |  |  |
| 76 | `ENQ.RECORD.STATUS` | `Enquiry_RecordStatus` | String |  |  |
| 77 | `ENQ.CURR.NO` | `Enquiry_CurrNo` | String |  |  |
| 78 | `ENQ.INPUTTER` | `Enquiry_Inputter` |  |  |  |
| 79 | `ENQ.DATE.TIME` | `Enquiry_DateTime` |  |  |  |
| 80 | `ENQ.AUTHORISER` | `Enquiry_Authoriser` | String |  |  |
| 81 | `ENQ.CO.CODE` | `Enquiry_CoCode` | String |  |  |
| 82 | `ENQ.DEPT.CODE` | `Enquiry_DeptCode` | String |  |  |
| 83 | `ENQ.AUDITOR.CODE` | `Enquiry_AuditorCode` | String |  |  |
| 84 | `ENQ.AUDIT.DATE.TIME` | `Enquiry_AuditDateTime` | String |  |  |
