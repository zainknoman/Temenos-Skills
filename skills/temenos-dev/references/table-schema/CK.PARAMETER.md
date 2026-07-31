# CK.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CK.PARAMETER` in `CK_Consent.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CK.PARAM.AUTO.CREATE.CONSENT` | `CkParameter_AutoCreateConsent` | TField |  | This field determines whether a consent needed to be created automatically or not Validation Rules: YES Default consent creation will be automated NO Default consent creation will not be automated API A valid EB.API record will be attached, which returns value to automate consent Sample API that can be configured CK.AUTO.CONSENT.CREATION |
| 2 | `CK.PARAM.CONSENT.PRODUCT` | `CkParameter_ConsentProduct` | TField |  | This field determines the consent product to be used for automatic consent creation. Validation Rules: Either a valid consent product or a valid EB.API record which returns a valid consent product. The arguments of this API are CustomerId (IN), ProductID (OUT), ReservedArg1, ReservedArg2. A sample API CK.VALID.CONSENT.PRODUCT is available for reference. |
| 3 | `CK.PARAM.AUTO.BLOCK.CONSENT` | `CkParameter_AutoBlockConsent` | TField |  | This field determines whether to block a consent automatically or not Validation Rules: YES Indicates automatic blocking of customers consent when customer activity is set to inactive NO Automatic consent will not be happened |
| 4 | `CK.PARAM.RESERVED.15` | `CkParameter_Reserved15` | TField |  |  |
| 5 | `CK.PARAM.RESERVED.14` | `CkParameter_Reserved14` | TField |  |  |
| 6 | `CK.PARAM.RESERVED.13` | `CkParameter_Reserved13` | TField |  |  |
| 7 | `CK.PARAM.RESERVED.12` | `CkParameter_Reserved12` | TField |  |  |
| 8 | `CK.PARAM.RESERVED.11` | `CkParameter_Reserved11` | TField |  |  |
| 9 | `CK.PARAM.RESERVED.10` | `CkParameter_Reserved10` | TField |  |  |
| 10 | `CK.PARAM.RESERVED.09` | `CkParameter_Reserved09` | TField |  |  |
| 11 | `CK.PARAM.RESERVED.08` | `CkParameter_Reserved08` | TField |  |  |
| 12 | `CK.PARAM.RESERVED.07` | `CkParameter_Reserved07` | TField |  |  |
| 13 | `CK.PARAM.RESERVED.06` | `CkParameter_Reserved06` | TField |  |  |
| 14 | `CK.PARAM.RESERVED.05` | `CkParameter_Reserved05` | TField |  |  |
| 15 | `CK.PARAM.RESERVED.04` | `CkParameter_Reserved04` | TField |  |  |
| 16 | `CK.PARAM.RESERVED.03` | `CkParameter_Reserved03` | TField |  |  |
| 17 | `CK.PARAM.RESERVED.02` | `CkParameter_Reserved02` | TField |  |  |
| 18 | `CK.PARAM.RESERVED.01` | `CkParameter_Reserved01` | TField |  |  |
| 19 | `CK.PARAM.LOCAL.REF` | `CkParameter_LocalRef` |  |  |  |
| 20 | `CK.PARAM.OVERRIDE` | `CkParameter_Override` |  |  |  |
| 21 | `CK.PARAM.RECORD.STATUS` | `CkParameter_RecordStatus` | String |  |  |
| 22 | `CK.PARAM.CURR.NO` | `CkParameter_CurrNo` | String |  |  |
| 23 | `CK.PARAM.INPUTTER` | `CkParameter_Inputter` |  |  |  |
| 24 | `CK.PARAM.DATE.TIME` | `CkParameter_DateTime` |  |  |  |
| 25 | `CK.PARAM.AUTHORISER` | `CkParameter_Authoriser` | String |  |  |
| 26 | `CK.PARAM.CO.CODE` | `CkParameter_CoCode` | String |  |  |
| 27 | `CK.PARAM.DEPT.CODE` | `CkParameter_DeptCode` | String |  |  |
| 28 | `CK.PARAM.AUDITOR.CODE` | `CkParameter_AuditorCode` | String |  |  |
| 29 | `CK.PARAM.AUDIT.DATE.TIME` | `CkParameter_AuditDateTime` | String |  |  |
