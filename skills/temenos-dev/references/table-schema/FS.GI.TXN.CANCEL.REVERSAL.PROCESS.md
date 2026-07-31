# FS.GI.TXN.CANCEL.REVERSAL.PROCESS — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.CANCEL.REVERSAL.PROCESS` in `FS_TransactionProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.PARENT.REF.ID` | `FsGiTxnCancelReversalProcess_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.ORA.ROWID` | `FsGiTxnCancelReversalProcess_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.ORDER.ID` | `FsGiTxnCancelReversalProcess_OrderId` | TField |  | Order identification number. Multifonds DB Column is NORDER. |
| 4 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.AGENT.ID` | `FsGiTxnCancelReversalProcess_AgentId` | TField |  | Agent Internal ID. Multifonds DB Column is NOUTLET. |
| 5 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.CUT.OFF` | `FsGiTxnCancelReversalProcess_CutOff` | TField |  | Cut off date. Multifonds DB Column is CUT_OFF. |
| 6 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.INTERNAL.REVERSAL.COMMENT` | `FsGiTxnCancelReversalProcess_InternalReversalComment` | TField |  | Internal comments for the reversal of contract. Multifonds DB Column is INT_REV_COMNT. |
| 7 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.CLIENT.FX.REVERSAL` | `FsGiTxnCancelReversalProcess_ClientFxReversal` | TField |  | Client FX reversal method. Multifonds DB Column is CLI_FX_REV. |
| 8 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.STP.CANC.MSG.SENT.FLAG` | `FsGiTxnCancelReversalProcess_StpCancMsgSentFlag` | TField |  | Flag to specify whether swift cancellation message should be sent. Multifonds DB Column is FLG_SWIFT_CAN_MSG_SENT. |
| 9 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.STP.CANCELLATION.REASON.CODE` | `FsGiTxnCancelReversalProcess_StpCancellationReasonCode` | TField | Yes | Swift cancellation reason code: Mandatory if the swift cancel message flag is Y. Multifonds DB Column is SWIFT_CAN_MSG_CODE. |
| 10 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.CORRECTION.PAYMENT.FLAG` | `FsGiTxnCancelReversalProcess_CorrectionPaymentFlag` | TField |  | Corrective payment indicator for automated correction payment generation. Multifonds DB Column is FLG_CORR_PAY. |
| 11 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.EXTERNAL.REVERSAL.COMMENT` | `FsGiTxnCancelReversalProcess_ExternalReversalComment` | TField |  | External comments entered during contract reversal. Multifonds DB Column is EXT_REV_COMNT. |
| 12 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.CONTRACT.NOTE.FLAG` | `FsGiTxnCancelReversalProcess_ContractNoteFlag` | TField |  | Flag to produce contract note on reversal. Multifonds DB Column is FLG_CONT_NOTE. |
| 13 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.ERROR.CORRECTION.ID` | `FsGiTxnCancelReversalProcess_ErrorCorrectionId` | TField |  | Error/Correction Identifier for a correction or reversal contract. Multifonds DB Column is ERR_CORR_ID. |
| 14 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.FUND.FX.REVERSAL.FLAG` | `FsGiTxnCancelReversalProcess_FundFxReversalFlag` | TField |  | Fund FX reversal flag. Multifonds DB Column is FLG_FUND_FX_REV. |
| 15 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.PROFIT.AND.LOSS.METHOD` | `FsGiTxnCancelReversalProcess_ProfitAndLossMethod` | TField |  | Method for calculation profit/loss. Multifonds DB Column is PL_METHOD. |
| 16 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.ACT.REVERSAL.TD` | `FsGiTxnCancelReversalProcess_ActReversalTd` | TField |  | Actual reversal trade date used for P/L reversal calculation and appro/expro amount calculation. Multifonds DB Column is ACT_REV_TD. |
| 17 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.REVERSAL.VALUE.DATE` | `FsGiTxnCancelReversalProcess_ReversalValueDate` | TField |  | Derived or user-overridden value date for the reversal Multifonds DB Column is REV_VD. |
| 18 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.CANCELLATION.RIGHTS.FLAG` | `FsGiTxnCancelReversalProcess_CancellationRightsFlag` | TField |  | Cancellation rights flag. Multifonds DB Column is FLG_CANC_RIGHTS. |
| 19 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.CANCELLATION.DATE` | `FsGiTxnCancelReversalProcess_CancellationDate` | TField |  | Order cancellation date. Multifonds DB Column is CANC_DATE. |
| 20 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.PROFIT.LOSS.BEARING` | `FsGiTxnCancelReversalProcess_ProfitLossBearing` | TField |  | Profit and Loss bearing code. Multifonds DB Column is PL_BEARING. |
| 21 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.TRUST.RECEIVED.DATE` | `FsGiTxnCancelReversalProcess_TrustReceivedDate` | TField |  | Date and time order is received from trusted STP counterparty source. Multifonds DB Column is CUT_OFF_TS. |
| 22 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.SOURCE.MESSAGE` | `FsGiTxnCancelReversalProcess_SourceMessage` | TField |  | Code for message source. Multifonds DB Column is SOURCE_MSG. |
| 23 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.SENDER.STP` | `FsGiTxnCancelReversalProcess_SenderStp` | TField |  | STP counterparty address. Multifonds DB Column is SENDER_STP. |
| 24 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.PRE.ORDER.FLAG` | `FsGiTxnCancelReversalProcess_PreOrderFlag` | TField |  | Pre order flag. Multifonds DB Column is FLG_PRE_ORDER. |
| 25 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.EXTERNAL.ORDER.ID` | `FsGiTxnCancelReversalProcess_ExternalOrderId` | TField |  | External order ID. Multifonds DB Column is NORDER_EXTERN. |
| 26 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.RESERVED10` | `FsGiTxnCancelReversalProcess_Reserved10` | TField |  |  |
| 27 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.RESERVED9` | `FsGiTxnCancelReversalProcess_Reserved9` | TField |  |  |
| 28 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.RESERVED8` | `FsGiTxnCancelReversalProcess_Reserved8` | TField |  |  |
| 29 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.RESERVED7` | `FsGiTxnCancelReversalProcess_Reserved7` | TField |  |  |
| 30 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.RESERVED6` | `FsGiTxnCancelReversalProcess_Reserved6` | TField |  |  |
| 31 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.RESERVED5` | `FsGiTxnCancelReversalProcess_Reserved5` | TField |  |  |
| 32 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.RESERVED4` | `FsGiTxnCancelReversalProcess_Reserved4` | TField |  |  |
| 33 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.RESERVED3` | `FsGiTxnCancelReversalProcess_Reserved3` | TField |  |  |
| 34 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.RESERVED2` | `FsGiTxnCancelReversalProcess_Reserved2` | TField |  |  |
| 35 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.RESERVED1` | `FsGiTxnCancelReversalProcess_Reserved1` | TField |  |  |
| 36 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.LOCAL.REF` | `FsGiTxnCancelReversalProcess_LocalRef` |  |  |  |
| 37 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.OVERRIDE` | `FsGiTxnCancelReversalProcess_Override` |  |  |  |
| 38 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.RECORD.STATUS` | `FsGiTxnCancelReversalProcess_RecordStatus` | String |  |  |
| 39 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.CURR.NO` | `FsGiTxnCancelReversalProcess_CurrNo` | String |  |  |
| 40 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.INPUTTER` | `FsGiTxnCancelReversalProcess_Inputter` |  |  |  |
| 41 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.DATE.TIME` | `FsGiTxnCancelReversalProcess_DateTime` |  |  |  |
| 42 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.AUTHORISER` | `FsGiTxnCancelReversalProcess_Authoriser` | String |  |  |
| 43 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.CO.CODE` | `FsGiTxnCancelReversalProcess_CoCode` | String |  |  |
| 44 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.DEPT.CODE` | `FsGiTxnCancelReversalProcess_DeptCode` | String |  |  |
| 45 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.AUDITOR.CODE` | `FsGiTxnCancelReversalProcess_AuditorCode` | String |  |  |
| 46 | `FS.GI.TXN.CANCEL.REVERSAL.PROCESS.AUDIT.DATE.TIME` | `FsGiTxnCancelReversalProcess_AuditDateTime` | String |  |  |
