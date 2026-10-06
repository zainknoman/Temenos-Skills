*-----------------------------------------------------------------------------
* Program    : GOLDEN.JBC.SERVICE
* Type       : BATCH .LOAD
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.JBC.SERVICE.LOAD
    $INSERT I_GOLDEN.JBC.SERVICE.COMMON
    $USING EB.DataAccess

    fnApp = 'F.CUSTOMER'
    fApp = ''
    EB.DataAccess.Opf(fnApp, fApp)
RETURN
END
