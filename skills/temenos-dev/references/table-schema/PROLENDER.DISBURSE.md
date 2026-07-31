# PROLENDER.DISBURSE — Table Schema

> Source: `INSERTS/I_F.PROLENDER.DISBURSE` in `CAPLND_ProlenderInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PRL.DIS.REQ` | `ProlenderDisburse_Req` |  |  |  |
| 2 | `PRL.DIS.DESCRIPTION` | `ProlenderDisburse_Description` |  |  |  |
| 3 | `PRL.DIS.CUID` | `ProlenderDisburse_Cuid` |  |  |  |
| 4 | `PRL.DIS.USERID` | `ProlenderDisburse_Userid` |  |  |  |
| 5 | `PRL.DIS.PASSWORD` | `ProlenderDisburse_Password` |  |  |  |
| 6 | `PRL.DIS.REQUEST.ID` | `ProlenderDisburse_RequestId` |  |  |  |
| 7 | `PRL.DIS.TIME.STAMP` | `ProlenderDisburse_TimeStamp` |  |  |  |
| 8 | `PRL.DIS.STATUS.CODE` | `ProlenderDisburse_StatusCode` |  |  |  |
| 9 | `PRL.DIS.ENTITY.TYPE` | `ProlenderDisburse_EntityType` |  |  |  |
| 10 | `PRL.DIS.MESSAGE.CODE` | `ProlenderDisburse_MessageCode` |  |  |  |
| 11 | `PRL.DIS.MESSAGE.TEXT` | `ProlenderDisburse_MessageText` |  |  |  |
| 12 | `PRL.DIS.CUSTOMER` | `ProlenderDisburse_Customer` |  |  |  |
| 13 | `PRL.DIS.LOAN.NO` | `ProlenderDisburse_LoanNo` |  |  |  |
| 14 | `PRL.DIS.LOAN.PRINCIPAL` | `ProlenderDisburse_LoanPrincipal` |  |  |  |
| 15 | `PRL.DIS.FIN.SP.PREMIUM` | `ProlenderDisburse_FinSpPremium` |  |  |  |
| 16 | `PRL.DIS.FIN.PREMIUM` | `ProlenderDisburse_FinPremium` |  |  |  |
| 17 | `PRL.DIS.ACCOUNT.NO` | `ProlenderDisburse_AccountNo` |  |  |  |
| 18 | `PRL.DIS.ACCOUNT.NO.CR` | `ProlenderDisburse_AccountNoCr` |  |  |  |
| 19 | `PRL.DIS.GL.NO` | `ProlenderDisburse_GlNo` |  |  |  |
| 20 | `PRL.DIS.TXN.CODE` | `ProlenderDisburse_TxnCode` |  |  |  |
| 21 | `PRL.DIS.TXN.AMOUNT` | `ProlenderDisburse_TxnAmount` |  |  |  |
| 22 | `PRL.DIS.PAYEE.ON.MTA` | `ProlenderDisburse_PayeeOnMta` |  |  |  |
| 23 | `PRL.DIS.MISC.TYPE` | `ProlenderDisburse_MiscType` |  |  |  |
| 24 | `PRL.DIS.MISC.VAL` | `ProlenderDisburse_MiscVal` |  |  |  |
| 25 | `PRL.DIS.EFFECTIVE.DATE` | `ProlenderDisburse_EffectiveDate` |  |  |  |
| 26 | `PRL.DIS.RESERVED.10` | `ProlenderDisburse_Reserved10` |  |  |  |
| 27 | `PRL.DIS.RESERVED.9` | `ProlenderDisburse_Reserved9` |  |  |  |
| 28 | `PRL.DIS.RESERVED.8` | `ProlenderDisburse_Reserved8` |  |  |  |
| 29 | `PRL.DIS.RESERVED.7` | `ProlenderDisburse_Reserved7` |  |  |  |
| 30 | `PRL.DIS.RESERVED.6` | `ProlenderDisburse_Reserved6` |  |  |  |
| 31 | `PRL.DIS.RESERVED.5` | `ProlenderDisburse_Reserved5` |  |  |  |
| 32 | `PRL.DIS.RESERVED.4` | `ProlenderDisburse_Reserved4` |  |  |  |
| 33 | `PRL.DIS.RESERVED.3` | `ProlenderDisburse_Reserved3` |  |  |  |
| 34 | `PRL.DIS.RESERVED.2` | `ProlenderDisburse_Reserved2` |  |  |  |
| 35 | `PRL.DIS.RESERVED.1` | `ProlenderDisburse_Reserved1` |  |  |  |
| 36 | `PRL.DIS.LOCAL.REF` | `ProlenderDisburse_LocalRef` |  |  |  |
| 37 | `PRL.DIS.RECORD.STATUS` | `ProlenderDisburse_RecordStatus` |  |  |  |
| 38 | `PRL.DIS.CURR.NO` | `ProlenderDisburse_CurrNo` |  |  |  |
| 39 | `PRL.DIS.INPUTTER` | `ProlenderDisburse_Inputter` |  |  |  |
| 40 | `PRL.DIS.DATE.TIME` | `ProlenderDisburse_DateTime` |  |  |  |
| 41 | `PRL.DIS.AUTHORISER` | `ProlenderDisburse_Authoriser` |  |  |  |
| 42 | `PRL.DIS.CO.CODE` | `ProlenderDisburse_CoCode` |  |  |  |
| 43 | `PRL.DIS.DEPT.CODE` | `ProlenderDisburse_DeptCode` |  |  |  |
| 44 | `PRL.DIS.AUDITOR.CODE` | `ProlenderDisburse_AuditorCode` |  |  |  |
| 45 | `PRL.DIS.AUDIT.DATE.TIME` | `ProlenderDisburse_AuditDateTime` |  |  |  |
