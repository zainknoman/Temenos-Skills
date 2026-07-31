# PRE.SYNDICATION.FILE — Table Schema

> Source: `INSERTS/I_F.PRE.SYNDICATION.FILE` in `SL_Presyndication.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PRE.SYND.CUSTOMER` | `PreSyndicationFile_Customer` | TField | Yes | The counterparty of the contract. This field contains the identification number assigned to the customer (borrower) and will accept the customer's mnemonic also. The system will use this number to identify the borrower of the credit line as well as to obtain the customer's name and address for delivery purposes. Validation Rules: 3-10 alphanumeric customer mnemonic or 1-10 numeric character customer number Must be a valid record on the CUSTOMER table Mandatory input |
| 2 | `PRE.SYND.SL.DESC` | `PreSyndicationFile_SlDesc` |  |  |  |
| 3 | `PRE.SYND.SL.SHORT.DESC` | `PreSyndicationFile_SlShortDesc` | TField | Yes | Short description of the syndication. 3-15 character alphanumeric value would be accepted Validation Rules: Mandatory input |
| 4 | `PRE.SYND.CUSTOMER.REF` | `PreSyndicationFile_CustomerRef` | TField | No | 35 alphanumeric character free text field to record the customer reference details. Validation Rules: Optional Input |
| 5 | `PRE.SYND.SL.FUNCTION` | `PreSyndicationFile_SlFunction` | TField | Yes | Field that determines nature of role played by T24 bank in the syndicate. The bank could play any of the three roles namely AGENT - In this instance the bank does not participate by way of subscription and only manages the syndicate AGENT cum PARTICIPANT - The bank handles the Agency functions and is also a subscriber (participant) to the syndicate. MERE PARTICIPANT - The bank is only a participant Validation Rules: Only allowed values are A (Agent) AP (Agent cum Participant) and P (Only Participant) Mandatory Input |
| 6 | `PRE.SYND.CATEGORY` | `PreSyndicationFile_Category` | TField | Yes | Contains the category code to which this transaction would be assigned. The category code should be within range 20000 - 49999 and should be a valid record on the CATEGORY table. Validation Rules: 1-5 numeric characters Must be a valid record on the CATEGORY table Mandatory input |
| 7 | `PRE.SYND.MANDATE.DATE` | `PreSyndicationFile_MandateDate` | TField | No | Date on which mandate was received from the borrower. This field is used only for information purposes and not for any processing. Validation Rules: 1-9 type (A) alphanumeric characters Optional input. System defaults process date Should be less than Presyn Start Date |
| 8 | `PRE.SYND.PRESYND.START.DATE` | `PreSyndicationFile_PresyndStartDate` | TField |  | Date on which the pre-syndication work is expected to commence. The pre-syndication process starts with receiving the mandate from the customer and ends with creation of facility after the entire credit line is tied up. The start and end of this period is defined in this set of fields for information. Validation Rules: 1-9 type (A) alpha numeric characters. Can only be later than the Presyn start date |
| 9 | `PRE.SYND.PRESYND.END.DATE` | `PreSyndicationFile_PresyndEndDate` | TField | Yes | End date for the pre-syndication activity. Validation Rules: 1-9 (A) type alphanumeric characters Mandatory input Should be later than the Presynd.start.date |
| 10 | `PRE.SYND.MIN.SUBSN` | `PreSyndicationFile_MinSubsn` | TField | No | Minimum subscription required for grant of facility. This is expressed as a percentage of the mandate amount (SL.AMOUNT) or the amount sought by the borrower. Recorded for information only. Validation Rules: Two digit numeric value between 1-99 would be accepted Optional input |
| 11 | `PRE.SYND.ACCOUNT.OFFICER` | `PreSyndicationFile_AccountOfficer` | TField | No | Indicates the account officer for MIS reporting and profitability purposes. Validation Rules: 1-4 numeric characters Optional input. System defaults the account officer of the customer. Must be a valid record on the DEPT.ACCT.OFFICER table |
| 12 | `PRE.SYND.SL.CURRENCY` | `PreSyndicationFile_SlCurrency` |  |  |  |
| 13 | `PRE.SYND.SL.FACILITY` | `PreSyndicationFile_SlFacility` |  |  |  |
| 14 | `PRE.SYND.REVOL.TYPE` | `PreSyndicationFile_RevolType` |  |  |  |
| 15 | `PRE.SYND.SL.AMOUNT` | `PreSyndicationFile_SlAmount` |  |  |  |
| 16 | `PRE.SYND.DD.CURRENCY` | `PreSyndicationFile_DdCurrency` |  |  |  |
| 17 | `PRE.SYND.DEF.ACCOUNT` | `PreSyndicationFile_DefAccount` |  |  |  |
| 18 | `PRE.SYND.SL.STATUS` | `PreSyndicationFile_SlStatus` |  |  |  |
| 19 | `PRE.SYND.INT.RATE.TYPE` | `PreSyndicationFile_IntRateType` |  |  |  |
| 20 | `PRE.SYND.INTEREST.RATE` | `PreSyndicationFile_InterestRate` |  |  |  |
| 21 | `PRE.SYND.INTEREST.KEY` | `PreSyndicationFile_InterestKey` |  |  |  |
| 22 | `PRE.SYND.CUSTOMER.SPR` | `PreSyndicationFile_CustomerSpr` |  |  |  |
| 23 | `PRE.SYND.CUSTOMER.FEE` | `PreSyndicationFile_CustomerFee` |  |  |  |
| 24 | `PRE.SYND.UW.FEE.ACC` | `PreSyndicationFile_UwFeeAcc` |  |  |  |
| 25 | `PRE.SYND.UNDERWRITER` | `PreSyndicationFile_Underwriter` |  |  |  |
| 26 | `PRE.SYND.UW.AGREE.DT` | `PreSyndicationFile_UwAgreeDt` |  |  |  |
| 27 | `PRE.SYND.UW.AMOUNT` | `PreSyndicationFile_UwAmount` |  |  |  |
| 28 | `PRE.SYND.UW.PERC` | `PreSyndicationFile_UwPerc` |  |  |  |
| 29 | `PRE.SYND.UW.COMMN` | `PreSyndicationFile_UwCommn` |  |  |  |
| 30 | `PRE.SYND.UW.COMM.AMT` | `PreSyndicationFile_UwCommAmt` |  |  |  |
| 31 | `PRE.SYND.SUBS.BROUGHT` | `PreSyndicationFile_SubsBrought` |  |  |  |
| 32 | `PRE.SYND.TOTAL.UW.AMOUNT` | `PreSyndicationFile_TotalUwAmount` |  |  |  |
| 33 | `PRE.SYND.TOTAL.UW.PERC` | `PreSyndicationFile_TotalUwPerc` |  |  |  |
| 34 | `PRE.SYND.PARTICIPATOR` | `PreSyndicationFile_Participator` |  |  |  |
| 35 | `PRE.SYND.PART.AGR.DT` | `PreSyndicationFile_PartAgrDt` |  |  |  |
| 36 | `PRE.SYND.AMT.SOUGHT` | `PreSyndicationFile_AmtSought` |  |  |  |
| 37 | `PRE.SYND.PERC.SOUGHT` | `PreSyndicationFile_PercSought` |  |  |  |
| 38 | `PRE.SYND.AMT.ALLOT` | `PreSyndicationFile_AmtAllot` |  |  |  |
| 39 | `PRE.SYND.PERC.ALLOT` | `PreSyndicationFile_PercAllot` |  |  |  |
| 40 | `PRE.SYND.PART.FEE` | `PreSyndicationFile_PartFee` |  |  |  |
| 41 | `PRE.SYND.TOTAL.PART.AMT` | `PreSyndicationFile_TotalPartAmt` |  |  |  |
| 42 | `PRE.SYND.TOTAL.PART.PERC` | `PreSyndicationFile_TotalPartPerc` |  |  |  |
| 43 | `PRE.SYND.UW.DEVOL` | `PreSyndicationFile_UwDevol` |  |  |  |
| 44 | `PRE.SYND.DEVOL.TYPE` | `PreSyndicationFile_DevolType` |  |  |  |
| 45 | `PRE.SYND.DEVOL.UW` | `PreSyndicationFile_DevolUw` |  |  |  |
| 46 | `PRE.SYND.DEVOL.AMOUNT` | `PreSyndicationFile_DevolAmount` |  |  |  |
| 47 | `PRE.SYND.REQ.BANK` | `PreSyndicationFile_ReqBank` |  |  |  |
| 48 | `PRE.SYND.DATE.SENT` | `PreSyndicationFile_DateSent` |  |  |  |
| 49 | `PRE.SYND.RESP.BY.DT` | `PreSyndicationFile_RespByDt` |  |  |  |
| 50 | `PRE.SYND.RESPONSE.DT` | `PreSyndicationFile_ResponseDt` |  |  |  |
| 51 | `PRE.SYND.COMMENTS` | `PreSyndicationFile_Comments` |  |  |  |
| 52 | `PRE.SYND.ROLE` | `PreSyndicationFile_Role` |  |  |  |
| 53 | `PRE.SYND.ROLE.CUST` | `PreSyndicationFile_RoleCust` |  |  |  |
| 54 | `PRE.SYND.CREATE.FACILITY` | `PreSyndicationFile_CreateFacility` | TField |  | Once the entire credit line is tied up, value YES could be input in this field to create the FACILITY records. In order to create the FACILITY, the Total.Part.Amt should be equal to SL.AMOUNT within each multi-value set. On authorisation, as many FACILITY records as defined in Presyn file would be created in IHLD status with necessary default information. Validation Rules: Only allowed value is YES |
| 55 | `PRE.SYND.ROUNDING.RULE` | `PreSyndicationFile_RoundingRule` | TField |  | This field will hold contract level rounding rule for underwriting fee calculations. Validation Rules: Should be a valid EB.ROUNDING.RULE id. No change permitted after first authorization For detailed options on different rounding options help text on EB.ROUNDING.RULE file can be referred. |
| 56 | `PRE.SYND.AVL.FRONTING` | `PreSyndicationFile_AvlFronting` |  |  |  |
| 57 | `PRE.SYND.RESERVED.FIELD.8` | `PreSyndicationFile_ReservedField8` | TField |  |  |
| 58 | `PRE.SYND.RESERVED.FIELD.7` | `PreSyndicationFile_ReservedField7` | TField |  |  |
| 59 | `PRE.SYND.RESERVED.FIELD.6` | `PreSyndicationFile_ReservedField6` | TField |  |  |
| 60 | `PRE.SYND.RESERVED.FIELD.5` | `PreSyndicationFile_ReservedField5` | TField |  |  |
| 61 | `PRE.SYND.RESERVED.FIELD.4` | `PreSyndicationFile_ReservedField4` | TField |  |  |
| 62 | `PRE.SYND.RESERVED.FIELD.3` | `PreSyndicationFile_ReservedField3` | TField |  |  |
| 63 | `PRE.SYND.RESERVED.FIELD.2` | `PreSyndicationFile_ReservedField2` | TField |  |  |
| 64 | `PRE.SYND.RESERVED.FIELD.1` | `PreSyndicationFile_ReservedField1` | TField |  |  |
| 65 | `PRE.SYND.LOCAL.REF` | `PreSyndicationFile_LocalRef` |  |  |  |
| 66 | `PRE.SYND.STMT.NO` | `PreSyndicationFile_StmtNo` |  |  |  |
| 67 | `PRE.SYND.OVERRIDE` | `PreSyndicationFile_Override` |  |  |  |
| 68 | `PRE.SYND.RECORD.STATUS` | `PreSyndicationFile_RecordStatus` | String |  |  |
| 69 | `PRE.SYND.CURR.NO` | `PreSyndicationFile_CurrNo` | String |  |  |
| 70 | `PRE.SYND.INPUTTER` | `PreSyndicationFile_Inputter` |  |  |  |
| 71 | `PRE.SYND.DATE.TIME` | `PreSyndicationFile_DateTime` |  |  |  |
| 72 | `PRE.SYND.AUTHORISER` | `PreSyndicationFile_Authoriser` | String |  |  |
| 73 | `PRE.SYND.CO.CODE` | `PreSyndicationFile_CoCode` | String |  |  |
| 74 | `PRE.SYND.DEPT.CODE` | `PreSyndicationFile_DeptCode` | String |  |  |
| 75 | `PRE.SYND.AUDITOR.CODE` | `PreSyndicationFile_AuditorCode` | String |  |  |
| 76 | `PRE.SYND.AUDIT.DATE.TIME` | `PreSyndicationFile_AuditDateTime` | String |  |  |
