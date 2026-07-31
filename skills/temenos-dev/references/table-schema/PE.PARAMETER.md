# PE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PE.PARAMETER` in `SC_ScPeFunds.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PE.PARAM.PE.TRANSFER.IN.CODE` | `PeParameter_PeTransferInCode` | TField | Yes | This field holds the transaction Code used for Free of Payment (FOP) Security transfer (Transfer In) transaction Validation Rules: Input should be a valid record in SC.TRANS.NAME, and this should be defined as a valid Credit code in SC.TRANS.TYPE Mandatory input |
| 2 | `SC.PE.PARAM.PE.TRANSFER.OUT.CODE` | `PeParameter_PeTransferOutCode` | TField | Yes | This field holds the transaction Code used for Free of Payment (FOP) Security transfer (Transfer Out)transaction Validation Rules: Input should be a valid record in SC.TRANS.NAME, and this should be defined as a valid Debit code in SC.TRANS.TYPE Mandatory input |
| 3 | `SC.PE.PARAM.PE.BUY.TRADE.CODE` | `PeParameter_PeBuyTradeCode` | TField | Yes | This field holds the transaction Code used for Security Purchase transaction created automatically during authorisation of PE.CUSTOMER.TXN for a particular event Validation Rules: Input should be a valid record in SC.TRANS.NAME, and this should be defined as a valid credit code in SC.TRANS.TYPE Mandatory input |
| 4 | `SC.PE.PARAM.PE.SELL.TRADE.CODE` | `PeParameter_PeSellTradeCode` | TField | Yes | This field holds the transaction Code used for Security Sell transaction created automatically during authorisation of PE.CUSTOMER.TXN for a particular event Validation Rules: Input should be a valid record in SC.TRANS.NAME, and this should be defined as a valid debit code in SC.TRANS.TYPE Mandatory input |
| 5 | `SC.PE.PARAM.CHARGE.TYPE` | `PeParameter_ChargeType` | TField | No | The commission code to be charged for a Private Equity Investments can be updated in this field Optional field |
| 6 | `SC.PE.PARAM.PL.CATEGORY` | `PeParameter_PlCategory` | TField | Conditional | This fields holds valid category code The commission charged for a PE investment would be posted to this PL Category Optional field, but mandatory when CHARGE.TYPE is inputted |
| 7 | `SC.PE.PARAM.DB.TRANS.CODE` | `PeParameter_DbTransCode` | TField | Conditional | This fields holds valid transaction code from TRANSACTION Input should be defined as a valid Debit code in TRANSACTION This transaction code will be used for generation of commission accounting entries for PE investment Optional field, but mandatory when CHARGE.TYPE is inputted |
| 8 | `SC.PE.PARAM.CR.TRANS.CODE` | `PeParameter_CrTransCode` | TField | Conditional | This fields holds valid transaction code from TRANSACTION Input should be defined as a valid Credit code in TRANSACTION This transaction code will be used for generation of commission accounting entries for PE investment Optional field, but mandatory when CHARGE.TYPE is inputted |
| 9 | `SC.PE.PARAM.TAX.TYPE` | `PeParameter_TaxType` | TField | Conditional | This field is used to define the tax code that will be applied on the commission. This would cater to scenarios where there is tax that applied on the commission (such as GST) Value in this field will be defaulted to TAX.KEY field of PE.CUSTOMER.TXN Optional field, but mandatory when CHARGE.TYPE is inputted |
| 10 | `SC.PE.PARAM.EVENT` | `PeParameter_Event` |  |  |  |
| 11 | `SC.PE.PARAM.EB.ACTIVITY` | `PeParameter_EbActivity` |  |  |  |
| 12 | `SC.PE.PARAM.DIARY.TYPE` | `PeParameter_DiaryType` | TField |  | This field holds the DIARY.TYPE used to process income distributions from the fund The DIARY.TYPE defined in this field should be defined with below values CASH - Y, SECURITY.UPDATE - No, NEW.SECURITIES - No, OPTIONS - No, REINVEST - No, RIGHTS - No, FREE.SECURITIES - No, RETAIN.ORIGINAL - Y This DIARY.TYPE can be used to process the Income Distributions from the PE fund |
| 13 | `SC.PE.PARAM.TRADE.OFS.VERSION` | `PeParameter_TradeOfsVersion` | TField | Yes | SEC.TRADE transaction for the PE events are created automatically using OFS Version when PE.CUSTOMER.TXN is authorised This field accepts a valid VERSION record for SEC.TRADE application and this field value is used for automatic creation of SEC.TRADE Mandatory input |
| 14 | `SC.PE.PARAM.TRADE.OFS.SOURCE` | `PeParameter_TradeOfsSource` | TField | Yes | SEC.TRADE transaction for the PE events are created automatically using OFS when PE.CUSTOMER.TXN is authorised This field accepts a valid OFS.SOURCE record and this field value is used for automatic creation of SEC.TRADE Mandatory input |
| 15 | `SC.PE.PARAM.TRANSFER.OFS.VERSION` | `PeParameter_TransferOfsVersion` | TField | Yes | SECURITY.TRANSFER(FOP)transaction for the PE events are created automatically using OFS when PE.CUSTOMER.TXN is authorised This field accepts a valid VERSION record for SECURITY.TRANSFER application and this field value is used for automatic creation of SECURITY.TRANSFER Mandatory input |
| 16 | `SC.PE.PARAM.TRANSFER.OFS.SOURCE` | `PeParameter_TransferOfsSource` | TField | Yes | SECURITY.TRANSFER(FOP) transaction for the PE events are created automatically using OFS when PE.CUSTOMER.TXN is authorised This field accepts a valid OFS.SOURCE record and this field value is used for automatic creation of SECURITY.TRNASFER Mandatory input |
| 17 | `SC.PE.PARAM.FT.TXN.TYPE` | `PeParameter_FtTxnType` | TField | Yes | This field accepts a valid record id from FT.TXN.TYPE.CONDITION table The management fees collected from the PE fund investors are posted to the issuer through an Funds transfer transaction. This field holds the FT.TXN.TYPE.CONDITION to be used for the FT Mandatory input |
| 18 | `SC.PE.PARAM.FT.OFS.VERSION` | `PeParameter_FtOfsVersion` | TField | Yes | FT transaction for the PE Management Fees will be created automatically using OFS when PE.MANAGEMENT.FEES is authorised This field accepts a valid VERSION record for FUNDS.TRANSFER application and this field value is used for automatic creation of FT Mandatory input |
| 19 | `SC.PE.PARAM.FT.OFS.SOURCE` | `PeParameter_FtOfsSource` | TField | Yes | FT transaction for the PE Management Fees will be created automatically using this OFS version when PE.MANAGEMENT.FEES is authorised This field accepts a valid OFS.SOURCE record and this field value is used for automatic creation of FUNDS.TRNASFER for PE Management fees Mandatory input |
| 20 | `SC.PE.PARAM.CUS.OFS.VERSION` | `PeParameter_CusOfsVersion` | TField | Yes | PE.CUSTOMER.TXN transaction will be amended automatically and will be put in INAU after the process of events defined in PE.PRODUCT.EVENTS using OFS This field accepts a valid VERSION record for PE.CUSTOMER.TXN application and this field value is used for automatic processing of PE.CUSTOMER.TXN Mandatory input |
| 21 | `SC.PE.PARAM.CUS.OFS.SOURCE` | `PeParameter_CusOfsSource` | TField | Yes | PE.CUSTOMER.TXN will be amended automatically and will be put in INAU after the process of events defined in PE.PRODUCT.EVENTS using OFS This field accepts a valid OFS.SOURCE record and this field value is used for automatic processing of PE.CUSTOMER.TXN through the new service PE.UPDATE.CUSTOMER.TXN Mandatory input |
| 22 | `SC.PE.PARAM.SM.OFS.VERSION` | `PeParameter_SmOfsVersion` | TField | Yes | SECURITY.MASTER records for SM2(Draw down), SM3(Capital Call), SM4(Maturity) will be created automatically through OFS when SM1(Initial Commitment) is authorised This field accepts a valid VERSION record for SECURITY.MASTER application and this will be used for automatic creation of SM records Mandatory input |
| 23 | `SC.PE.PARAM.SM.OFS.SOURCE` | `PeParameter_SmOfsSource` | TField | Yes | SECURITY.MASTER records for SM2(Draw down), SM3(Capital Call), SM4(Maturity) will be created automatically through OFS when SM1(Initial Commitment) is authorised This field accepts a valid OFS.SOURCE record and this field value is used for automatic creation of SM records Mandatory input |
| 24 | `SC.PE.PARAM.INT.DR.TR.CODE` | `PeParameter_IntDrTrCode` | TField |  |  |
| 25 | `SC.PE.PARAM.INT.CR.TR.CODE` | `PeParameter_IntCrTrCode` | TField | Yes | This fields holds valid transaction code from TRANSACTION Input should be defined as a valid Credit code in TRANSACTION This transaction will be used for generation of accounting entries for the interest amount credited to the customer during Capital return event Mandatory Input |
| 26 | `SC.PE.PARAM.FEES.OFS.VERSION` | `PeParameter_FeesOfsVersion` | TField | Yes | PE.MANAGEMENT.FEES records will be created automatically during COB on frequency date and these records will be automatically marked as COMPLETED during the service PE.UPDATE.MGMT.FEES This field accepts a valid VERSION record for PE.MANAGEMENT.FEES application and this field value is used for automatic processing of PE.MANAGEMENT.FEES records Mandatory input |
| 27 | `SC.PE.PARAM.FEES.OFS.SOURCE` | `PeParameter_FeesOfsSource` | TField | Yes | PE.MANAGEMENT.FEES records will be created automatically during COB on frequency date and these records will be automatically marked as COMPLETED during the service PE.UPDATE.MGMT.FEES This field accepts a valid OFS.SOURCE record this field value is used for automatic processing of PE.MANAGEMENT.FEES records Mandatory input |
| 28 | `SC.PE.PARAM.RESERVED9` | `PeParameter_Reserved9` |  |  |  |
| 29 | `SC.PE.PARAM.RESERVED10` | `PeParameter_Reserved10` |  |  |  |
| 30 | `SC.PE.PARAM.RESERVED11` | `PeParameter_Reserved11` |  |  |  |
| 31 | `SC.PE.PARAM.RESERVED12` | `PeParameter_Reserved12` |  |  |  |
| 32 | `SC.PE.PARAM.RESERVED13` | `PeParameter_Reserved13` |  |  |  |
| 33 | `SC.PE.PARAM.RESERVED14` | `PeParameter_Reserved14` |  |  |  |
| 34 | `SC.PE.PARAM.RESERVED15` | `PeParameter_Reserved15` |  |  |  |
| 35 | `SC.PE.PARAM.RESERVED16` | `PeParameter_Reserved16` |  |  |  |
| 36 | `SC.PE.PARAM.RESERVED17` | `PeParameter_Reserved17` |  |  |  |
| 37 | `SC.PE.PARAM.RESERVED18` | `PeParameter_Reserved18` |  |  |  |
| 38 | `SC.PE.PARAM.RESERVED19` | `PeParameter_Reserved19` |  |  |  |
| 39 | `SC.PE.PARAM.RESERVED20` | `PeParameter_Reserved20` |  |  |  |
| 40 | `SC.PE.PARAM.LOCAL.REF` | `PeParameter_LocalRef` |  |  |  |
| 41 | `SC.PE.PARAM.OVERRIDE` | `PeParameter_Override` |  |  |  |
| 42 | `SC.PE.PARAM.RECORD.STATUS` | `PeParameter_RecordStatus` | String |  |  |
| 43 | `SC.PE.PARAM.CURR.NO` | `PeParameter_CurrNo` | String |  |  |
| 44 | `SC.PE.PARAM.INPUTTER` | `PeParameter_Inputter` |  |  |  |
| 45 | `SC.PE.PARAM.DATE.TIME` | `PeParameter_DateTime` |  |  |  |
| 46 | `SC.PE.PARAM.AUTHORISER` | `PeParameter_Authoriser` | String |  |  |
| 47 | `SC.PE.PARAM.CO.CODE` | `PeParameter_CoCode` | String |  |  |
| 48 | `SC.PE.PARAM.DEPT.CODE` | `PeParameter_DeptCode` | String |  |  |
| 49 | `SC.PE.PARAM.AUDITOR.CODE` | `PeParameter_AuditorCode` | String |  |  |
| 50 | `SC.PE.PARAM.AUDIT.DATE.TIME` | `PeParameter_AuditDateTime` | String |  |  |
