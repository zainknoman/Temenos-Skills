# AC.EXTERNAL.CONTRACT — Table Schema

> Source: `INSERTS/I_F.AC.EXTERNAL.CONTRACT` in `AC_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.XC.CUSTOMER.ID` | `AcExternalContract_CustomerId` |  |  |  |
| 2 | `AC.XC.REPORTING.CUSTOMER` | `AcExternalContract_ReportingCustomer` |  |  |  |
| 3 | `AC.XC.JOINT.OWNERSHIP.PERCENTAGE` | `AcExternalContract_JointOwnershipPercentage` |  |  |  |
| 4 | `AC.XC.JOINT.OWNER` | `AcExternalContract_JointOwner` |  |  |  |
| 5 | `AC.XC.PRIMARY.CUSTOMER` | `AcExternalContract_PrimaryCustomer` | TField |  |  |
| 6 | `AC.XC.CATEGORY` | `AcExternalContract_Category` | TField |  |  |
| 7 | `AC.XC.POSITION.TYPE` | `AcExternalContract_PositionType` | TField |  |  |
| 8 | `AC.XC.CURRENCY` | `AcExternalContract_Currency` | TField |  |  |
| 9 | `AC.XC.CURRENCY.MARKET` | `AcExternalContract_CurrencyMarket` | TField |  |  |
| 10 | `AC.XC.ACCOUNT.OFFICER` | `AcExternalContract_AccountOfficer` | TField |  |  |
| 11 | `AC.XC.START.DATE` | `AcExternalContract_StartDate` | TField |  |  |
| 12 | `AC.XC.MATURITY.DATE` | `AcExternalContract_MaturityDate` | TField |  |  |
| 13 | `AC.XC.BOOK.DATE` | `AcExternalContract_BookDate` | TField |  |  |
| 14 | `AC.XC.CONTRACT.ID` | `AcExternalContract_ContractId` | TField |  |  |
| 15 | `AC.XC.COMPANY.ID` | `AcExternalContract_CompanyId` | TField |  |  |
| 16 | `AC.XC.SOURCE.SYSTEM` | `AcExternalContract_SourceSystem` | TField |  |  |
| 17 | `AC.XC.CONTRACT.STATUS` | `AcExternalContract_ContractStatus` | TField |  |  |
| 18 | `AC.XC.PRODUCT.LINE` | `AcExternalContract_ProductLine` | TField |  |  |
| 19 | `AC.XC.REVOLVING` | `AcExternalContract_Revolving` | TField |  |  |
| 20 | `AC.XC.JOINT.LIABILITY` | `AcExternalContract_JointLiability` | TField |  |  |
| 21 | `AC.XC.LIMIT.ID` | `AcExternalContract_LimitId` | TField |  |  |
| 22 | `AC.XC.LIMIT.PRODUCT` | `AcExternalContract_LimitProduct` | TField |  |  |
| 23 | `AC.XC.PREV.LIMIT.ID` | `AcExternalContract_PrevLimitId` | TField |  |  |
| 24 | `AC.XC.UNIQUE.LIMIT` | `AcExternalContract_UniqueLimit` | TField |  |  |
| 25 | `AC.XC.CONTRIBUTE.CR.BALANCE` | `AcExternalContract_ContributeCrBalance` | TField |  |  |
| 26 | `AC.XC.COMMITMENT.CONTRACT` | `AcExternalContract_CommitmentContract` | TField |  |  |
| 27 | `AC.XC.CLOSED.FLAG` | `AcExternalContract_ClosedFlag` | TField |  |  |
| 28 | `AC.XC.CLOSED.DATE` | `AcExternalContract_ClosedDate` | TField |  |  |
| 29 | `AC.XC.SYSTEM.ID` | `AcExternalContract_SystemId` | TField |  |  |
| 30 | `AC.XC.RESERVED.1` | `AcExternalContract_Reserved1` |  |  |  |
| 31 | `AC.XC.RESERVED.2` | `AcExternalContract_Reserved2` | TField |  |  |
| 32 | `AC.XC.RESERVED.3` | `AcExternalContract_Reserved3` | TField |  |  |
| 33 | `AC.XC.RESERVED.4` | `AcExternalContract_Reserved4` | TField |  |  |
| 34 | `AC.XC.RESERVED.5` | `AcExternalContract_Reserved5` | TField |  |  |
| 35 | `AC.XC.RESERVED.6` | `AcExternalContract_Reserved6` | TField |  |  |
| 36 | `AC.XC.RESERVED.7` | `AcExternalContract_Reserved7` | TField |  |  |
| 37 | `AC.XC.RESERVED.8` | `AcExternalContract_Reserved8` | TField |  |  |
| 38 | `AC.XC.RESERVED.9` | `AcExternalContract_Reserved9` | TField |  |  |
| 39 | `AC.XC.RESERVED.10` | `AcExternalContract_Reserved10` | TField |  |  |
| 40 | `AC.XC.LOCAL.REF` | `AcExternalContract_LocalRef` |  |  |  |
| 41 | `AC.XC.OVERRIDE` | `AcExternalContract_Override` |  |  |  |
| 42 | `AC.XC.RECORD.STATUS` | `AcExternalContract_RecordStatus` | String |  |  |
| 43 | `AC.XC.CURR.NO` | `AcExternalContract_CurrNo` | String |  |  |
| 44 | `AC.XC.INPUTTER` | `AcExternalContract_Inputter` |  |  |  |
| 45 | `AC.XC.DATE.TIME` | `AcExternalContract_DateTime` |  |  |  |
| 46 | `AC.XC.AUTHORISER` | `AcExternalContract_Authoriser` | String |  |  |
| 47 | `AC.XC.CO.CODE` | `AcExternalContract_CoCode` | String |  |  |
| 48 | `AC.XC.DEPT.CODE` | `AcExternalContract_DeptCode` | String |  |  |
| 49 | `AC.XC.AUDITOR.CODE` | `AcExternalContract_AuditorCode` | String |  |  |
| 50 | `AC.XC.AUDIT.DATE.TIME` | `AcExternalContract_AuditDateTime` | String |  |  |
