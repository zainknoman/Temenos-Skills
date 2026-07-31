# PV.MANAGEMENT — Table Schema

> Source: `INSERTS/I_F.PV.MANAGEMENT` in `PV_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PVM.DESCRIPTION` | `PvManagement_Description` |  |  |  |
| 2 | `PVM.JOB.FREQUENCY` | `PvManagement_JobFrequency` | TField |  | Specifies a recurrence pattern for a scheduled job. Classification Job, PV.CLASSIFICATION will run on this frequency if CLASS.FREQUENCY is not defined. Based on the this, calculation and posting job will run. If CLASS.FREQUENCY is defined, then CLASS.FREQUENCY takes the precedence for arriving next frequency to perform classification job. Validation Rules: Only MONTHLY fqu is allowed. |
| 3 | `PVM.JOB.RUN.DATE` | `PvManagement_JobRunDate` | TField |  | For an ad-hoc job this is the only date the job will be run. |
| 4 | `PVM.POSTING.TIMING` | `PvManagement_PostingTiming` | TField |  | To indicate when Posting should be done Options are, DELAY - It means there is a time lag between Calculation and Posting. |
| 5 | `PVM.POSTING.DELAY` | `PvManagement_PostingDelay` | TField |  | Number of Working days. |
| 6 | `PVM.PROFILE.ID` | `PvManagement_ProfileId` | TField |  | A link to the rules dictating the classification and provisioning calculations. Validation Rules: Should be a valid Id to PV.PROFILE.XREF Based on the calculation date, latest record from PV.PROFILE will be used |
| 7 | `PVM.CLASS.LEVEL` | `PvManagement_ClassLevel` | TField |  | Dictates whether each loan's individual classification will be used for provisioning or whether a customer's worst classification of the loans in the job will be used for all of the loans in the job. CUST.ALL.LOANS and CUST.JOINT.LOANS options are the worst classification to be considered based all the applicable contracts of the customer This is the default setting if not defined at Application Level. The Options are LOAN : If individual's classification is used CUSTOMER: If worst classification for customer is used CUST.ALL.LOANS: Worst classification for the customer across all contracts that are subject to provisioning and for which the customer is the primary owner. CUST.JOINT.LOANS:The PV.CUSTOMER.DETAIL record will be updated by the worst classification for the customer across only the contracts that are owned by the customer and that are subject to provisioning. The joint accounts are ignored here. |
| 8 | `PVM.PRODUCT` | `PvManagement_Product` |  |  |  |
| 9 | `PVM.CLASS.RULE` | `PvManagement_ClassRule` |  |  |  |
| 10 | `PVM.CLASS.API` | `PvManagement_ClassApi` |  |  |  |
| 11 | `PVM.CATEG.START` | `PvManagement_CategStart` |  |  |  |
| 12 | `PVM.CATEG.END` | `PvManagement_CategEnd` |  |  |  |
| 13 | `PVM.PRODUCT.LINE` | `PvManagement_ProductLine` |  |  |  |
| 14 | `PVM.PRODUCT.GRP` | `PvManagement_ProductGrp` |  |  |  |
| 15 | `PVM.LIMIT.PRODUCT.START` | `PvManagement_LimitProductStart` |  |  |  |
| 16 | `PVM.LIMIT.PRODUCT.END` | `PvManagement_LimitProductEnd` |  |  |  |
| 17 | `PVM.CUSTOMER.FIELD` | `PvManagement_CustomerField` |  |  |  |
| 18 | `PVM.CUST.OPERAND` | `PvManagement_CustOperand` |  |  |  |
| 19 | `PVM.CUST.VALUE` | `PvManagement_CustValue` |  |  |  |
| 20 | `PVM.CLASS.FREQUENCY` | `PvManagement_ClassFrequency` | TField | Yes | Holds the frequency at which the assets are to be classified. Classification Job, PV.CLASSIFICATION will run on this frequency if defined, else by considering JOB.FREQUENCY. Used when the classification frequency is different from the job frequency. Validation Rules: Non-Mandatory field Should not be same or greater than JOB.FREQUENCY Allowed frequencies are DAILY, BSNSS, WEEKLY, TWMTH and MONTHLY. |
| 21 | `PVM.LOCAL.REF` | `PvManagement_LocalRef` |  |  |  |
| 22 | `PVM.CALC.POST.FREQ` | `PvManagement_CalcPostFreq` | TField |  | Specifies the recurrence pattern for calculation and posting of provision. When this field is defined, Calculation and Posting of an asset will be performed daily irrespective of the frequency defined in JOB.FREQUENCY field. Validation Rules: Only Business Frequency is allowed |
| 23 | `PVM.SKIP.CUS.DETAIL.UPD` | `PvManagement_SkipCusDetailUpd` | TField |  | This Field is used to control if PV.CUSTOMER.DETAIL file to be updated or not when Class Level is LOAN. If there is no PV.MANAGEMENT record with Class Level as CUST.ALL.LOANS or CUST.JOINT.LOANS then update to PV.CUSTOMER.DETAIL can be skipped by setting this field as YES in any of PV.MANAGEMENT records with Class Level as LOAN. Only those contracts falling under PV.MANAGEMENT with Class Level as LOAN will be skipped if this field is YES. By default PV.CUSTOMER.DETAIL will always be updated for all types of Class Level. |
| 24 | `PVM.RESERVED.6` | `PvManagement_Reserved6` | TField |  |  |
| 25 | `PVM.RESERVED.5` | `PvManagement_Reserved5` | TField |  |  |
| 26 | `PVM.RESERVED.4` | `PvManagement_Reserved4` | TField |  |  |
| 27 | `PVM.RESERVED.3` | `PvManagement_Reserved3` | TField |  |  |
| 28 | `PVM.RESERVED.2` | `PvManagement_Reserved2` | TField |  |  |
| 29 | `PVM.OVERRIDE` | `PvManagement_Override` |  |  |  |
| 30 | `PVM.RECORD.STATUS` | `PvManagement_RecordStatus` | String |  |  |
| 31 | `PVM.CURR.NO` | `PvManagement_CurrNo` | String |  |  |
| 32 | `PVM.INPUTTER` | `PvManagement_Inputter` |  |  |  |
| 33 | `PVM.DATE.TIME` | `PvManagement_DateTime` |  |  |  |
| 34 | `PVM.AUTHORISER` | `PvManagement_Authoriser` | String |  |  |
| 35 | `PVM.CO.CODE` | `PvManagement_CoCode` | String |  |  |
| 36 | `PVM.DEPT.CODE` | `PvManagement_DeptCode` | String |  |  |
| 37 | `PVM.AUDITOR.CODE` | `PvManagement_AuditorCode` | String |  |  |
| 38 | `PVM.AUDIT.DATE.TIME` | `PvManagement_AuditDateTime` | String |  |  |
| 39 | `PVM.SEGMENT.RULE` | `PvManagement_SegmentRule` |  |  |  |
| 40 | `PVM.SEGMENT.API` | `PvManagement_SegmentApi` |  |  |  |
