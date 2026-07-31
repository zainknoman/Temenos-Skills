# INLEND.IMPEXP.FILE.TRANSMIT.DTLS — Table Schema

> Source: `INSERTS/I_F.INLEND.IMPEXP.FILE.TRANSMIT.DTLS` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.IMPEXP.FT.TRANSMITTED.DATE.TIME` | `InlendImpexpFileTransmitDtls_TransmittedDateTime` |  |  |  |
| 2 | `INLEND.IMPEXP.FT.ERROR.DATE.TIME` | `InlendImpexpFileTransmitDtls_ErrorDateTime` |  |  |  |
| 3 | `INLEND.IMPEXP.FT.FILE.STATUS` | `InlendImpexpFileTransmitDtls_FileStatus` |  |  |  |
| 4 | `INLEND.IMPEXP.FT.FILE.SEQUENCE` | `InlendImpexpFileTransmitDtls_FileSequence` |  |  |  |
| 5 | `INLEND.IMPEXP.FT.RESERVED.4` | `InlendImpexpFileTransmitDtls_Reserved4` | TField |  |  |
| 6 | `INLEND.IMPEXP.FT.RESERVED.3` | `InlendImpexpFileTransmitDtls_Reserved3` | TField |  |  |
| 7 | `INLEND.IMPEXP.FT.RESERVED.2` | `InlendImpexpFileTransmitDtls_Reserved2` | TField |  |  |
| 8 | `INLEND.IMPEXP.FT.RESERVED.1` | `InlendImpexpFileTransmitDtls_Reserved1` | TField |  |  |
