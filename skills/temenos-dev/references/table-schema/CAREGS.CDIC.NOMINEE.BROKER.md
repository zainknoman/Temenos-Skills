# CAREGS.CDIC.NOMINEE.BROKER — Table Schema

> Source: `INSERTS/I_F.CAREGS.CDIC.NOMINEE.BROKER` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.NOM.BRK.BENEFICIARY.ID` | `CaregsCdicNomineeBroker_BeneficiaryId` |  |  |  |
| 2 | `CDIC.NOM.BRK.SIA.FLAG` | `CaregsCdicNomineeBroker_SiaFlag` |  |  |  |
| 3 | `CDIC.NOM.BRK.INTEREST.FLAG` | `CaregsCdicNomineeBroker_InterestFlag` |  |  |  |
| 4 | `CDIC.NOM.BRK.INTEREST` | `CaregsCdicNomineeBroker_Interest` |  |  |  |
| 5 | `CDIC.NOM.BRK.IB.LEI` | `CaregsCdicNomineeBroker_IbLei` | TField |  |  |
| 6 | `CDIC.NOM.BRK.RESERVED.1` | `CaregsCdicNomineeBroker_Reserved1` | TField |  |  |
| 7 | `CDIC.NOM.BRK.RESERVED.2` | `CaregsCdicNomineeBroker_Reserved2` | TField |  |  |
| 8 | `CDIC.NOM.BRK.RESERVED.3` | `CaregsCdicNomineeBroker_Reserved3` | TField |  |  |
| 9 | `CDIC.NOM.BRK.RESERVED.4` | `CaregsCdicNomineeBroker_Reserved4` | TField |  |  |
| 10 | `CDIC.NOM.BRK.RESERVED.5` | `CaregsCdicNomineeBroker_Reserved5` | TField |  |  |
| 11 | `CDIC.NOM.BRK.LOCAL.REF` | `CaregsCdicNomineeBroker_LocalRef` |  |  |  |
| 12 | `CDIC.NOM.BRK.RECORD.STATUS` | `CaregsCdicNomineeBroker_RecordStatus` | String |  |  |
| 13 | `CDIC.NOM.BRK.CURR.NO` | `CaregsCdicNomineeBroker_CurrNo` | String |  |  |
| 14 | `CDIC.NOM.BRK.INPUTTER` | `CaregsCdicNomineeBroker_Inputter` |  |  |  |
| 15 | `CDIC.NOM.BRK.DATE.TIME` | `CaregsCdicNomineeBroker_DateTime` |  |  |  |
| 16 | `CDIC.NOM.BRK.AUTHORISER` | `CaregsCdicNomineeBroker_Authoriser` | String |  |  |
| 17 | `CDIC.NOM.BRK.CO.CODE` | `CaregsCdicNomineeBroker_CoCode` | String |  |  |
| 18 | `CDIC.NOM.BRK.DEPT.CODE` | `CaregsCdicNomineeBroker_DeptCode` | String |  |  |
| 19 | `CDIC.NOM.BRK.AUDITOR.CODE` | `CaregsCdicNomineeBroker_AuditorCode` | String |  |  |
| 20 | `CDIC.NOM.BRK.AUDIT.DATE.TIME` | `CaregsCdicNomineeBroker_AuditDateTime` | String |  |  |
