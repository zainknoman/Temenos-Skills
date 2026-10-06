*-----------------------------------------------------------------------------
* Program    : GOLDEN.COUNT.SECTOR
* Type       : PROGRAM
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
    PROGRAM GOLDEN.COUNT.SECTOR
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.CUSTOMER

    FN.APP = 'F.CUSTOMER'
    F.APP = ''
    CALL OPF(FN.APP, F.APP)

    SEL.CMD = 'SELECT ':FN.APP:' WITH SECTOR EQ ':DQUOTE('1001')
    SEL.LIST = ''
    NO.OF.REC = ''
    SEL.ERR = ''
    CALL EB.READLIST(SEL.CMD, SEL.LIST, '', NO.OF.REC, SEL.ERR)

    Y.COUNT = 0
    LOOP
        REMOVE Y.ID FROM SEL.LIST SETTING Y.POS
    WHILE Y.ID:Y.POS
        R.APP = ''
        Y.READ.ERR = ''
        CALL F.READ(FN.APP, Y.ID, R.APP, F.APP, Y.READ.ERR)
        IF Y.READ.ERR EQ '' AND R.APP<EB.CUS.SECTOR> EQ '1001' THEN
            Y.COUNT += 1
        END
    REPEAT
    CRT 'GOLDEN.COUNT.SECTOR: ':Y.COUNT:' record(s)'
END
