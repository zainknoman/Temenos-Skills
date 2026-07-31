# USREGS.REG.D.VIOLATION.ACTION — Table Schema

> Source: `INSERTS/I_F.USREGS.REG.D.VIOLATION.ACTION` in `USREGS_RegD.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `VIOLATION.DESCRIPTION` | `UsregsRegDViolationAction_Description` |  |  |  |
| 2 | `VIOLATION.ADVICE` | `UsregsRegDViolationAction_Advice` | TField |  | Field to define the letter type (format &amp; layout) to be sent. Required letter format such as First letter, Second letter, etc. can be selected for corresponding violation action record. Input must be a valid record in EB.ADVICES. |
| 3 | `VIOLATION.CHANGE.PRODUCT` | `UsregsRegDViolationAction_ChangeProduct` | TField |  | Indicator to determine whether product change is required as part of this violation action. The allowed values are YES &amp; NO. |
| 4 | `VIOLATION.TARGET.PRODUCT` | `UsregsRegDViolationAction_TargetProduct` | TField | Yes | Target product or new product to which account will be changed into, in the event of occurance of specified Reg-D violation. Current product type of the account and the target product must be part of same Product Group. Input is mandatory if Change Product is set to Yes and value is not defined in Change Product Rule field. |
| 5 | `VIOLATION.TARGET.PRODUCT.RULE` | `UsregsRegDViolationAction_TargetProductRule` | TField | Yes | ID of rule defined using Rules Engine. The rule will dictate selection of product to change, based on user defined rules, in this case, account balance. Input is mandatory if Change Product is set to Yes and value is not defined in Target Product field. |
| 6 | `VIOLATION.DEFER.DAYS` | `UsregsRegDViolationAction_DeferDays` | TField |  | Number of business days from the period end date after which account product must be changed. Business day definition at account level will be used to identify the change product effective date. If not defined then change of product will occur on period end date. |
| 7 | `VIOLATION.TARGET.ACTIVITY` | `UsregsRegDViolationAction_TargetActivity` | TField |  | The change product activity that must be used to change product type of the account upon breach of Reg D threshold. |
| 8 | `VIOLATION.RESERVED.15` | `UsregsRegDViolationAction_Reserved15` | TField |  |  |
| 9 | `VIOLATION.RESERVED.14` | `UsregsRegDViolationAction_Reserved14` | TField |  |  |
| 10 | `VIOLATION.RESERVED.13` | `UsregsRegDViolationAction_Reserved13` | TField |  |  |
| 11 | `VIOLATION.RESERVED.12` | `UsregsRegDViolationAction_Reserved12` | TField |  |  |
| 12 | `VIOLATION.RESERVED.11` | `UsregsRegDViolationAction_Reserved11` | TField |  |  |
| 13 | `VIOLATION.RESERVED.10` | `UsregsRegDViolationAction_Reserved10` | TField |  |  |
| 14 | `VIOLATION.RESERVED.9` | `UsregsRegDViolationAction_Reserved9` | TField |  |  |
| 15 | `VIOLATION.RESERVED.8` | `UsregsRegDViolationAction_Reserved8` | TField |  |  |
| 16 | `VIOLATION.RESERVED.7` | `UsregsRegDViolationAction_Reserved7` | TField |  |  |
| 17 | `VIOLATION.RESERVED.6` | `UsregsRegDViolationAction_Reserved6` | TField |  |  |
| 18 | `VIOLATION.RESERVED.5` | `UsregsRegDViolationAction_Reserved5` | TField |  |  |
| 19 | `VIOLATION.RESERVED.4` | `UsregsRegDViolationAction_Reserved4` | TField |  |  |
| 20 | `VIOLATION.RESERVED.3` | `UsregsRegDViolationAction_Reserved3` | TField |  |  |
| 21 | `VIOLATION.RESERVED.2` | `UsregsRegDViolationAction_Reserved2` | TField |  |  |
| 22 | `VIOLATION.RESERVED.1` | `UsregsRegDViolationAction_Reserved1` | TField |  |  |
| 23 | `VIOLATION.LOCAL.REF` | `UsregsRegDViolationAction_LocalRef` |  |  |  |
| 24 | `VIOLATION.STMT.NOS` | `UsregsRegDViolationAction_StmtNos` |  |  |  |
| 25 | `VIOLATION.OVERRIDE` | `UsregsRegDViolationAction_Override` |  |  |  |
| 26 | `VIOLATION.RECORD.STATUS` | `UsregsRegDViolationAction_RecordStatus` | String |  |  |
| 27 | `VIOLATION.CURR.NO` | `UsregsRegDViolationAction_CurrNo` | String |  |  |
| 28 | `VIOLATION.INPUTTER` | `UsregsRegDViolationAction_Inputter` |  |  |  |
| 29 | `VIOLATION.DATE.TIME` | `UsregsRegDViolationAction_DateTime` |  |  |  |
| 30 | `VIOLATION.AUTHORISER` | `UsregsRegDViolationAction_Authoriser` | String |  |  |
| 31 | `VIOLATION.CO.CODE` | `UsregsRegDViolationAction_CoCode` | String |  |  |
| 32 | `VIOLATION.DEPT.CODE` | `UsregsRegDViolationAction_DeptCode` | String |  |  |
| 33 | `VIOLATION.AUDITOR.CODE` | `UsregsRegDViolationAction_AuditorCode` | String |  |  |
| 34 | `VIOLATION.AUDIT.DATE.TIME` | `UsregsRegDViolationAction_AuditDateTime` | String |  |  |
