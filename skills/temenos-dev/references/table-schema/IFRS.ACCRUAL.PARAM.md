# IFRS.ACCRUAL.PARAM — Table Schema

> Source: `INSERTS/I_F.IFRS.ACCRUAL.PARAM` in `IA_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IFRS.ACC.PAR.DESC` | `IfrsAccrualParam_Desc` |  |  |  |
| 2 | `IFRS.ACC.PAR.IFRS.SUB.TYPE` | `IfrsAccrualParam_IfrsSubType` |  |  |  |
| 3 | `IFRS.ACC.PAR.ACCT.FREQ` | `IfrsAccrualParam_AcctFreq` |  |  |  |
| 4 | `IFRS.ACC.PAR.UPD.ACCT.DTLS` | `IfrsAccrualParam_UpdAcctDtls` | TField |  | This field provides the option to update IFRS.ACCOUNTING.DETAILS. Value "YES" indicates the system should update IFRS.ACCOUNTING.DETAILS. Value "NO" indicates the system should not update IFRS.ACCOUNTING.DETAILS. |
| 5 | `IFRS.ACC.PAR.RECORD.STATUS` | `IfrsAccrualParam_RecordStatus` | String |  |  |
| 6 | `IFRS.ACC.PAR.CURR.NO` | `IfrsAccrualParam_CurrNo` | String |  |  |
| 7 | `IFRS.ACC.PAR.INPUTTER` | `IfrsAccrualParam_Inputter` |  |  |  |
| 8 | `IFRS.ACC.PAR.DATE.TIME` | `IfrsAccrualParam_DateTime` |  |  |  |
| 9 | `IFRS.ACC.PAR.AUTHORISER` | `IfrsAccrualParam_Authoriser` | String |  |  |
| 10 | `IFRS.ACC.PAR.CO.CODE` | `IfrsAccrualParam_CoCode` | String |  |  |
| 11 | `IFRS.ACC.PAR.DEPT.CODE` | `IfrsAccrualParam_DeptCode` | String |  |  |
| 12 | `IFRS.ACC.PAR.AUDITOR.CODE` | `IfrsAccrualParam_AuditorCode` | String |  |  |
| 13 | `IFRS.ACC.PAR.AUDIT.DATE.TIME` | `IfrsAccrualParam_AuditDateTime` | String |  |  |
| 14 | `IFRS.ACC.PAR.SPLIT.DELTA` | `IfrsAccrualParam_SplitDelta` | TField |  | This field provides the option to split the amortised amount with its respective fee/cost Amortised amount(delta) which is the difference between the asset value measured in standard method and the asset value measured in the EIR method will be split and shown fee and cost wise. Setting this field as "Y" enables banks to account for non-refundable fees and cost incurred by a loan as per FASB91. Value "Y" indicates the system should split the AMORTISED amount. Value "N" indicates the system should not split the AMORTISED amount. Validation Rules: Once the Split Delta is enabled, its value can't be reverted back to "N" or "NONE" This field is allowed to input only when RN(Recoginition of fees) module is installed. |
| 15 | `IFRS.ACC.PAR.RECOVERY.ORDER` | `IfrsAccrualParam_RecoveryOrder` | TField |  | Banks initiate charge-off on a loan when they got the objective evidence that the customer will not repay, further repayment to a charged off loan is considered as recovery When recovery is made more than the charged off amount, it is considered as excess. Value in this field indicates order of priority in which excess recovery should be handled. Normal recovery will reduce the charge off portion of the loan. Excess recovery then reduce the unamortised portion of fee, cost or IAP, based on the order specified here. FEE/COST - unamortised fees and cost incurred at the time of disbursement of the loan. IAP - interest applied to principal- Whenever a contract moves to non-performing status, amortisation to P &amp; L is stopped. On resume, the unamortised portion during the stop period is treated as a new charge. |
