# PP.AUTHORIZATIONPRINCIPLE.PDS — Table Schema

> Source: `INSERTS/I_F.PP.AUTHORIZATIONPRINCIPLE.PDS` in `PP_InquiryGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.AUP.ProcessingCompany` | `PpAuthorizationprinciplePds_Processingcompany` | TField |  |  |
| 2 | `PP.AUP.Status` | `PpAuthorizationprinciplePds_Status` | TField |  |  |
| 3 | `PP.AUP.Ranking` | `PpAuthorizationprinciplePds_Ranking` | TField |  |  |
| 4 | `PP.AUP.Direction` | `PpAuthorizationprinciplePds_Direction` | TField |  |  |
| 5 | `PP.AUP.TransactionAmountLowerLimit` | `PpAuthorizationprinciplePds_Transactionamountlowerlimit` | TField |  |  |
| 6 | `PP.AUP.TransactionAmountUpperLimit` | `PpAuthorizationprinciplePds_Transactionamountupperlimit` | TField |  |  |
| 7 | `PP.AUP.TransactionCurrencyCode` | `PpAuthorizationprinciplePds_Transactioncurrencycode` | TField |  |  |
| 8 | `PP.AUP.LowerMessagePriority` | `PpAuthorizationprinciplePds_Lowermessagepriority` | TField |  |  |
| 9 | `PP.AUP.UpperMessagePriority` | `PpAuthorizationprinciplePds_Uppermessagepriority` | TField |  |  |
| 10 | `PP.AUP.IncomingMessageType` | `PpAuthorizationprinciplePds_Incomingmessagetype` | TField |  |  |
| 11 | `PP.AUP.OriginatingSource` | `PpAuthorizationprinciplePds_Originatingsource` | TField |  |  |
| 12 | `PP.AUP.CTRBTRIndicator` | `PpAuthorizationprinciplePds_Ctrbtrindicator` | TField |  |  |
| 13 | `PP.AUP.DebitBusinessLine` | `PpAuthorizationprinciplePds_Debitbusinessline` | TField |  |  |
| 14 | `PP.AUP.CreditBusinessLine` | `PpAuthorizationprinciplePds_Creditbusinessline` | TField |  |  |
| 15 | `PP.AUP.HighWeightCode` | `PpAuthorizationprinciplePds_Highweightcode` | TField |  |  |
| 16 | `PP.AUP.StartDate` | `PpAuthorizationprinciplePds_Startdate` | TField |  |  |
| 17 | `PP.AUP.AuthorizationPrinciple` | `PpAuthorizationprinciplePds_Authorizationprinciple` | TField |  |  |
| 18 | `PP.AUP.EndDate` | `PpAuthorizationprinciplePds_Enddate` | TField |  |  |
| 19 | `PP.AUP.RESERVED.5` | `PpAuthorizationprinciplePds_Reserved5` | TField |  |  |
| 20 | `PP.AUP.RESERVED.4` | `PpAuthorizationprinciplePds_Reserved4` | TField |  |  |
| 21 | `PP.AUP.RESERVED.3` | `PpAuthorizationprinciplePds_Reserved3` | TField |  |  |
| 22 | `PP.AUP.RESERVED.2` | `PpAuthorizationprinciplePds_Reserved2` | TField |  |  |
| 23 | `PP.AUP.RESERVED.1` | `PpAuthorizationprinciplePds_Reserved1` | TField |  |  |
| 24 | `PP.AUP.LOCAL.REF` | `PpAuthorizationprinciplePds_LocalRef` |  |  |  |
| 25 | `PP.AUP.LinkID` | `PpAuthorizationprinciplePds_Linkid` | TField |  |  |
| 26 | `PP.AUP.OVERRIDE` | `PpAuthorizationprinciplePds_Override` |  |  |  |
| 27 | `PP.AUP.RECORD.STATUS` | `PpAuthorizationprinciplePds_RecordStatus` | String |  |  |
| 28 | `PP.AUP.CURR.NO` | `PpAuthorizationprinciplePds_CurrNo` | String |  |  |
| 29 | `PP.AUP.INPUTTER` | `PpAuthorizationprinciplePds_Inputter` |  |  |  |
| 30 | `PP.AUP.DATE.TIME` | `PpAuthorizationprinciplePds_DateTime` |  |  |  |
| 31 | `PP.AUP.AUTHORISER` | `PpAuthorizationprinciplePds_Authoriser` | String |  |  |
| 32 | `PP.AUP.CO.CODE` | `PpAuthorizationprinciplePds_CoCode` | String |  |  |
| 33 | `PP.AUP.DEPT.CODE` | `PpAuthorizationprinciplePds_DeptCode` | String |  |  |
| 34 | `PP.AUP.AUDITOR.CODE` | `PpAuthorizationprinciplePds_AuditorCode` | String |  |  |
| 35 | `PP.AUP.AUDIT.DATE.TIME` | `PpAuthorizationprinciplePds_AuditDateTime` | String |  |  |
