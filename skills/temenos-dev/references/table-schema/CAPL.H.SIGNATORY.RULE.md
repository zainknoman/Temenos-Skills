# CAPL.H.SIGNATORY.RULE — Table Schema

> Source: `INSERTS/I_F.CAPL.H.SIGNATORY.RULE` in `CABASE_CustomerRelation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.SR.DESCRIPTION` | `CaplHSignatoryRule_Description` |  |  |  |
| 2 | `CAPL.SR.CUS.NO.OF.SIGNERS` | `CaplHSignatoryRule_CusNoOfSigners` | TField |  | The purpose of the field is to define the number of signatures required at the container layer.Validation: NONE, ANY or a specific value from the CAPL.H.SIGNATURE.TYPE.NONE means that NO signatures are applicable to this rule.ANY means that any type of signature is applicable for this rule as per the CAPL.H.SIGNATURE.TYPE table explained below.Specific means that a defined number of signers are applicableExample for "Personal Container Tenants in Common" the value configured should be '99 All are required to sign" |
| 3 | `CAPL.SR.CUS.SIGN.REL.CODE` | `CaplHSignatoryRule_CusSignRelCode` |  |  |  |
| 4 | `CAPL.SR.POA.REL.CODE` | `CaplHSignatoryRule_PoaRelCode` |  |  |  |
| 5 | `CAPL.SR.SAM.NO.OF.SIGNERS` | `CaplHSignatoryRule_SamNoOfSigners` | TField |  | This field is used to define the number of signatures required at portfolio layer.It defines the number of signatures required at portfolio layer for this typeof rule/customer.Allowed values are Null, ANY, or a specific value. |
| 6 | `CAPL.SR.SAM.SIGN.REL.CODE` | `CaplHSignatoryRule_SamSignRelCode` |  |  |  |
| 7 | `CAPL.SR.SAM.POA.REL.CODE` | `CaplHSignatoryRule_SamPoaRelCode` |  |  |  |
| 8 | `CAPL.SR.PROD.NO.OF.SIGNERS` | `CaplHSignatoryRule_ProdNoOfSigners` | TField |  | Purpose of this field is to defines the number of signatures at account/product layer.Allowed values CUS, SAM, Null, ANY or a specific value from the CAPL.H.SIGNATURE.TYPE. |
| 9 | `CAPL.SR.PROD.SIGN.REL.CODE` | `CaplHSignatoryRule_ProdSignRelCode` |  |  |  |
| 10 | `CAPL.SR.PROD.POA.REL.CODE` | `CaplHSignatoryRule_ProdPoaRelCode` |  |  |  |
| 11 | `CAPL.SR.SIGNATORY.MESS.TYPE` | `CaplHSignatoryRule_SignatoryMessType` | TField |  | This field is used to define the override or message if signatory rules setup is being violated.Allowed values are None, Eb.error, Override |
| 12 | `CAPL.SR.SIGNATORY.MESS.ID` | `CaplHSignatoryRule_SignatoryMessId` | TField |  | This field is used to define the error or override message for the corresponding option defined in SIGNATORY.MESS.TYPE field.Validation: Valid record from OVERRIDE table is it is an override. In case of error valid record from EB.ERROR.E.g CP-CU.PROD.SIGNERS.INVALID |
| 13 | `CAPL.SR.POA.MESS.TYPE` | `CaplHSignatoryRule_PoaMessType` | TField |  | This field is used to define the override or message if signatory rules setup is being violated.Allowed values are None, Eb.error, Override |
| 14 | `CAPL.SR.POA.MESS.ID` | `CaplHSignatoryRule_PoaMessId` | TField |  | This field is used to define the error or override message for the corresponding option defined in SIGNATORY.MESS.TYPE field.Validation: Valid record from OVERRIDE table is it is an override. In case of error valid record from EB.ERROR.E.g CP-CU.PROD.SIGNERS.INVALID |
| 15 | `CAPL.SR.PROD.ROLE` | `CaplHSignatoryRule_ProdRole` |  |  |  |
| 16 | `CAPL.SR.RESERVED.10` | `CaplHSignatoryRule_Reserved10` |  |  |  |
| 17 | `CAPL.SR.RESERVED.9` | `CaplHSignatoryRule_Reserved9` |  |  |  |
| 18 | `CAPL.SR.RESERVED.8` | `CaplHSignatoryRule_Reserved8` |  |  |  |
| 19 | `CAPL.SR.RESERVED.7` | `CaplHSignatoryRule_Reserved7` |  |  |  |
| 20 | `CAPL.SR.RESERVED.6` | `CaplHSignatoryRule_Reserved6` |  |  |  |
| 21 | `CAPL.SR.RESERVED.5` | `CaplHSignatoryRule_Reserved5` |  |  |  |
| 22 | `CAPL.SR.RESERVED.4` | `CaplHSignatoryRule_Reserved4` |  |  |  |
| 23 | `CAPL.SR.RESERVED.3` | `CaplHSignatoryRule_Reserved3` |  |  |  |
| 24 | `CAPL.SR.RESERVED.2` | `CaplHSignatoryRule_Reserved2` |  |  |  |
| 25 | `CAPL.SR.RESERVED.1` | `CaplHSignatoryRule_Reserved1` |  |  |  |
| 26 | `CAPL.SR.LOCAL.REF` | `CaplHSignatoryRule_LocalRef` |  |  |  |
| 27 | `CAPL.SR.OVERRIDE` | `CaplHSignatoryRule_Override` |  |  |  |
| 28 | `CAPL.SR.RECORD.STATUS` | `CaplHSignatoryRule_RecordStatus` | String |  |  |
| 29 | `CAPL.SR.CURR.NO` | `CaplHSignatoryRule_CurrNo` | String |  |  |
| 30 | `CAPL.SR.INPUTTER` | `CaplHSignatoryRule_Inputter` |  |  |  |
| 31 | `CAPL.SR.DATE.TIME` | `CaplHSignatoryRule_DateTime` |  |  |  |
| 32 | `CAPL.SR.AUTHORISER` | `CaplHSignatoryRule_Authoriser` | String |  |  |
| 33 | `CAPL.SR.CO.CODE` | `CaplHSignatoryRule_CoCode` | String |  |  |
| 34 | `CAPL.SR.DEPT.CODE` | `CaplHSignatoryRule_DeptCode` | String |  |  |
| 35 | `CAPL.SR.AUDITOR.CODE` | `CaplHSignatoryRule_AuditorCode` | String |  |  |
| 36 | `CAPL.SR.AUDIT.DATE.TIME` | `CaplHSignatoryRule_AuditDateTime` | String |  |  |
