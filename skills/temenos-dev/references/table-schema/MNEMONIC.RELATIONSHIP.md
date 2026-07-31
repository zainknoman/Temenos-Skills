# MNEMONIC.RELATIONSHIP — Table Schema

> Source: `INSERTS/I_F.MNEMONIC.RELATIONSHIP` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MNE.REL.CR.ID` | `MnemonicRelationship_CrId` | TField |  | Updated with the latest dated CR id. First time when a new CR record is created, this would be updated Subsequently when new dated record of an existing record is created, the latest dated record ID should be updated under the sameCR mnemonic |
| 2 | `MNE.REL.RECORD.STATUS` | `MnemonicRelationship_RecordStatus` | String |  |  |
| 3 | `MNE.REL.CURR.NO` | `MnemonicRelationship_CurrNo` | String |  |  |
| 4 | `MNE.REL.INPUTTER` | `MnemonicRelationship_Inputter` |  |  |  |
| 5 | `MNE.REL.DATE.TIME` | `MnemonicRelationship_DateTime` |  |  |  |
| 6 | `MNE.REL.AUTHORISER` | `MnemonicRelationship_Authoriser` | String |  |  |
| 7 | `MNE.REL.CO.CODE` | `MnemonicRelationship_CoCode` | String |  |  |
| 8 | `MNE.REL.DEPT.CODE` | `MnemonicRelationship_DeptCode` | String |  |  |
| 9 | `MNE.REL.AUDITOR.CODE` | `MnemonicRelationship_AuditorCode` | String |  |  |
| 10 | `MNE.REL.AUDIT.DATE.TIME` | `MnemonicRelationship_AuditDateTime` | String |  |  |
