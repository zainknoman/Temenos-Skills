# NOMINEE.CUMUL.PAYORDER.HIST — Table Schema

> Source: `INSERTS/I_F.NOMINEE.CUMUL.PAYORDER.HIST` in `CAEFPA_EFTPap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NOM.PO.HIST.ARR.NUMBER` | `NomineeCumulPayorderHist_ArrNumber` |  |  |  |
| 2 | `NOM.PO.HIST.PAY.ORDER.ID` | `NomineeCumulPayorderHist_PayOrderId` |  |  |  |
| 3 | `NOM.PO.HIST.VALUE.DATE` | `NomineeCumulPayorderHist_ValueDate` |  |  |  |
| 4 | `NOM.PO.HIST.AMOUNT` | `NomineeCumulPayorderHist_Amount` |  |  |  |
| 5 | `NOM.PO.HIST.TOTAL.AMOUNT` | `NomineeCumulPayorderHist_TotalAmount` | TField |  |  |
| 6 | `NOM.PO.HIST.CUSTOMER` | `NomineeCumulPayorderHist_Customer` | TField |  |  |
| 7 | `NOM.PO.HIST.BENEFICIARY` | `NomineeCumulPayorderHist_Beneficiary` | TField |  |  |
| 8 | `NOM.PO.HIST.PO.PRODUCT` | `NomineeCumulPayorderHist_PoProduct` | TField |  |  |
| 9 | `NOM.PO.HIST.DR.AMOUNT` | `NomineeCumulPayorderHist_DrAmount` | TField |  |  |
| 10 | `NOM.PO.HIST.CR.AMOUNT` | `NomineeCumulPayorderHist_CrAmount` | TField |  |  |
| 11 | `NOM.PO.HIST.HIST.ID` | `NomineeCumulPayorderHist_HistId` |  |  |  |
| 12 | `NOM.PO.HIST.RESERVED.9` | `NomineeCumulPayorderHist_Reserved9` |  |  |  |
| 13 | `NOM.PO.HIST.RESERVED.8` | `NomineeCumulPayorderHist_Reserved8` | TField |  |  |
| 14 | `NOM.PO.HIST.RESERVED.7` | `NomineeCumulPayorderHist_Reserved7` | TField |  |  |
| 15 | `NOM.PO.HIST.RESERVED.6` | `NomineeCumulPayorderHist_Reserved6` | TField |  |  |
| 16 | `NOM.PO.HIST.RESERVED.5` | `NomineeCumulPayorderHist_Reserved5` | TField |  |  |
| 17 | `NOM.PO.HIST.RESERVED.4` | `NomineeCumulPayorderHist_Reserved4` | TField |  |  |
| 18 | `NOM.PO.HIST.RESERVED.3` | `NomineeCumulPayorderHist_Reserved3` | TField |  |  |
| 19 | `NOM.PO.HIST.RESERVED.2` | `NomineeCumulPayorderHist_Reserved2` | TField |  |  |
| 20 | `NOM.PO.HIST.RESERVED.1` | `NomineeCumulPayorderHist_Reserved1` | TField |  |  |
