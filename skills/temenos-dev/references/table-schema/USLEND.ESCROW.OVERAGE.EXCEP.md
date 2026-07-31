# USLEND.ESCROW.OVERAGE.EXCEP — Table Schema

> Source: `INSERTS/I_F.USLEND.ESCROW.OVERAGE.EXCEP` in `USLEND_EscrowProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USLEND.OVERAGE.ACCOUNT.ID` | `UslendEscrowOverageExcep_AccountId` | TField |  | Not Used |
| 2 | `USLEND.OVERAGE.POSTING.RESTRICT` | `UslendEscrowOverageExcep_PostingRestrict` | TField |  | Not Used |
| 3 | `USLEND.OVERAGE.SURPLUS.AMOUNT` | `UslendEscrowOverageExcep_SurplusAmount` | TField |  | Not Used |
| 4 | `USLEND.OVERAGE.RESERVED.10` | `UslendEscrowOverageExcep_Reserved10` | TField |  |  |
| 5 | `USLEND.OVERAGE.RESERVED.9` | `UslendEscrowOverageExcep_Reserved9` | TField |  |  |
| 6 | `USLEND.OVERAGE.RESERVED.8` | `UslendEscrowOverageExcep_Reserved8` | TField |  |  |
| 7 | `USLEND.OVERAGE.RESERVED.7` | `UslendEscrowOverageExcep_Reserved7` | TField |  |  |
| 8 | `USLEND.OVERAGE.RESERVED.6` | `UslendEscrowOverageExcep_Reserved6` | TField |  |  |
| 9 | `USLEND.OVERAGE.RESERVED.5` | `UslendEscrowOverageExcep_Reserved5` | TField |  |  |
| 10 | `USLEND.OVERAGE.RESERVED.4` | `UslendEscrowOverageExcep_Reserved4` | TField |  |  |
| 11 | `USLEND.OVERAGE.RESERVED.3` | `UslendEscrowOverageExcep_Reserved3` | TField |  |  |
| 12 | `USLEND.OVERAGE.RESERVED.2` | `UslendEscrowOverageExcep_Reserved2` | TField |  |  |
| 13 | `USLEND.OVERAGE.RESERVED.1` | `UslendEscrowOverageExcep_Reserved1` | TField |  |  |
| 14 | `USLEND.OVERAGE.LOCAL.REF` | `UslendEscrowOverageExcep_LocalRef` |  |  |  |
