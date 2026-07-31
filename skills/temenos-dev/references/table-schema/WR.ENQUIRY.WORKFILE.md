# WR.ENQUIRY.WORKFILE — Table Schema

> Source: `INSERTS/I_F.WR.ENQUIRY.WORKFILE` in `WR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `WR.ENQWK.SAM.NO` | `WrEnquiryWorkfile_SamNo` | TField |  | Selection Field value as input into enquiry (if used): Sam No |
| 2 | `WR.ENQWK.PORTFOLIO` | `WrEnquiryWorkfile_Portfolio` | TField |  | Selection Field value as input into enquiry (if used): Portfolio |
| 3 | `WR.ENQWK.ACCOUNT.NUMBER` | `WrEnquiryWorkfile_AccountNumber` | TField |  | Selection Field value as input into enquiry (if used): Account Number |
| 4 | `WR.ENQWK.WR.REPORTING` | `WrEnquiryWorkfile_WrReporting` | TField |  | Selection Field value as input into enquiry (if used): Wr Reporting |
| 5 | `WR.ENQWK.START.DATE` | `WrEnquiryWorkfile_StartDate` | TField |  | Selection Field value as input into enquiry (if used): Start Date |
| 6 | `WR.ENQWK.END.DATE` | `WrEnquiryWorkfile_EndDate` | TField |  | Selection Field value as input into enquiry (if used): End Date |
| 7 | `WR.ENQWK.EXTRACT.DATE` | `WrEnquiryWorkfile_ExtractDate` | TField |  | Selection Field value as input into enquiry (if used): Extract Date |
| 8 | `WR.ENQWK.BOOKING.DATE` | `WrEnquiryWorkfile_BookingDate` | TField |  | Selection Field value as input into enquiry (if used): Booking Date |
| 9 | `WR.ENQWK.CUSTOMER.NO` | `WrEnquiryWorkfile_CustomerNo` | TField |  | Selection Field value as input into enquiry (if used): Customer No |
| 10 | `WR.ENQWK.GROUP.NO` | `WrEnquiryWorkfile_GroupNo` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 11 | `WR.ENQWK.RESERVED.03` | `WrEnquiryWorkfile_Reserved03` | TField |  |  |
| 12 | `WR.ENQWK.RESERVED.02` | `WrEnquiryWorkfile_Reserved02` | TField |  |  |
| 13 | `WR.ENQWK.RESERVED.01` | `WrEnquiryWorkfile_Reserved01` | TField |  |  |
| 14 | `WR.ENQWK.SEQ` | `WrEnquiryWorkfile_Seq` | TField |  | For a detail record, this is the row number of the array returned from the NOFILE routine that this record represents. For a header record, this is the total number of rows that were returned within the array from the NOFILE routine. |
| 15 | `WR.ENQWK.F.001` | `WrEnquiryWorkfile_F001` | TField |  | data row - element 1 (see enquiry for details) |
| 16 | `WR.ENQWK.F.002` | `WrEnquiryWorkfile_F002` | TField |  | data row - element 2 (see enquiry for details) |
| 17 | `WR.ENQWK.F.003` | `WrEnquiryWorkfile_F003` | TField |  | data row - element 3 (see enquiry for details) |
| 18 | `WR.ENQWK.F.004` | `WrEnquiryWorkfile_F004` | TField |  | data row - element 4 (see enquiry for details) |
| 19 | `WR.ENQWK.F.005` | `WrEnquiryWorkfile_F005` | TField |  | data row - element 5 (see enquiry for details) |
| 20 | `WR.ENQWK.F.006` | `WrEnquiryWorkfile_F006` | TField |  | data row - element 6 (see enquiry for details) |
| 21 | `WR.ENQWK.F.007` | `WrEnquiryWorkfile_F007` | TField |  | data row - element 7 (see enquiry for details) |
| 22 | `WR.ENQWK.F.008` | `WrEnquiryWorkfile_F008` | TField |  | data row - element 8 (see enquiry for details) |
| 23 | `WR.ENQWK.F.009` | `WrEnquiryWorkfile_F009` | TField |  | data row - element 9 (see enquiry for details) |
| 24 | `WR.ENQWK.F.010` | `WrEnquiryWorkfile_F010` | TField |  | data row - element 10 (see enquiry for details) |
| 25 | `WR.ENQWK.F.011` | `WrEnquiryWorkfile_F011` | TField |  | data row - element 11 (see enquiry for details) |
| 26 | `WR.ENQWK.F.012` | `WrEnquiryWorkfile_F012` | TField |  | data row - element 12 (see enquiry for details) |
| 27 | `WR.ENQWK.F.013` | `WrEnquiryWorkfile_F013` | TField |  | data row - element 13 (see enquiry for details) |
| 28 | `WR.ENQWK.F.014` | `WrEnquiryWorkfile_F014` | TField |  | data row - element 14 (see enquiry for details) |
| 29 | `WR.ENQWK.F.015` | `WrEnquiryWorkfile_F015` | TField |  | data row - element 15 (see enquiry for details) |
| 30 | `WR.ENQWK.F.016` | `WrEnquiryWorkfile_F016` | TField |  | data row - element 16 (see enquiry for details) |
| 31 | `WR.ENQWK.F.017` | `WrEnquiryWorkfile_F017` | TField |  | data row - element 17 (see enquiry for details) |
| 32 | `WR.ENQWK.F.018` | `WrEnquiryWorkfile_F018` | TField |  | data row - element 18 (see enquiry for details) |
| 33 | `WR.ENQWK.F.019` | `WrEnquiryWorkfile_F019` | TField |  | data row - element 19 (see enquiry for details) |
| 34 | `WR.ENQWK.F.020` | `WrEnquiryWorkfile_F020` | TField |  | data row - element 20 (see enquiry for details) |
| 35 | `WR.ENQWK.F.021` | `WrEnquiryWorkfile_F021` | TField |  | data row - element 21 (see enquiry for details) |
| 36 | `WR.ENQWK.F.022` | `WrEnquiryWorkfile_F022` | TField |  | data row - element 22 (see enquiry for details) |
| 37 | `WR.ENQWK.F.023` | `WrEnquiryWorkfile_F023` | TField |  | data row - element 23 (see enquiry for details) |
| 38 | `WR.ENQWK.F.024` | `WrEnquiryWorkfile_F024` | TField |  | data row - element 24 (see enquiry for details) |
| 39 | `WR.ENQWK.F.025` | `WrEnquiryWorkfile_F025` | TField |  | data row - element 25 (see enquiry for details) |
| 40 | `WR.ENQWK.F.026` | `WrEnquiryWorkfile_F026` | TField |  | data row - element 26 (see enquiry for details) |
| 41 | `WR.ENQWK.F.027` | `WrEnquiryWorkfile_F027` | TField |  | data row - element 27 (see enquiry for details) |
| 42 | `WR.ENQWK.F.028` | `WrEnquiryWorkfile_F028` | TField |  | data row - element 28 (see enquiry for details) |
| 43 | `WR.ENQWK.F.029` | `WrEnquiryWorkfile_F029` | TField |  | data row - element 29 (see enquiry for details) |
| 44 | `WR.ENQWK.F.030` | `WrEnquiryWorkfile_F030` | TField |  | data row - element 30 (see enquiry for details) |
| 45 | `WR.ENQWK.F.031` | `WrEnquiryWorkfile_F031` | TField |  | data row - element 31 (see enquiry for details) |
| 46 | `WR.ENQWK.F.032` | `WrEnquiryWorkfile_F032` | TField |  | data row - element 32 (see enquiry for details) |
| 47 | `WR.ENQWK.F.033` | `WrEnquiryWorkfile_F033` | TField |  | data row - element 33 (see enquiry for details) |
| 48 | `WR.ENQWK.F.034` | `WrEnquiryWorkfile_F034` | TField |  | data row - element 34 (see enquiry for details) |
| 49 | `WR.ENQWK.F.035` | `WrEnquiryWorkfile_F035` | TField |  | data row - element 35 (see enquiry for details) |
| 50 | `WR.ENQWK.F.036` | `WrEnquiryWorkfile_F036` | TField |  | data row - element 36 (see enquiry for details) |
| 51 | `WR.ENQWK.F.037` | `WrEnquiryWorkfile_F037` | TField |  | data row - element 37 (see enquiry for details) |
| 52 | `WR.ENQWK.F.038` | `WrEnquiryWorkfile_F038` | TField |  | data row - element 38 (see enquiry for details) |
| 53 | `WR.ENQWK.F.039` | `WrEnquiryWorkfile_F039` | TField |  | data row - element 39 (see enquiry for details) |
| 54 | `WR.ENQWK.F.040` | `WrEnquiryWorkfile_F040` | TField |  | data row - element 40 (see enquiry for details) |
| 55 | `WR.ENQWK.F.041` | `WrEnquiryWorkfile_F041` | TField |  | data row - element 41 (see enquiry for details) |
| 56 | `WR.ENQWK.F.042` | `WrEnquiryWorkfile_F042` | TField |  | data row - element 42 (see enquiry for details) |
| 57 | `WR.ENQWK.F.043` | `WrEnquiryWorkfile_F043` | TField |  | data row - element 43 (see enquiry for details) |
| 58 | `WR.ENQWK.F.044` | `WrEnquiryWorkfile_F044` | TField |  | data row - element 44 (see enquiry for details) |
| 59 | `WR.ENQWK.F.045` | `WrEnquiryWorkfile_F045` | TField |  | data row - element 45 (see enquiry for details) |
| 60 | `WR.ENQWK.F.046` | `WrEnquiryWorkfile_F046` | TField |  | data row - element 46 (see enquiry for details) |
| 61 | `WR.ENQWK.F.047` | `WrEnquiryWorkfile_F047` | TField |  | data row - element 47 (see enquiry for details) |
| 62 | `WR.ENQWK.F.048` | `WrEnquiryWorkfile_F048` | TField |  | data row - element 48 (see enquiry for details) |
| 63 | `WR.ENQWK.F.049` | `WrEnquiryWorkfile_F049` | TField |  | data row - element 49 (see enquiry for details) |
| 64 | `WR.ENQWK.F.050` | `WrEnquiryWorkfile_F050` | TField |  | data row - element 50 (see enquiry for details) |
| 65 | `WR.ENQWK.F.051` | `WrEnquiryWorkfile_F051` | TField |  | data row - element 51 (see enquiry for details) |
| 66 | `WR.ENQWK.F.052` | `WrEnquiryWorkfile_F052` | TField |  | data row - element 52 (see enquiry for details) |
| 67 | `WR.ENQWK.F.053` | `WrEnquiryWorkfile_F053` | TField |  | data row - element 53 (see enquiry for details) |
| 68 | `WR.ENQWK.F.054` | `WrEnquiryWorkfile_F054` | TField |  | data row - element 54 (see enquiry for details) |
| 69 | `WR.ENQWK.F.055` | `WrEnquiryWorkfile_F055` | TField |  | data row - element 55 (see enquiry for details) |
| 70 | `WR.ENQWK.F.056` | `WrEnquiryWorkfile_F056` | TField |  | data row - element 56 (see enquiry for details) |
| 71 | `WR.ENQWK.F.057` | `WrEnquiryWorkfile_F057` | TField |  | data row - element 57 (see enquiry for details) |
| 72 | `WR.ENQWK.F.058` | `WrEnquiryWorkfile_F058` | TField |  | data row - element 58 (see enquiry for details) |
| 73 | `WR.ENQWK.F.059` | `WrEnquiryWorkfile_F059` | TField |  | data row - element 59 (see enquiry for details) |
| 74 | `WR.ENQWK.F.060` | `WrEnquiryWorkfile_F060` | TField |  | data row - element 60 (see enquiry for details) |
| 75 | `WR.ENQWK.F.061` | `WrEnquiryWorkfile_F061` | TField |  | data row - element 61 (see enquiry for details) |
| 76 | `WR.ENQWK.F.062` | `WrEnquiryWorkfile_F062` | TField |  | data row - element 62 (see enquiry for details) |
| 77 | `WR.ENQWK.F.063` | `WrEnquiryWorkfile_F063` | TField |  | data row - element 63 (see enquiry for details) |
| 78 | `WR.ENQWK.F.064` | `WrEnquiryWorkfile_F064` | TField |  | data row - element 64 (see enquiry for details) |
| 79 | `WR.ENQWK.F.065` | `WrEnquiryWorkfile_F065` | TField |  | data row - element 65 (see enquiry for details) |
| 80 | `WR.ENQWK.F.066` | `WrEnquiryWorkfile_F066` | TField |  | data row - element 66 (see enquiry for details) |
| 81 | `WR.ENQWK.F.067` | `WrEnquiryWorkfile_F067` | TField |  | data row - element 67 (see enquiry for details) |
| 82 | `WR.ENQWK.F.068` | `WrEnquiryWorkfile_F068` | TField |  | data row - element 68 (see enquiry for details) |
| 83 | `WR.ENQWK.F.069` | `WrEnquiryWorkfile_F069` | TField |  | data row - element 69 (see enquiry for details) |
| 84 | `WR.ENQWK.F.070` | `WrEnquiryWorkfile_F070` | TField |  | data row - element 70 (see enquiry for details) |
| 85 | `WR.ENQWK.F.071` | `WrEnquiryWorkfile_F071` | TField |  | data row - element 71 (see enquiry for details) |
| 86 | `WR.ENQWK.F.072` | `WrEnquiryWorkfile_F072` | TField |  | data row - element 72 (see enquiry for details) |
| 87 | `WR.ENQWK.F.073` | `WrEnquiryWorkfile_F073` | TField |  | data row - element 73 (see enquiry for details) |
| 88 | `WR.ENQWK.F.074` | `WrEnquiryWorkfile_F074` | TField |  | data row - element 74 (see enquiry for details) |
| 89 | `WR.ENQWK.F.075` | `WrEnquiryWorkfile_F075` | TField |  | data row - element 75 (see enquiry for details) |
| 90 | `WR.ENQWK.F.076` | `WrEnquiryWorkfile_F076` | TField |  | data row - element 76 (see enquiry for details) |
| 91 | `WR.ENQWK.F.077` | `WrEnquiryWorkfile_F077` | TField |  | data row - element 77 (see enquiry for details) |
| 92 | `WR.ENQWK.F.078` | `WrEnquiryWorkfile_F078` | TField |  | data row - element 78 (see enquiry for details) |
| 93 | `WR.ENQWK.F.079` | `WrEnquiryWorkfile_F079` | TField |  | data row - element 79 (see enquiry for details) |
| 94 | `WR.ENQWK.F.080` | `WrEnquiryWorkfile_F080` | TField |  | data row - element 80 (see enquiry for details) |
| 95 | `WR.ENQWK.F.081` | `WrEnquiryWorkfile_F081` | TField |  | data row - element 81 (see enquiry for details) |
| 96 | `WR.ENQWK.F.082` | `WrEnquiryWorkfile_F082` | TField |  | data row - element 82 (see enquiry for details) |
| 97 | `WR.ENQWK.F.083` | `WrEnquiryWorkfile_F083` | TField |  | data row - element 83 (see enquiry for details) |
| 98 | `WR.ENQWK.F.084` | `WrEnquiryWorkfile_F084` | TField |  | data row - element 84 (see enquiry for details) |
| 99 | `WR.ENQWK.F.085` | `WrEnquiryWorkfile_F085` | TField |  | data row - element 85 (see enquiry for details) |
| 100 | `WR.ENQWK.F.086` | `WrEnquiryWorkfile_F086` | TField |  | data row - element 86 (see enquiry for details) |
| 101 | `WR.ENQWK.F.087` | `WrEnquiryWorkfile_F087` | TField |  | data row - element 87 (see enquiry for details) |
| 102 | `WR.ENQWK.F.088` | `WrEnquiryWorkfile_F088` | TField |  | data row - element 88 (see enquiry for details) |
| 103 | `WR.ENQWK.F.089` | `WrEnquiryWorkfile_F089` | TField |  | data row - element 89 (see enquiry for details) |
| 104 | `WR.ENQWK.F.090` | `WrEnquiryWorkfile_F090` | TField |  | data row - element 90 (see enquiry for details) |
| 105 | `WR.ENQWK.F.091` | `WrEnquiryWorkfile_F091` | TField |  | data row - element 91 (see enquiry for details) |
| 106 | `WR.ENQWK.F.092` | `WrEnquiryWorkfile_F092` | TField |  | data row - element 92 (see enquiry for details) |
| 107 | `WR.ENQWK.F.093` | `WrEnquiryWorkfile_F093` | TField |  | data row - element 93 (see enquiry for details) |
| 108 | `WR.ENQWK.F.094` | `WrEnquiryWorkfile_F094` | TField |  | data row - element 94 (see enquiry for details) |
| 109 | `WR.ENQWK.F.095` | `WrEnquiryWorkfile_F095` | TField |  | data row - element 95 (see enquiry for details) |
| 110 | `WR.ENQWK.F.096` | `WrEnquiryWorkfile_F096` | TField |  | data row - element 96 (see enquiry for details) |
| 111 | `WR.ENQWK.F.097` | `WrEnquiryWorkfile_F097` | TField |  | data row - element 97 (see enquiry for details) |
| 112 | `WR.ENQWK.F.098` | `WrEnquiryWorkfile_F098` | TField |  | data row - element 98 (see enquiry for details) |
| 113 | `WR.ENQWK.F.099` | `WrEnquiryWorkfile_F099` | TField |  | data row - element 99 (see enquiry for details) |
| 114 | `WR.ENQWK.F.100` | `WrEnquiryWorkfile_F100` | TField |  | data row - element 100 (see enquiry for details) |
