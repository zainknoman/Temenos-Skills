# AC.XML.INTERIM.STMT.HIST — Table Schema

> Source: `INSERTS/I_F.AC.XML.INTERIM.STMT.HIST` in `IX_XmlStmtPrinting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.XML.INWARD.REF` | `AcXmlInterimStmtHist_InwardRef` | TField |  | INWARD.REF This field holds the inward reference from DE.STATEMENT.REQUEST application It will be updated only when the request for CAMT052 comes from DE.STATEMENT.REQUEST |
| 2 | `AC.XML.XML.OUTPUT.REF` | `AcXmlInterimStmtHist_XmlOutputRef` |  |  |  |
| 3 | `AC.XML.NO.ENTRIES` | `AcXmlInterimStmtHist_NoEntries` | TField |  | Number of entries This field holds the number of entries for the CAMT052 |
| 4 | `AC.XML.RESERVED.15` | `AcXmlInterimStmtHist_Reserved15` | TField |  |  |
| 5 | `AC.XML.RESERVED.14` | `AcXmlInterimStmtHist_Reserved14` | TField |  |  |
| 6 | `AC.XML.RESERVED.13` | `AcXmlInterimStmtHist_Reserved13` | TField |  |  |
| 7 | `AC.XML.RESERVED.12` | `AcXmlInterimStmtHist_Reserved12` | TField |  |  |
| 8 | `AC.XML.RESERVED.11` | `AcXmlInterimStmtHist_Reserved11` | TField |  |  |
| 9 | `AC.XML.RESERVED.10` | `AcXmlInterimStmtHist_Reserved10` | TField |  |  |
| 10 | `AC.XML.RESERVED.09` | `AcXmlInterimStmtHist_Reserved09` | TField |  |  |
| 11 | `AC.XML.RESERVED.08` | `AcXmlInterimStmtHist_Reserved08` | TField |  |  |
| 12 | `AC.XML.RESERVED.07` | `AcXmlInterimStmtHist_Reserved07` | TField |  |  |
| 13 | `AC.XML.RESERVED.06` | `AcXmlInterimStmtHist_Reserved06` | TField |  |  |
| 14 | `AC.XML.RESERVED.05` | `AcXmlInterimStmtHist_Reserved05` | TField |  |  |
| 15 | `AC.XML.RESERVED.04` | `AcXmlInterimStmtHist_Reserved04` | TField |  |  |
| 16 | `AC.XML.RESERVED.03` | `AcXmlInterimStmtHist_Reserved03` | TField |  |  |
| 17 | `AC.XML.RESERVED.02` | `AcXmlInterimStmtHist_Reserved02` | TField |  |  |
| 18 | `AC.XML.RESERVED.01` | `AcXmlInterimStmtHist_Reserved01` | TField |  |  |
| 19 | `AC.XML.RECORD.STATUS` | `AcXmlInterimStmtHist_RecordStatus` | String |  |  |
| 20 | `AC.XML.CURR.NO` | `AcXmlInterimStmtHist_CurrNo` | String |  |  |
| 21 | `AC.XML.INPUTTER` | `AcXmlInterimStmtHist_Inputter` |  |  |  |
| 22 | `AC.XML.DATE.TIME` | `AcXmlInterimStmtHist_DateTime` |  |  |  |
| 23 | `AC.XML.AUTHORISER` | `AcXmlInterimStmtHist_Authoriser` | String |  |  |
| 24 | `AC.XML.CO.CODE` | `AcXmlInterimStmtHist_CoCode` | String |  |  |
| 25 | `AC.XML.DEPT.CODE` | `AcXmlInterimStmtHist_DeptCode` | String |  |  |
| 26 | `AC.XML.AUDITOR.CODE` | `AcXmlInterimStmtHist_AuditorCode` | String |  |  |
| 27 | `AC.XML.AUDIT.DATE.TIME` | `AcXmlInterimStmtHist_AuditDateTime` | String |  |  |
