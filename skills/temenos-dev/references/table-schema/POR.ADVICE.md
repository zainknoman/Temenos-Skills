# POR.ADVICE — Table Schema

> Source: `INSERTS/I_F.POR.ADVICE` in `PP_ConfirmationsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPAD.CompanyID` | `PorAdvice_Companyid` |  |  |  |
| 2 | `PPPAD.FTNumber` | `PorAdvice_Ftnumber` |  |  |  |
| 3 | `PPPAD.SequenceNumber` | `PorAdvice_Sequencenumber` |  |  |  |
| 4 | `PPPAD.DebitCreditAdvice` | `PorAdvice_Debitcreditadvice` |  |  |  |
| 5 | `PPPAD.AdviceNumber` | `PorAdvice_Advicenumber` |  |  |  |
| 6 | `PPPAD.BCIndicator` | `PorAdvice_Bcindicator` |  |  |  |
| 7 | `PPPAD.CTRBTRIndicator` | `PorAdvice_Ctrbtrindicator` |  |  |  |
| 8 | `PPPAD.DeliveryMethod` | `PorAdvice_Deliverymethod` |  |  |  |
| 9 | `PPPAD.DeliveryInformationLine1` | `PorAdvice_Deliveryinformationline1` |  |  |  |
| 10 | `PPPAD.DeliveryInformationLine2` | `PorAdvice_Deliveryinformationline2` |  |  |  |
| 11 | `PPPAD.DeliveryInformationLine3` | `PorAdvice_Deliveryinformationline3` |  |  |  |
| 12 | `PPPAD.DeliveryInformationLine4` | `PorAdvice_Deliveryinformationline4` |  |  |  |
| 13 | `PPPAD.Attention` | `PorAdvice_Attention` |  |  |  |
| 14 | `PPPAD.AdviceType` | `PorAdvice_Advicetype` |  |  |  |
| 15 | `PPPAD.CustomerStatusMsg` | `PorAdvice_Customerstatusmsg` |  |  |  |
