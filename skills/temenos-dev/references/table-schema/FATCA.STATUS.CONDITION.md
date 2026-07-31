# FATCA.STATUS.CONDITION — Table Schema

> Source: `INSERTS/I_F.FATCA.STATUS.CONDITION` in `FA_CustomerIdentification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FA.FC.DECISION.FIELD` | `FatcaStatusCondition_DecisionField` |  |  |  |
| 2 | `FA.FC.DECISION` | `FatcaStatusCondition_Decision` |  |  |  |
| 3 | `FA.FC.DECISION.VALUE` | `FatcaStatusCondition_DecisionValue` |  |  |  |
| 4 | `FA.FC.LEVEL` | `FatcaStatusCondition_Level` |  |  |  |
| 5 | `FA.FC.OPERAND` | `FatcaStatusCondition_Operand` |  |  |  |
| 6 | `FA.FC.EXISTING.NEW` | `FatcaStatusCondition_ExistingNew` | TField |  | The field is used to indicate whether the conditions above areapplicable only to new clients or existing clients or both. This will be determined by referring to the CUSTOMER SINCE field in CUSTOMER. If the date is on or after 1st July2013, the relationship will be considered new else (even if the field is blank), the relationship will beconsidered existing. If the condition, for example, is specified only for New, the conditions specified here willnot apply for Existing accounts. When this field value is not updated, it will be considered as BOTH, it will be applicable to both New andExisting accounts. Validation Rules: NEW or EXISTING or BOTH |
| 7 | `FA.FC.KYC.CHECK` | `FatcaStatusCondition_KycCheck` | TField |  | If this field is set to YES, only clients with KYC checks completed (KYC.CHECK field inFATCA.CUSTOMER.SUPPLEMENTARY.INFO record set to YES), will be considered to have complied with this rule. If thisfield is left blank, then the value of KYC check field will not be considered for status classification. Validation rules The allowed values are YES or NO |
| 8 | `FA.FC.ENTITY.STATUS` | `FatcaStatusCondition_EntityStatus` | TField |  | This field accepts a valid FATCA.TAX.STATUS record identifier. If a value is defined in this field, then duringthe account classification determination process, the system will check for a positive match with the value definedin ENTITY.STATUS field of the corresponding FATCA.CUSTOMER.SUPPLEMENTARY.INFO record. Validation rules A valid FATCA TAX STATUS ID |
| 9 | `FA.FC.CHECK.JO.BO.STATUS` | `FatcaStatusCondition_CheckJoBoStatus` | TField |  | If this field is set to YES, then the owner status will also be considered in evaluating the accountclassification. Owners with role type JOINT / BENEFICIAL / SUBSTANTIAL will only be considered for evaluation. If the field is blank then it will not be considered for status classification. Validation rules Allowed values 'YES', BLANK |
| 10 | `FA.FC.JO.BO.STATUS` | `FatcaStatusCondition_JoBoStatus` | TField | Yes | This field accepts one of the values defined in DEFLT.US.STATUS, DEFLT.NONUS.STATUS fields in FATCA.PARAMETER. If the JO.BO.STATUS value is defined with a value specified in DEFLT.US.STATUS field of FATCA.PARAMETER, then theaccount with even one US Joint or beneficial or Substantial owner will be considered as US account. If the JO.BO.STATUS value is defined with a value specified in DEFLT.NONUS.STATUS field of FATCA.PARAMETER, thenthe account with all non-us owners (Joint or beneficial or Substantial owner) will be considered as Non-US account. Validation Rules: Mandatory when CHECK.JO.BO.STATUS is set as YES Must be a valid value from the FATCA.TAX.STATUS application. |
| 11 | `FA.FC.NARRATIVE` | `FatcaStatusCondition_Narrative` | TField |  | The Narrative to be updated in the Status Narrative field in FATCA.CUSTOMER.SUPPLEMENTARY.INFO along with theAccount classification Validation rules 1-35 ANY characters |
| 12 | `FA.FC.INDICIA` | `FatcaStatusCondition_Indicia` | TField |  | If the FATCA.STATUS has to be automatically updated for clients with no indicia (say, NON.US.NO.INDICIA), thenthis field will have to be set as NULL and only the clients with no indicia (identified based on INDICIA STRENGTHin FATCA.CUSTOMER.SUPPLEMENTARY.INFO) will be considered as complying with the condition. This can be set only in conjunction with any of the documents in DECISION.FIELD and DECISION.VALUE above. Validation Rules: NULL is the only allowed value for this field. |
| 13 | `FA.FC.RESERVED.2` | `FatcaStatusCondition_Reserved2` | TField |  | This field is reserved for future use. |
| 14 | `FA.FC.RESERVED.1` | `FatcaStatusCondition_Reserved1` | TField |  | This field is reserved for future use. |
| 15 | `FA.FC.LOCAL.REF` | `FatcaStatusCondition_LocalRef` |  |  |  |
| 16 | `FA.FC.OVERRIDE` | `FatcaStatusCondition_Override` |  |  |  |
| 17 | `FA.FC.RECORD.STATUS` | `FatcaStatusCondition_RecordStatus` | String |  |  |
| 18 | `FA.FC.CURR.NO` | `FatcaStatusCondition_CurrNo` | String |  |  |
| 19 | `FA.FC.INPUTTER` | `FatcaStatusCondition_Inputter` |  |  |  |
| 20 | `FA.FC.DATE.TIME` | `FatcaStatusCondition_DateTime` |  |  |  |
| 21 | `FA.FC.AUTHORISER` | `FatcaStatusCondition_Authoriser` | String |  |  |
| 22 | `FA.FC.CO.CODE` | `FatcaStatusCondition_CoCode` | String |  |  |
| 23 | `FA.FC.DEPT.CODE` | `FatcaStatusCondition_DeptCode` | String |  |  |
| 24 | `FA.FC.AUDITOR.CODE` | `FatcaStatusCondition_AuditorCode` | String |  |  |
| 25 | `FA.FC.AUDIT.DATE.TIME` | `FatcaStatusCondition_AuditDateTime` | String |  |  |
| 26 | `FA.FC.DECISION.APP.FIELD` | `FatcaStatusCondition_DecisionAppField` |  |  |  |
