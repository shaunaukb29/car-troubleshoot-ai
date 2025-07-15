vehicle_issues = {
    "Check Engine Light": {
  "Actual Issue": "The CEL can be triggered by various sensor faults, emission issues, or engine misbehavior.",
  "Severity Level": "Variable — can range from minor issues causing no immediate harm to serious faults that reduce engine performance or cause emissions failure; requires prompt diagnosis to prevent damage.",
  "Possible Causes": [
    {"cause": "Loose fuel cap", "probability": 0.25},
    {"cause": "Faulty oxygen sensor", "probability": 0.35},
    {"cause": "Misfiring engine (plugs/coils)", "probability": 0.25},
    {"cause": "Catalytic converter failure", "probability": 0.15}
  ],
  "Diagnostics": [
    "Scan with OBD-II tool for error codes (e.g., P0300 for misfire)",
    "Check fuel cap tightness and seal",
    "Observe engine performance and fuel economy",
    "Inspect exhaust emissions"
  ],
  "Fixes": [
    "Tighten or replace gas cap",
    "Replace faulty sensor or component based on code",
    "Fix misfire cause (plugs, coils, fuel)",
    "Replace catalytic converter"
  ],
  "Temporary Solutions": [
    "Reset light with scanner after tightening gas cap",
    "Drive gently and monitor if light comes back"
  ]
},

  "Start-Stop System Malfunction": {
  "Actual Issue": "Automatic engine start-stop system does not function as expected.",
  "Severity Level": "Low — mainly affects fuel efficiency and emissions; does not impact drivability or safety but may indicate underlying electrical or sensor issues.",
  "Possible Causes": [
    {"cause": "Weak or aging 12V battery", "probability": 0.4},
    {"cause": "Faulty brake pedal switch", "probability": 0.25},
    {"cause": "Incorrect ambient temperature readings", "probability": 0.15},
    {"cause": "Driver door sensor malfunction", "probability": 0.1},
    {"cause": "Software glitches", "probability": 0.1}
  ],
    "Symptoms": [
      "Engine doesn't turn off at red lights",
      "Warning icon on dashboard",
      "Reduced fuel economy"
    ],
    "Diagnostics": [
      "Battery health check",
      "Scan for body control module (BCM) codes",
      "Check temperature sensor and brake switch input"
    ],
    "Fixes": [
      "Replace battery if below threshold",
      "Reprogram/update vehicle software",
      "Replace faulty brake switch or door sensor"
    ],
    "Temporary Solutions": [
      "Manually disable start-stop from console if available"
    ]
  },

    "Poor Fuel Economy": {
  "Actual Issue": "Reduced fuel efficiency caused by engine inefficiency, tire pressure, or driving behavior.",
  "Severity Level": "Low — primarily affects fuel costs and emissions; no direct safety risk but may indicate underlying issues that could worsen if ignored.",
  "Possible Causes": [
    {"cause": "Under-inflated tires", "probability": 0.3},
    {"cause": "Dirty air filter", "probability": 0.25},
    {"cause": "Faulty oxygen or MAF sensor", "probability": 0.25},
    {"cause": "Aggressive driving or short trips", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check and inflate tires to recommended PSI",
    "Inspect air filter and replace if dirty",
    "Scan for sensor faults (oxygen/MAF)",
    "Compare fuel logs and mileage drop"
  ],
  "Fixes": [
    "Inflate tires properly",
    "Replace air/fuel sensors as needed",
    "Use fuel injector cleaner",
    "Adopt smoother driving habits"
  ],
  "Temporary Solutions": [
    "Avoid idling and quick acceleration",
    "Plan trips to reduce cold starts"
  ]
},

"Fuel Injector Clogging": {
  "Actual Issue": "Fuel injectors partially blocked reducing fuel spray quality.",
  "Severity Level": "Moderate — causes drivability issues like misfires and rough idling; can lead to engine damage if untreated.",
  "Possible Causes": [
    {"cause": "Low-quality or contaminated fuel", "probability": 0.5},
    {"cause": "Lack of fuel system maintenance", "probability": 0.3},
    {"cause": "Faulty fuel filter", "probability": 0.15},
    {"cause": "Carbon buildup inside injectors", "probability": 0.05}
  ],
  "Symptoms": [
    "Engine misfires or hesitation",
    "Poor fuel economy",
    "Rough idle",
    "Hard starting"
  ],
  "Diagnostics": [
    "Fuel pressure test",
    "Injector balance test",
    "Check fuel filter condition",
    "Scan for misfire or injector codes"
  ],
  "Fixes": [
    "Use fuel injector cleaner additives",
    "Replace fuel filter",
    "Clean or replace clogged injectors"
  ],
  "Temporary Solutions": [
    "Use premium or cleaner fuel temporarily",
    "Avoid aggressive driving"
  ]
},

"Hybrid Battery Module Failure": {
  "Actual Issue": "One or more cells in the hybrid battery pack fail, reducing overall capacity.",
  "Severity Level": "High — significantly reduces electric driving range and may cause limp mode; battery failure is costly and critical for hybrid system health.",
  "Possible Causes": [
    {"cause": "Cell degradation due to age", "probability": 0.6},
    {"cause": "Thermal stress or overheating", "probability": 0.2},
    {"cause": "Manufacturing defects", "probability": 0.1},
    {"cause": "Faulty battery management system", "probability": 0.1}
  ],
  "Symptoms": [
    "Reduced electric-only driving range",
    "Battery warning light on dashboard",
    "Decreased fuel efficiency",
    "Hybrid system limp mode"
  ],
  "Diagnostics": [
    "Battery state of health test",
    "Scan hybrid system fault codes",
    "Temperature sensor check"
  ],
  "Fixes": [
    "Replace faulty battery modules",
    "Repair or replace battery management system",
    "Improve battery cooling system"
  ],
  "Temporary Solutions": [
    "Avoid heavy acceleration",
    "Drive in hybrid mode with low electric demand"
  ]
},

"Throttle Body Carbon Buildup": {
  "Actual Issue": "Carbon deposits restrict throttle plate movement causing poor air flow.",
  "Severity Level": "Moderate — can cause rough idle and reduced power; prolonged neglect may trigger engine warning lights or stalling.",
  "Possible Causes": [
    {"cause": "EGR system introducing exhaust gases", "probability": 0.5},
    {"cause": "PCV system oil vapors", "probability": 0.3},
    {"cause": "Infrequent throttle cleaning", "probability": 0.15},
    {"cause": "Fuel additives not used", "probability": 0.05}
  ],
  "Symptoms": [
    "Rough idle or stalling",
    "Reduced engine power",
    "Check engine light",
    "Poor throttle response"
  ],
  "Diagnostics": [
    "Visual inspection of throttle body",
    "Scan for throttle position sensor codes",
    "Check idle control system"
  ],
  "Fixes": [
    "Clean throttle body with appropriate cleaner",
    "Replace throttle position sensor if faulty"
  ],
  "Temporary Solutions": [
    "Avoid prolonged idling",
    "Use fuel system cleaners"
  ]
},

"Hybrid Brake Regeneration Failure": {
  "Actual Issue": "Regenerative braking system is not recovering energy or providing correct braking force.",
  "Severity Level": "High — reduces braking efficiency and energy recovery; increased wear on friction brakes can lead to costly repairs and decreased safety margin.",
  "Possible Causes": [
    {"cause": "Faulty brake pedal sensor", "probability": 0.35},
    {"cause": "Hybrid control module error", "probability": 0.3},
    {"cause": "Worn brake pads reducing regen effect", "probability": 0.2},
    {"cause": "Low hybrid battery state of charge", "probability": 0.1},
    {"cause": "Electrical wiring faults", "probability": 0.05}
  ],
  "Symptoms": [
    "Brake pedal feels different or inconsistent",
    "Warning light for hybrid system",
    "Reduced energy recovery",
    "Increased wear on traditional brakes"
  ],
  "Diagnostics": [
    "Scan hybrid brake system codes",
    "Test brake pedal sensor operation",
    "Check hybrid battery charge level"
  ],
  "Fixes": [
    "Replace faulty brake pedal sensors",
    "Repair or reprogram hybrid control module",
    "Replace brake pads if worn"
  ],
  "Temporary Solutions": [
    "Drive gently to reduce braking demand",
    "Use traditional brakes carefully"
  ]
},

"Evaporative Emission System Leak": {
  "Actual Issue": "Fuel vapor containment system leak causing fuel smell and emissions warning.",
  "Severity Level": "Moderate — causes increased emissions and possible fuel odor; not immediately dangerous but fails emissions tests and can worsen fuel efficiency.",
  "Possible Causes": [
    {"cause": "Loose or damaged gas cap", "probability": 0.5},
    {"cause": "Cracked or disconnected EVAP hoses", "probability": 0.3},
    {"cause": "Faulty purge valve or vent solenoid", "probability": 0.15},
    {"cause": "Carbon canister damage", "probability": 0.05}
  ],
  "Symptoms": [
    "Fuel odor near vehicle",
    "Check engine light with EVAP codes",
    "Failed emissions test"
  ],
  "Diagnostics": [
    "Smoke test for EVAP leaks",
    "Inspect gas cap condition",
    "Scan EVAP system codes"
  ],
  "Fixes": [
    "Tighten or replace gas cap",
    "Replace cracked hoses",
    "Repair or replace purge valve"
  ],
  "Temporary Solutions": [
    "Ensure gas cap is properly tightened",
    "Avoid refueling in windy conditions"
  ]
},

"Idle Air Control Valve Malfunction": {
  "Actual Issue": "IAC valve fails to regulate air flow at idle causing unstable idle.",
  "Severity Level": "Moderate — causes rough or fluctuating idle and stalling; may trigger check engine light, affecting drivability but usually not immediate safety.",
  "Possible Causes": [
    {"cause": "Carbon deposits on valve", "probability": 0.5},
    {"cause": "Valve electrical failure", "probability": 0.25},
    {"cause": "Vacuum leaks", "probability": 0.15},
    {"cause": "Faulty wiring or connectors", "probability": 0.1}
  ],
  "Symptoms": [
    "Rough or fluctuating idle",
    "Engine stalling at idle",
    "Check engine light"
  ],
  "Diagnostics": [
    "Check IAC valve operation",
    "Inspect for vacuum leaks",
    "Scan for idle control codes"
  ],
  "Fixes": [
    "Clean or replace IAC valve",
    "Repair wiring",
    "Fix vacuum leaks"
  ],
  "Temporary Solutions": [
    "Avoid frequent engine off/on",
    "Keep throttle body clean"
  ]
},

  "Transmission Fluid Overheating": {
  "Actual Issue": "Transmission fluid overheats causing shifting problems and potential damage.",
  "Severity Level": "High — prolonged overheating can cause severe transmission damage and costly repairs; immediate attention required to prevent failure.",
  "Possible Causes": [
    {"cause": "Low transmission fluid level", "probability": 0.4},
    {"cause": "Blocked transmission cooler", "probability": 0.25},
    {"cause": "Faulty transmission pump", "probability": 0.2},
    {"cause": "Severe driving conditions", "probability": 0.1},
    {"cause": "Old or degraded fluid", "probability": 0.05}
  ],
  "Symptoms": [
    "Transmission warning light",
    "Delayed or harsh shifting",
    "Burnt smell from transmission area",
    "Fluid temperature gauge high"
  ],
  "Diagnostics": [
    "Check fluid level and condition",
    "Scan transmission codes",
    "Inspect transmission cooler"
  ],
  "Fixes": [
    "Top up or replace transmission fluid",
    "Clean or replace transmission cooler",
    "Repair or replace transmission pump"
  ],
  "Temporary Solutions": [
    "Avoid towing or heavy loads",
    "Limit stop-and-go driving"
  ]
},

"Oxygen Sensor Intermittent Fault": {
  "Actual Issue": "O2 sensor produces inconsistent signals causing poor fuel mixture adjustments.",
  "Severity Level": "Moderate — leads to poor fuel economy and emissions; prolonged issues can cause catalytic converter damage.",
  "Possible Causes": [
    {"cause": "Wiring harness damage", "probability": 0.35},
    {"cause": "Sensor contamination or aging", "probability": 0.4},
    {"cause": "Exhaust leaks", "probability": 0.15},
    {"cause": "ECU software issues", "probability": 0.1}
  ],
  "Symptoms": [
    "Check engine light intermittent",
    "Poor fuel economy",
    "Rough running",
    "Failed emissions test"
  ],
  "Diagnostics": [
    "Read intermittent O2 sensor codes",
    "Inspect wiring and connectors",
    "Check for exhaust leaks"
  ],
  "Fixes": [
    "Repair wiring",
    "Replace oxygen sensor",
    "Fix exhaust leaks"
  ],
  "Temporary Solutions": [
    "Avoid excessive idling",
    "Use high-quality fuel"
  ]
},

"Exhaust Gas Recirculation (EGR) Valve Failure": {
  "Actual Issue": "EGR valve stuck open or closed, causing improper exhaust gas recirculation.",
  "Severity Level": "Moderate — increases emissions and can cause rough idle or stalling; may lead to engine performance issues over time.",
  "Possible Causes": [
    {"cause": "Carbon buildup causing valve sticking", "probability": 0.5},
    {"cause": "Faulty EGR valve sensor", "probability": 0.25},
    {"cause": "Electrical connector issues", "probability": 0.15},
    {"cause": "Vacuum leaks affecting valve operation", "probability": 0.1}
  ],
  "Symptoms": [
    "Rough idle or stalling",
    "Increased NOx emissions",
    "Check engine light",
    "Poor fuel economy"
  ],
  "Diagnostics": [
    "Scan for EGR-related trouble codes",
    "Inspect EGR valve movement and operation",
    "Check vacuum lines",
    "Perform smoke test for leaks"
  ],
  "Fixes": [
    "Clean carbon deposits from valve",
    "Replace faulty EGR valve or sensor",
    "Repair vacuum lines"
  ],
  "Temporary Solutions": [
    "Drive gently to reduce load on engine",
    "Avoid prolonged idling"
  ]
},

"Catalytic Converter Efficiency Decrease": {
  "Actual Issue": "Catalytic converter becomes clogged or ineffective, increasing emissions.",
  "Severity Level": "High — causes emissions failure and reduced engine performance; prolonged use can damage the engine and lead to costly replacement.",
  "Possible Causes": [
    {"cause": "Contaminants from engine misfire", "probability": 0.4},
    {"cause": "Physical damage or clogging", "probability": 0.3},
    {"cause": "Age and thermal degradation", "probability": 0.2},
    {"cause": "Fuel additives causing deposits", "probability": 0.1}
  ],
  "Symptoms": [
    "Check engine light with P0420/P0430 codes",
    "Reduced engine performance",
    "Poor fuel economy",
    "Failed emissions test"
  ],
  "Diagnostics": [
    "Measure exhaust backpressure",
    "O2 sensor upstream/downstream comparison",
    "Visual inspection"
  ],
  "Fixes": [
    "Replace catalytic converter",
    "Fix underlying misfire issues",
    "Use fuel system cleaners"
  ],
  "Temporary Solutions": [
    "Avoid aggressive driving",
    "Use high-quality fuel"
  ]
},

"Ignition Coil Pack Failure": {
  "Actual Issue": "One or more ignition coils malfunction causing weak or no spark.",
  "Severity Level": "High — causes engine misfires, rough running, and potential catalytic converter damage; can cause drivability loss and increased emissions.",
  "Possible Causes": [
    {"cause": "Coil internal winding failure", "probability": 0.5},
    {"cause": "Overheating due to poor cooling", "probability": 0.25},
    {"cause": "Connector or wiring issues", "probability": 0.15},
    {"cause": "Faulty engine control module", "probability": 0.1}
  ],
  "Symptoms": [
    "Engine misfire",
    "Rough running or hesitation",
    "Reduced power and fuel economy",
    "Check engine light"
  ],
  "Diagnostics": [
    "Check coil resistance and output",
    "Scan for misfire codes",
    "Inspect wiring and connectors"
  ],
  "Fixes": [
    "Replace faulty ignition coils",
    "Repair wiring",
    "Check cooling system"
  ],
  "Temporary Solutions": [
    "Avoid heavy acceleration",
    "Drive at moderate speeds"
  ]
},

"PCV Valve Failure": {
  "Actual Issue": "PCV valve stuck open or closed leading to increased crankcase pressure or vacuum leaks.",
  "Severity Level": "Moderate — causes rough idle and potential oil leaks; long-term neglect can lead to engine sludge and gasket failure.",
  "Possible Causes": [
    {"cause": "Valve clogging with sludge or oil", "probability": 0.6},
    {"cause": "Broken valve spring or diaphragm", "probability": 0.2},
    {"cause": "Faulty valve gasket", "probability": 0.1},
    {"cause": "Disconnected or damaged hoses", "probability": 0.1}
  ],
  "Symptoms": [
    "Rough idle",
    "Oil leaks",
    "High or fluctuating RPM at idle",
    "Increased oil consumption"
  ],
  "Diagnostics": [
    "Inspect PCV valve operation",
    "Check for vacuum leaks",
    "Visual inspection of hoses"
  ],
  "Fixes": [
    "Replace PCV valve",
    "Repair or replace damaged hoses"
  ],
  "Temporary Solutions": [
    "Avoid high RPM driving",
    "Use fuel system cleaner additives"
  ]
},

"Fuel Pump Relay Fault": {
  "Actual Issue": "Fuel pump relay intermittently fails causing fuel delivery loss.",
  "Severity Level": "High — can cause engine stalls and no-start conditions, potentially leaving vehicle stranded; urgent repair recommended.",
  "Possible Causes": [
    {"cause": "Relay contact wear", "probability": 0.5},
    {"cause": "Corroded relay socket or terminals", "probability": 0.25},
    {"cause": "Faulty wiring or connectors", "probability": 0.15},
    {"cause": "Failed fuel pump", "probability": 0.1}
  ],
  "Symptoms": [
    "Intermittent engine stalls",
    "No start condition",
    "Fuel pump not activating",
    "Clicking sound near relay"
  ],
  "Diagnostics": [
    "Check relay resistance and operation",
    "Scan for fuel system codes",
    "Inspect wiring harness"
  ],
  "Fixes": [
    "Replace faulty relay",
    "Repair wiring and connectors",
    "Replace fuel pump if needed"
  ],
  "Temporary Solutions": [
    "Tap relay gently to temporarily restore contact",
    "Turn ignition off and on to reset"
  ]
},

"Coolant Temperature Sensor Fault": {
  "Actual Issue": "Faulty sensor provides incorrect temperature readings affecting fuel and ignition.",
  "Severity Level": "Moderate — causes poor cold start and engine management issues; can lead to overheating if not addressed.",
  "Possible Causes": [
    {"cause": "Sensor element failure", "probability": 0.6},
    {"cause": "Wiring damage or corrosion", "probability": 0.25},
    {"cause": "Faulty ECU input", "probability": 0.1},
    {"cause": "Poor sensor mounting or seal", "probability": 0.05}
  ],
  "Symptoms": [
    "Engine overheating warning light",
    "Poor cold start behavior",
    "Erratic temperature gauge",
    "Check engine light"
  ],
  "Diagnostics": [
    "Scan for coolant temp codes",
    "Test sensor resistance at various temps",
    "Inspect wiring harness"
  ],
  "Fixes": [
    "Replace coolant temperature sensor",
    "Repair wiring",
    "Check ECU inputs"
  ],
  "Temporary Solutions": [
    "Avoid heavy engine load",
    "Monitor engine temperature gauge"
  ]
},

"Hybrid Inverter Cooling System Failure": {
  "Actual Issue": "Cooling system for hybrid inverter fails, causing overheating and system derate.",
  "Severity Level": "High — inverter overheating leads to reduced hybrid performance and potential component damage; urgent repair advised.",
  "Possible Causes": [
    {"cause": "Coolant leak in inverter system", "probability": 0.4},
    {"cause": "Faulty inverter coolant pump", "probability": 0.3},
    {"cause": "Clogged cooling passages", "probability": 0.2},
    {"cause": "Sensor or thermostat failure", "probability": 0.1}
  ],
  "Symptoms": [
    "Hybrid warning light",
    "Reduced power from electric motor",
    "Unusual heat from inverter area",
    "System enters limp mode"
  ],
  "Diagnostics": [
    "Check inverter coolant level and pressure",
    "Scan hybrid control module for faults",
    "Test coolant pump operation"
  ],
  "Fixes": [
    "Repair coolant leaks",
    "Replace inverter coolant pump",
    "Flush and clean cooling system"
  ],
  "Temporary Solutions": [
    "Avoid heavy hybrid system usage",
    "Limit stop/start cycles"
  ]
},

"Turbocharger Wastegate Malfunction": {
  "Actual Issue": "Wastegate fails to open or close properly, causing overboost or underboost conditions.",
  "Severity Level": "Moderate to High — can cause engine performance loss and risk of engine damage if overboost occurs; timely diagnosis and repair required.",
  "Possible Causes": [
    {"cause": "Stuck wastegate actuator due to carbon buildup", "probability": 0.45},
    {"cause": "Vacuum leak in actuator hose", "probability": 0.25},
    {"cause": "Faulty wastegate solenoid valve", "probability": 0.15},
    {"cause": "Damaged wastegate spring", "probability": 0.1},
    {"cause": "ECU control error", "probability": 0.05}
  ],
  "Symptoms": [
    "Loss of power or hesitation under boost",
    "Check engine light with turbo codes",
    "Poor acceleration",
    "High exhaust temperatures"
  ],
  "Diagnostics": [
    "Check boost pressure with gauge",
    "Inspect wastegate actuator and hoses",
    "Scan for turbocharger-related trouble codes",
    "Smoke test for vacuum leaks"
  ],
  "Fixes": [
    "Clean or replace wastegate actuator",
    "Repair or replace vacuum hoses",
    "Replace faulty solenoid valve",
    "Reprogram ECU if needed"
  ],
  "Temporary Solutions": [
    "Avoid heavy acceleration",
    "Limit engine load until fixed"
  ]
},

"Hybrid Battery Cell Imbalance": {
  "Actual Issue": "Individual battery cells in the hybrid pack have uneven charge or voltage levels causing reduced battery performance.",
  "Severity Level": "High — prolonged imbalance can damage battery cells, reduce pack lifespan, and impair hybrid system performance; timely rebalancing advised.",
  "Possible Causes": [
    {"cause": "Aging cells with capacity loss", "probability": 0.5},
    {"cause": "Poor battery management system (BMS) balancing", "probability": 0.3},
    {"cause": "Corrosion or poor electrical contacts", "probability": 0.1},
    {"cause": "Thermal management issues", "probability": 0.1}
  ],
  "Symptoms": [
    "Reduced electric-only range",
    "Hybrid warning light on dashboard",
    "Inconsistent battery state of charge readings",
    "Reduced regenerative braking efficiency"
  ],
  "Diagnostics": [
    "Battery pack voltage and current analysis",
    "Cell voltage monitoring with diagnostic tools",
    "Thermal imaging for hotspots",
    "BMS error code retrieval"
  ],
  "Fixes": [
    "Battery pack rebalancing via BMS",
    "Replace faulty cells or modules",
    "Clean and tighten electrical connections",
    "Improve cooling system for battery pack"
  ],
  "Temporary Solutions": [
    "Limit electric mode driving",
    "Avoid rapid acceleration and deceleration"
  ]
},

"Variable Valve Timing (VVT) Solenoid Failure": {
  "Actual Issue": "VVT solenoid fails to actuate the camshaft timing correctly, causing poor engine performance.",
  "Severity Level": "Moderate — causes drivability issues and fuel inefficiency; early repair prevents engine damage or emissions failure.",
  "Possible Causes": [
    {"cause": "Solenoid coil failure", "probability": 0.4},
    {"cause": "Clogged oil passages or debris", "probability": 0.35},
    {"cause": "Faulty camshaft position sensor", "probability": 0.15},
    {"cause": "Electrical wiring or connector damage", "probability": 0.1}
  ],
  "Symptoms": [
    "Check engine light with VVT-related codes",
    "Rough idle or hesitation",
    "Reduced fuel economy",
    "Loss of power at certain RPM ranges"
  ],
  "Diagnostics": [
    "Scan for VVT trouble codes",
    "Test solenoid electrical resistance",
    "Inspect oil quality and pressure",
    "Visual inspection of wiring and connectors"
  ],
  "Fixes": [
    "Replace VVT solenoid",
    "Clean or change engine oil",
    "Repair wiring",
    "Replace camshaft position sensor if faulty"
  ],
  "Temporary Solutions": [
    "Avoid heavy engine load",
    "Use high-quality synthetic oil"
  ]
},

"Fuel Injector Clogging": {
  "Actual Issue": "Fuel injectors partially blocked, causing uneven fuel spray and poor combustion.",
  "Severity Level": "Moderate to High — results in misfires and reduced performance; prolonged clogging risks catalytic converter damage.",
  "Possible Causes": [
    {"cause": "Poor fuel quality with deposits", "probability": 0.5},
    {"cause": "Aging injectors with wear", "probability": 0.25},
    {"cause": "Contaminated fuel filters", "probability": 0.15},
    {"cause": "Corroded injector electrical connectors", "probability": 0.1}
  ],
  "Symptoms": [
    "Engine misfires",
    "Rough idle",
    "Poor acceleration",
    "Increased emissions"
  ],
  "Diagnostics": [
    "Injector balance testing",
    "Fuel pressure and volume test",
    "Visual inspection of fuel filters",
    "Electrical testing of injector connectors"
  ],
  "Fixes": [
    "Use fuel injector cleaner additives",
    "Replace fuel filters",
    "Replace or clean fuel injectors",
    "Repair wiring and connectors"
  ],
  "Temporary Solutions": [
    "Use high-quality fuel",
    "Avoid prolonged idling"
  ]
},

"Transmission Torque Converter Lockup Failure": {
  "Actual Issue": "Torque converter clutch fails to lock up, causing slipping and increased fuel consumption.",
  "Severity Level": "High — causes fuel economy loss and potential transmission overheating; can lead to transmission damage if untreated.",
  "Possible Causes": [
    {"cause": "Faulty torque converter clutch solenoid", "probability": 0.4},
    {"cause": "Low transmission fluid level or quality", "probability": 0.3},
    {"cause": "Worn clutch plates", "probability": 0.2},
    {"cause": "Transmission control module malfunction", "probability": 0.1}
  ],
  "Symptoms": [
    "Transmission slipping at highway speeds",
    "Poor fuel economy",
    "Overheating transmission",
    "Delayed or harsh shifts"
  ],
  "Diagnostics": [
    "Scan transmission control module codes",
    "Check transmission fluid condition and level",
    "Test clutch solenoid operation",
    "Pressure test transmission hydraulics"
  ],
  "Fixes": [
    "Replace clutch solenoid",
    "Change transmission fluid and filter",
    "Rebuild or replace torque converter",
    "Reprogram transmission control module"
  ],
  "Temporary Solutions": [
    "Avoid high-speed cruising",
    "Limit heavy acceleration"
  ]
},

"Rough Acceleration": {
  "Actual Issue": "Acceleration stumbles due to ignition or fuel delivery issues.",
  "Severity Level": "Moderate — affects drivability and safety; early diagnosis helps prevent engine damage or stalling.",
  "Possible Causes": [
    {"cause": "Dirty throttle body or MAF sensor", "probability": 0.3},
    {"cause": "Clogged fuel filter or bad fuel pump", "probability": 0.25},
    {"cause": "Faulty spark plugs or coils", "probability": 0.3},
    {"cause": "Transmission or clutch issues", "probability": 0.15}
  ],
  "Diagnostics": [
    "Scan for engine codes",
    "Test fuel pressure at rail",
    "Inspect spark plugs and throttle body",
    "Check air intake and MAF sensor readings"
  ],
  "Fixes": [
    "Clean throttle body and MAF sensor",
    "Replace fuel filter or faulty pump",
    "Replace plugs or coils",
    "Adjust clutch or check transmission mounts"
  ],
  "Temporary Solutions": [
    "Accelerate gently",
    "Avoid uphill driving or overtaking until resolved"
  ]
},

"Turbocharger Lag or Hesitation": {
  "Actual Issue": "Sluggish acceleration, especially at low RPM in turbocharged engines.",
  "Severity Level": "Moderate — reduces performance and drivability; prolonged boost issues can stress engine components.",
  "Possible Causes": [
    {"cause": "Electronic wastegate actuator malfunction", "probability": 0.25},
    {"cause": "Boost leak from intercooler or hoses", "probability": 0.35},
    {"cause": "Faulty turbo boost pressure sensor", "probability": 0.2},
    {"cause": "Clogged air filter or dirty MAF sensor", "probability": 0.2}
  ],
  "Symptoms": [
    "Engine hesitation",
    "Reduced power delivery",
    "Whistling noise or abnormal turbo sounds"
  ],
  "Diagnostics": [
    "OBD scan for turbo-related codes (e.g. P0299)",
    "Pressure testing boost lines",
    "Test actuator response with diagnostic tool"
  ],
  "Fixes": [
    "Tighten or replace boost hoses",
    "Clean or replace MAF sensor",
    "Replace wastegate actuator if unresponsive"
  ],
  "Temporary Solutions": [
    "Limit hard acceleration until resolved"
  ]
},

"Tire Wear & Alignment": {
  "Actual Issue": "Uneven or excessive tire wear affects handling, comfort, and safety.",
  "Severity Level": "Moderate — poor alignment can lead to unsafe handling and premature tire failure; timely correction recommended.",
  "Possible Causes": [
    {"cause": "Improper wheel alignment", "probability": 0.35},
    {"cause": "Unbalanced tires", "probability": 0.25},
    {"cause": "Under or overinflation", "probability": 0.25},
    {"cause": "Worn suspension components", "probability": 0.15}
  ],
  "Diagnostics": [
    "Visually inspect tire tread for uneven wear patterns",
    "Check tire pressure with gauge",
    "Measure tread depth across the tire width",
    "Inspect alignment angles and suspension bushings"
  ],
  "Fixes": [
    "Perform wheel alignment",
    "Balance tires",
    "Inflate to manufacturer-recommended PSI",
    "Replace worn suspension components"
  ],
  "Temporary Solutions": [
    "Rotate tires to reduce further uneven wear",
    "Drive slower and avoid cornering aggressively"
  ]
},

"AC or Heater Problems": {
  "Actual Issue": "Ineffective cooling or heating affects cabin comfort.",
  "Severity Level": "Low to Moderate — primarily comfort issues; severe HVAC faults can affect window defrosting and visibility safety.",
  "Possible Causes": [
    {"cause": "Low refrigerant (AC)", "probability": 0.35},
    {"cause": "Faulty blower motor", "probability": 0.25},
    {"cause": "Clogged cabin air filter", "probability": 0.2},
    {"cause": "Bad thermostat or heater core (heater)", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check airflow from vents",
    "Listen for blower motor noise",
    "Inspect refrigerant pressure (AC)",
    "Feel for hose temperature differences (heater)"
  ],
  "Fixes": [
    "Recharge AC refrigerant",
    "Replace blower motor or fuse",
    "Change cabin air filter",
    "Replace thermostat or flush heater core"
  ],
  "Temporary Solutions": [
    "Use recirculation mode to improve air efficiency",
    "Crack windows slightly if heating/cooling is weak"
  ]
},

"Dashboard Warning Lights": {
  "Actual Issue": "Warning lights indicate system issues that may need urgent attention.",
  "Severity Level": "Varies — some warnings indicate critical faults (e.g., engine or brake), others minor; always scan codes promptly.",
  "Possible Causes": [
    {"cause": "Sensor malfunction", "probability": 0.3},
    {"cause": "Low fluid levels (oil, brake, coolant)", "probability": 0.25},
    {"cause": "Battery/charging issues", "probability": 0.2},
    {"cause": "Transmission or engine fault", "probability": 0.25}
  ],
  "Diagnostics": [
    "Scan with OBD-II for fault codes",
    "Visually check fluid levels",
    "Test battery voltage and alternator output",
    "Note patterns of light appearance (steady, blinking)"
  ],
  "Fixes": [
    "Fix root issue based on fault code",
    "Top up or change fluids",
    "Replace faulty sensors",
    "Repair damaged wiring or replace faulty component"
  ],
  "Temporary Solutions": [
    "Clear codes to monitor recurrence (only if safe)",
    "Drive conservatively and monitor system behavior"
  ]
},

"Steering Noise": {
  "Actual Issue": "Clunks, whining, or creaks while steering may indicate worn or dry components.",
  "Severity Level": "Moderate — may affect steering feel and safety; worn joints can cause sudden failure if ignored.",
  "Possible Causes": [
    {"cause": "Low power steering fluid", "probability": 0.35},
    {"cause": "Worn tie rod ends or ball joints", "probability": 0.3},
    {"cause": "Dry suspension bushings", "probability": 0.2},
    {"cause": "Rack and pinion damage", "probability": 0.15}
  ],
  "Diagnostics": [
    "Listen while turning at low speeds",
    "Inspect fluid reservoir for level and leaks",
    "Jack up car and manually turn wheels to feel resistance",
    "Check joints for play"
  ],
  "Fixes": [
    "Top up or flush power steering fluid",
    "Replace worn tie rods or ball joints",
    "Lubricate or replace bushings",
    "Repair or replace steering rack"
  ],
  "Temporary Solutions": [
    "Avoid full-lock steering turns",
    "Drive gently on rough surfaces"
  ]
},

"Fuel Smells": {
  "Actual Issue": "Strong fuel odors indicate possible leaks or evaporative system failure.",
  "Severity Level": "High — fuel leaks pose fire hazards and environmental risks; immediate inspection recommended.",
  "Possible Causes": [
    {"cause": "Loose or damaged fuel cap", "probability": 0.4},
    {"cause": "Leaking fuel lines or injectors", "probability": 0.4},
    {"cause": "Faulty charcoal canister or EVAP purge valve", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check cap seal and click tightness",
    "Inspect for fuel drips under car or engine bay",
    "Scan EVAP system codes (e.g., P0442, P0455)",
    "Sniff near engine/fuel tank when car is cold"
  ],
  "Fixes": [
    "Replace fuel cap",
    "Repair or replace fuel line fittings",
    "Replace EVAP canister or purge valve"
  ],
  "Temporary Solutions": [
    "Avoid parking in enclosed areas",
    "Limit driving and keep windows open"
  ]
},

"GDI Carbon Buildup": {
  "Actual Issue": "Excessive carbon accumulation on intake valves in GDI engines.",
  "Severity Level": "Moderate — causes drivability issues and misfires; if untreated, may require costly intake cleaning.",
  "Possible Causes": [
    {"cause": "No fuel spray over intake valves in GDI engines", "probability": 0.5},
    {"cause": "Short trip driving habits", "probability": 0.3},
    {"cause": "PCV system oil vapor condensation", "probability": 0.2}
  ],
  "Symptoms": [
    "Rough idle",
    "Check engine light (random misfire codes)",
    "Hesitation under acceleration"
  ],
  "Diagnostics": [
    "Borescope inspection of intake valves",
    "Scan for misfire codes (P0300 series)",
    "Intake manifold removal and visual inspection"
  ],
  "Fixes": [
    "Walnut blasting of intake valves",
    "Install oil catch can",
    "Use of GDI-safe fuel additives periodically"
  ],
  "Temporary Solutions": [
    "Occasionally rev engine fully warm to help burn off deposits"
  ]
},

"Brake Squeal or Grinding": {
  "Actual Issue": "High-pitched squeals or grinding indicate worn pads or rotor damage.",
  "Severity Level": "Moderate — affects braking performance and safety; worn pads should be replaced promptly.",
  "Possible Causes": [
    {"cause": "Worn brake pads", "probability": 0.5},
    {"cause": "Glazed pads or rotors", "probability": 0.2},
    {"cause": "Debris caught between pad and rotor", "probability": 0.2},
    {"cause": "Missing anti-rattle clips or shims", "probability": 0.1}
  ],
  "Diagnostics": [
    "Listen for squealing when braking lightly",
    "Inspect pad thickness and rotor surface",
    "Look for dust, rust, or scoring",
    "Test braking effectiveness on flat surface"
  ],
  "Fixes": [
    "Replace brake pads and possibly rotors",
    "Clean caliper assembly",
    "Install new shims or clips",
    "Apply anti-squeal lubricant to pads"
  ],
  "Temporary Solutions": [
    "Drive slowly and avoid hard braking",
    "Tap brakes briefly to dislodge debris"
  ]
},
  "Brake Pedal Pulsation or Vibration": {
  "Actual Issue": "Brake pedal shakes or pulses when braking, usually due to rotor issues.",
  "Severity Level": "Moderate — affects braking stability and safety; timely rotor service needed to avoid worsening.",
  "Possible Causes": [
    {"cause": "Warped brake rotors", "probability": 1.0}
  ],
  "Diagnostics": [
    "Check for rotor runout using a dial indicator",
    "Inspect rotor surfaces for uneven wear"
  ],
  "Fixes": [
    "Resurface warped brake rotors",
    "Replace rotors if resurfacing is not sufficient"
  ],
  "Temporary Solutions": [
    "Reduce speed and brake gently until issue is resolved"
  ]
},

"Soft or Spongy Brake Pedal": {
  "Actual Issue": "Brake pedal feels soft or sinks to the floor when pressed.",
  "Severity Level": "High — indicates possible brake fluid or hydraulic issues; critical for safe braking, fix urgently.",
  "Possible Causes": [
    {"cause": "Air trapped in brake lines", "probability": 0.6},
    {"cause": "Low or contaminated brake fluid", "probability": 0.4}
  ],
  "Diagnostics": [
    "Inspect brake fluid level and condition",
    "Perform brake line bleeding to check for air bubbles"
  ],
  "Fixes": [
    "Bleed the brake system to remove air",
    "Refill or replace brake fluid as needed"
  ],
  "Temporary Solutions": [
    "Pump brake pedal gently to regain firmness in emergency"
  ]
},

"Knocking or Pinging Under Load": {
  "Actual Issue": "Engine produces knocking or pinging sounds during acceleration or load.",
  "Severity Level": "Moderate — can cause engine damage if untreated; requires timely tuning or fuel upgrade.",
  "Possible Causes": [
    {"cause": "Low octane fuel", "probability": 0.5},
    {"cause": "Carbon buildup in combustion chamber", "probability": 0.3},
    {"cause": "Incorrect ignition timing", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check fuel octane rating used",
    "Inspect for carbon buildup in combustion chambers",
    "Scan and verify ignition timing parameters"
  ],
  "Fixes": [
    "Switch to higher octane fuel",
    "Perform engine decarbonization",
    "Adjust or inspect ignition timing"
  ],
  "Temporary Solutions": [
    "Avoid heavy acceleration until issue is resolved"
  ]
},

"Ticking or Clicking Noise from Engine": {
  "Actual Issue": "Ticking sound from engine area, often due to lubrication or valvetrain issues.",
  "Severity Level": "Moderate — lubrication faults can cause engine wear; early oil checks and repairs prevent damage.",
  "Possible Causes": [
    {"cause": "Low oil pressure", "probability": 0.6},
    {"cause": "Worn or malfunctioning valve lifters", "probability": 0.4}
  ],
  "Diagnostics": [
    "Check engine oil level and condition",
    "Use oil pressure gauge to verify pressure",
    "Listen with mechanic’s stethoscope to locate source"
  ],
  "Fixes": [
    "Refill or replace engine oil",
    "Replace faulty valve lifters",
    "Perform valve lash adjustment if required"
  ],
  "Temporary Solutions": [
    "Drive gently and monitor oil level frequently"
  ]
},

"VVT System Failure": {
  "Actual Issue": "Timing-related performance issues due to VVT malfunction.",
  "Severity Level": "Moderate — causes drivability issues and fuel inefficiency; timely maintenance recommended.",
  "Possible Causes": [
    {"cause": "Dirty or sludged oil blocking VVT solenoid", "probability": 0.5},
    {"cause": "Faulty camshaft actuator", "probability": 0.3},
    {"cause": "Low oil pressure", "probability": 0.2}
  ],
  "Symptoms": [
    "Rattling noise on cold start",
    "Poor throttle response",
    "Check engine light (P0010–P0015)"
  ],
  "Diagnostics": [
    "Check oil level and cleanliness",
    "Test VVT solenoid actuation",
    "Scan for camshaft timing error codes"
  ],
  "Fixes": [
    "Replace VVT solenoid",
    "Perform oil flush or change with correct spec",
    "Replace actuator if mechanically stuck"
  ],
  "Temporary Solutions": [
    "Avoid aggressive driving until resolved"
  ]
},

"Hissing or Steam Sound from Engine Bay": {
  "Actual Issue": "High-pitched hissing or steam noise from under the hood, typically due to leaks or overheating.",
  "Severity Level": "High — potential coolant leaks or overheating can cause engine damage; inspect urgently.",
  "Possible Causes": [
    {"cause": "Vacuum leak", "probability": 0.4},
    {"cause": "Coolant leak", "probability": 0.4},
    {"cause": "Engine overheating", "probability": 0.2}
  ],
  "Diagnostics": [
    "Inspect all vacuum hoses for cracks or disconnections",
    "Check coolant level and look for visible leaks or steam",
    "Monitor engine temperature gauge"
  ],
  "Fixes": [
    "Replace or reconnect damaged vacuum hoses",
    "Repair coolant system leaks",
    "Ensure radiator and fan are functioning properly"
  ],
  "Temporary Solutions": [
    "Let engine cool before opening hood",
    "Avoid driving until leak or overheating issue is resolved"
  ]
},

"Engine Stalling": {
  "Actual Issue": "Engine shuts off unexpectedly during idle or driving.",
  "Severity Level": "High — sudden stalling is a safety hazard; prompt diagnosis and repair required.",
  "Possible Causes": [
    {"cause": "Faulty idle air control valve (IAC)", "probability": 0.3},
    {"cause": "Vacuum leak", "probability": 0.25},
    {"cause": "Fuel delivery issue", "probability": 0.25},
    {"cause": "Crankshaft position sensor failure", "probability": 0.2}
  ],
  "Diagnostics": [
    "Scan for error codes",
    "Inspect vacuum hoses",
    "Monitor fuel pressure",
    "Check RPM behavior at idle"
  ],
  "Fixes": [
    "Clean or replace IAC valve",
    "Seal vacuum leaks",
    "Replace crankshaft sensor",
    "Repair fuel system"
  ],
  "Temporary Solutions": [
    "Keep engine revved slightly at stops",
    "Avoid idling with AC or lights on"
  ]
},

"Oil Dilution in Turbocharged Engines": {
  "Actual Issue": "Fuel mixes with engine oil, reducing lubrication and increasing wear.",
  "Severity Level": "Moderate — increases engine wear and oil degradation; oil change frequency should increase.",
  "Possible Causes": [
    {"cause": "Short driving cycles in cold weather", "probability": 0.4},
    {"cause": "Fuel-rich air-fuel mixtures", "probability": 0.35},
    {"cause": "Worn piston rings", "probability": 0.25}
  ],
  "Symptoms": [
    "Oil level rising above full mark",
    "Strong fuel smell in oil",
    "Check engine light in severe cases"
  ],
  "Diagnostics": [
    "Oil analysis for fuel content",
    "Examine engine run time patterns",
    "Look for rich fuel codes (P0172)"
  ],
  "Fixes": [
    "Change oil more frequently",
    "ECU software update to adjust injection timing",
    "Address ring seal wear if chronic"
  ],
  "Temporary Solutions": [
    "Drive longer distances to allow full warm-up and fuel vapor burn-off"
  ]
},

"Hybrid Battery Cooling Fan Blocked": {
  "Actual Issue": "Overheating of hybrid battery due to clogged or faulty cooling fan.",
  "Severity Level": "High — overheating risks battery damage and reduced hybrid performance; fix urgently.",
  "Possible Causes": [
    {"cause": "Dust/pet hair buildup in fan intake", "probability": 0.5},
    {"cause": "Faulty cooling fan motor", "probability": 0.3},
    {"cause": "Temperature sensor failure", "probability": 0.2}
  ],
  "Symptoms": [
    "Warning light for hybrid system",
    "Battery fan running loud",
    "Reduced power output"
  ],
  "Diagnostics": [
    "Scan for HV battery cooling codes",
    "Visual inspection of fan duct",
    "Monitor battery temperature sensors"
  ],
  "Fixes": [
    "Clean fan and intake duct",
    "Replace defective fan motor",
    "Replace battery temp sensor if readings are abnormal"
  ],
  "Temporary Solutions": [
    "Turn off AC to reduce battery strain, ventilate cabin"
  ]
},

"Hybrid Brake Regeneration Fault": {
  "Actual Issue": "Regenerative braking system fails or partially works.",
  "Severity Level": "Moderate — reduces braking efficiency and fuel economy; timely fix recommended.",
  "Possible Causes": [
    {"cause": "Faulty brake booster or sensor", "probability": 0.4},
    {"cause": "ABS module malfunction", "probability": 0.3},
    {"cause": "Inconsistent regen-brake software response", "probability": 0.3}
  ],
  "Symptoms": [
    "Brake pedal feels inconsistent",
    "Reduced fuel efficiency",
    "ABS or brake warning lights"
  ],
  "Diagnostics": [
    "OBD scan for ABS or hybrid codes",
    "Test brake booster vacuum pressure",
    "Review regen braking history if available"
  ],
  "Fixes": [
    "Reprogram or recalibrate brake module",
    "Replace faulty sensor or ABS unit",
    "Flush brake fluid if degraded"
  ],
  "Temporary Solutions": [
    "Drive gently and avoid abrupt braking"
  ]
},

"Engine Overheating in Traffic": {
  "Actual Issue": "Temperature rises mainly in slow or idle conditions.",
  "Severity Level": "High — sustained overheating causes engine damage; fix cooling system urgently.",
  "Possible Causes": [
    {"cause": "Cooling fan not working", "probability": 0.4},
    {"cause": "Clogged radiator", "probability": 0.35},
    {"cause": "Thermostat stuck closed", "probability": 0.25}
  ],
  "Diagnostics": [
    "Check fan operation with engine on",
    "Inspect radiator for debris or rust",
    "Check coolant flow after warm-up"
  ],
  "Fixes": [
    "Replace fan motor or relay",
    "Flush or replace radiator",
    "Replace thermostat"
  ],
  "Temporary Solutions": [
    "Turn off AC and rev engine slightly to cool",
    "Turn on heater to draw heat from engine"
  ]
},

  "Loud Exhaust Noise or Popping": {
    "Actual Issue": "Unusual loudness or popping sounds from the exhaust system.",
    "Possible Causes": [
      {"cause": "Exhaust leak", "probability": 0.45},
      {"cause": "Damaged muffler", "probability": 0.35},
      {"cause": "Faulty catalytic converter", "probability": 0.2}
    ],
    "Diagnostics": [
      "Inspect exhaust system for leaks or holes",
      "Check muffler and piping condition",
      "Scan for catalytic converter error codes"
    ],
    "Fixes": [
      "Seal or weld exhaust leaks",
      "Replace damaged muffler",
      "Install new catalytic converter if faulty"
    ],
    "Temporary Solutions": [
      "Avoid prolonged driving to prevent further damage or emissions issues"
    ]
  },

  "Battery Diagnosis": {
    "Functions": [
      "Supplies power to starter motor and ignition system",
      "Acts as chassis ground",
      "Stores alternator-generated energy"
    ],
    "Types of Batteries": [
      "Conventional lead-acid",
      "Low-maintenance",
      "Maintenance-free"
    ],
    "Maintenance Tips": [
      "Check and maintain electrolyte levels",
      "Clean terminals and apply petroleum jelly",
      "Disconnect battery if unused for long periods"
    ],
    "Troubleshooting Steps": [
      "Turn off all accessories",
      "Inspect for corrosion and tightness",
      "Use voltmeter to check voltage (should be ~12.6V)",
      "Charge if voltage is <12.4V"
    ]
  },

  "Clunking or Knocking When Going Over Bumps": {
    "Actual Issue": "Loud impact or knocking noise from suspension area when driving over uneven surfaces.",
    "Possible Causes": [
      {"cause": "Worn shock absorbers or struts", "probability": 0.45},
      {"cause": "Damaged suspension bushings", "probability": 0.35},
      {"cause": "Worn ball joints", "probability": 0.2}
    ],
    "Diagnostics": [
      "Visually inspect shocks and struts for leaks or damage",
      "Check suspension bushings for cracks or looseness",
      "Jack up vehicle and test ball joint play"
    ],
    "Fixes": [
      "Replace worn shock absorbers or struts",
      "Replace worn or damaged bushings",
      "Replace worn ball joints"
    ],
    "Temporary Solutions": [
      "Drive at slower speeds over bumps to reduce stress"
    ]
  },

  "Creaking or Squeaking When Turning Steering Wheel": {
    "Actual Issue": "Audible creaking or squeaking while turning, indicating friction or wear in the steering system.",
    "Possible Causes": [
      {"cause": "Dry or worn power steering components", "probability": 0.6},
      {"cause": "Worn or unlubricated bushings", "probability": 0.4}
    ],
    "Diagnostics": [
      "Listen for noise source while turning wheel at low speed",
      "Inspect steering linkage and bushings",
      "Check for lubrication points"
    ],
    "Fixes": [
      "Lubricate dry components or bushings",
      "Replace worn power steering parts",
      "Replace deteriorated bushings"
    ],
    "Temporary Solutions": [
      "Avoid full lock turns until serviced"
    ]
  },

  "Grinding or Growling When Turning": {
    "Actual Issue": "Harsh grinding noise while turning the steering wheel, often due to power steering issues.",
    "Possible Causes": [
      {"cause": "Low power steering fluid", "probability": 0.6},
      {"cause": "Worn or failing power steering pump", "probability": 0.4}
    ],
    "Diagnostics": [
      "Check power steering fluid level and condition",
      "Listen to pump operation while turning",
      "Inspect for fluid leaks"
    ],
    "Fixes": [
      "Refill power steering fluid",
      "Repair leaks in the power steering system",
      "Replace worn power steering pump"
    ],
    "Temporary Solutions": [
      "Avoid tight turns and check fluid level frequently"
    ]
  },

  "Loose or Rattling Noise from Undercarriage": {
    "Actual Issue": "Rattling or clanking noise from underneath vehicle, indicating unsecured components.",
    "Possible Causes": [
      {"cause": "Loose heat shields", "probability": 0.4},
      {"cause": "Loose exhaust system parts", "probability": 0.35},
      {"cause": "Worn or loose suspension components", "probability": 0.25}
    ],
    "Diagnostics": [
      "Inspect undercarriage for any visibly loose parts",
      "Check heat shields and exhaust hangers",
      "Check for worn suspension bolts or mounts"
    ],
    "Fixes": [
      "Tighten or replace heat shields and exhaust brackets",
      "Replace loose suspension hardware",
      "Secure or repair affected undercarriage components"
    ],
    "Temporary Solutions": [
      "Avoid rough roads; check for further loosening regularly"
    ]
  },

  "Whining Noise When Accelerating": {
    "Actual Issue": "High-pitched whining sound during acceleration, usually from drivetrain components.",
    "Possible Causes": [
      {"cause": "Low transmission fluid", "probability": 0.6},
      {"cause": "Worn gears or bearings in transmission", "probability": 0.4}
    ],
    "Diagnostics": [
      "Check transmission fluid level and condition",
      "Listen for noise under acceleration",
      "Inspect for transmission leaks"
    ],
    "Fixes": [
      "Refill or replace transmission fluid",
      "Repair or replace worn transmission gears"
    ],
    "Temporary Solutions": [
      "Drive gently to reduce drivetrain load until repaired"
    ]
  },

  "Clunking Noise When Shifting Gears": {
    "Actual Issue": "Heavy clunk or thud sound when changing gears, indicating looseness in transmission mounts or clutch system.",
    "Possible Causes": [
      {"cause": "Worn clutch components", "probability": 0.6},
      {"cause": "Damaged or degraded transmission mounts", "probability": 0.4}
    ],
    "Diagnostics": [
      "Inspect clutch operation and engagement",
      "Check transmission and engine mounts for movement",
      "Listen for clunk during gear shift"
    ],
    "Fixes": [
      "Replace worn clutch components",
      "Replace faulty transmission mounts"
    ],
    "Temporary Solutions": [
      "Shift gears gently and avoid aggressive driving"
    ]
  },

  "Transmission Slipping": {
    "Actual Issue": "Engine revs but car does not accelerate properly.",
    "Possible Causes": [
      {"cause": "Low transmission fluid", "probability": 0.5},
      {"cause": "Worn clutch plates", "probability": 0.3},
      {"cause": "Faulty transmission solenoids", "probability": 0.2}
    ],
    "Diagnostics": [
      "Check transmission fluid level and smell",
      "Scan for transmission fault codes",
      "Observe RPM vs speed during acceleration"
    ],
    "Fixes": [
      "Top up or change transmission fluid",
      "Repair internal clutch packs",
      "Replace faulty solenoids"
    ],
    "Temporary Solutions": [
      "Avoid rapid acceleration or hill climbing",
      "Drive in lower gear if possible"
    ]
  },

  "Clicking or Popping During Turns": {
    "Actual Issue": "Repeated clicking or popping noise when turning, typically from CV joints or axles.",
    "Possible Causes": [
      {"cause": "Worn CV joints", "probability": 0.7},
      {"cause": "Damaged or dry axle shafts", "probability": 0.3}
    ],
    "Diagnostics": [
      "Turn steering fully in both directions while driving slowly and listen for noise",
      "Inspect CV boots for tears or leaking grease",
      "Check axle shaft play"
    ],
    "Fixes": [
      "Replace CV joints",
      "Replace entire axle shaft if necessary"
    ],
    "Temporary Solutions": [
      "Avoid sharp turns and monitor for worsening symptoms"
    ]
  },

  "Grinding Noise When Shifting": {
    "Actual Issue": "Grinding sound when shifting gears, typically due to internal wear or clutch issues.",
    "Possible Causes": [
      {"cause": "Worn synchro rings", "probability": 0.6},
      {"cause": "Clutch not fully disengaging", "probability": 0.4}
    ],
    "Diagnostics": [
      "Observe grinding during specific gear shifts",
      "Check clutch pedal free play and engagement",
      "Inspect transmission fluid condition"
    ],
    "Fixes": [
      "Repair or replace worn synchros",
      "Adjust or replace clutch"
    ],
    "Temporary Solutions": [
      "Double-clutch when shifting to reduce grinding"
    ]
  },

  "Whining Noise From Alternator": {
    "Actual Issue": "A whining or high-pitched noise near the engine that increases with RPM, often from the alternator or its components.",
    "Possible Causes": [
      {"cause": "Worn alternator bearings", "probability": 0.7},
      {"cause": "Loose or worn drive belt", "probability": 0.3}
    ],
    "Diagnostics": [
      "Listen near alternator for high-pitched whining",
      "Check alternator pulley for wobble or noise",
      "Inspect drive belt condition and tension"
    ],
    "Fixes": [
      "Replace alternator",
      "Replace or tighten drive belt"
    ],
    "Temporary Solutions": [
      "Avoid high electrical load until repaired"
    ]
  },

  "Squealing Belt Noises From Engine Bay": {
    "Actual Issue": "High-pitched squeal from the front of the engine, often due to slipping belts.",
    "Possible Causes": [
      {"cause": "Loose accessory belts", "probability": 0.6},
      {"cause": "Worn or glazed drive belts", "probability": 0.4}
    ],
    "Diagnostics": [
      "Inspect belts for cracking or glazing",
      "Check belt tension",
      "Listen for squeal during startup or acceleration"
    ],
    "Fixes": [
      "Adjust belt tension",
      "Replace worn accessory belts"
    ],
    "Temporary Solutions": [
      "Limit use of accessories until belts are serviced"
    ]
  },

  "Power Windows Not Working": {
    "Actual Issue": "Window does not move up or down when switch is pressed.",
    "Possible Causes": [
      {"cause": "Blown fuse", "probability": 0.3},
      {"cause": "Faulty window motor or regulator", "probability": 0.4},
      {"cause": "Broken window switch", "probability": 0.2},
      {"cause": "Wiring issue in door harness", "probability": 0.1}
    ],
    "Diagnostics": [
      "Test switch operation",
      "Check fuse related to power windows",
      "Listen for motor noise when pressing switch",
      "Check continuity in door wiring harness"
    ],
    "Fixes": [
      "Replace fuse",
      "Replace faulty motor or regulator",
      "Replace defective switch",
      "Repair or replace damaged wiring"
    ],
    "Temporary Solutions": [
      "Manually assist window movement if partially functional",
      "Avoid using windows until repaired"
    ]
  },

  "Central Locking Not Working": {
    "Actual Issue": "Doors don’t lock/unlock with key fob or central switch.",
    "Possible Causes": [
      {"cause": "Dead key fob battery", "probability": 0.4},
      {"cause": "Faulty door lock actuator", "probability": 0.3},
      {"cause": "Blown fuse or relay", "probability": 0.2},
      {"cause": "Wiring or control module fault", "probability": 0.1}
    ],
    "Diagnostics": [
      "Test key fob battery and response",
      "Check fuse box for blown central locking fuse",
      "Listen for actuator sound when pressing lock/unlock",
      "Scan for body control module errors"
    ],
    "Fixes": [
      "Replace key fob battery",
      "Replace failed actuators",
      "Replace fuse or relay",
      "Repair wiring or replace BCM"
    ],
    "Temporary Solutions": [
      "Lock doors manually",
      "Use mechanical key"
    ]
  },

  "Ignition Switch Issues": {
    "Actual Issue": "Turning the key doesn’t start the vehicle or accessories fail to power up.",
    "Possible Causes": [
      {"cause": "Worn ignition cylinder", "probability": 0.5},
      {"cause": "Bad ignition switch contacts", "probability": 0.3},
      {"cause": "Loose wiring or connector", "probability": 0.2}
    ],
    "Diagnostics": [
      "Turn key to accessory and observe behavior",
      "Check voltage to ignition wires",
      "Wiggle key and observe any change"
    ],
    "Fixes": [
      "Replace ignition switch assembly",
      "Repair electrical connectors"
    ],
    "Temporary Solutions": [
      "Try repositioning key slightly while turning"
    ]
  },

  "Blind Spot Monitor Not Working": {
    "Actual Issue": "Blind spot system fails to detect vehicles or gives false alerts.",
    "Possible Causes": [
      {"cause": "Dirty radar sensors", "probability": 0.5},
      {"cause": "Faulty radar module", "probability": 0.3},
      {"cause": "Wiring fault in mirror harness", "probability": 0.2}
    ],
    "Diagnostics": [
      "Check for warning lights on dash",
      "Clean rear corner sensors",
      "Scan system with OEM diagnostic tool"
    ],
    "Fixes": [
      "Clean sensors",
      "Replace faulty module or sensors",
      "Repair wiring"
    ],
    "Temporary Solutions": [
      "Use mirrors with extra caution until system is restored"
    ]
  },
  "Loud Exhaust Noise or Popping": {
    "Actual Issue": "Unusual loudness or popping sounds from the exhaust system.",
    "Severity Level": "Moderate — Indicates exhaust leaks or damaged components that can lead to emissions problems and further damage if not addressed.",
    "Possible Causes": [
      {"cause": "Exhaust leak", "probability": 0.45},
      {"cause": "Damaged muffler", "probability": 0.35},
      {"cause": "Faulty catalytic converter", "probability": 0.2}
    ],
    "Diagnostics": [
      "Inspect exhaust system for leaks or holes",
      "Check muffler and piping condition",
      "Scan for catalytic converter error codes"
    ],
    "Fixes": [
      "Seal or weld exhaust leaks",
      "Replace damaged muffler",
      "Install new catalytic converter if faulty"
    ],
    "Temporary Solutions": [
      "Avoid prolonged driving to prevent further damage or emissions issues"
    ]
  },

  "Battery Diagnosis": {
    "Severity Level": "Low — Battery issues generally cause starting or electrical accessory problems; urgent if battery fails to start vehicle.",
    "Functions": [
      "Supplies power to starter motor and ignition system",
      "Acts as chassis ground",
      "Stores alternator-generated energy"
    ],
    "Types of Batteries": [
      "Conventional lead-acid",
      "Low-maintenance",
      "Maintenance-free"
    ],
    "Maintenance Tips": [
      "Check and maintain electrolyte levels",
      "Clean terminals and apply petroleum jelly",
      "Disconnect battery if unused for long periods"
    ],
    "Troubleshooting Steps": [
      "Turn off all accessories",
      "Inspect for corrosion and tightness",
      "Use voltmeter to check voltage (should be ~12.6V)",
      "Charge if voltage is <12.4V"
    ]
  },

  "Clunking or Knocking When Going Over Bumps": {
    "Actual Issue": "Loud impact or knocking noise from suspension area when driving over uneven surfaces.",
    "Severity Level": "Moderate — Indicates worn suspension parts that affect ride comfort and handling; timely repair advised.",
    "Possible Causes": [
      {"cause": "Worn shock absorbers or struts", "probability": 0.45},
      {"cause": "Damaged suspension bushings", "probability": 0.35},
      {"cause": "Worn ball joints", "probability": 0.2}
    ],
    "Diagnostics": [
      "Visually inspect shocks and struts for leaks or damage",
      "Check suspension bushings for cracks or looseness",
      "Jack up vehicle and test ball joint play"
    ],
    "Fixes": [
      "Replace worn shock absorbers or struts",
      "Replace worn or damaged bushings",
      "Replace worn ball joints"
    ],
    "Temporary Solutions": [
      "Drive at slower speeds over bumps to reduce stress"
    ]
  },

  "Creaking or Squeaking When Turning Steering Wheel": {
    "Actual Issue": "Audible creaking or squeaking while turning, indicating friction or wear in the steering system.",
    "Severity Level": "Low to Moderate — Usually minor wear or lubrication issues, but may worsen to affect steering safety if ignored.",
    "Possible Causes": [
      {"cause": "Dry or worn power steering components", "probability": 0.6},
      {"cause": "Worn or unlubricated bushings", "probability": 0.4}
    ],
    "Diagnostics": [
      "Listen for noise source while turning wheel at low speed",
      "Inspect steering linkage and bushings",
      "Check for lubrication points"
    ],
    "Fixes": [
      "Lubricate dry components or bushings",
      "Replace worn power steering parts",
      "Replace deteriorated bushings"
    ],
    "Temporary Solutions": [
      "Avoid full lock turns until serviced"
    ]
  },

  "Grinding or Growling When Turning": {
    "Actual Issue": "Harsh grinding noise while turning the steering wheel, often due to power steering issues.",
    "Severity Level": "Moderate — Can cause power steering pump failure leading to loss of steering assist; repair soon for safety.",
    "Possible Causes": [
      {"cause": "Low power steering fluid", "probability": 0.6},
      {"cause": "Worn or failing power steering pump", "probability": 0.4}
    ],
    "Diagnostics": [
      "Check power steering fluid level and condition",
      "Listen to pump operation while turning",
      "Inspect for fluid leaks"
    ],
    "Fixes": [
      "Refill power steering fluid",
      "Repair leaks in the power steering system",
      "Replace worn power steering pump"
    ],
    "Temporary Solutions": [
      "Avoid tight turns and check fluid level frequently"
    ]
  },

  "Loose or Rattling Noise from Undercarriage": {
    "Actual Issue": "Rattling or clanking noise from underneath vehicle, indicating unsecured components.",
    "Severity Level": "Low to Moderate — Usually annoying but can worsen if parts come loose; inspect and secure to prevent damage.",
    "Possible Causes": [
      {"cause": "Loose heat shields", "probability": 0.4},
      {"cause": "Loose exhaust system parts", "probability": 0.35},
      {"cause": "Worn or loose suspension components", "probability": 0.25}
    ],
    "Diagnostics": [
      "Inspect undercarriage for any visibly loose parts",
      "Check heat shields and exhaust hangers",
      "Check for worn suspension bolts or mounts"
    ],
    "Fixes": [
      "Tighten or replace heat shields and exhaust brackets",
      "Replace loose suspension hardware",
      "Secure or repair affected undercarriage components"
    ],
    "Temporary Solutions": [
      "Avoid rough roads; check for further loosening regularly"
    ]
  },

  "Whining Noise When Accelerating": {
    "Actual Issue": "High-pitched whining sound during acceleration, usually from drivetrain components.",
    "Severity Level": "Moderate — May indicate transmission or differential issues; early service can prevent costly damage.",
    "Possible Causes": [
      {"cause": "Low transmission fluid", "probability": 0.6},
      {"cause": "Worn gears or bearings in transmission", "probability": 0.4}
    ],
    "Diagnostics": [
      "Check transmission fluid level and condition",
      "Listen for noise under acceleration",
      "Inspect for transmission leaks"
    ],
    "Fixes": [
      "Refill or replace transmission fluid",
      "Repair or replace worn transmission gears"
    ],
    "Temporary Solutions": [
      "Drive gently to reduce drivetrain load until repaired"
    ]
  },

  "Clunking Noise When Shifting Gears": {
    "Actual Issue": "Heavy clunk or thud sound when changing gears, indicating looseness in transmission mounts or clutch system.",
    "Severity Level": "Moderate to High — Can cause transmission or drivetrain damage; should be addressed promptly to avoid failure.",
    "Possible Causes": [
      {"cause": "Worn clutch components", "probability": 0.6},
      {"cause": "Damaged or degraded transmission mounts", "probability": 0.4}
    ],
    "Diagnostics": [
      "Inspect clutch operation and engagement",
      "Check transmission and engine mounts for movement",
      "Listen for clunk during gear shift"
    ],
    "Fixes": [
      "Replace worn clutch components",
      "Replace faulty transmission mounts"
    ],
    "Temporary Solutions": [
      "Shift gears gently and avoid aggressive driving"
    ]
  },

  "Transmission Slipping": {
    "Actual Issue": "Engine revs but car does not accelerate properly.",
    "Severity Level": "High — Indicates transmission failure or clutch wear; risks loss of power and unsafe driving, needs urgent repair.",
    "Possible Causes": [
      {"cause": "Low transmission fluid", "probability": 0.5},
      {"cause": "Worn clutch plates", "probability": 0.3},
      {"cause": "Faulty transmission solenoids", "probability": 0.2}
    ],
    "Diagnostics": [
      "Check transmission fluid level and smell",
      "Scan for transmission fault codes",
      "Observe RPM vs speed during acceleration"
    ],
    "Fixes": [
      "Top up or change transmission fluid",
      "Repair internal clutch packs",
      "Replace faulty solenoids"
    ],
    "Temporary Solutions": [
      "Avoid rapid acceleration or hill climbing",
      "Drive in lower gear if possible"
    ]
  },

  "Clicking or Popping During Turns": {
    "Actual Issue": "Repeated clicking or popping noise when turning, typically from CV joints or axles.",
    "Severity Level": "Moderate — Often indicates worn CV joints; failure can cause axle breakage and loss of drive; repair soon.",
    "Possible Causes": [
      {"cause": "Worn CV joints", "probability": 0.7},
      {"cause": "Damaged or dry axle shafts", "probability": 0.3}
    ],
    "Diagnostics": [
      "Turn steering fully in both directions while driving slowly and listen for noise",
      "Inspect CV boots for tears or leaking grease",
      "Check axle shaft play"
    ],
    "Fixes": [
      "Replace CV joints",
      "Replace entire axle shaft if necessary"
    ],
    "Temporary Solutions": [
      "Avoid sharp turns and monitor for worsening symptoms"
    ]
  },

  "Grinding Noise When Shifting": {
    "Actual Issue": "Grinding sound when shifting gears, typically due to internal wear or clutch issues.",
    "Severity Level": "Moderate to High — Indicates clutch or synchro failure; can lead to transmission damage if not repaired.",
    "Possible Causes": [
      {"cause": "Worn synchro rings", "probability": 0.6},
      {"cause": "Clutch not fully disengaging", "probability": 0.4}
    ],
    "Diagnostics": [
      "Observe grinding during specific gear shifts",
      "Check clutch pedal free play and engagement",
      "Inspect transmission fluid condition"
    ],
    "Fixes": [
      "Repair or replace worn synchros",
      "Adjust or replace clutch"
    ],
    "Temporary Solutions": [
      "Double-clutch when shifting to reduce grinding"
    ]
  },

  "Whining Noise From Alternator": {
    "Actual Issue": "A whining or high-pitched noise near the engine that increases with RPM, often from the alternator or its components.",
    "Severity Level": "Low to Moderate — Usually indicates worn bearings or belts; can lead to alternator failure if ignored.",
    "Possible Causes": [
      {"cause": "Worn alternator bearings", "probability": 0.7},
      {"cause": "Loose or worn drive belt", "probability": 0.3}
    ],
    "Diagnostics": [
      "Listen near alternator for high-pitched whining",
      "Check alternator pulley for wobble or noise",
      "Inspect drive belt condition and tension"
    ],
    "Fixes": [
      "Replace alternator",
      "Replace or tighten drive belt"
    ],
    "Temporary Solutions": [
      "Avoid high electrical load until repaired"
    ]
  },

  "Squealing Belt Noises From Engine Bay": {
    "Actual Issue": "High-pitched squeal from the front of the engine, often due to slipping belts.",
    "Severity Level": "Low to Moderate — Usually caused by loose or worn belts; can cause accessory failure if not addressed.",
    "Possible Causes": [
      {"cause": "Loose accessory belts", "probability": 0.6},
      {"cause": "Worn or glazed drive belts", "probability": 0.4}
    ],
    "Diagnostics": [
      "Inspect belts for cracking or glazing",
      "Check belt tension",
      "Listen for squeal during startup or acceleration"
    ],
    "Fixes": [
      "Adjust belt tension",
      "Replace worn accessory belts"
    ],
    "Temporary Solutions": [
      "Limit use of accessories until belts are serviced"
    ]
  },

  "Power Windows Not Working": {
    "Actual Issue": "Window does not move up or down when switch is pressed.",
    "Severity Level": "Low — Convenience issue only; no impact on safety but can affect vehicle comfort.",
    "Possible Causes": [
      {"cause": "Blown fuse", "probability": 0.3},
      {"cause": "Faulty window motor or regulator", "probability": 0.4},
      {"cause": "Broken window switch", "probability": 0.2},
      {"cause": "Wiring issue in door harness", "probability": 0.1}
    ],
    "Diagnostics": [
      "Test switch operation",
      "Check fuse related to power windows",
      "Listen for motor noise when pressing switch",
      "Check continuity in door wiring harness"
    ],
    "Fixes": [
      "Replace fuse",
      "Replace faulty motor or regulator",
      "Replace defective switch",
      "Repair or replace damaged wiring"
    ],
    "Temporary Solutions": [
      "Manually assist window movement if partially functional",
      "Avoid using windows until repaired"
    ]
  },

  "Central Locking Not Working": {
    "Actual Issue": "Doors don’t lock/unlock with key fob or central switch.",
    "Severity Level": "Low — Convenience and security issue; manual locking possible.",
    "Possible Causes": [
      {"cause": "Dead key fob battery", "probability": 0.4},
      {"cause": "Faulty door lock actuator", "probability": 0.3},
      {"cause": "Blown fuse or relay", "probability": 0.2},
      {"cause": "Wiring or control module fault", "probability": 0.1}
    ],
    "Diagnostics": [
      "Test key fob battery and response",
      "Check fuse box for blown central locking fuse",
      "Listen for actuator sound when pressing lock/unlock",
      "Scan for body control module errors"
    ],
    "Fixes": [
      "Replace key fob battery",
      "Replace failed actuators",
      "Replace fuse or relay",
      "Repair wiring or replace BCM"
    ],
    "Temporary Solutions": [
      "Lock doors manually",
      "Use mechanical key"
    ]
  },

  "Ignition Switch Issues": {
    "Actual Issue": "Turning the key doesn’t start the vehicle or accessories fail to power up.",
    "Severity Level": "Moderate — Can prevent vehicle start and cause electrical issues; repair needed for reliable operation.",
    "Possible Causes": [
      {"cause": "Worn ignition cylinder", "probability": 0.5},
      {"cause": "Bad ignition switch contacts", "probability": 0.3},
      {"cause": "Loose wiring or connector", "probability": 0.2}
    ],
    "Diagnostics": [
      "Turn key to accessory and observe behavior",
      "Check voltage to ignition wires",
      "Wiggle key and observe any change"
    ],
    "Fixes": [
      "Replace ignition switch assembly",
      "Repair electrical connectors"
    ],
    "Temporary Solutions": [
      "Try repositioning key slightly while turning"
    ]
  },

  "Blind Spot Monitor Not Working": {
    "Actual Issue": "Blind spot system fails to detect vehicles or gives false alerts.",
    "Severity Level": "Low to Moderate — Safety feature compromised; manual vigilance required until repaired.",
    "Possible Causes": [
      {"cause": "Dirty radar sensors", "probability": 0.5},
      {"cause": "Faulty radar module", "probability": 0.3},
      {"cause": "Wiring fault in mirror harness", "probability": 0.2}
    ],
    "Diagnostics": [
      "Check for warning lights on dash",
      "Clean rear corner sensors",
      "Scan system with OEM diagnostic tool"
    ],
    "Fixes": [
      "Clean sensors",
      "Replace faulty module or sensors",
      "Repair wiring"
    ],
    "Temporary Solutions": [
      "Use mirrors with extra caution until system is restored"
    ]
  },

  "Rear View Camera Not Working": {
    "Actual Issue": "Reverse camera fails to activate or shows black/blue screen.",
    "Severity Level": "Low — Convenience and safety feature affected; manual reversing required.",
    "Possible Causes": [
      {"cause": "Faulty camera module", "probability": 0.5},
      {"cause": "Broken wiring", "probability": 0.3},
      {"cause": "Blown fuse for camera circuit", "probability": 0.2}
    ],
    "Diagnostics": [
      "Engage reverse and observe screen",
      "Inspect camera lens and wiring",
      "Check camera-related fuse"
    ],
    "Fixes": [
      "Replace rear view camera",
      "Repair or replace wiring harness",
      "Replace fuse"
    ],
    "Temporary Solutions": [
      "Use mirrors and turn head while reversing"
    ]
  },

  "Keyless Entry Not Working": {
    "Actual Issue": "Car does not unlock when touching door handle with fob nearby.",
    "Severity Level": "Low — Convenience issue only; manual unlocking required.",
    "Possible Causes": [
      {"cause": "Weak key fob battery", "probability": 0.5},
      {"cause": "Faulty proximity sensor", "probability": 0.3},
      {"cause": "Receiver module malfunction", "probability": 0.2}
    ],
    "Diagnostics": [
      "Replace fob battery and test",
      "Test second fob if available",
      "Check for error codes related to keyless system"
    ],
    "Fixes": [
      "Replace fob battery",
      "Replace proximity sensor",
      "Repair or replace antenna/receiver module"
    ],
    "Temporary Solutions": [
      "Use physical key blade to unlock door"
    ]
  },

  "Sunroof Not Closing or Stuck": {
    "Actual Issue": "Sunroof gets stuck or does not operate smoothly.",
    "Severity Level": "Low — Convenience and weather sealing affected; no safety hazard.",
    "Possible Causes": [
      {"cause": "Motor failure", "probability": 0.5},
      {"cause": "Debris in sunroof tracks", "probability": 0.3},
      {"cause": "Faulty switch or relay", "probability": 0.2}
    ],
    "Diagnostics": [
      "Listen for motor noise when pressing switch",
      "Check sunroof tracks for obstruction",
      "Test sunroof relay"
    ],
    "Fixes": [
      "Clean and lubricate tracks",
      "Replace sunroof motor",
      "Replace faulty switch or relay"
    ],
    "Temporary Solutions": [
      "Gently push glass while activating switch"
    ]
  },

  "Electric Parking Brake Won’t Release": {
    "Actual Issue": "EPB stays engaged even when attempting to release it.",
    "Severity Level": "High — Can prevent vehicle movement and cause brake overheating; requires prompt repair.",
    "Possible Causes": [
      {"cause": "Faulty brake actuator", "probability": 0.5},
      {"cause": "Low battery voltage", "probability": 0.3},
      {"cause": "Software or sensor fault", "probability": 0.2}
    ],
    "Diagnostics": [
      "Check dashboard for EPB warning",
      "Check voltage at actuator",
      "Scan with diagnostic tool for EPB fault codes"
    ],
    "Fixes": [
      "Replace actuator",
      "Charge or replace battery",
      "Reset system or update software"
    ],
    "Temporary Solutions": [
      "Rock vehicle gently to relieve brake tension"
    ]
  },

  "Clicking Sound When Turning Key": {
    "Actual Issue": "Clicking noise when starting the car, usually indicating insufficient power or a faulty starting system.",
    "Severity Level": "High — Vehicle may not start; urgent attention needed.",
    "Possible Causes": [
      {"cause": "Weak or dead battery", "probability": 0.7},
      {"cause": "Faulty starter motor or solenoid", "probability": 0.3}
    ],
    "Diagnostics": [
      "Check battery voltage and connections",
      "Test starter draw and relay function",
      "Observe if dash lights dim when turning the key"
    ],
    "Fixes": [
      "Recharge or replace battery",
      "Repair or replace starter motor"
    ],
    "Temporary Solutions": [
      "Try jump-starting the car as a temporary fix"
    ]
  },

  "Buzzing or Humming From Speakers": {
    "Actual Issue": "Continuous or intermittent noise from the speakers when the engine or accessories are on.",
    "Severity Level": "Low — Audio annoyance; no safety impact.",
    "Possible Causes": [
      {"cause": "Ground loop in audio system", "probability": 0.6},
      {"cause": "Electrical interference from other components", "probability": 0.4}
    ],
    "Diagnostics": [
      "Listen for hum that changes with engine speed",
      "Check audio wiring and ground points",
      "Test with engine off to isolate interference"
    ],
    "Fixes": [
      "Use ground loop isolators in audio system",
      "Improve wiring shielding and reroute signal cables"
    ],
    "Temporary Solutions": [
      "Lower volume or disconnect accessory inputs temporarily"
    ]
  },

  "Rattling or Buzzing Under Hood at Idle": {
    "Actual Issue": "A metallic rattling or buzzing noise from the engine bay while idling, often caused by loose components.",
    "Severity Level": "Low to Moderate — May cause further damage if loose parts fall off; inspect soon.",
    "Possible Causes": [
      {"cause": "Loose heat shields", "probability": 0.6},
      {"cause": "Loose pulleys or brackets", "probability": 0.4}
    ],
    "Diagnostics": [
      "Listen for metallic noise near engine at idle",
      "Tap suspected components lightly to replicate sound",
      "Inspect pulleys, heat shields, and brackets for looseness"
    ],
    "Fixes": [
      "Tighten or replace loose components",
      "Replace missing mounting hardware"
    ],
    "Temporary Solutions": [
      "Secure parts with heat-resistant zip ties until fixed"
    ]
  },

  "Buzzing or Humming at High Speed": {
    "Actual Issue": "A low-frequency hum or buzz that increases with speed, often due to rotating parts.",
    "Severity Level": "Moderate — Could indicate worn wheel bearings, a safety concern if left unchecked.",
    "Possible Causes": [
      {"cause": "Worn wheel bearings", "probability": 0.7},
      {"cause": "Imbalanced tires", "probability": 0.3}
    ],
    "Diagnostics": [
      "Listen for humming that gets louder with speed",
      "Check for play in wheels or uneven tire wear",
      "Rotate tires to isolate noise"
    ],
    "Fixes": [
      "Replace worn wheel bearings",
      "Balance and rotate tires"
    ],
    "Temporary Solutions": [
      "Drive at lower speeds to minimize vibration"
    ]
  },

  "Squeaking or Chirping From Doors or Windows": {
    "Actual Issue": "High-pitched squeaks or chirps from vehicle doors or windows when moving or during wind exposure.",
    "Severity Level": "Low — Purely a comfort/noise annoyance issue.",
    "Possible Causes": [
      {"cause": "Dry or worn rubber door/window seals", "probability": 1.0}
    ],
    "Diagnostics": [
      "Open and close doors to identify sound",
      "Inspect seals for dryness, cracks, or damage",
      "Check if sound is affected by temperature or wind"
    ],
    "Fixes": [
      "Lubricate seals with silicone spray",
      "Replace damaged or worn weatherstripping"
    ],
    "Temporary Solutions": [
      "Apply petroleum jelly or rubber conditioner to quiet squeaks"
    ]
  },

  "Interior & Comfort": {
    "Seat Adjustment Not Working": {
      "Actual Issue": "Power seat doesn’t move in one or more directions.",
      "Severity Level": "Low — Convenience issue; no impact on vehicle operation.",
      "Possible Causes": [
        {"cause": "Faulty seat motor", "probability": 0.5},
        {"cause": "Blown fuse", "probability": 0.3},
        {"cause": "Broken switch", "probability": 0.2}
      ],
      "Diagnostics": [
        "Listen for motor operation",
        "Test seat switches with multimeter",
        "Check related fuse"
      ],
      "Fixes": [
        "Replace seat motor",
        "Replace seat adjustment switch",
        "Repair wiring or connectors"
      ],
      "Temporary Solutions": [
        "Manually position seat if possible",
        "Avoid changing seat settings until repaired"
      ]
    }
  },

  "High Oil Consumption": {
    "Actual Issue": "Engine is consuming more oil than usual, indicating leaks or internal wear.",
    "Severity Level": "High — Can lead to engine damage or failure if not addressed.",
    "Possible Causes": [
      {"cause": "External leakage (gaskets, seals)", "probability": 0.6},
      {"cause": "Internal leakage (worn piston rings)", "probability": 0.4}
    ],
    "Symptoms": [
      "Oil puddles under vehicle",
      "Blue smoke from exhaust"
    ],
    "Diagnostics": [
      "Inspect engine seals and gaskets for leaks",
      "Perform compression test to check piston rings"
    ],
    "Fixes": [
      "Replace worn gaskets or seals",
      "Repair or rebuild engine components"
    ]
  },

  "Lubrication and Oil Leaks": {
    "Oil Leak Fixing": {
      "Actual Issue": "Process of identifying and repairing engine oil leaks.",
      "Severity Level": "Moderate — Leaks can cause oil loss and environmental damage; repair advised.",
      "Possible Causes": [
        {"cause": "Worn gaskets or seals", "probability": 0.6},
        {"cause": "Loose or over-torqued bolts", "probability": 0.2},
        {"cause": "Damaged oil pan or drain plug", "probability": 0.2}
      ],
      "Symptoms": [
        "Visible oil spots under the car",
        "Burning oil smell",
        "Low oil level warning"
      ],
      "Diagnostics": [
        "Use degreaser and paper towels to find leak sources",
        "Torque bolts to manufacturer specs",
        "Check hoses and lines for damage"
      ],
      "Fixes": [
        "Replace worn gaskets or seals",
        "Apply sealants or replace parts as needed"
      ]
    },

    "Changing Engine Oil": {
      "Actual Issue": "Guidelines for changing engine oil to maintain engine health.",
      "Severity Level": "Low — Routine maintenance task to prevent engine damage.",
      "Possible Causes": [
        {"cause": "Extended oil change interval", "probability": 0.5},
        {"cause": "Use of incorrect oil grade", "probability": 0.3},
        {"cause": "Neglecting oil checks", "probability": 0.2}
      ],
      "Symptoms": [
        "Engine running rough",
        "Oil warning light on",
        "Unusual engine noises"
      ],
      "Diagnostics": [
        "Check oil monthly, especially for high-mileage cars",
        "Use proper oil grade",
        "Monitor oil pressure gauge"
      ],
      "Fixes": [
        "Perform regular oil changes",
        "Check for leaks after oil change"
      ]
    }
  },

  "Spark Plug Issues": {
    "Common Conditions": {
      "Actual Issue": "Various spark plug conditions indicate engine and fuel system issues.",
      "Severity Level": "Moderate — Affects engine performance and emissions; timely maintenance needed.",
      "Possible Causes": [
        {"cause": "Wet black deposits: Excessive oil in piston chamber; requires rebuild", "probability": 0.35},
        {"cause": "Dry black deposits: Rich fuel, dirty air filter, excessive idling", "probability": 0.25},
        {"cause": "Worn electrode: Plug is old or damaged", "probability": 0.15},
        {"cause": "Melted electrode: Check fuel type, timing, valves", "probability": 0.15},
        {"cause": "White tips with black spots: Overheating or wrong plug", "probability": 0.10}
      ],
      "Diagnostics": [
        "Visual inspection for carbon or ash deposits",
        "Check for oil or additive buildup",
        "Adjust gap as per manual"
      ],
      "Fixes": [
        "Replace damaged or worn plugs"
      ]
    },
    "Warnings": {
      "Actual Issue": "Important precautions for spark plug handling and installation.",
      "Fixes": [
        "Install spark plugs when engine is cool",
        "Avoid over-tightening or under-tightening plugs"
      ]
    },
    "Bad Spark Plug Wires Symptoms": {
      "Actual Issue": "Symptoms indicating faulty spark plug wires.",
      "Severity Level": "Moderate — Leads to misfires and poor engine operation.",
      "Symptoms": [
        "Rough engine idle",
        "Engine misfiring or surging",
        "Hesitation during acceleration",
        "Reduced engine power"
      ]
    }
  },

  "Air Conditioning System": {
    "No Cooling": {
      "Actual Issue": "A/C does not cool the cabin as expected.",
      "Severity Level": "Low to Moderate — Comfort affected; no safety risk.",
      "Possible Causes": [
        {"cause": "Low refrigerant", "probability": 0.7},
        {"cause": "Compressor won't engage due to low pressure switch", "probability": 0.3}
      ],
      "Diagnostics": [
        "Use A/C gauges to check refrigerant pressure",
        "Inspect system for leaks before recharging"
      ]
    },
    "Refrigerant Leak": {
      "Actual Issue": "Loss of refrigerant due to leaks in the system.",
      "Severity Level": "Moderate — Causes cooling loss and environmental harm.",
      "Diagnostics": [
        "Detect leaks with dye, electronic leak detector, or soapy water",
        "Older cars tend to leak more frequently"
      ],
      "Fixes": [
        "Replace O-rings or seals if leaking"
      ]
    },
    "Poor Cooling": {
      "Actual Issue": "A/C cools but not to expected levels.",
      "Severity Level": "Low to Moderate — Comfort issue.",
      "Diagnostics": [
        "Check pressure gauge readings (e.g., 56 psi on an 80°F day)",
        "Low pressure indicates low refrigerant",
        "Refer to OEM specs for normal values"
      ]
    },
    "Intermittent Cooling": {
      "Actual Issue": "A/C cools inconsistently or freezes up.",
      "Severity Level": "Moderate — System inefficiency and potential damage if not fixed.",
      "Possible Causes": [
        {"cause": "Air or moisture trapped in system causing freezing", "probability": 1.0}
      ],
      "Fixes": [
        "Evacuate system using vacuum pump for 30–45 minutes"
      ]
    }
  },

  "Timing Belt Troubleshooting": {
    "Actual Issue": "Issues related to timing belt wear, damage, and failure.",
    "Severity Level": "High — Timing belt failure can cause severe engine damage.",
    "Possible Causes": [
      {"cause": "Worn or damaged timing belt", "probability": 0.6},
      {"cause": "Oil soaking causing belt degradation", "probability": 0.25},
      {"cause": "Improper tension causing slippage", "probability": 0.15}
    ],
    "Diagnostics": [
      "Listen for squealing or screeching noises from engine",
      "Inspect timing belt for cracks or oil contamination",
      "Check for excess smoke from exhaust indicating timing issues"
    ],
    "Fixes": [
      "Replace timing belt every 60,000–90,000 miles",
      "Replace tensioner and other components along with belt",
      "Ensure proper installation and tensioning"
    ]
  },

  "Braking System": {
    "Brake Pedal Goes Too Far": {
      "Actual Issue": "Brake pedal travels too far when pressed.",
      "Severity Level": "High — Reduced braking effectiveness, urgent repair needed.",
      "Possible Causes": [
        {"cause": "Low brake fluid level", "probability": 0.4},
        {"cause": "Contaminated brake fluid", "probability": 0.25},
        {"cause": "Worn brake pads", "probability": 0.2},
        {"cause": "Faulty brake booster", "probability": 0.15}
      ],
      "Diagnostics": [
        "Check brake fluid reservoir level",
        "Inspect brake fluid condition and bleed if contaminated",
        "Check brake pad thickness",
        "Test brake booster operation"
      ],
      "Fixes": [
        "Top up or replace brake fluid",
        "Replace worn brake pads",
        "Repair or replace brake booster"
      ]
    },
    "Brake Pedal Too Firm": {
      "Actual Issue": "Brake pedal feels very stiff when pressed.",
      "Severity Level": "High — Affects braking performance, potentially unsafe.",
      "Possible Causes": [
        {"cause": "Vacuum leaks affecting brake booster", "probability": 0.6},
        {"cause": "Brake line obstruction", "probability": 0.4}
      ],
      "Diagnostics": [
        "Check vacuum lines for leaks",
        "Inspect brake lines for blockages or damage"
      ],
      "Fixes": [
        "Repair vacuum leaks",
        "Clear or replace obstructed brake lines"
      ]
    },
    "Brake Pedal Goes To Floor": {
      "Actual Issue": "Brake pedal presses down to the floor with little resistance.",
      "Severity Level": "High — Critical brake failure risk; immediate repair required.",
      "Possible Causes": [
        {"cause": "Low brake fluid", "probability": 0.5},
        {"cause": "Air in brake lines", "probability": 0.3},
        {"cause": "Bad master cylinder", "probability": 0.2}
      ],
      "Diagnostics": [
        "Check brake fluid level",
        "Bleed brake lines to remove air",
        "Inspect master cylinder for leaks or failure"
      ],
      "Fixes": [
        "Refill brake fluid",
        "Bleed brake system",
        "Replace master cylinder if faulty"
      ]
    },
    "Weak or Spongy Brakes": {
      "Actual Issue": "Brake pedal feels soft or spongy when pressed.",
      "Severity Level": "High — Impaired braking performance; safety risk.",
      "Possible Causes": [
        {"cause": "Low or contaminated brake fluid", "probability": 0.6},
        {"cause": "Worn brake pads", "probability": 0.4}
      ],
      "Diagnostics": [
        "Check fluid level and condition",
        "Inspect brake pads for wear"
      ],
      "Fixes": [
        "Replace or flush brake fluid",
        "Replace worn brake pads"
      ]
    },
    "Brakes Grabbing or Pulling": {
      "Actual Issue": "Vehicle pulls to one side or brakes grab unexpectedly.",
      "Severity Level": "Moderate to High — Can affect vehicle control.",
      "Possible Causes": [
        {"cause": "Worn brake pads", "probability": 0.5},
        {"cause": "Warped or damaged brake discs", "probability": 0.5}
      ],
      "Diagnostics": [
        "Inspect brake pads for uneven wear",
        "Check brake discs for warping or damage"
      ],
      "Fixes": [
        "Replace brake pads",
        "Resurface or replace brake discs"
      ]
    },
    "Pedal Vibration": {
      "Actual Issue": "Brake pedal vibrates or pulses when braking.",
      "Severity Level": "Moderate — Indicates brake system issues; affects comfort and safety.",
      "Possible Causes": [
        {"cause": "Worn or warped brake pads/discs", "probability": 0.5},
        {"cause": "Misalignment of brake components", "probability": 0.3},
        {"cause": "Worn suspension parts affecting braking", "probability": 0.2}
      ],
      "Diagnostics": [
        "Check brake components for wear or damage",
        "Inspect suspension parts",
        "Test for proper brake alignment"
      ],
      "Fixes": [
        "Replace brake pads and/or discs",
        "Realign brake system",
        "Repair or replace worn suspension components"
      ]
    }
  },

  "Suspension and Shock Absorbers": {
    "Common Problems": {
      "Suspension Topping or Bottoming Out": {
        "Actual Issue": "Suspension compresses fully or bottoms out causing harsh ride.",
        "Severity Level": "Moderate — Ride comfort affected; potential damage if ignored.",
        "Possible Causes": [
          {"cause": "Defective spring or shock absorber", "probability": 0.5},
          {"cause": "Missing rubber bumper", "probability": 0.3},
          {"cause": "Vehicle heavily loaded", "probability": 0.2}
        ],
        "Diagnostics": [
          "Visual inspection of springs and shocks",
          "Check for missing or damaged bump stops",
          "Assess vehicle load"
        ],
        "Fixes": [
          "Replace defective springs or shocks",
          "Install or replace missing bumpers",
          "Reduce vehicle load"
        ]
      }
    },
      "Spring Breakage": {
    "Actual Issue": "Broken or cracked springs causing suspension issues.",
    "Severity Level": "High — Critical suspension failure can severely affect handling and safety, requiring prompt repair.",
    "Possible Causes": [
      {"cause": "Overloading vehicle", "probability": 0.5},
      {"cause": "Loose leaf spring centre", "probability": 0.3},
      {"cause": "Tight spring shackle", "probability": 0.2}
    ],
    "Diagnostics": [
      "Inspect springs for cracks or breaks",
      "Check tightness of leaf spring center",
      "Inspect shackles for tightness or damage"
    ],
    "Fixes": [
      "Avoid overloading vehicle",
      "Tighten or replace leaf spring centre",
      "Adjust or replace spring shackles"
    ]
  },
  "Improper Suspension Height": {
    "Actual Issue": "Suspension height is lower or higher than normal.",
    "Severity Level": "Moderate — Can affect ride quality and handling; potential precursor to further damage.",
    "Possible Causes": [
      {"cause": "Broken or weak spring", "probability": 0.7},
      {"cause": "Defective shock absorber", "probability": 0.3}
    ],
    "Diagnostics": [
      "Measure suspension height",
      "Inspect springs and shocks for damage"
    ],
    "Fixes": [
      "Replace broken or weak springs",
      "Replace defective shock absorbers"
    ]
  },
  "Suspension & Steering": {
    "Vehicle Pulls to One Side": {
      "Actual Issue": "Vehicle drifts left or right even on straight roads.",
      "Severity Level": "Moderate — Affects control and safety; should be fixed promptly.",
      "Possible Causes": [
        {"cause": "Misaligned wheels", "probability": 0.4},
        {"cause": "Uneven tire pressure", "probability": 0.3},
        {"cause": "Sticking brake caliper", "probability": 0.2},
        {"cause": "Worn steering/suspension components", "probability": 0.1}
      ],
      "Diagnostics": [
        "Check tire pressure on all wheels",
        "Inspect tire wear patterns",
        "Test brake drag on individual wheels",
        "Measure wheel alignment angles"
      ],
      "Fixes": [
        "Perform wheel alignment",
        "Correct tire pressure",
        "Replace faulty brake caliper",
        "Replace worn bushings or tie rods"
      ],
      "Temporary Solutions": [
        "Keep hands on wheel and compensate while driving",
        "Avoid aggressive cornering or long trips"
      ]
    }
  },
  "Overheating While Driving": {
    "Actual Issue": "Engine temperature rises excessively during operation, risking damage.",
    "Severity Level": "High — Risk of severe engine damage or failure; requires immediate attention.",
    "Possible Causes": [
      {"cause": "Stuck thermostat", "probability": 0.3},
      {"cause": "Radiator blockage", "probability": 0.25},
      {"cause": "Failed cooling fan", "probability": 0.2},
      {"cause": "Low coolant level", "probability": 0.25}
    ],
    "Diagnostics": [
      "Check coolant level",
      "Inspect radiator for clogs",
      "Verify fan operation",
      "Monitor temperature gauge"
    ],
    "Fixes": [
      "Replace thermostat",
      "Flush radiator",
      "Repair/replace cooling fan",
      "Top up coolant"
    ],
    "Temporary Solutions": [
      "Turn heater on full blast to reduce engine heat",
      "Pull over and let engine cool"
    ]
  },
  "Coolant Smell Inside Cabin": {
    "Actual Issue": "Sweet smell and mist in cabin indicate heater core leak.",
    "Severity Level": "Moderate — Affects comfort and can cause coolant loss; requires timely repair.",
    "Possible Causes": [
      {"cause": "Leaking heater core", "probability": 1.0}
    ],
    "Diagnostics": [
      "Check for wet passenger carpet",
      "Smell for coolant odor inside cabin",
      "Check coolant level drop"
    ],
    "Fixes": [
      "Replace heater core"
    ],
    "Temporary Solutions": [
      "Bypass heater core loop"
    ]
  },
  "Vibration at Highway Speeds": {
    "Actual Issue": "Car vibrates noticeably at 60+ mph due to imbalance or wear.",
    "Severity Level": "Moderate — Affects ride comfort and may indicate wear needing prompt repair.",
    "Possible Causes": [
      {"cause": "Imbalanced tires", "probability": 0.5},
      {"cause": "Bent rim", "probability": 0.2},
      {"cause": "Worn wheel bearings", "probability": 0.3}
    ],
    "Diagnostics": [
      "Inspect tire wear",
      "Check balance weights",
      "Jack up and test wheel play"
    ],
    "Fixes": [
      "Balance tires",
      "Replace bent rim",
      "Replace wheel bearings"
    ],
    "Temporary Solutions": [
      "Drive below vibration speed",
      "Avoid sudden maneuvers"
    ]
  },
  "Delayed Gear Engagement": {
    "Actual Issue": "Automatic transmission delays when shifting into gear.",
    "Severity Level": "Moderate — Can worsen over time, potentially causing transmission damage.",
    "Possible Causes": [
      {"cause": "Low or old transmission fluid", "probability": 0.7},
      {"cause": "Internal clutch wear", "probability": 0.3}
    ],
    "Diagnostics": [
      "Check fluid level and color",
      "Look for burnt smell in fluid",
      "Monitor delay duration"
    ],
    "Fixes": [
      "Flush and replace transmission fluid",
      "Service or rebuild transmission"
    ],
    "Temporary Solutions": [
      "Warm up car before shifting",
      "Avoid hard acceleration"
    ]
  },
  "Car Won’t Shift Out of Park": {
    "Actual Issue": "Gear selector stuck in Park even with brake applied.",
    "Severity Level": "High — Immobilizes vehicle; requires prompt fix.",
    "Possible Causes": [
      {"cause": "Faulty brake light switch", "probability": 0.5},
      {"cause": "Shift interlock solenoid failure", "probability": 0.5}
    ],
    "Diagnostics": [
      "Check if brake lights illuminate",
      "Listen for click when pressing brake",
      "Inspect shift interlock mechanism"
    ],
    "Fixes": [
      "Replace brake light switch",
      "Replace interlock solenoid"
    ],
    "Temporary Solutions": [
      "Use shift lock override (check owner's manual)"
    ]
  },
  "Lights Flicker While Driving": {
    "Actual Issue": "Headlights or dashboard lights flicker intermittently.",
    "Severity Level": "High — Electrical instability can cause safety hazards; urgent attention advised.",
    "Possible Causes": [
      {"cause": "Failing alternator", "probability": 0.6},
      {"cause": "Loose battery terminals", "probability": 0.4}
    ],
    "Diagnostics": [
      "Measure alternator output (13.5–14.8V)",
      "Inspect and tighten battery connections"
    ],
    "Fixes": [
      "Replace alternator",
      "Clean and tighten terminals"
    ],
    "Temporary Solutions": [
      "Turn off non-essential accessories"
    ]
  },
  "Rotten Egg Smell": {
    "Actual Issue": "Sulfur-like smell from exhaust system, often due to emissions issues.",
    "Severity Level": "Low to Moderate — Emissions concern; potential catalytic converter damage.",
    "Possible Causes": [
      {"cause": "Failing catalytic converter", "probability": 0.7},
      {"cause": "Over-rich fuel mixture", "probability": 0.3}
    ],
    "Diagnostics": [
      "Scan for engine codes (e.g., P0420)",
      "Smell exhaust after warm-up",
      "Check fuel trims"
    ],
    "Fixes": [
      "Replace catalytic converter",
      "Fix fuel mixture issue (e.g., O2 sensor)"
    ],
    "Temporary Solutions": [
      "Drive gently to avoid overheating converter"
    ]
  },
  "Key Stuck in Ignition": {
    "Actual Issue": "Ignition key cannot be removed even when in park.",
    "Severity Level": "Moderate — Immobilizes vehicle; can often be temporarily resolved.",
    "Possible Causes": [
      {"cause": "Steering wheel lock engaged", "probability": 0.6},
      {"cause": "Shift interlock issue", "probability": 0.4}
    ],
    "Diagnostics": [
      "Wiggle steering wheel while turning key",
      "Check if shifter is fully in park",
      "Inspect ignition cylinder"
    ],
    "Fixes": [
      "Replace ignition switch or cylinder",
      "Service shift interlock mechanism"
    ],
    "Temporary Solutions": [
      "Gently move wheel and shifter to free key"
    ]
  },

 "Noise and Vibration": {
    "Actual Issue": "Noise or vibration from suspension or chassis components.",
    "Severity Level": "Medium — Can affect ride comfort and may indicate early wear; requires inspection to prevent escalation.",
    "Possible Causes": [
      {"cause": "Loose or unlubricated parts", "probability": 0.7},
      {"cause": "Tight shock absorber bushings", "probability": 0.3}
    ],
    "Actions": [
      "Lubricate and repair"
    ]
  },

  "Engine Overheating": {
    "Actual Issue": "Engine temperature rises beyond normal limits, causing overheating.",
    "Severity Level": "High — Overheating can cause serious engine damage and breakdown; immediate attention required.",
    "Symptoms": [
      "High temperature gauge reading",
      "Steam or smoke from engine bay",
      "Coolant warning light on",
      "Loss of power or engine knocking"
    ],
    "Possible Causes": [
      {"cause": "Coolant leak (radiator, hoses, water pump)", "probability": 0.3},
      {"cause": "Faulty thermostat stuck closed", "probability": 0.25},
      {"cause": "Radiator blockage or failure", "probability": 0.15},
      {"cause": "Malfunctioning water pump", "probability": 0.15},
      {"cause": "Low coolant level", "probability": 0.1},
      {"cause": "Head gasket failure causing coolant leakage", "probability": 0.05}
    ],
    "Diagnostics": [
      "Check coolant level and condition",
      "Inspect radiator and hoses for leaks",
      "Pressure test cooling system",
      "Check thermostat operation",
      "Perform cylinder leak-down test for head gasket",
      "Scan engine codes for related faults"
    ],
    "Fixes": [
      "Repair leaks and refill coolant",
      "Replace faulty thermostat",
      "Flush or replace radiator",
      "Replace water pump",
      "Replace head gasket if damaged"
    ],
    "Temporary Solutions": [
      "Stop driving immediately to avoid engine damage",
      "Add coolant if low, but only as emergency",
      "Allow engine to cool before restarting"
    ]
  },

  "Engine Block Crack or Damage": {
    "Actual Issue": "Physical cracks or damage to the engine block causing leaks or loss of compression.",
    "Severity Level": "Critical — Serious engine damage requiring immediate repair or replacement to avoid catastrophic failure.",
    "Symptoms": [
      "Coolant or oil leaks under the vehicle",
      "White smoke from exhaust (coolant burning)",
      "Overheating issues",
      "Loss of engine power or misfires",
      "Milky oil appearance (coolant contamination)"
    ],
    "Possible Causes": [
      {"cause": "Severe engine overheating", "probability": 0.5},
      {"cause": "Freezing of coolant causing block cracking", "probability": 0.2},
      {"cause": "Physical impact or accident damage", "probability": 0.25},
      {"cause": "Manufacturing defects (rare)", "probability": 0.05}
    ],
    "Diagnostics": [
      "Visual inspection for cracks or leaks",
      "Pressure test cooling system",
      "Compression test or leak-down test",
      "Oil analysis for coolant contamination"
    ],
    "Fixes": [
      "Engine block repair with welding (if possible)",
      "Replace engine block (often required)",
      "Replace damaged gaskets and seals"
    ],
    "Temporary Solutions": [
      "Use of engine block sealants (limited and temporary)",
      "Avoid heavy engine load or overheating"
    ]
  },

  "Engine Block Warping": {
    "Actual Issue": "Engine block surface warps due to overheating or improper torqueing.",
    "Severity Level": "High — Causes gasket failure and compression loss, affecting engine reliability; timely repair needed.",
    "Symptoms": [
      "Coolant leaks at head gasket",
      "Loss of compression",
      "Overheating issues",
      "Poor engine performance"
    ],
    "Possible Causes": [
      {"cause": "Overheating due to coolant failure", "probability": 0.6},
      {"cause": "Incorrect cylinder head torque", "probability": 0.25},
      {"cause": "Rapid engine temperature changes", "probability": 0.15}
    ],
    "Diagnostics": [
      "Check head gasket leaks",
      "Perform surface flatness check with straight edge and feeler gauge",
      "Compression or leak-down test"
    ],
    "Fixes": [
      "Machining (resurfacing) of engine block deck",
      "Replace head gasket",
      "Proper torqueing of cylinder head bolts"
    ],
    "Temporary Solutions": [
      "Avoid driving under heavy load",
      "Keep engine coolant system well maintained"
    ]
  },

  "Oil Leaks from Engine Block": {
    "Actual Issue": "Oil leaking from seals or cracks in the engine block.",
    "Severity Level": "Medium — Can cause oil loss and engine damage if untreated; repair advised soon.",
    "Symptoms": [
      "Oil spots under vehicle",
      "Burning oil smell",
      "Low oil levels",
      "Smoke from engine bay"
    ],
    "Possible Causes": [
      {"cause": "Worn or damaged oil pan gasket", "probability": 0.4},
      {"cause": "Cracked engine block or oil passages", "probability": 0.2},
      {"cause": "Faulty seals (rear main seal, camshaft seals)", "probability": 0.3},
      {"cause": "Loose or damaged oil drain plug", "probability": 0.1}
    ],
    "Diagnostics": [
      "Visual inspection of engine block and oil pan",
      "Clean engine and check leak origin",
      "Use UV dye to trace leaks",
      "Check oil pressure"
    ],
    "Fixes": [
      "Replace oil pan gasket",
      "Replace damaged seals",
      "Repair or replace cracked engine block",
      "Tighten or replace drain plug"
    ],
    "Temporary Solutions": [
      "Use oil stop-leak additives",
      "Regularly check oil levels and top up"
    ]
  },

  "Coolant Leaks from Engine Block": {
    "Actual Issue": "Coolant leaking due to cracks or gasket failure around the engine block.",
    "Severity Level": "High — Causes overheating risk and potential engine damage; prompt fix essential.",
    "Symptoms": [
      "Coolant puddles under vehicle",
      "Sweet smell near engine bay",
      "Overheating engine",
      "White exhaust smoke"
    ],
    "Possible Causes": [
      {"cause": "Cracked engine block", "probability": 0.35},
      {"cause": "Failed head gasket", "probability": 0.40},
      {"cause": "Damaged freeze plugs", "probability": 0.15},
      {"cause": "Loose or damaged coolant hoses", "probability": 0.10}
    ],
    "Diagnostics": [
      "Pressure test cooling system",
      "Inspect freeze plugs and gasket areas",
      "Check coolant level and look for contamination",
      "Look for white smoke or milky oil"
    ],
    "Fixes": [
      "Replace head gasket",
      "Replace freeze plugs",
      "Repair or replace cracked engine block",
      "Replace damaged hoses"
    ],
    "Temporary Solutions": [
      "Add coolant to maintain levels",
      "Use radiator sealants temporarily"
    ]
  },

  "Piston Issues": {
    "Piston Slap": {
      "Actual Issue": "Noise caused by piston rocking inside the cylinder due to wear or clearance.",
      "Severity Level": "Medium — Causes noise and reduced engine smoothness; repair recommended to prevent further wear.",
      "Symptoms": [
        "Knocking or slapping noise from engine at cold start",
        "Noise reduces as engine warms up"
      ],
      "Possible Causes": [
        {"cause": "Worn piston skirts", "probability": 0.50},
        {"cause": "Excessive piston-to-cylinder clearance", "probability": 0.35},
        {"cause": "Worn or damaged piston rings", "probability": 0.15}
      ],
      "Diagnostics": [
        "Listen for noise on cold start",
        "Measure piston clearance",
        "Inspect piston skirts and rings"
      ],
      "Fixes": [
        "Replace pistons or rings",
        "Re-bore cylinders and fit new pistons"
      ],
      "Temporary Solutions": [
        "Warm up engine before driving",
        "Use thicker viscosity oil"
      ]
    },
    "Piston Ring Failure": {
      "Actual Issue": "Worn or broken piston rings causing loss of compression and oil consumption.",
      "Severity Level": "High — Leads to poor engine performance, increased emissions, and possible engine damage; requires timely repair.",
      "Symptoms": [
        "Excessive smoke from exhaust (blue or gray)",
        "Loss of engine power",
        "Increased oil consumption",
        "Poor fuel economy"
      ],
      "Possible Causes": [
        {"cause": "Wear over time", "probability": 0.55},
        {"cause": "Poor lubrication", "probability": 0.25},
        {"cause": "Overheating", "probability": 0.15},
        {"cause": "Contamination or debris", "probability": 0.05}
      ],
      "Diagnostics": [
        "Compression test",
        "Leak-down test",
        "Visual inspection during engine teardown"
      ],
      "Fixes": [
        "Replace piston rings",
        "Clean cylinder walls",
        "Ensure proper lubrication"
      ],
      "Temporary Solutions": [
        "Use oil additives to reduce consumption",
        "Drive gently until repair"
      ]
    },
    "Piston Seizure": {
      "Actual Issue": "Piston gets stuck in the cylinder, causing engine seizure.",
      "Severity Level": "Critical — Engine will stall and possibly cause severe damage; immediate repair necessary.",
      "Symptoms": [
        "Engine stalls suddenly",
        "Loud knocking or banging",
        "Engine will not turn over"
      ],
      "Possible Causes": [
        {"cause": "Severe overheating", "probability": 0.50},
        {"cause": "Lack of lubrication", "probability": 0.30},
        {"cause": "Cylinder wall damage", "probability": 0.15},
        {"cause": "Incorrect piston-to-cylinder clearance", "probability": 0.05}
      ],
      "Diagnostics": [
        "Visual inspection of pistons and cylinder walls",
        "Check oil pressure",
        "Check for signs of overheating"
      ],
      "Fixes": [
        "Replace or re-bore cylinder and pistons",
        "Fix lubrication system",
        "Replace damaged components"
      ],
      "Temporary Solutions": [
        "Avoid driving to prevent further damage"
      ]
    }
  },

  "Crankshaft Issues": {
    "Crankshaft Bearing Failure": {
      "Actual Issue": "Worn or damaged crankshaft bearings causing metal-to-metal contact and engine damage.",
      "Severity Level": "Critical — Causes severe engine damage and potential failure; immediate repair is critical.",
      "Symptoms": [
        "Knocking noise from engine (rod knock or main bearing knock)",
        "Low oil pressure warning",
        "Metal shavings in oil",
        "Engine vibration"
      ],
      "Possible Causes": [
        {"cause": "Insufficient lubrication", "probability": 0.60},
        {"cause": "Contaminated or degraded engine oil", "probability": 0.20},
        {"cause": "Excessive engine load or overheating", "probability": 0.15},
        {"cause": "Incorrect bearing installation", "probability": 0.05}
      ],
      "Diagnostics": [
        "Oil pressure test",
        "Visual inspection during engine teardown",
        "Check for metal debris in oil filter and pan",
        "Engine noise diagnosis"
      ],
      "Fixes": [
        "Replace crankshaft bearings",
        "Inspect and machine crankshaft journals if needed",
        "Flush and change engine oil",
        "Correct oiling system issues"
      ],
      "Temporary Solutions": [
        "Stop driving to prevent severe damage",
        "Use high-quality oil and change frequently"
      ]
    },
    "Crankshaft Wear or Damage": {
      "Actual Issue": "Physical wear, scoring, or cracks in the crankshaft causing imbalance and engine failure.",
      "Severity Level": "Critical — Can lead to catastrophic engine failure; urgent repair or replacement required.",
      "Symptoms": [
        "Severe engine knocking",
        "Excessive vibration",
        "Oil pressure drop",
        "Engine failure or stalls"
      ],
      "Possible Causes": [
        {"cause": "Bearing failure causing crankshaft damage", "probability": 0.50},
        {"cause": "Overheating", "probability": 0.25},
        {"cause": "Metal fatigue", "probability": 0.15},
        {"cause": "Improper installation or torqueing", "probability": 0.10}
      ],
      "Diagnostics": [
        "Visual inspection and magnetic particle testing",
        "Check crankshaft runout (straightness)",
        "Engine vibration analysis"
      ],
      "Fixes": [
        "Crankshaft grinding and polishing (if minor damage)",
        "Replace crankshaft",
        "Replace damaged bearings and components"
      ],
      "Temporary Solutions": [
        "Avoid heavy engine load",
        "Frequent oil changes to reduce wear"
      ]
    },
    "Crankshaft Seal Leak": {
      "Actual Issue": "Oil leaks from front or rear crankshaft seals.",
      "Severity Level": "Medium — Causes oil loss and potential contamination; repair recommended to prevent engine damage.",
      "Symptoms": [
        "Oil puddle under vehicle",
        "Oil dripping near transmission bell housing",
        "Low oil levels",
        "Burning oil smell"
      ],
      "Possible Causes": [
        {"cause": "Worn or hardened seals", "probability": 0.50},
        {"cause": "Improper seal installation", "probability": 0.20},
        {"cause": "Damaged crankshaft surface", "probability": 0.20},
        {"cause": "Excessive crankshaft end play", "probability": 0.10}
      ],
      "Diagnostics": [
        "Visual inspection of seals",
        "Check for oil leaks at seal areas",
        "Check crankshaft axial movement"
      ],
      "Fixes": [
        "Replace crankshaft seals",
        "Repair or polish crankshaft sealing surfaces",
        "Check and correct crankshaft end play"
      ],
      "Temporary Solutions": [
        "Add oil stop-leak additives",
        "Regularly monitor and top up oil"
      ]
    }
  },

  "Camshaft Issues": {
    "Camshaft Wear": {
      "Actual Issue": "Wear on cam lobes or journals causing improper valve timing and reduced engine performance.",
      "Severity Level": "High — Leads to valve timing issues and engine misfire; timely repair advised.",
      "Symptoms": [
        "Engine misfire or rough idle",
        "Loss of power",
        "Ticking or tapping noise from valve cover",
        "Check engine light (sometimes)"
      ],
      "Possible Causes": [
        {"cause": "Insufficient lubrication", "probability": 0.50},
        {"cause": "Use of wrong or contaminated oil", "probability": 0.25},
        {"cause": "Over-revving engine", "probability": 0.15},
        {"cause": "Normal wear over time", "probability": 0.10}
      ],
      "Diagnostics": [
        "Visual inspection of cam lobes and journals",
        "Check oil pressure",
        "Valve timing check",
        "Scan for misfire or camshaft position sensor codes"
      ],
      "Fixes": [
        "Replace camshaft if lobes are severely worn",
        "Use proper oil and maintain oil change intervals",
        "Inspect and replace lifters and followers if worn"
      ],
      "Temporary Solutions": [
        "Use high-quality engine oil",
        "Avoid high RPM until fixed"
      ]
    },
    "Camshaft Timing Issues": {
      "Actual Issue": "Incorrect camshaft timing caused by timing belt/chain failure or misalignment, leading to poor engine performance or damage.",
      "Severity Level": "Critical — Can cause severe engine damage if valves contact pistons; immediate repair required.",
      "Symptoms": [
        "Engine runs rough or won't start",
        "Loss of power",
        "Engine knocking or tapping noises",
        "Check engine light",
        "Backfiring or misfires"
      ],
      "Possible Causes": [
        {"cause": "Worn or broken timing belt/chain", "probability": 0.60},
        {"cause": "Incorrect timing belt/chain installation", "probability": 0.20},
        {"cause": "Faulty timing tensioner or guides", "probability": 0.15},
        {"cause": "Skipped timing teeth", "probability": 0.05}
      ],
      "Diagnostics": [
        "Inspect timing belt/chain condition",
        "Check timing marks alignment",
        "Scan engine codes for camshaft position sensor faults",
        "Compression test to check valve timing"
      ],
      "Fixes": [
        "Replace timing belt/chain and tensioner",
        "Correct timing alignment",
        "Replace damaged guides"
      ],
      "Temporary Solutions": [
        "Avoid driving if timing belt/chain is suspected broken",
        "Check timing belt service interval regularly"
      ]
    },
    "Camshaft Bearing Failure": {
      "Actual Issue": "Wear or damage to camshaft bearings causing noise and lubrication issues.",
      "Severity Level": "High — Causes engine noise and potential damage; repair needed soon.",
      "Symptoms": [
        "Knocking or ticking noises from engine",
        "Low oil pressure",
        "Metal debris in oil",
        "Engine performance issues"
      ],
      "Possible Causes": [
        {"cause": "Poor lubrication", "probability": 0.50},
        {"cause": "Contaminated or low oil", "probability": 0.25},
        {"cause": "Bearing material fatigue", "probability": 0.15},
        {"cause": "Overheating", "probability": 0.10}
      ],
      "Diagnostics": [
        "Oil pressure test",
        "Visual inspection of bearings",
        "Oil analysis for metal particles"
      ],
      "Fixes": [
        "Replace camshaft bearings",
        "Check and restore oil flow",
        "Replace camshaft if damaged"
      ],
      "Temporary Solutions": [
        "Use high-quality oil and change frequently",
        "Avoid high engine loads"
      ]
    },

"Valve and Valve Train Issues": {
  "Valve Wear or Burning": {
    "Actual Issue": "Valve faces or seats become worn or burned, causing poor sealing and compression loss.",
    "Severity Level": "High — Valve damage leads to poor engine performance and possible further damage if untreated, requiring timely repair.",
    "Possible Causes": [
      {"cause": "Overheating", "probability": 0.30},
      {"cause": "Incorrect valve clearance", "probability": 0.25},
      {"cause": "Poor lubrication", "probability": 0.20},
      {"cause": "Detonation or pre-ignition", "probability": 0.15},
      {"cause": "Carbon buildup", "probability": 0.10}
    ],
    "Diagnostics": [
      "Compression test",
      "Leak-down test",
      "Visual inspection of valves and seats",
      "Check valve clearances"
    ],
    "Fixes": [
      "Replace or regrind valves and valve seats",
      "Adjust valve clearance",
      "Clean carbon deposits",
      "Use proper fuel and oil"
    ],
    "Temporary Solutions": [
      "Avoid high engine load",
      "Use fuel additives to clean valves"
    ]
  },
  "Valve Lash or Clearance Issues": {
    "Actual Issue": "Incorrect valve clearance causes noisy operation or poor valve seating.",
    "Severity Level": "Medium — Causes noise and inefficiency; can lead to damage if left unattended, so adjustment is recommended.",
    "Possible Causes": [
      {"cause": "Improper adjustment", "probability": 0.40},
      {"cause": "Wear of camshaft or rocker arms", "probability": 0.30},
      {"cause": "Thermal expansion differences", "probability": 0.20},
      {"cause": "Faulty lifters or tappets", "probability": 0.10}
    ],
    "Diagnostics": [
      "Measure valve lash with feeler gauge",
      "Inspect lifters and rocker arms",
      "Listen for valve train noise"
    ],
    "Fixes": [
      "Adjust valve clearance",
      "Replace worn components",
      "Use hydraulic lifters if applicable"
    ],
    "Temporary Solutions": [
      "Reduce engine speed",
      "Use oil additives to reduce noise"
    ]
  },
  "Bent or Broken Valves": {
    "Actual Issue": "Valves are physically bent or broken due to mechanical failure or timing issues.",
    "Severity Level": "Critical — Severe mechanical failure that can cause catastrophic engine damage; immediate repair required.",
    "Possible Causes": [
      {"cause": "Timing belt/chain failure causing piston-valve collision", "probability": 0.50},
      {"cause": "Over-revving engine", "probability": 0.25},
      {"cause": "Valve spring failure", "probability": 0.15},
      {"cause": "Foreign object in combustion chamber", "probability": 0.10}
    ],
    "Diagnostics": [
      "Compression test",
      "Visual inspection during teardown",
      "Check timing components",
      "Scan for engine codes"
    ],
    "Fixes": [
      "Replace bent or broken valves",
      "Replace timing belt/chain and related parts",
      "Inspect and repair cylinder head"
    ],
    "Temporary Solutions": [
      "Do not run engine if suspected valve damage",
      "Tow vehicle to repair shop"
    ]
  },
  "Valve Spring Failure": {
    "Actual Issue": "Valve springs lose tension or break, affecting valve operation.",
    "Severity Level": "High — Valve spring failure compromises engine reliability and valve control; repair promptly.",
    "Possible Causes": [
      {"cause": "Spring fatigue", "probability": 0.60},
      {"cause": "Over-revving", "probability": 0.30},
      {"cause": "Manufacturing defects", "probability": 0.10}
    ],
    "Diagnostics": [
      "Visual inspection of valve springs",
      "Check valve operation",
      "Listen for valve train noise"
    ],
    "Fixes": [
      "Replace faulty valve springs",
      "Avoid excessive RPMs"
    ],
    "Temporary Solutions": [
      "Drive gently until repaired"
    ]
  }
},

"Timing System Issues": {
  "Timing Belt/Chain Failure": {
    "Actual Issue": "Timing belt or chain breaks or slips, causing loss of synchronization between crankshaft and camshaft.",
    "Severity Level": "Critical — Loss of synchronization can cause severe engine damage; immediate repair necessary.",
    "Possible Causes": [
      {"cause": "Timing belt wear or age", "probability": 0.50},
      {"cause": "Incorrect installation or tension", "probability": 0.20},
      {"cause": "Faulty tensioner or guides", "probability": 0.20},
      {"cause": "Chain stretching (in chain systems)", "probability": 0.10}
    ],
    "Diagnostics": [
      "Visual inspection of timing belt/chain",
      "Check belt tension and condition",
      "Listen for unusual noises",
      "Scan for cam/crank position sensor errors",
      "Compression test if damage suspected"
    ],
    "Fixes": [
      "Replace timing belt/chain and tensioners",
      "Correct timing alignment",
      "Replace damaged valves/pistons if interference occurred"
    ],
    "Temporary Solutions": [
      "Avoid driving if timing belt/chain suspected damaged",
      "Perform regular maintenance as per schedule"
    ]
  },
  "Timing Belt/Chain Tensioner Failure": {
    "Actual Issue": "Tensioner fails to maintain proper tension on timing belt or chain, causing slippage or noise.",
    "Severity Level": "High — Tensioner failure risks timing slip and engine damage; timely replacement recommended.",
    "Possible Causes": [
      {"cause": "Worn or seized tensioner", "probability": 0.60},
      {"cause": "Oil contamination", "probability": 0.30},
      {"cause": "Incorrect installation", "probability": 0.10}
    ],
    "Diagnostics": [
      "Inspect tensioner for wear or damage",
      "Check belt/chain tension",
      "Listen for noise"
    ],
    "Fixes": [
      "Replace tensioner and related components",
      "Inspect and replace timing belt/chain if needed"
    ],
    "Temporary Solutions": [
      "Reduce engine load",
      "Avoid high RPM"
    ]
  },
  "Timing Marks Misalignment": {
    "Actual Issue": "Incorrect alignment of timing marks during assembly causing improper valve timing.",
    "Severity Level": "Critical — Causes poor engine performance and risk of engine damage; must be corrected immediately.",
    "Possible Causes": [
      {"cause": "Incorrect timing belt/chain installation", "probability": 0.60},
      {"cause": "Slipped timing components", "probability": 0.30},
      {"cause": "Improper maintenance", "probability": 0.10}
    ],
    "Diagnostics": [
      "Check timing marks alignment",
      "Perform compression test",
      "Scan for cam/crank sensor codes"
    ],
    "Fixes": [
      "Realign timing marks",
      "Replace timing components if damaged"
    ],
    "Temporary Solutions": [
      "Avoid driving until corrected"
    ]
  }
},

"Fuel System Issues": {
  "Fuel Pump Failure": {
    "Actual Issue": "Fuel pump fails to deliver adequate fuel pressure to the engine.",
    "Severity Level": "High — Causes engine stalling or no-start conditions; urgent repair required.",
    "Possible Causes": [
      {"cause": "Electrical failure of fuel pump", "probability": 0.40},
      {"cause": "Clogged fuel filter", "probability": 0.30},
      {"cause": "Fuel contamination", "probability": 0.20},
      {"cause": "Worn pump components", "probability": 0.10}
    ],
    "Diagnostics": [
      "Measure fuel pressure with gauge",
      "Check electrical connections and fuses",
      "Inspect fuel filter for clogging",
      "Listen for fuel pump operation noise"
    ],
    "Fixes": [
      "Replace fuel pump",
      "Replace clogged fuel filter",
      "Clean fuel tank and lines",
      "Repair electrical faults"
    ],
    "Temporary Solutions": [
      "Add fuel system cleaner additives",
      "Avoid running on low fuel"
    ]
  },
  "Fuel Injector Issues": {
    "Actual Issue": "Fuel injectors clog, leak, or fail to deliver proper fuel spray.",
    "Severity Level": "Medium — Causes poor fuel delivery and engine roughness; repair recommended to maintain performance.",
    "Possible Causes": [
      {"cause": "Clogged injectors", "probability": 0.45},
      {"cause": "Electrical faults in injector circuit", "probability": 0.25},
      {"cause": "Fuel contamination", "probability": 0.20},
      {"cause": "Worn injector seals", "probability": 0.10}
    ],
    "Diagnostics": [
      "Injector resistance test",
      "Fuel pressure test",
      "Use of injector cleaning tools",
      "Scan engine codes"
    ],
    "Fixes": [
      "Clean or replace fuel injectors",
      "Repair wiring or connectors",
      "Replace fuel filter",
      "Use high-quality fuel"
    ],
    "Temporary Solutions": [
      "Use fuel injector cleaner additives",
      "Drive gently until repair"
    ]
  },
  "Fuel Filter Clogging": {
    "Actual Issue": "Fuel filter clogged, restricting fuel flow.",
    "Severity Level": "Medium — Restricts fuel delivery causing poor engine performance; filter replacement advised.",
    "Possible Causes": [
      {"cause": "Dirty or contaminated fuel", "probability": 0.50},
      {"cause": "Long service interval", "probability": 0.35},
      {"cause": "Poor quality fuel", "probability": 0.15}
    ],
    "Diagnostics": [
      "Fuel pressure test before and after filter",
      "Inspect and replace filter"
    ],
    "Fixes": [
      "Replace fuel filter at recommended intervals"
    ],
    "Temporary Solutions": [
      "Use fuel system cleaners",
      "Avoid fuel from unreliable sources"
    ]
  }
},

"Lubrication System Issues": {
  "Low Oil Pressure": {
    "Actual Issue": "Oil pressure drops below normal, risking engine damage due to insufficient lubrication.",
    "Severity Level": "Critical — Immediate risk of engine damage; must be addressed urgently.",
    "Possible Causes": [
      {"cause": "Low oil level", "probability": 0.35},
      {"cause": "Worn oil pump", "probability": 0.25},
      {"cause": "Clogged oil passages or filter", "probability": 0.20},
      {"cause": "Oil leaks", "probability": 0.10},
      {"cause": "Worn engine bearings", "probability": 0.10}
    ],
    "Diagnostics": [
      "Check oil level",
      "Measure oil pressure with gauge",
      "Inspect for leaks",
      "Oil analysis for contamination",
      "Inspect oil pump and bearings"
    ],
    "Fixes": [
      "Refill or change engine oil",
      "Replace oil pump",
      "Clean or replace oil filter",
      "Repair leaks",
      "Replace worn bearings"
    ],
    "Temporary Solutions": [
      "Avoid heavy engine load",
      "Stop driving if pressure warning appears"
    ]
  },
  "Oil Leaks": {
    "Actual Issue": "Oil leaking from gaskets, seals, or cracks causing loss of lubrication and contamination.",
    "Severity Level": "Medium — Causes oil loss and contamination; repair recommended to prevent damage.",
    "Possible Causes": [
      {"cause": "Worn or damaged gaskets and seals", "probability": 0.50},
      {"cause": "Cracked oil pan or engine block", "probability": 0.20},
      {"cause": "Loose oil drain plug", "probability": 0.20},
      {"cause": "Overfilled oil", "probability": 0.10}
    ],
    "Diagnostics": [
      "Visual inspection",
      "Use UV dye to trace leaks",
      "Check oil level regularly"
    ],
    "Fixes": [
      "Replace gaskets and seals",
      "Repair or replace damaged parts",
      "Tighten or replace drain plug",
      "Drain excess oil"
    ],
    "Temporary Solutions": [
      "Use oil stop-leak additives",
      "Monitor oil level and top up"
    ]
  },
  "Oil Pump Failure": {
    "Actual Issue": "Oil pump fails to circulate oil properly, risking engine damage.",
    "Severity Level": "Critical — Oil circulation failure risks catastrophic engine damage; urgent repair necessary.",
    "Possible Causes": [
      {"cause": "Wear or damage to oil pump", "probability": 0.60},
      {"cause": "Clogged oil pickup tube", "probability": 0.25},
      {"cause": "Oil contamination", "probability": 0.15}
    ],
    "Diagnostics": [
      "Oil pressure test",
      "Inspect oil pump and pickup tube",
      "Oil analysis"
    ],
    "Fixes": [
      "Replace oil pump",
      "Clean oil pickup tube",
      "Change oil and filter"
    ],
    "Temporary Solutions": [
      "Avoid engine overload",
      "Frequent oil checks"
    ]
  }
},

"Cooling System Issues": {
  "Radiator Leak": {
    "Actual Issue": "Radiator develops leaks causing coolant loss and overheating.",
    "Severity Level": "High — Coolant loss can cause engine overheating and damage; repair promptly.",
    "Possible Causes": [
      {"cause": "Corrosion", "probability": 0.40},
      {"cause": "Physical damage", "probability": 0.30},
      {"cause": "Loose or damaged hoses", "probability": 0.20},
      {"cause": "Faulty radiator cap", "probability": 0.10}
    ],
    "Diagnostics": [
      "Visual inspection",
      "Pressure test cooling system",
      "Check hoses and clamps"
    ],
    "Fixes": [
      "Repair or replace radiator",
      "Replace hoses and clamps",
      "Replace radiator cap"
    ],
    "Temporary Solutions": [
      "Use radiator sealant",
      "Add coolant as needed"
    ]
  }
},
   "Thermostat Failure": {
    "Actual Issue": "Thermostat stuck open or closed causing overheating or poor engine warm-up.",
    "Severity Level": "Medium — Can cause inefficient engine operation or overheating if not addressed.",
    "Possible Causes": [
      {"cause": "Thermostat stuck closed (overheating)", "probability": 0.60},
      {"cause": "Thermostat stuck open (engine runs cold)", "probability": 0.40}
    ],
    "Diagnostics": [
      "Remove and test thermostat",
      "Monitor engine temperature"
    ],
    "Fixes": [
      "Replace thermostat"
    ],
    "Temporary Solutions": [
      "Avoid heavy engine load",
      "Allow engine to warm up fully"
    ]
  },
  "Water Pump Failure": {
    "Actual Issue": "Water pump fails to circulate coolant properly causing overheating.",
    "Severity Level": "High — Coolant circulation failure can lead to engine overheating and severe damage.",
    "Possible Causes": [
      {"cause": "Worn bearings or seals", "probability": 0.50},
      {"cause": "Corrosion or blockage", "probability": 0.30},
      {"cause": "Broken impeller", "probability": 0.20}
    ],
    "Diagnostics": [
      "Visual inspection",
      "Check for leaks and noise",
      "Pressure test cooling system"
    ],
    "Fixes": [
      "Replace water pump"
    ],
    "Temporary Solutions": [
      "Avoid driving when overheating",
      "Add coolant as emergency"
    ]
  },
  "Exhaust System Issues": {
    "Exhaust Leak": {
      "Actual Issue": "Leak in exhaust system causing noise, emissions issues, and loss of performance.",
      "Severity Level": "Medium — Can cause performance loss and emissions failures, but usually not immediately dangerous.",
      "Possible Causes": [
        {"cause": "Cracked exhaust manifold", "probability": 0.35},
        {"cause": "Damaged or rusted exhaust pipes", "probability": 0.30},
        {"cause": "Loose or damaged exhaust clamps", "probability": 0.20},
        {"cause": "Faulty gaskets or seals", "probability": 0.15}
      ],
      "Diagnostics": [
        "Visual inspection for cracks and holes",
        "Listen for unusual noise",
        "Check exhaust system mounting points",
        "Smoke test for leaks"
      ],
      "Fixes": [
        "Repair or replace damaged exhaust components",
        "Tighten or replace clamps",
        "Replace faulty gaskets"
      ],
      "Temporary Solutions": [
        "Use exhaust tape or sealant",
        "Avoid high engine loads"
      ]
    },
    "Catalytic Converter Failure": {
      "Actual Issue": "Catalytic converter clogged or damaged causing poor emissions and performance.",
      "Severity Level": "High — Can cause engine performance loss and emissions failures, requiring timely repair.",
      "Possible Causes": [
        {"cause": "Contamination by unburnt fuel or oil", "probability": 0.50},
        {"cause": "Physical damage", "probability": 0.30},
        {"cause": "Excessive exhaust backpressure", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan for related engine codes (e.g., P0420)",
        "Measure exhaust backpressure",
        "Visual inspection"
      ],
      "Fixes": [
        "Replace catalytic converter",
        "Fix engine issues causing contamination"
      ],
      "Temporary Solutions": [
        "Avoid aggressive driving",
        "Use fuel additives for catalytic cleaner"
      ]
    },
    "Muffler Damage or Corrosion": {
      "Actual Issue": "Muffler damaged or rusted causing excessive noise and emissions.",
      "Severity Level": "Medium — Causes noise and emissions issues but typically does not affect safety immediately.",
      "Possible Causes": [
        {"cause": "Corrosion from moisture", "probability": 0.60},
        {"cause": "Physical damage", "probability": 0.25},
        {"cause": "Exhaust system age", "probability": 0.15}
      ],
      "Diagnostics": [
        "Visual inspection",
        "Listen for unusual noises"
      ],
      "Fixes": [
        "Replace or repair muffler"
      ],
      "Temporary Solutions": [
        "Patch holes with exhaust tape",
        "Avoid driving in wet conditions when possible"
      ]
    }
  },
  "Suspension System Issues": {
    "Worn Shock Absorbers or Struts": {
      "Actual Issue": "Shock absorbers or struts lose damping ability, causing poor ride quality and handling.",
      "Severity Level": "Medium — Impacts comfort and handling; prolonged use can affect safety.",
      "Possible Causes": [
        {"cause": "Normal wear and tear", "probability": 0.70},
        {"cause": "Leaks in shock absorber seals", "probability": 0.20},
        {"cause": "Physical damage", "probability": 0.10}
      ],
      "Diagnostics": [
        "Visual inspection for leaks and damage",
        "Bounce test on each corner of vehicle",
        "Check tire wear patterns"
      ],
      "Fixes": [
        "Replace shock absorbers or struts"
      ],
      "Temporary Solutions": [
        "Drive carefully over rough roads",
        "Avoid heavy loads"
      ]
    },
    "Worn or Broken Suspension Springs": {
      "Actual Issue": "Coil or leaf springs weaken or break causing sagging or uneven ride height.",
      "Severity Level": "High — Broken springs can severely affect vehicle stability and safety, requiring prompt attention.",
      "Possible Causes": [
        {"cause": "Corrosion", "probability": 0.40},
        {"cause": "Metal fatigue", "probability": 0.40},
        {"cause": "Physical damage or impact", "probability": 0.20}
      ],
      "Diagnostics": [
        "Visual inspection",
        "Measure ride height",
        "Listen for noises"
      ],
      "Fixes": [
        "Replace worn or broken springs"
      ],
      "Temporary Solutions": [
        "Avoid heavy loads",
        "Drive cautiously over potholes"
      ]
    },
    "Worn Bushings": {
      "Actual Issue": "Suspension bushings degrade causing noise, looseness, and poor handling.",
      "Severity Level": "Medium — Causes noise and handling issues but usually not immediately dangerous.",
      "Possible Causes": [
        {"cause": "Aging and wear", "probability": 0.70},
        {"cause": "Exposure to chemicals or road salt", "probability": 0.20},
        {"cause": "Physical damage", "probability": 0.10}
      ],
      "Diagnostics": [
        "Visual inspection",
        "Check for play in suspension components"
      ],
      "Fixes": [
        "Replace worn bushings"
      ],
      "Temporary Solutions": [
        "Drive carefully",
        "Avoid rough terrain"
      ]
    },
    "Ball Joint Wear": {
      "Actual Issue": "Ball joints wear out causing looseness and potential steering issues.",
      "Severity Level": "High — Can cause steering problems and potential loss of control, urgent replacement needed.",
      "Possible Causes": [
        {"cause": "Normal wear", "probability": 0.60},
        {"cause": "Lack of lubrication", "probability": 0.30},
        {"cause": "Physical damage", "probability": 0.10}
      ],
      "Diagnostics": [
        "Visual inspection",
        "Check for play in ball joints"
      ],
      "Fixes": [
        "Replace ball joints"
      ],
      "Temporary Solutions": [
        "Drive cautiously",
        "Avoid rough terrain"
      ]
    }
  },
  "Electric Power Steering (EPS) Issues": {
    "EPS Motor Failure": {
      "Actual Issue": "Failure or malfunction of the electric motor that provides steering assist.",
      "Severity Level": "High — Loss of power assist can make steering difficult, especially at low speeds.",
      "Possible Causes": [
        {"cause": "Electrical faults in motor windings", "probability": 0.50},
        {"cause": "Overheating or mechanical damage", "probability": 0.30},
        {"cause": "Connector or wiring issues", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan EPS control module for fault codes",
        "Check motor electrical resistance and power supply",
        "Visual inspection of wiring and connectors"
      ],
      "Fixes": [
        "Repair or replace EPS motor",
        "Fix wiring/connectors",
        "Reset EPS control module"
      ],
      "Temporary Solutions": [
        "Drive cautiously without power assist",
        "Avoid sharp turns and heavy steering"
      ]
    },
    "EPS Control Module Failure": {
      "Actual Issue": "Malfunction of the EPS control module leading to loss of steering assist or erratic behavior.",
      "Severity Level": "High — Can cause sudden loss of power steering assist; needs immediate attention.",
      "Possible Causes": [
        {"cause": "Software bugs or glitches", "probability": 0.40},
        {"cause": "Water ingress or physical damage", "probability": 0.35},
        {"cause": "Electrical faults", "probability": 0.25}
      ],
      "Diagnostics": [
        "Scan control module for error codes",
        "Check wiring and connectors",
        "Perform module reset or reprogramming"
      ],
      "Fixes": [
        "Reprogram or replace EPS control module",
        "Repair wiring or connectors"
      ],
      "Temporary Solutions": [
        "Drive carefully with reduced assist",
        "Avoid sudden steering inputs"
      ]
    },
    "EPS Sensor Failure": {
      "Actual Issue": "Faulty torque or position sensors in the EPS system causing incorrect assist levels.",
      "Severity Level": "Medium — Steering feel may be affected; usually manageable but requires repair.",
      "Possible Causes": [
        {"cause": "Sensor wear or damage", "probability": 0.50},
        {"cause": "Electrical faults or poor connections", "probability": 0.35},
        {"cause": "Contamination or corrosion", "probability": 0.15}
      ],
      "Diagnostics": [
        "Scan for sensor-related error codes",
        "Inspect sensor wiring and connectors",
        "Test sensor output signals"
      ],
      "Fixes": [
        "Replace faulty sensors",
        "Repair wiring/connectors"
      ],
      "Temporary Solutions": [
        "Drive cautiously",
        "Avoid abrupt steering movements"
      ]
    },
    "EPS Software Calibration Issues": {
      "Actual Issue": "Incorrect EPS system calibration causing steering feel or behavior issues.",
      "Severity Level": "Low — Usually affects steering feel but not safety; fix with recalibration.",
      "Possible Causes": [
        {"cause": "After repairs or part replacements without proper calibration", "probability": 0.70},
        {"cause": "Battery disconnect or power loss", "probability": 0.30}
      ],
      "Diagnostics": [
        "Perform EPS system calibration with diagnostic tool",
        "Check for error codes"
      ],
      "Fixes": [
        "Recalibrate EPS system",
        "Reset or update software"
      ],
      "Temporary Solutions": [
        "Drive carefully until calibrated"
      ]
    }
  },
  "Braking System Issues": {
    "Brake Pad Wear": {
      "Actual Issue": "Brake pads worn down reducing braking efficiency and risking damage to rotors.",
      "Severity Level": "High — Reduced braking power increases stopping distances and risk of accidents.",
      "Possible Causes": [
        {"cause": "Normal wear", "probability": 0.60},
        {"cause": "Driving habits (hard braking)", "probability": 0.30},
        {"cause": "Contaminated brake pads", "probability": 0.10}
      ],
      "Diagnostics": [
        "Visual inspection of brake pads",
        "Measure pad thickness",
        "Brake performance test"
      ],
      "Fixes": [
        "Replace brake pads",
        "Inspect and resurface or replace rotors if needed"
      ],
      "Temporary Solutions": [
        "Drive gently to reduce wear",
        "Avoid sudden braking"
      ]
    },
    "Brake Fluid Leak": {
      "Actual Issue": "Leak in brake lines, calipers, or master cylinder causing reduced hydraulic pressure.",
      "Severity Level": "Critical — Loss of hydraulic pressure can lead to brake failure, immediate repair required.",
      "Possible Causes": [
        {"cause": "Damaged brake lines or hoses", "probability": 0.40},
        {"cause": "Worn caliper seals", "probability": 0.30},
        {"cause": "Faulty master cylinder", "probability": 0.20},
        {"cause": "Loose fittings", "probability": 0.10}
      ],
      "Diagnostics": [
        "Visual inspection for leaks",
        "Brake pressure test",
        "Check fluid level and condition"
      ],
      "Fixes": [
        "Repair or replace leaking components",
        "Bleed brake system",
        "Refill brake fluid"
      ],
      "Temporary Solutions": [
        "Avoid hard braking",
        "Regularly check fluid level"
      ]
    },
    "ABS Sensor Failure": {
      "Actual Issue": "Faulty ABS wheel speed sensors causing malfunction of anti-lock braking system.",
      "Severity Level": "Medium — ABS may be disabled, reducing safety in slippery conditions.",
      "Possible Causes": [
        {"cause": "Sensor damage or contamination", "probability": 0.50},
        {"cause": "Wiring faults", "probability": 0.30},
        {"cause": "Corroded connectors", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan ABS control module for error codes",
        "Visual inspection of sensors and wiring",
        "Measure sensor signals"
      ],
      "Fixes": [
        "Clean or replace faulty sensors",
        "Repair wiring and connectors"
      ],
      "Temporary Solutions": [
        "Drive cautiously, especially on slippery roads",
        "Avoid sudden braking"
      ]
    },
    "Brake Caliper Sticking": {
      "Actual Issue": "Caliper pistons stick or seize causing uneven brake pad wear and pulling.",
      "Severity Level": "High — Can cause uneven braking and vehicle pulling, urgent repair needed.",
      "Possible Causes": [
        {"cause": "Corrosion or dirt in caliper pistons", "probability": 0.50},
        {"cause": "Worn caliper seals", "probability": 0.30},
        {"cause": "Damaged slide pins", "probability": 0.20}
      ],
      "Diagnostics": [
        "Visual inspection",
        "Check caliper piston movement",
        "Brake performance test"
      ],
      "Fixes": [
        "Clean and rebuild calipers",
        "Replace calipers if severely damaged",
        "Lubricate slide pins"
      ],
      "Temporary Solutions": [
        "Avoid heavy braking",
        "Drive gently until repaired"
      ]
    }
  },
  "Electronic Parking Brake (EPB) Failure": {
    "Actual Issue": "Malfunction of the electronic parking brake system.",
    "Severity Level": "Medium — Can cause parking brake failure; may prevent secure parking on slopes.",
    "Possible Causes": [
      {"cause": "Faulty EPB motor or actuator", "probability": 0.50},
      {"cause": "Electrical faults or sensor issues", "probability": 0.30},
      {"cause": "Mechanical failure in brake components", "probability": 0.20}
    ],
    "Diagnostics": [
      "Scan EPB control module for codes",
      "Check wiring and connectors",
      "Test EPB motor operation"
    ],
    "Fixes": [
      "Repair or replace EPB components",
      "Reset or reprogram EPB system"
    ],
    "Temporary Solutions": [
      "Use manual parking brake if available",
      "Avoid parking on slopes"
    ]
  },
  "Electrical System Issues": {
    "Battery Failure": {
      "Actual Issue": "Battery unable to hold charge or deliver sufficient current.",
      "Severity Level": "High — Can cause vehicle not to start or electrical failures.",
      "Possible Causes": [
        {"cause": "Old or worn-out battery", "probability": 0.50},
        {"cause": "Parasitic drain", "probability": 0.20},
        {"cause": "Faulty alternator", "probability": 0.20},
        {"cause": "Corroded or loose connections", "probability": 0.10}
      ],
      "Diagnostics": [
        "Battery load test",
        "Check voltage and specific gravity",
        "Inspect terminals and cables",
        "Check alternator output"
      ],
      "Fixes": [
        "Replace battery",
        "Clean and tighten terminals",
        "Repair charging system"
      ],
      "Temporary Solutions": [
        "Jump start vehicle",
        "Limit electrical load"
      ]
    },
    "Alternator Failure": {
      "Actual Issue": "Alternator fails to charge battery or power electrical systems properly.",
      "Severity Level": "High — Battery will drain causing vehicle to stop if alternator fails.",
      "Possible Causes": [
        {"cause": "Worn brushes or bearings", "probability": 0.50},
        {"cause": "Faulty voltage regulator", "probability": 0.30},
        {"cause": "Broken drive belt", "probability": 0.20}
      ],
      "Diagnostics": [
        "Measure charging voltage",
        "Inspect alternator belt",
        "Check alternator output"
      ],
      "Fixes": [
        "Replace or rebuild alternator",
        "Replace drive belt",
        "Repair wiring"
      ],
      "Temporary Solutions": [
        "Minimize electrical use",
        "Drive to recharge battery"
      ]
    },
    "Starter Motor Issues": {
      "Actual Issue": "Starter motor fails to crank engine reliably.",
      "Severity Level": "High — Prevents engine from starting, urgent repair needed.",
      "Possible Causes": [
        {"cause": "Worn starter motor brushes", "probability": 0.40},
        {"cause": "Faulty solenoid", "probability": 0.30},
        {"cause": "Battery or wiring issues", "probability": 0.30}
      ],
      "Diagnostics": [
        "Voltage drop test",
        "Check battery and cables",
        "Bench test starter motor"
      ],
      "Fixes": [
        "Repair or replace starter motor",
        "Repair wiring or connections"
      ],
      "Temporary Solutions": [
        "Tap starter motor gently",
        "Ensure battery is fully charged"
      ]
    },
    "CAN Bus Communication Fault": {
      "Actual Issue": "Faults in Controller Area Network (CAN) bus causing communication failures between electronic modules.",
      "Severity Level": "Medium — May cause multiple system malfunctions but rarely causes immediate safety issues.",
      "Possible Causes": [
        {"cause": "Damaged wiring or connectors", "probability": 0.50},
        {"cause": "Faulty control module", "probability": 0.30},
        {"cause": "Electrical interference", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan CAN bus for error codes",
        "Inspect wiring harness and connectors",
        "Check module responses"
      ],
      "Fixes": [
        "Repair wiring or connectors",
        "Replace faulty control modules"
      ],
      "Temporary Solutions": [
        "Disconnect battery and restart vehicle",
        "Drive cautiously"
      ]
    }
  },

"Transmission System Issues": {
    "Manual Transmission Clutch Wear": {
      "Actual Issue": "Clutch disc wears down causing slipping and poor power transfer.",
      "Severity Level": "High — Clutch slipping severely affects drivability and may cause further transmission damage if not repaired promptly.",
      "Possible Causes": [
        {"cause": "Normal wear", "probability": 0.60},
        {"cause": "Riding the clutch", "probability": 0.25},
        {"cause": "Incorrect clutch adjustment", "probability": 0.10},
        {"cause": "Oil contamination", "probability": 0.05}
      ],
      "Diagnostics": [
        "Clutch slip test",
        "Visual inspection of clutch components",
        "Check clutch pedal free play"
      ],
      "Fixes": [
        "Replace clutch disc and pressure plate",
        "Adjust clutch linkage or hydraulic system"
      ],
      "Temporary Solutions": [
        "Avoid riding clutch",
        "Drive gently"
      ]
    },
    "Automatic Transmission Fluid Leak": {
      "Actual Issue": "Leakage of transmission fluid leading to low fluid level and transmission issues.",
      "Severity Level": "High — Fluid leaks can cause transmission overheating and failure, requiring urgent repair.",
      "Possible Causes": [
        {"cause": "Damaged seals or gaskets", "probability": 0.50},
        {"cause": "Worn transmission pan", "probability": 0.30},
        {"cause": "Loose or damaged cooler lines", "probability": 0.20}
      ],
      "Diagnostics": [
        "Visual inspection for leaks",
        "Check fluid level and condition",
        "Pressure test transmission"
      ],
      "Fixes": [
        "Replace seals, gaskets, or damaged parts",
        "Refill and flush transmission fluid"
      ],
      "Temporary Solutions": [
        "Avoid heavy towing or load",
        "Monitor fluid level regularly"
      ]
    },
    "CVT Belt or Chain Wear": {
      "Actual Issue": "Wear or damage to continuously variable transmission belt or chain causing slipping or noise.",
      "Severity Level": "High — Worn CVT components cause slipping and potential transmission failure if ignored.",
      "Possible Causes": [
        {"cause": "Normal wear", "probability": 0.60},
        {"cause": "Overheating", "probability": 0.25},
        {"cause": "Incorrect fluid type or level", "probability": 0.15}
      ],
      "Diagnostics": [
        "Scan transmission control unit for codes",
        "Check fluid condition",
        "Test drive for symptoms"
      ],
      "Fixes": [
        "Replace CVT belt or chain",
        "Change fluid with manufacturer recommended type"
      ],
      "Temporary Solutions": [
        "Drive gently",
        "Avoid rapid acceleration"
      ]
    },
    "Dual-Clutch Transmission (DCT) Mechatronic Failure": {
      "Actual Issue": "Failure in electronic-mechanical system controlling clutch and gear changes in DCT.",
      "Severity Level": "High — Mechatronic faults can cause loss of drive or erratic shifting, posing safety risks.",
      "Possible Causes": [
        {"cause": "Mechatronic unit software issues", "probability": 0.50},
        {"cause": "Hydraulic leaks", "probability": 0.30},
        {"cause": "Electrical faults", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan transmission control module for faults",
        "Inspect wiring and hydraulic system",
        "Test gear engagement"
      ],
      "Fixes": [
        "Reprogram or replace mechatronic unit",
        "Repair hydraulic leaks",
        "Replace damaged wiring"
      ],
      "Temporary Solutions": [
        "Use manual mode if available",
        "Drive gently"
      ]
    }
  },
  "Ignition System Issues": {
    "Faulty Spark Plugs": {
      "Actual Issue": "Spark plugs worn or fouled causing weak or no spark.",
      "Severity Level": "Medium — Causes rough running and misfires; impacts performance but not usually immediate danger.",
      "Possible Causes": [
        {"cause": "Normal wear", "probability": 0.60},
        {"cause": "Carbon or oil fouling", "probability": 0.25},
        {"cause": "Incorrect heat range", "probability": 0.10},
        {"cause": "Improper gap", "probability": 0.05}
      ],
      "Diagnostics": [
        "Visual inspection",
        "Check spark plug gap",
        "Scan for misfire codes"
      ],
      "Fixes": [
        "Replace spark plugs",
        "Adjust gap",
        "Use manufacturer recommended plugs"
      ],
      "Temporary Solutions": [
        "Use fuel additives",
        "Drive gently"
      ]
    },
    "Ignition Coil Failure": {
      "Actual Issue": "Ignition coils fail causing weak or no spark at spark plugs.",
      "Severity Level": "High — Coil failure causes misfires and poor engine performance; urgent replacement needed.",
      "Possible Causes": [
        {"cause": "Coil overheating", "probability": 0.50},
        {"cause": "Electrical faults", "probability": 0.30},
        {"cause": "Physical damage", "probability": 0.20}
      ],
      "Diagnostics": [
        "Check coil resistance",
        "Scan for fault codes",
        "Visual inspection"
      ],
      "Fixes": [
        "Replace ignition coil",
        "Repair wiring"
      ],
      "Temporary Solutions": [
        "Avoid high engine loads",
        "Drive gently"
      ]
    },
    "Distributor or Ignition Module Fault": {
      "Actual Issue": "Faulty distributor or ignition control module causing timing issues.",
      "Severity Level": "Medium — Causes timing problems and engine roughness; repair recommended to avoid damage.",
      "Possible Causes": [
        {"cause": "Wear and tear", "probability": 0.50},
        {"cause": "Moisture ingress", "probability": 0.30},
        {"cause": "Electrical faults", "probability": 0.20}
      ],
      "Diagnostics": [
        "Check ignition timing",
        "Scan for fault codes",
        "Visual inspection"
      ],
      "Fixes": [
        "Replace distributor cap/rotor or ignition module",
        "Repair wiring"
      ],
      "Temporary Solutions": [
        "Keep components dry",
        "Avoid driving in wet conditions"
      ]
    },
    "Coil-on-Plug (COP) System Issues": {
      "Actual Issue": "Failure of individual ignition coils directly mounted on spark plugs.",
      "Severity Level": "High — Coil failures cause cylinder misfires affecting performance and emissions.",
      "Possible Causes": [
        {"cause": "Coil failure", "probability": 0.60},
        {"cause": "Connector or wiring faults", "probability": 0.30},
        {"cause": "ECU issues", "probability": 0.10}
      ],
      "Diagnostics": [
        "Scan for cylinder-specific misfire codes",
        "Test coil resistance",
        "Check wiring and connectors"
      ],
      "Fixes": [
        "Replace faulty ignition coils",
        "Repair wiring/connectors"
      ],
      "Temporary Solutions": [
        "Drive gently",
        "Avoid high RPMs"
      ]
    }
  },
  "Air Conditioning System Issues": {
    "Refrigerant Leak": {
      "Actual Issue": "Leak in the A/C system causing loss of refrigerant and reduced cooling.",
      "Severity Level": "Medium — Causes reduced cooling efficiency and potential compressor damage if untreated.",
      "Possible Causes": [
        {"cause": "Worn or damaged hoses", "probability": 0.40},
        {"cause": "Leaking seals or O-rings", "probability": 0.30},
        {"cause": "Corroded condenser or evaporator", "probability": 0.20},
        {"cause": "Loose fittings", "probability": 0.10}
      ],
      "Diagnostics": [
        "Use UV dye and UV light to detect leaks",
        "Electronic leak detectors",
        "Pressure testing the system"
      ],
      "Fixes": [
        "Repair or replace leaking components",
        "Recharge refrigerant",
        "Replace damaged seals or hoses"
      ],
      "Temporary Solutions": [
        "Limit A/C use",
        "Avoid high ambient temperatures"
      ]
    },
    "Compressor Failure": {
      "Actual Issue": "A/C compressor seizes or fails to compress refrigerant effectively.",
      "Severity Level": "High — Compressor failure leads to total loss of A/C function; costly repairs required.",
      "Possible Causes": [
        {"cause": "Compressor wear", "probability": 0.50},
        {"cause": "Electrical faults", "probability": 0.25},
        {"cause": "Low refrigerant level", "probability": 0.15},
        {"cause": "Contamination inside system", "probability": 0.10}
      ],
      "Diagnostics": [
        "Check compressor clutch operation",
        "Measure system pressures",
        "Scan HVAC control module for codes"
      ],
      "Fixes": [
        "Replace or rebuild compressor",
        "Flush system",
        "Recharge refrigerant"
      ],
      "Temporary Solutions": [
        "Use A/C sparingly",
        "Avoid idling for long periods"
      ]
    },
    "Expansion Valve or Orifice Tube Blockage": {
      "Actual Issue": "Blockage causing restricted refrigerant flow and poor cooling.",
      "Severity Level": "Medium — Causes reduced cooling; if untreated may damage compressor.",
      "Possible Causes": [
        {"cause": "Debris or contamination", "probability": 0.70},
        {"cause": "Wear and corrosion", "probability": 0.30}
      ],
      "Diagnostics": [
        "Measure system pressures",
        "Inspect and replace valve or tube"
      ],
      "Fixes": [
        "Replace expansion valve or orifice tube",
        "Flush system"
      ],
      "Temporary Solutions": [
        "Limit A/C use",
        "Regular maintenance"
      ]
    },
    "Climate Control Module Failure": {
      "Actual Issue": "Fault in electronic climate control system causing erratic A/C or heating operation.",
      "Severity Level": "Low — Affects comfort and convenience but not safety.",
      "Possible Causes": [
        {"cause": "Software glitches", "probability": 0.50},
        {"cause": "Electrical faults", "probability": 0.30},
        {"cause": "Sensor failures", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan HVAC control module",
        "Check wiring and connectors",
        "Test sensors and actuators"
      ],
      "Fixes": [
        "Reprogram or replace control module",
        "Repair wiring",
        "Replace faulty sensors"
      ],
      "Temporary Solutions": [
        "Manual climate control if available",
        "Reset system by battery disconnect"
      ]
    }
  },
  "Hybrid and Electric Powertrain Issues": {
    "Hybrid Battery Degradation": {
      "Actual Issue": "Loss of capacity or failure of the high-voltage hybrid battery pack.",
      "Severity Level": "High — Reduced battery capacity impacts hybrid performance and range; replacement is expensive but critical.",
      "Possible Causes": [
        {"cause": "Battery cell aging", "probability": 0.60},
        {"cause": "Thermal stress", "probability": 0.30},
        {"cause": "Improper charging cycles", "probability": 0.10}
      ],
      "Diagnostics": [
        "Hybrid battery state of health (SOH) test",
        "Check hybrid system error codes",
        "Visual inspection for damage"
      ],
      "Fixes": [
        "Replace battery pack or modules",
        "Battery reconditioning (if supported)"
      ],
      "Temporary Solutions": [
        "Avoid heavy acceleration",
        "Keep battery charged appropriately"
      ]
    },
    "Regenerative Braking Failure": {
      "Actual Issue": "Malfunction of regenerative braking system reducing energy recovery and braking efficiency.",
      "Severity Level": "Medium — Affects efficiency and braking feel but conventional brakes remain functional.",
      "Possible Causes": [
        {"cause": "Faulty sensors", "probability": 0.50},
        {"cause": "Electrical faults in inverter or motor generator", "probability": 0.30},
        {"cause": "Software issues", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan hybrid control module",
        "Check sensor signals",
        "Test regenerative braking function"
      ],
      "Fixes": [
        "Repair or replace faulty sensors or components",
        "Update software"
      ],
      "Temporary Solutions": [
        "Drive gently",
        "Use conventional brakes carefully"
      ]
    },
    "Inverter or Power Electronics Failure": {
      "Actual Issue": "Failure of inverter or power electronics that manage high voltage flow to electric motors.",
      "Severity Level": "High — Causes loss of electric drive and potential safety risks; requires immediate repair.",
      "Possible Causes": [
        {"cause": "Component overheating", "probability": 0.50},
        {"cause": "Electrical faults", "probability": 0.30},
        {"cause": "Water ingress or contamination", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan inverter control module",
        "Inspect cooling system for inverter",
        "Visual inspection for damage"
      ],
      "Fixes": [
        "Replace inverter or power electronics",
        "Repair cooling system"
      ],
      "Temporary Solutions": [
        "Avoid high load driving",
        "Limit use of electric drive"
      ]
    }
  },
  "Fuel Injection System Issues": {
    "Clogged Fuel Injectors": {
      "Actual Issue": "Fuel injectors clogged or dirty, causing poor fuel atomization and engine performance.",
      "Severity Level": "Medium — Leads to rough running and decreased fuel efficiency; repair advised to prevent damage.",
      "Possible Causes": [
        {"cause": "Poor fuel quality", "probability": 0.40},
        {"cause": "Carbon deposits", "probability": 0.40},
        {"cause": "Contaminated fuel", "probability": 0.20}
      ],
      "Diagnostics": [
        "Fuel pressure test",
        "Injector balance test",
        "Scan for fault codes"
      ],
      "Fixes": [
        "Clean fuel injectors professionally",
        "Use fuel additives",
        "Replace faulty injectors"
      ],
      "Temporary Solutions": [
        "Use high-quality fuel",
        "Periodic fuel system cleaning"
      ]
    },
    "Fuel Pump Failure": {
      "Actual Issue": "Fuel pump fails to deliver required fuel pressure.",
      "Severity Level": "High — Engine may stall or fail to start; immediate repair necessary.",
      "Possible Causes": [
        {"cause": "Wear or electrical failure", "probability": 0.50},
        {"cause": "Clogged fuel filter", "probability": 0.30},
        {"cause": "Faulty relay or wiring", "probability": 0.20}
      ],
      "Diagnostics": [
        "Measure fuel pressure",
        "Check electrical supply to pump",
        "Inspect fuel filter"
      ],
      "Fixes": [
        "Replace fuel pump",
        "Replace fuel filter",
        "Repair wiring or relay"
      ],
      "Temporary Solutions": [
        "Avoid heavy acceleration",
        "Limit driving until fixed"
      ]
    }
  },
  "Common Rail Diesel Injector Issues": {
    "Actual Issue": "High-pressure injectors in diesel engines malfunction causing poor combustion.",
    "Severity Level": "High — Injector faults reduce engine power and increase emissions; repair essential.",
    "Possible Causes": [
      {"cause": "Injector nozzle clogging", "probability": 0.50},
      {"cause": "Electrical faults", "probability": 0.30},
      {"cause": "Poor fuel quality", "probability": 0.20}
    ],
    "Diagnostics": [
      "Injector balance and leakage test",
      "Scan diesel control module",
      "Fuel quality analysis"
    ],
    "Fixes": [
      "Replace or clean injectors",
      "Repair electrical faults"
    ],
    "Temporary Solutions": [
      "Use diesel additives",
      "Drive gently"
    ]
  },
  "EGR System Issues": {
    "Clogged EGR Valve": {
      "Actual Issue": "Carbon buildup causes EGR valve to stick or clog, leading to poor exhaust gas recirculation.",
      "Severity Level": "Medium — Causes rough idle and emissions issues; cleaning recommended.",
      "Possible Causes": [
        {"cause": "Carbon deposits from combustion", "probability": 0.70},
        {"cause": "Short trips not allowing full combustion temperature", "probability": 0.30}
      ],
      "Diagnostics": [
        "Scan for EGR-related codes (e.g., P0401)",
        "Inspect EGR valve and passages",
        "Test valve operation"
      ],
      "Fixes": [
        "Clean or replace EGR valve",
        "Use fuel additives to reduce carbon",
        "Improve driving habits"
      ],
      "Temporary Solutions": [
        "Avoid excessive idling",
        "Drive at highway speeds periodically"
      ]
    },
    "Faulty EGR Valve": {
      "Actual Issue": "EGR valve fails to open or close properly due to electrical or mechanical faults.",
      "Severity Level": "Medium — Causes emissions faults and engine performance issues; repair advised.",
      "Possible Causes": [
        {"cause": "Electrical failure", "probability": 0.50},
        {"cause": "Mechanical sticking", "probability": 0.30},
        {"cause": "Wiring or sensor issues", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan for EGR valve error codes",
        "Test valve electrical function",
        "Check wiring and connectors"
      ],
      "Fixes": [
        "Repair wiring",
        "Replace EGR valve"
      ],
      "Temporary Solutions": [
        "Drive gently",
        "Avoid stop-and-go traffic"
      ]
    }
  },
  "Turbocharger Issues": {
    "Turbo Lag or Slow Response": {
      "Actual Issue": "Delay in turbocharger boost build-up causing reduced engine responsiveness.",
      "Severity Level": "Medium — Reduces engine performance; repair needed to restore full power.",
      "Possible Causes": [
        {"cause": "Worn or sticking wastegate", "probability": 0.30},
        {"cause": "Boost leaks in intercooler or pipes", "probability": 0.30},
        {"cause": "Faulty turbo actuator", "probability": 0.20},
        {"cause": "Dirty or clogged turbo", "probability": 0.20}
      ],
      "Diagnostics": [
        "Check for boost leaks with smoke test",
        "Scan for turbo-related codes",
        "Inspect wastegate and actuator"
      ],
      "Fixes": [
        "Repair boost leaks",
        "Replace faulty actuator",
        "Clean or rebuild turbocharger"
      ],
      "Temporary Solutions": [
        "Drive gently",
        "Avoid aggressive acceleration"
      ]
    },
    "Turbocharger Noise or Whine": {
      "Actual Issue": "Unusual noises from turbocharger indicating wear or damage.",
      "Severity Level": "High — Turbo failure can lead to major engine damage; immediate attention required.",
      "Possible Causes": [
        {"cause": "Worn bearings", "probability": 0.50},
        {"cause": "Damaged compressor or turbine blades", "probability": 0.30},
        {"cause": "Insufficient lubrication", "probability": 0.20}
      ],
      "Diagnostics": [
        "Listen for abnormal turbo noises",
        "Inspect turbocharger shaft play",
        "Check oil supply"
      ],
      "Fixes": [
        "Rebuild or replace turbocharger",
        "Fix oil supply issues"
      ],
      "Temporary Solutions": [
        "Avoid high RPMs",
        "Monitor oil levels"
      ]
    }
  },
    "Variable Geometry Turbo (VGT) Failure": {
    "Actual Issue": "Failure of variable vanes mechanism causing loss of boost control.",
    "Severity Level": "High — Loss of boost control leads to reduced engine power and possible engine damage; urgent repair needed.",
    "Possible Causes": [
      {"cause": "Carbon buildup causing vane sticking", "probability": 0.50},
      {"cause": "Faulty VGT actuator", "probability": 0.30},
      {"cause": "Electrical faults", "probability": 0.20}
    ],
    "Diagnostics": [
      "Scan for VGT fault codes",
      "Inspect and clean VGT mechanism",
      "Test actuator operation"
    ],
    "Fixes": [
      "Clean or replace VGT vanes",
      "Replace actuator",
      "Repair wiring"
    ],
    "Temporary Solutions": [
      "Drive gently",
      "Avoid prolonged high load"
    ]
  },

  "Drivetrain System Issues": {
    "CV Joint Wear or Failure": {
      "Actual Issue": "Constant velocity (CV) joints wear or fail causing vibration and noise.",
      "Severity Level": "High — Failed CV joints can cause loss of drive and unsafe vibrations; repair promptly.",
      "Possible Causes": [
        {"cause": "Torn or damaged CV boot allowing dirt ingress", "probability": 0.50},
        {"cause": "Normal wear", "probability": 0.30},
        {"cause": "Lack of lubrication", "probability": 0.20}
      ],
      "Diagnostics": [
        "Visual inspection of CV boots",
        "Check for play in CV joints",
        "Test drive for noises"
      ],
      "Fixes": [
        "Replace CV boots if damaged",
        "Replace CV joint or axle shaft if worn"
      ],
      "Temporary Solutions": [
        "Drive gently",
        "Avoid sharp turns"
      ]
    },
    "Differential Fluid Leak": {
      "Actual Issue": "Leakage of lubricant from differential causing poor lubrication and noise.",
      "Severity Level": "High — Fluid loss can cause differential failure; needs urgent repair.",
      "Possible Causes": [
        {"cause": "Worn seals or gaskets", "probability": 0.40},
        {"cause": "Damaged differential cover", "probability": 0.30},
        {"cause": "Overfilled or underfilled fluid", "probability": 0.30}
      ],
      "Diagnostics": [
        "Visual inspection for leaks",
        "Check differential fluid level",
        "Listen for abnormal noises"
      ],
      "Fixes": [
        "Replace seals or gaskets",
        "Repair or replace cover",
        "Change differential fluid"
      ],
      "Temporary Solutions": [
        "Avoid heavy loads",
        "Drive carefully"
      ]
    },
    "All-Wheel Drive (AWD) System Malfunction": {
      "Actual Issue": "Faults in AWD system causing improper torque distribution.",
      "Severity Level": "High — AWD faults can reduce traction and safety; repair promptly.",
      "Possible Causes": [
        {"cause": "Faulty transfer case", "probability": 0.40},
        {"cause": "Damaged electronic control units", "probability": 0.40},
        {"cause": "Sensor failures", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan AWD control module for errors",
        "Inspect transfer case and sensors",
        "Test torque distribution"
      ],
      "Fixes": [
        "Repair or replace faulty components",
        "Reprogram control units"
      ],
      "Temporary Solutions": [
        "Drive cautiously",
        "Avoid off-road conditions"
      ]
    },
    "Driveshaft Imbalance or Damage": {
      "Actual Issue": "Bent or imbalanced driveshaft causing vibration and noise.",
      "Severity Level": "Medium — Vibration affects comfort and may cause damage; repair recommended.",
      "Possible Causes": [
        {"cause": "Physical impact", "probability": 0.40},
        {"cause": "Wear of universal joints", "probability": 0.40},
        {"cause": "Corrosion", "probability": 0.20}
      ],
      "Diagnostics": [
        "Visual inspection",
        "Check universal joint play",
        "Test drive for vibration"
      ],
      "Fixes": [
        "Balance or replace driveshaft",
        "Replace universal joints"
      ],
      "Temporary Solutions": [
        "Drive carefully",
        "Avoid rough terrain"
      ]
    }
  },

  "Cooling System Issues": {
    "Coolant Leak": {
      "Actual Issue": "Loss of coolant due to leaks causing engine overheating.",
      "Severity Level": "High — Overheating can cause severe engine damage; immediate repair required.",
      "Possible Causes": [
        {"cause": "Damaged hoses or radiator", "probability": 0.40},
        {"cause": "Faulty water pump seal", "probability": 0.30},
        {"cause": "Leaking heater core", "probability": 0.20},
        {"cause": "Loose hose clamps", "probability": 0.10}
      ],
      "Diagnostics": [
        "Pressure test cooling system",
        "Visual inspection",
        "Check coolant level and condition"
      ],
      "Fixes": [
        "Repair or replace leaking components",
        "Refill coolant",
        "Tighten clamps"
      ],
      "Temporary Solutions": [
        "Avoid heavy engine load",
        "Monitor temperature gauge"
      ]
    },
    "Electric Water Pump Failure": {
      "Actual Issue": "Failure of electric water pump in modern cooling systems causing overheating.",
      "Severity Level": "High — Pump failure causes overheating; urgent repair required.",
      "Possible Causes": [
        {"cause": "Electrical failure", "probability": 0.50},
        {"cause": "Pump wear", "probability": 0.30},
        {"cause": "Control module fault", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan for fault codes",
        "Check pump electrical supply",
        "Visual inspection"
      ],
      "Fixes": [
        "Replace electric water pump",
        "Repair wiring or control module"
      ],
      "Temporary Solutions": [
        "Avoid heavy loads",
        "Drive gently"
      ]
    },
    "Thermostat Stuck Open or Closed": {
      "Actual Issue": "Thermostat malfunction causing poor temperature regulation.",
      "Severity Level": "Medium — Poor cooling or overheating affects engine efficiency; repair recommended.",
      "Possible Causes": [
        {"cause": "Thermostat wear or corrosion", "probability": 0.70},
        {"cause": "Mechanical failure", "probability": 0.30}
      ],
      "Diagnostics": [
        "Check coolant temperature",
        "Test thermostat operation"
      ],
      "Fixes": [
        "Replace thermostat"
      ],
      "Temporary Solutions": [
        "Drive gently",
        "Avoid heavy loads"
      ]
    },
    "Radiator Fan Failure": {
      "Actual Issue": "Radiator fan not operating properly leading to overheating at idle or low speeds.",
      "Severity Level": "High — Causes overheating risk during idle or slow traffic; urgent repair advised.",
      "Possible Causes": [
        {"cause": "Faulty fan motor", "probability": 0.50},
        {"cause": "Blown fuse or relay", "probability": 0.30},
        {"cause": "Sensor or control module failure", "probability": 0.20}
      ],
      "Diagnostics": [
        "Test fan motor and wiring",
        "Check fuses and relays",
        "Scan for fan control errors"
      ],
      "Fixes": [
        "Replace fan motor",
        "Repair wiring",
        "Replace fuses or relays"
      ],
      "Temporary Solutions": [
        "Avoid idling for long periods",
        "Drive at higher speeds to increase airflow"
      ]
    }
  },

  "Suspension System Issues": {
    "Worn Shock Absorbers or Struts": {
      "Actual Issue": "Shock absorbers or struts worn causing poor ride quality and handling.",
      "Severity Level": "Medium — Affects comfort and vehicle control; repair advised to maintain safety.",
      "Possible Causes": [
        {"cause": "Normal wear and tear", "probability": 0.60},
        {"cause": "Fluid leaks", "probability": 0.30},
        {"cause": "Physical damage", "probability": 0.10}
      ],
      "Diagnostics": [
        "Visual inspection for leaks",
        "Bounce test",
        "Check tire wear patterns"
      ],
      "Fixes": [
        "Replace shocks or struts"
      ],
      "Temporary Solutions": [
        "Drive cautiously",
        "Avoid rough roads"
      ]
    },
    "Broken or Worn Suspension Bushings": {
      "Actual Issue": "Bushings worn or broken causing noise and poor suspension performance.",
      "Severity Level": "Medium — Causes noise and affects handling; replacement recommended.",
      "Possible Causes": [
        {"cause": "Age and wear", "probability": 0.70},
        {"cause": "Road impacts", "probability": 0.30}
      ],
      "Diagnostics": [
        "Visual inspection",
        "Check suspension play"
      ],
      "Fixes": [
        "Replace worn bushings"
      ],
      "Temporary Solutions": [
        "Drive carefully"
      ]
    },
    "Adaptive Suspension Failure": {
      "Actual Issue": "Malfunction of electronically controlled suspension systems affecting ride and handling.",
      "Severity Level": "Medium — Reduces suspension effectiveness; repair needed to restore performance.",
      "Possible Causes": [
        {"cause": "Sensor failure", "probability": 0.40},
        {"cause": "Electrical faults", "probability": 0.40},
        {"cause": "Damaged actuators", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan suspension control module",
        "Test sensors and actuators",
        "Check wiring"
      ],
      "Fixes": [
        "Repair or replace faulty components",
        "Reprogram control module"
      ],
      "Temporary Solutions": [
        "Drive cautiously",
        "Avoid rough terrain"
      ]
    }
  },

  "Driver Assistance Systems Issues": {
    "Lane Keep Assist Malfunction": {
      "Actual Issue": "Failure in lane-keeping assist system causing intermittent or no lane corrections.",
      "Severity Level": "Medium — Affects driver assistance but manual control remains; caution advised.",
      "Possible Causes": [
        {"cause": "Dirty or blocked cameras/sensors", "probability": 0.40},
        {"cause": "Software glitches", "probability": 0.30},
        {"cause": "Faulty steering actuator", "probability": 0.20},
        {"cause": "Electrical wiring issues", "probability": 0.10}
      ],
      "Diagnostics": [
        "Scan ADAS control unit for error codes",
        "Inspect cameras and sensors",
        "Test actuator response"
      ],
      "Fixes": [
        "Clean or replace cameras/sensors",
        "Update or reflash software",
        "Repair wiring or replace actuators"
      ],
      "Temporary Solutions": [
        "Drive cautiously",
        "Disable system if unreliable"
      ]
    },
    "Adaptive Cruise Control (ACC) Fault": {
      "Actual Issue": "Malfunction in ACC system affecting speed and distance control.",
      "Severity Level": "Medium — Affects automated speed control; manual control remains.",
      "Possible Causes": [
        {"cause": "Radar sensor obstruction or damage", "probability": 0.50},
        {"cause": "Software errors", "probability": 0.30},
        {"cause": "Electrical faults", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan ACC control module",
        "Inspect radar sensor",
        "Check wiring and connections"
      ],
      "Fixes": [
        "Clean or replace radar sensor",
        "Update software",
        "Repair wiring"
      ],
      "Temporary Solutions": [
        "Use manual cruise control",
        "Drive cautiously"
      ]
    },
    "Blind Spot Monitor Failure": {
      "Actual Issue": "Blind spot detection system not functioning properly.",
      "Severity Level": "Low — Reduces driver awareness aid; driver must be more vigilant.",
      "Possible Causes": [
        {"cause": "Sensor damage or blockage", "probability": 0.50},
        {"cause": "Electrical wiring issues", "probability": 0.30},
        {"cause": "Software glitches", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan relevant control modules",
        "Inspect sensors for damage or dirt",
        "Check wiring"
      ],
      "Fixes": [
        "Clean or replace sensors",
        "Repair wiring",
        "Update software"
      ],
      "Temporary Solutions": [
        "Use mirrors carefully",
        "Disable system if unreliable"
      ]
    }
  },

  "Infotainment System Issues": {
    "Touchscreen Unresponsive": {
      "Actual Issue": "Touchscreen does not respond to inputs due to software or hardware faults.",
      "Severity Level": "Low — Affects convenience but not vehicle safety.",
      "Possible Causes": [
        {"cause": "Software glitches", "probability": 0.50},
        {"cause": "Hardware failure", "probability": 0.30},
        {"cause": "Loose connections", "probability": 0.20}
      ],
      "Diagnostics": [
        "Perform system reset",
        "Check for software updates",
        "Inspect wiring connections"
      ],
      "Fixes": [
        "Update or reinstall software",
        "Repair or replace touchscreen hardware",
        "Secure wiring connections"
      ],
      "Temporary Solutions": [
        "Use physical buttons or voice commands",
        "Restart system"
      ]
    },
    "Bluetooth Connectivity Issues": {
      "Actual Issue": "Problems pairing or maintaining connection with Bluetooth devices.",
      "Severity Level": "Low — Affects convenience but does not affect driving safety.",
      "Possible Causes": [
        {"cause": "Software bugs", "probability": 0.50},
        {"cause": "Interference from other devices", "probability": 0.30},
        {"cause": "Outdated firmware", "probability": 0.20}
      ],
      "Diagnostics": [
        "Check device compatibility",
        "Update infotainment system firmware",
        "Reset Bluetooth settings"
      ],
      "Fixes": [
        "Update software",
        "Clear paired devices and re-pair",
        "Repair wiring if hardware issue"
      ],
      "Temporary Solutions": [
        "Use auxiliary input or USB",
        "Minimize device interference"
      ]
    },
    "Navigation System Malfunction": {
      "Actual Issue": "Navigation system fails to provide correct directions or map data.",
      "Severity Level": "Low — Affects convenience; alternative navigation methods should be used.",
      "Possible Causes": [
        {"cause": "Outdated map data", "probability": 0.50},
        {"cause": "Software bugs", "probability": 0.30},
        {"cause": "GPS signal loss", "probability": 0.20}
      ],
      "Diagnostics": [
        "Check GPS signal strength",
        "Update map software",
        "Perform system reset"
      ],
      "Fixes": [
        "Update maps and software",
        "Repair GPS antenna or wiring",
        "Reinstall navigation software"
      ],
      "Temporary Solutions": [
        "Use smartphone navigation apps",
        "Drive cautiously"
      ]
    }
  },

  "Lighting System Issues": {
    "Headlight Failure (Halogen, HID, LED)": {
      "Actual Issue": "One or both headlights stop working due to bulb, wiring, or control module issues.",
      "Severity Level": "High — Reduces night driving visibility and safety; urgent repair needed.",
      "Possible Causes": [
        {"cause": "Blown bulb (halogen)", "probability": 0.50},
        {"cause": "Ballast or igniter failure (HID)", "probability": 0.20},
        {"cause": "LED module failure", "probability": 0.15},
        {"cause": "Wiring or fuse issues", "probability": 0.15}
      ],
      "Diagnostics": [
        "Inspect bulbs and connections",
        "Check fuses and relays",
        "Scan for lighting control module errors"
      ],
      "Fixes": [
        "Replace bulb, ballast, or LED module",
        "Repair wiring or connectors",
        "Replace fuse or relay"
      ],
      "Temporary Solutions": [
        "Use high beams temporarily (if legal/safe)",
        "Avoid night driving"
      ]
    },
    "Adaptive Headlight Malfunction": {
      "Actual Issue": "Adaptive headlights fail to adjust beam direction or level properly.",
      "Severity Level": "Medium — Reduces headlight effectiveness; repair recommended.",
      "Possible Causes": [
        {"cause": "Faulty headlight leveling sensor", "probability": 0.45},
        {"cause": "Steering angle sensor issues", "probability": 0.35},
        {"cause": "Control module failure", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan headlight control module",
        "Check sensor calibration",
        "Test motorized adjustment"
      ],
      "Fixes": [
        "Replace faulty sensors",
        "Reprogram or reset system",
        "Repair wiring"
      ],
      "Temporary Solutions": [
        "Disable adaptive feature (if possible)",
        "Manually adjust headlight alignment"
      ]
    }
  },

  "Interior Lighting Malfunction": {
    "Actual Issue": "Cabin lights fail or behave erratically.",
    "Severity Level": "Low — Affects convenience but not critical for vehicle operation.",
    "Possible Causes": [
      {"cause": "Faulty door switches", "probability": 0.40},
      {"cause": "Wiring issues", "probability": 0.35},
      {"cause": "Control module fault", "probability": 0.25}
    ],
    "Diagnostics": [
      "Check door switch operation",
      "Inspect wiring and grounds",
      "Scan for BCM (Body Control Module) errors"
    ],
    "Fixes": [
      "Replace door switch or faulty bulbs",
      "Repair wiring",
      "Reflash or replace BCM"
    ],
    "Temporary Solutions": [
      "Manually turn off cabin lights",
      "Use flashlight as backup"
    ]
  },

  "TPMS (Tire Pressure Monitoring System) Issues": {
    "TPMS Warning Light On": {
      "Actual Issue": "System detects one or more tires with incorrect pressure or faulty sensor.",
      "Severity Level": "Medium — Alerts driver to potential tire pressure issues that can affect safety and fuel efficiency; prompt check recommended.",
      "Possible Causes": [
        {"cause": "Low or high tire pressure", "probability": 0.50},
        {"cause": "Temperature change affecting pressure", "probability": 0.20},
        {"cause": "Faulty or dead TPMS sensor battery", "probability": 0.20},
        {"cause": "Incorrect tire size or rotation", "probability": 0.10}
      ],
      "Diagnostics": [
        "Check tire pressures manually with gauge",
        "Scan TPMS module for fault codes",
        "Use TPMS scan tool to check sensor status"
      ],
      "Fixes": [
        "Adjust tire pressure to recommended levels",
        "Replace faulty sensors",
        "Relearn/reset TPMS system"
      ],
      "Temporary Solutions": [
        "Monitor tire pressure manually",
        "Ignore warning if pressure is verified and safe"
      ]
    },
    "TPMS Sensor Not Communicating": {
      "Actual Issue": "One or more tire sensors fail to transmit data to vehicle’s TPMS receiver.",
      "Severity Level": "Medium — Loss of sensor data reduces TPMS functionality; manual pressure checks needed until repair.",
      "Possible Causes": [
        {"cause": "Dead sensor battery (common after 5–10 years)", "probability": 0.60},
        {"cause": "Sensor damage during tire change", "probability": 0.25},
        {"cause": "Receiver module or antenna fault", "probability": 0.15}
      ],
      "Diagnostics": [
        "TPMS scan tool to check sensor battery and signal",
        "Scan vehicle for DTCs",
        "Inspect sensor placement and condition"
      ],
      "Fixes": [
        "Replace non-communicating sensor",
        "Repair or replace TPMS receiver if needed"
      ],
      "Temporary Solutions": [
        "Use external tire pressure monitor",
        "Check pressures regularly with gauge"
      ]
    },
    "Indirect TPMS False Alarm": {
      "Actual Issue": "ABS-based system misinterprets tire rotation speed as a pressure issue.",
      "Severity Level": "Low — False alarms do not indicate real safety issues but can cause driver distraction.",
      "Possible Causes": [
        {"cause": "Uneven tire wear", "probability": 0.45},
        {"cause": "Tire replacement without recalibration", "probability": 0.35},
        {"cause": "System not reset after tire service", "probability": 0.20}
      ],
      "Diagnostics": [
        "Inspect tire tread depth and wear",
        "Check calibration/reset history",
        "Scan ABS/TPMS modules"
      ],
      "Fixes": [
        "Reset/recalibrate indirect TPMS",
        "Ensure tires are evenly worn and properly matched"
      ],
      "Temporary Solutions": [
        "Ignore if pressure verified",
        "Perform manual resets regularly"
      ]
    }
  },

  "Braking System Issues": {
    "Worn Brake Pads or Rotors": {
      "Actual Issue": "Brake pads or rotors worn down causing poor braking performance and noise.",
      "Severity Level": "High — Reduced braking efficiency and increased stopping distances compromise safety; prompt replacement needed.",
      "Possible Causes": [
        {"cause": "Normal wear and tear", "probability": 0.60},
        {"cause": "Driving in harsh conditions", "probability": 0.25},
        {"cause": "Poor-quality parts", "probability": 0.15}
      ],
      "Diagnostics": [
        "Inspect pad thickness and rotor condition",
        "Measure rotor runout",
        "Check brake fluid level"
      ],
      "Fixes": [
        "Replace brake pads and/or rotors",
        "Resurface rotors (if within spec)"
      ],
      "Temporary Solutions": [
        "Drive cautiously",
        "Avoid sudden braking"
      ]
    },
    "ABS System Malfunction": {
      "Actual Issue": "Anti-lock braking system not working properly, reducing stability during emergency braking.",
      "Severity Level": "High — ABS failure increases risk of wheel lockup and loss of control under heavy braking; repair urgently required.",
      "Possible Causes": [
        {"cause": "Faulty ABS sensor or tone ring", "probability": 0.50},
        {"cause": "Damaged wiring", "probability": 0.30},
        {"cause": "Failed ABS module", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan ABS control module for fault codes",
        "Inspect wheel speed sensors",
        "Check ABS fuse and wiring"
      ],
      "Fixes": [
        "Replace faulty ABS sensors",
        "Repair wiring",
        "Replace or reprogram ABS module"
      ],
      "Temporary Solutions": [
        "Drive more cautiously in wet/icy conditions",
        "Manually modulate braking if necessary"
      ]
    },
    "Electronic Parking Brake (EPB) Failure": {
      "Actual Issue": "EPB fails to engage or disengage properly, sometimes locking the vehicle unexpectedly.",
      "Severity Level": "High — EPB malfunction can cause vehicle immobilization or unsafe conditions; repair promptly.",
      "Possible Causes": [
        {"cause": "Stuck actuator motor", "probability": 0.50},
        {"cause": "Software error", "probability": 0.30},
        {"cause": "Faulty switch or wiring", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan EPB module for errors",
        "Check actuator movement",
        "Test switch and circuit"
      ],
      "Fixes": [
        "Replace or reset actuator",
        "Repair wiring",
        "Update or reset software"
      ],
      "Temporary Solutions": [
        "Use gear position (P or low gear) to hold vehicle",
        "Manually override brake if supported"
      ]
    },
    "Automatic Emergency Braking (AEB) False Activation": {
      "Actual Issue": "AEB system applies brakes unexpectedly due to sensor misinterpretation.",
      "Severity Level": "Medium — Unexpected braking can be hazardous; driver must remain alert until fixed.",
      "Possible Causes": [
        {"cause": "Dirty or misaligned front radar/camera", "probability": 0.50},
        {"cause": "Software bugs", "probability": 0.30},
        {"cause": "Environmental reflections (e.g. sunlight, water)", "probability": 0.20}
      ],
      "Diagnostics": [
        "Inspect and clean sensors",
        "Scan ADAS system for codes",
        "Check calibration status"
      ],
      "Fixes": [
        "Calibrate or align sensors",
        "Update AEB software",
        "Replace faulty sensor"
      ],
      "Temporary Solutions": [
        "Disable AEB in settings (if allowed)",
        "Drive cautiously with extra space"
      ]
    }
  },

  "Steering System Issues": {
    "Electric Power Steering (EPS) Failure": {
      "Actual Issue": "EPS system fails, leading to loss or reduction of steering assist.",
      "Severity Level": "High — Increased steering effort and reduced control at low speeds; immediate attention advised.",
      "Possible Causes": [
        {"cause": "Faulty EPS motor or control module", "probability": 0.40},
        {"cause": "Sensor failure (torque, angle, speed sensors)", "probability": 0.30},
        {"cause": "Electrical issues (wiring, connectors, fuses)", "probability": 0.20},
        {"cause": "Overheated EPS from excessive use (e.g., frequent tight maneuvers)", "probability": 0.10}
      ],
      "Diagnostics": [
        "Scan steering module for error codes",
        "Check voltage supply and ground",
        "Test motor operation and steering sensors"
      ],
      "Fixes": [
        "Replace faulty EPS motor or ECU",
        "Repair or replace wiring/connectors",
        "Reprogram or reset EPS control module"
      ],
      "Temporary Solutions": [
        "Shut off and restart engine to reset system",
        "Avoid tight turns until fixed",
        "Drive cautiously with extra steering effort"
      ]
    },
    "Steering Rack or Gearbox Problems": {
      "Actual Issue": "Wear or failure in steering rack causes poor control or abnormal noises.",
      "Severity Level": "High — Poor steering response and potential safety hazard; repair necessary.",
      "Possible Causes": [
        {"cause": "Wear in internal components", "probability": 0.50},
        {"cause": "Fluid contamination (in hydraulic systems)", "probability": 0.30},
        {"cause": "Loose mounts or joints", "probability": 0.20}
      ],
      "Diagnostics": [
        "Inspect for steering play",
        "Check rack mounts and bushings",
        "Test for fluid leaks (if hydraulic)"
      ],
      "Fixes": [
        "Replace or rebuild steering rack",
        "Tighten or replace mounts",
        "Flush fluid (if hydraulic)"
      ],
      "Temporary Solutions": [
        "Drive carefully at lower speeds",
        "Avoid rough or uneven roads"
      ]
    },
    "Steering Angle Sensor Fault": {
      "Actual Issue": "Sensor misreads steering input, affecting systems like ESP, lane-keep assist, and EPS.",
      "Severity Level": "Medium — May cause malfunction of driver assistance systems; manual driving remains possible.",
      "Possible Causes": [
        {"cause": "Sensor misalignment", "probability": 0.40},
        {"cause": "Sensor failure or poor calibration", "probability": 0.35},
        {"cause": "Electrical faults", "probability": 0.25}
      ],
      "Diagnostics": [
        "Scan for steering angle sensor codes",
        "Check sensor values while steering",
        "Verify calibration status"
      ],
      "Fixes": [
        "Recalibrate steering angle sensor",
        "Replace sensor",
        "Repair wiring or module"
      ],
      "Temporary Solutions": [
        "Disable related driver assistance features",
        "Drive cautiously — avoid reliance on assists"
      ]
    }
  },

  "Engine Timing System Issues": {
    "Timing Belt or Chain Wear/Failure": {
      "Actual Issue": "Worn or broken timing belt/chain leads to loss of synchronization between camshaft and crankshaft.",
      "Severity Level": "Critical — Risk of catastrophic engine damage; immediate stop and repair required.",
      "Possible Causes": [
        {"cause": "Age and wear (belt: ~60,000–100,000 km / chain: ~150,000–250,000 km)", "probability": 0.60},
        {"cause": "Poor lubrication (for chain)", "probability": 0.25},
        {"cause": "Tensioner or guide failure", "probability": 0.15}
      ],
      "Diagnostics": [
        "Listen for timing noises",
        "Check belt/chain condition (visual or borescope)",
        "Scan for cam/crank position codes (e.g., P0016, P0017)"
      ],
      "Fixes": [
        "Replace timing belt/chain and tensioners",
        "Inspect and replace pulleys and guides",
        "Reset timing alignment marks"
      ],
      "Temporary Solutions": [
        "None — risk of catastrophic engine damage",
        "Stop driving immediately if noise or misalignment is suspected"
      ]
    }
  },

  "Engine Timing & Lubrication": {
    "Variable Valve Timing (VVT) System Failure": {
      "Actual Issue": "VVT system fails to properly adjust valve timing, affecting performance and efficiency.",
      "Severity Level": "High — Reduces engine performance and may cause damage if oil issues persist; repair advised.",
      "Possible Causes": [
        {"cause": "Dirty or low engine oil", "probability": 0.50},
        {"cause": "Faulty VVT solenoid or oil control valve", "probability": 0.30},
        {"cause": "Timing chain stretch or phaser wear", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan for VVT-specific codes",
        "Check oil level and cleanliness",
        "Test VVT solenoid operation"
      ],
      "Fixes": [
        "Clean or replace VVT solenoid",
        "Change engine oil and filter",
        "Replace cam phasers or timing chain if worn"
      ],
      "Temporary Solutions": [
        "Avoid hard acceleration",
        "Change oil immediately if old or dirty"
      ]
    },
    "Timing Tensioner or Guide Failure": {
      "Actual Issue": "Hydraulic or spring-loaded tensioner fails, causing slack in chain/belt and noise or misalignment.",
      "Severity Level": "High — Slack can cause timing failure and engine damage; repair promptly.",
      "Possible Causes": [
        {"cause": "Oil pressure issues (hydraulic tensioners)", "probability": 0.40},
        {"cause": "Wear and fatigue", "probability": 0.40},
        {"cause": "Broken plastic guides", "probability": 0.20}
      ],
      "Diagnostics": [
        "Visual/aural inspection for noise",
        "Timing inspection during disassembly",
        "Oil pressure test (for hydraulic units)"
      ],
      "Fixes": [
        "Replace tensioner and guides",
        "Flush oil system if debris found"
      ],
      "Temporary Solutions": [
        "Avoid high RPM driving",
        "Limit engine use until repaired"
      ]
    }
  },

  "Engine Lubrication System Issues": {
    "Low Engine Oil Pressure": {
      "Actual Issue": "Insufficient oil pressure can lead to engine damage due to lack of lubrication.",
      "Severity Level": "Critical — Immediate risk of severe engine damage; check and repair urgently.",
      "Possible Causes": [
        {"cause": "Low oil level", "probability": 0.40},
        {"cause": "Worn oil pump", "probability": 0.30},
        {"cause": "Clogged oil pickup screen or filter", "probability": 0.20},
        {"cause": "Excessive bearing or lifter clearance", "probability": 0.10}
      ],
      "Diagnostics": [
        "Check oil level and condition",
        "Use mechanical gauge to verify actual oil pressure",
        "Inspect for sludge buildup or pump wear"
      ],
      "Fixes": [
        "Top off or change oil",
        "Replace oil pump or clogged filter",
        "Repair worn internal engine components"
      ],
      "Temporary Solutions": [
        "Use thicker oil as a stopgap (if safe)",
        "Avoid high RPM and load"
      ]
    },
    "Oil Leaks": {
      "Actual Issue": "External oil leaks reduce oil level and can damage other components or cause fire risk.",
      "Severity Level": "Medium — Needs repair to prevent further damage or hazards; may cause engine issues if severe.",
      "Possible Causes": [
        {"cause": "Worn valve cover gasket, oil pan gasket, or main seals", "probability": 0.60},
        {"cause": "Cracked oil filter housing or lines", "probability": 0.25},
        {"cause": "Improperly installed drain plug or filter", "probability": 0.15}
      ],
      "Diagnostics": [
        "Visual inspection under car and around engine",
        "UV dye leak test",
        "Pressure test or steam clean for confirmation"
      ],
      "Fixes": [
        "Replace leaking gaskets or seals",
        "Tighten or replace drain plug/filter",
        "Use high-temp RTV (in minor cases)"
      ],
      "Temporary Solutions": [
        "Monitor and top off oil regularly",
        "Use oil stop-leak additive (not long-term safe)"
      ]
    },
    "Oil Sludge Buildup": {
      "Actual Issue": "Sludge restricts oil flow and causes overheating and wear.",
      "Severity Level": "High — Leads to poor lubrication and engine damage if untreated; thorough cleaning required.",
      "Possible Causes": [
        {"cause": "Infrequent oil changes", "probability": 0.50},
        {"cause": "Cheap or wrong oil type", "probability": 0.30},
        {"cause": "High engine heat or short trips only", "probability": 0.20}
      ],
      "Diagnostics": [
        "Inspect under valve cover or oil cap",
        "Check oil filter for clogging",
        "Oil analysis (optional)"
      ],
      "Fixes": [
        "Use engine flush additive before oil change",
        "Perform multiple short oil changes with quality oil",
        "Disassemble and manually clean (severe cases)"
      ],
      "Temporary Solutions": [
        "Use high-detergent synthetic oil",
        "Change oil more frequently"
      ]
    },
    "Electronic Oil Pressure Sensor Failure": {
      "Actual Issue": "False low pressure readings from faulty sensor, triggering warning lights without real issue.",
      "Severity Level": "Low — Sensor fault does not impact engine but may cause false alarms; verify with manual gauge.",
      "Possible Causes": [
        {"cause": "Sensor wear or contamination", "probability": 0.50},
        {"cause": "Electrical connector issues", "probability": 0.30},
        {"cause": "Short circuits", "probability": 0.20}
      ],
      "Diagnostics": [
        "Scan for fault codes",
        "Compare sensor reading to manual gauge",
        "Inspect wiring and connector"
      ],
      "Fixes": [
        "Replace oil pressure sensor",
        "Repair connector or wiring"
      ],
      "Temporary Solutions": [
        "Verify oil level and continue driving cautiously if mechanical pressure is confirmed"
      ]
    }
  },

  "Suspension Issues": {
    "Knocking on Bumps": {
      "Severity Level": "Medium — Causes noise and may indicate worn suspension components; repair advised to maintain comfort and safety.",
      "Possible Causes": [
        {"cause": "Worn shocks or struts", "probability": 0.70},
        {"cause": "Worn ball joint", "probability": 0.30}
      ],
      "Fixes": [
        "Replace worn parts"
      ]
    },
    "Car Bounces After Bumps": {
      "Severity Level": "Medium — Reduced damping performance affects ride comfort and control; repair recommended.",
      "Possible Causes": [
        {"cause": "Worn shocks", "probability": 0.60},
        {"cause": "Slipped/damaged leaf spring", "probability": 0.40}
      ],
      "Fixes": [
        "Replace or repair shocks/springs"
      ]
    }
    }
    }
    }
    }
obd_ii_codes = {
    
"P0300": {
  "Actual Issue": "Random/Multiple Cylinder Misfire Detected",
  "Severity": "High (Can cause catalytic converter damage and engine damage if untreated)",
  "Possible Causes": [
    {"cause": "Faulty spark plugs or ignition coils", "probability": 0.40},
    {"cause": "Fuel delivery problem", "probability": 0.35},
    {"cause": "Compression issues", "probability": 0.25}
  ],
  "Symptoms": [
    "Rough idling",
    "Engine shaking",
    "Increased emissions"
  ],
  "Diagnostics": [
    "Inspect spark plugs and ignition coils",
    "Check fuel system operation",
    "Perform compression test"
  ],
  "Fixes": [
    "Replace spark plugs or ignition coils",
    "Repair fuel delivery issues",
    "Address compression problems"
  ],
  "Temporary Solutions": [
    "Drive gently to avoid engine damage",
    "Avoid heavy loads or acceleration"
  ]
},

"P0301": {
  "Actual Issue": "Cylinder 1 Misfire Detected",
  "Severity": "High (Single cylinder misfire risks engine damage and increased emissions)",
  "Possible Causes": [
    {"cause": "Faulty spark plug in cylinder 1", "probability": 0.40},
    {"cause": "Bad ignition coil", "probability": 0.30},
    {"cause": "Fuel injector issue", "probability": 0.20},
    {"cause": "Compression problem", "probability": 0.10}
  ],
  "Symptoms": [
    "Rough idle",
    "Poor acceleration",
    "Engine hesitation",
    "Check engine light"
  ],
  "Diagnostics": [
    "Check spark plug and ignition coil in cylinder 1",
    "Test fuel injector operation",
    "Perform compression test on cylinder 1"
  ],
  "Fixes": [
    "Replace spark plug or coil in cylinder 1",
    "Repair or replace fuel injector",
    "Fix compression issues"
  ],
  "Temporary Solutions": [
    "Avoid aggressive driving",
    "Drive gently until repaired"
  ]
},

"P0302": {
  "Actual Issue": "Cylinder 2 Misfire Detected",
  "Severity": "High (Misfires can cause engine damage, catalytic converter harm, and poor drivability)",
  "Possible Causes": [
    {"cause": "Worn spark plug in cylinder 2", "probability": 0.40},
    {"cause": "Coil pack failure", "probability": 0.30},
    {"cause": "Injector blockage", "probability": 0.20},
    {"cause": "Burnt valve or head gasket leak", "probability": 0.10}
  ],
  "Symptoms": [
    "Shaking engine",
    "Reduced power",
    "Illuminated check engine light"
  ],
  "Diagnostics": [
    "Inspect spark plug and coil pack in cylinder 2",
    "Check and clean injector",
    "Perform compression and leak-down tests"
  ],
  "Fixes": [
    "Replace spark plug and coil pack",
    "Clean or replace injector",
    "Repair valve or gasket issues"
  ],
  "Temporary Solutions": [
    "Avoid hard acceleration",
    "Drive gently until fixed"
  ]
},

"P0303": {
  "Actual Issue": "Cylinder 3 Misfire Detected",
  "Severity": "High (Continued misfire risks engine damage and emission problems)",
  "Possible Causes": [
    {"cause": "Bad spark plug or coil in cylinder 3", "probability": 0.50},
    {"cause": "Vacuum leak near the intake manifold", "probability": 0.30},
    {"cause": "Fuel pressure drop", "probability": 0.20}
  ],
  "Symptoms": [
    "Engine stutter or hesitation",
    "Poor fuel economy",
    "Engine light flashing"
  ],
  "Diagnostics": [
    "Check spark plug and coil in cylinder 3",
    "Inspect intake manifold for vacuum leaks",
    "Test fuel pressure and regulator"
  ],
  "Fixes": [
    "Replace spark plug or coil",
    "Seal vacuum leaks",
    "Repair fuel pressure issues"
  ],
  "Temporary Solutions": [
    "Drive cautiously",
    "Avoid heavy throttle"
  ]
},

"P0304": {
  "Actual Issue": "Cylinder 4 Misfire Detected",
  "Severity": "High (Serious if ignored; misfires damage engine and emissions system)",
  "Possible Causes": [
    {"cause": "Faulty ignition coil or plug", "probability": 0.45},
    {"cause": "Fuel injector fault", "probability": 0.35},
    {"cause": "Low compression", "probability": 0.20}
  ],
  "Symptoms": [
    "Engine runs rough at idle",
    "Loss of power",
    "Flashing check engine light"
  ],
  "Diagnostics": [
    "Swap ignition coil with known good unit",
    "Run fuel injector test",
    "Perform cylinder leak-down test"
  ],
  "Fixes": [
    "Replace faulty ignition coil or plug",
    "Repair or replace fuel injector",
    "Fix compression issues"
  ],
  "Temporary Solutions": [
    "Avoid aggressive driving",
    "Drive carefully until repaired"
  ]
},

"P0305": {
  "Actual Issue": "Cylinder 5 Misfire Detected",
  "Severity": "High (Can cause severe drivability issues and engine damage if unresolved)",
  "Possible Causes": [
    {"cause": "Faulty spark plug or ignition coil in cylinder 5", "probability": 0.50},
    {"cause": "Fuel injector issues", "probability": 0.30},
    {"cause": "Low compression in cylinder 5", "probability": 0.20}
  ],
  "Symptoms": [
    "Engine rough idle",
    "Loss of power",
    "Check engine light on",
    "Engine vibration"
  ],
  "Diagnostics": [
    "Inspect spark plug and ignition coil in cylinder 5",
    "Check fuel injector operation",
    "Perform compression test"
  ],
  "Fixes": [
    "Replace spark plug or ignition coil",
    "Clean or replace fuel injector",
    "Repair compression issues"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid hard acceleration"
  ]
},

"P0306": {
  "Actual Issue": "Cylinder 6 Misfire Detected",
  "Severity": "High (Engine damage risk; repair recommended ASAP)",
  "Possible Causes": [
    {"cause": "Faulty spark plug or ignition coil in cylinder 6", "probability": 0.50},
    {"cause": "Fuel injector problems", "probability": 0.30},
    {"cause": "Compression issues in cylinder 6", "probability": 0.20}
  ],
  "Symptoms": [
    "Engine rough idle",
    "Loss of power",
    "Check engine light on",
    "Vibrations from engine"
  ],
  "Diagnostics": [
    "Inspect spark plug and ignition coil in cylinder 6",
    "Check fuel injector operation",
    "Perform compression test"
  ],
  "Fixes": [
    "Replace spark plug or ignition coil",
    "Clean or replace fuel injector",
    "Repair compression issues"
  ],
  "Temporary Solutions": [
    "Avoid heavy acceleration",
    "Drive gently"
  ]
},

"P0307": {
  "Actual Issue": "Cylinder 7 Misfire Detected",
  "Severity": "High (Misfire can quickly damage engine components and affect emissions)",
  "Possible Causes": [
    {"cause": "Faulty spark plug or ignition coil on cylinder 7", "probability": 0.40},
    {"cause": "Fuel injector problem on cylinder 7", "probability": 0.25},
    {"cause": "Compression issues in cylinder 7", "probability": 0.15},
    {"cause": "Vacuum leak near cylinder 7", "probability": 0.10},
    {"cause": "Wiring or connector issues", "probability": 0.10}
  ],
  "Symptoms": [
    "Engine runs rough",
    "Loss of power",
    "Increased fuel consumption",
    "Check engine light ON"
  ],
  "Diagnostics": [
    "Check spark plug and ignition coil on cylinder 7",
    "Inspect fuel injector operation",
    "Perform compression test",
    "Inspect wiring and connectors"
  ],
  "Fixes": [
    "Replace faulty spark plug or ignition coil",
    "Clean or replace fuel injector",
    "Repair compression issues",
    "Fix wiring or connector problems"
  ],
  "Temporary Solutions": [
    "Avoid heavy acceleration",
    "Drive gently until repair"
  ]
},

"P0308": {
  "Actual Issue": "Cylinder 8 Misfire Detected",
  "Severity": "High (Can cause serious engine damage and emissions failure)",
  "Possible Causes": [
    {"cause": "Faulty spark plug or ignition coil on cylinder 8", "probability": 0.40},
    {"cause": "Fuel injector problem on cylinder 8", "probability": 0.25},
    {"cause": "Compression issues in cylinder 8", "probability": 0.15},
    {"cause": "Vacuum leak near cylinder 8", "probability": 0.10},
    {"cause": "Wiring or connector issues", "probability": 0.10}
  ],
  "Symptoms": [
    "Engine runs rough",
    "Loss of power",
    "Increased fuel consumption",
    "Check engine light ON"
  ],
  "Diagnostics": [
    "Check spark plug and ignition coil on cylinder 8",
    "Inspect fuel injector operation",
    "Perform compression test",
    "Inspect wiring and connectors"
  ],
  "Fixes": [
    "Replace faulty spark plug or ignition coil",
    "Clean or replace fuel injector",
    "Repair compression issues",
    "Fix wiring or connector problems"
  ],
  "Temporary Solutions": [
    "Avoid heavy acceleration",
    "Drive gently until repair"
  ]
},

"P0310": {
  "Actual Issue": "Misfire Detected on Startup",
  "Severity": "Medium-High (Startup misfires can cause drivability issues and potential damage if persistent)",
  "Possible Causes": [
    {"cause": "Ignition system faults", "probability": 0.35},
    {"cause": "Fuel delivery problems", "probability": 0.25},
    {"cause": "Sensor issues affecting startup", "probability": 0.20},
    {"cause": "Vacuum leaks", "probability": 0.10},
    {"cause": "Low compression", "probability": 0.10}
  ],
  "Symptoms": [
    "Engine hesitation or stumble during startup",
    "Rough idling initially",
    "Check engine light ON"
  ],
  "Diagnostics": [
    "Scan for misfire codes",
    "Check ignition components",
    "Inspect fuel system",
    "Test sensors related to engine startup"
  ],
  "Fixes": [
    "Repair or replace faulty ignition parts",
    "Clean or repair fuel injectors",
    "Fix vacuum leaks",
    "Replace defective sensors"
  ],
  "Temporary Solutions": [
    "Avoid rapid throttle during startup",
    "Ensure proper engine warm-up"
  ]
},

    "P0171": {
  "Actual Issue": "System Too Lean (Bank 1)",
  "Severity": "Medium-High (Can cause poor performance, increased emissions, and potential engine damage if ignored)",
  "Possible Causes": [
    {"cause": "Vacuum leaks", "probability": 0.30},
    {"cause": "Faulty or dirty mass airflow sensor", "probability": 0.25},
    {"cause": "Low fuel pressure", "probability": 0.20},
    {"cause": "Faulty oxygen sensor", "probability": 0.15},
    {"cause": "Clogged fuel injectors", "probability": 0.10}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor engine performance",
    "Rough idle",
    "Increased fuel consumption"
  ],
  "Diagnostics": [
    "Inspect vacuum hoses for leaks",
    "Test mass airflow sensor output",
    "Check fuel pressure",
    "Test oxygen sensors",
    "Inspect and clean fuel injectors"
  ],
  "Fixes": [
    "Repair vacuum leaks",
    "Clean or replace mass airflow sensor",
    "Repair fuel pressure issues",
    "Replace faulty oxygen sensor",
    "Clean or replace fuel injectors"
  ],
  "Temporary Solutions": [
    "Avoid heavy acceleration",
    "Drive gently until repair"
  ]
},
"P0174": {
  "Actual Issue": "System Too Lean (Bank 2)",
  "Severity": "Medium-High (Same risks as Bank 1 lean condition; affects engine smoothness and emissions)",
  "Possible Causes": [
    {"cause": "Vacuum leaks", "probability": 0.30},
    {"cause": "Faulty or dirty mass airflow sensor", "probability": 0.25},
    {"cause": "Low fuel pressure", "probability": 0.20},
    {"cause": "Faulty oxygen sensor", "probability": 0.15},
    {"cause": "Clogged fuel injectors", "probability": 0.10}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor engine performance",
    "Rough idle",
    "Increased fuel consumption"
  ],
  "Diagnostics": [
    "Inspect vacuum hoses for leaks",
    "Test mass airflow sensor output",
    "Check fuel pressure",
    "Test oxygen sensors",
    "Inspect and clean fuel injectors"
  ],
  "Fixes": [
    "Repair vacuum leaks",
    "Clean or replace mass airflow sensor",
    "Repair fuel pressure issues",
    "Replace faulty oxygen sensor",
    "Clean or replace fuel injectors"
  ],
  "Temporary Solutions": [
    "Avoid heavy acceleration",
    "Drive gently until repair"
  ]
},
"P0420": {
  "Actual Issue": "Catalyst System Efficiency Below Threshold (Bank 1)",
  "Severity": "High (Damaged catalytic converter causes emissions failure, may lead to engine issues)",
  "Possible Causes": [
    {"cause": "Damaged catalytic converter", "probability": 0.50},
    {"cause": "Faulty oxygen sensors", "probability": 0.30},
    {"cause": "Exhaust leaks", "probability": 0.15},
    {"cause": "Engine misfires", "probability": 0.05}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Reduced fuel efficiency",
    "Failed emissions test",
    "Possible engine performance issues"
  ],
  "Diagnostics": [
    "Scan for catalytic converter related codes",
    "Test oxygen sensors",
    "Inspect exhaust system for leaks",
    "Check for engine misfires"
  ],
  "Fixes": [
    "Replace catalytic converter",
    "Replace faulty oxygen sensors",
    "Repair exhaust leaks",
    "Fix engine misfires"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid heavy loads until repaired"
  ]
},
"P0430": {
  "Actual Issue": "Catalyst System Efficiency Below Threshold (Bank 2)",
  "Severity": "High (Same risks as Bank 1 catalytic issues; emissions and performance affected)",
  "Possible Causes": [
    {"cause": "Damaged catalytic converter", "probability": 0.50},
    {"cause": "Faulty oxygen sensors", "probability": 0.30},
    {"cause": "Exhaust leaks", "probability": 0.15},
    {"cause": "Engine misfires", "probability": 0.05}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Reduced fuel efficiency",
    "Failed emissions test",
    "Possible engine performance issues"
  ],
  "Diagnostics": [
    "Scan for catalytic converter related codes",
    "Test oxygen sensors",
    "Inspect exhaust system for leaks",
    "Check for engine misfires"
  ],
  "Fixes": [
    "Replace catalytic converter",
    "Replace faulty oxygen sensors",
    "Repair exhaust leaks",
    "Fix engine misfires"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid heavy loads until repaired"
  ]
},
"P0133": {
  "Actual Issue": "O2 Sensor Circuit Slow Response (Bank 1 Sensor 1)",
  "Severity": "Medium (Can lead to inefficient fuel management and increased emissions)",
  "Possible Causes": [
    {"cause": "Faulty oxygen sensor", "probability": 0.50},
    {"cause": "Wiring issues", "probability": 0.30},
    {"cause": "Exhaust leaks", "probability": 0.10},
    {"cause": "Contaminated sensor", "probability": 0.10}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor fuel economy",
    "Engine hesitation"
  ],
  "Diagnostics": [
    "Scan for oxygen sensor codes",
    "Inspect wiring and connectors",
    "Check for exhaust leaks",
    "Test oxygen sensor response time"
  ],
  "Fixes": [
    "Replace oxygen sensor",
    "Repair wiring or connectors",
    "Fix exhaust leaks",
    "Clean or replace sensor"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid aggressive driving until fixed"
  ]
},
"P0135": {
  "Actual Issue": "O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 1)",
  "Severity": "Medium (Slower sensor readiness can affect emissions and drivability)",
  "Possible Causes": [
    {"cause": "Faulty oxygen sensor heater", "probability": 0.60},
    {"cause": "Blown fuse or relay", "probability": 0.25},
    {"cause": "Wiring problems", "probability": 0.15}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor engine performance",
    "Increased emissions"
  ],
  "Diagnostics": [
    "Check oxygen sensor heater circuit",
    "Test related fuses and relays",
    "Inspect wiring"
  ],
  "Fixes": [
    "Replace oxygen sensor",
    "Replace blown fuses or relays",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid heavy loads"
  ]
},
"P0141": {
  "Actual Issue": "O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 2)",
  "Severity": "Medium (Same impact as P0135, sensor readiness affected)",
  "Possible Causes": [
    {"cause": "Faulty oxygen sensor heater", "probability": 0.60},
    {"cause": "Blown fuse or relay", "probability": 0.25},
    {"cause": "Wiring problems", "probability": 0.15}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor engine performance",
    "Increased emissions"
  ],
  "Diagnostics": [
    "Check oxygen sensor heater circuit",
    "Test related fuses and relays",
    "Inspect wiring"
  ],
  "Fixes": [
    "Replace oxygen sensor",
    "Replace blown fuses or relays",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid heavy loads"
  ]
},
"P0455": {
  "Actual Issue": "Evaporative Emission System Leak Detected (Large Leak)",
  "Severity": "Low-Medium (Causes emissions leak, fuel odor; usually not urgent but needs repair)",
  "Possible Causes": [
    {"cause": "Loose or missing gas cap", "probability": 0.50},
    {"cause": "Cracked or disconnected EVAP hoses", "probability": 0.35},
    {"cause": "Faulty purge valve or vent valve", "probability": 0.15}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Fuel odor",
    "Failed emissions test"
  ],
  "Diagnostics": [
    "Inspect gas cap condition and fitment",
    "Check EVAP hoses for cracks or disconnections",
    "Test purge and vent valves"
  ],
  "Fixes": [
    "Tighten or replace gas cap",
    "Repair or replace EVAP hoses",
    "Replace faulty valves"
  ],
  "Temporary Solutions": [
    "Avoid fueling until leak is fixed",
    "Drive gently"
  ]
},
"P0442": {
  "Actual Issue": "Evaporative Emission System Leak Detected (Small Leak)",
  "Severity": "Low-Medium (Similar to P0455, minor leak that should be fixed)",
  "Possible Causes": [
    {"cause": "Loose or missing gas cap", "probability": 0.50},
    {"cause": "Cracked or disconnected EVAP hoses", "probability": 0.35},
    {"cause": "Faulty purge valve or vent valve", "probability": 0.15}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Fuel odor",
    "Failed emissions test"
  ],
  "Diagnostics": [
    "Inspect gas cap condition and fitment",
    "Check EVAP hoses for cracks or disconnections",
    "Test purge and vent valves"
  ],
  "Fixes": [
    "Tighten or replace gas cap",
    "Repair or replace EVAP hoses",
    "Replace faulty valves"
  ],
  "Temporary Solutions": [
    "Avoid fueling until leak is fixed",
    "Drive gently"
  ]
},
"P0113": {
  "Actual Issue": "Intake Air Temperature Sensor 1 Circuit High Input",
  "Severity": "Low-Medium (Sensor fault usually affects performance mildly but should be checked)",
  "Possible Causes": [
    {"cause": "Faulty intake air temperature sensor", "probability": 0.60},
    {"cause": "Wiring issues", "probability": 0.30},
    {"cause": "Sensor connector problems", "probability": 0.10}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor engine performance",
    "Hard starting"
  ],
  "Diagnostics": [
    "Test intake air temperature sensor",
    "Inspect wiring and connectors"
  ],
  "Fixes": [
    "Replace intake air temperature sensor",
    "Repair wiring or connectors"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid harsh starts"
  ]
},
"P0117": {
  "Actual Issue": "Engine Coolant Temperature Sensor Circuit Low Input",
  "Severity": "Medium (Can cause engine overheating or poor fuel economy; needs timely repair)",
  "Possible Causes": [
    {"cause": "Faulty coolant temperature sensor", "probability": 0.50},
    {"cause": "Wiring problems", "probability": 0.30},
    {"cause": "Thermostat malfunction", "probability": 0.20}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Engine overheating",
    "Poor fuel economy"
  ],
  "Diagnostics": [
    "Test coolant temperature sensor",
    "Inspect wiring",
    "Check thermostat operation"
  ],
  "Fixes": [
    "Replace coolant temperature sensor",
    "Repair wiring",
    "Replace thermostat if needed"
  ],
  "Temporary Solutions": [
    "Avoid heavy engine load",
    "Drive gently"
  ]
},
"P0118": {
  "Actual Issue": "Engine Coolant Temperature Sensor Circuit High Input",
  "Severity": "Medium (Similar risks as P0117; timely repair advised)",
  "Possible Causes": [
    {"cause": "Faulty coolant temperature sensor", "probability": 0.50},
    {"cause": "Wiring issues", "probability": 0.30},
    {"cause": "Connector problems", "probability": 0.20}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Engine overheating",
    "Poor fuel economy"
  ],
  "Diagnostics": [
    "Test coolant temperature sensor",
    "Inspect wiring and connectors"
  ],
  "Fixes": [
    "Replace coolant temperature sensor",
    "Repair wiring/connectors"
  ],
  "Temporary Solutions": [
    "Avoid heavy engine load",
    "Drive gently"
  ]
},
"P0128": {
  "Actual Issue": "Coolant Thermostat (Coolant Temperature Below Thermostat Regulating Temperature)",
  "Severity": "Medium (Faulty thermostat causes poor engine temp regulation, fuel efficiency loss, heater issues)",
  "Possible Causes": [
    {"cause": "Faulty thermostat stuck open", "probability": 0.60},
    {"cause": "Low coolant level", "probability": 0.25},
    {"cause": "Wiring issues", "probability": 0.15}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Engine runs cold",
    "Poor heater performance",
    "Reduced fuel efficiency"
  ],
  "Diagnostics": [
    "Test thermostat operation",
    "Check coolant level",
    "Inspect wiring"
  ],
  "Fixes": [
    "Replace thermostat",
    "Refill coolant",
    "Repair wiring if needed"
  ],
  "Temporary Solutions": [
    "Avoid prolonged cold engine operation",
    "Drive gently until fixed"
  ]
},
"P0120": {
  "Actual Issue": "Throttle/Pedal Position Sensor/Switch “A” Circuit Malfunction",
  "Severity": "Medium (Affects throttle response and drivability; timely repair advised)",
  "Possible Causes": [
    {"cause": "Faulty throttle position sensor (TPS)", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Connector problems", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor acceleration",
    "Engine hesitation or stalling"
  ],
  "Diagnostics": [
    "Test throttle position sensor output",
    "Inspect wiring harness and connectors",
    "Scan for related trouble codes"
  ],
  "Fixes": [
    "Replace throttle position sensor",
    "Repair wiring/connectors"
  ],
  "Temporary Solutions": [
    "Avoid rapid acceleration",
    "Drive gently until repaired"
  ]
},
"P0121": {
  "Actual Issue": "Throttle/Pedal Position Sensor/Switch “A” Circuit Range/Performance Problem",
  "Severity": "Medium (Can cause inconsistent throttle response and poor fuel economy)",
  "Possible Causes": [
    {"cause": "Faulty throttle position sensor", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Connector problems", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Engine hesitation",
    "Poor fuel economy"
  ],
  "Diagnostics": [
    "Test throttle position sensor signal range",
    "Check wiring and connectors",
    "Scan for related trouble codes"
  ],
  "Fixes": [
    "Replace throttle position sensor",
    "Repair wiring/connectors"
  ],
  "Temporary Solutions": [
    "Avoid heavy acceleration",
    "Drive gently until repaired"
  ]
},
"P0122": {
  "Actual Issue": "Throttle/Pedal Position Sensor/Switch “A” Circuit Low Input",
  "Severity": "Medium (Leads to poor throttle response and hesitation)",
  "Possible Causes": [
    {"cause": "Faulty throttle position sensor", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Connector problems", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor throttle response",
    "Engine hesitation"
  ],
  "Diagnostics": [
    "Measure throttle position sensor voltage",
    "Inspect wiring harness",
    "Scan for trouble codes"
  ],
  "Fixes": [
    "Replace throttle position sensor",
    "Repair wiring/connectors"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid aggressive throttle inputs"
  ]
},
"P0123": {
  "Actual Issue": "Throttle/Pedal Position Sensor/Switch “A” Circuit High Input",
  "Severity": "Medium (May cause poor throttle response and engine hesitation)",
  "Possible Causes": [
    {"cause": "Faulty throttle position sensor", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Connector problems", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor throttle response",
    "Engine hesitation"
  ],
  "Diagnostics": [
    "Check throttle position sensor voltage output",
    "Inspect wiring and connectors",
    "Scan ECU for related codes"
  ],
  "Fixes": [
    "Replace throttle position sensor",
    "Repair wiring/connectors"
  ],
  "Temporary Solutions": [
    "Avoid heavy throttle",
    "Drive gently until repair"
  ]
},
"P0130": {
  "Actual Issue": "O2 Sensor Circuit Malfunction (Bank 1 Sensor 1)",
  "Severity": "Medium (Affects emissions and fuel efficiency)",
  "Possible Causes": [
    {"cause": "Faulty oxygen sensor", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Exhaust leaks", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor fuel economy",
    "Engine hesitation"
  ],
  "Diagnostics": [
    "Test oxygen sensor voltage",
    "Inspect wiring and connectors",
    "Check exhaust system for leaks"
  ],
  "Fixes": [
    "Replace oxygen sensor",
    "Repair wiring",
    "Fix exhaust leaks"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid rapid acceleration"
  ]
},
"P0146": {
  "Actual Issue": "O2 Sensor Circuit Malfunction (Bank 1 Sensor 3)",
  "Severity": "Medium (Impacts emissions control and engine performance)",
  "Possible Causes": [
    {"cause": "Faulty oxygen sensor", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Exhaust leaks", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor fuel economy",
    "Engine hesitation"
  ],
  "Diagnostics": [
    "Test oxygen sensor voltage",
    "Inspect wiring and connectors",
    "Check exhaust system for leaks"
  ],
  "Fixes": [
    "Replace oxygen sensor",
    "Repair wiring",
    "Fix exhaust leaks"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid rapid acceleration"
  ]
},
"P0138": {
  "Actual Issue": "O2 Sensor Circuit High Voltage (Bank 1 Sensor 2)",
  "Severity": "Medium (May cause poor fuel economy and emissions issues)",
  "Possible Causes": [
    {"cause": "Faulty oxygen sensor", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Contaminated sensor", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor fuel economy",
    "Engine hesitation"
  ],
  "Diagnostics": [
    "Check oxygen sensor voltage output",
    "Inspect wiring and connectors",
    "Test sensor contamination"
  ],
  "Fixes": [
    "Replace oxygen sensor",
    "Repair wiring",
    "Clean or replace sensor"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid heavy loads"
  ]
},
"P0139": {
  "Actual Issue": "O2 Sensor Circuit Slow Response (Bank 1 Sensor 2)",
  "Severity": "Medium (Can lead to inefficient engine performance and emissions)",
  "Possible Causes": [
    {"cause": "Faulty oxygen sensor", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Contaminated sensor", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor fuel economy",
    "Engine hesitation"
  ],
  "Diagnostics": [
    "Check oxygen sensor response time",
    "Inspect wiring and connectors",
    "Test sensor contamination"
  ],
  "Fixes": [
    "Replace oxygen sensor",
    "Repair wiring",
    "Clean or replace sensor"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid heavy loads"
  ]
},
"P0401": {
  "Actual Issue": "Exhaust Gas Recirculation Flow Insufficient Detected",
  "Severity": "Medium (Causes rough idle and reduced engine performance)",
  "Possible Causes": [
    {"cause": "Clogged EGR valve", "probability": 0.4},
    {"cause": "Faulty EGR valve", "probability": 0.3},
    {"cause": "Vacuum leaks", "probability": 0.2},
    {"cause": "Faulty EGR sensor", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Rough idle",
    "Reduced engine performance"
  ],
  "Diagnostics": [
    "Inspect and clean EGR valve",
    "Test EGR sensor operation",
    "Check vacuum lines"
  ],
  "Fixes": [
    "Clean or replace EGR valve",
    "Repair vacuum leaks",
    "Replace EGR sensor"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid heavy loads"
  ]
},
"P0402": {
  "Actual Issue": "Exhaust Gas Recirculation Flow Excessive Detected",
  "Severity": "Medium (Can cause rough idle and reduced performance)",
  "Possible Causes": [
    {"cause": "Stuck open EGR valve", "probability": 0.5},
    {"cause": "Faulty EGR valve", "probability": 0.3},
    {"cause": "Wiring issues", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Rough idle",
    "Reduced engine performance"
  ],
  "Diagnostics": [
    "Inspect EGR valve operation",
    "Check wiring and connectors"
  ],
  "Fixes": [
    "Replace or repair EGR valve",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid heavy loads"
  ]
},
"P0410": {
  "Actual Issue": "Secondary Air Injection System Malfunction",
  "Severity": "Low to Medium (Affects emissions, minimal drivability impact)",
  "Possible Causes": [
    {"cause": "Faulty air pump", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Faulty relay or fuse", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Increased emissions",
    "Rough idle"
  ],
  "Diagnostics": [
    "Test air pump operation",
    "Inspect wiring and connectors",
    "Check relay and fuse"
  ],
  "Fixes": [
    "Replace air pump",
    "Repair wiring",
    "Replace faulty relay/fuse"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid heavy loads"
  ]
},
"P0440": {
  "Actual Issue": "Evaporative Emission Control System Malfunction",
  "Severity": "Low to Medium (May cause fuel odor and emissions test failure)",
  "Possible Causes": [
    {"cause": "Loose or damaged gas cap", "probability": 0.5},
    {"cause": "Faulty purge valve", "probability": 0.3},
    {"cause": "Wiring issues", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Fuel odor",
    "Failed emissions test"
  ],
  "Diagnostics": [
    "Check gas cap fit and condition",
    "Test purge valve operation",
    "Inspect wiring"
  ],
  "Fixes": [
    "Tighten or replace gas cap",
    "Replace purge valve",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Avoid fueling until repaired",
    "Drive gently"
  ]
},
"P0446": {
  "Actual Issue": "Evaporative Emission Control System Vent Control Circuit Malfunction",
  "Severity": "Low to Medium (May cause emissions issues and fuel odor)",
  "Possible Causes": [
    {"cause": "Faulty vent valve", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Connector problems", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Fuel odor",
    "Failed emissions test"
  ],
  "Diagnostics": [
    "Test vent valve operation",
    "Inspect wiring and connectors"
  ],
  "Fixes": [
    "Replace vent valve",
    "Repair wiring/connectors"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid fueling until repaired"
  ]
},
"P0507": {
  "Actual Issue": "Idle Control System RPM Higher Than Expected",
  "Severity": "Medium (May cause engine running fast at idle and possible stalling)",
  "Possible Causes": [
    {"cause": "Vacuum leaks", "probability": 0.5},
    {"cause": "Faulty idle air control valve", "probability": 0.3},
    {"cause": "Throttle body issues", "probability": 0.2}
  ],
  "Symptoms": [
    "High idle speed",
    "Engine runs fast at idle",
    "Possible stalling"
  ],
  "Diagnostics": [
    "Inspect vacuum hoses",
    "Test idle air control valve",
    "Check throttle body cleanliness"
  ],
  "Fixes": [
    "Repair vacuum leaks",
    "Clean or replace idle air control valve",
    "Clean throttle body"
  ],
  "Temporary Solutions": [
    "Avoid high engine loads",
    "Drive gently"
  ]
},
"P0505": {
  "Actual Issue": "Idle Control System Malfunction",
  "Severity": "Medium (Affects idle speed stability; timely repair advised)",
  "Possible Causes": [
    {"cause": "Faulty idle air control valve", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Vacuum leaks", "probability": 0.2}
  ],
  "Symptoms": [
    "Irregular idle speed",
    "Engine stalling at idle",
    "Check Engine Light on"
  ],
  "Diagnostics": [
    "Test idle air control valve",
    "Inspect wiring",
    "Check for vacuum leaks"
  ],
  "Fixes": [
    "Replace idle air control valve",
    "Repair wiring",
    "Fix vacuum leaks"
  ],
  "Temporary Solutions": [
    "Avoid engine idling for long periods",
    "Drive gently"
  ]
},
"P0606": {
  "Actual Issue": "ECM/PCM Processor Fault",
  "Severity": "High (Can cause engine no-start or serious drivability issues; urgent attention needed)",
  "Possible Causes": [
    {"cause": "Faulty ECM/PCM", "probability": 0.5},
    {"cause": "Electrical issues", "probability": 0.3},
    {"cause": "Software corruption", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Engine performance issues",
    "Possible no start"
  ],
  "Diagnostics": [
    "Scan ECM/PCM for errors",
    "Check electrical connections",
    "Attempt software reflash"
  ],
  "Fixes": [
    "Replace ECM/PCM",
    "Repair electrical faults",
    "Reprogram or update software"
  ],
  "Temporary Solutions": [
    "Avoid unnecessary engine starts",
    "Seek professional repair promptly"
  ]
},
"P0172": {
  "System": "Fuel/Air Mixture",
  "Category": "Fuel System",
  "Code Meaning": "System Too Rich (Bank 1)",
  "Severity": "Medium (Can cause poor fuel economy and emissions issues)",
  "Symptoms": [
    "Check Engine Light on",
    "Poor fuel economy",
    "Black smoke from exhaust"
  ],
  "Possible Causes": [
    {"cause": "Faulty fuel injectors", "probability": 0.5},
    {"cause": "Leaking fuel pressure regulator", "probability": 0.3},
    {"cause": "Faulty oxygen sensor", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check fuel injector operation and spray pattern",
    "Test fuel pressure regulator",
    "Test oxygen sensor output"
  ],
  "Fixes": [
    "Replace faulty injectors",
    "Replace fuel pressure regulator",
    "Replace oxygen sensor"
  ],
  "Temporary Solutions": [
    "Drive gently to reduce fuel demand",
    "Avoid heavy acceleration"
  ]
},
"P0175": {
  "System": "Fuel/Air Mixture",
  "Category": "Fuel System",
  "Code Meaning": "System Too Rich (Bank 2)",
  "Severity": "Medium (Can cause poor fuel economy and emissions issues)",
  "Symptoms": [
    "Check Engine Light on",
    "Poor fuel economy",
    "Black smoke from exhaust"
  ],
  "Possible Causes": [
    {"cause": "Faulty fuel injectors", "probability": 0.5},
    {"cause": "Leaking fuel pressure regulator", "probability": 0.3},
    {"cause": "Faulty oxygen sensor", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check fuel injector operation and spray pattern",
    "Test fuel pressure regulator",
    "Test oxygen sensor output"
  ],
  "Fixes": [
    "Replace faulty injectors",
    "Replace fuel pressure regulator",
    "Replace oxygen sensor"
  ],
  "Temporary Solutions": [
    "Drive gently to reduce fuel demand",
    "Avoid heavy acceleration"
  ]
},
"P0219": {
  "System": "Transmission",
  "Category": "Temperature Condition",
  "Code Meaning": "Transmission Over Temperature Condition",
  "Severity": "High (Risk of transmission damage if unaddressed; urgent repair recommended)",
  "Symptoms": [
    "Transmission slipping",
    "Delayed shifting",
    "Warning light on dashboard"
  ],
  "Possible Causes": [
    {"cause": "Low transmission fluid", "probability": 0.5},
    {"cause": "Faulty transmission cooler", "probability": 0.3},
    {"cause": "Heavy towing or overheating", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check transmission fluid level and condition",
    "Test transmission cooler operation",
    "Inspect for signs of overheating"
  ],
  "Fixes": [
    "Check and refill transmission fluid",
    "Replace transmission cooler",
    "Avoid heavy towing"
  ],
  "Temporary Solutions": [
    "Allow transmission to cool before driving",
    "Drive gently to reduce heat build-up"
  ]
},
"P0700": {
  "System": "Transmission",
  "Category": "Control System",
  "Code Meaning": "Transmission Control System Malfunction",
  "Severity": "High (May cause transmission failure; prompt diagnosis required)",
  "Symptoms": [
    "Check Engine Light on",
    "Transmission warning light",
    "Transmission shifting problems"
  ],
  "Possible Causes": [
    {"cause": "Faulty transmission control module", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Internal transmission problems", "probability": 0.2}
  ],
  "Diagnostics": [
    "Scan transmission control module for specific codes",
    "Inspect wiring harness and connectors",
    "Perform transmission system diagnostics"
  ],
  "Fixes": [
    "Repair wiring issues",
    "Replace transmission control module if faulty",
    "Repair internal transmission faults"
  ],
  "Temporary Solutions": [
    "Avoid heavy loads or aggressive driving",
    "Drive gently until repaired"
  ]
},
"P0730": {
  "System": "Transmission",
  "Category": "Gear Ratio",
  "Code Meaning": "Incorrect Gear Ratio",
  "Severity": "Medium (Can cause poor acceleration and transmission wear)",
  "Symptoms": [
    "Check Engine Light on",
    "Harsh or incorrect shifting",
    "Poor acceleration"
  ],
  "Possible Causes": [
    {"cause": "Worn or damaged transmission bands or clutches", "probability": 0.5},
    {"cause": "Faulty shift solenoids", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check transmission fluid level and condition",
    "Test shift solenoid operation",
    "Inspect transmission bands and clutches"
  ],
  "Fixes": [
    "Repair or replace transmission bands/clutches",
    "Replace faulty shift solenoids",
    "Check and refill transmission fluid"
  ],
  "Temporary Solutions": [
    "Avoid aggressive shifting",
    "Drive gently"
  ]
},
"P0740": {
  "System": "Transmission",
  "Category": "Torque Converter",
  "Code Meaning": "Torque Converter Clutch Circuit Malfunction",
  "Severity": "Medium (May cause slipping and reduced fuel economy)",
  "Symptoms": [
    "Check Engine Light on",
    "Transmission slipping",
    "Poor fuel economy"
  ],
  "Possible Causes": [
    {"cause": "Faulty torque converter clutch solenoid", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Internal transmission failure", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test torque converter clutch solenoid",
    "Inspect wiring and connectors",
    "Scan transmission for related faults"
  ],
  "Fixes": [
    "Replace torque converter clutch solenoid",
    "Repair wiring",
    "Repair or replace transmission if severe"
  ],
  "Temporary Solutions": [
    "Drive gently to reduce load",
    "Avoid heavy towing"
  ]
},
"P0750": {
  "System": "Transmission",
  "Category": "Shift Solenoid",
  "Code Meaning": "Shift Solenoid A Malfunction",
  "Severity": "Medium (Affects shifting; timely repair advised)",
  "Symptoms": [
    "Check Engine Light on",
    "Transmission stuck in gear",
    "Delayed or harsh shifting"
  ],
  "Possible Causes": [
    {"cause": "Faulty shift solenoid A", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test shift solenoid A",
    "Inspect wiring and connectors",
    "Check transmission fluid level"
  ],
  "Fixes": [
    "Replace shift solenoid A",
    "Repair wiring",
    "Refill transmission fluid if low"
  ],
  "Temporary Solutions": [
    "Avoid aggressive shifting",
    "Drive gently"
  ]
},
"P0755": {
  "System": "Transmission",
  "Category": "Shift Solenoid",
  "Code Meaning": "Shift Solenoid B Malfunction",
  "Severity": "Medium (Affects shifting; timely repair advised)",
  "Symptoms": [
    "Check Engine Light on",
    "Transmission stuck in gear",
    "Delayed or harsh shifting"
  ],
  "Possible Causes": [
    {"cause": "Faulty shift solenoid B", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test shift solenoid B",
    "Inspect wiring and connectors",
    "Check transmission fluid level"
  ],
  "Fixes": [
    "Replace shift solenoid B",
    "Repair wiring",
    "Refill transmission fluid if low"
  ],
  "Temporary Solutions": [
    "Avoid aggressive shifting",
    "Drive gently"
  ]
},
"P0760": {
  "System": "Transmission",
  "Category": "Shift Solenoid",
  "Code Meaning": "Shift Solenoid C Malfunction",
  "Severity": "Medium (Affects shifting; timely repair advised)",
  "Symptoms": [
    "Check Engine Light on",
    "Transmission stuck in gear",
    "Delayed or harsh shifting"
  ],
  "Possible Causes": [
    {"cause": "Faulty shift solenoid C", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test shift solenoid C",
    "Inspect wiring and connectors",
    "Check transmission fluid level"
  ],
  "Fixes": [
    "Replace shift solenoid C",
    "Repair wiring",
    "Refill transmission fluid if low"
  ],
  "Temporary Solutions": [
    "Avoid aggressive shifting",
    "Drive gently"
  ]
},
"P0770": {
  "System": "Transmission",
  "Category": "Shift Solenoid",
  "Code Meaning": "Shift Solenoid D Malfunction",
  "Severity": "Medium (Affects shifting; timely repair advised)",
  "Symptoms": [
    "Check Engine Light on",
    "Transmission stuck in gear",
    "Delayed or harsh shifting"
  ],
  "Possible Causes": [
    {"cause": "Faulty shift solenoid D", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test shift solenoid D",
    "Inspect wiring and connectors",
    "Check transmission fluid level"
  ],
  "Fixes": [
    "Replace shift solenoid D",
    "Repair wiring",
    "Refill transmission fluid if low"
  ],
  "Temporary Solutions": [
    "Avoid aggressive shifting",
    "Drive gently"
  ]
},
"P0780": {
  "System": "Transmission",
  "Category": "Shift Error",
  "Code Meaning": "Shift Incorrect",
  "Severity": "Medium (Can cause transmission wear and poor drivability)",
  "Symptoms": [
    "Check Engine Light on",
    "Harsh or delayed shifts",
    "Transmission slipping"
  ],
  "Possible Causes": [
    {"cause": "Faulty shift solenoids", "probability": 0.5},
    {"cause": "Mechanical transmission problems", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test shift solenoids",
    "Inspect transmission mechanical components",
    "Check transmission fluid level"
  ],
  "Fixes": [
    "Replace faulty shift solenoids",
    "Repair transmission",
    "Refill transmission fluid if low"
  ],
  "Temporary Solutions": [
    "Avoid aggressive driving",
    "Drive gently"
  ]
},
"P0101": {
  "Actual Issue": "Mass Air Flow Circuit Range/Performance Problem",
  "System": "Air Intake",
  "Category": "Mass Air Flow Sensor",
  "Severity": "Medium (Affects engine air-fuel mixture and performance)",
  "Possible Causes": [
    {"cause": "Dirty or faulty MAF sensor", "probability": 0.5},
    {"cause": "Vacuum leaks", "probability": 0.3},
    {"cause": "Wiring issues", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor acceleration",
    "Rough idle"
  ],
  "Diagnostics": [
    "Inspect and clean MAF sensor",
    "Check for vacuum leaks",
    "Test wiring and connectors"
  ],
  "Fixes": [
    "Clean or replace MAF sensor",
    "Repair vacuum leaks",
    "Fix wiring/connectors"
  ],
  "Temporary Solutions": [
    "Drive gently to reduce engine load",
    "Avoid harsh acceleration"
  ]
},
"P0102": {
  "Actual Issue": "Mass Air Flow Circuit Low Input",
  "System": "Air Intake",
  "Category": "Mass Air Flow Sensor",
  "Severity": "Medium (Leads to poor engine performance and rough idle)",
  "Possible Causes": [
    {"cause": "Faulty MAF sensor", "probability": 0.5},
    {"cause": "Wiring problems", "probability": 0.3},
    {"cause": "Sensor contamination", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor engine performance",
    "Rough idle"
  ],
  "Diagnostics": [
    "Test MAF sensor output",
    "Inspect wiring and connectors",
    "Clean sensor if contaminated"
  ],
  "Fixes": [
    "Replace MAF sensor",
    "Repair wiring",
    "Clean sensor"
  ],
  "Temporary Solutions": [
    "Avoid heavy throttle",
    "Drive gently"
  ]
},
"P0103": {
  "Actual Issue": "Mass Air Flow Circuit High Input",
  "System": "Air Intake",
  "Category": "Mass Air Flow Sensor",
  "Severity": "Medium (Leads to poor engine performance and rough idle)",
  "Possible Causes": [
    {"cause": "Faulty MAF sensor", "probability": 0.5},
    {"cause": "Wiring problems", "probability": 0.3},
    {"cause": "Sensor contamination", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor engine performance",
    "Rough idle"
  ],
  "Diagnostics": [
    "Test MAF sensor output",
    "Inspect wiring and connectors",
    "Clean sensor if contaminated"
  ],
  "Fixes": [
    "Replace MAF sensor",
    "Repair wiring",
    "Clean sensor"
  ],
  "Temporary Solutions": [
    "Avoid heavy throttle",
    "Drive gently"
  ]
},
"P0110": {
  "Actual Issue": "Intake Air Temperature Sensor Circuit Malfunction",
  "Severity": "Low to Medium (Monitor symptoms; repair advised to avoid fuel issues)",
  "System": "Air Intake",
  "Category": "Intake Air Temperature Sensor",
  "Possible Causes": [
    {"cause": "Faulty intake air temperature sensor", "probability": 0.7},
    {"cause": "Wiring issues", "probability": 0.3}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor engine performance",
    "Poor fuel economy"
  ],
  "Diagnostics": [
    "Test intake air temperature sensor",
    "Inspect wiring and connectors"
  ],
  "Fixes": [
    "Replace intake air temperature sensor",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Avoid heavy load driving",
    "Drive gently until fixed"
  ]
},

"P0112": {
  "Actual Issue": "Intake Air Temperature Sensor Circuit Low Input",
  "Severity": "Low to Medium (Monitor symptoms; timely repair recommended)",
  "System": "Air Intake",
  "Category": "Intake Air Temperature Sensor",
  "Possible Causes": [
    {"cause": "Faulty intake air temperature sensor", "probability": 0.7},
    {"cause": "Wiring issues", "probability": 0.3}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor engine performance",
    "Poor fuel economy"
  ],
  "Diagnostics": [
    "Test intake air temperature sensor",
    "Inspect wiring and connectors"
  ],
  "Fixes": [
    "Replace intake air temperature sensor",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Avoid heavy load driving",
    "Drive gently until fixed"
  ]
},

"P0134": {
  "Actual Issue": "O2 Sensor Circuit No Activity Detected (Bank 1 Sensor 1)",
  "Severity": "Medium (Impacts fuel efficiency; timely repair advised)",
  "System": "Oxygen Sensor",
  "Category": "Sensor Circuit",
  "Possible Causes": [
    {"cause": "Faulty oxygen sensor", "probability": 0.7},
    {"cause": "Wiring issues", "probability": 0.3}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor fuel economy",
    "Engine hesitation"
  ],
  "Diagnostics": [
    "Test oxygen sensor output",
    "Inspect wiring and connectors"
  ],
  "Fixes": [
    "Replace oxygen sensor",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Avoid heavy acceleration",
    "Drive gently"
  ]
},

"P0170": {
  "Actual Issue": "Fuel Trim Malfunction (Bank 1)",
  "Severity": "Medium to High (Can lead to poor engine performance and emissions issues)",
  "System": "Fuel System",
  "Category": "Fuel Trim",
  "Possible Causes": [
    {"cause": "Vacuum leaks", "probability": 0.4},
    {"cause": "Faulty fuel injectors", "probability": 0.4},
    {"cause": "Exhaust leaks", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor fuel economy",
    "Engine performance issues"
  ],
  "Diagnostics": [
    "Inspect for vacuum leaks",
    "Test fuel injectors",
    "Check exhaust system for leaks"
  ],
  "Fixes": [
    "Repair vacuum leaks",
    "Replace faulty injectors",
    "Fix exhaust leaks"
  ],
  "Temporary Solutions": [
    "Drive gently to reduce fuel demand",
    "Avoid high engine load"
  ]
},

"P0173": {
  "Actual Issue": "Fuel Trim Malfunction (Bank 2)",
  "Severity": "Medium to High (Similar to P0170; impacts engine efficiency)",
  "System": "Fuel System",
  "Category": "Fuel Trim",
  "Possible Causes": [
    {"cause": "Vacuum leaks", "probability": 0.4},
    {"cause": "Faulty fuel injectors", "probability": 0.4},
    {"cause": "Exhaust leaks", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Poor fuel economy",
    "Engine performance issues"
  ],
  "Diagnostics": [
    "Inspect for vacuum leaks",
    "Test fuel injectors",
    "Check exhaust system for leaks"
  ],
  "Fixes": [
    "Repair vacuum leaks",
    "Replace faulty injectors",
    "Fix exhaust leaks"
  ],
  "Temporary Solutions": [
    "Drive gently to reduce fuel demand",
    "Avoid high engine load"
  ]
},

"P0506": {
  "Actual Issue": "Idle Control System RPM Lower Than Expected",
  "Severity": "Low to Medium (May cause drivability issues; repair recommended)",
  "System": "Idle Control",
  "Category": "RPM Low",
  "Possible Causes": [
    {"cause": "Vacuum leaks", "probability": 0.4},
    {"cause": "Faulty idle air control valve", "probability": 0.4},
    {"cause": "Dirty throttle body", "probability": 0.2}
  ],
  "Symptoms": [
    "Low idle speed",
    "Engine stalls at idle",
    "Rough idle"
  ],
  "Diagnostics": [
    "Check for vacuum leaks",
    "Test idle air control valve",
    "Inspect and clean throttle body"
  ],
  "Fixes": [
    "Fix vacuum leaks",
    "Clean or replace idle air control valve",
    "Clean throttle body"
  ],
  "Temporary Solutions": [
    "Avoid extended idling",
    "Drive gently"
  ]
},

"P0309": {
  "Actual Issue": "Cylinder 9 Misfire Detected",
  "Severity": "High (Misfires can cause engine damage; prompt repair needed)",
  "System": "Engine",
  "Category": "Misfire",
  "Possible Causes": [
    {"cause": "Faulty spark plug or ignition coil", "probability": 0.5},
    {"cause": "Fuel injector issues", "probability": 0.3},
    {"cause": "Compression problems", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Engine roughness",
    "Poor acceleration"
  ],
  "Diagnostics": [
    "Test spark plug and ignition coil",
    "Inspect fuel injector operation",
    "Perform compression test"
  ],
  "Fixes": [
    "Replace spark plug or ignition coil",
    "Check/replace fuel injector",
    "Repair engine compression issues"
  ],
  "Temporary Solutions": [
    "Drive gently to avoid engine stress",
    "Avoid heavy acceleration"
  ]
},

"P0315": {
  "Actual Issue": "Crankshaft Position Sensor Circuit Malfunction",
  "Severity": "High (Can cause engine stalls or no start; timely repair critical)",
  "System": "Engine",
  "Category": "Sensor Circuit",
  "Possible Causes": [
    {"cause": "Faulty crankshaft position sensor", "probability": 0.7},
    {"cause": "Wiring problems", "probability": 0.3}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Engine stalls or no start",
    "Poor engine performance"
  ],
  "Diagnostics": [
    "Test crankshaft position sensor",
    "Inspect wiring and connectors"
  ],
  "Fixes": [
    "Replace crankshaft position sensor",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Avoid repeated engine starts",
    "Drive gently if possible"
  ]
},

"P0325": {
  "Actual Issue": "Knock Sensor Circuit Malfunction (Bank 1 or Single Sensor)",
  "Severity": "Medium (Engine knocking can cause damage; repair recommended)",
  "System": "Engine",
  "Category": "Knock Sensor",
  "Possible Causes": [
    {"cause": "Faulty knock sensor", "probability": 0.7},
    {"cause": "Wiring issues", "probability": 0.3}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Engine pinging or knocking noise",
    "Poor performance"
  ],
  "Diagnostics": [
    "Test knock sensor output",
    "Inspect wiring and connectors"
  ],
  "Fixes": [
    "Replace knock sensor",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Use lower octane fuel temporarily",
    "Avoid heavy acceleration"
  ]
},

"P0335": {
  "Actual Issue": "Crankshaft Position Sensor A Circuit Malfunction",
  "Severity": "High (Similar to P0315; engine may stall or not start)",
  "System": "Engine",
  "Category": "Sensor Circuit",
  "Possible Causes": [
    {"cause": "Faulty crankshaft position sensor", "probability": 0.7},
    {"cause": "Wiring problems", "probability": 0.3}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Engine stalls or no start",
    "Poor engine performance"
  ],
  "Diagnostics": [
    "Test crankshaft position sensor",
    "Inspect wiring and connectors"
  ],
  "Fixes": [
    "Replace crankshaft position sensor",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Avoid repeated engine starts",
    "Drive gently if possible"
  ]
},

"P0340": {
  "Actual Issue": "Camshaft Position Sensor Circuit Malfunction",
  "Severity": "Medium to High (May cause misfires and starting issues; repair soon)",
  "System": "Engine",
  "Category": "Sensor Circuit",
  "Possible Causes": [
    {"cause": "Faulty camshaft position sensor", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Faulty sensor reluctor ring", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Engine misfire or rough idle",
    "Difficulty starting engine"
  ],
  "Diagnostics": [
    "Test camshaft position sensor",
    "Inspect wiring and connectors",
    "Check sensor reluctor ring condition"
  ],
  "Fixes": [
    "Replace camshaft position sensor",
    "Repair wiring or connectors",
    "Replace reluctor ring if damaged"
  ],
  "Temporary Solutions": [
    "Avoid hard starts",
    "Drive gently"
  ]
},

"P0345": {
  "Actual Issue": "Camshaft Position Sensor Circuit Malfunction (Bank 2)",
  "Severity": "Medium to High (Similar to P0340; affects Bank 2)",
  "System": "Engine",
  "Category": "Sensor Circuit",
  "Possible Causes": [
    {"cause": "Faulty camshaft position sensor (Bank 2)", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Faulty sensor reluctor ring", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Engine misfire or rough idle",
    "Difficulty starting engine"
  ],
  "Diagnostics": [
    "Test camshaft position sensor (Bank 2)",
    "Inspect wiring and connectors",
    "Check sensor reluctor ring condition"
  ],
  "Fixes": [
    "Replace camshaft position sensor (Bank 2)",
    "Repair wiring or connectors",
    "Replace reluctor ring if damaged"
  ],
  "Temporary Solutions": [
    "Avoid hard starts",
    "Drive gently"
  ]
},

  "P0411": {
  "Actual Issue": "Secondary Air Injection System Incorrect Flow Detected",
  "Severity": "Medium (May cause emissions issues; repair recommended)",
  "System": "Emission Control",
  "Category": "Secondary Air Injection",
  "Possible Causes": [
    {"cause": "Faulty secondary air injection pump", "probability": 0.5},
    {"cause": "Blocked or damaged air injection hoses", "probability": 0.3},
    {"cause": "Faulty air injection check valve", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Failed emissions test",
    "Engine performance issues"
  ],
  "Diagnostics": [
    "Test secondary air injection pump operation",
    "Inspect air injection hoses for blockages or damage",
    "Check air injection check valve function"
  ],
  "Fixes": [
    "Replace secondary air injection pump",
    "Repair or replace air injection hoses",
    "Replace air injection check valve"
  ],
  "Temporary Solutions": [
    "Drive gently",
    "Avoid heavy engine loads"
  ]
},

"P0421": {
  "Actual Issue": "Catalyst System Efficiency Below Threshold (Bank 1)",
  "Severity": "High (Can cause emissions failure and fuel economy loss; prompt repair advised)",
  "System": "Emission Control",
  "Category": "Catalyst System",
  "Possible Causes": [
    {"cause": "Faulty catalytic converter", "probability": 0.5},
    {"cause": "Oxygen sensor malfunction", "probability": 0.3},
    {"cause": "Exhaust leaks", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Failed emissions test",
    "Poor fuel economy"
  ],
  "Diagnostics": [
    "Perform emissions test",
    "Test oxygen sensors",
    "Inspect exhaust system for leaks"
  ],
  "Fixes": [
    "Replace catalytic converter",
    "Replace oxygen sensors",
    "Repair exhaust leaks"
  ],
  "Temporary Solutions": [
    "Drive gently to reduce emissions",
    "Avoid heavy acceleration"
  ]
},

"P0441": {
  "Actual Issue": "Evaporative Emission Control System Incorrect Purge Flow",
  "Severity": "Medium (Affects emissions; repair recommended)",
  "System": "Emission Control",
  "Category": "Evaporative Emission System",
  "Possible Causes": [
    {"cause": "Faulty purge valve", "probability": 0.5},
    {"cause": "Blocked or damaged purge lines", "probability": 0.3},
    {"cause": "Faulty EVAP canister", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Fuel odor",
    "Poor engine performance"
  ],
  "Diagnostics": [
    "Test purge valve operation",
    "Inspect purge lines for blockages or damage",
    "Check EVAP canister condition"
  ],
  "Fixes": [
    "Replace purge valve",
    "Repair purge lines",
    "Replace EVAP canister"
  ],
  "Temporary Solutions": [
    "Avoid spilling fuel",
    "Minimize driving in hot conditions"
  ]
},

"P0456": {
  "Actual Issue": "Evaporative Emission System Leak Detected (Very Small Leak)",
  "Severity": "Low (Small leak, but can cause emissions failure; fix when possible)",
  "System": "Emission Control",
  "Category": "Evaporative Emission System",
  "Possible Causes": [
    {"cause": "Loose or damaged gas cap", "probability": 0.6},
    {"cause": "Small leaks in EVAP system hoses", "probability": 0.3},
    {"cause": "Faulty EVAP system components", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Fuel odor",
    "Failed emissions test"
  ],
  "Diagnostics": [
    "Check and tighten gas cap",
    "Inspect EVAP hoses for leaks",
    "Test EVAP system components"
  ],
  "Fixes": [
    "Tighten or replace gas cap",
    "Repair EVAP hoses",
    "Replace faulty EVAP components"
  ],
  "Temporary Solutions": [
    "Ensure gas cap is properly tightened",
    "Avoid frequent refueling stops"
  ]
},

"P0500": {
  "Actual Issue": "Vehicle Speed Sensor Malfunction",
  "Severity": "Medium (Affects speedometer and transmission; repair advised)",
  "System": "Vehicle Speed",
  "Category": "Sensor Malfunction",
  "Possible Causes": [
    {"cause": "Faulty vehicle speed sensor", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Damaged tone ring", "probability": 0.1}
  ],
  "Symptoms": [
    "Speedometer not working",
    "Transmission shifting problems",
    "Check Engine Light on"
  ],
  "Diagnostics": [
    "Test vehicle speed sensor output",
    "Inspect wiring and connectors",
    "Check tone ring condition"
  ],
  "Fixes": [
    "Replace vehicle speed sensor",
    "Repair wiring",
    "Replace tone ring if damaged"
  ],
  "Temporary Solutions": [
    "Drive cautiously without speedometer input",
    "Avoid high-speed driving"
  ]
},

"P0550": {
  "Actual Issue": "Auxiliary Vacuum Pump Control Circuit Malfunction",
  "Severity": "Medium (Impacts brake assist and HVAC; repair recommended)",
  "System": "Vacuum",
  "Category": "Auxiliary Vacuum Pump",
  "Possible Causes": [
    {"cause": "Faulty vacuum pump", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Faulty vacuum pump relay", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Brake assist or HVAC system issues",
    "Reduced vacuum assist"
  ],
  "Diagnostics": [
    "Test vacuum pump operation",
    "Inspect wiring and relay",
    "Check vacuum levels"
  ],
  "Fixes": [
    "Replace vacuum pump",
    "Repair wiring",
    "Replace vacuum pump relay"
  ],
  "Temporary Solutions": [
    "Drive gently to reduce brake assist demand",
    "Avoid heavy HVAC use"
  ]
},

"P0601": {
  "Actual Issue": "Internal Control Module Memory Check Sum Error",
  "Severity": "High (May cause intermittent electrical/vehicle issues; repair/reprogram needed)",
  "System": "Control Module",
  "Category": "Memory Checksum Error",
  "Possible Causes": [
    {"cause": "Faulty engine control module (ECM)", "probability": 0.6},
    {"cause": "Memory corruption", "probability": 0.3},
    {"cause": "Software issues", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Intermittent electrical issues",
    "Vehicle performance problems"
  ],
  "Diagnostics": [
    "Scan ECM for error codes",
    "Check ECM memory integrity",
    "Test ECM software"
  ],
  "Fixes": [
    "Reprogram ECM",
    "Replace ECM if reprogramming fails"
  ],
  "Temporary Solutions": [
    "Avoid rough driving",
    "Perform software resets if possible"
  ]
},

"P0602": {
  "Actual Issue": "Control Module Programming Error",
  "Severity": "High (ECM programming error can cause drivability problems; repair needed)",
  "System": "Control Module",
  "Category": "Programming Error",
  "Possible Causes": [
    {"cause": "Improper ECM programming", "probability": 0.7},
    {"cause": "Software corruption", "probability": 0.3}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "ECM malfunction",
    "Vehicle running issues"
  ],
  "Diagnostics": [
    "Verify ECM software version",
    "Check programming integrity"
  ],
  "Fixes": [
    "Reprogram ECM",
    "Replace ECM if reprogramming fails"
  ],
  "Temporary Solutions": [
    "Avoid complex driving conditions",
    "Perform software resets if supported"
  ]
},

"P0603": {
  "Actual Issue": "Internal Control Module Keep Alive Memory (KAM) Error",
  "Severity": "Medium to High (Memory errors cause intermittent issues; repair recommended)",
  "System": "Control Module",
  "Category": "Keep Alive Memory Error",
  "Possible Causes": [
    {"cause": "Faulty ECM", "probability": 0.7},
    {"cause": "Memory corruption", "probability": 0.3}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Intermittent electrical problems"
  ],
  "Diagnostics": [
    "Test ECM memory",
    "Inspect ECM wiring"
  ],
  "Fixes": [
    "Replace ECM",
    "Software update if available"
  ],
  "Temporary Solutions": [
    "Avoid frequent engine restarts",
    "Drive gently"
  ]
},

"P0705": {
  "Actual Issue": "Transmission Range Sensor Circuit Malfunction (PRNDL Input)",
  "Severity": "Medium to High (Can cause incorrect gear display and shifting issues; repair advised)",
  "System": "Transmission",
  "Category": "Sensor Circuit",
  "Possible Causes": [
    {"cause": "Faulty transmission range sensor", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Faulty transmission control module", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Incorrect gear display",
    "Transmission shifting problems"
  ],
  "Diagnostics": [
    "Test transmission range sensor",
    "Inspect wiring and connectors",
    "Scan transmission control module"
  ],
  "Fixes": [
    "Replace transmission range sensor",
    "Repair wiring",
    "Replace transmission control module if needed"
  ],
  "Temporary Solutions": [
    "Drive carefully avoiding gear shifts",
    "Use manual mode if available"
  ]
},

"P0715": {
  "Actual Issue": "Input/Turbine Speed Sensor Circuit Malfunction",
  "Severity": "Medium (Affects transmission shifting; repair recommended)",
  "System": "Transmission",
  "Category": "Sensor Circuit",
  "Possible Causes": [
    {"cause": "Faulty input speed sensor", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Faulty transmission control module", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Transmission shifting problems",
    "Poor acceleration"
  ],
  "Diagnostics": [
    "Test input speed sensor",
    "Inspect wiring and connectors",
    "Scan transmission control module"
  ],
  "Fixes": [
    "Replace input speed sensor",
    "Repair wiring",
    "Replace transmission control module if needed"
  ],
  "Temporary Solutions": [
    "Avoid aggressive acceleration",
    "Drive gently"
  ]
},

"P0720": {
  "Actual Issue": "Output Speed Sensor Circuit Malfunction",
  "Severity": "Medium (Impacts transmission shifting; repair recommended)",
  "System": "Transmission",
  "Category": "Sensor Circuit",
  "Possible Causes": [
    {"cause": "Faulty output speed sensor", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Faulty transmission control module", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Transmission shifting problems",
    "Poor acceleration"
  ],
  "Diagnostics": [
    "Test output speed sensor",
    "Inspect wiring and connectors",
    "Scan transmission control module"
  ],
  "Fixes": [
    "Replace output speed sensor",
    "Repair wiring",
    "Replace transmission control module if needed"
  ],
  "Temporary Solutions": [
    "Avoid aggressive acceleration",
    "Drive gently"
  ]
},

  "P0731": {
  "Actual Issue": "Gear 1 Incorrect Ratio",
  "Severity": "High (Can cause harsh shifting and drivability issues; timely repair advised)",
  "System": "Transmission",
  "Category": "Gear Ratio",
  "Possible Causes": [
    {"cause": "Worn or damaged transmission bands or clutches", "probability": 0.5},
    {"cause": "Faulty shift solenoids", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Harsh or incorrect shifting",
    "Poor acceleration"
  ],
  "Diagnostics": [
    "Check transmission fluid level and condition",
    "Test shift solenoids",
    "Inspect transmission bands and clutches"
  ],
  "Fixes": [
    "Replace or repair shift solenoids",
    "Repair or replace transmission bands/clutches",
    "Check and refill transmission fluid"
  ],
  "Temporary Solutions": [
    "Avoid hard acceleration and shifting",
    "Drive gently"
  ]
},

"P0732": {
  "Actual Issue": "Gear 2 Incorrect Ratio",
  "Severity": "High (May cause transmission slipping and rough shifts; repair recommended)",
  "System": "Transmission",
  "Category": "Gear Ratio",
  "Possible Causes": [
    {"cause": "Worn or damaged transmission bands or clutches", "probability": 0.5},
    {"cause": "Faulty shift solenoids", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Harsh or incorrect shifting",
    "Poor acceleration"
  ],
  "Diagnostics": [
    "Check transmission fluid level and condition",
    "Test shift solenoids",
    "Inspect transmission bands and clutches"
  ],
  "Fixes": [
    "Replace or repair shift solenoids",
    "Repair or replace transmission bands/clutches",
    "Check and refill transmission fluid"
  ],
  "Temporary Solutions": [
    "Avoid hard acceleration and shifting",
    "Drive gently"
  ]
},

"P0733": {
  "Actual Issue": "Gear 3 Incorrect Ratio",
  "Severity": "High (Causes shifting problems and drivability issues; timely repair advised)",
  "System": "Transmission",
  "Category": "Gear Ratio",
  "Possible Causes": [
    {"cause": "Worn or damaged transmission bands or clutches", "probability": 0.5},
    {"cause": "Faulty shift solenoids", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Harsh or incorrect shifting",
    "Poor acceleration"
  ],
  "Diagnostics": [
    "Check transmission fluid level and condition",
    "Test shift solenoids",
    "Inspect transmission bands and clutches"
  ],
  "Fixes": [
    "Replace or repair shift solenoids",
    "Repair or replace transmission bands/clutches",
    "Check and refill transmission fluid"
  ],
  "Temporary Solutions": [
    "Avoid hard acceleration and shifting",
    "Drive gently"
  ]
},

"P0734": {
  "Actual Issue": "Gear 4 Incorrect Ratio",
  "Severity": "High (Impacts smooth shifting and performance; repair recommended)",
  "System": "Transmission",
  "Category": "Gear Ratio",
  "Possible Causes": [
    {"cause": "Worn or damaged transmission bands or clutches", "probability": 0.5},
    {"cause": "Faulty shift solenoids", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Harsh or incorrect shifting",
    "Poor acceleration"
  ],
  "Diagnostics": [
    "Check transmission fluid level and condition",
    "Test shift solenoids",
    "Inspect transmission bands and clutches"
  ],
  "Fixes": [
    "Replace or repair shift solenoids",
    "Repair or replace transmission bands/clutches",
    "Check and refill transmission fluid"
  ],
  "Temporary Solutions": [
    "Avoid hard acceleration and shifting",
    "Drive gently"
  ]
},

"P0735": {
  "Actual Issue": "Gear 5 Incorrect Ratio",
  "Severity": "High (Affects top gear performance; repair needed for smooth operation)",
  "System": "Transmission",
  "Category": "Gear Ratio",
  "Possible Causes": [
    {"cause": "Worn or damaged transmission bands or clutches", "probability": 0.5},
    {"cause": "Faulty shift solenoids", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Harsh or incorrect shifting",
    "Poor acceleration"
  ],
  "Diagnostics": [
    "Check transmission fluid level and condition",
    "Test shift solenoids",
    "Inspect transmission bands and clutches"
  ],
  "Fixes": [
    "Replace or repair shift solenoids",
    "Repair or replace transmission bands/clutches",
    "Check and refill transmission fluid"
  ],
  "Temporary Solutions": [
    "Avoid hard acceleration and shifting",
    "Drive gently"
  ]
},

"P0736": {
  "Actual Issue": "Reverse Gear Incorrect Ratio",
  "Severity": "High (Can cause reverse gear issues and safety risks; repair promptly)",
  "System": "Transmission",
  "Category": "Gear Ratio",
  "Possible Causes": [
    {"cause": "Worn or damaged transmission bands or clutches", "probability": 0.5},
    {"cause": "Faulty shift solenoids", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.2}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Harsh or incorrect shifting into reverse",
    "Poor reverse performance"
  ],
  "Diagnostics": [
    "Check transmission fluid level and condition",
    "Test shift solenoids",
    "Inspect transmission bands and clutches"
  ],
  "Fixes": [
    "Replace or repair shift solenoids",
    "Repair or replace transmission bands/clutches",
    "Check and refill transmission fluid"
  ],
  "Temporary Solutions": [
    "Avoid hard acceleration and shifting",
    "Drive gently"
  ]
},

"P0756": {
  "Actual Issue": "Shift Solenoid B Performance or Stuck Off",
  "Severity": "Medium to High (Causes shifting delays or stuck gears; repair recommended)",
  "System": "Transmission",
  "Category": "Shift Solenoid",
  "Possible Causes": [
    {"cause": "Faulty shift solenoid B", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Transmission stuck in gear",
    "Delayed or harsh shifting"
  ],
  "Diagnostics": [
    "Test shift solenoid B operation",
    "Inspect wiring and connectors",
    "Check transmission fluid level"
  ],
  "Fixes": [
    "Replace shift solenoid B",
    "Repair wiring",
    "Check and refill transmission fluid"
  ],
  "Temporary Solutions": [
    "Avoid aggressive driving",
    "Drive gently"
  ]
},

"P0775": {
  "Actual Issue": "Shift Solenoid D Performance or Stuck Off",
  "Severity": "Medium to High (Causes shifting issues; repair advised)",
  "System": "Transmission",
  "Category": "Shift Solenoid",
  "Possible Causes": [
    {"cause": "Faulty shift solenoid D", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Transmission stuck in gear",
    "Delayed or harsh shifting"
  ],
  "Diagnostics": [
    "Test shift solenoid D operation",
    "Inspect wiring and connectors",
    "Check transmission fluid level"
  ],
  "Fixes": [
    "Replace shift solenoid D",
    "Repair wiring",
    "Check and refill transmission fluid"
  ],
  "Temporary Solutions": [
    "Avoid aggressive driving",
    "Drive gently"
  ]
},

"P0785": {
  "Actual Issue": "Shift to Reverse or Park Inhibited",
  "Severity": "High (Prevents shifting to critical gears; safety concern, repair promptly)",
  "System": "Transmission",
  "Category": "Shift Control",
  "Possible Causes": [
    {"cause": "Faulty transmission range sensor", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Transmission control module malfunction", "probability": 0.1}
  ],
  "Symptoms": [
    "Unable to shift into reverse or park",
    "Check Engine Light on",
    "Transmission stuck in gear"
  ],
  "Diagnostics": [
    "Test transmission range sensor",
    "Inspect wiring and connectors",
    "Scan transmission control module"
  ],
  "Fixes": [
    "Replace transmission range sensor",
    "Repair wiring",
    "Replace transmission control module if needed"
  ],
  "Temporary Solutions": [
    "Avoid shifting frequently",
    "Drive carefully"
  ]
},

"P0795": {
  "Actual Issue": "Pressure Control Solenoid Malfunction",
  "Severity": "Medium to High (Can cause slipping and harsh shifting; repair recommended)",
  "System": "Transmission",
  "Category": "Pressure Control",
  "Possible Causes": [
    {"cause": "Faulty pressure control solenoid", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Low transmission fluid", "probability": 0.1}
  ],
  "Symptoms": [
    "Check Engine Light on",
    "Transmission slipping",
    "Harsh shifting"
  ],
  "Diagnostics": [
    "Test pressure control solenoid",
    "Inspect wiring and connectors",
    "Check transmission fluid level"
  ],
  "Fixes": [
    "Replace pressure control solenoid",
    "Repair wiring",
    "Check and refill transmission fluid"
  ],
  "Temporary Solutions": [
    "Avoid aggressive acceleration",
    "Drive gently"
  ]
},

"P0801": {
  "Actual Issue": "Reverse Inhibit Control Circuit Malfunction",
  "Severity": "High (Prevents safe shifting to reverse; repair promptly)",
  "System": "Transmission",
  "Category": "Reverse Inhibit Control",
  "Possible Causes": [
    {"cause": "Faulty reverse inhibit switch", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Transmission control module malfunction", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test reverse inhibit switch operation",
    "Inspect wiring and connectors",
    "Scan transmission control module for faults"
  ],
  "Fixes": [
    "Replace reverse inhibit switch",
    "Repair wiring",
    "Replace transmission control module if needed"
  ],
  "Temporary Solutions": [
    "Avoid shifting into reverse until fixed",
    "Drive cautiously avoiding gear shifts"
  ]
},

"P0805": {
  "Actual Issue": "Clutch Position Sensor Circuit Malfunction",
  "Severity": "Medium (Affects clutch operation; repair recommended)",
  "System": "Transmission",
  "Category": "Sensor Circuit",
  "Possible Causes": [
    {"cause": "Faulty clutch position sensor", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.4}
  ],
  "Diagnostics": [
    "Test clutch position sensor output",
    "Inspect wiring and connectors"
  ],
  "Fixes": [
    "Replace clutch position sensor",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Avoid hard shifting",
    "Drive gently until repaired"
  ]
},

"P0830": {
  "Actual Issue": "Clutch Pedal Position Sensor Circuit Malfunction",
  "Severity": "Medium (Impacts clutch pedal sensing; timely repair advised)",
  "System": "Transmission",
  "Category": "Sensor Circuit",
  "Possible Causes": [
    {"cause": "Faulty clutch pedal position sensor", "probability": 0.5},
    {"cause": "Wiring or connector issues", "probability": 0.3},
    {"cause": "Sensor misalignment", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test sensor signals",
    "Inspect wiring and connectors",
    "Check sensor alignment and adjust if needed"
  ],
  "Fixes": [
    "Replace clutch pedal position sensor",
    "Repair wiring/connectors",
    "Realign or adjust sensor"
  ],
  "Temporary Solutions": [
    "Avoid aggressive clutch use",
    "Drive smoothly"
  ]
},
  "P0841": {
  "Actual Issue": "Transmission Fluid Pressure Sensor Circuit Range/Performance",
  "System": "Transmission",
  "Category": "Sensor Circuit",
  "Severity": "Medium (Important to diagnose soon to prevent transmission damage)",
  "Possible Causes": [
    {"cause": "Faulty transmission fluid pressure sensor", "probability": 0.5},
    {"cause": "Wiring or connector faults", "probability": 0.3},
    {"cause": "Low or dirty transmission fluid", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test transmission fluid pressure sensor",
    "Inspect wiring/connectors",
    "Check transmission fluid level and quality"
  ],
  "Fixes": [
    "Replace transmission fluid pressure sensor",
    "Repair wiring/connectors",
    "Change or refill transmission fluid"
  ],
  "Temporary Solutions": [
    "Drive gently to reduce transmission stress",
    "Avoid towing or heavy loads"
  ]
},
"P0850": {
  "Actual Issue": "Transmission Fluid Pressure Sensor Circuit Malfunction",
  "System": "Transmission",
  "Category": "Sensor Circuit",
  "Severity": "Medium (Risk of transmission issues if not repaired promptly)",
  "Possible Causes": [
    {"cause": "Faulty transmission fluid pressure sensor", "probability": 0.5},
    {"cause": "Damaged wiring or connectors", "probability": 0.3},
    {"cause": "Low transmission fluid level", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test sensor operation",
    "Inspect wiring and connectors",
    "Check transmission fluid level"
  ],
  "Fixes": [
    "Replace sensor",
    "Repair wiring/connectors",
    "Refill transmission fluid"
  ],
  "Temporary Solutions": [
    "Drive gently and avoid high load",
    "Monitor transmission temperature"
  ]
},
"P0868": {
  "Actual Issue": "Transmission Fluid Pressure Low",
  "System": "Transmission",
  "Category": "Fluid Pressure",
  "Severity": "High (Low pressure can cause severe transmission damage; repair urgently)",
  "Possible Causes": [
    {"cause": "Low or dirty transmission fluid", "probability": 0.5},
    {"cause": "Faulty transmission fluid pump", "probability": 0.3},
    {"cause": "Blocked transmission fluid passages", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check fluid level and condition",
    "Test transmission fluid pump pressure",
    "Inspect fluid passages for blockage"
  ],
  "Fixes": [
    "Replace or flush transmission fluid",
    "Repair or replace transmission fluid pump",
    "Clean or flush fluid passages"
  ],
  "Temporary Solutions": [
    "Avoid aggressive driving",
    "Drive gently to reduce transmission load"
  ]
},
"P0870": {
  "Actual Issue": "Transmission Fluid Pressure High",
  "System": "Transmission",
  "Category": "Fluid Pressure",
  "Severity": "Medium (High pressure can cause transmission wear; diagnosis needed)",
  "Possible Causes": [
    {"cause": "Blocked transmission fluid passages", "probability": 0.4},
    {"cause": "Faulty pressure control valve", "probability": 0.4},
    {"cause": "Excessive transmission fluid level", "probability": 0.2}
  ],
  "Diagnostics": [
    "Inspect fluid passages",
    "Test pressure control valve",
    "Check transmission fluid level"
  ],
  "Fixes": [
    "Flush fluid passages",
    "Replace pressure control valve",
    "Adjust fluid level"
  ],
  "Temporary Solutions": [
    "Avoid high RPMs and heavy loads",
    "Drive smoothly"
  ]
},

  "P0986": {
  "Actual Issue": "EGR Valve Position Sensor Circuit Malfunction",
  "System": "Emission Control",
  "Category": "Sensor Circuit",
  "Severity": "Medium (Timely repair advised to maintain emissions and engine performance)",
  "Possible Causes": [
    {"cause": "Faulty EGR valve position sensor", "probability": 0.5},
    {"cause": "Wiring or connector problems", "probability": 0.3},
    {"cause": "Stuck or faulty EGR valve", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test EGR valve position sensor",
    "Inspect wiring/connectors",
    "Check EGR valve operation"
  ],
  "Fixes": [
    "Replace sensor",
    "Repair wiring/connectors",
    "Clean or replace EGR valve"
  ],
  "Temporary Solutions": [
    "Avoid aggressive acceleration",
    "Drive gently"
  ]
},

"P1000": {
  "Actual Issue": "OBD Systems Readiness Test Not Complete",
  "System": "OBD",
  "Category": "System Readiness",
  "Severity": "Low (No direct mechanical impact; complete drive cycle to clear)",
  "Possible Causes": [
    {"cause": "Recently cleared diagnostic codes", "probability": 0.5},
    {"cause": "Vehicle not driven long enough for tests", "probability": 0.3},
    {"cause": "Pending repairs", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check readiness monitor status",
    "Review recent code clearing history",
    "Complete drive cycle"
  ],
  "Fixes": [
    "Drive vehicle through complete drive cycle",
    "Complete all pending repairs"
  ],
  "Temporary Solutions": [
    "Drive vehicle as recommended by manufacturer"
  ]
},

"P1101": {
  "Actual Issue": "Mass Air Flow Sensor Out of Self-Test Range",
  "System": "Engine",
  "Category": "Sensor",
  "Severity": "Medium (May affect engine performance and emissions; prompt repair recommended)",
  "Possible Causes": [
    {"cause": "Faulty mass air flow sensor", "probability": 0.5},
    {"cause": "Dirty or contaminated sensor", "probability": 0.3},
    {"cause": "Wiring or connector issues", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test mass air flow sensor signal with scan tool",
    "Inspect and clean sensor",
    "Check wiring and connectors for damage"
  ],
  "Fixes": [
    "Clean or replace mass air flow sensor",
    "Repair wiring/connectors"
  ],
  "Temporary Solutions": [
    "Avoid high engine loads",
    "Drive gently until repaired"
  ]
},

"P1121": {
  "Actual Issue": "Throttle Position Sensor Circuit Range/Performance",
  "System": "Engine",
  "Category": "Sensor Circuit",
  "Severity": "Medium (Throttle issues can cause drivability problems; repair advised)",
  "Possible Causes": [
    {"cause": "Faulty throttle position sensor", "probability": 0.5},
    {"cause": "Wiring or connector issues", "probability": 0.3},
    {"cause": "Sensor misalignment", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test throttle position sensor voltage and signal",
    "Inspect wiring and connectors",
    "Check sensor alignment"
  ],
  "Fixes": [
    "Replace throttle position sensor",
    "Repair wiring/connectors",
    "Adjust or calibrate sensor"
  ],
  "Temporary Solutions": [
    "Avoid rapid acceleration",
    "Drive cautiously"
  ]
},

"P1151": {
  "Actual Issue": "Oxygen Sensor Heater Resistance High (Bank 1 Sensor 1)",
  "System": "Engine",
  "Category": "Oxygen Sensor Heater",
  "Severity": "Low (Impacts sensor efficiency; monitor and repair to maintain emissions control)",
  "Possible Causes": [
    {"cause": "Faulty oxygen sensor heater circuit", "probability": 0.5},
    {"cause": "Damaged wiring or connectors", "probability": 0.3},
    {"cause": "Failed oxygen sensor", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test oxygen sensor heater resistance",
    "Inspect wiring and connectors",
    "Check oxygen sensor function"
  ],
  "Fixes": [
    "Replace oxygen sensor",
    "Repair wiring/connectors"
  ],
  "Temporary Solutions": [
    "Drive gently to avoid rich or lean conditions",
    "Avoid extended idling"
  ]
},

"P1259": {
  "Actual Issue": "Injector Circuit Malfunction",
  "System": "Fuel",
  "Category": "Injector Circuit",
  "Severity": "High (Fuel injector issues affect engine performance; fix promptly)",
  "Possible Causes": [
    {"cause": "Faulty fuel injector", "probability": 0.5},
    {"cause": "Wiring or connector issues", "probability": 0.3},
    {"cause": "Faulty injector control module", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test fuel injector operation",
    "Inspect wiring and connectors",
    "Scan injector control module"
  ],
  "Fixes": [
    "Replace or repair fuel injector",
    "Repair wiring/connectors",
    "Replace injector control module if needed"
  ],
  "Temporary Solutions": [
    "Avoid heavy acceleration",
    "Drive smoothly"
  ]
},
"P0449": {
  "Actual Issue": "Evaporative Emission System Vent Valve/Solenoid Circuit Malfunction",
  "Severity": "Low (Primarily emissions related; timely repair recommended to avoid fuel vapor leaks)",
  "Possible Causes": [
    {"cause": "Faulty vent valve/solenoid", "probability": 0.4},
    {"cause": "Damaged or disconnected wiring", "probability": 0.3},
    {"cause": "Faulty EVAP canister", "probability": 0.2},
    {"cause": "PCM failure", "probability": 0.1}
  ],
  "Diagnostics": [
    "Check vent valve operation and resistance",
    "Inspect EVAP wiring harness for damage",
    "Test EVAP canister for blockage",
    "Scan PCM for additional codes"
  ],
  "Fixes": [
    "Replace faulty vent valve or solenoid",
    "Repair or replace damaged wiring",
    "Replace EVAP canister if needed",
    "Reprogram or replace PCM"
  ],
  "Temporary Solutions": [
    "Clear the code and tighten gas cap if loose"
  ]
},

"P0452": {
  "Actual Issue": "Evaporative Emission Control System Pressure Sensor Low Input",
  "Severity": "Low (Emissions related; no immediate impact on drivability)",
  "Possible Causes": [
    {"cause": "Faulty pressure sensor", "probability": 0.5},
    {"cause": "Shorted or open EVAP sensor circuit", "probability": 0.3},
    {"cause": "Faulty PCM", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test EVAP pressure sensor with scan tool",
    "Inspect wiring and connectors",
    "Check voltage and ground to sensor"
  ],
  "Fixes": [
    "Replace pressure sensor",
    "Repair wiring",
    "Replace PCM if necessary"
  ],
  "Temporary Solutions": [
    "Clear codes and monitor for return"
  ]
},

"P0453": {
  "Actual Issue": "Evaporative Emission Control System Pressure Sensor High Input",
  "Severity": "Low (Emissions system fault; repair to prevent fuel vapor leaks)",
  "Possible Causes": [
    {"cause": "Faulty pressure sensor", "probability": 0.5},
    {"cause": "Wiring short to voltage", "probability": 0.3},
    {"cause": "Clogged EVAP vent line", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check sensor readings using a scan tool",
    "Inspect wiring for shorts",
    "Check EVAP lines for blockage"
  ],
  "Fixes": [
    "Replace faulty sensor",
    "Repair shorted wiring",
    "Clear or replace vent line"
  ],
  "Temporary Solutions": [
    "Tighten gas cap and clear codes"
  ]
},

"P0463": {
  "Actual Issue": "Fuel Level Sensor Circuit High Input",
  "Severity": "Low (Fuel gauge fault; may cause inaccurate fuel readings)",
  "Possible Causes": [
    {"cause": "Faulty fuel level sensor", "probability": 0.5},
    {"cause": "Wiring issue in fuel level circuit", "probability": 0.3},
    {"cause": "PCM failure", "probability": 0.2}
  ],
  "Diagnostics": [
    "Use scan tool to monitor fuel level readings",
    "Inspect sensor wiring and connectors",
    "Test sensor resistance"
  ],
  "Fixes": [
    "Replace fuel level sensor",
    "Repair circuit wiring",
    "Replace PCM if required"
  ],
  "Temporary Solutions": [
    "Keep tank above half and monitor mileage"
  ]
},

"P0496": {
  "Actual Issue": "EVAP Flow During Non-Purge Condition",
  "Severity": "Medium (Potential fuel vapor leak; emissions fault requiring repair)",
  "Possible Causes": [
    {"cause": "Faulty purge valve", "probability": 0.4},
    {"cause": "Leaking EVAP canister", "probability": 0.3},
    {"cause": "Stuck open purge solenoid", "probability": 0.2},
    {"cause": "PCM issue", "probability": 0.1}
  ],
  "Diagnostics": [
    "Test purge valve operation with a vacuum pump",
    "Inspect canister for leaks",
    "Use scan tool to monitor purge command",
    "Check for related EVAP codes"
  ],
  "Fixes": [
    "Replace purge valve or solenoid",
    "Replace leaking EVAP canister",
    "Reprogram or replace PCM"
  ],
  "Temporary Solutions": [
    "Clear code and monitor fuel system performance"
  ]
},

"P0520": {
  "Actual Issue": "Engine Oil Pressure Sensor/Switch Circuit Malfunction",
  "Severity": "High (Oil pressure faults can cause severe engine damage; immediate attention required)",
  "Possible Causes": [
    {"cause": "Faulty oil pressure sensor", "probability": 0.4},
    {"cause": "Low oil level or pressure", "probability": 0.3},
    {"cause": "Wiring issues", "probability": 0.2},
    {"cause": "Oil pump failure", "probability": 0.1}
  ],
  "Diagnostics": [
    "Check oil level and quality",
    "Test oil pressure with mechanical gauge",
    "Inspect sensor wiring"
  ],
  "Fixes": [
    "Replace oil pressure sensor",
    "Top up or change oil",
    "Repair wiring or replace oil pump"
  ],
  "Temporary Solutions": [
    "Add oil if low and reset code"
  ]
},

"P0522": {
  "Actual Issue": "Engine Oil Pressure Sensor/Switch Low Voltage",
  "Severity": "High (Critical oil pressure warning; risk of engine damage if ignored)",
  "Possible Causes": [
    {"cause": "Faulty sensor", "probability": 0.5},
    {"cause": "Low oil pressure", "probability": 0.3},
    {"cause": "Open circuit in sensor wiring", "probability": 0.2}
  ],
  "Diagnostics": [
    "Measure voltage at sensor",
    "Check oil pressure with a mechanical gauge",
    "Inspect sensor wiring for damage or disconnection"
  ],
  "Fixes": [
    "Replace oil pressure sensor",
    "Repair or replace damaged wiring",
    "Correct oil level or oil pressure issues"
  ],
  "Temporary Solutions": [
    "Top off engine oil and reset ECU"
  ]
},

"P0562": {
  "Actual Issue": "System Voltage Low",
  "Severity": "Medium (Low voltage can cause multiple system issues; repair recommended)",
  "Possible Causes": [
    {"cause": "Weak battery", "probability": 0.5},
    {"cause": "Faulty alternator", "probability": 0.3},
    {"cause": "Poor charging system connection", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test battery voltage and alternator output",
    "Check for loose or corroded battery and alternator connections",
    "Scan for additional charging system-related codes"
  ],
  "Fixes": [
    "Replace battery or alternator as needed",
    "Clean and tighten battery and alternator connections",
    "Repair charging system wiring"
  ],
  "Temporary Solutions": [
    "Jump-start the vehicle and drive to recharge battery"
  ]
},

"P0563": {
  "Actual Issue": "System Voltage High",
  "Severity": "Medium (High voltage may damage components; repair advised)",
  "Possible Causes": [
    {"cause": "Faulty voltage regulator", "probability": 0.5},
    {"cause": "Overcharging alternator", "probability": 0.3},
    {"cause": "Wiring issues", "probability": 0.2}
  ],
  "Diagnostics": [
    "Measure charging voltage with a multimeter",
    "Check alternator and voltage regulator functionality",
    "Inspect wiring for damage or shorts"
  ],
  "Fixes": [
    "Replace voltage regulator or alternator",
    "Repair damaged wiring",
    "Reprogram PCM if applicable"
  ],
  "Temporary Solutions": [
    "Disconnect battery briefly to reset the system"
  ]
},

"P0597": {
  "Actual Issue": "Thermostat Heater Control Circuit/Open",
  "System": "Engine Cooling",
  "Category": "Electrical",
  "Severity": "Low (May cause slow warm-up and reduced efficiency; repair recommended)",
  "Symptoms": [
    "Engine takes too long to warm up",
    "Poor fuel economy",
    "Check Engine Light on"
  ],
  "Possible Causes": [
    {"cause": "Open or shorted thermostat heater circuit", "probability": 0.5},
    {"cause": "Faulty thermostat", "probability": 0.3},
    {"cause": "Wiring issues", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check thermostat heater resistance with a multimeter",
    "Inspect wiring and connectors for damage",
    "Use scan tool to monitor engine temperature readings"
  ],
  "Fixes": [
    "Replace faulty thermostat",
    "Repair wiring or connectors"
  ],
  "Temporary Solutions": [
    "Allow engine to warm up longer before driving"
  ]
},

  "P0610": {
    "Actual Issue": "Control Module Vehicle Options Error",
    "Severity": "Medium (Can affect transmission and drivability; reprogramming may be needed)",
    "System": "Powertrain Control Module (PCM)",
    "Category": "Configuration",
    "Symptoms": [
      "Improper transmission behavior",
      "Check Engine Light on"
    ],
    "Possible Causes": [
      {"cause": "Incorrect PCM programming", "probability": 0.6},
      {"cause": "Faulty PCM", "probability": 0.4}
    ],
    "Diagnostics": [
      "Verify PCM calibration and VIN matching",
      "Scan for related module codes"
    ],
    "Fixes": [
      "Reprogram or replace PCM"
    ],
    "Temporary Solutions": [
      "Reset codes and retest"
    ]
  },
  "P0615": {
    "Actual Issue": "Starter Relay Circuit",
    "Severity": "High (Prevents engine start; immediate attention required)",
    "System": "Starting System",
    "Category": "Electrical",
    "Symptoms": [
      "Engine won’t crank",
      "Clicking noise when turning key"
    ],
    "Possible Causes": [
      {"cause": "Faulty starter relay", "probability": 0.5},
      {"cause": "Wiring issue", "probability": 0.3},
      {"cause": "PCM not sending start signal", "probability": 0.2}
    ],
    "Diagnostics": [
      "Test starter relay function",
      "Check for voltage at starter relay terminal",
      "Inspect wiring continuity"
    ],
    "Fixes": [
      "Replace starter relay",
      "Repair wiring"
    ],
    "Temporary Solutions": [
      "Try jump-starting vehicle"
    ]
  },
  "P0620": {
    "Actual Issue": "Generator Control Circuit Malfunction",
    "Severity": "High (Leads to battery drain or stalling; fix as soon as possible)",
    "System": "Charging System",
    "Category": "Electrical",
    "Symptoms": [
      "Battery warning light on dashboard",
      "Dead battery",
      "Engine stalls"
    ],
    "Possible Causes": [
      {"cause": "Faulty alternator", "probability": 0.5},
      {"cause": "Broken wiring", "probability": 0.3},
      {"cause": "Faulty PCM", "probability": 0.2}
    ],
    "Diagnostics": [
      "Test alternator output voltage and current",
      "Inspect generator control circuit wiring"
    ],
    "Fixes": [
      "Replace alternator",
      "Repair wiring",
      "Replace PCM if necessary"
    ],
    "Temporary Solutions": [
      "Limit electrical usage until repair"
    ]
  },
  "P0627": {
    "Actual Issue": "Fuel Pump A Control Circuit / Open",
    "Severity": "High (Engine may not start or lose power; critical for drivability)",
    "System": "Fuel System",
    "Category": "Electrical",
    "Symptoms": [
      "Engine won’t start",
      "No fuel pressure"
    ],
    "Possible Causes": [
      {"cause": "Open fuel pump circuit", "probability": 0.5},
      {"cause": "Faulty fuel pump", "probability": 0.3},
      {"cause": "Faulty PCM", "probability": 0.2}
    ],
    "Diagnostics": [
      "Check for voltage at fuel pump connector",
      "Inspect fuel pump wiring and relay"
    ],
    "Fixes": [
      "Repair fuel pump circuit wiring",
      "Replace fuel pump"
    ],
    "Temporary Solutions": [
      "Cycle ignition key to prime fuel system"
    ]
  },
  "P0650": {
    "Actual Issue": "Malfunction Indicator Lamp (MIL) Control Circuit Malfunction",
    "Severity": "Low (May cause emissions test failure or delayed detection of other issues)",
    "System": "Instrument Cluster",
    "Category": "Electrical",
    "Symptoms": [
      "Check Engine Light does not illuminate",
      "Fails emissions test"
    ],
    "Possible Causes": [
      {"cause": "Burnt out MIL bulb", "probability": 0.5},
      {"cause": "Faulty PCM", "probability": 0.3},
      {"cause": "Open circuit", "probability": 0.2}
    ],
    "Diagnostics": [
      "Test MIL bulb",
      "Check PCM output for MIL control"
    ],
    "Fixes": [
      "Replace bulb",
      "Repair wiring",
      "Replace PCM"
    ],
    "Temporary Solutions": [
      "Use scan tool to monitor codes without MIL"
    ]
  },

  "P0685": {
  "Actual Issue": "ECM/PCM Power Relay Control Circuit/Open",
  "Severity": "High (May lead to stalling or complete no-start condition)",
  "System": "Powertrain",
  "Category": "ECM/PCM Control",
  "Symptoms": [
    "No start or hard start",
    "Engine stalling",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Faulty ECM/PCM relay", "probability": 0.4},
    {"cause": "Blown fuse", "probability": 0.3},
    {"cause": "Wiring or connector issues", "probability": 0.2},
    {"cause": "Faulty ECM/PCM", "probability": 0.1}
  ],
  "Diagnostics": [
    "Check power relay operation",
    "Inspect fuse and wiring continuity",
    "Test for voltage at control circuit",
    "Scan for related DTCs"
  ],
  "Fixes": [
    "Replace ECM/PCM relay if faulty",
    "Repair or replace damaged wiring or fuse",
    "Replace ECM/PCM if confirmed defective"
  ],
  "Temporary Solutions": [
    "Reset relay and check fuse connections"
  ]
},

"P0706": {
  "Actual Issue": "Transmission Range Sensor Circuit Range/Performance",
  "Severity": "Medium (May cause drivability issues; repair soon)",
  "System": "Transmission",
  "Category": "Sensor",
  "Symptoms": [
    "Transmission not shifting correctly",
    "Gear indicator malfunction",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Faulty transmission range sensor", "probability": 0.4},
    {"cause": "Wiring harness issues", "probability": 0.3},
    {"cause": "Misaligned gear shifter", "probability": 0.2},
    {"cause": "Faulty TCM", "probability": 0.1}
  ],
  "Diagnostics": [
    "Check sensor alignment and resistance",
    "Inspect wiring and connectors",
    "Use scan tool to monitor range sensor output"
  ],
  "Fixes": [
    "Replace or adjust transmission range sensor",
    "Repair damaged wiring or connectors",
    "Recalibrate or replace TCM if necessary"
  ],
  "Temporary Solutions": [
    "Wiggle shifter into gear manually until fixed"
  ]
},

"P0710": {
  "Actual Issue": "Transmission Fluid Temperature Sensor Circuit Malfunction",
  "Severity": "Medium (May lead to erratic shifting and overheating)",
  "System": "Transmission",
  "Category": "Sensor",
  "Symptoms": [
    "Harsh or delayed shifting",
    "Transmission overheating",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Faulty temperature sensor", "probability": 0.4},
    {"cause": "Wiring or connector damage", "probability": 0.3},
    {"cause": "Low or dirty transmission fluid", "probability": 0.2},
    {"cause": "TCM issues", "probability": 0.1}
  ],
  "Diagnostics": [
    "Monitor temperature sensor readings with scan tool",
    "Check fluid condition",
    "Test sensor resistance"
  ],
  "Fixes": [
    "Replace fluid and filter",
    "Repair or replace sensor",
    "Repair damaged wiring"
  ],
  "Temporary Solutions": [
    "Let vehicle cool before driving if overheated"
  ]
},

"P0717": {
  "Actual Issue": "Input/Turbine Speed Sensor No Signal",
  "Severity": "High (Impacts gear shifting and speed sensing; fix promptly)",
  "System": "Transmission",
  "Category": "Sensor",
  "Symptoms": [
    "Transmission slips or does not shift",
    "Speedometer malfunction",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Failed speed sensor", "probability": 0.4},
    {"cause": "Wiring or connector fault", "probability": 0.3},
    {"cause": "Internal transmission problem", "probability": 0.2},
    {"cause": "Faulty TCM", "probability": 0.1}
  ],
  "Diagnostics": [
    "Use scan tool to check input sensor data",
    "Check sensor wiring continuity",
    "Test sensor with multimeter"
  ],
  "Fixes": [
    "Replace input speed sensor",
    "Repair wiring or connector",
    "Replace or service TCM if needed"
  ],
  "Temporary Solutions": [
    "Drive in manual mode if available"
  ]
},

"P0725": {
  "Actual Issue": "Engine Speed Input Circuit Malfunction",
  "Severity": "High (Affects engine-transmission coordination; repair urgently)",
  "System": "Transmission",
  "Category": "Sensor",
  "Symptoms": [
    "Erratic shifting",
    "Loss of power",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Crankshaft position sensor failure", "probability": 0.5},
    {"cause": "Wiring harness issue", "probability": 0.3},
    {"cause": "Faulty ECM or TCM", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check crankshaft sensor signal with scan tool",
    "Inspect wiring and ground connections",
    "Test sensor resistance"
  ],
  "Fixes": [
    "Replace crankshaft position sensor",
    "Repair damaged circuits",
    "Replace ECM/TCM if confirmed bad"
  ],
  "Temporary Solutions": [
    "Restart vehicle to clear temporary glitch"
  ]
},

"P0741": {
  "Actual Issue": "Torque Converter Clutch Circuit Performance/Stuck Off",
  "Severity": "Medium (Affects fuel economy and transmission performance)",
  "System": "Transmission",
  "Category": "Torque Converter",
  "Symptoms": [
    "Poor fuel economy",
    "Overheating transmission",
    "High RPM at highway speeds",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Faulty torque converter clutch solenoid", "probability": 0.5},
    {"cause": "Wiring or connector fault", "probability": 0.3},
    {"cause": "Internal transmission fault", "probability": 0.2}
  ],
  "Diagnostics": [
    "Monitor TCC lockup via scan tool",
    "Check solenoid resistance",
    "Inspect fluid condition"
  ],
  "Fixes": [
    "Replace TCC solenoid",
    "Repair damaged wiring",
    "Flush and replace transmission fluid"
  ],
  "Temporary Solutions": [
    "Drive gently and avoid highway speeds"
  ]
},

"P0742": {
  "Actual Issue": "Torque Converter Clutch Circuit Stuck On",
  "Severity": "High (Can cause stalling or unsafe driving conditions)",
  "System": "Transmission",
  "Category": "Torque Converter",
  "Symptoms": [
    "Stalling at low speeds",
    "Shuddering when coming to a stop",
    "Poor acceleration",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Stuck TCC solenoid", "probability": 0.4},
    {"cause": "Wiring short", "probability": 0.3},
    {"cause": "Contaminated fluid", "probability": 0.2},
    {"cause": "Internal mechanical fault", "probability": 0.1}
  ],
  "Diagnostics": [
    "Use scan tool to verify TCC status",
    "Check wiring for shorts",
    "Inspect transmission fluid"
  ],
  "Fixes": [
    "Replace solenoid",
    "Flush fluid and clean system",
    "Repair or replace wiring"
  ],
  "Temporary Solutions": [
    "Shift to neutral at stops to prevent stalling"
  ]
},

"P0751": {
  "Actual Issue": "Shift Solenoid A Performance or Stuck Off",
  "Severity": "Medium (May impair gear engagement; not immediately critical)",
  "System": "Transmission",
  "Category": "Solenoid",
  "Symptoms": [
    "Erratic shifting",
    "Stuck in one gear",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Sticking solenoid", "probability": 0.5},
    {"cause": "Wiring or connection problems", "probability": 0.3},
    {"cause": "Faulty valve body", "probability": 0.2}
  ],
  "Diagnostics": [
    "Use scan tool to test shift solenoid operation",
    "Check fluid pressure readings",
    "Inspect harness and plug"
  ],
  "Fixes": [
    "Replace solenoid A",
    "Clean or replace valve body",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Shift manually if vehicle allows it"
  ]
},

"P0753": {
  "Actual Issue": "Shift Solenoid A Electrical",
  "Severity": "Medium (Electrical fault may trigger limp mode)",
  "System": "Transmission",
  "Category": "Solenoid",
  "Symptoms": [
    "Transmission shifts hard or fails to shift",
    "Limp mode activation",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Open or short in solenoid circuit", "probability": 0.5},
    {"cause": "Failed solenoid", "probability": 0.3},
    {"cause": "TCM failure", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check circuit continuity",
    "Test solenoid resistance",
    "Scan for related codes"
  ],
  "Fixes": [
    "Replace solenoid A",
    "Repair or replace faulty wiring",
    "Replace TCM if necessary"
  ],
  "Temporary Solutions": [
    "Reset codes and restart vehicle"
  ]
},

"P0761": {
  "Actual Issue": "Shift Solenoid C Performance or Stuck Off",
  "Severity": "Medium (Can lead to gear shift issues; resolve promptly)",
  "System": "Transmission",
  "Category": "Solenoid",
  "Symptoms": [
    "Erratic shifting",
    "Stuck in gear",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Solenoid C failure", "probability": 0.5},
    {"cause": "Hydraulic blockages", "probability": 0.3},
    {"cause": "Damaged wiring", "probability": 0.2}
  ],
  "Diagnostics": [
    "Use scan tool to monitor gear shifts",
    "Test solenoid operation",
    "Inspect transmission harness"
  ],
  "Fixes": [
    "Replace solenoid C",
    "Flush transmission",
    "Repair harness"
  ],
  "Temporary Solutions": [
    "Drive in low gear if possible"
  ]
},

"P0766": {
  "Actual Issue": "Shift Solenoid D Performance or Stuck Off",
  "Severity": "Medium (Impacts smoothness of gear changes; service soon)",
  "System": "Transmission",
  "Category": "Solenoid",
  "Symptoms": [
    "Shift delay",
    "Transmission slipping",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Sticking solenoid D", "probability": 0.5},
    {"cause": "Low or dirty transmission fluid", "probability": 0.3},
    {"cause": "Faulty TCM", "probability": 0.2}
  ],
  "Diagnostics": [
    "Scan transmission data",
    "Test solenoid function",
    "Inspect fluid condition"
  ],
  "Fixes": [
    "Replace solenoid D",
    "Flush and refill transmission fluid",
    "Replace or reprogram TCM"
  ],
  "Temporary Solutions": [
    "Manually control shifting if supported"
  ]
},

"P0776": {
  "Actual Issue": "Pressure Control Solenoid B Performance/Stuck Off",
  "Severity": "High (May lead to harsh or unsafe shifting behavior)",
  "System": "Transmission",
  "Category": "Solenoid",
  "Symptoms": [
    "Harsh shifting",
    "Slipping transmission",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Sticking or failed solenoid B", "probability": 0.5},
    {"cause": "Low transmission fluid", "probability": 0.3},
    {"cause": "Internal transmission blockage", "probability": 0.2}
  ],
  "Diagnostics": [
    "Monitor solenoid B activity with scan tool",
    "Test transmission fluid pressure",
    "Inspect solenoid resistance"
  ],
  "Fixes": [
    "Replace solenoid B",
    "Flush and replace transmission fluid",
    "Repair or clean transmission valve body"
  ],
  "Temporary Solutions": [
    "Drive at moderate speeds and avoid heavy loads"
  ]
},

  "P0806": {
  "Actual Issue": "Clutch Position Sensor Circuit Range/Performance",
  "Severity": "Medium (Can lead to shifting issues; should be checked soon)",
  "System": "Transmission",
  "Category": "Sensor",
  "Symptoms": [
    "Hard gear shifting",
    "Clutch pedal not engaging properly",
    "Check engine or transmission warning light"
  ],
  "Possible Causes": [
    {"cause": "Faulty clutch position sensor", "probability": 0.5},
    {"cause": "Damaged wiring or poor connections", "probability": 0.3},
    {"cause": "Mechanical clutch linkage issue", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test sensor signal with scan tool",
    "Inspect sensor wiring and connector",
    "Check clutch pedal and linkage"
  ],
  "Fixes": [
    "Replace faulty sensor",
    "Repair wiring",
    "Adjust or service clutch linkage"
  ],
  "Temporary Solutions": [
    "Shift gears slowly to reduce load on the system"
  ]
},
"P0833": {
  "Actual Issue": "Clutch Pedal Switch 'B' Circuit",
  "Severity": "Medium (Affects starting and cruise control safety)",
  "System": "Transmission",
  "Category": "Sensor",
  "Symptoms": [
    "Cruise control may not disengage",
    "Starting issues",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Faulty clutch pedal switch B", "probability": 0.5},
    {"cause": "Wiring short or open circuit", "probability": 0.3},
    {"cause": "Sensor misalignment", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check switch continuity",
    "Inspect wiring and connectors",
    "Test switch response with clutch pedal movement"
  ],
  "Fixes": [
    "Replace clutch pedal switch",
    "Repair wiring issues",
    "Re-align or re-install sensor"
  ],
  "Temporary Solutions": [
    "Manually ensure pedal is fully depressed to start engine"
  ]
},
"P0845": {
  "Actual Issue": "Transmission Fluid Pressure Sensor/Switch B Circuit",
  "Severity": "High (Transmission performance affected; urgent attention needed)",
  "System": "Transmission",
  "Category": "Sensor",
  "Symptoms": [
    "Transmission slipping",
    "Incorrect gear shifting",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Failed fluid pressure sensor B", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Faulty TCM", "probability": 0.2}
  ],
  "Diagnostics": [
    "Monitor sensor B with scan tool",
    "Test circuit continuity",
    "Inspect connectors"
  ],
  "Fixes": [
    "Replace pressure sensor B",
    "Repair circuit wiring",
    "Replace TCM if needed"
  ],
  "Temporary Solutions": [
    "Avoid aggressive acceleration and deceleration"
  ]
},
"P0846": {
  "Actual Issue": "Transmission Fluid Pressure Sensor/Switch B Range/Performance",
  "Severity": "Medium (Can lead to drivability issues if ignored)",
  "System": "Transmission",
  "Category": "Sensor",
  "Symptoms": [
    "Delayed shifting",
    "Harsh gear changes",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Sensor B failure", "probability": 0.5},
    {"cause": "Low fluid level", "probability": 0.3},
    {"cause": "Sensor contamination", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check pressure values with scan tool",
    "Test sensor output and resistance",
    "Inspect fluid for contamination"
  ],
  "Fixes": [
    "Replace sensor B",
    "Flush and replace transmission fluid",
    "Clean or replace connectors"
  ],
  "Temporary Solutions": [
    "Shift manually if transmission supports it"
  ]
},
"P0861": {
  "Actual Issue": "TCM Communication Circuit",
  "Severity": "High (Loss of communication with TCM; may trigger limp mode)",
  "System": "Transmission",
  "Category": "Communication",
  "Symptoms": [
    "Transmission may go into limp mode",
    "No communication with TCM",
    "Check transmission light"
  ],
  "Possible Causes": [
    {"cause": "Damaged CAN bus wiring", "probability": 0.5},
    {"cause": "TCM failure", "probability": 0.3},
    {"cause": "Loose or corroded connectors", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test communication lines with diagnostic tool",
    "Inspect wiring harness",
    "Scan for other communication-related DTCs"
  ],
  "Fixes": [
    "Repair CAN bus wiring",
    "Reconnect or clean TCM connectors",
    "Replace TCM if necessary"
  ],
  "Temporary Solutions": [
    "Restart vehicle to temporarily clear limp mode"
  ]
},
"P0871": {
  "Actual Issue": "Transmission Fluid Pressure Sensor/Switch C Range/Performance",
  "Severity": "High (Impacts fluid pressure and transmission operation)",
  "System": "Transmission",
  "Category": "Sensor",
  "Symptoms": [
    "Erratic shifting",
    "Transmission overheating",
    "Check engine light"
  ],
  "Possible Causes": [
    {"cause": "Faulty sensor C", "probability": 0.5},
    {"cause": "Low fluid pressure", "probability": 0.3},
    {"cause": "Electrical circuit issues", "probability": 0.2}
  ],
  "Diagnostics": [
    "Monitor sensor readings via scan tool",
    "Test for voltage at connector",
    "Check fluid level and quality"
  ],
  "Fixes": [
    "Replace sensor C",
    "Fix or replace wiring",
    "Flush and refill fluid"
  ],
  "Temporary Solutions": [
    "Limit high-speed driving to reduce transmission stress"
  ]
},
"P0894": {
  "Actual Issue": "Transmission Component Slipping",
  "Severity": "Critical (Risk of complete transmission failure)",
  "Possible Causes": [
    {"cause": "Worn clutch packs", "probability": 0.5},
    {"cause": "Internal transmission failure", "probability": 0.3},
    {"cause": "Low or burnt transmission fluid", "probability": 0.2}
  ],
  "Symptoms": [
    "RPM increases but vehicle speed does not",
    "Burnt smell from transmission",
    "Check engine light"
  ],
  "Diagnostics": [
    "Compare RPM vs vehicle speed with scan tool",
    "Inspect fluid condition",
    "Check for metal debris in pan"
  ],
  "Fixes": [
    "Rebuild or replace transmission",
    "Replace worn clutch packs",
    "Flush and replace fluid"
  ],
  "Temporary Solutions": [
    "Stop driving to prevent total transmission failure"
  ]
},
"P0900": {
  "Actual Issue": "Clutch Actuator Circuit/Open",
  "Severity": "High (Can prevent clutch engagement; immediate attention advised)",
  "Possible Causes": [
    {"cause": "Faulty clutch actuator", "probability": 0.5},
    {"cause": "Open or short circuit", "probability": 0.3},
    {"cause": "TCM error", "probability": 0.2}
  ],
  "Symptoms": [
    "Hard shifting in automatic manual transmission",
    "Inability to engage clutch",
    "Check transmission warning light"
  ],
  "Diagnostics": [
    "Test actuator with scan tool",
    "Check circuit continuity",
    "Inspect TCM commands to actuator"
  ],
  "Fixes": [
    "Replace clutch actuator",
    "Repair wiring or replace connector",
    "Reprogram or replace TCM"
  ],
  "Temporary Solutions": [
    "Use manual clutch override if available"
  ]
},
"P0935": {
  "Actual Issue": "Hydraulic Pressure Sensor Circuit High",
  "Severity": "Medium (Can lead to shifting issues or limp mode)",
  "Possible Causes": [
    {"cause": "Short circuit in pressure sensor circuit", "probability": 0.5},
    {"cause": "Failed hydraulic pressure sensor", "probability": 0.3},
    {"cause": "Contaminated fluid", "probability": 0.2}
  ],
  "Symptoms": [
    "Harsh or erratic shifting",
    "Transmission warning light",
    "Possible limp mode"
  ],
  "Diagnostics": [
    "Monitor hydraulic pressure readings via scan tool",
    "Inspect circuit for shorts or opens",
    "Check fluid quality"
  ],
  "Fixes": [
    "Replace hydraulic pressure sensor",
    "Repair circuit wiring",
    "Flush transmission"
  ],
  "Temporary Solutions": [
    "Drive slowly and monitor transmission behavior"
  ]
},
"P0960": {
  "Actual Issue": "Pressure Control Solenoid 'A' Control Circuit/Open",
  "Severity": "Medium (Causes drivability issues but not critical unless ignored)",
  "Possible Causes": [
    {"cause": "Open circuit in solenoid wiring", "probability": 0.5},
    {"cause": "Failed pressure control solenoid A", "probability": 0.3},
    {"cause": "Faulty TCM", "probability": 0.2}
  ],
  "Symptoms": [
    "Poor shift quality",
    "Delayed engagement",
    "Check engine light"
  ],
  "Diagnostics": [
    "Test solenoid A with scan tool",
    "Check circuit voltage and continuity",
    "Inspect TCM output signal"
  ],
  "Fixes": [
    "Replace solenoid A",
    "Repair control circuit wiring",
    "Reprogram or replace TCM"
  ],
  "Temporary Solutions": [
    "Limit vehicle speed and use manual mode if possible"
  ]
},
"P0962": {
  "Actual Issue": "Pressure Control Solenoid “A” Control Circuit Low",
  "Severity": "Medium (Can lead to hard shifting or reduced performance)",
  "Possible Causes": [
    {"cause": "Faulty pressure control solenoid 'A'", "probability": 0.5},
    {"cause": "Wiring issues or poor connection", "probability": 0.3},
    {"cause": "Low transmission fluid level", "probability": 0.2}
  ],
  "Symptoms": [
    "Transmission shifting issues",
    "Erratic or harsh shifting"
  ],
  "Diagnostics": [
    "Check transmission fluid level and condition",
    "Inspect wiring and connectors to solenoid 'A'",
    "Test solenoid operation with scan tool"
  ],
  "Fixes": [
    "Repair wiring/connectors",
    "Replace faulty solenoid",
    "Flush and refill transmission fluid if needed"
  ],
  "Temporary Solutions": []
},
"P0965": {
  "Actual Issue": "Pressure Control Solenoid “B” Control Circuit/Open",
  "Severity": "High (Transmission can become unresponsive; repair promptly)",
  "Possible Causes": [
    {"cause": "Faulty pressure control solenoid 'B'", "probability": 0.5},
    {"cause": "Open or damaged wiring", "probability": 0.3},
    {"cause": "Faulty transmission control module", "probability": 0.2}
  ],
  "Symptoms": [
    "Transmission slipping or delayed shifting",
    "Check engine light on"
  ],
  "Diagnostics": [
    "Scan for codes related to transmission",
    "Inspect wiring harness for breaks or damage",
    "Test solenoid electrical resistance"
  ],
  "Fixes": [
    "Repair or replace wiring",
    "Replace solenoid 'B'",
    "Reprogram or replace transmission control module if necessary"
  ],
  "Temporary Solutions": []
},
"P0970": {
  "Actual Issue": "Shift Solenoid “C” Control Circuit/Open",
  "Severity": "Medium (May lock transmission in one gear)",
  "Possible Causes": [
    {"cause": "Faulty shift solenoid 'C'", "probability": 0.5},
    {"cause": "Open or damaged wiring", "probability": 0.3},
    {"cause": "Faulty transmission control module", "probability": 0.2}
  ],
  "Symptoms": [
    "Transmission stuck in one gear",
    "Delayed or no shifting",
    "Check engine light on"
  ],
  "Diagnostics": [
    "Check wiring and connectors for solenoid 'C'",
    "Test solenoid resistance and operation",
    "Scan transmission control module for faults"
  ],
  "Fixes": [
    "Repair wiring",
    "Replace shift solenoid 'C'",
    "Replace or reprogram transmission control module"
  ],
  "Temporary Solutions": []
},
"P0973": {
  "Actual Issue": "Shift Solenoid “A” Control Circuit Low",
  "Severity": "Medium (May cause erratic shifting or limp mode)",
  "Possible Causes": [
    {"cause": "Faulty shift solenoid 'A'", "probability": 0.5},
    {"cause": "Low voltage or wiring issues", "probability": 0.3},
    {"cause": "Transmission control module problems", "probability": 0.2}
  ],
  "Symptoms": [
    "Hard shifting or slipping gears",
    "Transmission warning light",
    "Delayed engagement"
  ],
  "Diagnostics": [
    "Inspect wiring and connectors",
    "Test solenoid electrical values",
    "Use scan tool to monitor solenoid operation"
  ],
  "Fixes": [
    "Fix wiring issues",
    "Replace shift solenoid 'A'",
    "Service or replace transmission control module"
  ],
  "Temporary Solutions": []
},
"P0980": {
  "Actual Issue": "Shift Solenoid “B” Control Circuit High",
  "Severity": "Medium (Will affect shift quality; prompt service recommended)",
  "Possible Causes": [
    {"cause": "Faulty shift solenoid 'B'", "probability": 0.5},
    {"cause": "Short circuit in wiring", "probability": 0.3},
    {"cause": "Transmission control module failure", "probability": 0.2}
  ],
  "Symptoms": [
    "Transmission stuck or delayed shifting",
    "Check engine light on"
  ],
  "Diagnostics": [
    "Check wiring for shorts",
    "Test solenoid electrical parameters",
    "Scan for additional transmission codes"
  ],
  "Fixes": [
    "Repair wiring shorts",
    "Replace solenoid 'B'",
    "Replace or reprogram transmission control module"
  ],
  "Temporary Solutions": []
},
"P0983": {
  "Actual Issue": "Shift Solenoid “C” Control Circuit High",
  "Severity": "Medium (High voltage signal; risks erratic shifts)",
  "Possible Causes": [
    {"cause": "Faulty shift solenoid 'C'", "probability": 0.5},
    {"cause": "Short in wiring or connectors", "probability": 0.3},
    {"cause": "Transmission control module malfunction", "probability": 0.2}
  ],
  "Symptoms": [
    "Transmission shifting issues",
    "Delayed or harsh shifts",
    "Check engine light on"
  ],
  "Diagnostics": [
    "Inspect wiring harness",
    "Test solenoid resistance",
    "Use scan tool diagnostics"
  ],
  "Fixes": [
    "Repair wiring shorts",
    "Replace shift solenoid 'C'",
    "Reprogram or replace transmission control module"
  ],
  "Temporary Solutions": []
},
   "P0983": {
  "Actual Issue": "Shift Solenoid “C” Control Circuit High",
  "Severity": "Medium (High voltage signal; risks erratic shifts)",
  "Possible Causes": [
    {"cause": "Faulty shift solenoid 'C'", "probability": 0.5},
    {"cause": "Short in wiring or connectors", "probability": 0.3},
    {"cause": "Transmission control module malfunction", "probability": 0.2}
  ],
  "Symptoms": [
    "Transmission shifting issues",
    "Delayed or harsh shifts",
    "Check engine light on"
  ],
  "Diagnostics": [
    "Inspect wiring harness",
    "Test solenoid resistance",
    "Use scan tool diagnostics"
  ],
  "Fixes": [
    "Repair wiring shorts",
    "Replace shift solenoid 'C'",
    "Reprogram or replace transmission control module"
  ],
  "Temporary Solutions": []
},

    "Emissions & Engine & Fuel System & Security": {
  "P1001": {
    "Actual Issue": "Manufacturer Controlled Auxiliary Emission Controls",
    "Severity": "Medium (May affect emissions; repair advised to pass tests)",
    "Possible Causes": [
      {"cause": "Issues with manufacturer auxiliary emission controls", "probability": 0.5},
      {"cause": "Faulty sensors or actuators", "probability": 0.3},
      {"cause": "Software or calibration issues", "probability": 0.2}
    ],
    "Symptoms": [
      "Check engine light on",
      "Possible emission test failure"
    ],
    "Diagnostics": [
      "Use manufacturer specific scan tool",
      "Check emission control components",
      "Verify software updates"
    ],
    "Fixes": [
      "Repair or replace faulty emission components",
      "Update vehicle software",
      "Clear codes after repairs"
    ],
    "Temporary Solutions": [
      "Drive gently to minimize emissions",
      "Avoid heavy loads until repaired"
    ]
  },

  "P1004": {
    "Actual Issue": "Short Runner Valve Control Performance",
    "Severity": "Low to Medium (May reduce engine power; safe to drive with caution)",
    "Possible Causes": [
      {"cause": "Faulty short runner valve", "probability": 0.5},
      {"cause": "Wiring or connector problems", "probability": 0.3},
      {"cause": "Vacuum leaks", "probability": 0.2}
    ],
    "Symptoms": [
      "Reduced engine power",
      "Check engine light on"
    ],
    "Diagnostics": [
      "Inspect valve operation",
      "Check wiring and connectors",
      "Perform vacuum leak test"
    ],
    "Fixes": [
      "Replace or repair valve",
      "Fix wiring issues",
      "Repair vacuum leaks"
    ],
    "Temporary Solutions": []
  },

  "P1031": {
    "Actual Issue": "Heated O2 Sensor Control Circuit (Bank 1 Sensor 1)",
    "Severity": "Medium (Affects fuel economy and emissions; timely repair recommended)",
    "Possible Causes": [
      {"cause": "Faulty heated oxygen sensor", "probability": 0.5},
      {"cause": "Wiring or connector issues", "probability": 0.3},
      {"cause": "ECM problems", "probability": 0.2}
    ],
    "Symptoms": [
      "Check engine light",
      "Poor fuel economy",
      "Rough idle"
    ],
    "Diagnostics": [
      "Test oxygen sensor heater circuit",
      "Inspect wiring and connectors",
      "Scan ECM for faults"
    ],
    "Fixes": [
      "Replace oxygen sensor",
      "Repair wiring/connectors",
      "Update or reflash ECM"
    ],
    "Temporary Solutions": []
  },

  "P1106": {
    "Actual Issue": "Manifold Absolute Pressure (MAP) Sensor Range/Performance",
    "Severity": "Medium (Can cause drivability issues; prompt diagnosis advised)",
    "Possible Causes": [
      {"cause": "Faulty MAP sensor", "probability": 0.5},
      {"cause": "Wiring problems", "probability": 0.3},
      {"cause": "Vacuum leaks", "probability": 0.2}
    ],
    "Symptoms": [
      "Engine performance issues",
      "Check engine light",
      "Poor acceleration"
    ],
    "Diagnostics": [
      "Test MAP sensor output",
      "Inspect wiring and connectors",
      "Check for vacuum leaks"
    ],
    "Fixes": [
      "Replace MAP sensor",
      "Repair wiring",
      "Fix vacuum leaks"
    ],
    "Temporary Solutions": []
  },

  "P1111": {
    "Actual Issue": "Intake Air Temperature Sensor Intermittent High Voltage",
    "Severity": "Low to Medium (Can cause erratic behavior; not usually critical)",
    "Possible Causes": [
      {"cause": "Faulty intake air temperature sensor", "probability": 0.5},
      {"cause": "Wiring shorts or opens", "probability": 0.3},
      {"cause": "ECM faults", "probability": 0.2}
    ],
    "Symptoms": [
      "Erratic engine behavior",
      "Check engine light"
    ],
    "Diagnostics": [
      "Test sensor and wiring",
      "Inspect connectors",
      "Scan ECM codes"
    ],
    "Fixes": [
      "Replace intake air temperature sensor",
      "Repair wiring/connectors",
      "Update ECM software"
    ],
    "Temporary Solutions": []
  },

  "P1125": {
    "Actual Issue": "Throttle Position Sensor Intermittent",
    "Severity": "High (Can cause drivability issues including stalling; repair promptly)",
    "Possible Causes": [
      {"cause": "Faulty throttle position sensor (TPS)", "probability": 0.5},
      {"cause": "Loose or corroded wiring/connectors", "probability": 0.3},
      {"cause": "Throttle body issues", "probability": 0.2}
    ],
    "Symptoms": [
      "Intermittent engine hesitation",
      "Surging or stalling",
      "Check engine light"
    ],
    "Diagnostics": [
      "Inspect wiring and connectors",
      "Test TPS with a multimeter or scan tool",
      "Check throttle body for dirt or sticking"
    ],
    "Fixes": [
      "Replace faulty TPS",
      "Repair wiring/connectors",
      "Clean throttle body"
    ],
    "Temporary Solutions": []
  },

  "P1131": {
    "Actual Issue": "Lack of HO2S Switch - Sensor Indicates Lean (Bank 1 Sensor 1)",
    "Severity": "Medium (Lean condition affects engine performance and emissions)",
    "Possible Causes": [
      {"cause": "Faulty HO2S sensor", "probability": 0.5},
      {"cause": "Vacuum leak causing lean condition", "probability": 0.3},
      {"cause": "Fuel delivery issues", "probability": 0.2}
    ],
    "Symptoms": [
      "Poor fuel economy",
      "Rough idle",
      "Check engine light"
    ],
    "Diagnostics": [
      "Inspect for vacuum leaks",
      "Test HO2S sensor output",
      "Check fuel pressure"
    ],
    "Fixes": [
      "Replace HO2S sensor",
      "Repair vacuum leaks",
      "Service fuel system"
    ],
    "Temporary Solutions": []
  },

  "P1137": {
    "Actual Issue": "Lack of HO2S Switch - Sensor Indicates Lean (Bank 1 Sensor 2)",
    "Severity": "Medium (Impacts emissions and engine efficiency)",
    "Possible Causes": [
      {"cause": "Faulty HO2S sensor downstream", "probability": 0.5},
      {"cause": "Exhaust leaks", "probability": 0.3},
      {"cause": "Fuel delivery problems", "probability": 0.2}
    ],
    "Symptoms": [
      "Engine hesitation",
      "Poor fuel economy",
      "Check engine light"
    ],
    "Diagnostics": [
      "Check exhaust system for leaks",
      "Test sensor response",
      "Inspect fuel system"
    ],
    "Fixes": [
      "Replace downstream HO2S sensor",
      "Repair exhaust leaks",
      "Fix fuel delivery issues"
    ],
    "Temporary Solutions": []
  },

  "P1153": {
    "Actual Issue": "HO2S Insufficient Switching (Bank 2 Sensor 1)",
    "Severity": "Medium (Leads to increased emissions and poor engine performance)",
    "Possible Causes": [
      {"cause": "Faulty HO2S sensor", "probability": 0.5},
      {"cause": "Wiring issues", "probability": 0.3},
      {"cause": "Fuel system problems", "probability": 0.2}
    ],
    "Symptoms": [
      "Poor engine performance",
      "Increased emissions",
      "Check engine light"
    ],
    "Diagnostics": [
      "Test sensor signal with scan tool",
      "Inspect wiring/connectors",
      "Check fuel trims"
    ],
    "Fixes": [
      "Replace HO2S sensor",
      "Repair wiring",
      "Service fuel system"
    ],
    "Temporary Solutions": []
  },

  "P1166": {
    "Actual Issue": "Trim Adaptation",
    "Severity": "Low to Medium (Indicates sensor aging or imbalance; monitor and service)",
    "Possible Causes": [
      {"cause": "HO2S sensor aging or contamination", "probability": 0.5},
      {"cause": "Fuel system imbalance", "probability": 0.3},
      {"cause": "Vacuum leaks", "probability": 0.2}
    ],
    "Symptoms": [
      "Rough idle",
      "Poor fuel economy",
      "Check engine light"
    ],
    "Diagnostics": [
      "Check sensor readings",
      "Inspect fuel system",
      "Check for vacuum leaks"
    ],
    "Fixes": [
      "Replace HO2S sensor if necessary",
      "Repair fuel system issues",
      "Fix vacuum leaks"
    ],
    "Temporary Solutions": []
  },

  "P1171": {
    "Actual Issue": "Fuel System Lean During Acceleration (Bank 1)",
    "Severity": "High (Can cause drivability issues and potential engine damage if ignored)",
    "Possible Causes": [
      {"cause": "Vacuum leaks", "probability": 0.5},
      {"cause": "Faulty fuel injectors", "probability": 0.3},
      {"cause": "Fuel pump issues", "probability": 0.2}
    ],
    "Symptoms": [
      "Engine hesitation",
      "Poor acceleration",
      "Check engine light"
    ],
    "Diagnostics": [
      "Inspect for vacuum leaks",
      "Test fuel injectors",
      "Check fuel pressure"
    ],
    "Fixes": [
      "Repair vacuum leaks",
      "Replace faulty injectors",
      "Service fuel pump"
    ],
    "Temporary Solutions": []
  },

  "P1200": {
    "Actual Issue": "Injector Control Circuit",
    "Severity": "High (May cause misfires and poor performance; fix promptly)",
    "Possible Causes": [
      {"cause": "Faulty injector or wiring", "probability": 0.5},
      {"cause": "ECM issues", "probability": 0.3},
      {"cause": "Connector problems", "probability": 0.2}
    ],
    "Symptoms": [
      "Engine misfire",
      "Poor performance",
      "Check engine light"
    ],
    "Diagnostics": [
      "Check wiring and connectors",
      "Test injectors electrically",
      "Scan ECM for faults"
    ],
    "Fixes": [
      "Repair wiring/connectors",
      "Replace faulty injector",
      "Reprogram or replace ECM if needed"
    ],
    "Temporary Solutions": []
  },

  "P1211": {
    "Actual Issue": "Injector Control Pressure Too High",
    "Severity": "Medium to High (Can cause performance issues and fuel waste)",
    "Possible Causes": [
      {"cause": "Faulty fuel pressure regulator", "probability": 0.5},
      {"cause": "Injector control pressure sensor issues", "probability": 0.3},
      {"cause": "Fuel pump problems", "probability": 0.2}
    ],
    "Symptoms": [
      "Poor engine performance",
      "High fuel consumption",
      "Check engine light"
    ],
    "Diagnostics": [
      "Check fuel pressure",
      "Test pressure sensor",
      "Inspect fuel pump operation"
    ],
    "Fixes": [
      "Replace fuel pressure regulator",
      "Repair or replace sensor",
      "Service fuel pump"
    ],
    "Temporary Solutions": []
  },

  "P1225": {
    "Actual Issue": "Fuel Pump Feedback Circuit",
    "Severity": "High (May cause engine stalling; repair urgently)",
    "Possible Causes": [
      {"cause": "Faulty fuel pump relay or wiring", "probability": 0.5},
      {"cause": "Fuel pump driver module issues", "probability": 0.3},
      {"cause": "ECM problems", "probability": 0.2}
    ],
    "Symptoms": [
      "Fuel pump not operating properly",
      "Engine stalling",
      "Check engine light"
    ],
    "Diagnostics": [
      "Check relay and wiring",
      "Test fuel pump driver module",
      "Scan ECM for related codes"
    ],
    "Fixes": [
      "Repair wiring and relay",
      "Replace driver module",
      "Service or replace ECM if needed"
    ],
    "Temporary Solutions": []
  }
},
    "P1233": {
  "Actual Issue": "Fuel Pump Driver Module Disabled",
  "Severity": "High (Fuel pump disabled causes no start; immediate repair needed)",
  "Possible Causes": [
    {"cause": "Failed fuel pump driver module", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "ECM communication problems", "probability": 0.2}
  ],
  "Symptoms": [
    "Fuel pump failure",
    "Engine won't start",
    "Check engine light"
  ],
  "Diagnostics": [
    "Test driver module",
    "Inspect wiring and connections",
    "Scan ECM for faults"
  ],
  "Fixes": [
    "Replace fuel pump driver module",
    "Repair wiring",
    "Reprogram ECM if required"
  ],
  "Temporary Solutions": []
},

"P1247": {
  "Actual Issue": "Turbo Boost Pressure Low",
  "Severity": "Medium (Loss of power and efficiency; timely repair recommended)",
  "Possible Causes": [
    {"cause": "Boost leaks or vacuum leaks", "probability": 0.5},
    {"cause": "Faulty turbocharger wastegate", "probability": 0.3},
    {"cause": "Faulty boost pressure sensor", "probability": 0.2}
  ],
  "Symptoms": [
    "Loss of power",
    "Poor acceleration",
    "Check engine light"
  ],
  "Diagnostics": [
    "Inspect for boost leaks",
    "Test wastegate operation",
    "Check boost sensor readings"
  ],
  "Fixes": [
    "Repair boost or vacuum leaks",
    "Replace faulty wastegate actuator",
    "Replace boost pressure sensor"
  ],
  "Temporary Solutions": []
},

"P1250": {
  "Actual Issue": "Pressure Regulator Control Solenoid Circuit",
  "Severity": "Medium (May cause rough idle and poor performance; repair advised)",
  "Possible Causes": [
    {"cause": "Faulty pressure regulator solenoid", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "ECM control problems", "probability": 0.2}
  ],
  "Symptoms": [
    "Poor engine performance",
    "Erratic idle",
    "Check engine light"
  ],
  "Diagnostics": [
    "Check solenoid wiring and connectors",
    "Test solenoid operation",
    "Scan ECM for related codes"
  ],
  "Fixes": [
    "Repair wiring/connectors",
    "Replace faulty solenoid",
    "Reprogram or repair ECM if needed"
  ],
  "Temporary Solutions": []
},

"P1260": {
  "Actual Issue": "Theft Detected, Engine Disabled",
  "Severity": "High (Engine disabled due to security; immediate attention required)",
  "Possible Causes": [
    {"cause": "Faulty immobilizer system", "probability": 0.5},
    {"cause": "Key or transponder issues", "probability": 0.3},
    {"cause": "ECM communication failure", "probability": 0.2}
  ],
  "Symptoms": [
    "Engine cranks but does not start",
    "Security light on",
    "No fuel or ignition"
  ],
  "Diagnostics": [
    "Check key and transponder",
    "Scan immobilizer system",
    "Inspect wiring between ECM and immobilizer"
  ],
  "Fixes": [
    "Reprogram or replace key/transponder",
    "Repair immobilizer wiring",
    "Replace ECM if required"
  ],
  "Temporary Solutions": [
    "Use spare key if available",
    "Disconnect battery for a few minutes and retry start"
  ]
},

"P1288": {
  "Actual Issue": "Cylinder Head Temperature Sensor Out of Range",
  "Severity": "High (Risk of overheating and engine damage; prompt repair necessary)",
  "Possible Causes": [
    {"cause": "Faulty cylinder head temperature sensor", "probability": 0.5},
    {"cause": "Wiring issues", "probability": 0.3},
    {"cause": "Actual overheating", "probability": 0.2}
  ],
  "Symptoms": [
    "Engine overheating",
    "Check engine light",
    "Poor engine performance"
  ],
  "Diagnostics": [
    "Test sensor resistance and output",
    "Inspect wiring/connectors",
    "Check cooling system operation"
  ],
  "Fixes": [
    "Replace faulty temperature sensor",
    "Repair wiring",
    "Fix cooling system problems"
  ],
  "Temporary Solutions": [
    "Avoid hard driving",
    "Check coolant level regularly"
  ]
},

"Engine & Ignition & Emissions": {
  "P1299": {
    "Actual Issue": "Cylinder Head Overtemperature Protection Active",
    "Severity": "High (Engine power reduced to prevent damage; urgent attention needed)",
    "Possible Causes": [
      {"cause": "Actual engine overheating", "probability": 0.5},
      {"cause": "Faulty temperature sensor", "probability": 0.3},
      {"cause": "Cooling system failure", "probability": 0.2}
    ],
    "Symptoms": [
      "Engine power reduced",
      "Engine overheating warning",
      "Possible limp mode"
    ],
    "Diagnostics": [
      "Check coolant temperature",
      "Inspect temperature sensor",
      "Test cooling system components"
    ],
    "Fixes": [
      "Repair cooling system",
      "Replace faulty sensor",
      "Address overheating causes"
    ],
    "Temporary Solutions": [
      "Avoid hard driving",
      "Stop engine if overheating warning appears"
    ]
  },

  "P1320": {
    "Actual Issue": "Ignition Signal Primary",
    "Severity": "High (May cause misfires or no start; repair promptly)",
    "Possible Causes": [
      {"cause": "Faulty ignition switch or wiring", "probability": 0.5},
      {"cause": "Ignition coil issues", "probability": 0.3},
      {"cause": "ECM ignition control faults", "probability": 0.2}
    ],
    "Symptoms": [
      "Engine misfire",
      "Hard starting",
      "Check engine light"
    ],
    "Diagnostics": [
      "Test ignition switch and wiring",
      "Check ignition coil operation",
      "Scan ECM for ignition faults"
    ],
    "Fixes": [
      "Repair ignition wiring",
      "Replace ignition coil",
      "Service or replace ECM"
    ],
    "Temporary Solutions": []
  },

  "P1335": {
    "Actual Issue": "Crankshaft Position Sensor REF Signal",
    "Severity": "High (Engine stall/no start risk; immediate repair recommended)",
    "Possible Causes": [
      {"cause": "Faulty crankshaft position sensor", "probability": 0.5},
      {"cause": "Wiring issues", "probability": 0.3},
      {"cause": "Sensor reluctor ring damage", "probability": 0.2}
    ],
    "Symptoms": [
      "Engine stalling",
      "No start",
      "Check engine light"
    ],
    "Diagnostics": [
      "Test sensor and wiring",
      "Inspect reluctor ring",
      "Scan ECM for related codes"
    ],
    "Fixes": [
      "Replace crankshaft position sensor",
      "Repair wiring",
      "Repair or replace reluctor ring"
    ],
    "Temporary Solutions": [
      "Avoid driving if engine stalls",
      "Try restarting engine"
    ]
  },

  "P1345": {
    "Actual Issue": "Camshaft Position Sensor/Crankshaft Position Sensor Correlation",
    "Severity": "High (Timing issues may cause misfire or engine damage; fix ASAP)",
    "Possible Causes": [
      {"cause": "Timing chain/belt issues", "probability": 0.5},
      {"cause": "Faulty sensors", "probability": 0.3},
      {"cause": "Incorrect sensor alignment", "probability": 0.2}
    ],
    "Symptoms": [
      "Engine misfire",
      "Hard start",
      "Check engine light"
    ],
    "Diagnostics": [
      "Inspect timing components",
      "Test sensors",
      "Check sensor alignment"
    ],
    "Fixes": [
      "Repair or replace timing chain/belt",
      "Replace faulty sensors",
      "Correct sensor alignment"
    ],
    "Temporary Solutions": [
      "Avoid hard acceleration",
      "Limit driving until fixed"
    ]
  },

  "P1401": {
    "Actual Issue": "Differential Pressure Feedback Sensor Circuit High Voltage",
    "Severity": "Medium (Can cause emissions and performance issues; timely repair needed)",
    "Possible Causes": [
      {"cause": "Faulty differential pressure feedback sensor", "probability": 0.5},
      {"cause": "Wiring issues", "probability": 0.3},
      {"cause": "EGR valve problems", "probability": 0.2}
    ],
    "Symptoms": [
      "Poor engine performance",
      "Increased emissions",
      "Check engine light"
    ],
    "Diagnostics": [
      "Test sensor output voltage",
      "Inspect wiring",
      "Check EGR valve operation"
    ],
    "Fixes": [
      "Replace sensor",
      "Repair wiring",
      "Service or replace EGR valve"
    ],
    "Temporary Solutions": []
  },

  "P1406": {
    "Actual Issue": "EGR Valve Pintle Position Circuit",
    "Severity": "Medium (May cause rough idle and emissions issues; repair advised)",
    "Possible Causes": [
      {"cause": "Faulty EGR valve position sensor", "probability": 0.5},
      {"cause": "Wiring or connector issues", "probability": 0.3},
      {"cause": "Sticking EGR valve", "probability": 0.2}
    ],
    "Symptoms": [
      "Rough idle",
      "Poor performance",
      "Check engine light"
    ],
    "Diagnostics": [
      "Test sensor and wiring",
      "Inspect EGR valve movement",
      "Check for carbon buildup"
    ],
    "Fixes": [
      "Replace sensor",
      "Repair wiring/connectors",
      "Clean or replace EGR valve"
    ],
    "Temporary Solutions": []
  },

  "P1410": {
    "Actual Issue": "Secondary Air Injection System Switching Valve Circuit",
    "Severity": "Low to Medium (Impacts emissions and cold starts; monitor and repair)",
    "Possible Causes": [
      {"cause": "Faulty air injection valve or solenoid", "probability": 0.5},
      {"cause": "Wiring issues", "probability": 0.3},
      {"cause": "Faulty control module", "probability": 0.2}
    ],
    "Symptoms": [
      "Check engine light",
      "Failed emissions test",
      "Poor cold start"
    ],
    "Diagnostics": [
      "Test valve operation",
      "Inspect wiring/connectors",
      "Scan control module for codes"
    ],
    "Fixes": [
      "Replace faulty valve or solenoid",
      "Repair wiring",
      "Repair or replace control module"
    ],
    "Temporary Solutions": []
  },

  "P1441": {
    "Actual Issue": "EVAP System Flow During Non-Purge Condition",
    "Severity": "Low to Medium (May cause fuel odor and failed emissions; repair recommended)",
    "Possible Causes": [
      {"cause": "Faulty EVAP purge valve", "probability": 0.5},
      {"cause": "Wiring or vacuum leaks", "probability": 0.3},
      {"cause": "Faulty EVAP canister", "probability": 0.2}
    ],
    "Symptoms": [
      "Check engine light",
      "Fuel odor",
      "Failed emissions test"
    ],
    "Diagnostics": [
      "Inspect purge valve operation",
      "Check for vacuum leaks",
      "Test EVAP canister"
    ],
    "Fixes": [
      "Replace purge valve",
      "Repair leaks",
      "Replace EVAP canister if needed"
    ],
    "Temporary Solutions": []
  }
},

  "Emissions & Engine & Electrical & Security": {
  "P1447": {
    "Actual Issue": "EVAP Emission Control System Leak Detected",
    "Severity": "Low to Medium (Causes emissions issues and fuel odor; timely repair recommended)",
    "Possible Causes": [
      {"cause": "Loose or damaged gas cap", "probability": 0.5},
      {"cause": "EVAP hose or valve leak", "probability": 0.3},
      {"cause": "Faulty purge or vent valve", "probability": 0.2}
    ],
    "Symptoms": [
      "Check engine light",
      "Fuel odor",
      "Failed emissions test"
    ],
    "Diagnostics": [
      "Inspect gas cap and tighten/replace if needed",
      "Perform smoke test to find leaks",
      "Test purge and vent valves"
    ],
    "Fixes": [
      "Replace gas cap if faulty",
      "Repair or replace leaking hoses/valves",
      "Clear codes after repair"
    ],
    "Temporary Solutions": [
      "Tighten gas cap securely",
      "Avoid refueling until leak fixed"
    ]
  },

  "P1456": {
    "Actual Issue": "EVAP Control System Leak (Fuel Tank System)",
    "Severity": "Medium (Fuel system leak can cause emissions issues; repair promptly)",
    "Possible Causes": [
      {"cause": "Leaking or damaged fuel tank or lines", "probability": 0.5},
      {"cause": "Faulty fuel tank pressure sensor", "probability": 0.3},
      {"cause": "EVAP system leak", "probability": 0.2}
    ],
    "Symptoms": [
      "Check engine light",
      "Fuel odor near tank",
      "Failed emissions test"
    ],
    "Diagnostics": [
      "Inspect fuel tank and lines for damage",
      "Test fuel tank pressure sensor",
      "Perform smoke test for leaks"
    ],
    "Fixes": [
      "Repair or replace leaking tank or lines",
      "Replace faulty sensor",
      "Clear codes after repair"
    ],
    "Temporary Solutions": [
      "Avoid excessive vehicle movement",
      "Minimize fuel tank pressure changes"
    ]
  },

  "P1470": {
    "Actual Issue": "LDP (Load Dump Protection) Switch Function",
    "Severity": "Low to Medium (May affect engine performance; monitor and repair as needed)",
    "Possible Causes": [
      {"cause": "Faulty LDP switch", "probability": 0.7},
      {"cause": "Wiring or connector problems", "probability": 0.3}
    ],
    "Symptoms": [
      "Possible engine performance issues",
      "Check engine light"
    ],
    "Diagnostics": [
      "Test LDP switch operation",
      "Inspect wiring and connectors"
    ],
    "Fixes": [
      "Replace faulty LDP switch",
      "Repair wiring/connectors"
    ],
    "Temporary Solutions": []
  },

  "P1504": {
    "Actual Issue": "Idle Air Control Circuit Malfunction",
    "Severity": "Medium (Can cause rough or high idle and stalling; timely repair recommended)",
    "Possible Causes": [
      {"cause": "Faulty idle air control valve", "probability": 0.5},
      {"cause": "Wiring issues", "probability": 0.3},
      {"cause": "Carbon buildup", "probability": 0.2}
    ],
    "Symptoms": [
      "Rough or high idle",
      "Stalling at idle",
      "Check engine light"
    ],
    "Diagnostics": [
      "Test IAC valve operation",
      "Inspect wiring",
      "Clean throttle body"
    ],
    "Fixes": [
      "Replace idle air control valve if faulty",
      "Repair wiring",
      "Clean throttle body"
    ],
    "Temporary Solutions": [
      "Avoid prolonged idling",
      "Restart engine if stalling occurs"
    ]
  },

  "P1516": {
    "Actual Issue": "Throttle Actuator Control Module",
    "Severity": "Medium (May cause poor throttle response and hesitation; repair advised)",
    "Possible Causes": [
      {"cause": "Faulty throttle actuator control module", "probability": 0.6},
      {"cause": "Wiring or sensor issues", "probability": 0.4}
    ],
    "Symptoms": [
      "Poor throttle response",
      "Engine hesitation",
      "Check engine light"
    ],
    "Diagnostics": [
      "Scan for module codes",
      "Inspect wiring and throttle position sensor"
    ],
    "Fixes": [
      "Repair or replace throttle actuator control module",
      "Fix wiring issues"
    ],
    "Temporary Solutions": []
  },

  "P1524": {
    "Actual Issue": "Variable Camshaft Timing Oil Control Valve",
    "Severity": "Medium (Impacts engine performance and timing; timely repair needed)",
    "Possible Causes": [
      {"cause": "Faulty oil control valve", "probability": 0.5},
      {"cause": "Wiring or connector issues", "probability": 0.3},
      {"cause": "Low engine oil level or quality", "probability": 0.2}
    ],
    "Symptoms": [
      "Poor engine performance",
      "Rough idle",
      "Check engine light"
    ],
    "Diagnostics": [
      "Test oil control valve",
      "Inspect wiring",
      "Check oil level and condition"
    ],
    "Fixes": [
      "Replace oil control valve",
      "Repair wiring/connectors",
      "Change engine oil"
    ],
    "Temporary Solutions": [
      "Avoid hard driving",
      "Check oil regularly"
    ]
  },

  "P1530": {
    "Actual Issue": "A/C Clutch Relay Circuit",
    "Severity": "Low (Affects air conditioning function; repair when convenient)",
    "Possible Causes": [
      {"cause": "Faulty A/C clutch relay", "probability": 0.5},
      {"cause": "Wiring issues", "probability": 0.3},
      {"cause": "Failed A/C compressor clutch", "probability": 0.2}
    ],
    "Symptoms": [
      "A/C compressor not engaging",
      "No cooling",
      "Check engine or HVAC light"
    ],
    "Diagnostics": [
      "Test A/C clutch relay",
      "Inspect wiring/connectors",
      "Check compressor clutch operation"
    ],
    "Fixes": [
      "Replace A/C clutch relay",
      "Repair wiring",
      "Replace A/C compressor clutch"
    ],
    "Temporary Solutions": [
      "Use fan only mode for cooling",
      "Avoid A/C use until fixed"
    ]
  },

  "P1550": {
    "Actual Issue": "Power Steering Pressure Sensor Circuit Malfunction",
    "Severity": "Medium (Can cause hard steering and warning lights; repair advised)",
    "Possible Causes": [
      {"cause": "Faulty pressure sensor", "probability": 0.5},
      {"cause": "Wiring problems", "probability": 0.3},
      {"cause": "Power steering pump issues", "probability": 0.2}
    ],
    "Symptoms": [
      "Hard steering",
      "Power steering warning light",
      "Check engine light"
    ],
    "Diagnostics": [
      "Test pressure sensor",
      "Inspect wiring",
      "Check power steering pump"
    ],
    "Fixes": [
      "Replace pressure sensor",
      "Repair wiring",
      "Service or replace power steering pump"
    ],
    "Temporary Solutions": [
      "Avoid sharp turns",
      "Use extra caution when steering"
    ]
  },

  "P1602": {
    "Actual Issue": "Battery Voltage Too Low",
    "Severity": "High (Can cause starting failure; repair urgently)",
    "Possible Causes": [
      {"cause": "Weak or discharged battery", "probability": 0.5},
      {"cause": "Faulty alternator", "probability": 0.3},
      {"cause": "Poor battery connections", "probability": 0.2}
    ],
    "Symptoms": [
      "Starting issues",
      "Battery warning light",
      "Check engine light"
    ],
    "Diagnostics": [
      "Test battery voltage",
      "Check alternator output",
      "Inspect battery terminals"
    ],
    "Fixes": [
      "Recharge or replace battery",
      "Repair or replace alternator",
      "Clean and tighten battery terminals"
    ],
    "Temporary Solutions": [
      "Minimize electrical load",
      "Avoid short trips to allow battery charging"
    ]
  },

  "P1603": {
    "Actual Issue": "ECM Backup Circuit",
    "Severity": "Medium (May cause engine running issues; repair recommended)",
    "Possible Causes": [
      {"cause": "Faulty ECM backup circuit", "probability": 0.6},
      {"cause": "Wiring problems", "probability": 0.4}
    ],
    "Symptoms": [
      "Engine running issues",
      "Check engine light"
    ],
    "Diagnostics": [
      "Inspect ECM backup circuit wiring",
      "Test ECM operation"
    ],
    "Fixes": [
      "Repair wiring",
      "Replace ECM if faulty"
    ],
    "Temporary Solutions": []
  },

  "P1626": {
    "Actual Issue": "Theft Deterrent Fuel Enable Signal Not Received",
    "Severity": "High (Engine immobilized for security; urgent repair required)",
    "Possible Causes": [
      {"cause": "Faulty theft deterrent system", "probability": 0.7},
      {"cause": "Wiring or module failure", "probability": 0.3}
    ],
    "Symptoms": [
      "Engine cranks but no start",
      "Security light on"
    ],
    "Diagnostics": [
      "Check theft deterrent module",
      "Inspect wiring"
    ],
    "Fixes": [
      "Repair or replace theft deterrent module",
      "Fix wiring issues"
    ],
    "Temporary Solutions": []
  },

  "P1631": {
    "Actual Issue": "Theft Deterrent Start Enable Signal Not Correct",
    "Severity": "High (Prevents engine start; immediate repair recommended)",
    "Possible Causes": [
      {"cause": "Faulty theft deterrent system", "probability": 0.7},
      {"cause": "ECM communication error", "probability": 0.3}
    ],
    "Symptoms": [
      "No start condition",
      "Security warning light"
    ],
    "Diagnostics": [
      "Scan theft deterrent codes",
      "Inspect ECM communication"
    ],
    "Fixes": [
      "Repair or replace theft deterrent components",
      "Fix ECM communication"
    ],
    "Temporary Solutions": []
  },

  "P1682": {
    "Actual Issue": "Ignition 1 Switch Circuit 2",
    "Severity": "High (No start or intermittent electrical issues; urgent repair needed)",
    "Possible Causes": [
      {"cause": "Faulty ignition switch", "probability": 0.7},
      {"cause": "Wiring problems", "probability": 0.3}
    ],
    "Symptoms": [
      "No start",
      "Intermittent electrical issues"
    ],
    "Diagnostics": [
      "Test ignition switch",
      "Inspect wiring"
    ],
    "Fixes": [
      "Replace ignition switch",
      "Repair wiring"
    ],
    "Temporary Solutions": []
  },

  "P1684": {
    "Actual Issue": "Battery Disconnected (Last 50 Starts)",
    "Severity": "Low (Not a fault, informational only; check connections)",
    "Possible Causes": [
      {"cause": "Battery disconnection or replacement", "probability": 0.6},
      {"cause": "Loose battery terminals", "probability": 0.4}
    ],
    "Symptoms": [
      "Loss of stored settings",
      "Check engine light"
    ],
    "Diagnostics": [
      "Inspect battery terminals",
      "Check stored fault codes"
    ],
    "Fixes": [
      "Secure battery terminals",
      "Clear fault codes after battery replacement"
    ],
    "Temporary Solutions": []
  }
},

"Transmission & Throttle": {
  "P1705": {
    "Actual Issue": "Throttle Position Sensor Circuit Malfunction (Transmission Related)",
    "Severity": "Medium (Affects transmission control; repair advised)",
    "Possible Causes": [
      {"cause": "Faulty throttle position sensor", "probability": 0.7},
      {"cause": "Wiring issues", "probability": 0.3}
    ],
    "Diagnostics": [
      "Test throttle position sensor",
      "Inspect wiring"
    ],
    "Fixes": [
      "Replace throttle position sensor",
      "Repair wiring"
    ],
    "Temporary Solutions": [
      "Avoid aggressive acceleration until fixed"
    ]
  }
},

"P1740": {
  "Actual Issue": "Torque Converter Clutch or Overdrive Solenoid Performance",
  "Severity": "Medium (Can cause transmission slipping and poor shift quality; repair advised)",
  "Possible Causes": [
    {"cause": "Faulty torque converter clutch solenoid", "probability": 0.6},
    {"cause": "Wiring problems", "probability": 0.4}
  ],
  "Diagnostics": [
    "Test solenoid operation",
    "Inspect wiring"
  ],
  "Fixes": [
    "Replace solenoid",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Drive at moderate speeds to prevent further slipping"
  ]
  },

"P1751": {
  "Actual Issue": "Shift Solenoid Malfunction",
  "Severity": "Medium (Shift delays or harsh shifts likely; timely repair recommended)",
  "Possible Causes": [
    {"cause": "Faulty shift solenoid", "probability": 0.7},
    {"cause": "Wiring issues", "probability": 0.3}
  ],
  "Diagnostics": [
    "Test solenoid",
    "Inspect wiring"
  ],
  "Fixes": [
    "Replace solenoid",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Manually shift if applicable and avoid harsh driving"
  ]
},

"P1760": {
  "Actual Issue": "Overrun Clutch Solenoid Circuit Malfunction",
  "Severity": "Medium (May affect smooth shifting; repair advised)",
  "Possible Causes": [
    {"cause": "Faulty overrun clutch solenoid", "probability": 0.7},
    {"cause": "Wiring problems", "probability": 0.3}
  ],
  "Diagnostics": [
    "Test solenoid",
    "Inspect wiring"
  ],
  "Fixes": [
    "Replace solenoid",
    "Repair wiring"
  ],
  "Temporary Solutions": []
},

"P1776": {
  "Actual Issue": "Solenoid Switch Valve Latched in LR Position",
  "Severity": "Medium (May cause transmission stuck in low/reverse; avoid driving in reverse)",
  "Possible Causes": [
    {"cause": "Faulty solenoid valve", "probability": 0.5},
    {"cause": "Mechanical blockage", "probability": 0.5}
  ],
  "Diagnostics": [
    "Inspect solenoid operation",
    "Check transmission mechanical parts"
  ],
  "Fixes": [
    "Replace solenoid",
    "Repair transmission"
  ],
  "Temporary Solutions": [
    "Avoid driving in reverse until resolved"
  ]
},

"P1780": {
  "Actual Issue": "Park/Neutral Position Switch Malfunction",
  "Severity": "Medium (May cause starting issues; repair recommended)",
  "Possible Causes": [
    {"cause": "Faulty park/neutral switch", "probability": 0.6},
    {"cause": "Wiring issues", "probability": 0.4}
  ],
  "Diagnostics": [
    "Test switch operation",
    "Inspect wiring"
  ],
  "Fixes": [
    "Replace switch",
    "Repair wiring"
  ],
  "Temporary Solutions": [
    "Try starting in neutral instead of park (if allowed)"
  ]
},

"P1790": {
  "Actual Issue": "Fault Immediately After Shift",
  "Severity": "High (Immediate transmission fault after shift; urgent diagnostics needed)",
  "Possible Causes": [
    {"cause": "Transmission control module issue", "probability": 0.5},
    {"cause": "Shift solenoid or valve malfunction", "probability": 0.5}
  ],
  "Diagnostics": [
    "Scan TCM for faults",
    "Test solenoids and valves"
  ],
  "Fixes": [
    "Repair or replace TCM",
    "Replace faulty solenoids or valves"
  ],
  "Temporary Solutions": []
},

"P1810": {
  "Actual Issue": "Transmission Fluid Pressure Switch Assembly",
  "Severity": "Medium (Fluid pressure issues can affect shifting; repair advised)",
  "Possible Causes": [
    {"cause": "Faulty transmission fluid pressure switch", "probability": 0.5},
    {"cause": "Wiring or connector issues", "probability": 0.3},
    {"cause": "Low transmission fluid pressure", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test fluid pressure switch resistance and operation",
    "Inspect wiring and connectors",
    "Check transmission fluid level and condition"
  ],
  "Fixes": [
    "Replace faulty pressure switch",
    "Repair wiring/connectors",
    "Service transmission fluid"
  ],
  "Temporary Solutions": [
    "Avoid aggressive acceleration or towing"
  ]
},

"P1860": {
  "Actual Issue": "TCC PWM Solenoid Circuit Electrical",
  "Severity": "Medium (Torque converter clutch issues causing slipping; repair recommended)",
  "Possible Causes": [
    {"cause": "Faulty TCC PWM solenoid", "probability": 0.5},
    {"cause": "Wiring or connector problems", "probability": 0.3},
    {"cause": "ECM/TCM issues", "probability": 0.2}
  ],
  "Diagnostics": [
    "Test solenoid operation and wiring",
    "Scan ECM/TCM for related codes",
    "Check transmission fluid condition"
  ],
  "Fixes": [
    "Replace faulty solenoid",
    "Repair wiring/connectors",
    "Repair or reflash ECM/TCM"
  ],
  "Temporary Solutions": [
    "Drive gently and monitor for worsening symptoms"
  ]
},

"P1870": {
  "Actual Issue": "Transmission Component Slipping",
  "Severity": "High (Transmission slipping affecting drivability; urgent repair needed)",
  "Possible Causes": [
    {"cause": "Worn transmission components", "probability": 0.5},
    {"cause": "Low or contaminated transmission fluid", "probability": 0.3},
    {"cause": "Faulty sensors or solenoids", "probability": 0.2}
  ],
  "Diagnostics": [
    "Inspect transmission components",
    "Check fluid level and quality",
    "Scan for related codes"
  ],
  "Fixes": [
    "Repair or replace transmission components",
    "Change transmission fluid",
    "Replace faulty sensors or solenoids"
  ],
  "Temporary Solutions": [
    "Avoid towing or steep inclines"
  ]
},

"P1890": {
  "Actual Issue": "Transmission Performance Degraded",
  "Severity": "Medium (Mechanical wear or hydraulic issues; repair recommended)",
  "Possible Causes": [
    {"cause": "Mechanical wear", "probability": 0.4},
    {"cause": "Hydraulic issues", "probability": 0.3},
    {"cause": "Faulty control modules", "probability": 0.3}
  ],
  "Diagnostics": [
    "Test transmission hydraulic pressure",
    "Inspect mechanical parts",
    "Scan control modules for faults"
  ],
  "Fixes": [
    "Repair or replace worn parts",
    "Flush and replace transmission fluid",
    "Service control modules"
  ],
  "Temporary Solutions": [
    "Limit vehicle load and avoid high-speed driving"
  ]
},

"P2101": {
  "Actual Issue": "Throttle Actuator Control Motor Circuit Range/Performance",
  "Severity": "Medium (Throttle response issues; repair advised)",
  "Possible Causes": [
    {"cause": "Faulty throttle actuator motor", "probability": 0.6},
    {"cause": "Wiring or connector problems", "probability": 0.3},
    {"cause": "ECM control issues", "probability": 0.1}
  ],
  "Diagnostics": [
    "Test throttle actuator motor and wiring",
    "Scan ECM for throttle-related codes",
    "Check for mechanical throttle body issues"
  ],
  "Fixes": [
    "Replace faulty throttle actuator motor",
    "Repair wiring/connectors",
    "Reprogram or repair ECM"
  ],
  "Temporary Solutions": [
    "Avoid sudden throttle input"
  ]
},

"P2106": {
  "Actual Issue": "Throttle Actuator Control System – Forced Limited Power",
  "Severity": "High (Limp mode activation; limited power until repair)",
  "Possible Causes": [
    {"cause": "Throttle actuator malfunction", "probability": 0.5},
    {"cause": "Wiring faults", "probability": 0.3},
    {"cause": "ECM control issues", "probability": 0.2}
  ],
  "Diagnostics": [
    "Check throttle actuator operation and wiring",
    "Scan ECM for error codes",
    "Inspect throttle body for faults"
  ],
  "Fixes": [
    "Repair or replace throttle actuator",
    "Fix wiring issues",
    "Repair or reflash ECM"
  ],
  "Temporary Solutions": [
    "Avoid highway driving if engine enters limp mode"
  ]
}
}