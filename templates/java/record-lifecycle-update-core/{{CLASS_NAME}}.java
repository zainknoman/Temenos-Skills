package {{JAVA_PACKAGE}};
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: {{APP}}
// Hook type: RecordLifecycle.updateCoreRecord

import java.util.List;

import com.temenos.api.TBoolean;
import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.{{RECORD_PACKAGE}}.{{RECORD_CLASS}}Record;

public class {{CLASS_NAME}} extends RecordLifecycle {

    @Override
    public void updateCoreRecord(String application, String currentRecordId, TStructure currentRecord,
            TStructure unauthorisedRecord, TStructure liveRecord, List<String> versionNames,
            TBoolean isZeroAuth, List<String> recordIds, List<TStructure> records,
            TransactionContext transactionContext) {

        {{RECORD_CLASS}}Record rec = new {{RECORD_CLASS}}Record(currentRecord);
        rec.set{{FIELD}}("{{FIELD_VALUE}}");
        currentRecord.set(rec.toStructure());
    }
}
