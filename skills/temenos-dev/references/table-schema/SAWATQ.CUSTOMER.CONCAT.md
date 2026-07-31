# SAWATQ.CUSTOMER.CONCAT — Table Schema

> Source: `INSERTS/I_F.SAWATQ.CUSTOMER.CONCAT` in `SAWATQ_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CUS.CON.LEGAL.DOC.NAME` | `SawatqCustomerConcat_LegalDocName` | TField |  | This indicates the Legal Document Name of the Customer or Person/Entity of the corresponding LEGAL.ID |
| 2 | `CUS.CON.APPLICATION` | `SawatqCustomerConcat_Application` | TField |  | This indicates the Application from which the Customer or Person/Entity is taken |
| 3 | `CUS.CON.CUSTOMER.ID` | `SawatqCustomerConcat_CustomerId` | TField |  | This indicates the Customer Number |
| 4 | `CUS.CON.RESERVED.2` | `SawatqCustomerConcat_Reserved2` | TField |  | Reserved For Future Use |
| 5 | `CUS.CON.RESERVED.3` | `SawatqCustomerConcat_Reserved3` | TField |  | Reserved For Future Use |
| 6 | `CUS.CON.RESERVED.4` | `SawatqCustomerConcat_Reserved4` | TField |  | Reserved For Future Use |
| 7 | `CUS.CON.RESERVED.5` | `SawatqCustomerConcat_Reserved5` | TField |  | Reserved For Future Use |
