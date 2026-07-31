# ARPYMT.MANDATE.AMENDMENT.DETAILS — Table Schema

> Source: `INSERTS/I_F.ARPYMT.MANDATE.AMENDMENT.DETAILS` in `ARPYMT_MandateRegistration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARPYMT.MNDT.OLD.DD.DDI` | `ArpymtMandateAmendmentDetails_OldDdDdi` | TField |  | This DDI.ID will be the @id of previous record |
| 2 | `ARPYMT.MNDT.OLD.CREDITOR.ID` | `ArpymtMandateAmendmentDetails_OldCreditorId` | TField |  | Creditor Id brfore amendment |
| 3 | `ARPYMT.MNDT.EXPIRATION.DATE` | `ArpymtMandateAmendmentDetails_ExpirationDate` | TField |  | Stores the date of expiration based on SLA days |
| 4 | `ARPYMT.MNDT.STATUS` | `ArpymtMandateAmendmentDetails_Status` | TField |  | Status of the mandate record |
| 5 | `ARPYMT.MNDT.LOCAL.REF` | `ArpymtMandateAmendmentDetails_LocalRef` |  |  |  |
| 6 | `ARPYMT.MNDT.OVERRIDE` | `ArpymtMandateAmendmentDetails_Override` |  |  |  |
| 7 | `ARPYMT.MNDT.RECORD.STATUS` | `ArpymtMandateAmendmentDetails_RecordStatus` | String |  |  |
| 8 | `ARPYMT.MNDT.CURR.NO` | `ArpymtMandateAmendmentDetails_CurrNo` | String |  |  |
| 9 | `ARPYMT.MNDT.INPUTTER` | `ArpymtMandateAmendmentDetails_Inputter` |  |  |  |
| 10 | `ARPYMT.MNDT.DATE.TIME` | `ArpymtMandateAmendmentDetails_DateTime` |  |  |  |
| 11 | `ARPYMT.MNDT.AUTHORISER` | `ArpymtMandateAmendmentDetails_Authoriser` | String |  |  |
| 12 | `ARPYMT.MNDT.CO.CODE` | `ArpymtMandateAmendmentDetails_CoCode` | String |  |  |
| 13 | `ARPYMT.MNDT.DEPT.CODE` | `ArpymtMandateAmendmentDetails_DeptCode` | String |  |  |
| 14 | `ARPYMT.MNDT.AUDITOR.CODE` | `ArpymtMandateAmendmentDetails_AuditorCode` | String |  |  |
