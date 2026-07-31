# AULEFS.LEGAL.ENTITY.PLATFORM — Table Schema

> Source: `INSERTS/I_F.AULEFS.LEGAL.ENTITY.PLATFORM` in `AULEFS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ENTITY.PARAM.LEGAL.ENTITY.TYPE` | `AulefsLegalEntityPlatform_LegalEntityType` | TField |  | The type of Legal Entity as to whether it is a Super, IDPS, Separately Managed Account, Individually managed account etc. Validation Rule: Vetted to EB.LOOKUP with ID as AULEFS.LEGAL.ENTITY.TYPE. If @ID consists of TTR, ACCU or PENSION, then this should get defaulted to SUPER and can be changed from SUPER to SMSF or vice-versa. If @ID consists of TTR, ACCU or PENSION, it is assumed to be a Super Fund or a Self Managed Super Fund. |
| 2 | `ENTITY.PARAM.LEGAL.ENTITY.SUB.TYPE` | `AulefsLegalEntityPlatform_LegalEntitySubType` | TField |  |  |
| 3 | `ENTITY.PARAM.FUND.NAME` | `AulefsLegalEntityPlatform_FundName` | TField |  | Full name of the fund for informational purposes. |
| 4 | `ENTITY.PARAM.FUND.RESIDENCE` | `AulefsLegalEntityPlatform_FundResidence` | TField |  | The applicable Tax residence of the Legal Entity. Vetted to COUNTRY application |
| 5 | `ENTITY.PARAM.CURR.RITC.RATE` | `AulefsLegalEntityPlatform_CurrRitcRate` | TField |  | The current RITC rate applicable for this Entity. |
| 6 | `ENTITY.PARAM.CURR.RITC.EFF.DATE` | `AulefsLegalEntityPlatform_CurrRitcEffDate` | TField |  | The date on which the current RITC rate became effective. |
| 7 | `ENTITY.PARAM.FWD.RITC.RATE` | `AulefsLegalEntityPlatform_FwdRitcRate` |  |  |  |
| 8 | `ENTITY.PARAM.FWD.RITC.EFF.DATE` | `AulefsLegalEntityPlatform_FwdRitcEffDate` |  |  |  |
| 9 | `ENTITY.PARAM.LOCAL.REF` | `AulefsLegalEntityPlatform_LocalRef` |  |  |  |
| 10 | `ENTITY.PARAM.NRWHT.LOOK.THROUGH` | `AulefsLegalEntityPlatform_NrwhtLookThrough` | TField |  | This indicates if the withholding tax residence is Look-Through or not. A value of "Yes" indicates that Look-Through is enabled for the Legal Entity which means that the underlying customer's portfolio residence would determine the Tax residence. A value of "No" indicates that the legal entity's residence would determine the Tax residence. |
| 11 | `ENTITY.PARAM.TFN.STATUS` | `AulefsLegalEntityPlatform_TfnStatus` | TField |  | The TFN Status of the Legal Entity. This indicates if a valid TFN/Exemption is provided by the resident customer. |
| 12 | `ENTITY.PARAM.TFN.STATUS.EFF.DATE` | `AulefsLegalEntityPlatform_TfnStatusEffDate` | TField |  |  |
| 13 | `ENTITY.PARAM.RESERVED.4` | `AulefsLegalEntityPlatform_Reserved4` | TField |  |  |
| 14 | `ENTITY.PARAM.RESERVED.5` | `AulefsLegalEntityPlatform_Reserved5` | TField |  |  |
| 15 | `ENTITY.PARAM.RESERVED.6` | `AulefsLegalEntityPlatform_Reserved6` | TField |  |  |
| 16 | `ENTITY.PARAM.RESERVED.7` | `AulefsLegalEntityPlatform_Reserved7` | TField |  |  |
| 17 | `ENTITY.PARAM.RESERVED.8` | `AulefsLegalEntityPlatform_Reserved8` | TField |  |  |
| 18 | `ENTITY.PARAM.RESERVED.9` | `AulefsLegalEntityPlatform_Reserved9` | TField |  |  |
| 19 | `ENTITY.PARAM.RESERVED.10` | `AulefsLegalEntityPlatform_Reserved10` | TField |  |  |
| 20 | `ENTITY.PARAM.OVERRIDE` | `AulefsLegalEntityPlatform_Override` |  |  |  |
| 21 | `ENTITY.PARAM.RECORD.STATUS` | `AulefsLegalEntityPlatform_RecordStatus` | String |  |  |
| 22 | `ENTITY.PARAM.CURR.NO` | `AulefsLegalEntityPlatform_CurrNo` | String |  |  |
| 23 | `ENTITY.PARAM.INPUTTER` | `AulefsLegalEntityPlatform_Inputter` |  |  |  |
| 24 | `ENTITY.PARAM.DATE.TIME` | `AulefsLegalEntityPlatform_DateTime` |  |  |  |
| 25 | `ENTITY.PARAM.AUTHORISER` | `AulefsLegalEntityPlatform_Authoriser` | String |  |  |
| 26 | `ENTITY.PARAM.CO.CODE` | `AulefsLegalEntityPlatform_CoCode` | String |  |  |
| 27 | `ENTITY.PARAM.DEPT.CODE` | `AulefsLegalEntityPlatform_DeptCode` | String |  |  |
| 28 | `ENTITY.PARAM.AUDITOR.CODE` | `AulefsLegalEntityPlatform_AuditorCode` | String |  |  |
| 29 | `ENTITY.PARAM.AUDIT.DATE.TIME` | `AulefsLegalEntityPlatform_AuditDateTime` | String |  |  |
