# OX.OBLIGOR.DETAILS — Table Schema

> Source: `INSERTS/I_F.OX.OBLIGOR.DETAILS` in `OX_ObligorObject.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OXOD.DESCRIPTION` | `OxObligorDetails_Description` |  |  |  |
| 2 | `OXOD.OBLIGOR.TYPE` | `OxObligorDetails_ObligorType` | TField |  | This system updated field holds value as Individual, Joint or Relation based on the owner of the Loan. |
| 3 | `OXOD.OBLIGOR.STATUS` | `OxObligorDetails_ObligorStatus` | TField |  | This system updated field determines the status of the obligor, based on the activity of the contracts belonging to the obligors. Validation Rules: Possible values are Active and Inactive. Whenever Obligor Object is created for the first time, OBLIGOR.STATUS will be in ACTIVE. When the status of all individual contracts belonging to a obligor become closed, OBLIGOR.STATUS will be marked as INACTIVE. OBLIGOR.STATUS of Relation obligor will be marked as INACTIVE, when the CUSTOMER.GROUP record is closed. |
| 4 | `OXOD.CREATION.CLOSE.DATE` | `OxObligorDetails_CreationCloseDate` | TField |  | This system updated field holds the date on which the obligor record created for the first time or the date on which it has been closed. This field is updated with Obligor Object Creation date, when the OBLIGOR.STATUS is ACTIVE. This field is updated with Obligor Object Close date, when the OBLIGOR.STATUS becomes INACTIVE. Standard date format. |
| 5 | `OXOD.CUSTOMER.ID` | `OxObligorDetails_CustomerId` |  |  |  |
| 6 | `OXOD.GROUP.PURPOSE` | `OxObligorDetails_GroupPurpose` | TField |  | This system updated field holds valid Customer Group ID. This field is updated only for Relation type of Obligors. This field value is a valid record in CUST.GROUP.PURPOSE Aplhanumeric field. |
| 7 | `OXOD.CONT.APPLICATION` | `OxObligorDetails_ContApplication` |  |  |  |
| 8 | `OXOD.CONTRACT.ID` | `OxObligorDetails_ContractId` |  |  |  |
| 9 | `OXOD.COMPANY.ID` | `OxObligorDetails_CompanyId` |  |  |  |
| 10 | `OXOD.CONTRACT.STATUS` | `OxObligorDetails_ContractStatus` |  |  |  |
| 11 | `OXOD.PREV.OBLIGOR.ID` | `OxObligorDetails_PrevObligorId` |  |  |  |
| 12 | `OXOD.REF.CUSTOMER.ID` | `OxObligorDetails_RefCustomerId` | TField |  | This system updated field holds the Beneficiary owner of the Joint Obligor. This field value is derived based on the DATA.INHERIT.API or DATA.INHERIT.RULE field values defined in OX.OBLIGOR.PARAMETER Single value field. Valid Id from CUSTOMER table. |
| 13 | `OXOD.CONTAGION.RULE` | `OxObligorDetails_ContagionRule` | TField |  | This system updated field holds the Contagion rule based on which the obligor has been contaminated. Validation Rules: NoInput Field. Possible values are ALL.LINKS and THRESHOLD. Example: Let A,C be Individual obligor(IO), AB be Joint Obligor(JO) and AC be Relational Obligor(RO). Assume OX.OBLIGOR.PARAMETER is defined with Contagion Type as Contractual and Relationship with Contagion Rule as Threshold and All.links respectively. Consider A obligor's Status is made Default. Now A will contaminate AB via Threshold rule. Then A will contaminate C via Customer group relation. Hence Contagion Rule field value will be Threshold for AB obligor and will be All.links for C obligor. Contagion link will be updated as A for both AB and C obligors. |
| 14 | `OXOD.LAST.CLASS.DATE` | `OxObligorDetails_LastClassDate` | TField |  | This system updated fields holds the date on which obligor was last classified. Updated by OX.OBLIGOR.CLASSIFY.PROCESS Job. Validation Rules: NoInput Field. Standard date format. |
| 15 | `OXOD.AUTO.CLASS` | `OxObligorDetails_AutoClass` | TField |  | This system updated fields holds the Classification of an obligor. Updated by OX.OBLIGOR.CLASSIFY.PROCESS Job. Validation Rules: NoInput Field. Valid record to PV.LOAN.CLASSIFICATION |
| 16 | `OXOD.AUTO.DEFAULT.STATUS` | `OxObligorDetails_AutoDefaultStatus` | TField |  | This system updated field holds the status of the obligor based on auto classification. Validation Rules: NoInput Field. Possible values are DEFAULT, PERFORMING. DEFAULT status updated, when AUTO.CLASS field value is located in the DEF.EQUI.CLASS field of OX.OBLIGOR.PARAMETER PERFORMING status updated, when AUTO.CLASS field value is not located in the DEF.EQUI.CLASS field of OX.OBLIGOR.PARAMETER |
| 17 | `OXOD.MANUAL.CLASS` | `OxObligorDetails_ManualClass` | TField |  | This field allows the user to manually classify the obligor. Allowed Input only when PV is not installed in the system. Validation Rules: Should be a Valid record in PV.LOAN.CLASSIFICATION, when PV is installed in the company. Should be a valid EB.LOOKUP record in DEFAULT.CLASSIFICATION, when PV is not installed in the company. |
| 18 | `OXOD.MANUAL.DEFAULT.STATUS` | `OxObligorDetails_ManualDefaultStatus` | TField |  | This system updated field holds the status of an obligor based on manual classification. Validation Rules: NoInput Field. Possible values are DEFAULT, PERFORMING. DEFAULT status updated, when MANUAL.CLASS field value is located in the DEF.EQUI.CLASS field of OX.OBLIGOR.PARAMETER PERFORMING status updated, when MANUAL.CLASS field value is not located in the DEF.EQUI.CLASS field of OX.OBLIGOR.PARAMETER |
| 19 | `OXOD.PREV.LAST.CLASS.DATE` | `OxObligorDetails_PrevLastClassDate` |  |  |  |
| 20 | `OXOD.PREV.AUTO.CLASS` | `OxObligorDetails_PrevAutoClass` |  |  |  |
| 21 | `OXOD.PREV.AUTO.DEFAULT.STATUS` | `OxObligorDetails_PrevAutoDefaultStatus` |  |  |  |
| 22 | `OXOD.PREV.MANUAL.CLASS` | `OxObligorDetails_PrevManualClass` |  |  |  |
| 23 | `OXOD.PREV.MANUAL.DEFAULT.STATUS` | `OxObligorDetails_PrevManualDefaultStatus` |  |  |  |
| 24 | `OXOD.CONTAGION.EXCLUDE` | `OxObligorDetails_ContagionExclude` | TField |  | This field indicates whether the obligor is Excluded from Contagion Process. Allowed Values - YES, NULL. Input not allowed for Relation type Obligors and when Contagion fields are not defined in Obligor parameter. |
| 25 | `OXOD.CONTAGION.LINK` | `OxObligorDetails_ContagionLink` | TField |  | This system updated field holds the Id of the obligor that contaminated the current obligor during contagion process. Updated by JX.CONTAGION.PROCESS Job. Valid record in OX.OBLIGOR.DETAILS |
| 26 | `OXOD.LAST.CONTAGION.DATE` | `OxObligorDetails_LastContagionDate` | TField |  | This system updated field denotes the date on which the Obligor has been contaminated recently. Updated by JX.CONTAGION.PROCESS Job. Validation Rules: NoInput Field. Standard date format. |
| 27 | `OXOD.AUTO.CONTAGION.CLASS` | `OxObligorDetails_AutoContagionClass` | TField |  | This system updated field holds the Contagion Class, when the obligor is automatically contaminated during contagion process. Validation Rules: NoInput Field. Valid record to PV.LOAN.CLASSIFICATION |
| 28 | `OXOD.AUTO.CONTAGION.STATUS` | `OxObligorDetails_AutoContagionStatus` | TField |  | This field holds the Contagion status arising out of the automatic contamination done by the system. Validation Rules: NoInput Field. Possible values are DEFAULT, PERFORMING. |
| 29 | `OXOD.MANUAL.CONTAGION.CLASS` | `OxObligorDetails_ManualContagionClass` | TField |  | This field facilitates manual contamination by the user. If the classification given in this field by user, is located in the DEF.EQUI.CLASS of OX.OBLIGOR.PARAMETER. Then Obligor is contaminated. If the classification given in this field by user, is not located in the DEF.EQUI.CLASS of OX.OBLIGOR.PARAMETER. Then Obligor is decontaminated. Validation Rules: NoInput Field. Should be a Valid record in PV.LOAN.CLASSIFICATION, when PV is installed in the company. Should be a valid EB.LOOKUP record in DEFAULT.CLASSIFICATION, when PV is not installed in the company. |
| 30 | `OXOD.MANUAL.CONTAGION.STATUS` | `OxObligorDetails_ManualContagionStatus` | TField |  | This system field holds the Contagion status, as a result of manual contamination triggered by the user. This field value takes precedence over AUTO.CLASS, AUTO.CONTAGION.CLASS and MANUAL.CLASS field values, during provision calculation. Validation Rules: NoInput Field. Possible values are DEFAULT, PERFORMING. |
| 31 | `OXOD.PREV.LAST.CONTAGION.DATE` | `OxObligorDetails_PrevLastContagionDate` |  |  |  |
| 32 | `OXOD.PREV.AUTO.CONTAGION.CLASS` | `OxObligorDetails_PrevAutoContagionClass` |  |  |  |
| 33 | `OXOD.PREV.AUTO.CONTAGION.STATUS` | `OxObligorDetails_PrevAutoContagionStatus` |  |  |  |
| 34 | `OXOD.PREV.MANUAL.CONTAGION.CLASS` | `OxObligorDetails_PrevManualContagionClass` |  |  |  |
| 35 | `OXOD.PREV.MANUAL.CONTAGION.STATUS` | `OxObligorDetails_PrevManualContagionStatus` |  |  |  |
| 36 | `OXOD.PREV.CONTAGION.LINK` | `OxObligorDetails_PrevContagionLink` |  |  |  |
| 37 | `OXOD.RESERVED.7` | `OxObligorDetails_Reserved7` | TField |  |  |
| 38 | `OXOD.RESERVED.6` | `OxObligorDetails_Reserved6` | TField |  |  |
| 39 | `OXOD.RESERVED.5` | `OxObligorDetails_Reserved5` | TField |  |  |
| 40 | `OXOD.RESERVED.4` | `OxObligorDetails_Reserved4` | TField |  |  |
| 41 | `OXOD.RESERVED.3` | `OxObligorDetails_Reserved3` | TField |  |  |
| 42 | `OXOD.RESERVED.2` | `OxObligorDetails_Reserved2` | TField |  |  |
| 43 | `OXOD.RESERVED.1` | `OxObligorDetails_Reserved1` | TField |  |  |
| 44 | `OXOD.LOCAL.REF` | `OxObligorDetails_LocalRef` |  |  |  |
| 45 | `OXOD.OVERRIDE` | `OxObligorDetails_Override` |  |  |  |
| 46 | `OXOD.RECORD.STATUS` | `OxObligorDetails_RecordStatus` | String |  |  |
| 47 | `OXOD.CURR.NO` | `OxObligorDetails_CurrNo` | String |  |  |
| 48 | `OXOD.INPUTTER` | `OxObligorDetails_Inputter` |  |  |  |
| 49 | `OXOD.DATE.TIME` | `OxObligorDetails_DateTime` |  |  |  |
| 50 | `OXOD.AUTHORISER` | `OxObligorDetails_Authoriser` | String |  |  |
| 51 | `OXOD.CO.CODE` | `OxObligorDetails_CoCode` | String |  |  |
| 52 | `OXOD.DEPT.CODE` | `OxObligorDetails_DeptCode` | String |  |  |
| 53 | `OXOD.AUDITOR.CODE` | `OxObligorDetails_AuditorCode` | String |  |  |
| 54 | `OXOD.AUDIT.DATE.TIME` | `OxObligorDetails_AuditDateTime` | String |  |  |
| 55 | `OXOD.CUSTOMER.TYPE` | `OxObligorDetails_CustomerType` |  |  |  |
| 56 | `OXOD.OBLIGOR.CLASSIFICATION` | `OxObligorDetails_ObligorClassification` | TField |  | This system updated field specifies Classification of the obligor based on customer type as Retail / Non-Retail. The Individual and Retail SME obligors fall under the Retail classification, while the corporate and corporate SME obligors fall under the non-retail classification. In case of joint obligor, even if one customer / customers that are part of obligor are CORPORATE or CORPORATE-SME, then obligor will be classified as Non-Retail. Possible values are Retail,Non-Retail |
| 57 | `OXOD.AGG.CURRENCY` | `OxObligorDetails_AggCurrency` | TField |  | This field stores the currency in which the overall exposure of the obligor is calculated. This shall be same as the currency in which the absolute threshold is defined. Valid currency. System updated field from PV.DOD.PARAMETER. |
| 58 | `OXOD.AGG.PAST.DUE.AMT` | `OxObligorDetails_AggPastDueAmt` | TField |  | This field stores the sum of past due balances of all contracts of an obligor in AGG.CURRENCY. Valid amount field. System updated field from PV.DOD.CUSTOMER.DETS. |
| 59 | `OXOD.AGG.EXPOSURE.AMT` | `OxObligorDetails_AggExposureAmt` | TField |  | The field stores the sum exposure of all contracts of an obligor in AGG.CURRENCY. Valid amount field. System updated field from PV.DOD.CUSTOMER.DETS. |
| 60 | `OXOD.DOD.LAST.DEF.DATE` | `OxObligorDetails_DodLastDefDate` | TField |  | This system updated field holds the date on which Regulatory DOD(Definition of Default) based default assessment was last performed on the obligor. Validation Rules: NoInput Field. Standard date format. |
| 61 | `OXOD.DOD.DEF.STATUS` | `OxObligorDetails_DodDefStatus` | TField |  | This system updated field specifies the status of the obligor based on the Regulatory DOD default assessment. Regulatory DOD default assessment - An obligor will be classified as Default or Performing, based on the DPD(Days Past Due) materiality test or UTP indicators. DPD materiality test default the obligor, when both the Absolute threshold amount and Relative threshold percentage is breached for a certain period, defined in the PV.DOD.PARAMETER. Automatic UTP indicator will default the obligor, if the Pulling effective threshold defined in the PV.DOD.PARAMETER is breached. User can also specify manual UTP indicators and default the obligor. Validation Rules: NoInput Field. Possible values are DEFAULT, PERFORMING. DEFAULT status updated, when DPD.DEFAULT.FLAG or UTP.DEFAULT.FLAG or PROB.DEFAULT.FLAG is updated as YES in PV.DOD.CUSTOMER.DETS table. PERFORMING status updated, when DPD.DEFAULT.FLAG, UTP.DEFAULT.FLAG and PROB.DEFAULT.FLAG are null in PV.DOD.CUSTOMER.DETS table. |
| 62 | `OXOD.DOD.MANUAL.DEF.STATUS` | `OxObligorDetails_DodManualDefStatus` | TField |  | This field allows user to manually specify status of an obligor as per regulatory DOD. Input is allowed if RX is installed and PV module is not installed. Value specified in this field takes precedence over DOD.DEF.STATUS. Validation Rules: Options allowed: Default Performing Currently this functionality not available. So NoInput field. |
| 63 | `OXOD.PREV.DOD.LAST.DEF.DATE` | `OxObligorDetails_PrevDodLastDefDate` |  |  |  |
| 64 | `OXOD.PREV.DOD.DEF.STATUS` | `OxObligorDetails_PrevDodDefStatus` |  |  |  |
| 65 | `OXOD.PREV.DOD.MANUAL.DEF.STATUS` | `OxObligorDetails_PrevDodManualDefStatus` |  |  |  |
| 66 | `OXOD.DOD.CONTAGION.LINK` | `OxObligorDetails_DodContagionLink` | TField |  | This system updated field holds the obligor id of the obligor that has contaminated the current obligor based on the regulatory DOD default assessment. System updated field. Updated by OX.OBLIGOR.PROCESS Job. Valid record in OX.OBLIGOR.DETAILS |
| 67 | `OXOD.DOD.LAST.CONTAGION.DATE` | `OxObligorDetails_DodLastContagionDate` | TField |  | This field denotes the date on which the obligor go contaminated, based on regulatory DOD default assessment. The date in this field reflect the �Start� date of the DOD contagion default. This will be cleared only when the status is changed from Default to Performing. System updated field. Updated by OX.OBLIGOR.PROCESS Job. Validation Rules: NoInput Field. Standard date format. |
| 68 | `OXOD.DOD.CONTAGION.STATUS` | `OxObligorDetails_DodContagionStatus` | TField |  | This field specifies the contagion status of an obligor based on regulatory DOD default assessment. The value in this field has a material impact on the regulatory capital calculations, since the contagion default status is considered at par with Default status. System updated field. Updated by OX.OBLIGOR.PROCESS Job. Possible values are Default, Performing. |
| 69 | `OXOD.DOD.MAN.CONTAGION.STATUS` | `OxObligorDetails_DodManContagionStatus` | TField |  | This user inputtable field, thereby enabling the manual contamination of an obligor by the user. Allowed only if RX and JX module is installed and contagion frequency is defined in OX.OBLIGOR.PARAMETER. If present, takes precedence over the value in DOD.CONTAGION.STATUS the manual contamination Validation Rules: Options allowed: Default Performing Currently this functionality not available. So NoInput field. |
| 70 | `OXOD.PREV.DOD.LAST.CONTAGION.DATE` | `OxObligorDetails_PrevDodLastContagionDate` |  |  |  |
| 71 | `OXOD.PREV.DOD.CONTAGION.STATUS` | `OxObligorDetails_PrevDodContagionStatus` |  |  |  |
| 72 | `OXOD.PREV.DOD.MAN.CONTAGION.STATUS` | `OxObligorDetails_PrevDodManContagionStatus` |  |  |  |
| 73 | `OXOD.PREV.DOD.CONTAGION.LINK` | `OxObligorDetails_PrevDodContagionLink` |  |  |  |
| 74 | `OXOD.DOD.JOINT.CONTAGION.LINK` | `OxObligorDetails_DodJointContagionLink` | TField |  |  |
| 75 | `OXOD.DOD.CONTAGION.PROCESS.DATE` | `OxObligorDetails_DodContagionProcessDate` | TField |  | This field denotes the date on which the obligor has been subjected to DOD contagion process. System updated field. Updated by OX.OBLIGOR.PROCESS Job. Validation Rules: NoInput Field. Standard date format. |
