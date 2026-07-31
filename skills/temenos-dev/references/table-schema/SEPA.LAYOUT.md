# SEPA.LAYOUT — Table Schema

> Source: `INSERTS/I_F.SEPA.LAYOUT` in `EP_Layout.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.LAY.DESCRIPTION` | `SepaLayout_Description` | TField |  |  |
| 2 | `SEP.LAY.MSG.NATURE` | `SepaLayout_MsgNature` | TField |  |  |
| 3 | `SEP.LAY.SENDER.RECEIVER` | `SepaLayout_SenderReceiver` | TField |  |  |
| 4 | `SEP.LAY.PURPOSE` | `SepaLayout_Purpose` | TField |  |  |
| 5 | `SEP.LAY.TRANSACTION.TYPE` | `SepaLayout_TransactionType` | TField |  |  |
| 6 | `SEP.LAY.CUSTOMER.SIGN` | `SepaLayout_CustomerSign` | TField |  |  |
| 7 | `SEP.LAY.PROCESS.TYPE` | `SepaLayout_ProcessType` | TField |  |  |
| 8 | `SEP.LAY.COMMISSION.CODE` | `SepaLayout_CommissionCode` | TField |  |  |
| 9 | `SEP.LAY.CHARGE.CODE` | `SepaLayout_ChargeCode` | TField |  |  |
| 10 | `SEP.LAY.NOSTRO.ACCT.NO` | `SepaLayout_NostroAcctNo` | TField |  |  |
| 11 | `SEP.LAY.TRANSIT.ACCT.NO` | `SepaLayout_TransitAcctNo` | TField |  |  |
| 12 | `SEP.LAY.SUSPENS.ACCT.NO` | `SepaLayout_SuspensAcctNo` | TField |  |  |
| 13 | `SEP.LAY.OFFSET.ACCT.NO` | `SepaLayout_OffsetAcctNo` | TField |  |  |
| 14 | `SEP.LAY.VALIDATION.RTN` | `SepaLayout_ValidationRtn` |  |  |  |
| 15 | `SEP.LAY.AFTER.AUTH.RTN` | `SepaLayout_AfterAuthRtn` |  |  |  |
| 16 | `SEP.LAY.CUT.OFF.TIME.DESC` | `SepaLayout_CutOffTimeDesc` |  |  |  |
| 17 | `SEP.LAY.SETTLEMENT.DAYS` | `SepaLayout_SettlementDays` |  |  |  |
| 18 | `SEP.LAY.TIME.FROM` | `SepaLayout_TimeFrom` |  |  |  |
| 19 | `SEP.LAY.TIME.TILL` | `SepaLayout_TimeTill` |  |  |  |
| 20 | `SEP.LAY.REDUCTION.ALLOWED` | `SepaLayout_ReductionAllowed` | TField |  |  |
| 21 | `SEP.LAY.MAPPING.KEY` | `SepaLayout_MappingKey` | TField |  |  |
| 22 | `SEP.LAY.APPLICATION.FORMAT` | `SepaLayout_ApplicationFormat` | TField |  |  |
| 23 | `SEP.LAY.DELIVERY.ROUTINE` | `SepaLayout_DeliveryRoutine` | TField |  |  |
| 24 | `SEP.LAY.PREVIOUS.OPER` | `SepaLayout_PreviousOper` |  |  |  |
| 25 | `SEP.LAY.REJECT.OPER` | `SepaLayout_RejectOper` | TField |  |  |
| 26 | `SEP.LAY.REVERSE.OPER` | `SepaLayout_ReverseOper` | TField |  |  |
| 27 | `SEP.LAY.RETURN.OPER` | `SepaLayout_ReturnOper` | TField |  |  |
| 28 | `SEP.LAY.REFUND.OPER` | `SepaLayout_RefundOper` | TField |  |  |
| 29 | `SEP.LAY.CANCEL.OPER` | `SepaLayout_CancelOper` | TField |  |  |
| 30 | `SEP.LAY.GENERATED.OPER` | `SepaLayout_GeneratedOper` |  |  |  |
| 31 | `SEP.LAY.GENERATED.OPER.RTN` | `SepaLayout_GeneratedOperRtn` |  |  |  |
| 32 | `SEP.LAY.ANSWER.POSSIBLE.RTN` | `SepaLayout_AnswerPossibleRtn` | TField |  |  |
| 33 | `SEP.LAY.CB.FILE.POSTING` | `SepaLayout_CbFilePosting` | TField |  |  |
| 34 | `SEP.LAY.CUT.OFF.TIME.LEVL` | `SepaLayout_CutOffTimeLevl` | TField |  |  |
| 35 | `SEP.LAY.FT.VERSION` | `SepaLayout_FtVersion` | TField |  |  |
| 36 | `SEP.LAY.FUP.VERSION` | `SepaLayout_FupVersion` | TField |  |  |
| 37 | `SEP.LAY.RESERVED.12` | `SepaLayout_Reserved12` | TField |  |  |
| 38 | `SEP.LAY.RESERVED.11` | `SepaLayout_Reserved11` | TField |  |  |
| 39 | `SEP.LAY.RESERVED.10` | `SepaLayout_Reserved10` | TField |  |  |
| 40 | `SEP.LAY.RESERVED.9` | `SepaLayout_Reserved9` | TField |  |  |
| 41 | `SEP.LAY.RESERVED.8` | `SepaLayout_Reserved8` | TField |  |  |
| 42 | `SEP.LAY.RESERVED.7` | `SepaLayout_Reserved7` | TField |  |  |
| 43 | `SEP.LAY.RESERVED.6` | `SepaLayout_Reserved6` | TField |  |  |
| 44 | `SEP.LAY.RESERVED.5` | `SepaLayout_Reserved5` | TField |  |  |
| 45 | `SEP.LAY.UNIFI.XML.MSG.ID` | `SepaLayout_UnifiXmlMsgId` | TField |  |  |
| 46 | `SEP.LAY.FIELD.TAG.ID` | `SepaLayout_FieldTagId` |  |  |  |
| 47 | `SEP.LAY.FIELD.TAG.OCCUR` | `SepaLayout_FieldTagOccur` |  |  |  |
| 48 | `SEP.LAY.FIELD.TAG.ALTER` | `SepaLayout_FieldTagAlter` |  |  |  |
| 49 | `SEP.LAY.FIELD.NAME` | `SepaLayout_FieldName` |  |  |  |
| 50 | `SEP.LAY.FIELD.FORMAT` | `SepaLayout_FieldFormat` |  |  |  |
| 51 | `SEP.LAY.FIELD.DETAIL` | `SepaLayout_FieldDetail` |  |  |  |
| 52 | `SEP.LAY.FIELD.EXTRCT` | `SepaLayout_FieldExtrct` |  |  |  |
| 53 | `SEP.LAY.FIELD.ARCHVE` | `SepaLayout_FieldArchve` |  |  |  |
| 54 | `SEP.LAY.PEACH.ID` | `SepaLayout_PeachId` |  |  |  |
| 55 | `SEP.LAY.RESERVED.3` | `SepaLayout_Reserved3` | TField |  |  |
| 56 | `SEP.LAY.RESERVED.2` | `SepaLayout_Reserved2` | TField |  |  |
| 57 | `SEP.LAY.RESERVED.1` | `SepaLayout_Reserved1` | TField |  |  |
| 58 | `SEP.LAY.LOCAL.REF` | `SepaLayout_LocalRef` |  |  |  |
| 59 | `SEP.LAY.OVERRIDE` | `SepaLayout_Override` |  |  |  |
| 60 | `SEP.LAY.RECORD.STATUS` | `SepaLayout_RecordStatus` | String |  |  |
| 61 | `SEP.LAY.CURR.NO` | `SepaLayout_CurrNo` | String |  |  |
| 62 | `SEP.LAY.INPUTTER` | `SepaLayout_Inputter` |  |  |  |
| 63 | `SEP.LAY.DATE.TIME` | `SepaLayout_DateTime` |  |  |  |
| 64 | `SEP.LAY.AUTHORISER` | `SepaLayout_Authoriser` | String |  |  |
| 65 | `SEP.LAY.CO.CODE` | `SepaLayout_CoCode` | String |  |  |
| 66 | `SEP.LAY.DEPT.CODE` | `SepaLayout_DeptCode` | String |  |  |
| 67 | `SEP.LAY.AUDITOR.CODE` | `SepaLayout_AuditorCode` | String |  |  |
| 68 | `SEP.LAY.AUDIT.DATE.TIME` | `SepaLayout_AuditDateTime` | String |  |  |
