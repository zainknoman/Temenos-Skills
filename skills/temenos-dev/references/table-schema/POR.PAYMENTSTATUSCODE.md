# POR.PAYMENTSTATUSCODE — Table Schema

> Source: `INSERTS/I_F.POR.PAYMENTSTATUSCODE` in `PP_PaymentFrameworkService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPSC.CompanyID` | `PorPaymentstatuscode_Companyid` |  |  |  |
| 2 | `PPPSC.FTNumber` | `PorPaymentstatuscode_Ftnumber` |  |  |  |
| 3 | `PPPSC.Timestamp` | `PorPaymentstatuscode_Timestamp` |  |  |  |
| 4 | `PPPSC.StatusCode` | `PorPaymentstatuscode_Statuscode` |  |  |  |
| 5 | `PPPSC.ProcessedIndicator` | `PorPaymentstatuscode_Processedindicator` |  |  |  |
| 6 | `PPPSC.TTIndicator` | `PorPaymentstatuscode_Ttindicator` |  |  |  |
| 7 | `PPPSC.WeightCode` | `PorPaymentstatuscode_Weightcode` |  |  |  |
| 8 | `PPPSC.SpecificWeightCode` | `PorPaymentstatuscode_Specificweightcode` |  |  |  |
| 9 | `PPPSC.ProcessID` | `PorPaymentstatuscode_Processid` |  |  |  |
