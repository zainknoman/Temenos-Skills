# FS.GA.CORP.ACTION.TAX — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORP.ACTION.TAX` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CORP.ACTION.TAX.PARENT.REF.ID` | `FsGaCorpActionTax_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CORP.ACTION.TAX.ORA.ROWID` | `FsGaCorpActionTax_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CORP.ACTION.TAX.OPERATION.CODE` | `FsGaCorpActionTax_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 4 | `FS.GA.CORP.ACTION.TAX.INTERNAL.SECURITY.ID` | `FsGaCorpActionTax_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 5 | `FS.GA.CORP.ACTION.TAX.NSEQUENCE` | `FsGaCorpActionTax_Nsequence` | TField |  | Corresponds to the sequence number Multifonds DB Column is NSEQ. |
| 6 | `FS.GA.CORP.ACTION.TAX.SUBSEQUENCE.NUMBER` | `FsGaCorpActionTax_SubsequenceNumber` | TField |  | Corresponds to the sub sequence number Multifonds DB Column is NSUB_SEQ. |
| 7 | `FS.GA.CORP.ACTION.TAX.FEE.CODE` | `FsGaCorpActionTax_FeeCode` | TField |  | Fees code for booking transaction fees Multifonds DB Column is CODE_COM. |
| 8 | `FS.GA.CORP.ACTION.TAX.FEES.RATE` | `FsGaCorpActionTax_FeesRate` | TField |  | The percentage of fees that needs to be applied on a transaction. Multifonds DB Column is PC_MNT. |
| 9 | `FS.GA.CORP.ACTION.TAX.LOCAL.CURRENCY` | `FsGaCorpActionTax_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 10 | `FS.GA.CORP.ACTION.TAX.EXTERNAL.REFERENCE.NUMBER` | `FsGaCorpActionTax_ExternalReferenceNumber` | TField |  | External reference corresponds a trade,security or fund Multifonds DB Column is EXT_REF. |
| 11 | `FS.GA.CORP.ACTION.TAX.RESERVED10` | `FsGaCorpActionTax_Reserved10` | TField |  |  |
| 12 | `FS.GA.CORP.ACTION.TAX.RESERVED9` | `FsGaCorpActionTax_Reserved9` | TField |  |  |
| 13 | `FS.GA.CORP.ACTION.TAX.RESERVED8` | `FsGaCorpActionTax_Reserved8` | TField |  |  |
| 14 | `FS.GA.CORP.ACTION.TAX.RESERVED7` | `FsGaCorpActionTax_Reserved7` | TField |  |  |
| 15 | `FS.GA.CORP.ACTION.TAX.RESERVED6` | `FsGaCorpActionTax_Reserved6` | TField |  |  |
| 16 | `FS.GA.CORP.ACTION.TAX.RESERVED5` | `FsGaCorpActionTax_Reserved5` | TField |  |  |
| 17 | `FS.GA.CORP.ACTION.TAX.RESERVED4` | `FsGaCorpActionTax_Reserved4` | TField |  |  |
| 18 | `FS.GA.CORP.ACTION.TAX.RESERVED3` | `FsGaCorpActionTax_Reserved3` | TField |  |  |
| 19 | `FS.GA.CORP.ACTION.TAX.RESERVED2` | `FsGaCorpActionTax_Reserved2` | TField |  |  |
| 20 | `FS.GA.CORP.ACTION.TAX.RESERVED1` | `FsGaCorpActionTax_Reserved1` | TField |  |  |
| 21 | `FS.GA.CORP.ACTION.TAX.LOCAL.REF` | `FsGaCorpActionTax_LocalRef` |  |  |  |
| 22 | `FS.GA.CORP.ACTION.TAX.OVERRIDE` | `FsGaCorpActionTax_Override` |  |  |  |
| 23 | `FS.GA.CORP.ACTION.TAX.RECORD.STATUS` | `FsGaCorpActionTax_RecordStatus` | String |  |  |
| 24 | `FS.GA.CORP.ACTION.TAX.CURR.NO` | `FsGaCorpActionTax_CurrNo` | String |  |  |
| 25 | `FS.GA.CORP.ACTION.TAX.INPUTTER` | `FsGaCorpActionTax_Inputter` |  |  |  |
| 26 | `FS.GA.CORP.ACTION.TAX.DATE.TIME` | `FsGaCorpActionTax_DateTime` |  |  |  |
| 27 | `FS.GA.CORP.ACTION.TAX.AUTHORISER` | `FsGaCorpActionTax_Authoriser` | String |  |  |
| 28 | `FS.GA.CORP.ACTION.TAX.CO.CODE` | `FsGaCorpActionTax_CoCode` | String |  |  |
| 29 | `FS.GA.CORP.ACTION.TAX.DEPT.CODE` | `FsGaCorpActionTax_DeptCode` | String |  |  |
| 30 | `FS.GA.CORP.ACTION.TAX.AUDITOR.CODE` | `FsGaCorpActionTax_AuditorCode` | String |  |  |
| 31 | `FS.GA.CORP.ACTION.TAX.AUDIT.DATE.TIME` | `FsGaCorpActionTax_AuditDateTime` | String |  |  |
