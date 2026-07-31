# PP.POSTING.SET — Table Schema

> Source: `INSERTS/I_F.PP.POSTING.SET` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.ST.CompanyID` | `PpPostingSet_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. NoInput Field The value gets autopopulated based on the company that you login |
| 2 | `PP.ST.PostingProduct` | `PpPostingSet_Postingproduct` | TField | Yes | Posting product attached to the posting set defined. Validation Rules: Mandatory field. This field must match the posting product retrieved as output from product determination process. |
| 3 | `PP.ST.Ranking` | `PpPostingSet_Ranking` | TField | Yes | Specifies the order (sequence) of the record in the application. Based on the value, a record is prioritised in such a way that, it is given higher preference for selection under peeling logic applied in the payments hub. Validation Rules: Mandatory field. 9 numeric characters. |
| 4 | `PP.ST.StartDate` | `PpPostingSet_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. |
| 5 | `PP.ST.ChargePostingSeparately` | `PpPostingSet_Chargepostingseparately` | TField |  | Indicate whether the charges have to be posted along with the principal amount or have to be posted separately from the principal amount. Possible values: D: The Posting Set contains separate posting lines only for the debit side charges. C: The Posting Set contains separate posting lines only for the credit side charges. B: The Posting Set contains separate posting lines for both debit and credit charges. N: The Posting Set will not have separate posting lines for debit and credit charges. If a side(debit and credit) of the payment has "ChargePostingSeparately" set or such a setup is not present but the side has more than one charge excluding the VAT charge, then it indicates that the charges have to be posted separately from the principal for that side of the payment. Field should be checked twice (Debit side and Credit Side) |
| 6 | `PP.ST.ChargePostingDetail` | `PpPostingSet_Chargepostingdetail` | TField |  | Indicates whether each charge has to be displayed in a separate line or the charges can be summed up and only the summary charge amount needs to be displayed. Possible values: D: The posting set will have a separate posting line for each debit party charges. C: The posting set will have a separate posting line for each credit party charges. B: The posting set will have a separate posting line for both debit party and credit party charges N: The posting set will only have one posting line for all the debit party charges and one posting line for all the credit party charges. If a side(debit and credit) of the payment has "ChargePostingDetail" set or such a setup is not present but the side has more than one charge excluding the VAT charge, then it indicates that the charges have to be posted in detail for that side of the payment. Field should be checked twice (Debit side and Credit Side) |
| 7 | `PP.ST.VATONPrincipal` | `PpPostingSet_Vatonprincipal` | TField |  | Possible values: D: The Posting Set will have a posting Line for VAT on principal for the debit side only. C: The Posting Set will have a posting Line for VAT on principal for the credit side only. B: The Posting Set will have a posting Line for VAT on principal for both the sides of the payment (debit and credit). N: The Posting Set will not have postinglines for VAT on principal for both the sides of the payment (debit and credit). S: The posting set will have posting line for VAT on Principal for both the sides of the payment with a Zero suppress flag set on each side .The Zero suppress flag indicates that if the VAT on Principal amount is 0 , the posting line will not be displayed (suppress it). If a side of the payment has VATONPrincipal with a value other than zero , then that side require the VAT on principal Posting line. Field should be checked twice (Debit side and Credit Side) If the variable is present only on the debit side then the match criteria for this field must be D or S If the variable is present only on the credit side then the match criteria for this field must be C or S If the variable is present on both the sides then the match criteria for this field must be B or S If the variable is not present both the sides then the match criteria for this field must be N or S |
| 8 | `PP.ST.VATOnCharge` | `PpPostingSet_Vatoncharge` | TField |  | Possible values: D: The Posting Set will have a posting Line for VAT on Charges for the debit side only. C: The Posting Set will have a posting Line for VAT on Charges for the credit side only. B: The Posting Set will have a posting Line for VAT on Charges for both the sides of the payment (debit and credit). N: The Posting Set will not have posting lines for VAT on Charges for both the sides of the payment (debit and credit). S: The posting set will have posting line for VAT on charges for both the sides of the payment with a Zero suppress flag set on each side .The Zero suppress flag indicates that if the VAT on Charges amount is 0 , do not display the posting line(suppress it). If a side of the payment contains the field, "VATOnCharge" with a value set as "Yes" , then that side require the VAT on charges Posting line. Field should be checked twice (Debit side and Credit Side) If the field with value "Yes" is present only on the debit side then the match criteria for this field must be D or S If the field with value "Yes" is present only on the credit side then the match criteria for this field must be C or S If the field with value "Yes" is present on both the sides then the match criteria for this field must be B or S If the field is not present both the sides then the match criteria for this field must be N or S |
| 9 | `PP.ST.OCPPostingFlag` | `PpPostingSet_Ocppostingflag` | TField |  | Indicates whether OCP posting entries should be part of the posting set. Description of the field values are as follows. N: The Posting set will not have OCP posting lines Y: The Posting set will have OCP posting lines |
| 10 | `PP.ST.EndDate` | `PpPostingSet_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 11 | `PP.ST.PartyFlag` | `PpPostingSet_Partyflag` |  |  |  |
| 12 | `PP.ST.SequenceNumber` | `PpPostingSet_Sequencenumber` |  |  |  |
| 13 | `PP.ST.AccountToken` | `PpPostingSet_Accounttoken` |  |  |  |
| 14 | `PP.ST.AmountToken` | `PpPostingSet_Amounttoken` |  |  |  |
| 15 | `PP.ST.BookingDate` | `PpPostingSet_Bookingdate` |  |  |  |
| 16 | `PP.ST.ValueDateToken` | `PpPostingSet_Valuedatetoken` |  |  |  |
| 17 | `PP.ST.BookingCode` | `PpPostingSet_Bookingcode` |  |  |  |
| 18 | `PP.ST.SuppressZeroFlag` | `PpPostingSet_Suppresszeroflag` |  |  |  |
| 19 | `PP.ST.StatementFormat` | `PpPostingSet_Statementformat` |  |  |  |
| 20 | `PP.ST.RESERVED.5` | `PpPostingSet_Reserved5` | TField |  |  |
| 21 | `PP.ST.RESERVED.4` | `PpPostingSet_Reserved4` | TField |  |  |
| 22 | `PP.ST.RESERVED.3` | `PpPostingSet_Reserved3` | TField |  |  |
| 23 | `PP.ST.RESERVED.2` | `PpPostingSet_Reserved2` | TField |  |  |
| 24 | `PP.ST.RESERVED.1` | `PpPostingSet_Reserved1` | TField |  |  |
| 25 | `PP.ST.LOCAL.REF` | `PpPostingSet_LocalRef` |  |  |  |
| 26 | `PP.ST.LinkID` | `PpPostingSet_Linkid` | TField |  |  |
| 27 | `PP.ST.OVERRIDE` | `PpPostingSet_Override` |  |  |  |
| 28 | `PP.ST.RECORD.STATUS` | `PpPostingSet_RecordStatus` | String |  |  |
| 29 | `PP.ST.CURR.NO` | `PpPostingSet_CurrNo` | String |  |  |
| 30 | `PP.ST.INPUTTER` | `PpPostingSet_Inputter` |  |  |  |
| 31 | `PP.ST.DATE.TIME` | `PpPostingSet_DateTime` |  |  |  |
| 32 | `PP.ST.AUTHORISER` | `PpPostingSet_Authoriser` | String |  |  |
| 33 | `PP.ST.CO.CODE` | `PpPostingSet_CoCode` | String |  |  |
| 34 | `PP.ST.DEPT.CODE` | `PpPostingSet_DeptCode` | String |  |  |
| 35 | `PP.ST.AUDITOR.CODE` | `PpPostingSet_AuditorCode` | String |  |  |
| 36 | `PP.ST.AUDIT.DATE.TIME` | `PpPostingSet_AuditDateTime` | String |  |  |
