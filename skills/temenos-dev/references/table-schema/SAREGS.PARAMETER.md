# SAREGS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SAREGS.PARAMETER` in `SAREGS_EarlyClosure.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SAREGS.NO.OF.INSTALMENT` | `SaregsParameter_NoOfInstalment` | TField |  | The number of future Profit Instalments that should be summed and collected as Early Closure charge when payoff is triggered. If value = 0, early closure charge will not be calculated. If value = 3, Early Closure Charge will calculated as sum of the three future profit instalment amounts. If the number of instalments remaining before maturity is less than the value maintained, it will override this value. |
| 2 | `SAREGS.PRODUCT` | `SaregsParameter_Product` |  |  |  |
| 3 | `SAREGS.NO.OF.INSTALMENT.FOR.PRODUCT` | `SaregsParameter_NoOfInstalmentForProduct` |  |  |  |
| 4 | `SAREGS.RESERVED.1` | `SaregsParameter_Reserved1` |  |  |  |
| 5 | `SAREGS.RESERVED.2` | `SaregsParameter_Reserved2` |  |  |  |
| 6 | `SAREGS.RESERVED.3` | `SaregsParameter_Reserved3` |  |  |  |
| 7 | `SAREGS.RESERVED.4` | `SaregsParameter_Reserved4` |  |  |  |
| 8 | `SAREGS.RESERVED.5` | `SaregsParameter_Reserved5` |  |  |  |
| 9 | `SAREGS.RESERVED.6` | `SaregsParameter_Reserved6` |  |  |  |
| 10 | `SAREGS.RESERVED.7` | `SaregsParameter_Reserved7` | TField |  |  |
| 11 | `SAREGS.RESERVED.8` | `SaregsParameter_Reserved8` | TField |  |  |
| 12 | `SAREGS.RESERVED.9` | `SaregsParameter_Reserved9` | TField |  |  |
| 13 | `SAREGS.RESERVED.10` | `SaregsParameter_Reserved10` | TField |  |  |
| 14 | `SAREGS.LOCAL.REF` | `SaregsParameter_LocalRef` |  |  |  |
| 15 | `SAREGS.OVERRIDE` | `SaregsParameter_Override` |  |  |  |
| 16 | `SAREGS.RECORD.STATUS` | `SaregsParameter_RecordStatus` | String |  |  |
| 17 | `SAREGS.CURR.NO` | `SaregsParameter_CurrNo` | String |  |  |
| 18 | `SAREGS.INPUTTER` | `SaregsParameter_Inputter` |  |  |  |
| 19 | `SAREGS.DATE.TIME` | `SaregsParameter_DateTime` |  |  |  |
| 20 | `SAREGS.AUTHORISER` | `SaregsParameter_Authoriser` | String |  |  |
| 21 | `SAREGS.CO.CODE` | `SaregsParameter_CoCode` | String |  |  |
| 22 | `SAREGS.DEPT.CODE` | `SaregsParameter_DeptCode` | String |  |  |
| 23 | `SAREGS.AUDITOR.CODE` | `SaregsParameter_AuditorCode` | String |  |  |
| 24 | `SAREGS.AUDIT.DATE.TIME` | `SaregsParameter_AuditDateTime` | String |  |  |
