# MDI.TXN.TYPE.MAPPING — Table Schema

> Source: `INSERTS/I_F.MDI.TXN.TYPE.MAPPING` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDI.TXN.TYP.TXN.DESC` | `MdiTxnTypeMapping_TxnDesc` | TField |  | This field used to specify brief Description of the record.Eg: ATM-Transfer Out |
| 2 | `MDI.TXN.TYP.MDI.TXN.CODE` | `MdiTxnTypeMapping_MdiTxnCode` | TField |  | This field used to define the MDI Transaction code for the equivalent T24 Transaction code.Eg: 998 |
| 3 | `MDI.TXN.TYP.MDI.DESC.1` | `MdiTxnTypeMapping_MdiDesc1` | TField |  | This should be kept blank, as first line of Narrative will be taken from T24 Statement record. |
| 4 | `MDI.TXN.TYP.CONV.FUNC.1` | `MdiTxnTypeMapping_ConvFunc1` | TField |  | Conversion function to be used for converting the data using the above field |
| 5 | `MDI.TXN.TYP.CONV.PARAM.1` | `MdiTxnTypeMapping_ConvParam1` | TField |  | Conversion value to be used for processing the Narrative |
| 6 | `MDI.TXN.TYP.MDI.DESC.2` | `MdiTxnTypeMapping_MdiDesc2` | TField |  | This is to indicate the second line of Transaction narrative to be shown in the Member direct Statement.If there are specific Transaction record fields to be displayed as part of Narrative then it should follow the below syntax.Linking one application field value - APPLICATION NAME&gt;FIELD.NAMELinking more than one application field value - APPLICATION NAME1&gt;FIELD.NAME1* APPLICATION NAME2&gt;FIELD.NAME2* APPLICATION NAME3&gt;FIELD.NAME3 |
| 7 | `MDI.TXN.TYP.CONV.FUNC.2` | `MdiTxnTypeMapping_ConvFunc2` | TField |  | Conversion function to be used for converting the data using the above field |
| 8 | `MDI.TXN.TYP.CONV.PARAM.2` | `MdiTxnTypeMapping_ConvParam2` | TField |  | Conversion value to be used for processing the Narrative |
| 9 | `MDI.TXN.TYP.MDI.DESC.3` | `MdiTxnTypeMapping_MdiDesc3` | TField |  | This is to indicate the third line of Transaction narrative to be shown in the Member direct Statement.If there are specific Transaction record fields to be displayed as part of Narrative then it should follow the below syntax.Linking one application field value - APPLICATION NAME&gt;FIELD.NAMELinking more than one application field value - APPLICATION NAME1&gt;FIELD.NAME1* APPLICATION NAME2&gt;FIELD.NAME2* APPLICATION NAME3&gt;FIELD.NAME3 |
| 10 | `MDI.TXN.TYP.CONV.FUNC.3` | `MdiTxnTypeMapping_ConvFunc3` | TField |  | Conversion function to be used for converting the data using the above field |
| 11 | `MDI.TXN.TYP.CONV.PARAM.3` | `MdiTxnTypeMapping_ConvParam3` | TField |  | Conversion value to be used for processing the Narrative |
| 12 | `MDI.TXN.TYP.MDI.ATTRI.CODE` | `MdiTxnTypeMapping_MdiAttriCode` |  |  |  |
| 13 | `MDI.TXN.TYP.LENGTH` | `MdiTxnTypeMapping_Length` |  |  |  |
| 14 | `MDI.TXN.TYP.DATA.TYPE` | `MdiTxnTypeMapping_DataType` |  |  |  |
| 15 | `MDI.TXN.TYP.T24.APP.FLD` | `MdiTxnTypeMapping_T24AppFld` |  |  |  |
| 16 | `MDI.TXN.TYP.CONV.FUNC` | `MdiTxnTypeMapping_ConvFunc` |  |  |  |
| 17 | `MDI.TXN.TYP.CONV.PARAM` | `MdiTxnTypeMapping_ConvParam` |  |  |  |
| 18 | `MDI.TXN.TYP.LOCAL.CORE` | `MdiTxnTypeMapping_LocalCore` | TField |  | Purpose of the field to indicate whether the transaction narrative description to be followed as per CAMB or core.Allowed inputs - Local/CoreLocal - CAMB functionality will be used for transaction narrative.Core - Core functionality will be used for transaction narrative. |
| 19 | `MDI.TXN.TYP.RESERVED.1` | `MdiTxnTypeMapping_Reserved1` | TField |  |  |
| 20 | `MDI.TXN.TYP.RECORD.STATUS` | `MdiTxnTypeMapping_RecordStatus` | String |  |  |
| 21 | `MDI.TXN.TYP.CURR.NO` | `MdiTxnTypeMapping_CurrNo` | String |  |  |
| 22 | `MDI.TXN.TYP.INPUTTER` | `MdiTxnTypeMapping_Inputter` |  |  |  |
| 23 | `MDI.TXN.TYP.DATE.TIME` | `MdiTxnTypeMapping_DateTime` |  |  |  |
| 24 | `MDI.TXN.TYP.AUTHORISER` | `MdiTxnTypeMapping_Authoriser` | String |  |  |
| 25 | `MDI.TXN.TYP.CO.CODE` | `MdiTxnTypeMapping_CoCode` | String |  |  |
| 26 | `MDI.TXN.TYP.DEPT.CODE` | `MdiTxnTypeMapping_DeptCode` | String |  |  |
| 27 | `MDI.TXN.TYP.AUDITOR.CODE` | `MdiTxnTypeMapping_AuditorCode` | String |  |  |
| 28 | `MDI.TXN.TYP.AUDIT.DATE.TIME` | `MdiTxnTypeMapping_AuditDateTime` | String |  |  |
