# LBNCDR.CUST.FIN.OUT — Table Schema

> Source: `INSERTS/I_F.LBNCDR.CUST.FIN.OUT` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.OUT.AA.CONTRACT.ID` | `LbncdrCustFinOut_AaContractId` |  |  |  |
| 2 | `LBNCDR.OUT.AA.APPLIN` | `LbncdrCustFinOut_AaApplin` |  |  |  |
| 3 | `LBNCDR.OUT.AA.CLIENT.NO` | `LbncdrCustFinOut_AaClientNo` |  |  |  |
| 4 | `LBNCDR.OUT.AA.BRANCH.NO` | `LbncdrCustFinOut_AaBranchNo` |  |  |  |
| 5 | `LBNCDR.OUT.AA.LIMIT.ID` | `LbncdrCustFinOut_AaLimitId` |  |  |  |
| 6 | `LBNCDR.OUT.AA.LIMIT.ALLOC` | `LbncdrCustFinOut_AaLimitAlloc` |  |  |  |
| 7 | `LBNCDR.OUT.AA.LIMIT.UTIL` | `LbncdrCustFinOut_AaLimitUtil` |  |  |  |
| 8 | `LBNCDR.OUT.AA.COLL.RGT` | `LbncdrCustFinOut_AaCollRgt` |  |  |  |
| 9 | `LBNCDR.OUT.AA.COLL.ID` | `LbncdrCustFinOut_AaCollId` |  |  |  |
| 10 | `LBNCDR.OUT.AA.COLL.TYP` | `LbncdrCustFinOut_AaCollTyp` |  |  |  |
| 11 | `LBNCDR.OUT.AA.LIAB.TYPE` | `LbncdrCustFinOut_AaLiabType` |  |  |  |
| 12 | `LBNCDR.OUT.AA.COLL.AMT` | `LbncdrCustFinOut_AaCollAmt` |  |  |  |
| 13 | `LBNCDR.OUT.CREDIT.DETAILS` | `LbncdrCustFinOut_CreditDetails` |  |  |  |
| 14 | `LBNCDR.OUT.LIABILITY.GRP` | `LbncdrCustFinOut_LiabilityGrp` |  |  |  |
| 15 | `LBNCDR.OUT.LIAB.SUB.GRP` | `LbncdrCustFinOut_LiabSubGrp` |  |  |  |
| 16 | `LBNCDR.OUT.LOAN.TYPE` | `LbncdrCustFinOut_LoanType` |  |  |  |
| 17 | `LBNCDR.OUT.CURRENCY.CODE` | `LbncdrCustFinOut_CurrencyCode` |  |  |  |
| 18 | `LBNCDR.OUT.CREDIT.LIMIT` | `LbncdrCustFinOut_CreditLimit` |  |  |  |
| 19 | `LBNCDR.OUT.CREDIT.USED` | `LbncdrCustFinOut_CreditUsed` |  |  |  |
| 20 | `LBNCDR.OUT.ECON.SECTOR` | `LbncdrCustFinOut_EconSector` |  |  |  |
| 21 | `LBNCDR.OUT.REMAIN.PERIOD` | `LbncdrCustFinOut_RemainPeriod` |  |  |  |
| 22 | `LBNCDR.OUT.CLASS.RISK` | `LbncdrCustFinOut_ClassRisk` |  |  |  |
| 23 | `LBNCDR.OUT.MARG` | `LbncdrCustFinOut_Marg` |  |  |  |
| 24 | `LBNCDR.OUT.LIAB.COUNTRY` | `LbncdrCustFinOut_LiabCountry` |  |  |  |
| 25 | `LBNCDR.OUT.TXN.CONTRACT.ID` | `LbncdrCustFinOut_TxnContractId` |  |  |  |
| 26 | `LBNCDR.OUT.TXN.APPLIN` | `LbncdrCustFinOut_TxnApplin` |  |  |  |
| 27 | `LBNCDR.OUT.TXN.CLIENT.NO` | `LbncdrCustFinOut_TxnClientNo` |  |  |  |
| 28 | `LBNCDR.OUT.TXN.BRANCH.NO` | `LbncdrCustFinOut_TxnBranchNo` |  |  |  |
| 29 | `LBNCDR.OUT.TXN.LIMIT.ID` | `LbncdrCustFinOut_TxnLimitId` |  |  |  |
| 30 | `LBNCDR.OUT.TXN.LIMIT.ALLOC` | `LbncdrCustFinOut_TxnLimitAlloc` |  |  |  |
| 31 | `LBNCDR.OUT.TXN.LIMIT.UTIL` | `LbncdrCustFinOut_TxnLimitUtil` |  |  |  |
| 32 | `LBNCDR.OUT.TXN.COLL.RGT` | `LbncdrCustFinOut_TxnCollRgt` |  |  |  |
| 33 | `LBNCDR.OUT.TXN.COLL.ID` | `LbncdrCustFinOut_TxnCollId` |  |  |  |
| 34 | `LBNCDR.OUT.TXN.COLL.TYP` | `LbncdrCustFinOut_TxnCollTyp` |  |  |  |
| 35 | `LBNCDR.OUT.TXN.LIB.TYP` | `LbncdrCustFinOut_TxnLibTyp` |  |  |  |
| 36 | `LBNCDR.OUT.TXN.COLL.AMT` | `LbncdrCustFinOut_TxnCollAmt` |  |  |  |
| 37 | `LBNCDR.OUT.CRED.DETAILS` | `LbncdrCustFinOut_CredDetails` |  |  |  |
| 38 | `LBNCDR.OUT.LIAB.GRP` | `LbncdrCustFinOut_LiabGrp` |  |  |  |
| 39 | `LBNCDR.OUT.LIB.SB.GRP` | `LbncdrCustFinOut_LibSbGrp` |  |  |  |
| 40 | `LBNCDR.OUT.LN.TYP` | `LbncdrCustFinOut_LnTyp` |  |  |  |
| 41 | `LBNCDR.OUT.CCY.CODE` | `LbncdrCustFinOut_CcyCode` |  |  |  |
| 42 | `LBNCDR.OUT.CRE.LIMIT` | `LbncdrCustFinOut_CreLimit` |  |  |  |
| 43 | `LBNCDR.OUT.CRE.USED` | `LbncdrCustFinOut_CreUsed` |  |  |  |
| 44 | `LBNCDR.OUT.ECO.SEC` | `LbncdrCustFinOut_EcoSec` |  |  |  |
| 45 | `LBNCDR.OUT.REM.PER` | `LbncdrCustFinOut_RemPer` |  |  |  |
| 46 | `LBNCDR.OUT.CLS.RSK` | `LbncdrCustFinOut_ClsRsk` |  |  |  |
| 47 | `LBNCDR.OUT.MARGIN` | `LbncdrCustFinOut_Margin` |  |  |  |
| 48 | `LBNCDR.OUT.TOWN.COUNTRY` | `LbncdrCustFinOut_TownCountry` |  |  |  |
| 49 | `LBNCDR.OUT.BANK.RATING` | `LbncdrCustFinOut_BankRating` | TField |  |  |
| 50 | `LBNCDR.OUT.FORMAT.CHARACTER` | `LbncdrCustFinOut_FormatCharacter` | TField |  |  |
| 51 | `LBNCDR.OUT.BRANCH.NUMBER` | `LbncdrCustFinOut_BranchNumber` | TField |  | Holds the brach number of customer Validation Rules 3 A |
| 52 | `LBNCDR.OUT.CLIENT.NUMBER` | `LbncdrCustFinOut_ClientNumber` | TField |  | Holds the new client of temp CDR number value Validation Rules 3 A |
| 53 | `LBNCDR.OUT.CLIENT.SEQUENCE` | `LbncdrCustFinOut_ClientSequence` | TField |  | Holds the sequence value Validation Rules 3 A |
| 54 | `LBNCDR.OUT.OPERATION.TYPE` | `LbncdrCustFinOut_OperationType` | TField |  | Holds the new clients or old clients value Validation Rules 3 A |
| 55 | `LBNCDR.OUT.CLIENT.TYPE` | `LbncdrCustFinOut_ClientType` | TField |  | Holds the type of ind or corp value Validation Rules 3 A |
| 56 | `LBNCDR.OUT.SEX` | `LbncdrCustFinOut_Sex` | TField |  | Holds the sex value Validation Rules 3 A |
| 57 | `LBNCDR.OUT.BIRTH.OR.FOUNDATION.DATE` | `LbncdrCustFinOut_BirthOrFoundationDate` | TField |  | Holds the client birth foundation value Validation Rules 3 A |
| 58 | `LBNCDR.OUT.NATIONALITY` | `LbncdrCustFinOut_Nationality` | TField |  | Holds the client nationality value Validation Rules 3 A |
| 59 | `LBNCDR.OUT.STREET` | `LbncdrCustFinOut_Street` | TField |  | Holds the client street value Validation Rules 3 A |
| 60 | `LBNCDR.OUT.POSTAL.CODE` | `LbncdrCustFinOut_PostalCode` | TField |  | Holds the client poastal code value Validation Rules 3 A |
| 61 | `LBNCDR.OUT.TELEPHONE.NUMBER.1` | `LbncdrCustFinOut_TelephoneNumber1` | TField |  | Holds the client telephone number value Validation Rules 3 A |
| 62 | `LBNCDR.OUT.TELEPHONE.NUMBER` | `LbncdrCustFinOut_TelephoneNumber` | TField |  | Holds the client telephone number value Validation Rules 3 A |
| 63 | `LBNCDR.OUT.CLIENT.CLASSIFIC` | `LbncdrCustFinOut_ClientClassific` | TField |  | Holds the client classification value Validation Rules 3 A |
| 64 | `LBNCDR.OUT.LEGAL.FORM` | `LbncdrCustFinOut_LegalForm` | TField |  | Holds the client legal form value Validation Rules 3 A |
| 65 | `LBNCDR.OUT.JUDICIAL.STATUS` | `LbncdrCustFinOut_JudicialStatus` | TField |  | Holds the client judicial value Validation Rules 3 A |
| 66 | `LBNCDR.OUT.COMMERCIAL.NAMES` | `LbncdrCustFinOut_CommercialNames` | TField |  | Holds the client commercial name value Validation Rules 3 A |
| 67 | `LBNCDR.OUT.RISK.NUMBER` | `LbncdrCustFinOut_RiskNumber` | TField |  | Holds the client CDR NUMBER value Validation Rules 3 A |
| 68 | `LBNCDR.OUT.PARTICIPATION.PERC` | `LbncdrCustFinOut_ParticipationPerc` | TField |  | Holds the client percentage value Validation Rules 3 A |
| 69 | `LBNCDR.OUT.CREDIT.PROTFOLIO` | `LbncdrCustFinOut_CreditProtfolio` | TField |  | Holds the client credit portfolio value Validation Rules 3 A |
| 70 | `LBNCDR.OUT.FORMAT.CHRACTER` | `LbncdrCustFinOut_FormatChracter` | TField |  |  |
| 71 | `LBNCDR.OUT.ADDRESS.LOCATION.CO` | `LbncdrCustFinOut_AddressLocationCo` | TField |  |  |
| 72 | `LBNCDR.OUT.CITY.VILLAGE` | `LbncdrCustFinOut_CityVillage` | TField |  |  |
| 73 | `LBNCDR.OUT.AV.CREDIT.DETAILS` | `LbncdrCustFinOut_AvCreditDetails` |  |  |  |
| 74 | `LBNCDR.OUT.AV.LIABILITY.GRP` | `LbncdrCustFinOut_AvLiabilityGrp` |  |  |  |
| 75 | `LBNCDR.OUT.AV.LIAB.SUB.GRP` | `LbncdrCustFinOut_AvLiabSubGrp` |  |  |  |
| 76 | `LBNCDR.OUT.AV.LIAB.TYPE` | `LbncdrCustFinOut_AvLiabType` |  |  |  |
| 77 | `LBNCDR.OUT.AV.LOAN.TYPE` | `LbncdrCustFinOut_AvLoanType` |  |  |  |
| 78 | `LBNCDR.OUT.AV.CURRENCY.CODE` | `LbncdrCustFinOut_AvCurrencyCode` |  |  |  |
| 79 | `LBNCDR.OUT.AV.CREDIT.LIMIT` | `LbncdrCustFinOut_AvCreditLimit` |  |  |  |
| 80 | `LBNCDR.OUT.AV.CREDIT.USED` | `LbncdrCustFinOut_AvCreditUsed` |  |  |  |
| 81 | `LBNCDR.OUT.AV.ECON.SECTOR` | `LbncdrCustFinOut_AvEconSector` |  |  |  |
| 82 | `LBNCDR.OUT.AV.REMAIN.PERIOD` | `LbncdrCustFinOut_AvRemainPeriod` |  |  |  |
| 83 | `LBNCDR.OUT.AV.CLASS.RISK` | `LbncdrCustFinOut_AvClassRisk` |  |  |  |
| 84 | `LBNCDR.OUT.AV.MARG` | `LbncdrCustFinOut_AvMarg` |  |  |  |
| 85 | `LBNCDR.OUT.AV.LIAB.COUNTRY` | `LbncdrCustFinOut_AvLiabCountry` |  |  |  |
| 86 | `LBNCDR.OUT.RESERVED.1` | `LbncdrCustFinOut_Reserved1` | TField |  |  |
| 87 | `LBNCDR.OUT.RESERVED.2` | `LbncdrCustFinOut_Reserved2` | TField |  |  |
| 88 | `LBNCDR.OUT.RESERVED.3` | `LbncdrCustFinOut_Reserved3` | TField |  |  |
| 89 | `LBNCDR.OUT.RESERVED.4` | `LbncdrCustFinOut_Reserved4` | TField |  |  |
| 90 | `LBNCDR.OUT.RESERVED.5` | `LbncdrCustFinOut_Reserved5` | TField |  |  |
| 91 | `LBNCDR.OUT.RESERVED.6` | `LbncdrCustFinOut_Reserved6` | TField |  |  |
| 92 | `LBNCDR.OUT.RESERVED.7` | `LbncdrCustFinOut_Reserved7` | TField |  |  |
| 93 | `LBNCDR.OUT.RESERVED.8` | `LbncdrCustFinOut_Reserved8` | TField |  |  |
