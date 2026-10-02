*-----------------------------------------------------------------------------
* Program    : E.GOLDEN.JBC.NOFILE
* Type       : NOFILE
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Api
SUBROUTINE E.GOLDEN.JBC.NOFILE(returnData)
    $USING EB.Reports
    $USING EB.DataAccess

    returnData = ''
    selValue = ''
    LOCATE 'SECTOR' IN EB.Reports.getDFields()<1> SETTING fieldPos THEN
        selValue = EB.Reports.getDRangeAndValue()<fieldPos>
    END
    selCmd = 'SELECT F.CUSTOMER WITH SECTOR EQ ':DQUOTE(selValue)
    idList = ''
    noOfRecords = ''
    retCode = ''
    EB.DataAccess.Readlist(selCmd, idList, '', noOfRecords, retCode)
    returnData = idList
RETURN
END
