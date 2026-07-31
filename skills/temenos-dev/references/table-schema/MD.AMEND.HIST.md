# MD.AMEND.HIST — Table Schema

> Source: `INSERTS/I_F.MD.AMEND.HIST` in `MD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MD.AMD.MT767.AMENDMENT.NO` | `MdAmendHist_MtSevSixSevAmendmenNo` |  |  |  |
| 2 | `MD.AMD.AMENDMENT.DATE` | `MdAmendHist_AmendmentDate` |  |  |  |
| 3 | `MD.AMD.MT767.OUT.PURP.OF.MSG` | `MdAmendHist_MtSevSixSevOutPurpOfMsg` |  |  |  |
| 4 | `MD.AMD.MT767.IN.PURP.OF.MSG` | `MdAmendHist_MtSevSixSevInPurpOfMsg` |  |  |  |
| 5 | `MD.AMD.CANCELLATION.REQUEST` | `MdAmendHist_CancellationRequest` |  |  |  |
| 6 | `MD.AMD.MT767.SENDER.INFO` | `MdAmendHist_MtSevSixSevSenderInfo` |  |  |  |
| 7 | `MD.AMD.MT767.FILE.IDENTIFICATION` | `MdAmendHist_MtSevSixSevFileIdentification` |  |  |  |
| 8 | `MD.AMD.INC.DEC.AMOUNT` | `MdAmendHist_IncDecAmount` |  |  |  |
| 9 | `MD.AMD.MT767.EXPIRY.TYPE` | `MtSevSixSevExpiryType` |  |  |  |
| 10 | `MD.AMD.MT767.ADVICE.EXPIRY.DATE` | `MdAmendHist_MtSevSixSevAdviceExpiryDate` |  |  |  |
| 11 | `MD.AMD.MT767.EXPIRY.EVENT` | `MdAmendHist_MtSevSixSevExpiryEvent` |  |  |  |
| 12 | `MD.AMD.MT767.BENEF.CUST.1` | `MdAmendHist_MtSevSixSevBenefCust1` |  |  |  |
| 13 | `MD.AMD.MT767.BEN.ADDRESS` | `MdAmendHist_MtSevSixSevBenAddress` |  |  |  |
| 14 | `MD.AMD.MT767.UNDK.TERM.COND` | `MdAmendHist_MtSevSixSevUndkTermCond` |  |  |  |
| 15 | `MD.AMD.MT767.DELIVERY.ORG.UNDK` | `MdAmendHist_MtSevSixSevDeliveryOrgUndk` |  |  |  |
| 16 | `MD.AMD.MT767.DELIVERY.TO.COLL.BY` | `MdAmendHist_MtSevSixSevDeliveryToCollBy` |  |  |  |
| 17 | `MD.AMD.MT767.C.INC.DEC.AMOUNT` | `MdAmendHist_MtSevSixSevCIncDecAmount` |  |  |  |
| 18 | `MD.AMD.MT767.C.EXPIRY.TYPE` | `MdAmendHist_MtSevSixSevCExpiryType` |  |  |  |
| 19 | `MD.AMD.MT767.C.ADVICE.EXPIRY.DATE` | `MdAmendHist_MtSevSixSevCAdviceExpiryDate` |  |  |  |
| 20 | `MD.AMD.MT767.C.EXPIRY.EVENT` | `MdAmendHist_MtSevSixSevCExpiryEvent` |  |  |  |
| 21 | `MD.AMD.MT767.C.BENEF.CUST.1` | `MdAmendHist_MtSevSixSevCBenefCust1` |  |  |  |
| 22 | `MD.AMD.MT767.C.BEN.ADDRESS` | `MdAmendHist_MtSevSixSevCBenAddress` |  |  |  |
| 23 | `MD.AMD.MT767.C.UNDK.TERM.COND` | `MdAmendHist_MtSevSixSevCUndkTermCond` |  |  |  |
| 24 | `MD.AMD.MT767.C.DELIVERY.ORG.UNDK` | `MdAmendHist_MtSevSixSevCDeliveryOrgUndk` |  |  |  |
| 25 | `MD.AMD.MT767.C.DELIVERY.TO.COLL.BY` | `MdAmendHist_MtSevSixSevCDeliveryToCollBy` |  |  |  |
| 26 | `MD.AMD.AMENDMENT.STATUS` | `MdAmendHist_AmendmentStatus` |  |  |  |
| 27 | `MD.AMD.RESERVED.1` | `MdAmendHist_Reserved1` |  |  |  |
| 28 | `MD.AMD.RESERVED.2` | `MdAmendHist_Reserved2` |  |  |  |
| 29 | `MD.AMD.RESERVED.3` | `MdAmendHist_Reserved3` |  |  |  |
| 30 | `MD.AMD.RESERVED.4` | `MdAmendHist_Reserved4` |  |  |  |
| 31 | `MD.AMD.RESERVED.5` | `MdAmendHist_Reserved5` |  |  |  |
| 32 | `MD.AMD.RESERVED.6` | `MdAmendHist_Reserved6` |  |  |  |
| 33 | `MD.AMD.RESERVED.7` | `MdAmendHist_Reserved7` |  |  |  |
| 34 | `MD.AMD.RESERVED.8` | `MdAmendHist_Reserved8` |  |  |  |
| 35 | `MD.AMD.RESERVED.9` | `MdAmendHist_Reserved9` |  |  |  |
| 36 | `MD.AMD.RESERVED.10` | `MdAmendHist_Reserved10` |  |  |  |
| 37 | `MD.AMD.RESERVED.11` | `MdAmendHist_Reserved11` | TField |  |  |
| 38 | `MD.AMD.RESERVED.12` | `MdAmendHist_Reserved12` | TField |  |  |
| 39 | `MD.AMD.RESERVED.13` | `MdAmendHist_Reserved13` | TField |  |  |
| 40 | `MD.AMD.RESERVED.14` | `MdAmendHist_Reserved14` | TField |  |  |
| 41 | `MD.AMD.RESERVED.15` | `MdAmendHist_Reserved15` | TField |  |  |
| 42 | `MD.AMD.RESERVED.16` | `MdAmendHist_Reserved16` | TField |  |  |
| 43 | `MD.AMD.RESERVED.17` | `MdAmendHist_Reserved17` | TField |  |  |
| 44 | `MD.AMD.RESERVED.18` | `MdAmendHist_Reserved18` | TField |  |  |
| 45 | `MD.AMD.RESERVED.19` | `MdAmendHist_Reserved19` | TField |  |  |
| 46 | `MD.AMD.RESERVED.20` | `MdAmendHist_Reserved20` | TField |  |  |
