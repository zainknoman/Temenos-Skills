# ID.PDS.ACTION.STATUS — Table Schema

> Source: `INSERTS/I_F.ID.PDS.ACTION.STATUS` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IPS.STATUS` | `IdPdsActionStatus_Status` | TField |  | This field will hold the date in which the settlement account payment or repayment of arrangement happened. Validation Rules: 1. Allowed values are SUBMIT, STARTED, INPROGRESS, COMPLETE and ERROR. |
| 2 | `ID.IPS.PDS.ACTION.ID` | `IdPdsActionStatus_PdsActionId` | TField |  | It is the record id of the ID.PDS.ACTION for which the status is updated. |
| 3 | `ID.IPS.NEW.ACTION.REF` | `IdPdsActionStatus_NewActionRef` | TField |  | This field will be update with the new ID.PDS.ACTION for a previous distributed ID.PDS.ACTION marked for reverse and redistribution. |
| 4 | `ID.IPS.RESERVED.3` | `IdPdsActionStatus_Reserved3` |  |  |  |
| 5 | `ID.IPS.RESERVED.2` | `IdPdsActionStatus_Reserved2` |  |  |  |
| 6 | `ID.IPS.RESERVED.1` | `IdPdsActionStatus_Reserved1` | TField |  |  |
