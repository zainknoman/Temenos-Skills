# ACCR.REV.PARAM — Table Schema

> Source: `INSERTS/I_F.ACCR.REV.PARAM` in `AC_Fees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARP.REVERSE.FCY` | `AccrRevParam_ReverseFcy` | TField |  | Reversal Accrual processing for foreign currency contracts. Valid options YES or NO. |
| 2 | `ARP.REVERSAL.RATE` | `AccrRevParam_ReversalRate` | TField |  | Mondatory field if REVERSE.FCY is YES. Valid options are TODAY or YDAY. TODAY = Reversal entry using todays exchange rate. YDAY = Reverse using the exchange rate that was used to posted the accrual. |
| 3 | `ARP.REVERSE.LCY` | `AccrRevParam_ReverseLcy` | TField |  | Reversal Accrual processing for Local currency contracts. Valid options YES or NO. |
| 4 | `ARP.SYSTEM.IND` | `AccrRevParam_SystemInd` |  |  |  |
| 5 | `ARP.PL.CATEGORY` | `AccrRevParam_PlCategory` |  |  |  |
| 6 | `ARP.LINK.PL.CAT` | `AccrRevParam_LinkPlCat` |  |  |  |
| 7 | `ARP.OPP.TYPE` | `AccrRevParam_OppType` |  |  |  |
| 8 | `ARP.RESERVED14` | `AccrRevParam_Reserved14` |  |  |  |
| 9 | `ARP.RESERVED13` | `AccrRevParam_Reserved13` |  |  |  |
| 10 | `ARP.APP.CASH.TXN.CODE` | `AccrRevParam_AppCashTxnCode` |  |  |  |
| 11 | `ARP.RESERVED11` | `AccrRevParam_Reserved11` |  |  |  |
| 12 | `ARP.REBUILD.IND.FCY` | `AccrRevParam_RebuildIndFcy` | TField |  | No input field. If REVERSE.FCY changes then this field is updated by the system. |
| 13 | `ARP.REBUILD.IND.LCY` | `AccrRevParam_RebuildIndLcy` | TField |  | No input field. If REVERSE.LCY changes then this field is updated by the system. |
| 14 | `ARP.CASH.TXN.CODE` | `AccrRevParam_CashTxnCode` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 15 | `ARP.RESERVED09` | `AccrRevParam_Reserved09` | TField |  |  |
| 16 | `ARP.RESERVED08` | `AccrRevParam_Reserved08` | TField |  |  |
| 17 | `ARP.RESERVED07` | `AccrRevParam_Reserved07` | TField |  |  |
| 18 | `ARP.RESERVED06` | `AccrRevParam_Reserved06` | TField |  |  |
| 19 | `ARP.RESERVED05` | `AccrRevParam_Reserved05` | TField |  |  |
| 20 | `ARP.RESERVED04` | `AccrRevParam_Reserved04` | TField |  |  |
| 21 | `ARP.RESERVED03` | `AccrRevParam_Reserved03` | TField |  |  |
| 22 | `ARP.RESERVED02` | `AccrRevParam_Reserved02` | TField |  |  |
| 23 | `ARP.RESERVED01` | `AccrRevParam_Reserved01` | TField |  |  |
| 24 | `ARP.RECORD.STATUS` | `AccrRevParam_RecordStatus` | String |  |  |
| 25 | `ARP.CURR.NO` | `AccrRevParam_CurrNo` | String |  |  |
| 26 | `ARP.INPUTTER` | `AccrRevParam_Inputter` |  |  |  |
| 27 | `ARP.DATE.TIME` | `AccrRevParam_DateTime` |  |  |  |
| 28 | `ARP.AUTHORISER` | `AccrRevParam_Authoriser` | String |  |  |
| 29 | `ARP.CO.CODE` | `AccrRevParam_CoCode` | String |  |  |
| 30 | `ARP.DEPT.CODE` | `AccrRevParam_DeptCode` | String |  |  |
| 31 | `ARP.AUDITOR.CODE` | `AccrRevParam_AuditorCode` | String |  |  |
| 32 | `ARP.AUDIT.DATE.TIME` | `AccrRevParam_AuditDateTime` | String |  |  |
