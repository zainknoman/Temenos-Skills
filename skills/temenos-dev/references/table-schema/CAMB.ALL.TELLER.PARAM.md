# CAMB.ALL.TELLER.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.ALL.TELLER.PARAM` in `CAVLTT_ValueAddedTeller.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.ALP.MEMBERSHIP.CODE` | `CambAllTellerParam_MembershipCode` |  |  |  |
| 2 | `CAMB.ALP.NONMEMBER.CAT` | `CambAllTellerParam_NonmemberCat` | TField |  | For bill payment functionality, the customer may wish to pay the bill in branch using Cash (Non customer) or cheque.In case of cheque, this field is used to form the internal account.Input allowed - Valid CATEGORY |
| 3 | `CAMB.ALP.CAMB.MKT.10` | `CambAllTellerParam_CambMkt10` | TField |  | Field is used to define the currency market for TFS CASH type transaction which involves transaction in different currency, the currency market defined here is used for conversion rate.Validation - records of CURRENCY.MARKET modified |
| 4 | `CAMB.ALP.CAMB.MKT.11` | `CambAllTellerParam_CambMkt11` | TField |  | Field used to define the currency market for TFS CHEQUE transaction which involves transaction in different currency, the currency market defined here is used for conversion rate modified |
| 5 | `CAMB.ALP.CAMB.CASH.IN` | `CambAllTellerParam_CambCashIn` |  |  |  |
| 6 | `CAMB.ALP.CAMB.CASH.OUT` | `CambAllTellerParam_CambCashOut` |  |  |  |
| 7 | `CAMB.ALP.CAMB.NONMEM` | `CambAllTellerParam_CambNonmem` | TField |  | For bill payment functionality and TFS functionality, the non-customer may wish to do some financial transaction.This field holds the account mnemonic which will be defaulted automatically which does the TFS or bill payment.Validation : field NONMEM.ACCT in TFS is validated against this field, if value matches, system uses the category defined in NONMEMBER.CAT to form the account for posting entries.The value should be NONMEMBER.Note: There must be an internal or dummy customer account with MNEMONIC as NONMEM |
| 8 | `CAMB.ALP.CAMB.V.AML.PERS` | `CambAllTellerParam_CambVAmlPers` | TField |  | Field is obsolete. Not in use modified |
| 9 | `CAMB.ALP.CAMB.V.AML.NPERS` | `CambAllTellerParam_CambVAmlNpers` | TField |  | Field is obsolete. Not in use |
| 10 | `CAMB.ALP.CAMB.UB.NONM.CHQ` | `CambAllTellerParam_CambUbNonmChq` |  |  |  |
| 11 | `CAMB.ALP.CASH.CAT` | `CambAllTellerParam_CashCat` | TField |  | For bill payment functionality, the customer may wish to pay the bill in branch using Cash (Non customer)This field is used to define the cash account category.This field is also used to displaying the cash position of teller. This field is used to determine the cash account categoryNote: there must be an internal account with this category code. |
| 12 | `CAMB.ALP.CLEARING.CAT` | `CambAllTellerParam_ClearingCat` | TField |  | This field is used to define the category code used for cheque clearing. (Used in EOD balancing screen - Submit cheque for clearing)Validation - record of CATEGORY table. |
| 13 | `CAMB.ALP.ATM.CAT` | `CambAllTellerParam_AtmCat` | TField |  | This field is used to define the category code to derive the ATM account.Validation - record of CATEGORY table. |
| 14 | `CAMB.ALP.RECYCLER.CAT` | `CambAllTellerParam_RecyclerCat` | TField |  | This field is used to define the category code to derive the recycler account. Needed for EOD balancing screen to cash from recycler to till or vault.Validation - record of CATEGORY table. |
| 15 | `CAMB.ALP.VAULT.CAT` | `CambAllTellerParam_VaultCat` | TField |  | This field is used to define the category code to derive the recycler account. Needed for EOD balancing screen to define the value accountValidation - record of CATEGORY table. |
| 16 | `CAMB.ALP.BRINKS.CAT` | `CambAllTellerParam_BrinksCat` | TField |  | This field is used to define the category code to derive the brinks account, used for cash shipment. Needed for EOD balancing screen.Validation - record of CATEGORY table. |
| 17 | `CAMB.ALP.DEPOSITS` | `CambAllTellerParam_Deposits` |  |  |  |
| 18 | `CAMB.ALP.WITHDRAWALS` | `CambAllTellerParam_Withdrawals` |  |  |  |
| 19 | `CAMB.ALP.TRANSFERS` | `CambAllTellerParam_Transfers` |  |  |  |
| 20 | `CAMB.ALP.FRGN.EXCHANGE` | `CambAllTellerParam_FrgnExchange` |  |  |  |
| 21 | `CAMB.ALP.SERVICES` | `CambAllTellerParam_Services` |  |  |  |
| 22 | `CAMB.ALP.FTTC.FPOST` | `CambAllTellerParam_FttcFpost` |  |  |  |
| 23 | `CAMB.ALP.CAMB.ACCOUNT.CLASS` | `CambAllTellerParam_CambAccountClass` |  |  |  |
| 24 | `CAMB.ALP.OFF.CHQ.CAT` | `CambAllTellerParam_OffChqCat` | TField |  | For issuing office cheque, this field is referred to form an internal account to be credited.Validation - record from CATEGORY table. |
| 25 | `CAMB.ALP.EOD.TELL.TRAN.CHEQ` | `CambAllTellerParam_EodTellTranCheq` | TField |  | Used to define the CHEQUE related TFS.TRANSACTION for EOD balancing screen to list cheque position of tellerTELLER transaction matching the field value is considered as Cheque related transactions.Used in the End of Day Balancing screen Enquires. |
| 26 | `CAMB.ALP.EOD.TELL.TRAN.TC` | `CambAllTellerParam_EodTellTranTc` | TField |  | Used to define the TRAVALLER CHEQUE related TFS.TRANSACTION for EOD balancing screen to list cheque position of tellerTeller transaction matching the field value is considered as TC related transactions.Used in the End of Day Balancing screen Enquires. |
| 27 | `CAMB.ALP.EOD.EXCL.CURR` | `CambAllTellerParam_EodExclCurr` |  |  |  |
| 28 | `CAMB.ALP.EOD.TFS.TRANS` | `CambAllTellerParam_EodTfsTrans` |  |  |  |
| 29 | `CAMB.ALP.EOD.PAP.BILLS` | `CambAllTellerParam_EodPapBills` | TField |  | Paper bill related description to be entered here.Valid Input "PAPERBILL"applicable when issuing a paper bills using the version, FUNDS.TRANSFER,CAMB.PAPER.BILLS.NONMEMBERFUNDS.TRANSFER,CAMB.PAPER.BILLSeg. PAPERBILLS |
| 30 | `CAMB.ALP.EOD.OFCQ` | `CambAllTellerParam_EodOfcq` | TField |  | OFFICE cheque related description to be entered here.Valid Input "OFCQ"applicable when issuing a office cheque using version FUNDS.TRANSFER,CAMB.OFF.CHEQ.NONMEMBERFUNDS.TRANSFER,CAMB.OFF.CHQeg. OFCQ |
| 31 | `CAMB.ALP.OFF.CHQ.SEL` | `CambAllTellerParam_OffChqSel` | TField |  | Field to store the Valid ID from CAMB.W.SAM.REC.EXT.PARAM to consider for office cheque selection for Match and Kill process.Usage in Other negotiable enquries of End of Day balancing screenValidation - record from CAMB.W.SAM.REC.EXT.PARAMeg. OFCQ |
| 32 | `CAMB.ALP.OFF.CHQ.COMM` | `CambAllTellerParam_OffChqComm` | TField |  |  |
| 33 | `CAMB.ALP.OFCQ.TRN.TYPE` | `CambAllTellerParam_OfcqTrnType` |  |  |  |
| 34 | `CAMB.ALP.PAPBILL.TRN.TYPE` | `CambAllTellerParam_PapbillTrnType` |  |  |  |
| 35 | `CAMB.ALP.PAP.BILLS.ACCT.IDS` | `CambAllTellerParam_PapBillsAcctIds` |  |  |  |
| 36 | `CAMB.ALP.SUBMIT.CHQ.CONSOL` | `CambAllTellerParam_SubmitChqConsol` | TField |  | The purpose of this field is used to consolidate the cheque transactions in the EOD balancing screen for cheque position enquiry (CAMB.TT.CHQ.POSITION). This will consolidate the cheque transactions on currency wise.Yes - Consolidation will be done.No/None - Consolidation will not be done and each entry will be reported separately in the enquiry. |
| 37 | `CAMB.ALP.CHQ.TT.TYPE` | `CambAllTellerParam_ChqTtType` |  |  |  |
| 38 | `CAMB.ALP.RESERVED.2` | `CambAllTellerParam_Reserved2` | TField |  |  |
| 39 | `CAMB.ALP.RESERVED.3` | `CambAllTellerParam_Reserved3` | TField |  |  |
| 40 | `CAMB.ALP.RESERVED.4` | `CambAllTellerParam_Reserved4` | TField |  |  |
| 41 | `CAMB.ALP.RESERVED.5` | `CambAllTellerParam_Reserved5` | TField |  |  |
| 42 | `CAMB.ALP.LOCAL.REF` | `CambAllTellerParam_LocalRef` |  |  |  |
| 43 | `CAMB.ALP.RECORD.STATUS` | `CambAllTellerParam_RecordStatus` | String |  |  |
| 44 | `CAMB.ALP.CURR.NO` | `CambAllTellerParam_CurrNo` | String |  |  |
| 45 | `CAMB.ALP.INPUTTER` | `CambAllTellerParam_Inputter` |  |  |  |
| 46 | `CAMB.ALP.DATE.TIME` | `CambAllTellerParam_DateTime` |  |  |  |
| 47 | `CAMB.ALP.AUTHORISER` | `CambAllTellerParam_Authoriser` | String |  |  |
| 48 | `CAMB.ALP.CO.CODE` | `CambAllTellerParam_CoCode` | String |  |  |
| 49 | `CAMB.ALP.DEPT.CODE` | `CambAllTellerParam_DeptCode` | String |  |  |
| 50 | `CAMB.ALP.AUDITOR.CODE` | `CambAllTellerParam_AuditorCode` | String |  |  |
| 51 | `CAMB.ALP.AUDIT.DATE.TIME` | `CambAllTellerParam_AuditDateTime` | String |  |  |
