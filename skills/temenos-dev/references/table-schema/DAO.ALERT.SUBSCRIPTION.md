# DAO.ALERT.SUBSCRIPTION — Table Schema

> Source: `INSERTS/I_F.DAO.ALERT.SUBSCRIPTION` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.DAS.EVENT` | `DaoAlertSubscription_Event` |  |  |  |
| 2 | `ST.DAS.FIELD` | `DaoAlertSubscription_Field` |  |  |  |
| 3 | `ST.DAS.OPERAND` | `DaoAlertSubscription_Operand` |  |  |  |
| 4 | `ST.DAS.VALUE` | `DaoAlertSubscription_Value` |  |  |  |
| 5 | `ST.DAS.MV.ALERT.RES6` | `DaoAlertSubscription_MvAlertRes6` |  |  |  |
| 6 | `ST.DAS.MV.ALERT.RES5` | `DaoAlertSubscription_MvAlertRes5` |  |  |  |
| 7 | `ST.DAS.MV.ALERT.RES4` | `DaoAlertSubscription_MvAlertRes4` |  |  |  |
| 8 | `ST.DAS.MV.ALERT.RES3` | `DaoAlertSubscription_MvAlertRes3` |  |  |  |
| 9 | `ST.DAS.MV.ALERT.RES2` | `DaoAlertSubscription_MvAlertRes2` |  |  |  |
| 10 | `ST.DAS.MV.ALERT.RES1` | `DaoAlertSubscription_MvAlertRes1` |  |  |  |
| 11 | `ST.DAS.REQUEST.ID` | `DaoAlertSubscription_RequestId` |  |  |  |
