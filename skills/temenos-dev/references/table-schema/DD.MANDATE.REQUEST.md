# DD.MANDATE.REQUEST — Table Schema

> Source: `INSERTS/I_F.DD.MANDATE.REQUEST` in `DD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DMR.REQUEST.TYPE` | `Dmr_RequestType` |  |  |  |
| 2 | `DMR.MANDATE.SERVICE` | `Dmr_MandateService` |  |  |  |
| 3 | `DMR.PAYMNT.SRVC.LVL` | `Dmr_PaymntSrvcLvl` |  |  |  |
| 4 | `DMR.LOCAL.INST.CODE` | `Dmr_LocalInstCode` |  |  |  |
| 5 | `DMR.MANDATE.REFERENCE` | `Dmr_MandateReference` |  |  |  |
| 6 | `DMR.CREDITOR.IDENTIFIER` | `Dmr_CreditorIdentifier` |  |  |  |
| 7 | `DMR.NEW.DEBIT.ACCOUNT` | `Dmr_NewDebitAccount` |  |  |  |
| 8 | `DMR.NEW.DEBIT.IBAN` | `Dmr_NewDebitIban` |  |  |  |
| 9 | `DMR.REASON.CODE` | `Dmr_ReasonCode` |  |  |  |
| 10 | `DMR.REASON.DETAILS` | `Dmr_ReasonDetails` |  |  |  |
| 11 | `DMR.INITIATED.BY` | `Dmr_InitiatedBy` |  |  |  |
| 12 | `DMR.REQUEST.STATUS` | `Dmr_RequestStatus` |  |  |  |
| 13 | `DMR.ACCEPTANCE.STATUS` | `Dmr_AcceptanceStatus` |  |  |  |
| 14 | `DMR.ACCEPTANCE.RSN.CODE` | `Dmr_AcceptanceRsnCode` |  |  |  |
| 15 | `DMR.ORIG.DD.DDI.ID` | `Dmr_OrigDdDdiId` |  |  |  |
| 16 | `DMR.DD.MNDT.SENT.TXN.ID` | `Dmr_DdMndtSentTxnId` |  |  |  |
| 17 | `DMR.RESERVED10` | `Dmr_Reserved10` |  |  |  |
| 18 | `DMR.RESERVED9` | `Dmr_Reserved9` |  |  |  |
| 19 | `DMR.RESERVED8` | `Dmr_Reserved8` |  |  |  |
| 20 | `DMR.RESERVED7` | `Dmr_Reserved7` |  |  |  |
| 21 | `DMR.RESERVED6` | `Dmr_Reserved6` |  |  |  |
| 22 | `DMR.RESERVED5` | `Dmr_Reserved5` |  |  |  |
| 23 | `DMR.RESERVED4` | `Dmr_Reserved4` |  |  |  |
| 24 | `DMR.RESERVED3` | `Dmr_Reserved3` |  |  |  |
| 25 | `DMR.RESERVED2` | `Dmr_Reserved2` |  |  |  |
| 26 | `DMR.RESERVED1` | `Dmr_Reserved1` |  |  |  |
| 27 | `DMR.LOCAL.REF` | `Dmr_LocalRef` |  |  |  |
| 28 | `DMR.OVERRIDE` | `Dmr_Override` |  |  |  |
| 29 | `DMR.RECORD.STATUS` | `Dmr_RecordStatus` |  |  |  |
| 30 | `DMR.CURR.NO` | `Dmr_CurrNo` |  |  |  |
| 31 | `DMR.INPUTTER` | `Dmr_Inputter` |  |  |  |
| 32 | `DMR.DATE.TIME` | `Dmr_DateTime` |  |  |  |
| 33 | `DMR.AUTHORISER` | `Dmr_Authoriser` |  |  |  |
| 34 | `DMR.CO.CODE` | `Dmr_CoCode` |  |  |  |
| 35 | `DMR.DEPT.CODE` | `Dmr_DeptCode` |  |  |  |
| 36 | `DMR.AUDITOR.CODE` | `Dmr_AuditorCode` |  |  |  |
| 37 | `DMR.AUDIT.DATE.TIME` | `Dmr_AuditDateTime` |  |  |  |
