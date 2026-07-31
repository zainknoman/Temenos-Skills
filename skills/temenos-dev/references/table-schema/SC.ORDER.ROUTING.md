# SC.ORDER.ROUTING — Table Schema

> Source: `INSERTS/I_F.SC.ORDER.ROUTING` in `SC_SctOrderCapture.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ORR.ROUT.COMPANY` | `ScOrderRouting_RoutCompany` |  |  |  |
| 2 | `SC.ORR.ROUT.SEC.ACC` | `ScOrderRouting_RoutSecAcc` |  |  |  |
| 3 | `SC.ORR.APP.FIELD` | `ScOrderRouting_AppField` |  |  |  |
| 4 | `SC.ORR.APP.OPERATOR` | `ScOrderRouting_AppOperator` |  |  |  |
| 5 | `SC.ORR.APP.DELIMIT` | `ScOrderRouting_AppDelimit` |  |  |  |
| 6 | `SC.ORR.APP.VALUE` | `ScOrderRouting_AppValue` |  |  |  |
| 7 | `SC.ORR.APPLICATION` | `ScOrderRouting_Application` |  |  |  |
| 8 | `SC.ORR.DEFAULT.COMPANY` | `ScOrderRouting_DefaultCompany` |  |  |  |
| 9 | `SC.ORR.DEFAULT.PORTFOLIO` | `ScOrderRouting_DefaultPortfolio` |  |  |  |
| 10 | `SC.ORR.EXE.ORIG.COMP` | `ScOrderRouting_ExeOrigComp` | TField |  | This field will be used to determine where the execution of a routed order will take place.If set to YES, then the routed order will be executed in the originating (Bank) company and the executionwill be mirrored in the route-to (Broker-dealer) company Validation Rules: Allowed Values: Yes or Blank. Default Value will be Blank. |
| 11 | `SC.ORR.RESERVED.5` | `ScOrderRouting_Reserved5` | TField |  |  |
| 12 | `SC.ORR.RESERVED.4` | `ScOrderRouting_Reserved4` | TField |  |  |
| 13 | `SC.ORR.RESERVED.3` | `ScOrderRouting_Reserved3` | TField |  |  |
| 14 | `SC.ORR.RESERVED.2` | `ScOrderRouting_Reserved2` | TField |  |  |
| 15 | `SC.ORR.RESERVED.1` | `ScOrderRouting_Reserved1` | TField |  |  |
| 16 | `SC.ORR.RESERVED.0` | `ScOrderRouting_Reserved0` | TField |  |  |
| 17 | `SC.ORR.LOCAL.REF` | `ScOrderRouting_LocalRef` |  |  |  |
| 18 | `SC.ORR.OVERRIDE` | `ScOrderRouting_Override` |  |  |  |
| 19 | `SC.ORR.RECORD.STATUS` | `ScOrderRouting_RecordStatus` | String |  |  |
| 20 | `SC.ORR.CURR.NO` | `ScOrderRouting_CurrNo` | String |  |  |
| 21 | `SC.ORR.INPUTTER` | `ScOrderRouting_Inputter` |  |  |  |
| 22 | `SC.ORR.DATE.TIME` | `ScOrderRouting_DateTime` |  |  |  |
| 23 | `SC.ORR.AUTHORISER` | `ScOrderRouting_Authoriser` | String |  |  |
| 24 | `SC.ORR.CO.CODE` | `ScOrderRouting_CoCode` | String |  |  |
| 25 | `SC.ORR.DEPT.CODE` | `ScOrderRouting_DeptCode` | String |  |  |
| 26 | `SC.ORR.AUDITOR.CODE` | `ScOrderRouting_AuditorCode` | String |  |  |
| 27 | `SC.ORR.AUDIT.DATE.TIME` | `ScOrderRouting_AuditDateTime` | String |  |  |
