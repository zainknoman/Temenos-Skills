package {{JAVA_PACKAGE}};
// Implements: ActivityLifecycle from AA_ActivityHook.jar
// T24 Application: {{APP}}
// Hook type: ActivityLifecycle.updateLookupTable

import java.util.List;

import com.temenos.api.TBoolean;
import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.aa.activityhook.ArrangementContext;
import com.temenos.t24.api.complex.aa.activityhook.LookupData;
import com.temenos.t24.api.hook.arrangement.ActivityLifecycle;
import com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord;
import com.temenos.t24.api.records.aaarrangement.AaArrangementRecord;
import com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord;
import com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord;

public class {{CLASS_NAME}} extends ActivityLifecycle {

    @Override
    public TBoolean updateLookupTable(AaAccountDetailsRecord accountDetailRecord,
            AaArrangementActivityRecord arrangementActivityRecord, ArrangementContext arrangementContext,
            AaArrangementRecord arrangementRecord, AaArrangementActivityRecord masterActivityRecord,
            TStructure productPropertyRecord, AaProductCatalogRecord productRecord, TStructure record,
            List<LookupData> lookupData) {

        LookupData entry = new LookupData();
        entry.setLookupTableName("{{LOOKUP_TABLE}}");
        entry.setKey("{{LOOKUP_KEY}}");
        entry.setEntryToAdd(arrangementContext.getArrangementId());
        lookupData.add(entry);
        return new TBoolean(true);
    }
}
