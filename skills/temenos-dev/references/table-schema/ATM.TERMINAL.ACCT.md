# ATM.TERMINAL.ACCT — Table Schema

> Source: `INSERTS/I_F.ATM.TERMINAL.ACCT` in `ATMFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ATM.TERM.DESCRIPTION` | `AtmTerminalAcct_Description` |  |  |  |
| 2 | `ATM.TERM.PROC.CODE` | `AtmTerminalAcct_ProcCode` |  |  |  |
| 3 | `ATM.TERM.ACCT.CCY` | `AtmTerminalAcct_AcctCcy` |  |  |  |
| 4 | `ATM.TERM.PAY.ACCT` | `AtmTerminalAcct_PayAcct` |  |  |  |
| 5 | `ATM.TERM.RECV.ACCT` | `AtmTerminalAcct_RecvAcct` |  |  |  |
| 6 | `ATM.TERM.PAY.CATEGORY` | `AtmTerminalAcct_PayCategory` |  |  |  |
| 7 | `ATM.TERM.RECEIVE.CATEGORY` | `AtmTerminalAcct_ReceiveCategory` |  |  |  |
| 8 | `ATM.TERM.ACCT.TYPE` | `AtmTerminalAcct_AcctType` |  |  |  |
| 9 | `ATM.TERM.DEF.PAY.ACCT` | `AtmTerminalAcct_DefPayAcct` |  |  |  |
| 10 | `ATM.TERM.DEF.PAY.ACCT.CCY` | `AtmTerminalAcct_DefPayAcctCcy` |  |  |  |
| 11 | `ATM.TERM.DEF.RECV.ACCT` | `AtmTerminalAcct_DefRecvAcct` |  |  |  |
| 12 | `ATM.TERM.DEF.RECV.ACCT.CCY` | `AtmTerminalAcct_DefRecvAcctCcy` |  |  |  |
| 13 | `ATM.TERM.DEFAULT.PAY.CATEGORY` | `AtmTerminalAcct_DefaultPayCategory` | TField |  | category code defined here is used to post contra entry based on transaction currency/cardholder currency.This category is used if USE.DEF.ACCT is set to Yes. |
| 14 | `ATM.TERM.DEFAULT.RECEIVE.CATEGORY` | `AtmTerminalAcct_DefaultReceiveCategory` | TField |  | Category code defined here is used to frame default receive account based on transaction currency/card holder currency. Category defined here is used only when USE.DEF.ACCT is set to Yes. |
| 15 | `ATM.TERM.DEF.ACCT.TYPE` | `AtmTerminalAcct_DefAcctType` |  |  |  |
| 16 | `ATM.TERM.RESERVED.14` | `AtmTerminalAcct_Reserved14` | TField |  |  |
| 17 | `ATM.TERM.RESERVED.13` | `AtmTerminalAcct_Reserved13` | TField |  |  |
| 18 | `ATM.TERM.RESERVED.12` | `AtmTerminalAcct_Reserved12` | TField |  |  |
| 19 | `ATM.TERM.RESERVED.11` | `AtmTerminalAcct_Reserved11` | TField |  |  |
| 20 | `ATM.TERM.USE.DEF.ACCT` | `AtmTerminalAcct_UseDefAcct` | TField |  | If set to YES, account stored in DEF.PAY.ACCT or DEF.RECV.ACCT will be used. If set to NO, account stored based on currency and the processing code will be proceeded(which is from PAY.ACCT or RECV.ACCT) |
| 21 | `ATM.TERM.CUSTOMER` | `AtmTerminalAcct_Customer` | TField |  | Field to capture the T24 customer number linked to the terminal/POS ID. For information purpose only |
| 22 | `ATM.TERM.COMPANY.CODE` | `AtmTerminalAcct_CompanyCode` | TField |  | This field stores the Company Code where the ATM terminal belongs. |
| 23 | `ATM.TERM.LOCAL.API` | `AtmTerminalAcct_LocalApi` | TField |  | This is a locally developed routine/method that will be called only when USE.DEF.ACCT is set to "Yes".It takes two arguments. One incoming i.e. ATM.TERMINAL.ACCT record and one outgoing that returns Account id. Routine attached could be either: A jBC implementation by using an EB.API record with a source type of BASIC. For java implementations: An EB.API record id with a source type of HOOK which implements an interface defined in the EB.API record ATM.TER.ACCT.LOCAL.API.HOOK. This field supports the AtmMessageLifecycle.updateAccountNumber() method. The AtmMessageLifecycleclass is in the com.temenos.t24.api.hook.atm package which is in ATMFRM_MessageHook.jar shipped with T24. |
| 24 | `ATM.TERM.RESERVED.9` | `AtmTerminalAcct_Reserved9` | TField |  |  |
| 25 | `ATM.TERM.RESERVED.8` | `AtmTerminalAcct_Reserved8` | TField |  |  |
| 26 | `ATM.TERM.RESERVED.7` | `AtmTerminalAcct_Reserved7` | TField |  |  |
| 27 | `ATM.TERM.RESERVED.6` | `AtmTerminalAcct_Reserved6` | TField |  |  |
| 28 | `ATM.TERM.LOCAL.REF` | `AtmTerminalAcct_LocalRef` |  |  |  |
| 29 | `ATM.TERM.RESERVED.5` | `AtmTerminalAcct_Reserved5` | TField |  |  |
| 30 | `ATM.TERM.RESERVED.4` | `AtmTerminalAcct_Reserved4` | TField |  |  |
| 31 | `ATM.TERM.RESERVED.3` | `AtmTerminalAcct_Reserved3` | TField |  |  |
| 32 | `ATM.TERM.RESERVED.2` | `AtmTerminalAcct_Reserved2` | TField |  |  |
| 33 | `ATM.TERM.RESERVED.1` | `AtmTerminalAcct_Reserved1` | TField |  |  |
| 34 | `ATM.TERM.RECORD.STATUS` | `AtmTerminalAcct_RecordStatus` | String |  |  |
| 35 | `ATM.TERM.CURR.NO` | `AtmTerminalAcct_CurrNo` | String |  |  |
| 36 | `ATM.TERM.INPUTTER` | `AtmTerminalAcct_Inputter` |  |  |  |
| 37 | `ATM.TERM.DATE.TIME` | `AtmTerminalAcct_DateTime` |  |  |  |
| 38 | `ATM.TERM.AUTHORISER` | `AtmTerminalAcct_Authoriser` | String |  |  |
| 39 | `ATM.TERM.CO.CODE` | `AtmTerminalAcct_CoCode` | String |  |  |
| 40 | `ATM.TERM.DEPT.CODE` | `AtmTerminalAcct_DeptCode` | String |  |  |
| 41 | `ATM.TERM.AUDITOR.CODE` | `AtmTerminalAcct_AuditorCode` | String |  |  |
| 42 | `ATM.TERM.AUDIT.DATE.TIME` | `AtmTerminalAcct_AuditDateTime` | String |  |  |
