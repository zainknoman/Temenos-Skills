# EB.CHALLENGE.RESPONSE — Table Schema

> Source: `INSERTS/I_F.EB.CHALLENGE.RESPONSE` in `EB_ARC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.CH.RP.DESCRIPTION` | `EbChallengeResponse_Description` | TField |  | Description of the flow intended from this record |
| 2 | `EB.CH.RP.VERSION` | `EbChallengeResponse_Version` |  |  |  |
| 3 | `EB.CH.RP.FIELD.NAME` | `EbChallengeResponse_FieldName` |  |  |  |
| 4 | `EB.CH.RP.START.RANGE` | `EbChallengeResponse_StartRange` |  |  |  |
| 5 | `EB.CH.RP.END.RANGE` | `EbChallengeResponse_EndRange` |  |  |  |
| 6 | `EB.CH.RP.TEXT` | `EbChallengeResponse_Text` |  |  |  |
| 7 | `EB.CH.RP.RESERVED.10` | `EbChallengeResponse_Reserved10` | TField |  |  |
| 8 | `EB.CH.RP.RESERVED.9` | `EbChallengeResponse_Reserved9` | TField |  |  |
| 9 | `EB.CH.RP.RESERVED.8` | `EbChallengeResponse_Reserved8` | TField |  |  |
| 10 | `EB.CH.RP.RESERVED.7` | `EbChallengeResponse_Reserved7` | TField |  |  |
| 11 | `EB.CH.RP.RESERVED.6` | `EbChallengeResponse_Reserved6` | TField |  |  |
| 12 | `EB.CH.RP.RESERVED.5` | `EbChallengeResponse_Reserved5` | TField |  |  |
| 13 | `EB.CH.RP.RESERVED.4` | `EbChallengeResponse_Reserved4` | TField |  |  |
| 14 | `EB.CH.RP.RESERVED.3` | `EbChallengeResponse_Reserved3` | TField |  |  |
| 15 | `EB.CH.RP.RESERVED.2` | `EbChallengeResponse_Reserved2` | TField |  |  |
| 16 | `EB.CH.RP.RESERVED.1` | `EbChallengeResponse_Reserved1` | TField |  |  |
| 17 | `EB.CH.RP.LOCAL.REF` | `EbChallengeResponse_LocalRef` |  |  |  |
| 18 | `EB.CH.RP.OVERRIDE` | `EbChallengeResponse_Override` |  |  |  |
| 19 | `EB.CH.RP.RECORD.STATUS` | `EbChallengeResponse_RecordStatus` | String |  |  |
| 20 | `EB.CH.RP.CURR.NO` | `EbChallengeResponse_CurrNo` | String |  |  |
| 21 | `EB.CH.RP.INPUTTER` | `EbChallengeResponse_Inputter` |  |  |  |
| 22 | `EB.CH.RP.DATE.TIME` | `EbChallengeResponse_DateTime` |  |  |  |
| 23 | `EB.CH.RP.AUTHORISER` | `EbChallengeResponse_Authoriser` | String |  |  |
| 24 | `EB.CH.RP.CO.CODE` | `EbChallengeResponse_CoCode` | String |  |  |
| 25 | `EB.CH.RP.DEPT.CODE` | `EbChallengeResponse_DeptCode` | String |  |  |
| 26 | `EB.CH.RP.AUDITOR.CODE` | `EbChallengeResponse_AuditorCode` | String |  |  |
| 27 | `EB.CH.RP.AUDIT.DATE.TIME` | `EbChallengeResponse_AuditDateTime` | String |  |  |
