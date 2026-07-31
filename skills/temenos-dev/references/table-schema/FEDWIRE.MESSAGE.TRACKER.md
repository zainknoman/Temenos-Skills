# FEDWIRE.MESSAGE.TRACKER — Table Schema

> Source: `INSERTS/I_F.FEDWIRE.MESSAGE.TRACKER` in `USRTGS_Fedwire.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FWMTR.DIRECTION` | `FedwireMessageTracker_Direction` | TField |  | Contains the direction of message flow. Possible values: INWARD OUTWARD |
| 2 | `FWMTR.COMPANY.CODE` | `FedwireMessageTracker_CompanyCode` | TField |  | Company code where the message was processed. A valid entry in COMPANY. |
| 3 | `FWMTR.APPLICATION` | `FedwireMessageTracker_Application` | TField |  | T24 application used to originate/post the fedwire message |
| 4 | `FWMTR.TRANS.REF` | `FedwireMessageTracker_TransRef` | TField |  | Reference of the request/posted transaction. |
| 5 | `FWMTR.PROCESSING.DATE` | `FedwireMessageTracker_ProcessingDate` | TField |  | Date on which the message was processed. |
| 6 | `FWMTR.RTGS.TIME.STAMP` | `FedwireMessageTracker_RtgsTimeStamp` | TField |  | Tag {1110} value mapped to this field. |
| 7 | `FWMTR.AMOUNT` | `FedwireMessageTracker_Amount` | TField |  | Amount of the transaction processed. |
| 8 | `FWMTR.ORIGINATOR` | `FedwireMessageTracker_Originator` | TField |  | Originator of the payment transaction. |
| 9 | `FWMTR.BENEFICIARY` | `FedwireMessageTracker_Beneficiary` |  |  |  |
| 10 | `FWMTR.IMAD.NUMBER` | `FedwireMessageTracker_ImadNumber` | TField |  | Input Message Accountability Data (IMAD) number assigned to this message. |
| 11 | `FWMTR.PREV.IMAD.NUMBER` | `FedwireMessageTracker_PrevImadNumber` | TField |  | Previous IMAD number referenced by this message. |
| 12 | `FWMTR.OMAD.NUMBER` | `FedwireMessageTracker_OmadNumber` | TField |  | Output Message Accountability Data (IMAD) number assigned to this message. |
| 13 | `FWMTR.STATUS` | `FedwireMessageTracker_Status` | TField |  | Status of the message processed. Possible values: PROCESSED REQUEST.SENT RESUBMIT RESUBMITTED REPAIR ACK NACK RESPONSE.RECEIVED REVERSED WAITING.LIST AWAITING.RETURN.APPROVAL RETURNED AWAITING.REJECT.APPROVAL REJECTED VOID MANDATE.MATCHED DRWI DRWERR DRWM AWAITING.APPROVAL OFAC.PENDING OFAC.FAILED PENDING.ACTION MANUAL.REJECTED |
| 14 | `FWMTR.STATUS.DT.TIME` | `FedwireMessageTracker_StatusDtTime` | TField |  | Status date and time |
| 15 | `FWMTR.PREV.STATUS` | `FedwireMessageTracker_PrevStatus` |  |  |  |
| 16 | `FWMTR.PREV.STATUS.DT` | `FedwireMessageTracker_PrevStatusDt` |  |  |  |
| 17 | `FWMTR.BUSINESS.FUNCTION` | `FedwireMessageTracker_BusinessFunction` | TField |  | Business function code associated with the message. Valid entry in FEDWIRE.BUSINESS.FUNCTION |
| 18 | `FWMTR.MESSAGE.TYPE` | `FedwireMessageTracker_MessageType` | TField |  | A combination of Message Type code and Subtype code. |
| 19 | `FWMTR.EXCH.RATE` | `FedwireMessageTracker_ExchRate` | TField |  | The currency conversion rate, if any. Mapped form tag {3720} |
| 20 | `FWMTR.TEST.PROD` | `FedwireMessageTracker_TestProd` | TField |  | Test or production environment indicator. Possible values: T - Test P - Production |
| 21 | `FWMTR.SENDER.ABA` | `FedwireMessageTracker_SenderAba` | TField |  | Tag {3100} value mapped to this field. Contains the Sender &apos; s ABA number. |
| 22 | `FWMTR.RECEIVER.ABA` | `FedwireMessageTracker_ReceiverAba` | TField |  | Tag {3400} value mapped to this field. Contains the Receiver &apos; s ABA number. |
| 23 | `FWMTR.PH.MESSAGE` | `FedwireMessageTracker_PhMessage` |  |  |  |
| 24 | `FWMTR.FEDWIRE.MESSAGE` | `FedwireMessageTracker_FedwireMessage` |  |  |  |
| 25 | `FWMTR.TAG` | `FedwireMessageTracker_Tag` |  |  |  |
| 26 | `FWMTR.TAG.VALUE` | `FedwireMessageTracker_TagValue` |  |  |  |
| 27 | `FWMTR.TAG.ELEMENT` | `FedwireMessageTracker_TagElement` |  |  |  |
| 28 | `FWMTR.TAG.ELEMENT.VAL` | `FedwireMessageTracker_TagElementVal` |  |  |  |
| 29 | `FWMTR.RESERVED.25` | `FedwireMessageTracker_Reserved25` |  |  |  |
| 30 | `FWMTR.RESERVED.24` | `FedwireMessageTracker_Reserved24` |  |  |  |
| 31 | `FWMTR.RESERVED.23` | `FedwireMessageTracker_Reserved23` |  |  |  |
| 32 | `FWMTR.ERROR.MSG` | `FedwireMessageTracker_ErrorMsg` |  |  |  |
| 33 | `FWMTR.LOCAL.REF` | `FedwireMessageTracker_LocalRef` |  |  |  |
| 34 | `FWMTR.CORRECTED.ACCOUNT.NUMBER` | `FedwireMessageTracker_CorrectedAccountNumber` | TField |  | Will store the repaired account number based on the outcome of the routines configured in FEDWIRE.PARAMETER |
| 35 | `FWMTR.RESERVED.20` | `FedwireMessageTracker_Reserved20` | TField |  |  |
| 36 | `FWMTR.RESERVED.19` | `FedwireMessageTracker_Reserved19` | TField |  |  |
| 37 | `FWMTR.RESERVED.18` | `FedwireMessageTracker_Reserved18` | TField |  |  |
| 38 | `FWMTR.RESERVED.17` | `FedwireMessageTracker_Reserved17` | TField |  |  |
| 39 | `FWMTR.RESERVED.16` | `FedwireMessageTracker_Reserved16` | TField |  |  |
| 40 | `FWMTR.RESERVED.15` | `FedwireMessageTracker_Reserved15` | TField |  |  |
| 41 | `FWMTR.RESERVED.14` | `FedwireMessageTracker_Reserved14` | TField |  |  |
| 42 | `FWMTR.RESERVED.13` | `FedwireMessageTracker_Reserved13` | TField |  |  |
| 43 | `FWMTR.RESERVED.12` | `FedwireMessageTracker_Reserved12` | TField |  |  |
| 44 | `FWMTR.RESERVED.11` | `FedwireMessageTracker_Reserved11` | TField |  |  |
| 45 | `FWMTR.RESERVED.10` | `FedwireMessageTracker_Reserved10` | TField |  |  |
| 46 | `FWMTR.RESERVED.9` | `FedwireMessageTracker_Reserved9` | TField |  |  |
| 47 | `FWMTR.RESERVED.8` | `FedwireMessageTracker_Reserved8` | TField |  |  |
| 48 | `FWMTR.RESERVED.7` | `FedwireMessageTracker_Reserved7` | TField |  |  |
| 49 | `FWMTR.RESERVED.6` | `FedwireMessageTracker_Reserved6` | TField |  |  |
| 50 | `FWMTR.RESERVED.5` | `FedwireMessageTracker_Reserved5` | TField |  |  |
| 51 | `FWMTR.RESERVED.4` | `FedwireMessageTracker_Reserved4` | TField |  |  |
| 52 | `FWMTR.RESERVED.3` | `FedwireMessageTracker_Reserved3` | TField |  |  |
| 53 | `FWMTR.RESERVED.2` | `FedwireMessageTracker_Reserved2` | TField |  |  |
| 54 | `FWMTR.RESERVED.1` | `FedwireMessageTracker_Reserved1` | TField |  |  |
| 55 | `FWMTR.OVERRIDE` | `FedwireMessageTracker_Override` |  |  |  |
| 56 | `FWMTR.RECORD.STATUS` | `FedwireMessageTracker_RecordStatus` | String |  |  |
| 57 | `FWMTR.CURR.NO` | `FedwireMessageTracker_CurrNo` | String |  |  |
| 58 | `FWMTR.INPUTTER` | `FedwireMessageTracker_Inputter` |  |  |  |
| 59 | `FWMTR.DATE.TIME` | `FedwireMessageTracker_DateTime` |  |  |  |
| 60 | `FWMTR.AUTHORISER` | `FedwireMessageTracker_Authoriser` | String |  |  |
| 61 | `FWMTR.CO.CODE` | `FedwireMessageTracker_CoCode` | String |  |  |
| 62 | `FWMTR.DEPT.CODE` | `FedwireMessageTracker_DeptCode` | String |  |  |
| 63 | `FWMTR.AUDITOR.CODE` | `FedwireMessageTracker_AuditorCode` | String |  |  |
| 64 | `FWMTR.AUDIT.DATE.TIME` | `FedwireMessageTracker_AuditDateTime` | String |  |  |
