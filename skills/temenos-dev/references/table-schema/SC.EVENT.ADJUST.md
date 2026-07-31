# SC.EVENT.ADJUST — Table Schema

> Source: `INSERTS/I_F.SC.EVENT.ADJUST` in `SC_SccEventCapture.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SADJ.SECURITY.NO` | `ScEventAdjust_SecurityNo` | TField |  | Event Security of an Event . Defaulted with SECURITY.NO from DIARY Validation Rules : NOINPUT Field |
| 2 | `SC.SADJ.OLD.MKT.PRC` | `ScEventAdjust_OldMktPrc` | TField |  | Market Price of Event Security. Defaulted with OLD.MKT.PRC from DIARY Validation Rules : NOINPUT Field |
| 3 | `SC.SADJ.NARRATIVE` | `ScEventAdjust_Narrative` | TField |  | Narrative Field. Defaulted with NARRATIVE from DIARY |
| 4 | `SC.SADJ.EVENT.TYPE` | `ScEventAdjust_EventType` | TField |  | This field holds the event type. Defaulted with EVENT.TYPE from DIARY Validation Rules : NOINPUT Field |
| 5 | `SC.SADJ.EX.DATE` | `ScEventAdjust_ExDate` | TField |  | This field holds the ex date of the event. Defaulted with EX.DATE from DIARY Purpose of this information only field is to aid the user with details of the event, without having to refer tothe DIARY. Validation Rules : NOINPUT Field |
| 6 | `SC.SADJ.PAY.DATE` | `ScEventAdjust_PayDate` | TField |  | This field holds the pay date of the event. Defaulted with PAY.DATE from DIARY Validation Rules : NOINPUT Field |
| 7 | `SC.SADJ.VALUE.DATE` | `ScEventAdjust_ValueDate` | TField |  | This field holds the value date of the event. Defaulted with VALUE.DATE from DIARY Validation Rules : NOINPUT Field |
| 8 | `SC.SADJ.OPTION.DESC` | `ScEventAdjust_OptionDesc` |  |  |  |
| 9 | `SC.SADJ.RATE` | `ScEventAdjust_Rate` |  |  |  |
| 10 | `SC.SADJ.NEW.SEC.NO` | `ScEventAdjust_NewSecNo` |  |  |  |
| 11 | `SC.SADJ.NEW.MKT.PRC` | `ScEventAdjust_NewMktPrc` |  |  |  |
| 12 | `SC.SADJ.302W` | `ScEventAdjust_302w` |  |  |  |
| 13 | `SC.SADJ.302X` | `ScEventAdjust_302x` |  |  |  |
| 14 | `SC.SADJ.HYP.CONV.OLD.RATIO` | `ScEventAdjust_HypConvOldRatio` | TField |  | Hypothetical Conversion Ratio if all Target Shareholders had Exchanged their Shares of Target Common Stock Solelyfor Shares of Acquirer Merger Stock in the Merger This information would be provided by the custodian. The ratio is expressed in conjunction with the fieldHYP.CONV.NEW.RATIO. For example if the ratio is 1:5, i.e., if there are 5 shares of acquirer share for every oneshare of the target stock, then HYP.CONV.OLD.RATIO should be 1 and HYP.CONV.NEW.RATIO would be 5 |
| 15 | `SC.SADJ.HYP.CONV.NEW.RATIO` | `ScEventAdjust_HypConvNewRatio` | TField |  | Hypothetical Conversion Ratio if all Target Shareholders had Exchanged their Shares of Target Common Stock Solelyfor Shares of Acquirer Merger Stock in the Merger This information will be provided by the custodian. This field is used in the conjunction with the fieldHYP.CONV.OLD.RATIO. |
| 16 | `SC.SADJ.FORM.SUBMIT.DATE` | `ScEventAdjust_FormSubmitDate` | TField |  | The last date by which the S302 form needs to be submitted |
| 17 | `SC.SADJ.LOCAL.REF` | `ScEventAdjust_LocalRef` |  |  |  |
| 18 | `SC.SADJ.OVERRIDE` | `ScEventAdjust_Override` |  |  |  |
| 19 | `SC.SADJ.RECORD.STATUS` | `ScEventAdjust_RecordStatus` | String |  |  |
| 20 | `SC.SADJ.CURR.NO` | `ScEventAdjust_CurrNo` | String |  |  |
| 21 | `SC.SADJ.INPUTTER` | `ScEventAdjust_Inputter` |  |  |  |
| 22 | `SC.SADJ.DATE.TIME` | `ScEventAdjust_DateTime` |  |  |  |
| 23 | `SC.SADJ.AUTHORISER` | `ScEventAdjust_Authoriser` | String |  |  |
| 24 | `SC.SADJ.CO.CODE` | `ScEventAdjust_CoCode` | String |  |  |
| 25 | `SC.SADJ.DEPT.CODE` | `ScEventAdjust_DeptCode` | String |  |  |
| 26 | `SC.SADJ.AUDITOR.CODE` | `ScEventAdjust_AuditorCode` | String |  |  |
| 27 | `SC.SADJ.AUDIT.DATE.TIME` | `ScEventAdjust_AuditDateTime` | String |  |  |
| 28 | `SC.SADJ.TAX.EFF.DATE` | `ScEventAdjust_TaxEffDate` | TField |  | This is input field If not manually given, respective SC.TAX.EFF.DATE from diary will be defaulted Validation Rules: Date can not be greater than today |
