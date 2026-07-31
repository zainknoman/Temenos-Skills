# AA.SETTLEMENT.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.SETTLEMENT.TYPE` in `AA_Settlement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ST.DESCRIPTION` | `AaSettlementType_Description` |  |  |  |
| 2 | `AA.ST.DEBIT.RULE` | `AaSettlementType_DebitRule` | TField |  | The field decides the manner in which system should utilize the funds available in PAYIN.ACCOUNT during settlement process. 1) FULL: System debits the PAYIN account to the extent of the bill amount irrespective of whether or not the funds are available in the specified account. For this purpose, system creates an overdraft in the PAYIN.ACCOUNT in case funds are only partially available provided the PAYIN.ACCOUNT has a limit attached to it. 2) PARTIAL: System debits the PAYIN.ACCOUNT only to the extent of funds available. 3) NONE: System would not debit the PAYIN.ACCOUNT if funds are not fully available to settle the bill. Validation Rules 1. For Payout "DEBIT.RULE" must always be NULL 2. For Payin "DEBIT.RULE" should not be NULL |
| 3 | `AA.ST.USER.RULE.ROUTINE` | `AaSettlementType_UserRuleRoutine` |  |  |  |
| 4 | `AA.ST.RESERVED.10` | `AaSettlementType_Reserved10` | TField |  |  |
| 5 | `AA.ST.RESERVED.9` | `AaSettlementType_Reserved9` | TField |  |  |
| 6 | `AA.ST.RESERVED.8` | `AaSettlementType_Reserved8` | TField |  |  |
| 7 | `AA.ST.RESERVED.7` | `AaSettlementType_Reserved7` | TField |  |  |
| 8 | `AA.ST.RESERVED.6` | `AaSettlementType_Reserved6` | TField |  |  |
| 9 | `AA.ST.RESERVED.5` | `AaSettlementType_Reserved5` | TField |  |  |
| 10 | `AA.ST.RESERVED.4` | `AaSettlementType_Reserved4` | TField |  |  |
| 11 | `AA.ST.RESERVED.3` | `AaSettlementType_Reserved3` | TField |  |  |
| 12 | `AA.ST.RESERVED.2` | `AaSettlementType_Reserved2` | TField |  |  |
| 13 | `AA.ST.RESERVED.1` | `AaSettlementType_Reserved1` | TField |  |  |
| 14 | `AA.ST.LOCAL.REF` | `AaSettlementType_LocalRef` |  |  |  |
| 15 | `AA.ST.OVERRIDE` | `AaSettlementType_Override` |  |  |  |
| 16 | `AA.ST.RECORD.STATUS` | `AaSettlementType_RecordStatus` | String |  |  |
| 17 | `AA.ST.CURR.NO` | `AaSettlementType_CurrNo` | String |  |  |
| 18 | `AA.ST.INPUTTER` | `AaSettlementType_Inputter` |  |  |  |
| 19 | `AA.ST.DATE.TIME` | `AaSettlementType_DateTime` |  |  |  |
| 20 | `AA.ST.AUTHORISER` | `AaSettlementType_Authoriser` | String |  |  |
| 21 | `AA.ST.CO.CODE` | `AaSettlementType_CoCode` | String |  |  |
| 22 | `AA.ST.DEPT.CODE` | `AaSettlementType_DeptCode` | String |  |  |
| 23 | `AA.ST.AUDITOR.CODE` | `AaSettlementType_AuditorCode` | String |  |  |
| 24 | `AA.ST.AUDIT.DATE.TIME` | `AaSettlementType_AuditDateTime` | String |  |  |
