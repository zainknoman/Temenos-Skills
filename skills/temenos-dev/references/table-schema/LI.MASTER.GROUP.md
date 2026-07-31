# LI.MASTER.GROUP — Table Schema

> Source: `INSERTS/I_F.LI.MASTER.GROUP` in `LI_GroupLimit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.MG.GROUP.KEYS` | `LiMasterGroup_GroupKeys` |  |  |  |
| 2 | `LI.MG.GROUP.CUSTOMER` | `LiMasterGroup_GroupCustomer` |  |  |  |
| 3 | `LI.MG.CUSTOMER.PRIORITY` | `LiMasterGroup_CustomerPriority` |  |  |  |
| 4 | `LI.MG.SINGLE.CREDIT.LINE` | `LiMasterGroup_SingleCreditLine` | TField |  |  |
| 5 | `LI.MG.RESERVED.9` | `LiMasterGroup_Reserved9` | TField |  |  |
| 6 | `LI.MG.RESERVED.8` | `LiMasterGroup_Reserved8` | TField |  |  |
| 7 | `LI.MG.RESERVED.7` | `LiMasterGroup_Reserved7` | TField |  |  |
| 8 | `LI.MG.RESERVED.6` | `LiMasterGroup_Reserved6` | TField |  |  |
| 9 | `LI.MG.RESERVED.5` | `LiMasterGroup_Reserved5` | TField |  |  |
| 10 | `LI.MG.RESERVED.4` | `LiMasterGroup_Reserved4` | TField |  |  |
| 11 | `LI.MG.RESERVED.3` | `LiMasterGroup_Reserved3` | TField |  |  |
| 12 | `LI.MG.RESERVED.2` | `LiMasterGroup_Reserved2` | TField |  |  |
| 13 | `LI.MG.RESERVED.1` | `LiMasterGroup_Reserved1` | TField |  |  |
