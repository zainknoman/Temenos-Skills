# CAPL.TX.FT4A.SLIPS — Table Schema

> Source: `INSERTS/I_F.CAPL.TX.FT4A.SLIPS` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `T4A.ID` | `CaplTxFt4aSlips_Id` | TField |  | The ID of the table is alphanemuric character will maximum length of 49.The id of the table will be customer number,portfolio id and year.E.g 100516-100516-1.2015 |
| 2 | `T4A.SLIP.YEAR` | `CaplTxFt4aSlips_SlipYear` | TField |  | The purpose of the field is to define the year for which the slip to be generated.Valid Year to be defined here. |
| 3 | `T4A.SLIP.NUMBER` | `CaplTxFt4aSlips_SlipNumber` | TField |  | The purpose of the field is to define the slip number for the slip.The slip number must be nemuric value with continuous series.Allowed values are 35 alphanemuric characters. |
| 4 | `T4A.SLIP.SEQ.NO` | `CaplTxFt4aSlips_SlipSeqNo` | TField |  | This field is used to define the number sequence allowed for slip number mentioned.Allowed values are 35 alphanemuric characters. |
| 5 | `T4A.CUSTOMER.1` | `CaplTxFt4aSlips_Customer1` | TField |  | The purpose of this field is used to specify the customer for the slip record.Valid record from CUSTOMER table. |
| 6 | `T4A.CUSTOMER.2` | `CaplTxFt4aSlips_Customer2` | TField |  | The purpose of this field is used to specify the customer for the slip record. This will capture the joint customer details, if any.Valid record from CUSTOMER table. |
| 7 | `T4A.COMPANY` | `CaplTxFt4aSlips_Company` | TField |  | The Field denotes the company to which the slip belongs.Valid record from COMPANY table. |
| 8 | `T4A.SLIP.PROCESS` | `CaplTxFt4aSlips_SlipProcess` | TField |  | This field is to capture the slip process, like Amend or original or cancel etc.Allowed Values are:AmendOriginalCancelDuplicate |
| 9 | `T4A.SLIP.AMENDED` | `CaplTxFt4aSlips_SlipAmended` | TField |  | This field denotes whether the slip is amended or not.Allowed values are Yes/No. |
| 10 | `T4A.AMEND.SEQ.NO` | `CaplTxFt4aSlips_AmendSeqNo` | TField |  | This field holds the slip amend sequence number for the xml generated. |
| 11 | `T4A.SLIP.DATE` | `CaplTxFt4aSlips_SlipDate` | TField |  | Field holds the date on which the slip was processed.Valid date to be stored. |
| 12 | `T4A.SLIP.USER` | `CaplTxFt4aSlips_SlipUser` | TField |  | The purpose of this field is used to define the user who generated the slip.Valid record from USER application.E.g. INPUTTER.. |
| 13 | `T4A.BOX.16` | `CaplTxFt4aSlips_Box16` | TField |  | Box 16 - This value indicates the amount of annuity paymentsValue for Box 24 will be fetched from AMOUNT.CODES.1 field from CAPL.H.TX.FORM.TYPE table. |
| 14 | `T4A.BOX.28` | `CaplTxFt4aSlips_Box28` | TField |  | Box 28 - The box indicates other income or deductionsValue for Box 24 will be fetched from AMOUNT.CODES.9 field from CAPL.H.TX.FORM.TYPE table. |
| 15 | `T4A.BOX.46` | `CaplTxFt4aSlips_Box46` | TField |  | This field is used to denote Charitable donations, if any |
| 16 | `T4A.BOX.18` | `CaplTxFt4aSlips_Box18` | TField |  | Box 16 - This value indicates the Refund of premiumsValue for Box 24 will be fetched from AMOUNT.CODES.2 field from CAPL.H.TX.FORM.TYPE table. |
| 17 | `T4A.BOX.30` | `CaplTxFt4aSlips_Box30` | TField |  | Box 30 - The amount which is deducted for income tax purpose, if the income tax is not deducted the box is left blank.Value for Box 30 will be fetched from AMOUNT.CODES.6 field from CAPL.H.TX.FORM.TYPE table. |
| 18 | `T4A.BOX.12` | `CaplTxFt4aSlips_Box12` | TField |  | Box 12 - The field denoted the SIN of the recipient.The value for this field os fetched from the CUSTOMER table. |
| 19 | `T4A.BOX.20` | `CaplTxFt4aSlips_Box20` | TField |  | This field is used to define the Box.20. Which will report the amount code for Refund of excess contributions amount.Value for Box 20 will be fetched from AMOUNT.CODES.1 field from CAPL.H.TX.FORM.TYPE table. |
| 20 | `T4A.BOX.32` | `CaplTxFt4aSlips_Box32` | TField |  | Box 32 - The field denoted the SIN of the recipient.The value for this field os fetched from the CUSTOMER table. |
| 21 | `T4A.BOX.38` | `CaplTxFt4aSlips_Box38` | TField |  | Box 38 - This box will fetch the SIN of the recipient to display in CRA.The value for this field os fetched from the CUSTOMER table. |
| 22 | `T4A.BOX.22` | `CaplTxFt4aSlips_Box22` | TField |  | This field is used to define the Box.22. Which will report the amount code for Withdrawal and commutation payments.Value for Box 22 will be fetched from AMOUNT.CODES.2 field from CAPL.H.TX.FORM.TYPE table. |
| 23 | `T4A.BOX.34` | `CaplTxFt4aSlips_Box34` | TField |  | Box 34 - The box indicates amounts deemed received on death.Value for Box 24 will be fetched from AMOUNT.CODES.8 field from CAPL.H.TX.FORM.TYPE table. |
| 24 | `T4A.BOX.13` | `CaplTxFt4aSlips_Box13` | TField |  | This field denotes the value from the Amount.1 field which will be displayed in the slip.Valid amount to be stores here. |
| 25 | `T4A.BOX.24` | `CaplTxFt4aSlips_Box24` | TField |  | Box 24 - A spousal or common-law partner in RRSPto which the annuitant's spouse contributed.Value for Box 24 will be fetched from AMOUNT.CODES.8 field from CAPL.H.TX.FORM.TYPE table. |
| 26 | `T4A.BOX.36` | `CaplTxFt4aSlips_Box36` | TField |  | Box 36 - This box will fetch the SIN of the recipient to display in CRA.The value for this field os fetched from the CUSTOMER table. |
| 27 | `T4A.BOX.14` | `CaplTxFt4aSlips_Box14` | TField |  | Box 14 - This will fetch the value of the contract number.Validated against the @id of the Plan number. |
| 28 | `T4A.BOX.26` | `CaplTxFt4aSlips_Box26` | TField |  | Box.26 - The value indicated whether the plan has second customer or not.The will capture Yes/No value in the slip. |
| 29 | `T4A.BOX.40` | `CaplTxFt4aSlips_Box40` | TField |  | This field is used to record the taxable benefit for the entire year. |
| 30 | `T4A.BOX.61` | `CaplTxFt4aSlips_Box61` | TField |  | Box 61 - The box indicates the business no to be display to CRA.The value is fetched from BUSINESS.NO field of CAPL.H.TX.FORM.TYPE table. |
| 31 | `T4A.BOX.27` | `CaplTxFt4aSlips_Box27` | TField |  | Box 27 -The amount withdrawn from an RRSP by an eligible individual participating in the Home Buyers' Plan (HBP).Value for Box 27 will be fetched from AMOUNT.CODES.5 field from CAPL.H.TX.FORM.TYPE table. |
| 32 | `T4A.BOX.42` | `CaplTxFt4aSlips_Box42` | TField |  |  |
| 33 | `T4A.BOX.35` | `CaplTxFt4aSlips_Box35` | TField |  | Box 35 - The amount transferred on breakdown of marriage orcommon-law partnership.Value for Box 35 will be fetched from AMOUNT.CODES.7 field from CAPL.H.TX.FORM.TYPE table. |
| 34 | `T4A.BOX.60` | `CaplTxFt4aSlips_Box60` | TField |  | Box 60 - The box indicates the full name of the RRSP payer. |
| 35 | `T4A.PAYOR.NAME` | `CaplTxFt4aSlips_PayorName` | TField |  | This field denotes the tax payor name for the slip |
| 36 | `T4A.YEAR` | `CaplTxFt4aSlips_Year` | TField |  | This field denotes the year which the slip was processed.Valid year to be defined here. |
| 37 | `T4A.BEN.NAME.1` | `CaplTxFt4aSlips_BenName1` | TField |  | This field is used to denote the customer name for the slip generation.Value will be fetched from CUSTOMER table. |
| 38 | `T4A.BEN.ADR.1` | `CaplTxFt4aSlips_BenAdr1` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 39 | `T4A.BEN.ADR.2` | `CaplTxFt4aSlips_BenAdr2` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 40 | `T4A.BEN.ADR.3` | `CaplTxFt4aSlips_BenAdr3` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 41 | `T4A.BEN.ADR.4` | `CaplTxFt4aSlips_BenAdr4` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 42 | `T4A.BEN.ADR.5` | `CaplTxFt4aSlips_BenAdr5` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 43 | `T4A.BEN.ADR.6` | `CaplTxFt4aSlips_BenAdr6` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 44 | `T4A.BEN.ADR.7` | `CaplTxFt4aSlips_BenAdr7` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 45 | `T4A.BEN.ADR.8` | `CaplTxFt4aSlips_BenAdr8` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 46 | `T4A.BEN.ADR.9` | `CaplTxFt4aSlips_BenAdr9` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 47 | `T4A.FOOTNOTE.EXPLANATION` | `CaplTxFt4aSlips_FootnoteExplanation` | TField |  |  |
| 48 | `T4A.PRINT.STATUS` | `CaplTxFt4aSlips_PrintStatus` | TField |  | This field holds the slip print status, which will store the slip has been Modified, reprinted,duplicate or amended. |
| 49 | `T4A.EXCL.CUST.FLAG` | `CaplTxFt4aSlips_ExclCustFlag` | TField |  | This field is to define whether the cust flag to be excluded or not for the receipt generation.Allowed values are Yes/No |
| 50 | `T4A.BAD.ADDRESS` | `CaplTxFt4aSlips_BadAddress` | TField |  | Field is to map the bad address to de.address of xml.1 and print.1If the bad address is set to YES, then the return mail in DE.ADDRESS will be updated to Yes.Allowed values are Yes/No |
| 51 | `T4A.RECORD.STATUS` | `CaplTxFt4aSlips_RecordStatus` | String |  |  |
| 52 | `T4A.CURR.NO` | `CaplTxFt4aSlips_CurrNo` | String |  |  |
| 53 | `T4A.INPUTTER` | `CaplTxFt4aSlips_Inputter` |  |  |  |
| 54 | `T4A.DATE.TIME` | `CaplTxFt4aSlips_DateTime` |  |  |  |
| 55 | `T4A.AUTHORISER` | `CaplTxFt4aSlips_Authoriser` | String |  |  |
| 56 | `T4A.CO.CODE` | `CaplTxFt4aSlips_CoCode` | String |  |  |
| 57 | `T4A.DEPT.CODE` | `CaplTxFt4aSlips_DeptCode` | String |  |  |
| 58 | `T4A.AUDITOR.CODE` | `CaplTxFt4aSlips_AuditorCode` | String |  |  |
| 59 | `T4A.AUDIT.DATE.TIME` | `CaplTxFt4aSlips_AuditDateTime` | String |  |  |
