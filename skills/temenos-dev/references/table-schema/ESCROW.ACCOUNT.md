# ESCROW.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.ESCROW.ACCOUNT` in `ESCROW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.ACC.OPERATION` | `EscrowAccount_Operation` | TField | Yes | Determines the operation performed on escrow account. Possible values: NEW, MAINTENANCE, CLOSURE Mandatory on each record input. |
| 2 | `ESCROW.ACC.CURRENCY` | `EscrowAccount_Currency` | TField |  | Escrow Account Currency. Defaulted from AA.ARRANGEMENT>CURRENCY No Input |
| 3 | `ESCROW.ACC.PAYEE` | `EscrowAccount_Payee` |  |  |  |
| 4 | `ESCROW.ACC.REFERENCE.NO` | `EscrowAccount_ReferenceNo` |  |  |  |
| 5 | `ESCROW.ACC.ADDITIONAL.INFO` | `EscrowAccount_AdditionalInfo` |  |  |  |
| 6 | `ESCROW.ACC.NOTES` | `EscrowAccount_Notes` |  |  |  |
| 7 | `ESCROW.ACC.START.DATE` | `EscrowAccount_StartDate` |  |  |  |
| 8 | `ESCROW.ACC.DISBURSE.FREQ` | `EscrowAccount_DisburseFreq` |  |  |  |
| 9 | `ESCROW.ACC.IRREGULAR.PRD` | `EscrowAccount_IrregularPrd` |  |  |  |
| 10 | `ESCROW.ACC.ANNUAL.DISBURSE.AMT` | `EscrowAccount_AnnualDisburseAmt` |  |  |  |
| 11 | `ESCROW.ACC.ADJUST.PERCENT` | `EscrowAccount_AdjustPercent` |  |  |  |
| 12 | `ESCROW.ACC.END.DATE` | `EscrowAccount_EndDate` |  |  |  |
| 13 | `ESCROW.ACC.RESERVED.46` | `EscrowAccount_Reserved46` |  |  |  |
| 14 | `ESCROW.ACC.RESERVED.45` | `EscrowAccount_Reserved45` |  |  |  |
| 15 | `ESCROW.ACC.RESERVED.44` | `EscrowAccount_Reserved44` |  |  |  |
| 16 | `ESCROW.ACC.RESERVED.43` | `EscrowAccount_Reserved43` |  |  |  |
| 17 | `ESCROW.ACC.RESERVED.42` | `EscrowAccount_Reserved42` |  |  |  |
| 18 | `ESCROW.ACC.RESERVED.41` | `EscrowAccount_Reserved41` |  |  |  |
| 19 | `ESCROW.ACC.RESERVED.40` | `EscrowAccount_Reserved40` |  |  |  |
| 20 | `ESCROW.ACC.RESERVED.39` | `EscrowAccount_Reserved39` |  |  |  |
| 21 | `ESCROW.ACC.RESERVED.38` | `EscrowAccount_Reserved38` |  |  |  |
| 22 | `ESCROW.ACC.RESERVED.37` | `EscrowAccount_Reserved37` |  |  |  |
| 23 | `ESCROW.ACC.RESERVED.36` | `EscrowAccount_Reserved36` |  |  |  |
| 24 | `ESCROW.ACC.RESERVED.35` | `EscrowAccount_Reserved35` |  |  |  |
| 25 | `ESCROW.ACC.RESERVED.34` | `EscrowAccount_Reserved34` |  |  |  |
| 26 | `ESCROW.ACC.RESERVED.33` | `EscrowAccount_Reserved33` |  |  |  |
| 27 | `ESCROW.ACC.RESERVED.32` | `EscrowAccount_Reserved32` |  |  |  |
| 28 | `ESCROW.ACC.RESERVED.31` | `EscrowAccount_Reserved31` |  |  |  |
| 29 | `ESCROW.ACC.RESERVED.30` | `EscrowAccount_Reserved30` |  |  |  |
| 30 | `ESCROW.ACC.RESERVED.29` | `EscrowAccount_Reserved29` |  |  |  |
| 31 | `ESCROW.ACC.RESERVED.28` | `EscrowAccount_Reserved28` |  |  |  |
| 32 | `ESCROW.ACC.RESERVED.27` | `EscrowAccount_Reserved27` |  |  |  |
| 33 | `ESCROW.ACC.RESERVED.26` | `EscrowAccount_Reserved26` |  |  |  |
| 34 | `ESCROW.ACC.DISBURSE.DATE` | `EscrowAccount_DisburseDate` |  |  |  |
| 35 | `ESCROW.ACC.DISBURSE.AMT` | `EscrowAccount_DisburseAmt` |  |  |  |
| 36 | `ESCROW.ACC.ACTUAL.AMOUNT` | `EscrowAccount_ActualAmount` |  |  |  |
| 37 | `ESCROW.ACC.RESERVED.25` | `EscrowAccount_Reserved25` |  |  |  |
| 38 | `ESCROW.ACC.RESERVED.24` | `EscrowAccount_Reserved24` |  |  |  |
| 39 | `ESCROW.ACC.RESERVED.23` | `EscrowAccount_Reserved23` |  |  |  |
| 40 | `ESCROW.ACC.RESERVED.22` | `EscrowAccount_Reserved22` |  |  |  |
| 41 | `ESCROW.ACC.RESERVED.21` | `EscrowAccount_Reserved21` |  |  |  |
| 42 | `ESCROW.ACC.RESERVED.20` | `EscrowAccount_Reserved20` |  |  |  |
| 43 | `ESCROW.ACC.OVERDRAW` | `EscrowAccount_Overdraw` | TField | No | Determine if the Escrow account can be overdrawn or not. Optional input. If left blank, defaulted from ESCROW.PARAMETER>OVERDRAW |
| 44 | `ESCROW.ACC.CUSHION.PERIOD` | `EscrowAccount_CushionPeriod` | TField | No | Determine number of Instalments to be used as a cushion for the initial Escrow Payment Calculation. Optional input. If left blank, defaulted from ESCROW.PARAMETER>CUSHION.PERIOD |
| 45 | `ESCROW.ACC.ANALYSIS.TYPE` | `EscrowAccount_AnalysisType` | TField |  | Determines the type of analysis to be performed on the ESCROW account. Should exist in the table ESCROW.ANALYSIS.TYPE |
| 46 | `ESCROW.ACC.TEST.ANALYSIS` | `EscrowAccount_TestAnalysis` | TField |  | Once the Annual Analysis Date is determined, Test Analysis Date is then calculated by using the Annual Analysis Date less Test Effective Period value in the Escrow Parameter. If the date falls before the current system date then the test analysis date will be one calendar day forward. If the a date is entered in the field and it before the system date the system will produce an error. |
| 47 | `ESCROW.ACC.ANALYSIS.DATE` | `EscrowAccount_AnalysisDate` | TField |  | The date on which analysis has to be performed. Would be defaulted based on the analysis type chosed for the record. Can be modified by the user. |
| 48 | `ESCROW.ACC.ADHOC.ANALYSIS.DT` | `EscrowAccount_AdhocAnalysisDt` | TField | No | Ad-hoc date on which analysis has to be performed. Note: Analysis period will be considered before the new payment eff date. Optional input |
| 49 | `ESCROW.ACC.LAST.ANALYSIS.DT` | `EscrowAccount_LastAnalysisDt` | TField |  | Date on which last analysis was performed. No input. System updated field. |
| 50 | `ESCROW.ACC.RESERVED.19` | `EscrowAccount_Reserved19` | TField |  |  |
| 51 | `ESCROW.ACC.RESERVED.18` | `EscrowAccount_Reserved18` | TField |  |  |
| 52 | `ESCROW.ACC.RESERVED.17` | `EscrowAccount_Reserved17` | TField |  |  |
| 53 | `ESCROW.ACC.RESERVED.16` | `EscrowAccount_Reserved16` | TField |  |  |
| 54 | `ESCROW.ACC.RESERVED.15` | `EscrowAccount_Reserved15` | TField |  |  |
| 55 | `ESCROW.ACC.INITIAL.AMOUNT` | `EscrowAccount_InitialAmount` | TField |  | If the analysis type requires an initial amount to be collected, the amount is calculated and updated in this field. Can be overridden by the user. |
| 56 | `ESCROW.ACC.INSTAL.EFF.DATE` | `EscrowAccount_InstalEffDate` | TField |  | Effective Date of installment amount. |
| 57 | `ESCROW.ACC.INSTAL.AMOUNT` | `EscrowAccount_InstalAmount` | TField | Yes | Installment amount for the escrow due from customer. Mandatory input. If left blank, System calculated installment amount defaulted. |
| 58 | `ESCROW.ACC.NEW.INSTAL.EFF.DATE` | `EscrowAccount_NewInstalEffDate` | TField | No | The effective date when the new calculated installment amount would be effective. Optional input |
| 59 | `ESCROW.ACC.NEW.INSTAL.AMOUNT` | `EscrowAccount_NewInstalAmount` | TField | No | The new installment amount after a year end analysis would be stored here. Optional input |
| 60 | `ESCROW.ACC.CLOSURE.DATE` | `EscrowAccount_ClosureDate` | TField |  | Date when escrow account is closed. This field is defaulted to system date when OPERATION is set to CLOSURE. |
| 61 | `ESCROW.ACC.ARRANGEMENT.ID` | `EscrowAccount_ArrangementId` | TField |  |  |
| 62 | `ESCROW.ACC.OPENING.DATE` | `EscrowAccount_OpeningDate` | TField |  | Date when the escrow account was opened. Defaulted to Today when Status is NEW |
| 63 | `ESCROW.ACC.RESERVED.14` | `EscrowAccount_Reserved14` | TField |  |  |
| 64 | `ESCROW.ACC.RESERVED.13` | `EscrowAccount_Reserved13` | TField |  |  |
| 65 | `ESCROW.ACC.RESERVED.12` | `EscrowAccount_Reserved12` | TField |  |  |
| 66 | `ESCROW.ACC.RESERVED.11` | `EscrowAccount_Reserved11` | TField |  |  |
| 67 | `ESCROW.ACC.RESERVED.10` | `EscrowAccount_Reserved10` | TField |  |  |
| 68 | `ESCROW.ACC.RESERVED.9` | `EscrowAccount_Reserved9` | TField |  |  |
| 69 | `ESCROW.ACC.RESERVED.8` | `EscrowAccount_Reserved8` | TField |  |  |
| 70 | `ESCROW.ACC.RESERVED.7` | `EscrowAccount_Reserved7` | TField |  |  |
| 71 | `ESCROW.ACC.RESERVED.6` | `EscrowAccount_Reserved6` | TField |  |  |
| 72 | `ESCROW.ACC.RESERVED.5` | `EscrowAccount_Reserved5` | TField |  |  |
| 73 | `ESCROW.ACC.RESERVED.4` | `EscrowAccount_Reserved4` | TField |  |  |
| 74 | `ESCROW.ACC.RESERVED.3` | `EscrowAccount_Reserved3` | TField |  |  |
| 75 | `ESCROW.ACC.RESERVED.2` | `EscrowAccount_Reserved2` | TField |  |  |
| 76 | `ESCROW.ACC.RESERVED.1` | `EscrowAccount_Reserved1` | TField |  |  |
| 77 | `ESCROW.ACC.LOCAL.REF` | `EscrowAccount_LocalRef` |  |  |  |
| 78 | `ESCROW.ACC.DELIVERY.REF` | `EscrowAccount_DeliveryRef` |  |  |  |
| 79 | `ESCROW.ACC.OVERRIDE` | `EscrowAccount_Override` |  |  |  |
| 80 | `ESCROW.ACC.RECORD.STATUS` | `EscrowAccount_RecordStatus` | String |  |  |
| 81 | `ESCROW.ACC.CURR.NO` | `EscrowAccount_CurrNo` | String |  |  |
| 82 | `ESCROW.ACC.INPUTTER` | `EscrowAccount_Inputter` |  |  |  |
| 83 | `ESCROW.ACC.DATE.TIME` | `EscrowAccount_DateTime` |  |  |  |
| 84 | `ESCROW.ACC.AUTHORISER` | `EscrowAccount_Authoriser` | String |  |  |
| 85 | `ESCROW.ACC.CO.CODE` | `EscrowAccount_CoCode` | String |  |  |
| 86 | `ESCROW.ACC.DEPT.CODE` | `EscrowAccount_DeptCode` | String |  |  |
| 87 | `ESCROW.ACC.AUDITOR.CODE` | `EscrowAccount_AuditorCode` | String |  |  |
| 88 | `ESCROW.ACC.AUDIT.DATE.TIME` | `EscrowAccount_AuditDateTime` | String |  |  |
