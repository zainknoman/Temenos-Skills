# FATCA.AGGREGATION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FATCA.AGGREGATION.PARAMETER` in `FA_BalanceAggregation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FA.AGP.RELATION.LEVEL` | `FatcaAggregationParameter_RelationLevel` | TField |  | As per the FATCA regulation, the balance of pre-existing accounts needs to be determined taking into account all the accounts/portfolios held by the client including the joint accounts. In the case of joint accounts, the entire balance of the joint account will be attributed to all the joint holders. In T24, the relationship can be defined at Customer Level (CUSTOMER) or account level (ACCOUNT). If the relationships are defined at customer level in T24 CUSTOMER, the field has to be set as CUSTOMER. It will be assumed that all the accounts are jointly held and the balance of all the accounts will be attributed to all the joint holders. However, if the field is set to ACCOUNT, the relationships will be checked at individual account level and only the balances of accounts that are held jointly will be attributed to all the joint holders. Validation Rules: Input allowed: CUSTOMER or ACCOUNT. |
| 2 | `FA.AGP.RELATION.CODE` | `FatcaAggregationParameter_RelationCode` |  |  |  |
| 3 | `FA.AGP.EXCLD.FOR.ACCT.AGG` | `FatcaAggregationParameter_ExcldForAcctAgg` |  |  |  |
| 4 | `FA.AGP.SAM.FIELD` | `FatcaAggregationParameter_SamField` |  |  |  |
| 5 | `FA.AGP.SAM.OPERAND` | `FatcaAggregationParameter_SamOperand` |  |  |  |
| 6 | `FA.AGP.SAM.VALUE` | `FatcaAggregationParameter_SamValue` |  |  |  |
| 7 | `FA.AGP.ROLE.TYPE` | `FatcaAggregationParameter_RoleType` |  |  |  |
| 8 | `FA.AGP.ENT.CUST.FIELD` | `FatcaAggregationParameter_EntCustField` |  |  |  |
| 9 | `FA.AGP.ENT.CUST.OPERAND` | `FatcaAggregationParameter_EntCustOperand` |  |  |  |
| 10 | `FA.AGP.ENT.CUST.VALUE` | `FatcaAggregationParameter_EntCustValue` |  |  |  |
| 11 | `FA.AGP.ACCT.AGGR.RTN` | `FatcaAggregationParameter_AcctAggrRtn` | TField |  | A local routine can be attached here which will be called during balance aggregation batch jobs. This routine will take two arguments, first argument is the customer number second one is FATCA.AGGREGATE.BALANCE record. This routine can be used to consider additional positions for balance aggregation. Customer number is the input argument and FATCA aggregate balance record is both input/output argument. |
| 12 | `FA.AGP.AGGR.BAL.FILE` | `FatcaAggregationParameter_AggrBalFile` | TField |  | This field represents the file which will be selected for balance aggregation processing. If FCSI is chosen then balance will be aggregated for customers having FCSI record. If REPORTABLE.STATUS is chosen balance will be aggregated only for the customers with FCSI, Who is having their FATCA.STATUS as defined in REPORTING.PARAMETER. If nothing is selected then balance will be aggregated as usual for all customers. Validation Rules: Input allowed: FCSI or REPORTABLE.STATUS. |
| 13 | `FA.AGP.EXTERNAL.ARRANGEMENTS` | `FatcaAggregationParameter_ExternalArrangements` | TField |  | This field specifies if contracts from EXTERNAL.ARRANGEMENT.FILE needs to be included in the balance aggregation processing Validation Rules: YES or NO |
| 14 | `FA.AGP.SAME.CUS.REL.CODE` | `FatcaAggregationParameter_SameCusRelCode` |  |  |  |
| 15 | `FA.AGP.INCL.EX.JOINT.HOLDER` | `FatcaAggregationParameter_InclExJointHolder` | TField |  | This field is to instruct the system to store the details of former joint owners or related customers and to include them in the year-end report. Allowed values - YES,NO,NULL YES - When set to YES, whenever a customer is removed from an arrangement(AA.ARRANGEMENT.ACTIVITY>CUSTOMER) or a related customer is removed from customer CUSTOMER>RELATION.CUSTOMER, the details will be stored in FATCA.FCSI.AMENDMENTS and this information will be used in the year-end report. NO, Blank- If set to NO or blank then ex-joint holder details will not be stored or included in the year-end report. Validation Rules: Field value can be changed from NO to YES only once. Once set as YES, this cannot be changed back to NO/NULL. By default, this field is set to NO. |
| 16 | `FA.AGP.RESERVED.07` | `FatcaAggregationParameter_Reserved07` |  |  |  |
| 17 | `FA.AGP.RESERVED.06` | `FatcaAggregationParameter_Reserved06` | TField |  |  |
| 18 | `FA.AGP.RESERVED.05` | `FatcaAggregationParameter_Reserved05` | TField |  |  |
| 19 | `FA.AGP.RESERVED.04` | `FatcaAggregationParameter_Reserved04` | TField |  |  |
| 20 | `FA.AGP.RESERVED.03` | `FatcaAggregationParameter_Reserved03` | TField |  |  |
| 21 | `FA.AGP.RESERVED.02` | `FatcaAggregationParameter_Reserved02` | TField |  |  |
| 22 | `FA.AGP.RESERVED.01` | `FatcaAggregationParameter_Reserved01` | TField |  |  |
| 23 | `FA.AGP.LOCAL.REF` | `FatcaAggregationParameter_LocalRef` |  |  |  |
| 24 | `FA.AGP.OVERRIDE` | `FatcaAggregationParameter_Override` |  |  |  |
| 25 | `FA.AGP.RECORD.STATUS` | `FatcaAggregationParameter_RecordStatus` | String |  |  |
| 26 | `FA.AGP.CURR.NO` | `FatcaAggregationParameter_CurrNo` | String |  |  |
| 27 | `FA.AGP.INPUTTER` | `FatcaAggregationParameter_Inputter` |  |  |  |
| 28 | `FA.AGP.DATE.TIME` | `FatcaAggregationParameter_DateTime` |  |  |  |
| 29 | `FA.AGP.AUTHORISER` | `FatcaAggregationParameter_Authoriser` | String |  |  |
| 30 | `FA.AGP.CO.CODE` | `FatcaAggregationParameter_CoCode` | String |  |  |
| 31 | `FA.AGP.DEPT.CODE` | `FatcaAggregationParameter_DeptCode` | String |  |  |
| 32 | `FA.AGP.AUDITOR.CODE` | `FatcaAggregationParameter_AuditorCode` | String |  |  |
| 33 | `FA.AGP.AUDIT.DATE.TIME` | `FatcaAggregationParameter_AuditDateTime` | String |  |  |
