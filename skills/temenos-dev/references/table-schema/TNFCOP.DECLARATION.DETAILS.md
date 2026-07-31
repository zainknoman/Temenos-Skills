# TNFCOP.DECLARATION.DETAILS — Table Schema

> Source: `INSERTS/I_F.TNFCOP.DECLARATION.DETAILS` in `TNFCOP_Agency.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNFCOP.DEC.DECLARATION.DATE` | `TnfcopDeclarationDetails_DeclarationDate` | TField |  | Date on which the declaration is issued by customs.To be updated by user when the declaration is recorded. This is a no change field therefore once updated, the value cannot be changed |
| 2 | `TNFCOP.DEC.DECLARATION.EXPIRY.DATE` | `TnfcopDeclarationDetails_DeclarationExpiryDate` | TField |  | Date on which the declaration expires. Value in this field is auto populated based on the default maturity months defined in TNFCOP.AVA.LIMIT.PARAM.No input field. User will not be able to alter or update this field. |
| 3 | `TNFCOP.DEC.DECLARATION.CURRENCY` | `TnfcopDeclarationDetails_DeclarationCurrency` |  |  |  |
| 4 | `TNFCOP.DEC.DECLARATION.AMOUNT` | `TnfcopDeclarationDetails_DeclarationAmount` |  |  |  |
| 5 | `TNFCOP.DEC.CUSTOMER.ID` | `TnfcopDeclarationDetails_CustomerId` | TField |  | TRANSACT Customer id of the declaration owner. This field has to be updated when declaration owner is bank customer. No change field |
| 6 | `TNFCOP.DEC.FIRST.NAME` | `TnfcopDeclarationDetails_FirstName` | TField |  | First name of the declaration owner. This field is enabled only when CUSTOMER.ID is empty. This field has to be updated only for non-customers.No change field |
| 7 | `TNFCOP.DEC.LEGAL.ID.NAME` | `TnfcopDeclarationDetails_LegalIdName` | TField |  | Legal doc name provided by the customer. This field is enabled only when CUSTOMER.ID is empty. This field has to be updated only for non-customers.No change field |
| 8 | `TNFCOP.DEC.LEGAL.DOC.ID` | `TnfcopDeclarationDetails_LegalDocId` | TField |  | Id of the Legal doc provided by the non-customer. This field is enabled only when CUSTOMER.ID is empty. This field has to be updated only for non-customers.No change field |
| 9 | `TNFCOP.DEC.ADDRESS` | `TnfcopDeclarationDetails_Address` | TField |  | Address of the customer. This field is enabled only when CUSTOMER.ID is empty. This field has to be updated only for non-customers.No change field |
| 10 | `TNFCOP.DEC.RESIDENCE` | `TnfcopDeclarationDetails_Residence` | TField |  | Residence of the declaration owner. This field is enabled only when CUSTOMER.ID is empty. This field has to be updated only for non-customers.No change field |
| 11 | `TNFCOP.DEC.NATIONALITY` | `TnfcopDeclarationDetails_Nationality` | TField |  | Nationality of the declaration owner. This field is enabled only when CUSTOMER.ID is empty. This field has to be updated only for non-customers |
| 12 | `TNFCOP.DEC.STATUS` | `TnfcopDeclarationDetails_Status` | TField |  | This field will be used to indicate if the declaration is active or expired. This is a no input field |
| 13 | `TNFCOP.DEC.RESERVED.10` | `TnfcopDeclarationDetails_Reserved10` | TField |  | Field for future use |
| 14 | `TNFCOP.DEC.RESERVED.9` | `TnfcopDeclarationDetails_Reserved9` | TField |  | Field for future use |
| 15 | `TNFCOP.DEC.RESERVED.8` | `TnfcopDeclarationDetails_Reserved8` | TField |  | Field for future use |
| 16 | `TNFCOP.DEC.RESERVED.7` | `TnfcopDeclarationDetails_Reserved7` | TField |  | Field for future use |
| 17 | `TNFCOP.DEC.RESERVED.6` | `TnfcopDeclarationDetails_Reserved6` | TField |  | Field for future use |
| 18 | `TNFCOP.DEC.RESERVED.5` | `TnfcopDeclarationDetails_Reserved5` | TField |  | Field for future use |
| 19 | `TNFCOP.DEC.RESERVED.4` | `TnfcopDeclarationDetails_Reserved4` | TField |  | Field for future use |
| 20 | `TNFCOP.DEC.RESERVED.3` | `TnfcopDeclarationDetails_Reserved3` | TField |  | Field for future use |
| 21 | `TNFCOP.DEC.RESERVED.2` | `TnfcopDeclarationDetails_Reserved2` | TField |  | Field for future use |
| 22 | `TNFCOP.DEC.RESERVED.1` | `TnfcopDeclarationDetails_Reserved1` | TField |  | Field for future use |
| 23 | `TNFCOP.DEC.LOCAL.REF` | `TnfcopDeclarationDetails_LocalRef` |  |  |  |
| 24 | `TNFCOP.DEC.OVERRIDE` | `TnfcopDeclarationDetails_Override` |  |  |  |
| 25 | `TNFCOP.DEC.RECORD.STATUS` | `TnfcopDeclarationDetails_RecordStatus` | String |  |  |
| 26 | `TNFCOP.DEC.CURR.NO` | `TnfcopDeclarationDetails_CurrNo` | String |  |  |
| 27 | `TNFCOP.DEC.INPUTTER` | `TnfcopDeclarationDetails_Inputter` |  |  |  |
| 28 | `TNFCOP.DEC.DATE.TIME` | `TnfcopDeclarationDetails_DateTime` |  |  |  |
| 29 | `TNFCOP.DEC.AUTHORISER` | `TnfcopDeclarationDetails_Authoriser` | String |  |  |
| 30 | `TNFCOP.DEC.CO.CODE` | `TnfcopDeclarationDetails_CoCode` | String |  |  |
| 31 | `TNFCOP.DEC.DEPT.CODE` | `TnfcopDeclarationDetails_DeptCode` | String |  |  |
| 32 | `TNFCOP.DEC.AUDITOR.CODE` | `TnfcopDeclarationDetails_AuditorCode` | String |  |  |
| 33 | `TNFCOP.DEC.AUDIT.DATE.TIME` | `TnfcopDeclarationDetails_AuditDateTime` | String |  |  |
