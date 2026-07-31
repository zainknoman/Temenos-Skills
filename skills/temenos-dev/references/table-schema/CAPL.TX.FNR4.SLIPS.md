# CAPL.TX.FNR4.SLIPS — Table Schema

> Source: `INSERTS/I_F.CAPL.TX.FNR4.SLIPS` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NR4.SLIP.ID` | `CaplTxFnr4Slips_SlipId` | TField |  | This field is to store the slip id, which will be similar to the @id.E.g. 100006.CA.27 |
| 2 | `NR4.SLIP.YEAR` | `CaplTxFnr4Slips_SlipYear` | TField |  | The purpose of the field is to define the year for which the slip to be generated.Valid Year to be defined here. |
| 3 | `NR4.SLIP.NUMBER` | `CaplTxFnr4Slips_SlipNumber` | TField |  | The purpose of the field is to define the slip number for the slip.The slip number must be nemuric value with continuous series.Allowed values are 35 alphanemuric characters. |
| 4 | `NR4.SLIP.SEQ.NO` | `CaplTxFnr4Slips_SlipSeqNo` | TField |  | This field is used to define the number sequence allowed for slip number mentioned.Allowed values are 35 alphanemuric characters. |
| 5 | `NR4.CUSTOMER.1` | `CaplTxFnr4Slips_Customer1` | TField |  |  |
| 6 | `NR4.CUSTOMER.2` | `CaplTxFnr4Slips_Customer2` | TField |  |  |
| 7 | `NR4.COMPANY` | `CaplTxFnr4Slips_Company` | TField |  | The Field denotes the company to which the slip belongs.Valid record from COMPANY table. |
| 8 | `NR4.SLIP.PROCESS` | `CaplTxFnr4Slips_SlipProcess` | TField |  | This field is to capture the slip process, like Amend or original or cancel etc.Allowed Values are:AmendOriginalCancelDuplicate |
| 9 | `NR4.SLIP.AMENDED` | `CaplTxFnr4Slips_SlipAmended` | TField |  | This field denotes whether the slip is amended or not.Allowed values are Yes/No. |
| 10 | `NR4.AMEND.SEQ.NO` | `CaplTxFnr4Slips_AmendSeqNo` | TField |  | This field holds the slip amend sequence number for the xml generated. |
| 11 | `NR4.SLIP.DATE` | `CaplTxFnr4Slips_SlipDate` | TField |  | Field holds the date on which the slip was processed.Valid date to be stored. |
| 12 | `NR4.SLIP.USER` | `CaplTxFnr4Slips_SlipUser` | TField |  | The purpose of this field is used to define the user who generated the slip.Valid record from USER application.E.g. INPUTTER.. |
| 13 | `NR4.AMOUNT.1` | `CaplTxFnr4Slips_Amount1` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 14 | `NR4.AMOUNT.2` | `CaplTxFnr4Slips_Amount2` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 15 | `NR4.AMOUNT.3` | `CaplTxFnr4Slips_Amount3` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 16 | `NR4.AMOUNT.4` | `CaplTxFnr4Slips_Amount4` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 17 | `NR4.AMOUNT.5` | `CaplTxFnr4Slips_Amount5` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 18 | `NR4.AMOUNT.6` | `CaplTxFnr4Slips_Amount6` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 19 | `NR4.BOX.10` | `CaplTxFnr4Slips_Box10` | TField |  | This field is used to denote year in which the payment was made to the recipient.Valid year to be defined here. |
| 20 | `NR4.BOX.11` | `CaplTxFnr4Slips_Box11` | TField |  | This field is used to denote the recipient code to be displayed in the xml.Valid receipt code to be displayed here.E.g1 - Individual2- Joint account. |
| 21 | `NR4.BOX.12` | `CaplTxFnr4Slips_Box12` | TField |  | Box 12 - The field denoted the SIN of the recipient.The value for this field os fetched from the CUSTOMER table. |
| 22 | `NR4.BOX.13` | `CaplTxFnr4Slips_Box13` | TField |  | This field denotes the value from the Amount.1 field which will be displayed in the slip.Valid amount to be stores here. |
| 23 | `NR4.BOX.14` | `CaplTxFnr4Slips_Box14` | TField |  | Box 14 - This will fetch the value of the contract number.Validated against the @id of the Plan number. |
| 24 | `NR4.BOX.15` | `CaplTxFnr4Slips_Box15` | TField |  | This field denotes the all the incomes and withholding tax which are reported in cancdian funds. |
| 25 | `NR4.BOX.16` | `CaplTxFnr4Slips_Box16` | TField |  | Box 16 - This value indicates the amount of annuity paymentsValue for Box 24 will be fetched from AMOUNT.CODES.1 field from CAPL.H.TX.FORM.TYPE table. |
| 26 | `NR4.BOX.17` | `CaplTxFnr4Slips_Box17` | TField |  | This field is to denote the with held tax for non resident on canadian funds. |
| 27 | `NR4.BOX.18` | `CaplTxFnr4Slips_Box18` | TField |  | Box 18 - The amount you paid from an unmatured RRSP to the spouse or common-law partner of the RRSP annuitant, when the annuitant is deseased.Value for Box 18 will be fetched from AMOUNT.CODES.4 field from CAPL.H.TX.FORM.TYPE table. |
| 28 | `NR4.BOX.24` | `CaplTxFnr4Slips_Box24` | TField |  | Box 24 - A spousal or common-law partner in RRSPto which the annuitant's spouse contributed.Value for Box 24 will be fetched from AMOUNT.CODES.8 field from CAPL.H.TX.FORM.TYPE table. |
| 29 | `NR4.BOX.25` | `CaplTxFnr4Slips_Box25` | TField |  | Box 25 - the amount withdrawn from RRSP by an eligible individual participating in the Lifelong Learning Plan (LLP).Value for Box 25 will be fetched from AMOUNT.CODES.3 field from CAPL.H.TX.FORM.TYPE table. |
| 30 | `NR4.BOX.26` | `CaplTxFnr4Slips_Box26` | TField |  | Box.26 - The value indicated whether the plan has second customer or not.The will capture Yes/No value in the slip. |
| 31 | `NR4.BOX.27` | `CaplTxFnr4Slips_Box27` | TField |  | Box 27 -The amount withdrawn from an RRSP by an eligible individual participating in the Home Buyers' Plan (HBP).Value for Box 27 will be fetched from AMOUNT.CODES.5 field from CAPL.H.TX.FORM.TYPE table. |
| 32 | `NR4.BOX.28` | `CaplTxFnr4Slips_Box28` | TField |  | Box 28 - The box indicates other income or deductionsValue for Box 24 will be fetched from AMOUNT.CODES.9 field from CAPL.H.TX.FORM.TYPE table. |
| 33 | `NR4.BEN.NAME.1` | `CaplTxFnr4Slips_BenName1` | TField |  | This field is used to denote the customer name for the slip generation.Value will be fetched from CUSTOMER table. |
| 34 | `NR4.BEN.NAME.2` | `CaplTxFnr4Slips_BenName2` | TField |  | This field is used to denote the customer name for the slip generation.Value will be fetched from CUSTOMER table. |
| 35 | `NR4.BEN.ADR.1` | `CaplTxFnr4Slips_BenAdr1` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 36 | `NR4.BEN.ADR.2` | `CaplTxFnr4Slips_BenAdr2` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 37 | `NR4.BEN.ADR.3` | `CaplTxFnr4Slips_BenAdr3` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 38 | `NR4.BEN.ADR.4` | `CaplTxFnr4Slips_BenAdr4` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 39 | `NR4.BEN.ADR.5` | `CaplTxFnr4Slips_BenAdr5` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 40 | `NR4.BEN.ADR.6` | `CaplTxFnr4Slips_BenAdr6` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 41 | `NR4.BEN.ADR.7` | `CaplTxFnr4Slips_BenAdr7` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 42 | `NR4.BEN.ADR.8` | `CaplTxFnr4Slips_BenAdr8` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 43 | `NR4.BEN.ADR.9` | `CaplTxFnr4Slips_BenAdr9` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 44 | `NR4.BANK.NAME` | `CaplTxFnr4Slips_BankName` | TField |  | This field holds the bank name to be displaued on the tax slip.Valid bank name to be stored here. |
| 45 | `NR4.BANK.ADR.1` | `CaplTxFnr4Slips_BankAdr1` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 46 | `NR4.BANK.ADR.2` | `CaplTxFnr4Slips_BankAdr2` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 47 | `NR4.BANK.ADR.3` | `CaplTxFnr4Slips_BankAdr3` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 48 | `NR4.BANK.ADR.4` | `CaplTxFnr4Slips_BankAdr4` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 49 | `NR4.BANK.ADR.5` | `CaplTxFnr4Slips_BankAdr5` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 50 | `NR4.BANK.ADR.6` | `CaplTxFnr4Slips_BankAdr6` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 51 | `NR4.BANK.ADR.7` | `CaplTxFnr4Slips_BankAdr7` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 52 | `NR4.BANK.ADR.8` | `CaplTxFnr4Slips_BankAdr8` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 53 | `NR4.BANK.ADR.9` | `CaplTxFnr4Slips_BankAdr9` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 54 | `NR4.NR.ACCOUNT` | `CaplTxFnr4Slips_NrAccount` | TField |  |  |
| 55 | `NR4.COUNTRY.CODE` | `CaplTxFnr4Slips_CountryCode` | TField |  |  |
| 56 | `NR4.PRINT.STATUS` | `CaplTxFnr4Slips_PrintStatus` | TField |  |  |
| 57 | `NR4.EXCL.CUST.FLAG` | `CaplTxFnr4Slips_ExclCustFlag` | TField |  |  |
| 58 | `NR4.BAD.ADDRESS` | `CaplTxFnr4Slips_BadAddress` | TField |  | Field is to map the bad address to de.address of xml.1 and print.1If the bad address is set to YES, then the return mail in DE.ADDRESS will be updated to Yes.Allowed values are Yes/No |
| 59 | `NR4.RECORD.STATUS` | `CaplTxFnr4Slips_RecordStatus` | String |  |  |
| 60 | `NR4.CURR.NO` | `CaplTxFnr4Slips_CurrNo` | String |  |  |
| 61 | `NR4.INPUTTER` | `CaplTxFnr4Slips_Inputter` |  |  |  |
| 62 | `NR4.DATE.TIME` | `CaplTxFnr4Slips_DateTime` |  |  |  |
| 63 | `NR4.AUTHORISER` | `CaplTxFnr4Slips_Authoriser` | String |  |  |
| 64 | `NR4.CO.CODE` | `CaplTxFnr4Slips_CoCode` | String |  |  |
| 65 | `NR4.DEPT.CODE` | `CaplTxFnr4Slips_DeptCode` | String |  |  |
| 66 | `NR4.AUDITOR.CODE` | `CaplTxFnr4Slips_AuditorCode` | String |  |  |
| 67 | `NR4.AUDIT.DATE.TIME` | `CaplTxFnr4Slips_AuditDateTime` | String |  |  |
