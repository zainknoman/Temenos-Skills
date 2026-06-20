# DE Code Patterns — jBC Templates

## Table of Contents
1. [FT Handoff Routine (<PKG>.DE.FT.DETAILS pattern)](#ft-handoff-routine)
2. [TT Handoff Routine (<PKG>.DE.TT.DETAILS pattern)](#tt-handoff-routine)
3. [Document Data FUNCTION (<PKG>.GET.ACCxx pattern)](#document-data-function)
4. [Event Mapping Table Definition](#event-mapping-table-definition)
5. [Event Mapping Fields Definition](#event-mapping-fields-definition)
6. [Print Interface Carrier](#print-interface-carrier)
7. [Date/Time Formatting](#datetime-formatting)
8. [Language Resolution for Currency Names](#language-resolution-for-currency-names)

---

## FT Handoff Routine

Full template for a new FT-based handoff. Replace `<APP>` with your application name.

```jBC
$PACKAGE <PKG>.LocalDevelopments
SUBROUTINE <PKG>.DE.<APP>.DETAILS

    $USING EB.API
    $USING EB.DataAccess
    $USING EB.SystemTables
    $USING ST.Customer
    $USING FT.Contract
    $USING DE.API
    $USING AC.AccountOpening
    $USING ST.CurrencyConfig
    $USING ST.Config
    $USING FT.Config
    $USING EB.LocalReferences

    ftTransactionType = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.TransactionType)
    mappingRecord = <PKG>.LocalDevelopments.<Pkg>DeEventMapping.Read(ftTransactionType, mappingError)

    IF mappingRecord NE "" THEN
        GOSUB PREP
        GOSUB GET.DR.SIDE
        GOSUB GET.CR.SIDE
        GOSUB UPDATE.DR.HANDOFF.REC
        GOSUB UPDATE.CR.HANDOFF.REC
    END

RETURN

PREP:

    ftTxnTypeRecord = FT.Config.TxnTypeCondition.Read(ftTransactionType, ftTxnTypeError)

    debitCurrency  = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.DebitCurrency)
    creditCurrency = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.CreditCurrency)

    debitCurrencyRecord   = ST.CurrencyConfig.Currency.Read(debitCurrency,  drCcyError)
    debitCurrencyNameEn   = debitCurrencyRecord<ST.CurrencyConfig.Currency.EbCurCcyName><1,1>
    debitCurrencyNameAr   = debitCurrencyRecord<ST.CurrencyConfig.Currency.EbCurCcyName><1,2>

    creditCurrencyRecord  = ST.CurrencyConfig.Currency.Read(creditCurrency, crCcyError)
    creditCurrencyNameEn  = creditCurrencyRecord<ST.CurrencyConfig.Currency.EbCurCcyName><1,1>
    creditCurrencyNameAr  = creditCurrencyRecord<ST.CurrencyConfig.Currency.EbCurCcyName><1,2>

    ftId       = EB.SystemTables.getIdNew()
    department = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.DeptCode)
    company    = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.CoCode)
    debitAccount  = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.DebitAcctNo)
    creditAccount = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.CreditAcctNo)

    dateTime = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.DateTime)
    hour   = dateTime[7,2]
    minute = dateTime[9,2]

    date  = OCONV(DATE(), 'D4-')
    year  = FIELD(date,'-',3)
    month = FIELD(date,'-',1)
    day   = FIELD(date,'-',2)
    primeDate = year:'-':month:'-':day

    debitValueDate  = primeDate:" ":hour:':':minute
    creditValueDate = primeDate:" ":hour:':':minute

    debitAmount  = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.DebitAmount)
    creditAmount = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.CreditAmount)

    totalCommissionAmount = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.TotalChargeAmount)
    IF totalCommissionAmount EQ "" THEN totalCommissionAmount = "0"
    totalCommissionAmount = totalCommissionAmount[4, LEN(totalCommissionAmount)]
    totalCommissionAmount = FMTS(totalCommissionAmount, ",")

    amountDebited  = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.AmountDebited)
    amountCredited = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.AmountCredited)
    amountDebited  = amountDebited[4,  LEN(amountDebited)]  ; amountDebited  = FMTS(amountDebited,  ",")
    amountCredited = amountCredited[4, LEN(amountCredited)] ; amountCredited = FMTS(amountCredited, ",")

    localCurrency = EB.SystemTables.getLccy()

    EB.LocalReferences.GetLocRef('FUNDS.TRANSFER','ENTRY.NO',   EntryNoPos)
    EB.LocalReferences.GetLocRef('FUNDS.TRANSFER','ENTRY.OP',   EntryOpPos)
    EB.LocalReferences.GetLocRef('FUNDS.TRANSFER','ENTRY.CONF', EntryConfPos)
    entryNo   = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.LocalRef)<1,EntryNoPos>
    entryOp   = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.LocalRef)<1,EntryOpPos>
    entryConf = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.LocalRef)<1,EntryConfPos>

RETURN

GET.DR.SIDE:

    debitAccountRecord   = AC.AccountOpening.Account.Read(debitAccount, drAcError)
    debitAccountCategory = debitAccountRecord<AC.AccountOpening.Account.Category>
    debitAccountName     = debitAccountRecord<AC.AccountOpening.Account.AccountTitleOne>
    availableDrBalance   = debitAccountRecord<AC.AccountOpening.Account.WorkingBalance>
    debitAccountBalance  = FMTS(availableDrBalance, ",")
    debitCustomerId      = debitAccountRecord<AC.AccountOpening.Account.Customer>

    debitCustomerRecord   = ST.Customer.Customer.Read(debitCustomerId, drCuError)
    debitCustomerLanguage = debitCustomerRecord<ST.Customer.Customer.EbCusLanguage>
    debitCustomerCompany  = debitCustomerRecord<ST.Customer.Customer.EbCusCoCode>

    BEGIN CASE
        CASE debitCustomerLanguage EQ '1' ; debitCurrency = debitCurrencyNameEn
        CASE debitCustomerLanguage EQ '2' ; debitCurrency = debitCurrencyNameAr
    END CASE

    BEGIN CASE
        CASE debitCustomerLanguage EQ '1' ; drDescription = ftTxnTypeRecord<FT.Config.TxnTypeCondition.FtSixDescription><1,1>
        CASE debitCustomerLanguage EQ '2' ; drDescription = ftTxnTypeRecord<FT.Config.TxnTypeCondition.FtSixDescription><1,2>
    END CASE

RETURN

GET.CR.SIDE:

    creditAccountRecord   = AC.AccountOpening.Account.Read(creditAccount, crAcError)
    creditAccountCategory = creditAccountRecord<AC.AccountOpening.Account.Category>
    creditAccountName     = creditAccountRecord<AC.AccountOpening.Account.AccountTitleOne>
    availableCrBalance    = creditAccountRecord<AC.AccountOpening.Account.WorkingBalance>
    creditAccountBalance  = FMTS(availableCrBalance, ",")
    creditCustomerId      = creditAccountRecord<AC.AccountOpening.Account.Customer>

    creditCustomerRecord   = ST.Customer.Customer.Read(creditCustomerId, crCuError)
    creditCustomerLanguage = creditCustomerRecord<ST.Customer.Customer.EbCusLanguage>
    creditCustomerCompany  = creditCustomerRecord<ST.Customer.Customer.EbCusCoCode>

    BEGIN CASE
        CASE creditCustomerLanguage EQ '1' ; creditCurrency = creditCurrencyNameEn
        CASE creditCustomerLanguage EQ '2' ; creditCurrency = creditCurrencyNameAr
    END CASE

    BEGIN CASE
        CASE creditCustomerLanguage EQ '1' ; crDescription = ftTxnTypeRecord<FT.Config.TxnTypeCondition.FtSixDescription><1,1>
        CASE creditCustomerLanguage EQ '2' ; crDescription = ftTxnTypeRecord<FT.Config.TxnTypeCondition.FtSixDescription><1,2>
    END CASE

RETURN

UPDATE.DR.HANDOFF.REC:

    DrMappingKeys = mappingRecord<<PKG>.LocalDevelopments.<Pkg>DeEventMapping.CbiHDrDeMapping>

    IF DrMappingKeys NE "" THEN
        numOfDrMapping = DCOUNT(DrMappingKeys, @VM)

        FOR JJ = 1 TO numOfDrMapping

            DrCategory      = mappingRecord<<PKG>.LocalDevelopments.<Pkg>DeEventMapping.CbiHDrCategory><1,JJ>
            debitDocCode    = mappingRecord<<PKG>.LocalDevelopments.<Pkg>DeEventMapping.CbiHDrDocCode><1,JJ>
            debitUserRef    = mappingRecord<<PKG>.LocalDevelopments.<Pkg>DeEventMapping.CbiHDrUserRef><1,JJ>
            debitParamCode  = mappingRecord<<PKG>.LocalDevelopments.<Pkg>DeEventMapping.CbiHDrParamCode><1,JJ>

            IF INDEX(DrCategory, debitAccountCategory, 1) THEN

                DrArray.5 = ""
                DrArray.5<1>  = ftId
                DrArray.5<2>  = company
                DrArray.5<3>  = department
                DrArray.5<4>  = debitCustomerId
                DrArray.5<6>  = debitCustomerLanguage
                DrArray.5<8>  = debitCustomerCompany
                DrArray.5<10> = debitAccountBalance
                DrArray.5<12> = debitAccount
                DrArray.5<14> = '-':FMTS(debitAmount, ",")
                DrArray.5<16> = debitValueDate
                DrArray.5<18> = debitCurrency
                DrArray.5<20> = totalCommissionAmount
                DrArray.5<22> = '-':amountDebited
                DrArray.5<23> = drDescription
                DrArray.5<24> = entryNo
                DrArray.5<25> = entryOp
                DrArray.5<26> = entryConf
                DrArray.5<27> = debitAccountName
                DrArray.5<28> = debitDocCode
                DrArray.5<29> = debitUserRef
                DrArray.5<30> = debitParamCode

                DrRec1 = "" ; DrRec2 = "" ; DrRec3 = "" ; DrRec4 = ""
                DrRec5 = DrArray.5
                DrRec6 = "" ; DrRec7 = "" ; DrRec8 = "" ; DrRec9 = ""
                DrVKey   = ""
                DrMapKey = DrMappingKeys<1,JJ>
                DrErrMsg = ""

                DE.API.ApplicationHandoff(DrRec1,DrRec2,DrRec3,DrRec4,DrRec5,DrRec6,DrRec7,DrRec8,DrRec9, DrMapKey,DrVKey,DrErrMsg)

                deliveryRef = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.DeliveryOutref)
                IF deliveryRef EQ "" THEN
                    deliveryRef = DrVKey
                ELSE
                    deliveryRef<1,-1> = DrVKey
                END
                EB.SystemTables.setRNew(FT.Contract.FundsTransfer.DeliveryOutref, deliveryRef)

            END

        NEXT JJ
    END

RETURN

UPDATE.CR.HANDOFF.REC:

    CrMappingKeys = mappingRecord<<PKG>.LocalDevelopments.<Pkg>DeEventMapping.CbiHCrDeMapping>

    IF CrMappingKeys NE "" THEN
        numOfCrMapping = DCOUNT(CrMappingKeys, @VM)

        FOR KK = 1 TO numOfCrMapping

            CrCategory      = mappingRecord<<PKG>.LocalDevelopments.<Pkg>DeEventMapping.CbiHCrCategory><1,KK>
            creditDocCode   = mappingRecord<<PKG>.LocalDevelopments.<Pkg>DeEventMapping.CbiHCrDocCode><1,KK>
            creditUserRef   = mappingRecord<<PKG>.LocalDevelopments.<Pkg>DeEventMapping.CbiHCrUserRef><1,KK>
            creditParamCode = mappingRecord<<PKG>.LocalDevelopments.<Pkg>DeEventMapping.CbiHCrParamCode><1,KK>

            IF INDEX(CrCategory, creditAccountCategory, 1) THEN

                CrArray.5 = ""
                CrArray.5<1>  = ftId
                CrArray.5<2>  = company
                CrArray.5<3>  = department
                CrArray.5<5>  = creditCustomerId
                CrArray.5<7>  = creditCustomerLanguage
                CrArray.5<9>  = creditCustomerCompany
                CrArray.5<11> = creditAccountBalance
                CrArray.5<13> = creditAccount
                CrArray.5<15> = '+':FMTS(creditAmount, ",")
                CrArray.5<17> = creditValueDate
                CrArray.5<19> = creditCurrency
                CrArray.5<20> = totalCommissionAmount
                CrArray.5<21> = '+':amountCredited
                CrArray.5<22> = crDescription
                CrArray.5<24> = entryNo
                CrArray.5<25> = entryOp
                CrArray.5<26> = entryConf
                CrArray.5<27> = creditAccountName
                CrArray.5<28> = creditDocCode
                CrArray.5<29> = creditUserRef
                CrArray.5<30> = creditParamCode

                CrRec1 = "" ; CrRec2 = "" ; CrRec3 = "" ; CrRec4 = ""
                CrRec5 = CrArray.5
                CrRec6 = "" ; CrRec7 = "" ; CrRec8 = "" ; CrRec9 = ""
                CrVKey   = ""
                CrMapKey = CrMappingKeys<1,KK>
                CrErrMsg = ""

                DE.API.ApplicationHandoff(CrRec1,CrRec2,CrRec3,CrRec4,CrRec5,CrRec6,CrRec7,CrRec8,CrRec9, CrMapKey,CrVKey,CrErrMsg)

                deliveryRef = EB.SystemTables.getRNew(FT.Contract.FundsTransfer.DeliveryOutref)
                IF deliveryRef EQ "" THEN
                    deliveryRef = CrVKey
                ELSE
                    deliveryRef<1,-1> = CrVKey
                END
                EB.SystemTables.setRNew(FT.Contract.FundsTransfer.DeliveryOutref, deliveryRef)

            END

        NEXT KK
    END

RETURN

END
```

---

## TT Handoff Routine

Refer to `<PKG>.DE.TT.DETAILS.b` for the full working pattern. Key differences from FT:
- Transaction type: `EB.SystemTables.getRNew(TT.Contract.Teller.TeTransactionCode)`
- Two sides named `SIDE.1` / `SIDE.2` (not DR/CR)
- Array positions differ — see [de-arrays.md](de-arrays.md)
- No `EB.LocalReferences` for entry numbers
- Balance fields: `newCustomerBalance`, `chargeAmountLcy` (not from LocalRef)

---

## Document Data FUNCTION

Template for a REST endpoint that provides document data to Docupilot.

```jBC
$PACKAGE <PKG>.LocalDevelopments
*
* Implementation of <PKG>.LocalDevelopments.get<Name>
*
* <inputParam>(IN) : <description>
*
FUNCTION <PKG>.GET.<CATEGORY><NN>.<NAME>(<inputParam>)

    $USING EB.SystemTables
    $USING EB.API
    $USING EB.DataAccess
    $USING FT.Contract          ;* or AA.Contract / TT.Contract etc.
    $USING AC.AccountOpening
    $USING EB.LocalReferences
    $USING EB.Security
    $USING DE.Outward

    IF <PKG>.LocalDevelopments.getinitialised() NE 'Y' THEN
        <PKG>.LocalDevelopments.initialiseDigiArena()
    END

    GOSUB PREP

RETURN outRecord

PREP:

    ;* Read live record, fall back to history
    srcRecord = <Application>.<Table>.Read(<inputParam>, readError)
    IF srcRecord EQ "" THEN
        srcRecord = <Application>.<Table>.ReadHis(<inputParam>:';1', readError)
    END

    IF srcRecord NE "" THEN

        ;* Extract and format fields
        dateTime = srcRecord<FT.Contract.FundsTransfer.DateTime>
        hour   = dateTime[7,2]
        minute = dateTime[9,2]

        date  = OCONV(DATE(), 'D4-')
        year  = FIELD(date,'-',3)
        month = FIELD(date,'-',1)
        day   = FIELD(date,'-',2)
        formattedDate = year:'-':month:'-':day:" ":hour:':':minute

        ;* Amount handling
        rawAmount  = srcRecord<FT.Contract.FundsTransfer.AmountDebited>
        amount     = rawAmount[4, LEN(rawAmount)]
        currency   = rawAmount[1,3]

        ;* Amount in words (Arabic)
        DE.Outward.OPrintWords(amount:'*':currency, amountWords, 'AR', LineLength, NoOfLines, ErrMsg)
        CHANGE '*' TO ' ' IN amountWords

    END

    ;* Build output record using component struct equates
    outRecord = ""
    outRecord<<PKG>.LocalDevelopments.<docStruct>.<field1>> = <value1>
    outRecord<<PKG>.LocalDevelopments.<docStruct>.<field2>> = <value2>
    ;* ... add all required fields

RETURN
```

---

## Event Mapping Table Definition

```jBC
$PACKAGE <PKG>.LocalDevelopments
SUBROUTINE <PKG>.DE.EVENT.MAPPING

    $USING EB.SystemTables
    $USING EB.API
    $USING EB.Template

    EB.Template.setTableName('<PKG>.DE.EVENT.MAPPING')
    EB.Template.setTableTitle('Link Events to DE')
    EB.Template.setTableStereotype('H')
    EB.Template.setTableProduct('EB')
    EB.Template.setTableSubproduct('')
    EB.Template.setTableClassification('INT')
    EB.Template.setTableSystemclearfile('Y')
    EB.Template.setTableRelatedfiles('')
    EB.Template.setTableIspostclosingfile('')
    EB.Template.setTableEquateprefix('<PKG>.H')
    EB.Template.setTableIdprefix('')
    EB.Template.setTableBlockedfunctions('')
    Table.trigger = ''

RETURN
END
```

---

## Event Mapping Fields Definition

```jBC
$PACKAGE <PKG>.LocalDevelopments
SUBROUTINE <PKG>.DE.EVENT.MAPPING.FIELDS

    $USING EB.SystemTables
    $USING EB.API
    $USING EB.Template
    $USING DE.Config
    $USING ST.Config

    EB.SystemTables.setIdF('@ID')
    EB.SystemTables.setIdN('35')
    EB.SystemTables.setIdT('A')
    Z = 0

    Z+=1 ; EB.SystemTables.setF(Z,"XX.LL.DESCRIPTION")   ; EB.SystemTables.setN(Z,'35') ; EB.SystemTables.setT(Z,'A')

    Z+=1 ; EB.SystemTables.setF(Z,"XX<DR.DE.MAPPING")    ; EB.SystemTables.setN(Z,'35') ; EB.SystemTables.setT(Z,'A')
    EB.SystemTables.setCheckfile(Z,"DE.MAPPING":@FM:DE.Config.Mapping.MapDescription:@FM:"L.A")

    Z+=1 ; EB.SystemTables.setF(Z,"XX-XX.DR.CATEGORY")   ; EB.SystemTables.setN(Z,'35') ; EB.SystemTables.setT(Z,'A')
    EB.SystemTables.setCheckfile(Z,"CATEGORY":@FM:ST.Config.Category.EbCatDescription:@FM:"L.A")

    Z+=1 ; EB.SystemTables.setF(Z,"XX-DR.DOC.CODE")      ; EB.SystemTables.setN(Z,'35') ; EB.SystemTables.setT(Z,'A')
    Z+=1 ; EB.SystemTables.setF(Z,"XX-DR.USER.REF")      ; EB.SystemTables.setN(Z,'35') ; EB.SystemTables.setT(Z,'ANY')
    Z+=1 ; EB.SystemTables.setF(Z,"XX>DR.PARAM.CODE")    ; EB.SystemTables.setN(Z,'35') ; EB.SystemTables.setT(Z,'A')

    Z+=1 ; EB.SystemTables.setF(Z,"XX<CR.DE.MAPPING")    ; EB.SystemTables.setN(Z,'35') ; EB.SystemTables.setT(Z,'A')
    EB.SystemTables.setCheckfile(Z,"DE.MAPPING":@FM:DE.Config.Mapping.MapDescription:@FM:"L.A")

    Z+=1 ; EB.SystemTables.setF(Z,"XX-XX.CR.CATEGORY")   ; EB.SystemTables.setN(Z,'35') ; EB.SystemTables.setT(Z,'A')
    EB.SystemTables.setCheckfile(Z,"CATEGORY":@FM:ST.Config.Category.EbCatDescription:@FM:"L.A")

    Z+=1 ; EB.SystemTables.setF(Z,"XX-CR.DOC.CODE")      ; EB.SystemTables.setN(Z,'35') ; EB.SystemTables.setT(Z,'A')
    Z+=1 ; EB.SystemTables.setF(Z,"XX-CR.USER.REF")      ; EB.SystemTables.setN(Z,'35') ; EB.SystemTables.setT(Z,'ANY')
    Z+=1 ; EB.SystemTables.setF(Z,"XX>CR.PARAM.CODE")    ; EB.SystemTables.setN(Z,'35') ; EB.SystemTables.setT(Z,'A')

    Z+=1 ; EB.SystemTables.setF(Z,"XX.LOCAL.REF")        ; EB.SystemTables.setN(Z,'35') ; EB.SystemTables.setT(Z,'A')

    EB.SystemTables.setV(Z + 9)

RETURN
END
```

---

## Print Interface Carrier

The carrier subroutine (`<PKG>.DE.PRINT.INTERFACE`) signature:
```jBC
SUBROUTINE <PKG>.DE.PRINT.INTERFACE(misn, deliveryPackage, genericData, errorResponse)
```

Key patterns:
```jBC
;* Error format that stops DE retry
errorResponse = 'STOP-':errorMessage

;* Response audit record
responseRecord<<PKG>.LocalDevelopments.<Pkg>DeDocuResponse.CbiLFullRequest>  = DATA.OBJ
responseRecord<<PKG>.LocalDevelopments.<Pkg>DeDocuResponse.CbiLFullResponse> = response
<PKG>.LocalDevelopments.<Pkg>DeDocuResponse.Write(deId, responseRecord)
```

---

## DateTime Formatting

Standard pattern used in all handoff routines:
```jBC
dateTime = EB.SystemTables.getRNew(<Contract>.<Entity>.DateTime)
hour   = dateTime[7,2]   ;* positions 7-8 in YYYYMMDDHHMMSS
minute = dateTime[9,2]   ;* positions 9-10

date  = OCONV(DATE(), 'D4-')   ;* returns MM-DD-YYYY
year  = FIELD(date,'-',3)
month = FIELD(date,'-',1)
day   = FIELD(date,'-',2)
formattedDate = year:'-':month:'-':day:" ":hour:':':minute
;* Result: "YYYY-MM-DD HH:MM"
```

---

## Language Resolution for Currency Names

```jBC
BEGIN CASE
    CASE customerLanguage EQ '1'
        currencyDisplay = currencyNameEn
    CASE customerLanguage EQ '2'
        currencyDisplay = currencyNameAr
END CASE
```

Where `currencyNameEn = currencyRecord<ST.CurrencyConfig.Currency.EbCurCcyName><1,1>` and `<1,2>` for Arabic.
