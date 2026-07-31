# CAPL.TX.FT4RSP.SLIPS — Table Schema

> Source: `INSERTS/I_F.CAPL.TX.FT4RSP.SLIPS` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `T4RSP.ID` | `CaplTxFt4rspSlips_Id` |  |  |  |
| 2 | `T4RSP.SLIP.YEAR` | `CaplTxFt4rspSlips_SlipYear` | TField |  | The purpose of the field is to define the year for which the slip to be generated.Valid Year to be defined here. |
| 3 | `T4RSP.SLIP.NUMBER` | `CaplTxFt4rspSlips_SlipNumber` | TField |  | The purpose of the field is to define the slip number for the slip.The slip number must be nemuric value with continuous series.Allowed values are 35 alphanemuric characters. |
| 4 | `T4RSP.SLIP.SEQ.NO` | `CaplTxFt4rspSlips_SlipSeqNo` | TField |  | This field is used to define the number sequence allowed for slip number mentioned.Allowed values are 35 alphanemuric characters. |
| 5 | `T4RSP.CUSTOMER.1` | `CaplTxFt4rspSlips_Customer1` | TField |  | The purpose of this field is used to specify the customer for the slip record.Valid record from CUSTOMER table. |
| 6 | `T4RSP.CUSTOMER.2` | `CaplTxFt4rspSlips_Customer2` | TField |  | The purpose of this field is used to specify the customer for the slip record. This will capture the joint customer details, if any.Valid record from CUSTOMER table. |
| 7 | `T4RSP.COMPANY` | `CaplTxFt4rspSlips_Company` | TField |  | The Field denotes the company to which the slip belongs.Valid record from COMPANY table. |
| 8 | `T4RSP.SLIP.PROCESS` | `CaplTxFt4rspSlips_SlipProcess` | TField |  | This field is to capture the slip process, like Amend or original or cancel etc.Allowed Values are:AmendOriginalCancelDuplicate |
| 9 | `T4RSP.SLIP.AMENDED` | `CaplTxFt4rspSlips_SlipAmended` | TField |  | This field denotes whether the slip is amended or not.Allowed values are Yes/No. |
| 10 | `T4RSP.AMEND.SEQ.NO` | `CaplTxFt4rspSlips_AmendSeqNo` | TField |  | This field holds the slip amend sequence number for the xml generated. |
| 11 | `T4RSP.SLIP.DATE` | `CaplTxFt4rspSlips_SlipDate` | TField |  | Field holds the date on which the slip was processed.Valid date to be stored. |
| 12 | `T4RSP.SLIP.USER` | `CaplTxFt4rspSlips_SlipUser` | TField |  | The purpose of this field is used to define the user who generated the slip.Valid record from USER application.E.g. INPUTTER.. |
| 13 | `T4RSP.BOX.20` | `CaplTxFt4rspSlips_Box20` | TField |  | This field is used to define the Box.20. Which will report the amount code for Refund of excess contributions amount.Value for Box 20 will be fetched from AMOUNT.CODES.1 field from CAPL.H.TX.FORM.TYPE table. |
| 14 | `T4RSP.BOX.22` | `CaplTxFt4rspSlips_Box22` | TField |  | This field is used to define the Box.22. Which will report the amount code for Withdrawal and commutation payments.Value for Box 22 will be fetched from AMOUNT.CODES.2 field from CAPL.H.TX.FORM.TYPE table. |
| 15 | `T4RSP.BOX.25` | `CaplTxFt4rspSlips_Box25` | TField |  | Box 25 - the amount withdrawn from RRSP by an eligible individual participating in the Lifelong Learning Plan (LLP).Value for Box 25 will be fetched from AMOUNT.CODES.3 field from CAPL.H.TX.FORM.TYPE table. |
| 16 | `T4RSP.BOX.18` | `CaplTxFt4rspSlips_Box18` | TField |  | Box 18 - The amount you paid from an unmatured RRSP to the spouse or common-law partner of the RRSP annuitant, when the annuitant is deseased.Value for Box 18 will be fetched from AMOUNT.CODES.4 field from CAPL.H.TX.FORM.TYPE table. |
| 17 | `T4RSP.BOX.27` | `CaplTxFt4rspSlips_Box27` | TField |  | Box 27 -The amount withdrawn from an RRSP by an eligible individual participating in the Home Buyers' Plan (HBP).Value for Box 27 will be fetched from AMOUNT.CODES.5 field from CAPL.H.TX.FORM.TYPE table. |
| 18 | `T4RSP.BOX.30` | `CaplTxFt4rspSlips_Box30` | TField |  | Box 30 - The amount which is deducted for income tax purpose, if the income tax is not deducted the box is left blank.Value for Box 30 will be fetched from AMOUNT.CODES.6 field from CAPL.H.TX.FORM.TYPE table. |
| 19 | `T4RSP.BOX.35` | `CaplTxFt4rspSlips_Box35` | TField |  | Box 35 - The amount transferred on breakdown of marriage orcommon-law partnership.Value for Box 35 will be fetched from AMOUNT.CODES.7 field from CAPL.H.TX.FORM.TYPE table. |
| 20 | `T4RSP.YEAR` | `CaplTxFt4rspSlips_Year` | TField |  | This field denotes the year which the slip was processed.Valid year to be defined here. |
| 21 | `T4RSP.BOX.24` | `CaplTxFt4rspSlips_Box24` | TField |  | Box 24 - A spousal or common-law partner in RRSPto which the annuitant's spouse contributed.Value for Box 24 will be fetched from AMOUNT.CODES.8 field from CAPL.H.TX.FORM.TYPE table. |
| 22 | `T4RSP.BOX.12` | `CaplTxFt4rspSlips_Box12` | TField |  | Box 12 - The field denoted the SIN of the recipient.The value for this field os fetched from the CUSTOMER table. |
| 23 | `T4RSP.BOX.36` | `CaplTxFt4rspSlips_Box36` | TField |  | Box 36 - This box will fetch the SIN of the recipient to display in CRA.The value for this field os fetched from the CUSTOMER table. |
| 24 | `T4RSP.BOX.14` | `CaplTxFt4rspSlips_Box14` | TField |  | Box 14 - This will fetch the value of the contract number.Validated against the @id of the Plan number. |
| 25 | `T4RSP.BOX.60` | `CaplTxFt4rspSlips_Box60` | TField |  | Box 60 - The box indicates the full name of the RRSP payer. |
| 26 | `T4RSP.BOX.61` | `CaplTxFt4rspSlips_Box61` | TField |  | Box 61 - The box indicates the business no to be display to CRA.The value is fetched from BUSINESS.NO field of CAPL.H.TX.FORM.TYPE table. |
| 27 | `T4RSP.BEN.NAME.1` | `CaplTxFt4rspSlips_BenName1` | TField |  | This field is used to denote the customer name for the slip generation.Value will be fetched from CUSTOMER table. |
| 28 | `T4RSP.BEN.ADR.1` | `CaplTxFt4rspSlips_BenAdr1` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 29 | `T4RSP.BEN.ADR.2` | `CaplTxFt4rspSlips_BenAdr2` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 30 | `T4RSP.BEN.ADR.3` | `CaplTxFt4rspSlips_BenAdr3` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 31 | `T4RSP.BEN.ADR.4` | `CaplTxFt4rspSlips_BenAdr4` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 32 | `T4RSP.BEN.ADR.5` | `CaplTxFt4rspSlips_BenAdr5` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 33 | `T4RSP.BEN.ADR.6` | `CaplTxFt4rspSlips_BenAdr6` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 34 | `T4RSP.BEN.ADR.7` | `CaplTxFt4rspSlips_BenAdr7` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 35 | `T4RSP.BEN.ADR.8` | `CaplTxFt4rspSlips_BenAdr8` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 36 | `T4RSP.BEN.ADR.9` | `CaplTxFt4rspSlips_BenAdr9` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 37 | `T4RSP.BOX.34` | `CaplTxFt4rspSlips_Box34` | TField |  | Box 34 - The box indicates amounts deemed received on death.Value for Box 24 will be fetched from AMOUNT.CODES.8 field from CAPL.H.TX.FORM.TYPE table. |
| 38 | `T4RSP.BOX.28` | `CaplTxFt4rspSlips_Box28` | TField |  | Box 28 - The box indicates other income or deductionsValue for Box 24 will be fetched from AMOUNT.CODES.9 field from CAPL.H.TX.FORM.TYPE table. |
| 39 | `T4RSP.EXCL.CUST.FLAG` | `CaplTxFt4rspSlips_ExclCustFlag` | TField |  | This field is to define whether the cust flag to be excluded or not for the receipt generation.Allowed values are Yes/No |
| 40 | `T4RSP.BAD.ADDRESS` | `CaplTxFt4rspSlips_BadAddress` | TField |  | Field is to map the bad address to de.address of xml.1 and print.1If the bad address is set to YES, then the return mail in DE.ADDRESS will be updated to Yes.Allowed values are Yes/No |
| 41 | `T4RSP.BOX.40` | `CaplTxFt4rspSlips_Box40` | TField |  |  |
| 42 | `T4RSP.DEATH.SETTLE` | `CaplTxFt4rspSlips_DeathSettle` | TField |  |  |
| 43 | `T4RSP.RECORD.STATUS` | `CaplTxFt4rspSlips_RecordStatus` | String |  |  |
| 44 | `T4RSP.CURR.NO` | `CaplTxFt4rspSlips_CurrNo` | String |  |  |
| 45 | `T4RSP.INPUTTER` | `CaplTxFt4rspSlips_Inputter` |  |  |  |
| 46 | `T4RSP.DATE.TIME` | `CaplTxFt4rspSlips_DateTime` |  |  |  |
| 47 | `T4RSP.AUTHORISER` | `CaplTxFt4rspSlips_Authoriser` | String |  |  |
| 48 | `T4RSP.CO.CODE` | `CaplTxFt4rspSlips_CoCode` | String |  |  |
| 49 | `T4RSP.DEPT.CODE` | `CaplTxFt4rspSlips_DeptCode` | String |  |  |
| 50 | `T4RSP.AUDITOR.CODE` | `CaplTxFt4rspSlips_AuditorCode` | String |  |  |
| 51 | `T4RSP.AUDIT.DATE.TIME` | `CaplTxFt4rspSlips_AuditDateTime` | String |  |  |
