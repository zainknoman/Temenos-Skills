# CAPL.H.TX.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CAPL.H.TX.PARAMETER` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.TP.DESCRIPTION` | `CaplHTxParameter_Description` |  |  |  |
| 2 | `CAPL.TP.NR.LCY.CODE` | `CaplHTxParameter_NrLcyCode` | TField |  | This field is used to define the Non-resident income code in local currency CAD. Used to return NR Type for NR.CODE in xml extract.Field accepts alphanumeric codeE.g. 1, 2 ,10,15 |
| 3 | `CAPL.TP.NR.FCY.CODE` | `CaplHTxParameter_NrFcyCode` | TField |  | This field is used to define the Non-resident income code in foreign ccy. Used to return NR Type for NR.CODE in xml extract.Field accepts alphanumeric codeE.g. 1,2,10,15 |
| 4 | `CAPL.TP.NR.EXP.CODE` | `CaplHTxParameter_NrExpCode` | TField |  | This field is used to define the NR exemption code for foreign ccy. Used to return NR Type for NR.CODE in xml extract.Field accepts alphanumeric codeE.g. 1,2,10,15 |
| 5 | `CAPL.TP.REC.SECTOR` | `CaplHTxParameter_RecSector` |  |  |  |
| 6 | `CAPL.TP.REC.INDUSTRY` | `CaplHTxParameter_RecIndustry` |  |  |  |
| 7 | `CAPL.TP.REC.JOINT` | `CaplHTxParameter_RecJoint` |  |  |  |
| 8 | `CAPL.TP.REC.SPOUSE.JOINT` | `CaplHTxParameter_RecSpouseJoint` |  |  |  |
| 9 | `CAPL.TP.REC.TYPE` | `CaplHTxParameter_RecType` |  |  |  |
| 10 | `CAPL.TP.NTR.LAW.IND` | `CaplHTxParameter_NtrLawInd` |  |  |  |
| 11 | `CAPL.TP.NTR.NAME` | `CaplHTxParameter_NtrName` |  |  |  |
| 12 | `CAPL.TP.NTR.ADR.1` | `CaplHTxParameter_NtrAdr1` |  |  |  |
| 13 | `CAPL.TP.NTR.ADR.2` | `CaplHTxParameter_NtrAdr2` |  |  |  |
| 14 | `CAPL.TP.NTR.ADR.3` | `CaplHTxParameter_NtrAdr3` |  |  |  |
| 15 | `CAPL.TP.NTR.ADR.4` | `CaplHTxParameter_NtrAdr4` |  |  |  |
| 16 | `CAPL.TP.NTR.ADR.5` | `CaplHTxParameter_NtrAdr5` |  |  |  |
| 17 | `CAPL.TP.NTR.ADR.6` | `CaplHTxParameter_NtrAdr6` |  |  |  |
| 18 | `CAPL.TP.SLP.YEAR` | `CaplHTxParameter_SlpYear` |  |  |  |
| 19 | `CAPL.TP.SLP.CCY` | `CaplHTxParameter_SlpCcy` |  |  |  |
| 20 | `CAPL.TP.SLP.RATE` | `CaplHTxParameter_SlpRate` |  |  |  |
| 21 | `CAPL.TP.TRANS.NUMBER` | `CaplHTxParameter_TransNumber` | TField |  | This field is used to define the Transmitter No to whom the slip to be sent.Free text field 8 alphanumeric character. |
| 22 | `CAPL.TP.TRANS.TYPE` | `CaplHTxParameter_TransType` | TField |  | This field is used to define transmitter type Not sure |
| 23 | `CAPL.TP.TRANS.LANG` | `CaplHTxParameter_TransLang` | TField |  | This field is used to indicate the transmitter language code. It allows 1 alpha-numeric character as an input. Allowed values.- E = English- F = French |
| 24 | `CAPL.TP.TRANS.NAME.1` | `CaplHTxParameter_TransName1` | TField |  | This field is expected to be captured manually by the bank's user. It indicates the Transmitters name. |
| 25 | `CAPL.TP.TRANS.NAME.2` | `CaplHTxParameter_TransName2` | TField |  | This field is used to define the transmitter address.Free text field 30 alphanumeric character. |
| 26 | `CAPL.TP.TRANS.ADDR.1` | `CaplHTxParameter_TransAddr1` | TField |  | This field is used to define the transmitter address.Free text field 30 alphanumeric character. |
| 27 | `CAPL.TP.TRANS.ADDR.2` | `CaplHTxParameter_TransAddr2` | TField |  | This field is used to define the transmitter address.Free text field 30 alphanumeric character. |
| 28 | `CAPL.TP.TRANS.CITY` | `CaplHTxParameter_TransCity` | TField |  | This field is used to define the transmitter cityFree text field 30 alphanumeric character. |
| 29 | `CAPL.TP.TRANS.PROV` | `CaplHTxParameter_TransProv` | TField |  | This field is used to define the transmitter provinceFree text field 30 alphanumeric character. |
| 30 | `CAPL.TP.TRANS.COUNTRY` | `CaplHTxParameter_TransCountry` | TField |  | This field is expected to be captured manually by the bank's user. It indicates the country code of the transmitter. |
| 31 | `CAPL.TP.TRANS.POST` | `CaplHTxParameter_TransPost` | TField |  | This field is used to define the transmitter postal codeFree text field 30 alphanumeric character. |
| 32 | `CAPL.TP.CONT1.NAME` | `CaplHTxParameter_Cont1Name` | TField |  | This field is expected to be captured manually by the bank's user. It indicates the Name of the contact person of the transmitter. The first name should be followed by surname. This should not include titles (for example, Mr. or Mrs.) |
| 33 | `CAPL.TP.CONT1.PH.AREA` | `CaplHTxParameter_Cont1PhArea` | TField |  | This field is expected to be captured manually by the bank's user. It indicates the telephone contact area code of the contact person. |
| 34 | `CAPL.TP.CONT1.PHONE` | `CaplHTxParameter_Cont1Phone` | TField |  | This field is expected to be captured manually by the bank's user. It indicates the telephone number of the contact person. |
| 35 | `CAPL.TP.CONT1.PH.EXT` | `CaplHTxParameter_Cont1PhExt` | TField |  | This field is expected to be captured manually by the bank's user. It indicates the extension number of the contact person. |
| 36 | `CAPL.TP.CONT1.EMAIL` | `CaplHTxParameter_Cont1Email` | TField |  | This field is expected to be captured manually by the bank's user. It indicates the primary email id of the contact person to be used for contact purposes. |
| 37 | `CAPL.TP.CONT2.NAME` | `CaplHTxParameter_Cont2Name` | TField |  | This field is used to define the counter party second contact name.Free text field 61 alphanumeric character. |
| 38 | `CAPL.TP.CONT2.PH.AREA` | `CaplHTxParameter_Cont2PhArea` | TField |  | This field is used to define the counter party area code.Free text field 3 alphanumeric character. |
| 39 | `CAPL.TP.CONT2.PHONE` | `CaplHTxParameter_Cont2Phone` | TField |  | This field is used to define the counter party phone number.Validation.Format should be NNN-NNNN. User should input only 7 Numeric |
| 40 | `CAPL.TP.CONT2.PH.EXT` | `CaplHTxParameter_Cont2PhExt` | TField |  | This field is used to define the counter party phone extension.Free text field 3 alphanumeric character. |
| 41 | `CAPL.TP.PAYER.NAME.1` | `CaplHTxParameter_PayerName1` | TField |  | This field is used to define the Payer name for the tax slip processing.Free text field 35 alphanumeric character. |
| 42 | `CAPL.TP.PAYER.NAME.2` | `CaplHTxParameter_PayerName2` | TField |  | This field is used to define the Payer name for the tax slip processing.Free text field 35 alphanumeric character. |
| 43 | `CAPL.TP.PAYER.NAME.3` | `CaplHTxParameter_PayerName3` | TField |  | This field is used to define the Payer name for the tax slip processing.Free text field 35 alphanumeric character. |
| 44 | `CAPL.TP.PAYER.ADR.1` | `CaplHTxParameter_PayerAdr1` | TField |  | This field is used to define the Payer address for the tax slip processing.Free text field 30 alphanumeric character. |
| 45 | `CAPL.TP.PAYER.ADR.2` | `CaplHTxParameter_PayerAdr2` | TField |  | This field is used to define the Payer address for the tax slip processing.Free text field 30 alphanumeric character. |
| 46 | `CAPL.TP.PAYER.CITY` | `CaplHTxParameter_PayerCity` | TField |  | This field is used to define the Payer city for the tax slip processing.Free text field 28 alphanumeric character. |
| 47 | `CAPL.TP.PAYER.PROV` | `CaplHTxParameter_PayerProv` | TField |  | This field is used to define the Payer province for the tax slip processing.Free text field 2 alphanumeric character. |
| 48 | `CAPL.TP.PAYER.COUNTRY` | `CaplHTxParameter_PayerCountry` | TField |  | This field is used to define the Payer city for the tax slip processing.Free text field 3 alphanumeric character. |
| 49 | `CAPL.TP.PAYER.POST` | `CaplHTxParameter_PayerPost` | TField |  | This field is used to define the Payer postal code for the tax slip processing.Free text field 10 alphanumeric character. |
| 50 | `CAPL.TP.TAX.FORM` | `CaplHTxParameter_TaxForm` |  |  |  |
| 51 | `CAPL.TP.FORM.CHK.RTN` | `CaplHTxParameter_FormChkRtn` |  |  |  |
| 52 | `CAPL.TP.EXC.INDUSTRY` | `CaplHTxParameter_ExcIndustry` |  |  |  |
| 53 | `CAPL.TP.CONT2.EMAIL` | `CaplHTxParameter_Cont2Email` | TField |  | This field is expected to be captured manually by the bank's user. It indicates the secondary / alternate email id of the contact person. |
| 54 | `CAPL.TP.CONT1.OCCUP` | `CaplHTxParameter_Cont1Occup` |  |  |  |
| 55 | `CAPL.TP.TAX.CAPTURE.VERS` | `CaplHTxParameter_TaxCaptureVers` | TField |  | This field is used to define the version to be used for the tax capture entry.Valid record from VERSION table. |
| 56 | `CAPL.TP.TAX.OFS.SOURCE` | `CaplHTxParameter_TaxOfsSource` | TField |  | This field is used to define the ofs source id for posting of the tax capture entry.Record from OFS.SOURCE table. |
| 57 | `CAPL.TP.NR.CODE` | `CaplHTxParameter_NrCode` | TField |  | This field is used to store the income source code for non resident slip. |
| 58 | `CAPL.TP.PROV.REGION` | `CaplHTxParameter_ProvRegion` | TField |  | This field is used to define the province for the tax processing for NR slips.Valid record from REGION table. |
| 59 | `CAPL.TP.CIF.SECTOR` | `CaplHTxParameter_CifSector` |  |  |  |
| 60 | `CAPL.TP.CIF.INDUSTRY` | `CaplHTxParameter_CifIndustry` |  |  |  |
| 61 | `CAPL.TP.AMOUNT.CODES` | `CaplHTxParameter_AmountCodes` |  |  |  |
| 62 | `CAPL.TP.LOG.FILE.NAME` | `CaplHTxParameter_LogFileName` | TField |  | This field is used to indicate exception LOG FILE name to capture the sequence number exceptions.Valid file name to be defined here. |
| 63 | `CAPL.TP.LOG.DIR` | `CaplHTxParameter_LogDir` | TField |  | This field is used to indicate LOG Directory name to capture the Slip sequence number exceptions.Valid folder path to be defined here.E.g. ./bnk.interface/TAXECEPTION.LOGNote: While producing the Slip Number for Slips, If the slip Number is out of range defined in CAPL.H.TX.FORM.TYPE table, then the exception will be captured in the log directory. |
| 64 | `CAPL.TP.INCL.NR.CODE` | `CaplHTxParameter_InclNrCode` | TField |  | This field is used to define whether the NR.CODE in Slip Id to be included or not.Possible values are "YES" or "NO".IF "NO" NR.CODE will not be included as part of Slip Id.IF "YES" NR.CODE will be included as part of Slip Id. |
| 65 | `CAPL.TP.AMEND.SEQ.NO.VAL` | `CaplHTxParameter_AmendSeqNoVal` | TField |  | This field is used to define the AMEND SEQ NO should display either the Previous Slip Number or the Original Slip Number.Possible values are "ORIGINAL" or "PREVIOUS"ORIGINAL will display the original Slip number and PREVIOUS will display the Previous Slip number.By default, the Original Slip number will be displayed |
| 66 | `CAPL.TP.REM.SAM.ACTIVITY` | `CaplHTxParameter_RemSamActivity` |  |  |  |
| 67 | `CAPL.TP.RECEIP.BUS.NO` | `CaplHTxParameter_ReceipBusNo` | TField |  | This field is used to parameterize the customer field which needs to be considered as Business number. If this field is not defined CUSTOMER>BIN.NO will be considered as business number. |
| 68 | `CAPL.TP.TRUST.INDUSTRY` | `CaplHTxParameter_TrustIndustry` |  |  |  |
| 69 | `CAPL.TP.PAYOUT.CHARGE` | `CaplHTxParameter_PayoutCharge` | TField |  |  |
| 70 | `CAPL.TP.DOD.SLIP.DATE` | `CaplHTxParameter_DodSlipDate` | TField |  |  |
| 71 | `CAPL.TP.CUSTOMER.TYPE` | `CaplHTxParameter_CustomerType` |  |  |  |
| 72 | `CAPL.TP.LOCAL.REF` | `CaplHTxParameter_LocalRef` |  |  |  |
| 73 | `CAPL.TP.OVERRIDE` | `CaplHTxParameter_Override` |  |  |  |
| 74 | `CAPL.TP.RECORD.STATUS` | `CaplHTxParameter_RecordStatus` | String |  |  |
| 75 | `CAPL.TP.CURR.NO` | `CaplHTxParameter_CurrNo` | String |  |  |
| 76 | `CAPL.TP.INPUTTER` | `CaplHTxParameter_Inputter` |  |  |  |
| 77 | `CAPL.TP.DATE.TIME` | `CaplHTxParameter_DateTime` |  |  |  |
| 78 | `CAPL.TP.AUTHORISER` | `CaplHTxParameter_Authoriser` | String |  |  |
| 79 | `CAPL.TP.CO.CODE` | `CaplHTxParameter_CoCode` | String |  |  |
| 80 | `CAPL.TP.DEPT.CODE` | `CaplHTxParameter_DeptCode` | String |  |  |
| 81 | `CAPL.TP.AUDITOR.CODE` | `CaplHTxParameter_AuditorCode` | String |  |  |
| 82 | `CAPL.TP.AUDIT.DATE.TIME` | `CaplHTxParameter_AuditDateTime` | String |  |  |
| 83 | `CAPL.TP.MAP.FIELD.NAME` | `CaplHTxParameter_MapFieldName` |  |  |  |
| 84 | `CAPL.TP.MAP.FIELD.TYPE` | `CaplHTxParameter_MapFieldType` |  |  |  |
