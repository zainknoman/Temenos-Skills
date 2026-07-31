# FS.GA.DIVIDEND.ANNOUNCEMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.DIVIDEND.ANNOUNCEMENT` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.DIVIDEND.ANNOUNCEMENT.PARENT.REF.ID` | `FsGaDividendAnnouncement_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.DIVIDEND.ANNOUNCEMENT.ORA.ROWID` | `FsGaDividendAnnouncement_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.DIVIDEND.ANNOUNCEMENT.INTERNAL.SECURITY.ID` | `FsGaDividendAnnouncement_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 4 | `FS.GA.DIVIDEND.ANNOUNCEMENT.EXEC.DATE` | `FsGaDividendAnnouncement_ExecDate` | TField |  | This field displays the ex-date of a security and any securities purchased from a company on the ex-date will not be entitled to receive dividend Multifonds DB Column is DATE_EX. |
| 5 | `FS.GA.DIVIDEND.ANNOUNCEMENT.UNIT.AMOUNT` | `FsGaDividendAnnouncement_UnitAmount` | TField |  | Denotes the per unit amount in the security currency or the quoted currency Multifonds DB Column is MNTUNIT. |
| 6 | `FS.GA.DIVIDEND.ANNOUNCEMENT.EX.DATE` | `FsGaDividendAnnouncement_ExDate` | TField |  | Execution date for Dividend announcement and Corporate Action Multifonds DB Column is DPAYMNT. |
| 7 | `FS.GA.DIVIDEND.ANNOUNCEMENT.SETTLE.DATE` | `FsGaDividendAnnouncement_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 8 | `FS.GA.DIVIDEND.ANNOUNCEMENT.LOCAL.CURRENCY` | `FsGaDividendAnnouncement_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 9 | `FS.GA.DIVIDEND.ANNOUNCEMENT.RECOVERABLE.TAX.1.PERCENTAGE` | `FsGaDividendAnnouncement_RecoverableTax1Percentage` | TField |  | Recoverable tax percentage at dividend announcement , type 1 Multifonds DB Column is PCT_RC. |
| 10 | `FS.GA.DIVIDEND.ANNOUNCEMENT.UNRECOVERABLE.TAX.1.PERCENTAGE` | `FsGaDividendAnnouncement_UnrecoverableTax1Percentage` | TField |  | Unrecoverable tax percentage at dividend announcement , type 1 Multifonds DB Column is PCT_UN. |
| 11 | `FS.GA.DIVIDEND.ANNOUNCEMENT.REC.TAX.IN.PERCENT.TYPE.2` | `FsGaDividendAnnouncement_RecTaxInPercentType2` | TField |  | Recoverable tax percentage at dividend announcement , type 2 Multifonds DB Column is PCT_RC_2. |
| 12 | `FS.GA.DIVIDEND.ANNOUNCEMENT.UNREC.TAX.IN.PERCENT.TYPE.2` | `FsGaDividendAnnouncement_UnrecTaxInPercentType2` | TField |  | Unrecoverable tax percentage at dividend announcement , type 2 Multifonds DB Column is PCT_UN_2. |
| 13 | `FS.GA.DIVIDEND.ANNOUNCEMENT.NET.UNIT.AMOUNT.IDENTIFIER` | `FsGaDividendAnnouncement_NetUnitAmountIdentifier` | TField |  | Denotes whether the income is Grossed up from the Net amount. Usually arises when Net amount per unit announcement is done in market Multifonds DB Column is FLAG_BRUT. |
| 14 | `FS.GA.DIVIDEND.ANNOUNCEMENT.OPERATION.CODE` | `FsGaDividendAnnouncement_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 15 | `FS.GA.DIVIDEND.ANNOUNCEMENT.UNIT.AMOUNT.TAX.1` | `FsGaDividendAnnouncement_UnitAmountTax1` | TField |  | This field is not used anymore Multifonds DB Column is RECOVERABLE. |
| 16 | `FS.GA.DIVIDEND.ANNOUNCEMENT.UNIT.AMOUNT.TAX.2` | `FsGaDividendAnnouncement_UnitAmountTax2` | TField |  | This field is not used anymore Multifonds DB Column is RECOVERABLE_1. |
| 17 | `FS.GA.DIVIDEND.ANNOUNCEMENT.EXTERNAL.REFERENCE.NUMBER` | `FsGaDividendAnnouncement_ExternalReferenceNumber` | TField |  | External reference corresponds a trade,security or fund Multifonds DB Column is EXT_REF. |
| 18 | `FS.GA.DIVIDEND.ANNOUNCEMENT.TAX.REGIME` | `FsGaDividendAnnouncement_TaxRegime` | TField |  | A group of Tax rules can be defined in the Tax tables against a Tax regime and all the funds defined with the respective Tax regime would follow the tax rules defined under this Tax regime. Multifonds DB Column is TAX_REG. |
| 19 | `FS.GA.DIVIDEND.ANNOUNCEMENT.SHORT.DESCRIPTION` | `FsGaDividendAnnouncement_ShortDescription` | TField |  | Input the description of the transaction, else auto generated Multifonds DB Column is TXT_OST. |
| 20 | `FS.GA.DIVIDEND.ANNOUNCEMENT.PAYABLE.TAX.1.PERCENTAGE` | `FsGaDividendAnnouncement_PayableTax1Percentage` | TField |  | Rate of Tax payable on the income , type of tax 1 Multifonds DB Column is PCT_TAX_1. |
| 21 | `FS.GA.DIVIDEND.ANNOUNCEMENT.PAYABLE.TAX.2.PERCENTAGE` | `FsGaDividendAnnouncement_PayableTax2Percentage` | TField |  | Rate of Tax payable on the income , type of tax 2 Multifonds DB Column is PCT_TAX_2. |
| 22 | `FS.GA.DIVIDEND.ANNOUNCEMENT.ENTITLE.DATE` | `FsGaDividendAnnouncement_EntitleDate` | TField |  | This field displays the entitlement date for a security on which a dividend entitlement will be available to shareholders Multifonds DB Column is DENTITLE. |
| 23 | `FS.GA.DIVIDEND.ANNOUNCEMENT.DEAL.STATUS.CODE` | `FsGaDividendAnnouncement_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 24 | `FS.GA.DIVIDEND.ANNOUNCEMENT.SECURITY` | `FsGaDividendAnnouncement_Security` | TField |  | Existing Security identification Multifonds DB Column is NOVAL_LINK. |
| 25 | `FS.GA.DIVIDEND.ANNOUNCEMENT.FEE.1.PERCENTAGE` | `FsGaDividendAnnouncement_Fee1Percentage` | TField |  | Rate of Fees charged on Income , type of fee 1 Multifonds DB Column is MFRAIS1. |
| 26 | `FS.GA.DIVIDEND.ANNOUNCEMENT.FEE.2.PERCENTAGE` | `FsGaDividendAnnouncement_Fee2Percentage` | TField |  | Percentage of Fees charged on Income , type of fee 2 Multifonds DB Column is MFRAIS2. |
| 27 | `FS.GA.DIVIDEND.ANNOUNCEMENT.FRANKED.INCOME.PERCENT` | `FsGaDividendAnnouncement_FrankedIncomePercent` | TField |  | Determines the percentage of Franked income for Franking credit Multifonds DB Column is FRANK_INC. |
| 28 | `FS.GA.DIVIDEND.ANNOUNCEMENT.RECORD.DATE` | `FsGaDividendAnnouncement_RecordDate` | TField |  | The record date, or date of record, is the cut-off date established by a company in order to determine which shareholders are eligible to receive a dividend or distribution Multifonds DB Column is DRECORD. |
| 29 | `FS.GA.DIVIDEND.ANNOUNCEMENT.ISSUE.COUNTRY` | `FsGaDividendAnnouncement_IssueCountry` | TField |  | Internal Identifier for a country, which is used in various places to include or exclude a specific country from a functionality Multifonds DB Column is CPAYSVAL. |
| 30 | `FS.GA.DIVIDEND.ANNOUNCEMENT.NUMBER.SEQUENCE` | `FsGaDividendAnnouncement_NumberSequence` | TField |  | Sequence Number Multifonds DB Column is NO_SEQ. |
| 31 | `FS.GA.DIVIDEND.ANNOUNCEMENT.LONG.DESCRIPTION` | `FsGaDividendAnnouncement_LongDescription` | TField |  | Long description Multifonds DB Column is XLIBELLE_NEW. |
| 32 | `FS.GA.DIVIDEND.ANNOUNCEMENT.CA.TRANSACTION.TYPE` | `FsGaDividendAnnouncement_CaTransactionType` | TField |  | Corresponds to the corporate action transaction type Multifonds DB Column is COPER_CA. |
| 33 | `FS.GA.DIVIDEND.ANNOUNCEMENT.NSEQUENCE` | `FsGaDividendAnnouncement_Nsequence` | TField |  | Corresponds to the sequence number Multifonds DB Column is NSEQ. |
| 34 | `FS.GA.DIVIDEND.ANNOUNCEMENT.SUBSEQUENCE.NUMBER` | `FsGaDividendAnnouncement_SubsequenceNumber` | TField |  | Corresponds to the sub sequence number Multifonds DB Column is NSUB_SEQ. |
| 35 | `FS.GA.DIVIDEND.ANNOUNCEMENT.PA.MODULE` | `FsGaDividendAnnouncement_PaModule` | TField |  | PA Module Multifonds DB Column is FLG_PA_MODULE. |
| 36 | `FS.GA.DIVIDEND.ANNOUNCEMENT.ANNOUNCE.DATE` | `FsGaDividendAnnouncement_AnnounceDate` | TField |  | Announce Date Multifonds DB Column is DANNOUNCE. |
| 37 | `FS.GA.DIVIDEND.ANNOUNCEMENT.ACTION` | `FsGaDividendAnnouncement_Action` | TField |  | Action Multifonds DB Column is ACTION. |
| 38 | `FS.GA.DIVIDEND.ANNOUNCEMENT.PA.STATUS` | `FsGaDividendAnnouncement_PaStatus` | TField |  | PA Status Multifonds DB Column is PA_CDSTATUS. |
| 39 | `FS.GA.DIVIDEND.ANNOUNCEMENT.EXTERNAL.SECURITY.ID` | `FsGaDividendAnnouncement_ExternalSecurityId` | TField |  | The External identification code for Security like 01 for Telekurs, 03 for Sedol. Also used for other provider identifiers Multifonds DB Column is SEC_ID. |
| 40 | `FS.GA.DIVIDEND.ANNOUNCEMENT.SECURITY.ID.CODE` | `FsGaDividendAnnouncement_SecurityIdCode` | TField |  | Security Id Code Multifonds DB Column is ID_CODE_SEC. |
| 41 | `FS.GA.DIVIDEND.ANNOUNCEMENT.DIVIDEND.REINVESTMENT.DATE` | `FsGaDividendAnnouncement_DividendReinvestmentDate` | TField |  | Dividend reinvestment date Multifonds DB Column is DREINV. |
| 42 | `FS.GA.DIVIDEND.ANNOUNCEMENT.DIVIDEND.REINVESTMENT.PRICE` | `FsGaDividendAnnouncement_DividendReinvestmentPrice` | TField |  | The price at which dividend is reinvested. Multifonds DB Column is COURS_REINV. |
| 43 | `FS.GA.DIVIDEND.ANNOUNCEMENT.CONDUIT.FOREIGN.INCOME.PERCENT` | `FsGaDividendAnnouncement_ConduitForeignIncomePercent` | TField |  | Conduit Foreign Income percentage. CFI is ultimately received by a foreign resident through one or more interposed Australian corporate tax entities Multifonds DB Column is CFI_RATE. |
| 44 | `FS.GA.DIVIDEND.ANNOUNCEMENT.CORPORATE.ACTION.TYPE` | `FsGaDividendAnnouncement_CorporateActionType` | TField |  | Corporate Action Type Multifonds DB Column is CA_TYPE. |
| 45 | `FS.GA.DIVIDEND.ANNOUNCEMENT.RESERVED10` | `FsGaDividendAnnouncement_Reserved10` | TField |  |  |
| 46 | `FS.GA.DIVIDEND.ANNOUNCEMENT.RESERVED9` | `FsGaDividendAnnouncement_Reserved9` | TField |  |  |
| 47 | `FS.GA.DIVIDEND.ANNOUNCEMENT.RESERVED8` | `FsGaDividendAnnouncement_Reserved8` | TField |  |  |
| 48 | `FS.GA.DIVIDEND.ANNOUNCEMENT.RESERVED7` | `FsGaDividendAnnouncement_Reserved7` | TField |  |  |
| 49 | `FS.GA.DIVIDEND.ANNOUNCEMENT.RESERVED6` | `FsGaDividendAnnouncement_Reserved6` | TField |  |  |
| 50 | `FS.GA.DIVIDEND.ANNOUNCEMENT.RESERVED5` | `FsGaDividendAnnouncement_Reserved5` | TField |  |  |
| 51 | `FS.GA.DIVIDEND.ANNOUNCEMENT.RESERVED4` | `FsGaDividendAnnouncement_Reserved4` | TField |  |  |
| 52 | `FS.GA.DIVIDEND.ANNOUNCEMENT.RESERVED3` | `FsGaDividendAnnouncement_Reserved3` | TField |  |  |
| 53 | `FS.GA.DIVIDEND.ANNOUNCEMENT.RESERVED2` | `FsGaDividendAnnouncement_Reserved2` | TField |  |  |
| 54 | `FS.GA.DIVIDEND.ANNOUNCEMENT.RESERVED1` | `FsGaDividendAnnouncement_Reserved1` | TField |  |  |
| 55 | `FS.GA.DIVIDEND.ANNOUNCEMENT.LOCAL.REF` | `FsGaDividendAnnouncement_LocalRef` |  |  |  |
| 56 | `FS.GA.DIVIDEND.ANNOUNCEMENT.OVERRIDE` | `FsGaDividendAnnouncement_Override` |  |  |  |
| 57 | `FS.GA.DIVIDEND.ANNOUNCEMENT.RECORD.STATUS` | `FsGaDividendAnnouncement_RecordStatus` | String |  |  |
| 58 | `FS.GA.DIVIDEND.ANNOUNCEMENT.CURR.NO` | `FsGaDividendAnnouncement_CurrNo` | String |  |  |
| 59 | `FS.GA.DIVIDEND.ANNOUNCEMENT.INPUTTER` | `FsGaDividendAnnouncement_Inputter` |  |  |  |
| 60 | `FS.GA.DIVIDEND.ANNOUNCEMENT.DATE.TIME` | `FsGaDividendAnnouncement_DateTime` |  |  |  |
| 61 | `FS.GA.DIVIDEND.ANNOUNCEMENT.AUTHORISER` | `FsGaDividendAnnouncement_Authoriser` | String |  |  |
| 62 | `FS.GA.DIVIDEND.ANNOUNCEMENT.CO.CODE` | `FsGaDividendAnnouncement_CoCode` | String |  |  |
| 63 | `FS.GA.DIVIDEND.ANNOUNCEMENT.DEPT.CODE` | `FsGaDividendAnnouncement_DeptCode` | String |  |  |
| 64 | `FS.GA.DIVIDEND.ANNOUNCEMENT.AUDITOR.CODE` | `FsGaDividendAnnouncement_AuditorCode` | String |  |  |
| 65 | `FS.GA.DIVIDEND.ANNOUNCEMENT.AUDIT.DATE.TIME` | `FsGaDividendAnnouncement_AuditDateTime` | String |  |  |
