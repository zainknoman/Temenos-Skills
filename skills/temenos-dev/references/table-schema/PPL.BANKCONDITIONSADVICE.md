# PPL.BANKCONDITIONSADVICE — Table Schema

> Source: `INSERTS/I_F.PPL.BANKCONDITIONSADVICE` in `PP_BankConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPBCE.BankAdviceID` | `PplBankconditionsadvice_Bankadviceid` |  |  |  |
| 2 | `PPBCE.BankConditionsID` | `PplBankconditionsadvice_Bankconditionsid` |  |  |  |
| 3 | `PPBCE.SequenceNumber` | `PplBankconditionsadvice_Sequencenumber` |  |  |  |
| 4 | `PPBCE.DebitCreditAdvice` | `PplBankconditionsadvice_Debitcreditadvice` |  |  |  |
| 5 | `PPBCE.CTRBTRIndicator` | `PplBankconditionsadvice_Ctrbtrindicator` |  |  |  |
| 6 | `PPBCE.InitiatedByOthers` | `PplBankconditionsadvice_Initiatedbyothers` |  |  |  |
| 7 | `PPBCE.FromAmount` | `PplBankconditionsadvice_Fromamount` |  |  |  |
| 8 | `PPBCE.ToAmount` | `PplBankconditionsadvice_Toamount` |  |  |  |
| 9 | `PPBCE.DeliveryMethod` | `PplBankconditionsadvice_Deliverymethod` |  |  |  |
| 10 | `PPBCE.Telephonenumber` | `PplBankconditionsadvice_Telephonenumber` |  |  |  |
| 11 | `PPBCE.EmailID` | `PplBankconditionsadvice_Emailid` |  |  |  |
| 12 | `PPBCE.BICAddress` | `PplBankconditionsadvice_Bicaddress` |  |  |  |
| 13 | `PPBCE.SMSNumber` | `PplBankconditionsadvice_Smsnumber` |  |  |  |
| 14 | `PPBCE.FaxNumber` | `PplBankconditionsadvice_Faxnumber` |  |  |  |
| 15 | `PPBCE.PostName` | `PplBankconditionsadvice_Postname` |  |  |  |
| 16 | `PPBCE.PostAddress1` | `PplBankconditionsadvice_Postaddress1` |  |  |  |
| 17 | `PPBCE.PostAddress2` | `PplBankconditionsadvice_Postaddress2` |  |  |  |
| 18 | `PPBCE.PostAddress3` | `PplBankconditionsadvice_Postaddress3` |  |  |  |
| 19 | `PPBCE.Attention` | `PplBankconditionsadvice_Attention` |  |  |  |
