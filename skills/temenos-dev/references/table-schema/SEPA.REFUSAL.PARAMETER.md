# SEPA.REFUSAL.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SEPA.REFUSAL.PARAMETER` in `EP_Refusal.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEPA.REFP.SEQUENCE.DIGIT` | `SepaRefusalParameter_SequenceDigit` | TField | Yes | Used to define the number of digit in third part of the refusal ID. Validation Rules Value upto 1 type numeric and Mandatory field No change field |
| 2 | `SEPA.REFP.OFS.PROCESS.MODE` | `SepaRefusalParameter_OfsProcessMode` | A (Alphanumeric) |  | This field holds the mode of Refusla Processing. Validation Rules Value upto 10 type A(Alphanumeric) Valid values are "Offline Ofs" and "Online Ofs" |
| 3 | `SEPA.REFP.OFS.VERSION` | `SepaRefusalParameter_OfsVersion` | TField |  | This field holds the SEPA.REFUSAL version record name for Refusal process. Validation Rules Value upto 54 type ANY(Any Character). Value must exists in VERSION application |
| 4 | `SEPA.REFP.OFS.SOURCE` | `SepaRefusalParameter_OfsSource` | TField |  | This field holds the record Id of OFS.SOURCE used for Refusal process Validation Rules Value upto 54 type ANY(Any Character). Version must exists in OFS.SOURCE application |
| 5 | `SEPA.REFP.OFS.USER.NAME` | `SepaRefusalParameter_OfsUserName` | A (Alphanumeric) |  | This field holds the value of the T24 User name that can be used for Refusal OFS processing Validation Rules Value upto 40 type A(Alphanumeric) |
| 6 | `SEPA.REFP.OFS.PASSWORD` | `SepaRefusalParameter_OfsPassword` | TField |  | This field holds the value of the Password for the User provided in OFS.USER.NAME field that can be used for Refusal OFS processing Validation Rules Value upto 40 type PASSWD |
| 7 | `SEPA.REFP.RESERVED.15` | `SepaRefusalParameter_Reserved15` | TField |  |  |
| 8 | `SEPA.REFP.RESERVED.14` | `SepaRefusalParameter_Reserved14` | TField |  |  |
| 9 | `SEPA.REFP.RESERVED.13` | `SepaRefusalParameter_Reserved13` | TField |  |  |
| 10 | `SEPA.REFP.FIELDS.NAME` | `SepaRefusalParameter_FieldsName` |  |  |  |
| 11 | `SEPA.REFP.SHORT.NAME` | `SepaRefusalParameter_ShortName` |  |  |  |
| 12 | `SEPA.REFP.ALLOW.OPERATION` | `SepaRefusalParameter_AllowOperation` |  |  |  |
| 13 | `SEPA.REFP.SINGLE.MULTI` | `SepaRefusalParameter_SingleMulti` |  |  |  |
| 14 | `SEPA.REFP.RESERVED.12` | `SepaRefusalParameter_Reserved12` |  |  |  |
| 15 | `SEPA.REFP.RESERVED.11` | `SepaRefusalParameter_Reserved11` |  |  |  |
| 16 | `SEPA.REFP.T24.POSITION` | `SepaRefusalParameter_T24Position` |  |  |  |
| 17 | `SEPA.REFP.REFUSE.FTTC` | `SepaRefusalParameter_RefuseFttc` | A (Alphanumeric) |  | Value define here will be used in �TRANSACTION.TYPE� for inward transaction if the record is refused successfully. Validation Rules Value upto 4 type A(Alphanumeric) |
| 18 | `SEPA.REFP.REFUSE.PROC.TYPE` | `SepaRefusalParameter_RefuseProcType` | TField |  | Process type for inward transaction if the record is refused successfully. �MAN� and �RET� are the possible values. Validation Rules Value upto 3 characters |
| 19 | `SEPA.REFP.REFUSE.REASON.CODE` | `SepaRefusalParameter_RefuseReasonCode` | A (Alphanumeric) |  | Value define here will be used as reason code for successfully refusal of the incoming transaction. Validation Rules Value upto 4 type A(Alphanumeric) and Value should exist SEPA.REASONS Application |
| 20 | `SEPA.REFP.SORT.METHOD` | `SepaRefusalParameter_SortMethod` | A (Alphanumeric) |  | Type of sort method used in the selection process to select the refusal record. Possible values are CREATED � Will be sorted according to the date of creation. (I.e. Second part of the refusal ID). UPDATE � Record will be sorted based on the update. (I.e. Order in SEPA.REFUSAL.ACTIVE application). MANUAL � Manual process. The routine define in MAN.SORT.RNT will be called for sort the select refusal ids. Validation Rules Value upto 10 type A(Alphanumeric) |
| 21 | `SEPA.REFP.MAN.SORT.RNT` | `SepaRefusalParameter_ManSortRnt` | A (Alphanumeric) |  | Only allowed if the SORT.METHOD is set to �MANUAL�. Name of the routine to sort the select refusal ids. The selected refusal ids will be passed as argument. User can define the own logics to sort then sent back the ids in same argument. Validation Rules Value upto 65 type A(Alphanumeric) |
| 22 | `SEPA.REFP.RESERVED.10` | `SepaRefusalParameter_Reserved10` | TField |  |  |
| 23 | `SEPA.REFP.RESERVED.9` | `SepaRefusalParameter_Reserved9` | TField |  |  |
| 24 | `SEPA.REFP.RESERVED.8` | `SepaRefusalParameter_Reserved8` | TField |  |  |
| 25 | `SEPA.REFP.RESERVED.7` | `SepaRefusalParameter_Reserved7` | TField |  |  |
| 26 | `SEPA.REFP.RESERVED.6` | `SepaRefusalParameter_Reserved6` | TField |  |  |
| 27 | `SEPA.REFP.RESERVED.5` | `SepaRefusalParameter_Reserved5` | TField |  |  |
| 28 | `SEPA.REFP.RESERVED.4` | `SepaRefusalParameter_Reserved4` | TField |  |  |
| 29 | `SEPA.REFP.RESERVED.3` | `SepaRefusalParameter_Reserved3` | TField |  |  |
| 30 | `SEPA.REFP.RESERVED.2` | `SepaRefusalParameter_Reserved2` | TField |  |  |
| 31 | `SEPA.REFP.RESERVED.1` | `SepaRefusalParameter_Reserved1` | TField |  |  |
| 32 | `SEPA.REFP.LOCAL.REF` | `SepaRefusalParameter_LocalRef` |  |  |  |
| 33 | `SEPA.REFP.OVERRIDE` | `SepaRefusalParameter_Override` |  |  |  |
| 34 | `SEPA.REFP.RECORD.STATUS` | `SepaRefusalParameter_RecordStatus` | String |  |  |
| 35 | `SEPA.REFP.CURR.NO` | `SepaRefusalParameter_CurrNo` | String |  |  |
| 36 | `SEPA.REFP.INPUTTER` | `SepaRefusalParameter_Inputter` |  |  |  |
| 37 | `SEPA.REFP.DATE.TIME` | `SepaRefusalParameter_DateTime` |  |  |  |
| 38 | `SEPA.REFP.AUTHORISER` | `SepaRefusalParameter_Authoriser` | String |  |  |
| 39 | `SEPA.REFP.CO.CODE` | `SepaRefusalParameter_CoCode` | String |  |  |
| 40 | `SEPA.REFP.DEPT.CODE` | `SepaRefusalParameter_DeptCode` | String |  |  |
| 41 | `SEPA.REFP.AUDITOR.CODE` | `SepaRefusalParameter_AuditorCode` | String |  |  |
| 42 | `SEPA.REFP.AUDIT.DATE.TIME` | `SepaRefusalParameter_AuditDateTime` | String |  |  |
