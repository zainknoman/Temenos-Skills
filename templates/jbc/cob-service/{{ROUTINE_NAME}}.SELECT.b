*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : BATCH .SELECT
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
SUBROUTINE {{ROUTINE_NAME}}.SELECT
    $INSERT I_{{ROUTINE_NAME}}.COMMON
    $USING EB.DataAccess

    selCmd = 'SELECT ':fnApp:' WITH {{FIELD_NAME}} EQ ':DQUOTE('{{SELECT_VALUE}}')
    idList = ''
    noOfRecords = ''
    retCode = ''
    EB.DataAccess.Readlist(selCmd, idList, '', noOfRecords, retCode)
    CALL BATCH.BUILD.LIST('', idList)
RETURN
END
