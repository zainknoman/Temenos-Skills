package {{JAVA_PACKAGE}};
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: {{APP}}
// Hook type: RecordLifecycle.defaultFieldValues

import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.{{RECORD_PACKAGE}}.{{RECORD_CLASS}}Record;

public class {{CLASS_NAME}} extends RecordLifecycle {

    @Override
    public void defaultFieldValues(String application, String currentRecordId, TStructure currentRecord,
            TStructure unauthorisedRecord, TStructure liveRecord, TransactionContext transactionContext) {

        {{RECORD_CLASS}}Record rec = new {{RECORD_CLASS}}Record(currentRecord);
        String value = rec.get{{FIELD}}().getValue();
        if (value == null || value.isEmpty()) {
            rec.set{{FIELD}}("{{DEFAULT_VALUE}}");
            currentRecord.set(rec.toStructure());
        }
    }
}
