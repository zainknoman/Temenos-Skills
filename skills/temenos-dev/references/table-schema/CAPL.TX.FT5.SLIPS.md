# CAPL.TX.FT5.SLIPS — Table Schema

> Source: `INSERTS/I_F.CAPL.TX.FT5.SLIPS` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `T5.SLIP.ID` | `CaplTxFt5Slips_SlipId` | TField |  | Field will be defaulted with the slip id.The Slip ids selected should be populated only when CUSTOMER.NO is inputted and not when SEL.CRITERIA is given. NO INPUT Field.E.g.113035.CA.43.2015 |
| 2 | `T5.SLIP.YEAR` | `CaplTxFt5Slips_SlipYear` | TField |  | The purpose of the field is to define the year for which the slip to be generated.Valid Year to be defined here. |
| 3 | `T5.SLIP.NUMBER` | `CaplTxFt5Slips_SlipNumber` | TField |  | The purpose of the field is to define the slip number for the slip.The slip number must be nemuric value with continuous series.Allowed values are 35 alphanemuric characters. |
| 4 | `T5.SLIP.SEQ.NO` | `CaplTxFt5Slips_SlipSeqNo` | TField |  | This field is used to define the number sequence allowed for slip number mentioned.Allowed values are 35 alphanemuric characters. |
| 5 | `T5.CUSTOMER.1` | `CaplTxFt5Slips_Customer1` | TField |  | The purpose of this field is used to specify the customer for the slip record.Valid record from CUSTOMER table. |
| 6 | `T5.CUSTOMER.2` | `CaplTxFt5Slips_Customer2` | TField |  | The purpose of this field is used to specify the customer for the slip record. This will capture the joint customer details, if any.Valid record from CUSTOMER table. |
| 7 | `T5.COMPANY` | `CaplTxFt5Slips_Company` | TField |  | The Field denotes the company to which the slip belongs.Valid record from COMPANY table. |
| 8 | `T5.SLIP.PROCESS` | `CaplTxFt5Slips_SlipProcess` | TField |  | This field is to capture the slip process, like Amend or original or cancel etc.Allowed Values are:AmendOriginalCancelDuplicate |
| 9 | `T5.SLIP.AMENDED` | `CaplTxFt5Slips_SlipAmended` | TField |  | This field denotes whether the slip is amended or not.Allowed values are Yes/No. |
| 10 | `T5.AMEND.SEQ.NO` | `CaplTxFt5Slips_AmendSeqNo` | TField |  | This field holds the slip amend sequence number for the xml generated. |
| 11 | `T5.SLIP.DATE` | `CaplTxFt5Slips_SlipDate` | TField |  | Field holds the date on which the slip was processed.Valid date to be stored. |
| 12 | `T5.SLIP.USER` | `CaplTxFt5Slips_SlipUser` | TField |  | The purpose of this field is used to define the user who generated the slip.Valid record from USER application.E.g. INPUTTER.. |
| 13 | `T5.AMOUNT.1` | `CaplTxFt5Slips_Amount1` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE This table is used in the incoming file from the path CRA.IN.No mapping is available. |
| 14 | `T5.AMOUNT.2` | `CaplTxFt5Slips_Amount2` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 15 | `T5.AMOUNT.3` | `CaplTxFt5Slips_Amount3` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 16 | `T5.AMOUNT.4` | `CaplTxFt5Slips_Amount4` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 17 | `T5.AMOUNT.5` | `CaplTxFt5Slips_Amount5` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 18 | `T5.AMOUNT.6` | `CaplTxFt5Slips_Amount6` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 19 | `T5.BOX.13` | `CaplTxFt5Slips_Box13` | TField |  | This field denotes the value from the Amount.1 field which will be displayed in the slip.Valid amount to be stores here. |
| 20 | `T5.BOX.21` | `CaplTxFt5Slips_Box21` | TField |  | This field is used to indicate whether the slip is Original or Amended or Cancelled in the xml. |
| 21 | `T5.BOX.23` | `CaplTxFt5Slips_Box23` | TField |  | This field is used to denote the recipient code to be displayed in the xml.Valid receipt code to be displayed here.E.g1 - Individual2- Joint account. |
| 22 | `T5.BOX.22` | `CaplTxFt5Slips_Box22` | TField |  | This field is used to define the Box.22. Which will report the amount code for Withdrawal and commutation payments.Value for Box 22 will be fetched from AMOUNT.CODES.2 field from CAPL.H.TX.FORM.TYPE table. |
| 23 | `T5.BEN.NAME.1` | `CaplTxFt5Slips_BenName1` | TField |  | This field is used to denote the customer name for the slip generation.Value will be fetched from CUSTOMER table. |
| 24 | `T5.BEN.NAME.2` | `CaplTxFt5Slips_BenName2` | TField |  | This field is used to denote the customer name for the slip generation.Value will be fetched from CUSTOMER table. |
| 25 | `T5.BEN.ADR.1` | `CaplTxFt5Slips_BenAdr1` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 26 | `T5.BEN.ADR.2` | `CaplTxFt5Slips_BenAdr2` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 27 | `T5.BEN.ADR.3` | `CaplTxFt5Slips_BenAdr3` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 28 | `T5.BEN.ADR.4` | `CaplTxFt5Slips_BenAdr4` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 29 | `T5.BEN.ADR.5` | `CaplTxFt5Slips_BenAdr5` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 30 | `T5.BEN.ADR.6` | `CaplTxFt5Slips_BenAdr6` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 31 | `T5.BEN.ADR.7` | `CaplTxFt5Slips_BenAdr7` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 32 | `T5.BEN.ADR.8` | `CaplTxFt5Slips_BenAdr8` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 33 | `T5.BEN.ADR.9` | `CaplTxFt5Slips_BenAdr9` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 34 | `T5.BANK.NAME` | `CaplTxFt5Slips_BankName` | TField |  | This field holds the bank name to be displaued on the tax slip.Valid bank name to be stored here. |
| 35 | `T5.BANK.ADR.1` | `CaplTxFt5Slips_BankAdr1` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 36 | `T5.BANK.ADR.2` | `CaplTxFt5Slips_BankAdr2` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 37 | `T5.BANK.ADR.3` | `CaplTxFt5Slips_BankAdr3` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 38 | `T5.BANK.ADR.4` | `CaplTxFt5Slips_BankAdr4` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 39 | `T5.BANK.ADR.5` | `CaplTxFt5Slips_BankAdr5` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 40 | `T5.BANK.ADR.6` | `CaplTxFt5Slips_BankAdr6` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 41 | `T5.BANK.ADR.7` | `CaplTxFt5Slips_BankAdr7` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 42 | `T5.BANK.ADR.8` | `CaplTxFt5Slips_BankAdr8` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 43 | `T5.BANK.ADR.9` | `CaplTxFt5Slips_BankAdr9` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 44 | `T5.PRINT.STATUS` | `CaplTxFt5Slips_PrintStatus` | TField |  | This field holds the slip print status, which will store the slip has been Modified, reprinted,duplicate or amended. |
| 45 | `T5.EXCL.CUST.FLAG` | `CaplTxFt5Slips_ExclCustFlag` | TField |  | This field is to define whether the cust flag to be excluded or not for the receipt generation.Allowed values are Yes/No |
| 46 | `T5.BAD.ADDRESS` | `CaplTxFt5Slips_BadAddress` | TField |  | Field is to map the bad address to de.address of xml.1 and print.1If the bad address is set to YES, then the return mail in DE.ADDRESS will be updated to Yes.Allowed values are Yes/No |
| 47 | `T5.BOX.30` | `CaplTxFt5Slips_Box30` | TField |  | This field denotes the value from the Equity Linked Notes Interest amount field which will be displayed in the slip.Valid amount to be stores here. |
| 48 | `T5.RECORD.STATUS` | `CaplTxFt5Slips_RecordStatus` | String |  |  |
| 49 | `T5.CURR.NO` | `CaplTxFt5Slips_CurrNo` | String |  |  |
| 50 | `T5.INPUTTER` | `CaplTxFt5Slips_Inputter` |  |  |  |
| 51 | `T5.DATE.TIME` | `CaplTxFt5Slips_DateTime` |  |  |  |
| 52 | `T5.AUTHORISER` | `CaplTxFt5Slips_Authoriser` | String |  |  |
| 53 | `T5.CO.CODE` | `CaplTxFt5Slips_CoCode` | String |  |  |
| 54 | `T5.DEPT.CODE` | `CaplTxFt5Slips_DeptCode` | String |  |  |
| 55 | `T5.AUDITOR.CODE` | `CaplTxFt5Slips_AuditorCode` | String |  |  |
| 56 | `T5.AUDIT.DATE.TIME` | `CaplTxFt5Slips_AuditDateTime` | String |  |  |
