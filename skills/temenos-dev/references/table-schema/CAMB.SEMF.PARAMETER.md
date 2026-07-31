# CAMB.SEMF.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CAMB.SEMF.PARAMETER` in `CAATMI_EverlinkATMInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.SEMF.CARD.STATUS` | `CambSemfParameter_CardStatus` |  |  |  |
| 2 | `CAMB.SEMF.CUSTOMER.STATUS` | `CambSemfParameter_CustomerStatus` |  |  |  |
| 3 | `CAMB.SEMF.REFRESH.GROUP` | `CambSemfParameter_RefreshGroup` | TField |  | For future use |
| 4 | `CAMB.SEMF.EXT.COMPANY` | `CambSemfParameter_ExtCompany` |  |  |  |
| 5 | `CAMB.SEMF.COMPANY.WISE` | `CambSemfParameter_CompanyWise` | TField |  | It is a Yes/No field used to define whether lead company wise extract has to be produced or consolidated extract has to be produced.If 'YES' parameterised Lead Company Wise extract generated, otherwise single extract file generated with all parameterised Lead company data |
| 6 | `CAMB.SEMF.RESERVED.10` | `CambSemfParameter_Reserved10` | TField |  |  |
| 7 | `CAMB.SEMF.RESERVED.9` | `CambSemfParameter_Reserved9` | TField |  |  |
| 8 | `CAMB.SEMF.RESERVED.8` | `CambSemfParameter_Reserved8` | TField |  |  |
| 9 | `CAMB.SEMF.RESERVED.7` | `CambSemfParameter_Reserved7` | TField |  |  |
| 10 | `CAMB.SEMF.RESERVED.6` | `CambSemfParameter_Reserved6` | TField |  |  |
| 11 | `CAMB.SEMF.RESERVED.5` | `CambSemfParameter_Reserved5` | TField |  |  |
| 12 | `CAMB.SEMF.RESERVED.4` | `CambSemfParameter_Reserved4` | TField |  |  |
| 13 | `CAMB.SEMF.RESERVED.3` | `CambSemfParameter_Reserved3` | TField |  |  |
| 14 | `CAMB.SEMF.RESERVED.2` | `CambSemfParameter_Reserved2` | TField |  |  |
| 15 | `CAMB.SEMF.RESERVED.1` | `CambSemfParameter_Reserved1` | TField |  |  |
| 16 | `CAMB.SEMF.RECORD.STATUS` | `CambSemfParameter_RecordStatus` | String |  |  |
| 17 | `CAMB.SEMF.CURR.NO` | `CambSemfParameter_CurrNo` | String |  |  |
| 18 | `CAMB.SEMF.INPUTTER` | `CambSemfParameter_Inputter` |  |  |  |
| 19 | `CAMB.SEMF.DATE.TIME` | `CambSemfParameter_DateTime` |  |  |  |
| 20 | `CAMB.SEMF.AUTHORISER` | `CambSemfParameter_Authoriser` | String |  |  |
| 21 | `CAMB.SEMF.CO.CODE` | `CambSemfParameter_CoCode` | String |  |  |
| 22 | `CAMB.SEMF.DEPT.CODE` | `CambSemfParameter_DeptCode` | String |  |  |
| 23 | `CAMB.SEMF.AUDITOR.CODE` | `CambSemfParameter_AuditorCode` | String |  |  |
| 24 | `CAMB.SEMF.AUDIT.DATE.TIME` | `CambSemfParameter_AuditDateTime` | String |  |  |
