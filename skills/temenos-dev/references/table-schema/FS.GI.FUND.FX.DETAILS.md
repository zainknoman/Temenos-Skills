# FS.GI.FUND.FX.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.FX.DETAILS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.FX.DETAILS.PARENT.REF.ID` | `FsGiFundFxDetails_ParentRefId` |  |  |  |
| 2 | `FS.GI.FUND.FX.DETAILS.ORA.ROWID` | `FsGiFundFxDetails_OraRowid` |  |  |  |
| 3 | `FS.GI.FUND.FX.DETAILS.FUND.ID` | `FsGiFundFxDetails_FundId` |  |  |  |
| 4 | `FS.GI.FUND.FX.DETAILS.FX.PROVIDER` | `FsGiFundFxDetails_FxProvider` |  |  |  |
| 5 | `FS.GI.FUND.FX.DETAILS.INVESTOR.SOURCE.SYSTEM.ID` | `FsGiFundFxDetails_InvestorSourceSystemId` |  |  |  |
| 6 | `FS.GI.FUND.FX.DETAILS.FUND.SOURCE.SYSTEM.ID` | `FsGiFundFxDetails_FundSourceSystemId` |  |  |  |
| 7 | `FS.GI.FUND.FX.DETAILS.DIV.INVESTOR.SOURCE.SYSTEM.ID` | `FsGiFundFxDetails_DivInvestorSourceSystemId` |  |  |  |
| 8 | `FS.GI.FUND.FX.DETAILS.DIV.FUND.SOURCE.SYSTEM.ID` | `FsGiFundFxDetails_DivFundSourceSystemId` |  |  |  |
| 9 | `FS.GI.FUND.FX.DETAILS.COMMISSION.SOURCE.SYSTEM.ID` | `FsGiFundFxDetails_CommissionSourceSystemId` |  |  |  |
| 10 | `FS.GI.FUND.FX.DETAILS.CUSTOMER.NUMBER` | `FsGiFundFxDetails_CustomerNumber` |  |  |  |
| 11 | `FS.GI.FUND.FX.DETAILS.INVESTOR.CUSTOMER.NUMBER` | `FsGiFundFxDetails_InvestorCustomerNumber` |  |  |  |
| 12 | `FS.GI.FUND.FX.DETAILS.FUND.CUSTOMER.NUMBER` | `FsGiFundFxDetails_FundCustomerNumber` |  |  |  |
| 13 | `FS.GI.FUND.FX.DETAILS.DIV.INVESTOR.CUST.NUMBER` | `FsGiFundFxDetails_DivInvestorCustNumber` |  |  |  |
| 14 | `FS.GI.FUND.FX.DETAILS.FUND.INVESTOR.CUST.NUMBER` | `FsGiFundFxDetails_FundInvestorCustNumber` |  |  |  |
| 15 | `FS.GI.FUND.FX.DETAILS.COMMISSION.CUST.NUMBER` | `FsGiFundFxDetails_CommissionCustNumber` |  |  |  |
| 16 | `FS.GI.FUND.FX.DETAILS.BRANCH.CODE` | `FsGiFundFxDetails_BranchCode` |  |  |  |
| 17 | `FS.GI.FUND.FX.DETAILS.SECURITY.ACCOUNT.NUMBER` | `FsGiFundFxDetails_SecurityAccountNumber` |  |  |  |
| 18 | `FS.GI.FUND.FX.DETAILS.RESERVED10` | `FsGiFundFxDetails_Reserved10` |  |  |  |
| 19 | `FS.GI.FUND.FX.DETAILS.RESERVED9` | `FsGiFundFxDetails_Reserved9` |  |  |  |
| 20 | `FS.GI.FUND.FX.DETAILS.RESERVED8` | `FsGiFundFxDetails_Reserved8` |  |  |  |
| 21 | `FS.GI.FUND.FX.DETAILS.RESERVED7` | `FsGiFundFxDetails_Reserved7` |  |  |  |
| 22 | `FS.GI.FUND.FX.DETAILS.RESERVED6` | `FsGiFundFxDetails_Reserved6` |  |  |  |
| 23 | `FS.GI.FUND.FX.DETAILS.RESERVED5` | `FsGiFundFxDetails_Reserved5` |  |  |  |
| 24 | `FS.GI.FUND.FX.DETAILS.RESERVED4` | `FsGiFundFxDetails_Reserved4` |  |  |  |
| 25 | `FS.GI.FUND.FX.DETAILS.RESERVED3` | `FsGiFundFxDetails_Reserved3` |  |  |  |
| 26 | `FS.GI.FUND.FX.DETAILS.RESERVED2` | `FsGiFundFxDetails_Reserved2` |  |  |  |
| 27 | `FS.GI.FUND.FX.DETAILS.RESERVED1` | `FsGiFundFxDetails_Reserved1` |  |  |  |
| 28 | `FS.GI.FUND.FX.DETAILS.LOCAL.REF` | `FsGiFundFxDetails_LocalRef` |  |  |  |
| 29 | `FS.GI.FUND.FX.DETAILS.OVERRIDE` | `FsGiFundFxDetails_Override` |  |  |  |
| 30 | `FS.GI.FUND.FX.DETAILS.RECORD.STATUS` | `FsGiFundFxDetails_RecordStatus` |  |  |  |
| 31 | `FS.GI.FUND.FX.DETAILS.CURR.NO` | `FsGiFundFxDetails_CurrNo` |  |  |  |
| 32 | `FS.GI.FUND.FX.DETAILS.INPUTTER` | `FsGiFundFxDetails_Inputter` |  |  |  |
| 33 | `FS.GI.FUND.FX.DETAILS.DATE.TIME` | `FsGiFundFxDetails_DateTime` |  |  |  |
| 34 | `FS.GI.FUND.FX.DETAILS.AUTHORISER` | `FsGiFundFxDetails_Authoriser` |  |  |  |
| 35 | `FS.GI.FUND.FX.DETAILS.CO.CODE` | `FsGiFundFxDetails_CoCode` |  |  |  |
| 36 | `FS.GI.FUND.FX.DETAILS.DEPT.CODE` | `FsGiFundFxDetails_DeptCode` |  |  |  |
| 37 | `FS.GI.FUND.FX.DETAILS.AUDITOR.CODE` | `FsGiFundFxDetails_AuditorCode` |  |  |  |
| 38 | `FS.GI.FUND.FX.DETAILS.AUDIT.DATE.TIME` | `FsGiFundFxDetails_AuditDateTime` |  |  |  |
