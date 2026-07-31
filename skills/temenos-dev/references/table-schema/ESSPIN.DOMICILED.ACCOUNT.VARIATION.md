# ESSPIN.DOMICILED.ACCOUNT.VARIATION — Table Schema

> Source: `INSERTS/I_F.ESSPIN.DOMICILED.ACCOUNT.VARIATION` in `ESSPIN_TgssDomiciledPayments.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESSPIN.DOMI.FORWARD.ACCOUNT` | `EsspinDomiciledAccountVariation_ForwardAccount` | TField |  | The IBAN of the account |
| 2 | `ESSPIN.DOMI.SUFFIX` | `EsspinDomiciledAccountVariation_Suffix` | TField |  | This field use to bulk the transactions |
| 3 | `ESSPIN.DOMI.REQUEST.STATUS` | `EsspinDomiciledAccountVariation_RequestStatus` | TField |  |  |
| 4 | `ESSPIN.DOMI.LOCAL.REF` | `EsspinDomiciledAccountVariation_LocalRef` |  |  |  |
