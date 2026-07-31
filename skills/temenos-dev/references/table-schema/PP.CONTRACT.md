# PP.CONTRACT — Table Schema

> Source: `INSERTS/I_F.PP.CONTRACT` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CN.CompanyID` | `PpContract_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: Its defaulted automatically and is a no input field |
| 2 | `PP.CN.StartDate` | `PpContract_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. |
| 3 | `PP.CN.BusinessLine` | `PpContract_Businessline` | TField | Yes | Every company has a number of business lines. Country and Party contracts can be made specific to a business line. Validation Rules: 1) Mandatory. 2) Free Text field. |
| 4 | `PP.CN.ContractType` | `PpContract_Contracttype` | TField | Yes | Contracts can be defined for a credit party of a payment or for the destination country of a payment. A Contract defined for the credit party is called as a PTY Contract and a Contract defined for the destination country is called as a CTY Contract. Value can also be BNK: Bank Contract. Validation Rules: 1) Mandatory. 2) Dropdown with allowed values BNK, CTY &amp; PTY. Where BNK - Bank level contracts CTY - Country level contracts PTY - Party level contracts Only BNK option will be availble if PH is not installed. |
| 5 | `PP.CN.RoutingProduct` | `PpContract_Routingproduct` | TField |  | When specified, the Routing Product can be used to define Product specific routing mechanisms. Routing Product is set as per the Product determination step of STP process flow. Validation Rules: 1) Default value is * 2) Should be a valid entry in PP.ROUTING.PRODUCT table |
| 6 | `PP.CN.PartyIDType` | `PpContract_Partyidtype` | TField |  | This field is applicable only for the Party Contract. The Party ID type for a BIC is B. The Party ID type for a national clearing is N. |
| 7 | `PP.CN.PartyID` | `PpContract_Partyid` | TField |  | This field gives the party for which the PTY Contract is defined. The PTY Contract party can be defined as a BIC in which case it can be specified as a BIC4, BIC6, BIC-8 or BIC-11. The Party ID type for a BIC is B. A Party ID Type and Party ID can therefore be defined for example as � B BARC, B BARCGB, B BARCGB21 or B BARCGB2106P. (An Contract with a BIC-11 has a higher priority compared to an Contract defined at BIC-8. Similarly in terms of pririty - BIC-8 Contract &gt; BIC-6 Contract &gt; BIC-4 Contract) The Party ID can also be defined as a National Clearing Code (NCC). The Party ID type for a national clearing is N. A Party ID Type and Party ID can therefore be defined for example as - N SC200050 |
| 8 | `PP.CN.Destination` | `PpContract_Destination` | TField | Yes | Destination Country Code to which the payment needs to be routed. Validation Rules: 1) Mandatory for Country level contracts. 2) Dropdown linked to PP.COUNTRYIBANSTRUCTURE table. |
| 9 | `PP.CN.EndDate` | `PpContract_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be Inactive. |
| 10 | `PP.CN.Ranking` | `PpContract_Ranking` |  |  |  |
| 11 | `PP.CN.SLACode` | `PpContract_Slacode` |  |  |  |
| 12 | `PP.CN.Priority` | `PpContract_Priority` |  |  |  |
| 13 | `PP.CN.CurrencyCode` | `PpContract_Currencycode` |  |  |  |
| 14 | `PP.CN.TransactionLowerLimit` | `PpContract_Transactionlowerlimit` |  |  |  |
| 15 | `PP.CN.TransactionUpperLimit` | `PpContract_Transactionupperlimit` |  |  |  |
| 16 | `PP.CN.ChargeOption` | `PpContract_Chargeoption` |  |  |  |
| 17 | `PP.CN.OptionRanking` | `PpContract_Optionranking` |  |  |  |
| 18 | `PP.CN.RSOption` | `PpContract_Rsoption` |  |  |  |
| 19 | `PP.CN.RSPartyIDType` | `PpContract_Rspartyidtype` |  |  |  |
| 20 | `PP.CN.RSPartyID` | `PpContract_Rspartyid` |  |  |  |
| 21 | `PP.CN.AccountCompany` | `PpContract_Accountcompany` |  |  |  |
| 22 | `PP.CN.AccountCurrency` | `PpContract_Accountcurrency` |  |  |  |
| 23 | `PP.CN.AccountNumber` | `PpContract_Accountnumber` |  |  |  |
| 24 | `PP.CN.MessageChannel` | `PpContract_Messagechannel` |  |  |  |
| 25 | `PP.CN.CoverIndicator` | `PpContract_Coverindicator` |  |  |  |
| 26 | `PP.CN.LeadTime` | `PpContract_Leadtime` |  |  |  |
| 27 | `PP.CN.AlternativeForCutoff` | `PpContract_Alternativeforcutoff` |  |  |  |
| 28 | `PP.CN.AlternativeForRS` | `PpContract_Alternativeforrs` |  |  |  |
| 29 | `PP.CN.AuthoriserDateTime` | `PpContract_Authoriserdatetime` | TField |  |  |
| 30 | `PP.CN.RESERVED.5` | `PpContract_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 31 | `PP.CN.RESERVED.4` | `PpContract_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 32 | `PP.CN.RESERVED.3` | `PpContract_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 33 | `PP.CN.RESERVED.2` | `PpContract_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 34 | `PP.CN.RESERVED.1` | `PpContract_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 35 | `PP.CN.LOCAL.REF` | `PpContract_LocalRef` |  |  |  |
| 36 | `PP.CN.LinkID` | `PpContract_Linkid` | TField |  | Standard T24 String. No Input Field This field gets updated after authorisation of the record. This field contains the ID of the .PDS table. It contains ConcatID-BusinessDate. |
| 37 | `PP.CN.OVERRIDE` | `PpContract_Override` |  |  |  |
| 38 | `PP.CN.RECORD.STATUS` | `PpContract_RecordStatus` | String |  |  |
| 39 | `PP.CN.CURR.NO` | `PpContract_CurrNo` | String |  |  |
| 40 | `PP.CN.INPUTTER` | `PpContract_Inputter` |  |  |  |
| 41 | `PP.CN.DATE.TIME` | `PpContract_DateTime` |  |  |  |
| 42 | `PP.CN.AUTHORISER` | `PpContract_Authoriser` | String |  |  |
| 43 | `PP.CN.CO.CODE` | `PpContract_CoCode` | String |  |  |
| 44 | `PP.CN.DEPT.CODE` | `PpContract_DeptCode` | String |  |  |
| 45 | `PP.CN.AUDITOR.CODE` | `PpContract_AuditorCode` | String |  |  |
| 46 | `PP.CN.AUDIT.DATE.TIME` | `PpContract_AuditDateTime` | String |  |  |
