# ST.CUST.RELATIONSHIP.DATES — Table Schema

> Source: `INSERTS/I_F.ST.CUST.RELATIONSHIP.DATES` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REL.DAT.CR.DATE` | `StCustRelationshipDates_CrDate` | TField |  | Date part of the CUSTOMER.RELATIONSHIP record is stored First time when a new CR record is created, this would be updated Subsequently when new dated record of an existing CR id is created, the new dated would get appended in the ascending order of the date |
