# BULK.BOOK.TRANSFER — Table Schema

> Source: `INSERTS/I_F.BULK.BOOK.TRANSFER` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BLK.BK.TRANS.BROKER.FROM` | `BulkBookTransfer_BrokerFrom` | TField |  | This field is Inputable only if the first part of ID is Broker.This field is used to capture the BROKER From Number for which the bulk transfer of products is required. |
| 2 | `BLK.BK.TRANS.AGENT.ARR.FR` | `BulkBookTransfer_AgentArrFr` |  |  |  |
| 3 | `BLK.BK.TRANS.REP.FROM` | `BulkBookTransfer_RepFrom` |  |  |  |
| 4 | `BLK.BK.TRANS.CUSTOMER.INCLUDE` | `BulkBookTransfer_CustomerInclude` |  |  |  |
| 5 | `BLK.BK.TRANS.CUSTOMER.EXCLUDE` | `BulkBookTransfer_CustomerExclude` |  |  |  |
| 6 | `BLK.BK.TRANS.PROD.LINE.INCLUDE` | `BulkBookTransfer_ProdLineInclude` |  |  |  |
| 7 | `BLK.BK.TRANS.SAM.PLAN.INCLUDE` | `BulkBookTransfer_SamPlanInclude` | TField |  | This field is used to indicate if the SAM Plan Broker Number should also be changed or not.YES, Means SAM Broker number will changedNO or Blank Means SAM plan should not be included in bulk transfer |
| 8 | `BLK.BK.TRANS.CUSTOMER.SECTOR.INC` | `BulkBookTransfer_CustomerSectorInc` |  |  |  |
| 9 | `BLK.BK.TRANS.CUSTOMER.INDUSTRY.INC` | `BulkBookTransfer_CustomerIndustryInc` |  |  |  |
| 10 | `BLK.BK.TRANS.CUSTOMER.SECTOR.EXC` | `BulkBookTransfer_CustomerSectorExc` |  |  |  |
| 11 | `BLK.BK.TRANS.CUSTOMER.INDUSTRY.EXC` | `BulkBookTransfer_CustomerIndustryExc` |  |  |  |
| 12 | `BLK.BK.TRANS.REP.TO` | `BulkBookTransfer_RepTo` | TField |  | This field is Inputable only if the first part of ID is BrokerThis Field is used to define the REP number to for bulk transfer. |
| 13 | `BLK.BK.TRANS.AGENT.ARR.TO` | `BulkBookTransfer_AgentArrTo` | TField |  | This field is Inputable only if the first part of ID is BrokerThis field is used to define the Agent arrangement number to for bulk transferNote: if there is only 1 agent arrangement, then this field can be left blank, but if there are more than 1, error should be thrown to warn user.This field is used to define the Agent arrangement number to for bulk transfer |
| 14 | `BLK.BK.TRANS.BROKER.TO` | `BulkBookTransfer_BrokerTo` | TField |  | This field is Inputable only if the first part of ID is BrokerThis field is used to define the broker Number to for bulk transfer |
| 15 | `BLK.BK.TRANS.CUSTOMER.FROM` | `BulkBookTransfer_CustomerFrom` | TField |  | This field is Inputable only if the first part of ID is CUSTOMERThis field is used to define the list of customers for bulk transfer of products |
| 16 | `BLK.BK.TRANS.CUS.PROD.LINE.INCUDE` | `BulkBookTransfer_CusProdLineIncude` |  |  |  |
| 17 | `BLK.BK.TRANS.CUSTOMER.TO` | `BulkBookTransfer_CustomerTo` | TField |  | This field is Inputable only if the first part of ID is CUSTOMERThis field is used to define the Customer to for bulk transfer. |
| 18 | `BLK.BK.TRANS.PRODUCT.LINE` | `BulkBookTransfer_ProductLine` |  |  |  |
| 19 | `BLK.BK.TRANS.AA.ACTIVITY.BR` | `BulkBookTransfer_AaActivityBr` |  |  |  |
| 20 | `BLK.BK.TRANS.AA.ACTIVITY.CUS` | `BulkBookTransfer_AaActivityCus` |  |  |  |
| 21 | `BLK.BK.TRANS.OFS.SOURCE` | `BulkBookTransfer_OfsSource` | TField |  | Input allowed only for SYSTEM record |
| 22 | `BLK.BK.TRANS.SAM.VERSION` | `BulkBookTransfer_SamVersion` | TField |  | Input allowed only for SYSTEM record |
| 23 | `BLK.BK.TRANS.AA.ACTIVITY.VERSION` | `BulkBookTransfer_AaActivityVersion` | TField |  | Input allowed only for SYSTEM record |
| 24 | `BLK.BK.TRANS.RESERVED.1` | `BulkBookTransfer_Reserved1` | TField |  |  |
| 25 | `BLK.BK.TRANS.RESERVED.2` | `BulkBookTransfer_Reserved2` | TField |  |  |
| 26 | `BLK.BK.TRANS.RESERVED.3` | `BulkBookTransfer_Reserved3` | TField |  |  |
| 27 | `BLK.BK.TRANS.RESERVED.4` | `BulkBookTransfer_Reserved4` | TField |  |  |
| 28 | `BLK.BK.TRANS.RESERVED.5` | `BulkBookTransfer_Reserved5` | TField |  |  |
| 29 | `BLK.BK.TRANS.RESERVED.6` | `BulkBookTransfer_Reserved6` | TField |  |  |
| 30 | `BLK.BK.TRANS.RESERVED.7` | `BulkBookTransfer_Reserved7` | TField |  |  |
| 31 | `BLK.BK.TRANS.RESERVED.8` | `BulkBookTransfer_Reserved8` | TField |  |  |
| 32 | `BLK.BK.TRANS.RESERVED.9` | `BulkBookTransfer_Reserved9` | TField |  |  |
| 33 | `BLK.BK.TRANS.RESERVED.10` | `BulkBookTransfer_Reserved10` | TField |  |  |
| 34 | `BLK.BK.TRANS.LOCAL.REF` | `BulkBookTransfer_LocalRef` |  |  |  |
| 35 | `BLK.BK.TRANS.OVERRIDE` | `BulkBookTransfer_Override` |  |  |  |
| 36 | `BLK.BK.TRANS.RECORD.STATUS` | `BulkBookTransfer_RecordStatus` | String |  |  |
| 37 | `BLK.BK.TRANS.CURR.NO` | `BulkBookTransfer_CurrNo` | String |  |  |
| 38 | `BLK.BK.TRANS.INPUTTER` | `BulkBookTransfer_Inputter` |  |  |  |
| 39 | `BLK.BK.TRANS.DATE.TIME` | `BulkBookTransfer_DateTime` |  |  |  |
| 40 | `BLK.BK.TRANS.AUTHORISER` | `BulkBookTransfer_Authoriser` | String |  |  |
| 41 | `BLK.BK.TRANS.CO.CODE` | `BulkBookTransfer_CoCode` | String |  |  |
| 42 | `BLK.BK.TRANS.DEPT.CODE` | `BulkBookTransfer_DeptCode` | String |  |  |
| 43 | `BLK.BK.TRANS.AUDITOR.CODE` | `BulkBookTransfer_AuditorCode` | String |  |  |
| 44 | `BLK.BK.TRANS.AUDIT.DATE.TIME` | `BulkBookTransfer_AuditDateTime` | String |  |  |
