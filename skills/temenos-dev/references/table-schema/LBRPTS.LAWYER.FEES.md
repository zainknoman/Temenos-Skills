# LBRPTS.LAWYER.FEES — Table Schema

> Source: `INSERTS/I_F.LBRPTS.LAWYER.FEES` in `LBRPTS_HonoraryCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LA.FE.AGENCY.ID` | `LbrptsLawyerFees_AgencyId` | TField |  | This field is the Agency ID of the Lawyer. |
| 2 | `LA.FE.LEGAL.PAYMENT.DATE` | `LbrptsLawyerFees_LegalPaymentDate` |  |  |  |
| 3 | `LA.FE.COMMISSION.PERC` | `LbrptsLawyerFees_CommissionPerc` |  |  |  |
| 4 | `LA.FE.APAY.CURR.COMM` | `LbrptsLawyerFees_ApayCurrComm` |  |  |  |
| 5 | `LA.FE.APAY.COMMISSION` | `LbrptsLawyerFees_ApayCommission` |  |  |  |
| 6 | `LA.FE.APAY.LEGAL.FEES` | `LbrptsLawyerFees_ApayLegalFees` |  |  |  |
| 7 | `LA.FE.APAY.RECOVERY.FEES` | `LbrptsLawyerFees_ApayRecoveryFees` |  |  |  |
| 8 | `LA.FE.APAY.TOTAL.COMM` | `LbrptsLawyerFees_ApayTotalComm` |  |  |  |
| 9 | `LA.FE.PREVIOUS.AGENT.ID` | `LbrptsLawyerFees_PreviousAgentId` | TField |  | Placeholder to save the old lawyer details. |
| 10 | `LA.FE.PREV.AGENCY.CHANGE.DATE` | `LbrptsLawyerFees_PrevAgencyChangeDate` | TField |  | The date on which the Lawyer was changed for the customer. |
| 11 | `LA.FE.TRANS.DATE` | `LbrptsLawyerFees_TransDate` |  |  |  |
| 12 | `LA.FE.TRANS.REFERENCE` | `LbrptsLawyerFees_TransReference` |  |  |  |
| 13 | `LA.FE.TRANS.AMOUNT` | `LbrptsLawyerFees_TransAmount` |  |  |  |
| 14 | `LA.FE.RESERVED.10` | `LbrptsLawyerFees_Reserved10` | TField |  |  |
| 15 | `LA.FE.RESERVED.9` | `LbrptsLawyerFees_Reserved9` | TField |  |  |
| 16 | `LA.FE.RESERVED.8` | `LbrptsLawyerFees_Reserved8` | TField |  |  |
| 17 | `LA.FE.RESERVED.7` | `LbrptsLawyerFees_Reserved7` | TField |  |  |
| 18 | `LA.FE.RESERVED.6` | `LbrptsLawyerFees_Reserved6` | TField |  |  |
| 19 | `LA.FE.RESERVED.5` | `LbrptsLawyerFees_Reserved5` | TField |  |  |
| 20 | `LA.FE.RESERVED.4` | `LbrptsLawyerFees_Reserved4` | TField |  |  |
| 21 | `LA.FE.RESERVED.3` | `LbrptsLawyerFees_Reserved3` | TField |  |  |
| 22 | `LA.FE.RESERVED.2` | `LbrptsLawyerFees_Reserved2` | TField |  |  |
| 23 | `LA.FE.RESERVED.1` | `LbrptsLawyerFees_Reserved1` | TField |  |  |
