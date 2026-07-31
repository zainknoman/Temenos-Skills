# PPT.PAYMENTROUTERCOMPANY — Table Schema

> Source: `INSERTS/I_F.PPT.PAYMENTROUTERCOMPANY` in `PP_PaymentRouterService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPRC.CompanyCode` | `PptPaymentroutercompany_Companycode` |  |  |  |
| 2 | `PPPRC.StartDatePaymentRouterCompany` | `PptPaymentroutercompany_Startdatepaymentroutercompany` |  |  |  |
| 3 | `PPPRC.CompanyID` | `PptPaymentroutercompany_Companyid` |  |  |  |
| 4 | `PPPRC.EndDatePaymentRouterCompany` | `PptPaymentroutercompany_Enddatepaymentroutercompany` |  |  |  |
| 5 | `PPPRC.RACPaymentRouterCompany` | `PptPaymentroutercompany_Racpaymentroutercompany` |  |  |  |
| 6 | `PPPRC.RSCPaymentRouterCompany` | `PptPaymentroutercompany_Rscpaymentroutercompany` |  |  |  |
| 7 | `PPPRC.EntryUserID` | `PptPaymentroutercompany_Entryuserid` |  |  |  |
| 8 | `PPPRC.EntryDateTime` | `PptPaymentroutercompany_Entrydatetime` |  |  |  |
| 9 | `PPPRC.ApproverUserID` | `PptPaymentroutercompany_Approveruserid` |  |  |  |
| 10 | `PPPRC.ApprovedDateTime` | `PptPaymentroutercompany_Approveddatetime` |  |  |  |
