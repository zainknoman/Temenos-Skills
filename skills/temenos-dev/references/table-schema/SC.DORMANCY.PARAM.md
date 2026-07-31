# SC.DORMANCY.PARAM — Table Schema

> Source: `INSERTS/I_F.SC.DORMANCY.PARAM` in `SC_ScoPortfolioMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.DPRM.PORT.DORMANT.PERIOD` | `ScDormancyParam_PortDormantPeriod` | TField |  | This field holds the period within which if a customer hasn�t initiated any of the activities in the portfolio, the portfolio would be marked INACTIVE. Validation Rules: Input should be given in terms of months. |
| 2 | `SC.DPRM.DORM.EXEMPT.MGT.ACCT` | `ScDormancyParam_DormExemptMgtAcct` |  |  |  |
| 3 | `SC.DPRM.DORMANCY.CHK.APPL` | `ScDormancyParam_DormancyChkAppl` |  |  |  |
| 4 | `SC.DPRM.RESERVED20` | `ScDormancyParam_Reserved20` | TField |  |  |
| 5 | `SC.DPRM.RESERVED19` | `ScDormancyParam_Reserved19` | TField |  |  |
| 6 | `SC.DPRM.RESERVED18` | `ScDormancyParam_Reserved18` | TField |  |  |
| 7 | `SC.DPRM.RESERVED17` | `ScDormancyParam_Reserved17` | TField |  |  |
| 8 | `SC.DPRM.RESERVED16` | `ScDormancyParam_Reserved16` | TField |  |  |
| 9 | `SC.DPRM.RESERVED15` | `ScDormancyParam_Reserved15` | TField |  |  |
| 10 | `SC.DPRM.RESERVED14` | `ScDormancyParam_Reserved14` | TField |  |  |
| 11 | `SC.DPRM.RESERVED13` | `ScDormancyParam_Reserved13` | TField |  |  |
| 12 | `SC.DPRM.RESERVED12` | `ScDormancyParam_Reserved12` | TField |  |  |
| 13 | `SC.DPRM.RESERVED11` | `ScDormancyParam_Reserved11` | TField |  |  |
| 14 | `SC.DPRM.RESERVED10` | `ScDormancyParam_Reserved10` | TField |  |  |
| 15 | `SC.DPRM.RESERVED9` | `ScDormancyParam_Reserved9` | TField |  |  |
| 16 | `SC.DPRM.RESERVED8` | `ScDormancyParam_Reserved8` | TField |  |  |
| 17 | `SC.DPRM.RESERVED7` | `ScDormancyParam_Reserved7` | TField |  |  |
| 18 | `SC.DPRM.RESERVED6` | `ScDormancyParam_Reserved6` | TField |  |  |
| 19 | `SC.DPRM.RESERVED5` | `ScDormancyParam_Reserved5` | TField |  |  |
| 20 | `SC.DPRM.RESERVED4` | `ScDormancyParam_Reserved4` | TField |  |  |
| 21 | `SC.DPRM.RESERVED3` | `ScDormancyParam_Reserved3` | TField |  |  |
| 22 | `SC.DPRM.RESERVED2` | `ScDormancyParam_Reserved2` | TField |  |  |
| 23 | `SC.DPRM.RESERVED1` | `ScDormancyParam_Reserved1` | TField |  |  |
| 24 | `SC.DPRM.LOCAL.REF` | `ScDormancyParam_LocalRef` |  |  |  |
| 25 | `SC.DPRM.OVERRIDE` | `ScDormancyParam_Override` |  |  |  |
| 26 | `SC.DPRM.RECORD.STATUS` | `ScDormancyParam_RecordStatus` | String |  |  |
| 27 | `SC.DPRM.CURR.NO` | `ScDormancyParam_CurrNo` | String |  |  |
| 28 | `SC.DPRM.INPUTTER` | `ScDormancyParam_Inputter` |  |  |  |
| 29 | `SC.DPRM.DATE.TIME` | `ScDormancyParam_DateTime` |  |  |  |
| 30 | `SC.DPRM.AUTHORISER` | `ScDormancyParam_Authoriser` | String |  |  |
| 31 | `SC.DPRM.CO.CODE` | `ScDormancyParam_CoCode` | String |  |  |
| 32 | `SC.DPRM.DEPT.CODE` | `ScDormancyParam_DeptCode` | String |  |  |
| 33 | `SC.DPRM.AUDITOR.CODE` | `ScDormancyParam_AuditorCode` | String |  |  |
| 34 | `SC.DPRM.AUDIT.DATE.TIME` | `ScDormancyParam_AuditDateTime` | String |  |  |
