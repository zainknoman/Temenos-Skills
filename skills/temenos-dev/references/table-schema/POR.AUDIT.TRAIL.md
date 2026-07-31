# POR.AUDIT.TRAIL — Table Schema

> Source: `INSERTS/I_F.POR.AUDIT.TRAIL` in `PP_PaymentWorkflowGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PORAT.ERROR.TIME.STAMP` | `PorAuditTrail_ErrorTimeStamp` |  |  |  |
| 2 | `PORAT.ERROR.CODE` | `PorAuditTrail_ErrorCode` |  |  |  |
| 3 | `PORAT.ERROR.TYPE` | `PorAuditTrail_ErrorType` |  |  |  |
| 4 | `PORAT.ADDITIONAL.INFORMATION` | `PorAuditTrail_AdditionalInformation` |  |  |  |
| 5 | `PORAT.ACTIVE.FLAG` | `PorAuditTrail_ActiveFlag` |  |  |  |
| 6 | `PORAT.ORIGINATED.BY` | `PorAuditTrail_OriginatedBy` |  |  |  |
| 7 | `PORAT.EB.ERROR.OVERRIDE.ID` | `PorAuditTrail_EbErrorOverrideId` |  |  |  |
| 8 | `PORAT.RESERVED.2` | `PorAuditTrail_Reserved2` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 9 | `PORAT.RESERVED.3` | `PorAuditTrail_Reserved3` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 10 | `PORAT.RESERVED.4` | `PorAuditTrail_Reserved4` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 11 | `PORAT.RESERVED.5` | `PorAuditTrail_Reserved5` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 12 | `PORAT.HISTORY.TIME.STAMP` | `PorAuditTrail_HistoryTimeStamp` |  |  |  |
| 13 | `PORAT.EVENT.TYPE` | `PorAuditTrail_EventType` |  |  |  |
| 14 | `PORAT.EVENT.DESCRIPTION` | `PorAuditTrail_EventDescription` |  |  |  |
| 15 | `PORAT.HL.ERROR.CODE` | `PorAuditTrail_HlErrorCode` |  |  |  |
| 16 | `PORAT.HL.ADDITIONAL.INFORMATION` | `PorAuditTrail_HlAdditionalInformation` |  |  |  |
| 17 | `PORAT.RESERVED.6` | `PorAuditTrail_Reserved6` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 18 | `PORAT.RESERVED.7` | `PorAuditTrail_Reserved7` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 19 | `PORAT.RESERVED.8` | `PorAuditTrail_Reserved8` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 20 | `PORAT.RESERVED.9` | `PorAuditTrail_Reserved9` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 21 | `PORAT.RESERVED.10` | `PorAuditTrail_Reserved10` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 22 | `PORAT.TIME.STAMP` | `PorAuditTrail_TimeStamp` |  |  |  |
| 23 | `PORAT.STATUS.CODE` | `PorAuditTrail_StatusCode` |  |  |  |
| 24 | `PORAT.PROCESSED.INDICATOR` | `PorAuditTrail_ProcessedIndicator` |  |  |  |
| 25 | `PORAT.TT.INDICATOR` | `PorAuditTrail_TtIndicator` |  |  |  |
| 26 | `PORAT.WEIGHT.CODE` | `PorAuditTrail_WeightCode` |  |  |  |
| 27 | `PORAT.SPECIFIC.WEIGHT.CODE` | `PorAuditTrail_SpecificWeightCode` |  |  |  |
| 28 | `PORAT.PROCESS.ID` | `PorAuditTrail_ProcessId` |  |  |  |
| 29 | `PORAT.RESERVED.11` | `PorAuditTrail_Reserved11` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 30 | `PORAT.RESERVED.12` | `PorAuditTrail_Reserved12` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 31 | `PORAT.RESERVED.13` | `PorAuditTrail_Reserved13` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 32 | `PORAT.RESERVED.14` | `PorAuditTrail_Reserved14` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
| 33 | `PORAT.RESERVED.15` | `PorAuditTrail_Reserved15` | TField |  | Reserverd field for future use. Not Valid. Not Applicable. Not Applicable. |
