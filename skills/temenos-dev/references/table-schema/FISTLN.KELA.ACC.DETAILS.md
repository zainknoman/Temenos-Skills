# FISTLN.KELA.ACC.DETAILS — Table Schema

> Source: `INSERTS/I_F.FISTLN.KELA.ACC.DETAILS` in `FISTLN_StudentLoan.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `KELA.ACC.DETAILS.FIRST.CAP.DATE` | `FistlnKelaAccDetails_FirstCapDate` | TField |  | The Date on which the first capitalization happens for the account |
| 2 | `KELA.ACC.DETAILS.KELA.COUNTER` | `FistlnKelaAccDetails_KelaCounter` | TField |  | The number of consecutive time KELA did not give confirmation. |
| 3 | `KELA.ACC.DETAILS.FIRST.REPAYMENT.DATE` | `FistlnKelaAccDetails_FirstRepaymentDate` | TField |  | The date on which the repayment starts for an arrangement |
| 4 | `KELA.ACC.DETAILS.RESERVED.8` | `FistlnKelaAccDetails_Reserved8` | TField |  |  |
| 5 | `KELA.ACC.DETAILS.RESERVED.7` | `FistlnKelaAccDetails_Reserved7` | TField |  |  |
| 6 | `KELA.ACC.DETAILS.RESERVED.6` | `FistlnKelaAccDetails_Reserved6` | TField |  |  |
| 7 | `KELA.ACC.DETAILS.RESERVED.5` | `FistlnKelaAccDetails_Reserved5` | TField |  |  |
| 8 | `KELA.ACC.DETAILS.RESERVED.4` | `FistlnKelaAccDetails_Reserved4` | TField |  |  |
| 9 | `KELA.ACC.DETAILS.RESERVED.3` | `FistlnKelaAccDetails_Reserved3` | TField |  |  |
| 10 | `KELA.ACC.DETAILS.RESERVED.2` | `FistlnKelaAccDetails_Reserved2` | TField |  |  |
| 11 | `KELA.ACC.DETAILS.RESERVED.1` | `FistlnKelaAccDetails_Reserved1` | TField |  |  |
| 12 | `KELA.ACC.DETAILS.LOCAL.REF` | `FistlnKelaAccDetails_LocalRef` |  |  |  |
