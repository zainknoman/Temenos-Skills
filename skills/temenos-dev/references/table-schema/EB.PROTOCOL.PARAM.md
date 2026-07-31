# EB.PROTOCOL.PARAM — Table Schema

> Source: `INSERTS/I_F.EB.PROTOCOL.PARAM` in `EB_Logging.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PRO.PAR.DESCRIPTION` | `EbProtocolParam_Description` |  |  |  |
| 2 | `PRO.PAR.TXN.LOG.REQUIRED` | `EbProtocolParam_TxnLogRequired` | TField |  | This field defines whether transaction log should be recorded or not. If set to YES, log should be recorded. If set to No, no need to record the log. Default is NONE. Validation Rules: Allowed values are YES, NO or NONE. Input allowed only if @ID is SYSTEM. |
| 3 | `PRO.PAR.ENQ.LOG.REQUIRED` | `EbProtocolParam_EnqLogRequired` | TField |  | This field defines whether enquiry log should be recorded or not. If set to YES, log should be recorded. If set to No, no need to record the log. Default is NONE. Validation Rules: Allowed values are YES, NO or NONE. Input allowed only if @ID is SYSTEM. |
| 4 | `PRO.PAR.CUSTOMER.FIELD` | `EbProtocolParam_CustomerField` |  |  |  |
| 5 | `PRO.PAR.PROTOCOL.INFO.API` | `EbProtocolParam_ProtocolInfoApi` | TField | No | Common API for version/enquiries and system will indicate the context whether it is coming from enquiry or from transaction Validation Rules: Optional Input. Must be defined in EB.API record. |
| 6 | `PRO.PAR.RESERVED.10` | `EbProtocolParam_Reserved10` | TField |  |  |
| 7 | `PRO.PAR.RESERVED.9` | `EbProtocolParam_Reserved9` | TField |  |  |
| 8 | `PRO.PAR.RESERVED.8` | `EbProtocolParam_Reserved8` | TField |  |  |
| 9 | `PRO.PAR.RESERVED.7` | `EbProtocolParam_Reserved7` | TField |  |  |
| 10 | `PRO.PAR.RESERVED.6` | `EbProtocolParam_Reserved6` | TField |  |  |
| 11 | `PRO.PAR.RESERVED.5` | `EbProtocolParam_Reserved5` | TField |  |  |
| 12 | `PRO.PAR.RESERVED.4` | `EbProtocolParam_Reserved4` | TField |  |  |
| 13 | `PRO.PAR.RESERVED.3` | `EbProtocolParam_Reserved3` | TField |  |  |
| 14 | `PRO.PAR.RESERVED.2` | `EbProtocolParam_Reserved2` | TField |  |  |
| 15 | `PRO.PAR.RESERVED.1` | `EbProtocolParam_Reserved1` | TField |  |  |
| 16 | `PRO.PAR.LOCAL.REF` | `EbProtocolParam_LocalRef` |  |  |  |
| 17 | `PRO.PAR.OVERRIDE` | `EbProtocolParam_Override` |  |  |  |
| 18 | `PRO.PAR.RECORD.STATUS` | `EbProtocolParam_RecordStatus` | String |  |  |
| 19 | `PRO.PAR.CURR.NO` | `EbProtocolParam_CurrNo` | String |  |  |
| 20 | `PRO.PAR.INPUTTER` | `EbProtocolParam_Inputter` |  |  |  |
| 21 | `PRO.PAR.DATE.TIME` | `EbProtocolParam_DateTime` |  |  |  |
| 22 | `PRO.PAR.AUTHORISER` | `EbProtocolParam_Authoriser` | String |  |  |
| 23 | `PRO.PAR.CO.CODE` | `EbProtocolParam_CoCode` | String |  |  |
| 24 | `PRO.PAR.DEPT.CODE` | `EbProtocolParam_DeptCode` | String |  |  |
| 25 | `PRO.PAR.AUDITOR.CODE` | `EbProtocolParam_AuditorCode` | String |  |  |
| 26 | `PRO.PAR.AUDIT.DATE.TIME` | `EbProtocolParam_AuditDateTime` | String |  |  |
