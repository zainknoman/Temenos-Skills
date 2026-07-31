# ATM.SPLIT.CHG.TABLE — Table Schema

> Source: `INSERTS/I_F.ATM.SPLIT.CHG.TABLE` in `ATMFRM_Charges.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AT.CSP.DESCRIPTION` | `AtmSplitChgTable_Description` |  |  |  |
| 2 | `AT.CSP.CHARGE.DESC` | `AtmSplitChgTable_ChargeDesc` |  |  |  |
| 3 | `AT.CSP.CHARGE.TYPE` | `AtmSplitChgTable_ChargeType` |  |  |  |
| 4 | `AT.CSP.CHG.TXN.CCY` | `AtmSplitChgTable_ChgTxnCcy` |  |  |  |
| 5 | `AT.CSP.CHG.AMT` | `AtmSplitChgTable_ChgAmt` |  |  |  |
| 6 | `AT.CSP.CHG.PERC` | `AtmSplitChgTable_ChgPerc` |  |  |  |
| 7 | `AT.CSP.DR.ACCT.TYPE` | `AtmSplitChgTable_DrAcctType` |  |  |  |
| 8 | `AT.CSP.CHG.DR.ACCT` | `AtmSplitChgTable_ChgDrAcct` |  |  |  |
| 9 | `AT.CSP.CHG.CR.ACCT` | `AtmSplitChgTable_ChgCrAcct` |  |  |  |
| 10 | `AT.CSP.RESERVED.4` | `AtmSplitChgTable_Reserved4` |  |  |  |
| 11 | `AT.CSP.RESERVED.3` | `AtmSplitChgTable_Reserved3` |  |  |  |
| 12 | `AT.CSP.RESERVED.2` | `AtmSplitChgTable_Reserved2` |  |  |  |
| 13 | `AT.CSP.RESERVED.1` | `AtmSplitChgTable_Reserved1` |  |  |  |
| 14 | `AT.CSP.LOCAL.REF` | `AtmSplitChgTable_LocalRef` |  |  |  |
| 15 | `AT.CSP.RESERVED.10` | `AtmSplitChgTable_Reserved10` | TField |  |  |
| 16 | `AT.CSP.RESERVED.9` | `AtmSplitChgTable_Reserved9` | TField |  |  |
| 17 | `AT.CSP.RESERVED.8` | `AtmSplitChgTable_Reserved8` | TField |  |  |
| 18 | `AT.CSP.RESERVED.7` | `AtmSplitChgTable_Reserved7` | TField |  |  |
| 19 | `AT.CSP.RESERVED.6` | `AtmSplitChgTable_Reserved6` | TField |  |  |
| 20 | `AT.CSP.RESERVED.5` | `AtmSplitChgTable_Reserved5` | TField |  |  |
| 21 | `AT.CSP.RECORD.STATUS` | `AtmSplitChgTable_RecordStatus` | String |  |  |
| 22 | `AT.CSP.CURR.NO` | `AtmSplitChgTable_CurrNo` | String |  |  |
| 23 | `AT.CSP.INPUTTER` | `AtmSplitChgTable_Inputter` |  |  |  |
| 24 | `AT.CSP.DATE.TIME` | `AtmSplitChgTable_DateTime` |  |  |  |
| 25 | `AT.CSP.AUTHORISER` | `AtmSplitChgTable_Authoriser` | String |  |  |
| 26 | `AT.CSP.CO.CODE` | `AtmSplitChgTable_CoCode` | String |  |  |
| 27 | `AT.CSP.DEPT.CODE` | `AtmSplitChgTable_DeptCode` | String |  |  |
| 28 | `AT.CSP.AUDITOR.CODE` | `AtmSplitChgTable_AuditorCode` | String |  |  |
| 29 | `AT.CSP.AUDIT.DATE.TIME` | `AtmSplitChgTable_AuditDateTime` | String |  |  |
