# FEDWIRE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FEDWIRE.PARAMETER` in `USRTGS_Fedwire.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FWPAR.DESC` | `FedwireParameter_Desc` |  |  |  |
| 2 | `FWPAR.OFS.SOURCE` | `FedwireParameter_OfsSource` | TField | Yes | Valid OFS.SOURCE record for posting message into T24 tables. Mandatory input. |
| 3 | `FWPAR.SENDER.DI` | `FedwireParameter_SenderDi` |  |  |  |
| 4 | `FWPAR.FT.MID.ID` | `FedwireParameter_FtMidId` | TField | Yes | MID-ID used in FLASH Function Management Header (FMH) of all &quot; Outgoing from the DI Funds Transfer &quot; messages. Mandatory input. |
| 5 | `FWPAR.O.INTERFACE.DATA` | `FedwireParameter_OInterfaceData` | TField | Yes | For originating Fedwire Funds transfer message. This value is appended to the advice and reject notification message. For Outgoing from the DI messages: �XFT811 � - For FLASH senders. All new FedLine Direct customers must use this format. �ZFT811 � - Only appropriate for existing FRISC senders. �YFT811 � - For FedLine Advantage senders. Mandatory input. supply this value; rather, it is supplied by the Federal Reserve Banks. |
| 6 | `FWPAR.DELIVERY.MODE` | `FedwireParameter_DeliveryMode` | TField | Yes | Determines whether file based delivery on queue based service. Possible values: FILE - All originating Fedwire messages will be file-based (either BULK or Individual depending on the MSG.FREQUENCY) and stored in OUT.PATH location. JMS.QUEUE - All originating Fedwire messages will be individually posted to a JMS queue configured in O.QUEUE.DEFN. User can choose to deliver VALUE or NON-VALUE messages to separate queue by specifying O.MSG.TYPE. Mandatory input. |
| 7 | `FWPAR.O.MSG.TYPE` | `FedwireParameter_OMsgType` |  |  |  |
| 8 | `FWPAR.RESERVED.25` | `FedwireParameter_Reserved25` |  |  |  |
| 9 | `FWPAR.RESERVED.24` | `FedwireParameter_Reserved24` |  |  |  |
| 10 | `FWPAR.RESERVED.23` | `FedwireParameter_Reserved23` |  |  |  |
| 11 | `FWPAR.O.QUEUE.DEFN` | `FedwireParameter_OQueueDefn` |  |  |  |
| 12 | `FWPAR.RESERVED.22` | `FedwireParameter_Reserved22` |  |  |  |
| 13 | `FWPAR.RESERVED.21` | `FedwireParameter_Reserved21` |  |  |  |
| 14 | `FWPAR.MSG.FREQUENCY` | `FedwireParameter_MsgFrequency` | TField |  | Determines the message delivery frequency to FFS, i.e. DAILY, HOURLY or IMMEDIATE. Input allowed only when DELIVERY.MODE is FILE Possible values are : DAILY - All originating messages will be sequenced into one file which has TODAY date as part of sequential filename. HOURLY - All originating messages will be sequenced into one file each hour (HH) where TODAY and HH is part of sequential filename. IMMEDIATE - Each originating message is published in a unique file name. |
| 15 | `FWPAR.OUT.ID.PREFIX` | `FedwireParameter_OutIdPrefix` | TField | No | The string entered in this field will be prefixed in Outward filename where DELIVERY.MODE is FILE. Optional Input. |
| 16 | `FWPAR.OUT.ID.SUFFIX` | `FedwireParameter_OutIdSuffix` | TField | No | The string entered in this field will be suffix in Outward filename where DELIVERY.MODE is FILE. Optional Input. |
| 17 | `FWPAR.OUT.ID.API` | `FedwireParameter_OutIdApi` | TField | No | A user-defined API can be attached to this field to return a filename used to publish each originating message. Optional Input. Routine attached could be either: A jBC implementation by using an EB.API record with a source type of BASIC. For java implementations: An EB.API record id with a source type of HOOK which implements an interface defined in the EB.API record USRTGS.OUT.ID.API.HOOK This field supports the Fedwire.getOutwardFileName() method. The Fedwire Class is in the hook.countrymodelbank.Fedwire package which is in USRTGS_FedwireHook.jar shipped with T24. |
| 18 | `FWPAR.OUT.PATH` | `FedwireParameter_OutPath` | TField | Yes | Directory path used by fedwire outbound service to publish Fedwire messages. Mandatory when DELIVERY.MODE is FILE |
| 19 | `FWPAR.IN.PATH` | `FedwireParameter_InPath` | TField | Yes | FedLine Direct customer, messages posted by FFS must be placed in the directory. Mandatory input. |
| 20 | `FWPAR.IN.BACKUP.PATH` | `FedwireParameter_InBackupPath` | TField | Yes | Back up directory path referred by both inbound service to maintain a copy of the message received. Mandatory input. |
| 21 | `FWPAR.OUR.LTERM` | `FedwireParameter_OurLterm` | TField | Yes | Endpoint terminal identifier for the current company. Mandatory input. |
| 22 | `FWPAR.TEST.PROD` | `FedwireParameter_TestProd` | TField |  | Test or Production environment indicator. Used to populate TEST PRODUCTION CODE element in tag {1100} |
| 23 | `FWPAR.LOG.LEVEL` | `FedwireParameter_LogLevel` | TField | Yes | This fields determines whether to maintain the log by the inbound and outbound message processing service. Mandatory input. Possible values: FULL - Capture log information. NONE - No information is logged. |
| 24 | `FWPAR.LOCAL.REF` | `FedwireParameter_LocalRef` |  |  |  |
| 25 | `FWPAR.VERIFY.MANDATE` | `FedwireParameter_VerifyMandate` | TField | No | It is an optional field to Enable/Disable Drawdown request functionality. |
| 26 | `FWPAR.FF.ACCOUNT.NO` | `FedwireParameter_FfAccountNo` | TField |  | Default Fed funds account number. |
| 27 | `FWPAR.FF.NAME.ADDR` | `FedwireParameter_FfNameAddr` |  |  |  |
| 28 | `FWPAR.ACCOUNT.VALIDATION.API` | `FedwireParameter_AccountValidationApi` |  |  |  |
| 29 | `FWPAR.IMPLIED.CREDIT.DEFAULT` | `FedwireParameter_IMPLIED.CREDIT.DEFAULT` |  |  |  |
| 30 | `FWPAR.RESERVED.13` | `FedwireParameter_Reserved13` |  |  |  |
| 31 | `FWPAR.RESERVED.12` | `FedwireParameter_Reserved12` |  |  |  |
| 32 | `FWPAR.RESERVED.11` | `FedwireParameter_Reserved11` | TField |  |  |
| 33 | `FWPAR.RESERVED.10` | `FedwireParameter_Reserved10` | TField |  |  |
| 34 | `FWPAR.RESERVED.9` | `FedwireParameter_Reserved9` | TField |  |  |
| 35 | `FWPAR.RESERVED.8` | `FedwireParameter_Reserved8` | TField |  |  |
| 36 | `FWPAR.RESERVED.7` | `FedwireParameter_Reserved7` | TField |  |  |
| 37 | `FWPAR.RESERVED.6` | `FedwireParameter_Reserved6` | TField |  |  |
| 38 | `FWPAR.RESERVED.5` | `FedwireParameter_Reserved5` | TField |  |  |
| 39 | `FWPAR.RESERVED.4` | `FedwireParameter_Reserved4` | TField |  |  |
| 40 | `FWPAR.RESERVED.3` | `FedwireParameter_Reserved3` | TField |  |  |
| 41 | `FWPAR.RESERVED.2` | `FedwireParameter_Reserved2` | TField |  |  |
| 42 | `FWPAR.RESERVED.1` | `FedwireParameter_Reserved1` | TField |  |  |
| 43 | `FWPAR.OVERRIDE` | `FedwireParameter_Override` |  |  |  |
| 44 | `FWPAR.RECORD.STATUS` | `FedwireParameter_RecordStatus` | String |  |  |
| 45 | `FWPAR.CURR.NO` | `FedwireParameter_CurrNo` | String |  |  |
| 46 | `FWPAR.INPUTTER` | `FedwireParameter_Inputter` |  |  |  |
| 47 | `FWPAR.DATE.TIME` | `FedwireParameter_DateTime` |  |  |  |
| 48 | `FWPAR.AUTHORISER` | `FedwireParameter_Authoriser` | String |  |  |
| 49 | `FWPAR.CO.CODE` | `FedwireParameter_CoCode` | String |  |  |
| 50 | `FWPAR.DEPT.CODE` | `FedwireParameter_DeptCode` | String |  |  |
| 51 | `FWPAR.AUDITOR.CODE` | `FedwireParameter_AuditorCode` | String |  |  |
| 52 | `FWPAR.AUDIT.DATE.TIME` | `FedwireParameter_AuditDateTime` | String |  |  |
