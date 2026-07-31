# NACUST.CUSTOMER.DETAILS — Table Schema

> Source: `INSERTS/I_F.NACUST.CUSTOMER.DETAILS` in `NACUST_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CUS.DET.LAST.CUSTOMER.CONTACT` | `NacustCustomerDetails_LastCustomerContact` | TField |  | This field have the latest customer contact. |
| 2 | `CUS.DET.APPLICATION` | `NacustCustomerDetails_Application` |  |  |  |
| 3 | `CUS.DET.APPLICATION.ID` | `NacustCustomerDetails_ApplicationId` |  |  |  |
| 4 | `CUS.DET.INTERFACE.REF` | `NacustCustomerDetails_InterfaceRef` |  |  |  |
| 5 | `CUS.DET.CONTACT.DATE` | `NacustCustomerDetails_ContactDate` |  |  |  |
| 6 | `CUS.DET.RESERVED.15` | `NacustCustomerDetails_Reserved15` | TField |  |  |
| 7 | `CUS.DET.RESERVED.14` | `NacustCustomerDetails_Reserved14` | TField |  |  |
| 8 | `CUS.DET.RESERVED.13` | `NacustCustomerDetails_Reserved13` | TField |  |  |
| 9 | `CUS.DET.RESERVED.12` | `NacustCustomerDetails_Reserved12` | TField |  |  |
| 10 | `CUS.DET.RESERVED.11` | `NacustCustomerDetails_Reserved11` | TField |  |  |
| 11 | `CUS.DET.RESERVED.10` | `NacustCustomerDetails_Reserved10` | TField |  |  |
| 12 | `CUS.DET.RESERVED.9` | `NacustCustomerDetails_Reserved9` | TField |  |  |
| 13 | `CUS.DET.RESERVED.8` | `NacustCustomerDetails_Reserved8` | TField |  |  |
| 14 | `CUS.DET.RESERVED.7` | `NacustCustomerDetails_Reserved7` | TField |  |  |
| 15 | `CUS.DET.RESERVED.6` | `NacustCustomerDetails_Reserved6` | TField |  |  |
| 16 | `CUS.DET.RESERVED.5` | `NacustCustomerDetails_Reserved5` | TField |  |  |
| 17 | `CUS.DET.RESERVED.4` | `NacustCustomerDetails_Reserved4` | TField |  |  |
| 18 | `CUS.DET.RESERVED.3` | `NacustCustomerDetails_Reserved3` | TField |  |  |
| 19 | `CUS.DET.RESERVED.2` | `NacustCustomerDetails_Reserved2` | TField |  |  |
| 20 | `CUS.DET.RESERVED.1` | `NacustCustomerDetails_Reserved1` | TField |  |  |
