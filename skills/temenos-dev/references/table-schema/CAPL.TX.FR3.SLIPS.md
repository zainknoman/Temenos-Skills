# CAPL.TX.FR3.SLIPS — Table Schema

> Source: `INSERTS/I_F.CAPL.TX.FR3.SLIPS` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `R3.SLIP.YEAR` | `CaplTxFr3Slips_SlipYear` | TField |  | The purpose of the field is to define the year for which the slip to be generated.Valid Year to be defined here. |
| 2 | `R3.SLIP.ID` | `CaplTxFr3Slips_SlipId` | TField |  | Field will be defaulted with the slip id.The Slip ids selected should be populated only when CUSTOMER.NO is inputted and not when SEL.CRITERIA is given. NO INPUT Field.E.g.113035.CA.43.2015 |
| 3 | `R3.SLIP.NUMBER` | `CaplTxFr3Slips_SlipNumber` | TField |  | The purpose of the field is to define the slip number for the slip.The slip number must be nemuric value with continuous series.Allowed values are 35 alphanemuric characters. |
| 4 | `R3.SLIP.SEQ.NO` | `CaplTxFr3Slips_SlipSeqNo` | TField |  | This field is used to define the number sequence allowed for slip number mentioned.Allowed values are 35 alphanemuric characters. |
| 5 | `R3.CUSTOMER.1` | `CaplTxFr3Slips_Customer1` | TField |  | The purpose of this field is used to specify the customer for the slip record.Valid record from CUSTOMER table. |
| 6 | `R3.CUSTOMER.2` | `CaplTxFr3Slips_Customer2` | TField |  | The purpose of this field is used to specify the customer for the slip record. This will capture the joint customer details, if any.Valid record from CUSTOMER table. |
| 7 | `R3.COMPANY` | `CaplTxFr3Slips_Company` | TField |  | The Field denotes the company to which the slip belongs.Valid record from COMPANY table. |
| 8 | `R3.SLIP.PROCESS` | `CaplTxFr3Slips_SlipProcess` | TField |  | This field is to capture the slip process, like Amend or original or cancel etc.Allowed Values are:AmendOriginalCancelDuplicate |
| 9 | `R3.SLIP.AMENDED` | `CaplTxFr3Slips_SlipAmended` | TField |  | This field denotes whether the slip is amended or not.Allowed values are Yes/No. |
| 10 | `R3.AMEND.SEQ.NO` | `CaplTxFr3Slips_AmendSeqNo` | TField |  | This field holds the slip amend sequence number for the xml generated. |
| 11 | `R3.SLIP.DATE` | `CaplTxFr3Slips_SlipDate` | TField |  | Field holds the date on which the slip was processed.Valid date to be stored. |
| 12 | `R3.SLIP.USER` | `CaplTxFr3Slips_SlipUser` | TField |  | The purpose of this field is used to define the user who generated the slip.Valid record from USER application.E.g. INPUTTER.. |
| 13 | `R3.AMOUNT.1` | `CaplTxFr3Slips_Amount1` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 14 | `R3.AMOUNT.2` | `CaplTxFr3Slips_Amount2` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 15 | `R3.AMOUNT.3` | `CaplTxFr3Slips_Amount3` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 16 | `R3.AMOUNT.4` | `CaplTxFr3Slips_Amount4` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 17 | `R3.AMOUNT.5` | `CaplTxFr3Slips_Amount5` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 18 | `R3.AMOUNT.6` | `CaplTxFr3Slips_Amount6` | TField |  | This field holds the Amount associated to AMOUNT.CODE defined in CAPL.H.TX.FORM.TYPE |
| 19 | `R3.YEAR` | `CaplTxFr3Slips_Year` | TField |  | This field denotes the year which the slip was processed.Valid year to be defined here. |
| 20 | `R3.REPORT.CODE` | `CaplTxFr3Slips_ReportCode` | TField |  |  |
| 21 | `R3.CURRENCY` | `CaplTxFr3Slips_Currency` | TField |  | This field is used to denote the currency in which the tax is applicable for R3 slips.Valid currency to be defined here. |
| 22 | `R3.BOX.ID` | `CaplTxFr3Slips_BoxId` | TField |  | Not In use |
| 23 | `R3.TYPE` | `CaplTxFr3Slips_Type` | TField |  | This field denotes the type of slip which is to be displayed in the xml file. |
| 24 | `R3.SIN.NO.1` | `CaplTxFr3Slips_SinNo1` | TField |  | This field is used to denote the Sin Number of the customer to be displayed in the xml.Value will be fetched from CUSTOMER table. |
| 25 | `R3.SIN.NO.2` | `CaplTxFr3Slips_SinNo2` | TField |  | This field is used to denote the Sin Number of the customer to be displayed in the xml. If there is more than one customer.Value will be fetched from CUSTOMER table. |
| 26 | `R3.BEN.NAME.1` | `CaplTxFr3Slips_BenName1` | TField |  | This field is used to denote the customer name for the slip generation.Value will be fetched from CUSTOMER table. |
| 27 | `R3.BEN.NAME.2` | `CaplTxFr3Slips_BenName2` | TField |  | This field is used to denote the customer name for the slip generation.Value will be fetched from CUSTOMER table. |
| 28 | `R3.BEN.ADR.1` | `CaplTxFr3Slips_BenAdr1` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 29 | `R3.BEN.ADR.2` | `CaplTxFr3Slips_BenAdr2` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 30 | `R3.BEN.ADR.3` | `CaplTxFr3Slips_BenAdr3` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 31 | `R3.BEN.ADR.4` | `CaplTxFr3Slips_BenAdr4` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 32 | `R3.BEN.ADR.5` | `CaplTxFr3Slips_BenAdr5` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 33 | `R3.BEN.ADR.6` | `CaplTxFr3Slips_BenAdr6` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 34 | `R3.BEN.ADR.7` | `CaplTxFr3Slips_BenAdr7` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 35 | `R3.BEN.ADR.8` | `CaplTxFr3Slips_BenAdr8` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 36 | `R3.BEN.ADR.9` | `CaplTxFr3Slips_BenAdr9` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 37 | `R3.BANK.NAME` | `CaplTxFr3Slips_BankName` | TField |  | This field holds the bank name to be displaued on the tax slip.Valid bank name to be stored here. |
| 38 | `R3.BANK.ADR.1` | `CaplTxFr3Slips_BankAdr1` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 39 | `R3.BANK.ADR.2` | `CaplTxFr3Slips_BankAdr2` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 40 | `R3.BANK.ADR.3` | `CaplTxFr3Slips_BankAdr3` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 41 | `R3.BANK.ADR.4` | `CaplTxFr3Slips_BankAdr4` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 42 | `R3.BANK.ADR.5` | `CaplTxFr3Slips_BankAdr5` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 43 | `R3.BANK.ADR.6` | `CaplTxFr3Slips_BankAdr6` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 44 | `R3.BANK.ADR.7` | `CaplTxFr3Slips_BankAdr7` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 45 | `R3.BANK.ADR.8` | `CaplTxFr3Slips_BankAdr8` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 46 | `R3.BANK.ADR.9` | `CaplTxFr3Slips_BankAdr9` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 47 | `R3.PRINT.STATUS` | `CaplTxFr3Slips_PrintStatus` | TField |  | This field holds the slip print status, which will store the slip has been Modified, reprinted,duplicate or amended. |
| 48 | `R3.EXCL.CUST.FLAG` | `CaplTxFr3Slips_ExclCustFlag` | TField |  | This field is to define whether the cust flag to be excluded or not for the receipt generation.Allowed values are Yes/No |
| 49 | `R3.BAD.ADDRESS` | `CaplTxFr3Slips_BadAddress` | TField |  | Field is to map the bad address to de.address of xml.1 and print.1If the bad address is set to YES, then the return mail in DE.ADDRESS will be updated to Yes.Allowed values are Yes/No |
| 50 | `R3.RECORD.STATUS` | `CaplTxFr3Slips_RecordStatus` | String |  |  |
| 51 | `R3.CURR.NO` | `CaplTxFr3Slips_CurrNo` | String |  |  |
| 52 | `R3.INPUTTER` | `CaplTxFr3Slips_Inputter` |  |  |  |
| 53 | `R3.DATE.TIME` | `CaplTxFr3Slips_DateTime` |  |  |  |
| 54 | `R3.AUTHORISER` | `CaplTxFr3Slips_Authoriser` | String |  |  |
| 55 | `R3.CO.CODE` | `CaplTxFr3Slips_CoCode` | String |  |  |
| 56 | `R3.DEPT.CODE` | `CaplTxFr3Slips_DeptCode` | String |  |  |
| 57 | `R3.AUDITOR.CODE` | `CaplTxFr3Slips_AuditorCode` | String |  |  |
| 58 | `R3.AUDIT.DATE.TIME` | `CaplTxFr3Slips_AuditDateTime` | String |  |  |
