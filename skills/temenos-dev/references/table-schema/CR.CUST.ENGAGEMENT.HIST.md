# CR.CUST.ENGAGEMENT.HIST — Table Schema

> Source: `INSERTS/I_F.CR.CUST.ENGAGEMENT.HIST` in `CR_Analytical.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CR.CEH.DATE` | `CrCustEngagementHist_Date` |  |  |  |
| 2 | `CR.CEH.CUST.ENGAGEMENT.ID` | `CrCustEngagementHist_CustEngagementId` |  |  |  |
| 3 | `CR.CEH.RESERVED.10` | `CrCustEngagementHist_Reserved10` | TField |  |  |
| 4 | `CR.CEH.RESERVED.09` | `CrCustEngagementHist_Reserved09` | TField |  |  |
| 5 | `CR.CEH.RESERVED.08` | `CrCustEngagementHist_Reserved08` | TField |  |  |
| 6 | `CR.CEH.RESERVED.07` | `CrCustEngagementHist_Reserved07` | TField |  |  |
| 7 | `CR.CEH.RESERVED.06` | `CrCustEngagementHist_Reserved06` | TField |  |  |
| 8 | `CR.CEH.RESERVED.05` | `CrCustEngagementHist_Reserved05` | TField |  |  |
| 9 | `CR.CEH.RESERVED.04` | `CrCustEngagementHist_Reserved04` | TField |  |  |
| 10 | `CR.CEH.RESERVED.03` | `CrCustEngagementHist_Reserved03` | TField |  |  |
| 11 | `CR.CEH.RESERVED.02` | `CrCustEngagementHist_Reserved02` | TField |  |  |
| 12 | `CR.CEH.RESERVED.01` | `CrCustEngagementHist_Reserved01` | TField |  |  |
