*-----------------------------------------------------------------------------
* Program    : E.GOLDEN.NOFILE
* Type       : NOFILE
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE E.GOLDEN.NOFILE(Y.ID.LIST)
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_ENQUIRY.COMMON

    Y.ID.LIST = ''
    Y.SEL.VALUE = ''
    LOCATE 'SECTOR' IN D.FIELDS<1> SETTING Y.POS THEN
        Y.SEL.VALUE = D.RANGE.AND.VALUE<Y.POS>
    END

    FN.APP = 'F.CUSTOMER'
    F.APP = ''
    CALL OPF(FN.APP, F.APP)
    SEL.CMD = 'SELECT ':FN.APP:' WITH SECTOR EQ ':DQUOTE(Y.SEL.VALUE)
    SEL.LIST = ''
    NO.OF.REC = ''
    SEL.ERR = ''
    CALL EB.READLIST(SEL.CMD, SEL.LIST, '', NO.OF.REC, SEL.ERR)
    Y.ID.LIST = SEL.LIST
    RETURN
END
