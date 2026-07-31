# STATIC.CHANGE.TODAY — Table Schema

> Source: `INSERTS/I_F.STATIC.CHANGE.TODAY` in `RE_Consolidation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RE.SCT.SYSTEM.ID` | `StaticChangeToday_SystemId` |  |  |  |
| 2 | `RE.SCT.OLD.CONSOL.KEY` | `StaticChangeToday_OldConsolKey` |  |  |  |
| 3 | `RE.SCT.NEW.CONSOL.KEY` | `StaticChangeToday_NewConsolKey` |  |  |  |
| 4 | `RE.SCT.OLD.TYPE` | `StaticChangeToday_OldType` |  |  |  |
| 5 | `RE.SCT.NEW.TYPE` | `StaticChangeToday_NewType` |  |  |  |
| 6 | `RE.SCT.OLD.DATE` | `StaticChangeToday_OldDate` |  |  |  |
| 7 | `RE.SCT.NEW.DATE` | `StaticChangeToday_NewDate` |  |  |  |
| 8 | `RE.SCT.TXN.REF` | `StaticChangeToday_TxnRef` |  |  |  |
| 9 | `RE.SCT.PRODUCT` | `StaticChangeToday_Product` |  |  |  |
| 10 | `RE.SCT.CUSTOMER` | `StaticChangeToday_Customer` |  |  |  |
| 11 | `RE.SCT.CURRENCY` | `StaticChangeToday_Currency` |  |  |  |
| 12 | `RE.SCT.CURRENCY.MARKET` | `StaticChangeToday_CurrencyMarket` |  |  |  |
| 13 | `RE.SCT.INTEREST.RATE` | `StaticChangeToday_InterestRate` |  |  |  |
| 14 | `RE.SCT.INTEREST.KEY` | `StaticChangeToday_InterestKey` |  |  |  |
| 15 | `RE.SCT.INTEREST.BASIS` | `StaticChangeToday_InterestBasis` |  |  |  |
| 16 | `RE.SCT.CRF.TXN.CODE` | `StaticChangeToday_CrfTxnCode` |  |  |  |
| 17 | `RE.SCT.OLD.PRODCAT` | `StaticChangeToday_OldProdcat` |  |  |  |
| 18 | `RE.SCT.NEW.PRODCAT` | `StaticChangeToday_NewProdcat` |  |  |  |
| 19 | `RE.SCT.CONTRACT.VALUE.DATE` | `StaticChangeToday_ContractValueDate` | TField |  | Description: It will be populated from application while updating this file to trigger generic static changes processing and this field value will later be updated in EB.CONTRACT.BALANCES. Validation rules: � No input field -Updated by system |
| 20 | `RE.SCT.CONTRACT.ACCT.OFFICER` | `StaticChangeToday_ContractAccofficer` |  |  |  |
| 21 | `RE.SCT.CONTRACT.DEPT.CODE` | `StaticChangeToday_ContractDeptCode` |  |  |  |
