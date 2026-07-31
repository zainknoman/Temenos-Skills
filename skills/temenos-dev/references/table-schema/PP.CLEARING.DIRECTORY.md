# PP.CLEARING.DIRECTORY — Table Schema

> Source: `INSERTS/I_F.PP.CLEARING.DIRECTORY` in `PP_ClearingFrameworkService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CLD.CompanyID` | `PpClearingDirectory_Companyid` | TField |  | Indicates the company ID for which the record is created. Example BNK,GB1 Validation Rules: NoInput Field. 3 alphanumeric characters. The value gets Auto populated based on the company that you login |
| 2 | `PP.CLD.BICCode` | `PpClearingDirectory_Biccode` | TField |  | This is the unique BIC related to the institution from the BIC Directory. � institution code (4 char) � country code (2 char) � location code (2 char) � branch code (3 char � XXX for main office) Validation Rules: The value links to field 'BICCODE' in PPT.BICTABLE. |
| 3 | `PP.CLD.Receiver` | `PpClearingDirectory_Receiver` | TField |  | BIC to be used in the header of the SWIFT message. Validation Rules: The value links to field 'BICCODE' in PPT.BICTABLE. |
| 4 | `PP.CLD.AccountHolder` | `PpClearingDirectory_Accountholder` | TField |  | BIC identifying the settlement bank. Validation Rules: The value links to field 'BICCODE' in PPT.BICTABLE. |
| 5 | `PP.CLD.InstitutionName` | `PpClearingDirectory_Institutionname` | TField |  | Participant�s company name. This field can hold upto 65 alphanumeric characters and the value is not editable by the user. |
| 6 | `PP.CLD.CityHeading` | `PpClearingDirectory_Cityheading` | TField |  | Participant�s establishment. |
| 7 | `PP.CLD.ParticipationType` | `PpClearingDirectory_Participationtype` | TField |  | Validation Rules: DP - direct participant IP - indirect participant |
| 8 | `PP.CLD.NationalClearingCode` | `PpClearingDirectory_Nationalclearingcode` | TField |  | The National identifier of the institution/branch . |
| 9 | `PP.CLD.CTReachability` | `PpClearingDirectory_Ctreachability` | TField |  | Reachability for Credit Transfers Validation Rules: Y - reachable N - not reachable |
| 10 | `PP.CLD.DDReachability` | `PpClearingDirectory_Ddreachability` | TField |  | Reachability for Direct Debit Transfers Validation Rules: Y - reachable N - not reachable |
| 11 | `PP.CLD.FastDDReachability` | `PpClearingDirectory_Fastddreachability` | TField |  | Reachability for CORE Direct Debit Transfers Validation Rules: Y - reachable N - not reachable |
| 12 | `PP.CLD.B2BReachability` | `PpClearingDirectory_B2breachability` | TField |  |  |
| 13 | `PP.CLD.StartDate` | `PpClearingDirectory_Startdate` | TField |  |  |
| 14 | `PP.CLD.EndDate` | `PpClearingDirectory_Enddate` | TField |  |  |
| 15 | `PP.CLD.OverrideThroughUpload` | `PpClearingDirectory_Overridethroughupload` | TField |  | If this field is �N� then it implies that the data entry will never be updated by the upload process. If set to �Y� then the data can be overridden by the upload process. |
| 16 | `PP.CLD.StateOrTerritory` | `PpClearingDirectory_Stateorterritory` | TField |  |  |
| 17 | `PP.CLD.FundsStlmntOnly` | `PpClearingDirectory_Fundsstlmntonly` | TField |  |  |
| 18 | `PP.CLD.FundsTrnsStatus` | `PpClearingDirectory_Fundstrnsstatus` | TField |  |  |
| 19 | `PP.CLD.RESERVED.2` | `PpClearingDirectory_Reserved2` | TField |  |  |
| 20 | `PP.CLD.RESERVED.1` | `PpClearingDirectory_Reserved1` | TField |  |  |
| 21 | `PP.CLD.LOCAL.REF` | `PpClearingDirectory_LocalRef` |  |  |  |
| 22 | `PP.CLD.OVERRIDE` | `PpClearingDirectory_Override` |  |  |  |
| 23 | `PP.CLD.RECORD.STATUS` | `PpClearingDirectory_RecordStatus` | String |  |  |
| 24 | `PP.CLD.CURR.NO` | `PpClearingDirectory_CurrNo` | String |  |  |
| 25 | `PP.CLD.INPUTTER` | `PpClearingDirectory_Inputter` |  |  |  |
| 26 | `PP.CLD.DATE.TIME` | `PpClearingDirectory_DateTime` |  |  |  |
| 27 | `PP.CLD.AUTHORISER` | `PpClearingDirectory_Authoriser` | String |  |  |
| 28 | `PP.CLD.CO.CODE` | `PpClearingDirectory_CoCode` | String |  |  |
| 29 | `PP.CLD.DEPT.CODE` | `PpClearingDirectory_DeptCode` | String |  |  |
| 30 | `PP.CLD.AUDITOR.CODE` | `PpClearingDirectory_AuditorCode` | String |  |  |
| 31 | `PP.CLD.AUDIT.DATE.TIME` | `PpClearingDirectory_AuditDateTime` | String |  |  |
