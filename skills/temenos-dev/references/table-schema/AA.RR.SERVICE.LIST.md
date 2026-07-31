# AA.RR.SERVICE.LIST — Table Schema

> Source: `INSERTS/I_F.AA.RR.SERVICE.LIST` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.RRS..PROCESS.DATE` | `AaRrServiceList_ProcessDate` | TField |  | Effective date of back dated activity which has happened but��R&amp;R still pending to be done. |
| 2 | `AA.RRS..MASTER.AAA` | `AaRrServiceList_MasterAaa` | TField |  | AAA reference of back dated activity which has happened but��R&amp;R still pending to be done. |
