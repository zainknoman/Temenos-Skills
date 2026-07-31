# FS.GI.TXN.ORDER.CORRECTION.LINK — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.ORDER.CORRECTION.LINK` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.ORDER.CORRECTION.LINK.PARENT.REF.ID` | `FsGiTxnOrderCorrectionLink_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.ORDER.CORRECTION.LINK.ORA.ROWID` | `FsGiTxnOrderCorrectionLink_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.ORDER.CORRECTION.LINK.ORDER.ID.CORRECTION` | `FsGiTxnOrderCorrectionLink_OrderIdCorrection` | TField |  | Order identification number of the Main Correction Deal. Multifonds DB Column is NORDER_CORR. |
| 4 | `FS.GI.TXN.ORDER.CORRECTION.LINK.AGENT.ID.CORRECTION` | `FsGiTxnOrderCorrectionLink_AgentIdCorrection` | TField |  | Agent internal ID of the Main Correction Deal. Multifonds DB Column is NOUTLET_CORR. |
| 5 | `FS.GI.TXN.ORDER.CORRECTION.LINK.AGENT.ID` | `FsGiTxnOrderCorrectionLink_AgentId` | TField |  | Agent of the Correction linked deal. Multifonds DB Column is NOUTLET. |
| 6 | `FS.GI.TXN.ORDER.CORRECTION.LINK.ORDER.ID` | `FsGiTxnOrderCorrectionLink_OrderId` | TField |  | Order identification number of the Correction linked deal. Multifonds DB Column is NORDER. |
| 7 | `FS.GI.TXN.ORDER.CORRECTION.LINK.CR.DEAL.REFERENCE` | `FsGiTxnOrderCorrectionLink_CrDealReference` | TField |  | Credit deal reference of the correction linked deal. Multifonds DB Column is DEAL_REF_CR. |
| 8 | `FS.GI.TXN.ORDER.CORRECTION.LINK.IN.DEAL.REFERENCE` | `FsGiTxnOrderCorrectionLink_InDealReference` | TField |  | Leg In Credit deal reference of the correction linked deal. Multifonds DB Column is DEAL_REF_IN. |
| 9 | `FS.GI.TXN.ORDER.CORRECTION.LINK.RESERVED10` | `FsGiTxnOrderCorrectionLink_Reserved10` | TField |  |  |
| 10 | `FS.GI.TXN.ORDER.CORRECTION.LINK.RESERVED9` | `FsGiTxnOrderCorrectionLink_Reserved9` | TField |  |  |
| 11 | `FS.GI.TXN.ORDER.CORRECTION.LINK.RESERVED8` | `FsGiTxnOrderCorrectionLink_Reserved8` | TField |  |  |
| 12 | `FS.GI.TXN.ORDER.CORRECTION.LINK.RESERVED7` | `FsGiTxnOrderCorrectionLink_Reserved7` | TField |  |  |
| 13 | `FS.GI.TXN.ORDER.CORRECTION.LINK.RESERVED6` | `FsGiTxnOrderCorrectionLink_Reserved6` | TField |  |  |
| 14 | `FS.GI.TXN.ORDER.CORRECTION.LINK.RESERVED5` | `FsGiTxnOrderCorrectionLink_Reserved5` | TField |  |  |
| 15 | `FS.GI.TXN.ORDER.CORRECTION.LINK.RESERVED4` | `FsGiTxnOrderCorrectionLink_Reserved4` | TField |  |  |
| 16 | `FS.GI.TXN.ORDER.CORRECTION.LINK.RESERVED3` | `FsGiTxnOrderCorrectionLink_Reserved3` | TField |  |  |
| 17 | `FS.GI.TXN.ORDER.CORRECTION.LINK.RESERVED2` | `FsGiTxnOrderCorrectionLink_Reserved2` | TField |  |  |
| 18 | `FS.GI.TXN.ORDER.CORRECTION.LINK.RESERVED1` | `FsGiTxnOrderCorrectionLink_Reserved1` | TField |  |  |
| 19 | `FS.GI.TXN.ORDER.CORRECTION.LINK.LOCAL.REF` | `FsGiTxnOrderCorrectionLink_LocalRef` |  |  |  |
| 20 | `FS.GI.TXN.ORDER.CORRECTION.LINK.OVERRIDE` | `FsGiTxnOrderCorrectionLink_Override` |  |  |  |
| 21 | `FS.GI.TXN.ORDER.CORRECTION.LINK.RECORD.STATUS` | `FsGiTxnOrderCorrectionLink_RecordStatus` | String |  |  |
| 22 | `FS.GI.TXN.ORDER.CORRECTION.LINK.CURR.NO` | `FsGiTxnOrderCorrectionLink_CurrNo` | String |  |  |
| 23 | `FS.GI.TXN.ORDER.CORRECTION.LINK.INPUTTER` | `FsGiTxnOrderCorrectionLink_Inputter` |  |  |  |
| 24 | `FS.GI.TXN.ORDER.CORRECTION.LINK.DATE.TIME` | `FsGiTxnOrderCorrectionLink_DateTime` |  |  |  |
| 25 | `FS.GI.TXN.ORDER.CORRECTION.LINK.AUTHORISER` | `FsGiTxnOrderCorrectionLink_Authoriser` | String |  |  |
| 26 | `FS.GI.TXN.ORDER.CORRECTION.LINK.CO.CODE` | `FsGiTxnOrderCorrectionLink_CoCode` | String |  |  |
| 27 | `FS.GI.TXN.ORDER.CORRECTION.LINK.DEPT.CODE` | `FsGiTxnOrderCorrectionLink_DeptCode` | String |  |  |
| 28 | `FS.GI.TXN.ORDER.CORRECTION.LINK.AUDITOR.CODE` | `FsGiTxnOrderCorrectionLink_AuditorCode` | String |  |  |
| 29 | `FS.GI.TXN.ORDER.CORRECTION.LINK.AUDIT.DATE.TIME` | `FsGiTxnOrderCorrectionLink_AuditDateTime` | String |  |  |
