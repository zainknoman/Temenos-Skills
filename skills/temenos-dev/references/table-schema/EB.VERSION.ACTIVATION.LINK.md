# EB.VERSION.ACTIVATION.LINK — Table Schema

> Source: `INSERTS/I_F.EB.VERSION.ACTIVATION.LINK` in `EB_TransactionControl.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.AL.DESCRIPTION` | `EbVersionActivationLink_Description` |  |  |  |
| 2 | `EB.AL.QUEUE.SERVICE` | `EbVersionActivationLink_QueueService` |  |  |  |
| 3 | `EB.AL.QUEUE.NAME` | `EbVersionActivationLink_QueueName` |  |  |  |
| 4 | `EB.AL.QUEUE.ID` | `EbVersionActivationLink_QueueId` |  |  |  |
| 5 | `EB.AL.QUEUE.ID.POS` | `EbVersionActivationLink_QueueIdPos` |  |  |  |
| 6 | `EB.AL.QUEUE.MESSAGE` | `EbVersionActivationLink_QueueMessage` |  |  |  |
| 7 | `EB.AL.QUEUE.MESSAGE.POS` | `EbVersionActivationLink_QueueMessagePos` |  |  |  |
| 8 | `EB.AL.QUEUE.PRIORITY` | `EbVersionActivationLink_QueuePriority` |  |  |  |
| 9 | `EB.AL.EMIT.REVERSAL` | `EbVersionActivationLink_EmitReversal` |  |  |  |
| 10 | `EB.AL.RESERVEDFLD.10` | `EbVersionActivationLink_Reservedfld10` |  |  |  |
| 11 | `EB.AL.RESERVEDFLD.9` | `EbVersionActivationLink_Reservedfld9` |  |  |  |
| 12 | `EB.AL.RESERVEDFLD.8` | `EbVersionActivationLink_Reservedfld8` |  |  |  |
| 13 | `EB.AL.RESERVEDFLD.7` | `EbVersionActivationLink_Reservedfld7` |  |  |  |
| 14 | `EB.AL.RESERVEDFLD.6` | `EbVersionActivationLink_Reservedfld6` |  |  |  |
| 15 | `EB.AL.RESERVED.5` | `EbVersionActivationLink_Reserved5` | TField |  | Reserved for future use |
| 16 | `EB.AL.RESERVED.4` | `EbVersionActivationLink_Reserved4` | TField |  | Reserved for future use |
| 17 | `EB.AL.RESERVED.3` | `EbVersionActivationLink_Reserved3` | TField |  | Reserved for future use |
| 18 | `EB.AL.RESERVED.2` | `EbVersionActivationLink_Reserved2` | TField |  | Reserved for future use |
| 19 | `EB.AL.RESERVED.1` | `EbVersionActivationLink_Reserved1` | TField |  | Reserved for future use |
| 20 | `EB.AL.LOCAL.REF` | `EbVersionActivationLink_LocalRef` |  |  |  |
| 21 | `EB.AL.OVERRIDE` | `EbVersionActivationLink_Override` |  |  |  |
| 22 | `EB.AL.RECORD.STATUS` | `EbVersionActivationLink_RecordStatus` | String |  |  |
| 23 | `EB.AL.CURR.NO` | `EbVersionActivationLink_CurrNo` | String |  |  |
| 24 | `EB.AL.INPUTTER` | `EbVersionActivationLink_Inputter` |  |  |  |
| 25 | `EB.AL.DATE.TIME` | `EbVersionActivationLink_DateTime` |  |  |  |
| 26 | `EB.AL.AUTHORISER` | `EbVersionActivationLink_Authoriser` | String |  |  |
| 27 | `EB.AL.CO.CODE` | `EbVersionActivationLink_CoCode` | String |  |  |
| 28 | `EB.AL.DEPT.CODE` | `EbVersionActivationLink_DeptCode` | String |  |  |
| 29 | `EB.AL.AUDITOR.CODE` | `EbVersionActivationLink_AuditorCode` | String |  |  |
| 30 | `EB.AL.AUDIT.DATE.TIME` | `EbVersionActivationLink_AuditDateTime` | String |  |  |
