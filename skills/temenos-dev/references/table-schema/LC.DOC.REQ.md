# LC.DOC.REQ — Table Schema

> Source: `INSERTS/I_F.LC.DOC.REQ` in `LC_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LC.DOC.REQ.DOCUMENT.CODE` | `LcDocReq_DocumentCode` |  |  |  |
| 2 | `LC.DOC.REQ.DOCUMENT.TXT` | `LcDocReq_DocumentTxt` |  |  |  |
| 3 | `LC.DOC.REQ.AMEND.STATUS` | `LcDocReq_AmendStatus` |  |  |  |
| 4 | `LC.DOC.REQ.AMEND.DATE` | `LcDocReq_AmendDate` |  |  |  |
| 5 | `LC.DOC.REQ.UPDATE.NO` | `LcDocReq_UpdateNo` |  |  |  |
