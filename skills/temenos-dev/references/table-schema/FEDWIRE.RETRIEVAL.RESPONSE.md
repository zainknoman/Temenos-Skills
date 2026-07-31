# FEDWIRE.RETRIEVAL.RESPONSE — Table Schema

> Source: `INSERTS/I_F.FEDWIRE.RETRIEVAL.RESPONSE` in `USRTGS_Fedwire.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FWRR.URC` | `FedwireRetrievalResponse_Urc` | TField |  | User Request Correlation (URC). This is the ID to FEDWIRE.PDF.MESSAGE used to request retrievals. |
| 2 | `FWRR.CYCLE.DATE` | `FedwireRetrievalResponse_CycleDate` | TField |  | Current cycle date for which messages are returned. Retrievals can be requested. The value to this field is mapped from FEDWIRE.PDF.MESSAGE - CYCLE.DATE field. |
| 3 | `FWRR.ENDPOINT.ID` | `FedwireRetrievalResponse_EndpointId` | TField |  | Identifier of the endpoint for which the information is requested. The response is always routed to the requesting endpoint. Mapped from FEDWIRE.PDF.MESSAGE - ENDPOINT.ID |
| 4 | `FWRR.SEQ.NO` | `FedwireRetrievalResponse_SeqNo` | TField |  | The sequence number of the details requested. |
| 5 | `FWRR.REQ.START.SEQ` | `FedwireRetrievalResponse_ReqStartSeq` | TField |  | The start sequence numbers for which details are required If TRAFFIC.TYPE is &quot; &quot; S &quot; &quot; then these are IMAD numbers IF TRAFFIC.TYPE IS &quot; &quot; M &quot; &quot; then these are OMAD numbers Mapped from FEDWIRE.PDF.MESSAGE - START.SEQ |
| 6 | `FWRR.REQ.STOP.SEQ` | `FedwireRetrievalResponse_ReqStopSeq` | TField |  | The end sequence numbers up to which details are required If TRAFFIC.TYPE is &quot; &quot; S &quot; &quot; then these are IMAD numbers IF TRAFFIC.TYPE IS &quot; &quot; M &quot; &quot; then these are OMAD numbers Mapped from FEDWIRE.PDF.MESSAGE - STOP.SEQ |
| 7 | `FWRR.RESPONSE.FLAG` | `FedwireRetrievalResponse_ResponseFlag` | TField |  | Flag to indicate whether response is received. Possible values: YES NO |
| 8 | `FWRR.RESPONSE.DESC` | `FedwireRetrievalResponse_ResponseDesc` | TField |  | Message Status Indicator from incoming tag {1100} |
| 9 | `FWRR.TRACKER.ID` | `FedwireRetrievalResponse_TrackerId` | TField |  | FEDWIRE.MESSAGE.TRACKER ID of the Original IMAD. |
| 10 | `FWRR.RESPONSE.MSG` | `FedwireRetrievalResponse_ResponseMsg` | TField |  | LN-DATA response message received in retrieval response. |
| 11 | `FWRR.PROCESSED.DATE` | `FedwireRetrievalResponse_ProcessedDate` | TField |  | T24 date when the retrieval response was received. |
| 12 | `FWRR.RECV.DATE.TIME` | `FedwireRetrievalResponse_RecvDateTime` |  |  |  |
| 13 | `FWRR.RESERVED.13` | `FedwireRetrievalResponse_Reserved13` | TField |  |  |
| 14 | `FWRR.RESERVED.12` | `FedwireRetrievalResponse_Reserved12` | TField |  |  |
| 15 | `FWRR.RESERVED.11` | `FedwireRetrievalResponse_Reserved11` | TField |  |  |
| 16 | `FWRR.RESERVED.10` | `FedwireRetrievalResponse_Reserved10` | TField |  |  |
| 17 | `FWRR.RESERVED.9` | `FedwireRetrievalResponse_Reserved9` | TField |  |  |
| 18 | `FWRR.RESERVED.8` | `FedwireRetrievalResponse_Reserved8` | TField |  |  |
| 19 | `FWRR.RESERVED.7` | `FedwireRetrievalResponse_Reserved7` | TField |  |  |
| 20 | `FWRR.RESERVED.6` | `FedwireRetrievalResponse_Reserved6` | TField |  |  |
| 21 | `FWRR.RESERVED.5` | `FedwireRetrievalResponse_Reserved5` | TField |  |  |
| 22 | `FWRR.RESERVED.4` | `FedwireRetrievalResponse_Reserved4` | TField |  |  |
| 23 | `FWRR.RESERVED.3` | `FedwireRetrievalResponse_Reserved3` | TField |  |  |
| 24 | `FWRR.RESERVED.2` | `FedwireRetrievalResponse_Reserved2` | TField |  |  |
| 25 | `FWRR.RESERVED.1` | `FedwireRetrievalResponse_Reserved1` | TField |  |  |
