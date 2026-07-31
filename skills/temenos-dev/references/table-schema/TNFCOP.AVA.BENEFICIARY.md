# TNFCOP.AVA.BENEFICIARY — Table Schema

> Source: `INSERTS/I_F.TNFCOP.AVA.BENEFICIARY` in `TNFCOP_AVA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNFCOP.AVA.BENEFICIARY.ROLE.CODE` | `TnfcopAvaBeneficiary_RoleCode` | TField |  | Role of AVA beneficiary |
| 2 | `TNFCOP.AVA.BENEFICIARY.ADDITION.DATE` | `TnfcopAvaBeneficiary_AdditionDate` | TField |  | Date of beneficiary addition to AVA |
| 3 | `TNFCOP.AVA.BENEFICIARY.REMOVE.BENEF` | `TnfcopAvaBeneficiary_RemoveBenef` | TField |  | Removal of beneficiary from AVA |
| 4 | `TNFCOP.AVA.BENEFICIARY.REMOVAL.DATE` | `TnfcopAvaBeneficiary_RemovalDate` | TField |  | Date of beneficiary removal |
| 5 | `TNFCOP.AVA.BENEFICIARY.LOCAL.REF` | `TnfcopAvaBeneficiary_LocalRef` |  |  |  |
| 6 | `TNFCOP.AVA.BENEFICIARY.RESERVED.10` | `TnfcopAvaBeneficiary_Reserved10` | TField |  | Reserved field for future use |
| 7 | `TNFCOP.AVA.BENEFICIARY.RESERVED.9` | `TnfcopAvaBeneficiary_Reserved9` | TField |  | Reserved field for future use |
| 8 | `TNFCOP.AVA.BENEFICIARY.RESERVED.8` | `TnfcopAvaBeneficiary_Reserved8` | TField |  | Reserved field for future use |
| 9 | `TNFCOP.AVA.BENEFICIARY.RESERVED.7` | `TnfcopAvaBeneficiary_Reserved7` | TField |  | Reserved field for future use |
| 10 | `TNFCOP.AVA.BENEFICIARY.RESERVED.6` | `TnfcopAvaBeneficiary_Reserved6` | TField |  | Reserved field for future use |
| 11 | `TNFCOP.AVA.BENEFICIARY.RESERVED.5` | `TnfcopAvaBeneficiary_Reserved5` | TField |  | Reserved field for future use |
| 12 | `TNFCOP.AVA.BENEFICIARY.RESERVED.4` | `TnfcopAvaBeneficiary_Reserved4` | TField |  | Reserved field for future use |
| 13 | `TNFCOP.AVA.BENEFICIARY.RESERVED.3` | `TnfcopAvaBeneficiary_Reserved3` | TField |  | Reserved field for future use |
| 14 | `TNFCOP.AVA.BENEFICIARY.RESERVED.2` | `TnfcopAvaBeneficiary_Reserved2` | TField |  | Reserved field for future use |
| 15 | `TNFCOP.AVA.BENEFICIARY.RESERVED.1` | `TnfcopAvaBeneficiary_Reserved1` | TField |  | Reserved field for future use |
| 16 | `TNFCOP.AVA.BENEFICIARY.OVERRIDE` | `TnfcopAvaBeneficiary_Override` |  |  |  |
| 17 | `TNFCOP.AVA.BENEFICIARY.RECORD.STATUS` | `TnfcopAvaBeneficiary_RecordStatus` | String |  |  |
| 18 | `TNFCOP.AVA.BENEFICIARY.CURR.NO` | `TnfcopAvaBeneficiary_CurrNo` | String |  |  |
| 19 | `TNFCOP.AVA.BENEFICIARY.INPUTTER` | `TnfcopAvaBeneficiary_Inputter` |  |  |  |
| 20 | `TNFCOP.AVA.BENEFICIARY.DATE.TIME` | `TnfcopAvaBeneficiary_DateTime` |  |  |  |
| 21 | `TNFCOP.AVA.BENEFICIARY.AUTHORISER` | `TnfcopAvaBeneficiary_Authoriser` | String |  |  |
| 22 | `TNFCOP.AVA.BENEFICIARY.CO.CODE` | `TnfcopAvaBeneficiary_CoCode` | String |  |  |
| 23 | `TNFCOP.AVA.BENEFICIARY.DEPT.CODE` | `TnfcopAvaBeneficiary_DeptCode` | String |  |  |
| 24 | `TNFCOP.AVA.BENEFICIARY.AUDITOR.CODE` | `TnfcopAvaBeneficiary_AuditorCode` | String |  |  |
| 25 | `TNFCOP.AVA.BENEFICIARY.AUDIT.DATE.TIME` | `TnfcopAvaBeneficiary_AuditDateTime` | String |  |  |
