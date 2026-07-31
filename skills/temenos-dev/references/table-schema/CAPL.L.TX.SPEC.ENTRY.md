# CAPL.L.TX.SPEC.ENTRY — Table Schema

> Source: `INSERTS/I_F.CAPL.L.TX.SPEC.ENTRY` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.H.TX.SPEC.TXN.CODE` | `CaplLTxSpecEntry_TxnCode` | TField |  | This field is used to denote the transaction code to be used for the dpec entry.Valid record from CAPL.H.TX.TRANSACTION table. |
| 2 | `CAPL.H.TX.SPEC.CUSTOMER.NO` | `CaplLTxSpecEntry_CustomerNo` | TField |  | Field is to denote the customer number for the spec entry.Valid record from CUSTOMER table. |
| 3 | `CAPL.H.TX.SPEC.ACCOUNT.NO` | `CaplLTxSpecEntry_AccountNo` | TField |  | This field denotes the acocunt number of the customer for which the transaction is performed.Valis ACCOUNT number to be defined here. |
| 4 | `CAPL.H.TX.SPEC.AMOUNT.LCY` | `CaplLTxSpecEntry_AmountLcy` | TField |  | Field denotes the transaction amount in LCY for the spec entry.Valid amount to be defined here. |
| 5 | `CAPL.H.TX.SPEC.VALUE.DATE` | `CaplLTxSpecEntry_ValueDate` | TField |  | The purpose of the field is used to define the value date for the spec transation.Allowed valus is a valid date. |
| 6 | `CAPL.H.TX.SPEC.BOOKING.DATE` | `CaplLTxSpecEntry_BookingDate` | TField |  | The purpose of the field is used to define the booking date for the spec transation.Allowed valus is a valid date. |
| 7 | `CAPL.H.TX.SPEC.PRD.CATEGORY` | `CaplLTxSpecEntry_PrdCategory` | TField |  | This field denote the product category for the spec entry to identify the product.Allowed value is CATEGORY. |
| 8 | `CAPL.H.TX.SPEC.TXN.REFERENCE` | `CaplLTxSpecEntry_TxnReference` | TField |  | Field holds th etransaction reference for the spec entry transaction.The transaction referemce is the portfoli id.E.g. 102299-1 |
| 9 | `CAPL.H.TX.SPEC.TAX.REFERENCE` | `CaplLTxSpecEntry_TaxReference` | TField |  | This field hodls the tax reference for the spec entry tranaction.E.g.CAPLTX1409800014 |
| 10 | `CAPL.H.TX.SPEC.SYSTEM.ID` | `CaplLTxSpecEntry_SystemId` | TField |  | The field denotes the system id for the spec entry. Field is to identify to which system the entry belongs to.E.g. FT, TT |
| 11 | `CAPL.H.TX.SPEC.AMOUNT.FCY` | `CaplLTxSpecEntry_AmountFcy` | TField |  | This field store the FCY transaction. Valid amount is store here. |
| 12 | `CAPL.H.TX.SPEC.CONV.RATE` | `CaplLTxSpecEntry_ConvRate` | TField |  | The field denotes the FCY amount conversion rate to LCY amount for the spec entry |
| 13 | `CAPL.H.TX.SPEC.CURRENCY` | `CaplLTxSpecEntry_Currency` | TField |  |  |
| 14 | `CAPL.H.TX.SPEC.RESIDENCE` | `CaplLTxSpecEntry_Residence` | TField |  | This field denotes the residence of the customer for the spec entry.Valid record from COUNTRY table. |
| 15 | `CAPL.H.TX.SPEC.PROVINCE` | `CaplLTxSpecEntry_Province` | TField |  | This field denotes the province of the customer for the spec entry.Valid record from REGION table. |
| 16 | `CAPL.H.TX.SPEC.SLIP.AMENDED` | `CaplLTxSpecEntry_SlipAmended` | TField |  | This Field is denotes whether the slip amended or not.Allowed values are 3 alphanumeric character. |
| 17 | `CAPL.H.TX.SPEC.AMEND.SEQ.NO` | `CaplLTxSpecEntry_AmendSeqNo` | TField |  | This field holds the Amend slip Number |
| 18 | `CAPL.H.TX.SPEC.NR.CODE` | `CaplLTxSpecEntry_NrCode` | TField |  | This field holds the NR.CODE for Non resident Transactions |
| 19 | `CAPL.H.TX.SPEC.R2.SOURCE` | `CaplLTxSpecEntry_R2Source` | TField |  | This field holds the R2 code for the Quebac customer transactions |
| 20 | `CAPL.H.TX.SPEC.PLAN.TYPE` | `CaplLTxSpecEntry_PlanType` | TField |  | This field denotes the plan type for the spec entry.Valid record from CAPL.PLAN.TYPE. |
| 21 | `CAPL.H.TX.SPEC.PLAN.GROUP` | `CaplLTxSpecEntry_PlanGroup` | TField |  | This field denotes the plan group for the spec entry.Valid record from CAPL.PLAN.TYPE.PARAM. |
| 22 | `CAPL.H.TX.SPEC.PRD.NAME` | `CaplLTxSpecEntry_PrdName` | TField |  | This field denotes the product name for the spec entry.Valid record from CAPL.PLAN.TYPE.PARAM. |
| 23 | `CAPL.H.TX.SPEC.RESERVED.4` | `CaplLTxSpecEntry_Reserved4` | TField |  |  |
| 24 | `CAPL.H.TX.SPEC.RESERVED.3` | `CaplLTxSpecEntry_Reserved3` | TField |  |  |
| 25 | `CAPL.H.TX.SPEC.RESERVED.2` | `CaplLTxSpecEntry_Reserved2` | TField |  |  |
| 26 | `CAPL.H.TX.SPEC.RESERVED.1` | `CaplLTxSpecEntry_Reserved1` | TField |  |  |
| 27 | `CAPL.H.TX.SPEC.LOCAL.REF` | `CaplLTxSpecEntry_LocalRef` |  |  |  |
