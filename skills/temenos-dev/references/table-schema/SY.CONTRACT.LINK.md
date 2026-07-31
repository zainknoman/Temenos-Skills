# SY.CONTRACT.LINK — Table Schema

> Source: `INSERTS/I_F.SY.CONTRACT.LINK` in `SY_Trading.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.CL.UNDER.APPLICATION` | `SyContractLink_UnderApplication` | TField |  | The underlying application |
| 2 | `SY.CL.UNDER.ID` | `SyContractLink_UnderId` | TField |  | The ID of the record in the underlying application |
| 3 | `SY.CL.SY.PRD.ID` | `SyContractLink_SyPrdId` | TField |  | The SY.PRODUCT ID relating to thistransaction |
| 4 | `SY.CL.SY.TXN.ID` | `SyContractLink_SyTxnId` | TField |  | The SY.TRANSACTION table ID |
| 5 | `SY.CL.SY.UNIT.ID` | `SyContractLink_SyUnitId` | TField |  | The SY.UNIT ID that triggered the use of the underlying application. |
| 6 | `SY.CL.RESERVED.10` | `SyContractLink_Reserved10` | TField |  |  |
| 7 | `SY.CL.RESERVED.9` | `SyContractLink_Reserved9` | TField |  |  |
| 8 | `SY.CL.RESERVED.8` | `SyContractLink_Reserved8` | TField |  |  |
| 9 | `SY.CL.RESERVED.7` | `SyContractLink_Reserved7` | TField |  |  |
| 10 | `SY.CL.RESERVED.6` | `SyContractLink_Reserved6` | TField |  |  |
| 11 | `SY.CL.RESERVED.5` | `SyContractLink_Reserved5` | TField |  |  |
| 12 | `SY.CL.RESERVED.4` | `SyContractLink_Reserved4` | TField |  |  |
| 13 | `SY.CL.RESERVED.3` | `SyContractLink_Reserved3` | TField |  |  |
| 14 | `SY.CL.RESERVED.2` | `SyContractLink_Reserved2` | TField |  |  |
| 15 | `SY.CL.RESERVED.1` | `SyContractLink_Reserved1` | TField |  |  |
| 16 | `SY.CL.LOCAL.REF` | `SyContractLink_LocalRef` |  |  |  |
| 17 | `SY.CL.OVERRIDE` | `SyContractLink_Override` |  |  |  |
