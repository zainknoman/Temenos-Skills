# HUGIRO.PRENOTIFICATION.REPORT — Table Schema

> Source: `INSERTS/I_F.HUGIRO.PRENOTIFICATION.REPORT` in `HUGIRO_IG2SettlementReports.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HU.PRENOTE.CREATION.DATE.TIME` | `HugiroPrenotificationReport_CreationDateTime` |  |  |  |
| 2 | `HU.PRENOTE.SETTLEMENT.DATE` | `HugiroPrenotificationReport_SettlementDate` | TField |  | It is the settlement date for which IG2 is sending this report. |
| 3 | `HU.PRENOTE.MESSAGE.SOURCE` | `HugiroPrenotificationReport_MessageSource` |  |  |  |
| 4 | `HU.PRENOTE.SESSION.NUMBER` | `HugiroPrenotificationReport_SessionNumber` | TField |  | It is the session number for which IG2 is preparing the report. 1 is for the first session, 2 for the second etc. |
| 5 | `HU.PRENOTE.SESSION.ID` | `HugiroPrenotificationReport_SessionId` | TField |  | It is the session ID. |
| 6 | `HU.PRENOTE.RECEIVED.BIC` | `HugiroPrenotificationReport_ReceivedBic` | TField |  | It is the SWIFT BIC of the direct clearing member that receives this report. |
| 7 | `HU.PRENOTE.RECEIVED.BANK.CODE` | `HugiroPrenotificationReport_ReceivedBankCode` | TField |  | It is the bank code of the direct. |
| 8 | `HU.PRENOTE.NET.AMOUNT` | `HugiroPrenotificationReport_NetAmount` | TField |  | NetAmount is the net amount and currency (always HUF) of CTs and RCTs for the specific clearing session identified above, Net amount is always a signed integer or 0, it is the difference between the amount to be received and the sent gross amount to be cleared. NetAmt= amount to be received - GrossAmt. |
| 9 | `HU.PRENOTE.GROSS.AMOUNT` | `HugiroPrenotificationReport_GrossAmount` | TField |  | It is the sent gross amount of CTs and RCTs to be cleared and currency (always HUF) for the specific clearing session identified above. |
| 10 | `HU.PRENOTE.GROSS.NUMBER` | `HugiroPrenotificationReport_GrossNumber` | TField |  | It is the number of sent, accepted CTs and RCTs to be cleared in that session. The GrossAmount and GrossNumber indicate the number and amounts of all HCTs, both the HCTs sent in this session and those rolled over from previous session(s). |
