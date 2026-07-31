# SC.WAIVE.COMM — Table Schema

> Source: `INSERTS/I_F.SC.WAIVE.COMM` in `SC_SctTrading.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.WACO.ALL.IN.FEE` | `ScWaiveComm_AllInFee` | TField |  | Parameters to determine Waiver (i.e.This Is an YES/NO Field.This Field decides whether to waive CU.BRKR.COMM or not.) |
| 2 | `SC.WACO.INDEX` | `ScWaiveComm_Index` |  |  |  |
| 3 | `SC.WACO.PRODUCT.TYPE` | `ScWaiveComm_ProductType` |  |  |  |
| 4 | `SC.WACO.SEC.DOMICILE` | `ScWaiveComm_SecDomicile` |  |  |  |
| 5 | `SC.WACO.RESERVED.1` | `ScWaiveComm_Reserved1` | TField |  |  |
| 6 | `SC.WACO.RESERVED.2` | `ScWaiveComm_Reserved2` | TField |  |  |
| 7 | `SC.WACO.RESERVED.3` | `ScWaiveComm_Reserved3` | TField |  |  |
| 8 | `SC.WACO.RESERVED.4` | `ScWaiveComm_Reserved4` | TField |  |  |
| 9 | `SC.WACO.RESERVED.5` | `ScWaiveComm_Reserved5` | TField |  |  |
| 10 | `SC.WACO.RESERVED.6` | `ScWaiveComm_Reserved6` | TField |  |  |
| 11 | `SC.WACO.RESERVED.7` | `ScWaiveComm_Reserved7` | TField |  |  |
| 12 | `SC.WACO.RESERVED.8` | `ScWaiveComm_Reserved8` | TField |  |  |
| 13 | `SC.WACO.RESERVED.9` | `ScWaiveComm_Reserved9` | TField |  |  |
| 14 | `SC.WACO.RESERVED.10` | `ScWaiveComm_Reserved10` | TField |  |  |
| 15 | `SC.WACO.LOCAL.REF` | `ScWaiveComm_LocalRef` |  |  |  |
| 16 | `SC.WACO.RECORD.STATUS` | `ScWaiveComm_RecordStatus` | String |  |  |
| 17 | `SC.WACO.CURR.NO` | `ScWaiveComm_CurrNo` | String |  |  |
| 18 | `SC.WACO.INPUTTER` | `ScWaiveComm_Inputter` |  |  |  |
| 19 | `SC.WACO.DATE.TIME` | `ScWaiveComm_DateTime` |  |  |  |
| 20 | `SC.WACO.AUTHORISER` | `ScWaiveComm_Authoriser` | String |  |  |
| 21 | `SC.WACO.CO.CODE` | `ScWaiveComm_CoCode` | String |  |  |
| 22 | `SC.WACO.DEPT.CODE` | `ScWaiveComm_DeptCode` | String |  |  |
| 23 | `SC.WACO.AUDITOR.CODE` | `ScWaiveComm_AuditorCode` | String |  |  |
| 24 | `SC.WACO.AUDIT.DATE.TIME` | `ScWaiveComm_AuditDateTime` | String |  |  |
