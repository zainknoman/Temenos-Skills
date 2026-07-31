# EB.MANDATE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.EB.MANDATE.PARAMETER` in `EB_Mandate.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.MAND.PAR.DESCRIPTION` | `EbMandateParameter_Description` |  |  |  |
| 2 | `EB.MAND.PAR.AMOUNT.FIELD` | `EbMandateParameter_AmountField` |  |  |  |
| 3 | `EB.MAND.PAR.AMOUNT.CURRENCY` | `EbMandateParameter_AmountCurrency` |  |  |  |
| 4 | `EB.MAND.PAR.VALUE.DATE` | `EbMandateParameter_ValueDate` |  |  |  |
| 5 | `EB.MAND.PAR.MANDATE.FIELD` | `EbMandateParameter_MandateField` |  |  |  |
| 6 | `EB.MAND.PAR.APPL.FIELD.NAME` | `EbMandateParameter_ApplFieldName` |  |  |  |
| 7 | `EB.MAND.PAR.EXTRACT.VALUE` | `EbMandateParameter_ExtractValue` |  |  |  |
| 8 | `EB.MAND.PAR.MANDATE.RULE.GATEWAY` | `EbMandateParameter_MandateRuleGateway` | TField |  | Reserved for future use |
| 9 | `EB.MAND.PAR.MANDATE.RULE.API` | `EbMandateParameter_MandateRuleApi` | TField |  | Reserved for future use |
| 10 | `EB.MAND.PAR.RAISE.ALERT` | `EbMandateParameter_RaiseAlert` | TField |  | Indicates if alerts should be raised to pending Signatories using Business events. Validation Rules: Defaulted to YES, if required can be set to NO |
| 11 | `EB.MAND.PAR.PROTECTION.LIMIT.CHECK` | `EbMandateParameter_ProtectionLimitCheck` | TField |  | Indicates if application requires protection limit check. Validation Rules: Input allowed only when AMOUNT.FIELD exists. If it set to YES means enables the protection limit check process. System defaults it to NO. |
| 12 | `EB.MAND.PAR.MANDATE.PROC.OPTION` | `EbMandateParameter_MandateProcOption` | TField | Yes | The mandate processing refers this setup to decide which applications will be checked to determine the mandate requirements that apply to the transactions being processed. Mandatory for the SYSTEM record. Allowed Options APPLICATION : This allows the mandate requirements to be processed based on definition in ACCOUNT and CUSTOMER record. Portfolio level mandate processing will not be supported in this mode CENRTALISED - This allows the mandate requirements to be processed based on MANDATE.REQUIREMENTS definition. System will not support Mandate definitons in ACCOUNT and CUSTOMER records. MIXED - This allows mandate definitions to co-exist between MANDATE.REQUIREMENTS, ACCOUNT and CUSTOMER tables and mandate processing will first check the CENRTALISED setup, if no setup is found system will proceed to check the respective ACCOUNT or CUSTOMER definitions. |
| 13 | `EB.MAND.PAR.RESERVED.2` | `EbMandateParameter_Reserved2` |  |  |  |
| 14 | `EB.MAND.PAR.RESERVED.1` | `EbMandateParameter_Reserved1` |  |  |  |
| 15 | `EB.MAND.PAR.LOCAL.REF` | `EbMandateParameter_LocalRef` |  |  |  |
| 16 | `EB.MAND.PAR.OVERRIDE` | `EbMandateParameter_Override` |  |  |  |
| 17 | `EB.MAND.PAR.RECORD.STATUS` | `EbMandateParameter_RecordStatus` | String |  |  |
| 18 | `EB.MAND.PAR.CURR.NO` | `EbMandateParameter_CurrNo` | String |  |  |
| 19 | `EB.MAND.PAR.INPUTTER` | `EbMandateParameter_Inputter` |  |  |  |
| 20 | `EB.MAND.PAR.DATE.TIME` | `EbMandateParameter_DateTime` |  |  |  |
| 21 | `EB.MAND.PAR.AUTHORISER` | `EbMandateParameter_Authoriser` | String |  |  |
| 22 | `EB.MAND.PAR.CO.CODE` | `EbMandateParameter_CoCode` | String |  |  |
| 23 | `EB.MAND.PAR.DEPT.CODE` | `EbMandateParameter_DeptCode` | String |  |  |
| 24 | `EB.MAND.PAR.AUDITOR.CODE` | `EbMandateParameter_AuditorCode` | String |  |  |
| 25 | `EB.MAND.PAR.AUDIT.DATE.TIME` | `EbMandateParameter_AuditDateTime` | String |  |  |
