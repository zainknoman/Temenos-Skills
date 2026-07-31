# LQ.LTA.QUALIFICATION — Table Schema

> Source: `INSERTS/I_F.LQ.LTA.QUALIFICATION` in `LQ_LiquidityManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LQ.LTA.SENDER.INSTITUTION.ID` | `LqLtaQualification_SenderInstitutionId` | TField |  |  |
| 2 | `LQ.LTA.RECEIVER.INSTITUTION.ID` | `LqLtaQualification_ReceiverInstitutionId` | TField |  |  |
| 3 | `LQ.LTA.PARTICIPANT.IDENTIFICATION` | `LqLtaQualification_ParticipantIdentification` | TField |  | BIC of our bank. |
| 4 | `LQ.LTA.RANKING` | `LqLtaQualification_Ranking` |  |  |  |
| 5 | `LQ.LTA.ADVICE.TYPE` | `LqLtaQualification_AdviceType` |  |  |  |
| 6 | `LQ.LTA.TRANSFER.TYPE` | `LqLtaQualification_TransferType` |  |  |  |
| 7 | `LQ.LTA.CSM.STATUS.CODE` | `LqLtaQualification_CsmStatusCode` |  |  |  |
| 8 | `LQ.LTA.LOCAL.INSTRUMENT.CODE` | `LqLtaQualification_LocalInstrumentCode` |  |  |  |
| 9 | `LQ.LTA.LOCAL.INSTRUMENT.PROP` | `LqLtaQualification_LocalInstrumentProp` |  |  |  |
| 10 | `LQ.LTA.LTA.PAYMENT` | `LqLtaQualification_LtaPayment` |  |  |  |
| 11 | `LQ.LTA.RESERVED.12` | `LqLtaQualification_Reserved12` |  |  |  |
| 12 | `LQ.LTA.RESERVED.11` | `LqLtaQualification_Reserved11` |  |  |  |
| 13 | `LQ.LTA.ACCOUNT.IDENTIFICATION` | `LqLtaQualification_AccountIdentification` |  |  |  |
| 14 | `LQ.LTA.DEBTOR.ACCOUNT` | `LqLtaQualification_DebtorAccount` |  |  |  |
| 15 | `LQ.LTA.DEBTOR.AGENT` | `LqLtaQualification_DebtorAgent` |  |  |  |
| 16 | `LQ.LTA.CREDITOR.AGENT` | `LqLtaQualification_CreditorAgent` |  |  |  |
| 17 | `LQ.LTA.CREDITOR.ACCOUNT` | `LqLtaQualification_CreditorAccount` |  |  |  |
| 18 | `LQ.LTA.CONTEXT.NAME` | `LqLtaQualification_ContextName` |  |  |  |
| 19 | `LQ.LTA.CONTEXT.VALUE` | `LqLtaQualification_ContextValue` |  |  |  |
| 20 | `LQ.LTA.RESERVED.10` | `LqLtaQualification_Reserved10` | TField |  |  |
| 21 | `LQ.LTA.RESERVED.9` | `LqLtaQualification_Reserved9` | TField |  |  |
| 22 | `LQ.LTA.RESERVED.8` | `LqLtaQualification_Reserved8` | TField |  |  |
| 23 | `LQ.LTA.RESERVED.7` | `LqLtaQualification_Reserved7` | TField |  |  |
| 24 | `LQ.LTA.RESERVED.6` | `LqLtaQualification_Reserved6` | TField |  |  |
| 25 | `LQ.LTA.RESERVED.5` | `LqLtaQualification_Reserved5` | TField |  |  |
| 26 | `LQ.LTA.RESERVED.4` | `LqLtaQualification_Reserved4` | TField |  |  |
| 27 | `LQ.LTA.RESERVED.3` | `LqLtaQualification_Reserved3` | TField |  |  |
| 28 | `LQ.LTA.RESERVED.2` | `LqLtaQualification_Reserved2` | TField |  |  |
| 29 | `LQ.LTA.RESERVED.1` | `LqLtaQualification_Reserved1` | TField |  |  |
| 30 | `LQ.LTA.LOCAL.REF` | `LqLtaQualification_LocalRef` |  |  |  |
| 31 | `LQ.LTA.OVERRIDE` | `LqLtaQualification_Override` |  |  |  |
| 32 | `LQ.LTA.RECORD.STATUS` | `LqLtaQualification_RecordStatus` | String |  |  |
| 33 | `LQ.LTA.CURR.NO` | `LqLtaQualification_CurrNo` | String |  |  |
| 34 | `LQ.LTA.INPUTTER` | `LqLtaQualification_Inputter` |  |  |  |
| 35 | `LQ.LTA.DATE.TIME` | `LqLtaQualification_DateTime` |  |  |  |
| 36 | `LQ.LTA.AUTHORISER` | `LqLtaQualification_Authoriser` | String |  |  |
| 37 | `LQ.LTA.CO.CODE` | `LqLtaQualification_CoCode` | String |  |  |
| 38 | `LQ.LTA.DEPT.CODE` | `LqLtaQualification_DeptCode` | String |  |  |
| 39 | `LQ.LTA.AUDITOR.CODE` | `LqLtaQualification_AuditorCode` | String |  |  |
| 40 | `LQ.LTA.AUDIT.DATE.TIME` | `LqLtaQualification_AuditDateTime` | String |  |  |
