*-----------------------------------------------------------------------------
* Program    : GOLDEN.DE.CONV
* Type       : DE CONVERSION
* Description: Golden case
* Application: ACCOUNT
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE GOLDEN.DE.CONV(IN.VALUE, HEADER.REC, MV.NO, OUT.VALUE, ERROR.MSG)
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.ACCOUNT

    OUT.VALUE = ''
    ERROR.MSG = ''
    IF IN.VALUE EQ '' THEN RETURN

    FN.APP = 'F.ACCOUNT'
    F.APP = ''
    CALL OPF(FN.APP, F.APP)
    R.APP = ''
    Y.READ.ERR = ''
    CALL F.READ(FN.APP, IN.VALUE, R.APP, F.APP, Y.READ.ERR)
    IF Y.READ.ERR EQ '' THEN
        OUT.VALUE = R.APP<AC.CURRENCY>
    END
    RETURN
END
