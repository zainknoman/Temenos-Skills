# SAWATQ.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SAWATQ.PARAMETER` in `SAWATQ_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SAMA.PARAM.SERVICE.NAME` | `SawatqParameter_ServiceName` |  |  |  |
| 2 | `SAMA.PARAM.PARTY.TYPE` | `SawatqParameter_PartyType` |  |  |  |
| 3 | `SAMA.PARAM.ID.TYPE` | `SawatqParameter_IdType` |  |  |  |
| 4 | `SAMA.PARAM.ID.CODE` | `SawatqParameter_IdCode` |  |  |  |
| 5 | `SAMA.PARAM.ALT.ACCT.TYPE` | `SawatqParameter_AltAcctType` | TField |  | Holds the alternate account type value Which need to check at the account level |
| 6 | `SAMA.PARAM.SUCCESS.CODE` | `SawatqParameter_SuccessCode` |  |  |  |
| 7 | `SAMA.PARAM.SUCCESS.DESC` | `SawatqParameter_SuccessDesc` |  |  |  |
| 8 | `SAMA.PARAM.ERROR.CODE` | `SawatqParameter_ErrorCode` |  |  |  |
| 9 | `SAMA.PARAM.ERROR.DESC` | `SawatqParameter_ErrorDesc` |  |  |  |
| 10 | `SAMA.PARAM.LOCAL.REF` | `SawatqParameter_LocalRef` |  |  |  |
| 11 | `SAMA.PARAM.OVERRIDE` | `SawatqParameter_Override` |  |  |  |
| 12 | `SAMA.PARAM.CUSTOMER.ROLE` | `SawatqParameter_CustomerRole` |  |  |  |
| 13 | `SAMA.PARAM.CORP.CATEGORY.RANGE.START` | `SawatqParameter_CorpCategoryRangeStart` | TField |  | This indicates the Sector of the Corporate customer |
| 14 | `SAMA.PARAM.CORP.CATEGORY.RANGE.END` | `SawatqParameter_CorpCategoryRangeEnd` | TField |  | This indicates the Sector of the Corporate customer |
| 15 | `SAMA.PARAM.ACCOUNT.STATUS` | `SawatqParameter_AccountStatus` |  |  |  |
| 16 | `SAMA.PARAM.ACCOUNT.STATUS.CODE` | `SawatqParameter_AccountStatusCode` |  |  |  |
| 17 | `SAMA.PARAM.POSTING.RESTRICTION.CODE` | `SawatqParameter_PostingRestrictionCode` |  |  |  |
| 18 | `SAMA.PARAM.RELATION` | `SawatqParameter_Relation` |  |  |  |
| 19 | `SAMA.PARAM.RELATION.TYPE` | `SawatqParameter_RelationType` |  |  |  |
| 20 | `SAMA.PARAM.PRODUCT.CATEGORY` | `SawatqParameter_ProductCategory` |  |  |  |
| 21 | `SAMA.PARAM.PRODUCT.CATEGORY.CODES` | `SawatqParameter_ProductCategoryCodes` |  |  |  |
| 22 | `SAMA.PARAM.LD.TOTAL.LIABILITY.AMOUNT` | `SawatqParameter_LdTotalLiabilityAmount` |  |  |  |
| 23 | `SAMA.PARAM.LD.DEPOSIT.BALANCE` | `SawatqParameter_LdDepositBalance` |  |  |  |
| 24 | `SAMA.PARAM.TRANSFER.TO.INT.AC.VERSION` | `SawatqParameter_TransferToIntAcVersion` | TField |  | This indicates the Version for Internal Transfer |
| 25 | `SAMA.PARAM.AC.TRFR.HOME.VERSION` | `SawatqParameter_AcTrfrHomeVersion` | TField |  | This indicates the Version for Watheeq Book Transfer |
| 26 | `SAMA.PARAM.SARIE.TRFR.VERSION` | `SawatqParameter_SarieTrfrVersion` | TField |  | This indicates the Version for Sarie Transfer |
| 27 | `SAMA.PARAM.OUTWARD.REMIT.TRFR.VERSION` | `SawatqParameter_OutwardRemitTrfrVersion` | TField |  | This indicates the Version for Outward Remittance Transfer |
| 28 | `SAMA.PARAM.TARGET.PRODUCT` | `SawatqParameter_TargetProduct` |  |  |  |
| 29 | `SAMA.PARAM.CATEGORY.FOR.LIFTING` | `SawatqParameter_CategoryForLifting` | TField |  | This indicates the Account Number which is used to transfer Amount during Lift |
| 30 | `SAMA.PARAM.PRIORITY.OF.CURRENCY` | `SawatqParameter_PriorityOfCurrency` |  |  |  |
| 31 | `SAMA.PARAM.CUSTOMER.ROLE.TYPE` | `SawatqParameter_CustomerRoleType` |  |  |  |
| 32 | `SAMA.PARAM.SHAREHOLDER` | `SawatqParameter_Shareholder` | TField |  | This indicates the shareholder's Relation to the customer |
| 33 | `SAMA.PARAM.TOTAL.BALANCE` | `SawatqParameter_TotalBalance` | TField |  | The value in this field indicates the Type of balance |
| 34 | `SAMA.PARAM.AVAILABLE.BALANCE` | `SawatqParameter_AvailableBalance` | TField |  |  |
| 35 | `SAMA.PARAM.AA.PAYMENT.TYPE` | `SawatqParameter_AaPaymentType` |  |  |  |
| 36 | `SAMA.PARAM.BLOCK.TYPE` | `SawatqParameter_BlockType` |  |  |  |
| 37 | `SAMA.PARAM.BLOCK.POSTING.RESTRICTION.CODE` | `SawatqParameter_BlockPostingRestrictionCode` |  |  |  |
| 38 | `SAMA.PARAM.TYPE.OF.RATE` | `SawatqParameter_TypeOfRate` | TField |  | This indicates the Type of Rate that needs to be imposed during Full lift transfer |
| 39 | `SAMA.PARAM.DEPOSIT.BLOCK.ACCOUNT` | `SawatqParameter_DepositBlockAccount` | TField |  | This indicates the Block Amount for Deposits |
| 40 | `SAMA.PARAM.CURRENCY.MARKET` | `SawatqParameter_CurrencyMarket` | TField |  | This indicates the Currency Market |
| 41 | `SAMA.PARAM.SAWATQ.ROLE` | `SawatqParameter_SawatqRole` |  |  |  |
| 42 | `SAMA.PARAM.SAWATQ.ROLE.TYPE` | `SawatqParameter_SawatqRoleType` |  |  |  |
| 43 | `SAMA.PARAM.SARIE.BEN.BANK` | `SawatqParameter_SarieBenBank` | TField |  |  |
| 44 | `SAMA.PARAM.SARIE.PURPOSE.OF.TRANSFER` | `SawatqParameter_SariePurposeOfTransfer` | TField |  |  |
| 45 | `SAMA.PARAM.PS.RELATION.CODE` | `SawatqParameter_PsRelationCode` |  |  |  |
| 46 | `SAMA.PARAM.PS.RELATION.CONDITION` | `SawatqParameter_PsRelationCondition` |  |  |  |
| 47 | `SAMA.PARAM.PS.RELATION.DESC` | `SawatqParameter_PsRelationDesc` |  |  |  |
| 48 | `SAMA.PARAM.RECORD.STATUS` | `SawatqParameter_RecordStatus` | String |  |  |
| 49 | `SAMA.PARAM.CURR.NO` | `SawatqParameter_CurrNo` | String |  |  |
| 50 | `SAMA.PARAM.INPUTTER` | `SawatqParameter_Inputter` |  |  |  |
| 51 | `SAMA.PARAM.DATE.TIME` | `SawatqParameter_DateTime` |  |  |  |
| 52 | `SAMA.PARAM.AUTHORISER` | `SawatqParameter_Authoriser` | String |  |  |
| 53 | `SAMA.PARAM.CO.CODE` | `SawatqParameter_CoCode` | String |  |  |
| 54 | `SAMA.PARAM.DEPT.CODE` | `SawatqParameter_DeptCode` | String |  |  |
| 55 | `SAMA.PARAM.AUDITOR.CODE` | `SawatqParameter_AuditorCode` | String |  |  |
| 56 | `SAMA.PARAM.AUDIT.DATE.TIME` | `SawatqParameter_AuditDateTime` | String |  |  |
