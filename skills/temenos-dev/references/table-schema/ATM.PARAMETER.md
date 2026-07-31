# ATM.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ATM.PARAMETER` in `ATMFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ATM.PARA.BANK.IMD` | `AtmParameter_BankImd` | TField | Yes | This is a mandatory field which stores the unique IMD for the bank for the ATM |
| 2 | `ATM.PARA.NETWORK.IMD` | `AtmParameter_NetworkImd` |  |  |  |
| 3 | `ATM.PARA.FILE.TYPE` | `AtmParameter_FileType` |  |  |  |
| 4 | `ATM.PARA.FILE.NAME` | `AtmParameter_FileName` |  |  |  |
| 5 | `ATM.PARA.FILE.PATH` | `AtmParameter_FilePath` |  |  |  |
| 6 | `ATM.PARA.DAYS.IN.HIST` | `AtmParameter_DaysInHist` | TField |  | Days before the log file are to be archived |
| 7 | `ATM.PARA.OFS.USER` | `AtmParameter_OfsUser` | TField |  | User Sign on to be used by OFS. |
| 8 | `ATM.PARA.OFS.PASSWORD` | `AtmParameter_OfsPassword` |  |  |  |
| 9 | `ATM.PARA.DEF.ATM.BRANCH` | `AtmParameter_DefAtmBranch` | TField |  | If Terminal Id was not configured for every terminal in ATM.TERMINAL.ACCT, then default Terminal id stored here will be taken and processed. |
| 10 | `ATM.PARA.DEF.ATM.BIN` | `AtmParameter_DefAtmBin` | TField |  | If Other Bank Bin was not configured for every terminal in ATM.TERMINAL.ACCT, then default bin stored here will be taken and processed. |
| 11 | `ATM.PARA.DEF.POS.MRCNT` | `AtmParameter_DefPosMrcnt` | TField |  | If any Bank owned POS device id for every device was not configured in ATM.TERMINAL.ACCT, then default device id stored here will be taken and processed. |
| 12 | `ATM.PARA.DEF.POS.BIN` | `AtmParameter_DefPosBin` | TField |  | If Other Bank Pos Device Id for every device was not configured in ATM.TERMINAL.ACCT, then default device id stored here will be taken and processed. |
| 13 | `ATM.PARA.CHG.CCY.POS` | `AtmParameter_ChgCcyPos` | TField |  | Currency position for raising charge entries |
| 14 | `ATM.PARA.TXN.CCY.POS` | `AtmParameter_TxnCcyPos` | TField |  | Currency position for raising charge entries |
| 15 | `ATM.PARA.MSG.ID` | `AtmParameter_MsgId` | TField | Yes | This is a mandatory field stores the type of ISO Message format used for validating the incoming requests. IF 5002 is set, then BASE24 based Messages can be posted. If 5003 is set, then standard ISO Messages can be posted. If 5004 is set, then PHOENIX based messages can be posted. |
| 16 | `ATM.PARA.UNIQUE.ID` | `AtmParameter_UniqueId` | TField |  | ISO Message Fields will be stored here. Data from these fields will be generated as Unique Id for each transaction. Customized routine can also be attached here. Specify either: i) A jBC subroutine name, or ii)For java implementations: An EB.API record id with a source type of METHOD which implements an interface defined in the EB.API record ATM.PARAMETER.UNIQUE.ID.HOOK. This field supports the AtmMessageLifecycle.getAtmTransactionId() method. The AtmMessageLifecycle class is in the com.temenos.t24.api.hook.atm package which is in ATMFRM_MessageHook.jar shipped with T24. |
| 17 | `ATM.PARA.GEN.COM.CODE` | `AtmParameter_GenComCode` | TField |  | Default Company Code. |
| 18 | `ATM.PARA.LOCK.PERIOD` | `AtmParameter_LockPeriod` | TField |  | For Authorization request transactions, the lock period mentioned will be used for locking the amount. User has to input it as e.g.:+10C. |
| 19 | `ATM.PARA.DUAL.TXN.ID` | `AtmParameter_DualTxnId` | TField |  | ISO Message Fields will be stored here .Unique id for releasing the locked amount and raising accounting entry. Customized routine can also be attached here Routine attached could be either: A jBC implementation by using an EB.API record with a source type of BASIC. For java implementations: An EB.API record id with a source type of HOOK which implements an interface defined in the EB.API record ATM.DUAL.TXN.ID.HOOK. This field supports the AtmMessageLifecycle.getDualTransactionId() method. The AtmMessageLifecycleclass is in the com.temenos.t24.api.hook.atm package which is in ATMFRM_MessageHook.jar shipped with T24. |
| 20 | `ATM.PARA.CHG.OFS.SOURC` | `AtmParameter_ChgOfsSourc` | TField |  | OFS SOURCE stored here can be used for raising charges or can be used in any customized hook routines for raising Separate Transactions. |
| 21 | `ATM.PARA.ATM.GEN.MSG.ID` | `AtmParameter_AtmGenMsgId` | TField |  | This field stores the type of ISO Message format used for initiating ISO Message from T24 side. |
| 22 | `ATM.PARA.ATM.GEN.API.ID` | `AtmParameter_AtmGenApiId` | TField |  | This field stores java EB.API for connecting to switch. |
| 23 | `ATM.PARA.PHX.BAL.FMT.TYPE` | `AtmParameter_PhxBalFmtType` | TField |  | This field used only in PHOENIX Interface. If ACTUAL is set, then Actual Balance alone will be sent for all transactions. If AVAILABLE is set, then Available Balance alone will be sent for all transactions. If BOTH is set, Actual and Available balance will be sent for all transactions. |
| 24 | `ATM.PARA.LOG.TYPE` | `AtmParameter_LogType` | TField |  | Stores whether the log type is DUMP or LOG4J.Allowed values are stored on the lookup files for ATM.LOG.TYPE |
| 25 | `ATM.PARA.LOG.RTN` | `AtmParameter_LogRtn` | TField |  | This routine will be called from within the log message routine. Any additional processing required can be handled through this routine. For future use |
| 26 | `ATM.PARA.LOG.PATH` | `AtmParameter_LogPath` | TField |  | Stores the file path where the incoming ISO requests are stored. |
| 27 | `ATM.PARA.AMT.FMT` | `AtmParameter_AmtFmt` | TField |  | This field is used for formatting the amount to be returned in ISO Response Message. The formats are specified in EB.LOOKUP for ATM.FMT. The balance amount being processed for statement generation will use add the credit/debit indicators as mentioned in the format |
| 28 | `ATM.PARA.AMT.LENGTH` | `AtmParameter_AmtLength` | TField |  | Provides the length of the amount field which will be returned in ISO Response message. |
| 29 | `ATM.PARA.REQ.VERSION` | `AtmParameter_ReqVersion` |  |  |  |
| 30 | `ATM.PARA.REQ.MAPPING` | `AtmParameter_ReqMapping` |  |  |  |
| 31 | `ATM.PARA.LOCAL.REF` | `AtmParameter_LocalRef` |  |  |  |
| 32 | `ATM.PARA.DEF.RES.MAP.ID` | `AtmParameter_DefResMapId` | TField |  | If INTRF.MAPPING Request record invalid then response ISO message will form by using the DEF.RES.MAP.ID |
| 33 | `ATM.PARA.INTERFACE.TO` | `AtmParameter_InterfaceTo` | TField |  | This field used for OFS Clearing Process, If CLEARING is set then process the ac.inward.entry transactions |
| 34 | `ATM.PARA.LOCK.REV.VERSION` | `AtmParameter_LockRevVersion` | TField |  | In case of clearing request, this field is used to define the version for reversing AC.LOCKED.EVENTS when a Reversal of Authorisation request is received.In case of Non-clearing request, this field is used to define the version for reversing AC.LOCKED.EVENTS while processsing a Dual transaction request |
| 35 | `ATM.PARA.ISSUER.BIN` | `AtmParameter_IssuerBin` |  |  |  |
| 36 | `ATM.PARA.FF.TRANSACTION.LIMIT` | `AtmParameter_FfTransactionLimit` | TField |  | This field used to define Fast funds authorization amount limit. |
| 37 | `ATM.PARA.FF.SUSPENSE.ACCOUNT` | `AtmParameter_FfSuspenseAccount` | TField |  | This field used to define Suspense account which will be debited during Fast funds request |
| 38 | `ATM.PARA.PAN.MASKING` | `AtmParameter_PanMasking` | TField |  | If set to "YES" then PAN number is masked in ATM logs and ATM.TRANSACTION to support PCI compliance |
| 39 | `ATM.PARA.ATM.CHARGE.CONFIG` | `AtmParameter_AtmChargeConfig` | TField |  |  |
| 40 | `ATM.PARA.RECORD.STATUS` | `AtmParameter_RecordStatus` | String |  |  |
| 41 | `ATM.PARA.CURR.NO` | `AtmParameter_CurrNo` | String |  |  |
| 42 | `ATM.PARA.INPUTTER` | `AtmParameter_Inputter` |  |  |  |
| 43 | `ATM.PARA.DATE.TIME` | `AtmParameter_DateTime` |  |  |  |
| 44 | `ATM.PARA.AUTHORISER` | `AtmParameter_Authoriser` | String |  |  |
| 45 | `ATM.PARA.CO.CODE` | `AtmParameter_CoCode` | String |  |  |
| 46 | `ATM.PARA.DEPT.CODE` | `AtmParameter_DeptCode` | String |  |  |
| 47 | `ATM.PARA.AUDITOR.CODE` | `AtmParameter_AuditorCode` | String |  |  |
| 48 | `ATM.PARA.AUDIT.DATE.TIME` | `AtmParameter_AuditDateTime` | String |  |  |
| 49 | `ATM.PARA.ADVICE.MESSAGE` | `AtmParameter_AdviceMessage` | TField |  | This field is set to YES ,In order to generate advice message response for the zero dollar transaction/for the ISO message which has unsuccessful response code |
| 50 | `ATM.PARA.ADVICE.MESSAGE.ID` | `AtmParameter_AdviceMessageId` | TField |  | Input this field as CSM0200999999 , If ADVICE.MESSAGE is set to YES |
| 51 | `ATM.PARA.PARTIAL.AUTH.DATA.ELEMENT` | `AtmParameter_PartialAuthDataElement` |  |  |  |
| 52 | `ATM.PARA.PARTIAL.AUTH.CODE` | `AtmParameter_PartialAuthCode` |  |  |  |
| 53 | `ATM.PARA.RESERVED.1` | `AtmParameter_Reserved.1` |  |  |  |
| 54 | `ATM.PARA.SERVICE.PROVIDER` | `AtmParameter_ServiceProvider` | TField |  | Specifies the ATM service provider of the bank.If this field is defined,then the INTRF.MAPPING records suffixed with this value should be selected for processing Allowed values: Blank 01 - Visa DPS 02 - ACI worldwide |
| 55 | `ATM.PARA.INCREMENTAL.AUTH.DE` | `AtmParameter_IncrementalAuthDe` | TField |  | Specifies the data element, sub-field and position where the indicator for incremental authorisation will be present in the ISO Authorisation request |
| 56 | `ATM.PARA.INCREMENTAL.AUTH.CODE` | `AtmParameter_IncrementalAuthCode` |  |  |  |
| 57 | `ATM.PARA.INCLUDE.CR.RESERVE.BAL` | `AtmParameter_IncludeCrReserveBal` | TField |  | This field is set to YES ,to include the Credit Reserve amount in Available balance |
