# BENEFICIARY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.BENEFICIARY.PARAMETER` in `BY_Payments.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BEN.PAR.VALIDATE.BENEFICIARY.LINKS` | `BeneficiaryParameter_ValidateBeneficiaryLinks` | TField |  | Indicates whether system should maintain BENEFICIARY.LINKS Beneficiary link file is data between the BENEFICIARY and the contract where the BENEFICIARY is linked. So that reversal of BENEFICIARY will raise override when its linked to a contract. Allowed Options - YES or NO YES - Indicates system will maintain link between contracts and BENEFICIARY. Once the field is defined with YES, the option cannot be modified to NO/NULL. NO/NULL - Indicates system will not maintain link between contracts and BENEFICIARY. |
| 2 | `BEN.PAR.UPDATE.ACCT.BLOCK.CLOSURE` | `BeneficiaryParameter_UpdateAcctBlockClosure` | TField |  | Indicates if the Account Block Closure file should be updated when the account is referred in a BENEFICIARY So that closure of account will raise override when it is linked to any BENEFICIARY Allowed Options - YES or NO YES - Indicates system will udpate Account block closure when an account is linked to BENEFICIARY. Once the field is defined with YES, the option cannot be modified to NO/NULL. NO/NULL - Indicates system will not update Account block closure when an account is linked to BENEFICIARY. |
| 3 | `BEN.PAR.INTERNAL.BEN.PURGE.DAYS` | `BeneficiaryParameter_InternalBenPurgeDays` | TField |  | INTERNAL.BEN.PURGE.DAYS field is added to hold the purge days period in working days After which beneficiary must be purged if not linked to any contract. Allowed only when UPDATE.BENEFICIARY.LINKS is enabled Allowed values - 4 Numeric values from 1 to 9999 |
| 4 | `BEN.PAR.RESERVED09` | `BeneficiaryParameter_Reserved09` |  |  |  |
| 5 | `BEN.PAR.RESERVED08` | `BeneficiaryParameter_Reserved08` | TField |  |  |
| 6 | `BEN.PAR.RESERVED07` | `BeneficiaryParameter_Reserved07` | TField |  |  |
| 7 | `BEN.PAR.RESERVED06` | `BeneficiaryParameter_Reserved06` | TField |  |  |
| 8 | `BEN.PAR.RESERVED05` | `BeneficiaryParameter_Reserved05` | TField |  |  |
| 9 | `BEN.PAR.RESERVED04` | `BeneficiaryParameter_Reserved04` | TField |  |  |
| 10 | `BEN.PAR.RESERVED03` | `BeneficiaryParameter_Reserved03` | TField |  |  |
| 11 | `BEN.PAR.RESERVED02` | `BeneficiaryParameter_Reserved02` | TField |  |  |
| 12 | `BEN.PAR.RESERVED01` | `BeneficiaryParameter_Reserved01` | TField |  |  |
| 13 | `BEN.PAR.LOCAL.REF` | `BeneficiaryParameter_LocalRef` |  |  |  |
| 14 | `BEN.PAR.OVERRIDE` | `BeneficiaryParameter_Override` |  |  |  |
| 15 | `BEN.PAR.RECORD.STATUS` | `BeneficiaryParameter_RecordStatus` | String |  |  |
| 16 | `BEN.PAR.CURR.NO` | `BeneficiaryParameter_CurrNo` | String |  |  |
| 17 | `BEN.PAR.INPUTTER` | `BeneficiaryParameter_Inputter` |  |  |  |
| 18 | `BEN.PAR.DATE.TIME` | `BeneficiaryParameter_DateTime` |  |  |  |
| 19 | `BEN.PAR.AUTHORISER` | `BeneficiaryParameter_Authoriser` | String |  |  |
| 20 | `BEN.PAR.CO.CODE` | `BeneficiaryParameter_CoCode` | String |  |  |
| 21 | `BEN.PAR.DEPT.CODE` | `BeneficiaryParameter_DeptCode` | String |  |  |
| 22 | `BEN.PAR.AUDITOR.CODE` | `BeneficiaryParameter_AuditorCode` | String |  |  |
| 23 | `BEN.PAR.AUDIT.DATE.TIME` | `BeneficiaryParameter_AuditDateTime` | String |  |  |
