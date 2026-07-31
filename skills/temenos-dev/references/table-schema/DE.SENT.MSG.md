# DE.SENT.MSG — Table Schema

> Source: `INSERTS/I_F.DE.SENT.MSG` in `PP_SwiftOutService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DSM.CompanyID` | `DeSentMsg_Companyid` |  |  |  |
| 2 | `DSM.FtNumber` | `DeSentMsg_Ftnumber` |  |  |  |
| 3 | `DSM.SenderReference` | `DeSentMsg_Senderreference` |  |  |  |
| 4 | `DSM.MsgType` | `DeSentMsg_Msgtype` |  |  |  |
| 5 | `DSM.SendingBIC` | `DeSentMsg_Sendingbic` |  |  |  |
| 6 | `DSM.OVERRIDE` | `DeSentMsg_Override` |  |  |  |
