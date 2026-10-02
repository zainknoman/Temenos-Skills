package {{JAVA_PACKAGE}};
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: {{APP}}
// Hook type: RecordLifecycle

import com.temenos.api.TStructure;
import com.temenos.api.TValidationResponse;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.{{RECORD_PACKAGE}}.{{RECORD_CLASS}}Record;

public class {{CLASS_NAME}} extends RecordLifecycle {

    @Override
    public TValidationResponse validateRecord(String application, String currentRecordId,
            TStructure currentRecord, TStructure unauthorisedRecord,
            TStructure liveRecord, TransactionContext transactionContext) {

        {{RECORD_CLASS}}Record rec = new {{RECORD_CLASS}}Record(currentRecord);
        String value = rec.get{{FIELD}}().getValue();
        if (value == null || value.isEmpty()) {
            rec.get{{FIELD}}().setError("{{ERROR_TEXT}}");
        }
        currentRecord.set(rec.toStructure());
        return rec.getValidationResponse();
    }
}
