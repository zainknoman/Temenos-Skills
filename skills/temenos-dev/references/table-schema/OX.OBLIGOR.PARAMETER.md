# OX.OBLIGOR.PARAMETER — Table Schema

> Source: `INSERTS/I_F.OX.OBLIGOR.PARAMETER` in `OX_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OX.PAR.CONTAGION.EXCLUDE.RULE` | `OxObligorParameter_ContagionExcludeRule` | TField | No | The rule that decides on exclusion of Obligors during Contagion processing. It is optional. This functionality is currently not available. |
| 2 | `OX.PAR.OBLIGOR.API` | `OxObligorParameter_ObligorApi` | TField | Yes | This field holds a valid record ID from EB.API table, for returning the Obligor Type as Individual, Joint or Relational. In EB.API record, specify either a jBC subroutine name with source type as BASIC or a valid java method with a source type as METHOD, which implements an interface defined in the EB.API record HOOK.OX.GET.OBLIGORS See the EB.API record HOOK.OX.GET.OBLIGORS for the list of supported interfaces. Validation Rules: must be a record in EB.API Mandatory Input field. |
| 3 | `OX.PAR.PRODUCT` | `OxObligorParameter_Product` |  |  |  |
| 4 | `OX.PAR.PRODUCT.CAT.START` | `OxObligorParameter_ProductCatStart` |  |  |  |
| 5 | `OX.PAR.PRODUCT.CAT.END` | `OxObligorParameter_ProductCatEnd` |  |  |  |
| 6 | `OX.PAR.PRODUCT.LINE` | `OxObligorParameter_ProductLine` |  |  |  |
| 7 | `OX.PAR.PRODUCT.GRP` | `OxObligorParameter_ProductGrp` |  |  |  |
| 8 | `OX.PAR.CUST.GRP.PURPOSE` | `OxObligorParameter_CustGrpPurpose` |  |  |  |
| 9 | `OX.PAR.DATA.INHERIT.RULE` | `OxObligorParameter_DataInheritRule` | TField | No | The rule which decides on the Reference customer in the Joint Obligor. It is optional input. Validation Rules: This field holds a valid record from EB.RULE.GATEWAY. DATA.INHERIT.RULE and DATA.INHERIT.API field values are mutually inputtable. |
| 10 | `OX.PAR.DATA.INHERIT.API` | `OxObligorParameter_DataInheritApi` | TField | No | The API which decides on the Reference customer in the Joint Obligor. It is optional input. Validation Rules: This field holds a valid record from EB.API. DATA.INHERIT.RULE and DATA.INHERIT.API field values are mutually inputtable. Specify either a jBC subroutine name with source type as BASIC or a valid java method have a entry on EB.API with a source type as METHOD, which implements an interface defined in the EB.API record HOOK.OX.GET.REFERENCE.OBLIGOR. See the EB.API record HOOK.OX.GET.REFERENCE.OBLIGOR for the list of supported interface. |
| 11 | `OX.PAR.DEF.EQUI.CLASS` | `OxObligorParameter_DefEquiClass` |  |  |  |
| 12 | `OX.PAR.CONTAGION.TYPE` | `OxObligorParameter_ContagionType` |  |  |  |
| 13 | `OX.PAR.CONTAGION.RULE` | `OxObligorParameter_ContagionRule` |  |  |  |
| 14 | `OX.PAR.DEFAULT.STATUS.FREQ` | `OxObligorParameter_DefaultStatusFreq` | TField |  | This field allows to define the frequency for Obligor classification process. Validation Rules: Valid frequency to be given. |
| 15 | `OX.PAR.DEFAULT.STATUS.API` | `OxObligorParameter_DefaultStatusApi` | TField |  | Defines the API that returns the Obligor classification. Allowed to input only when PV is not installed. Validation Rules: This field holds a valid record from EB.API. Specify either a jBC subroutine name with source type as BASIC or a valid java method have a entry on EB.API with a source type as METHOD, which implements an interface defined in the EB.API record OX.OBLIGOR.PARAMETER.DEF.CLASS.HOOK. See the EB.API record OX.OBLIGOR.PARAMETER.DEF.CLASS.HOOK for the list of supported interfaces. Can be input only when DEFAULT.STATUS.FREQ is defined. |
| 16 | `OX.PAR.CONTAGION.FREQUENCY` | `OxObligorParameter_ContagionFrequency` | TField |  | This field allows to define the frequency of Contagion Process Contagion Process will happen during COB based on the frequency given here. Validation Rules: Valid frequency to be given. Input is not allowed when PV.MANAGEMENT is not configured. |
| 17 | `OX.PAR.EXTEND.JO.IO.CONTAGION` | `OxObligorParameter_ExtendJoIoContagion` | TField |  | This field controls the second level contamination of JO to another IO, When the current IO is defaulted. Validation Rules: Possible values are Null, No, Yes. Input allowed only when RX is installed. Default value is No, when RX is installed Example: Let A,B be individual obligors and AB be joint obligor. Assume A is in Default and it contaminates AB, via Contractual rule. This is first level contamination. If Extend Jo Io Contagion field is set as Yes, then B will be contaminated by A via the joint obligor AB. If Extend Jo Io Contagion field is set as no, then B will not be contaminated. This field value is applicable only for DOD contagion process. Once the OX.OBLIGOR.PARAMETER set up is completed and OX.OBLIGOR.DETAILS are created. It is not recommended to change the value from yes to no. |
| 18 | `OX.PAR.RESERVED.16` | `OxObligorParameter_Reserved16` | TField |  |  |
| 19 | `OX.PAR.RESERVED.15` | `OxObligorParameter_Reserved15` | TField |  |  |
| 20 | `OX.PAR.RESERVED.14` | `OxObligorParameter_Reserved14` | TField |  |  |
| 21 | `OX.PAR.RESERVED.13` | `OxObligorParameter_Reserved13` | TField |  |  |
| 22 | `OX.PAR.RESERVED.12` | `OxObligorParameter_Reserved12` | TField |  |  |
| 23 | `OX.PAR.RESERVED.11` | `OxObligorParameter_Reserved11` | TField |  |  |
| 24 | `OX.PAR.RESERVED.10` | `OxObligorParameter_Reserved10` | TField |  |  |
| 25 | `OX.PAR.RESERVED.09` | `OxObligorParameter_Reserved09` | TField |  |  |
| 26 | `OX.PAR.RESERVED.08` | `OxObligorParameter_Reserved08` | TField |  |  |
| 27 | `OX.PAR.RESERVED.07` | `OxObligorParameter_Reserved07` | TField |  |  |
| 28 | `OX.PAR.RESERVED.06` | `OxObligorParameter_Reserved06` | TField |  |  |
| 29 | `OX.PAR.RESERVED.05` | `OxObligorParameter_Reserved05` | TField |  |  |
| 30 | `OX.PAR.RESERVED.04` | `OxObligorParameter_Reserved04` | TField |  |  |
| 31 | `OX.PAR.RESERVED.03` | `OxObligorParameter_Reserved03` | TField |  |  |
| 32 | `OX.PAR.RESERVED.02` | `OxObligorParameter_Reserved02` | TField |  |  |
| 33 | `OX.PAR.RESERVED.01` | `OxObligorParameter_Reserved01` | TField |  |  |
| 34 | `OX.PAR.LOCAL.REF` | `OxObligorParameter_LocalRef` |  |  |  |
| 35 | `OX.PAR.OVERRIDE` | `OxObligorParameter_Override` |  |  |  |
| 36 | `OX.PAR.RECORD.STATUS` | `OxObligorParameter_RecordStatus` | String |  |  |
| 37 | `OX.PAR.CURR.NO` | `OxObligorParameter_CurrNo` | String |  |  |
| 38 | `OX.PAR.INPUTTER` | `OxObligorParameter_Inputter` |  |  |  |
| 39 | `OX.PAR.DATE.TIME` | `OxObligorParameter_DateTime` |  |  |  |
| 40 | `OX.PAR.AUTHORISER` | `OxObligorParameter_Authoriser` | String |  |  |
| 41 | `OX.PAR.CO.CODE` | `OxObligorParameter_CoCode` | String |  |  |
| 42 | `OX.PAR.DEPT.CODE` | `OxObligorParameter_DeptCode` | String |  |  |
| 43 | `OX.PAR.AUDITOR.CODE` | `OxObligorParameter_AuditorCode` | String |  |  |
| 44 | `OX.PAR.AUDIT.DATE.TIME` | `OxObligorParameter_AuditDateTime` | String |  |  |
| 45 | `OX.PAR.CUST.SECTOR.TYPE` | `OxObligorParameter_CustSectorType` |  |  |  |
| 46 | `OX.PAR.CUST.CLASS.SECTOR.START` | `OxObligorParameter_CustClassSectorStart` |  |  |  |
| 47 | `OX.PAR.CUST.CLASS.SECTOR.END` | `OxObligorParameter_CustClassSectorEnd` |  |  |  |
| 48 | `OX.PAR.DEFAULT.CUSTOMER.TYPE` | `OxObligorParameter_DefaultCustomerType` | TField | Yes | Purpose of this field is to define default customer sector type to be considered when customer sector doesn't fall in any of the defined sector ranges. Validation Rules: Options allowed: Retail-Oth(Retail Others) Coporate-Oth(Corporate Others) Becomes mandatory when PV.DOD.PARAMETER is setup for the company Input is allowed only when PV.DOD.PARAMETER is setup for the company. |
| 49 | `OX.PAR.OBLIGOR.CLASS.API` | `OxObligorParameter_ObligorClassApi` | TField |  | Allows user to input a API to perform obligor classification. Specify either a jBC subroutine name that have a entry on EB.API with source type as BASICor a valid java method have a entry on EB.API with a source type as METHOD which implements an interface. Validation Rules: Valid EB.API. Either Obligor Class Api or Customer Sector Type can be specified but not both. Currently this functionality is not enabled. |
| 50 | `OX.PAR.IO.JO.THRESHOLD.PERC` | `OxObligorParameter_IoJoThresholdPerc` | TField | Yes | Threshold defined here is referred when an Individual Obligor(IO) tries to contaminate a Joint Obligor(JO). During this contamination, if the percentage obtained in dividing the Exposure of IO to the sum of exposure of IO and JO is greater than the threshold percentage specified here, then the JO will be contaminated. If the IO exposure in default is non material of total exposure of IO and JO, then JO can be excluded from contamination process. Validation Rules: Percentage field of range 0-100. Input mandatory when Contagion Type is Contractual and Contagion Rule is Threshold. Input not allowed, if the Contagion Type is not Contractual and Contagion Rule is not Threshold. |
| 51 | `OX.PAR.JO.IO.THRESHOLD.PERC` | `OxObligorParameter_JoIoThresholdPerc` | TField | Yes | Threshold defined here is referred when an Joint Obligor(IO) tries to contaminate a Individual Obligor(JO). During this contamination, if the percentage obtained in dividing the Exposure of JO to the sum of exposure of IO and JO is greater than the threshold percentage specified here, then the IO will be contaminated. If the JO exposure in default is non material of total exposure of JO and IO, then IO can be excluded from contamination process. Validation Rules: Percentage field of range 0-100. Input mandatory when Contagion Type is Contractual and Contagion Rule is Threshold. Input not allowed, if the Contagion Type is not Contractual and Contagion Rule is not Threshold. |
