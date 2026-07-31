# SEPA.PEACH — Table Schema

> Source: `INSERTS/I_F.SEPA.PEACH` in `EP_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.PEA.NAME` | `SepaPeach_Name` |  |  |  |
| 2 | `SEP.PEA.COMMENT` | `SepaPeach_Comment` |  |  |  |
| 3 | `SEP.PEA.BIC.CODE` | `SepaPeach_BicCode` | A (Alphanumeric) |  | This field has the BIC identification of the the PE-ACH center. Valid BIC identification / SWIFT Code of the PE-ACH. e.g. &apos;EBATBEBBXXX&apos; is for EBA CLEARING, &apos;MARKDEFFXXX&apos; is for Bundesbank, Germany. Used for populating the Destination tag &lt;RcvgInst&gt; in the outward XML. Validation rule Value upto 11 type A(Alphanumeric) |
| 4 | `SEP.PEA.MSG.NATURE` | `SepaPeach_MsgNature` |  |  |  |
| 5 | `SEP.PEA.ACCT.NUMBER` | `SepaPeach_AcctNumber` |  |  |  |
| 6 | `SEP.PEA.IBAN.NUMBER` | `SepaPeach_IbanNumber` |  |  |  |
| 7 | `SEP.PEA.LAST.OUT.NUMBER` | `SepaPeach_LastOutNumber` |  |  |  |
| 8 | `SEP.PEA.SERVICE.ID` | `SepaPeach_ServiceId` |  |  |  |
| 9 | `SEP.PEA.CLEAR.SYSTEM.ID` | `SepaPeach_ClearSystemId` | A (Alphanumeric) |  | The Field holds the value of the Identifier of the the Clearing System. This is the Proprietary identification of the Clearing System. (e.g value for EBA STEP2 is &apos;ST2&apos;). This field is used to fill the tag &lt;Prtry&gt; in the below path of the outward message. &lt;GrpHdr&gt;*&lt;SttlmInf&gt;*&lt;ClrSys&gt;*&lt;Prtry&gt; Validation rule Value upto 35 type A(Alphanumeric) |
| 10 | `SEP.PEA.FILE.NO` | `SepaPeach_FileNo` | N (Numeric) |  | Field holds the Number of files posted on the given file date, no input is allowed in this field and get Updated while generating the outward XML file. Validation rule Value upto 6 type N(Numeric) and NOINPUT field |
| 11 | `SEP.PEA.FILE.DATE` | `SepaPeach_FileDate` | A (Alphanumeric) |  | This field holds the Date on which last file is posted to the PE-ACH, and no input is allowed. This field is Updated while generating the outward XML file. Validation rule Value upto 8 type A(Alphanumeric)and NOINPUT field |
| 12 | `SEP.PEA.FILE.NAME.CRT.RTN` | `SepaPeach_FileNameCrtRtn` | A (Alphanumeric) |  | Field contains the Routine name prefixed with @. It will get executed when the outward file is created. This routine creates the File Name in the format specified by the PE-ACH. In addition, a specific sub-directory could be set by this routine where the outward generated SEPA file will be stored Validation rule Value upto 45 type A(Alphanumeric) |
| 13 | `SEP.PEA.SDD.FILE.PER.TYPE` | `SepaPeach_SddFilePerType` | TField |  | The SEPA module should be able to generate different file for the SEPA Direct Debits of the �Core�- and the �B2B�-type. This is not needed by every PE-ACH. Therefore this flag on PE-ACH-level should be added to decide whether the module should generate different files for the two different SEPA Direct Debit types, or not. Possible Values : Yes or No &apos;YES&apos; = Outward XML is generated per SDD Type &apos;NO&apos; = No separate XML file per SDD type. Both CORE and B2B will be generated in one file. &apos;NONE&apos; = Same as &apos;NO&apos; Validation rule Value upto 3 and User can Input only &apos;YES&apos; or &apos;NO&apos; |
| 14 | `SEP.PEA.BULKING.ALLOWED` | `SepaPeach_BulkingAllowed` | TField |  | This Field specifies whether Bulking is allowed or not by specifying either &apos;YES&apos; or &apos;NO&apos; .Not each PE-ACH supports more than one bulk in the SEPA XML file. For example PE-ACH �Equens�, does only allow one bulk per SEPA XML File. For that reason it should be possible to parameterize per PE-ACH, if bulking is allowed or not. Validation rule Value upto 3 and User can Input only &apos;YES&apos; or &apos;NO&apos; |
| 15 | `SEP.PEA.XML.WITH.CRLF` | `SepaPeach_XmlWithCrlf` | TField |  | This Field specifies if the XML file has to be generested with/without CRLF Validation Rules Value upto 3 Values allowed are YES or NO |
| 16 | `SEP.PEA.PEACH.NAME` | `SepaPeach_PeachName` | TField | Yes | This Field specifies the name of the PEACH. Validation Rules Value upto 10 and mandatory field Values allowed are EBA, BUBA and EQUENS |
| 17 | `SEP.PEA.RESERVED.2` | `SepaPeach_Reserved2` | TField |  |  |
| 18 | `SEP.PEA.RESERVED.1` | `SepaPeach_Reserved1` | TField |  |  |
| 19 | `SEP.PEA.LOCAL.REF` | `SepaPeach_LocalRef` |  |  |  |
| 20 | `SEP.PEA.OVERRIDE` | `SepaPeach_Override` |  |  |  |
| 21 | `SEP.PEA.RECORD.STATUS` | `SepaPeach_RecordStatus` | String |  |  |
| 22 | `SEP.PEA.CURR.NO` | `SepaPeach_CurrNo` | String |  |  |
| 23 | `SEP.PEA.INPUTTER` | `SepaPeach_Inputter` |  |  |  |
| 24 | `SEP.PEA.DATE.TIME` | `SepaPeach_DateTime` |  |  |  |
| 25 | `SEP.PEA.AUTHORISER` | `SepaPeach_Authoriser` | String |  |  |
| 26 | `SEP.PEA.CO.CODE` | `SepaPeach_CoCode` | String |  |  |
| 27 | `SEP.PEA.DEPT.CODE` | `SepaPeach_DeptCode` | String |  |  |
| 28 | `SEP.PEA.AUDITOR.CODE` | `SepaPeach_AuditorCode` | String |  |  |
| 29 | `SEP.PEA.AUDIT.DATE.TIME` | `SepaPeach_AuditDateTime` | String |  |  |
