# SC.FACILITY.APPLN — Table Schema

> Source: `INSERTS/I_F.SC.FACILITY.APPLN` in `SC_ScvValuationUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.FAA.CUSTOMER.ID` | `ScFacilityAppln_CustomerId` | TField |  |  |
| 2 | `SC.FAA.PORTFOLIO.ID` | `ScFacilityAppln_PortfolioId` | TField |  |  |
| 3 | `SC.FAA.FACILITY.PRODUCT` | `ScFacilityAppln_FacilityProduct` | TField |  |  |
| 4 | `SC.FAA.OPENING.DATE` | `ScFacilityAppln_OpeningDate` | TField |  |  |
| 5 | `SC.FAA.CLOSING.DATE` | `ScFacilityAppln_ClosingDate` | TField |  |  |
| 6 | `SC.FAA.REVIEW.DATE` | `ScFacilityAppln_ReviewDate` | TField |  |  |
| 7 | `SC.FAA.APPLICATION.NO` | `ScFacilityAppln_ApplicationNo` | TField |  |  |
| 8 | `SC.FAA.REQUESTED.CCY` | `ScFacilityAppln_RequestedCcy` | TField |  |  |
| 9 | `SC.FAA.REQUESTED.AMT` | `ScFacilityAppln_RequestedAmt` | TField |  |  |
| 10 | `SC.FAA.FACILITY.QUESTION` | `ScFacilityAppln_FacilityQuestion` |  |  |  |
| 11 | `SC.FAA.RESPONSE` | `ScFacilityAppln_Response` |  |  |  |
| 12 | `SC.FAA.DOCUMENT.TYPE` | `ScFacilityAppln_DocumentType` |  |  |  |
| 13 | `SC.FAA.DOCUMENT.DESCRIPTION` | `ScFacilityAppln_DocumentDescription` |  |  |  |
| 14 | `SC.FAA.DATE.RECEIVED` | `ScFacilityAppln_DateReceived` |  |  |  |
| 15 | `SC.FAA.EXPIRY.DATE` | `ScFacilityAppln_ExpiryDate` |  |  |  |
| 16 | `SC.FAA.COLLATERAL.TYPE` | `ScFacilityAppln_CollateralType` | TField |  |  |
| 17 | `SC.FAA.COLLATERAL.CODE` | `ScFacilityAppln_CollateralCode` | TField |  |  |
| 18 | `SC.FAA.COLLATERAL.PROVIDED` | `ScFacilityAppln_CollateralProvided` |  |  |  |
| 19 | `SC.FAA.PLEDGED.QUANTITY` | `ScFacilityAppln_PledgedQuantity` |  |  |  |
| 20 | `SC.FAA.DEPOSITORY` | `ScFacilityAppln_Depository` |  |  |  |
| 21 | `SC.FAA.RESERVED.07` | `ScFacilityAppln_Reserved07` |  |  |  |
| 22 | `SC.FAA.PERCENTAGE` | `ScFacilityAppln_Percentage` |  |  |  |
| 23 | `SC.FAA.COLLATERAL.ID` | `ScFacilityAppln_CollateralId` | TField |  |  |
| 24 | `SC.FAA.APPLICATION.STAGE` | `ScFacilityAppln_ApplicationStage` | TField |  |  |
| 25 | `SC.FAA.FACILITY.SANCTIONED` | `ScFacilityAppln_FacilitySanctioned` | TField |  |  |
| 26 | `SC.FAA.SANCTIONED.AMOUNT` | `ScFacilityAppln_SanctionedAmount` | TField |  |  |
| 27 | `SC.FAA.LIMIT.REFERENCE` | `ScFacilityAppln_LimitReference` | TField |  |  |
| 28 | `SC.FAA.LOAN.STATUS` | `ScFacilityAppln_LoanStatus` | TField |  |  |
| 29 | `SC.FAA.LIMIT.ID` | `ScFacilityAppln_LimitId` | TField |  |  |
| 30 | `SC.FAA.COLLATERAL.RIGHT.ID` | `ScFacilityAppln_CollateralRightId` | TField |  |  |
| 31 | `SC.FAA.LOAN.ID` | `ScFacilityAppln_LoanId` | TField |  |  |
| 32 | `SC.FAA.RESERVED.02` | `ScFacilityAppln_Reserved02` | TField |  |  |
| 33 | `SC.FAA.RESERVED.01` | `ScFacilityAppln_Reserved01` | TField |  |  |
| 34 | `SC.FAA.LOCAL.REF` | `ScFacilityAppln_LocalRef` |  |  |  |
| 35 | `SC.FAA.OVERRIDE` | `ScFacilityAppln_Override` |  |  |  |
| 36 | `SC.FAA.RECORD.STATUS` | `ScFacilityAppln_RecordStatus` | String |  |  |
| 37 | `SC.FAA.CURR.NO` | `ScFacilityAppln_CurrNo` | String |  |  |
| 38 | `SC.FAA.INPUTTER` | `ScFacilityAppln_Inputter` |  |  |  |
| 39 | `SC.FAA.DATE.TIME` | `ScFacilityAppln_DateTime` |  |  |  |
| 40 | `SC.FAA.AUTHORISER` | `ScFacilityAppln_Authoriser` | String |  |  |
| 41 | `SC.FAA.CO.CODE` | `ScFacilityAppln_CoCode` | String |  |  |
| 42 | `SC.FAA.DEPT.CODE` | `ScFacilityAppln_DeptCode` | String |  |  |
| 43 | `SC.FAA.AUDITOR.CODE` | `ScFacilityAppln_AuditorCode` | String |  |  |
| 44 | `SC.FAA.AUDIT.DATE.TIME` | `ScFacilityAppln_AuditDateTime` | String |  |  |
