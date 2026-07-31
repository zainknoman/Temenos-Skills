# CAPL.H.FHM.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CAPL.H.FHM.PARAMETER` in `CABASE_ATMFoundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FHM.PARAM.REQ.MAPPING.ID` | `CaplHFhmParameter_ReqMappingId` | TField |  | This field used to define the INTRF.MAPPING ID to form the Request FHM message.Validation: It should be valid FHM messageEg: ISO0300001000 |
| 2 | `FHM.PARAM.WAIT.TIME.IN.SECS` | `CaplHFhmParameter_WaitTimeInSecs` | TField |  | This field used to define the response time out for FHM in seconds. If FHM not responded with in this time then T24 system will resend the request based on REPEAT.ITERATION field value.Validation: The value in this field is in seconds.Eg: 10 |
| 3 | `FHM.PARAM.REPEAT.ITERATION` | `CaplHFhmParameter_RepeatIteration` | TField |  | This field used to define the number of Retry has to be made in case the FHM not responded within the define time in WAIT.TIME.IN.SECSEg: 3 |
| 4 | `FHM.PARAM.REPEAT.MESSAGE` | `CaplHFhmParameter_RepeatMessage` | TField |  | This field used to define the INTRF.MAPPING ID to form the repeat request FHM message.Validation: It should be valid FHM messageEg: ISO0300001000 |
| 5 | `FHM.PARAM.HOST.IP` | `CaplHFhmParameter_HostIp` | TField |  | This field used to define the IP address to send the FHM request message.Eg: 10.155.22.11 |
| 6 | `FHM.PARAM.PORT` | `CaplHFhmParameter_Port` | TField |  | This field used to define the port number corresponding to the IP address to send the FHM request message.Eg: 2034 |
| 7 | `FHM.PARAM.TIMEOUT` | `CaplHFhmParameter_Timeout` | TField |  | For future use |
| 8 | `FHM.PARAM.DIRECTION` | `CaplHFhmParameter_Direction` | TField |  | For future use |
| 9 | `FHM.PARAM.IN.QUEUE.DIR` | `CaplHFhmParameter_InQueueDir` | TField |  | This field used to hold the directory path where the FHM request will be placed. It should be a valid directory path.Eg: .\FHM.DATA\FHM.REQ1 |
| 10 | `FHM.PARAM.OUT.QUEUE.DIR` | `CaplHFhmParameter_OutQueueDir` | TField |  | This field used to hold the directory path where the FHM response will be placed. It should be a valid directory path.Eg: .\FHM.DATA\FHM.RES1 |
| 11 | `FHM.PARAM.ERR.QUEUE.DIR` | `CaplHFhmParameter_ErrQueueDir` | TField |  | This field used to hold the directory path where the FHM errors will be placed. It should be a valid directory path.Eg: .\FHM.DATA\FHM.ERR1 |
| 12 | `FHM.PARAM.PIN.EXP.TIME` | `CaplHFhmParameter_PinExpTime` | TField |  | This field used to define how long the pin change window in open from the time of triggering the pin change request.The possible values in this field can be&lt;H&gt;&lt;No of hours&gt;&lt;M&gt;&lt;No of minutes&gt;&lt;S&gt;&lt;No of Seconds&gt;Eg: H2 - 2 hoursM60 - 60 minutesS120 - 120 seconds |
| 13 | `FHM.PARAM.HEADER.TAG` | `CaplHFhmParameter_HeaderTag` | TField |  | This field used to define a static value which can use as a header tag for the FHM message.Eg: File |
| 14 | `FHM.PARAM.FILE.NAME.TAG` | `CaplHFhmParameter_FileNameTag` | TField |  | This field used to define a static value which can use as a filename tag for the FHM message.Eg: FileName |
| 15 | `FHM.PARAM.INNER.HDR.TAG` | `CaplHFhmParameter_InnerHdrTag` | TField |  |  |
| 16 | `FHM.PARAM.FILE.REC.TAG` | `CaplHFhmParameter_FileRecTag` | TField |  | This field used to define a static value which can use as a file record tag for the FHM message.Eg: FileRow |
| 17 | `FHM.PARAM.GIT.INT.ID` | `CaplHFhmParameter_GitIntId` | TField |  | This field used to hold a DFE.MAPPING record which will triggered to form the FHM message.Validation: It should be a valid DFE.MAPPING record.Eg: CARD.FHM.UPD |
| 18 | `FHM.PARAM.STATIC.VALUE` | `CaplHFhmParameter_StaticValue` |  |  |  |
| 19 | `FHM.PARAM.UPDATE.FLAG` | `CaplHFhmParameter_UpdateFlag` | TField |  | This field used to define whether the transaction for which the FHM request is sent to be committed based on FHM response or Not.The possible values are ERROR and UPDATEERROR - Transaction should not be committed.UPDATE - Transaction will be committed with update as failed if FHM failed. |
| 20 | `FHM.PARAM.NO.OF.ACCTS` | `CaplHFhmParameter_NoOfAccts` | TField |  | This field used to define a value to denote the maximum number of accounts from a CARD.ISSUE record can be send as a part of FHM. So that accounts alone will be accessed through ATM/POS channel. It is a numeric fieldEg: 10 |
| 21 | `FHM.PARAM.MSG.HEADER` | `CaplHFhmParameter_MsgHeader` | TField |  | This field used to define a INTRF.MAPPING is which will be used to form a header for the whole FHM message.Eg: ISO085000055 |
| 22 | `FHM.PARAM.LOG.DIR` | `CaplHFhmParameter_LogDir` | TField |  | This field used to define a directory path for logging purpose.It should be a valid directory path.Eg: ./bnk.interface/FHM/LOG.DIR |
| 23 | `FHM.PARAM.LOG.FILE.NAME` | `CaplHFhmParameter_LogFileName` | TField |  | This field used to define the log file name which will be written on the directory parameterised in the field LOG.FILE.NAMEIt is a free text field.Eg: logfhm.txt |
| 24 | `FHM.PARAM.INTRF.MSG.ID` | `CaplHFhmParameter_IntrfMsgId` | TField |  | This field used to hold the INTRF.MESSAGE id which is used to parse the FHM request and response based on the ISO standards.Eg: FHM-8583 |
| 25 | `FHM.PARAM.BKUP.QUEUE.DIR` | `CaplHFhmParameter_BkupQueueDir` | TField |  | This field used to hold the directory path to backup the FHM request messages. It should be a valid directory pathEg: ./bnk.interface/FHH.BKUP.REQ |
| 26 | `FHM.PARAM.ARCH.QUEUE.DIR` | `CaplHFhmParameter_ArchQueueDir` | TField |  | This field used to hold the directory path to archive the FHM request messages. It should be a valid directory pathEg: ./bnk.interface/FHH.BKUP.REQ |
| 27 | `FHM.PARAM.RESP.MAXWAITIME` | `CaplHFhmParameter_RespMaxwaitime` | TField |  | This field used to define the maximum Response wai time of the FHM Message.This will be in seconds.Eg: 10 |
| 28 | `FHM.PARAM.PIN.WIND.REQ` | `CaplHFhmParameter_PinWindReq` | TField |  | For future use |
| 29 | `FHM.PARAM.INSTITUTION.ID` | `CaplHFhmParameter_InstitutionId` | TField |  | This field used to define the institution id which is a static value to be send as a part of FHM request message.Eg: 675456 |
| 30 | `FHM.PARAM.BRANCH.ID` | `CaplHFhmParameter_BranchId` | TField |  | This field used to define the branch id which is a static value to be send as a part of FHM request message.Eg: 765898 |
| 31 | `FHM.PARAM.TRACE.BM` | `CaplHFhmParameter_TraceBm` | TField |  | This field used to define the trace bit map position of incoming FHM response.Eg: 4, 5 |
| 32 | `FHM.PARAM.EXC.CARD.STATUS` | `CaplHFhmParameter_ExcCardStatus` |  |  |  |
| 33 | `FHM.PARAM.VLD.CARD.STATUS` | `CaplHFhmParameter_VldCardStatus` |  |  |  |
| 34 | `FHM.PARAM.FHM.REQ.RETAIN` | `CaplHFhmParameter_FhmReqRetain` | TField |  | In the table CAPL.H.FHM.PARAMETER, we have introduced new field as FHM.REQ.RETAIN with options as YES/NO/NONEYES - Retained the files from deleting in the FHM.REQ folderNO/NONE - Existing Functionality of deleting the files from FHM.REQ folderNote : FHM will be stopped when full CAF running and that time interacting messages are not reaching FHM. To overcome that we should retain the messages in request queue so that post Full CAF messages get processed from queue. To retain the messages in queue new field introduced at parameter |
| 35 | `FHM.PARAM.RESERVED.2` | `CaplHFhmParameter_Reserved2` |  |  |  |
| 36 | `FHM.PARAM.RESERVED.1` | `CaplHFhmParameter_Reserved1` | TField |  |  |
| 37 | `FHM.PARAM.LOCAL.REF` | `CaplHFhmParameter_LocalRef` |  |  |  |
| 38 | `FHM.PARAM.OVERRIDE` | `CaplHFhmParameter_Override` |  |  |  |
| 39 | `FHM.PARAM.RECORD.STATUS` | `CaplHFhmParameter_RecordStatus` | String |  |  |
| 40 | `FHM.PARAM.CURR.NO` | `CaplHFhmParameter_CurrNo` | String |  |  |
| 41 | `FHM.PARAM.INPUTTER` | `CaplHFhmParameter_Inputter` |  |  |  |
| 42 | `FHM.PARAM.DATE.TIME` | `CaplHFhmParameter_DateTime` |  |  |  |
| 43 | `FHM.PARAM.AUTHORISER` | `CaplHFhmParameter_Authoriser` | String |  |  |
| 44 | `FHM.PARAM.CO.CODE` | `CaplHFhmParameter_CoCode` | String |  |  |
| 45 | `FHM.PARAM.DEPT.CODE` | `CaplHFhmParameter_DeptCode` | String |  |  |
| 46 | `FHM.PARAM.AUDITOR.CODE` | `CaplHFhmParameter_AuditorCode` | String |  |  |
| 47 | `FHM.PARAM.AUDIT.DATE.TIME` | `CaplHFhmParameter_AuditDateTime` | String |  |  |
