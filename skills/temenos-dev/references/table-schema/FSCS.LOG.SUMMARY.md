# FSCS.LOG.SUMMARY — Table Schema

> Source: `INSERTS/I_F.FSCS.LOG.SUMMARY` in `UKFSCS_Reporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FSCS.SUMMARY.DATE` | `FscsLogSummary_Date` | TField |  | This field contains today's date. |
| 2 | `FSCS.SUMMARY.CLASSIFICATION` | `FscsLogSummary_Classification` | TField |  | This Field will have only either of the two values - SCV EXCLUSION |
| 3 | `FSCS.SUMMARY.TOTAL.CUSTOMER.COUNT` | `FscsLogSummary_TotalCustomerCount` | TField |  | This Field will contain the Total Number of Customers as a part of the FSCS Reporting who fall into either SCV / EXCLUSION |
| 4 | `FSCS.SUMMARY.TOTAL.ACCOUNTS.COUNT` | `FscsLogSummary_TotalAccountsCount` | TField |  | This Field will contain the Total Number of Accounts as a part of the FSCS Reporting who fall into either SCV / EXCLUSION |
| 5 | `FSCS.SUMMARY.BALANCE.WITH.INTEREST` | `FscsLogSummary_BalanceWithInterest` | TField |  | This Field will contain the Total Balance of all Accounts FSCS Reporting who fall into either SCV / EXCLUSION based on the field 'Account Balances in Sterling' |
| 6 | `FSCS.SUMMARY.BALANCE.WITHOUT.INTEREST` | `FscsLogSummary_BalanceWithoutInterest` | TField |  | This Field will contain the Total Balance of all Accounts FSCS Reporting who fall into either SCV / EXCLUSION based on the field 'Original Account Balance Before Interest' |
| 7 | `FSCS.SUMMARY.PRIORITY` | `FscsLogSummary_Priority` | TField |  | This Field will be used to define the priority of the classification. |
| 8 | `FSCS.SUMMARY.RESERVED.10` | `FscsLogSummary_Reserved10` | TField |  |  |
| 9 | `FSCS.SUMMARY.RESERVED.9` | `FscsLogSummary_Reserved9` | TField |  |  |
| 10 | `FSCS.SUMMARY.RESERVED.8` | `FscsLogSummary_Reserved8` | TField |  |  |
| 11 | `FSCS.SUMMARY.RESERVED.7` | `FscsLogSummary_Reserved7` | TField |  |  |
| 12 | `FSCS.SUMMARY.RESERVED.6` | `FscsLogSummary_Reserved6` | TField |  |  |
| 13 | `FSCS.SUMMARY.RESERVED.5` | `FscsLogSummary_Reserved5` | TField |  |  |
| 14 | `FSCS.SUMMARY.RESERVED.4` | `FscsLogSummary_Reserved4` | TField |  |  |
| 15 | `FSCS.SUMMARY.RESERVED.3` | `FscsLogSummary_Reserved3` | TField |  |  |
| 16 | `FSCS.SUMMARY.RESERVED.2` | `FscsLogSummary_Reserved2` | TField |  |  |
| 17 | `FSCS.SUMMARY.RESERVED.1` | `FscsLogSummary_Reserved1` | TField |  |  |
