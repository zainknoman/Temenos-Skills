# RE.STAT.REP.LINE — Table Schema

> Source: `INSERTS/I_F.RE.STAT.REP.LINE` in `RE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RE.SRL.TYPE` | `ReStatRepLine_Type` | TField |  | The field TYPE will classify a Line as a Heading, Detail or Total Line. HEADING = A Descriptive title given in a line without any finance value. DETAIL = Returns a financial value for the selected criteria. LINK = Used to do maturity splits in the same line, they are same as Detail. TOTAL = Used to define Total or Sub totals for the Detail Line. |
| 2 | `RE.SRL.DESC` | `ReStatRepLine_Desc` |  |  |  |
| 3 | `RE.SRL.TOTAL.PRINT` | `ReStatRepLine_TotalPrint` | A (alphanumeric) | Yes | Defines the line as either a Heading, Total or Detail line. Validation Rules: Up to 11 type A (alphanumeric) characters allowing for the following values: . Heading . Total . Detail . Link Mandatory input. The following values only are accepted: HEADING - Signifies that the line is a section heading line to be printed at the beginning of a section. TOTAL - Denotes that the line is one in which totals are to be printed. DETAIL - Denotes that the line is one for which data accumulated from the Consolidate ASSET&amp;LIAB and Consolidate PROFIT&amp;LOSS record files are to be printed. LINK - Same as DETAIL, but applicable (if required) for MM, LD etc. The information is broken down into Time periods specified in the file RE.REP.STAT.LINK. 'LINK' can only be used for group type of CLOSING. The checking is performed by the RE.REP.STAT.LINK file program. If, at the time of printing, there is no details on the RE.REP.STAT.LINK file for this line number and report name, then the line is treated as a DETAIL line. |
| 4 | `RE.SRL.TOTAL.ACCUM` | `ReStatRepLine_TotalAccum` |  |  |  |
| 5 | `RE.SRL.SUPRESSION` | `ReStatRepLine_Supression` | A (alphanumeric) | No | Indicator to suppress or print a line with zero values. If suppression of 'Y' is asked on a Heading line, then the heading line is only printed if a DETAIL, LINK, or TOTAL line is to be printed before the next heading line is encountered. If suppression is numeric and if it matches with one of the group specified in RE.STAT.REPORT.HEAD, then the line is suppressed for zero values. Validation Rules: Up to 2 type A (alphanumeric) and 9 type N (numeric) characters (with the following values: Y = To suppress lines with zero values. N(o) = Do not suppress the lines with zero values. 1 to 9 Optional input. If left blank then the No option is assumed at printing time. |
| 6 | `RE.SRL.SPACE.BEFORE` | `ReStatRepLine_SpaceBefore` | A (alphanumeric) | No | Indicator of number of lines to be left blank before printing of the specified line. This spacing is only performed if the line is actually printed and is in addition to whatever was asked for as SPACE AFTER (Field 7) in the previous line. Validation Rules: Up to 3 type A (alphanumeric) characters with the following values: . N = Number of lines to be left blank. . NEW= Print line on new page. Optional input. Allowed values are 0 - 9 or NEW. |
| 7 | `RE.SRL.SPACE.AFTER` | `ReStatRepLine_SpaceAfter` | A (alphanumeric) | No | Indicator of number of lines to be left blank after printing of the specified line. This spacing is only performed if the line is actually printed and is in addition to whatever was asked for as SPACE BEFORE (Field 6) on the next line. Validation Rules: Up to 3 type A (alphanumeric) characters with the following values: . N = Number of lines to be left blank. . NEW= Skip to new page for next line. Optional input. Allowed values are 0 - 9 or NEW. |
| 8 | `RE.SRL.MAT.DATE.TO` | `ReStatRepLine_MatDateTo` |  |  |  |
| 9 | `RE.SRL.MAT.LINE.NO` | `ReStatRepLine_MatLineNo` |  |  |  |
| 10 | `RE.SRL.ASSET.SIGN` | `ReStatRepLine_AssetSign` | TField | Yes | This field together with "ASSET SIGN" allows the user to report in different lines the result of an asset and liability line definition according to the sign (debit or credit) of the total line. Validation Rules: Acceptable values in this field are: . Debit or . Credit Mandatory input when "ASSET OPP LINE" has been input; otherwise not allowed. Input in this field is only allowed for asset and liability lines type i.e. where fields 21.1 to 38.1 are used to define the details of the line. |
| 11 | `RE.SRL.ASSET.OPP.LINE` | `ReStatRepLine_AssetOppLine` | TField | Yes | This field together with "ASSET SIGN" allows the user to report in different lines the result of an asset and liability line definition according to the sign (debit or credit) of the total line. Validation Rules: Up to 4 numeric characters representing the line number. Mandatory field when "PROFIT TYPE" entered; otherwise not allowed. Input in this field is only allowed for asset and liability lines type i.e. where fields 21.1 to 38.1 are used to define the details of the line. |
| 12 | `RE.SRL.PROFIT.TYPE` | `ReStatRepLine_ProfitType` | TField | Conditional | This field together with 'PROFIT.SIGN' and 'PROFIT.OPP.LINE' allows the user to report in different lines the result of a Profit and Loss line definition according to the sign (debit or credit) of the total line or the various consolidate records which are included in the definition of the line. he two values have the following meaning: . Line: When the condition defined for the sign applies to the total line result. . Record: When the condition defined for the sign applies to the individual consolidation records contained in the line being created Validation Rules: Acceptable values in this field are: Line or Record/ Optional Input. Default = Nil. Input in this field is only allowed for Profit and Loss Lines type i.e. where fields 39.1 to 53.1 are used to define the details of the line. When 'Record' has been input in this field, input of 'REC' will be mandatory in at least one multivalue of the field 'PROFIT.EXT.DUP' (Field 53.1). |
| 13 | `RE.SRL.PROFIT.SIGN` | `ReStatRepLine_ProfitSign` | TField | Yes | This field together with 'PROFIT TYPE' and 'PROFIT.OPP.LINE' allows the user to report in different lines the result of a Profit and Loss line definition according to the sign (debit or credit) of the total line or the various consolidate records which are included in the definition of the line. Validation Rules: Acceptable values in this field are: . Debit or . Credit Mandatory input when 'PROFIT TYPE' has been input; otherwise not allowed. Input in this field is only allowed for Profit and Loss Lines type i.e. where fields 39.1 to 53.1 are used to define the details of the line. |
| 14 | `RE.SRL.PROFIT.OPP.LINE` | `ReStatRepLine_ProfitOppLine` | TField | Yes | This field together with 'PROFIT TYPE' and 'PROFIT SIGN' allows the user to report in different lines the result of a Profit and Loss line definition according to the sign (debit or credit) of the total line or the various consolidate records which are included in the definition of the line. Validation Rules: Up to 4 numeric characters representing the line number. Mandatory field when 'PROFIT TYPE' entered; otherwise not allowed. Input in this field is only allowed for Profit and Loss Lines type i.e. where fields 39.1 to 53.1 are used to define the details of the line. |
| 15 | `RE.SRL.PROFIT.PERIOD` | `ReStatRepLine_ProfitPeriod` | TField | Yes | This field togethr with PP.OPP.LINE allows the user to report in different lines the result of a profit and loss line definition according to the period (current month or year to date or both). Validation Rules: Acceptable values in this field are: Cm, Ytd or All Mandatory input when Profit details are specified. Input in this field is mandatory for Profit and Loss Lines type i.e. where fields 39.1 to 51.1 are used to define the details of the line. |
| 16 | `RE.SRL.PP.OPP.LINE` | `ReStatRepLine_PpOppLine` | TField | Yes | This field togethr with PROFIT PERIOD allows the user to report in different lines the result of a profit and loss line definition according to the period (current month or year to date). Validation Rules: Up to 4 numeric characters representing the line number. Mandatory input if PROFIT.PERIOD is current month or year to date. But override is allowed if the PROFIT.PERIOD is current month or year to date. Must be a valid report line for that report. Not allowed if PROFIT.PERIOD is all. |
| 17 | `RE.SRL.FX.REP.RATE` | `ReStatRepLine_FxRepRate` | TField |  | Is used to specify that the original exchange rates are to be of the FX contracts are to be reported. When this field is set to historic for a closing line. The amounts local cuurency equivalents are not taken from the CRF base but taken directly from the Forex contracts. Validation Rules: Acceptable values in this field are : HISTORIC or NULL |
| 18 | `RE.SRL.LINE.BALANCE` | `ReStatRepLine_LineBalance` | TField | No | Specifies whether line balances are to be recorded for this report. 'DETAIL' - denotes that details of individual movements behind the line are to be recorded by default. 'SUMMARY' - denotes that only line level movements and balances are to be recorded by default. No Value indicates that no balances will be recorded. Validation Rules: Valid values are 'DETAIL' &amp; 'SUMMARY' Input Optional A value is only allowed for the main report i.e. when there is no '.' in the key. |
| 19 | `RE.SRL.LOCAL.REF` | `ReStatRepLine_LocalRef` |  |  |  |
| 20 | `RE.SRL.MNEMONIC` | `ReStatRepLine_Mnemonic` | TField | No | Specifies an alternative easy means of referencing the RE.STAT.REP.LINE. Any value can be entered in this field with the exception that the first character must be alpha. Like the ID (Field 0) the Mnemonic must be unique across T24 Note: For each re.stat.rep.line, the System will automatically update the internal file "RE.MNEMONIC.LINE" which allows the User to display the RE.STAT.REP.LINE codes in mnemonic sequence instead. Validation Rules: 3-10 type MNE (Uppercase alpha or numeric, first character alpha, or ".") characters. (Optional input) |
| 21 | `RE.SRL.ASSET.APPLIC.ID` | `ReStatRepLine_AssetApplicId` |  |  |  |
| 22 | `RE.SRL.ASSET.CCY.MKT` | `ReStatRepLine_AssetCcyMkt` |  |  |  |
| 23 | `RE.SRL.ASSET.POS.TYPE` | `ReStatRepLine_AssetPosType` |  |  |  |
| 24 | `RE.SRL.ASSET.CURRENCY` | `ReStatRepLine_AssetCurrency` |  |  |  |
| 25 | `RE.SRL.ASSET1` | `ReStatRepLine_Asset1` |  |  |  |
| 26 | `RE.SRL.ASSET2` | `ReStatRepLine_Asset2` |  |  |  |
| 27 | `RE.SRL.ASSET3` | `ReStatRepLine_Asset3` |  |  |  |
| 28 | `RE.SRL.ASSET4` | `ReStatRepLine_Asset4` |  |  |  |
| 29 | `RE.SRL.ASSET5` | `ReStatRepLine_Asset5` |  |  |  |
| 30 | `RE.SRL.ASSET6` | `ReStatRepLine_Asset6` |  |  |  |
| 31 | `RE.SRL.ASSET7` | `ReStatRepLine_Asset7` |  |  |  |
| 32 | `RE.SRL.ASSET8` | `ReStatRepLine_Asset8` |  |  |  |
| 33 | `RE.SRL.ASSET9` | `ReStatRepLine_Asset9` |  |  |  |
| 34 | `RE.SRL.ASSET10` | `ReStatRepLine_Asset10` |  |  |  |
| 35 | `RE.SRL.ASSET11` | `ReStatRepLine_Asset11` |  |  |  |
| 36 | `RE.SRL.ASSET12` | `ReStatRepLine_Asset12` |  |  |  |
| 37 | `RE.SRL.ASSET.TYPE` | `ReStatRepLine_AssetType` |  |  |  |
| 38 | `RE.SRL.ASSET.EXT.DUP` | `ReStatRepLine_AssetExtDup` |  |  |  |
| 39 | `RE.SRL.PROFT.APPLIC.ID` | `ReStatRepLine_ProftApplicId` |  |  |  |
| 40 | `RE.SRL.PROFIT1` | `ReStatRepLine_Profit1` |  |  |  |
| 41 | `RE.SRL.PROFIT2` | `ReStatRepLine_Profit2` |  |  |  |
| 42 | `RE.SRL.PROFIT3` | `ReStatRepLine_Profit3` |  |  |  |
| 43 | `RE.SRL.PROFIT4` | `ReStatRepLine_Profit4` |  |  |  |
| 44 | `RE.SRL.PROFIT5` | `ReStatRepLine_Profit5` |  |  |  |
| 45 | `RE.SRL.PROFIT6` | `ReStatRepLine_Profit6` |  |  |  |
| 46 | `RE.SRL.PROFIT7` | `ReStatRepLine_Profit7` |  |  |  |
| 47 | `RE.SRL.PROFIT8` | `ReStatRepLine_Profit8` |  |  |  |
| 48 | `RE.SRL.PROFIT9` | `ReStatRepLine_Profit9` |  |  |  |
| 49 | `RE.SRL.PROFIT10` | `ReStatRepLine_Profit10` |  |  |  |
| 50 | `RE.SRL.PROFIT11` | `ReStatRepLine_Profit11` |  |  |  |
| 51 | `RE.SRL.PROFIT12` | `ReStatRepLine_Profit12` |  |  |  |
| 52 | `RE.SRL.PROFT.CURRENCY` | `ReStatRepLine_ProftCurrency` |  |  |  |
| 53 | `RE.SRL.PROFT.EXT.DUP` | `ReStatRepLine_ProftExtDup` |  |  |  |
| 54 | `RE.SRL.CONSOL.NAME` | `ReStatRepLine_ConsolName` |  |  |  |
| 55 | `RE.SRL.LDAT.APPLIC` | `ReStatRepLine_LdatApplic` |  |  |  |
| 56 | `RE.SRL.LDAT.CCY.MKT` | `ReStatRepLine_LdatCcyMkt` |  |  |  |
| 57 | `RE.SRL.LDAT.POS.TYP` | `ReStatRepLine_LdatPosTyp` |  |  |  |
| 58 | `RE.SRL.LDAT.CCY` | `ReStatRepLine_LdatCcy` |  |  |  |
| 59 | `RE.SRL.ASSET1.1` | `ReStatRepLine_Asset11` |  |  |  |
| 60 | `RE.SRL.ASSET2.1` | `ReStatRepLine_Asset21` |  |  |  |
| 61 | `RE.SRL.ASSET3.1` | `ReStatRepLine_Asset31` |  |  |  |
| 62 | `RE.SRL.ASSET4.1` | `ReStatRepLine_Asset41` |  |  |  |
| 63 | `RE.SRL.ASSET5.1` | `ReStatRepLine_Asset51` |  |  |  |
| 64 | `RE.SRL.ASSET6.1` | `ReStatRepLine_Asset61` |  |  |  |
| 65 | `RE.SRL.ASSET7.1` | `ReStatRepLine_Asset71` |  |  |  |
| 66 | `RE.SRL.ASSET8.1` | `ReStatRepLine_Asset81` |  |  |  |
| 67 | `RE.SRL.ASSET9.1` | `ReStatRepLine_Asset91` |  |  |  |
| 68 | `RE.SRL.ASSET10.1` | `ReStatRepLine_Asset101` |  |  |  |
| 69 | `RE.SRL.ASSET11.1` | `ReStatRepLine_Asset111` |  |  |  |
| 70 | `RE.SRL.ASSET12.1` | `ReStatRepLine_Asset121` |  |  |  |
| 71 | `RE.SRL.LDAT.TYPE` | `ReStatRepLine_LdatType` |  |  |  |
| 72 | `RE.SRL.LDAT.EXT.DUP` | `ReStatRepLine_LdatExtDup` |  |  |  |
| 73 | `RE.SRL.LDPT.APPLIC` | `ReStatRepLine_LdptApplic` |  |  |  |
| 74 | `RE.SRL.PROFIT1.1` | `ReStatRepLine_Profit11` |  |  |  |
| 75 | `RE.SRL.PROFIT2.1` | `ReStatRepLine_Profit21` |  |  |  |
| 76 | `RE.SRL.PROFIT3.1` | `ReStatRepLine_Profit31` |  |  |  |
| 77 | `RE.SRL.PROFIT4.1` | `ReStatRepLine_Profit41` |  |  |  |
| 78 | `RE.SRL.PROFIT5.1` | `ReStatRepLine_Profit51` |  |  |  |
| 79 | `RE.SRL.PROFIT6.1` | `ReStatRepLine_Profit61` |  |  |  |
| 80 | `RE.SRL.PROFIT7.1` | `ReStatRepLine_Profit71` |  |  |  |
| 81 | `RE.SRL.PROFIT8.1` | `ReStatRepLine_Profit81` |  |  |  |
| 82 | `RE.SRL.PROFIT9.1` | `ReStatRepLine_Profit91` |  |  |  |
| 83 | `RE.SRL.PROFIT10.1` | `ReStatRepLine_Profit101` |  |  |  |
| 84 | `RE.SRL.PROFIT11.1` | `ReStatRepLine_Profit111` |  |  |  |
| 85 | `RE.SRL.PROFIT12.1` | `ReStatRepLine_Profit121` |  |  |  |
| 86 | `RE.SRL.LDPT.CCY` | `ReStatRepLine_LdptCcy` |  |  |  |
| 87 | `RE.SRL.LDPT.EXT.DUP` | `ReStatRepLine_LdptExtDup` |  |  |  |
| 88 | `RE.SRL.OVERRIDE` | `ReStatRepLine_Override` |  |  |  |
| 89 | `RE.SRL.RECORD.STATUS` | `ReStatRepLine_RecordStatus` | String |  |  |
| 90 | `RE.SRL.CURR.NO` | `ReStatRepLine_CurrNo` | String |  |  |
| 91 | `RE.SRL.INPUTTER` | `ReStatRepLine_Inputter` |  |  |  |
| 92 | `RE.SRL.DATE.TIME` | `ReStatRepLine_DateTime` |  |  |  |
| 93 | `RE.SRL.AUTHORISER` | `ReStatRepLine_Authoriser` | String |  |  |
| 94 | `RE.SRL.CO.CODE` | `ReStatRepLine_CoCode` | String |  |  |
| 95 | `RE.SRL.DEPT.CODE` | `ReStatRepLine_DeptCode` | String |  |  |
| 96 | `RE.SRL.AUDITOR.CODE` | `ReStatRepLine_AuditorCode` | String |  |  |
| 97 | `RE.SRL.AUDIT.DATE.TIME` | `ReStatRepLine_AuditDateTime` | String |  |  |
