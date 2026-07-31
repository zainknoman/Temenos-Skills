# NSF.PARAMETER — Table Schema

> Source: `INSERTS/I_F.NSF.PARAMETER` in `AC_NSF.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NSF.PARAM.ORDER` | `NsfParameter_Order` | TField | No | This indicates the order in which the entries for the day would be evalueted during end of day processing Validation Rule: This is a optional field CreditDebit - Default option if not defined by user. Evaluation would take place by posting all credit entries first then followed by bank initiated debits followed by customer initiated debits. Time - Evaluation would take place by posting entries in the same order they were raised. |
| 2 | `NSF.PARAM.SETTLE.TYPE` | `NsfParameter_SettleType` |  |  |  |
| 3 | `NSF.PARAM.EXPIRY.DAYS` | `NsfParameter_ExpiryDays` |  |  |  |
| 4 | `NSF.PARAM.DEF.FUND.DECISION` | `NsfParameter_DefFundDecision` |  |  |  |
| 5 | `NSF.PARAM.FUND.DECISION.UPD` | `NsfParameter_FundDecisionUpd` |  |  |  |
| 6 | `NSF.PARAM.FUND.DECI.APPROVE.ACT` | `NsfParameter_FundDeciApproveAct` |  |  |  |
| 7 | `NSF.PARAM.FUND.DECI.REJ.ACT` | `NsfParameter_FundDeciRejAct` |  |  |  |
| 8 | `NSF.PARAM.REV.APPROVE.ACT` | `NsfParameter_RevApproveAct` |  |  |  |
| 9 | `NSF.PARAM.REV.REJ.ACT` | `NsfParameter_RevRejAct` |  |  |  |
| 10 | `NSF.PARAM.CHRG.NEGOTIABLE` | `NsfParameter_ChrgNegotiable` |  |  |  |
| 11 | `NSF.PARAM.FUND.RES.REQ.FEE` | `NsfParameter_FundResReqFee` |  |  |  |
| 12 | `NSF.PARAM.RESERVED.10` | `NsfParameter_Reserved10` |  |  |  |
| 13 | `NSF.PARAM.RESERVED.9` | `NsfParameter_Reserved9` |  |  |  |
| 14 | `NSF.PARAM.RESERVED.8` | `NsfParameter_Reserved8` |  |  |  |
| 15 | `NSF.PARAM.RESERVED.7` | `NsfParameter_Reserved7` |  |  |  |
| 16 | `NSF.PARAM.RESERVED.6` | `NsfParameter_Reserved6` |  |  |  |
| 17 | `NSF.PARAM.RESERVED.5` | `NsfParameter_Reserved5` |  |  |  |
| 18 | `NSF.PARAM.RESERVED.4` | `NsfParameter_Reserved4` |  |  |  |
| 19 | `NSF.PARAM.RESERVED.3` | `NsfParameter_Reserved3` |  |  |  |
| 20 | `NSF.PARAM.RESERVED.2` | `NsfParameter_Reserved2` |  |  |  |
| 21 | `NSF.PARAM.RESERVED.1` | `NsfParameter_Reserved1` |  |  |  |
| 22 | `NSF.PARAM.LOCAL.REF` | `NsfParameter_LocalRef` |  |  |  |
| 23 | `NSF.PARAM.OVERRIDE` | `NsfParameter_Override` |  |  |  |
| 24 | `NSF.PARAM.RECORD.STATUS` | `NsfParameter_RecordStatus` | String |  |  |
| 25 | `NSF.PARAM.CURR.NO` | `NsfParameter_CurrNo` | String |  |  |
| 26 | `NSF.PARAM.INPUTTER` | `NsfParameter_Inputter` |  |  |  |
| 27 | `NSF.PARAM.DATE.TIME` | `NsfParameter_DateTime` |  |  |  |
| 28 | `NSF.PARAM.AUTHORISER` | `NsfParameter_Authoriser` | String |  |  |
| 29 | `NSF.PARAM.CO.CODE` | `NsfParameter_CoCode` | String |  |  |
| 30 | `NSF.PARAM.DEPT.CODE` | `NsfParameter_DeptCode` | String |  |  |
| 31 | `NSF.PARAM.AUDITOR.CODE` | `NsfParameter_AuditorCode` | String |  |  |
| 32 | `NSF.PARAM.AUDIT.DATE.TIME` | `NsfParameter_AuditDateTime` | String |  |  |
| 33 | `NSF.PARAM.AC.NSF.REFUND.HANDOFF` | `NsfParameter_AcNsfRefundHandoff` | TField |  |  |
| 34 | `NSF.PARAM.NSF.DECISION.HOOK` | `NsfParameter_NsfDecisionHook` | TField | No | Hook routine field to override the NSF decision. The hook routine can do the following Update an NSF Entry as Non-NSF Entry - Flag Update the Overdraft Amount for each entry - Only reduce the overdraft amount or mark as zero Update the Settlement Type for each entry - Should be either POL, PTL or SET only. Optional field. |
