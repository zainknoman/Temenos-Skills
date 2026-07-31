# SC.SRD.HLD.REQUEST — Table Schema

> Source: `INSERTS/I_F.SC.SRD.HLD.REQUEST` in `SC_ScSrdEventCapture.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SRQ.SENDER.BIC` | `ScSrdHldRequest_SenderBic` | TField |  | Field holds BIC Address of Sender from message |
| 2 | `SC.SRQ.SECURITY.NO` | `ScSrdHldRequest_SecurityNo` |  |  |  |
| 3 | `SC.SRQ.DEPOSITORY` | `ScSrdHldRequest_Depository` | TField |  | Field holds the Depository number where the shares are held. Validation Rules Must be a Depository Customer type or ALL |
| 4 | `SC.SRQ.REQ.TYPE` | `ScSrdHldRequest_ReqType` | TField |  | Field is to capture the type of disclosure request. Validation Rules Possible value are NEWM or REPL |
| 5 | `SC.SRQ.SRD.REQ.ID` | `ScSrdHldRequest_SrdReqId` | TField |  | Field denotes the unique id assigned to a shareholder identification disclosure request process by the issuer orthird party nominated by the issuer. |
| 6 | `SC.SRQ.PREV.REQ.ID` | `ScSrdHldRequest_PrevReqId` | TField |  | Field denotes the id of previously sent shareholder identification disclosure request message |
| 7 | `SC.SRQ.FWRD.REQ` | `ScSrdHldRequest_FwrdReq` | TField |  | This field indicates whether the request is to be forwarded to and responded by the other intermediaries down thechain of intermediaries or not. This field is for information purpose |
| 8 | `SC.SRQ.RSPN.THRGH.INTERM` | `ScSrdHldRequest_RspnThrghInterm` | TField |  | Field indicates whether the shareholder identification disclosure response is to be sentback down the chain ofintermediaries or directly to the identified response recipient. |
| 9 | `SC.SRQ.SRD.INDICATOR` | `ScSrdHldRequest_SrdIndicator` | TField |  | Field indicates whether the request was initiated by the first intermediary in the custody chain inaccordancewith SRD II. |
| 10 | `SC.SRQ.RECORD.DATE` | `ScSrdHldRequest_RecordDate` | TField | Yes | Field denotes the date set by the issuer on which the shareholders identity is determined based on thesettledpositions. Validation Rules Input Mandatory |
| 11 | `SC.SRQ.RECORD.DATE.TIME` | `ScSrdHldRequest_RecordDateTime` |  |  |  |
| 12 | `SC.SRQ.THRESHOLD.QTY` | `ScSrdHldRequest_ThresholdQty` | TField |  | Field denotes the minimum number of shares need to be held by a shareholder above which the identificationmust bedisclosed. |
| 13 | `SC.SRQ.SHARE.HLD.DATE.MTHD` | `ScSrdHldRequest_ShareHldDateMthd` | TField |  | Field indicates the method to be used to determine from which date the shares have been held. |
| 14 | `SC.SRQ.RECIPIENT.LEI` | `ScSrdHldRequest_RecipientLei` | TField |  | Field denotes the Legal entity identifier of the issuer or third party nominated by the issuer to whom thedisclosure response shall be transmitted. |
| 15 | `SC.SRQ.RECIPIENT.NAME` | `ScSrdHldRequest_RecipientName` | TField |  | Field denotes the name of the party to whom the disclosure response must be sent. |
| 16 | `SC.SRQ.RECIPIENT.BIC` | `ScSrdHldRequest_RecipientBic` | TField |  | Field denotes the BIC of the party to whom the disclosure response must be sent. |
| 17 | `SC.SRQ.RECIPIENT.ADDR.TYPE` | `ScSrdHldRequest_RecipientAddrType` | TField |  | Field identifies the nature of postal address. |
| 18 | `SC.SRQ.RECIPIENT.ADDR` | `ScSrdHldRequest_RecipientAddr` | TField |  | Field provides the address of the issuer or the third party nominated by the issuer to whom the disclosureresponse shall be transmitted. |
| 19 | `SC.SRQ.RECIPIENT.STREET` | `ScSrdHldRequest_RecipientStreet` | TField |  | Field provides the street name where the issuer's or the third party nominated by the issuer building is located. |
| 20 | `SC.SRQ.RECIPIENT.BLDG.NUM` | `ScSrdHldRequest_RecipientBldgNum` | TField |  | Field provides the building number of the issuer or third party nominated by the issuer to whom the disclosureresponse shall be transmitted by the intermediary. |
| 21 | `SC.SRQ.RECIPIENT.POST.BOX` | `ScSrdHldRequest_RecipientPostBox` | TField |  | Field denotes the post box number of the issuer or or third party nominated by the issuer to whom thedisclosureresponse shall be transmitted by the intermediary. |
| 22 | `SC.SRQ.RECIPIENT.POST.CODE` | `ScSrdHldRequest_RecipientPostCode` | TField |  | Field provides the postal code of the issuer or third party nominated by the issuer. |
| 23 | `SC.SRQ.RECIPIENT.TOWN.NAME` | `ScSrdHldRequest_RecipientTownName` | TField |  | Field denotes the town name of the issuer's building or the third party to whom the disclosure response shall betransmitted. |
| 24 | `SC.SRQ.RECIPIENT.CTRY.SUB.DIV` | `ScSrdHldRequest_RecipientCtrySubDiv` | TField |  | Field denotes the region/ state of the issuer's or the third party's building location. |
| 25 | `SC.SRQ.RECIPIENT.COUNTRY` | `ScSrdHldRequest_RecipientCountry` | TField |  | Field denotes the country code of the issuer's location or the third party's location. |
| 26 | `SC.SRQ.RECIPIENT.EMAIL` | `ScSrdHldRequest_RecipientEmail` | TField |  | Field denotes the email address of the issuer or third party nominated by the issuer. |
| 27 | `SC.SRQ.RECIPIENT.URL` | `ScSrdHldRequest_RecipientUrl` | TField |  | Field denotes the URL address of the issuer or third party nominated by the issuer. |
| 28 | `SC.SRQ.RESPONSE.DATE` | `ScSrdHldRequest_ResponseDate` | TField |  | Field denotes the date by which a response to the Shareholders Identification Disclosure Request shall beprovided |
| 29 | `SC.SRQ.RESPONSE.DATE.TIME` | `ScSrdHldRequest_ResponseDateTime` |  |  |  |
| 30 | `SC.SRQ.ISSUER.DEADLINE.DATE` | `ScSrdHldRequest_IssuerDeadlineDate` | TField |  | Field denotes the latest date set by the issuer or a third party appointed by the issuer by which a responsetothe Shareholders Identification Disclosure Request shall be provided. |
| 31 | `SC.SRQ.ISSUER.DEADLINE.DATE.TIME` | `ScSrdHldRequest_IssuerDeadlineDateTime` |  |  |  |
| 32 | `SC.SRQ.ISSUER.LEI` | `ScSrdHldRequest_IssuerLei` | TField |  | Field denotes the Legal entity identifier of the issuer. |
| 33 | `SC.SRQ.ISSUER.NAME` | `ScSrdHldRequest_IssuerName` | TField |  | Field denotes the name of the issuer of the security. |
| 34 | `SC.SRQ.ISSUER.BIC` | `ScSrdHldRequest_IssuerBic` | TField |  | Field denotes the BIC of the issuer of the security |
| 35 | `SC.SRQ.ISSUER.ADDR.TYPE` | `ScSrdHldRequest_IssuerAddrType` | TField |  | Field identifies the nature of postal address. Validation Rules Allowed Values are - ADDR,PBOX,HOME,BIZZ,MLTO,DLVY |
| 36 | `SC.SRQ.ISSUER.ADDR` | `ScSrdHldRequest_IssuerAddr` | TField |  | Field provides the address of the issuer. |
| 37 | `SC.SRQ.ISSUER.STREET` | `ScSrdHldRequest_IssuerStreet` | TField |  | Field provides the street name where the issuer's building is located. |
| 38 | `SC.SRQ.ISSUER.BLDG.NUM` | `ScSrdHldRequest_IssuerBldgNum` | TField |  | Field provides the issuer's building number. |
| 39 | `SC.SRQ.ISSUER.POST.CODE` | `ScSrdHldRequest_IssuerPostCode` | TField |  | Field provides the postal code of the issuer building location. |
| 40 | `SC.SRQ.ISSUER.TOWN.NAME` | `ScSrdHldRequest_IssuerTownName` | TField |  | Field denotes the town name of the issuer's building. |
| 41 | `SC.SRQ.ISSUER.CTRY.SUB.DIV` | `ScSrdHldRequest_IssuerCtrySubDiv` | TField |  | Field denotes the region/ state of the issuer's building location. |
| 42 | `SC.SRQ.ISSUER.COUNTRY` | `ScSrdHldRequest_IssuerCountry` | TField |  | Field denotes the country of the issuer's location. |
| 43 | `SC.SRQ.I.S.I.N` | `ScSrdHldRequest_ISIN` | TField |  | Field denotes the ISIN number of the security for which the Shareholders Identification Disclosure Request isreceived. Validation Rules ISIN should not be mapped into multiple security Security Number mapped in this ISIN will be mapped to SECURITY.NO field |
| 44 | `SC.SRQ.SECURITY.ID` | `ScSrdHldRequest_SecurityId` | TField |  | Field dedenotes the identification of security based on domestic identification schema. |
| 45 | `SC.SRQ.SECURITY.SUFFIX` | `ScSrdHldRequest_SecuritySuffix` | TField |  | Field denotes the suffix of the SECURITY.ID |
| 46 | `SC.SRQ.SECURITY.TYPE` | `ScSrdHldRequest_SecurityType` | TField |  | Field denotes the Unique and unambiguous identification source of the SECURITY.ID |
| 47 | `SC.SRQ.SECURITY.DESC` | `ScSrdHldRequest_SecurityDesc` | TField |  | Field holds the description of the security. |
| 48 | `SC.SRQ.STATUS` | `ScSrdHldRequest_Status` | TField |  | Field denote the status of the record.A) ERR if there is any values missingB) OK if all details are received andthe record is authorised.C) CANC if seev.046 message is receivedD) RESPONDED if seev.047 is sent outE) RESPOND.CANCif seev.048 is sent out and no seev.047 is resent again |
| 49 | `SC.SRQ.ERR.REASON` | `ScSrdHldRequest_ErrReason` |  |  |  |
| 50 | `SC.SRQ.CANC.REASON` | `ScSrdHldRequest_CancReason` | TField |  | Field holds the reason of the Cancellation |
| 51 | `SC.SRQ.RERUN` | `ScSrdHldRequest_Rerun` | TField |  | Field can be set to Yes in order to recheck the qualified holdings as on record date. Validation Rules Input not allowed when STATUS is CANC |
| 52 | `SC.SRQ.DELIVERY.INREF` | `ScSrdHldRequest_DeliveryInref` | TField |  | Field holds the inward delivery reference of seev.045.(Shareholders Identification Disclosure Request). |
| 53 | `SC.SRQ.CANC.DELIVERY.INREF` | `ScSrdHldRequest_CancDeliveryInref` | TField |  | Field holds holds the inward delivery reference of seev.046 (Shareholders Identification Disclosure RequestCancellation Advice). |
| 54 | `SC.SRQ.RESPONSE.GEN` | `ScSrdHldRequest_ResponseGen` | TField |  | Field is set to Yes, system will generate a Shareholders Identification Disclosure Response message. Validation Rules Field not allowed when the status is not set as OK |
| 55 | `SC.SRQ.RESP.DELIVERY.OUTREF` | `ScSrdHldRequest_RespDeliveryOutref` |  |  |  |
| 56 | `SC.SRQ.RESP.CANC.OUTREF` | `ScSrdHldRequest_RespCancOutref` |  |  |  |
| 57 | `SC.SRQ.RESP.STATUS.INREF` | `ScSrdHldRequest_RespStatusInref` |  |  |  |
| 58 | `SC.SRQ.RESPONSE.ID` | `ScSrdHldRequest_ResponseId` |  |  |  |
| 59 | `SC.SRQ.RESPONSE.STATUS` | `ScSrdHldRequest_ResponseStatus` |  |  |  |
| 60 | `SC.SRQ.STATUS.REASON` | `ScSrdHldRequest_StatusReason` |  |  |  |
| 61 | `SC.SRQ.DEPO` | `ScSrdHldRequest_Depo` |  |  |  |
| 62 | `SC.SRQ.SUB.ACCOUNT` | `ScSrdHldRequest_SubAccount` |  |  |  |
| 63 | `SC.SRQ.OWN.ACC.QTY` | `ScSrdHldRequest_OwnAccQty` |  |  |  |
| 64 | `SC.SRQ.CLIENT.ACC.QTY` | `ScSrdHldRequest_ClientAccQty` |  |  |  |
| 65 | `SC.SRQ.TOTAL.QTY` | `ScSrdHldRequest_TotalQty` |  |  |  |
| 66 | `SC.SRQ.QTY.BELOW.THRSHLD` | `ScSrdHldRequest_QtyBelowThrshld` |  |  |  |
| 67 | `SC.SRQ.STP` | `ScSrdHldRequest_Stp` | TField |  | Field denotes whether the request is created via STP/manual process |
| 68 | `SC.SRQ.RESERVED.10` | `ScSrdHldRequest_Reserved10` | TField |  |  |
| 69 | `SC.SRQ.RESERVED.9` | `ScSrdHldRequest_Reserved9` | TField |  |  |
| 70 | `SC.SRQ.RESERVED.8` | `ScSrdHldRequest_Reserved8` | TField |  |  |
| 71 | `SC.SRQ.RESERVED.7` | `ScSrdHldRequest_Reserved7` | TField |  |  |
| 72 | `SC.SRQ.RESERVED.6` | `ScSrdHldRequest_Reserved6` | TField |  |  |
| 73 | `SC.SRQ.RESERVED.5` | `ScSrdHldRequest_Reserved5` | TField |  |  |
| 74 | `SC.SRQ.RESERVED.4` | `ScSrdHldRequest_Reserved4` | TField |  |  |
| 75 | `SC.SRQ.RESERVED.3` | `ScSrdHldRequest_Reserved3` | TField |  |  |
| 76 | `SC.SRQ.RESERVED.2` | `ScSrdHldRequest_Reserved2` | TField |  |  |
| 77 | `SC.SRQ.RESERVED.1` | `ScSrdHldRequest_Reserved1` | TField |  |  |
| 78 | `SC.SRQ.LOCAL.REF` | `ScSrdHldRequest_LocalRef` |  |  |  |
| 79 | `SC.SRQ.OVERRIDE` | `ScSrdHldRequest_Override` |  |  |  |
| 80 | `SC.SRQ.RECORD.STATUS` | `ScSrdHldRequest_RecordStatus` | String |  |  |
| 81 | `SC.SRQ.CURR.NO` | `ScSrdHldRequest_CurrNo` | String |  |  |
| 82 | `SC.SRQ.INPUTTER` | `ScSrdHldRequest_Inputter` |  |  |  |
| 83 | `SC.SRQ.DATE.TIME` | `ScSrdHldRequest_DateTime` |  |  |  |
| 84 | `SC.SRQ.AUTHORISER` | `ScSrdHldRequest_Authoriser` | String |  |  |
| 85 | `SC.SRQ.CO.CODE` | `ScSrdHldRequest_CoCode` | String |  |  |
| 86 | `SC.SRQ.DEPT.CODE` | `ScSrdHldRequest_DeptCode` | String |  |  |
| 87 | `SC.SRQ.AUDITOR.CODE` | `ScSrdHldRequest_AuditorCode` | String |  |  |
| 88 | `SC.SRQ.AUDIT.DATE.TIME` | `ScSrdHldRequest_AuditDateTime` | String |  |  |
