# EB.MANDATE.REQUIREMENTS — Table Schema

> Source: `INSERTS/I_F.EB.MANDATE.REQUIREMENTS` in `EB_Mandate.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.MDR.APPLICATION.LEVEL` | `EbMandateRequirements_ApplicationLevel` | TField | Yes | Indicates standard T24 Transact entity for which the mandate requirement is captured. Validation Rules: Mandatory field. Allowed options are ACCOUNT, CUSTOMER and PORTFOLIO |
| 2 | `EB.MDR.APPLICATION.ID` | `EbMandateRequirements_ApplicationId` | TField | Yes | Identifies the customer/account for which the requirement is captured. Validation Rules: Mandatory. Must be a valid id in the application implied by the requirement application level - CUSTOMER or ACCOUNT or SEC.ACC.MASTER. |
| 3 | `EB.MDR.APPLICATION.GROUP` | `EbMandateRequirements_ApplicationGroup` |  |  |  |
| 4 | `EB.MDR.MANDATE.ID` | `EbMandateRequirements_MandateId` |  |  |  |
| 5 | `EB.MDR.DEFAULT.MANDATE.ID` | `EbMandateRequirements_DefaultMandateId` | TField | Yes | Defines the default mandate which will be used when a transaction is triggered through an application for which the mandate processing is defined in EB.MANDATE.PARAMETER but is not covered by any of the Mandate Application Group specified in the mandate requirement. Validation Rules: Should be a valid id of a record in EB.MANDATE. If no value is provided in Mandate Id field, this field is mandatory. |
| 6 | `EB.MDR.LOCAL.REF` | `EbMandateRequirements_LocalRef` |  |  |  |
| 7 | `EB.MDR.OVERRIDE` | `EbMandateRequirements_Override` |  |  |  |
| 8 | `EB.MDR.RECORD.STATUS` | `EbMandateRequirements_RecordStatus` | String |  |  |
| 9 | `EB.MDR.CURR.NO` | `EbMandateRequirements_CurrNo` | String |  |  |
| 10 | `EB.MDR.INPUTTER` | `EbMandateRequirements_Inputter` |  |  |  |
| 11 | `EB.MDR.DATE.TIME` | `EbMandateRequirements_DateTime` |  |  |  |
| 12 | `EB.MDR.AUTHORISER` | `EbMandateRequirements_Authoriser` | String |  |  |
| 13 | `EB.MDR.CO.CODE` | `EbMandateRequirements_CoCode` | String |  |  |
| 14 | `EB.MDR.DEPT.CODE` | `EbMandateRequirements_DeptCode` | String |  |  |
| 15 | `EB.MDR.AUDITOR.CODE` | `EbMandateRequirements_AuditorCode` | String |  |  |
| 16 | `EB.MDR.AUDIT.DATE.TIME` | `EbMandateRequirements_AuditDateTime` | String |  |  |
