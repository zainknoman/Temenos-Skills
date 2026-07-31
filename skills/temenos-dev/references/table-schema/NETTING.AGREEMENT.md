# NETTING.AGREEMENT — Table Schema

> Source: `INSERTS/I_F.NETTING.AGREEMENT` in `AC_PaymentNetting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NP.AG.AGREEMENT.NO` | `NettingAgreement_AgreementNo` | TField | Yes | The netting agreement number given by the customer. Validation Rules: 3-16 Alpha numeric characters. Mandatory input |
| 2 | `NP.AG.START.DATE` | `NettingAgreement_StartDate` | TField | Yes | Indicates the start date applicable to this agreement. Validation Rules: Date to be entered in the standard date format. Mandatory input |
| 3 | `NP.AG.END.DATE` | `NettingAgreement_EndDate` | TField |  | Indicates the final date covered by this netting agreement. Any contracts value after this date will NOT be eligible for netting under this agreement. Any contracts from START.DATE to END.DATE will default to Y in the NETTING.STATUS field on the transaction. Leaving this field blank indicates that the agreement is open ended. Validation Rules: Enter date in standard date format. |
| 4 | `NP.AG.EXCLUDED.CCY` | `NettingAgreement_ExcludedCcy` |  |  |  |
| 5 | `NP.AG.RESERVED.10` | `NettingAgreement_Reserved10` | TField |  |  |
| 6 | `NP.AG.INCLUDED.CCY` | `NettingAgreement_IncludedCcy` |  |  |  |
| 7 | `NP.AG.AGREED.CUSTS` | `NettingAgreement_AgreedCusts` |  |  |  |
| 8 | `NP.AG.SETTLEMENT.CCY` | `NettingAgreement_SettlementCcy` |  |  |  |
| 9 | `NP.AG.SETTLEMENT.AMT` | `NettingAgreement_SettlementAmt` |  |  |  |
| 10 | `NP.AG.OPERATION.CODE` | `NettingAgreement_OperationCode` | TField |  | This field identifies the type of operation. If this field is null then the agreement is valid for both CREDIT and CHQB. This field is inputable if the Netting Agreement Id has message type 102. Validation Rules: Up to 12 type AMT (Standard Amount Format) characters plus a decimal point. It is associated to SETTLEMENT.CCY field. This field is allowed only when currency is given. |
| 11 | `NP.AG.AGREED.ACCTS` | `NettingAgreement_AgreedAccts` |  |  |  |
| 12 | `NP.AG.RESERVED.5` | `NettingAgreement_Reserved5` | TField |  | Reserved for future use. |
| 13 | `NP.AG.RESERVED.4` | `NettingAgreement_Reserved4` | TField |  | Reserved for future use. |
| 14 | `NP.AG.RESERVED.3` | `NettingAgreement_Reserved3` | TField |  | Reserved for future use. |
| 15 | `NP.AG.RESERVED.2` | `NettingAgreement_Reserved2` | TField |  | Reserved for future use. |
| 16 | `NP.AG.RESERVED.1` | `NettingAgreement_Reserved1` | TField |  | Reserved for future use. |
| 17 | `NP.AG.LOCAL.REF` | `NettingAgreement_LocalRef` |  |  |  |
| 18 | `NP.AG.OVERRIDE` | `NettingAgreement_Override` |  |  |  |
| 19 | `NP.AG.RECORD.STATUS` | `NettingAgreement_RecordStatus` | String |  |  |
| 20 | `NP.AG.CURR.NO` | `NettingAgreement_CurrNo` | String |  |  |
| 21 | `NP.AG.INPUTTER` | `NettingAgreement_Inputter` |  |  |  |
| 22 | `NP.AG.DATE.TIME` | `NettingAgreement_DateTime` |  |  |  |
| 23 | `NP.AG.AUTHORISER` | `NettingAgreement_Authoriser` | String |  |  |
| 24 | `NP.AG.CO.CODE` | `NettingAgreement_CoCode` | String |  |  |
| 25 | `NP.AG.DEPT.CODE` | `NettingAgreement_DeptCode` | String |  |  |
| 26 | `NP.AG.AUDITOR.CODE` | `NettingAgreement_AuditorCode` | String |  |  |
| 27 | `NP.AG.AUDIT.DATE.TIME` | `NettingAgreement_AuditDateTime` | String |  |  |
