# COLLATERAL.RIGHT — Table Schema

> Source: `INSERTS/I_F.COLLATERAL.RIGHT` in `CO_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COLL.RIGHT.COLLATERAL.CODE` | `CollateralRight_CollateralCode` | TField | Yes | Code of the category to which the collateral right belongs. The content of this field must be a valid code defined on the collateral code file. Validation Rules: 1-3 digit numeric. (Mandatory input) |
| 2 | `COLL.RIGHT.COMPANY` | `CollateralRight_Company` |  |  |  |
| 3 | `COLL.RIGHT.LIMIT.REFERENCE` | `CollateralRight_LimitReference` |  |  |  |
| 4 | `COLL.RIGHT.LIMIT.REF.CUST` | `CollateralRight_LimitRefCust` |  |  |  |
| 5 | `COLL.RIGHT.PERCENT.ALLOC` | `CollateralRight_PercentAlloc` |  |  |  |
| 6 | `COLL.RIGHT.ALLOCATION.CCY` | `CollateralRight_AllocationCcy` |  |  |  |
| 7 | `COLL.RIGHT.ALLOCATION.AMT` | `CollateralRight_AllocationAmt` |  |  |  |
| 8 | `COLL.RIGHT.LIMIT.CAP.PERC` | `CollateralRight_LimitCapPerc` |  |  |  |
| 9 | `COLL.RIGHT.RESERVED.5` | `CollateralRight_Reserved5` |  |  |  |
| 10 | `COLL.RIGHT.RESERVED.6` | `CollateralRight_Reserved6` |  |  |  |
| 11 | `COLL.RIGHT.PERCENTAGE.COVER` | `CollateralRight_PercentageCover` | TField | No | The percentage of cover which applies to the collateral. The percentage of cover belonging to a collateral right is calculated by the formula: % of cover = 100 x debit balance / value where: debit balance = (sum of) debit balance(s) under the limit reference (or contract id) belonging to the collateral right. value = (sum of) net execution value(s) belonging to collateral objects attached to the right, net execution value = execution value - third party value. Note that, for the purposes of this calculation, the system always assumes that the entire value of a given entity belongs exclusively to the right under which it occurs. The percentage of cover may initially be entered by the user and subsequently updated periodically by the system according to a frequency determined per collateral code. This field may take the value zero (=0%) or null (=unknown or not applicable) or greater than 100%. The system-calculated value is available as an on-line default (when attached collateral values have been authorized), but will not override any user-input. The value in this field is for information only, and has no subsequent impact on the system's reallocation process (ie. in determining whether a given level of excess value exists). Note : If the system's calculation of this value yields an invalid result, the value 999 will be returned. Validation Rules: 1 to 3-digit numeric. (Optional input) |
| 12 | `COLL.RIGHT.VALIDITY.DATE` | `CollateralRight_ValidityDate` | TField | Yes | The date upon which the collateral right becomes effective. This date corresponds to the date on which the right of security becomes legal. A forward date may be entered, in which case no reallocation of the attached collateral values will take place (the status of the record is treated as 'forward'). Validation Rules: 11 type D characters. Mandatory input; default is today's date. |
| 13 | `COLL.RIGHT.REVIEW.DATE.FQU` | `CollateralRight_ReviewDateFqu` | TField | No | The review date &amp; frequency which is to apply to the collateral right. The date of the next review combined with the frequency of review. A default frequency may be defined on the collateral code file. If so, the value of this field defaults to one cycle forward from today's date according to this default frequency. The date part of this field is automatically cycled by the system. Validation Rules: 17 type frequency format. (Optional input; default, if applicable, according to the collateral code) |
| 14 | `COLL.RIGHT.EXPIRY.DATE` | `CollateralRight_ExpiryDate` | TField | No | The expiry date of the collateral right. For certain types of collateral, the values attached to the collateral may only be valid for a limited period. This field may be used to record, in advance, the expiry date associated with the collateral. Although this is mainly for reporting and management purposes, the presence of a date in this field also blocks the reallocation process for the collateral values (after such date has passed). A past date in this field always indicates a status of 'liquidated', both on the collateral right itself and on any associated collateral objects. Validation Rules: 11 type D (date format). (Optional input) The date may not be earlier than the VALIDITY.DATE. |
| 15 | `COLL.RIGHT.NOTARY` | `CollateralRight_Notary` | TField | No | A customer id which may be used to reference details of the public notary. Details of the public notary are recorded on a customer record, which is indicated in this field. Validation Rules: 1-10 digit numeric (customer id). (Optional input) |
| 16 | `COLL.RIGHT.NOTES` | `CollateralRight_Notes` |  |  |  |
| 17 | `COLL.RIGHT.CUSTOMER` | `CollateralRight_Customer` |  |  |  |
| 18 | `COLL.RIGHT.LOCAL.REF` | `CollateralRight_LocalRef` |  |  |  |
| 19 | `COLL.RIGHT.STATUS` | `CollateralRight_Status` | TField |  | The status of the collateral right. The status of the collateral right is indicated in this field as follows: FWD - forward status; validity date is forward; CUR - current status; expiry date is forward &amp; validity date is not; LIQ - liquidated status; expiry date is past; MAT - matured status; record occurs only on history file. The only status under which a collateral right is considered by the system's reallocation process is current. In most cases, the status indicated against the collateral right will also be indicated against any collateral objects belonging to the right. The sole exception is when a collateral object has an earlier expiry date than its corresponding right (in which case the object is considered expired whilst the right remains current). This field is automatically maintained by the system by an end-of-day process and is updated in accordance with any changes to the dates entered on-line. Validation Rules: 'FWD', 'CUR', 'LIQ' or 'MAT'. Internal field. This is a NOINPUT field. |
| 20 | `COLL.RIGHT.LIMIT.ID` | `CollateralRight_LimitId` |  |  |  |
| 21 | `COLL.RIGHT.OS.PERCENT.COVER` | `CollateralRight_OsPercentCover` | TField |  | Reserved for future use. |
| 22 | `COLL.RIGHT.ALLOC.WORK.ID` | `CollateralRight_AllocWorkId` | TField |  | This is a work field used by the system to maintain a temporary pointer to a work record used in the allocation of collateral. It has no direct business use. Validation Rules: System-maintained |
| 23 | `COLL.RIGHT.COLLATERAL.ID` | `CollateralRight_CollateralId` |  |  |  |
| 24 | `COLL.RIGHT.CO.PRIORITY` | `CollateralRight_CoPriority` | TField | No | Defines the priority of the Collateral Right Input not allowed for Collateral Right of old ID format that is A.1. It will be defaulted from the Collateral Right ID. Validation Rules: For transaction key type Collateral Right,this is an Optional field.If this field value is not given, this Collateral Right will be given the least precedence over the Collateral Right where priority is defined. |
| 25 | `COLL.RIGHT.RESERVED.1` | `CollateralRight_Reserved1` | TField |  |  |
| 26 | `COLL.RIGHT.OVERRIDE` | `CollateralRight_Override` |  |  |  |
| 27 | `COLL.RIGHT.RECORD.STATUS` | `CollateralRight_RecordStatus` | String |  |  |
| 28 | `COLL.RIGHT.CURR.NO` | `CollateralRight_CurrNo` | String |  |  |
| 29 | `COLL.RIGHT.INPUTTER` | `CollateralRight_Inputter` |  |  |  |
| 30 | `COLL.RIGHT.DATE.TIME` | `CollateralRight_DateTime` |  |  |  |
| 31 | `COLL.RIGHT.AUTHORISER` | `CollateralRight_Authoriser` | String |  |  |
| 32 | `COLL.RIGHT.CO.CODE` | `CollateralRight_CoCode` | String |  |  |
| 33 | `COLL.RIGHT.DEPT.CODE` | `CollateralRight_DeptCode` | String |  |  |
| 34 | `COLL.RIGHT.AUDITOR.CODE` | `CollateralRight_AuditorCode` | String |  |  |
| 35 | `COLL.RIGHT.AUDIT.DATE.TIME` | `CollateralRight_AuditDateTime` | String |  |  |
