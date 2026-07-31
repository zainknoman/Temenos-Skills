# PPADEB.COLLECTING.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.PPADEB.COLLECTING.ACCOUNT` in `PPADEB_DebitOrder.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCA.CBU.ACCOUNT.NUMBER` | `PpadebCollectingAccount_CbuAccountNumber` | TField | Yes | CBU number of the DEBIN participant. Mandatory input. |
| 2 | `PPCA.LEGAL.DOC.NUMBER` | `PpadebCollectingAccount_LegalDocNumber` | TField |  | Document reference of the DEBIN participant. |
| 3 | `PPCA.CONCEPT` | `PpadebCollectingAccount_Concept` |  |  |  |
| 4 | `PPCA.STATUS` | `PpadebCollectingAccount_Status` | TField |  | Status of the collecting account is available in this field. |
| 5 | `PPCA.STATUS.DATE` | `PpadebCollectingAccount_StatusDate` | TField |  | The date of the respective status update is available in this field. No input field for the user. |
| 6 | `PPCA.RESPONSE.CODE` | `PpadebCollectingAccount_ResponseCode` | TField |  | Response code from clearing house (COELSA) is updated in this field using API. No input field for the user. |
| 7 | `PPCA.RESPONSE.DESCRIPTION` | `PpadebCollectingAccount_ResponseDescription` | TField |  | Response description from clearing house (COELSA) is updated in this field using API. No input field for the user. |
| 8 | `PPCA.RESERVED.10` | `PpadebCollectingAccount_Reserved10` | TField |  |  |
| 9 | `PPCA.RESERVED.9` | `PpadebCollectingAccount_Reserved9` | TField |  |  |
| 10 | `PPCA.RESERVED.8` | `PpadebCollectingAccount_Reserved8` | TField |  |  |
| 11 | `PPCA.RESERVED.7` | `PpadebCollectingAccount_Reserved7` | TField |  |  |
| 12 | `PPCA.RESERVED.6` | `PpadebCollectingAccount_Reserved6` | TField |  |  |
| 13 | `PPCA.RESERVED.5` | `PpadebCollectingAccount_Reserved5` | TField |  |  |
| 14 | `PPCA.RESERVED.4` | `PpadebCollectingAccount_Reserved4` | TField |  |  |
| 15 | `PPCA.RESERVED.3` | `PpadebCollectingAccount_Reserved3` | TField |  |  |
| 16 | `PPCA.RESERVED.2` | `PpadebCollectingAccount_Reserved2` | TField |  |  |
| 17 | `PPCA.RESERVED.1` | `PpadebCollectingAccount_Reserved1` | TField |  |  |
| 18 | `PPCA.LOCAL.REF` | `PpadebCollectingAccount_LocalRef` |  |  |  |
| 19 | `PPCA.OVERRIDE` | `PpadebCollectingAccount_Override` |  |  |  |
| 20 | `PPCA.RECORD.STATUS` | `PpadebCollectingAccount_RecordStatus` | String |  |  |
| 21 | `PPCA.CURR.NO` | `PpadebCollectingAccount_CurrNo` | String |  |  |
| 22 | `PPCA.INPUTTER` | `PpadebCollectingAccount_Inputter` |  |  |  |
| 23 | `PPCA.DATE.TIME` | `PpadebCollectingAccount_DateTime` |  |  |  |
| 24 | `PPCA.AUTHORISER` | `PpadebCollectingAccount_Authoriser` | String |  |  |
| 25 | `PPCA.CO.CODE` | `PpadebCollectingAccount_CoCode` | String |  |  |
| 26 | `PPCA.DEPT.CODE` | `PpadebCollectingAccount_DeptCode` | String |  |  |
| 27 | `PPCA.AUDITOR.CODE` | `PpadebCollectingAccount_AuditorCode` | String |  |  |
| 28 | `PPCA.AUDIT.DATE.TIME` | `PpadebCollectingAccount_AuditDateTime` | String |  |  |
