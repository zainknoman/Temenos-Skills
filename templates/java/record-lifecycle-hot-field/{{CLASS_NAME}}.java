package {{JAVA_PACKAGE}};
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: {{APP}}
// Hook type: RecordLifecycle.defaultFieldValuesOnHotField

import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.{{RECORD_PACKAGE}}.{{RECORD_CLASS}}Record;
import com.temenos.t24.api.complex.eb.templatehook.InputValue;

public class {{CLASS_NAME}} extends RecordLifecycle {

    @Override
    public void defaultFieldValuesOnHotField(String application, String currentRecordId, TStructure currentRecord,
            InputValue currentInputValue, TStructure unauthorisedRecord, TStructure liveRecord,
            TransactionContext transactionContext) {

        if (!"{{FIELD_NAME}}".equals(currentInputValue.getFieldName())) {
            return;
        }
        {{RECORD_CLASS}}Record rec = new {{RECORD_CLASS}}Record(currentRecord);
        rec.set{{TARGET_FIELD}}("{{DEFAULT_VALUE}}");
        currentRecord.set(rec.toStructure());
    }
}
