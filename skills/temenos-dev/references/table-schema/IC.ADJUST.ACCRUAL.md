# IC.ADJUST.ACCRUAL — Table Schema

> Source: `INSERTS/I_F.IC.ADJUST.ACCRUAL` in `IC_OtherInterest.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IC.ADJ.DR.ADJ.AMOUNT` | `IcAdjustAccrual_DrAdjAmount` | TField | No | Optional input, the debit 1 interest adjustment amount. |
| 2 | `IC.ADJ.DR2.ADJ.AMOUNT` | `IcAdjustAccrual_Dr2AdjAmount` | TField | No | Optional input, the credit 2 interest adjustment amount. |
| 3 | `IC.ADJ.CR.ADJ.AMOUNT` | `IcAdjustAccrual_CrAdjAmount` | TField | No | Optional input, the credit 1 interest adjustment amount. |
| 4 | `IC.ADJ.CR2.ADJ.AMOUNT` | `IcAdjustAccrual_Cr2AdjAmount` | TField | No | Optional input, the credit 2 interest adjustment amount. |
| 5 | `IC.ADJ.RESERVED.10` | `IcAdjustAccrual_Reserved10` | TField |  |  |
| 6 | `IC.ADJ.RESERVED.9` | `IcAdjustAccrual_Reserved9` | TField |  |  |
| 7 | `IC.ADJ.RESERVED.8` | `IcAdjustAccrual_Reserved8` | TField |  |  |
| 8 | `IC.ADJ.RESERVED.7` | `IcAdjustAccrual_Reserved7` | TField |  |  |
| 9 | `IC.ADJ.RESERVED.6` | `IcAdjustAccrual_Reserved6` | TField |  |  |
| 10 | `IC.ADJ.RESERVED.5` | `IcAdjustAccrual_Reserved5` | TField |  |  |
| 11 | `IC.ADJ.RESERVED.4` | `IcAdjustAccrual_Reserved4` | TField |  |  |
| 12 | `IC.ADJ.RESERVED.3` | `IcAdjustAccrual_Reserved3` | TField |  |  |
| 13 | `IC.ADJ.RESERVED.2` | `IcAdjustAccrual_Reserved2` | TField |  |  |
| 14 | `IC.ADJ.RESERVED.1` | `IcAdjustAccrual_Reserved1` | TField |  |  |
| 15 | `IC.ADJ.LOCAL.REF` | `IcAdjustAccrual_LocalRef` |  |  |  |
| 16 | `IC.ADJ.STMT.NOS` | `IcAdjustAccrual_StmtNos` |  |  |  |
| 17 | `IC.ADJ.OVERRIDE` | `IcAdjustAccrual_Override` |  |  |  |
| 18 | `IC.ADJ.RECORD.STATUS` | `IcAdjustAccrual_RecordStatus` | String |  |  |
| 19 | `IC.ADJ.CURR.NO` | `IcAdjustAccrual_CurrNo` | String |  |  |
| 20 | `IC.ADJ.INPUTTER` | `IcAdjustAccrual_Inputter` |  |  |  |
| 21 | `IC.ADJ.DATE.TIME` | `IcAdjustAccrual_DateTime` |  |  |  |
| 22 | `IC.ADJ.AUTHORISER` | `IcAdjustAccrual_Authoriser` | String |  |  |
| 23 | `IC.ADJ.CO.CODE` | `IcAdjustAccrual_CoCode` | String |  |  |
| 24 | `IC.ADJ.DEPT.CODE` | `IcAdjustAccrual_DeptCode` | String |  |  |
| 25 | `IC.ADJ.AUDITOR.CODE` | `IcAdjustAccrual_AuditorCode` | String |  |  |
| 26 | `IC.ADJ.AUDIT.DATE.TIME` | `IcAdjustAccrual_AuditDateTime` | String |  |  |
