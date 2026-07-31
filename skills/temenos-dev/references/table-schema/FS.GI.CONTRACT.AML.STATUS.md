# FS.GI.CONTRACT.AML.STATUS — Table Schema

> Source: `INSERTS/I_F.FS.GI.CONTRACT.AML.STATUS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.CONTRACT.AML.STATUS.PARENT.REF.ID` | `FsGiContractAmlStatus_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.CONTRACT.AML.STATUS.ORA.ROWID` | `FsGiContractAmlStatus_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.CONTRACT.AML.STATUS.REGISTER.ID` | `FsGiContractAmlStatus_RegisterId` | TField |  | Register internal Id. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.CONTRACT.AML.STATUS.AGENT.ID` | `FsGiContractAmlStatus_AgentId` | TField |  | Agent internal Id. Multifonds DB Column is NOUTLET. |
| 5 | `FS.GI.CONTRACT.AML.STATUS.TRADE.DATE` | `FsGiContractAmlStatus_TradeDate` | TField |  | Trade date of the contract. Multifonds DB Column is DOPER. |
| 6 | `FS.GI.CONTRACT.AML.STATUS.VALUE.DATE` | `FsGiContractAmlStatus_ValueDate` | TField |  | Value date of the contract. Multifonds DB Column is DVALEUR. |
| 7 | `FS.GI.CONTRACT.AML.STATUS.CONTRACT.ID` | `FsGiContractAmlStatus_ContractId` | TField |  | Internal id of the contract. Multifonds DB Column is NCONTRACT. |
| 8 | `FS.GI.CONTRACT.AML.STATUS.STATUS` | `FsGiContractAmlStatus_Status` | TField |  | Status of the contract. Multifonds DB Column is STATUS. |
| 9 | `FS.GI.CONTRACT.AML.STATUS.ORDER.ID` | `FsGiContractAmlStatus_OrderId` | TField |  | Order number of the contract. Multifonds DB Column is NORDER. |
| 10 | `FS.GI.CONTRACT.AML.STATUS.DEAL.REFERENCE` | `FsGiContractAmlStatus_DealReference` | TField |  | Deal reference number of the contract. Multifonds DB Column is DEAL_REF. |
| 11 | `FS.GI.CONTRACT.AML.STATUS.LEG.LINK` | `FsGiContractAmlStatus_LegLink` | TField |  | Leg link of the contract. Multifonds DB Column is LEG_LINK. |
| 12 | `FS.GI.CONTRACT.AML.STATUS.FUND.ID` | `FsGiContractAmlStatus_FundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 13 | `FS.GI.CONTRACT.AML.STATUS.SHARE.CLASS.CODE` | `FsGiContractAmlStatus_ShareClassCode` | TField |  | Fund share class. Multifonds DB Column is TPART. |
| 14 | `FS.GI.CONTRACT.AML.STATUS.PAYMENT.TYPE` | `FsGiContractAmlStatus_PaymentType` | TField |  | Status type of the payment related to the contract. Multifonds DB Column is PAYMENT_TYPE. |
| 15 | `FS.GI.CONTRACT.AML.STATUS.RESERVED10` | `FsGiContractAmlStatus_Reserved10` | TField |  |  |
| 16 | `FS.GI.CONTRACT.AML.STATUS.RESERVED9` | `FsGiContractAmlStatus_Reserved9` | TField |  |  |
| 17 | `FS.GI.CONTRACT.AML.STATUS.RESERVED8` | `FsGiContractAmlStatus_Reserved8` | TField |  |  |
| 18 | `FS.GI.CONTRACT.AML.STATUS.RESERVED7` | `FsGiContractAmlStatus_Reserved7` | TField |  |  |
| 19 | `FS.GI.CONTRACT.AML.STATUS.RESERVED6` | `FsGiContractAmlStatus_Reserved6` | TField |  |  |
| 20 | `FS.GI.CONTRACT.AML.STATUS.RESERVED5` | `FsGiContractAmlStatus_Reserved5` | TField |  |  |
| 21 | `FS.GI.CONTRACT.AML.STATUS.RESERVED4` | `FsGiContractAmlStatus_Reserved4` | TField |  |  |
| 22 | `FS.GI.CONTRACT.AML.STATUS.RESERVED3` | `FsGiContractAmlStatus_Reserved3` | TField |  |  |
| 23 | `FS.GI.CONTRACT.AML.STATUS.RESERVED2` | `FsGiContractAmlStatus_Reserved2` | TField |  |  |
| 24 | `FS.GI.CONTRACT.AML.STATUS.RESERVED1` | `FsGiContractAmlStatus_Reserved1` | TField |  |  |
| 25 | `FS.GI.CONTRACT.AML.STATUS.LOCAL.REF` | `FsGiContractAmlStatus_LocalRef` |  |  |  |
| 26 | `FS.GI.CONTRACT.AML.STATUS.OVERRIDE` | `FsGiContractAmlStatus_Override` |  |  |  |
| 27 | `FS.GI.CONTRACT.AML.STATUS.RECORD.STATUS` | `FsGiContractAmlStatus_RecordStatus` | String |  |  |
| 28 | `FS.GI.CONTRACT.AML.STATUS.CURR.NO` | `FsGiContractAmlStatus_CurrNo` | String |  |  |
| 29 | `FS.GI.CONTRACT.AML.STATUS.INPUTTER` | `FsGiContractAmlStatus_Inputter` |  |  |  |
| 30 | `FS.GI.CONTRACT.AML.STATUS.DATE.TIME` | `FsGiContractAmlStatus_DateTime` |  |  |  |
| 31 | `FS.GI.CONTRACT.AML.STATUS.AUTHORISER` | `FsGiContractAmlStatus_Authoriser` | String |  |  |
| 32 | `FS.GI.CONTRACT.AML.STATUS.CO.CODE` | `FsGiContractAmlStatus_CoCode` | String |  |  |
| 33 | `FS.GI.CONTRACT.AML.STATUS.DEPT.CODE` | `FsGiContractAmlStatus_DeptCode` | String |  |  |
| 34 | `FS.GI.CONTRACT.AML.STATUS.AUDITOR.CODE` | `FsGiContractAmlStatus_AuditorCode` | String |  |  |
| 35 | `FS.GI.CONTRACT.AML.STATUS.AUDIT.DATE.TIME` | `FsGiContractAmlStatus_AuditDateTime` | String |  |  |
