# FS.GA.SECURITY.BLOCKING.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GA.SECURITY.BLOCKING.DETAIL` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SECURITY.BLOCKING.DETAIL.PARENT.REF.ID` | `FsGaSecurityBlockingDetail_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.SECURITY.BLOCKING.DETAIL.ORA.ROWID` | `FsGaSecurityBlockingDetail_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.SECURITY.BLOCKING.DETAIL.FUND.ID` | `FsGaSecurityBlockingDetail_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.SECURITY.BLOCKING.DETAIL.TRANSACTION.SERVICE.CODE` | `FsGaSecurityBlockingDetail_TransactionServiceCode` | TField |  | This is the transaction type. Multifonds DB Column is CSERV. |
| 5 | `FS.GA.SECURITY.BLOCKING.DETAIL.TRANSACTION.NUMBER` | `FsGaSecurityBlockingDetail_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 6 | `FS.GA.SECURITY.BLOCKING.DETAIL.COVERED.SECURITY.NUMBER` | `FsGaSecurityBlockingDetail_CoveredSecurityNumber` | TField |  | Security identifier used as cover/collateral in the transaction For trades like EM,IR,LD,LC,SP,MB(Manual payout With Irregular Period) Multifonds DB Column is NVAL_COVER. |
| 7 | `FS.GA.SECURITY.BLOCKING.DETAIL.DEPOSITORY.NUMBER.COVERED.SEC` | `FsGaSecurityBlockingDetail_DepositoryNumberCoveredSec` | TField |  | Depository number of the security ID attached to the transaction as collateral/cover For trades like EM,IR,LD,LC,SP,MB(Manual payout With Irregular Period) Multifonds DB Column is NDEP_COVER. |
| 8 | `FS.GA.SECURITY.BLOCKING.DETAIL.SERVICE.CODE.COVERED.SECURITY` | `FsGaSecurityBlockingDetail_ServiceCodeCoveredSecurity` | TField |  | Represents the security service code used as a collateral/cover Usually since the instrument is setup as equity like or bond security, the service code will be BO Multifonds DB Column is SERV_COVER. |
| 9 | `FS.GA.SECURITY.BLOCKING.DETAIL.CONTRACT.NUMBER.COVERED.TRANS` | `FsGaSecurityBlockingDetail_ContractNumberCoveredTrans` | TField |  | Represents contract no of the transaction(s) posted on the collateral or covering instrument which acts as underlying of the actual transaction eg trade posted or security pledged etc Multifonds DB Column is NCON_COVER. |
| 10 | `FS.GA.SECURITY.BLOCKING.DETAIL.TYPE.OF.COVER` | `FsGaSecurityBlockingDetail_TypeOfCover` | TField |  | Type Of Cover Multifonds DB Column is TYP_COVER. |
| 11 | `FS.GA.SECURITY.BLOCKING.DETAIL.QUANTITY.COVERED.TRANSACTION` | `FsGaSecurityBlockingDetail_QuantityCoveredTransaction` | TField |  | Represents quantity/units of the transaction(s) posted on the collateral or covering instrument which acts as underlying of the actual transaction eg trade posted as BO or security pledged etc Multifonds DB Column is QT_COVER. |
| 12 | `FS.GA.SECURITY.BLOCKING.DETAIL.DEAL.STATUS.CODE` | `FsGaSecurityBlockingDetail_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 13 | `FS.GA.SECURITY.BLOCKING.DETAIL.MANAGER.CODE` | `FsGaSecurityBlockingDetail_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 14 | `FS.GA.SECURITY.BLOCKING.DETAIL.QUANTITY.COVER.TMP` | `FsGaSecurityBlockingDetail_QuantityCoverTmp` | TField |  | Quantity Cover TMP Multifonds DB Column is QT_COVER_TMP. |
| 15 | `FS.GA.SECURITY.BLOCKING.DETAIL.ARCHIVE` | `FsGaSecurityBlockingDetail_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 16 | `FS.GA.SECURITY.BLOCKING.DETAIL.MATURITY.DATE.OF.CONTRACT` | `FsGaSecurityBlockingDetail_MaturityDateOfContract` | TField |  | Maturity Date of the Contract/Instrument Multifonds DB Column is DECH. |
| 17 | `FS.GA.SECURITY.BLOCKING.DETAIL.SETTLE.DATE` | `FsGaSecurityBlockingDetail_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 18 | `FS.GA.SECURITY.BLOCKING.DETAIL.TRADE.DATE` | `FsGaSecurityBlockingDetail_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 19 | `FS.GA.SECURITY.BLOCKING.DETAIL.REVERSE.DATE.COVERED.TRANS` | `FsGaSecurityBlockingDetail_ReverseDateCoveredTrans` | TField |  | Reversal date of transactions with colleral/cover (populated if processed through interface) Multifonds DB Column is DEXTOURE. |
| 20 | `FS.GA.SECURITY.BLOCKING.DETAIL.ELEMENT` | `FsGaSecurityBlockingDetail_Element` | TField |  | Element Multifonds DB Column is CELEM. |
| 21 | `FS.GA.SECURITY.BLOCKING.DETAIL.LONG.DESC` | `FsGaSecurityBlockingDetail_LongDesc` | TField |  | This represents description of a report, export type, language name etc Multifonds DB Column is LIBELLE. |
| 22 | `FS.GA.SECURITY.BLOCKING.DETAIL.STATUS.PENDING` | `FsGaSecurityBlockingDetail_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 23 | `FS.GA.SECURITY.BLOCKING.DETAIL.SOURCE.SYSTEM.DETAILS` | `FsGaSecurityBlockingDetail_SourceSystemDetails` | TField |  | Source System Details Multifonds DB Column is REPRISE. |
| 24 | `FS.GA.SECURITY.BLOCKING.DETAIL.USER.CREATION` | `FsGaSecurityBlockingDetail_UserCreation` | TField |  | Displays the username who created the transaction Multifonds DB Column is CREATEDBY. |
| 25 | `FS.GA.SECURITY.BLOCKING.DETAIL.UPDATE.RECORD.USER` | `FsGaSecurityBlockingDetail_UpdateRecordUser` | TField |  | Displays the username who last updated/modified the details of existing transaction Multifonds DB Column is UPDATEDBY. |
| 26 | `FS.GA.SECURITY.BLOCKING.DETAIL.TRANSACTION.PRICE` | `FsGaSecurityBlockingDetail_TransactionPrice` | TField |  | The unit price of an instrument which is being transacted. Multifonds DB Column is TCOURS. |
| 27 | `FS.GA.SECURITY.BLOCKING.DETAIL.AVAILABLE.QUANTITY.IN.FUND` | `FsGaSecurityBlockingDetail_AvailableQuantityInFund` | TField |  | This field displays current Security Position of the selected security in the fund Multifonds DB Column is AVL_QTY. |
| 28 | `FS.GA.SECURITY.BLOCKING.DETAIL.INTEREST.RATE` | `FsGaSecurityBlockingDetail_InterestRate` | TField |  | Interest rate applicable on the interest bearing instrument in the transaction Multifonds DB Column is TXINT. |
| 29 | `FS.GA.SECURITY.BLOCKING.DETAIL.SECURITY.PROVIDER.CODE` | `FsGaSecurityBlockingDetail_SecurityProviderCode` | TField |  | Security provider code in IRS collateral screen Multifonds DB Column is PROVIDER. |
| 30 | `FS.GA.SECURITY.BLOCKING.DETAIL.DEAL.CURRENCY` | `FsGaSecurityBlockingDetail_DealCurrency` | TField |  | Currency of settlement or currency of deal Multifonds DB Column is CDEV. |
| 31 | `FS.GA.SECURITY.BLOCKING.DETAIL.COUNTERPARTY` | `FsGaSecurityBlockingDetail_Counterparty` | TField |  | Counterparty of the transaction Multifonds DB Column is NCORRESP_EXEC. |
| 32 | `FS.GA.SECURITY.BLOCKING.DETAIL.NOMINAL.COVERED` | `FsGaSecurityBlockingDetail_NominalCovered` | TField |  | This field displays the nominal covered under repos collateral Multifonds DB Column is QT_COVER_FACT. |
| 33 | `FS.GA.SECURITY.BLOCKING.DETAIL.BROKER.ID.NUMBER` | `FsGaSecurityBlockingDetail_BrokerIdNumber` | TField |  | This field displays the broker id of the security to be blocked Multifonds DB Column is NCORRESP_LINK. |
| 34 | `FS.GA.SECURITY.BLOCKING.DETAIL.SUB.FUND.DEAL.TRANSACTION.CODE` | `FsGaSecurityBlockingDetail_SubFundDealTransactionCode` | TField |  | Corresponds to a deal transaction type abbreviation entered under a fund participating in the Pool or under a Pool or under a segment fund participating in a segment fund structure. Multifonds DB Column is CSERV_LINK. |
| 35 | `FS.GA.SECURITY.BLOCKING.DETAIL.CONTRACT.LINK` | `FsGaSecurityBlockingDetail_ContractLink` | TField |  | Contract Link Multifonds DB Column is NCONTRAT_LINK. |
| 36 | `FS.GA.SECURITY.BLOCKING.DETAIL.LINKED.DEAL.TYPE.AND.ENTRY.NO` | `FsGaSecurityBlockingDetail_LinkedDealTypeAndEntryNo` | TField |  | This field displays the service code and entry number linked to COAC Multifonds DB Column is CSERV_LINK_COAC. |
| 37 | `FS.GA.SECURITY.BLOCKING.DETAIL.SUB.FUND.ENTRY.NUMBER` | `FsGaSecurityBlockingDetail_SubFundEntryNumber` | TField |  | Corresponds to the deal entry number linked to the transaction entered under a fund participating in the Pool or under a Pool or under a segment fund participating in a segment fund structure Multifonds DB Column is NECRITUR_LINK. |
| 38 | `FS.GA.SECURITY.BLOCKING.DETAIL.CONTRACT.NUMBER.COLL` | `FsGaSecurityBlockingDetail_ContractNumberColl` | TField |  | Contract Number COLL Multifonds DB Column is NCONTRAT_COLL. |
| 39 | `FS.GA.SECURITY.BLOCKING.DETAIL.CORPORATE.ACTION.KEY` | `FsGaSecurityBlockingDetail_CorporateActionKey` | TField |  | Corporate Action Key Multifonds DB Column is CA_KEY. |
| 40 | `FS.GA.SECURITY.BLOCKING.DETAIL.RESERVED10` | `FsGaSecurityBlockingDetail_Reserved10` | TField |  |  |
| 41 | `FS.GA.SECURITY.BLOCKING.DETAIL.RESERVED9` | `FsGaSecurityBlockingDetail_Reserved9` | TField |  |  |
| 42 | `FS.GA.SECURITY.BLOCKING.DETAIL.RESERVED8` | `FsGaSecurityBlockingDetail_Reserved8` | TField |  |  |
| 43 | `FS.GA.SECURITY.BLOCKING.DETAIL.RESERVED7` | `FsGaSecurityBlockingDetail_Reserved7` | TField |  |  |
| 44 | `FS.GA.SECURITY.BLOCKING.DETAIL.RESERVED6` | `FsGaSecurityBlockingDetail_Reserved6` | TField |  |  |
| 45 | `FS.GA.SECURITY.BLOCKING.DETAIL.RESERVED5` | `FsGaSecurityBlockingDetail_Reserved5` | TField |  |  |
| 46 | `FS.GA.SECURITY.BLOCKING.DETAIL.RESERVED4` | `FsGaSecurityBlockingDetail_Reserved4` | TField |  |  |
| 47 | `FS.GA.SECURITY.BLOCKING.DETAIL.RESERVED3` | `FsGaSecurityBlockingDetail_Reserved3` | TField |  |  |
| 48 | `FS.GA.SECURITY.BLOCKING.DETAIL.RESERVED2` | `FsGaSecurityBlockingDetail_Reserved2` | TField |  |  |
| 49 | `FS.GA.SECURITY.BLOCKING.DETAIL.RESERVED1` | `FsGaSecurityBlockingDetail_Reserved1` | TField |  |  |
| 50 | `FS.GA.SECURITY.BLOCKING.DETAIL.LOCAL.REF` | `FsGaSecurityBlockingDetail_LocalRef` |  |  |  |
| 51 | `FS.GA.SECURITY.BLOCKING.DETAIL.OVERRIDE` | `FsGaSecurityBlockingDetail_Override` |  |  |  |
| 52 | `FS.GA.SECURITY.BLOCKING.DETAIL.RECORD.STATUS` | `FsGaSecurityBlockingDetail_RecordStatus` | String |  |  |
| 53 | `FS.GA.SECURITY.BLOCKING.DETAIL.CURR.NO` | `FsGaSecurityBlockingDetail_CurrNo` | String |  |  |
| 54 | `FS.GA.SECURITY.BLOCKING.DETAIL.INPUTTER` | `FsGaSecurityBlockingDetail_Inputter` |  |  |  |
| 55 | `FS.GA.SECURITY.BLOCKING.DETAIL.DATE.TIME` | `FsGaSecurityBlockingDetail_DateTime` |  |  |  |
| 56 | `FS.GA.SECURITY.BLOCKING.DETAIL.AUTHORISER` | `FsGaSecurityBlockingDetail_Authoriser` | String |  |  |
| 57 | `FS.GA.SECURITY.BLOCKING.DETAIL.CO.CODE` | `FsGaSecurityBlockingDetail_CoCode` | String |  |  |
| 58 | `FS.GA.SECURITY.BLOCKING.DETAIL.DEPT.CODE` | `FsGaSecurityBlockingDetail_DeptCode` | String |  |  |
| 59 | `FS.GA.SECURITY.BLOCKING.DETAIL.AUDITOR.CODE` | `FsGaSecurityBlockingDetail_AuditorCode` | String |  |  |
| 60 | `FS.GA.SECURITY.BLOCKING.DETAIL.AUDIT.DATE.TIME` | `FsGaSecurityBlockingDetail_AuditDateTime` | String |  |  |
