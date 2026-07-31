# CAPL.H.CAF.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.H.CAF.PARAM` in `CABASE_ATMFoundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.CAF.SEL.CRITERIA` | `CaplHCafParam_SelCriteria` |  |  |  |
| 2 | `CP.CAF.FILE.DELIM` | `CaplHCafParam_FileDelim` | TField |  | This field used to define the delimiter which will be used as a seperator between two field values on the caf extracts.Validation: It is a free text field.Eg: , |
| 3 | `CP.CAF.CAF.FILE.NAME` | `CaplHCafParam_CafFileName` |  |  |  |
| 4 | `CP.CAF.OUT.FILE.NAME` | `CaplHCafParam_OutFileName` |  |  |  |
| 5 | `CP.CAF.OUT.PATH` | `CaplHCafParam_OutPath` | TField |  | This field used to define output directory path where the CAF extract needs to be generated.Validation: It is a free text field.Eg: CAF.OUT |
| 6 | `CP.CAF.CAF.TYPE` | `CaplHCafParam_CafType` | TField | Yes | This field used to indicate whether define the type of CAF extract is Full or Partial. This is used as a Indicator when sending the CAF extract. This field will be used only if the switch is EverlinkValidation: The values from this field will be fetched from EB.LOOKUP which will have VIRTUAL.TABLE value as CAF.TYPE.0 - Full CAF1 - Partial CAFIf the value is 1 then EFFECTIVE.DATE field is mandatory |
| 7 | `CP.CAF.START.PAN.NO` | `CaplHCafParam_StartPanNo` | TField |  | This field used to indicate the Starting number of the range of the PAN no to be included for the CAF updates. This field will be used only if the switch is EverlinkEg: 1000000000000000000 We have to say which fields are used by Everlink/dcp |
| 8 | `CP.CAF.END.PAN.NO` | `CaplHCafParam_EndPanNo` | TField |  | This field used to indicate the ending number of the range of the PAN no to be included for the CAF updates. This field will be used only if the switch is EverlinkEg: 9999999999999999999 |
| 9 | `CP.CAF.CARD.TYPE` | `CaplHCafParam_CardType` |  |  |  |
| 10 | `CP.CAF.CARD.STATUS` | `CaplHCafParam_CardStatus` |  |  |  |
| 11 | `CP.CAF.DATA.COMPANY` | `CaplHCafParam_DataCompany` |  |  |  |
| 12 | `CP.CAF.EFFECTIVE.DATE` | `CaplHCafParam_EffectiveDate` | TField |  | This field used to hold the date of partial CAF extraction for the last time. So while running the partial CAF service for the next time the cards which are getting updated after this date only will be extracted.Validation: It is a date field.Eg: 20181231 |
| 13 | `CP.CAF.FILE.NETWORK` | `CaplHCafParam_FileNetwork` | TField |  |  |
| 14 | `CP.CAF.NO.OF.ACCTS` | `CaplHCafParam_NoOfAccts` | TField |  | This field used to define a value to denote the maximum number of accounts from a CARD.ISSUE record can be extracted as a part of CAF. So that accounts alone will be accessed through ATM/POS channel. It is a numeric fieldEg: 10 |
| 15 | `CP.CAF.CUST.STATUS` | `CaplHCafParam_CustStatus` |  |  |  |
| 16 | `CP.CAF.ISSUE.NUMBER` | `CaplHCafParam_IssueNumber` | TField |  | This Field used to define the sequence number to be used while doing the bulk order of card.Validation: It is a numeric field.Eg: 0 |
| 17 | `CP.CAF.LOCAL.REF` | `CaplHCafParam_LocalRef` |  |  |  |
| 18 | `CP.CAF.OVERRIDE` | `CaplHCafParam_Override` |  |  |  |
| 19 | `CP.CAF.START.DATE.TIME` | `CaplHCafParam_StartDateTime` |  |  |  |
| 20 | `CP.CAF.END.DATE.TIME` | `CaplHCafParam_EndDateTime` |  |  |  |
| 21 | `CP.CAF.EXC.CUST.PSN` | `CaplHCafParam_ExcCustPsn` | TField |  |  |
| 22 | `CP.CAF.C1.NAME.ON.CARD` | `CaplHCafParam_C1NameOnCard` | TField |  | Purpose of the field is to display the card naming information in FHM /CAF extracts.Allowed inputs:CustomerCard NameNoneNone - System will send customer name as blank as part of the extract.Customer-FIRST.NAME and LAST .NAME > CUSTOMER will be mapped for card naming information in the extract. (up to 26 characters)Card name-NAME.ON.CRD > CARD.ISSUE will be mapped for card naming information in the extract.Note: In case if FI wants special characters to be sent in customer same to be configured with necessary setup in ASCII.VAL.TABLE used for CARD.NAME. |
| 23 | `CP.CAF.ACCT.DESCRIPTION` | `CaplHCafParam_AcctDescription` | TField |  | Fields holds as ACCT.ALT.TITLE or ACCT.TITLE values.If this fields defined as ACCT.TITLE then system inform "AccountId\| Account name" part of Accounts CAF extract.If this fields defined as ACCT.ALT.TITLE then system inform "AccountId\| Account name - 3 digit Alternate Id" part of Accounts CAF extract |
| 24 | `CP.CAF.CAF.BR.CDE.LEN` | `CaplHCafParam_CafBrCdeLen` | TField |  | Fields holds the length of the Branch code |
| 25 | `CP.CAF.BRANCH.CODE` | `CaplHCafParam_BranchCode` | TField |  | Fields holds COMPANY.CODE or TRANSIT valueIf the field is defined as COMPANY.CODE then value from CARD.ISSUE>DEST.CO.CODE field to be shown in CAF extractIf the field is defined as TRANSIT then the value from COMPANY>BC.SORT.CODE to be shown in CAF extractBranch code length in CAF extract is based on CAF.BR.CDE.LEN field. |
| 26 | `CP.CAF.ACCT.LEN` | `CaplHCafParam_AcctLen` | TField |  | Fields holds Account LengthIf the field is defined with number upto which the account number to be shown in CAF extract |
| 27 | `CP.CAF.NO.EXPIRY.DAY` | `CaplHCafParam_NoExpiryDay` | TField |  | Field to decide whether EXPIRY.DAY field in extended fields of CAF for card should be extracted or should be blank. Possible values are YES, NO, None YES - The EXPIRY.DAY value in CAF extract should be blank NO/None - The EXPIRY.DAY value should be extracted. |
| 28 | `CP.CAF.ACCT.TYPE.PRIORITY` | `CaplHCafParam_AcctTypePriority` | TField |  | Based on the setup in CAPL.H.CAF.PARAM>ACCT.TYPE.PRIORITY, the Account type will be displayed during file extractionIf ACCT.TYPE.PRIORITY is 'BLANK' - Account type will be mapped from CARD.ACS.DEF>EN.FLAGIf ACCT.TYPE.PRIORITY is Card - Account type will be mapped from CARD.ACCESS>EN.FLAG |
| 29 | `CP.CAF.CUST.ID.API` | `CaplHCafParam_CustIdApi` | TField |  | This field used to define the CARD.STATUS records which needs to be included in the FHM request messages.It should be a valid record from CARD.STATUS table.It a multi value field. |
| 30 | `CP.CAF.CARD.NAME` | `CaplHCafParam_CardName` | TField |  | This field takes the value from EB.LOOKUP>CARD.NAME*Multifirstname. When the CARD.NAME is parameterised,and if the total length of the name (given name + family name) exceeds 26 characters,the middle name should be truncated with first character.Ex :GIVEN NAME : CHERYL ANNE BESANT LYNDEEFAMILY NAME : LINSTEADO/P will be CHERYL A B L LINSTEAD |
| 31 | `CP.CAF.RECORD.STATUS` | `CaplHCafParam_RecordStatus` | String |  |  |
| 32 | `CP.CAF.CURR.NO` | `CaplHCafParam_CurrNo` | String |  |  |
| 33 | `CP.CAF.INPUTTER` | `CaplHCafParam_Inputter` |  |  |  |
| 34 | `CP.CAF.DATE.TIME` | `CaplHCafParam_DateTime` |  |  |  |
| 35 | `CP.CAF.AUTHORISER` | `CaplHCafParam_Authoriser` | String |  |  |
| 36 | `CP.CAF.CO.CODE` | `CaplHCafParam_CoCode` | String |  |  |
| 37 | `CP.CAF.DEPT.CODE` | `CaplHCafParam_DeptCode` | String |  |  |
| 38 | `CP.CAF.AUDITOR.CODE` | `CaplHCafParam_AuditorCode` | String |  |  |
| 39 | `CP.CAF.AUDIT.DATE.TIME` | `CaplHCafParam_AuditDateTime` | String |  |  |
