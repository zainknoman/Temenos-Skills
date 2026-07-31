# TCIB.PRODUCT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.TCIB.PRODUCT.PARAMETER` in `CATCIB_TCIBOnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PROD.PARAM.ACCT.CREATE.ACTIVITY` | `TcibProductParameter_AcctCreateActivity` | TField |  | Activity to be used for account creation.valid AA.ACTIVITY |
| 2 | `PROD.PARAM.ACCT.UPDATE.ACTIVITY` | `TcibProductParameter_AcctUpdateActivity` | TField |  | Activity to be used for update account.valid AA.ACTIVITY |
| 3 | `PROD.PARAM.DEPOSITS.CREATE.ACTIVITY` | `TcibProductParameter_DepositsCreateActivity` | TField |  | Activity to be used for deposit creation.valid AA.ACTIVITY |
| 4 | `PROD.PARAM.DEPOSITS.UPDATE.ACTIVITY` | `TcibProductParameter_DepositsUpdateActivity` | TField |  | Activity to be used for update account.valid AA.ACTIVITY |
| 5 | `PROD.PARAM.AAA.CREATE.VERSION` | `TcibProductParameter_AaaCreateVersion` | TField |  | Versioin to be used for account or deposit creation.valid version record |
| 6 | `PROD.PARAM.AAA.SIMULATION.VERSION` | `TcibProductParameter_AaaSimulationVersion` | TField |  | Versioin to be used for simulation.valid version record |
| 7 | `PROD.PARAM.AAA.SIMEXEC.VERSION` | `TcibProductParameter_AaaSimexecVersion` | TField |  |  |
| 8 | `PROD.PARAM.OFS.SOURCE` | `TcibProductParameter_OfsSource` | TField |  | OFS source record to be used |
| 9 | `PROD.PARAM.NICK.NAME` | `TcibProductParameter_NickName` | TField |  | Name to be updated while creating account. Possible values are SHORT.TITLE,ACCOUNT.TITLE.1,ACCOUNT.TITLE.2 |
| 10 | `PROD.PARAM.DEP.INT.TYPE` | `TcibProductParameter_DepIntType` | TField |  | Purpose of the field to get the accrued balance for the defined interest property and displayed in the Get Account Information EnquiryValidation:Valid property from AA.PROPERTY |
| 11 | `PROD.PARAM.T24.FREQ` | `TcibProductParameter_T24Freq` |  |  |  |
| 12 | `PROD.PARAM.PAY.METHOD` | `TcibProductParameter_PayMethod` |  |  |  |
| 13 | `PROD.PARAM.ENQ.PAY.METHOD` | `TcibProductParameter_EnqPayMethod` |  |  |  |
| 14 | `PROD.PARAM.REG.FT.VERSION` | `TcibProductParameter_RegFtVersion` | TField |  | This field is used to define the FT version that is used to post the payout for registered product during closure.Valid record from VERSION application. |
| 15 | `PROD.PARAM.FT.VERSION` | `TcibProductParameter_FtVersion` | TField |  | This field is used to define the FT version that is used to post the payout for Non-registered product during closure.Valid record from VERSION application. |
| 16 | `PROD.PARAM.PO.VERSION` | `TcibProductParameter_PoVersion` | TField |  | This field is used to define the PO version that is used to post the payout during account closure.Valid record from VERSION application. |
| 17 | `PROD.PARAM.PLAN.GROUP` | `TcibProductParameter_PlanGroup` |  |  |  |
| 18 | `PROD.PARAM.PAYOFF.TXN.NO` | `TcibProductParameter_PayoffTxnNo` |  |  |  |
| 19 | `PROD.PARAM.RESERVED.5` | `TcibProductParameter_Reserved5` | TField |  |  |
| 20 | `PROD.PARAM.RESERVED.4` | `TcibProductParameter_Reserved4` | TField |  |  |
| 21 | `PROD.PARAM.RESERVED.3` | `TcibProductParameter_Reserved3` | TField |  |  |
| 22 | `PROD.PARAM.RESERVED.2` | `TcibProductParameter_Reserved2` | TField |  |  |
| 23 | `PROD.PARAM.RESERVED.1` | `TcibProductParameter_Reserved1` | TField |  |  |
| 24 | `PROD.PARAM.LOCAL.REF` | `TcibProductParameter_LocalRef` |  |  |  |
| 25 | `PROD.PARAM.OVERRIDE` | `TcibProductParameter_Override` |  |  |  |
| 26 | `PROD.PARAM.RECORD.STATUS` | `TcibProductParameter_RecordStatus` | String |  |  |
| 27 | `PROD.PARAM.CURR.NO` | `TcibProductParameter_CurrNo` | String |  |  |
| 28 | `PROD.PARAM.INPUTTER` | `TcibProductParameter_Inputter` |  |  |  |
| 29 | `PROD.PARAM.DATE.TIME` | `TcibProductParameter_DateTime` |  |  |  |
| 30 | `PROD.PARAM.AUTHORISER` | `TcibProductParameter_Authoriser` | String |  |  |
| 31 | `PROD.PARAM.CO.CODE` | `TcibProductParameter_CoCode` | String |  |  |
| 32 | `PROD.PARAM.DEPT.CODE` | `TcibProductParameter_DeptCode` | String |  |  |
| 33 | `PROD.PARAM.AUDITOR.CODE` | `TcibProductParameter_AuditorCode` | String |  |  |
| 34 | `PROD.PARAM.AUDIT.DATE.TIME` | `TcibProductParameter_AuditDateTime` | String |  |  |
