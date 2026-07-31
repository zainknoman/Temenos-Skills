# DX.CONTRACT.CLASS — Table Schema

> Source: `INSERTS/I_F.DX.CONTRACT.CLASS` in `DX_Configuration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.CC.CLASS.NAME` | `DxContractClass_ClassName` |  |  |  |
| 2 | `DX.CC.CLASS.CATEGORY` | `DxContractClass_ClassCategory` | TField | Yes | product category code used for particular derivative. Must exist in category code. Validation Rules: Up to 5 numerical characters &amp;#150; input must exist on CATEGORY application Mandatory Input |
| 3 | `DX.CC.O.BUY.CALL` | `DxContractClass_OBuyCall` |  |  |  |
| 4 | `DX.CC.O.BUY.PUT` | `DxContractClass_OBuyPut` |  |  |  |
| 5 | `DX.CC.O.SELL.CALL` | `DxContractClass_OSellCall` |  |  |  |
| 6 | `DX.CC.O.SELL.PUT` | `DxContractClass_OSellPut` |  |  |  |
| 7 | `DX.CC.F.BUY` | `DxContractClass_FBuy` |  |  |  |
| 8 | `DX.CC.F.SELL` | `DxContractClass_FSell` |  |  |  |
| 9 | `DX.CC.B2B.CO.OK` | `DxContractClass_B2bCoOk` | TField |  | This field defines whether back to back closeout can happen for the trades covered under this contract class record Validation Rules: Valid values are YES and NO Input can be YES only when B2B.ACTIVE field in DX.PARAMETER is set to YES |
| 10 | `DX.CC.CONTRACT.TYPE` | `DxContractClass_ContractType` | TField |  | Defines the type of contract whether FUTURE, OPTIONS or FX-OPTION. FUTURE and OPTION are for information only. FX-OPTION has to be selected if FX OTC functionality is needed. Any DX.CONTRACT.MASTER with an FX-OPTION enabled Contract Class and exchange as OTC, will be treated as an FX OTC option. For these kind of Contract Masters, the Trade and Delivery currencies can be left open at the Contract level and users can set up different Currency pairs at Trade level by using this single Contract Master. Validation Rule: A NOCHANGE field and will get defaulted to NONE when no values provided. |
| 11 | `DX.CC.DIGITAL` | `DxContractClass_Digital` | TField |  | When set to YES then the contract using it is treated as digital option contract Validation Rules: No Change field |
| 12 | `DX.CC.RESERVED1` | `DxContractClass_Reserved1` | TField |  | Reserved For Future Use Validation Rules: No Input field |
| 13 | `DX.CC.LOCAL.REF` | `DxContractClass_LocalRef` |  |  |  |
| 14 | `DX.CC.OVERRIDE` | `DxContractClass_Override` |  |  |  |
| 15 | `DX.CC.RECORD.STATUS` | `DxContractClass_RecordStatus` | String |  |  |
| 16 | `DX.CC.CURR.NO` | `DxContractClass_CurrNo` | String |  |  |
| 17 | `DX.CC.INPUTTER` | `DxContractClass_Inputter` |  |  |  |
| 18 | `DX.CC.DATE.TIME` | `DxContractClass_DateTime` |  |  |  |
| 19 | `DX.CC.AUTHORISER` | `DxContractClass_Authoriser` | String |  |  |
| 20 | `DX.CC.CO.CODE` | `DxContractClass_CoCode` | String |  |  |
| 21 | `DX.CC.DEPT.CODE` | `DxContractClass_DeptCode` | String |  |  |
| 22 | `DX.CC.AUDITOR.CODE` | `DxContractClass_AuditorCode` | String |  |  |
| 23 | `DX.CC.AUDIT.DATE.TIME` | `DxContractClass_AuditDateTime` | String |  |  |
