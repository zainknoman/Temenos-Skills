*-----------------------------------------------------------------------------
* Program    : B.GOLDEN.SERVICE
* Type       : BATCH .LOAD
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE B.GOLDEN.SERVICE.LOAD
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_B.GOLDEN.SERVICE.COMMON

    FN.APP = 'F.CUSTOMER'
    F.APP = ''
    CALL OPF(FN.APP, F.APP)
    RETURN
END
