# FS.GA.ANTICIPATED.REDEMPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.ANTICIPATED.REDEMPTION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ANTICIPATED.REDEMPTION.PARENT.REF.ID` | `FsGaAnticipatedRedemption_ParentRefId` |  |  |  |
| 2 | `FS.GA.ANTICIPATED.REDEMPTION.ORA.ROWID` | `FsGaAnticipatedRedemption_OraRowid` |  |  |  |
| 3 | `FS.GA.ANTICIPATED.REDEMPTION.INTERNAL.SECURITY.ID` | `FsGaAnticipatedRedemption_InternalSecurityId` |  |  |  |
| 4 | `FS.GA.ANTICIPATED.REDEMPTION.REDEMPTION.DATE.SECURITY` | `FsGaAnticipatedRedemption_RedemptionDateSecurity` |  |  |  |
| 5 | `FS.GA.ANTICIPATED.REDEMPTION.REDEMPTION.PERCENT` | `FsGaAnticipatedRedemption_RedemptionPercent` |  |  |  |
| 6 | `FS.GA.ANTICIPATED.REDEMPTION.MATURITY.REPAYMENT.PRICE` | `FsGaAnticipatedRedemption_MaturityRepaymentPrice` |  |  |  |
| 7 | `FS.GA.ANTICIPATED.REDEMPTION.REDEMPTION.CCY` | `FsGaAnticipatedRedemption_RedemptionCcy` |  |  |  |
| 8 | `FS.GA.ANTICIPATED.REDEMPTION.REDEMPTION.TYPE` | `FsGaAnticipatedRedemption_RedemptionType` |  |  |  |
| 9 | `FS.GA.ANTICIPATED.REDEMPTION.REDEMPTION` | `FsGaAnticipatedRedemption_Redemption` |  |  |  |
| 10 | `FS.GA.ANTICIPATED.REDEMPTION.FUND.ID` | `FsGaAnticipatedRedemption_FundId` |  |  |  |
| 11 | `FS.GA.ANTICIPATED.REDEMPTION.CALL.AMOUNT.IDENTIFIER` | `FsGaAnticipatedRedemption_CallAmountIdentifier` |  |  |  |
| 12 | `FS.GA.ANTICIPATED.REDEMPTION.DATE.OF.EFFECTIVE` | `FsGaAnticipatedRedemption_DateOfEffective` |  |  |  |
| 13 | `FS.GA.ANTICIPATED.REDEMPTION.FIXED.AMOUNT.PER.1000` | `FsGaAnticipatedRedemption_FixedAmountPer1000` |  |  |  |
| 14 | `FS.GA.ANTICIPATED.REDEMPTION.PAY.DATE` | `FsGaAnticipatedRedemption_PayDate` |  |  |  |
| 15 | `FS.GA.ANTICIPATED.REDEMPTION.RESERVED10` | `FsGaAnticipatedRedemption_Reserved10` |  |  |  |
| 16 | `FS.GA.ANTICIPATED.REDEMPTION.RESERVED9` | `FsGaAnticipatedRedemption_Reserved9` |  |  |  |
| 17 | `FS.GA.ANTICIPATED.REDEMPTION.RESERVED8` | `FsGaAnticipatedRedemption_Reserved8` |  |  |  |
| 18 | `FS.GA.ANTICIPATED.REDEMPTION.RESERVED7` | `FsGaAnticipatedRedemption_Reserved7` |  |  |  |
| 19 | `FS.GA.ANTICIPATED.REDEMPTION.RESERVED6` | `FsGaAnticipatedRedemption_Reserved6` |  |  |  |
| 20 | `FS.GA.ANTICIPATED.REDEMPTION.RESERVED5` | `FsGaAnticipatedRedemption_Reserved5` |  |  |  |
| 21 | `FS.GA.ANTICIPATED.REDEMPTION.RESERVED4` | `FsGaAnticipatedRedemption_Reserved4` |  |  |  |
| 22 | `FS.GA.ANTICIPATED.REDEMPTION.RESERVED3` | `FsGaAnticipatedRedemption_Reserved3` |  |  |  |
| 23 | `FS.GA.ANTICIPATED.REDEMPTION.RESERVED2` | `FsGaAnticipatedRedemption_Reserved2` |  |  |  |
| 24 | `FS.GA.ANTICIPATED.REDEMPTION.RESERVED1` | `FsGaAnticipatedRedemption_Reserved1` |  |  |  |
| 25 | `FS.GA.ANTICIPATED.REDEMPTION.LOCAL.REF` | `FsGaAnticipatedRedemption_LocalRef` |  |  |  |
| 26 | `FS.GA.ANTICIPATED.REDEMPTION.OVERRIDE` | `FsGaAnticipatedRedemption_Override` |  |  |  |
| 27 | `FS.GA.ANTICIPATED.REDEMPTION.RECORD.STATUS` | `FsGaAnticipatedRedemption_RecordStatus` |  |  |  |
| 28 | `FS.GA.ANTICIPATED.REDEMPTION.CURR.NO` | `FsGaAnticipatedRedemption_CurrNo` |  |  |  |
| 29 | `FS.GA.ANTICIPATED.REDEMPTION.INPUTTER` | `FsGaAnticipatedRedemption_Inputter` |  |  |  |
| 30 | `FS.GA.ANTICIPATED.REDEMPTION.DATE.TIME` | `FsGaAnticipatedRedemption_DateTime` |  |  |  |
| 31 | `FS.GA.ANTICIPATED.REDEMPTION.AUTHORISER` | `FsGaAnticipatedRedemption_Authoriser` |  |  |  |
| 32 | `FS.GA.ANTICIPATED.REDEMPTION.CO.CODE` | `FsGaAnticipatedRedemption_CoCode` |  |  |  |
| 33 | `FS.GA.ANTICIPATED.REDEMPTION.DEPT.CODE` | `FsGaAnticipatedRedemption_DeptCode` |  |  |  |
| 34 | `FS.GA.ANTICIPATED.REDEMPTION.AUDITOR.CODE` | `FsGaAnticipatedRedemption_AuditorCode` |  |  |  |
| 35 | `FS.GA.ANTICIPATED.REDEMPTION.AUDIT.DATE.TIME` | `FsGaAnticipatedRedemption_AuditDateTime` |  |  |  |
