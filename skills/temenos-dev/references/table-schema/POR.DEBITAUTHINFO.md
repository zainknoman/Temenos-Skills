# POR.DEBITAUTHINFO — Table Schema

> Source: `INSERTS/I_F.POR.DEBITAUTHINFO` in `PP_DebitAuthorityService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPDI.CompanyID` | `PorDebitauthinfo_Companyid` |  |  |  |
| 2 | `PPPDI.FTNumber` | `PorDebitauthinfo_Ftnumber` |  |  |  |
| 3 | `PPPDI.SendingBank` | `PorDebitauthinfo_Sendingbank` |  |  |  |
| 4 | `PPPDI.DebitAccountLine` | `PorDebitauthinfo_Debitaccountline` |  |  |  |
| 5 | `PPPDI.DebitPartyLine1` | `PorDebitauthinfo_Debitpartyline1` |  |  |  |
| 6 | `PPPDI.CreditorID` | `PorDebitauthinfo_Creditorid` |  |  |  |
| 7 | `PPPDI.MandateReference` | `PorDebitauthinfo_Mandatereference` |  |  |  |
| 8 | `PPPDI.SignatureDate` | `PorDebitauthinfo_Signaturedate` |  |  |  |
| 9 | `PPPDI.ElectronicSignature` | `PorDebitauthinfo_Electronicsignature` |  |  |  |
| 10 | `PPPDI.AmendmentIndicator` | `PorDebitauthinfo_Amendmentindicator` |  |  |  |
| 11 | `PPPDI.OriginalMandateReference` | `PorDebitauthinfo_Originalmandatereference` |  |  |  |
| 12 | `PPPDI.OriginalCreditorName` | `PorDebitauthinfo_Originalcreditorname` |  |  |  |
| 13 | `PPPDI.OriginalCreditorID` | `PorDebitauthinfo_Originalcreditorid` |  |  |  |
| 14 | `PPPDI.OriginalCreditorSchProp` | `PorDebitauthinfo_Originalcreditorschprop` |  |  |  |
| 15 | `PPPDI.OriginalDebtorAccount` | `PorDebitauthinfo_Originaldebtoraccount` |  |  |  |
| 16 | `PPPDI.OriginalDebtorAgtBIC` | `PorDebitauthinfo_Originaldebtoragtbic` |  |  |  |
| 17 | `PPPDI.SequenceType` | `PorDebitauthinfo_Sequencetype` |  |  |  |
| 18 | `PPPDI.ServiceLevelCode` | `PorDebitauthinfo_Servicelevelcode` |  |  |  |
| 19 | `PPPDI.OriginalDebtorAcctOtherID` | `PorDebitauthinfo_Originaldebtoracctotherid` |  |  |  |
