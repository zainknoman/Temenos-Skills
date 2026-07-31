# MD.GROUP.CONDITION — Table Schema

> Source: `INSERTS/I_F.MD.GROUP.CONDITION` in `MD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MD.GRP.DEAL.SUB.TYPE` | `MdGroupCondition_DealSubType` |  |  |  |
| 2 | `MD.GRP.CATEGORY` | `MdGroupCondition_Category` |  |  |  |
| 3 | `MD.GRP.PROV.PERCENT` | `MdGroupCondition_ProvPercent` |  |  |  |
| 4 | `MD.GRP.DEBIT.PROV.ACC` | `MdGroupCondition_DebitProvAcc` | TField |  | The default account to be used for debiting cash margin. Validation Rules: Input only if the ID is C-XXXXXX Cannot be the same as CREDIT.PROV.ACCOUNT. |
| 5 | `MD.GRP.CREDIT.PROV.ACC` | `MdGroupCondition_CreditProvAcc` | TField |  | The default account to be used for crediting cash margin. Validation Rules: Input only if the ID is C-XXXXXX Cannot be the same as DEBIT.PROV.ACCOUNT. |
| 6 | `MD.GRP.LOCAL.REF` | `MdGroupCondition_LocalRef` |  |  |  |
| 7 | `MD.GRP.IB.LIMIT` | `MdGroupCondition_IbLimit` | TField |  | Value in this field decides the stage at which the customer's limit must be updated when request for issuance of guarantee is initiated through Internet Banking. Allowed only for Internet enabled customers. Allowed values are "YES" or "NO". If "YES", the customer's limit will be checked and updated when the Corporate customer requests for issuance of guarantee through Internet Banking. If "NO", then the customer's limit will be checked and updated only when the request is approved at the Bank side. Value defined here will override the condition defined in MD.PARAMETER. |
| 8 | `MD.GRP.GTEE.CATEGORY` | `MdGroupCondition_GteeCategory` |  |  |  |
| 9 | `MD.GRP.CSN.PERC` | `MdGroupCondition_CsnPerc` |  |  |  |
| 10 | `MD.GRP.CSN.RATE` | `MdGroupCondition_CsnRate` |  |  |  |
| 11 | `MD.GRP.CSN.CCY` | `MdGroupCondition_CsnCcy` |  |  |  |
| 12 | `MD.GRP.CSN.AMT` | `MdGroupCondition_CsnAmt` |  |  |  |
| 13 | `MD.GRP.RESERVED.5` | `MdGroupCondition_Reserved5` |  |  |  |
| 14 | `MD.GRP.RESERVED.6` | `MdGroupCondition_Reserved6` |  |  |  |
| 15 | `MD.GRP.RESERVED.7` | `MdGroupCondition_Reserved7` |  |  |  |
| 16 | `MD.GRP.RESERVED.4` | `MdGroupCondition_Reserved4` | TField |  |  |
| 17 | `MD.GRP.RESERVED.3` | `MdGroupCondition_Reserved3` | TField |  |  |
| 18 | `MD.GRP.RESERVED.2` | `MdGroupCondition_Reserved2` | TField |  |  |
| 19 | `MD.GRP.RESERVED.1` | `MdGroupCondition_Reserved1` | TField |  |  |
| 20 | `MD.GRP.OVERRIDE` | `MdGroupCondition_Override` |  |  |  |
| 21 | `MD.GRP.RECORD.STATUS` | `MdGroupCondition_RecordStatus` | String |  |  |
| 22 | `MD.GRP.CURR.NO` | `MdGroupCondition_CurrNo` | String |  |  |
| 23 | `MD.GRP.INPUTTER` | `MdGroupCondition_Inputter` |  |  |  |
| 24 | `MD.GRP.DATE.TIME` | `MdGroupCondition_DateTime` |  |  |  |
| 25 | `MD.GRP.AUTHORISER` | `MdGroupCondition_Authoriser` | String |  |  |
| 26 | `MD.GRP.CO.CODE` | `MdGroupCondition_CoCode` | String |  |  |
| 27 | `MD.GRP.DEPT.CODE` | `MdGroupCondition_DeptCode` | String |  |  |
| 28 | `MD.GRP.AUDITOR.CODE` | `MdGroupCondition_AuditorCode` | String |  |  |
| 29 | `MD.GRP.AUDIT.DATE.TIME` | `MdGroupCondition_AuditDateTime` | String |  |  |
