# FS.GI.CONTRACT.FIELDS.CALCULATED — Table Schema

> Source: `INSERTS/I_F.FS.GI.CONTRACT.FIELDS.CALCULATED` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.CONTRACT.FIELDS.CALCULATED.PARENT.REF.ID` | `FsGiContractFieldsCalculated_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.CONTRACT.FIELDS.CALCULATED.ORA.ROWID` | `FsGiContractFieldsCalculated_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.CONTRACT.FIELDS.CALCULATED.REGISTER.ID` | `FsGiContractFieldsCalculated_RegisterId` | TField |  | Register internal Id. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.CONTRACT.FIELDS.CALCULATED.CONTRACT.ID` | `FsGiContractFieldsCalculated_ContractId` | TField |  | Internal id of the contract. Multifonds DB Column is NCONTRACT. |
| 5 | `FS.GI.CONTRACT.FIELDS.CALCULATED.FUND.ID` | `FsGiContractFieldsCalculated_FundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 6 | `FS.GI.CONTRACT.FIELDS.CALCULATED.SHARE.CLASS.CODE` | `FsGiContractFieldsCalculated_ShareClassCode` | TField |  | Fund Share class code. Multifonds DB Column is TPART. |
| 7 | `FS.GI.CONTRACT.FIELDS.CALCULATED.CALCULATED.FIELD.ID` | `FsGiContractFieldsCalculated_CalculatedFieldId` | TField |  | Calculated field ID of the contract. Multifonds DB Column is CONT_CAL_FLD. |
| 8 | `FS.GI.CONTRACT.FIELDS.CALCULATED.CALCULATED.FIELD.DESCRIPTION` | `FsGiContractFieldsCalculated_CalculatedFieldDescription` | TField |  | Calculated field description. Multifonds DB Column is CALC_FLD_XLIB. |
| 9 | `FS.GI.CONTRACT.FIELDS.CALCULATED.CALCULATED.AMOUNT` | `FsGiContractFieldsCalculated_CalculatedAmount` | TField |  | Calculated amount of the calculated field. Multifonds DB Column is CALC_MNT. |
| 10 | `FS.GI.CONTRACT.FIELDS.CALCULATED.PAYMENT.CURRENCY` | `FsGiContractFieldsCalculated_PaymentCurrency` | TField |  | Currency (in 3 letter ISO code, Eg: EUR). Multifonds DB Column is CMON. |
| 11 | `FS.GI.CONTRACT.FIELDS.CALCULATED.RESERVED10` | `FsGiContractFieldsCalculated_Reserved10` | TField |  |  |
| 12 | `FS.GI.CONTRACT.FIELDS.CALCULATED.RESERVED9` | `FsGiContractFieldsCalculated_Reserved9` | TField |  |  |
| 13 | `FS.GI.CONTRACT.FIELDS.CALCULATED.RESERVED8` | `FsGiContractFieldsCalculated_Reserved8` | TField |  |  |
| 14 | `FS.GI.CONTRACT.FIELDS.CALCULATED.RESERVED7` | `FsGiContractFieldsCalculated_Reserved7` | TField |  |  |
| 15 | `FS.GI.CONTRACT.FIELDS.CALCULATED.RESERVED6` | `FsGiContractFieldsCalculated_Reserved6` | TField |  |  |
| 16 | `FS.GI.CONTRACT.FIELDS.CALCULATED.RESERVED5` | `FsGiContractFieldsCalculated_Reserved5` | TField |  |  |
| 17 | `FS.GI.CONTRACT.FIELDS.CALCULATED.RESERVED4` | `FsGiContractFieldsCalculated_Reserved4` | TField |  |  |
| 18 | `FS.GI.CONTRACT.FIELDS.CALCULATED.RESERVED3` | `FsGiContractFieldsCalculated_Reserved3` | TField |  |  |
| 19 | `FS.GI.CONTRACT.FIELDS.CALCULATED.RESERVED2` | `FsGiContractFieldsCalculated_Reserved2` | TField |  |  |
| 20 | `FS.GI.CONTRACT.FIELDS.CALCULATED.RESERVED1` | `FsGiContractFieldsCalculated_Reserved1` | TField |  |  |
| 21 | `FS.GI.CONTRACT.FIELDS.CALCULATED.LOCAL.REF` | `FsGiContractFieldsCalculated_LocalRef` |  |  |  |
| 22 | `FS.GI.CONTRACT.FIELDS.CALCULATED.OVERRIDE` | `FsGiContractFieldsCalculated_Override` |  |  |  |
| 23 | `FS.GI.CONTRACT.FIELDS.CALCULATED.RECORD.STATUS` | `FsGiContractFieldsCalculated_RecordStatus` | String |  |  |
| 24 | `FS.GI.CONTRACT.FIELDS.CALCULATED.CURR.NO` | `FsGiContractFieldsCalculated_CurrNo` | String |  |  |
| 25 | `FS.GI.CONTRACT.FIELDS.CALCULATED.INPUTTER` | `FsGiContractFieldsCalculated_Inputter` |  |  |  |
| 26 | `FS.GI.CONTRACT.FIELDS.CALCULATED.DATE.TIME` | `FsGiContractFieldsCalculated_DateTime` |  |  |  |
| 27 | `FS.GI.CONTRACT.FIELDS.CALCULATED.AUTHORISER` | `FsGiContractFieldsCalculated_Authoriser` | String |  |  |
| 28 | `FS.GI.CONTRACT.FIELDS.CALCULATED.CO.CODE` | `FsGiContractFieldsCalculated_CoCode` | String |  |  |
| 29 | `FS.GI.CONTRACT.FIELDS.CALCULATED.DEPT.CODE` | `FsGiContractFieldsCalculated_DeptCode` | String |  |  |
| 30 | `FS.GI.CONTRACT.FIELDS.CALCULATED.AUDITOR.CODE` | `FsGiContractFieldsCalculated_AuditorCode` | String |  |  |
| 31 | `FS.GI.CONTRACT.FIELDS.CALCULATED.AUDIT.DATE.TIME` | `FsGiContractFieldsCalculated_AuditDateTime` | String |  |  |
