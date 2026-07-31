# ESCROW.ACH.FT.CAPTURE — Table Schema

> Source: `INSERTS/I_F.ESCROW.ACH.FT.CAPTURE` in `USLEND_EscrowProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FT.CAP.TRANS.DATE` | `EscrowAchFtCapture_TransDate` | TField |  | Not Used |
| 2 | `FT.CAP.TRANS.STATUS` | `EscrowAchFtCapture_TransStatus` | TField |  | Not Used |
| 3 | `FT.CAP.DEBIT.ACCT` | `EscrowAchFtCapture_DebitAcct` | TField |  | Not Used |
| 4 | `FT.CAP.CREDIT.ACCT` | `EscrowAchFtCapture_CreditAcct` | TField |  | Not Used |
| 5 | `FT.CAP.ERROR.MSG` | `EscrowAchFtCapture_ErrorMsg` | TField |  | Not Used |
| 6 | `FT.CAP.RESERVED.10` | `EscrowAchFtCapture_Reserved10` | TField |  |  |
| 7 | `FT.CAP.RESERVED.9` | `EscrowAchFtCapture_Reserved9` | TField |  |  |
| 8 | `FT.CAP.RESERVED.8` | `EscrowAchFtCapture_Reserved8` | TField |  |  |
| 9 | `FT.CAP.RESERVED.7` | `EscrowAchFtCapture_Reserved7` | TField |  |  |
| 10 | `FT.CAP.RESERVED.6` | `EscrowAchFtCapture_Reserved6` | TField |  |  |
| 11 | `FT.CAP.RESERVED.5` | `EscrowAchFtCapture_Reserved5` | TField |  |  |
| 12 | `FT.CAP.RESERVED.4` | `EscrowAchFtCapture_Reserved4` | TField |  |  |
| 13 | `FT.CAP.RESERVED.3` | `EscrowAchFtCapture_Reserved3` | TField |  |  |
| 14 | `FT.CAP.RESERVED.2` | `EscrowAchFtCapture_Reserved2` | TField |  |  |
| 15 | `FT.CAP.RESERVED.1` | `EscrowAchFtCapture_Reserved1` | TField |  |  |
