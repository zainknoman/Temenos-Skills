# POR.POSTCONFIRMATIONS — Table Schema

> Source: `INSERTS/I_F.POR.POSTCONFIRMATIONS` in `PP_ConfirmationsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPC.CompanyID` | `PorPostconfirmations_Companyid` |  |  |  |
| 2 | `PPPC.FTNumber` | `PorPostconfirmations_Ftnumber` |  |  |  |
| 3 | `PPPC.AdviceNumber` | `PorPostconfirmations_Advicenumber` |  |  |  |
| 4 | `PPPC.SequenceNumber` | `PorPostconfirmations_Sequencenumber` |  |  |  |
| 5 | `PPPC.ConfirmationSent` | `PorPostconfirmations_Confirmationsent` |  |  |  |
| 6 | `PPPC.DebitCreditAdvice` | `PorPostconfirmations_Debitcreditadvice` |  |  |  |
| 7 | `PPPC.DeliveryInformationLine1` | `PorPostconfirmations_Deliveryinformationline1` |  |  |  |
| 8 | `PPPC.DeliveryInformationLine2` | `PorPostconfirmations_Deliveryinformationline2` |  |  |  |
| 9 | `PPPC.DeliveryInformationLine3` | `PorPostconfirmations_Deliveryinformationline3` |  |  |  |
| 10 | `PPPC.DeliveryInformationLine4` | `PorPostconfirmations_Deliveryinformationline4` |  |  |  |
