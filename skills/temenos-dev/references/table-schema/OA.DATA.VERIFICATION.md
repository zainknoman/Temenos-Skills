# OA.DATA.VERIFICATION — Table Schema

> Source: `INSERTS/I_F.OA.DATA.VERIFICATION` in `OA_Status.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.DV.VERIFICATION` | `OaDataVerification_Verification` | TField |  | It is a system Calculated field and describes the overall verification status of the formlet. The verification value will be set as PENDING when it is creating first time. Then it will be calculated by the system based upon the worst status of each of the associated Evidence Requirements. Allowed values are PENDING, VERIFIED or NOT.VERIFIED |
| 2 | `OA.DV.ACTIVITY` | `OaDataVerification_Activity` | TField | Yes | This field defines the activity to be processed against the data verification. 1. Input in this field should be valid record under AA.CLASS.TYPE.ACTIVITY.CLASS application. 2. Input is mandatory in this field to commit the data verification transaction. |
| 3 | `OA.DV.RESERVED.13` | `OaDataVerification_Reserved13` | TField |  |  |
| 4 | `OA.DV.RESERVED.12` | `OaDataVerification_Reserved12` | TField |  |  |
| 5 | `OA.DV.EVIDENCE.REQUIREMENT` | `OaDataVerification_EvidenceRequirement` |  |  |  |
| 6 | `OA.DV.EVIDENCE.REQ.STATUS` | `OaDataVerification_EvidenceReqStatus` |  |  |  |
| 7 | `OA.DV.EVIDENCE.TYPE` | `OaDataVerification_EvidenceType` |  |  |  |
| 8 | `OA.DV.EVIDENCE` | `OaDataVerification_Evidence` |  |  |  |
| 9 | `OA.DV.EVIDENCE.USED` | `OaDataVerification_EvidenceUsed` |  |  |  |
| 10 | `OA.DV.RESERVED.11` | `OaDataVerification_Reserved11` |  |  |  |
| 11 | `OA.DV.RESERVED.10` | `OaDataVerification_Reserved10` |  |  |  |
| 12 | `OA.DV.RESERVED.9` | `OaDataVerification_Reserved9` |  |  |  |
| 13 | `OA.DV.FIELD.TO.VERIFY` | `OaDataVerification_FieldToVerify` |  |  |  |
| 14 | `OA.DV.FIELD.VALUE` | `OaDataVerification_FieldValue` |  |  |  |
| 15 | `OA.DV.VERIFIED` | `OaDataVerification_Verified` |  |  |  |
| 16 | `OA.DV.COMMENTS` | `OaDataVerification_Comments` |  |  |  |
| 17 | `OA.DV.APPLICATION` | `OaDataVerification_Application` | TField |  | It is system populated and no change field. It specify the application id of the current data verification. It should be a valid record under OA.APPLICATION. This field value will be used to construct the Formlet Record id to verify the data. |
| 18 | `OA.DV.DOMAIN.TYPE` | `OaDataVerification_DomainType` | TField |  | It is system populated and no change field. It specify the name of the domain type, which belongs to the form. It should be a valid record under OA.DOMAIN.TYPE. This field value will be used to construct the Formlet Record id to verify the data. |
| 19 | `OA.DV.ROLE` | `OaDataVerification_Role` | TField |  | It is system populated and no change field. It specify the Role of the form. It should be a valid record under OA.ROLE. This field value will be used to construct the Formlet Record id to verify the data. |
| 20 | `OA.DV.SEQUENCE.NO` | `OaDataVerification_SequenceNo` | TField |  | It is system populated and no change field. It specify the sequence number of the current FORM. This field value will be used to construct the Formlet Record id to verify the data. |
| 21 | `OA.DV.FORM` | `OaDataVerification_Form` | TField |  | It is system populated and no change field. It specifies the name of the form. It should be a valid record under OA.FORM application. |
| 22 | `OA.DV.FORMLET` | `OaDataVerification_Formlet` | TField |  | It is system populated and no change field. It specify the name of the formlet which requires the data verification. It should be a valid record under OA.FORMLET application. This input will be used to construct the formlet record key. |
| 23 | `OA.DV.RESERVED.2` | `OaDataVerification_Reserved2` | TField |  |  |
| 24 | `OA.DV.RESERVED.1` | `OaDataVerification_Reserved1` | TField |  |  |
| 25 | `OA.DV.LOCAL.REF` | `OaDataVerification_LocalRef` |  |  |  |
| 26 | `OA.DV.OVERRIDE` | `OaDataVerification_Override` |  |  |  |
| 27 | `OA.DV.RECORD.STATUS` | `OaDataVerification_RecordStatus` | String |  |  |
| 28 | `OA.DV.CURR.NO` | `OaDataVerification_CurrNo` | String |  |  |
| 29 | `OA.DV.INPUTTER` | `OaDataVerification_Inputter` |  |  |  |
| 30 | `OA.DV.DATE.TIME` | `OaDataVerification_DateTime` |  |  |  |
| 31 | `OA.DV.AUTHORISER` | `OaDataVerification_Authoriser` | String |  |  |
| 32 | `OA.DV.CO.CODE` | `OaDataVerification_CoCode` | String |  |  |
| 33 | `OA.DV.DEPT.CODE` | `OaDataVerification_DeptCode` | String |  |  |
| 34 | `OA.DV.AUDITOR.CODE` | `OaDataVerification_AuditorCode` | String |  |  |
| 35 | `OA.DV.AUDIT.DATE.TIME` | `OaDataVerification_AuditDateTime` | String |  |  |
| 36 | `OA.DV.EVIDENCE.SOURCE` | `OaDataVerification_EvidenceSource` |  |  |  |
| 37 | `OA.DV.EVIDENCE.DATA` | `OaDataVerification_EvidenceData` |  |  |  |
| 38 | `OA.DV.COMPARISON.TYPE` | `OaDataVerification_ComparisonType` |  |  |  |
| 39 | `OA.DV.VERIFICATION.STATUS` | `OaDataVerification_VerificationStatus` |  |  |  |
