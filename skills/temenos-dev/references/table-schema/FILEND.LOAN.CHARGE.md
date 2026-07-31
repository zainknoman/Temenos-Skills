# FILEND.LOAN.CHARGE — Table Schema

> Source: `INSERTS/I_F.FILEND.LOAN.CHARGE` in `FILEND_LegalFeeCap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LOAN.CHRG.ANNIVERSARY.DATE` | `FilendLoanCharge_AnniversaryDate` |  |  |  |
| 2 | `LOAN.CHRG.CHARGEABLE.LOAN.AMOUNT` | `FilendLoanCharge_ChargeableLoanAmount` |  |  |  |
| 3 | `LOAN.CHRG.DISBURSED.DATE` | `FilendLoanCharge_DisbursedDate` |  |  |  |
| 4 | `LOAN.CHRG.MAX.LOAN.CHARGE` | `FilendLoanCharge_MaxLoanCharge` |  |  |  |
| 5 | `LOAN.CHRG.MAX.LOAN.DAY.CHARGE` | `FilendLoanCharge_MaxLoanDayCharge` |  |  |  |
| 6 | `LOAN.CHRG.LOAN.COMMITMENT` | `FilendLoanCharge_LoanCommitment` |  |  |  |
| 7 | `LOAN.CHRG.LOCAL.REF` | `FilendLoanCharge_LocalRef` |  |  |  |
| 8 | `LOAN.CHRG.17B.ANNIVERSARY.START.DATE` | `FilendLoanCharge_17bAnniversaryStartDate` |  |  |  |
| 9 | `LOAN.CHRG.17B.ANNIVERSARY.END.DATE` | `FilendLoanCharge_17bAnniversaryEndDate` |  |  |  |
| 10 | `LOAN.CHRG.RESERVED.3` | `FilendLoanCharge_Reserved3` | TField |  | Reserved field for future use. |
| 11 | `LOAN.CHRG.RESERVED.2` | `FilendLoanCharge_Reserved2` | TField |  | Reserved field for future use. |
| 12 | `LOAN.CHRG.RESERVED.1` | `FilendLoanCharge_Reserved1` | TField |  | Reserved field for future use. |
| 13 | `LOAN.CHRG.TOPUP.DATE` | `FilendLoanCharge_TopupDate` |  |  |  |
| 14 | `LOAN.CHRG.ANNIVERSARY.START.DATE` | `FilendLoanCharge_AnniversaryStartDate` |  |  |  |
| 15 | `LOAN.CHRG.ANNIVERSARY.END.DATE` | `FilendLoanCharge_AnniversaryEndDate` |  |  |  |
