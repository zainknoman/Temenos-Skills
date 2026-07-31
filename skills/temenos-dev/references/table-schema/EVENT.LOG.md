# EVENT.LOG — Table Schema

> Source: `INSERTS/I_F.EVENT.LOG` in `EB_AlertProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EVT.LG.TEC.ITEM` | `EventLog_TecItem` |  |  |  |
| 2 | `EVT.LG.REQUEST.REF` | `EventLog_RequestRef` |  |  |  |
| 3 | `EVT.LG.EB.ALERT.REF` | `EventLog_EbAlertRef` |  |  |  |
| 4 | `EVT.LG.DATE.TIME` | `EventLog_DateTime` |  |  |  |
| 5 | `EVT.LG.SUBSCRIBER` | `EventLog_Subscriber` |  |  |  |
| 6 | `EVT.LG.DELIVERY.REF` | `EventLog_DeliveryRef` |  |  |  |
| 7 | `EVT.LG.STATUS` | `EventLog_Status` |  |  |  |
| 8 | `EVT.LG.PRECEDENCE` | `EventLog_Precedence` |  |  |  |
| 9 | `EVT.LG.COMPANY` | `EventLog_Company` | TField |  | T24 Company |
| 10 | `EVT.LG.APPLICATION` | `EventLog_Application` | TField |  | T24 Application or job name |
| 11 | `EVT.LG.TOUCH.POINT.REF` | `EventLog_TouchPointRef` | TField |  | ID.NEW,CONTRACT$ID or Supplied by touch point |
