# MT.TENANT — Table Schema

> Source: `INSERTS/I_F.MT.TENANT` in `MT_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MT.TNT.TENANT.NAME` | `MtTenant_TenantName` | TField | Yes | Specifies the name of the tenant. Validation Rules: Maximum of 35 characters allowed. Mandatory field |
| 2 | `MT.TNT.BANK.REFERENCE.CODE` | `MtTenant_BankReferenceCode` | TField | Yes | Specifies a unique identification or reference for each institution so that the list of tenants systems belonging to that institution can be identified. Validation Rules: Maximum of 35 characters allowed. Mandatory field |
| 3 | `MT.TNT.TENANT.TYPE` | `MtTenant_TenantType` | TField | Yes | This field defines the type of tenant system e.g. LIVE, DEMO, TRAINING, UAT etc. Validation Rules: must be a valid entry in MT.TENANT.TYPE table. Maximum of 35 characters allowed. Mandatory field |
| 4 | `MT.TNT.TENANT.STATUS` | `MtTenant_TenantStatus` | TField |  | The status of tenant based on which the master system is permitted or not allowed to send messages to them. Validation Rules: Acceptable values are: 1. ACTIVATED :- indicates the tenant system is activated and can receive messages 2. DEACTIVATED :- indicates the tenant system is deactivated messages are not to be sent.3. Blank, acts the same as DEACTIVATED option. |
| 5 | `MT.TNT.TENANT.CONTACT` | `MtTenant_TenantContact` |  |  |  |
| 6 | `MT.TNT.LEAD.COMPANY` | `MtTenant_LeadCompany` |  |  |  |
| 7 | `MT.TNT.LEAD.COMP.MNE` | `MtTenant_LeadCompMne` |  |  |  |
| 8 | `MT.TNT.LEAD.COMP.GROUP` | `MtTenant_LeadCompGroup` |  |  |  |
| 9 | `MT.TNT.RESERVED.21` | `MtTenant_Reserved21` |  |  |  |
| 10 | `MT.TNT.RESERVED.20` | `MtTenant_Reserved20` |  |  |  |
| 11 | `MT.TNT.RESERVED.19` | `MtTenant_Reserved19` |  |  |  |
| 12 | `MT.TNT.LINK.COMPANY` | `MtTenant_LinkCompany` |  |  |  |
| 13 | `MT.TNT.LINK.COMP.MNE` | `MtTenant_LinkCompMne` |  |  |  |
| 14 | `MT.TNT.RESERVED.18` | `MtTenant_Reserved18` |  |  |  |
| 15 | `MT.TNT.RESERVED.17` | `MtTenant_Reserved17` |  |  |  |
| 16 | `MT.TNT.RESERVED.16` | `MtTenant_Reserved16` |  |  |  |
| 17 | `MT.TNT.OFS.USR.TSA.SERVICE` | `MtTenant_OfsUsrTsaService` | TField | Yes | Defines the User sign-on name to be used for OFS message(s)for MT.TSA.SERVICE.CONSOLE table event generation. The MT Administrator must ensure it is a valid sign-on name in the tenant system. Validation Rules: Maximum of 35 characters allowed. Mandatory field |
| 18 | `MT.TNT.OFS.USR.REPLICATE` | `MtTenant_OfsUsrReplicate` | TField | Yes | Defines the User sign-on name to be used for OFS message(s)for MT.REPLICATE.CONSOLE table event generation. The MT Administrator must ensure it is a valid sign-on name in the tenant system. Validation Rules: Maximum of 35 characters allowed. Mandatory field |
| 19 | `MT.TNT.OFS.PGM.VERSION` | `MtTenant_OfsPgmVersion` | TField | No | Version suffix (pgm version) required for OFS(header) message formed during MT.TSA.SERVICE.CONSOLE and MT.REPLICATE.CONSOLE table event generation. Validation Rules: Maximum of 35 characters allowed. The OFS.PGM.VERSION set in MT.REPLICATE.CONSOLE will take precedence. Optional input. By default zero authoriser(0) will be used in OFS messages sent. |
| 20 | `MT.TNT.RESERVED.15` | `MtTenant_Reserved15` | TField |  |  |
| 21 | `MT.TNT.RESERVED.14` | `MtTenant_Reserved14` | TField |  |  |
| 22 | `MT.TNT.RESERVED.13` | `MtTenant_Reserved13` | TField |  |  |
| 23 | `MT.TNT.RESERVED.12` | `MtTenant_Reserved12` | TField |  |  |
| 24 | `MT.TNT.RESERVED.11` | `MtTenant_Reserved11` | TField |  |  |
| 25 | `MT.TNT.RESERVED.10` | `MtTenant_Reserved10` | TField |  |  |
| 26 | `MT.TNT.RESERVED.9` | `MtTenant_Reserved9` | TField |  |  |
| 27 | `MT.TNT.RESERVED.8` | `MtTenant_Reserved8` | TField |  |  |
| 28 | `MT.TNT.RESERVED.7` | `MtTenant_Reserved7` | TField |  |  |
| 29 | `MT.TNT.RESERVED.6` | `MtTenant_Reserved6` | TField |  |  |
| 30 | `MT.TNT.RESERVED.5` | `MtTenant_Reserved5` | TField |  |  |
| 31 | `MT.TNT.RESERVED.4` | `MtTenant_Reserved4` | TField |  |  |
| 32 | `MT.TNT.RESERVED.3` | `MtTenant_Reserved3` | TField |  |  |
| 33 | `MT.TNT.RESERVED.2` | `MtTenant_Reserved2` | TField |  |  |
| 34 | `MT.TNT.RESERVED.1` | `MtTenant_Reserved1` | TField |  |  |
| 35 | `MT.TNT.LOCAL.REF` | `MtTenant_LocalRef` |  |  |  |
| 36 | `MT.TNT.OVERRIDE` | `MtTenant_Override` |  |  |  |
| 37 | `MT.TNT.RECORD.STATUS` | `MtTenant_RecordStatus` | String |  |  |
| 38 | `MT.TNT.CURR.NO` | `MtTenant_CurrNo` | String |  |  |
| 39 | `MT.TNT.INPUTTER` | `MtTenant_Inputter` |  |  |  |
| 40 | `MT.TNT.DATE.TIME` | `MtTenant_DateTime` |  |  |  |
| 41 | `MT.TNT.AUTHORISER` | `MtTenant_Authoriser` | String |  |  |
| 42 | `MT.TNT.CO.CODE` | `MtTenant_CoCode` | String |  |  |
| 43 | `MT.TNT.DEPT.CODE` | `MtTenant_DeptCode` | String |  |  |
| 44 | `MT.TNT.AUDITOR.CODE` | `MtTenant_AuditorCode` | String |  |  |
| 45 | `MT.TNT.AUDIT.DATE.TIME` | `MtTenant_AuditDateTime` | String |  |  |
