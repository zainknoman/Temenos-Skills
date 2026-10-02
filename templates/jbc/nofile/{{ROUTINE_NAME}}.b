*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : NOFILE
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
SUBROUTINE {{ROUTINE_NAME}}(returnData)
    $USING EB.Reports
    $USING EB.DataAccess

    returnData = ''
    selValue = ''
    LOCATE '{{FIELD_NAME}}' IN EB.Reports.getDFields()<1> SETTING fieldPos THEN
        selValue = EB.Reports.getDRangeAndValue()<fieldPos>
    END
    selCmd = 'SELECT F.{{APP}} WITH {{FIELD_NAME}} EQ ':DQUOTE(selValue)
    idList = ''
    noOfRecords = ''
    retCode = ''
    EB.DataAccess.Readlist(selCmd, idList, '', noOfRecords, retCode)
    returnData = idList
RETURN
END
