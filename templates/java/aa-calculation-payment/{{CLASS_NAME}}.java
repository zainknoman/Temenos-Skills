package {{JAVA_PACKAGE}};
// Implements: Calculation from AA_CalculationHook.jar
// T24 Application: {{APP}}
// Hook type: Calculation.calculatePayment

import com.temenos.api.TDate;
import com.temenos.api.TNumber;
import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.aa.activityhook.ArrangementContext;
import com.temenos.t24.api.hook.arrangement.Calculation;
import com.temenos.t24.api.records.aaaccountdetails.AaAccountDetailsRecord;
import com.temenos.t24.api.records.aaarrangement.AaArrangementRecord;
import com.temenos.t24.api.records.aaarrangementactivity.AaArrangementActivityRecord;
import com.temenos.t24.api.records.aaprddespaymentschedule.AaPrdDesPaymentScheduleRecord;
import com.temenos.t24.api.records.aaproductcatalog.AaProductCatalogRecord;

public class {{CLASS_NAME}} extends Calculation {

    @Override
    public TNumber calculatePayment(String paymentType, String property,
            AaPrdDesPaymentScheduleRecord paymentScheduleRecord, TDate paymentDate, String calcType,
            TDate periodStart, String paymentMethod, String billType,
            AaAccountDetailsRecord accountDetailRecord, AaArrangementActivityRecord arrangementActivityRecord,
            ArrangementContext arrangementContext, AaArrangementRecord arrangementRecord,
            TStructure productPropertyRecord, AaProductCatalogRecord productRecord, TStructure record,
            AaArrangementActivityRecord masterActivityRecord) {

        return new TNumber("{{PAYMENT_AMOUNT}}");
    }
}
