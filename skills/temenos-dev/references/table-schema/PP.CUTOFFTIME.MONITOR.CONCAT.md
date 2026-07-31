# PP.CUTOFFTIME.MONITOR.CONCAT — Table Schema

> Source: `INSERTS/I_F.PP.CUTOFFTIME.MONITOR.CONCAT` in `PP_InquiryGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CM.CompanyID` | `PpCutofftimeMonitorConcat_Companyid` | TField |  |  |
| 2 | `PP.CM.CutoffTime` | `PpCutofftimeMonitorConcat_Cutofftime` | TField |  |  |
| 3 | `PP.CM.Name` | `PpCutofftimeMonitorConcat_Name` | TField |  |  |
| 4 | `PP.CM.TransactionCurrencyCode` | `PpCutofftimeMonitorConcat_Transactioncurrencycode` | TField |  |  |
| 5 | `PP.CM.TransactionAmount` | `PpCutofftimeMonitorConcat_Transactionamount` | TField |  |  |
| 6 | `PP.CM.TransactionAmountHome` | `PpCutofftimeMonitorConcat_Transactionamounthome` | TField |  |  |
| 7 | `PP.CM.TransferAndMessageType` | `PpCutofftimeMonitorConcat_Transferandmessagetype` | TField |  |  |
| 8 | `PP.CM.HomeCurrency` | `PpCutofftimeMonitorConcat_Homecurrency` | TField |  |  |
| 9 | `PP.CM.NumberofRecords` | `PpCutofftimeMonitorConcat_Numberofrecords` | TField |  |  |
| 10 | `PP.CM.ChannelName` | `PpCutofftimeMonitorConcat_Channelname` | TField |  |  |
| 11 | `PP.CM.ReocrdIDS` | `PpCutofftimeMonitorConcat_Reocrdids` | TField |  |  |
