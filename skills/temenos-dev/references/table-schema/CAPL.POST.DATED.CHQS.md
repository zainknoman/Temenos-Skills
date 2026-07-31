# CAPL.POST.DATED.CHQS — Table Schema

> Source: `INSERTS/I_F.CAPL.POST.DATED.CHQS` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.PDC.CUSTOMER` | `CaplPostDatedChqs_Customer` |  |  |  |
| 2 | `CAPL.PDC.RELATION` | `CaplPostDatedChqs_Relation` |  |  |  |
| 3 | `CAPL.PDC.CHQ.NUMBER` | `CaplPostDatedChqs_ChqNumber` |  |  |  |
| 4 | `CAPL.PDC.ISSUED.DATE` | `CaplPostDatedChqs_IssuedDate` |  |  |  |
| 5 | `CAPL.PDC.POSTED.DATE` | `CaplPostDatedChqs_PostedDate` |  |  |  |
| 6 | `CAPL.PDC.VALUE.DATE` | `CaplPostDatedChqs_ValueDate` |  |  |  |
| 7 | `CAPL.PDC.CHQ.CURRENCY` | `CaplPostDatedChqs_ChqCurrency` |  |  |  |
| 8 | `CAPL.PDC.CHQ.AMOUNT` | `CaplPostDatedChqs_ChqAmount` |  |  |  |
| 9 | `CAPL.PDC.STATUS` | `CaplPostDatedChqs_Status` |  |  |  |
| 10 | `CAPL.PDC.RESERVED.12` | `CaplPostDatedChqs_Reserved12` |  |  |  |
| 11 | `CAPL.PDC.RESERVED.11` | `CaplPostDatedChqs_Reserved11` |  |  |  |
| 12 | `CAPL.PDC.INFO.TXN.REF` | `CaplPostDatedChqs_InfoTxnRef` |  |  |  |
| 13 | `CAPL.PDC.DELIVERY.REF` | `CaplPostDatedChqs_DeliveryRef` |  |  |  |
| 14 | `CAPL.PDC.RESERVED.10` | `CaplPostDatedChqs_Reserved10` |  |  |  |
| 15 | `CAPL.PDC.RESERVED.9` | `CaplPostDatedChqs_Reserved9` |  |  |  |
| 16 | `CAPL.PDC.RESERVED.8` | `CaplPostDatedChqs_Reserved8` |  |  |  |
| 17 | `CAPL.PDC.RESERVED.7` | `CaplPostDatedChqs_Reserved7` |  |  |  |
| 18 | `CAPL.PDC.RESERVED.6` | `CaplPostDatedChqs_Reserved6` |  |  |  |
| 19 | `CAPL.PDC.RESERVED.5` | `CaplPostDatedChqs_Reserved5` |  |  |  |
| 20 | `CAPL.PDC.RESERVED.4` | `CaplPostDatedChqs_Reserved4` |  |  |  |
| 21 | `CAPL.PDC.RESERVED.3` | `CaplPostDatedChqs_Reserved3` |  |  |  |
| 22 | `CAPL.PDC.RESERVED.2` | `CaplPostDatedChqs_Reserved2` |  |  |  |
| 23 | `CAPL.PDC.RESERVED.1` | `CaplPostDatedChqs_Reserved1` |  |  |  |
| 24 | `CAPL.PDC.LOCAL.REF` | `CaplPostDatedChqs_LocalRef` |  |  |  |
| 25 | `CAPL.PDC.OVERRIDE` | `CaplPostDatedChqs_Override` |  |  |  |
| 26 | `CAPL.PDC.RECORD.STATUS` | `CaplPostDatedChqs_RecordStatus` |  |  |  |
| 27 | `CAPL.PDC.CURR.NO` | `CaplPostDatedChqs_CurrNo` |  |  |  |
| 28 | `CAPL.PDC.INPUTTER` | `CaplPostDatedChqs_Inputter` |  |  |  |
| 29 | `CAPL.PDC.DATE.TIME` | `CaplPostDatedChqs_DateTime` |  |  |  |
| 30 | `CAPL.PDC.AUTHORISER` | `CaplPostDatedChqs_Authoriser` |  |  |  |
| 31 | `CAPL.PDC.CO.CODE` | `CaplPostDatedChqs_CoCode` |  |  |  |
| 32 | `CAPL.PDC.DEPT.CODE` | `CaplPostDatedChqs_DeptCode` |  |  |  |
| 33 | `CAPL.PDC.AUDITOR.CODE` | `CaplPostDatedChqs_AuditorCode` |  |  |  |
| 34 | `CAPL.PDC.AUDIT.DATE.TIME` | `CaplPostDatedChqs_AuditDateTime` |  |  |  |
