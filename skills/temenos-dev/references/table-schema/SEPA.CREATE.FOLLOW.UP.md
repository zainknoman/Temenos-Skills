# SEPA.CREATE.FOLLOW.UP — Table Schema

> Source: `INSERTS/I_F.SEPA.CREATE.FOLLOW.UP` in `EP_OutwardProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EP.CRE.FUP.REASON.CODE` | `SepaCreateFollowUp_ReasonCode` | A (Alphanumeric) |  | This field defines the Reason code updated for reversal of transaction made. Validation Rules Value upto 4 type A(Alphanumeric) Value should exist in SEPA.REASONS Application |
| 2 | `EP.CRE.FUP.CURRENT.OPT.CODE` | `SepaCreateFollowUp_CurrentOptCode` | TField |  | This field specifies the SEPA operation code (3 digits) Validation Rules Value must be 3 numeirc values. NOINPUT FIELD |
| 3 | `EP.CRE.FUP.APPLYING.ON` | `SepaCreateFollowUp_ApplyingOn` | A (Alphanumeric) |  | This field specifies the Way of previous application referred to. �INWARD� : reply to a received operation �OUTWARD� : reply to a sent operation Validation Rules Value upto 7 type A(Alphanumeric) User can input only &apos;INWARD&apos; or &apos;OUTWARD&apos; |
| 4 | `EP.CRE.FUP.NEXT.OPERATION.CODE` | `SepaCreateFollowUp_NextOperationCode` | TField |  | This field specifies the SEPA operation code (3 digits) Validation Rules Value must be 3 with numeric values. Should be a valid Operation Code in SEPA.LAYOUT It is interlinked with NEXT.PURPOSE.CODE field. |
| 5 | `EP.CRE.FUP.NEXT.PURPOSE.CODE` | `SepaCreateFollowUp_NextPurposeCode` | TField |  | This field specifies the SEPA purpose code (3 digits) . Like "CXL,RET" . Validation Rules: Value must be 3 with A(Alphabetic). It is interlinked with NEXT.OPERATION.CODE field. |
| 6 | `EP.CRE.FUP.FOLLOWUP.ID` | `SepaCreateFollowUp_FollowupId` | TField |  | This field holds the SEPA.FOLLOW.UP ID to the generated After the authorisation of the SEPA.CREATE.FOLLOW.UP record � no input field. Validation Rules NOINPUT FIELD |
| 7 | `EP.CRE.FUP.FOLLOW.UP.VERSION` | `SepaCreateFollowUp_FollowUpVersion` | A (Alphanumeirc) |  | Value Given here is used fo OFS Version which used to create SEPA.FOLLOW.UP Record Validation Rules Value upto 70 type A(Alphanumeirc) Value should exist in VERSION Application. |
| 8 | `EP.CRE.FUP.RESERVED.10` | `SepaCreateFollowUp_Reserved10` | TField |  |  |
| 9 | `EP.CRE.FUP.RESERVED.09` | `SepaCreateFollowUp_Reserved09` | TField |  |  |
| 10 | `EP.CRE.FUP.RESERVED.08` | `SepaCreateFollowUp_Reserved08` | TField |  |  |
| 11 | `EP.CRE.FUP.RESERVED.07` | `SepaCreateFollowUp_Reserved07` | TField |  |  |
| 12 | `EP.CRE.FUP.RESERVED.06` | `SepaCreateFollowUp_Reserved06` | TField |  |  |
| 13 | `EP.CRE.FUP.RESERVED.05` | `SepaCreateFollowUp_Reserved05` | TField |  |  |
| 14 | `EP.CRE.FUP.RESERVED.04` | `SepaCreateFollowUp_Reserved04` | TField |  |  |
| 15 | `EP.CRE.FUP.RESERVED.03` | `SepaCreateFollowUp_Reserved03` | TField |  |  |
| 16 | `EP.CRE.FUP.RESERVED.02` | `SepaCreateFollowUp_Reserved02` | TField |  |  |
| 17 | `EP.CRE.FUP.RESERVED.01` | `SepaCreateFollowUp_Reserved01` | TField |  |  |
| 18 | `EP.CRE.FUP.LOCAL.REF` | `SepaCreateFollowUp_LocalRef` |  |  |  |
| 19 | `EP.CRE.FUP.OVERRIDE` | `SepaCreateFollowUp_Override` |  |  |  |
| 20 | `EP.CRE.FUP.RECORD.STATUS` | `SepaCreateFollowUp_RecordStatus` | String |  |  |
| 21 | `EP.CRE.FUP.CURR.NO` | `SepaCreateFollowUp_CurrNo` | String |  |  |
| 22 | `EP.CRE.FUP.INPUTTER` | `SepaCreateFollowUp_Inputter` |  |  |  |
| 23 | `EP.CRE.FUP.DATE.TIME` | `SepaCreateFollowUp_DateTime` |  |  |  |
| 24 | `EP.CRE.FUP.AUTHORISER` | `SepaCreateFollowUp_Authoriser` | String |  |  |
| 25 | `EP.CRE.FUP.CO.CODE` | `SepaCreateFollowUp_CoCode` | String |  |  |
| 26 | `EP.CRE.FUP.DEPT.CODE` | `SepaCreateFollowUp_DeptCode` | String |  |  |
| 27 | `EP.CRE.FUP.AUDITOR.CODE` | `SepaCreateFollowUp_AuditorCode` | String |  |  |
| 28 | `EP.CRE.FUP.AUDIT.DATE.TIME` | `SepaCreateFollowUp_AuditDateTime` | String |  |  |
