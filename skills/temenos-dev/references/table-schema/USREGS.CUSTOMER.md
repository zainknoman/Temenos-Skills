# USREGS.CUSTOMER — Table Schema

> Source: `INSERTS/I_F.USREGS.CUSTOMER` in `USREGS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USREGS.CUS.CA.PROVINCE` | `UsregsCustomer_CaProvince` | TField |  | Reserved for USREGS development |
| 2 | `USREGS.CUS.TIN.TYPE` | `UsregsCustomer_TinType` | TField |  | Reserved for CTR development. |
| 3 | `USREGS.CUS.PRIVACY.NOTICE` | `UsregsCustomer_PrivacyNotice` | TField |  | Reserved for USREGS development. |
| 4 | `USREGS.CUS.NOTICE.FREQ` | `UsregsCustomer_NoticeFreq` | TField |  | Reserved for USREGS development. |
| 5 | `USREGS.CUS.DELIVERY.MODE` | `UsregsCustomer_DeliveryMode` | TField |  | Reserved for USREGS development. |
| 6 | `USREGS.CUS.PRIVACY.STATUS` | `UsregsCustomer_PrivacyStatus` | TField |  | Reserved for USREGS development. |
| 7 | `USREGS.CUS.PRIVACY.DATE` | `UsregsCustomer_PrivacyDate` | TField |  | Reserved for USREGS development. |
| 8 | `USREGS.CUS.CTR.EXMPT` | `UsregsCustomer_CtrExmpt` | TField |  | Reserved for CTR development. |
| 9 | `USREGS.CUS.CTR.EXMPT.REASON` | `UsregsCustomer_CtrExmptReason` | TField |  | Reserved for CTR development. |
| 10 | `USREGS.CUS.APPLIED.CERTIFIED` | `UsregsCustomer_AppliedCertified` | TField |  | Reserved for USREGS development. |
| 11 | `USREGS.CUS.W8.BEN` | `UsregsCustomer_W8Ben` | TField |  | Reserved for B-Notices development. |
| 12 | `USREGS.CUS.ACCT.OPEN.DATE` | `UsregsCustomer_AcctOpenDate` | TField |  | Account Open date field is used to check whether customer account is a new account or not. Validation Rules: No-input Field |
| 13 | `USREGS.CUS.LAST.CHANGE.TIME` | `UsregsCustomer_LastChangeTime` | TField |  | Reserved for USREGS development. |
| 14 | `USREGS.CUS.RESERVED.31` | `UsregsCustomer_Reserved31` | TField |  |  |
| 15 | `USREGS.CUS.RESERVED.30` | `UsregsCustomer_Reserved30` | TField |  |  |
| 16 | `USREGS.CUS.RESERVED.29` | `UsregsCustomer_Reserved29` | TField |  |  |
| 17 | `USREGS.CUS.RESERVED.28` | `UsregsCustomer_Reserved28` | TField |  |  |
| 18 | `USREGS.CUS.RESERVED.27` | `UsregsCustomer_Reserved27` | TField |  |  |
| 19 | `USREGS.CUS.RESERVED.26` | `UsregsCustomer_Reserved26` | TField |  |  |
| 20 | `USREGS.CUS.RESERVED.25` | `UsregsCustomer_Reserved25` | TField |  |  |
| 21 | `USREGS.CUS.RESERVED.24` | `UsregsCustomer_Reserved24` | TField |  |  |
| 22 | `USREGS.CUS.RESERVED.23` | `UsregsCustomer_Reserved23` | TField |  |  |
| 23 | `USREGS.CUS.RESERVED.22` | `UsregsCustomer_Reserved22` | TField |  |  |
| 24 | `USREGS.CUS.RESERVED.21` | `UsregsCustomer_Reserved21` | TField |  |  |
| 25 | `USREGS.CUS.RESERVED.20` | `UsregsCustomer_Reserved20` | TField |  |  |
| 26 | `USREGS.CUS.RESERVED.19` | `UsregsCustomer_Reserved19` | TField |  |  |
| 27 | `USREGS.CUS.RESERVED.18` | `UsregsCustomer_Reserved18` | TField |  |  |
| 28 | `USREGS.CUS.RESERVED.17` | `UsregsCustomer_Reserved17` | TField |  |  |
| 29 | `USREGS.CUS.RESERVED.16` | `UsregsCustomer_Reserved16` | TField |  |  |
| 30 | `USREGS.CUS.RESERVED.14` | `UsregsCustomer_Reserved14` | TField |  |  |
| 31 | `USREGS.CUS.RESERVED.13` | `UsregsCustomer_Reserved13` | TField |  |  |
| 32 | `USREGS.CUS.RESERVED.12` | `UsregsCustomer_Reserved12` | TField |  |  |
| 33 | `USREGS.CUS.RESERVED.11` | `UsregsCustomer_Reserved11` | TField |  |  |
| 34 | `USREGS.CUS.RESERVED.10` | `UsregsCustomer_Reserved10` | TField |  |  |
| 35 | `USREGS.CUS.RESERVED.9` | `UsregsCustomer_Reserved9` | TField |  |  |
| 36 | `USREGS.CUS.RESERVED.8` | `UsregsCustomer_Reserved8` | TField |  |  |
| 37 | `USREGS.CUS.RESERVED.7` | `UsregsCustomer_Reserved7` | TField |  |  |
| 38 | `USREGS.CUS.RESERVED.6` | `UsregsCustomer_Reserved6` | TField |  |  |
| 39 | `USREGS.CUS.RESERVED.5` | `UsregsCustomer_Reserved5` | TField |  |  |
| 40 | `USREGS.CUS.RESERVED.4` | `UsregsCustomer_Reserved4` | TField |  |  |
| 41 | `USREGS.CUS.RESERVED.3` | `UsregsCustomer_Reserved3` | TField |  |  |
| 42 | `USREGS.CUS.RESERVED.2` | `UsregsCustomer_Reserved2` | TField |  |  |
| 43 | `USREGS.CUS.RESERVED.1` | `UsregsCustomer_Reserved1` | TField |  |  |
| 44 | `USREGS.CUS.OVERRIDE` | `UsregsCustomer_Override` |  |  |  |
| 45 | `USREGS.CUS.RECORD.STATUS` | `UsregsCustomer_RecordStatus` | String |  |  |
| 46 | `USREGS.CUS.CURR.NO` | `UsregsCustomer_CurrNo` | String |  |  |
| 47 | `USREGS.CUS.INPUTTER` | `UsregsCustomer_Inputter` |  |  |  |
| 48 | `USREGS.CUS.DATE.TIME` | `UsregsCustomer_DateTime` |  |  |  |
| 49 | `USREGS.CUS.AUTHORISER` | `UsregsCustomer_Authoriser` | String |  |  |
| 50 | `USREGS.CUS.CO.CODE` | `UsregsCustomer_CoCode` | String |  |  |
| 51 | `USREGS.CUS.DEPT.CODE` | `UsregsCustomer_DeptCode` | String |  |  |
| 52 | `USREGS.CUS.AUDITOR.CODE` | `UsregsCustomer_AuditorCode` | String |  |  |
| 53 | `USREGS.CUS.AUDIT.DATE.TIME` | `UsregsCustomer_AuditDateTime` | String |  |  |
