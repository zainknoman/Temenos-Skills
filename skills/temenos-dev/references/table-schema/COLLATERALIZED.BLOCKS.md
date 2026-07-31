# COLLATERALIZED.BLOCKS — Table Schema

> Source: `INSERTS/I_F.COLLATERALIZED.BLOCKS` in `RLGAAP_CollateralBorrowings.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COLL.BLK.NOM.BLOCK.ID` | `CollateralizedBlocks_NomBlockId` | TField |  | Indicates the ID of the SC.BLOCK.SEC.POS application of a block that is currently active on the system. |
| 2 | `COLL.BLK.RECORD.STATUS` | `CollateralizedBlocks_RecordStatus` | String |  |  |
| 3 | `COLL.BLK.CURR.NO` | `CollateralizedBlocks_CurrNo` | String |  |  |
| 4 | `COLL.BLK.INPUTTER` | `CollateralizedBlocks_Inputter` |  |  |  |
| 5 | `COLL.BLK.DATE.TIME` | `CollateralizedBlocks_DateTime` |  |  |  |
| 6 | `COLL.BLK.AUTHORISER` | `CollateralizedBlocks_Authoriser` | String |  |  |
| 7 | `COLL.BLK.CO.CODE` | `CollateralizedBlocks_CoCode` | String |  |  |
| 8 | `COLL.BLK.DEPT.CODE` | `CollateralizedBlocks_DeptCode` | String |  |  |
| 9 | `COLL.BLK.AUDITOR.CODE` | `CollateralizedBlocks_AuditorCode` | String |  |  |
| 10 | `COLL.BLK.AUDIT.DATE.TIME` | `CollateralizedBlocks_AuditDateTime` | String |  |  |
