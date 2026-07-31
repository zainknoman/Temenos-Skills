# MARKET.RATE.TEXT — Table Schema

> Source: `INSERTS/I_F.MARKET.RATE.TEXT` in `ST_RateParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.MRT.DESCRIPTION` | `MarketRateText_Description` |  |  |  |
| 2 | `EB.MRT.RATE.TEXT` | `MarketRateText_RateText` | TField | Yes | Must be a valid S.W.I.F.T. code word. This field specifies the Floating Rate Option of the swap transaction. The value in this field should be one of the valid code words as specified in the details for field 14F on MT360s. Input should be in the form ; alpha/alpha/alpha e.g. USD/LIBOR/ISDA or if the code word is not known input should be OTHER. Refer to the SWIFT manual and ISDA definitions for further details. Validation Rules: 24 alphanumeric characters. Mandatory input. |
| 3 | `EB.MRT.RATE.KEY` | `MarketRateText_RateKey` | TField | No | This field specifies a valid sequence number of the file PERIODIC.INTEREST. This sequence number is part of the key to the PERIODIC.INTEREST rate table. Validation Rules: 1-2 numeric characters. Optional input field. |
| 4 | `EB.MRT.SWIFT.CODE.WORD` | `MarketRateText_SwiftCodeWord` | TField | Yes | This field is meant for specifying the Bilaterally Agreed codes between the Parties involved in the Transaction. Validation Rules: When the value of field RATE.TEXT is OTHER, the value for SWIFT.CODE.WORD is mandatory. When the value of field RATE.TEXT is not OTHER, the value for SWIFT.CODE.WORD should be null. The content should be a valid record ID in the table SWIFT.CODE.WORDS. |
| 5 | `EB.MRT.RFR.CALENDAR` | `MarketRateText_RfrCalendar` |  |  |  |
| 6 | `EB.MRT.CURRENCY` | `MarketRateText_Currency` |  |  |  |
| 7 | `EB.MRT.RESERVED.2` | `MarketRateText_Reserved2` | TField |  |  |
| 8 | `EB.MRT.RESERVED.1` | `MarketRateText_Reserved1` | TField |  |  |
| 9 | `EB.MRT.RECORD.STATUS` | `MarketRateText_RecordStatus` | String |  |  |
| 10 | `EB.MRT.CURR.NO` | `MarketRateText_CurrNo` | String |  |  |
| 11 | `EB.MRT.INPUTTER` | `MarketRateText_Inputter` |  |  |  |
| 12 | `EB.MRT.DATE.TIME` | `MarketRateText_DateTime` |  |  |  |
| 13 | `EB.MRT.AUTHORISER` | `MarketRateText_Authoriser` | String |  |  |
| 14 | `EB.MRT.CO.CODE` | `MarketRateText_CoCode` | String |  |  |
| 15 | `EB.MRT.DEPT.CODE` | `MarketRateText_DeptCode` | String |  |  |
| 16 | `EB.MRT.AUDITOR.CODE` | `MarketRateText_AuditorCode` | String |  |  |
| 17 | `EB.MRT.AUDIT.DATE.TIME` | `MarketRateText_AuditDateTime` | String |  |  |
