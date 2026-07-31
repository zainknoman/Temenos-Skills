# SASIMA.LOG — Table Schema

> Source: `INSERTS/I_F.SASIMA.LOG` in `SASIMA_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SA.SI.LOG.ACTION` | `SasimaLog_Action` | TField |  |  |
| 2 | `SA.SI.LOG.STATUS` | `SasimaLog_Status` | TField |  |  |
| 3 | `SA.SI.LOG.MEMBER.ID` | `SasimaLog_MemberId` | TField |  |  |
| 4 | `SA.SI.LOG.USER.ID` | `SasimaLog_UserId` | TField |  |  |
| 5 | `SA.SI.LOG.TOT.ITEMS` | `SasimaLog_TotItems` | TField |  |  |
| 6 | `SA.SI.LOG.ERR.ITEMS` | `SasimaLog_ErrItems` | TField |  |  |
| 7 | `SA.SI.LOG.AREF` | `SasimaLog_Aref` |  |  |  |
| 8 | `SA.SI.LOG.APRD` | `SasimaLog_Aprd` |  |  |  |
| 9 | `SA.SI.LOG.FIELD` | `SasimaLog_Field` |  |  |  |
| 10 | `SA.SI.LOG.RSP.MSG` | `SasimaLog_RspMsg` |  |  |  |
| 11 | `SA.SI.LOG.DATA` | `SasimaLog_Data` |  |  |  |
| 12 | `SA.SI.LOG.NO.OF.ERRORS` | `SasimaLog_NoOfErrors` |  |  |  |
| 13 | `SA.SI.LOG.COMM.RESPONSE` | `SasimaLog_CommResponse` |  |  |  |
| 14 | `SA.SI.LOG.LOCAL.REF` | `SasimaLog_LocalRef` |  |  |  |
| 15 | `SA.SI.LOG.RESERVED.1` | `SasimaLog_Reserved1` | TField |  |  |
| 16 | `SA.SI.LOG.RESERVED.2` | `SasimaLog_Reserved2` | TField |  |  |
| 17 | `SA.SI.LOG.RESERVED.3` | `SasimaLog_Reserved3` | TField |  |  |
| 18 | `SA.SI.LOG.RESERVED.4` | `SasimaLog_Reserved4` | TField |  |  |
| 19 | `SA.SI.LOG.RESERVED.5` | `SasimaLog_Reserved5` | TField |  |  |
| 20 | `SA.SI.LOG.RESERVED.6` | `SasimaLog_Reserved6` | TField |  |  |
| 21 | `SA.SI.LOG.RESERVED.7` | `SasimaLog_Reserved7` | TField |  |  |
| 22 | `SA.SI.LOG.RESERVED.8` | `SasimaLog_Reserved8` | TField |  |  |
| 23 | `SA.SI.LOG.RESERVED.9` | `SasimaLog_Reserved9` | TField |  |  |
| 24 | `SA.SI.LOG.RESERVED.10` | `SasimaLog_Reserved10` | TField |  |  |
