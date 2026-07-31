# EB.SEC.INTEGRITY.MSG.CONF — Table Schema

> Source: `INSERTS/I_F.EB.SEC.INTEGRITY.MSG.CONF` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEC.INTEG.ALGORITHM` | `EbSecIntegrityMsgConf_Algorithm` | TField |  |  |
| 2 | `SEC.INTEG.KEY.CONFIGURATION` | `EbSecIntegrityMsgConf_KeyConfiguration` | TField |  |  |
| 3 | `SEC.INTEG.COMPLIANCE.ATTRIB` | `EbSecIntegrityMsgConf_ComplianceAttrib` | TField |  |  |
| 4 | `SEC.INTEG.X.CRYPTO.PROVIDER` | `EbSecIntegrityMsgConf_XCryptoProvider` | TField |  |  |
| 5 | `SEC.INTEG.CUSTOM.PROVIDER.NAME` | `EbSecIntegrityMsgConf_CustomProviderName` | TField |  |  |
| 6 | `SEC.INTEG.RESERVED.4` | `EbSecIntegrityMsgConf_Reserved4` |  |  |  |
| 7 | `SEC.INTEG.RESERVED.5` | `EbSecIntegrityMsgConf_Reserved5` | TField |  |  |
| 8 | `SEC.INTEG.RESERVED.6` | `EbSecIntegrityMsgConf_Reserved6` | TField |  |  |
| 9 | `SEC.INTEG.RESERVED.7` | `EbSecIntegrityMsgConf_Reserved7` | TField |  |  |
| 10 | `SEC.INTEG.RESERVED.8` | `EbSecIntegrityMsgConf_Reserved8` | TField |  |  |
| 11 | `SEC.INTEG.RESERVED.9` | `EbSecIntegrityMsgConf_Reserved9` | TField |  |  |
| 12 | `SEC.INTEG.RESERVED.10` | `EbSecIntegrityMsgConf_Reserved10` | TField |  |  |
| 13 | `SEC.INTEG.OVERRIDE` | `EbSecIntegrityMsgConf_Override` |  |  |  |
| 14 | `SEC.INTEG.RECORD.STATUS` | `EbSecIntegrityMsgConf_RecordStatus` | String |  |  |
| 15 | `SEC.INTEG.CURR.NO` | `EbSecIntegrityMsgConf_CurrNo` | String |  |  |
| 16 | `SEC.INTEG.INPUTTER` | `EbSecIntegrityMsgConf_Inputter` |  |  |  |
| 17 | `SEC.INTEG.DATE.TIME` | `EbSecIntegrityMsgConf_DateTime` |  |  |  |
| 18 | `SEC.INTEG.AUTHORISER` | `EbSecIntegrityMsgConf_Authoriser` | String |  |  |
| 19 | `SEC.INTEG.CO.CODE` | `EbSecIntegrityMsgConf_CoCode` | String |  |  |
| 20 | `SEC.INTEG.DEPT.CODE` | `EbSecIntegrityMsgConf_DeptCode` | String |  |  |
| 21 | `SEC.INTEG.AUDITOR.CODE` | `EbSecIntegrityMsgConf_AuditorCode` | String |  |  |
| 22 | `SEC.INTEG.AUDIT.DATE.TIME` | `EbSecIntegrityMsgConf_AuditDateTime` | String |  |  |
| 23 | `SEC.INTEG.DESCRIPTION` | `EbSecIntegrityMsgConf_Description` |  |  |  |
