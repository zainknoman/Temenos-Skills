# MD.TXN.TYPE.CONDITION — Table Schema

> Source: `INSERTS/I_F.MD.TXN.TYPE.CONDITION` in `MD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MD.TTC.PROVISION.PERCENT` | `MdTxnTypeCondition_ProvisionPercent` | TField | No | PROVISION.PERCENT The input here is used to default the percentage of Cash Margin to be used for a given DEAL.SUB.TYPE in the record. Validation Rules: Optional input |
| 2 | `MD.TTC.MIN.COMM.AMT.LCCY` | `MdTxnTypeCondition_MinCommAmtLccy` | TField |  | MIN.COMM.AMT.LCCY The minimum amount of commission in local currency equivalent. If the minimum commission amount is not defined or specified through the fields CURRENCY and MIN.COMM.AMT,then the local equivalent of the calculated commission is compared against this amount and greater of the two is applied Validation Rules: Standard Amount field. |
| 3 | `MD.TTC.CURRENCY` | `MdTxnTypeCondition_Currency` |  |  |  |
| 4 | `MD.TTC.MIN.COMM.AMT` | `MdTxnTypeCondition_MinCommAmt` |  |  |  |
| 5 | `MD.TTC.MIN.COMM.TENURE` | `MdTxnTypeCondition_MinCommTenure` | TField | No | MIN.COMM.TENURE The minimum tenure represented in days for which the commission is to be calculated. This field is used along with MIN.COMM.AMT. When the resultant commission of a Deal is greater than the default value, the computed value stays. When the resultant commission of a Deal is greater than the default value, but the tenor is less than the default value, the computed value stays. When the resultant commission of a Deal is less than the default value, but the tenor is greater than the default value, the default value is taken. When the resultant commission of a Deal is less than the default value and the tenor is less than the minimum period, the commission is calculated for the default period. If this commission is greater than the default commission, it is applied else the default commission is applied. Validation Rules: Optional input. |
| 6 | `MD.TTC.CATEGORY` | `MdTxnTypeCondition_Category` |  |  |  |
| 7 | `MD.TTC.COMMISSION.RATE` | `MdTxnTypeCondition_CommissionRate` |  |  |  |
| 8 | `MD.TTC.LOCAL.REF` | `MdTxnTypeCondition_LocalRef` |  |  |  |
| 9 | `MD.TTC.DUPLICATE.CHECK` | `MdTxnTypeCondition_DuplicateCheck` |  |  |  |
| 10 | `MD.TTC.CSN.PERIOD` | `MdTxnTypeCondition_CsnPeriod` | TField |  | Period for calculation of commission when commission rate is given. Values are � Monthly, Quarterly, Semester, Null Default value is null. Null indicates that the commission is to be calculated for the actual number of days considering the rate as �per annum� basis. When the csn period is defined, collection of commission must be upfront always. Event processing should be online and process at sod should be Yes and frequency not allowed. Rate change is not allowed if commission period is defined The below table illustrates the calculation of commission based on different csn periods. Commission Rate Csn Period Guarantee Amount Date of Issue Expiry Date Commission per csn period Number of months (csn periods) Total commission 0.1% Monthly 100,000 1st Jan. 2015 15th Mar 2016 100 15 1500 0.25% Quarterly 100,000 1st Jan. 2015 15th Mar 2016 250 5 1250 0.5% Semester 100,000 1st Jan. 2015 15th Mar 2016 500 3 1500 1% Null 100,000 1st Jan. 2015 15th Mar 2016 -- 429 days 1191.62 |
| 11 | `MD.TTC.MIN.COMM.RATE` | `MdTxnTypeCondition_MinCommRate` | TField |  |  |
| 12 | `MD.TTC.RESERVED.5` | `MdTxnTypeCondition_Reserved5` | TField |  |  |
| 13 | `MD.TTC.RESERVED.4` | `MdTxnTypeCondition_Reserved4` | TField |  |  |
| 14 | `MD.TTC.RESERVED.3` | `MdTxnTypeCondition_Reserved3` | TField |  |  |
| 15 | `MD.TTC.RESERVED.2` | `MdTxnTypeCondition_Reserved2` | TField |  |  |
| 16 | `MD.TTC.RESERVED.1` | `MdTxnTypeCondition_Reserved1` | TField |  |  |
| 17 | `MD.TTC.RESERVED.0` | `MdTxnTypeCondition_Reserved0` | TField |  |  |
| 18 | `MD.TTC.OVERRIDE` | `MdTxnTypeCondition_Override` |  |  |  |
| 19 | `MD.TTC.RECORD.STATUS` | `MdTxnTypeCondition_RecordStatus` | String |  |  |
| 20 | `MD.TTC.CURR.NO` | `MdTxnTypeCondition_CurrNo` | String |  |  |
| 21 | `MD.TTC.INPUTTER` | `MdTxnTypeCondition_Inputter` |  |  |  |
| 22 | `MD.TTC.DATE.TIME` | `MdTxnTypeCondition_DateTime` |  |  |  |
| 23 | `MD.TTC.AUTHORISER` | `MdTxnTypeCondition_Authoriser` | String |  |  |
| 24 | `MD.TTC.CO.CODE` | `MdTxnTypeCondition_CoCode` | String |  |  |
| 25 | `MD.TTC.DEPT.CODE` | `MdTxnTypeCondition_DeptCode` | String |  |  |
| 26 | `MD.TTC.AUDITOR.CODE` | `MdTxnTypeCondition_AuditorCode` | String |  |  |
| 27 | `MD.TTC.AUDIT.DATE.TIME` | `MdTxnTypeCondition_AuditDateTime` | String |  |  |
