# ALLIANCE.LOG.DETAILS — Table Schema

> Source: `INSERTS/I_F.ALLIANCE.LOG.DETAILS` in `SWFTAL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ALLIANCE.LOG.CONNECTION.TYPE` | `AllianceLogDetails_ConnectionType` | TField |  | It specifies the messages as INBOUND/OUTBOUND. |
| 2 | `ALLIANCE.LOG.CREATION.DATE` | `AllianceLogDetails_CreationDate` | TField |  | It specifies the Date of creation. |
| 3 | `ALLIANCE.LOG.TIME.STAMP` | `AllianceLogDetails_TimeStamp` | TField |  |  |
| 4 | `ALLIANCE.LOG.MSG.DETAIL` | `AllianceLogDetails_MsgDetail` |  |  |  |
| 5 | `ALLIANCE.LOG.DELIVERY.ID` | `AllianceLogDetails_DeliveryId` | TField |  | It contains the @ID of DE.O.HEADER record. |
| 6 | `ALLIANCE.LOG.CUS.COMPANY` | `AllianceLogDetails_CusCompany` | TField |  | It contains the company id of customer used in the DE.O.HEADER |
| 7 | `ALLIANCE.LOG.ERROR.DETAILS` | `AllianceLogDetails_ErrorDetails` | TField |  |  |
| 8 | `ALLIANCE.LOG.RESERVED.2` | `AllianceLogDetails_Reserved2` | TField |  |  |
| 9 | `ALLIANCE.LOG.RESERVED.1` | `AllianceLogDetails_Reserved1` | TField |  |  |
