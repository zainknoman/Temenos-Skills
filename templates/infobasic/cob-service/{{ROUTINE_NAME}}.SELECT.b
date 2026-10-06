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
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_{{ROUTINE_NAME}}.COMMON

    SEL.CMD = 'SELECT ':FN.APP:' WITH {{FIELD_NAME}} EQ ':DQUOTE('{{SELECT_VALUE}}')
    SEL.LIST = ''
    NO.OF.REC = ''
    SEL.ERR = ''
    CALL EB.READLIST(SEL.CMD, SEL.LIST, '', NO.OF.REC, SEL.ERR)
    CALL BATCH.BUILD.LIST('', SEL.LIST)
    RETURN
END
