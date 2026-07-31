# CAPL.TX.FT4RIF.SLIPS — Table Schema

> Source: `INSERTS/I_F.CAPL.TX.FT4RIF.SLIPS` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `T4RIF.ID` | `CaplTxFt4rifSlips_Id` |  |  |  |
| 2 | `T4RIF.SLIP.YEAR` | `CaplTxFt4rifSlips_SlipYear` | TField |  | The purpose of the field is to define the year for which the slip to be generated.Valid Year to be defined here. |
| 3 | `T4RIF.SLIP.NUMBER` | `CaplTxFt4rifSlips_SlipNumber` | TField |  | The purpose of the field is to define the slip number for the slip.The slip number must be nemuric value with continuous series.Allowed values are 35 alphanemuric characters. |
| 4 | `T4RIF.SLIP.SEQ.NO` | `CaplTxFt4rifSlips_SlipSeqNo` | TField |  | This field is used to define the number sequence allowed for slip number mentioned.Allowed values are 35 alphanemuric characters. |
| 5 | `T4RIF.CUSTOMER.1` | `CaplTxFt4rifSlips_Customer1` | TField |  | The purpose of this field is used to specify the customer for the slip record.Valid record from CUSTOMER table. |
| 6 | `T4RIF.CUSTOMER.2` | `CaplTxFt4rifSlips_Customer2` | TField |  | The purpose of this field is used to specify the customer for the slip record. This will capture the joint customer details, if any.Valid record from CUSTOMER table. |
| 7 | `T4RIF.COMPANY` | `CaplTxFt4rifSlips_Company` | TField |  | The Field denotes the company to which the slip belongs.Valid record from COMPANY table. |
| 8 | `T4RIF.SLIP.PROCESS` | `CaplTxFt4rifSlips_SlipProcess` | TField |  | This field is to capture the slip process, like Amend or original or cancel etc.Allowed Values are:AmendOriginalCancelDuplicate |
| 9 | `T4RIF.SLIP.AMENDED` | `CaplTxFt4rifSlips_SlipAmended` | TField |  | This field denotes whether the slip is amended or not.Allowed values are Yes/No. |
| 10 | `T4RIF.AMEND.SEQ.NO` | `CaplTxFt4rifSlips_AmendSeqNo` | TField |  | This field holds the slip amend sequence number for the xml generated. |
| 11 | `T4RIF.SLIP.DATE` | `CaplTxFt4rifSlips_SlipDate` | TField |  | Field holds the date on which the slip was processed.Valid date to be stored. |
| 12 | `T4RIF.SLIP.USER` | `CaplTxFt4rifSlips_SlipUser` | TField |  | The purpose of this field is used to define the user who generated the slip.Valid record from USER application.E.g. INPUTTER.. |
| 13 | `T4RIF.BOX.16` | `CaplTxFt4rifSlips_Box16` | TField |  | Box 16 - This value indicates the amount of annuity paymentsValue for Box 24 will be fetched from AMOUNT.CODES.1 field from CAPL.H.TX.FORM.TYPE table. |
| 14 | `T4RIF.BOX.18` | `CaplTxFt4rifSlips_Box18` | TField |  | Box 16 - This value indicates the Refund of premiumsValue for Box 24 will be fetched from AMOUNT.CODES.2 field from CAPL.H.TX.FORM.TYPE table. |
| 15 | `T4RIF.BOX.24` | `CaplTxFt4rifSlips_Box24` | TField |  | Box 24 - A spousal or common-law partner in RRSPto which the annuitant's spouse contributed.Value for Box 24 will be fetched from AMOUNT.CODES.8 field from CAPL.H.TX.FORM.TYPE table. |
| 16 | `T4RIF.BOX.28` | `CaplTxFt4rifSlips_Box28` | TField |  | Box 28 - The box indicates other income or deductionsValue for Box 24 will be fetched from AMOUNT.CODES.9 field from CAPL.H.TX.FORM.TYPE table. |
| 17 | `T4RIF.BOX.35` | `CaplTxFt4rifSlips_Box35` | TField |  | Box 35 - The amount transferred on breakdown of marriage orcommon-law partnership.Value for Box 35 will be fetched from AMOUNT.CODES.7 field from CAPL.H.TX.FORM.TYPE table. |
| 18 | `T4RIF.BOX.22` | `CaplTxFt4rifSlips_Box22` | TField |  | This field is used to define the Box.22. Which will report the amount code for Withdrawal and commutation payments.Value for Box 22 will be fetched from AMOUNT.CODES.2 field from CAPL.H.TX.FORM.TYPE table. |
| 19 | `T4RIF.BOX.30` | `CaplTxFt4rifSlips_Box30` | TField |  | Box 30 - The amount which is deducted for income tax purpose, if the income tax is not deducted the box is left blank.Value for Box 30 will be fetched from AMOUNT.CODES.6 field from CAPL.H.TX.FORM.TYPE table. |
| 20 | `T4RIF.YEAR` | `CaplTxFt4rifSlips_Year` | TField |  | This field denotes the year which the slip was processed.Valid year to be defined here. |
| 21 | `T4RIF.BOX.26` | `CaplTxFt4rifSlips_Box26` | TField |  | Box.26 - The value indicated whether the plan has second customer or not.The will capture Yes/No value in the slip. |
| 22 | `T4RIF.BOX.12` | `CaplTxFt4rifSlips_Box12` | TField |  | Box 12 - The field denoted the SIN of the recipient.The value for this field os fetched from the CUSTOMER table. |
| 23 | `T4RIF.BOX.32` | `CaplTxFt4rifSlips_Box32` | TField |  | Box 32 - The field denoted the SIN of the recipient.The value for this field os fetched from the CUSTOMER table. |
| 24 | `T4RIF.BOX.14` | `CaplTxFt4rifSlips_Box14` | TField |  | Box 14 - This will fetch the value of the contract number.Validated against the @id of the Plan number. |
| 25 | `T4RIF.BOX.60` | `CaplTxFt4rifSlips_Box60` | TField |  | Box 60 - The box indicates the full name of the RRSP payer. |
| 26 | `T4RIF.BOX.61` | `CaplTxFt4rifSlips_Box61` | TField |  | Box 61 - The box indicates the business no to be display to CRA.The value is fetched from BUSINESS.NO field of CAPL.H.TX.FORM.TYPE table. |
| 27 | `T4RIF.BEN.NAME.1` | `CaplTxFt4rifSlips_BenName1` | TField |  | This field is used to denote the customer name for the slip generation.Value will be fetched from CUSTOMER table. |
| 28 | `T4RIF.BEN.ADR.1` | `CaplTxFt4rifSlips_BenAdr1` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 29 | `T4RIF.BEN.ADR.2` | `CaplTxFt4rifSlips_BenAdr2` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 30 | `T4RIF.BEN.ADR.3` | `CaplTxFt4rifSlips_BenAdr3` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 31 | `T4RIF.BEN.ADR.4` | `CaplTxFt4rifSlips_BenAdr4` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 32 | `T4RIF.BEN.ADR.5` | `CaplTxFt4rifSlips_BenAdr5` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 33 | `T4RIF.BEN.ADR.6` | `CaplTxFt4rifSlips_BenAdr6` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 34 | `T4RIF.BEN.ADR.7` | `CaplTxFt4rifSlips_BenAdr7` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 35 | `T4RIF.BEN.ADR.8` | `CaplTxFt4rifSlips_BenAdr8` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 36 | `T4RIF.BEN.ADR.9` | `CaplTxFt4rifSlips_BenAdr9` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 37 | `T4RIF.PRINT.STATUS` | `CaplTxFt4rifSlips_PrintStatus` | TField |  | This field is used to denote the print status of the slip, as modified or amended or cancelled. |
| 38 | `T4RIF.EXCL.CUST.FLAG` | `CaplTxFt4rifSlips_ExclCustFlag` | TField |  | This field is to define whether the cust flag to be excluded or not for the receipt generation.Allowed values are Yes/No |
| 39 | `T4RIF.BAD.ADDRESS` | `CaplTxFt4rifSlips_BadAddress` | TField |  | Field is to map the bad address to de.address of xml.1 and print.1If the bad address is set to YES, then the return mail in DE.ADDRESS will be updated to Yes.Allowed values are Yes/No |
| 40 | `T4RIF.BOX.36` | `CaplTxFt4rifSlips_Box36` | TField |  |  |
| 41 | `T4RIF.DEATH.SETTLE` | `CaplTxFt4rifSlips_DeathSettle` | TField |  |  |
| 42 | `T4RIF.RECORD.STATUS` | `CaplTxFt4rifSlips_RecordStatus` | String |  |  |
| 43 | `T4RIF.CURR.NO` | `CaplTxFt4rifSlips_CurrNo` | String |  |  |
| 44 | `T4RIF.INPUTTER` | `CaplTxFt4rifSlips_Inputter` |  |  |  |
| 45 | `T4RIF.DATE.TIME` | `CaplTxFt4rifSlips_DateTime` |  |  |  |
| 46 | `T4RIF.AUTHORISER` | `CaplTxFt4rifSlips_Authoriser` | String |  |  |
| 47 | `T4RIF.CO.CODE` | `CaplTxFt4rifSlips_CoCode` | String |  |  |
| 48 | `T4RIF.DEPT.CODE` | `CaplTxFt4rifSlips_DeptCode` | String |  |  |
| 49 | `T4RIF.AUDITOR.CODE` | `CaplTxFt4rifSlips_AuditorCode` | String |  |  |
| 50 | `T4RIF.AUDIT.DATE.TIME` | `CaplTxFt4rifSlips_AuditDateTime` | String |  |  |
