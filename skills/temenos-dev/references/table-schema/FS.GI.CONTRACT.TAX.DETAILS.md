# FS.GI.CONTRACT.TAX.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.CONTRACT.TAX.DETAILS` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.CONTRACT.TAX.DETAILS.PARENT.REF.ID` | `FsGiContractTaxDetails_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.CONTRACT.TAX.DETAILS.ORA.ROWID` | `FsGiContractTaxDetails_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.CONTRACT.TAX.DETAILS.REGISTER.ID` | `FsGiContractTaxDetails_RegisterId` | TField |  | Register Internal Id. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.CONTRACT.TAX.DETAILS.CONTRACT.ID` | `FsGiContractTaxDetails_ContractId` | TField |  | Internal Id of the contract. Multifonds DB Column is NCONTRACT. |
| 5 | `FS.GI.CONTRACT.TAX.DETAILS.ORDER.ID` | `FsGiContractTaxDetails_OrderId` | TField |  | Order id of the contract. Multifonds DB Column is NORDER. |
| 6 | `FS.GI.CONTRACT.TAX.DETAILS.FUND.ID` | `FsGiContractTaxDetails_FundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 7 | `FS.GI.CONTRACT.TAX.DETAILS.SHARE.CLASS.CODE` | `FsGiContractTaxDetails_ShareClassCode` | TField |  | Fund Share class code. Multifonds DB Column is TPARTS. |
| 8 | `FS.GI.CONTRACT.TAX.DETAILS.AGENT.ID` | `FsGiContractTaxDetails_AgentId` | TField |  | Agent internal Id. Multifonds DB Column is NOUTLET. |
| 9 | `FS.GI.CONTRACT.TAX.DETAILS.TAX.ID` | `FsGiContractTaxDetails_TaxId` | TField |  | Tax Internal Id linked to the contract. Multifonds DB Column is TAX_ID. |
| 10 | `FS.GI.CONTRACT.TAX.DETAILS.TAX.DESCRIPTION` | `FsGiContractTaxDetails_TaxDescription` | TField |  | Tax profile description. Multifonds DB Column is TAX_PROFILE. |
| 11 | `FS.GI.CONTRACT.TAX.DETAILS.TAX.AMOUNT` | `FsGiContractTaxDetails_TaxAmount` | TField |  | Calculated Tax Amount linked to Tax Id. Multifonds DB Column is TAX_AMT. |
| 12 | `FS.GI.CONTRACT.TAX.DETAILS.TAX.RATE` | `FsGiContractTaxDetails_TaxRate` | TField |  | Tax Rate applied to the Tax id. Multifonds DB Column is TAX_RATE. |
| 13 | `FS.GI.CONTRACT.TAX.DETAILS.RESERVED10` | `FsGiContractTaxDetails_Reserved10` | TField |  |  |
| 14 | `FS.GI.CONTRACT.TAX.DETAILS.RESERVED9` | `FsGiContractTaxDetails_Reserved9` | TField |  |  |
| 15 | `FS.GI.CONTRACT.TAX.DETAILS.RESERVED8` | `FsGiContractTaxDetails_Reserved8` | TField |  |  |
| 16 | `FS.GI.CONTRACT.TAX.DETAILS.RESERVED7` | `FsGiContractTaxDetails_Reserved7` | TField |  |  |
| 17 | `FS.GI.CONTRACT.TAX.DETAILS.RESERVED6` | `FsGiContractTaxDetails_Reserved6` | TField |  |  |
| 18 | `FS.GI.CONTRACT.TAX.DETAILS.RESERVED5` | `FsGiContractTaxDetails_Reserved5` | TField |  |  |
| 19 | `FS.GI.CONTRACT.TAX.DETAILS.RESERVED4` | `FsGiContractTaxDetails_Reserved4` | TField |  |  |
| 20 | `FS.GI.CONTRACT.TAX.DETAILS.RESERVED3` | `FsGiContractTaxDetails_Reserved3` | TField |  |  |
| 21 | `FS.GI.CONTRACT.TAX.DETAILS.RESERVED2` | `FsGiContractTaxDetails_Reserved2` | TField |  |  |
| 22 | `FS.GI.CONTRACT.TAX.DETAILS.RESERVED1` | `FsGiContractTaxDetails_Reserved1` | TField |  |  |
| 23 | `FS.GI.CONTRACT.TAX.DETAILS.LOCAL.REF` | `FsGiContractTaxDetails_LocalRef` |  |  |  |
| 24 | `FS.GI.CONTRACT.TAX.DETAILS.OVERRIDE` | `FsGiContractTaxDetails_Override` |  |  |  |
| 25 | `FS.GI.CONTRACT.TAX.DETAILS.RECORD.STATUS` | `FsGiContractTaxDetails_RecordStatus` | String |  |  |
| 26 | `FS.GI.CONTRACT.TAX.DETAILS.CURR.NO` | `FsGiContractTaxDetails_CurrNo` | String |  |  |
| 27 | `FS.GI.CONTRACT.TAX.DETAILS.INPUTTER` | `FsGiContractTaxDetails_Inputter` |  |  |  |
| 28 | `FS.GI.CONTRACT.TAX.DETAILS.DATE.TIME` | `FsGiContractTaxDetails_DateTime` |  |  |  |
| 29 | `FS.GI.CONTRACT.TAX.DETAILS.AUTHORISER` | `FsGiContractTaxDetails_Authoriser` | String |  |  |
| 30 | `FS.GI.CONTRACT.TAX.DETAILS.CO.CODE` | `FsGiContractTaxDetails_CoCode` | String |  |  |
| 31 | `FS.GI.CONTRACT.TAX.DETAILS.DEPT.CODE` | `FsGiContractTaxDetails_DeptCode` | String |  |  |
| 32 | `FS.GI.CONTRACT.TAX.DETAILS.AUDITOR.CODE` | `FsGiContractTaxDetails_AuditorCode` | String |  |  |
| 33 | `FS.GI.CONTRACT.TAX.DETAILS.AUDIT.DATE.TIME` | `FsGiContractTaxDetails_AuditDateTime` | String |  |  |
