# PP.IN.CLAIM.REQ — Table Schema

> Source: `INSERTS/I_F.PP.IN.CLAIM.REQ` in `PP_InquiryGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CR.DeliveryRef` | `PpInClaimReq_Deliveryref` | TField |  |  |
| 2 | `PP.CR.SendersRef` | `PpInClaimReq_Sendersref` | TField |  | This field specifies the reference assigned by the Sender to unambiguously identify the message. |
| 3 | `PP.CR.RelatedRef` | `PpInClaimReq_Relatedref` | TField |  | This field contains the reference of the transaction to which the charge(s), interest and/or other expense(s) in this message apply. |
| 4 | `PP.CR.CcyAmount` | `PpInClaimReq_Ccyamount` | TField |  | This field specifies the currency and amount, that is, charges, interest or other expenses, claimed by the Sender. |
| 5 | `PP.CR.Ordins` | `PpInClaimReq_Ordins` | TField |  | This field identifies the ordering institution of the initial transaction, if different from the Receiver. |
| 6 | `PP.CR.SenderAddress` | `PpInClaimReq_Senderaddress` | TField |  | This field identifies the sender details of the Charge Payment Request. |
| 7 | `PP.CR.AcwinsBIC` | `PpInClaimReq_Acwinsbic` | TField |  | This field identifies the financial institution at which the Sender of the Charge Payment Request wishes to receive the funds. |
| 8 | `PP.CR.Status` | `PpInClaimReq_Status` | TField |  | This field indicates the status of the incoming charge payment request. |
| 9 | `PP.CR.RejectDescription` | `PpInClaimReq_Rejectdescription` | TField |  | This field identifies the reject reason of the charge payment request. |
| 10 | `PP.CR.RECORD.STATUS` | `PpInClaimReq_RecordStatus` | String |  |  |
| 11 | `PP.CR.CURR.NO` | `PpInClaimReq_CurrNo` | String |  |  |
| 12 | `PP.CR.INPUTTER` | `PpInClaimReq_Inputter` |  |  |  |
| 13 | `PP.CR.DATE.TIME` | `PpInClaimReq_DateTime` |  |  |  |
| 14 | `PP.CR.AUTHORISER` | `PpInClaimReq_Authoriser` | String |  |  |
| 15 | `PP.CR.CO.CODE` | `PpInClaimReq_CoCode` | String |  |  |
| 16 | `PP.CR.DEPT.CODE` | `PpInClaimReq_DeptCode` | String |  |  |
| 17 | `PP.CR.AUDITOR.CODE` | `PpInClaimReq_AuditorCode` | String |  |  |
| 18 | `PP.CR.AUDIT.DATE.TIME` | `PpInClaimReq_AuditDateTime` | String |  |  |
