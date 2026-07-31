# LBNCDR.CUST.FIN.AMEND — Table Schema

> Source: `INSERTS/I_F.LBNCDR.CUST.FIN.AMEND` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.AMEND.AA.CONTRACT.ID` | `LbncdrCustFinAmend_AaContractId` |  |  |  |
| 2 | `LBNCDR.AMEND.AA.APPLIN` | `LbncdrCustFinAmend_AaApplin` |  |  |  |
| 3 | `LBNCDR.AMEND.AA.CLIENT.NO` | `LbncdrCustFinAmend_AaClientNo` |  |  |  |
| 4 | `LBNCDR.AMEND.AA.BRANCH.NO` | `LbncdrCustFinAmend_AaBranchNo` |  |  |  |
| 5 | `LBNCDR.AMEND.AA.LIMIT.ID` | `LbncdrCustFinAmend_AaLimitId` |  |  |  |
| 6 | `LBNCDR.AMEND.AA.LIMIT.ALLOC` | `LbncdrCustFinAmend_AaLimitAlloc` |  |  |  |
| 7 | `LBNCDR.AMEND.AA.LIMIT.UTIL` | `LbncdrCustFinAmend_AaLimitUtil` |  |  |  |
| 8 | `LBNCDR.AMEND.AA.COLL.RGT` | `LbncdrCustFinAmend_AaCollRgt` |  |  |  |
| 9 | `LBNCDR.AMEND.AA.COLL.ID` | `LbncdrCustFinAmend_AaCollId` |  |  |  |
| 10 | `LBNCDR.AMEND.AA.COLL.TYP` | `LbncdrCustFinAmend_AaCollTyp` |  |  |  |
| 11 | `LBNCDR.AMEND.AA.LIAB.TYPE` | `LbncdrCustFinAmend_AaLiabType` |  |  |  |
| 12 | `LBNCDR.AMEND.AA.COLL.AMT` | `LbncdrCustFinAmend_AaCollAmt` |  |  |  |
| 13 | `LBNCDR.AMEND.CREDIT.DETAILS` | `LbncdrCustFinAmend_CreditDetails` |  |  |  |
| 14 | `LBNCDR.AMEND.LIABILITY.GRP` | `LbncdrCustFinAmend_LiabilityGrp` |  |  |  |
| 15 | `LBNCDR.AMEND.LIAB.SUB.GRP` | `LbncdrCustFinAmend_LiabSubGrp` |  |  |  |
| 16 | `LBNCDR.AMEND.LOAN.TYPE` | `LbncdrCustFinAmend_LoanType` |  |  |  |
| 17 | `LBNCDR.AMEND.CURRENCY.CODE` | `LbncdrCustFinAmend_CurrencyCode` |  |  |  |
| 18 | `LBNCDR.AMEND.CREDIT.LIMIT` | `LbncdrCustFinAmend_CreditLimit` |  |  |  |
| 19 | `LBNCDR.AMEND.CREDIT.USED` | `LbncdrCustFinAmend_CreditUsed` |  |  |  |
| 20 | `LBNCDR.AMEND.ECON.SECTOR` | `LbncdrCustFinAmend_EconSector` |  |  |  |
| 21 | `LBNCDR.AMEND.REMAIN.PERIOD` | `LbncdrCustFinAmend_RemainPeriod` |  |  |  |
| 22 | `LBNCDR.AMEND.CLASS.RISK` | `LbncdrCustFinAmend_ClassRisk` |  |  |  |
| 23 | `LBNCDR.AMEND.MARG` | `LbncdrCustFinAmend_Marg` |  |  |  |
| 24 | `LBNCDR.AMEND.LIAB.COUNTRY` | `LbncdrCustFinAmend_LiabCountry` |  |  |  |
| 25 | `LBNCDR.AMEND.TXN.CONTRACT.ID` | `LbncdrCustFinAmend_TxnContractId` |  |  |  |
| 26 | `LBNCDR.AMEND.TXN.APPLIN` | `LbncdrCustFinAmend_TxnApplin` |  |  |  |
| 27 | `LBNCDR.AMEND.TXN.CLIENT.NO` | `LbncdrCustFinAmend_TxnClientNo` |  |  |  |
| 28 | `LBNCDR.AMEND.TXN.BRANCH.NO` | `LbncdrCustFinAmend_TxnBranchNo` |  |  |  |
| 29 | `LBNCDR.AMEND.TXN.LIMIT.ID` | `LbncdrCustFinAmend_TxnLimitId` |  |  |  |
| 30 | `LBNCDR.AMEND.TXN.LIMIT.ALLOC` | `LbncdrCustFinAmend_TxnLimitAlloc` |  |  |  |
| 31 | `LBNCDR.AMEND.TXN.LIMIT.UTIL` | `LbncdrCustFinAmend_TxnLimitUtil` |  |  |  |
| 32 | `LBNCDR.AMEND.TXN.COLL.RGT` | `LbncdrCustFinAmend_TxnCollRgt` |  |  |  |
| 33 | `LBNCDR.AMEND.TXN.COLL.ID` | `LbncdrCustFinAmend_TxnCollId` |  |  |  |
| 34 | `LBNCDR.AMEND.TXN.COLL.TYP` | `LbncdrCustFinAmend_TxnCollTyp` |  |  |  |
| 35 | `LBNCDR.AMEND.TXN.LIB.TYP` | `LbncdrCustFinAmend_TxnLibTyp` |  |  |  |
| 36 | `LBNCDR.AMEND.TXN.COLL.AMT` | `LbncdrCustFinAmend_TxnCollAmt` |  |  |  |
| 37 | `LBNCDR.AMEND.CRED.DETAILS` | `LbncdrCustFinAmend_CredDetails` |  |  |  |
| 38 | `LBNCDR.AMEND.LIAB.GRP` | `LbncdrCustFinAmend_LiabGrp` |  |  |  |
| 39 | `LBNCDR.AMEND.LIB.SB.GRP` | `LbncdrCustFinAmend_LibSbGrp` |  |  |  |
| 40 | `LBNCDR.AMEND.LN.TYP` | `LbncdrCustFinAmend_LnTyp` |  |  |  |
| 41 | `LBNCDR.AMEND.CCY.CODE` | `LbncdrCustFinAmend_CcyCode` |  |  |  |
| 42 | `LBNCDR.AMEND.CRE.LIMIT` | `LbncdrCustFinAmend_CreLimit` |  |  |  |
| 43 | `LBNCDR.AMEND.CRE.USED` | `LbncdrCustFinAmend_CreUsed` |  |  |  |
| 44 | `LBNCDR.AMEND.ECO.SEC` | `LbncdrCustFinAmend_EcoSec` |  |  |  |
| 45 | `LBNCDR.AMEND.REM.PER` | `LbncdrCustFinAmend_RemPer` |  |  |  |
| 46 | `LBNCDR.AMEND.CLS.RSK` | `LbncdrCustFinAmend_ClsRsk` |  |  |  |
| 47 | `LBNCDR.AMEND.MARGIN` | `LbncdrCustFinAmend_Margin` |  |  |  |
| 48 | `LBNCDR.AMEND.TOWN.COUNTRY` | `LbncdrCustFinAmend_TownCountry` |  |  |  |
| 49 | `LBNCDR.AMEND.BANK.RATING` | `LbncdrCustFinAmend_BankRating` | TField |  |  |
| 50 | `LBNCDR.AMEND.FORMAT.CHARACTER` | `LbncdrCustFinAmend_FormatCharacter` | TField |  |  |
| 51 | `LBNCDR.AMEND.BRANCH.NUMBER` | `LbncdrCustFinAmend_BranchNumber` | TField |  | Holds the brach number of customer Validation Rules 3 A |
| 52 | `LBNCDR.AMEND.CLIENT.NUMBER` | `LbncdrCustFinAmend_ClientNumber` | TField |  | Holds the new client of temp CDR number value Validation Rules 3 A |
| 53 | `LBNCDR.AMEND.CLIENT.SEQUENCE` | `LbncdrCustFinAmend_ClientSequence` | TField |  | Holds the sequence value Validation Rules 3 A |
| 54 | `LBNCDR.AMEND.OPERATION.TYPE` | `LbncdrCustFinAmend_OperationType` | TField |  | Holds the new clients or old clients value Validation Rules 3 A |
| 55 | `LBNCDR.AMEND.CLIENT.TYPE` | `LbncdrCustFinAmend_ClientType` | TField |  | Holds the type of ind or corp value Validation Rules 3 A |
| 56 | `LBNCDR.AMEND.SEX` | `LbncdrCustFinAmend_Sex` | TField |  | Holds the sex value Validation Rules 3 A |
| 57 | `LBNCDR.AMEND.BIRTH.OR.FOUNDATION.DATE` | `LbncdrCustFinAmend_BirthOrFoundationDate` | TField |  | Holds the client birth foundation value Validation Rules 3 A |
| 58 | `LBNCDR.AMEND.NATIONALITY` | `LbncdrCustFinAmend_Nationality` | TField |  | Holds the client nationality value Validation Rules 3 A |
| 59 | `LBNCDR.AMEND.STREET` | `LbncdrCustFinAmend_Street` | TField |  | Holds the client street value Validation Rules 3 A |
| 60 | `LBNCDR.AMEND.POSTAL.CODE` | `LbncdrCustFinAmend_PostalCode` | TField |  | Holds the client poastal code value Validation Rules 3 A |
| 61 | `LBNCDR.AMEND.TELEPHONE.NUMBER.1` | `LbncdrCustFinAmend_TelephoneNumber1` | TField |  | Holds the client telephone number value Validation Rules 3 A |
| 62 | `LBNCDR.AMEND.TELEPHONE.NUMBER` | `LbncdrCustFinAmend_TelephoneNumber` | TField |  | Holds the client telephone number value Validation Rules 3 A |
| 63 | `LBNCDR.AMEND.CLIENT.CLASSIFIC` | `LbncdrCustFinAmend_ClientClassific` | TField |  | Holds the client classification value Validation Rules 3 A |
| 64 | `LBNCDR.AMEND.LEGAL.FORM` | `LbncdrCustFinAmend_LegalForm` | TField |  | Holds the client legal form value Validation Rules 3 A |
| 65 | `LBNCDR.AMEND.JUDICIAL.STATUS` | `LbncdrCustFinAmend_JudicialStatus` | TField |  | Holds the client judicial value Validation Rules 3 A |
| 66 | `LBNCDR.AMEND.COMMERCIAL.NAMES` | `LbncdrCustFinAmend_CommercialNames` | TField |  | Holds the client commercial name value Validation Rules 3 A |
| 67 | `LBNCDR.AMEND.RISK.NUMBER` | `LbncdrCustFinAmend_RiskNumber` | TField |  | Holds the client CDR NUMBER value Validation Rules 3 A |
| 68 | `LBNCDR.AMEND.PARTICIPATION.PERC` | `LbncdrCustFinAmend_ParticipationPerc` | TField |  | Holds the client percentage value Validation Rules 3 A |
| 69 | `LBNCDR.AMEND.CREDIT.PROTFOLIO` | `LbncdrCustFinAmend_CreditProtfolio` | TField |  | Holds the client credit portfolio value Validation Rules 3 A |
| 70 | `LBNCDR.AMEND.FORMAT.CHRACTER` | `LbncdrCustFinAmend_FormatChracter` | TField |  |  |
| 71 | `LBNCDR.AMEND.ADDRESS.LOCATION.CO` | `LbncdrCustFinAmend_AddressLocationCo` | TField |  |  |
| 72 | `LBNCDR.AMEND.CITY.VILLAGE` | `LbncdrCustFinAmend_CityVillage` | TField |  |  |
| 73 | `LBNCDR.AMEND.EXTRACT.CDR` | `LbncdrCustFinAmend_ExtractCdr` | TField |  |  |
| 74 | `LBNCDR.AMEND.ERROR.CASE` | `LbncdrCustFinAmend_ErrorCase` | TField |  |  |
| 75 | `LBNCDR.AMEND.RESERVED.1` | `LbncdrCustFinAmend_Reserved1` | TField |  |  |
| 76 | `LBNCDR.AMEND.RESERVED.2` | `LbncdrCustFinAmend_Reserved2` | TField |  |  |
| 77 | `LBNCDR.AMEND.RESERVED.3` | `LbncdrCustFinAmend_Reserved3` | TField |  |  |
| 78 | `LBNCDR.AMEND.RESERVED.4` | `LbncdrCustFinAmend_Reserved4` | TField |  |  |
| 79 | `LBNCDR.AMEND.RESERVED.5` | `LbncdrCustFinAmend_Reserved5` | TField |  |  |
| 80 | `LBNCDR.AMEND.RESERVED.6` | `LbncdrCustFinAmend_Reserved6` | TField |  |  |
| 81 | `LBNCDR.AMEND.RESERVED.7` | `LbncdrCustFinAmend_Reserved7` | TField |  |  |
| 82 | `LBNCDR.AMEND.RESERVED.8` | `LbncdrCustFinAmend_Reserved8` | TField |  |  |
| 83 | `LBNCDR.AMEND.LOCAL.REF` | `LbncdrCustFinAmend_LocalRef` |  |  |  |
| 84 | `LBNCDR.AMEND.OVERRIDE` | `LbncdrCustFinAmend_Override` |  |  |  |
| 85 | `LBNCDR.AMEND.RECORD.STATUS` | `LbncdrCustFinAmend_RecordStatus` | String |  |  |
| 86 | `LBNCDR.AMEND.CURR.NO` | `LbncdrCustFinAmend_CurrNo` | String |  |  |
| 87 | `LBNCDR.AMEND.INPUTTER` | `LbncdrCustFinAmend_Inputter` |  |  |  |
| 88 | `LBNCDR.AMEND.DATE.TIME` | `LbncdrCustFinAmend_DateTime` |  |  |  |
| 89 | `LBNCDR.AMEND.AUTHORISER` | `LbncdrCustFinAmend_Authoriser` | String |  |  |
| 90 | `LBNCDR.AMEND.CO.CODE` | `LbncdrCustFinAmend_CoCode` | String |  |  |
| 91 | `LBNCDR.AMEND.DEPT.CODE` | `LbncdrCustFinAmend_DeptCode` | String |  |  |
| 92 | `LBNCDR.AMEND.AUDITOR.CODE` | `LbncdrCustFinAmend_AuditorCode` | String |  |  |
| 93 | `LBNCDR.AMEND.AUDIT.DATE.TIME` | `LbncdrCustFinAmend_AuditDateTime` | String |  |  |
