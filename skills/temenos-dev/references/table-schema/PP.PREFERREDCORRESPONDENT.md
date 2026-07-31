# PP.PREFERREDCORRESPONDENT — Table Schema

> Source: `INSERTS/I_F.PP.PREFERREDCORRESPONDENT` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.PCT.CompanyID` | `PpPreferredcorrespondent_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. Its defaulted automatically and is a no input field |
| 2 | `PP.PCT.DestinationCountryCode` | `PpPreferredcorrespondent_Destinationcountrycode` | TField | Yes | Indicates the country Code for the Destination country. Validation Rules: Mandatory field. 2 alphanumeric characters. The value links to COUNTRY. |
| 3 | `PP.PCT.TransactionCurrency` | `PpPreferredcorrespondent_Transactioncurrency` | TField | Yes | Defines the currency of the transaction. Validation rules: Mandatory field. The value links to field 'CurrencyCode' in PP.CURRENCY. Defaulted to '*', if no value is defined. |
| 4 | `PP.PCT.RoutingProduct` | `PpPreferredcorrespondent_Routingproduct` | TField | Yes | Specifies the routing product based on which a contract can be selected. Validation rules: Mandatory field. Defaulted to '*', if no value is defined. |
| 5 | `PP.PCT.StartDate` | `PpPreferredcorrespondent_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. |
| 6 | `PP.PCT.PrefCorrespondentIDType` | `PpPreferredcorrespondent_Prefcorrespondentidtype` | TField |  | Indicates if the preferred correspondent is identified using a National Clearing Code or BIC. Possible values: B - BIC N - NCC |
| 7 | `PP.PCT.PrefCorrespondentID` | `PpPreferredcorrespondent_Prefcorrespondentid` | TField | Yes | Specifies either BIC or NCC of the preferred correspondant. Validation Rules: Mandatory field. 35 alphanumeric characters. |
| 8 | `PP.PCT.EndDate` | `PpPreferredcorrespondent_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 9 | `PP.PCT.RESERVED.5` | `PpPreferredcorrespondent_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 10 | `PP.PCT.RESERVED.4` | `PpPreferredcorrespondent_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 11 | `PP.PCT.RESERVED.3` | `PpPreferredcorrespondent_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 12 | `PP.PCT.RESERVED.2` | `PpPreferredcorrespondent_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 13 | `PP.PCT.RESERVED.1` | `PpPreferredcorrespondent_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 14 | `PP.PCT.DefineQuota` | `PpPreferredcorrespondent_Definequota` | TField |  | This field defines whether quota definition is applicable for the said Country and Currency. This field must be set to �Yes� if the user wants to define quota when there are more than one Nostro correspondents present per Currency |
| 15 | `PP.PCT.CorrespondentIDType` | `PpPreferredcorrespondent_Correspondentidtype` |  |  |  |
| 16 | `PP.PCT.CorrespondentID` | `PpPreferredcorrespondent_Correspondentid` |  |  |  |
| 17 | `PP.PCT.MessageType` | `PpPreferredcorrespondent_Messagetype` |  |  |  |
| 18 | `PP.PCT.PercentageAllotted` | `PpPreferredcorrespondent_Percentageallotted` |  |  |  |
| 19 | `PP.PCT.CountAllotted` | `PpPreferredcorrespondent_Countallotted` |  |  |  |
| 20 | `PP.PCT.CountPriority` | `PpPreferredcorrespondent_Countpriority` |  |  |  |
| 21 | `PP.PCT.AmountFrom` | `PpPreferredcorrespondent_Amountfrom` |  |  |  |
| 22 | `PP.PCT.AmountTo` | `PpPreferredcorrespondent_Amountto` |  |  |  |
| 23 | `PP.PCT.QuotaAPI` | `PpPreferredcorrespondent_Quotaapi` | TField |  | This is the API which performs the functionality of Quota Allocation Reserved for future use |
| 24 | `PP.PCT.ResetFrequency` | `PpPreferredcorrespondent_Resetfrequency` | TField |  | The value in this field indicates the frequency in which the Quota utilization must be reset |
| 25 | `PP.PCT.LOCAL.REF` | `PpPreferredcorrespondent_LocalRef` |  |  |  |
| 26 | `PP.PCT.LinkID` | `PpPreferredcorrespondent_Linkid` | TField |  | Standard T24 String. No Input Field This field gets updated after authorisation of the record. This field contains the ID of the .PDS table. It contains ConcatID-BusinessDate. |
| 27 | `PP.PCT.OVERRIDE` | `PpPreferredcorrespondent_Override` |  |  |  |
| 28 | `PP.PCT.RECORD.STATUS` | `PpPreferredcorrespondent_RecordStatus` | String |  |  |
| 29 | `PP.PCT.CURR.NO` | `PpPreferredcorrespondent_CurrNo` | String |  |  |
| 30 | `PP.PCT.INPUTTER` | `PpPreferredcorrespondent_Inputter` |  |  |  |
| 31 | `PP.PCT.DATE.TIME` | `PpPreferredcorrespondent_DateTime` |  |  |  |
| 32 | `PP.PCT.AUTHORISER` | `PpPreferredcorrespondent_Authoriser` | String |  |  |
| 33 | `PP.PCT.CO.CODE` | `PpPreferredcorrespondent_CoCode` | String |  |  |
| 34 | `PP.PCT.DEPT.CODE` | `PpPreferredcorrespondent_DeptCode` | String |  |  |
| 35 | `PP.PCT.AUDITOR.CODE` | `PpPreferredcorrespondent_AuditorCode` | String |  |  |
| 36 | `PP.PCT.AUDIT.DATE.TIME` | `PpPreferredcorrespondent_AuditDateTime` | String |  |  |
