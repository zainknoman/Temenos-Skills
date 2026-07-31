# XML.OUTPUT.MSG — Table Schema

> Source: `INSERTS/I_F.XML.OUTPUT.MSG` in `IX_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `XML.OUT.MSG.DATE` | `XmlOutputMsg_MsgDate` | TField |  | MSG.DATE Date on which the CAMT request was processed Statement frequency date if request was given from ACCOUNT.STATEMENT application Creation date if request was from DE.STATEMENT.REQUEST application |
| 2 | `XML.OUT.MESSAGE` | `XmlOutputMsg_Message` | TField |  |  |
| 3 | `XML.OUT.ACCOUNT.NUMBER` | `XmlOutputMsg_AccountNumber` | TField |  | ACCOUNT.NUMBER The account number for which the statement is being generated |
| 4 | `XML.OUT.CUSTOMER` | `XmlOutputMsg_Customer` | TField |  | CUSTOMER The customer number for the carrier address customer |
| 5 | `XML.OUT.STMT.FREQ` | `XmlOutputMsg_StmtFreq` | TField |  | STMT.FREQ The statement cycle for which the camt message is being generated. |
| 6 | `XML.OUT.RECIPIENT.ADDRESS` | `XmlOutputMsg_RecipientAddress` | TField |  | RECIPIENT.ADDRESS Holds the DE.ADDRESS record id, for the recipient of the camt message or the external recipient address used by local development. |
| 7 | `XML.OUT.AC.XML.STMT.ID` | `XmlOutputMsg_AcXmlStmtId` | TField |  | AC.XML.STMT.ID Holds the AC.XML.STMT.DATA record id, for the camt message. |
| 8 | `XML.OUT.RESERVED.10` | `XmlOutputMsg_Reserved10` | TField |  |  |
| 9 | `XML.OUT.RESERVED.09` | `XmlOutputMsg_Reserved09` | TField |  |  |
| 10 | `XML.OUT.RESERVED.08` | `XmlOutputMsg_Reserved08` | TField |  |  |
| 11 | `XML.OUT.RESERVED.07` | `XmlOutputMsg_Reserved07` | TField |  |  |
| 12 | `XML.OUT.RESERVED.06` | `XmlOutputMsg_Reserved06` | TField |  |  |
| 13 | `XML.OUT.RESERVED.05` | `XmlOutputMsg_Reserved05` | TField |  |  |
| 14 | `XML.OUT.RESERVED.04` | `XmlOutputMsg_Reserved04` | TField |  |  |
| 15 | `XML.OUT.RESERVED.03` | `XmlOutputMsg_Reserved03` | TField |  |  |
| 16 | `XML.OUT.RESERVED.02` | `XmlOutputMsg_Reserved02` | TField |  |  |
| 17 | `XML.OUT.RESERVED.01` | `XmlOutputMsg_Reserved01` | TField |  |  |
