*-----------------------------------------------------------------------------
* Program    : GOLDEN.BEFORE.AUTH
* Type       : BEFORE.AUTH.RTN
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.BEFORE.AUTH
    $USING EB.SystemTables
    $USING ST.Customer

    EB.SystemTables.setRNew(ST.Customer.Customer.EbCusMnemonic, 'SAMPLE')
RETURN
END
