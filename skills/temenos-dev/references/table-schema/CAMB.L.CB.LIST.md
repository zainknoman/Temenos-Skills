# CAMB.L.CB.LIST — Table Schema

> Source: `INSERTS/I_F.CAMB.L.CB.LIST` in `CACBRT_CreditBureau.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.CB.EXTRACT.DT` | `CambLCbList_ExtractDt` | TField |  | The purpose of this table is used to store the Equifax extract date. This will be store once the request is placed to Equifax and response is received.Valid DATE record is stored. |
| 2 | `CAPL.CB.SIN` | `CambLCbList_Sin` | TField |  | Field stores the SIN number of the customer.Valid Sin number to be stored here |
| 3 | `CAPL.CB.FILE.PATH` | `CambLCbList_FilePath` | TField |  | This field is used to define the path where the field will be stored once the response is received from Equifax.Valid path to be stored here. |
| 4 | `CAPL.CB.FILE.NAME` | `CambLCbList_FileName` | TField |  | The purpose of this field is used to store the file name of the extract received from Equifax.Valid field name to be store here. |
