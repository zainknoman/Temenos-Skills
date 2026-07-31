# PP.POSTING.SET.PDS — Table Schema

> Source: `INSERTS/I_F.PP.POSTING.SET.PDS` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.ST.CompanyID` | `PpPostingSetPds_Companyid` | TField |  |  |
| 2 | `PP.ST.PostingProduct` | `PpPostingSetPds_Postingproduct` | TField |  |  |
| 3 | `PP.ST.Ranking` | `PpPostingSetPds_Ranking` | TField |  |  |
| 4 | `PP.ST.StartDate` | `PpPostingSetPds_Startdate` | TField |  |  |
| 5 | `PP.ST.ChargePostingSeparately` | `PpPostingSetPds_Chargepostingseparately` | TField |  |  |
| 6 | `PP.ST.ChargePostingDetail` | `PpPostingSetPds_Chargepostingdetail` | TField |  |  |
| 7 | `PP.ST.VATONPrincipal` | `PpPostingSetPds_Vatonprincipal` | TField |  |  |
| 8 | `PP.ST.VATOnCharge` | `PpPostingSetPds_Vatoncharge` | TField |  |  |
| 9 | `PP.ST.OCPPostingFlag` | `PpPostingSetPds_Ocppostingflag` | TField |  |  |
| 10 | `PP.ST.EndDate` | `PpPostingSetPds_Enddate` | TField |  |  |
| 11 | `PP.ST.PartyFlag` | `PpPostingSetPds_Partyflag` |  |  |  |
| 12 | `PP.ST.SequenceNumber` | `PpPostingSetPds_Sequencenumber` |  |  |  |
| 13 | `PP.ST.AccountToken` | `PpPostingSetPds_Accounttoken` |  |  |  |
| 14 | `PP.ST.AmountToken` | `PpPostingSetPds_Amounttoken` |  |  |  |
| 15 | `PP.ST.BookingDate` | `PpPostingSetPds_Bookingdate` |  |  |  |
| 16 | `PP.ST.ValueDateToken` | `PpPostingSetPds_Valuedatetoken` |  |  |  |
| 17 | `PP.ST.BookingCode` | `PpPostingSetPds_Bookingcode` |  |  |  |
| 18 | `PP.ST.SuppressZeroFlag` | `PpPostingSetPds_Suppresszeroflag` |  |  |  |
| 19 | `PP.ST.StatementFormat` | `PpPostingSetPds_Statementformat` |  |  |  |
| 20 | `PP.ST.RESERVED.5` | `PpPostingSetPds_Reserved5` | TField |  |  |
| 21 | `PP.ST.RESERVED.4` | `PpPostingSetPds_Reserved4` | TField |  |  |
| 22 | `PP.ST.RESERVED.3` | `PpPostingSetPds_Reserved3` | TField |  |  |
| 23 | `PP.ST.RESERVED.2` | `PpPostingSetPds_Reserved2` | TField |  |  |
| 24 | `PP.ST.RESERVED.1` | `PpPostingSetPds_Reserved1` | TField |  |  |
| 25 | `PP.ST.LOCAL.REF` | `PpPostingSetPds_LocalRef` |  |  |  |
| 26 | `PP.ST.LinkID` | `PpPostingSetPds_Linkid` | TField |  |  |
| 27 | `PP.ST.OVERRIDE` | `PpPostingSetPds_Override` |  |  |  |
| 28 | `PP.ST.RECORD.STATUS` | `PpPostingSetPds_RecordStatus` | String |  |  |
| 29 | `PP.ST.CURR.NO` | `PpPostingSetPds_CurrNo` | String |  |  |
| 30 | `PP.ST.INPUTTER` | `PpPostingSetPds_Inputter` |  |  |  |
| 31 | `PP.ST.DATE.TIME` | `PpPostingSetPds_DateTime` |  |  |  |
| 32 | `PP.ST.AUTHORISER` | `PpPostingSetPds_Authoriser` | String |  |  |
| 33 | `PP.ST.CO.CODE` | `PpPostingSetPds_CoCode` | String |  |  |
| 34 | `PP.ST.DEPT.CODE` | `PpPostingSetPds_DeptCode` | String |  |  |
| 35 | `PP.ST.AUDITOR.CODE` | `PpPostingSetPds_AuditorCode` | String |  |  |
| 36 | `PP.ST.AUDIT.DATE.TIME` | `PpPostingSetPds_AuditDateTime` | String |  |  |
