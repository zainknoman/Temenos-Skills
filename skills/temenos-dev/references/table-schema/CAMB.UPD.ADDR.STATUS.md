# CAMB.UPD.ADDR.STATUS — Table Schema

> Source: `INSERTS/I_F.CAMB.UPD.ADDR.STATUS` in `CAADRT_AddressRight.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.UPDADD.APPLICATION` | `CambUpdAddrStatus_Application` | TField |  | Application name for which exception is raised.Valid entry like CUSTOMER_DE.ADDRESS |
| 2 | `CAMB.UPDADD.DATE.TIME` | `CambUpdAddrStatus_DateTime` |  |  |  |
| 3 | `CAMB.UPDADD.FILE.NAME` | `CambUpdAddrStatus_FileName` | TField |  | Name of the Incoming "Corrected Address" File Name |
| 4 | `CAMB.UPDADD.REASON` | `CambUpdAddrStatus_Reason` | TField |  | Reason for Failure |
| 5 | `CAMB.UPDADD.STATUS` | `CambUpdAddrStatus_Status` | TField |  | FAILURE |
| 6 | `CAMB.UPDADD.PROCESS.DATE` | `CambUpdAddrStatus_ProcessDate` | TField |  |  |
| 7 | `CAMB.UPDADD.CHK.ADDR.STATUS` | `CambUpdAddrStatus_ChkAddrStatus` | TField |  |  |
