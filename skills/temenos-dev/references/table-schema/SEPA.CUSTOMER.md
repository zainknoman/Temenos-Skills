# SEPA.CUSTOMER — Table Schema

> Source: `INSERTS/I_F.SEPA.CUSTOMER` in `EP_InwardProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.CUS.NAME` | `SepaCustomer_Name` |  |  |  |
| 2 | `SEP.CUS.COMMENT` | `SepaCustomer_Comment` |  |  |  |
| 3 | `SEP.CUS.BIC.CODE` | `SepaCustomer_BicCode` | A (Alphanumeric) |  | This Field specifies the BIC identification of a bank type CUSTOMER. Validation Rules Value upto 13 type A(Alphanumeric) |
| 4 | `SEP.CUS.STAT.FREQUENCY` | `SepaCustomer_StatFrequency` | TField | No | This Field holds the Frequency of statistic multi value (see below). Validation Rules Value upto 17 type FQU(Frequency) This field is in two parts. 1) Next Change Date: 1-9 type D (date format in range 1950-2049) characters. Default value calculated by the System depending on change frequency. (Optional input) 2) Change Frequency: 1-5 type SS (uppercase alpha or numeric, first character alpha) characters |
| 5 | `SEP.CUS.SEPA.LAYOUT.ID` | `SepaCustomer_SepaLayoutId` |  |  |  |
| 6 | `SEP.CUS.TRANS.TYPE` | `SepaCustomer_TransType` |  |  |  |
| 7 | `SEP.CUS.CUT.OFF.TIME` | `SepaCustomer_CutOffTime` |  |  |  |
| 8 | `SEP.CUS.ACCT.NUMBER` | `SepaCustomer_AcctNumber` |  |  |  |
| 9 | `SEP.CUS.IBAN.NUMBER` | `SepaCustomer_IbanNumber` |  |  |  |
| 10 | `SEP.CUS.MESS.PERIOD` | `SepaCustomer_MessPeriod` |  |  |  |
| 11 | `SEP.CUS.MESS.NUMBER` | `SepaCustomer_MessNumber` |  |  |  |
| 12 | `SEP.CUS.TRNS.NUMBER` | `SepaCustomer_TrnsNumber` |  |  |  |
| 13 | `SEP.CUS.TRNS.AMOUNT` | `SepaCustomer_TrnsAmount` |  |  |  |
| 14 | `SEP.CUS.FILE.POSTING` | `SepaCustomer_FilePosting` |  |  |  |
| 15 | `SEP.CUS.SERVICE.FLAG` | `SepaCustomer_ServiceFlag` |  |  |  |
| 16 | `SEP.CUS.FWD.CATEG.PURPOSE` | `SepaCustomer_FwdCategPurpose` | TField |  | Validation Rules Value upto 3 User can input only &apos;YES&apos; or &apos;NO&apos; Values can be modified using the EB.LOOKUP with Key SEPA.FWD.CATEG.PURPOSE |
| 17 | `SEP.CUS.ALLOWED.PEACH` | `SepaCustomer_AllowedPeach` | A (Alphanumeric) |  | This field contains the Peach Id in SEPA.PEACH Validation Rules Value upto 15 type A(Alphanumeric) Value should exist in SEPA.PEACH |
| 18 | `SEP.CUS.B2C.GEN.FILE.NAME` | `SepaCustomer_B2cGenFileName` | A (Alphanumeric) |  | Validation Rules Value upto 20 type A(Alphanumeric) |
| 19 | `SEP.CUS.FILE.NUM` | `SepaCustomer_FileNum` | A (Alphanumeric) |  | Validation Rules Value upto 30 type A(Alphanumeric) |
| 20 | `SEP.CUS.IN.DATE` | `SepaCustomer_InDate` |  |  |  |
| 21 | `SEP.CUS.NO.OF.FILES` | `SepaCustomer_NoOfFiles` |  |  |  |
| 22 | `SEP.CUS.NO.OF.TXNS` | `SepaCustomer_NoOfTxns` |  |  |  |
| 23 | `SEP.CUS.XML.WITH.CRLF` | `SepaCustomer_XmlWithCrlf` | TField |  | This Field specifieS if the XML file has to be generested with/without CRLF Validation Rules Value upto 3 Values allowed are YES or NO |
| 24 | `SEP.CUS.ALLOWED.B2C.TXNS` | `SepaCustomer_AllowedB2CTxns` |  |  |  |
| 25 | `SEP.CUS.RESERVED.10` | `SepaCustomer_Reserved10` | TField |  |  |
| 26 | `SEP.CUS.RESERVED.9` | `SepaCustomer_Reserved9` | TField |  |  |
| 27 | `SEP.CUS.RESERVED.8` | `SepaCustomer_Reserved8` | TField |  |  |
| 28 | `SEP.CUS.RESERVED.7` | `SepaCustomer_Reserved7` | TField |  |  |
| 29 | `SEP.CUS.RESERVED.6` | `SepaCustomer_Reserved6` | TField |  |  |
| 30 | `SEP.CUS.RESERVED.5` | `SepaCustomer_Reserved5` | TField |  |  |
| 31 | `SEP.CUS.RESERVED.4` | `SepaCustomer_Reserved4` | TField |  |  |
| 32 | `SEP.CUS.RESERVED.3` | `SepaCustomer_Reserved3` | TField |  |  |
| 33 | `SEP.CUS.RESERVED.2` | `SepaCustomer_Reserved2` | TField |  |  |
| 34 | `SEP.CUS.RESERVED.1` | `SepaCustomer_Reserved1` | TField |  |  |
| 35 | `SEP.CUS.LOCAL.REF` | `SepaCustomer_LocalRef` |  |  |  |
| 36 | `SEP.CUS.OVERRIDE` | `SepaCustomer_Override` |  |  |  |
| 37 | `SEP.CUS.RECORD.STATUS` | `SepaCustomer_RecordStatus` | String |  |  |
| 38 | `SEP.CUS.CURR.NO` | `SepaCustomer_CurrNo` | String |  |  |
| 39 | `SEP.CUS.INPUTTER` | `SepaCustomer_Inputter` |  |  |  |
| 40 | `SEP.CUS.DATE.TIME` | `SepaCustomer_DateTime` |  |  |  |
| 41 | `SEP.CUS.AUTHORISER` | `SepaCustomer_Authoriser` | String |  |  |
| 42 | `SEP.CUS.CO.CODE` | `SepaCustomer_CoCode` | String |  |  |
| 43 | `SEP.CUS.DEPT.CODE` | `SepaCustomer_DeptCode` | String |  |  |
| 44 | `SEP.CUS.AUDITOR.CODE` | `SepaCustomer_AuditorCode` | String |  |  |
| 45 | `SEP.CUS.AUDIT.DATE.TIME` | `SepaCustomer_AuditDateTime` | String |  |  |
