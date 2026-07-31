# RP.FEE.SCHEDULE — Table Schema

> Source: `INSERTS/I_F.RP.FEE.SCHEDULE` in `RP_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RP.FEE.REPO.TYPE` | `RpFeeSchedule_RepoType` | TField |  |  |
| 2 | `RP.FEE.BANK.MGN.PORTFOLIO` | `RpFeeSchedule_BankMgnPortfolio` | TField |  |  |
| 3 | `RP.FEE.CPTY.CLIENT.PORTFOLIO` | `RpFeeSchedule_CptyClientPortfolio` | TField |  |  |
| 4 | `RP.FEE.EXTERNAL.REF` | `RpFeeSchedule_ExternalRef` | TField |  |  |
| 5 | `RP.FEE.FEE.RATE` | `RpFeeSchedule_FeeRate` | TField |  |  |
| 6 | `RP.FEE.SPREAD` | `RpFeeSchedule_Spread` | TField |  |  |
| 7 | `RP.FEE.PAY.DAY.CONVENTION` | `RpFeeSchedule_PayDayConvention` | TField |  |  |
| 8 | `RP.FEE.START.DATE` | `RpFeeSchedule_StartDate` |  |  |  |
| 9 | `RP.FEE.END.DATE` | `RpFeeSchedule_EndDate` |  |  |  |
| 10 | `RP.FEE.FEE.AMT` | `RpFeeSchedule_FeeAmt` |  |  |  |
| 11 | `RP.FEE.PAYMENT.DATE` | `RpFeeSchedule_PaymentDate` |  |  |  |
| 12 | `RP.FEE.RESERVED.01` | `RpFeeSchedule_Reserved01` | TField |  |  |
| 13 | `RP.FEE.RESERVED.02` | `RpFeeSchedule_Reserved02` | TField |  |  |
| 14 | `RP.FEE.RESERVED.03` | `RpFeeSchedule_Reserved03` | TField |  |  |
| 15 | `RP.FEE.RESERVED.04` | `RpFeeSchedule_Reserved04` | TField |  |  |
| 16 | `RP.FEE.RESERVED.05` | `RpFeeSchedule_Reserved05` | TField |  |  |
| 17 | `RP.FEE.RESERVED.06` | `RpFeeSchedule_Reserved06` | TField |  |  |
| 18 | `RP.FEE.RESERVED.07` | `RpFeeSchedule_Reserved07` | TField |  |  |
| 19 | `RP.FEE.RESERVED.08` | `RpFeeSchedule_Reserved08` | TField |  |  |
| 20 | `RP.FEE.RESERVED.09` | `RpFeeSchedule_Reserved09` | TField |  |  |
| 21 | `RP.FEE.RESERVED.10` | `RpFeeSchedule_Reserved10` | TField |  |  |
| 22 | `RP.FEE.RESERVED.11` | `RpFeeSchedule_Reserved11` | TField |  |  |
| 23 | `RP.FEE.RESERVED.12` | `RpFeeSchedule_Reserved12` | TField |  |  |
| 24 | `RP.FEE.RESERVED.13` | `RpFeeSchedule_Reserved13` | TField |  |  |
| 25 | `RP.FEE.RESERVED.14` | `RpFeeSchedule_Reserved14` | TField |  |  |
| 26 | `RP.FEE.RESERVED.15` | `RpFeeSchedule_Reserved15` | TField |  |  |
| 27 | `RP.FEE.LOCAL.REF` | `RpFeeSchedule_LocalRef` |  |  |  |
| 28 | `RP.FEE.OVERRIDE` | `RpFeeSchedule_Override` |  |  |  |
| 29 | `RP.FEE.RECORD.STATUS` | `RpFeeSchedule_RecordStatus` | String |  |  |
| 30 | `RP.FEE.CURR.NO` | `RpFeeSchedule_CurrNo` | String |  |  |
| 31 | `RP.FEE.INPUTTER` | `RpFeeSchedule_Inputter` |  |  |  |
| 32 | `RP.FEE.DATE.TIME` | `RpFeeSchedule_DateTime` |  |  |  |
| 33 | `RP.FEE.AUTHORISER` | `RpFeeSchedule_Authoriser` | String |  |  |
| 34 | `RP.FEE.CO.CODE` | `RpFeeSchedule_CoCode` | String |  |  |
| 35 | `RP.FEE.DEPT.CODE` | `RpFeeSchedule_DeptCode` | String |  |  |
| 36 | `RP.FEE.AUDITOR.CODE` | `RpFeeSchedule_AuditorCode` | String |  |  |
| 37 | `RP.FEE.AUDIT.DATE.TIME` | `RpFeeSchedule_AuditDateTime` | String |  |  |
| 38 | `RP.FEE.PAYMENT.PROCESSED` | `RpFeeSchedule_PaymentProcessed` |  |  |  |
