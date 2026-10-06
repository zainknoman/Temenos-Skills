*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : GET (typed)
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
FUNCTION {{ROUTINE_NAME}}(recordId)
    $USING {{APP_COMPONENT}}

    outRecord = ''
    readErr = ''
    record = {{APP_COMPONENT}}.{{APP_RECORD}}.Read(recordId, readErr)
    outRecord<{{PACKAGE}}.{{TYPE_NAME}}.recordId> = recordId
    IF readErr EQ '' THEN
        outRecord<{{PACKAGE}}.{{TYPE_NAME}}.fieldValue> = record<{{FIELD}}>
    END
RETURN outRecord
END
