*-----------------------------------------------------------------------------
* Program    : GOLDEN.JBC.SERVICE
* Type       : BATCH .SELECT
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE GOLDEN.JBC.SERVICE.SELECT
    $INSERT I_GOLDEN.JBC.SERVICE.COMMON
    $USING EB.DataAccess

    selCmd = 'SELECT ':fnApp:' WITH SECTOR EQ ':DQUOTE('1001')
    idList = ''
    noOfRecords = ''
    retCode = ''
    EB.DataAccess.Readlist(selCmd, idList, '', noOfRecords, retCode)
    CALL BATCH.BUILD.LIST('', idList)
RETURN
END
