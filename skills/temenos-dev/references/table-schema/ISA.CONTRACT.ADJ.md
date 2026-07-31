# ISA.CONTRACT.ADJ — Table Schema

> Source: `INSERTS/I_F.ISA.CONTRACT.ADJ` in `UKISA1_Reporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ISA.CON.ADJ.ISA.CONTRACT.ID` | `IsaContractAdj_IsaContractId` | TField |  | ID of ISA.CONTRACT which is to be amended |
| 2 | `ISA.CON.ADJ.DATE` | `IsaContractAdj_Date` | TField |  | Date on when the ISA.CONTRACT is amended. Defaulted to TODAY's date |
| 3 | `ISA.CON.ADJ.SUB.ADJUSTMENT` | `IsaContractAdj_SubAdjustment` | TField |  | Amount to be adjusted. This amount can be positive or negative |
| 4 | `ISA.CON.ADJ.FIRST.SUB.DATE` | `IsaContractAdj_FirstSubDate` | TField |  | Date of first subscription in ISA.CONTRACT can be amended |
| 5 | `ISA.CON.ADJ.RESERVED.10` | `IsaContractAdj_Reserved10` |  |  |  |
| 6 | `ISA.CON.ADJ.RESERVED.9` | `IsaContractAdj_Reserved9` | TField |  |  |
| 7 | `ISA.CON.ADJ.RESERVED.8` | `IsaContractAdj_Reserved8` | TField |  |  |
| 8 | `ISA.CON.ADJ.RESERVED.7` | `IsaContractAdj_Reserved7` | TField |  |  |
| 9 | `ISA.CON.ADJ.RESERVED.6` | `IsaContractAdj_Reserved6` | TField |  |  |
| 10 | `ISA.CON.ADJ.RESERVED.5` | `IsaContractAdj_Reserved5` | TField |  |  |
| 11 | `ISA.CON.ADJ.RESERVED.4` | `IsaContractAdj_Reserved4` | TField |  |  |
| 12 | `ISA.CON.ADJ.RESERVED.3` | `IsaContractAdj_Reserved3` | TField |  |  |
| 13 | `ISA.CON.ADJ.RESERVED.2` | `IsaContractAdj_Reserved2` | TField |  |  |
| 14 | `ISA.CON.ADJ.RESERVED.1` | `IsaContractAdj_Reserved1` | TField |  |  |
| 15 | `ISA.CON.ADJ.RECORD.STATUS` | `IsaContractAdj_RecordStatus` | String |  |  |
| 16 | `ISA.CON.ADJ.CURR.NO` | `IsaContractAdj_CurrNo` | String |  |  |
| 17 | `ISA.CON.ADJ.INPUTTER` | `IsaContractAdj_Inputter` |  |  |  |
| 18 | `ISA.CON.ADJ.DATE.TIME` | `IsaContractAdj_DateTime` |  |  |  |
| 19 | `ISA.CON.ADJ.AUTHORISER` | `IsaContractAdj_Authoriser` | String |  |  |
| 20 | `ISA.CON.ADJ.CO.CODE` | `IsaContractAdj_CoCode` | String |  |  |
| 21 | `ISA.CON.ADJ.DEPT.CODE` | `IsaContractAdj_DeptCode` | String |  |  |
| 22 | `ISA.CON.ADJ.AUDITOR.CODE` | `IsaContractAdj_AuditorCode` | String |  |  |
| 23 | `ISA.CON.ADJ.AUDIT.DATE.TIME` | `IsaContractAdj_AuditDateTime` | String |  |  |
