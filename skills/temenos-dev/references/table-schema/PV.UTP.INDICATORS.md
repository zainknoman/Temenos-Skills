# PV.UTP.INDICATORS — Table Schema

> Source: `INSERTS/I_F.PV.UTP.INDICATORS` in `PV_DodRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PV.UTP.DESCRIPTION` | `PvUtpIndicators_Description` | TField | Yes | This field holds the Description for each UTP record ID. Validation Rules: Mandatory, Free Text field. |
| 2 | `PV.UTP.UTP.STATUS.UPDATE` | `PvUtpIndicators_UtpStatusUpdate` | TField |  | This field holds the option to be chosen by the user to indicate if the UTP is populated, in PV DOD CUSTOMER DETS table, by the system automatically or by the user manually. Validation Rules: Possible options are Automatic and Manual. Automatic - Indicates that the system will automatically update and remove the UTP indicator in the obligor, based on threshold limit check. For now, only one indicator i.e. Substantial Exposure at Default is considered for automatic update, to identify the status of the obligor. Manual - Indicates that the UTP should be manually selected for default assessment of the obligor and removal of the same should be done manually. If Null - defaulted as Manual. |
| 3 | `PV.UTP.REGULATORY.ADDITIONAL.UTP` | `PvUtpIndicators_RegulatoryAdditionalUtp` | TField | Yes | This field holds the option to be chosen by the user to indicate if the UTP is specified in the regulation or an additional indicator defined by the bank. This helps identifying the UTPs specified by the regulator and those internally. Validation Rules: The options are Reg and Add. Reg - Indicates that the UTP is regulation specific. Add - Indicates that the UTP is a additional one at the discretion of the bank. Mandatory field. |
| 4 | `PV.UTP.UTP.TYPE` | `PvUtpIndicators_UtpType` | TField | Yes | This field holds the type of the UTP indicator. The list of UTP indicator types are defined in EB.LOOKUP table. Additional UTPs can be added to the record PV.UTP.TYPE in EB.LOOKUP table. UTP Type includes Pulling effect, Non-accrued status, Distressed restructuring, and Bankruptcy etc. Validation Rules: Selection from the EB LOOKUP file data record PV.UTP.TYPE. Mandatory field. |
| 5 | `PV.UTP.PULLING.EFFECT.TEST` | `PvUtpIndicators_PullingEffectTest` | TField |  | This field indicates whether the pulling effective test is applied for the PV.UTP.TYPE. UTP indicators with this field marked as REQD can be specified in UTP.INDICATOR field of PV.DOD.PARAMETER, for automatic default assessment of the obligor. Validation Rules: Options allowed are REQD and Null. REQD option is allowed only when PV.UTP.STATUS.UPDATE is AUTOMATIC. When this field value is null, it signifies pulling effective test need not to be performed for this UTP. |
| 6 | `PV.UTP.DISTRESS.RESTRUCTURE.UTP` | `PvUtpIndicators_DistressRestructureUtp` | TField |  | Purpose of this field is to indicate whether this UTP is meant for Distressed Restructuring. UTP indicators with DISTRESS.RESTRUCTURE.UTP marked as YES can be specified in PV.DOD.CUSTOMER.DETS. When this UTP Type is removed from PV.DOD.CUSTOMER.DETS record, Distressed Restructuring Date field in PV.DOD.CUSTOMER.DETS will be updated. Validation Rules: Options allowed - YES / Null. No change field. When YES is chosen, it signifies that the UTP indicator is a distressed restructuring UTP When null is present, it signifies that the UTP indicator is not a distressed restructuring UTP. |
| 7 | `PV.UTP.RESERVED.9` | `PvUtpIndicators_Reserved9` | TField |  |  |
| 8 | `PV.UTP.RESERVED.8` | `PvUtpIndicators_Reserved8` | TField |  |  |
| 9 | `PV.UTP.RESERVED.7` | `PvUtpIndicators_Reserved7` | TField |  |  |
| 10 | `PV.UTP.RESERVED.6` | `PvUtpIndicators_Reserved6` | TField |  |  |
| 11 | `PV.UTP.RESERVED.5` | `PvUtpIndicators_Reserved5` | TField |  |  |
| 12 | `PV.UTP.RESERVED.4` | `PvUtpIndicators_Reserved4` | TField |  |  |
| 13 | `PV.UTP.RESERVED.3` | `PvUtpIndicators_Reserved3` | TField |  |  |
| 14 | `PV.UTP.RESERVED.2` | `PvUtpIndicators_Reserved2` | TField |  |  |
| 15 | `PV.UTP.RESERVED.1` | `PvUtpIndicators_Reserved1` | TField |  |  |
| 16 | `PV.UTP.LOCAL.REF` | `PvUtpIndicators_LocalRef` |  |  |  |
| 17 | `PV.UTP.OVERRIDE` | `PvUtpIndicators_Override` |  |  |  |
| 18 | `PV.UTP.RECORD.STATUS` | `PvUtpIndicators_RecordStatus` | String |  |  |
| 19 | `PV.UTP.CURR.NO` | `PvUtpIndicators_CurrNo` | String |  |  |
| 20 | `PV.UTP.INPUTTER` | `PvUtpIndicators_Inputter` |  |  |  |
| 21 | `PV.UTP.DATE.TIME` | `PvUtpIndicators_DateTime` |  |  |  |
| 22 | `PV.UTP.AUTHORISER` | `PvUtpIndicators_Authoriser` | String |  |  |
| 23 | `PV.UTP.CO.CODE` | `PvUtpIndicators_CoCode` | String |  |  |
| 24 | `PV.UTP.DEPT.CODE` | `PvUtpIndicators_DeptCode` | String |  |  |
| 25 | `PV.UTP.AUDITOR.CODE` | `PvUtpIndicators_AuditorCode` | String |  |  |
| 26 | `PV.UTP.AUDIT.DATE.TIME` | `PvUtpIndicators_AuditDateTime` | String |  |  |
