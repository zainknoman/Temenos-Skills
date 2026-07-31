# FS.GA.CGT.CARRYFORWARD.BALANCE — Table Schema

> Source: `INSERTS/I_F.FS.GA.CGT.CARRYFORWARD.BALANCE` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CGT.CARRYFORWARD.BALANCE.FUND.ID` | `FsGaCgtCarryforwardBalance_FundId` |  |  |  |
| 2 | `FS.GA.CGT.CARRYFORWARD.BALANCE.CAPITAL.GAIN.TAX.CODE` | `FsGaCgtCarryforwardBalance_CapitalGainTaxCode` |  |  |  |
| 3 | `FS.GA.CGT.CARRYFORWARD.BALANCE.TAX.DOMICILE` | `FsGaCgtCarryforwardBalance_TaxDomicile` |  |  |  |
| 4 | `FS.GA.CGT.CARRYFORWARD.BALANCE.CURRENCY.CODE` | `FsGaCgtCarryforwardBalance_CurrencyCode` |  |  |  |
| 5 | `FS.GA.CGT.CARRYFORWARD.BALANCE.DATE.OF.NAV` | `FsGaCgtCarryforwardBalance_DateOfNav` |  |  |  |
| 6 | `FS.GA.CGT.CARRYFORWARD.BALANCE.TAX.PERIOD.BEGIN.DATE` | `FsGaCgtCarryforwardBalance_TaxPeriodBeginDate` |  |  |  |
| 7 | `FS.GA.CGT.CARRYFORWARD.BALANCE.TAX.PERIOD.END.DATE` | `FsGaCgtCarryforwardBalance_TaxPeriodEndDate` |  |  |  |
| 8 | `FS.GA.CGT.CARRYFORWARD.BALANCE.CF.LONG.TERM.CAPITAL.LOSS.STT` | `FsGaCgtCarryforwardBalance_CfLongTermCapitalLossStt` |  |  |  |
| 9 | `FS.GA.CGT.CARRYFORWARD.BALANCE.CF.LONG.TERM.CAPITAL.LOSS.NSTT` | `FsGaCgtCarryforwardBalance_CfLongTermCapitalLossNstt` |  |  |  |
| 10 | `FS.GA.CGT.CARRYFORWARD.BALANCE.CF.SHORT.TERM.CAPITAL.LOSS.STT` | `FsGaCgtCarryforwardBalance_CfShortTermCapitalLossStt` |  |  |  |
| 11 | `FS.GA.CGT.CARRYFORWARD.BALANCE.CF.ST.CAPITAL.LOSS.NSTT` | `FsGaCgtCarryforwardBalance_CfStCapitalLossNstt` |  |  |  |
| 12 | `FS.GA.CGT.CARRYFORWARD.BALANCE.BEFORE.LTCL.STT.ADJUST.AMOUNT` | `FsGaCgtCarryforwardBalance_BeforeLtclSttAdjustAmount` |  |  |  |
| 13 | `FS.GA.CGT.CARRYFORWARD.BALANCE.BEFORE.LTCL.NSTT.ADJUST.AMT` | `FsGaCgtCarryforwardBalance_BeforeLtclNsttAdjustAmt` |  |  |  |
| 14 | `FS.GA.CGT.CARRYFORWARD.BALANCE.BEFORE.STCL.STT.ADJUST.AMOUNT` | `FsGaCgtCarryforwardBalance_BeforeStclSttAdjustAmount` |  |  |  |
| 15 | `FS.GA.CGT.CARRYFORWARD.BALANCE.BEFORE.STCL.NSTT.ADJUST.AMT` | `FsGaCgtCarryforwardBalance_BeforeStclNsttAdjustAmt` |  |  |  |
| 16 | `FS.GA.CGT.CARRYFORWARD.BALANCE.FLAG.NAV.ACCOUNTING` | `FsGaCgtCarryforwardBalance_FlagNavAccounting` |  |  |  |
| 17 | `FS.GA.CGT.CARRYFORWARD.BALANCE.PROCESS.ID` | `FsGaCgtCarryforwardBalance_ProcessId` |  |  |  |
| 18 | `FS.GA.CGT.CARRYFORWARD.BALANCE.VALUATION.TYPE` | `FsGaCgtCarryforwardBalance_ValuationType` |  |  |  |
| 19 | `FS.GA.CGT.CARRYFORWARD.BALANCE.PROCESSING.DATE` | `FsGaCgtCarryforwardBalance_ProcessingDate` |  |  |  |
| 20 | `FS.GA.CGT.CARRYFORWARD.BALANCE.RESERVED10` | `FsGaCgtCarryforwardBalance_Reserved10` |  |  |  |
| 21 | `FS.GA.CGT.CARRYFORWARD.BALANCE.RESERVED9` | `FsGaCgtCarryforwardBalance_Reserved9` |  |  |  |
| 22 | `FS.GA.CGT.CARRYFORWARD.BALANCE.RESERVED8` | `FsGaCgtCarryforwardBalance_Reserved8` |  |  |  |
| 23 | `FS.GA.CGT.CARRYFORWARD.BALANCE.RESERVED7` | `FsGaCgtCarryforwardBalance_Reserved7` |  |  |  |
| 24 | `FS.GA.CGT.CARRYFORWARD.BALANCE.RESERVED6` | `FsGaCgtCarryforwardBalance_Reserved6` |  |  |  |
| 25 | `FS.GA.CGT.CARRYFORWARD.BALANCE.RESERVED5` | `FsGaCgtCarryforwardBalance_Reserved5` |  |  |  |
| 26 | `FS.GA.CGT.CARRYFORWARD.BALANCE.RESERVED4` | `FsGaCgtCarryforwardBalance_Reserved4` |  |  |  |
| 27 | `FS.GA.CGT.CARRYFORWARD.BALANCE.RESERVED3` | `FsGaCgtCarryforwardBalance_Reserved3` |  |  |  |
| 28 | `FS.GA.CGT.CARRYFORWARD.BALANCE.RESERVED2` | `FsGaCgtCarryforwardBalance_Reserved2` |  |  |  |
| 29 | `FS.GA.CGT.CARRYFORWARD.BALANCE.RESERVED1` | `FsGaCgtCarryforwardBalance_Reserved1` |  |  |  |
| 30 | `FS.GA.CGT.CARRYFORWARD.BALANCE.RECORD.STATUS` | `FsGaCgtCarryforwardBalance_RecordStatus` |  |  |  |
| 31 | `FS.GA.CGT.CARRYFORWARD.BALANCE.CURR.NO` | `FsGaCgtCarryforwardBalance_CurrNo` |  |  |  |
| 32 | `FS.GA.CGT.CARRYFORWARD.BALANCE.INPUTTER` | `FsGaCgtCarryforwardBalance_Inputter` |  |  |  |
| 33 | `FS.GA.CGT.CARRYFORWARD.BALANCE.DATE.TIME` | `FsGaCgtCarryforwardBalance_DateTime` |  |  |  |
| 34 | `FS.GA.CGT.CARRYFORWARD.BALANCE.AUTHORISER` | `FsGaCgtCarryforwardBalance_Authoriser` |  |  |  |
| 35 | `FS.GA.CGT.CARRYFORWARD.BALANCE.CO.CODE` | `FsGaCgtCarryforwardBalance_CoCode` |  |  |  |
| 36 | `FS.GA.CGT.CARRYFORWARD.BALANCE.DEPT.CODE` | `FsGaCgtCarryforwardBalance_DeptCode` |  |  |  |
| 37 | `FS.GA.CGT.CARRYFORWARD.BALANCE.AUDITOR.CODE` | `FsGaCgtCarryforwardBalance_AuditorCode` |  |  |  |
| 38 | `FS.GA.CGT.CARRYFORWARD.BALANCE.AUDIT.DATE.TIME` | `FsGaCgtCarryforwardBalance_AuditDateTime` |  |  |  |
