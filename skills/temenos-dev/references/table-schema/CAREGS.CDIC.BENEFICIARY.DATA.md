# CAREGS.CDIC.BENEFICIARY.DATA — Table Schema

> Source: `INSERTS/I_F.CAREGS.CDIC.BENEFICIARY.DATA` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.BEN.DATA.BENE.NAME` | `CaregsCdicBeneficiaryData_BeneName` |  |  |  |
| 2 | `CDIC.BEN.DATA.BENE.FIRST.NAME` | `CaregsCdicBeneficiaryData_BeneFirstName` |  |  |  |
| 3 | `CDIC.BEN.DATA.BENE.MIDDLE.NAME` | `CaregsCdicBeneficiaryData_BeneMiddleName` |  |  |  |
| 4 | `CDIC.BEN.DATA.BENE.LAST.NAME` | `CaregsCdicBeneficiaryData_BeneLastName` |  |  |  |
| 5 | `CDIC.BEN.DATA.BENE.ADDR.1` | `CaregsCdicBeneficiaryData_BeneAddr1` |  |  |  |
| 6 | `CDIC.BEN.DATA.BENE.ADDR.2` | `CaregsCdicBeneficiaryData_BeneAddr2` |  |  |  |
| 7 | `CDIC.BEN.DATA.BENE.CITY` | `CaregsCdicBeneficiaryData_BeneCity` |  |  |  |
| 8 | `CDIC.BEN.DATA.BENE.PROVINCE` | `CaregsCdicBeneficiaryData_BeneProvince` |  |  |  |
| 9 | `CDIC.BEN.DATA.BENE.POST.CODE` | `CaregsCdicBeneficiaryData_BenePostCode` |  |  |  |
| 10 | `CDIC.BEN.DATA.BENE.COUNTRY` | `CaregsCdicBeneficiaryData_BeneCountry` |  |  |  |
| 11 | `CDIC.BEN.DATA.SIA.FLAG` | `CaregsCdicBeneficiaryData_SiaFlag` |  |  |  |
| 12 | `CDIC.BEN.DATA.INTEREST.FLAG` | `CaregsCdicBeneficiaryData_InterestFlag` |  |  |  |
| 13 | `CDIC.BEN.DATA.INTEREST` | `CaregsCdicBeneficiaryData_Interest` |  |  |  |
| 14 | `CDIC.BEN.DATA.RESERVED1` | `CaregsCdicBeneficiaryData_Reserved1` |  |  |  |
| 15 | `CDIC.BEN.DATA.RESERVED2` | `CaregsCdicBeneficiaryData_Reserved2` |  |  |  |
| 16 | `CDIC.BEN.DATA.RESERVED3` | `CaregsCdicBeneficiaryData_Reserved3` |  |  |  |
| 17 | `CDIC.BEN.DATA.RESERVED4` | `CaregsCdicBeneficiaryData_Reserved4` |  |  |  |
| 18 | `CDIC.BEN.DATA.RESERVED5` | `CaregsCdicBeneficiaryData_Reserved5` |  |  |  |
| 19 | `CDIC.BEN.DATA.RESERVED.1` | `CaregsCdicBeneficiaryData_Reserved1` |  |  |  |
| 20 | `CDIC.BEN.DATA.RESERVED.2` | `CaregsCdicBeneficiaryData_Reserved2` |  |  |  |
| 21 | `CDIC.BEN.DATA.RESERVED.3` | `CaregsCdicBeneficiaryData_Reserved3` |  |  |  |
| 22 | `CDIC.BEN.DATA.RESERVED.4` | `CaregsCdicBeneficiaryData_Reserved4` |  |  |  |
| 23 | `CDIC.BEN.DATA.RESERVED.5` | `CaregsCdicBeneficiaryData_Reserved5` |  |  |  |
| 24 | `CDIC.BEN.DATA.LOCAL.REF` | `CaregsCdicBeneficiaryData_LocalRef` |  |  |  |
| 25 | `CDIC.BEN.DATA.RECORD.STATUS` | `CaregsCdicBeneficiaryData_RecordStatus` | String |  |  |
| 26 | `CDIC.BEN.DATA.CURR.NO` | `CaregsCdicBeneficiaryData_CurrNo` | String |  |  |
| 27 | `CDIC.BEN.DATA.INPUTTER` | `CaregsCdicBeneficiaryData_Inputter` |  |  |  |
| 28 | `CDIC.BEN.DATA.DATE.TIME` | `CaregsCdicBeneficiaryData_DateTime` |  |  |  |
| 29 | `CDIC.BEN.DATA.AUTHORISER` | `CaregsCdicBeneficiaryData_Authoriser` | String |  |  |
| 30 | `CDIC.BEN.DATA.CO.CODE` | `CaregsCdicBeneficiaryData_CoCode` | String |  |  |
| 31 | `CDIC.BEN.DATA.DEPT.CODE` | `CaregsCdicBeneficiaryData_DeptCode` | String |  |  |
| 32 | `CDIC.BEN.DATA.AUDITOR.CODE` | `CaregsCdicBeneficiaryData_AuditorCode` | String |  |  |
| 33 | `CDIC.BEN.DATA.AUDIT.DATE.TIME` | `CaregsCdicBeneficiaryData_AuditDateTime` | String |  |  |
