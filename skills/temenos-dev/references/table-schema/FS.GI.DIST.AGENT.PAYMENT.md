# FS.GI.DIST.AGENT.PAYMENT — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AGENT.PAYMENT` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AGENT.PAYMENT.PARENT.REF.ID` | `FsGiDistAgentPayment_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AGENT.PAYMENT.ORA.ROWID` | `FsGiDistAgentPayment_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AGENT.PAYMENT.AGENT.ID` | `FsGiDistAgentPayment_AgentId` | TField |  | Agent Internal ID. Multifonds DB Column is NOUTLET. |
| 4 | `FS.GI.DIST.AGENT.PAYMENT.LEGAL.ENTITY.ID` | `FsGiDistAgentPayment_LegalEntityId` | TField |  | Legal Entity linked to the agent. Multifonds DB Column is NTFC. |
| 5 | `FS.GI.DIST.AGENT.PAYMENT.FUND.ID` | `FsGiDistAgentPayment_FundId` | TField |  | Fund internal Id linked to the agent. Multifonds DB Column is NPTF. |
| 6 | `FS.GI.DIST.AGENT.PAYMENT.SHARE.CLASS.CODE` | `FsGiDistAgentPayment_ShareClassCode` | TField |  | Fund share class linked to the agent. Multifonds DB Column is TPART. |
| 7 | `FS.GI.DIST.AGENT.PAYMENT.CORRESPONDANT.ID` | `FsGiDistAgentPayment_CorrespondantId` | TField |  | Correspondent ID. Multifonds DB Column is NCORRESP. |
| 8 | `FS.GI.DIST.AGENT.PAYMENT.BANK.ACCOUNT.NUMBER` | `FsGiDistAgentPayment_BankAccountNumber` | TField |  | Bank account number of the agent. Multifonds DB Column is BANK_ACCOUNT. |
| 9 | `FS.GI.DIST.AGENT.PAYMENT.PAYMENT.DATE` | `FsGiDistAgentPayment_PaymentDate` | TField |  | Date on which payment is made to the agent. Multifonds DB Column is DATE_PAYMENT. |
| 10 | `FS.GI.DIST.AGENT.PAYMENT.CALC.DATE` | `FsGiDistAgentPayment_CalcDate` | TField |  | Date on which calculation of the commission. Multifonds DB Column is DATE_CALC. |
| 11 | `FS.GI.DIST.AGENT.PAYMENT.INTERMEDIATE.BANK.ID` | `FsGiDistAgentPayment_IntermediateBankId` | TField |  | Intermediate bank ID of the agent. Multifonds DB Column is NCORESP_INTER. |
| 12 | `FS.GI.DIST.AGENT.PAYMENT.INTERM.BANK.ACCOUNT` | `FsGiDistAgentPayment_IntermBankAccount` | TField |  | Intermediate bank account number of the agent. Multifonds DB Column is BANK_ACCOUNT_INTER. |
| 13 | `FS.GI.DIST.AGENT.PAYMENT.PAYMENT.CCY` | `FsGiDistAgentPayment_PaymentCcy` | TField |  | Payment currency code (in 3 letter ISO code, Eg: EUR). Multifonds DB Column is CMON_PAYMENT. |
| 14 | `FS.GI.DIST.AGENT.PAYMENT.AMOUNT` | `FsGiDistAgentPayment_Amount` | TField |  | Payment amount. Multifonds DB Column is AMOUNT. |
| 15 | `FS.GI.DIST.AGENT.PAYMENT.RESERVED10` | `FsGiDistAgentPayment_Reserved10` | TField |  |  |
| 16 | `FS.GI.DIST.AGENT.PAYMENT.RESERVED9` | `FsGiDistAgentPayment_Reserved9` | TField |  |  |
| 17 | `FS.GI.DIST.AGENT.PAYMENT.RESERVED8` | `FsGiDistAgentPayment_Reserved8` | TField |  |  |
| 18 | `FS.GI.DIST.AGENT.PAYMENT.RESERVED7` | `FsGiDistAgentPayment_Reserved7` | TField |  |  |
| 19 | `FS.GI.DIST.AGENT.PAYMENT.RESERVED6` | `FsGiDistAgentPayment_Reserved6` | TField |  |  |
| 20 | `FS.GI.DIST.AGENT.PAYMENT.RESERVED5` | `FsGiDistAgentPayment_Reserved5` | TField |  |  |
| 21 | `FS.GI.DIST.AGENT.PAYMENT.RESERVED4` | `FsGiDistAgentPayment_Reserved4` | TField |  |  |
| 22 | `FS.GI.DIST.AGENT.PAYMENT.RESERVED3` | `FsGiDistAgentPayment_Reserved3` | TField |  |  |
| 23 | `FS.GI.DIST.AGENT.PAYMENT.RESERVED2` | `FsGiDistAgentPayment_Reserved2` | TField |  |  |
| 24 | `FS.GI.DIST.AGENT.PAYMENT.RESERVED1` | `FsGiDistAgentPayment_Reserved1` | TField |  |  |
| 25 | `FS.GI.DIST.AGENT.PAYMENT.LOCAL.REF` | `FsGiDistAgentPayment_LocalRef` |  |  |  |
| 26 | `FS.GI.DIST.AGENT.PAYMENT.OVERRIDE` | `FsGiDistAgentPayment_Override` |  |  |  |
| 27 | `FS.GI.DIST.AGENT.PAYMENT.RECORD.STATUS` | `FsGiDistAgentPayment_RecordStatus` | String |  |  |
| 28 | `FS.GI.DIST.AGENT.PAYMENT.CURR.NO` | `FsGiDistAgentPayment_CurrNo` | String |  |  |
| 29 | `FS.GI.DIST.AGENT.PAYMENT.INPUTTER` | `FsGiDistAgentPayment_Inputter` |  |  |  |
| 30 | `FS.GI.DIST.AGENT.PAYMENT.DATE.TIME` | `FsGiDistAgentPayment_DateTime` |  |  |  |
| 31 | `FS.GI.DIST.AGENT.PAYMENT.AUTHORISER` | `FsGiDistAgentPayment_Authoriser` | String |  |  |
| 32 | `FS.GI.DIST.AGENT.PAYMENT.CO.CODE` | `FsGiDistAgentPayment_CoCode` | String |  |  |
| 33 | `FS.GI.DIST.AGENT.PAYMENT.DEPT.CODE` | `FsGiDistAgentPayment_DeptCode` | String |  |  |
| 34 | `FS.GI.DIST.AGENT.PAYMENT.AUDITOR.CODE` | `FsGiDistAgentPayment_AuditorCode` | String |  |  |
| 35 | `FS.GI.DIST.AGENT.PAYMENT.AUDIT.DATE.TIME` | `FsGiDistAgentPayment_AuditDateTime` | String |  |  |
