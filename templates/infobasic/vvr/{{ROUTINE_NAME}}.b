*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : VVR
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
    $INSERT I_F.{{APP}}

    IF AF NE {{FIELD}} THEN RETURN
    IF COMI EQ '' THEN
        ETEXT = '{{ERROR_TEXT}}'
        CALL STORE.END.ERROR
    END
    RETURN
END
