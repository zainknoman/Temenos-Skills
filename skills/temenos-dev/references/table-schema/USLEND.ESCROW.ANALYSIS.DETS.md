# USLEND.ESCROW.ANALYSIS.DETS — Table Schema

> Source: `INSERTS/I_F.USLEND.ESCROW.ANALYSIS.DETS` in `USLEND_EscrowProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USLEND.DETS.ANALYSIS.TYPE` | `UslendEscrowAnalysisDets_AnalysisType` | TField |  | Identifies the type of analysis done either INITIAL or ACTUAL Validation Rules INTIAL - Analysis done upon enrolment for Escrow processing, i.e. when customer opts of escrow processing on the arrangement either on a NEW/existing arrangement. ACTUAL - Analysis done by the system based on NXT.ANLYSIS.FQU field in PAYMENT.SCHEDULE property class |
| 2 | `USLEND.DETS.CALC.DATE` | `UslendEscrowAnalysisDets_CalcDate` | TField |  | Stores the date on which the analysis was performed |
| 3 | `USLEND.DETS.DATE` | `UslendEscrowAnalysisDets_Date` |  |  |  |
| 4 | `USLEND.DETS.PAYMENT.DESC` | `UslendEscrowAnalysisDets_PaymentDesc` |  |  |  |
| 5 | `USLEND.DETS.AMOUNT` | `UslendEscrowAnalysisDets_Amount` |  |  |  |
| 6 | `USLEND.DETS.BALANCE` | `UslendEscrowAnalysisDets_Balance` |  |  |  |
| 7 | `USLEND.DETS.INITIAL.AMOUNT` | `UslendEscrowAnalysisDets_InitialAmount` | TField |  | This field contains the initial amount required from the customer once the analysis is performed. The initial amount is calculated taking into consideration the available balance in ESCROWBAL balance type. Validation rules 1-16 AMT Standard amount format. |
| 8 | `USLEND.DETS.NEW.ESCROW.AMOUNT` | `UslendEscrowAnalysisDets_NewEscrowAmount` | TField |  |  |
| 9 | `USLEND.DETS.ESCROW.BALANCE` | `UslendEscrowAnalysisDets_EscrowBalance` | TField |  |  |
| 10 | `USLEND.DETS.CUSHION.AMOUNT` | `UslendEscrowAnalysisDets_CushionAmount` | TField |  |  |
| 11 | `USLEND.DETS.PREV.DATE` | `UslendEscrowAnalysisDets_PrevDate` |  |  |  |
| 12 | `USLEND.DETS.PREV.PAYMENT.DESC` | `UslendEscrowAnalysisDets_PrevPaymentDesc` |  |  |  |
| 13 | `USLEND.DETS.PREV.AMOUNT` | `UslendEscrowAnalysisDets_PrevAmount` |  |  |  |
| 14 | `USLEND.DETS.PREV.BALANCE` | `UslendEscrowAnalysisDets_PrevBalance` |  |  |  |
| 15 | `USLEND.DETS.NEW.ESCROW.AMT.EFF` | `UslendEscrowAnalysisDets_NewEscrowAmtEff` | TField |  |  |
| 16 | `USLEND.DETS.PROJ.ESCROW.BAL` | `UslendEscrowAnalysisDets_ProjEscrowBal` | TField |  |  |
| 17 | `USLEND.DETS.REQD.ESCROW.BAL` | `UslendEscrowAnalysisDets_ReqdEscrowBal` | TField |  |  |
| 18 | `USLEND.DETS.MINIMUM.BAL` | `UslendEscrowAnalysisDets_MinimumBal` | TField |  |  |
| 19 | `USLEND.DETS.SHORT.OVER.AMT` | `UslendEscrowAnalysisDets_ShortOverAmt` | TField |  |  |
| 20 | `USLEND.DETS.SHORT.OVER.OPTION` | `UslendEscrowAnalysisDets_ShortOverOption` | TField |  |  |
| 21 | `USLEND.DETS.PREVIOUS.CALC.DATE` | `UslendEscrowAnalysisDets_PreviousCalcDate` | TField |  |  |
| 22 | `USLEND.DETS.PREV.ANNUAL.DT` | `UslendEscrowAnalysisDets_PrevAnnualDt` | TField |  |  |
| 23 | `USLEND.DETS.ANNUAL.ANALYSIS.DT` | `UslendEscrowAnalysisDets_AnnualAnalysisDt` | TField |  |  |
| 24 | `USLEND.DETS.PREV.REQ.ESCROWBAL` | `UslendEscrowAnalysisDets_PrevReqEscrowbal` | TField |  |  |
| 25 | `USLEND.DETS.ESCROW.PAYMENT` | `UslendEscrowAnalysisDets_EscrowPayment` | TField |  |  |
| 26 | `USLEND.DETS.INIT.STMT.STATUS` | `UslendEscrowAnalysisDets_InitStmtStatus` | TField |  |  |
| 27 | `USLEND.DETS.RESERVED.10` | `UslendEscrowAnalysisDets_Reserved10` | TField |  | Reserve Fields |
| 28 | `USLEND.DETS.RESERVED.9` | `UslendEscrowAnalysisDets_Reserved9` | TField |  | Reserve Fields |
| 29 | `USLEND.DETS.RESERVED.8` | `UslendEscrowAnalysisDets_Reserved8` | TField |  | Reserve Fields |
| 30 | `USLEND.DETS.RESERVED.7` | `UslendEscrowAnalysisDets_Reserved7` | TField |  | Reserve Fields |
| 31 | `USLEND.DETS.RESERVED.6` | `UslendEscrowAnalysisDets_Reserved6` | TField |  | Reserve Fields |
| 32 | `USLEND.DETS.RESERVED.5` | `UslendEscrowAnalysisDets_Reserved5` | TField |  | Reserve Fields |
| 33 | `USLEND.DETS.RESERVED.4` | `UslendEscrowAnalysisDets_Reserved4` | TField |  | Reserve Fields |
| 34 | `USLEND.DETS.RESERVED.3` | `UslendEscrowAnalysisDets_Reserved3` | TField |  | Reserve Fields |
| 35 | `USLEND.DETS.RESERVED.2` | `UslendEscrowAnalysisDets_Reserved2` | TField |  | Reserve Fields |
| 36 | `USLEND.DETS.RESERVED.1` | `UslendEscrowAnalysisDets_Reserved1` | TField |  | Reserve Fields |
| 37 | `USLEND.DETS.LOCAL.REF` | `UslendEscrowAnalysisDets_LocalRef` |  |  |  |
