# SEPA.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SEPA.PARAMETER` in `EP_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.PAR.FILE.DIRECTION` | `SepaParameter_FileDirection` |  |  |  |
| 2 | `SEP.PAR.FIXED.SELECTION` | `SepaParameter_FixedSelection` |  |  |  |
| 3 | `SEP.PAR.LOAD.ROUTINE` | `SepaParameter_LoadRoutine` |  |  |  |
| 4 | `SEP.PAR.DEFAULT.FTTC` | `SepaParameter_DefaultFttc` |  |  |  |
| 5 | `SEP.PAR.TYPE.OF.FORMAT` | `SepaParameter_TypeOfFormat` |  |  |  |
| 6 | `SEP.PAR.SUSPENS.ACCT.NO` | `SepaParameter_SuspensAcctNo` |  |  |  |
| 7 | `SEP.PAR.NOSTRO.ACCT.NO` | `SepaParameter_NostroAcctNo` |  |  |  |
| 8 | `SEP.PAR.TRANSIT.ACCT.DB` | `SepaParameter_TransitAcctDb` |  |  |  |
| 9 | `SEP.PAR.TRANSIT.ACCT.CR` | `SepaParameter_TransitAcctCr` |  |  |  |
| 10 | `SEP.PAR.DUPLICATE.PROC` | `SepaParameter_DuplicateProc` |  |  |  |
| 11 | `SEP.PAR.VALIDATE.RTN` | `SepaParameter_ValidateRtn` |  |  |  |
| 12 | `SEP.PAR.AFT.AUTH.RTN` | `SepaParameter_AftAuthRtn` |  |  |  |
| 13 | `SEP.PAR.PROCESS.SWITCH` | `SepaParameter_ProcessSwitch` |  |  |  |
| 14 | `SEP.PAR.COMMIT.NUMBER` | `SepaParameter_CommitNumber` |  |  |  |
| 15 | `SEP.PAR.SEQUENCE.DIGITS` | `SepaParameter_SequenceDigits` |  |  |  |
| 16 | `SEP.PAR.MAXIMUM.AMOUNT` | `SepaParameter_MaximumAmount` |  |  |  |
| 17 | `SEP.PAR.PENDING.DAYS` | `SepaParameter_PendingDays` |  |  |  |
| 18 | `SEP.PAR.MAP.FIELDS` | `SepaParameter_MapFields` |  |  |  |
| 19 | `SEP.PAR.MAP.MANDATORY` | `SepaParameter_MapMandatory` |  |  |  |
| 20 | `SEP.PAR.APPLICATION` | `SepaParameter_Application` |  |  |  |
| 21 | `SEP.PAR.VALIDATE.ROUTINE` | `SepaParameter_ValidateRoutine` |  |  |  |
| 22 | `SEP.PAR.BANK.DEF.BRANCH` | `SepaParameter_BankDefBranch` | A (Alphanumeric) |  | This field specifies the Default branch of the T24 bank. Validation rule Value upto 35 type A (Alphanumeric) |
| 23 | `SEP.PAR.BANK.NAME` | `SepaParameter_BankName` | TField | Yes | This field holds the Name of the T24 bank. Validation rule Value from 2 to 32 type S (SWIFT Character). Mandatory field |
| 24 | `SEP.PAR.BANK.BIC.CODE` | `SepaParameter_BankBicCode` | A (Alphanumeric) |  | This field holds the BIC identification of the T24 bank. This value is used while updating the sender information of the outward message Validation rule Value upto 11 type A (Alphanumeric) |
| 25 | `SEP.PAR.MSG.NATURE` | `SepaParameter_MsgNature` |  |  |  |
| 26 | `SEP.PAR.PEACH.ID` | `SepaParameter_PeachId` |  |  |  |
| 27 | `SEP.PAR.CUSTOMER.POSTING` | `SepaParameter_CustomerPosting` | TField |  | This field defines how the accounting entry for a destination customer in a CUSTOMER.TO.BANK XML is being processed �FT�: Processed through a generated FT. �SO�: Posting to SEPA outward. �SI�: Posting through SEPA inward. Validation rule Value must be 2 characters and user can input only &apos;FT� �SI� and �SO� |
| 28 | `SEP.PAR.PROCESS.TYPE` | `SepaParameter_ProcessType` | TField |  | This field specifies the Default process type for a transaction if none is associated to its own definition: �SAO�: Direct booking on the customer account whatever its status might be. �SNP�: Direct booking on the customer account unless blocked by an override message in which case the booking is done on a transit account and one accept manual FUNDS.TRANSFER is initiated (IN). �RET�: Booking on a transit account and generation of a return on SEPA.FOLLOW.UP, if possible, automatically authorized. �MAN�: Booking on a transit account and simultaneous non validated generation of a manual FUNDS.TRANSFER to accept and of a return/refund SEPA.FOLLOW.UP record. The manual validation of one of them will later remove the other one. �ALL�: Processing attempt in �SNP� and if it fails, switching to�MAN� option. Value highly recommended for that field. &apos;OFT&apos; : Only FT. Every transaction in SEPA will create an entry in core FT and entries will be posted only through FT. Validation rule Value upto 3 and user can input only &apos;SAO&apos; &apos;SNP&apos; &apos;RET&apos; &apos;MAN&apos; &apos;ALL&apos; and &apos;OFT&apos; |
| 29 | `SEP.PAR.CLEAR.CURRENCY` | `SepaParameter_ClearCurrency` | A (Alphanumeric) |  | This fields specifies the Interface Currency being used and it is defaulted with Value &apos;EUR&apos; Validation rule Value upto 4 type A (Alphanumeric) and Value must exist in CURRENCY Application |
| 30 | `SEP.PAR.CLEAR.CCY.MARKET` | `SepaParameter_ClearCcyMarket` | TField |  | This field holds the value of the Interface market code and it is defaulted with the Value &apos;1&apos; Validation rule Value upto 2 and Value must exist in CURRENCY.MARKET Application |
| 31 | `SEP.PAR.SUFFIX.BY.DEFAULT` | `SepaParameter_SuffixByDefault` | TField |  | This field specifies the Suffix of any internal account defined by its ACCOUNT.CLASS whenever initial account officer is unknown. Validation rule Value upto 4 |
| 32 | `SEP.PAR.BIC.ENRICHMENT.RTN` | `SepaParameter_BicEnrichmentRtn` | A (Alphanumeric) |  | This field provides the name of the routine used to add an enrichment narrative on a given BIC code. The standard @SEPA.BANK.ENRICH is using the delivered SEPA.BANK table. Validation rule Value upto 35 type A (Alphanumeric) |
| 33 | `SEP.PAR.DELIVERY.ROUTINE` | `SepaParameter_DeliveryRoutine` | A (Alphanumeric) |  | This field holds the name of the routine used by default to generate the customer�s advice @SEPA.FUP.DELIVERY is provided. This delivery routine is the only one in the SEPA application requiring arguments: Arguments IN : MAPPING.KEY&lt;1,1&gt; Key to DE.MAPPING MAPPING.KEY&lt;1,2&gt; Value of APP.FORMAT REVERSE.FLAG �R� in case of reverse, �� otherwise Arguments OUT : DELIVERY.REF Key of the T24 generated advice ERROR.MESSAGE Advice posting failure reason, if any Validation rule Value upto 35 type A (Alphanumeric) |
| 34 | `SEP.PAR.PENDING.SUFFIX.RTN` | `SepaParameter_PendingSuffixRtn` | A (Alphanumeric) |  | This field Gives the name of the routine that calculates the suffix code to be added to the SEPA.OUTWARD.PENDING key. This to allow a selection (grouping) of the outward transactions prior to the outgoing files generation via outward LOAD.ROUTINE. Validation rule Value upto 35 type A (Alphanumeric) |
| 35 | `SEP.PAR.DEBUG.OUTWARD` | `SepaParameter_DebugOutward` | TField |  | This field is defaulted with the Value &apos;Y&apos; which denotes &apos;storage of one record per outward transaction in the TOOLS library with detail of its elements� mapping&apos; Validation rule Value upto 1 and user can Input only &apos;Y&apos; |
| 36 | `SEP.PAR.ENTRIES.BY.LINE` | `SepaParameter_EntriesByLine` | TField |  | This field is defaulted with the Value &apos;Y&apos; which denotes Forced accounting entries on every inward and outward transactions. Allows the use of other accounts that those calculated by SEPA standard parameter tables using a validation routine. Validation rule Value upto 1 and user can Input only &apos;Y&apos; |
| 37 | `SEP.PAR.SEPARATOR` | `SepaParameter_Separator` | TField |  | This field specifies the Character to be used to concatenate the SEPA file identification with the rank of its multi-valued XML messages. Validation rule Value upto 1 type ANY (Any Character) |
| 38 | `SEP.PAR.APPLICATION.ID` | `SepaParameter_ApplicationId` |  |  |  |
| 39 | `SEP.PAR.EB.SYSTEM.ID` | `SepaParameter_EbSystemId` |  |  |  |
| 40 | `SEP.PAR.STO.PAY.METHOD` | `SepaParameter_StoPayMethod` |  |  |  |
| 41 | `SEP.PAR.PATH.SEPA.BIC.DIR` | `SepaParameter_PathSepaBicDir` | TField |  | This field specifies the Path where the SWIFT published SEPA Directory will be stored. This file can be uploaded directly to SEPA.BANK through a routine. Validation rule Value upto 50 type ANY (Any Character) |
| 42 | `SEP.PAR.NAT.BANK.BRANCH.CD` | `SepaParameter_NatBankBranchCd` | A (Alphanumeric) |  | This field contains the Bank branch code to calculate IBAN Validation rule Value upto 20 type A (Alphanumeric) |
| 43 | `SEP.PAR.DIRECTION.TYPE` | `SepaParameter_DirectionType` |  |  |  |
| 44 | `SEP.PAR.GENERATE.FT.RTN` | `SepaParameter_GenerateFtRtn` |  |  |  |
| 45 | `SEP.PAR.UPDATE.FILE` | `SepaParameter_UpdateFile` | A (Alphanumeric) |  | This fields specifies update to concat files and TOOLS to happen if set to 'Y' Validation rule Value upto 1 type A (Alphanumeric) and Value allowed 'Y' or null |
| 46 | `SEP.PAR.PSD.ROUTINE` | `SepaParameter_PsdRoutine` | TField |  | This field holds the value of the routine used to validate the PSD compliance Validation rule Value upto 50 type ANY (Any Character) and Value must exist in EB.API Application |
| 47 | `SEP.PAR.SDD.ADDNL.CHK.RTN` | `SepaParameter_SddAddnlChkRtn` | TField |  | This field provides the name of the routine used for additional validation over SEPA.MANDATE.ID Eg: When Buisness code in Creditor ID needs to be validated and by passed Validation rule Value upto 35 type ANY (Any Character) |
| 48 | `SEP.PAR.CUSTOMER.NETTING` | `SepaParameter_CustomerNetting` | A (Alphanumeric) |  | This field specifies Netting of transactions to Customer Account till the settlement date is applicable when set to 'Y' Validation rule Value upto 1 type A (Alphanumeric) and Value allowed 'Y' or null |
| 49 | `SEP.PAR.NET.SUSPENS.ACCT` | `SepaParameter_NetSuspensAcct` | A (Alphanumeric) |  | This field contains the Value of the default account that replaces the SUSPENS.ACCT.NO, whenever customer Netting is set to Y Validation rule Value upto 16 type A (Alphanumeric). Value should exist in ACCOUNT Application |
| 50 | `SEP.PAR.ON.US.TRANS` | `SepaParameter_OnUsTrans` | A (Alphanumeric) |  | This field specifies whether PACS files needs to be generated for Inward Processing, when a PAIN InHouse transaction is processed, when set to 'Y' Validation rule Value upto 1 type A (Alphanumeric) and Value allowed 'Y' or null |
| 51 | `SEP.PAR.NMS.OPT.IBAN.ONLY` | `SepaParameter_Reserved7` |  |  |  |
| 52 | `SEP.PAR.RESERVED6` | `SepaParameter_Reserved6` | TField |  |  |
| 53 | `SEP.PAR.RESERVED5` | `SepaParameter_Reserved5` | TField |  |  |
| 54 | `SEP.PAR.RESERVED4` | `SepaParameter_Reserved4` | TField |  |  |
| 55 | `SEP.PAR.RESERVED3` | `SepaParameter_Reserved3` | TField |  |  |
| 56 | `SEP.PAR.RESERVED2` | `SepaParameter_Reserved2` | TField |  |  |
| 57 | `SEP.PAR.RESERVED1` | `SepaParameter_Reserved1` | TField |  |  |
| 58 | `SEP.PAR.LOCAL.REF` | `SepaParameter_LocalRef` |  |  |  |
| 59 | `SEP.PAR.OVERRIDE` | `SepaParameter_Override` |  |  |  |
| 60 | `SEP.PAR.RECORD.STATUS` | `SepaParameter_RecordStatus` | String |  |  |
| 61 | `SEP.PAR.CURR.NO` | `SepaParameter_CurrNo` | String |  |  |
| 62 | `SEP.PAR.INPUTTER` | `SepaParameter_Inputter` |  |  |  |
| 63 | `SEP.PAR.DATE.TIME` | `SepaParameter_DateTime` |  |  |  |
| 64 | `SEP.PAR.AUTHORISER` | `SepaParameter_Authoriser` | String |  |  |
| 65 | `SEP.PAR.CO.CODE` | `SepaParameter_CoCode` | String |  |  |
| 66 | `SEP.PAR.DEPT.CODE` | `SepaParameter_DeptCode` | String |  |  |
| 67 | `SEP.PAR.AUDITOR.CODE` | `SepaParameter_AuditorCode` | String |  |  |
| 68 | `SEP.PAR.AUDIT.DATE.TIME` | `SepaParameter_AuditDateTime` | String |  |  |
