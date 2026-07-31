# DEP.H.EXT.TFR.PARAM — Table Schema

> Source: `INSERTS/I_F.DEP.H.EXT.TFR.PARAM` in `CABASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DEP.EXT.PROPERTY` | `DepHExtTfrParam_Property` |  |  |  |
| 2 | `DEP.EXT.PAYMENT.ORDER.PRODUCT` | `DepHExtTfrParam_PaymentOrderProduct` |  |  |  |
| 3 | `DEP.EXT.BENEFICIARY` | `DepHExtTfrParam_Beneficiary` |  |  |  |
| 4 | `DEP.EXT.AGENT.ID` | `DepHExtTfrParam_AgentId` | TField |  | Field is used to store the agent details which is be considered for the ID Customer.Input for the record with CUSTOMER ID.Validation: record from CUSTOMER table.Eg.ID : 100932AGENT.ID: 100931AGENT.ARR.ID: AA153502D2D8When an arrangement is created for a customer 100932, AGENT.ID and AGENT.ARR.ID at the arrangement level is defaulted with the details in AGENT.ID and AGENT.ARR.ID respectively.Note: Arrangement ID of AGENT Product line created for customer given in the field AGENT.ID |
| 5 | `DEP.EXT.AGENT.ARR.ID` | `DepHExtTfrParam_AgentArrId` | TField |  | Field is used to store the agent arrangement details which is be considered for the ID Customer.Input for the record with CUSTOMER ID.Validation: record from CUSTOMER table.Eg.ID : 100932AGENT.ID: 100931AGENT.ARR.ID: AA153502D2D8When an arrangement is created for a customer 100932, AGENT.ID and AGENT.ARR.ID at the arrangement level is defaulted with the details in AGENT.ID and AGENT.ARR.ID respectively. |
| 6 | `DEP.EXT.UPD.COMM.ACT.AA` | `DepHExtTfrParam_UpdCommActAa` | TField |  | Field is used to store the valid ACTIVITY id to default the agent details like AGENT.ID and AGENT arrangement ID in the product commission property at arrangement level.Applicable for ACCOUNTS product line.Validation: To be configured only in SYSTEM record.Valid record of AA.ACTIVITYeg. ACCOUNTS-UPDATE-AGENT.INFO |
| 7 | `DEP.EXT.UPD.COMM.ACT.AD` | `DepHExtTfrParam_UpdCommActAd` | TField |  | Field is is used to store the valid ACTIVITY id to default the agent details like AGENT.ID and AGENT arrangement ID in the product commission property at arrangement level.Applicable for DEPOSITS product line.Validation: To be configured only in SYSTEM record.Valid record of AA.ACTIVITYeg. LENDING-UPDATE-AGENT.INFO |
| 8 | `DEP.EXT.UPD.COMM.ACT.LD` | `DepHExtTfrParam_UpdCommActLd` | TField |  |  |
| 9 | `DEP.EXT.PRODUCT.LINE` | `DepHExtTfrParam_ProductLine` |  |  |  |
| 10 | `DEP.EXT.PRODUCT.GROUP` | `DepHExtTfrParam_ProductGroup` |  |  |  |
| 11 | `DEP.EXT.PRODUCT` | `DepHExtTfrParam_Product` |  |  |  |
| 12 | `DEP.EXT.RESERVED.5` | `DepHExtTfrParam_Reserved5` |  |  |  |
| 13 | `DEP.EXT.RESERVED.4` | `DepHExtTfrParam_Reserved4` |  |  |  |
| 14 | `DEP.EXT.RESERVED.3` | `DepHExtTfrParam_Reserved3` |  |  |  |
| 15 | `DEP.EXT.RESERVED.2` | `DepHExtTfrParam_Reserved2` |  |  |  |
| 16 | `DEP.EXT.RESERVED.1` | `DepHExtTfrParam_Reserved1` |  |  |  |
| 17 | `DEP.EXT.PAYMENT.TYPE` | `DepHExtTfrParam_PaymentType` |  |  |  |
| 18 | `DEP.EXT.PAYIN.ACCOUNT` | `DepHExtTfrParam_PayinAccount` |  |  |  |
| 19 | `DEP.EXT.PAYIN.BEN` | `DepHExtTfrParam_PayinBen` |  |  |  |
| 20 | `DEP.EXT.PAYIN.PO.PROD` | `DepHExtTfrParam_PayinPoProd` |  |  |  |
| 21 | `DEP.EXT.RESERVED.10` | `DepHExtTfrParam_Reserved10` |  |  |  |
| 22 | `DEP.EXT.RESERVED.9` | `DepHExtTfrParam_Reserved9` |  |  |  |
| 23 | `DEP.EXT.RESERVED.8` | `DepHExtTfrParam_Reserved8` |  |  |  |
| 24 | `DEP.EXT.RESERVED.7` | `DepHExtTfrParam_Reserved7` |  |  |  |
| 25 | `DEP.EXT.RESERVED.6` | `DepHExtTfrParam_Reserved6` |  |  |  |
| 26 | `DEP.EXT.PROPERTY.CLASS` | `DepHExtTfrParam_PropertyClass` |  |  |  |
| 27 | `DEP.EXT.PAYOUT.PROPERTY` | `DepHExtTfrParam_PayoutProperty` |  |  |  |
| 28 | `DEP.EXT.PAYOUT.ACCOUNT` | `DepHExtTfrParam_PayoutAccount` |  |  |  |
| 29 | `DEP.EXT.PAYOUT.BEN` | `DepHExtTfrParam_PayoutBen` |  |  |  |
| 30 | `DEP.EXT.PAYOUT.PO.PROD` | `DepHExtTfrParam_PayoutPoProd` |  |  |  |
| 31 | `DEP.EXT.RESERVED.15` | `DepHExtTfrParam_Reserved15` |  |  |  |
| 32 | `DEP.EXT.RESERVED.14` | `DepHExtTfrParam_Reserved14` |  |  |  |
| 33 | `DEP.EXT.RESERVED.13` | `DepHExtTfrParam_Reserved13` |  |  |  |
| 34 | `DEP.EXT.RESERVED.12` | `DepHExtTfrParam_Reserved12` |  |  |  |
| 35 | `DEP.EXT.RESERVED.11` | `DepHExtTfrParam_Reserved11` |  |  |  |
| 36 | `DEP.EXT.DEF.AGENT.ID` | `DepHExtTfrParam_DefAgentId` |  |  |  |
| 37 | `DEP.EXT.DEF.AGENT.ARR.ID` | `DepHExtTfrParam_DefAgentArrId` |  |  |  |
| 38 | `DEP.EXT.DEF.REP.NUMBER` | `DepHExtTfrParam_DefRepNumber` |  |  |  |
| 39 | `DEP.EXT.TRACK.CHANGES` | `DepHExtTfrParam_TrackChanges` | TField |  | This field is used to indicate if the Changes made in DEP.H.EXT.TRF.PARAM to be tracked to existing arrangements or applicable only for new arrangements.YES - all existing arrangements will be changed with new valuesNO - Existing arrangements will not be tracked. |
| 40 | `DEP.EXT.OFS.VERSION` | `DepHExtTfrParam_OfsVersion` | TField |  | Checkfile: VERSIONThis field to be inputable only for SYSTEM record |
| 41 | `DEP.EXT.OFS.SOURCE` | `DepHExtTfrParam_OfsSource` | TField |  | Checkfile: OFS.SOURCEThis field to be inputable only for SYSTEM record |
| 42 | `DEP.EXT.SETTLEMENT.OVERRIDE.FLAG` | `DepHExtTfrParam_SettlementOverrideFlag` | TField |  | This field is used to decide to display the settlement instruction override or not Possible values are YES/NO Yes - If the value is set as YES, override will be displayed when an arrangement is created if there is no record for customer value in DEP.H.EXT.TFR.PARAM No - If the value is set as NO, override will not be displayed when an arrangement is created if there is no record for customer value in DEP.H.EXT.TFR.PARAM |
| 43 | `DEP.EXT.DEF.AGENT.ACTIVITY` | `DepHExtTfrParam_DefAgentActivity` |  |  |  |
| 44 | `DEP.EXT.RESERVED.19` | `DepHExtTfrParam_Reserved19` | TField |  |  |
| 45 | `DEP.EXT.RESERVED.18` | `DepHExtTfrParam_Reserved18` | TField |  |  |
| 46 | `DEP.EXT.RESERVED.17` | `DepHExtTfrParam_Reserved17` | TField |  |  |
| 47 | `DEP.EXT.RESERVED.16` | `DepHExtTfrParam_Reserved16` | TField |  |  |
| 48 | `DEP.EXT.RECORD.STATUS` | `DepHExtTfrParam_RecordStatus` | String |  |  |
| 49 | `DEP.EXT.CURR.NO` | `DepHExtTfrParam_CurrNo` | String |  |  |
| 50 | `DEP.EXT.INPUTTER` | `DepHExtTfrParam_Inputter` |  |  |  |
| 51 | `DEP.EXT.DATE.TIME` | `DepHExtTfrParam_DateTime` |  |  |  |
| 52 | `DEP.EXT.AUTHORISER` | `DepHExtTfrParam_Authoriser` | String |  |  |
| 53 | `DEP.EXT.CO.CODE` | `DepHExtTfrParam_CoCode` | String |  |  |
| 54 | `DEP.EXT.DEPT.CODE` | `DepHExtTfrParam_DeptCode` | String |  |  |
| 55 | `DEP.EXT.AUDITOR.CODE` | `DepHExtTfrParam_AuditorCode` | String |  |  |
| 56 | `DEP.EXT.AUDIT.DATE.TIME` | `DepHExtTfrParam_AuditDateTime` | String |  |  |
