# SP.STP.PARAM — Table Schema

> Source: `INSERTS/I_F.SP.STP.PARAM` in `SP_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SP.STP.MSG.TYPE` | `SpStpParam_MsgType` |  |  |  |
| 2 | `SP.STP.AUTO.COMPARE` | `SpStpParam_AutoCompare` |  |  |  |
| 3 | `SP.STP.USER.ROUTINE` | `SpStpParam_UserRoutine` |  |  |  |
| 4 | `SP.STP.REASON.CODE` | `SpStpParam_ReasonCode` |  |  |  |
| 5 | `SP.STP.AGGR.VERSION` | `SpStpParam_AggrVersion` | TField |  | This field will accept a Version record that is used to authorise SP.AGGREGATION. |
| 6 | `SP.STP.RECON.VERSION` | `SpStpParam_ReconVersion` | TField |  | This field will accept a Version record that is used to authorise SP.RECONCILIATION. |
| 7 | `SP.STP.TRADE.VERSION` | `SpStpParam_TradeVersion` | TField |  | This field will accept a Version record that is used to authorise SEC.TRADE as a part of aggregated MT515. |
| 8 | `SP.STP.SETTLE.VERSION` | `SpStpParam_SettleVersion` | TField |  | This field will accept a Version record that is used to authorise SC.SETTLEMENT as a part of aggregated MT545 or MT547. |
| 9 | `SP.STP.OFS.SOURCE` | `SpStpParam_OfsSource` | TField |  | This field will hold the OFS.SOURCE record that will be used for aggregation process. |
| 10 | `SP.STP.XML.IN.DIR` | `SpStpParam_XmlInDir` | TField |  | Defines the name of the directory used to hold incoming MX xml messages. The UNIX or NT pathname for the directory can be specified with apos;/apos; separators (Note do not use apos;\apos; in an NT environment). If no path is specified the system will create a directory at authorisation if it does not exist, otherwise the directory must exist. validation: Must be a type 1 or 19 file if an existing directory is defined |
| 11 | `SP.STP.XML.ARC.DIR` | `SpStpParam_XmlArcDir` | TField |  | Defines the name of the directory used to hold archieved MX xml messages recieved. The UNIX or NT pathname for the directory can be specified with apos;/apos; separators (Note do not use apos;\apos; in an NT environment). If no path is specified the system will create a directory at authorisation if it does not exist, otherwise the directory must exist. validation: Must be a type 1 or 19 file if an existing directory is defined. |
| 12 | `SP.STP.OFSML.DIR` | `SpStpParam_OfsmlDir` | TField |  | Defines the name of the directory used to store the converted OFSML messages from XML message. The UNIX or NT pathname for the directory can be specified with apos;/apos; separators (Note do not use apos;\apos; in an NT environment). If no path is specified the system will create a directory at authorisation if it does not exist, otherwise the directory must exist. validation Must be a type 1 or 19 file if an existing directory is defined. |
| 13 | `SP.STP.LOCAL.REF` | `SpStpParam_LocalRef` |  |  |  |
| 14 | `SP.STP.RECORD.STATUS` | `SpStpParam_RecordStatus` | String |  |  |
| 15 | `SP.STP.CURR.NO` | `SpStpParam_CurrNo` | String |  |  |
| 16 | `SP.STP.INPUTTER` | `SpStpParam_Inputter` |  |  |  |
| 17 | `SP.STP.DATE.TIME` | `SpStpParam_DateTime` |  |  |  |
| 18 | `SP.STP.AUTHORISER` | `SpStpParam_Authoriser` | String |  |  |
| 19 | `SP.STP.CO.CODE` | `SpStpParam_CoCode` | String |  |  |
| 20 | `SP.STP.DEPT.CODE` | `SpStpParam_DeptCode` | String |  |  |
| 21 | `SP.STP.AUDITOR.CODE` | `SpStpParam_AuditorCode` | String |  |  |
| 22 | `SP.STP.AUDIT.DATE.TIME` | `SpStpParam_AuditDateTime` | String |  |  |
