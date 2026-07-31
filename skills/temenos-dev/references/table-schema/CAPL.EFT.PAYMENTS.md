# CAPL.EFT.PAYMENTS — Table Schema

> Source: `INSERTS/I_F.CAPL.EFT.PAYMENTS` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.EPAY.CUSTOMER.ID` | `CaplEftPayments_CustomerId` |  |  |  |
| 2 | `CAPL.EPAY.RELATION` | `CaplEftPayments_Relation` |  |  |  |
| 3 | `CAPL.EPAY.CURRENCY` | `CaplEftPayments_Currency` |  |  |  |
| 4 | `CAPL.EPAY.ISSUE.DATE` | `CaplEftPayments_IssueDate` |  |  |  |
| 5 | `CAPL.EPAY.POST.DATE` | `CaplEftPayments_PostDate` |  |  |  |
| 6 | `CAPL.EPAY.VALUE.DATE` | `CaplEftPayments_ValueDate` |  |  |  |
| 7 | `CAPL.EPAY.PAYMENT.AMT` | `CaplEftPayments_PaymentAmt` |  |  |  |
| 8 | `CAPL.EPAY.MINIMUM.AMT` | `CaplEftPayments_MinimumAmt` |  |  |  |
| 9 | `CAPL.EPAY.EXCESS.AMT` | `CaplEftPayments_ExcessAmt` |  |  |  |
| 10 | `CAPL.EPAY.PROVINCIAL.AMT` | `CaplEftPayments_ProvincialAmt` |  |  |  |
| 11 | `CAPL.EPAY.FEDERAL.AMT` | `CaplEftPayments_FederalAmt` |  |  |  |
| 12 | `CAPL.EPAY.NR.AMT` | `CaplEftPayments_NrAmt` |  |  |  |
| 13 | `CAPL.EPAY.TOTAL.AMT` | `CaplEftPayments_TotalAmt` |  |  |  |
| 14 | `CAPL.EPAY.NET.AMT` | `CaplEftPayments_NetAmt` |  |  |  |
| 15 | `CAPL.EPAY.NET.REF` | `CaplEftPayments_NetRef` |  |  |  |
| 16 | `CAPL.EPAY.PROV.REF` | `CaplEftPayments_ProvRef` |  |  |  |
| 17 | `CAPL.EPAY.FED.REF` | `CaplEftPayments_FedRef` |  |  |  |
| 18 | `CAPL.EPAY.NR.REF` | `CaplEftPayments_NrRef` |  |  |  |
| 19 | `CAPL.EPAY.INST.ID.NO` | `CaplEftPayments_InstIdNo` |  |  |  |
| 20 | `CAPL.EPAY.TRANSIT.NO` | `CaplEftPayments_TransitNo` |  |  |  |
| 21 | `CAPL.EPAY.PAYOR.AC.NO` | `CaplEftPayments_PayorAcNo` |  |  |  |
| 22 | `CAPL.EPAY.PAYOR.NAME` | `CaplEftPayments_PayorName` |  |  |  |
| 23 | `CAPL.EPAY.ORIG.CROSS.REF` | `CaplEftPayments_OrigCrossRef` |  |  |  |
| 24 | `CAPL.EPAY.PAYMENT.STATUS` | `CaplEftPayments_PaymentStatus` |  |  |  |
| 25 | `CAPL.EPAY.RESERVED.5` | `CaplEftPayments_Reserved5` |  |  |  |
| 26 | `CAPL.EPAY.RESERVED.4` | `CaplEftPayments_Reserved4` |  |  |  |
| 27 | `CAPL.EPAY.RESERVED.3` | `CaplEftPayments_Reserved3` |  |  |  |
| 28 | `CAPL.EPAY.RESERVED.2` | `CaplEftPayments_Reserved2` |  |  |  |
| 29 | `CAPL.EPAY.RESERVED.1` | `CaplEftPayments_Reserved1` |  |  |  |
| 30 | `CAPL.EPAY.LOCAL.REF` | `CaplEftPayments_LocalRef` |  |  |  |
| 31 | `CAPL.EPAY.OVERRIDE` | `CaplEftPayments_Override` |  |  |  |
