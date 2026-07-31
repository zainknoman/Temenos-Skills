# CZ.ACTIVE.ERASURE.DETAILS — Table Schema

> Source: `INSERTS/I_F.CZ.ACTIVE.ERASURE.DETAILS` in `CZ_ErasureProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CZ.AED.CUSTOMER` | `CzActiveErasureDetails_Customer` | TField |  | This field contains the customer to whom the erased contract belongs. |
| 2 | `CZ.AED.COMPANY` | `CzActiveErasureDetails_Company` | TField |  | The lead company to which the erased contract belongs. |
| 3 | `CZ.AED.CONTRACT.ID` | `CzActiveErasureDetails_ContractId` | TField |  | The ID of the erased contract. |
| 4 | `CZ.AED.CONTRACT.APPLN` | `CzActiveErasureDetails_ContractAppln` | TField |  | The field contains the application of the erased contract. |
| 5 | `CZ.AED.REQUEST.CAPTURE.ID` | `CzActiveErasureDetails_RequestCaptureId` |  |  |  |
| 6 | `CZ.AED.PURPOSE` | `CzActiveErasureDetails_Purpose` |  |  |  |
| 7 | `CZ.AED.RET.PERIOD.USED` | `CzActiveErasureDetails_RetPeriodUsed` |  |  |  |
| 8 | `CZ.AED.ERASURE.DATE` | `CzActiveErasureDetails_ErasureDate` |  |  |  |
| 9 | `CZ.AED.STATUS` | `CzActiveErasureDetails_Status` |  |  |  |
| 10 | `CZ.AED.REQ.CAP.RESERVED.10` | `CzActiveErasureDetails_ReqCapReserved10` |  |  |  |
| 11 | `CZ.AED.REQ.CAP.RESERVED.09` | `CzActiveErasureDetails_ReqCapReserved09` |  |  |  |
| 12 | `CZ.AED.REQ.CAP.RESERVED.08` | `CzActiveErasureDetails_ReqCapReserved08` |  |  |  |
| 13 | `CZ.AED.REQ.CAP.RESERVED.07` | `CzActiveErasureDetails_ReqCapReserved07` |  |  |  |
| 14 | `CZ.AED.REQ.CAP.RESERVED.06` | `CzActiveErasureDetails_ReqCapReserved06` |  |  |  |
| 15 | `CZ.AED.REQ.CAP.RESERVED.05` | `CzActiveErasureDetails_ReqCapReserved05` |  |  |  |
| 16 | `CZ.AED.REQ.CAP.RESERVED.04` | `CzActiveErasureDetails_ReqCapReserved04` |  |  |  |
| 17 | `CZ.AED.REQ.CAP.RESERVED.03` | `CzActiveErasureDetails_ReqCapReserved03` |  |  |  |
| 18 | `CZ.AED.REQ.CAP.RESERVED.02` | `CzActiveErasureDetails_ReqCapReserved02` |  |  |  |
| 19 | `CZ.AED.REQ.CAP.RESERVED.01` | `CzActiveErasureDetails_ReqCapReserved01` |  |  |  |
| 20 | `CZ.AED.OTHER.PURPOSES` | `CzActiveErasureDetails_OtherPurposes` |  |  |  |
| 21 | `CZ.AED.OVERALL.ERASURE.STATUS` | `CzActiveErasureDetails_OverallErasureStatus` | TField |  | The overall erasure status of the contract. The various statuses are: TO.BE.ERASED - When erasure has not started and there are triggers available for the erasure of the contract. IN.PROGRESS - When some of the purposes are erased and the remainsing erasure triggers are still present in the system. ERASED - when all the purposes attached to the application are erased. |
| 22 | `CZ.AED.CONTRACT.COMPLETION.DATE` | `CzActiveErasureDetails_ContractCompletionDate` | TField |  | This field hold the Date on when the contract Ends |
| 23 | `CZ.AED.RESERVED.14` | `CzActiveErasureDetails_Reserved14` | TField |  |  |
| 24 | `CZ.AED.RESERVED.13` | `CzActiveErasureDetails_Reserved13` | TField |  |  |
| 25 | `CZ.AED.RESERVED.12` | `CzActiveErasureDetails_Reserved12` | TField |  |  |
| 26 | `CZ.AED.RESERVED.11` | `CzActiveErasureDetails_Reserved11` | TField |  |  |
| 27 | `CZ.AED.RESERVED.10` | `CzActiveErasureDetails_Reserved10` | TField |  |  |
| 28 | `CZ.AED.RESERVED.09` | `CzActiveErasureDetails_Reserved09` | TField |  |  |
| 29 | `CZ.AED.RESERVED.08` | `CzActiveErasureDetails_Reserved08` | TField |  |  |
| 30 | `CZ.AED.RESERVED.07` | `CzActiveErasureDetails_Reserved07` | TField |  |  |
| 31 | `CZ.AED.RESERVED.06` | `CzActiveErasureDetails_Reserved06` | TField |  |  |
| 32 | `CZ.AED.RESERVED.05` | `CzActiveErasureDetails_Reserved05` | TField |  |  |
| 33 | `CZ.AED.RESERVED.04` | `CzActiveErasureDetails_Reserved04` | TField |  |  |
| 34 | `CZ.AED.RESERVED.03` | `CzActiveErasureDetails_Reserved03` | TField |  |  |
| 35 | `CZ.AED.RESERVED.02` | `CzActiveErasureDetails_Reserved02` | TField |  |  |
| 36 | `CZ.AED.RESERVED.01` | `CzActiveErasureDetails_Reserved01` | TField |  |  |
