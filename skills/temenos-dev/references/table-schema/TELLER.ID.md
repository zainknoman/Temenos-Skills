# TELLER.ID — Table Schema

> Source: `INSERTS/I_F.TELLER.ID` in `TT_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TT.TID.STATUS` | `TellerId_Status` | TField | No | Defines the status of the teller position. Transactions can only be entered when the teller position is open and a user has been assigned to a till. The vault (defined on the TELLER.PARAMETER file) cannot be opened or closed, hence transfers can take place to and from the vault regardless of status. When closing the till the user will be prompted for the current till balance (TILL.BALANCE) and any differences (vs the TILL.CLOS.BAL - the current system balance) will be reported and can be optionally posted to the over &amp; short accounts. When opening the till the current system balance(s) must match the TILL.BALANCE otherwise the till cannot be opened. The difference must be rectified by transfers from Data Capture. Validation Rules: O OPEN C CLOSED |
| 2 | `TT.TID.USER` | `TellerId_User` | TField |  | Specifies the id of the user that has been assigned to this till. Only this user will be allowed to perform Input, Reverse, Delete etc to this till. Must be a valid entry on the USER file. A user cannot be assigned to two open tills at any one time. Validation Rules: 16 Alphanumeric characters. (Noinput when the status is close) |
| 3 | `TT.TID.DATE.OF.OPEN` | `TellerId_DateOfOpen` | TField |  | Specifies the (bank) date when the till was opened. Maintained automatically by the system. Validation Rules: 8 Date type characters (YYYYMMDD). (Noinput field) |
| 4 | `TT.TID.TIME.OF.OPEN` | `TellerId_TimeOfOpen` | TField |  | Specifies the time when the till was opened. Automatically updated by the system. Validation Rules: 4 Numeric characters (HHMM). (Noinput field) |
| 5 | `TT.TID.DATE.OF.CLOSE` | `TellerId_DateOfClose` | TField |  | Specifies the date when the till was closed. Automatically updated by the system. Validation Rules: 8 Date type characters (YYYYMMDD). (Noinput field) |
| 6 | `TT.TID.TIME.OF.CLOSE` | `TellerId_TimeOfClose` | TField |  | Specifies the time when the till was closed. Automatically updated by the system. Validation Rules: 4 Numeric characters (HHMM). (Noinput field) |
| 7 | `TT.TID.CATEGORY` | `TellerId_Category` |  |  |  |
| 8 | `TT.TID.CURRENCY` | `TellerId_Currency` |  |  |  |
| 9 | `TT.TID.OPENING.BALANCE` | `TellerId_OpeningBalance` |  |  |  |
| 10 | `TT.TID.TILL.CLOS.BAL` | `TellerId_TillClosBal` |  |  |  |
| 11 | `TT.TID.TILL.BALANCE` | `TellerId_TillBalance` |  |  |  |
| 12 | `TT.TID.DENOMINATION` | `TellerId_Denomination` |  |  |  |
| 13 | `TT.TID.UNIT` | `TellerId_Unit` |  |  |  |
| 14 | `TT.TID.DIFFERENCE` | `TellerId_Difference` |  |  |  |
| 15 | `TT.TID.NOTES` | `TellerId_Notes` |  |  |  |
| 16 | `TT.TID.AUTOCASH.DEVICE` | `TellerId_AutocashDevice` | TField |  | Identification of autocash device installed at the teller position. Currently the only supported autocash device is a Nixdorf AKT. This field should contain the Identification Number of the AKT or be left blank if an AKT is not installed. If input, the current messages supported are OPEN, CLOSE, WITHDRAW, UNLOCK and PAID OUT. See Autocash &amp; Denomination processing in the Retail Bank module description. Validation Rules: 9 Alphanumeric |
| 17 | `TT.TID.PASSBOOK.DEVICE` | `TellerId_PassbookDevice` | TField |  | This field is used to indicate to the system that the Teller has a connection to a Passbook printer, which could be physically attached to their workstation or accessible via a Network connection. The model number or make of the passbook device should be entered here and should match the name used in PRINTER.ID. Where printer commands are to be sent to the Passbook printer this name will be used to find the record on PRINTER.ATTRIBUTES together with the settings from TELLER.PASSBOOK field called ATTRIBUTE. Example If we have a Passbook printer such as the Siemens HighPrint 4905 which needs a set of initialisation sequences to set the font, spacing etc. We would set the following values: Application Field Data PRINTER.ID @ID SIEMENHP TELLER.ID PASSBOOK.DEVICE SIEMENHP TELLER.PASSBOOK ATTRIBUTE INIT PRINTER.ATTRIBUTES @ID SIEMENHP.INIT Passbook updating will only take place if this field has been entered and the associated Printing files have been created. Validation Rules: 9 Alphanumeric |
| 18 | `TT.TID.TELLER.OFFICE` | `TellerId_TellerOffice` | TField | No | Holds the department or branch id, as defined in DEPT.ACCT.OFFICER, to which the teller position belongs. Normally used to allocate teller positions to a specific branch. This can then be used to output branch specific information on the deal slip or passbook, ie an address or branch code. This mechanism should be used rather than relying on the DEPARTMENT CODE on the USER file as an individual could be required to work in more than one branch. Validation Rules: 4 Numeric (Optional) Must be a valid key on the DEPT.ACCT.OFFICER file. |
| 19 | `TT.TID.DEALER.DESK` | `TellerId_DealerDesk` | TField | No | Indicates the dealer desk to which this Teller belongs. Optional input Validation Rules: Must be a valid record in the table DEALER.DESK |
| 20 | `TT.TID.LINKED.TILLS` | `TellerId_LinkedTills` |  |  |  |
| 21 | `TT.TID.TILL.TFR.ONLY` | `TellerId_TillTfrOnly` | TField |  | TELLER. ID TILL. TFR. ONLY Input in the field is either Yes or " " If input as Yes - the teller id of this record can be used for doing till-to-till transfers only. If left blank then only the usual restrictions on transactions apply. Validation Rules: can be Yes or " " |
| 22 | `TT.TID.STOCK.UPD` | `TellerId_StockUpd` | TField |  | Field to indicate if denomination units inputted in TELLER.ID during till closure treat this as final stock with teller and overwrite the TT.STOCK.CONTROL Can hold values YES or null. Default value from TELLER.PARAMETER. If the value is YES update the TT.STOCK.CONTROL according to the denomination units and TC serial numbers entered in TELLER.ID during till closure If the value is null it�s an exising functionality which will raise an override to the extent of shortage/overage of balances and raise an entry to that extent but not update TT.STOCK.CONTROL. |
| 23 | `TT.TID.TILL.LIMIT` | `TellerId_TillLimit` | TField |  | This field is to indicate whether the TILL level LIMIT definition is to be setup for respective tills It can hold values YES or NO and the default would be NO This is a control field to indicate that limit checking has been enabled for the respective TELLER.ID and this mandates the definition of limit related fields |
| 24 | `TT.TID.LIMIT.CATEGORY` | `TellerId_LimitCategory` |  |  |  |
| 25 | `TT.TID.EXCLUDE.CCY` | `TellerId_ExcludeCcy` |  |  |  |
| 26 | `TT.TID.DEF.FCY.EQV.LIM` | `TellerId_DefFcyEqvLim` |  |  |  |
| 27 | `TT.TID.LOCAL.CCY.LIMIT` | `TellerId_LocalCcyLimit` |  |  |  |
| 28 | `TT.TID.LIMIT.CCY` | `TellerId_LimitCcy` |  |  |  |
| 29 | `TT.TID.LIMIT.AMT` | `TellerId_LimitAmt` |  |  |  |
| 30 | `TT.TID.OVER.CATEGORY` | `TellerId_OverCategory` | TField |  |  |
| 31 | `TT.TID.SHORT.CATEGORY` | `TellerId_ShortCategory` | TField |  |  |
| 32 | `TT.TID.RESERVED.4` | `TellerId_Reserved4` | TField |  | Validation Rules: |
| 33 | `TT.TID.RESERVED.3` | `TellerId_Reserved3` | TField |  |  |
| 34 | `TT.TID.RESERVED.2` | `TellerId_Reserved2` | TField |  |  |
| 35 | `TT.TID.RESERVED.1` | `TellerId_Reserved1` | TField |  |  |
| 36 | `TT.TID.LOCAL.REF` | `TellerId_LocalRef` |  |  |  |
| 37 | `TT.TID.STMT.NO` | `TellerId_StmtNo` |  |  |  |
| 38 | `TT.TID.OVERRIDE` | `TellerId_Override` |  |  |  |
| 39 | `TT.TID.RECORD.STATUS` | `TellerId_RecordStatus` | String |  |  |
| 40 | `TT.TID.CURR.NO` | `TellerId_CurrNo` | String |  |  |
| 41 | `TT.TID.INPUTTER` | `TellerId_Inputter` |  |  |  |
| 42 | `TT.TID.DATE.TIME` | `TellerId_DateTime` |  |  |  |
| 43 | `TT.TID.AUTHORISER` | `TellerId_Authoriser` | String |  |  |
| 44 | `TT.TID.CO.CODE` | `TellerId_CoCode` | String |  |  |
| 45 | `TT.TID.DEPT.CODE` | `TellerId_DeptCode` | String |  |  |
| 46 | `TT.TID.AUDITOR.CODE` | `TellerId_AuditorCode` | String |  |  |
| 47 | `TT.TID.AUDIT.DATE.TIME` | `TellerId_AuditDateTime` | String |  |  |
