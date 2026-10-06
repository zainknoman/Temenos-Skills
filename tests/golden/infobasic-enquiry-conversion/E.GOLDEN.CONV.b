*-----------------------------------------------------------------------------
* Program    : E.GOLDEN.CONV
* Type       : ENQUIRY CONVERSION
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE E.GOLDEN.CONV
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_ENQUIRY.COMMON
    $INSERT I_F.CUSTOMER

    Y.ID = O.DATA
    IF Y.ID EQ '' THEN RETURN

    FN.APP = 'F.CUSTOMER'
    F.APP = ''
    CALL OPF(FN.APP, F.APP)
    R.APP = ''
    Y.READ.ERR = ''
    CALL F.READ(FN.APP, Y.ID, R.APP, F.APP, Y.READ.ERR)
    IF Y.READ.ERR EQ '' THEN
        O.DATA = R.APP<EB.CUS.SECTOR>
    END ELSE
        O.DATA = ''
    END
    RETURN
END
