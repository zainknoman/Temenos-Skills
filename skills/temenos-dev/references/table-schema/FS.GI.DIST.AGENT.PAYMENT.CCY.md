# FS.GI.DIST.AGENT.PAYMENT.CCY — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AGENT.PAYMENT.CCY` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AGENT.PAYMENT.CCY.PARENT.REF.ID` | `FsGiDistAgentPaymentCcy_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AGENT.PAYMENT.CCY.ORA.ROWID` | `FsGiDistAgentPaymentCcy_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AGENT.PAYMENT.CCY.AGENT.ID` | `FsGiDistAgentPaymentCcy_AgentId` | TField |  | Agent internal ID. Multifonds DB Column is NOUTLET. |
| 4 | `FS.GI.DIST.AGENT.PAYMENT.CCY.TA.FUND.ID` | `FsGiDistAgentPaymentCcy_TaFundId` | TField |  | Fund linked to the agent commission. Multifonds DB Column is NPTF. |
| 5 | `FS.GI.DIST.AGENT.PAYMENT.CCY.COMMISSION.PAYMENT.CURRENCY` | `FsGiDistAgentPaymentCcy_CommissionPaymentCurrency` | TField |  | Preferred commission payment currency. Multifonds DB Column is CMON_PAY. |
| 6 | `FS.GI.DIST.AGENT.PAYMENT.CCY.AGENT.PAY.CCY.ID` | `FsGiDistAgentPaymentCcy_AgentPayCcyId` | TField |  | Unique internal identifier for agent commission payment currency record. Multifonds DB Column is INTERNAL_ID. |
| 7 | `FS.GI.DIST.AGENT.PAYMENT.CCY.FUND.ID` | `FsGiDistAgentPaymentCcy_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 8 | `FS.GI.DIST.AGENT.PAYMENT.CCY.CLASS.CURRENCY` | `FsGiDistAgentPaymentCcy_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 9 | `FS.GI.DIST.AGENT.PAYMENT.CCY.RESERVED10` | `FsGiDistAgentPaymentCcy_Reserved10` | TField |  |  |
| 10 | `FS.GI.DIST.AGENT.PAYMENT.CCY.RESERVED9` | `FsGiDistAgentPaymentCcy_Reserved9` | TField |  |  |
| 11 | `FS.GI.DIST.AGENT.PAYMENT.CCY.RESERVED8` | `FsGiDistAgentPaymentCcy_Reserved8` | TField |  |  |
| 12 | `FS.GI.DIST.AGENT.PAYMENT.CCY.RESERVED7` | `FsGiDistAgentPaymentCcy_Reserved7` | TField |  |  |
| 13 | `FS.GI.DIST.AGENT.PAYMENT.CCY.RESERVED6` | `FsGiDistAgentPaymentCcy_Reserved6` | TField |  |  |
| 14 | `FS.GI.DIST.AGENT.PAYMENT.CCY.RESERVED5` | `FsGiDistAgentPaymentCcy_Reserved5` | TField |  |  |
| 15 | `FS.GI.DIST.AGENT.PAYMENT.CCY.RESERVED4` | `FsGiDistAgentPaymentCcy_Reserved4` | TField |  |  |
| 16 | `FS.GI.DIST.AGENT.PAYMENT.CCY.RESERVED3` | `FsGiDistAgentPaymentCcy_Reserved3` | TField |  |  |
| 17 | `FS.GI.DIST.AGENT.PAYMENT.CCY.RESERVED2` | `FsGiDistAgentPaymentCcy_Reserved2` | TField |  |  |
| 18 | `FS.GI.DIST.AGENT.PAYMENT.CCY.RESERVED1` | `FsGiDistAgentPaymentCcy_Reserved1` | TField |  |  |
| 19 | `FS.GI.DIST.AGENT.PAYMENT.CCY.LOCAL.REF` | `FsGiDistAgentPaymentCcy_LocalRef` |  |  |  |
| 20 | `FS.GI.DIST.AGENT.PAYMENT.CCY.OVERRIDE` | `FsGiDistAgentPaymentCcy_Override` |  |  |  |
| 21 | `FS.GI.DIST.AGENT.PAYMENT.CCY.RECORD.STATUS` | `FsGiDistAgentPaymentCcy_RecordStatus` | String |  |  |
| 22 | `FS.GI.DIST.AGENT.PAYMENT.CCY.CURR.NO` | `FsGiDistAgentPaymentCcy_CurrNo` | String |  |  |
| 23 | `FS.GI.DIST.AGENT.PAYMENT.CCY.INPUTTER` | `FsGiDistAgentPaymentCcy_Inputter` |  |  |  |
| 24 | `FS.GI.DIST.AGENT.PAYMENT.CCY.DATE.TIME` | `FsGiDistAgentPaymentCcy_DateTime` |  |  |  |
| 25 | `FS.GI.DIST.AGENT.PAYMENT.CCY.AUTHORISER` | `FsGiDistAgentPaymentCcy_Authoriser` | String |  |  |
| 26 | `FS.GI.DIST.AGENT.PAYMENT.CCY.CO.CODE` | `FsGiDistAgentPaymentCcy_CoCode` | String |  |  |
| 27 | `FS.GI.DIST.AGENT.PAYMENT.CCY.DEPT.CODE` | `FsGiDistAgentPaymentCcy_DeptCode` | String |  |  |
| 28 | `FS.GI.DIST.AGENT.PAYMENT.CCY.AUDITOR.CODE` | `FsGiDistAgentPaymentCcy_AuditorCode` | String |  |  |
| 29 | `FS.GI.DIST.AGENT.PAYMENT.CCY.AUDIT.DATE.TIME` | `FsGiDistAgentPaymentCcy_AuditDateTime` | String |  |  |
