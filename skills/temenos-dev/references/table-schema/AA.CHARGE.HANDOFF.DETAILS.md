# AA.CHARGE.HANDOFF.DETAILS — Table Schema

> Source: `INSERTS/I_F.AA.CHARGE.HANDOFF.DETAILS` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CHD.SOURCE.REFERENCE` | `AaChargeHandoffDetails_SourceReference` |  |  |  |
| 2 | `AA.CHD.SOURCE.APPLICATION` | `AaChargeHandoffDetails_SourceApplication` |  |  |  |
| 3 | `AA.CHD.SOURCE.ID` | `AaChargeHandoffDetails_SourceId` |  |  |  |
| 4 | `AA.CHD.PAYMENT.DATE` | `AaChargeHandoffDetails_PaymentDate` |  |  |  |
| 5 | `AA.CHD.ACTUAL.PAY.DATE` | `AaChargeHandoffDetails_ActualPayDate` |  |  |  |
| 6 | `AA.CHD.FINANCIAL.DATE` | `AaChargeHandoffDetails_FinancialDate` |  |  |  |
| 7 | `AA.CHD.DEFER.DATE` | `AaChargeHandoffDetails_DeferDate` |  |  |  |
| 8 | `AA.CHD.CURRENCY` | `AaChargeHandoffDetails_Currency` |  |  |  |
| 9 | `AA.CHD.OR.TOTAL.AMOUNT` | `AaChargeHandoffDetails_OrTotalAmount` |  |  |  |
| 10 | `AA.CHD.OR.TOTAL.AMT.LCY` | `AaChargeHandoffDetails_OrTotalAmtLcy` |  |  |  |
| 11 | `AA.CHD.PROPERTY` | `AaChargeHandoffDetails_Property` |  |  |  |
| 12 | `AA.CHD.OR.PROP.AMOUNT` | `AaChargeHandoffDetails_OrPropAmount` |  |  |  |
| 13 | `AA.CHD.OR.PROP.AMT.LCY` | `AaChargeHandoffDetails_OrPropAmtLcy` |  |  |  |
| 14 | `AA.CHD.PAYMENT.TYPE` | `AaChargeHandoffDetails_PaymentType` |  |  |  |
| 15 | `AA.CHD.WAIVE.AMOUNT` | `AaChargeHandoffDetails_WaiveAmount` |  |  |  |
| 16 | `AA.CHD.WAIVE.AMT.LCY` | `AaChargeHandoffDetails_WaiveAmtLcy` |  |  |  |
| 17 | `AA.CHD.WAIVE.REASON` | `AaChargeHandoffDetails_WaiveReason` |  |  |  |
| 18 | `AA.CHD.BILL.DATE` | `AaChargeHandoffDetails_BillDate` |  |  |  |
| 19 | `AA.CHD.BILL.TYPE` | `AaChargeHandoffDetails_BillType` |  |  |  |
| 20 | `AA.CHD.PAYMENT.METHOD` | `AaChargeHandoffDetails_PaymentMethod` |  |  |  |
| 21 | `AA.CHD.PAYMENT.INDICATOR` | `AaChargeHandoffDetails_PaymentIndicator` |  |  |  |
| 22 | `AA.CHD.BILL.STATUS` | `AaChargeHandoffDetails_BillStatus` |  |  |  |
| 23 | `AA.CHD.BILL.ST.CHG.DT` | `AaChargeHandoffDetails_BillStChgDt` |  |  |  |
| 24 | `AA.CHD.ISSUE.BILL.REFERENCE` | `AaChargeHandoffDetails_IssueBillReference` |  |  |  |
| 25 | `AA.CHD.DEFER.REFERENCE` | `AaChargeHandoffDetails_DeferReference` |  |  |  |
| 26 | `AA.CHD.DUE.REFERENCE` | `AaChargeHandoffDetails_DueReference` |  |  |  |
| 27 | `AA.CHD.RR.SOURCE.REFERENCE` | `AaChargeHandoffDetails_RrSourceReference` |  |  |  |
| 28 | `AA.CHD.RESERVED.10` | `AaChargeHandoffDetails_Reserved10` | TField |  |  |
| 29 | `AA.CHD.RESERVED.9` | `AaChargeHandoffDetails_Reserved9` | TField |  |  |
| 30 | `AA.CHD.RESERVED.8` | `AaChargeHandoffDetails_Reserved8` | TField |  |  |
| 31 | `AA.CHD.RESERVED.7` | `AaChargeHandoffDetails_Reserved7` | TField |  |  |
| 32 | `AA.CHD.RESERVED.6` | `AaChargeHandoffDetails_Reserved6` | TField |  |  |
| 33 | `AA.CHD.RESERVED.5` | `AaChargeHandoffDetails_Reserved5` | TField |  |  |
| 34 | `AA.CHD.RESERVED.4` | `AaChargeHandoffDetails_Reserved4` | TField |  |  |
| 35 | `AA.CHD.RESERVED.3` | `AaChargeHandoffDetails_Reserved3` | TField |  |  |
| 36 | `AA.CHD.RESERVED.2` | `AaChargeHandoffDetails_Reserved2` | TField |  |  |
| 37 | `AA.CHD.RESERVED.1` | `AaChargeHandoffDetails_Reserved1` | TField |  |  |
