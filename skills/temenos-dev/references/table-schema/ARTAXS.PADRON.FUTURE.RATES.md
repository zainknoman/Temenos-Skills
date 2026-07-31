# ARTAXS.PADRON.FUTURE.RATES — Table Schema

> Source: `INSERTS/I_F.ARTAXS.PADRON.FUTURE.RATES` in `ARTAXS_ProcessPadrons.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARPDRN.TAX.PAYER.ID` | `ArtaxsPadronFutureRates_TaxPayerId` | TField |  | Contains the CUIT/CUIL/CDI of the valid customer. Will be identified from the 1st position of the file. |
| 2 | `ARPDRN.IS.CUSTOMER` | `ArtaxsPadronFutureRates_IsCustomer` | TField |  | Once the customer is on-boarded in T24, this field will be marked to identify this record as T24 customer’s record. |
| 3 | `ARPDRN.VAT.TAX` | `ArtaxsPadronFutureRates_VatTax` | TField |  | Array of Padron Details. |
| 4 | `ARPDRN.INCOME.TAX` | `ArtaxsPadronFutureRates_IncomeTax` | TField |  | Array of Padron Details. |
| 5 | `ARPDRN.TRANSACTION.TAX` | `ArtaxsPadronFutureRates_TransactionTax` | TField |  | Array of Padron Details. |
| 6 | `ARPDRN.TURNOVER.TAX.COLLECTION` | `ArtaxsPadronFutureRates_TurnoverTaxCollection` | TField |  | Array of Padron Details. |
| 7 | `ARPDRN.REVERSE.WITHHOLDING.TAX.PERC` | `ArtaxsPadronFutureRates_ReverseWithholdingTaxPerc` | TField |  | Array of Padron Details. |
| 8 | `ARPDRN.WITHHOLDING.TAX.DET.RETENTION` | `ArtaxsPadronFutureRates_WithholdingTaxDetRetention` | TField |  | Array of Padron Details. |
| 9 | `ARPDRN.AFIP.EXEMPTION` | `ArtaxsPadronFutureRates_AfipExemption` | TField |  | Array of Padron Details. |
| 10 | `ARPDRN.CONTRIB.AFIP` | `ArtaxsPadronFutureRates_ContribAfip` | TField |  | Indicate if a customer is in the padron Exempted Entities which means that the customer is completely exempted.Yes=Customer is fully exempted Null=Customer is not fully exempted. |
| 11 | `ARPDRN.EXEMPT.RG17` | `ArtaxsPadronFutureRates_ExemptRg17` |  |  |  |
| 12 | `ARPDRN.RG17.START.DATE` | `ArtaxsPadronFutureRates_Rg17StartDate` |  |  |  |
| 13 | `ARPDRN.RG17.END.DATE` | `ArtaxsPadronFutureRates_Rg17EndDate` |  |  |  |
| 14 | `ARPDRN.EXEMPT.RG17.VAL` | `ArtaxsPadronFutureRates_ExemptRg17Val` |  |  |  |
| 15 | `ARPDRN.EXEMPTED.ENTITY` | `ArtaxsPadronFutureRates_ExemptedEntity` | TField |  | Indicate if a customer is in the padron Exempted Entities which means that the customer is completely exempted. Yes=Customer is fully exempted Null=Customer is not fully exempted. |
| 16 | `ARPDRN.FISCAL.BENEFIT` | `ArtaxsPadronFutureRates_FiscalBenefit` | TField |  | Indicate if a customer is in the padron Fiscal Benefits Register which means that the customer is partially exempted. Yes=Customer is partially exempted Null=Customer is not partially exempted. |
| 17 | `ARPDRN.BENEFIT.START.DATE` | `ArtaxsPadronFutureRates_BenefitStartDate` |  |  |  |
| 18 | `ARPDRN.BENEFIT.END.DATE` | `ArtaxsPadronFutureRates_BenefitEndDate` |  |  |  |
| 19 | `ARPDRN.BENEFIT.CBU` | `ArtaxsPadronFutureRates_BenefitCbu` |  |  |  |
| 20 | `ARPDRN.BENEFIT.NUMBER` | `ArtaxsPadronFutureRates_BenefitNumber` |  |  |  |
| 21 | `ARPDRN.TO.EXEM.PADRON` | `ArtaxsPadronFutureRates_ToExemPadron` |  |  |  |
| 22 | `ARPDRN.TO.COLL.PADRON` | `ArtaxsPadronFutureRates_ToCollPadron` |  |  |  |
| 23 | `ARPDRN.COLL.START.DATE` | `ArtaxsPadronFutureRates_CollStartDate` |  |  |  |
| 24 | `ARPDRN.COLL.END.DATE` | `ArtaxsPadronFutureRates_CollEndDate` |  |  |  |
| 25 | `ARPDRN.COLL.PADRON.RATE` | `ArtaxsPadronFutureRates_CollPadronRate` |  |  |  |
| 26 | `ARPDRN.TO.ML.PADRON` | `ArtaxsPadronFutureRates_ToMlPadron` |  |  |  |
| 27 | `ARPDRN.CERTIFICATE.EXEMPTION` | `ArtaxsPadronFutureRates_CertificateExemption` | TField |  | When a manual certificate exemption is input this flag should be mark like YES. |
| 28 | `ARPDRN.CONTRIB.AFIP.INCOME` | `ArtaxsPadronFutureRates_ContribAfipIncome` | TField |  | Indicate if a customer has a record in AFIP Contributor�s padron. Possible values Yes or Null |
| 29 | `ARPDRN.IMP.INCOME` | `ArtaxsPadronFutureRates_ImpIncome` | TField |  | Indicate the value that the customer has in IMP GANANCIAS field inside AFIP Contributor�s padron. Possible values NI, N, AC, S, EX, NA, XN, AN, NC, or Null |
| 30 | `ARPDRN.EXEMPT.RG2681` | `ArtaxsPadronFutureRates_ExemptRg2681` |  |  |  |
| 31 | `ARPDRN.START.DATE.RG2681` | `ArtaxsPadronFutureRates_StartDateRg2681` |  |  |  |
| 32 | `ARPDRN.END.DATE.RG2681` | `ArtaxsPadronFutureRates_EndDateRg2681` |  |  |  |
| 33 | `ARPDRN.EXEMPT.RG830` | `ArtaxsPadronFutureRates_ExemptRg830` |  |  |  |
| 34 | `ARPDRN.START.DATE.RG830` | `ArtaxsPadronFutureRates_StartDateRg830` |  |  |  |
| 35 | `ARPDRN.END.DATE.RG830` | `ArtaxsPadronFutureRates_EndDateRg830` |  |  |  |
| 36 | `ARPDRN.EXEMPT.RG830.VAL` | `ArtaxsPadronFutureRates_ExemptRg830Val` |  |  |  |
| 37 | `ARPDRN.IMP.VAT` | `ArtaxsPadronFutureRates_ImpVat` | TField |  | Indicate the value that the customer has in IMP IVA field inside AFIP Contributor�s padron. Possible values: NI, EX, NA, XN, AN, AC, S |
| 38 | `ARPDRN.MONOTAX` | `ArtaxsPadronFutureRates_Monotax` | TField |  | Indicate the value that the customer has in MONOTRIBUTO field. |
| 39 | `ARPDRN.TO.SIRCREB` | `ArtaxsPadronFutureRates_ToSircreb` |  |  |  |
| 40 | `ARPDRN.TO.SIRCREB.START` | `ArtaxsPadronFutureRates_ToSircrebStart` |  |  |  |
| 41 | `ARPDRN.TO.SIRCREB.END` | `ArtaxsPadronFutureRates_ToSircrebEnd` |  |  |  |
| 42 | `ARPDRN.TO.SIRCREB.RATE` | `ArtaxsPadronFutureRates_ToSircrebRate` |  |  |  |
| 43 | `ARPDRN.LOCAL.REF` | `ArtaxsPadronFutureRates_LocalRef` |  |  |  |
| 44 | `ARPDRN.OVERRIDE` | `ArtaxsPadronFutureRates_Override` |  |  |  |
| 45 | `ARPDRN.RECORD.STATUS` | `ArtaxsPadronFutureRates_RecordStatus` | String |  |  |
| 46 | `ARPDRN.CURR.NO` | `ArtaxsPadronFutureRates_CurrNo` | String |  |  |
| 47 | `ARPDRN.INPUTTER` | `ArtaxsPadronFutureRates_Inputter` |  |  |  |
| 48 | `ARPDRN.DATE.TIME` | `ArtaxsPadronFutureRates_DateTime` |  |  |  |
| 49 | `ARPDRN.AUTHORISER` | `ArtaxsPadronFutureRates_Authoriser` | String |  |  |
| 50 | `ARPDRN.CO.CODE` | `ArtaxsPadronFutureRates_CoCode` | String |  |  |
| 51 | `ARPDRN.DEPT.CODE` | `ArtaxsPadronFutureRates_DeptCode` | String |  |  |
| 52 | `ARPDRN.AUDITOR.CODE` | `ArtaxsPadronFutureRates_AuditorCode` | String |  |  |
| 53 | `ARPDRN.AUDIT.DATE.TIME` | `ArtaxsPadronFutureRates_AuditDateTime` | String |  |  |
| 54 | `ARPDRN.TO.SIRCREB.JURISDICTION` | `ArtaxsPadronFutureRates_ToSircrebJurisdiction` |  |  |  |
| 55 | `ARPDRN.TO.PERCEPTION` | `ArtaxsPadronFutureRates_ToPerception` |  |  |  |
| 56 | `ARPDRN.TO.PERCEPTION.START` | `ArtaxsPadronFutureRates_ToPerceptionStart` |  |  |  |
| 57 | `ARPDRN.TO.PERCEPTION.END` | `ArtaxsPadronFutureRates_ToPerceptionEnd` |  |  |  |
| 58 | `ARPDRN.TO.PERCEPTION.RATE` | `ArtaxsPadronFutureRates_ToPerceptionRate` |  |  |  |
| 59 | `ARPDRN.TO.PERCEPTION.PADRON.JURIS` | `ArtaxsPadronFutureRates_ToPerceptionPadronJuris` |  |  |  |
| 60 | `ARPDRN.TO.EXEM.PADRON.MN` | `ArtaxsPadronFutureRates_ToExemPadronMn` | TField |  | Reserved for future use. |
| 61 | `ARPDRN.TO.EXEM.PADRON.MN.CBU` | `ArtaxsPadronFutureRates_ToExemPadronMnCbu` |  |  |  |
| 62 | `ARPDRN.TO.SIRCREB.CRC` | `ArtaxsPadronFutureRates_ToSircrebCrc` |  |  |  |
| 63 | `ARPDRN.TO.EXE.START.DATE` | `ArtaxsPadronFutureRates_ToExemStartDate` |  |  |  |
| 64 | `ARPDRN.TO.EXEM.END.DATE` | `ArtaxsPadronFutureRates_ToExemEndDate` |  |  |  |
| 65 | `ARPDRN.TO.EXEM.JURISDICTION` | `ArtaxsPadronFutureRates_ToExemJurisdiction` |  |  |  |
| 66 | `ARPDRN.TO.EXEMPTION.TAX` | `ArtaxsPadronFutureRates_ToExemptionTax` | TField |  | Array of Padron Details. |
| 67 | `ARPDRN.TO.SIRCREB.TAX` | `ArtaxsPadronFutureRates_ToSircrebTax` | TField |  | Array of Padron Details. |
| 68 | `ARPDRN.TO.PERCEPTION.TAX` | `ArtaxsPadronFutureRates_ToEPerceptionTax` |  |  |  |
