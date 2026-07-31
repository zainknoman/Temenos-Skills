# FS.GI.TXN.ORDER.SOS — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.ORDER.SOS` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.ORDER.SOS.PARENT.REF.ID` | `FsGiTxnOrderSos_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.ORDER.SOS.ORA.ROWID` | `FsGiTxnOrderSos_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.ORDER.SOS.FUND.ID` | `FsGiTxnOrderSos_FundId` | TField |  | Fund ID for which order is created. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.TXN.ORDER.SOS.ORDER.ID` | `FsGiTxnOrderSos_OrderId` | TField |  | Order identification number. Multifonds DB Column is NORDER. |
| 5 | `FS.GI.TXN.ORDER.SOS.AGENT.ID` | `FsGiTxnOrderSos_AgentId` | TField |  | Agent ID linked to the order. Multifonds DB Column is NOUTLET. |
| 6 | `FS.GI.TXN.ORDER.SOS.SHARE.CLASS.CODE` | `FsGiTxnOrderSos_ShareClassCode` | TField |  | Multi Series Share Class which is linked for redemption. Multifonds DB Column is TPART. |
| 7 | `FS.GI.TXN.ORDER.SOS.QUANTITY` | `FsGiTxnOrderSos_Quantity` | TField |  | Quantity which is need to be redeemed from series share class. Multifonds DB Column is QUANTITY. |
| 8 | `FS.GI.TXN.ORDER.SOS.AMOUNT` | `FsGiTxnOrderSos_Amount` | TField |  | Redeemable Amount which is need to be redeemed from series share class. Multifonds DB Column is AMOUNT. |
| 9 | `FS.GI.TXN.ORDER.SOS.RESERVED10` | `FsGiTxnOrderSos_Reserved10` | TField |  |  |
| 10 | `FS.GI.TXN.ORDER.SOS.RESERVED9` | `FsGiTxnOrderSos_Reserved9` | TField |  |  |
| 11 | `FS.GI.TXN.ORDER.SOS.RESERVED8` | `FsGiTxnOrderSos_Reserved8` | TField |  |  |
| 12 | `FS.GI.TXN.ORDER.SOS.RESERVED7` | `FsGiTxnOrderSos_Reserved7` | TField |  |  |
| 13 | `FS.GI.TXN.ORDER.SOS.RESERVED6` | `FsGiTxnOrderSos_Reserved6` | TField |  |  |
| 14 | `FS.GI.TXN.ORDER.SOS.RESERVED5` | `FsGiTxnOrderSos_Reserved5` | TField |  |  |
| 15 | `FS.GI.TXN.ORDER.SOS.RESERVED4` | `FsGiTxnOrderSos_Reserved4` | TField |  |  |
| 16 | `FS.GI.TXN.ORDER.SOS.RESERVED3` | `FsGiTxnOrderSos_Reserved3` | TField |  |  |
| 17 | `FS.GI.TXN.ORDER.SOS.RESERVED2` | `FsGiTxnOrderSos_Reserved2` | TField |  |  |
| 18 | `FS.GI.TXN.ORDER.SOS.RESERVED1` | `FsGiTxnOrderSos_Reserved1` | TField |  |  |
| 19 | `FS.GI.TXN.ORDER.SOS.LOCAL.REF` | `FsGiTxnOrderSos_LocalRef` |  |  |  |
| 20 | `FS.GI.TXN.ORDER.SOS.OVERRIDE` | `FsGiTxnOrderSos_Override` |  |  |  |
| 21 | `FS.GI.TXN.ORDER.SOS.RECORD.STATUS` | `FsGiTxnOrderSos_RecordStatus` | String |  |  |
| 22 | `FS.GI.TXN.ORDER.SOS.CURR.NO` | `FsGiTxnOrderSos_CurrNo` | String |  |  |
| 23 | `FS.GI.TXN.ORDER.SOS.INPUTTER` | `FsGiTxnOrderSos_Inputter` |  |  |  |
| 24 | `FS.GI.TXN.ORDER.SOS.DATE.TIME` | `FsGiTxnOrderSos_DateTime` |  |  |  |
| 25 | `FS.GI.TXN.ORDER.SOS.AUTHORISER` | `FsGiTxnOrderSos_Authoriser` | String |  |  |
| 26 | `FS.GI.TXN.ORDER.SOS.CO.CODE` | `FsGiTxnOrderSos_CoCode` | String |  |  |
| 27 | `FS.GI.TXN.ORDER.SOS.DEPT.CODE` | `FsGiTxnOrderSos_DeptCode` | String |  |  |
| 28 | `FS.GI.TXN.ORDER.SOS.AUDITOR.CODE` | `FsGiTxnOrderSos_AuditorCode` | String |  |  |
| 29 | `FS.GI.TXN.ORDER.SOS.AUDIT.DATE.TIME` | `FsGiTxnOrderSos_AuditDateTime` | String |  |  |
