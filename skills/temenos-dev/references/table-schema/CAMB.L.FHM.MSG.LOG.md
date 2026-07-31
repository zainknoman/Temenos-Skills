# CAMB.L.FHM.MSG.LOG — Table Schema

> Source: `INSERTS/I_F.CAMB.L.FHM.MSG.LOG` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.L.FHM.MSG.LOG.CARD.ISSUE.ID` | `CambLFhmMsgLog_CardIssueId` | TField |  |  |
| 2 | `CAMB.L.FHM.MSG.LOG.CARD.ACCESS.ID` | `CambLFhmMsgLog_CardAccessId` | TField |  |  |
| 3 | `CAMB.L.FHM.MSG.LOG.PAN.NO` | `CambLFhmMsgLog_PanNo` | TField |  |  |
| 4 | `CAMB.L.FHM.MSG.LOG.REQ.DATE.TIME` | `CambLFhmMsgLog_ReqDateTime` |  |  |  |
| 5 | `CAMB.L.FHM.MSG.LOG.FHM.POSTED.TIME` | `CambLFhmMsgLog_FhmPostedTime` |  |  |  |
| 6 | `CAMB.L.FHM.MSG.LOG.UPDATE.STATUS` | `CambLFhmMsgLog_UpdateStatus` |  |  |  |
| 7 | `CAMB.L.FHM.MSG.LOG.RESPONSE.CODE` | `CambLFhmMsgLog_ResponseCode` | TField |  |  |
| 8 | `CAMB.L.FHM.MSG.LOG.NO.OF.ATTEMPTS` | `CambLFhmMsgLog_NoOfAttempts` | TField |  |  |
| 9 | `CAMB.L.FHM.MSG.LOG.RESP.DATE.TIME` | `CambLFhmMsgLog_RespDateTime` |  |  |  |
