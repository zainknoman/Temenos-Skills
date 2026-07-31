# ISA.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ISA.PARAMETER` in `UKISA1_Reporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ISA.PARAM.ISA.PRODUCT` | `IsaParameter_IsaProduct` |  |  |  |
| 2 | `ISA.PARAM.JISA.PRODUCT` | `IsaParameter_JisaProduct` |  |  |  |
| 3 | `ISA.PARAM.REPORTING.YEAR` | `IsaParameter_ReportingYear` | TField |  |  |
| 4 | `ISA.PARAM.REP.NAMING.CONV` | `IsaParameter_RepNamingConv` | TField |  | Naming convention for unstructured names in CUSTOMER fields NAME.1 and NAME.101: if the name is supplied as title, forename, middle name(s) or initial(s), surname � for example, Mr John Adam Smith, or Mr John A Smith02: if the name is supplied as surname, forename middle name(s) or initial(s), title � for example, Smith John Adam Mr, or Smith John A Mr03: if the name is supplied as surname, title, forename, middle name(s) or initial(s) � for example, Smith Mr John Adam or Smith Mr John A.04: if the name is supplied as forename, middle names or initial(s), surname � for example, John Adam Smith, or John A Smith05: if the name is supplied as surname, forename, middle names or initial(s) � for example Smith John Adam, or Smith John A |
| 5 | `ISA.PARAM.LOCAL.REF` | `IsaParameter_LocalRef` |  |  |  |
| 6 | `ISA.PARAM.SUN.ID` | `IsaParameter_SunId` | TField |  | The Service User Number (SUN) of the Submitter. The SUN of the submitter may be the same as the message originator if the originator is a direct submitter, or it may be the SUN of a bureau submitting on behalf of an originator. Where messages are inbound (coming from the Cash ISA Transfer Service) the value 999999 will appear in this element.Structural Validation Regular Expression: [B0-9][0-9]{5} |
| 7 | `ISA.PARAM.ACTIVITY.ATTRIBUTE` | `IsaParameter_ActivityAttribute` | TField |  | To define AA.ACTIVITY record which can be used for writing to AA from ISA.TRANSFER for incoming ISA transfer message. |
| 8 | `ISA.PARAM.ARR.CLOSURE.PERIOD` | `IsaParameter_ArrClosurePeriod` | TField |  | Refers to the period within which new arrangements are allowed to be cancelled. |
| 9 | `ISA.PARAM.REGD.CONTACT.ROLE` | `IsaParameter_RegdContactRole` | TField | Yes | Refers to the specific role to be considered as the Legal guardian. This role will be a mandatory input at the time of opening JISA. Further, to be removed on the 18th birth anniversary of the customer. |
| 10 | `ISA.PARAM.YEAR.END.DATE` | `IsaParameter_YearEndDate` | TField |  | Tax end date for the current year is given here |
| 11 | `ISA.PARAM.HELP.TO.BUY.ADD.ALLW` | `IsaParameter_HelpToBuyAddAllw` | TField |  | The first time subscription allowance for the HelptoBuy ISA product. |
| 12 | `ISA.PARAM.RESERVED.4` | `IsaParameter_Reserved4` |  |  |  |
| 13 | `ISA.PARAM.RESERVED.3` | `IsaParameter_Reserved3` |  |  |  |
| 14 | `ISA.PARAM.RESERVED.2` | `IsaParameter_Reserved2` |  |  |  |
| 15 | `ISA.PARAM.RESERVED.1` | `IsaParameter_Reserved1` |  |  |  |
| 16 | `ISA.PARAM.OVERRIDE` | `IsaParameter_Override` |  |  |  |
| 17 | `ISA.PARAM.RECORD.STATUS` | `IsaParameter_RecordStatus` | String |  |  |
| 18 | `ISA.PARAM.CURR.NO` | `IsaParameter_CurrNo` | String |  |  |
| 19 | `ISA.PARAM.INPUTTER` | `IsaParameter_Inputter` |  |  |  |
| 20 | `ISA.PARAM.DATE.TIME` | `IsaParameter_DateTime` |  |  |  |
| 21 | `ISA.PARAM.AUTHORISER` | `IsaParameter_Authoriser` | String |  |  |
| 22 | `ISA.PARAM.CO.CODE` | `IsaParameter_CoCode` | String |  |  |
| 23 | `ISA.PARAM.DEPT.CODE` | `IsaParameter_DeptCode` | String |  |  |
| 24 | `ISA.PARAM.AUDITOR.CODE` | `IsaParameter_AuditorCode` | String |  |  |
| 25 | `ISA.PARAM.AUDIT.DATE.TIME` | `IsaParameter_AuditDateTime` | String |  |  |
