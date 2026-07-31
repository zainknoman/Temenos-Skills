# FS.GA.CORRESPONDENT.CUSTODIAN — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORRESPONDENT.CUSTODIAN` in `FS_ThirdParties.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CORRESPONDENT.CUSTODIAN.PARENT.REF.ID` | `FsGaCorrespondentCustodian_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CORRESPONDENT.CUSTODIAN.ORA.ROWID` | `FsGaCorrespondentCustodian_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CORRESPONDENT.CUSTODIAN.CORRESPONDENT` | `FsGaCorrespondentCustodian_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 4 | `FS.GA.CORRESPONDENT.CUSTODIAN.FUND.ID` | `FsGaCorrespondentCustodian_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 5 | `FS.GA.CORRESPONDENT.CUSTODIAN.CUSTODIAN.EXTERNAL.ACCOUNT` | `FsGaCorrespondentCustodian_CustodianExternalAccount` | TField |  | Custodian external account number. Multifonds DB Column is NCORRESP_ACCOUNT. |
| 6 | `FS.GA.CORRESPONDENT.CUSTODIAN.DEFAULT.ACCOUNT` | `FsGaCorrespondentCustodian_DefaultAccount` | TField |  | Default account to be set for correspondant custodian. Multifonds DB Column is DFLT_ACCOUNT. |
| 7 | `FS.GA.CORRESPONDENT.CUSTODIAN.LOCAL.CURRENCY` | `FsGaCorrespondentCustodian_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 8 | `FS.GA.CORRESPONDENT.CUSTODIAN.ACCOUNT.STATUS` | `FsGaCorrespondentCustodian_AccountStatus` | TField |  | Account status (Y: Active account for reconciliation-N: Active account-C: Closed account) Multifonds DB Column is ACCOUNT_STATUS. |
| 9 | `FS.GA.CORRESPONDENT.CUSTODIAN.DEPOSITORY.STATUS` | `FsGaCorrespondentCustodian_DepositoryStatus` | TField |  | Depositary status (Y: Active account for reconciliation-N: Active account-C: Closed account) Multifonds DB Column is DEPOSITARY_STATUS. |
| 10 | `FS.GA.CORRESPONDENT.CUSTODIAN.RESERVED10` | `FsGaCorrespondentCustodian_Reserved10` | TField |  |  |
| 11 | `FS.GA.CORRESPONDENT.CUSTODIAN.RESERVED9` | `FsGaCorrespondentCustodian_Reserved9` | TField |  |  |
| 12 | `FS.GA.CORRESPONDENT.CUSTODIAN.RESERVED8` | `FsGaCorrespondentCustodian_Reserved8` | TField |  |  |
| 13 | `FS.GA.CORRESPONDENT.CUSTODIAN.RESERVED7` | `FsGaCorrespondentCustodian_Reserved7` | TField |  |  |
| 14 | `FS.GA.CORRESPONDENT.CUSTODIAN.RESERVED6` | `FsGaCorrespondentCustodian_Reserved6` | TField |  |  |
| 15 | `FS.GA.CORRESPONDENT.CUSTODIAN.RESERVED5` | `FsGaCorrespondentCustodian_Reserved5` | TField |  |  |
| 16 | `FS.GA.CORRESPONDENT.CUSTODIAN.RESERVED4` | `FsGaCorrespondentCustodian_Reserved4` | TField |  |  |
| 17 | `FS.GA.CORRESPONDENT.CUSTODIAN.RESERVED3` | `FsGaCorrespondentCustodian_Reserved3` | TField |  |  |
| 18 | `FS.GA.CORRESPONDENT.CUSTODIAN.RESERVED2` | `FsGaCorrespondentCustodian_Reserved2` | TField |  |  |
| 19 | `FS.GA.CORRESPONDENT.CUSTODIAN.RESERVED1` | `FsGaCorrespondentCustodian_Reserved1` | TField |  |  |
| 20 | `FS.GA.CORRESPONDENT.CUSTODIAN.LOCAL.REF` | `FsGaCorrespondentCustodian_LocalRef` |  |  |  |
| 21 | `FS.GA.CORRESPONDENT.CUSTODIAN.OVERRIDE` | `FsGaCorrespondentCustodian_Override` |  |  |  |
| 22 | `FS.GA.CORRESPONDENT.CUSTODIAN.RECORD.STATUS` | `FsGaCorrespondentCustodian_RecordStatus` | String |  |  |
| 23 | `FS.GA.CORRESPONDENT.CUSTODIAN.CURR.NO` | `FsGaCorrespondentCustodian_CurrNo` | String |  |  |
| 24 | `FS.GA.CORRESPONDENT.CUSTODIAN.INPUTTER` | `FsGaCorrespondentCustodian_Inputter` |  |  |  |
| 25 | `FS.GA.CORRESPONDENT.CUSTODIAN.DATE.TIME` | `FsGaCorrespondentCustodian_DateTime` |  |  |  |
| 26 | `FS.GA.CORRESPONDENT.CUSTODIAN.AUTHORISER` | `FsGaCorrespondentCustodian_Authoriser` | String |  |  |
| 27 | `FS.GA.CORRESPONDENT.CUSTODIAN.CO.CODE` | `FsGaCorrespondentCustodian_CoCode` | String |  |  |
| 28 | `FS.GA.CORRESPONDENT.CUSTODIAN.DEPT.CODE` | `FsGaCorrespondentCustodian_DeptCode` | String |  |  |
| 29 | `FS.GA.CORRESPONDENT.CUSTODIAN.AUDITOR.CODE` | `FsGaCorrespondentCustodian_AuditorCode` | String |  |  |
| 30 | `FS.GA.CORRESPONDENT.CUSTODIAN.AUDIT.DATE.TIME` | `FsGaCorrespondentCustodian_AuditDateTime` | String |  |  |
