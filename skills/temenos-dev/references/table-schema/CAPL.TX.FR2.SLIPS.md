# CAPL.TX.FR2.SLIPS — Table Schema

> Source: `INSERTS/I_F.CAPL.TX.FR2.SLIPS` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FR2.ID2` | `CaplTxFr2Slips_Id2` | TField |  |  |
| 2 | `FR2.SLIP.YEAR` | `CaplTxFr2Slips_SlipYear` | TField |  | The purpose of the field is to define the year for which the slip to be generated.Valid Year to be defined here. |
| 3 | `FR2.SLIP.NUMBER` | `CaplTxFr2Slips_SlipNumber` | TField |  | The purpose of the field is to define the slip number for the slip.The slip number must be nemuric value with continuous series.Allowed values are 35 alphanemuric characters. |
| 4 | `FR2.SLIP.SEQ.NO` | `CaplTxFr2Slips_SlipSeqNo` | TField |  | This field is used to define the number sequence allowed for slip number mentioned.Allowed values are 35 alphanemuric characters. |
| 5 | `FR2.CUSTOMER.1` | `CaplTxFr2Slips_Customer1` | TField |  | The purpose of this field is used to specify the customer for the slip record.Valid record from CUSTOMER table. |
| 6 | `FR2.CUSTOMER.2` | `CaplTxFr2Slips_Customer2` | TField |  | The purpose of this field is used to specify the customer for the slip record. This will capture the joint customer details, if any.Valid record from CUSTOMER table. |
| 7 | `FR2.COMPANY` | `CaplTxFr2Slips_Company` | TField |  | The Field denotes the company to which the slip belongs.Valid record from COMPANY table. |
| 8 | `FR2.SLIP.PROCESS` | `CaplTxFr2Slips_SlipProcess` | TField |  | This field is to capture the slip process, like Amend or original or cancel etc.Allowed Values are:AmendOriginalCancelDuplicate |
| 9 | `FR2.SLIP.AMENDED` | `CaplTxFr2Slips_SlipAmended` | TField |  | This field denotes whether the slip is amended or not.Allowed values are Yes/No. |
| 10 | `FR2.AMEND.SEQ.NO` | `CaplTxFr2Slips_AmendSeqNo` | TField |  | This field holds the slip amend sequence number for the xml generated. |
| 11 | `FR2.SLIP.DATE` | `CaplTxFr2Slips_SlipDate` | TField |  | Field holds the date on which the slip was processed.Valid date to be stored. |
| 12 | `FR2.SLIP.USER` | `CaplTxFr2Slips_SlipUser` | TField |  | The purpose of this field is used to define the user who generated the slip.Valid record from USER application.E.g. INPUTTER.. |
| 13 | `FR2.INCOME.SOURCE` | `CaplTxFr2Slips_IncomeSource` | TField |  | This field is used to define the sourece of income of the customer, which will be displayed in the xml file. |
| 14 | `FR2.REPORT.CODE` | `CaplTxFr2Slips_ReportCode` | TField |  |  |
| 15 | `FR2.TYPE` | `CaplTxFr2Slips_Type` | TField |  | This field denotes the type of slip which is to be displayed in the xml file. |
| 16 | `FR2.BOX.B` | `CaplTxFr2Slips_BoxB` | TField |  | Enter in box B the total QPP contributions withheld during the year. The highlighted field does not have mapping in dfe, so mentioned the BOX purpose.Check with Ramkumar. |
| 17 | `FR2.BOX.C` | `CaplTxFr2Slips_BoxC` | TField |  | This box denotes the Employment Insurance premium wothhel during the tax period. |
| 18 | `FR2.BOX.D` | `CaplTxFr2Slips_BoxD` | TField |  | This Box denoted the contribution toward registered pension plan. |
| 19 | `FR2.BOX.E` | `CaplTxFr2Slips_BoxE` | TField |  | This box is to dentoe the Quebec income tax withheld. |
| 20 | `FR2.BOX.F` | `CaplTxFr2Slips_BoxF` | TField |  | The amount withheld as union dues during the year should be included in box F. |
| 21 | `FR2.BOX.G` | `CaplTxFr2Slips_BoxG` | TField |  | This box is used to denote the Pensionable salary or wages under the QPP. |
| 22 | `FR2.BOX.H` | `CaplTxFr2Slips_BoxH` | TField |  | Enter in box H the total QPIP premiums withheld during the year |
| 23 | `FR2.BOX.I` | `CaplTxFr2Slips_BoxI` | TField |  | This box is to denote the Eligible salary or wages under the QPIP. |
| 24 | `FR2.BOX.J` | `CaplTxFr2Slips_BoxJ` | TField |  | This box is used to define Private health services plan or employer insurance. |
| 25 | `FR2.BOX.K` | `CaplTxFr2Slips_BoxK` | TField |  | This box is to denote the income paid/received for trip to employee from remote areas. |
| 26 | `FR2.BOX.L` | `CaplTxFr2Slips_BoxL` | TField |  | If the employee is also a shareholder and receives taxable benefits as a shareholder should be included here as other incomes |
| 27 | `FR2.BOX.O` | `CaplTxFr2Slips_BoxO` | TField |  | This box is used to denote Other income paid/earned. |
| 28 | `FR2.BOX.A` | `CaplTxFr2Slips_BoxA` | TField |  | This field is used to denote the Employment income for the R1 type slips. |
| 29 | `FR2.YEAR` | `CaplTxFr2Slips_Year` | TField |  | This field denotes the year which the slip was processed.Valid year to be defined here. |
| 30 | `FR2.SIN.NO.1` | `CaplTxFr2Slips_SinNo1` | TField |  | This field is used to denote the Sin Number of the customer to be displayed in the xml.Value will be fetched from CUSTOMER table. |
| 31 | `FR2.SIN.NO.2` | `CaplTxFr2Slips_SinNo2` | TField |  | This field is used to denote the Sin Number of the customer to be displayed in the xml. If there is more than one customer.Value will be fetched from CUSTOMER table. |
| 32 | `FR2.BEN.NAME.1` | `CaplTxFr2Slips_BenName1` | TField |  | This field is used to denote the customer name for the slip generation.Value will be fetched from CUSTOMER table. |
| 33 | `FR2.BEN.NAME.2` | `CaplTxFr2Slips_BenName2` | TField |  | This field is used to denote the customer name for the slip generation.Value will be fetched from CUSTOMER table. |
| 34 | `FR2.BEN.ADR.1` | `CaplTxFr2Slips_BenAdr1` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 35 | `FR2.BEN.ADR.2` | `CaplTxFr2Slips_BenAdr2` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 36 | `FR2.BEN.ADR.3` | `CaplTxFr2Slips_BenAdr3` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 37 | `FR2.BEN.ADR.4` | `CaplTxFr2Slips_BenAdr4` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 38 | `FR2.BEN.ADR.5` | `CaplTxFr2Slips_BenAdr5` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 39 | `FR2.BEN.ADR.6` | `CaplTxFr2Slips_BenAdr6` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 40 | `FR2.BEN.ADR.7` | `CaplTxFr2Slips_BenAdr7` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 41 | `FR2.BEN.ADR.8` | `CaplTxFr2Slips_BenAdr8` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 42 | `FR2.BEN.ADR.9` | `CaplTxFr2Slips_BenAdr9` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 43 | `FR2.BANK.NAME` | `CaplTxFr2Slips_BankName` | TField |  | This field holds the bank name to be displaued on the tax slip.Valid bank name to be stored here. |
| 44 | `FR2.BANK.ADR.1` | `CaplTxFr2Slips_BankAdr1` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 45 | `FR2.BANK.ADR.2` | `CaplTxFr2Slips_BankAdr2` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 46 | `FR2.BANK.ADR.3` | `CaplTxFr2Slips_BankAdr3` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 47 | `FR2.BANK.ADR.4` | `CaplTxFr2Slips_BankAdr4` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 48 | `FR2.BANK.ADR.5` | `CaplTxFr2Slips_BankAdr5` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 49 | `FR2.BANK.ADR.6` | `CaplTxFr2Slips_BankAdr6` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 50 | `FR2.BANK.ADR.7` | `CaplTxFr2Slips_BankAdr7` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 51 | `FR2.BANK.ADR.8` | `CaplTxFr2Slips_BankAdr8` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 52 | `FR2.BANK.ADR.9` | `CaplTxFr2Slips_BankAdr9` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 53 | `FR2.PRINT.STATUS` | `CaplTxFr2Slips_PrintStatus` | TField |  | This field holds the slip print status, which will store the slip has been Modified, reprinted,duplicate or amended. |
| 54 | `FR2.EXCL.CUST.FLAG` | `CaplTxFr2Slips_ExclCustFlag` | TField |  | This field is to define whether the cust flag to be excluded or not for the receipt generation.Allowed values are Yes/No |
| 55 | `FR2.BAD.ADDRESS` | `CaplTxFr2Slips_BadAddress` | TField |  | Field is to map the bad address to de.address of xml.1 and print.1If the bad address is set to YES, then the return mail in DE.ADDRESS will be updated to Yes.Allowed values are Yes/No |
| 56 | `FR2.RECORD.STATUS` | `CaplTxFr2Slips_RecordStatus` | String |  |  |
| 57 | `FR2.CURR.NO` | `CaplTxFr2Slips_CurrNo` | String |  |  |
| 58 | `FR2.INPUTTER` | `CaplTxFr2Slips_Inputter` |  |  |  |
| 59 | `FR2.DATE.TIME` | `CaplTxFr2Slips_DateTime` |  |  |  |
| 60 | `FR2.AUTHORISER` | `CaplTxFr2Slips_Authoriser` | String |  |  |
| 61 | `FR2.CO.CODE` | `CaplTxFr2Slips_CoCode` | String |  |  |
| 62 | `FR2.DEPT.CODE` | `CaplTxFr2Slips_DeptCode` | String |  |  |
| 63 | `FR2.AUDITOR.CODE` | `CaplTxFr2Slips_AuditorCode` | String |  |  |
| 64 | `FR2.AUDIT.DATE.TIME` | `CaplTxFr2Slips_AuditDateTime` | String |  |  |
