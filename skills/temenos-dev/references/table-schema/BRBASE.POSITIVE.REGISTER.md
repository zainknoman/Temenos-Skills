# BRBASE.POSITIVE.REGISTER — Table Schema

> Source: `INSERTS/I_F.BRBASE.POSITIVE.REGISTER` in `BRBASE_PositiveRegister.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BRBASE.POSREG.CUSTOMER.NO` | `BrbasePositiveRegister_CustomerNo` | TField |  | Customer number. |
| 2 | `BRBASE.POSREG.FILE.GEN.DATE` | `BrbasePositiveRegister_FileGenDate` | TField |  | File generation date. |
| 3 | `BRBASE.POSREG.ATTRIBUTE.NAME` | `BrbasePositiveRegister_AttributeName` |  |  |  |
| 4 | `BRBASE.POSREG.ATTRIBUTE.VALUE` | `BrbasePositiveRegister_AttributeValue` |  |  |  |
| 5 | `BRBASE.POSREG.LOCAL.REF` | `BrbasePositiveRegister_LocalRef` |  |  |  |
| 6 | `BRBASE.POSREG.RESERVED.5` | `BrbasePositiveRegister_Reserved5` | TField |  | Reserved for Future use. |
| 7 | `BRBASE.POSREG.RESERVED.4` | `BrbasePositiveRegister_Reserved4` | TField |  | Reserved for Future use. |
| 8 | `BRBASE.POSREG.RESERVED.3` | `BrbasePositiveRegister_Reserved3` | TField |  | Reserved for Future use. |
| 9 | `BRBASE.POSREG.RESERVED.2` | `BrbasePositiveRegister_Reserved2` | TField |  | Reserved for Future use. |
| 10 | `BRBASE.POSREG.RESERVED.1` | `BrbasePositiveRegister_Reserved1` | TField |  | Reserved for Future use. |
