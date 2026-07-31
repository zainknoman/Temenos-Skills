# DD.MANDATE.SERVICE.REASON.CODE — Table Schema

> Source: `INSERTS/I_F.DD.MANDATE.SERVICE.REASON.CODE` in `DD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.MSR.ERR.OR.OVR.CODE` | `DdMandateServiceReasonCode_ErrOrOvrCode` |  |  |  |
| 2 | `DD.MSR.MESSAGE.TYPE` | `DdMandateServiceReasonCode_MessageType` |  |  |  |
| 3 | `DD.MSR.REASON.CODE` | `DdMandateServiceReasonCode_ReasonCode` |  |  |  |
| 4 | `DD.MSR.DEFAULT.MESSAGE.TYPE` | `DdMandateServiceReasonCode_DefaultMessageType` |  |  |  |
| 5 | `DD.MSR.DEFAULT.ERROR.REASON.CD` | `DdMandateServiceReasonCode_DefaultErrorReasonCd` |  |  |  |
| 6 | `DD.MSR.SUCCESS.CODE` | `DdMandateServiceReasonCode_SuccessCode` |  |  |  |
| 7 | `DD.MSR.AMEND.INIT.BY` | `DdMandateServiceReasonCode_AmendInitBy` |  |  |  |
| 8 | `DD.MSR.AMEND.REASON.CODE` | `DdMandateServiceReasonCode_AmendReasonCode` |  |  |  |
| 9 | `DD.MSR.AMEND.REASON.DESC` | `DdMandateServiceReasonCode_AmendReasonDesc` |  |  |  |
| 10 | `DD.MSR.CANCEL.INIT.BY` | `DdMandateServiceReasonCode_CancelInitBy` |  |  |  |
| 11 | `DD.MSR.CANCEL.REASON.CODE` | `DdMandateServiceReasonCode_CancelReasonCode` |  |  |  |
| 12 | `DD.MSR.CANCEL.REASON.DESC` | `DdMandateServiceReasonCode_CancelReasonDesc` |  |  |  |
| 13 | `DD.MSR.RESERVED.9` | `DdMandateServiceReasonCode_Reserved9` | TField |  |  |
| 14 | `DD.MSR.RESERVED.8` | `DdMandateServiceReasonCode_Reserved8` | TField |  |  |
| 15 | `DD.MSR.RESERVED.7` | `DdMandateServiceReasonCode_Reserved7` | TField |  |  |
| 16 | `DD.MSR.RESERVED.6` | `DdMandateServiceReasonCode_Reserved6` | TField |  |  |
| 17 | `DD.MSR.RESERVED.5` | `DdMandateServiceReasonCode_Reserved5` | TField |  |  |
| 18 | `DD.MSR.RESERVED.4` | `DdMandateServiceReasonCode_Reserved4` | TField |  |  |
| 19 | `DD.MSR.RESERVED.3` | `DdMandateServiceReasonCode_Reserved3` | TField |  |  |
| 20 | `DD.MSR.RESERVED.2` | `DdMandateServiceReasonCode_Reserved2` | TField |  |  |
| 21 | `DD.MSR.RESERVED.1` | `DdMandateServiceReasonCode_Reserved1` | TField |  |  |
| 22 | `DD.MSR.LOCAL.REF` | `DdMandateServiceReasonCode_LocalRef` |  |  |  |
| 23 | `DD.MSR.OVERRIDE` | `DdMandateServiceReasonCode_Override` |  |  |  |
| 24 | `DD.MSR.RECORD.STATUS` | `DdMandateServiceReasonCode_RecordStatus` | String |  |  |
| 25 | `DD.MSR.CURR.NO` | `DdMandateServiceReasonCode_CurrNo` | String |  |  |
| 26 | `DD.MSR.INPUTTER` | `DdMandateServiceReasonCode_Inputter` |  |  |  |
| 27 | `DD.MSR.DATE.TIME` | `DdMandateServiceReasonCode_DateTime` |  |  |  |
| 28 | `DD.MSR.AUTHORISER` | `DdMandateServiceReasonCode_Authoriser` | String |  |  |
| 29 | `DD.MSR.CO.CODE` | `DdMandateServiceReasonCode_CoCode` | String |  |  |
| 30 | `DD.MSR.DEPT.CODE` | `DdMandateServiceReasonCode_DeptCode` | String |  |  |
| 31 | `DD.MSR.AUDITOR.CODE` | `DdMandateServiceReasonCode_AuditorCode` | String |  |  |
| 32 | `DD.MSR.AUDIT.DATE.TIME` | `DdMandateServiceReasonCode_AuditDateTime` | String |  |  |
