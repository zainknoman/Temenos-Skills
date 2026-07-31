# FEDWIRE.PDF.MESSAGE — Table Schema

> Source: `INSERTS/I_F.FEDWIRE.PDF.MESSAGE` in `USRTGS_Fedwire.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FWPM.MID.ID` | `FedwirePdfMessage_MidId` | TField | Yes | MID-ID associated with the request being origination. Possible values: FTIABAL � Account Balance Request FTI0041 � Endpoint Grand Total Request FTI0043 � Detailed Transfer Summary Request FTI0091 � Error Code Description Request FTI0051 � Retrieval Request Mandatory input. |
| 2 | `FWPM.INTERFACE.CD` | `FedwirePdfMessage_InterfaceCd` | TField |  | For FLASH senders, FedLine Direct customers must use X Defaulted to X. |
| 3 | `FWPM.INQUIRY.ABA` | `FedwirePdfMessage_InquiryAba` | TField | Yes | The 9 digit number of the master or subaccount for which totals are being requested. Input mandatory when MID.ID is FTIABAL |
| 4 | `FWPM.BALANCE.TYPE` | `FedwirePdfMessage_BalanceType` | TField | Yes | Identifies the type of balance (debits, credits and net position) requested. Possible values: S - Self Balance M - Master Balance Input mandatory when MID.ID is FTIABAL. |
| 5 | `FWPM.ENDPOINT.ID` | `FedwirePdfMessage_EndpointId` | TField | Yes | Identifier of the endpoint for which the information is requested. The response is always routed to the requesting endpoint. Input mandatory when MID.ID is FTI0051 (OR) FTI0043 |
| 6 | `FWPM.TRAFFIC.TYPE` | `FedwirePdfMessage_TrafficType` | TField | Yes | Messages sent/received from an endpoint. Possible values: S - Messages sent from the endpoint M - Messages received from the endpoint Input mandatory when MID.ID is FTI0051 (OR) FTI0043 |
| 7 | `FWPM.START.SEQ` | `FedwirePdfMessage_StartSeq` | TField | Yes | The start sequence numbers for which details are required If TRAFFIC.TYPE is &quot; &quot; S &quot; &quot; then these are IMAD numbers IF TRAFFIC.TYPE IS &quot; &quot; M &quot; &quot; then these are OMAD numbers Input mandatory when MID.ID is FTI0051 (OR) FTI0043 |
| 8 | `FWPM.STOP.SEQ` | `FedwirePdfMessage_StopSeq` | TField | Yes | The end sequence numbers up to which details are required If TRAFFIC.TYPE is &quot; &quot; S &quot; &quot; then these are IMAD numbers IF TRAFFIC.TYPE IS &quot; &quot; M &quot; &quot; then these are OMAD numbers The difference between START.SEQ and STOP.SEQ is limited up to 50 per request. If left bank, START.SEQ is defaulted. Input mandatory when MID.ID is FTI0051 (OR) FTI0043 |
| 9 | `FWPM.ERROR.CODE` | `FedwirePdfMessage_ErrorCode` | TField | Yes | The 4-digit error code for which description is being requested. Input mandatory when MID.ID is FTI0091 |
| 10 | `FWPM.CYCLE.DATE` | `FedwirePdfMessage_CycleDate` | TField | Yes | Current cycle date for which messages are returned. Retrievals can be requested. Defaulted to current date. Input mandatory when MID.ID is FTI0051 |
| 11 | `FWPM.RESPONSE.FLAG` | `FedwirePdfMessage_ResponseFlag` | TField |  | Flag to indicate whether response is received. Possible values: YES NO Noinput field. |
| 12 | `FWPM.PROCESSED.DATE` | `FedwirePdfMessage_ProcessedDate` | TField |  | T24 Date when the response was received. Noinput field. |
| 13 | `FWPM.FORMAT.ID` | `FedwirePdfMessage_FormatId` | TField |  | FORMAT-ID of the incoming message. Noinput field. |
| 14 | `FWPM.SOLICITED.MSG` | `FedwirePdfMessage_SolicitedMsg` | TField |  | Flag to indicate whether this record was a Solicited message or not. Possible values: YES NO Noinput field. |
| 15 | `FWPM.MSG.ID` | `FedwirePdfMessage_MsgId` |  |  |  |
| 16 | `FWPM.MSG.DETAILS` | `FedwirePdfMessage_MsgDetails` |  |  |  |
| 17 | `FWPM.RESERVED.25` | `FedwirePdfMessage_Reserved25` |  |  |  |
| 18 | `FWPM.RESERVED.23` | `FedwirePdfMessage_Reserved23` |  |  |  |
| 19 | `FWPM.RESERVED.22` | `FedwirePdfMessage_Reserved22` |  |  |  |
| 20 | `FWPM.RESERVED.21` | `FedwirePdfMessage_Reserved21` |  |  |  |
| 21 | `FWPM.RESERVED.20` | `FedwirePdfMessage_Reserved20` | TField |  |  |
| 22 | `FWPM.RESERVED.19` | `FedwirePdfMessage_Reserved19` | TField |  |  |
| 23 | `FWPM.RESERVED.18` | `FedwirePdfMessage_Reserved18` | TField |  |  |
| 24 | `FWPM.RESERVED.17` | `FedwirePdfMessage_Reserved17` | TField |  |  |
| 25 | `FWPM.RESERVED.16` | `FedwirePdfMessage_Reserved16` | TField |  |  |
| 26 | `FWPM.RESERVED.15` | `FedwirePdfMessage_Reserved15` | TField |  |  |
| 27 | `FWPM.RESERVED.14` | `FedwirePdfMessage_Reserved14` | TField |  |  |
| 28 | `FWPM.RESERVED.13` | `FedwirePdfMessage_Reserved13` | TField |  |  |
| 29 | `FWPM.RESERVED.12` | `FedwirePdfMessage_Reserved12` | TField |  |  |
| 30 | `FWPM.RESERVED.11` | `FedwirePdfMessage_Reserved11` | TField |  |  |
| 31 | `FWPM.RESERVED.10` | `FedwirePdfMessage_Reserved10` | TField |  |  |
| 32 | `FWPM.RESERVED.9` | `FedwirePdfMessage_Reserved9` | TField |  |  |
| 33 | `FWPM.RESERVED.8` | `FedwirePdfMessage_Reserved8` | TField |  |  |
| 34 | `FWPM.RESERVED.7` | `FedwirePdfMessage_Reserved7` | TField |  |  |
| 35 | `FWPM.RESERVED.6` | `FedwirePdfMessage_Reserved6` | TField |  |  |
| 36 | `FWPM.RESERVED.5` | `FedwirePdfMessage_Reserved5` | TField |  |  |
| 37 | `FWPM.RESERVED.4` | `FedwirePdfMessage_Reserved4` | TField |  |  |
| 38 | `FWPM.RESERVED.3` | `FedwirePdfMessage_Reserved3` | TField |  |  |
| 39 | `FWPM.RESERVED.2` | `FedwirePdfMessage_Reserved2` | TField |  |  |
| 40 | `FWPM.RESERVED.1` | `FedwirePdfMessage_Reserved1` | TField |  |  |
| 41 | `FWPM.OVERRIDE` | `FedwirePdfMessage_Override` |  |  |  |
| 42 | `FWPM.RECORD.STATUS` | `FedwirePdfMessage_RecordStatus` | String |  |  |
| 43 | `FWPM.CURR.NO` | `FedwirePdfMessage_CurrNo` | String |  |  |
| 44 | `FWPM.INPUTTER` | `FedwirePdfMessage_Inputter` |  |  |  |
| 45 | `FWPM.DATE.TIME` | `FedwirePdfMessage_DateTime` |  |  |  |
| 46 | `FWPM.AUTHORISER` | `FedwirePdfMessage_Authoriser` | String |  |  |
| 47 | `FWPM.CO.CODE` | `FedwirePdfMessage_CoCode` | String |  |  |
| 48 | `FWPM.DEPT.CODE` | `FedwirePdfMessage_DeptCode` | String |  |  |
| 49 | `FWPM.AUDITOR.CODE` | `FedwirePdfMessage_AuditorCode` | String |  |  |
| 50 | `FWPM.AUDIT.DATE.TIME` | `FedwirePdfMessage_AuditDateTime` | String |  |  |
