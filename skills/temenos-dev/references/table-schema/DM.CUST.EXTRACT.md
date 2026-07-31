# DM.CUST.EXTRACT — Table Schema

> Source: `INSERTS/I_F.DM.CUST.EXTRACT` in `DM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DM.CUS.CUST.ID` | `DmCustExtract_CustId` | TField |  |  |
| 2 | `DM.CUS.CUST.NAME` | `DmCustExtract_CustName` | TField |  |  |
| 3 | `DM.CUS.CUST.SHORT.NAME` | `DmCustExtract_CustShortName` | TField |  |  |
| 4 | `DM.CUS.CUST.NAME.ALIAS` | `DmCustExtract_CustNameAlias` | TField |  |  |
| 5 | `DM.CUS.DOC.TYPE` | `DmCustExtract_DocType` | TField |  |  |
| 6 | `DM.CUS.EXPIRY.DATE` | `DmCustExtract_ExpiryDate` | TField |  |  |
| 7 | `DM.CUS.GRACE.PERIOD` | `DmCustExtract_GracePeriod` | TField |  |  |
| 8 | `DM.CUS.RESTRICTION.DATE` | `DmCustExtract_RestrictionDate` | TField |  |  |
| 9 | `DM.CUS.ALERT.SENT` | `DmCustExtract_AlertSent` | TField |  |  |
| 10 | `DM.CUS.POSTING.RESTRICT` | `DmCustExtract_PostingRestrict` | TField |  |  |
| 11 | `DM.CUS.TYPE` | `DmCustExtract_Type` | TField |  |  |
| 12 | `DM.CUS.CUST.RESTRICTION.PLACED` | `DmCustExtract_CustRestrictionPlaced` | TField |  |  |
| 13 | `DM.CUS.ACCOUNT.NO` | `DmCustExtract_AccountNo` |  |  |  |
| 14 | `DM.CUS.ACCT.RESTRICTION.PLACED` | `DmCustExtract_AcctRestrictionPlaced` |  |  |  |
| 15 | `DM.CUS.RESERVED.10` | `DmCustExtract_Reserved10` | TField |  |  |
| 16 | `DM.CUS.RESERVED.9` | `DmCustExtract_Reserved9` | TField |  |  |
| 17 | `DM.CUS.RESERVED.8` | `DmCustExtract_Reserved8` | TField |  |  |
| 18 | `DM.CUS.RESERVED.7` | `DmCustExtract_Reserved7` | TField |  |  |
| 19 | `DM.CUS.RESERVED.6` | `DmCustExtract_Reserved6` | TField |  |  |
| 20 | `DM.CUS.RESERVED.5` | `DmCustExtract_Reserved5` | TField |  |  |
| 21 | `DM.CUS.RESERVED.4` | `DmCustExtract_Reserved4` | TField |  |  |
| 22 | `DM.CUS.RESERVED.3` | `DmCustExtract_Reserved3` | TField |  |  |
| 23 | `DM.CUS.RESERVED.2` | `DmCustExtract_Reserved2` | TField |  |  |
| 24 | `DM.CUS.RESERVED.1` | `DmCustExtract_Reserved1` | TField |  |  |
