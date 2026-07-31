# NOMINEE.CUMUL.PAYORDER — Table Schema

> Source: `INSERTS/I_F.NOMINEE.CUMUL.PAYORDER` in `CAEFPA_EFTPap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NOM.PAYORDER.ARR.NUMBER` | `NomineeCumulPayorder_ArrNumber` |  |  |  |
| 2 | `NOM.PAYORDER.PAY.ORDER.ID` | `NomineeCumulPayorder_PayOrderId` |  |  |  |
| 3 | `NOM.PAYORDER.VALUE.DATE` | `NomineeCumulPayorder_ValueDate` |  |  |  |
| 4 | `NOM.PAYORDER.AMOUNT` | `NomineeCumulPayorder_Amount` |  |  |  |
| 5 | `NOM.PAYORDER.TOTAL.AMOUNT` | `NomineeCumulPayorder_TotalAmount` | TField |  |  |
| 6 | `NOM.PAYORDER.CUSTOMER` | `NomineeCumulPayorder_Customer` | TField |  |  |
| 7 | `NOM.PAYORDER.BENEFICIARY` | `NomineeCumulPayorder_Beneficiary` | TField |  |  |
| 8 | `NOM.PAYORDER.PO.PRODUCT` | `NomineeCumulPayorder_PoProduct` | TField |  |  |
| 9 | `NOM.PAYORDER.DR.AMOUNT` | `NomineeCumulPayorder_DrAmount` | TField |  |  |
| 10 | `NOM.PAYORDER.CR.AMOUNT` | `NomineeCumulPayorder_CrAmount` | TField |  |  |
| 11 | `NOM.PAYORDER.HIST.ID` | `NomineeCumulPayorder_HistId` |  |  |  |
| 12 | `NOM.PAYORDER.RESERVED.10` | `NomineeCumulPayorder_Reserved10` |  |  |  |
| 13 | `NOM.PAYORDER.RESERVED.9` | `NomineeCumulPayorder_Reserved9` | TField |  |  |
| 14 | `NOM.PAYORDER.RESERVED.8` | `NomineeCumulPayorder_Reserved8` | TField |  |  |
| 15 | `NOM.PAYORDER.RESERVED.7` | `NomineeCumulPayorder_Reserved7` | TField |  |  |
| 16 | `NOM.PAYORDER.RESERVED.6` | `NomineeCumulPayorder_Reserved6` | TField |  |  |
| 17 | `NOM.PAYORDER.RESERVED.5` | `NomineeCumulPayorder_Reserved5` | TField |  |  |
| 18 | `NOM.PAYORDER.RESERVED.4` | `NomineeCumulPayorder_Reserved4` | TField |  |  |
| 19 | `NOM.PAYORDER.RESERVED.3` | `NomineeCumulPayorder_Reserved3` | TField |  |  |
| 20 | `NOM.PAYORDER.RESERVED.2` | `NomineeCumulPayorder_Reserved2` | TField |  |  |
| 21 | `NOM.PAYORDER.RESERVED.1` | `NomineeCumulPayorder_Reserved1` | TField |  |  |
