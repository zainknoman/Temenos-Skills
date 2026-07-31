# FEDWIRE.TAG — Table Schema

> Source: `INSERTS/I_F.FEDWIRE.TAG` in `USRTGS_Fedwire.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FWTG.DESC` | `FedwireTag_Desc` |  |  |  |
| 2 | `FWTG.SHORT.NAME` | `FedwireTag_ShortName` |  |  |  |
| 3 | `FWTG.TAG.NAME` | `FedwireTag_TagName` | TField | No | Tag name contained within the braces ({ }) Optional input. |
| 4 | `FWTG.ELEMENT.DELIM` | `FedwireTag_ElementDelim` | TField | No | Delimiter to be applied for each element within the tag. Optional input. |
| 5 | `FWTG.REPORT.TAG` | `FedwireTag_ReportTag` | TField | No | Field to denote whether the constructed tag value should be updated in MESSAGE.TRACKER table. Possible values: YES NO Optional input. |
| 6 | `FWTG.REPORT.FIELD` | `FedwireTag_ReportField` | TField | No | Contains the field in MESSAGE.TRACKER table where the tag value should be populated. Optional input. Input allowed only when REPORT.TAG is YES |
| 7 | `FWTG.APPEND.DELIM` | `FedwireTag_AppendDelim` | TField | No | Flag to denote that ELEMENT.DELIM should be appended or not after each TAG.ELEMENT value is returned. If element value returned is null and PROCESS.NULL is YES and APPEND.DELIM is YES only then ELEMENT.DELIM will be appended to the tag value. Possible values: YES NO Optional input. |
| 8 | `FWTG.PROCESS.NULL` | `FedwireTag_ProcessNull` | TField | No | Field to denote whether the constructed tag value if NULL/BLANK should be updated in MESSAGE.TRACKER table or elsewhere. Possible values: YES NO Optional input. |
| 9 | `FWTG.ELEMENT` | `FedwireTag_Element` |  |  |  |
| 10 | `FWTG.CONVERSION` | `FedwireTag_Conversion` |  |  |  |
| 11 | `FWTG.SUFFIX.DELIM` | `FedwireTag_SuffixDelim` |  |  |  |
| 12 | `FWTG.RESERVED.29` | `FedwireTag_Reserved29` |  |  |  |
| 13 | `FWTG.RESERVED.28` | `FedwireTag_Reserved28` |  |  |  |
| 14 | `FWTG.EDIT.PROPERTY` | `FedwireTag_EditProperty` |  |  |  |
| 15 | `FWTG.TAG` | `FedwireTag_Tag` |  |  |  |
| 16 | `FWTG.TAG.ELEMENT` | `FedwireTag_TagElement` |  |  |  |
| 17 | `FWTG.OPERAND` | `FedwireTag_Operand` |  |  |  |
| 18 | `FWTG.VALUE.FROM` | `FedwireTag_ValueFrom` |  |  |  |
| 19 | `FWTG.VALUE.TO` | `FedwireTag_ValueTo` |  |  |  |
| 20 | `FWTG.AND.OR` | `FedwireTag_AndOr` |  |  |  |
| 21 | `FWTG.RESERVED.27` | `FedwireTag_Reserved27` |  |  |  |
| 22 | `FWTG.RESERVED.26` | `FedwireTag_Reserved26` |  |  |  |
| 23 | `FWTG.RESERVED.25` | `FedwireTag_Reserved25` |  |  |  |
| 24 | `FWTG.DEF.VALUE` | `FedwireTag_DefValue` |  |  |  |
| 25 | `FWTG.RESERVED.24` | `FedwireTag_Reserved24` |  |  |  |
| 26 | `FWTG.RESERVED.23` | `FedwireTag_Reserved23` |  |  |  |
| 27 | `FWTG.RESERVED.22` | `FedwireTag_Reserved22` |  |  |  |
| 28 | `FWTG.RESERVED.21` | `FedwireTag_Reserved21` |  |  |  |
| 29 | `FWTG.TAG.API` | `FedwireTag_TagApi` | TField | No | API to be invoked to apply special formatting on the tag value after processing all associated elements. Optional input. Routine attached could be either: A jBC implementation by using an EB.API record with a source type of BASIC. For java implementations: An EB.API record id with a source type of HOOK which implements an interface defined in the EB.API record USRTGS.FEDWIRE.TAG.API.HOOK This field supports the Fedwire.updateFedwireTag() method. The Fedwire Class is in the hook.countrymodelbank.usa.Fedwire package which is in USRTGS_FedwireHook.jar shipped with T24. |
| 30 | `FWTG.RESERVED.20` | `FedwireTag_Reserved20` | TField |  |  |
| 31 | `FWTG.RESERVED.19` | `FedwireTag_Reserved19` | TField |  |  |
| 32 | `FWTG.RESERVED.18` | `FedwireTag_Reserved18` | TField |  |  |
| 33 | `FWTG.RESERVED.17` | `FedwireTag_Reserved17` | TField |  |  |
| 34 | `FWTG.RESERVED.16` | `FedwireTag_Reserved16` | TField |  |  |
| 35 | `FWTG.RESERVED.15` | `FedwireTag_Reserved15` | TField |  |  |
| 36 | `FWTG.RESERVED.14` | `FedwireTag_Reserved14` | TField |  |  |
| 37 | `FWTG.RESERVED.13` | `FedwireTag_Reserved13` | TField |  |  |
| 38 | `FWTG.RESERVED.12` | `FedwireTag_Reserved12` | TField |  |  |
| 39 | `FWTG.RESERVED.11` | `FedwireTag_Reserved11` | TField |  |  |
| 40 | `FWTG.RESERVED.10` | `FedwireTag_Reserved10` | TField |  |  |
| 41 | `FWTG.RESERVED.9` | `FedwireTag_Reserved9` | TField |  |  |
| 42 | `FWTG.RESERVED.8` | `FedwireTag_Reserved8` | TField |  |  |
| 43 | `FWTG.RESERVED.7` | `FedwireTag_Reserved7` | TField |  |  |
| 44 | `FWTG.RESERVED.6` | `FedwireTag_Reserved6` | TField |  |  |
| 45 | `FWTG.RESERVED.5` | `FedwireTag_Reserved5` | TField |  |  |
| 46 | `FWTG.RESERVED.4` | `FedwireTag_Reserved4` | TField |  |  |
| 47 | `FWTG.RESERVED.3` | `FedwireTag_Reserved3` | TField |  |  |
| 48 | `FWTG.RESERVED.2` | `FedwireTag_Reserved2` | TField |  |  |
| 49 | `FWTG.RESERVED.1` | `FedwireTag_Reserved1` | TField |  |  |
| 50 | `FWTG.OVERRIDE` | `FedwireTag_Override` |  |  |  |
| 51 | `FWTG.RECORD.STATUS` | `FedwireTag_RecordStatus` | String |  |  |
| 52 | `FWTG.CURR.NO` | `FedwireTag_CurrNo` | String |  |  |
| 53 | `FWTG.INPUTTER` | `FedwireTag_Inputter` |  |  |  |
| 54 | `FWTG.DATE.TIME` | `FedwireTag_DateTime` |  |  |  |
| 55 | `FWTG.AUTHORISER` | `FedwireTag_Authoriser` | String |  |  |
| 56 | `FWTG.CO.CODE` | `FedwireTag_CoCode` | String |  |  |
| 57 | `FWTG.DEPT.CODE` | `FedwireTag_DeptCode` | String |  |  |
| 58 | `FWTG.AUDITOR.CODE` | `FedwireTag_AuditorCode` | String |  |  |
| 59 | `FWTG.AUDIT.DATE.TIME` | `FedwireTag_AuditDateTime` | String |  |  |
