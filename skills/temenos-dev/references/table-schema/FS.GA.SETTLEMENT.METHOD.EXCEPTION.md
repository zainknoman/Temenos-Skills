# FS.GA.SETTLEMENT.METHOD.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.SETTLEMENT.METHOD.EXCEPTION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.PARENT.REF.ID` | `FsGaSettlementMethodException_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.ORA.ROWID` | `FsGaSettlementMethodException_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.FUND.ID` | `FsGaSettlementMethodException_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.OPERATION.CODE` | `FsGaSettlementMethodException_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 5 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.GTI.CODE` | `FsGaSettlementMethodException_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 6 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.LOCAL.CURRENCY` | `FsGaSettlementMethodException_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 7 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.AUTO.OR.MANUAL` | `FsGaSettlementMethodException_AutoOrManual` | TField |  | Auto or Manual Multifonds DB Column is FCPT_VAL. |
| 8 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.ISSUE.COUNTRY` | `FsGaSettlementMethodException_IssueCountry` | TField |  | Internal Identifier for a country, which is used in various places to include or exclude a specific country from a functionality Multifonds DB Column is CPAYSVAL. |
| 9 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.QUOTATION.PLACE` | `FsGaSettlementMethodException_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 10 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.DEPOSITORY` | `FsGaSettlementMethodException_Depository` | TField |  | Third party depository/correcpondence number Multifonds DB Column is NRACINE. |
| 11 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.ENHANCED.SETTLEMENT` | `FsGaSettlementMethodException_EnhancedSettlement` | TField |  | Enhanced Settlement Multifonds DB Column is FCPT_EN_VAL. |
| 12 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.NUMBER.OF.DAYS.REPAYMENT` | `FsGaSettlementMethodException_NumberOfDaysRepayment` | TField |  | Number Of Days Repayment Multifonds DB Column is NB_DAYS. |
| 13 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.FEE.CODE` | `FsGaSettlementMethodException_FeeCode` | TField |  | Fees code for booking transaction fees Multifonds DB Column is CODE_COM. |
| 14 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.COUNTERPARTY.CORRESPONDENT` | `FsGaSettlementMethodException_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 15 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.RESERVED10` | `FsGaSettlementMethodException_Reserved10` | TField |  |  |
| 16 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.RESERVED9` | `FsGaSettlementMethodException_Reserved9` | TField |  |  |
| 17 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.RESERVED8` | `FsGaSettlementMethodException_Reserved8` | TField |  |  |
| 18 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.RESERVED7` | `FsGaSettlementMethodException_Reserved7` | TField |  |  |
| 19 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.RESERVED6` | `FsGaSettlementMethodException_Reserved6` | TField |  |  |
| 20 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.RESERVED5` | `FsGaSettlementMethodException_Reserved5` | TField |  |  |
| 21 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.RESERVED4` | `FsGaSettlementMethodException_Reserved4` | TField |  |  |
| 22 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.RESERVED3` | `FsGaSettlementMethodException_Reserved3` | TField |  |  |
| 23 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.RESERVED2` | `FsGaSettlementMethodException_Reserved2` | TField |  |  |
| 24 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.RESERVED1` | `FsGaSettlementMethodException_Reserved1` | TField |  |  |
| 25 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.LOCAL.REF` | `FsGaSettlementMethodException_LocalRef` |  |  |  |
| 26 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.OVERRIDE` | `FsGaSettlementMethodException_Override` |  |  |  |
| 27 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.RECORD.STATUS` | `FsGaSettlementMethodException_RecordStatus` | String |  |  |
| 28 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.CURR.NO` | `FsGaSettlementMethodException_CurrNo` | String |  |  |
| 29 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.INPUTTER` | `FsGaSettlementMethodException_Inputter` |  |  |  |
| 30 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.DATE.TIME` | `FsGaSettlementMethodException_DateTime` |  |  |  |
| 31 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.AUTHORISER` | `FsGaSettlementMethodException_Authoriser` | String |  |  |
| 32 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.CO.CODE` | `FsGaSettlementMethodException_CoCode` | String |  |  |
| 33 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.DEPT.CODE` | `FsGaSettlementMethodException_DeptCode` | String |  |  |
| 34 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.AUDITOR.CODE` | `FsGaSettlementMethodException_AuditorCode` | String |  |  |
| 35 | `FS.GA.SETTLEMENT.METHOD.EXCEPTION.AUDIT.DATE.TIME` | `FsGaSettlementMethodException_AuditDateTime` | String |  |  |
