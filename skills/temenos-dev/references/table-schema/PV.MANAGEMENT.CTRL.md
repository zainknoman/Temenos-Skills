# PV.MANAGEMENT.CTRL — Table Schema

> Source: `INSERTS/I_F.PV.MANAGEMENT.CTRL` in `PV_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PVMC.NEXT.CLASS.DATE` | `PvManagementCtrl_NextClassDate` | TField |  | The date on which next classification will happen. Based on the frequency in PV.MANAGMENT this date is updated |
| 2 | `PVMC.NEXT.CALC.DATE` | `PvManagementCtrl_NextCalcDate` | TField |  | The date on which next calculation will happen Classification job updates this date. |
| 3 | `PVMC.NEXT.POST.DATE` | `PvManagementCtrl_NextPostDate` | TField |  | The date on which next posting will happen Classification job updates this date |
| 4 | `PVMC.RESERVED.10` | `PvManagementCtrl_Reserved10` |  |  |  |
| 5 | `PVMC.RESERVED.9` | `PvManagementCtrl_Reserved9` | TField |  |  |
| 6 | `PVMC.RESERVED.8` | `PvManagementCtrl_Reserved8` | TField |  |  |
| 7 | `PVMC.RESERVED.7` | `PvManagementCtrl_Reserved7` | TField |  |  |
| 8 | `PVMC.RESERVED.6` | `PvManagementCtrl_Reserved6` | TField |  |  |
| 9 | `PVMC.RESERVED.5` | `PvManagementCtrl_Reserved5` | TField |  |  |
| 10 | `PVMC.RESERVED.4` | `PvManagementCtrl_Reserved4` | TField |  |  |
| 11 | `PVMC.RESERVED.3` | `PvManagementCtrl_Reserved3` | TField |  |  |
| 12 | `PVMC.RESERVED.2` | `PvManagementCtrl_Reserved2` | TField |  |  |
| 13 | `PVMC.RESERVED.1` | `PvManagementCtrl_Reserved1` | TField |  |  |
