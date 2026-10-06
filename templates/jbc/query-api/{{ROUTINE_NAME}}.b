*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : QUERY
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
SUBROUTINE {{ROUTINE_NAME}}(selValue, rows)
    $USING EB.DataAccess
    $USING {{APP_COMPONENT}}

    rows = ''
    selCmd = 'SELECT F.{{APP}} WITH {{FIELD_NAME}} EQ ':DQUOTE(selValue)
    idList = ''
    noOfRecords = ''
    retCode = ''
    EB.DataAccess.Readlist(selCmd, idList, '', noOfRecords, retCode)
    LOOP
        REMOVE recordId FROM idList SETTING more
    WHILE recordId:more
        readErr = ''
        record = {{APP_COMPONENT}}.{{APP_RECORD}}.Read(recordId, readErr)
        IF readErr EQ '' THEN
            rows<-1> = recordId:'*':record<{{RETURN_FIELD}}>
        END
    REPEAT
RETURN
END
