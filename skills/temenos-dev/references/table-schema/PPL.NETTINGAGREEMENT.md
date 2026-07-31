# PPL.NETTINGAGREEMENT — Table Schema

> Source: `INSERTS/I_F.PPL.NETTINGAGREEMENT` in `PP_DebitAuthorityService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPNTA.CompanyID` | `PplNettingagreement_Companyid` |  |  |  |
| 2 | `PPNTA.IncomingMessageType` | `PplNettingagreement_Incomingmessagetype` |  |  |  |
| 3 | `PPNTA.SendingBank` | `PplNettingagreement_Sendingbank` |  |  |  |
| 4 | `PPNTA.DebitAccountLine` | `PplNettingagreement_Debitaccountline` |  |  |  |
| 5 | `PPNTA.DebitPartyLine1` | `PplNettingagreement_Debitpartyline1` |  |  |  |
| 6 | `PPNTA.StartDate` | `PplNettingagreement_Startdate` |  |  |  |
| 7 | `PPNTA.EndDate` | `PplNettingagreement_Enddate` |  |  |  |
| 8 | `PPNTA.RACNettingAgreement` | `PplNettingagreement_Racnettingagreement` |  |  |  |
| 9 | `PPNTA.RSCNettingAgreement` | `PplNettingagreement_Rscnettingagreement` |  |  |  |
| 10 | `PPNTA.EntryUserID` | `PplNettingagreement_Entryuserid` |  |  |  |
| 11 | `PPNTA.EntryDateTime` | `PplNettingagreement_Entrydatetime` |  |  |  |
| 12 | `PPNTA.ApproverUserID` | `PplNettingagreement_Approveruserid` |  |  |  |
| 13 | `PPNTA.ApprovedDateTime` | `PplNettingagreement_Approveddatetime` |  |  |  |
