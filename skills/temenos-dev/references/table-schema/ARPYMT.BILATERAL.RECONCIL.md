# ARPYMT.BILATERAL.RECONCIL — Table Schema

> Source: `INSERTS/I_F.ARPYMT.BILATERAL.RECONCIL` in `ARPYMT_ReconcilPayments.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BILATERAL.PRODUCT` | `ArpymtBilateralReconcil_Product` | TField |  | This is the unique Product identifier for Bilateral files - Eg: PPD/CCD/CTX |
| 2 | `BILATERAL.SESSION` | `ArpymtBilateralReconcil_Session` | TField |  | The session for which reconciliation information is sought P- Presented, R - Rejected |
| 3 | `BILATERAL.FILE.DATE` | `ArpymtBilateralReconcil_FileDate` | TField |  | The date for which the reconciliation information is picked fora and this date is the date give in the incoming file |
| 4 | `BILATERAL.CURRENCY` | `ArpymtBilateralReconcil_Currency` | TField |  | The currency of the session of reconciliation |
| 5 | `BILATERAL.ENTITY` | `ArpymtBilateralReconcil_Entity` | TField |  | The Bank/Entity to which this reconciliation information pertains to |
| 6 | `BILATERAL.ENTITY.CODE` | `ArpymtBilateralReconcil_EntityCode` | TField |  | The Bank code from where the transaction originated or transaction is being sent to - as the case may be. |
| 7 | `BILATERAL.DEBIT.TOT.COUNT` | `ArpymtBilateralReconcil_DebitTotCount` | TField |  | The total of transaction (in nos) for which the NOSTRO account was debited. |
| 8 | `BILATERAL.DEBIT.TOT.AMT` | `ArpymtBilateralReconcil_DebitTotAmt` | TField |  |  |
| 9 | `BILATERAL.CREDIT.TOT.COUNT` | `ArpymtBilateralReconcil_CreditTotCount` | TField |  | The total of transaction (in amount) for which the NOSTRO account was credited |
| 10 | `BILATERAL.CREDIT.TOT.AMT` | `ArpymtBilateralReconcil_CreditTotAmt` | TField |  |  |
| 11 | `BILATERAL.POSITION` | `ArpymtBilateralReconcil_Position` | TField |  | Difference between Debit Amount and Credit Amount as given above |
| 12 | `BILATERAL.DEBIT.TOT.COUNT.COELSA` | `ArpymtBilateralReconcil_DebitTotCountCoelsa` | TField |  | Information from COELSA on the total of transaction (in nos) for which the NOSTRO account was debited |
| 13 | `BILATERAL.DEBIT.TOTAL.AMOUNT.COELSA` | `ArpymtBilateralReconcil_DebitTotalAmountCoelsa` | TField |  |  |
| 14 | `BILATERAL.CREDIT.TOT.COUNT.COELSA` | `ArpymtBilateralReconcil_CreditTotCountCoelsa` | TField |  | Information from COELSA on the total of transaction (in nos) for which the NOSTRO account was credited |
| 15 | `BILATERAL.CREDIT.TOT.AMT.COELSA` | `ArpymtBilateralReconcil_CreditTotAmtCoelsa` | TField |  |  |
| 16 | `BILATERAL.POSITION.COELSA` | `ArpymtBilateralReconcil_PositionCoelsa` | TField |  | Information from COELSA on the difference between Debit Amount and Credit Amount as given above |
| 17 | `BILATERAL.LOCAL.REF` | `ArpymtBilateralReconcil_LocalRef` |  |  |  |
| 18 | `BILATERAL.RESERVED.1` | `ArpymtBilateralReconcil_Reserved1` | TField |  |  |
| 19 | `BILATERAL.RESERVED.2` | `ArpymtBilateralReconcil_Reserved2` | TField |  |  |
| 20 | `BILATERAL.RESERVED.3` | `ArpymtBilateralReconcil_Reserved3` | TField |  |  |
| 21 | `BILATERAL.RESERVED.4` | `ArpymtBilateralReconcil_Reserved4` | TField |  |  |
| 22 | `BILATERAL.RESERVED.5` | `ArpymtBilateralReconcil_Reserved5` | TField |  |  |
| 23 | `BILATERAL.RESERVED.6` | `ArpymtBilateralReconcil_Reserved6` | TField |  |  |
| 24 | `BILATERAL.RESERVED.7` | `ArpymtBilateralReconcil_Reserved7` | TField |  |  |
| 25 | `BILATERAL.RESERVED.8` | `ArpymtBilateralReconcil_Reserved8` | TField |  |  |
| 26 | `BILATERAL.RESERVED.9` | `ArpymtBilateralReconcil_Reserved9` | TField |  |  |
| 27 | `BILATERAL.RESERVED.10` | `ArpymtBilateralReconcil_Reserved10` | TField |  |  |
| 28 | `BILATERAL.OVERRIDE` | `ArpymtBilateralReconcil_Override` |  |  |  |
| 29 | `BILATERAL.RECORD.STATUS` | `ArpymtBilateralReconcil_RecordStatus` | String |  |  |
| 30 | `BILATERAL.CURR.NO` | `ArpymtBilateralReconcil_CurrNo` | String |  |  |
| 31 | `BILATERAL.INPUTTER` | `ArpymtBilateralReconcil_Inputter` |  |  |  |
| 32 | `BILATERAL.DATE.TIME` | `ArpymtBilateralReconcil_DateTime` |  |  |  |
| 33 | `BILATERAL.AUTHORISER` | `ArpymtBilateralReconcil_Authoriser` | String |  |  |
| 34 | `BILATERAL.CO.CODE` | `ArpymtBilateralReconcil_CoCode` | String |  |  |
| 35 | `BILATERAL.DEPT.CODE` | `ArpymtBilateralReconcil_DeptCode` | String |  |  |
| 36 | `BILATERAL.AUDITOR.CODE` | `ArpymtBilateralReconcil_AuditorCode` | String |  |  |
| 37 | `BILATERAL.AUDIT.DATE.TIME` | `ArpymtBilateralReconcil_AuditDateTime` | String |  |  |
