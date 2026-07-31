# LUCUPI.CARD.FINTRAN — Table Schema

> Source: `INSERTS/I_F.LUCUPI.CARD.FINTRAN` in `LUCUPI_CardsProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LUCUPI.CARD.FINTRAN.FILE.NAME` | `LucupiCardFintran_FileName` | TField |  | Name of the file received from SIX Ex: PREE20190322HHMMSS.XX. |
| 2 | `LUCUPI.CARD.FINTRAN.CARD.TYPE` | `LucupiCardFintran_CardType` | TField |  | Company identifier EUROPAYLUX if cyclic PREL for license managing company ERPLUX otherwise : name of license managing company (CDE_STE_GESTION) |
| 3 | `LUCUPI.CARD.FINTRAN.FILE.DATE` | `LucupiCardFintran_FileDate` | TField |  | This field denotes File creation date YYYYMMDD |
| 4 | `LUCUPI.CARD.FINTRAN.SWIFT.CODE` | `LucupiCardFintran_SwiftCode` | TField |  | Issuing bank swift code PRELMENS : issuing bank swift code PRELGEST : swift code of the administrative bank (some banks use a domiciled account in another bank � this other bank is the administrative bank) |
| 5 | `LUCUPI.CARD.FINTRAN.AWARD.REFERENCE` | `LucupiCardFintran_AwardReference` | TField |  | Reference of the award : R.yyyymmdd.PDI R.yyyymmdd.RDI R.yyyymmdd.PRG R.yyyymmdd.RRG |
| 6 | `LUCUPI.CARD.FINTRAN.P.NOSTRO.ACCOUNT` | `LucupiCardFintran_PNostroAccount` | TField |  | Header account for the transactions with ACCOUNT.MOVEMENT.TYPE as PIM or PDI. |
| 7 | `LUCUPI.CARD.FINTRAN.R.NOSTRO.ACCOUNT` | `LucupiCardFintran_RNostroAccount` | TField |  | Header account for the transactions with ACCOUNT.MOVEMENT.TYPE as RIM or RDI. |
| 8 | `LUCUPI.CARD.FINTRAN.ACCOUNT.MOVEMENT.TYPE` | `LucupiCardFintran_AccountMovementType` | TField |  | This field is used to indicate the type of transaction movement. Type of account movement PDI RDI PRG RRG |
| 9 | `LUCUPI.CARD.FINTRAN.HEADER.SEQ.NO` | `LucupiCardFintran_HeaderSeqNo` | TField |  | Batch sequence number within file |
| 10 | `LUCUPI.CARD.FINTRAN.DATARECORD.SEQ.NO` | `LucupiCardFintran_DatarecordSeqNo` | TField |  | Message sequence number from 0001 |
| 11 | `LUCUPI.CARD.FINTRAN.CARDHOLDER.BANK` | `LucupiCardFintran_CardholderBank` | TField |  | Cardholder bank code (issuing bank swift code) |
| 12 | `LUCUPI.CARD.FINTRAN.TOWN.CODE` | `LucupiCardFintran_TownCode` | TField |  | Town code (Example : LL for Luxembourg, BB for Bruxelles) |
| 13 | `LUCUPI.CARD.FINTRAN.CARDHOLDER.ACCOUNT` | `LucupiCardFintran_CardholderAccount` | TField |  | Cardholder account number to debit if levy to credit if payback. |
| 14 | `LUCUPI.CARD.FINTRAN.CARD.CURRENCY` | `LucupiCardFintran_CardCurrency` | TField |  | ISO cardholder currency code |
| 15 | `LUCUPI.CARD.FINTRAN.CARD.AMOUNT` | `LucupiCardFintran_CardAmount` | TField |  | Cardholder amount to debit if levy to credit if payback |
| 16 | `LUCUPI.CARD.FINTRAN.CARD.AMT.EURO` | `LucupiCardFintran_CardAmtEuro` | TField |  | cardholder amount in EURO to debit if levy to credit if payback |
| 17 | `LUCUPI.CARD.FINTRAN.CARDHOLDER.NAME` | `LucupiCardFintran_CardholderName` | TField |  | This field contains cardholder name |
| 18 | `LUCUPI.CARD.FINTRAN.CARD.NUMBER` | `LucupiCardFintran_CardNumber` | TField |  | This field contains cardholder's card number |
| 19 | `LUCUPI.CARD.FINTRAN.CARD.EXPIRY.DATE` | `LucupiCardFintran_CardExpiryDate` | TField |  | This field contains card's expiration date(YYMM) |
| 20 | `LUCUPI.CARD.FINTRAN.CARD.SEQ.NO` | `LucupiCardFintran_CardSeqNo` | TField |  | This field contains card's sequence number |
| 21 | `LUCUPI.CARD.FINTRAN.FEE.AMT` | `LucupiCardFintran_FeeAmt` | TField |  | Fee amount (commission fee amount + processing fee amount) |
| 22 | `LUCUPI.CARD.FINTRAN.TRANSACTION.REGION` | `LucupiCardFintran_TransactionRegion` | TField |  | Transaction region ONUS = Six/Cetrel network BANK = bank network INTL = outside Europe EURO = Europe outside ONUS |
| 23 | `LUCUPI.CARD.FINTRAN.PRODUCT.LABEL` | `LucupiCardFintran_ProductLabel` | TField |  | product label Example : VISACLAS , MAESPRM |
| 24 | `LUCUPI.CARD.FINTRAN.ACQUIRER.REF.NO` | `LucupiCardFintran_AcquirerRefNo` | TField |  | Applicable only for PRVP file |
| 25 | `LUCUPI.CARD.FINTRAN.MARKUP.AMT` | `LucupiCardFintran_MarkupAmt` | TField |  | Applicable only for PRVP file |
| 26 | `LUCUPI.CARD.FINTRAN.CENTRAL.UNIQUE.IDENTIFIER` | `LucupiCardFintran_CentralUniqueIdentifier` | TField |  | Unique identifier for all transactions Applicable only for PRVP file |
| 27 | `LUCUPI.CARD.FINTRAN.TOTAL.NO.DATA.RECORDS` | `LucupiCardFintran_TotalNoDataRecords` | TField |  | Messages number (DATA Record items counter). |
| 28 | `LUCUPI.CARD.FINTRAN.TOTAL.AMT` | `LucupiCardFintran_TotalAmt` | TField |  | Total amount in cardholder currency |
| 29 | `LUCUPI.CARD.FINTRAN.TOTAL.AMT.EURO` | `LucupiCardFintran_TotalAmtEuro` | TField |  | Batch total amount in EURO |
| 30 | `LUCUPI.CARD.FINTRAN.SUCCESS.INDICATOR` | `LucupiCardFintran_SuccessIndicator` | TField |  | If execution of the data record fails then update this field as N (Default value is Y) |
| 31 | `LUCUPI.CARD.FINTRAN.ERROR.MSG` | `LucupiCardFintran_ErrorMsg` | TField |  | Contains Error Message |
| 32 | `LUCUPI.CARD.FINTRAN.STMT.NO` | `LucupiCardFintran_StmtNo` | TField |  | The statement entry number picked up from AC.INWARD.ENTRY STMT.NO of the transaction corresponding to the Card Holder account. |
| 33 | `LUCUPI.CARD.FINTRAN.RELEASE.KEY` | `LucupiCardFintran_ReleaseKey` | TField |  | This field holds the @ID of AC.LOCKED.EVENTS which is used as reference to release the lock. |
| 34 | `LUCUPI.CARD.FINTRANFILE.TYPE` | `LucupiCardFintran_FileType` | TField |  |  |
| 35 | `LUCUPI.CARD.FINTRAN.RESERVED.3` | `LucupiCardFintran_Reserved3` | TField |  |  |
| 36 | `LUCUPI.CARD.FINTRAN.RESERVED.4` | `LucupiCardFintran_Reserved4` | TField |  |  |
| 37 | `LUCUPI.CARD.FINTRAN.RESERVED.5` | `LucupiCardFintran_Reserved5` | TField |  |  |
| 38 | `LUCUPI.CARD.FINTRAN.RESERVED.6` | `LucupiCardFintran_Reserved6` | TField |  |  |
| 39 | `LUCUPI.CARD.FINTRAN.RESERVED.7` | `LucupiCardFintran_Reserved7` | TField |  |  |
| 40 | `LUCUPI.CARD.FINTRAN.RESERVED.8` | `LucupiCardFintran_Reserved8` | TField |  |  |
| 41 | `LUCUPI.CARD.FINTRAN.RESERVED.9` | `LucupiCardFintran_Reserved9` | TField |  |  |
| 42 | `LUCUPI.CARD.FINTRAN.RESERVED.10` | `LucupiCardFintran_Reserved10` | TField |  |  |
