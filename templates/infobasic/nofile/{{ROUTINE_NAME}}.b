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
    SUBROUTINE {{ROUTINE_NAME}}(Y.ID.LIST)
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_ENQUIRY.COMMON

    Y.ID.LIST = ''
    Y.SEL.VALUE = ''
    LOCATE '{{FIELD_NAME}}' IN D.FIELDS<1> SETTING Y.POS THEN
        Y.SEL.VALUE = D.RANGE.AND.VALUE<Y.POS>
    END

    FN.APP = 'F.{{APP}}'
    F.APP = ''
    CALL OPF(FN.APP, F.APP)
    SEL.CMD = 'SELECT ':FN.APP:' WITH {{FIELD_NAME}} EQ ':DQUOTE(Y.SEL.VALUE)
    SEL.LIST = ''
    NO.OF.REC = ''
    SEL.ERR = ''
    CALL EB.READLIST(SEL.CMD, SEL.LIST, '', NO.OF.REC, SEL.ERR)
    Y.ID.LIST = SEL.LIST
    RETURN
END
