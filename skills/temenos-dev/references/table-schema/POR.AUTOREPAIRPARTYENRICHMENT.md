# POR.AUTOREPAIRPARTYENRICHMENT — Table Schema

> Source: `INSERTS/I_F.POR.AUTOREPAIRPARTYENRICHMENT` in `PP_AutomatedRepairToolService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPARP.CompanyID` | `PorAutorepairpartyenrichment_Companyid` |  |  |  |
| 2 | `PPARP.FTNumber` | `PorAutorepairpartyenrichment_Ftnumber` |  |  |  |
| 3 | `PPARP.PartyRole` | `PorAutorepairpartyenrichment_Partyrole` |  |  |  |
| 4 | `PPARP.PartyRoleIndicator` | `PorAutorepairpartyenrichment_Partyroleindicator` |  |  |  |
| 5 | `PPARP.PartyInformationTag` | `PorAutorepairpartyenrichment_Partyinformationtag` |  |  |  |
| 6 | `PPARP.PartyNationalId` | `PorAutorepairpartyenrichment_Partynationalid` |  |  |  |
| 7 | `PPARP.PartyIdentifierCode` | `PorAutorepairpartyenrichment_Partyidentifiercode` |  |  |  |
| 8 | `PPARP.PartyAccountLine` | `PorAutorepairpartyenrichment_Partyaccountline` |  |  |  |
| 9 | `PPARP.PartyFreeLine1` | `PorAutorepairpartyenrichment_Partyfreeline1` |  |  |  |
| 10 | `PPARP.PartyFreeLine2` | `PorAutorepairpartyenrichment_Partyfreeline2` |  |  |  |
| 11 | `PPARP.PartyFreeLine3` | `PorAutorepairpartyenrichment_Partyfreeline3` |  |  |  |
| 12 | `PPARP.PartyFreeLine4` | `PorAutorepairpartyenrichment_Partyfreeline4` |  |  |  |
| 13 | `PPARP.DirectPaymentFlag` | `PorAutorepairpartyenrichment_Directpaymentflag` |  |  |  |
