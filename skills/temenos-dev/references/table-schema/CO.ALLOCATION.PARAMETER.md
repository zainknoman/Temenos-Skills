# CO.ALLOCATION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CO.ALLOCATION.PARAMETER` in `CO_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CO.AL.PAR.COVER.LIABILITY` | `CoAllocationParameter_CoverLiability` | TField |  | Field to define the Giving Priority. Based on this setup Limits covered by a collateral right will be sorted during collateral allocation. Validation Rules: 1 - Own liabilities are covered first and allocations are sorted in ascending order. 2 - Own liabilities are covered first and allocations are sorted in descending order. null |
| 2 | `CO.AL.PAR.USE.COLLATERAL` | `CoAllocationParameter_UseCollateral` | TField |  | Receiving priority order, Based on this setup collateral rights used to cover a liability will be sorted and utilised based on the sorted order. Validation Rules: 1 - Own liabilities are covered first and allocations are sorted in ascending order. 2 - Own liabilities are covered first and allocations are sorted in descending order. null |
| 3 | `CO.AL.PAR.PRIORITY.RECEIVE` | `CoAllocationParameter_PriorityReceive` | TField |  | This field is used to specify the order by which collateral should be sorted. Validation Rules: 1 � ASSET TYPE - COLLATERAL.RIGHT received will be sorted by Asset first. When more than one asset of same type from different customers, then it will be further sorted by Customer key. The sorting can be set to sort largest to smallest or vice versa. 2 � CUSTOMER - COLLATERAL.RIGHT received will be sorted by Customer first. When there are multiple Assets for the same customer then they will be further sorted by Asset. The sorting can be set to sort largest to smallest or vice versa. Null � ASSET.TYPE will be considered as default while processing. |
| 4 | `CO.AL.PAR.ASSET.ORDER` | `CoAllocationParameter_AssetOrder` |  |  |  |
| 5 | `CO.AL.PAR.RESERVED.10` | `CoAllocationParameter_Reserved10` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 6 | `CO.AL.PAR.RESERVED.9` | `CoAllocationParameter_Reserved9` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 7 | `CO.AL.PAR.RESERVED.8` | `CoAllocationParameter_Reserved8` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 8 | `CO.AL.PAR.RESERVED.7` | `CoAllocationParameter_Reserved7` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 9 | `CO.AL.PAR.RESERVED.6` | `CoAllocationParameter_Reserved6` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 10 | `CO.AL.PAR.RESERVED.5` | `CoAllocationParameter_Reserved5` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 11 | `CO.AL.PAR.RESERVED.4` | `CoAllocationParameter_Reserved4` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 12 | `CO.AL.PAR.RESERVED.3` | `CoAllocationParameter_Reserved3` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 13 | `CO.AL.PAR.RESERVED.2` | `CoAllocationParameter_Reserved2` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 14 | `CO.AL.PAR.RESERVED.1` | `CoAllocationParameter_Reserved1` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 15 | `CO.AL.PAR.LOCAL.REF` | `CoAllocationParameter_LocalRef` |  |  |  |
| 16 | `CO.AL.PAR.RECORD.STATUS` | `CoAllocationParameter_RecordStatus` | String |  |  |
| 17 | `CO.AL.PAR.CURR.NO` | `CoAllocationParameter_CurrNo` | String |  |  |
| 18 | `CO.AL.PAR.INPUTTER` | `CoAllocationParameter_Inputter` |  |  |  |
| 19 | `CO.AL.PAR.DATE.TIME` | `CoAllocationParameter_DateTime` |  |  |  |
| 20 | `CO.AL.PAR.AUTHORISER` | `CoAllocationParameter_Authoriser` | String |  |  |
| 21 | `CO.AL.PAR.CO.CODE` | `CoAllocationParameter_CoCode` | String |  |  |
| 22 | `CO.AL.PAR.DEPT.CODE` | `CoAllocationParameter_DeptCode` | String |  |  |
| 23 | `CO.AL.PAR.AUDITOR.CODE` | `CoAllocationParameter_AuditorCode` | String |  |  |
| 24 | `CO.AL.PAR.AUDIT.DATE.TIME` | `CoAllocationParameter_AuditDateTime` | String |  |  |
