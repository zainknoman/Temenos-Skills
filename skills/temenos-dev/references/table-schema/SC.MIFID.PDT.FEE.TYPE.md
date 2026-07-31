# SC.MIFID.PDT.FEE.TYPE — Table Schema

> Source: `INSERTS/I_F.SC.MIFID.PDT.FEE.TYPE` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.MPF.CATEGORY` | `ScMifidPdtFeeType_Category` | TField | Yes | The category of the product fee will be defined in this field. Currently MiFID allows 5 categories and all the 5 categories will be supported in this field using an EB.LOOKUP table. This will be a mandatory field. Currently supported product categories are One-off Charges Ongoing Costs Transaction Costs Ancillary Charges Incidental Costs |
| 2 | `SC.MPF.LABEL` | `ScMifidPdtFeeType_Label` | TField |  | The description of the respective product fee will be defined in this field. |
| 3 | `SC.MPF.RESERVED.01` | `ScMifidPdtFeeType_Reserved01` | TField |  |  |
| 4 | `SC.MPF.RESERVED.02` | `ScMifidPdtFeeType_Reserved02` | TField |  |  |
| 5 | `SC.MPF.RESERVED.03` | `ScMifidPdtFeeType_Reserved03` | TField |  |  |
| 6 | `SC.MPF.RESERVED.04` | `ScMifidPdtFeeType_Reserved04` | TField |  |  |
| 7 | `SC.MPF.RESERVED.05` | `ScMifidPdtFeeType_Reserved05` | TField |  |  |
| 8 | `SC.MPF.LOCAL.REF` | `ScMifidPdtFeeType_LocalRef` |  |  |  |
| 9 | `SC.MPF.OVERRIDE` | `ScMifidPdtFeeType_Override` |  |  |  |
| 10 | `SC.MPF.RECORD.STATUS` | `ScMifidPdtFeeType_RecordStatus` | String |  |  |
| 11 | `SC.MPF.CURR.NO` | `ScMifidPdtFeeType_CurrNo` | String |  |  |
| 12 | `SC.MPF.INPUTTER` | `ScMifidPdtFeeType_Inputter` |  |  |  |
| 13 | `SC.MPF.DATE.TIME` | `ScMifidPdtFeeType_DateTime` |  |  |  |
| 14 | `SC.MPF.AUTHORISER` | `ScMifidPdtFeeType_Authoriser` | String |  |  |
| 15 | `SC.MPF.CO.CODE` | `ScMifidPdtFeeType_CoCode` | String |  |  |
| 16 | `SC.MPF.DEPT.CODE` | `ScMifidPdtFeeType_DeptCode` | String |  |  |
| 17 | `SC.MPF.AUDITOR.CODE` | `ScMifidPdtFeeType_AuditorCode` | String |  |  |
| 18 | `SC.MPF.AUDIT.DATE.TIME` | `ScMifidPdtFeeType_AuditDateTime` | String |  |  |
