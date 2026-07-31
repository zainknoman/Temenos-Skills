# CANNEX.REJECTION.CODE — Table Schema

> Source: `INSERTS/I_F.CANNEX.REJECTION.CODE` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CNX.REJ.CODE.REJECTION.DESCRIPTION` | `CannexRejectionCode_RejectionDescription` |  |  |  |
| 2 | `CNX.REJ.CODE.LOCAL.REF` | `CannexRejectionCode_LocalRef` |  |  |  |
| 3 | `CNX.REJ.CODE.OVERRIDE` | `CannexRejectionCode_Override` |  |  |  |
| 4 | `CNX.REJ.CODE.RECORD.STATUS` | `CannexRejectionCode_RecordStatus` | String |  |  |
| 5 | `CNX.REJ.CODE.CURR.NO` | `CannexRejectionCode_CurrNo` | String |  |  |
| 6 | `CNX.REJ.CODE.INPUTTER` | `CannexRejectionCode_Inputter` |  |  |  |
| 7 | `CNX.REJ.CODE.DATE.TIME` | `CannexRejectionCode_DateTime` |  |  |  |
| 8 | `CNX.REJ.CODE.AUTHORISER` | `CannexRejectionCode_Authoriser` | String |  |  |
| 9 | `CNX.REJ.CODE.CO.CODE` | `CannexRejectionCode_CoCode` | String |  |  |
| 10 | `CNX.REJ.CODE.DEPT.CODE` | `CannexRejectionCode_DeptCode` | String |  |  |
| 11 | `CNX.REJ.CODE.AUDITOR.CODE` | `CannexRejectionCode_AuditorCode` | String |  |  |
| 12 | `CNX.REJ.CODE.AUDIT.DATE.TIME` | `CannexRejectionCode_AuditDateTime` | String |  |  |
