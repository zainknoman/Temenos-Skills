# CAPL.H.CHANNEL.DETAILS — Table Schema

> Source: `INSERTS/I_F.CAPL.H.CHANNEL.DETAILS` in `CABASE_ATMFoundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.CHANNEL.KEY.EXCH.KEY` | `CaplHChannelDetails_KeyExchKey` | TField |  | Valid KEK for the HSM device to be specified here. This key will be used during the Key Exchange process between Switch and T24.Validation: It is a free text field.Eg: 7B6042D7245B242E03D602ACFDF |
| 2 | `CAPL.CHANNEL.KEY.STATIC.VALUE` | `CaplHChannelDetails_KeyStaticValue` | TField |  | For future use |
| 3 | `CAPL.CHANNEL.VMAC.STATIC.VALUE` | `CaplHChannelDetails_VmacStaticValue` | TField |  | For future use |
| 4 | `CAPL.CHANNEL.GMAC.STATIC.VALUE` | `CaplHChannelDetails_GmacStaticValue` | TField |  | For future use |
| 5 | `CAPL.CHANNEL.DESCRIPTION` | `CaplHChannelDetails_Description` | TField |  | This field used to define description about this record.Validation: It is a free text field.Eg: Channel details record |
| 6 | `CAPL.CHANNEL.REQUEST.LOG.DIR` | `CaplHChannelDetails_RequestLogDir` | TField |  | This field used to define a directory where the requests to encryption device are logged.Validation: It is a free text field.Eg: HSMREQ |
| 7 | `CAPL.CHANNEL.RESPONSE.LOG.DIR` | `CaplHChannelDetails_ResponseLogDir` | TField |  | This field used to define a directory where the responses from encryption device are logged.Validation: It is a free text field.Eg: HSMRES |
| 8 | `CAPL.CHANNEL.INDEX.NUMBER` | `CaplHChannelDetails_IndexNumber` |  |  |  |
| 9 | `CAPL.CHANNEL.ERROR.CODE` | `CaplHChannelDetails_ErrorCode` |  |  |  |
| 10 | `CAPL.CHANNEL.ERR.THRESHOLD` | `CaplHChannelDetails_ErrThreshold` |  |  |  |
| 11 | `CAPL.CHANNEL.LOC.REF` | `CaplHChannelDetails_LocRef` |  |  |  |
| 12 | `CAPL.CHANNEL.MAX.WORKING.KEY` | `CaplHChannelDetails_MaxWorkingKey` | TField |  | This field used to define maximum working keys maintained in T24.Eg: 50 |
| 13 | `CAPL.CHANNEL.MAC.ON` | `CaplHChannelDetails_MacOn` | TField |  | This field used to define whether the VMAC and GMAC validation to be done or not.It is a YES or NO field.YES - VMAC and GMAC request will be send to HSM device.NO - VMAC and GMAC request will not be initiated from T24. The NO value will be set only at the time simulation testing. |
| 14 | `CAPL.CHANNEL.REQ.QUEUE` | `CaplHChannelDetails_ReqQueue` | TField |  | JMS Request Queue defined in Jboss where the request from T24 is pushed |
| 15 | `CAPL.CHANNEL.RESP.QUEUE` | `CaplHChannelDetails_RespQueue` | TField |  | JMS Response Queue defined in Jboss where the response from Central1 is placed |
| 16 | `CAPL.CHANNEL.BNK.CCY.CONVERSION` | `CaplHChannelDetails_BnkCcyConversion` | TField |  | This field used to define whether the bank going to define there own exchange rate for foreign currency transactions or going to use the amount from ISO request.It is a YES or NO field.YES - Bank going to use their own exchange rateNO or &lt;NULL&gt; - The amount coming in the ISO request will the transaction amount for foreign currency transaction. |
| 17 | `CAPL.CHANNEL.OFS.USER` | `CaplHChannelDetails_OfsUser` | TField |  | This field used to define valid T24 user SIGN.ON.NAME which going to be used for posting transactions.Eg: ATM.USER |
| 18 | `CAPL.CHANNEL.OFS.PASSWORD` | `CaplHChannelDetails_OfsPassword` | TField |  | This is absolute now |
| 19 | `CAPL.CHANNEL.HSM.IP` | `CaplHChannelDetails_HsmIp` | TField |  | This field used to define Ip address of the HSM device.Eg: 10.156.22.11 |
| 20 | `CAPL.CHANNEL.HSM.PORT` | `CaplHChannelDetails_HsmPort` | TField |  | This field used to define port no corrresponding to the IP address mention in HSM.IP field. This port number will be used to send and receive the VMAC and GMAC messages to HSM device.Eg: 9080 |
| 21 | `CAPL.CHANNEL.CONN.FACTORY` | `CaplHChannelDetails_ConnFactory` | TField |  | If there are specific requirements around using different connection factory then the JNDI name for the Connection factory can be specified in this field. If this field is left blank then system will use default ConnectionFactory |
| 22 | `CAPL.CHANNEL.USE.QUEUE` | `CaplHChannelDetails_UseQueue` | TField |  | Yes/No field. 'YES' if CALLJEE functionality to be executed. 'NO' if CALLJ functionality to be executed |
| 23 | `CAPL.CHANNEL.PIN.MAC` | `CaplHChannelDetails_PinMac` | TField |  | This field is used to define whether 0620/0621 messages to be maced or not.Allowed values are: Yes/NoYes - If this field is set to yes, then VMAC and GMAC macing will be done for 0620/0621 message types.No - If this field is set to no, then VMAC and GMAC macing will not be done for 0620/0621 message types. |
| 24 | `CAPL.CHANNEL.FX.DETS.UPD` | `CaplHChannelDetails_FxDetsUpd` | TField |  | Yes/No field. 'YES' if PAYMENT.DETAILS field needs to be updated in the FT record. 'NO/NONE' if PAYMENT.DETAILS field not needs to be updated in the FT record. |
| 25 | `CAPL.CHANNEL.TIME.OUT` | `CaplHChannelDetails_TimeOut` | TField |  | The purpose of this field is used to define the time for theVMAC/GMAC request. If the response is not received with thetime defined in this field from the HSM then the response will beconsidered as time out.Allowed values are 35 alphanumeric characters.Ex. 10, 100 |
| 26 | `CAPL.CHANNEL.RESERVED.4` | `CaplHChannelDetails_Reserved4` | TField |  |  |
| 27 | `CAPL.CHANNEL.RESERVED.5` | `CaplHChannelDetails_Reserved5` | TField |  |  |
| 28 | `CAPL.CHANNEL.OVERRIDE` | `CaplHChannelDetails_Override` |  |  |  |
| 29 | `CAPL.CHANNEL.RECORD.STATUS` | `CaplHChannelDetails_RecordStatus` | String |  |  |
| 30 | `CAPL.CHANNEL.CURR.NO` | `CaplHChannelDetails_CurrNo` | String |  |  |
| 31 | `CAPL.CHANNEL.INPUTTER` | `CaplHChannelDetails_Inputter` |  |  |  |
| 32 | `CAPL.CHANNEL.DATE.TIME` | `CaplHChannelDetails_DateTime` |  |  |  |
| 33 | `CAPL.CHANNEL.AUTHORISER` | `CaplHChannelDetails_Authoriser` | String |  |  |
| 34 | `CAPL.CHANNEL.CO.CODE` | `CaplHChannelDetails_CoCode` | String |  |  |
| 35 | `CAPL.CHANNEL.DEPT.CODE` | `CaplHChannelDetails_DeptCode` | String |  |  |
| 36 | `CAPL.CHANNEL.AUDITOR.CODE` | `CaplHChannelDetails_AuditorCode` | String |  |  |
| 37 | `CAPL.CHANNEL.AUDIT.DATE.TIME` | `CaplHChannelDetails_AuditDateTime` | String |  |  |
