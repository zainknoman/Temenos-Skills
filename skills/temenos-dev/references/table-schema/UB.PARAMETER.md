# UB.PARAMETER — Table Schema

> Source: `INSERTS/I_F.UB.PARAMETER` in `CAEBPS_EbillsInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UB.PARAM.EXTERNAL.ID` | `UbParameter_ExternalId` | TField |  | This field is used to indicates the External IDeg. 99300 |
| 2 | `UB.PARAM.PAYEE.LIST.NO` | `UbParameter_PayeeListNo` | TField |  | This field is used to indicate the Payee List Number.Validation - allowed up to 9 digits.Eg. 20 |
| 3 | `UB.PARAM.UBR.OFS.SRC` | `UbParameter_UbrOfsSrc` | TField |  | This field indicates the OFS Source ID for Ebills switch process.Validation - record from OFS.SOURCEeg. EBILL.SRC.1 |
| 4 | `UB.PARAM.UBR.FT.TXN.TYPE` | `UbParameter_UbrFtTxnType` |  |  |  |
| 5 | `UB.PARAM.CUCBC.TIME` | `UbParameter_CucbcTime` | TField |  | Field is used to store the time at which the eBill switch will be on.Allowed up to 6 digits.Eg. 235510first 2 digits for hours, next 2 for minutes and last 2 digit for seconds. |
| 6 | `UB.PARAM.IN.DIR` | `UbParameter_InDir` | TField |  | Field is used to store valid directory for IN message to Ebill Switch.Eg. ./data/UD/TEST.IN |
| 7 | `UB.PARAM.CHANNEL` | `UbParameter_Channel` |  |  |  |
| 8 | `UB.PARAM.THRESHOLD.AMT` | `UbParameter_ThresholdAmt` |  |  |  |
| 9 | `UB.PARAM.EBILL.IP.ADDRESS` | `UbParameter_EbillIpAddress` | TField |  | Field to store the IP address of central1 server.Used to establish a real time connection with central1.eg. 10.92.5.175 |
| 10 | `UB.PARAM.EBILL.PORT.NO` | `UbParameter_EbillPortNo` | TField |  | Field to store the Port no of the central1 server.Used to establish a real time connection with central1eg. 800 |
| 11 | `UB.PARAM.OUT.DIR` | `UbParameter_OutDir` | TField |  | Field is used to store valid directory for OUT message to Ebill Switch.Eg. ./data/UD/TEST.OUT |
| 12 | `UB.PARAM.ALT.ACCT.TYPE` | `UbParameter_AltAcctType` | TField |  | Not in use |
| 13 | `UB.PARAM.LOCAL.REF` | `UbParameter_LocalRef` |  |  |  |
| 14 | `UB.PARAM.ALLOWED.INTF` | `UbParameter_AllowedIntf` |  |  |  |
| 15 | `UB.PARAM.CUCBC.OR.T24` | `UbParameter_CucbcOrT24` |  |  |  |
| 16 | `UB.PARAM.EBILL.SWITCH.STATUS` | `UbParameter_EbillSwitchStatus` | TField |  | Field is used to store eBIll status.The status of the Ebill status is defined here.Allowed inputs : TEST/PRODUCTION |
| 17 | `UB.PARAM.BRANCH.NUMBER` | `UbParameter_BranchNumber` | TField |  | This purpose of the field is to send the 2 digit member branch code as part of the each ebill ARU request initiated in T24.Allowed value is 2 numeric right justified zero filled.E.g. 01, 02 |
| 18 | `UB.PARAM.NO.CHARGE.REVERSE` | `UbParameter_NoChargeReverse` | TField |  | This field it used to inidicate whether the charges associated to bill payment needs to be reversed.Applicable during the reversal of Bill payment.Allowed inputs : YES / NOYES - Charges associated to bill payment will be reversed when a UB payment is reversed.NO - Charges associated to bill payment will not be reversed when a UB payment is reversed. |
| 19 | `UB.PARAM.IS.PROV.BC` | `UbParameter_IsProvBc` | TField | Yes | Mandatory field.Field is used to indicate Whether FI is from BC Province or not.Allowed inputs : YES/NOYES - FI from BC provinceNO - FI not from BC provinceValidation:if this field is set to NO, fields DELIMITER, BC.SORT.CODE and FILLER are mandatory for sending the request to ebill switch provider.if this field is set to YES - fields DELIMITER, BC.SORT.CODE and FILLER are noinput fields. |
| 20 | `UB.PARAM.DELIMITER` | `UbParameter_Delimiter` | TField | Yes | The fields which holds the delimiter that is used to report NON BC related fields, while sending the request to the ebill switch provider.applicable for FI from Non BC province.Holds the Delimiter VALUE.Currently set to \|~.Validation :Mandatory if the IS.PROV.BC field is set as NO |
| 21 | `UB.PARAM.BC.SORT.CODE` | `UbParameter_BcSortCode` | TField | Yes | Field is used to store the Bc sort code of the FI which is consist of Province code and Transit number of the Bank.Used to report NON BC related fields, while sending the request to the ebill switch provider.Province + Transit Number = BC.SORT.CODEAllowed up to 11 characters - NumericValidation :Mandatory if the IS.PROV.BC field is set as NORecords from BC.SORT.CODE table.eg.000100011 |
| 22 | `UB.PARAM.FILLER` | `UbParameter_Filler` | TField | Yes | Field is used to store the Filler ID which is used to report NON BC related fields, while sending the request to the ebill switch provider.Currently set to '00'Validation :Mandatory if the IS.PROV.BC field is set as NOallowed up to Alpha numeric - 2 characters |
| 23 | `UB.PARAM.PYMT.IND` | `UbParameter_PymtInd` | TField |  | This field is used to define whether the bill payment list to be stored in T24 or External.Allowed values are T24 and EXTERNAL.T24 - If it is set to T24 then T24 will store the details within T24 and during extracting the data, it will be done within T24 instead of sending request to Central1.External - If it is set to, EXTERNAL then T24 will send a request to Central1 each time when member tries to get Bill Payment List. |
| 24 | `UB.PARAM.REQ.QUEUE` | `UbParameter_ReqQueue` | TField |  | This field is a free text field used to define the request queue details for processing bill payment.Allowed value is t24EbillQueue |
| 25 | `UB.PARAM.RESP.QUEUE` | `UbParameter_RespQueue` | TField |  | This field is a free text field used to define the response queue details for processing bill payment.Allowed value is t24EbillReplyQueue |
| 26 | `UB.PARAM.CONN.FACTORY` | `UbParameter_ConnFactory` | TField |  | Field to store the connection factory with the swich. Eg: ConnectionFactory |
| 27 | `UB.PARAM.TIME.OUT` | `UbParameter_TimeOut` | TField |  | Field to store the number of seconds to be considered for processing the Bill payments transactions., after which transctions will be failed. |
| 28 | `UB.PARAM.MEM.VENDOR.IND` | `UbParameter_MemVendorInd` | TField |  | This field is used to define whether the member vendor details are to be auto defaulted or not in multi bill payment screen.Allowed values are Yes, No and Numeric Value.Yes - System will auto default all vendor details in multiple bill payment screen with no restriction on number of Vendors.No - System will not auto default all vendor details in Multiple Bill Payment screen.Numeric Value - System will auto default all vendor details in multiple bill payment screen with restricted number of Vendors defined here. If vendor is more than defined number, then system will not auto default.Validation:MEM.VEN.AUTO.DEF can be defined only if MEM.VENDOR.IND is set to T24 or not. |
| 29 | `UB.PARAM.MEM.VEN.AUTO.DEF` | `UbParameter_MemVenAutoDef` | TField |  | This field is used to define whether the member vendor details are to be auto defaulted or not in multi bill payment screen.Allowed values are Yes, No and Numeric Value.Yes - System will auto default all vendor details in multiple bill payment screen with no restriction on number of Vendors.No - System will not auto default all vendor details in Multiple Bill Payment screen.Numeric Value - System will auto default all vendor details in multiple bill payment screen with restricted number of Vendors defined here. If vendor is more than defined number, then system will not auto default.Validation:MEM.VEN.AUTO.DEF can be defined only if MEM.VENDOR.IND is set to T24 or not. |
| 30 | `UB.PARAM.MUTLI.TRANS.UB.VERSION` | `UbParameter_MutliTransUbVersion` | TField |  | Possible Value VersionThis version will be used to post the UB.PAYMENT from the BILL.PAYMENT application |
| 31 | `UB.PARAM.BATCH.REQ.QUEUE` | `UbParameter_BatchReqQueue` | TField | Yes | BATCH.REQ.QUEUE This field is a free text field used to define the request queue details for processing Multiple/Recurring bill payments. It is a Non-Mandatory field and FI can define this field if the volume of multiple bill payments are highIf this field is configured, then multiple bill payments will be processed through jboss request queue detailsIf this field is not configured(NULL), multiple bill payments will be processed via OFS message queueExample: EBILLBATCHREQ |
| 32 | `UB.PARAM.RECUR.PAY.TODAY` | `UbParameter_RecurPayToday` | TField |  | This field it used to indicate whether the recurring bill payment can be posted with today's date.Allowed inputs: YES / NOYES - recurring bill payment can be created for today's date.NO/None - System does not allow to create the recurring bill payment for today's date. |
| 33 | `UB.PARAM.BATCH.RES.QUEUE` | `UbParameter_BatchResQueue` | TField | Yes | This field is a free text field used to define the request queue details for processing Multiple/Recurring bill payments. It is a Non-Mandatory field and FI can define this field if the volume of multiple bill payments are highIf this field is configured, then multiple bill payments will be processed through jboss response queue detailsIf this field is not configured(NULL), then multiple bill payments will be processed via OFS message queueExample: EBILLBATCHRESP |
| 34 | `UB.PARAM.BATCH.CONN.FACTORY` | `UbParameter_BatchConnFactory` | TField |  | This field is a free text field used to define the Connection factory details for processing Multiple/Recurring Bill payments.FI Can define this field whenever the Remote JMS queue is used. |
| 35 | `UB.PARAM.RESERVERD.2` | `UbParameter_Reserverd2` | TField |  |  |
| 36 | `UB.PARAM.RESERVERD.3` | `UbParameter_Reserverd3` | TField |  |  |
| 37 | `UB.PARAM.RESERVERD.4` | `UbParameter_Reserverd4` | TField |  |  |
| 38 | `UB.PARAM.RESERVERD.5` | `UbParameter_Reserverd5` | TField |  |  |
| 39 | `UB.PARAM.RESERVERD.6` | `UbParameter_Reserverd6` | TField |  |  |
| 40 | `UB.PARAM.RESERVERD.7` | `UbParameter_Reserverd7` | TField |  |  |
| 41 | `UB.PARAM.RESERVERD.8` | `UbParameter_Reserverd8` | TField |  |  |
| 42 | `UB.PARAM.RESERVERD.9` | `UbParameter_Reserverd9` | TField |  |  |
| 43 | `UB.PARAM.RESERVERD.10` | `UbParameter_Reserverd10` | TField |  |  |
| 44 | `UB.PARAM.OVERRIDE` | `UbParameter_Override` |  |  |  |
| 45 | `UB.PARAM.RECORD.STATUS` | `UbParameter_RecordStatus` | String |  |  |
| 46 | `UB.PARAM.CURR.NO` | `UbParameter_CurrNo` | String |  |  |
| 47 | `UB.PARAM.INPUTTER` | `UbParameter_Inputter` |  |  |  |
| 48 | `UB.PARAM.DATE.TIME` | `UbParameter_DateTime` |  |  |  |
| 49 | `UB.PARAM.AUTHORISER` | `UbParameter_Authoriser` | String |  |  |
| 50 | `UB.PARAM.CO.CODE` | `UbParameter_CoCode` | String |  |  |
| 51 | `UB.PARAM.DEPT.CODE` | `UbParameter_DeptCode` | String |  |  |
| 52 | `UB.PARAM.AUDITOR.CODE` | `UbParameter_AuditorCode` | String |  |  |
| 53 | `UB.PARAM.AUDIT.DATE.TIME` | `UbParameter_AuditDateTime` | String |  |  |
