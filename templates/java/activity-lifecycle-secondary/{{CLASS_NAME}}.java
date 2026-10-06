package {{JAVA_PACKAGE}};
// Implements: ActivityLifecycle from AA_ActivityHook.jar
// T24 Application: {{APP}}
// Hook type: ActivityLifecycle.generateSecondaryActivity

import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.aa.activityhook.ArrangementContext;
import com.temenos.t24.api.complex.aa.activityhook.SecondaryActivity;
import com.temenos.t24.api.hook.arrangement.ActivityLifecycle;
import com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord;
import com.temenos.t24.api.records.aaarrangement.AaArrangementRecord;
import com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord;
import com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord;

public class {{CLASS_NAME}} extends ActivityLifecycle {

    @Override
    public void generateSecondaryActivity(AaAccountDetailsRecord accountDetailRecord,
            AaArrangementActivityRecord arrangementActivityRecord, ArrangementContext arrangementContext,
            AaArrangementRecord arrangementRecord, AaArrangementActivityRecord masterActivityRecord,
            TStructure productPropertyRecord, AaProductCatalogRecord productRecord, TStructure record,
            SecondaryActivity secondaryActivity) {

        secondaryActivity.setArrangementId(arrangementContext.getArrangementId());
        secondaryActivity.setNewActivity("{{SECONDARY_ACTIVITY}}");
    }
}
