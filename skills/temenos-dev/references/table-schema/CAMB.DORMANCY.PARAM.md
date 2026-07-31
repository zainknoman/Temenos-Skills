# CAMB.DORMANCY.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.DORMANCY.PARAM` in `CADEPO_Dormancy.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DOR.PARAM.STATUS` | `CambDormancyParam_Status` |  |  |  |
| 2 | `DOR.PARAM.UNCLAIM.ACCT` | `CambDormancyParam_UnclaimAcct` |  |  |  |
| 3 | `DOR.PARAM.REST.ACT` | `CambDormancyParam_RestAct` |  |  |  |
| 4 | `DOR.PARAM.ELIG.TO.ACTIVE` | `CambDormancyParam_EligToActive` |  |  |  |
| 5 | `DOR.PARAM.DORM.OVERRIDE` | `CambDormancyParam_DormOverride` |  |  |  |
| 6 | `DOR.PARAM.FREQ.OF.CLOSURE` | `CambDormancyParam_FreqOfClosure` |  |  |  |
| 7 | `DOR.PARAM.RESERVED.7` | `CambDormancyParam_Reserved7` |  |  |  |
| 8 | `DOR.PARAM.RESERVED.8` | `CambDormancyParam_Reserved8` |  |  |  |
| 9 | `DOR.PARAM.RESERVED.9` | `CambDormancyParam_Reserved9` |  |  |  |
| 10 | `DOR.PARAM.TXN.TYPE` | `CambDormancyParam_TxnType` | TField |  | This field is an associated multi-value set along with TXN.TYPE, BAL.TYPE, REQ.CLOSE.ACCT and CLOSE.ACT which are used to define the Product line, Txn type, bal type, close activity and request closure activity for movement of funds and closure of prolonged inactive account. Part of Multi-Value set Field to indicate the transaction type to define the FTTC based on product line |
| 11 | `DOR.PARAM.OFS.VERSION` | `CambDormancyParam_OfsVersion` | TField |  | The field is used to define the version, which is to be used to transfer funds to unclaimed account during closure. |
| 12 | `DOR.PARAM.BAL.TYPE` | `CambDormancyParam_BalType` | TField |  | This field is an associated multi-value set field which is used to define the Balance type, which should be referred for movement of funds. Part of Multi-Value set Balance type to be considered for the product line. |
| 13 | `DOR.PARAM.REQ.CLOSE.ACT` | `CambDormancyParam_ReqCloseAct` | TField |  |  |
| 14 | `DOR.PARAM.CLOSE.ACT` | `CambDormancyParam_CloseAct` | TField |  | This field is an associated multi-value set along with TXN.TYPE, BAL.TYPE, REQ.CLOSE.ACCT and CLOSE.ACT which are used to define the Product line, Txn type, bal type, close activity and request closure activity for movement of funds and closure of prolonged inactive account. Part of Multi-Value set Valid record from AA.ACTIVITY |
| 15 | `DOR.PARAM.OFS.SOURCE` | `CambDormancyParam_OfsSource` | TField |  | OFS to be used for closure of account and moving the funds to unclaimed account.This field is used to configure the OFS source id for the account which are close based on dormancy. Validations-This field will be allowed to input only when record id as SYSTEM. This is used for mass closure of account. |
| 16 | `DOR.PARAM.AAA.OFS.VERSION` | `CambDormancyParam_AaaOfsVersion` | TField |  | The field is used to define the version, which is to be used during request closure or closure Activity Validations-This field will be allowed to input only when record id as SYSTEM. This is used for mass closure of account. |
| 17 | `DOR.PARAM.EXCLUDE.ARR.STATUS` | `CambDormancyParam_ExcludeArrStatus` |  |  |  |
| 18 | `DOR.PARAM.AAA.SIM.VERSION` | `CambDormancyParam_AaaSimVersion` | TField |  | This field is used to store the simulation activity used for dormancy closure. Valid record from VERSION table. Validations-This field will be allowed to input only when record id as SYSTEM. This is used for mass closure of account. |
| 19 | `DOR.PARAM.NON.FINAN.ACT` | `CambDormancyParam_NonFinanAct` | TField |  | This field is used to define the non financial activty, which needs to be considered for account activation via MDI.This activity will be performed when the member login request is posted within the dormancy period and keep the account in active status.Valid record from AA.ACTIVITY table. |
| 20 | `DOR.PARAM.EXC.SECTOR` | `CambDormancyParam_ExcSector` |  |  |  |
| 21 | `DOR.PARAM.EXC.INDUSTRY` | `CambDormancyParam_ExcIndustry` |  |  |  |
| 22 | `DOR.PARAM.EXC.PRODUCT` | `CambDormancyParam_ExcProduct` |  |  |  |
| 23 | `DOR.PARAM.MASS.ACTIVE.VALIDATION` | `CambDormancyParam_MassActiveValidation` | TField |  | This field is used to define whether the mass activation validation needs to be performed for user priliveges during mass activation.When the user is allowed with necessary privileges of override classes, system will allow to proceed with mass activation. This field is allowed atSYSTEM record level in CAMB.DORMANCY.PARAM table.Allowed values are Yes_No_None.Yes - User will be restricted with a message for the missing override class and Account reset activity will not be allowed.No/None - User will not be warned with a message for the missing override class but the Account reset activity will go INAONote:If the override class is present at user level then mass activate will be allowed in both the cases.Override class will be configured at the override record level, which will be defined in CAMB.DORMANCY.PARAM > DORM.OVERRIDE field for each status separately as per the needs. |
| 24 | `DOR.PARAM.ACCT.LIMIT.CLOSE` | `CambDormancyParam_AcctLimitClose` | TField |  |  |
| 25 | `DOR.PARAM.RESERVED.4` | `CambDormancyParam_Reserved4` | TField |  |  |
| 26 | `DOR.PARAM.RESERVED.3` | `CambDormancyParam_Reserved3` | TField |  |  |
| 27 | `DOR.PARAM.RESERVED.2` | `CambDormancyParam_Reserved2` | TField |  |  |
| 28 | `DOR.PARAM.RESERVED.1` | `CambDormancyParam_Reserved1` | TField |  |  |
| 29 | `DOR.PARAM.LOCAL.REF` | `CambDormancyParam_LocalRef` |  |  |  |
| 30 | `DOR.PARAM.OVERRIDE` | `CambDormancyParam_Override` |  |  |  |
| 31 | `DOR.PARAM.RECORD.STATUS` | `CambDormancyParam_RecordStatus` | String |  |  |
| 32 | `DOR.PARAM.CURR.NO` | `CambDormancyParam_CurrNo` | String |  |  |
| 33 | `DOR.PARAM.INPUTTER` | `CambDormancyParam_Inputter` |  |  |  |
| 34 | `DOR.PARAM.DATE.TIME` | `CambDormancyParam_DateTime` |  |  |  |
| 35 | `DOR.PARAM.AUTHORISER` | `CambDormancyParam_Authoriser` | String |  |  |
| 36 | `DOR.PARAM.CO.CODE` | `CambDormancyParam_CoCode` | String |  |  |
| 37 | `DOR.PARAM.DEPT.CODE` | `CambDormancyParam_DeptCode` | String |  |  |
| 38 | `DOR.PARAM.AUDITOR.CODE` | `CambDormancyParam_AuditorCode` | String |  |  |
| 39 | `DOR.PARAM.AUDIT.DATE.TIME` | `CambDormancyParam_AuditDateTime` | String |  |  |
