# CAPL.TX.FR1.SLIPS — Table Schema

> Source: `INSERTS/I_F.CAPL.TX.FR1.SLIPS` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FR1.ID2` | `CaplTxFr1Slips_Id2` | TField |  |  |
| 2 | `FR1.SLIP.YEAR` | `CaplTxFr1Slips_SlipYear` | TField |  | The purpose of the field is to define the year for which the slip to be generated.Valid Year to be defined here. |
| 3 | `FR1.SLIP.NUMBER` | `CaplTxFr1Slips_SlipNumber` | TField |  | The purpose of the field is to define the slip number for the slip.The slip number must be nemuric value with continuous series.Allowed values are 35 alphanemuric characters. |
| 4 | `FR1.CUSTOMER.1` | `CaplTxFr1Slips_Customer1` | TField |  | The purpose of this field is used to specify the customer for the slip record.Valid record from CUSTOMER table. |
| 5 | `FR1.CUSTOMER.2` | `CaplTxFr1Slips_Customer2` | TField |  | The purpose of this field is used to specify the customer for the slip record.Valid record from CUSTOMER table. |
| 6 | `FR1.COMPANY` | `CaplTxFr1Slips_Company` | TField |  | The Field denotes the company to which the slip belongs.Valid record from COMPANY table. |
| 7 | `FR1.SLIP.PROCESS` | `CaplTxFr1Slips_SlipProcess` | TField |  | This field is to capture the slip process, like Amend or original or cancel etc.Allowed Values are:AmendOriginalCancelDuplicate |
| 8 | `FR1.SLIP.AMENDED` | `CaplTxFr1Slips_SlipAmended` | TField |  | This field denotes whether the slip is amended or not.Allowed values are Yes/No. |
| 9 | `FR1.AMEND.SEQ.NO` | `CaplTxFr1Slips_AmendSeqNo` | TField |  | This field holds the slip amend sequence number for the xml generated. |
| 10 | `FR1.SLIP.DATE` | `CaplTxFr1Slips_SlipDate` | TField |  | Field holds the date on which the slip was processed.Valid date to be stored. |
| 11 | `FR1.SLIP.USER` | `CaplTxFr1Slips_SlipUser` | TField |  | The purpose of this field is used to define the user who generated the slip.Valid record from USER application.E.g. INPUTTER.. |
| 12 | `FR1.INCOME.SOURCE` | `CaplTxFr1Slips_IncomeSource` | TField |  | This field is used to define the sourece of income of the customer, which will be displayed in the xml file. |
| 13 | `FR1.REPORT.CODE` | `CaplTxFr1Slips_ReportCode` | TField |  | Not In use This field is used from the incoming file in CRA.IN path, But no sample records are available in the environment. |
| 14 | `FR1.TYPE` | `CaplTxFr1Slips_Type` | TField |  | This field denotes the type of slip which is to be displayed in the xml file. |
| 15 | `FR1.BOX.O` | `CaplTxFr1Slips_BoxO` | TField |  | This box is used to denote Other income paid/earned. The highlighted field does not have mapping in dfe, so mentioned the BOX purpose.Check with Ramkumar. |
| 16 | `FR1.BOX.A` | `CaplTxFr1Slips_BoxA` | TField |  | This field is used to denote the Employment income for the R1 type slips. |
| 17 | `FR1.BOX.B` | `CaplTxFr1Slips_BoxB` | TField |  | Enter in box B the total QPP contributions withheld during the year. |
| 18 | `FR1.BOX.C` | `CaplTxFr1Slips_BoxC` | TField |  | This box denotes the Employment Insurance premium wothhel during the tax period. |
| 19 | `FR1.BOX.D` | `CaplTxFr1Slips_BoxD` | TField |  | This Box denoted the contribution toward registered pension plan. |
| 20 | `FR1.BOX.E` | `CaplTxFr1Slips_BoxE` | TField |  | This box is to dentoe the Quebec income tax withheld. |
| 21 | `FR1.BOX.F` | `CaplTxFr1Slips_BoxF` | TField |  | The amount withheld as union dues during the year should be included in box F. |
| 22 | `FR1.BOX.G` | `CaplTxFr1Slips_BoxG` | TField |  | This Box denoted the Pensionable salary or wages. |
| 23 | `FR1.BOX.H` | `CaplTxFr1Slips_BoxH` | TField |  |  |
| 24 | `FR1.BOX.I` | `CaplTxFr1Slips_BoxI` | TField |  | This box is to denote the Eligible salary or wages under the QPIP. |
| 25 | `FR1.BOX.J` | `CaplTxFr1Slips_BoxJ` | TField |  | This box is used to define Private health services plan or employer insurance. |
| 26 | `FR1.BOX.K` | `CaplTxFr1Slips_BoxK` | TField |  | This box is to denote the income paid/received for trip to employee from remote areas. |
| 27 | `FR1.BOX.L` | `CaplTxFr1Slips_BoxL` | TField |  | If the employee is also a shareholder and receives taxable benefits as a shareholder should be included here as other incomes |
| 28 | `FR1.BOX.M` | `CaplTxFr1Slips_BoxM` | TField |  | This box is to denote the Commissions paid to employee. |
| 29 | `FR1.BOX.N` | `CaplTxFr1Slips_BoxN` | TField |  | Enter in box N the total of any amounts withheld as donations and gifts during the year and paid on behalf of the employee to a registered charity or other recognized organization |
| 30 | `FR1.BOX.P` | `CaplTxFr1Slips_BoxP` | TField |  | This box is to denote the Multi-employer insurance plans. |
| 31 | `FR1.BOX.Q` | `CaplTxFr1Slips_BoxQ` | TField |  | This box is used to define the Deferred salary or wages paid to the employee. |
| 32 | `FR1.BOX.R` | `CaplTxFr1Slips_BoxR` | TField |  |  |
| 33 | `FR1.BOX.S` | `CaplTxFr1Slips_BoxS` | TField |  | This box denotes the Tips allocated by the employer to the employee which is not inclused under GST. |
| 34 | `FR1.BOX.T` | `CaplTxFr1Slips_BoxT` | TField |  | This box denotes the Tips allocated by the employer to the employee which is not inclused under GST. |
| 35 | `FR1.BOX.U` | `CaplTxFr1Slips_BoxU` | TField |  | Enter in box U the deemed salary or wages paid under a phased retirement arrangement that has been approved by Retraite Quebec. |
| 36 | `FR1.BOX.V` | `CaplTxFr1Slips_BoxV` | TField |  | This box is to denote the alloances like Meals and lodging |
| 37 | `FR1.BOX.W` | `CaplTxFr1Slips_BoxW` | TField |  | This box is used to define the Motor vehicle used for official purpose. |
| 38 | `FR1.YEAR` | `CaplTxFr1Slips_Year` | TField |  | This field denotes the year which the slip was processed.Valid year to be defined here. |
| 39 | `FR1.SIN.NO.1` | `CaplTxFr1Slips_SinNo1` | TField |  | This field is used to denote the Sin Number of the customer to be displayed in the xml.Value will be fetched from CUSTOMER table. |
| 40 | `FR1.SIN.NO.2` | `CaplTxFr1Slips_SinNo2` | TField |  | This field is used to denote the Sin Number of the customer to be displayed in the xml. If there is more than one customer.Value will be fetched from CUSTOMER table. |
| 41 | `FR1.BEN.NAME.1` | `CaplTxFr1Slips_BenName1` | TField |  | This field is used to denote the customer name for the slip generation.Value will be fetched from CUSTOMER table. |
| 42 | `FR1.BEN.NAME.2` | `CaplTxFr1Slips_BenName2` | TField |  | This field is used to denote the customer name for the slip generation.Value will be fetched from CUSTOMER table. |
| 43 | `FR1.BEN.ADR.1` | `CaplTxFr1Slips_BenAdr1` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 44 | `FR1.BEN.ADR.2` | `CaplTxFr1Slips_BenAdr2` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 45 | `FR1.BEN.ADR.3` | `CaplTxFr1Slips_BenAdr3` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 46 | `FR1.BEN.ADR.4` | `CaplTxFr1Slips_BenAdr4` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 47 | `FR1.BEN.ADR.5` | `CaplTxFr1Slips_BenAdr5` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 48 | `FR1.BEN.ADR.6` | `CaplTxFr1Slips_BenAdr6` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 49 | `FR1.BEN.ADR.7` | `CaplTxFr1Slips_BenAdr7` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 50 | `FR1.BEN.ADR.8` | `CaplTxFr1Slips_BenAdr8` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 51 | `FR1.BEN.ADR.9` | `CaplTxFr1Slips_BenAdr9` | TField |  | This field is used to define the customer address. The value in the field will be fetched form Customer and CAPL.H.TX.PARAMETER table and match the industry value. If the industry matches the address updated.Addres will be fetched from DE.ADDRESS table. |
| 52 | `FR1.BANK.NAME` | `CaplTxFr1Slips_BankName` | TField |  | This field holds the bank name to be displaued on the tax slip.Valid bank name to be stored here. |
| 53 | `FR1.BANK.ADR.1` | `CaplTxFr1Slips_BankAdr1` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 54 | `FR1.BANK.ADR.2` | `CaplTxFr1Slips_BankAdr2` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 55 | `FR1.BANK.ADR.3` | `CaplTxFr1Slips_BankAdr3` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 56 | `FR1.BANK.ADR.4` | `CaplTxFr1Slips_BankAdr4` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 57 | `FR1.BANK.ADR.5` | `CaplTxFr1Slips_BankAdr5` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 58 | `FR1.BANK.ADR.6` | `CaplTxFr1Slips_BankAdr6` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 59 | `FR1.BANK.ADR.7` | `CaplTxFr1Slips_BankAdr7` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 60 | `FR1.BANK.ADR.8` | `CaplTxFr1Slips_BankAdr8` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 61 | `FR1.BANK.ADR.9` | `CaplTxFr1Slips_BankAdr9` | TField |  | The field denoes the Bank address to be displayed on the tax slip.Valid address to be stored here. |
| 62 | `FR1.PRINT.STATUS` | `CaplTxFr1Slips_PrintStatus` | TField |  | This field holds the slip print status, which will store the slip has been Modified, reprinted,duplicate or amended. |
| 63 | `FR1.EXCL.CUST.FLAG` | `CaplTxFr1Slips_ExclCustFlag` | TField |  | This field is to define whether the cust flag to be excluded or not for the receipt generation.Allowed values are Yes/No |
| 64 | `FR1.BAD.ADDRESS` | `CaplTxFr1Slips_BadAddress` | TField |  | Field is to map the bad address to de.address of xml.1 and print.1If the bad address is set to YES, then the return mail in DE.ADDRESS will be updated to Yes.Allowed values are Yes/No |
| 65 | `FR1.RESERVED.1` | `CaplTxFr1Slips_Reserved1` | TField |  |  |
| 66 | `FR1.RESERVED.2` | `CaplTxFr1Slips_Reserved2` | TField |  |  |
| 67 | `FR1.RESERVED.3` | `CaplTxFr1Slips_Reserved3` | TField |  |  |
| 68 | `FR1.RESERVED.4` | `CaplTxFr1Slips_Reserved4` | TField |  |  |
| 69 | `FR1.RESERVED.5` | `CaplTxFr1Slips_Reserved5` | TField |  |  |
| 70 | `FR1.RESERVED.6` | `CaplTxFr1Slips_Reserved6` | TField |  |  |
| 71 | `FR1.RESERVED.7` | `CaplTxFr1Slips_Reserved7` | TField |  |  |
| 72 | `FR1.RESERVED.8` | `CaplTxFr1Slips_Reserved8` | TField |  |  |
| 73 | `FR1.RESERVED.9` | `CaplTxFr1Slips_Reserved9` | TField |  |  |
| 74 | `FR1.RESERVED.10` | `CaplTxFr1Slips_Reserved10` | TField |  |  |
| 75 | `FR1.LOCAL.REF` | `CaplTxFr1Slips_LocalRef` |  |  |  |
| 76 | `FR1.OVERRIDE` | `CaplTxFr1Slips_Override` |  |  |  |
| 77 | `FR1.RECORD.STATUS` | `CaplTxFr1Slips_RecordStatus` | String |  |  |
| 78 | `FR1.CURR.NO` | `CaplTxFr1Slips_CurrNo` | String |  |  |
| 79 | `FR1.INPUTTER` | `CaplTxFr1Slips_Inputter` |  |  |  |
| 80 | `FR1.DATE.TIME` | `CaplTxFr1Slips_DateTime` |  |  |  |
| 81 | `FR1.AUTHORISER` | `CaplTxFr1Slips_Authoriser` | String |  |  |
| 82 | `FR1.CO.CODE` | `CaplTxFr1Slips_CoCode` | String |  |  |
| 83 | `FR1.DEPT.CODE` | `CaplTxFr1Slips_DeptCode` | String |  |  |
| 84 | `FR1.AUDITOR.CODE` | `CaplTxFr1Slips_AuditorCode` | String |  |  |
| 85 | `FR1.AUDIT.DATE.TIME` | `CaplTxFr1Slips_AuditDateTime` | String |  |  |
