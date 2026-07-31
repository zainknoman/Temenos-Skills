# CANNEX.BROKER.IDEN.PARAM — Table Schema

> Source: `INSERTS/I_F.CANNEX.BROKER.IDEN.PARAM` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CANNEX.BR.IDEN.DESCRIPTION` | `CannexBrokerIdenParam_Description` |  |  |  |
| 2 | `CANNEX.BR.IDEN.RESERVED.1` | `CannexBrokerIdenParam_Reserved1` | TField |  |  |
| 3 | `CANNEX.BR.IDEN.RESERVED.2` | `CannexBrokerIdenParam_Reserved2` | TField |  |  |
| 4 | `CANNEX.BR.IDEN.RESERVED.3` | `CannexBrokerIdenParam_Reserved3` | TField |  |  |
| 5 | `CANNEX.BR.IDEN.RESERVED.4` | `CannexBrokerIdenParam_Reserved4` | TField |  |  |
| 6 | `CANNEX.BR.IDEN.RESERVED.5` | `CannexBrokerIdenParam_Reserved5` | TField |  |  |
| 7 | `CANNEX.BR.IDEN.RESERVED.6` | `CannexBrokerIdenParam_Reserved6` | TField |  |  |
| 8 | `CANNEX.BR.IDEN.RESERVED.7` | `CannexBrokerIdenParam_Reserved7` | TField |  |  |
| 9 | `CANNEX.BR.IDEN.RESERVED.8` | `CannexBrokerIdenParam_Reserved8` | TField |  |  |
| 10 | `CANNEX.BR.IDEN.RESERVED.9` | `CannexBrokerIdenParam_Reserved9` | TField |  |  |
| 11 | `CANNEX.BR.IDEN.RESERVED.10` | `CannexBrokerIdenParam_Reserved10` | TField |  |  |
| 12 | `CANNEX.BR.IDEN.LOCAL.REF` | `CannexBrokerIdenParam_LocalRef` |  |  |  |
| 13 | `CANNEX.BR.IDEN.OVERRIDE` | `CannexBrokerIdenParam_Override` |  |  |  |
| 14 | `CANNEX.BR.IDEN.RECORD.STATUS` | `CannexBrokerIdenParam_RecordStatus` | String |  |  |
| 15 | `CANNEX.BR.IDEN.CURR.NO` | `CannexBrokerIdenParam_CurrNo` | String |  |  |
| 16 | `CANNEX.BR.IDEN.INPUTTER` | `CannexBrokerIdenParam_Inputter` |  |  |  |
| 17 | `CANNEX.BR.IDEN.DATE.TIME` | `CannexBrokerIdenParam_DateTime` |  |  |  |
| 18 | `CANNEX.BR.IDEN.AUTHORISER` | `CannexBrokerIdenParam_Authoriser` | String |  |  |
| 19 | `CANNEX.BR.IDEN.CO.CODE` | `CannexBrokerIdenParam_CoCode` | String |  |  |
| 20 | `CANNEX.BR.IDEN.DEPT.CODE` | `CannexBrokerIdenParam_DeptCode` | String |  |  |
| 21 | `CANNEX.BR.IDEN.AUDITOR.CODE` | `CannexBrokerIdenParam_AuditorCode` | String |  |  |
| 22 | `CANNEX.BR.IDEN.AUDIT.DATE.TIME` | `CannexBrokerIdenParam_AuditDateTime` | String |  |  |
