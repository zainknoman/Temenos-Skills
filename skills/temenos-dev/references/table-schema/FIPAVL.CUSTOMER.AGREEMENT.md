# FIPAVL.CUSTOMER.AGREEMENT — Table Schema

> Source: `INSERTS/I_F.FIPAVL.CUSTOMER.AGREEMENT` in `FIPAVL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FIPAVL.CUSTOMER.AGREEMENT.CUSTOMER.AGREEMENT.EXISTS` | `FipavlCustomerAgreement_CustomerAgreementExists` | TField |  | Yes/No field. Indicates if Customer agreement exists or not |
| 2 | `FIPAVL.CUSTOMER.AGREEMENT.RESERVED.10` | `FipavlCustomerAgreement_Reserved10` | TField |  |  |
| 3 | `FIPAVL.CUSTOMER.AGREEMENT.RESERVED.9` | `FipavlCustomerAgreement_Reserved9` | TField |  |  |
| 4 | `FIPAVL.CUSTOMER.AGREEMENT.RESERVED.8` | `FipavlCustomerAgreement_Reserved8` | TField |  |  |
| 5 | `FIPAVL.CUSTOMER.AGREEMENT.RESERVED.7` | `FipavlCustomerAgreement_Reserved7` | TField |  |  |
| 6 | `FIPAVL.CUSTOMER.AGREEMENT.RESERVED.6` | `FipavlCustomerAgreement_Reserved6` | TField |  |  |
| 7 | `FIPAVL.CUSTOMER.AGREEMENT.RESERVED.5` | `FipavlCustomerAgreement_Reserved5` | TField |  |  |
| 8 | `FIPAVL.CUSTOMER.AGREEMENT.RESERVED.4` | `FipavlCustomerAgreement_Reserved4` | TField |  |  |
| 9 | `FIPAVL.CUSTOMER.AGREEMENT.RESERVED.3` | `FipavlCustomerAgreement_Reserved3` | TField |  |  |
| 10 | `FIPAVL.CUSTOMER.AGREEMENT.RESERVED.2` | `FipavlCustomerAgreement_Reserved2` | TField |  |  |
| 11 | `FIPAVL.CUSTOMER.AGREEMENT.RESERVED.1` | `FipavlCustomerAgreement_Reserved1` | TField |  |  |
| 12 | `FIPAVL.CUSTOMER.AGREEMENT.LOCAL.REF` | `FipavlCustomerAgreement_LocalRef` |  |  |  |
| 13 | `FIPAVL.CUSTOMER.AGREEMENT.OVERRIDE` | `FipavlCustomerAgreement_Override` |  |  |  |
| 14 | `FIPAVL.CUSTOMER.AGREEMENT.RECORD.STATUS` | `FipavlCustomerAgreement_RecordStatus` | String |  |  |
| 15 | `FIPAVL.CUSTOMER.AGREEMENT.CURR.NO` | `FipavlCustomerAgreement_CurrNo` | String |  |  |
| 16 | `FIPAVL.CUSTOMER.AGREEMENT.INPUTTER` | `FipavlCustomerAgreement_Inputter` |  |  |  |
| 17 | `FIPAVL.CUSTOMER.AGREEMENT.DATE.TIME` | `FipavlCustomerAgreement_DateTime` |  |  |  |
| 18 | `FIPAVL.CUSTOMER.AGREEMENT.AUTHORISER` | `FipavlCustomerAgreement_Authoriser` | String |  |  |
| 19 | `FIPAVL.CUSTOMER.AGREEMENT.CO.CODE` | `FipavlCustomerAgreement_CoCode` | String |  |  |
| 20 | `FIPAVL.CUSTOMER.AGREEMENT.DEPT.CODE` | `FipavlCustomerAgreement_DeptCode` | String |  |  |
| 21 | `FIPAVL.CUSTOMER.AGREEMENT.AUDITOR.CODE` | `FipavlCustomerAgreement_AuditorCode` | String |  |  |
| 22 | `FIPAVL.CUSTOMER.AGREEMENT.AUDIT.DATE.TIME` | `FipavlCustomerAgreement_AuditDateTime` | String |  |  |
