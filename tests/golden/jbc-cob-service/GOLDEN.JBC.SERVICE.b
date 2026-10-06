*-----------------------------------------------------------------------------
* Program    : GOLDEN.JBC.SERVICE
* Type       : BATCH record routine
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.JBC.SERVICE(recordId)
    $INSERT I_GOLDEN.JBC.SERVICE.COMMON
    $USING EB.DataAccess
    $USING ST.Customer

    record = ''
    readErr = ''
    EB.DataAccess.FRead(fnApp, recordId, record, fApp, readErr)
    IF readErr NE '' THEN RETURN
    IF record<ST.Customer.Customer.EbCusSector> NE '1001' THEN RETURN

*   Record-level processing goes here.
    CRT 'GOLDEN.JBC.SERVICE: ':recordId
RETURN
END
