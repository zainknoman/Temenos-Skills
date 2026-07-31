# PP.CLEARINGCORRESPONDENTS — Table Schema

> Source: `INSERTS/I_F.PP.CLEARINGCORRESPONDENTS` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CGC.CompanyID` | `PpClearingcorrespondents_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: NOINPUT Field 3 alphanumeric characters. The value gets autopopulated on validation based on the company that you login |
| 2 | `PP.CGC.BICCodeCorrespondent` | `PpClearingcorrespondents_Biccodecorrespondent` | TField | Yes | Holds the BIC of the correspondent bank that will act as a Direct Participant of the clearing on behalf of the company. Validation Rules: Mandatory field. 35 alphanumeric characters. |
| 3 | `PP.CGC.StartDate` | `PpClearingcorrespondents_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. |
| 4 | `PP.CGC.EndDate` | `PpClearingcorrespondents_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 5 | `PP.CGC.CorrespondentNCC` | `PpClearingcorrespondents_Correspondentncc` | TField |  | Holds the NCC of the correspondent bank. It is no inputtable field. Value will be defaulted from the ID Validation Rules: Valid entry in PPT.BANKCODE table |
| 6 | `PP.CGC.ClearingCurrency` | `PpClearingcorrespondents_Clearingcurrency` | TField |  |  |
| 7 | `PP.CGC.AccountCompany` | `PpClearingcorrespondents_Accountcompany` | TField |  | Holds the Vostro Account Company Id of the Clearing correspondent or Indirect Participant It is no inputtable field. Value will be defaulted from the current company Id |
| 8 | `PP.CGC.AccountNumber` | `PpClearingcorrespondents_Accountnumber` | TField | Yes | Holds the Vostro Account Number of the Clearing correspondent or Indirect Participant Validation Rules: Mandatory field when Clearing currency entered in ID |
| 9 | `PP.CGC.AccountCurrency` | `PpClearingcorrespondents_Accountcurrency` | TField |  | Holds the Vostro Account Currency of the Clearing correspondent or Indirect Participant It is no inputtable field. Value will be defaulted from Clearing Currency that entered in the ID |
| 10 | `PP.CGC.LOCAL.REF` | `PpClearingcorrespondents_LocalRef` |  |  |  |
| 11 | `PP.CGC.OVERRIDE` | `PpClearingcorrespondents_Override` |  |  |  |
| 12 | `PP.CGC.RECORD.STATUS` | `PpClearingcorrespondents_RecordStatus` | String |  |  |
| 13 | `PP.CGC.CURR.NO` | `PpClearingcorrespondents_CurrNo` | String |  |  |
| 14 | `PP.CGC.INPUTTER` | `PpClearingcorrespondents_Inputter` |  |  |  |
| 15 | `PP.CGC.DATE.TIME` | `PpClearingcorrespondents_DateTime` |  |  |  |
| 16 | `PP.CGC.AUTHORISER` | `PpClearingcorrespondents_Authoriser` | String |  |  |
| 17 | `PP.CGC.CO.CODE` | `PpClearingcorrespondents_CoCode` | String |  |  |
| 18 | `PP.CGC.DEPT.CODE` | `PpClearingcorrespondents_DeptCode` | String |  |  |
| 19 | `PP.CGC.AUDITOR.CODE` | `PpClearingcorrespondents_AuditorCode` | String |  |  |
| 20 | `PP.CGC.AUDIT.DATE.TIME` | `PpClearingcorrespondents_AuditDateTime` | String |  |  |
| 21 | `PP.CGC.Maxtransperbulk` | `PpClearingcorrespondents_Maxtransperbulk` | TField |  | Maximum number of transactions in a bulk, allowed to be sent to an IP can be set here |
| 22 | `PP.CGC.Maxbulksperfile` | `PpClearingcorrespondents_Maxbulksperfile` | TField |  | Maximum number of bulks, allowed to be sent to an IP can be set here |
| 23 | `PP.CGC.Maxfilespercycle` | `PpClearingcorrespondents_Maxfilespercycle` | TField |  | Maximum number of files per cycle, allowed to be sent to an IP can be set here |
