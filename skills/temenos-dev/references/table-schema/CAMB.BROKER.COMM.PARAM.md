# CAMB.BROKER.COMM.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.BROKER.COMM.PARAM` in `CABRCM_BrokerCommission.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COMM.PARAM.PROFILE` | `CambBrokerCommParam_Profile` |  |  |  |
| 2 | `COMM.PARAM.VOLUME.UPTO` | `CambBrokerCommParam_VolumeUpto` |  |  |  |
| 3 | `COMM.PARAM.TAX.TYPE` | `CambBrokerCommParam_TaxType` |  |  |  |
| 4 | `COMM.PARAM.TAX.CODE` | `CambBrokerCommParam_TaxCode` |  |  |  |
| 5 | `COMM.PARAM.VALID.REASONS` | `CambBrokerCommParam_ValidReasons` |  |  |  |
| 6 | `COMM.PARAM.RATE.CHANGE.REASON.VAL` | `CambBrokerCommParam_RateChangeReasonVal` |  |  |  |
| 7 | `COMM.PARAM.AA.ACTIVITY` | `CambBrokerCommParam_AaActivity` |  |  |  |
| 8 | `COMM.PARAM.RESERVED.12` | `CambBrokerCommParam_Reserved12` | TField |  |  |
| 9 | `COMM.PARAM.RESERVED.11` | `CambBrokerCommParam_Reserved11` | TField |  |  |
| 10 | `COMM.PARAM.RESERVED.10` | `CambBrokerCommParam_Reserved10` | TField |  |  |
| 11 | `COMM.PARAM.RESERVED.9` | `CambBrokerCommParam_Reserved9` | TField |  |  |
| 12 | `COMM.PARAM.RESERVED.8` | `CambBrokerCommParam_Reserved8` | TField |  |  |
| 13 | `COMM.PARAM.RESERVED.7` | `CambBrokerCommParam_Reserved7` | TField |  |  |
| 14 | `COMM.PARAM.RESERVED.6` | `CambBrokerCommParam_Reserved6` | TField |  |  |
| 15 | `COMM.PARAM.RESERVED.5` | `CambBrokerCommParam_Reserved5` | TField |  |  |
| 16 | `COMM.PARAM.RESERVED.4` | `CambBrokerCommParam_Reserved4` | TField |  |  |
| 17 | `COMM.PARAM.RESERVED.3` | `CambBrokerCommParam_Reserved3` | TField |  |  |
| 18 | `COMM.PARAM.RESERVED.2` | `CambBrokerCommParam_Reserved2` | TField |  |  |
| 19 | `COMM.PARAM.RESERVED.1` | `CambBrokerCommParam_Reserved1` | TField |  |  |
| 20 | `COMM.PARAM.RECORD.STATUS` | `CambBrokerCommParam_RecordStatus` | String |  |  |
| 21 | `COMM.PARAM.CURR.NO` | `CambBrokerCommParam_CurrNo` | String |  |  |
| 22 | `COMM.PARAM.INPUTTER` | `CambBrokerCommParam_Inputter` |  |  |  |
| 23 | `COMM.PARAM.DATE.TIME` | `CambBrokerCommParam_DateTime` |  |  |  |
| 24 | `COMM.PARAM.AUTHORISER` | `CambBrokerCommParam_Authoriser` | String |  |  |
| 25 | `COMM.PARAM.CO.CODE` | `CambBrokerCommParam_CoCode` | String |  |  |
| 26 | `COMM.PARAM.DEPT.CODE` | `CambBrokerCommParam_DeptCode` | String |  |  |
| 27 | `COMM.PARAM.AUDITOR.CODE` | `CambBrokerCommParam_AuditorCode` | String |  |  |
| 28 | `COMM.PARAM.AUDIT.DATE.TIME` | `CambBrokerCommParam_AuditDateTime` | String |  |  |
