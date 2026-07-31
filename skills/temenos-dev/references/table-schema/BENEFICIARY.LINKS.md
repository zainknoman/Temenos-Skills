# BENEFICIARY.LINKS — Table Schema

> Source: `INSERTS/I_F.BENEFICIARY.LINKS` in `BY_Payments.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BEN.LNK.USED.IN` | `BeneficiaryLinks_UsedIn` | TField |  | The id of the contract where the Beneficiary record is used Maximum value of size 60 will be allowed. |
| 2 | `BEN.LNK.LINKED.APPLICATION` | `BeneficiaryLinks_LinkedApplication` | TField |  | This Field Will indicate the T24 application of the linked contract Maximum value of size 35 will be allowed. |
| 3 | `BEN.LNK.REASON` | `BeneficiaryLinks_Reason` | TField |  | This will be a text which will indicate in which contract is the Beneficiary used Maximum value of size 99 will be allowed. |
| 4 | `BEN.LNK.COUNTER.TYPE` | `BeneficiaryLinks_CounterType` | TField |  | Indicates whether the beneficiary is linked to an arrangement contract as counter party or not |
| 5 | `BEN.LNK.RESERVED.04` | `BeneficiaryLinks_Reserved04` | TField |  |  |
| 6 | `BEN.LNK.RESERVED.03` | `BeneficiaryLinks_Reserved03` | TField |  |  |
| 7 | `BEN.LNK.RESERVED.02` | `BeneficiaryLinks_Reserved02` | TField |  |  |
| 8 | `BEN.LNK.RESERVED.01` | `BeneficiaryLinks_Reserved01` | TField |  |  |
