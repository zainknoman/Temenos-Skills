# CAPL.L.ENCRYPTION.DETAILS — Table Schema

> Source: `INSERTS/I_F.CAPL.L.ENCRYPTION.DETAILS` in `CABASE_ATMFoundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ENC.DET.MSG.AUTH.KEY` | `CaplLEncryptionDetails_MsgAuthKey` | TField |  | Message Authentication Key |
| 2 | `ENC.DET.CHECK.DIGITS` | `CaplLEncryptionDetails_CheckDigits` | TField |  | Check Digit for MAK |
| 3 | `ENC.DET.KEY.IN.USE` | `CaplLEncryptionDetails_KeyInUse` | TField |  | Key In Use |
| 4 | `ENC.DET.DATE.TIME` | `CaplLEncryptionDetails_DateTime` |  |  |  |
| 5 | `ENC.DET.LAST.AUTH.KEY` | `CaplLEncryptionDetails_LastAuthKey` |  |  |  |
| 6 | `ENC.DET.LAST.CHECK.DIGITS` | `CaplLEncryptionDetails_LastCheckDigits` |  |  |  |
| 7 | `ENC.DET.LAST.KEY.IN.USE` | `CaplLEncryptionDetails_LastKeyInUse` |  |  |  |
| 8 | `ENC.DET.LAST.DATE.TIME` | `CaplLEncryptionDetails_LastDateTime` |  |  |  |
| 9 | `ENC.DET.RESERVED.5` | `CaplLEncryptionDetails_Reserved5` |  |  |  |
| 10 | `ENC.DET.RESERVED.6` | `CaplLEncryptionDetails_Reserved6` |  |  |  |
| 11 | `ENC.DET.RESERVED.7` | `CaplLEncryptionDetails_Reserved7` |  |  |  |
| 12 | `ENC.DET.RESERVED.8` | `CaplLEncryptionDetails_Reserved8` |  |  |  |
| 13 | `ENC.DET.RESERVED.9` | `CaplLEncryptionDetails_Reserved9` |  |  |  |
| 14 | `ENC.DET.RESERVED.10` | `CaplLEncryptionDetails_Reserved10` |  |  |  |
