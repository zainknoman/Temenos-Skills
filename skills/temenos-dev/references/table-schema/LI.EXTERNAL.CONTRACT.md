# LI.EXTERNAL.CONTRACT — Table Schema

> Source: `INSERTS/I_F.LI.EXTERNAL.CONTRACT` in `LI_ExternalTxn.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.XC.EVENT.TYPE` | `LiExternalContract_EventType` | TField | Yes | This field indicates that whether the External contract is newly created or if amendment is done on the existing record in Limit System. Validation Rules: Non-mandatory field. For information purpose |
| 2 | `LI.XC.EVENT.REFERENCE` | `LiExternalContract_EventReference` | TField | Yes | Contains the External Event Reference which led to the creation or amendment of external contract in limit system. Validation Rules: Non-mandatory field. For information purpose |
| 3 | `LI.XC.CONTRACT.APPLICATION` | `LiExternalContract_ContractApplication` | TField | Yes | This field contains the source application name where the contract is created in external system. Validation Rules: Mandatory field. For information purpose |
| 4 | `LI.XC.CONTRACT.ID` | `LiExternalContract_ContractId` | TField | Yes | This field contains the Contract ID originated from the external system. Validation Rules: Mandatory field. |
| 5 | `LI.XC.COMPANY` | `LiExternalContract_Company` | TField | Yes | This field indicates the Company ID where the Contract resides in the external system. Validation Rules: Non mandatory field. |
| 6 | `LI.XC.CURRENCY` | `LiExternalContract_Currency` | TField | Yes | This field indicates the currency of the contract. Validation Rules: Mandatory field. Should be a valid T24 Currency. |
| 7 | `LI.XC.START.DATE` | `LiExternalContract_StartDate` | TField | Yes | This field indicates the start date or value date of the contract. Validation Rules: Standard T24 Date format. Non-mandatory field. |
| 8 | `LI.XC.MATURITY.DATE` | `LiExternalContract_MaturityDate` | TField | Yes | This field indicates the maturity date of the contract. Validation Rules: Standard T24 Date format. Non-mandatory field. |
| 9 | `LI.XC.BOOKING.DATE` | `LiExternalContract_BookingDate` | TField | Yes | This field indicates the date in which the contract is booked in the source system. Validation Rules: Standard T24 Date format. Non-mandatory field. |
| 10 | `LI.XC.REVOLVING` | `LiExternalContract_Revolving` | TField | Yes | This field specifies whether the contract is revolving or non-revolving in nature. If it is set as Yes, Contract is revolving in nature and any payment against the outstanding amount will result in available amount increase. Validation Rules: YES or NO field. Non-mandatory field. |
| 11 | `LI.XC.CONTRACT.STATUS` | `LiExternalContract_ContractStatus` | TField | Yes | This field specifies whether the contract is in unauthorized or authorized status. This field will be updated by the system. Validation Rules: Non-mandatory field. For information purpose |
| 12 | `LI.XC.PRODUCT.LINE` | `LiExternalContract_ProductLine` | TField | Yes | This field contains the nature of the external contract like ACCOUNTS, LENDING or DEPOSITS. Validation Rules: Non-mandatory field. |
| 13 | `LI.XC.CUSTOMER.IDS` | `LiExternalContract_CustomerIds` |  |  |  |
| 14 | `LI.XC.REPORTING.CUSTOMER` | `LiExternalContract_ReportingCustomer` |  |  |  |
| 15 | `LI.XC.JOINT.OWNERSHIP.PERCENTAGE` | `LiExternalContract_JointOwnershipPercentage` |  |  |  |
| 16 | `LI.XC.JOINT.OWNER` | `LiExternalContract_JointOwner` |  |  |  |
| 17 | `LI.XC.JOINT.LIABILITY` | `LiExternalContract_JointLiability` | TField | Yes | Flag to indicate that the customers are jointly liable for the contract. If this is set to Yes, the contract should also have same customers as limits to use the limit. Validation Rules: Yes or No field. Non-mandatory field. |
| 18 | `LI.XC.ACCOUNT.OFFICER` | `LiExternalContract_AccountOfficer` | TField | Yes | This field indicates the Account Officer of the contract. When it is not inputted, it will be defaulted with the Department Code of the current logged in user. Validation Rules: Non-mandatory field. Should be a valid record in DEPT.ACCT.OFFICER. |
| 19 | `LI.XC.CURRENCY.MARKET` | `LiExternalContract_CurrencyMarket` | TField | Yes | This field contains the Currency Market for exchange rate information of the contract, in countries where different rates are quoted for the same Currency. When it is not inputted, it will be defaulted with the value '1'. Validation Rules: Non-mandatory field. Should be a valid record in CURRENCY.MARKET. |
| 20 | `LI.XC.POSITION.TYPE` | `LiExternalContract_PositionType` | TField | Yes | This field contains the Type of Foreign Exchange Position which will be updated as a result of movements over the contract. When it is not inputted, it will be defaulted with the value 'TR'. Validation Rules: Non-mandatory field. |
| 21 | `LI.XC.CATEGORY` | `LiExternalContract_Category` | TField | Yes | This field contains the Product Category of the Contract. Validation Rules: Non-mandatory field. Should be a valid record in CATEGORY. |
| 22 | `LI.XC.LIMIT.ID` | `LiExternalContract_LimitId` | TField | Yes | This field contains the Limit ID to which the contract is linked. When a limit is linked to the contract, system will check if this limit is valid to link with this contract against the LIMIT.PARAMETER Product definitions. Validation Rules: Mandatory field. Should be a valid record in LIMIT. |
| 23 | `LI.XC.LIMIT.PRODUCT` | `LiExternalContract_LimitProduct` | TField | Yes | This field contains the Limit product of the limit linked to the contract. Validation Rules: Non-mandatory field. Should be a valid record in LIMIT.REFERENCE. |
| 24 | `LI.XC.PREV.LIMIT.ID` | `LiExternalContract_PrevLimitId` | TField | Yes | This field contains the Previous Limit ID which was linked to the contract. If there is a change in limit id linked to the contract Id in the source system, then this field retains the limit id removed from the contract. In transact system, if Limit has to be changed either they can input the old limit id in this field and input the new limit id in the LIMIT.ID field or they can replace the new limit id in the LIMIT.ID field and leave this field blank. Validation Rules: Non-mandatory field. Should be a valid record in LIMIT. |
| 25 | `LI.XC.UNIQUE.LIMIT` | `LiExternalContract_UniqueLimit` | TField | Yes | Flag to indicate whether only one contract can be linked to limit(Single Limit). Validation Rules: Yes or No field. Non-mandatory field. |
| 26 | `LI.XC.CONTRIBUTE.CR.BALANCE` | `LiExternalContract_ContributeCrBalance` | TField | Yes | Flag to indicate that the contract contributes its credit balance for group debit (Allow Netting). Validation Rules: Yes or No field. Non-mandatory field. |
| 27 | `LI.XC.COMMITMENT.CONTRACT` | `LiExternalContract_CommitmentContract` | TField | Yes | Flag to indicate whether the contract is a commitment contract. Validation Rules: Yes or No field. Non-mandatory field. |
| 28 | `LI.XC.CLOSED.FLAG` | `LiExternalContract_ClosedFlag` | TField | Yes | Flag to indicate the contract is closed or reversed in the source system. Validation Rules: Yes or No field. Non-mandatory field. |
| 29 | `LI.XC.CLOSED.DATE` | `LiExternalContract_ClosedDate` | TField | Yes | This field contains the date on which the contract is closed or reversed in the source system. Validation Rules: Standard T24 Date format. Non-mandatory field. |
| 30 | `LI.XC.SYSTEM.ID` | `LiExternalContract_SystemId` | TField |  | This field contains the Module ID of the contract originated. For information purpose. |
| 31 | `LI.XC.SOURCE.SYSTEM` | `LiExternalContract_SourceSystem` | TField |  | This field contains the identifier of the Source system from where the contract is initiated. For information purpose. |
| 32 | `LI.XC.SOURCE.SYSTEM.DATE` | `LiExternalContract_SourceSystemDate` | TField |  | This field contains the date of the Source system from where the contract is initiated. For information purpose. |
| 33 | `LI.XC.DELINK.REASON` | `LiExternalContract_DelinkReason` | TField | Yes | This field contains the reason for delinking the limit with the contract. Validation Rules: Free text field. Non-mandatory field. |
| 34 | `LI.XC.ADDITIONAL.DETAILS.LABEL` | `LiExternalContract_AdditionalDetailsLabel` |  |  |  |
| 35 | `LI.XC.ADDITIONAL.DETAILS.VALUE` | `LiExternalContract_AdditionalDetailsValue` |  |  |  |
| 36 | `LI.XC.RESERVED.5` | `LiExternalContract_Reserved5` | TField |  |  |
| 37 | `LI.XC.RESERVED.4` | `LiExternalContract_Reserved4` | TField |  |  |
| 38 | `LI.XC.RESERVED.3` | `LiExternalContract_Reserved3` | TField |  |  |
| 39 | `LI.XC.RESERVED.2` | `LiExternalContract_Reserved2` | TField |  |  |
| 40 | `LI.XC.RESERVED.1` | `LiExternalContract_Reserved1` | TField |  |  |
| 41 | `LI.XC.LOCAL.REF` | `LiExternalContract_LocalRef` |  |  |  |
| 42 | `LI.XC.STMT.NOS` | `LiExternalContract_StmtNos` |  |  |  |
| 43 | `LI.XC.OVERRIDE` | `LiExternalContract_Override` |  |  |  |
| 44 | `LI.XC.RECORD.STATUS` | `LiExternalContract_RecordStatus` | String |  |  |
| 45 | `LI.XC.CURR.NO` | `LiExternalContract_CurrNo` | String |  |  |
| 46 | `LI.XC.INPUTTER` | `LiExternalContract_Inputter` |  |  |  |
| 47 | `LI.XC.DATE.TIME` | `LiExternalContract_DateTime` |  |  |  |
| 48 | `LI.XC.AUTHORISER` | `LiExternalContract_Authoriser` | String |  |  |
| 49 | `LI.XC.CO.CODE` | `LiExternalContract_CoCode` | String |  |  |
| 50 | `LI.XC.DEPT.CODE` | `LiExternalContract_DeptCode` | String |  |  |
| 51 | `LI.XC.AUDITOR.CODE` | `LiExternalContract_AuditorCode` | String |  |  |
| 52 | `LI.XC.AUDIT.DATE.TIME` | `LiExternalContract_AuditDateTime` | String |  |  |
