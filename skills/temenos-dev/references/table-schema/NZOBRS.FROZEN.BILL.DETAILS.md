# NZOBRS.FROZEN.BILL.DETAILS — Table Schema

> Source: `INSERTS/I_F.NZOBRS.FROZEN.BILL.DETAILS` in `NZOBRS_OpenBankResolution.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FR.BILL.FROZEN.FUNDS.BILL.NO` | `NzobrsFrozenBillDetails_FrozenFundsBillNo` | TField |  | Frozen Funds Bill Number created and adjusted during the OBR process. |
| 2 | `FR.BILL.ORG.FROZEN.FUNDS.AMT` | `NzobrsFrozenBillDetails_OrgFrozenFundsAmt` | TField |  | Original Frozen Funds Amount or the Original Balance for which the Frozen Funds Bill was created. |
