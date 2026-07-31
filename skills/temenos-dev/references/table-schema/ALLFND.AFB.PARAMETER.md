# ALLFND.AFB.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ALLFND.AFB.PARAMETER` in `ALLFND_RebalancingOrder.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ALLFND.DISTRIBUTOR.CODE` | `AllfndAfbParameter_DistributorCode` | TField |  | This is the distributor code which will be updated in the outgoing file |
| 2 | `ALLFND.SUBDISTRIBUTOR.CODE` | `AllfndAfbParameter_SubdistributorCode` | TField |  | This is the sub distributor code which will be updated in the outgoing file |
| 3 | `ALLFND.FILEPATH.OUT` | `AllfndAfbParameter_FilepathOut` | TField |  | This is the path where we will extract the out going file |
| 4 | `ALLFND.SESSION` | `AllfndAfbParameter_Session` | TField |  | The session number in which the file got generated |
| 5 | `ALLFND.FUND.ID.PRIORITY` | `AllfndAfbParameter_FundIdPriority` | TField |  | The Value defined in this field should be equal to below values defined in SECURITY.MASTER. 1)I.S.I.N. 2)CUSIP.NO 3)SEDOL.NO 4)AFB Fund Code |
| 6 | `ALLFND.SUB.TRANS.CODE` | `AllfndAfbParameter_SubTransCode` | TField |  | The Value defined in this field should be equal to TRANSACTION.CODE in SEC.OPEN.ORDER for classifying Subscription order in Record type 10. Drop down from SC.TRANS.NAME |
| 7 | `ALLFND.RED.TRANS.CODE` | `AllfndAfbParameter_RedTransCode` | TField |  | The Value defined in this field should be equal to TRANSACTION.CODE in SEC.OPEN.ORDER for classifying Redemption order in Record type 10. Drop down from SC.TRANS.NAME |
| 8 | `ALLFND.TRASPASO.BUY.CODE` | `AllfndAfbParameter_TraspasoBuyCode` | TField |  | The Value defined in this field should be equal to TRANSACTION.CODE in SEC.OPEN.ORDER for classifying Buy leg of Internal Traspaso in Record type 40. Drop down from SC.TRANS.NAME |
| 9 | `ALLFND.TRASPASO.SEL.CODE` | `AllfndAfbParameter_TraspasoSelCode` | TField |  | The Value defined in this field should be equal to TRANSACTION.CODE in SEC.OPEN.ORDER for classifying Sell leg of Internal Traspaso in Record type 40. Drop down from SC.TRANS.NAME |
| 10 | `ALLFND.LOCAL.REF` | `AllfndAfbParameter_LocalRef` |  |  |  |
| 11 | `ALLFND.ALLFND.CHARGE.NAME` | `AllfndAfbParameter_AllfndChargeName` |  |  |  |
| 12 | `ALLFND.ALLFND.FUND.ATTRIBUTE` | `AllfndAfbParameter_AllfndFundAttribute` |  |  |  |
| 13 | `ALLFND.AFB.SESSION.TIME` | `AllfndAfbParameter_AfbSessionTime` |  |  |  |
| 14 | `ALLFND.DISTRIBUTOR.CODE.API` | `AllfndAfbParameter_DistributorCodeApi` | TField |  | This is the distributor code which will be updated in the JSON for api |
| 15 | `ALLFND.SUBDISTRIBUTOR.CODE.API` | `AllfndAfbParameter_SubdistributorCodeApi` | TField |  | This is the sub distributor code which will be updated in the JSON for api |
| 16 | `ALLFND.APP.FIELD` | `AllfndAfbParameter_AppField` | TField |  | This fields accept only values from STANDARD.SELECTION of SEC.ACC.MASTER that will decide the product id |
| 17 | `ALLFND.PRODUCT.CODE` | `AllfndAfbParameter_ProductCode` |  |  |  |
| 18 | `ALLFND.APP.VALUE` | `AllfndAfbParameter_AppValue` |  |  |  |
| 19 | `ALLFND.MIFID.PRODUCT.DETAILS` | `AllfndAfbParameter_MifidProductDetails` | TField |  | Flag For updating fee value of 73.02 in ALLFND.FUND.SECURITY or SC.MIFID.PRODUCT.DETS Yes - Fee value gets updated in SC.MIFID.PRODUCT.DETS and flags in ALLFND.FUND.SECURITY No or None - Both Fee value and flags get updated in ALLFND.FUND.SECURITY |
| 20 | `ALLFND.RESERVED.10` | `AllfndAfbParameter_Reserved10` | TField |  |  |
| 21 | `ALLFND.OVERRIDE` | `AllfndAfbParameter_Override` |  |  |  |
| 22 | `ALLFND.RECORD.STATUS` | `AllfndAfbParameter_RecordStatus` | String |  |  |
| 23 | `ALLFND.CURR.NO` | `AllfndAfbParameter_CurrNo` | String |  |  |
| 24 | `ALLFND.INPUTTER` | `AllfndAfbParameter_Inputter` |  |  |  |
| 25 | `ALLFND.DATE.TIME` | `AllfndAfbParameter_DateTime` |  |  |  |
| 26 | `ALLFND.AUTHORISER` | `AllfndAfbParameter_Authoriser` | String |  |  |
| 27 | `ALLFND.CO.CODE` | `AllfndAfbParameter_CoCode` | String |  |  |
| 28 | `ALLFND.DEPT.CODE` | `AllfndAfbParameter_DeptCode` | String |  |  |
| 29 | `ALLFND.AUDITOR.CODE` | `AllfndAfbParameter_AuditorCode` | String |  |  |
| 30 | `ALLFND.AUDIT.DATE.TIME` | `AllfndAfbParameter_AuditDateTime` | String |  |  |
