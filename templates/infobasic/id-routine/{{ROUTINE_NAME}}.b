*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : ID.RTN
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
    SUBROUTINE {{ROUTINE_NAME}}
    $INSERT I_COMMON
    $INSERT I_EQUATE

    Y.ID = ID.NEW
    IF Y.ID EQ '' THEN RETURN
    IF Y.ID[1, LEN('{{ID_PREFIX}}')] NE '{{ID_PREFIX}}' THEN
        E = '{{ERROR_TEXT}}'
    END
    RETURN
END
