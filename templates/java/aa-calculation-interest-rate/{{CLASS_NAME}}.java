package {{JAVA_PACKAGE}};
// Implements: Calculation from AA_CalculationHook.jar
// T24 Application: {{APP}}
// Hook type: Calculation.getInterestCustomRate

import java.util.List;

import com.temenos.api.TDate;
import com.temenos.api.TNumber;
import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.aa.activityhook.ArrangementContext;
import com.temenos.t24.api.complex.aa.calculationhook.InterestCustomRate;
import com.temenos.t24.api.hook.arrangement.Calculation;
import com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord;
import com.temenos.t24.api.records.aaarrangement.AaArrangementRecord;
import com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord;
import com.temenos.t24.api.records.aaprddesinterest.AaPrdDesInterestRecord;
import com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord;

public class {{CLASS_NAME}} extends Calculation {

    @Override
    public void getInterestCustomRate(String arrangementId, String interestProperty, TDate effectiveDate,
            String rateType, List<TDate> rateChangeDates, AaPrdDesInterestRecord interestRecord,
            String currency, AaArrangementActivityRecord arrangementActivityRecord,
            AaProductCatalogRecord productRecord, TStructure productPropertyRecord, TStructure record,
            ArrangementContext arrangementContext, AaAccountDetailsRecord accountDetailRecord,
            AaArrangementActivityRecord masterActivityRecord, InterestCustomRate interestCustomRate) {

        interestCustomRate.addEffectiveDate(effectiveDate);
        interestCustomRate.addEffectiveRate(new TNumber("{{RATE}}"));
    }
}
