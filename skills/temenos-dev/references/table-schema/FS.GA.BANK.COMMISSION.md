# FS.GA.BANK.COMMISSION — Table Schema

> Source: `INSERTS/I_F.FS.GA.BANK.COMMISSION` in `FS_Fee.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.BANK.COMMISSION.PARENT.REF.ID` | `FsGaBankCommission_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.BANK.COMMISSION.ORA.ROWID` | `FsGaBankCommission_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.BANK.COMMISSION.FEE.CODE` | `FsGaBankCommission_FeeCode` | TField |  | Fees code for booking transaction fees Multifonds DB Column is CODE_COM. |
| 4 | `FS.GA.BANK.COMMISSION.SERVICE.CODE` | `FsGaBankCommission_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 5 | `FS.GA.BANK.COMMISSION.FUND.ID` | `FsGaBankCommission_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 6 | `FS.GA.BANK.COMMISSION.CORRESPONDENT` | `FsGaBankCommission_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 7 | `FS.GA.BANK.COMMISSION.LOCAL.CURRENCY` | `FsGaBankCommission_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 8 | `FS.GA.BANK.COMMISSION.COMMISSION.GROUP` | `FsGaBankCommission_CommissionGroup` | TField |  | Enter a free definable commission group Multifonds DB Column is COMM_GRP. |
| 9 | `FS.GA.BANK.COMMISSION.FEE.TYPE` | `FsGaBankCommission_FeeType` | TField |  | Type of charge parameterized in multifonds Multifonds DB Column is TCHARGE. |
| 10 | `FS.GA.BANK.COMMISSION.CHARGE.CURRENCY` | `FsGaBankCommission_ChargeCurrency` | TField |  | Charge Currency Multifonds DB Column is CHARGE_CMON. |
| 11 | `FS.GA.BANK.COMMISSION.AMOUNT.OR.PERCENT` | `FsGaBankCommission_AmountOrPercent` | TField |  | Enter the percentage or amount of the fee Multifonds DB Column is MNTPRT. |
| 12 | `FS.GA.BANK.COMMISSION.SCALE.CODE` | `FsGaBankCommission_ScaleCode` | TField |  | If the fee type is equal to &quot;5 - Scale&quot;, a scale code needs to be entered. Note that scales must have been created before via the button scale Multifonds DB Column is CBAREME. |
| 13 | `FS.GA.BANK.COMMISSION.OPERATION.CODE` | `FsGaBankCommission_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 14 | `FS.GA.BANK.COMMISSION.COUNTRY.ID.CODE` | `FsGaBankCommission_CountryIdCode` | TField |  | Defines the country short code Multifonds DB Column is CPAYS. |
| 15 | `FS.GA.BANK.COMMISSION.RESERVED10` | `FsGaBankCommission_Reserved10` | TField |  |  |
| 16 | `FS.GA.BANK.COMMISSION.RESERVED9` | `FsGaBankCommission_Reserved9` | TField |  |  |
| 17 | `FS.GA.BANK.COMMISSION.RESERVED8` | `FsGaBankCommission_Reserved8` | TField |  |  |
| 18 | `FS.GA.BANK.COMMISSION.RESERVED7` | `FsGaBankCommission_Reserved7` | TField |  |  |
| 19 | `FS.GA.BANK.COMMISSION.RESERVED6` | `FsGaBankCommission_Reserved6` | TField |  |  |
| 20 | `FS.GA.BANK.COMMISSION.RESERVED5` | `FsGaBankCommission_Reserved5` | TField |  |  |
| 21 | `FS.GA.BANK.COMMISSION.RESERVED4` | `FsGaBankCommission_Reserved4` | TField |  |  |
| 22 | `FS.GA.BANK.COMMISSION.RESERVED3` | `FsGaBankCommission_Reserved3` | TField |  |  |
| 23 | `FS.GA.BANK.COMMISSION.RESERVED2` | `FsGaBankCommission_Reserved2` | TField |  |  |
| 24 | `FS.GA.BANK.COMMISSION.RESERVED1` | `FsGaBankCommission_Reserved1` | TField |  |  |
| 25 | `FS.GA.BANK.COMMISSION.LOCAL.REF` | `FsGaBankCommission_LocalRef` |  |  |  |
| 26 | `FS.GA.BANK.COMMISSION.OVERRIDE` | `FsGaBankCommission_Override` |  |  |  |
| 27 | `FS.GA.BANK.COMMISSION.RECORD.STATUS` | `FsGaBankCommission_RecordStatus` | String |  |  |
| 28 | `FS.GA.BANK.COMMISSION.CURR.NO` | `FsGaBankCommission_CurrNo` | String |  |  |
| 29 | `FS.GA.BANK.COMMISSION.INPUTTER` | `FsGaBankCommission_Inputter` |  |  |  |
| 30 | `FS.GA.BANK.COMMISSION.DATE.TIME` | `FsGaBankCommission_DateTime` |  |  |  |
| 31 | `FS.GA.BANK.COMMISSION.AUTHORISER` | `FsGaBankCommission_Authoriser` | String |  |  |
| 32 | `FS.GA.BANK.COMMISSION.CO.CODE` | `FsGaBankCommission_CoCode` | String |  |  |
| 33 | `FS.GA.BANK.COMMISSION.DEPT.CODE` | `FsGaBankCommission_DeptCode` | String |  |  |
| 34 | `FS.GA.BANK.COMMISSION.AUDITOR.CODE` | `FsGaBankCommission_AuditorCode` | String |  |  |
| 35 | `FS.GA.BANK.COMMISSION.AUDIT.DATE.TIME` | `FsGaBankCommission_AuditDateTime` | String |  |  |
