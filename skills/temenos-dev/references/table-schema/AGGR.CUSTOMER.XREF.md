# AGGR.CUSTOMER.XREF — Table Schema

> Source: `INSERTS/I_F.AGGR.CUSTOMER.XREF` in `LI_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AG.CUS.PARTY.ID` | `AggrCustomerXref_PartyId` | TField |  |  |
| 2 | `AG.CUS.CUSTOMER.GROUP` | `AggrCustomerXref_CustomerGroup` | TField |  |  |
| 3 | `AG.CUS.GROUP.PURPOSE` | `AggrCustomerXref_GroupPurpose` | TField |  |  |
| 4 | `AG.CUS.PRIMARY.PARTY` | `AggrCustomerXref_PrimaryParty` |  |  |  |
| 5 | `AG.CUS.AGGR.PARTY` | `AggrCustomerXref_AggrParty` |  |  |  |
