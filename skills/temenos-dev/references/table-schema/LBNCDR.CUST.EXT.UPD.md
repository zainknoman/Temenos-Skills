# LBNCDR.CUST.EXT.UPD — Table Schema

> Source: `INSERTS/I_F.LBNCDR.CUST.EXT.UPD` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.UPD.AA.CONTRACT.ID` | `LbncdrCustExtUpd_AaContractId` |  |  |  |
| 2 | `LBNCDR.UPD.AA.APPLIN` | `LbncdrCustExtUpd_AaApplin` |  |  |  |
| 3 | `LBNCDR.UPD.AA.CLIENT.NO` | `LbncdrCustExtUpd_AaClientNo` |  |  |  |
| 4 | `LBNCDR.UPD.AA.BRANCH.NO` | `LbncdrCustExtUpd_AaBranchNo` |  |  |  |
| 5 | `LBNCDR.UPD.AA.LIMIT.ID` | `LbncdrCustExtUpd_AaLimitId` |  |  |  |
| 6 | `LBNCDR.UPD.AA.LIMIT.ALLOC` | `LbncdrCustExtUpd_AaLimitAlloc` |  |  |  |
| 7 | `LBNCDR.UPD.AA.LIMIT.UTIL` | `LbncdrCustExtUpd_AaLimitUtil` |  |  |  |
| 8 | `LBNCDR.UPD.AA.COLL.RGT` | `LbncdrCustExtUpd_AaCollRgt` |  |  |  |
| 9 | `LBNCDR.UPD.AA.COLL.ID` | `LbncdrCustExtUpd_AaCollId` |  |  |  |
| 10 | `LBNCDR.UPD.AA.COLL.TYP` | `LbncdrCustExtUpd_AaCollTyp` |  |  |  |
| 11 | `LBNCDR.UPD.AA.LIAB.TYPE` | `LbncdrCustExtUpd_AaLiabType` |  |  |  |
| 12 | `LBNCDR.UPD.AA.COLL.AMT` | `LbncdrCustExtUpd_AaCollAmt` |  |  |  |
| 13 | `LBNCDR.UPD.CREDIT.DETAILS` | `LbncdrCustExtUpd_CreditDetails` |  |  |  |
| 14 | `LBNCDR.UPD.LIABILITY.GRP` | `LbncdrCustExtUpd_LiabilityGrp` |  |  |  |
| 15 | `LBNCDR.UPD.LIAB.SUB.GRP` | `LbncdrCustExtUpd_LiabSubGrp` |  |  |  |
| 16 | `LBNCDR.UPD.LOAN.TYPE` | `LbncdrCustExtUpd_LoanType` |  |  |  |
| 17 | `LBNCDR.UPD.CURRENCY.CODE` | `LbncdrCustExtUpd_CurrencyCode` |  |  |  |
| 18 | `LBNCDR.UPD.CREDIT.LIMIT` | `LbncdrCustExtUpd_CreditLimit` |  |  |  |
| 19 | `LBNCDR.UPD.CREDIT.USED` | `LbncdrCustExtUpd_CreditUsed` |  |  |  |
| 20 | `LBNCDR.UPD.ECON.SECTOR` | `LbncdrCustExtUpd_EconSector` |  |  |  |
| 21 | `LBNCDR.UPD.REMAIN.PERIOD` | `LbncdrCustExtUpd_RemainPeriod` |  |  |  |
| 22 | `LBNCDR.UPD.CLASS.RISK` | `LbncdrCustExtUpd_ClassRisk` |  |  |  |
| 23 | `LBNCDR.UPD.MARG` | `LbncdrCustExtUpd_Marg` |  |  |  |
| 24 | `LBNCDR.UPD.LIAB.COUNTRY` | `LbncdrCustExtUpd_LiabCountry` |  |  |  |
| 25 | `LBNCDR.UPD.TXN.CONTRACT.ID` | `LbncdrCustExtUpd_TxnContractId` |  |  |  |
| 26 | `LBNCDR.UPD.TXN.APPLIN` | `LbncdrCustExtUpd_TxnApplin` |  |  |  |
| 27 | `LBNCDR.UPD.TXN.CLIENT.NO` | `LbncdrCustExtUpd_TxnClientNo` |  |  |  |
| 28 | `LBNCDR.UPD.TXN.BRANCH.NO` | `LbncdrCustExtUpd_TxnBranchNo` |  |  |  |
| 29 | `LBNCDR.UPD.TXN.LIMIT.ID` | `LbncdrCustExtUpd_TxnLimitId` |  |  |  |
| 30 | `LBNCDR.UPD.TXN.LIMIT.ALLOC` | `LbncdrCustExtUpd_TxnLimitAlloc` |  |  |  |
| 31 | `LBNCDR.UPD.TXN.LIMIT.UTIL` | `LbncdrCustExtUpd_TxnLimitUtil` |  |  |  |
| 32 | `LBNCDR.UPD.TXN.COLL.RGT` | `LbncdrCustExtUpd_TxnCollRgt` |  |  |  |
| 33 | `LBNCDR.UPD.TXN.COLL.ID` | `LbncdrCustExtUpd_TxnCollId` |  |  |  |
| 34 | `LBNCDR.UPD.TXN.COLL.TYP` | `LbncdrCustExtUpd_TxnCollTyp` |  |  |  |
| 35 | `LBNCDR.UPD.TXN.LIB.TYP` | `LbncdrCustExtUpd_TxnLibTyp` |  |  |  |
| 36 | `LBNCDR.UPD.TXN.COLL.AMT` | `LbncdrCustExtUpd_TxnCollAmt` |  |  |  |
| 37 | `LBNCDR.UPD.CRED.DETAILS` | `LbncdrCustExtUpd_CredDetails` |  |  |  |
| 38 | `LBNCDR.UPD.LIAB.GRP` | `LbncdrCustExtUpd_LiabGrp` |  |  |  |
| 39 | `LBNCDR.UPD.LIB.SB.GRP` | `LbncdrCustExtUpd_LibSbGrp` |  |  |  |
| 40 | `LBNCDR.UPD.LN.TYP` | `LbncdrCustExtUpd_LnTyp` |  |  |  |
| 41 | `LBNCDR.UPD.CCY.CODE` | `LbncdrCustExtUpd_CcyCode` |  |  |  |
| 42 | `LBNCDR.UPD.CRE.LIMIT` | `LbncdrCustExtUpd_CreLimit` |  |  |  |
| 43 | `LBNCDR.UPD.CRE.USED` | `LbncdrCustExtUpd_CreUsed` |  |  |  |
| 44 | `LBNCDR.UPD.ECO.SEC` | `LbncdrCustExtUpd_EcoSec` |  |  |  |
| 45 | `LBNCDR.UPD.REM.PER` | `LbncdrCustExtUpd_RemPer` |  |  |  |
| 46 | `LBNCDR.UPD.CLS.RSK` | `LbncdrCustExtUpd_ClsRsk` |  |  |  |
| 47 | `LBNCDR.UPD.MARGIN` | `LbncdrCustExtUpd_Margin` |  |  |  |
| 48 | `LBNCDR.UPD.TOWN.COUNTRY` | `LbncdrCustExtUpd_TownCountry` |  |  |  |
| 49 | `LBNCDR.UPD.BANK.RATING` | `LbncdrCustExtUpd_BankRating` | TField |  |  |
| 50 | `LBNCDR.UPD.FORMAT.CHARACTER` | `LbncdrCustExtUpd_FormatCharacter` | TField |  |  |
| 51 | `LBNCDR.UPD.BRANCH.NUMBER` | `LbncdrCustExtUpd_BranchNumber` | TField |  | Holds the brach number of customer Validation Rules 3 A |
| 52 | `LBNCDR.UPD.CLIENT.NUMBER` | `LbncdrCustExtUpd_ClientNumber` | TField |  | Holds the new client of temp CDR number value Validation Rules 3 A |
| 53 | `LBNCDR.UPD.CLIENT.SEQUENCE` | `LbncdrCustExtUpd_ClientSequence` | TField |  | Holds the sequence value Validation Rules 3 A |
| 54 | `LBNCDR.UPD.OPERATION.TYPE` | `LbncdrCustExtUpd_OperationType` | TField |  | Holds the new clients or old clients value Validation Rules 3 A |
| 55 | `LBNCDR.UPD.CLIENT.TYPE` | `LbncdrCustExtUpd_ClientType` | TField |  | Holds the type of ind or corp value Validation Rules 3 A |
| 56 | `LBNCDR.UPD.SEX` | `LbncdrCustExtUpd_Sex` | TField |  | Holds the sex value Validation Rules 3 A |
| 57 | `LBNCDR.UPD.BIRTH.OR.FOUNDATION.DATE` | `LbncdrCustExtUpd_BirthOrFoundationDate` | TField |  | Holds the client birth foundation value Validation Rules 3 A |
| 58 | `LBNCDR.UPD.NATIONALITY` | `LbncdrCustExtUpd_Nationality` | TField |  | Holds the client nationality value Validation Rules 3 A |
| 59 | `LBNCDR.UPD.STREET` | `LbncdrCustExtUpd_Street` | TField |  | Holds the client street value Validation Rules 3 A |
| 60 | `LBNCDR.UPD.POSTAL.CODE` | `LbncdrCustExtUpd_PostalCode` | TField |  | Holds the client poastal code value Validation Rules 3 A |
| 61 | `LBNCDR.UPD.TELEPHONE.NUMBER.1` | `LbncdrCustExtUpd_TelephoneNumber1` | TField |  | Holds the client telephone number value Validation Rules 3 A |
| 62 | `LBNCDR.UPD.TELEPHONE.NUMBER` | `LbncdrCustExtUpd_TelephoneNumber` | TField |  | Holds the client telephone number value Validation Rules 3 A |
| 63 | `LBNCDR.UPD.CLIENT.CLASSIFIC` | `LbncdrCustExtUpd_ClientClassific` | TField |  | Holds the client classification value Validation Rules 3 A |
| 64 | `LBNCDR.UPD.LEGAL.FORM` | `LbncdrCustExtUpd_LegalForm` | TField |  | Holds the client legal form value Validation Rules 3 A |
| 65 | `LBNCDR.UPD.JUDICIAL.STATUS` | `LbncdrCustExtUpd_JudicialStatus` | TField |  | Holds the client judicial value Validation Rules 3 A |
| 66 | `LBNCDR.UPD.COMMERCIAL.NAMES` | `LbncdrCustExtUpd_CommercialNames` | TField |  | Holds the client commercial name value Validation Rules 3 A |
| 67 | `LBNCDR.UPD.RISK.NUMBER` | `LbncdrCustExtUpd_RiskNumber` | TField |  | Holds the client CDR NUMBER value Validation Rules 3 A |
| 68 | `LBNCDR.UPD.PARTICIPATION.PERC` | `LbncdrCustExtUpd_ParticipationPerc` | TField |  | Holds the client percentage value Validation Rules 3 A |
| 69 | `LBNCDR.UPD.CREDIT.PROTFOLIO` | `LbncdrCustExtUpd_CreditProtfolio` | TField |  | Holds the client credit portfolio value Validation Rules 3 A |
| 70 | `LBNCDR.UPD.FORMAT.CHRACTER` | `LbncdrCustExtUpd_FormatChracter` | TField |  |  |
| 71 | `LBNCDR.UPD.ADDRESS.LOCATION.CO` | `LbncdrCustExtUpd_AddressLocationCo` | TField |  |  |
| 72 | `LBNCDR.UPD.CITY.VILLAGE` | `LbncdrCustExtUpd_CityVillage` | TField |  |  |
| 73 | `LBNCDR.UPD.RESERVED.1` | `LbncdrCustExtUpd_Reserved1` | TField |  |  |
| 74 | `LBNCDR.UPD.RESERVED.2` | `LbncdrCustExtUpd_Reserved2` | TField |  |  |
| 75 | `LBNCDR.UPD.RESERVED.3` | `LbncdrCustExtUpd_Reserved3` | TField |  |  |
| 76 | `LBNCDR.UPD.RESERVED.4` | `LbncdrCustExtUpd_Reserved4` | TField |  |  |
| 77 | `LBNCDR.UPD.RESERVED.5` | `LbncdrCustExtUpd_Reserved5` | TField |  |  |
| 78 | `LBNCDR.UPD.RESERVED.6` | `LbncdrCustExtUpd_Reserved6` | TField |  |  |
| 79 | `LBNCDR.UPD.RESERVED.7` | `LbncdrCustExtUpd_Reserved7` | TField |  |  |
| 80 | `LBNCDR.UPD.RESERVED.8` | `LbncdrCustExtUpd_Reserved8` | TField |  |  |
