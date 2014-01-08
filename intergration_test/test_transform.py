from collections import defaultdict
value = {}
result = defaultdict(dict)
x = lambda m :  m[0].get(m[1]) if m[0].get(m[1],None) else m[2]
result['tobacco'] = x([value,'tobacco',{}])
result['type'] = x([value,'type',{}])

print result







import colander
class Parrot(object):
    def __init__(self):
        self._voltage = 230000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

a = Parrot()
print a.voltage
getattr(a, 'p',None)


class cat(object):
    def __init__(self,mapping):
        self.mapping = mapping
        
    def _get(self, paths, value):
        print paths, value
        for path in paths:
            if path in value:
                value = value[path]
            else:
                return colander.None
        return value if value else colander.None

    def __call__(self, values):
        modified_value = {}
        for k, v, f in self.mapping:
            result = self._get(k.split('.'), values)
            modified_value[v] = f(result) if result and\
                                hasattr(f, '__call__') else result
        return modified_value

def _parse_gender(gender):
    return {
              'm': 'Male',
              'f': 'Female'
           }.get(gender.lower()[0], '') if gender else ''


pt = cat([('id', 'encounter_id', None),
          ('patient.sex', 'gender', _parse_gender)
        ])
#value = {"id":23}
value = {"patient.sex":"m"} 

#print pt(value)



d = { "data" : 
    [
   {
      "patientType":"I",
      "intakesOutputs":[

      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"4101",
            "name":{
               "salutation":"DO",
               "middle":"V.",
               "last":"DEGENHARDT",
               "first":"DAVID"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"Single",
         "name":{
            "middle":"Z",
            "last":"Patient 1",
            "first":"Test"
         },
         "ssn":"4839642096902545877",
         "sex":"F",
         "contactDetails":{
            "workPhone":"",
            "homePhone":"(109)033-7464"
         },
         "dateOfBirth":"1919-09-01T05:00:00",
         "mrn":"7309883568227723610",
         "race":"Caucasian",
         "id":"52125d2157fa831fd6986ad3"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.075076",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.075072",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.075059",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.075086",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.075083",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.075080",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.075079",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"52125d159606ff381f5d82f8",
      "allergies":[
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-19T00:00:00",
            "name":"SULFA(SULFONAMIDE ANTIBIOTICS)"
         },
         {
            "name":"Codeine"
         },
         {
            "name":"SULFA (SULFONAMIDES)"
         }
      ],
      "admission":{
         "admissionDate":"2013-08-19T00:00:00",
         "assignedLocation":{
            "ward":"ED",
            "roomNo":"EMERGENCY DEPARTMENT"
         }
      },
      "patientId":"52125d2157fa831fd6986ad3",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"None",
         "firstPHCPVisit":"None",
         "registration":"2013-08-19T18:00:08",
         "firstBedAssignment":"2013-08-19T17:56:15",
         "firstAttendVisit":"2013-08-19T17:58:45",
         "lastEDMove":"2013-08-19T17:56:15",
         "radiologyOrder":"2013-08-19T18:10:08",
         "firstFinancialRegistration":"2013-08-19T18:04:39",
         "arrival":"2013-08-19T17:56:15",
         "lastBedAssignment":"2013-08-19T17:56:15",
         "careComplete":"2013-08-19T21:32:35",
         "lastMedicalScreening":"2013-08-19T18:07:33",
         "lastFinancialRegistration":"2013-08-19T18:04:39",
         "encounterLock":"None",
         "labOrderTime":"2013-08-19T18:10:08",
         "triage":"2013-08-19T18:19:49",
         "observation":"None",
         "firstMedicalScreening":"2013-08-19T18:07:33",
         "medicineOrder":"2013-08-19T19:29:51",
         "departure":"2013-08-19T23:18:27",
         "bedRequest":"None",
         "encounterCreation":"2013-08-19T17:55:36"
      },
      "homeMedications":[
         {
            "frequency":"daily",
            "medication":"atenolol Oral",
            "dosage":"25 mg",
            "route": "Oral"
         },
         {
            "frequency":"daily",
            "medication":"Lisinopril Oral",
            "dosage":"10 mg",
            "route": "Oral"
         },
         {
            "frequency":"daily",
            "medication":"Caltrate 600 + D Oral",
            "dosage":"None",
            "route": "IV"
         }
      ],
      "financialClass":"Z",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.075013",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.075001",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.075009",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.075016",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.075018",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"101",
               "method":"None",
               "diastolic":"67"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"54.43",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"21.9"
            },
            "pulse":{
               "value":"67",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"157",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T19:17:41",
            "temperature":{
               "value":"97.1",
               "method":"Temporal",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"98",
               "method":"None",
               "diastolic":"52"
            },
            "respiration":{
               "value":"None",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"71",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T23:16:47",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"110",
               "method":"None",
               "diastolic":"70"
            },
            "respiration":{
               "value":"17",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"68",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T21:21:00",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-19T17:56:15.093000",
            "name":"Altered Mental Status"
         }
      ],
      "discharge":{
         "edDischargeTime":"2013-08-19T23:18:27",
         "condition":"Serious"
      },
      "diagnoses":[
         {
            "code":"784.59",
            "type":"Slurred Speech",
            "description":""
         },
         {
            "code":"780.79",
            "type":"Weakness",
            "description":""
         },
         {
            "code":"276.51",
            "type":"Dehydration",
            "description":""
         }
      ],
      "visitNumber":"3147303",
      "lastModified":"2013-08-20T03:22:51.074487",
      "creationTime":"2013-08-20T01:12:03.911000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.075025",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.075028",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.075031",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.075034",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.075038",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.075041",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.075045",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.075048",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"7309883568227723610",
      "medicationsOrdered":[
         {
            "orderId":"10864339",
            "dosageForm":"MISC",
            "minAmount":1,
            "orderedTime":"2013-08-19T22:00:00",
            "dispenseAmount":"1",
            "code":"00000267",
            "unit":"EA",
            "dispenseUnit":"MISC",
            "providerInstruction":"^R.N NOTE: PLEASE VERIFY AND DOCUMENT  DISCHARGE ORDERS INCLUDE:STATIN,  ANTITHROMBOLITIC THERAPY AND  ANTICOAGULATION AS INDICATED FOR STROKE.",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/52125d159606ff381f5d82f8"
   },
   {
      "patientType":"I1",
      "intakesOutputs":[

      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"4101",
            "name":{
               "salutation":"DO",
               "middle":"V.",
               "last":"DEGENHARDT",
               "first":"DAVID"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"unmarried",
         "name":{
            "middle":"Z",
            "last":"Patient 2",
            "first":"Test"
         },
         "ssn":"2899544402856206392",
         "religion":"NP",
         "sex":"male",
         "contactDetails":{
            "homePhone":"(109)555-7815",
            "currentAddress":"5089 TERRAOBEB QE^^JRFG ZRYOBHEAR^SY^107828888^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1940-04-24T00:00:00",
         "mrn":"650401762442682614",
         "race":"Caucasian",
         "id":"52126c1257fa831fc4118f3a"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.075746",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.075742",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.075736",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.075779",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.075774",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.075748",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.075747",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"52126c1257fa831fc59aa7b3",
      "allergies":[
         {
            "name":"No known drug Allergies"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-07-16T00:00:00",
            "name":"NO KNOWN ALLERGIES"
         }
      ],
      "admission":{
         "admissionDate":"2013-08-19T00:00:00",
         "assignedLocation":{
            "ward":"ED",
            "roomNo":"EMERGENCY DEPARTMENT"
         }
      },
      "patientId":"52126c1257fa831fc4118f3a",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-19T19:13:16",
         "firstPHCPVisit":"2013-08-19T18:51:17",
         "registration":"2013-08-19T19:09:46",
         "firstBedAssignment":"2013-08-19T18:49:39",
         "firstAttendVisit":"None",
         "lastEDMove":"2013-08-19T18:49:39",
         "radiologyOrder":"2013-08-19T19:28:05",
         "firstFinancialRegistration":"2013-08-19T20:13:23",
         "arrival":"2013-08-19T18:49:39",
         "lastBedAssignment":"2013-08-19T18:49:39",
         "careComplete":"2013-08-19T20:55:36",
         "lastMedicalScreening":"2013-08-19T18:51:17",
         "lastFinancialRegistration":"2013-08-19T20:13:23",
         "encounterLock":"None",
         "labOrderTime":"2013-08-19T19:28:05",
         "triage":"2013-08-19T19:14:21",
         "observation":"None",
         "firstMedicalScreening":"2013-08-19T18:51:17",
         "medicineOrder":"2013-08-19T20:33:54",
         "departure":"2013-08-19T22:15:38",
         "bedRequest":"None",
         "encounterCreation":"2013-08-19T18:48:34"
      },
      "homeMedications":[
         {
            "frequency":"nightly",
            "medication":"Zetia Oral",
            "dosage":"10 mg",
            "route": "Oral"
         },
         {
            "frequency":"twice a day",
            "medication":"midodrine Oral",
            "dosage":"5 mg",
            "route": "Injection"
         },
         {
            "frequency":"nightly",
            "medication":"Flomax Oral",
            "dosage":"0.4 mg",
            "route": "IV"
         },
         {
            "frequency":"daily",
            "medication":"Glipizide Oral",
            "dosage":"5 mg",
            "route": "Oral"
         },
         {
            "frequency":"after meals",
            "medication":"Carbidopa-Levodopa Oral",
            "dosage":"25-100 mg",
            "route": "IV"
         },
         {
            "frequency":"nightly",
            "medication":"Carbidopa-Levodopa Oral",
            "dosage":"50-200 mg",
            "route": "Oral"
         },
         {
            "frequency":"daily",
            "medication":"AZILECT Oral",
            "dosage":"0.5 mg",
            "route": "Injection"
         },
         {
            "frequency":"daily",
            "medication":"Metformin  Oral",
            "dosage":"850 mg"
         },
         {
            "frequency":"twice a day",
            "medication":"Florastor Oral",
            "dosage":"250 mg ",
            "route": "Oral"
         },
         {
            "frequency":"nightly",
            "medication":"Lantus Sub-Q",
            "dosage":"10 units",
            "route": "Injection"
         },
         {
            "frequency":"daily",
            "medication":"omeprazole Oral",
            "dosage":"20 mg",
            "route": "Injection"
         },
         {
            "frequency":"daily",
            "medication":"Proscar Oral",
            "dosage":"5 mg",
            "route": "Oral"
         },
         {
            "frequency":"three times a day",
            "medication":"Robaxin Oral",
            "dosage":"1000 mg",
            "route": "Oral"
         },
         {
            "frequency":"(on 12hrs, off 12hrs) to L side",
            "medication":"Lidoderm Topical",
            "dosage":"1 patch",
            "route": "IV"
         },
         {
            "frequency":"twice a day",
            "medication":"Ativan Oral",
            "dosage":"1 mg",
            "route": "Injection"
         },
         {
            "frequency":"twice a day",
            "medication":"prostat AWC",
            "dosage":"30ml",
            "route": "Oral"
         },
         {
            "frequency":"daily",
            "medication":"Decubi Vite Oral",
            "dosage":"1 tab",
            "route": "Oral"
         },
         {
            "frequency":"BID before meals",
            "medication":"Questran Oral",
            "dosage":"4 g",
            "route": "IV"
         },
         {
            "frequency":"before meals, nightly",
            "medication":"Novolog Sub-Q",
            "dosage":"SSI",
            "route": "Oral"
         }
      ],
      "financialClass":"Z",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.075714",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.075708",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.075712",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.075716",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.075717",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"120",
               "method":"None",
               "diastolic":"61"
            },
            "respiration":{
               "value":"16",
               "unit":"bpm"
            },
            "weight":{
               "value":"68.04",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"22.2"
            },
            "pulse":{
               "value":"75",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"175",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T19:36:49",
            "temperature":{
               "value":"98.1",
               "method":"Rectal",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"142",
               "method":"None",
               "diastolic":"68"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"69",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T21:30:01",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-19T18:49:39.027000",
            "name":"Altered Mental Status"
         }
      ],
      "discharge":{
         "edDischargeTime":"2013-08-19T22:15:38",
         "condition":"Fair"
      },
      "diagnoses":[
         {
            "code":"780.97",
            "type":"Altered Mental Status",
            "description":""
         },
         {
            "code":"599.0",
            "type":"Urinary Tract Infection (UTI)",
            "description":""
         }
      ],
      "visitNumber":"3147316",
      "lastModified":"2013-08-20T03:22:51.075350",
      "creationTime":"2013-08-20T01:12:02.827000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.075720",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.075722",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.075724",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.075726",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.075728",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.075729",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.075731",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.075732",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"650401762442682614",
      "medicationsOrdered":[

      ],
      "resource_uri":"/v1/encounters/52126c1257fa831fc59aa7b3"
   },
   {
      "patientType":"I1",
      "intakesOutputs":[

      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"4101",
            "name":{
               "salutation":"DO",
               "middle":"V.",
               "last":"DEGENHARDT",
               "first":"DAVID"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"Married",
         "name":{
            "middle":"R",
            "last":"Patient 3",
            "first":"Test"
         },
         "ssn":"3177569509164821781",
         "sex":"F",
         "contactDetails":{
            "workPhone":"",
            "homePhone":"(109)327-9027"
         },
         "dateOfBirth":"1977-06-03T04:00:00",
         "mrn":"3419650173214337302",
         "race":"Caucasian",
         "id":"52121b889606ff0890ee4722"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.076406",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.076403",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.076397",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.076415",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.076412",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.076409",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.076408",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"5212565057fa831a1f56525a",
      "allergies":[
         {
            "name":"No known drug Allergies"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-02-03T00:00:00",
            "name":"NO KNOWN ALLERGIES"
         }
      ],
      "admission":{
         "admissionDate":"2013-08-19T00:00:00",
         "assignedLocation":{
            "ward":"ED",
            "roomNo":"EMERGENCY DEPARTMENT"
         }
      },
      "patientId":"52121b889606ff0890ee4722",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-19T18:26:40",
         "firstPHCPVisit":"None",
         "registration":"2013-08-19T17:35:58",
         "firstBedAssignment":"2013-08-19T17:35:57",
         "firstAttendVisit":"2013-08-19T17:36:35",
         "lastEDMove":"2013-08-19T17:35:57",
         "radiologyOrder":"2013-08-19T17:38:54",
         "firstFinancialRegistration":"2013-08-19T17:52:14",
         "arrival":"2013-08-19T17:30:00",
         "lastBedAssignment":"2013-08-19T17:35:57",
         "careComplete":"2013-08-19T20:02:43",
         "lastMedicalScreening":"2013-08-19T17:38:01",
         "lastFinancialRegistration":"2013-08-19T17:52:14",
         "encounterLock":"None",
         "labOrderTime":"2013-08-19T17:38:54",
         "triage":"2013-08-19T17:38:00",
         "observation":"None",
         "firstMedicalScreening":"2013-08-19T17:38:01",
         "medicineOrder":"2013-08-19T17:38:54",
         "departure":"2013-08-19T21:08:11",
         "bedRequest":"None",
         "encounterCreation":"2013-08-19T17:35:15"
      },
      "homeMedications":[
         {
            "frequency":"as needed, every 4 hours",
            "medication":"DuoNeb Inhl",
            "dosage":"3 ml",
            "route": "eyes"
         },
         {
            "frequency":"nightly",
            "medication":"Coumadin Oral",
            "dosage":"5 mg",
            "route": "oral"
         }
      ],
      "financialClass":"N",
      "vipIndicator":"S",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.076376",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.076369",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.076374",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.076377",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.076379",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"L Arm",
               "orthostatic":"Sitting",
               "systolic":"105",
               "method":"Auto",
               "diastolic":"81"
            },
            "respiration":{
               "value":"22",
               "unit":"bpm"
            },
            "weight":{
               "value":"95.25",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"33.0"
            },
            "pulse":{
               "value":"120",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"170",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T17:55:00",
            "temperature":{
               "value":"99",
               "method":"Temporal",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"None",
               "method":"None",
               "diastolic":"None"
            },
            "respiration":{
               "value":"None",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"None",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T18:01:47",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"None",
               "method":"None",
               "diastolic":"None"
            },
            "respiration":{
               "value":"16",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"110",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T20:10:24",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"None",
               "method":"None",
               "diastolic":"None"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"100",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T17:47:34",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"L Arm",
               "orthostatic":"Sitting",
               "systolic":"136",
               "method":"Auto",
               "diastolic":"75"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"118",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T19:28:00",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"L Arm",
               "orthostatic":"Sitting",
               "systolic":"108",
               "method":"Auto",
               "diastolic":"69"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"120",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T20:53:24",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-19T17:40:42.843000",
            "name":"Asthma Exacerbation"
         }
      ],
      "discharge":{
         "date":"2013-08-19T00:00:00",
         "edDischargeTime":"2013-08-19T21:08:11",
         "condition":"Serious"
      },
      "diagnoses":[
         {
            "code":"518.82",
            "type":"Acute Respiratory Distress/Insufficiency",
            "description":""
         },
         {
            "code":"493.91",
            "type":"Asthma with Status Asthmaticus",
            "description":""
         }
      ],
      "visitNumber":"3147298",
      "lastModified":"2013-08-20T03:22:51.075991",
      "creationTime":"2013-08-20T01:11:49.566000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.076381",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.076383",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.076385",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.076387",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.076388",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.076390",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.076392",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.076393",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"3419650173214337302",
      "medicationsOrdered":[
         {
            "orderId":"10864338",
            "dosageForm":"TAB",
            "minAmount":5,
            "orderedTime":"2013-08-19T22:00:00",
            "dispenseAmount":"1",
            "code":"41239440",
            "unit":"MG",
            "dispenseUnit":"TAB",
            "providerInstruction":"^STERICYCLE CODE: BKC _ANTICOAGULANT COMMON SIDE EFFECTS: BLEEDING,  BRUISING_",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/5212565057fa831a1f56525a"
   },
   {
      "patientType":"N5",
      "intakesOutputs":[
         {
            "intakes":[
               {
                  "amount":50.0,
                  "type":"LUNCH"
               }
            ],
            "observedTime":"2013-08-19T12:54:00"
         },
         {
            "intakes":[
               {
                  "amount":50.0,
                  "type":"BKFST"
               }
            ],
            "observedTime":"2013-08-19T07:55:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"1360",
            "name":{
               "salutation":"MD",
               "last":"LAGUD",
               "first":"ADINARAYANA"
            }
         },
         {
            "role":"AttendingDoctor",
            "id":"2255",
            "name":{
               "salutation":"MD",
               "last":"SANG",
               "first":"NELSON"
            }
         },
         {
            "role":"ReferringDoctor",
            "id":"8899",
            "name":{
               "middle":"DOCTOR",
               "last":"NO",
               "first":"REFERRING"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"0737",
            "name":{
               "salutation":"MD",
               "last":"ELMAGHRABY",
               "first":"ZAKI"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"2507",
            "name":{
               "salutation":"MD",
               "last":"SWAIN",
               "first":"THOMAS"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"3548",
            "name":{
               "salutation":"MD",
               "last":"GOODMAN",
               "first":"GARY"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"married",
         "name":{
            "last":"Patient 4",
            "first":"Test"
         },
         "ssn":"6695556538234240564",
         "id":"5211df9c57fa8368962f3015",
         "contactDetails":{
            "homePhone":"(109)037-9433",
            "currentAddress":"1692 FG NEZRAF PVE^^ZRYOBHEAR^SY^107126130^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1926-01-27T00:00:00",
         "mrn":"8167513295789735823",
         "race":"Caucasian",
         "sex":"male",
         "ethinicGroup":"O"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.077214",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.077211",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.077204",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.077223",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.077220",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.077217",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.077216",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"5211df9c57fa8368921a8fe1",
      "allergies":[
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-19T00:00:00",
            "name":"ERYTHROCIN"
         },
         {
            "name":"clams"
         },
         {
            "name":"Erythromycin"
         }
      ],
      "admission":{
         "admissionDate":"2013-08-19T00:00:00",
         "assignedLocation":{
            "bedNo":"1",
            "ward":"PC",
            "roomNo":"3107"
         },
         "admissionType":"1",
         "providers":[
            {
               "role":"AdmittingDoctor",
               "id":"1360",
               "name":{
                  "salutation":"MD",
                  "last":"LAGUD",
                  "first":"ADINARAYANA"
               }
            }
         ]
      },
      "patientId":"5211df9c57fa8368962f3015",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-19T09:25:48",
         "firstPHCPVisit":"None",
         "registration":"2013-08-19T09:07:07",
         "firstBedAssignment":"2013-08-19T08:59:30",
         "firstAttendVisit":"2013-08-19T09:20:20",
         "lastEDMove":"2013-08-19T08:59:30",
         "radiologyOrder":"2013-08-19T09:11:57",
         "firstFinancialRegistration":"2013-08-19T09:21:54",
         "arrival":"2013-08-19T08:59:30",
         "lastBedAssignment":"2013-08-19T08:59:30",
         "careComplete":"2013-08-19T10:33:42",
         "lastMedicalScreening":"2013-08-19T09:20:20",
         "lastFinancialRegistration":"2013-08-19T09:21:54",
         "encounterLock":"None",
         "labOrderTime":"2013-08-19T09:11:57",
         "triage":"2013-08-19T09:13:07",
         "observation":"None",
         "firstMedicalScreening":"2013-08-19T09:20:20",
         "medicineOrder":"2013-08-19T09:11:57",
         "departure":"2013-08-19T11:28:19",
         "bedRequest":"None",
         "encounterCreation":"2013-08-19T08:58:18"
      },
      "homeMedications":[
         {
            "frequency":"None",
            "medication":"Furosemide Oral",
            "dosage":"Unknown"
         },
         {
            "frequency":"None",
            "medication":"Digoxin Oral",
            "dosage":"None"
         },
         {
            "frequency":"None",
            "medication":"losartan Oral",
            "dosage":"None"
         },
         {
            "frequency":"None",
            "medication":"Amoxicillin Oral",
            "dosage":"None"
         }
      ],
      "financialClass":"Z",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.077180",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.077169",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.077177",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.077183",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.077185",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"117",
               "method":"None",
               "diastolic":"57"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"90",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T10:43:32",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"126",
               "method":"None",
               "diastolic":"57"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"80",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T11:01:35",
            "temperature":{
               "value":"97.1",
               "method":"None",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"65",
               "method":"None",
               "diastolic":"32"
            },
            "respiration":{
               "value":"23",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"80",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T09:30:00",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"118",
               "method":"None",
               "diastolic":"62"
            },
            "respiration":{
               "value":"24",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"78",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T09:37:00",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"115",
               "method":"None",
               "diastolic":"55"
            },
            "respiration":{
               "value":"23",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"80",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T10:07:00",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"140",
               "method":"None",
               "diastolic":"72"
            },
            "respiration":{
               "value":"16",
               "unit":"bpm"
            },
            "weight":{
               "value":"77.11",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"24.4"
            },
            "pulse":{
               "value":"79",
               "method":"Monitor",
               "unit":"bpm"
            },
            "height":{
               "value":"178",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T09:21:35",
            "temperature":{
               "value":"96.2",
               "method":"Temporal",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"65",
               "method":"None",
               "diastolic":"32"
            },
            "respiration":{
               "value":"23",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"80",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T09:31:00",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-19T08:59:29.777000",
            "name":"Chest Pain"
         }
      ],
      "discharge":{
         "date":"2013-08-19T00:00:00",
         "edDischargeTime":"2013-08-19T11:28:19",
         "condition":"Stable"
      },
      "diagnoses":[
         {
            "code":"786.50",
            "type":"Chest Pain",
            "description":""
         },
         {
            "code":"585.9",
            "type":"Chronic Renal Failure/Insufficiency",
            "description":""
         }
      ],
      "visitNumber":"3147187",
      "lastModified":"2013-08-20T03:22:51.076750",
      "creationTime":"2013-08-20T00:01:00.835000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.077189",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.077191",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.077192",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.077194",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.077196",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.077197",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.077199",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.077200",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"8167513295789735823",
      "medicationsOrdered":[
         {
            "orderId":"10864325",
            "dosageForm":"MISC",
            "minAmount":1,
            "orderedTime":"2013-08-19T22:00:00",
            "dispenseAmount":"1",
            "code":"00000267",
            "unit":"EA",
            "dispenseUnit":"MISC",
            "providerInstruction":"^R.N NOTE: PLEASE VERIFY AND DOCUMENT  DISCHARGE ORDERS INCLUDE:ASPIRIN,  B-BLOCKER, ACE (OR) ARB AND STATIN  AS INDICATED FOR AMI.",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/5211df9c57fa8368921a8fe1"
   },
   {
      "patientType":"I",
      "intakesOutputs":[
         {
            "intakes":[
               {
                  "amount":100.0,
                  "type":"SUPPR"
               }
            ],
            "observedTime":"2013-08-19T20:06:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"1757",
            "name":{
               "salutation":"MD",
               "last":"NALIPIREDDY",
               "first":"VASUDEVA"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"unmarried",
         "name":{
            "last":"Patient 5",
            "first":"Test"
         },
         "ssn":"8691223373680516055",
         "id":"5211b5f357fa836895b3fd6e",
         "contactDetails":{
            "homePhone":"(109)086-1342",
            "currentAddress":"9505 NINPNQB NIR^^ZRYOBHEAR^SY^107138888^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1982-05-15T00:00:00",
         "mrn":"7742063704602610142",
         "race":"Hispanic",
         "sex":"male",
         "ethinicGroup":"O"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.077865",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.077861",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.077854",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.077874",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.077872",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.077868",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.077867",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"5211b5ec9606ff08602d3502",
      "allergies":[
         {
            "name":"No known drug Allergies"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-19T00:00:00",
            "name":"NKA"
         }
      ],
      "admission":{
         "admissionDate":"2013-08-19T00:00:00",
         "assignedLocation":{
            "ward":"3412-1",
            "roomNo":"PC"
         }
      },
      "patientId":"5211b5f357fa836895b3fd6e",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-19T06:11:39",
         "firstPHCPVisit":"None",
         "registration":"2013-08-19T06:08:37",
         "firstBedAssignment":"2013-08-19T05:58:24",
         "firstAttendVisit":"2013-08-19T06:02:03",
         "lastEDMove":"2013-08-19T05:58:24",
         "radiologyOrder":"2013-08-19T07:00:03",
         "firstFinancialRegistration":"2013-08-19T06:12:04",
         "arrival":"2013-08-19T05:58:24",
         "lastBedAssignment":"2013-08-19T05:58:24",
         "careComplete":"2013-08-19T07:43:05",
         "lastMedicalScreening":"2013-08-19T06:02:03",
         "lastFinancialRegistration":"2013-08-19T06:12:04",
         "encounterLock":"None",
         "labOrderTime":"2013-08-19T06:04:37",
         "triage":"2013-08-19T06:08:32",
         "observation":"None",
         "firstMedicalScreening":"2013-08-19T06:02:03",
         "medicineOrder":"2013-08-19T06:04:37",
         "departure":"2013-08-19T08:45:34",
         "bedRequest":"None",
         "encounterCreation":"2013-08-19T05:57:13"
      },
      "homeMedications":[

      ],
      "financialClass":"C",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.077833",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.077826",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.077832",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.077835",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.077836",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"130",
               "method":"None",
               "diastolic":"78"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"84",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T08:19:30",
            "temperature":{
               "value":"98.0",
               "method":"Tympanic",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"133",
               "method":"None",
               "diastolic":"72"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"70",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T07:28:00",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"142",
               "method":"None",
               "diastolic":"82"
            },
            "respiration":{
               "value":"16",
               "unit":"bpm"
            },
            "weight":{
               "value":"68.04",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"22.8"
            },
            "pulse":{
               "value":"89",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"173",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T06:09:30",
            "temperature":{
               "value":"97.7",
               "method":"None",
               "unit":"F"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-19T07:43:25.223000",
            "name":"Medical Complaint"
         }
      ],
      "discharge":{
         "date":"2013-08-19T00:00:00",
         "edDischargeTime":"2013-08-19T08:45:34",
         "condition":"Satisfactory"
      },
      "diagnoses":[
         {
            "priority":"8",
            "code":"7557",
            "type":"N",
            "codingMethod":"V7",
            "description":"CBVFBA-ZRQVPVANY NTG ABF"
         },
         {
            "priority":"9",
            "code":"7557",
            "type":"C",
            "codingMethod":"V7",
            "description":"CBVFBA-ZRQVPVANY NTG ABF"
         },
         {
            "priority":"0",
            "code":"50666",
            "type":"F",
            "codingMethod":"V7",
            "description":"EUNOQBZLBYLFVF"
         },
         {
            "priority":"0",
            "code":"18279",
            "type":"F",
            "codingMethod":"V7",
            "description":"QEHT QRCRAQ ABF-PBAGVA"
         },
         {
            "priority":"0",
            "code":"1350",
            "type":"F",
            "codingMethod":"V7",
            "description":"ARHEBCNGUL VA QVNORGRF"
         },
         {
            "priority":"0",
            "code":"1839",
            "type":"F",
            "codingMethod":"V7",
            "description":"GBONPPB HFR QVFBEQRE"
         },
         {
            "priority":"0",
            "code":"R7683",
            "type":"F",
            "codingMethod":"V7",
            "description":"HAQRG CBVF-ZRQ NTAG ABF"
         },
         {
            "priority":"0",
            "code":"56875",
            "type":"F",
            "codingMethod":"V7",
            "description":"NYGRERQ ZRAGNY FGNGHF"
         },
         {
            "priority":"0",
            "code":"03848",
            "type":"F",
            "codingMethod":"V7",
            "description":"QZVV ARHEB AG FG HAPAGEY"
         },
         {
            "priority":"0",
            "code":"59724",
            "type":"F",
            "codingMethod":"V7",
            "description":"WBVAG CNVA-Y/YRT"
         },
         {
            "priority":"0",
            "code":"85698",
            "type":"F",
            "codingMethod":"V7",
            "description":"IVENY JNEGF ABF"
         }
      ],
      "visitNumber":"3147185",
      "lastModified":"2013-08-20T03:22:51.077436",
      "creationTime":"2013-08-20T01:25:27.647000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.077839",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.077841",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.077843",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.077844",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.077846",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.077848",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.077850",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.077851",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"7742063704602610142",
      "medicationsOrdered":[
         {
            "orderId":"10864337",
            "dosageForm":"SOLN",
            "minAmount":15,
            "orderedTime":"2013-08-19T21:25:00",
            "dispenseAmount":"1",
            "code":"41219910",
            "unit":"MG",
            "dispenseUnit":"SOLN",
            "providerInstruction":"^_NON-STEROIDAL ANTI-INFLAMATORY  (PAIN,FEVER, INFLAMMATION) COMMON SIDE EFFECTS: STOMACH PAIN,  DYSPEPSIA, N/V, CONSTIPATION, H/A,  DIARRHEA, GASTRITIS, RECTAL BLEED,  SWEATING_",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/5211b5ec9606ff08602d3502"
   },
   {
      "patientType":"I1",
      "intakesOutputs":[
         {
            "outputs":[
               {
                  "amount":350.0,
                  "type":"VOID"
               }
            ],
            "observedTime":"2013-08-19T16:50:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"4101",
            "name":{
               "salutation":"DO",
               "middle":"V.",
               "last":"DEGENHARDT",
               "first":"DAVID"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"unmarried",
         "name":{
            "middle":"YBH",
            "last":"Patient 6",
            "first":"Test"
         },
         "ssn":"3349569207433711269",
         "id":"5212167257fa836890700202",
         "contactDetails":{
            "homePhone":"(109)525-7622",
            "currentAddress":"2886 YHPREAR PG^^ZRYOBHEAR^SY^10782^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1949-12-23T00:00:00",
         "mrn":"3682382223611956923",
         "race":"Other",
         "sex":"female",
         "ethinicGroup":"O"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.078643",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.078639",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.078632",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.078656",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.078649",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.078646",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.078645",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"521216659606ff087874e400",
      "allergies":[
         {
            "name":"actofed"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-19T00:00:00",
            "name":"TRIPROLIDINE"
         }
      ],
      "admission":{
         "dischargeDate":"2013-08-19T00:00:00",
         "admissionDate":"2013-08-19T00:00:00",
         "assignedLocation":{
            "ward":"ER"
         }
      },
      "patientId":"5212167257fa836890700202",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-19T13:36:12",
         "firstPHCPVisit":"None",
         "registration":"2013-08-19T12:58:29",
         "firstBedAssignment":"2013-08-19T13:11:26",
         "firstAttendVisit":"2013-08-19T13:14:17",
         "lastEDMove":"2013-08-19T13:11:26",
         "radiologyOrder":"2013-08-19T13:27:27",
         "firstFinancialRegistration":"2013-08-19T13:32:17",
         "arrival":"2013-08-19T12:58:00",
         "lastBedAssignment":"2013-08-19T13:11:26",
         "careComplete":"2013-08-19T14:52:17",
         "lastMedicalScreening":"2013-08-19T13:25:59",
         "lastFinancialRegistration":"2013-08-19T13:32:17",
         "encounterLock":"None",
         "labOrderTime":"2013-08-19T13:27:27",
         "triage":"2013-08-19T13:27:44",
         "observation":"None",
         "firstMedicalScreening":"2013-08-19T13:25:59",
         "medicineOrder":"2013-08-19T13:35:26",
         "departure":"None",
         "bedRequest":"None",
         "encounterCreation":"2013-08-19T12:58:27"
      },
      "homeMedications":[
         {
            "frequency":"twice a day",
            "medication":"lisinopril Oral",
            "dosage":"20 mg"
         },
         {
            "frequency":"nightly",
            "medication":"Simvastatin Oral",
            "dosage":"20 mg"
         },
         {
            "frequency":"daily",
            "medication":"D3",
            "dosage":"1000I"
         },
         {
            "frequency":"twice a day",
            "medication":"Metoprolol Tartrate Oral",
            "dosage":"100 mg"
         },
         {
            "frequency":"daily",
            "medication":"Levothroid Oral",
            "dosage":"75 mcg"
         },
         {
            "frequency":"daily",
            "medication":"loratadine Oral",
            "dosage":"10 mg"
         },
         {
            "frequency":"daily",
            "medication":"amlodipine Oral",
            "dosage":"5 mg"
         },
         {
            "frequency":"twice a day",
            "medication":"Metformin  Oral",
            "dosage":"500 mg"
         },
         {
            "frequency":"daily",
            "medication":"Aspirin Oral",
            "dosage":"81 mg"
         }
      ],
      "financialClass":"R",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.078599",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.078592",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.078597",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.078600",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.078602",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"R Arm",
               "orthostatic":"Sitting",
               "systolic":"173",
               "method":"Auto",
               "diastolic":"70"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"71",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T16:15:00",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"Right Arm",
               "orthostatic":"Sitting",
               "systolic":"161",
               "method":"Auto",
               "diastolic":"73"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"72",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T15:15:00",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"201",
               "method":"None",
               "diastolic":"85"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"65.32",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"23.2"
            },
            "pulse":{
               "value":"81",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"168",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T13:33:33",
            "temperature":{
               "value":"97.5",
               "method":"Temporal",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"R Arm",
               "orthostatic":"Sitting",
               "systolic":"160",
               "method":"Auto",
               "diastolic":"72"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"72",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T16:54:12",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"Right Arm",
               "orthostatic":"Sitting",
               "systolic":"165",
               "method":"Auto",
               "diastolic":"77"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"80",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T14:25:00",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-19T12:58:46.887000",
            "name":"Dizziness"
         },
         {
            "complaintTime":"2013-08-19T12:58:46.893000",
            "name":"High Blood Pressure"
         }
      ],
      "discharge":{
         "date":"2013-08-19T00:00:00"
      },
      "diagnoses":[
         {
            "code":"780.4",
            "type":"Dizziness - Vertigo",
            "description":""
         },
         {
            "code":"401.9",
            "type":"Hypertensive Emergency",
            "description":""
         }
      ],
      "visitNumber":"3147214",
      "lastModified":"2013-08-20T03:22:51.078099",
      "creationTime":"2013-08-20T02:13:16.721000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.078604",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.078613",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.078615",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.078617",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.078619",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.078620",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.078622",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.078623",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"3682382223611956923",
      "medicationsOrdered":[
         {
            "orderId":"10864033",
            "dosageForm":"TAB",
            "minAmount":325,
            "orderedTime":"2013-08-19T17:00:00",
            "dispenseAmount":"1",
            "code":"41202260",
            "unit":"MG",
            "dispenseUnit":"TAB",
            "providerInstruction":"^_ANTIPLATELET  COMMON SIDE EFFECTS: BLEEDING, UPSET  STOMACH, BRUISING_",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/521216659606ff087874e400"
   },
   {
      "patientType":"I",
      "intakesOutputs":[

      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"4101",
            "name":{
               "salutation":"DO",
               "middle":"V.",
               "last":"DEGENHARDT",
               "first":"DAVID"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"Single",
         "name":{
            "middle":"None",
            "last":"Patient 7",
            "first":"Test"
         },
         "ssn":"8370062220418061738",
         "sex":"M",
         "contactDetails":{
            "workPhone":"",
            "homePhone":"(569)398-8349"
         },
         "dateOfBirth":"1946-09-04T05:00:00",
         "mrn":"7716278348032036710",
         "race":"Caucasian",
         "id":"5212551157fa831a12e877ce"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.079487",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.079483",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.079477",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.079496",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.079493",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.079490",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.079489",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"521255049606ff32ca6e7787",
      "allergies":[
         {
            "name":"No known drug Allergies"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-04T00:00:00",
            "name":"NO KNOWN ALLERGIES"
         }
      ],
      "admission":{
         "dischargeDate":"2013-08-19T00:00:00",
         "admissionDate":"2013-08-19T00:00:00",
         "assignedLocation":{
            "ward":"QUE",
            "roomNo":"ER QUICK ADMIT"
         }
      },
      "patientId":"5212551157fa831a12e877ce",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"None",
         "firstPHCPVisit":"None",
         "registration":"2013-08-19T17:26:00",
         "firstBedAssignment":"2013-08-19T17:38:17",
         "firstAttendVisit":"2013-08-19T17:42:32",
         "lastEDMove":"2013-08-19T17:38:17",
         "radiologyOrder":"2013-08-19T17:48:13",
         "firstFinancialRegistration":"2013-08-19T18:01:36",
         "arrival":"2013-08-19T17:25:00",
         "lastBedAssignment":"2013-08-19T17:38:17",
         "careComplete":"2013-08-19T21:13:05",
         "lastMedicalScreening":"2013-08-19T17:47:35",
         "lastFinancialRegistration":"2013-08-19T18:01:36",
         "encounterLock":"None",
         "labOrderTime":"2013-08-19T17:48:13",
         "triage":"2013-08-19T17:38:37",
         "observation":"None",
         "firstMedicalScreening":"2013-08-19T17:47:35",
         "medicineOrder":"2013-08-19T19:14:22",
         "departure":"2013-08-19T22:42:07",
         "bedRequest":"None",
         "encounterCreation":"2013-08-19T17:25:58"
      },
      "homeMedications":[
         {
            "frequency":"as needed, every 4 hours",
            "medication":"Morphine Oral",
            "dosage":"15 mg"
         },
         {
            "frequency":"Q 3 DAYS",
            "medication":"Fentanyl Patch Topical",
            "dosage":"50 mcg/hr"
         }
      ],
      "financialClass":"R",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.079454",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.079447",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.079452",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.079456",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.079457",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"143",
               "method":"None",
               "diastolic":"84"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"72.57",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"22.3"
            },
            "pulse":{
               "value":"87",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"180",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T17:52:11",
            "temperature":{
               "value":"98.5",
               "method":"Temporal",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"138",
               "method":"None",
               "diastolic":"78"
            },
            "respiration":{
               "value":"17",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"81",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T22:25:00",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-19T17:26:31.900000",
            "name":"Shortness Of Breath"
         },
         {
            "complaintTime":"2013-08-19T17:26:31.933000",
            "name":"Difficulty Swallowing"
         },
         {
            "complaintTime":"2013-08-19T17:26:31.950000",
            "name":"Chest Pain"
         }
      ],
      "discharge":{
         "date":"2013-08-19T00:00:00",
         "edDischargeTime":"2013-08-19T22:42:07",
         "condition":"Serious"
      },
      "diagnoses":[
         {
            "code":"786.09",
            "type":"Dyspnea",
            "description":""
         },
         {
            "code":"162.9",
            "type":"Lung Cancer",
            "description":""
         },
         {
            "code":"276.8",
            "type":"Hypokalemia",
            "description":""
         },
         {
            "code":"275.41",
            "type":"Hypocalcemia",
            "description":""
         }
      ],
      "visitNumber":"3147296",
      "lastModified":"2013-08-20T03:22:51.078934",
      "creationTime":"2013-08-20T01:12:32.214000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.079460",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.079462",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.079464",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.079466",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.079468",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.079470",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.079471",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.079472",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"7716278348032036710",
      "medicationsOrdered":[

      ],
      "resource_uri":"/v1/encounters/521255049606ff32ca6e7787"
   },
   {
      "patientType":"O",
      "intakesOutputs":[
         {
            "intakes":[
               {
                  "amount":480.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-19T07:27:00"
         },
         {
            "intakes":[
               {
                  "amount":80.0,
                  "type":"LUNCH"
               }
            ],
            "observedTime":"2013-08-19T11:58:00"
         },
         {
            "outputs":[
               {
                  "amount":750.0,
                  "type":"VOID"
               }
            ],
            "observedTime":"2013-08-19T16:57:00"
         },
         {
            "intakes":[
               {
                  "amount":50.0,
                  "type":"BKFST"
               }
            ],
            "observedTime":"2013-08-19T08:12:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"8691757",
            "name":{
               "last":"NALIPIREDDY",
               "first":"VASUDEVA"
            }
         },
         {
            "role":"ReferringDoctor",
            "id":"8691757",
            "name":{
               "last":"NALIPIREDDY",
               "first":"VASUDEVA"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"unmarried",
         "name":{
            "last":"Patient 8",
            "first":"Test"
         },
         "ssn":"1135152088410276880",
         "religion":"NP",
         "sex":"male",
         "contactDetails":{
            "homePhone":"(109)508-7283",
            "currentAddress":"0301 TYNFOREA PVE^^JRFG ZRYOBHEAR^SY^107826852^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1963-03-13T00:00:00",
         "mrn":"1243790403352200246",
         "race":"Caucasian",
         "id":"5211496557fa836895b3f8f3"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.080122",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.080115",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.080105",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.080141",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.080135",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.080128",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.080126",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"5211495e9606ff0883255a11",
      "allergies":[
         {
            "name":"No known drug Allergies"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-18T00:00:00",
            "name":"NO KNOWN ALLERGIES"
         }
      ],
      "admission":{
         "dischargeDate":"2013-08-19T00:00:00",
         "admissionDate":"2013-08-18T00:00:00"
      },
      "patientId":"5211496557fa836895b3f8f3",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-18T23:40:58",
         "firstPHCPVisit":"2013-08-18T22:27:46",
         "registration":"2013-08-18T22:23:58",
         "firstBedAssignment":"2013-08-18T22:27:09",
         "firstAttendVisit":"None",
         "lastEDMove":"2013-08-18T22:27:09",
         "radiologyOrder":"2013-08-18T22:36:06",
         "firstFinancialRegistration":"2013-08-18T22:25:02",
         "arrival":"2013-08-18T22:23:00",
         "lastBedAssignment":"2013-08-18T22:27:09",
         "careComplete":"2013-08-19T00:03:54",
         "lastMedicalScreening":"2013-08-18T22:27:46",
         "lastFinancialRegistration":"2013-08-18T22:25:02",
         "encounterLock":"None",
         "labOrderTime":"2013-08-18T22:36:06",
         "triage":"2013-08-18T22:28:56",
         "observation":"None",
         "firstMedicalScreening":"2013-08-18T22:27:46",
         "medicineOrder":"2013-08-18T22:36:06",
         "departure":"2013-08-19T02:44:05",
         "bedRequest":"None",
         "encounterCreation":"2013-08-18T22:23:56"
      },
      "homeMedications":[
         {
            "frequency":"None",
            "medication":"Metformin  Oral",
            "dosage":"Unknown"
         },
         {
            "frequency":"None",
            "medication":"Lisinopril Oral",
            "dosage":"Unknown"
         },
         {
            "frequency":"None",
            "medication":"Hydrocodone-Acetaminophen Oral",
            "dosage":"Unknown"
         },
         {
            "frequency":"twice a day",
            "medication":"Metformin  Oral",
            "dosage":"500 mg"
         },
         {
            "frequency":"daily",
            "medication":"Lisinopril Oral",
            "dosage":"2.5 mg"
         },
         {
            "frequency":"as needed, every 6 hours",
            "medication":"Hydrocodone-Acetaminophen Oral",
            "dosage":"5-500 mg"
         }
      ],
      "financialClass":"Z",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.080083",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.080077",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.080082",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.080085",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.080086",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"110",
               "method":"None",
               "diastolic":"66"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"70",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T01:11:23",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"122",
               "method":"None",
               "diastolic":"68"
            },
            "respiration":{
               "value":"16",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"78",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T02:28:57",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"129",
               "method":"None",
               "diastolic":"64"
            },
            "respiration":{
               "value":"16",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"85",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T23:45:01",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"206",
               "method":"None",
               "diastolic":"99"
            },
            "respiration":{
               "value":"12",
               "unit":"bpm"
            },
            "weight":{
               "value":"90.72",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"27.1"
            },
            "pulse":{
               "value":"76",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"183",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T22:33:57",
            "temperature":{
               "value":"98.4",
               "method":"None",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"129",
               "method":"None",
               "diastolic":"64"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"80",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T23:46:13",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-18T22:24:22.510000",
            "name":"Dizziness"
         }
      ],
      "discharge":{
         "date":"2013-08-19T00:00:00",
         "edDischargeTime":"2013-08-19T02:44:05",
         "condition":"Good"
      },
      "diagnoses":[
         {
            "code":"785.1",
            "type":"Palpitations",
            "description":""
         },
         {
            "code":"780.79",
            "type":"Weakness",
            "description":""
         }
      ],
      "visitNumber":"3147169",
      "lastModified":"2013-08-20T03:22:51.079728",
      "creationTime":"2013-08-20T00:48:53.609000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.080089",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.080092",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.080093",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.080095",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.080097",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.080098",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.080100",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.080101",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"1243790403352200246",
      "medicationsOrdered":[
         {
            "orderId":"10863785",
            "dosageForm":"TAB",
            "minAmount":50,
            "orderedTime":"2013-08-19T18:00:00",
            "dispenseAmount":"1",
            "code":"41224110",
            "unit":"MG",
            "dispenseUnit":"TAB",
            "providerInstruction":"^GIVE WITH A SMALL SIP OF WATER EVEN  IF ORAL INTAKE STATUS IS NPO. IF SYSTOLIC BLOOD PRESSURE IS LESS  THAN 100 MMHG, HOLD DOSE AND CONTACT  PHYSICIAN FOR PARAMETERS. _BETA BLOCKER (HR,B/P,ANGINA,  MIGRAINE) COMMON SIDE EFFECTS: LOW B/P,  DIZZINESS, IRREGULAR HEART RATE_",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/5211495e9606ff0883255a11"
   },
   {
      "patientType":"I1",
      "intakesOutputs":[
         {
            "outputs":[
               {
                  "amount":1.0,
                  "type":"STOOL"
               }
            ],
            "observedTime":"2013-08-19T18:51:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"1757",
            "name":{
               "salutation":"MD",
               "last":"NALIPIREDDY",
               "first":"VASUDEVA"
            }
         },
         {
            "role":"ReferringDoctor",
            "id":"8899",
            "name":{
               "middle":"DOCTOR",
               "last":"NO",
               "first":"REFERRING"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"0737",
            "name":{
               "salutation":"MD",
               "last":"ELMAGHRABY",
               "first":"ZAKI"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"3548",
            "name":{
               "salutation":"MD",
               "last":"GOODMAN",
               "first":"GARY"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"unmarried",
         "name":{
            "middle":"N",
            "last":"Patient 9",
            "first":"Test"
         },
         "ssn":"1602388335622837923",
         "religion":"NP",
         "id":"5211736d57fa836895b3fb06",
         "contactDetails":{
            "workPhone":"(109)037-2378",
            "homePhone":"(109)037-2378",
            "currentAddress":"9508 NAPUBENTR YA YBG 6^^ZRYOBHEAR^SY^107138888^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1964-01-31T00:00:00",
         "mrn":"5822463540997443537",
         "race":"Caucasian",
         "sex":"female",
         "ethinicGroup":"O"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.080765",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.080762",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.080756",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.080774",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.080771",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.080768",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.080767",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"5211736d57fa83688fa108e7",
      "allergies":[
         {
            "name":"Benadryl"
         },
         {
            "name":"Vistaril IM"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-02-01T00:00:00",
            "name":"VISTARIL"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2011-12-22T00:00:00",
            "name":"PENICILLIN CLASS ALLERGY"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2011-12-22T00:00:00",
            "name":"DIPHENHYDRAMINE"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2011-12-22T00:00:00",
            "name":"SULFONYLUREA ALLERGY"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2012-05-06T00:00:00",
            "name":"TRAMADOL"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2011-12-22T00:00:00",
            "name":"ERYTHROMYCIN ALLERGY"
         },
         {
            "name":"Ultram"
         },
         {
            "name":"SULFA (SULFONAMIDES)"
         },
         {
            "name":"Erythromycin"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-02-01T00:00:00",
            "name":"IBUPROFEN"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2011-12-22T00:00:00",
            "name":"ASPIRIN"
         },
         {
            "name":"PENICILLINS"
         },
         {
            "severityLevel":"other",
            "reaction":"swollen sking and marks^",
            "identificationDate":"2011-12-22T00:00:00",
            "name":"ADHESIVE TAPE",
            "type":"drug"
         }
      ],
      "admission":{
         "admissionDate":"2013-08-18T00:00:00",
         "assignedLocation":{
            "bedNo":"1",
            "ward":"MS",
            "roomNo":"2107"
         },
         "admissionType":"1",
         "providers":[
            {
               "role":"AdmittingDoctor",
               "id":"1757",
               "name":{
                  "salutation":"MD",
                  "last":"NALIPIREDDY",
                  "first":"VASUDEVA"
               }
            }
         ]
      },
      "patientId":"5211736d57fa836895b3fb06",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"None",
         "firstPHCPVisit":"None",
         "registration":"2013-08-19T01:23:01",
         "firstBedAssignment":"2013-08-19T01:22:00",
         "firstAttendVisit":"2013-08-19T01:26:40",
         "lastEDMove":"2013-08-19T01:22:00",
         "radiologyOrder":"2013-08-19T01:41:43",
         "firstFinancialRegistration":"2013-08-19T01:23:42",
         "arrival":"2013-08-19T01:21:47",
         "lastBedAssignment":"2013-08-19T01:22:00",
         "careComplete":"2013-08-19T02:42:13",
         "lastMedicalScreening":"2013-08-19T01:26:40",
         "lastFinancialRegistration":"2013-08-19T01:23:42",
         "encounterLock":"None",
         "labOrderTime":"2013-08-19T01:41:43",
         "triage":"2013-08-19T01:27:14",
         "observation":"None",
         "firstMedicalScreening":"2013-08-19T01:26:40",
         "medicineOrder":"2013-08-19T01:41:43",
         "departure":"2013-08-19T03:51:06",
         "bedRequest":"None",
         "encounterCreation":"2013-08-19T01:20:32"
      },
      "homeMedications":[
         {
            "frequency":"daily",
            "medication":"Fluoxetine Oral",
            "dosage":"40 mg"
         },
         {
            "frequency":"twice a day",
            "medication":"topiramate Oral",
            "dosage":"150mg"
         },
         {
            "frequency":"as needed, three times a day",
            "medication":"Flexeril Oral",
            "dosage":"10 mg"
         },
         {
            "frequency":"nightly",
            "medication":"clozapine Oral",
            "dosage":"100 mg"
         },
         {
            "frequency":"twice a day",
            "medication":"Lyrica Oral",
            "dosage":"100 mg"
         },
         {
            "frequency":"daily",
            "medication":"meloxicam Oral",
            "dosage":"15 mg"
         },
         {
            "frequency":"daily",
            "medication":"pantoprazole Oral",
            "dosage":"40 mg"
         },
         {
            "frequency":"daily",
            "medication":"Enalapril Oral",
            "dosage":"2.5 mg"
         },
         {
            "frequency":"daily",
            "medication":"Ranitidine Oral",
            "dosage":"300 mg"
         },
         {
            "frequency":"daily",
            "medication":"Fluoxetine Oral",
            "dosage":"60 mg"
         },
         {
            "frequency":"None",
            "medication":"Albuterol Nebulizer",
            "dosage":"2.5 MG/3ML HHN Q 6 H PRN"
         },
         {
            "frequency":"daily",
            "medication":"Bumex Oral",
            "dosage":"2 mg"
         },
         {
            "frequency":"every 8 hours",
            "medication":"Lortab 10 Oral",
            "dosage":"1 tablet"
         },
         {
            "frequency":"None",
            "medication":"Ventolin Nebulizer",
            "dosage":"90 MCG HFA AER BID PRN"
         }
      ],
      "financialClass":"N",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.080735",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.080728",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.080733",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.080736",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.080738",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"133",
               "method":"None",
               "diastolic":"78"
            },
            "respiration":{
               "value":"22",
               "unit":"bpm"
            },
            "weight":{
               "value":"81.65",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"35.2"
            },
            "pulse":{
               "value":"100",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"152",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T03:13:24",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"145",
               "method":"None",
               "diastolic":"86"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"98",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T03:50:36",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"130",
               "method":"None",
               "diastolic":"68"
            },
            "respiration":{
               "value":"24",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"100",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-19T01:35:18",
            "temperature":{
               "value":"98.6",
               "method":"Oral",
               "unit":"F"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-19T01:22:00.393000",
            "name":"Breathing Difficulty"
         }
      ],
      "discharge":{
         "date":"2013-08-18T00:00:00",
         "edDischargeTime":"2013-08-19T03:51:06",
         "condition":"Stable"
      },
      "diagnoses":[
         {
            "priority":"8",
            "code":"27909",
            "type":"N",
            "codingMethod":"V7",
            "description":"BOF PUE OEBAP J(NP) RKNP"
         },
         {
            "priority":"9",
            "code":"27909",
            "type":"C",
            "codingMethod":"V7",
            "description":"BOF PUE OEBAP J(NP) RKNP"
         },
         {
            "priority":"0",
            "code":"12618",
            "type":"F",
            "codingMethod":"V7",
            "description":"RAPRCUNYBCNGUL ABF"
         },
         {
            "priority":"0",
            "code":"0549",
            "type":"F",
            "codingMethod":"V7",
            "description":"ULCBFZBYNYVGL"
         },
         {
            "priority":"0",
            "code":"50666",
            "type":"F",
            "codingMethod":"V7",
            "description":"EUNOQBZLBYLFVF"
         },
         {
            "priority":"0",
            "code":"56418",
            "type":"F",
            "codingMethod":"V7",
            "description":"URZBCGLFVF ABF"
         },
         {
            "priority":"0",
            "code":"0637",
            "type":"F",
            "codingMethod":"V7",
            "description":"NARZVN ABF"
         }
      ],
      "visitNumber":"3147178",
      "lastModified":"2013-08-20T03:22:51.080377",
      "creationTime":"2013-08-19T23:46:14.429000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.080740",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.080742",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.080744",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.080745",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.080747",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.080749",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.080751",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.080752",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"5822463540997443537",
      "medicationsOrdered":[
         {
            "orderId":"10864232",
            "dosageForm":"CAP",
            "minAmount":150,
            "orderedTime":"2013-08-19T20:00:00",
            "dispenseAmount":"2",
            "code":"41203943",
            "unit":"MG",
            "dispenseUnit":"CAP",
            "providerInstruction":"^_ANTACID (ULCERS,GERD, HYPERSECRETORY)  COMMON SIDE EFFECTS: HEADACHE, DIZZINESS, CONSTIPATION, DIARRHEA,  NAUSEA, VOMITING, ABDOMINAL  DISCOMFORT_",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/5211736d57fa83688fa108e7"
   },
   {
      "patientType":"N5",
      "intakesOutputs":[
         {
            "intakes":[
               {
                  "amount":1000.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-19T05:36:00"
         },
         {
            "outputs":[
               {
                  "amount":2.0,
                  "type":"STOOL"
               }
            ],
            "observedTime":"2013-08-19T18:18:00"
         },
         {
            "intakes":[
               {
                  "amount":1420.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-18T17:19:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"1456",
            "name":{
               "salutation":"MD",
               "last":"LORENTE",
               "first":"MIGUEL"
            }
         },
         {
            "role":"AttendingDoctor",
            "id":"3417",
            "name":{
               "salutation":"MD",
               "last":"HARDOON",
               "first":"SCOTT"
            }
         },
         {
            "role":"ReferringDoctor",
            "id":"8899",
            "name":{
               "middle":"DOCTOR",
               "last":"NO",
               "first":"REFERRING"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"1144",
            "name":{
               "salutation":"MD",
               "last":"HYNES",
               "first":"RICHARD"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"2960",
            "name":{
               "salutation":"DO",
               "last":"HARBOUR",
               "first":"DAVID"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"unmarried",
         "name":{
            "last":"Patient 10",
            "first":"Test"
         },
         "ssn":"4536970345502327832",
         "religion":"CA",
         "id":"521064099606ff088f5a69a4",
         "contactDetails":{
            "homePhone":"(109)236-1832",
            "currentAddress":"1193 SENAXVR YNAR^^PBPBN^SY^107048888^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1955-06-07T00:00:00",
         "mrn":"86017545243754652",
         "race":"Caucasian",
         "sex":"female",
         "ethinicGroup":"O"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.081399",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.081396",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.081390",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.081408",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.081406",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.081403",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.081402",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"521064919606ff0890ee2d63",
      "allergies":[
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-19T00:00:00",
            "name":"CODEINE"
         },
         {
            "name":"TOMATO (SOLANUM LYCOPERSICUM)"
         },
         {
            "name":"SULFA (SULFONAMIDES)"
         },
         {
            "name":"Percocet"
         },
         {
            "name":"Wasps"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-19T00:00:00",
            "name":"PERCODAN"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-19T00:00:00",
            "name":"OXYCODONE"
         },
         {
            "name":"Lortab"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-19T00:00:00",
            "name":"HYDROMORPHONE"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-19T00:00:00",
            "name":"ADHESIVE"
         },
         {
            "name":"lidoderm patch"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-19T00:00:00",
            "name":"SULFA(SULFONAMIDE ANTIBIOTICS)"
         },
         {
            "name":"Bees"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-19T00:00:00",
            "name":"DARVOCET"
         },
         {
            "name":"peppers"
         },
         {
            "name":"Darvon"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-19T00:00:00",
            "name":"METFORMIN"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-19T00:00:00",
            "name":"ASPIRIN"
         },
         {
            "name":"paper tape"
         },
         {
            "name":"Nicoderm CQ"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-19T00:00:00",
            "name":"AMOXICILLIN/CLAVULANATE POTASSI"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-19T00:00:00",
            "name":"OXYCONTIN"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-19T00:00:00",
            "name":"MORPHINE"
         },
         {
            "name":"ONION"
         },
         {
            "name":"Amoxicillin"
         },
         {
            "name":"Dilaudid"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-19T00:00:00",
            "name":"CHLORAL HYDRATE"
         },
         {
            "name":"Metformin HCl"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-07-23T00:00:00",
            "name":"THORAZINE"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-03-19T00:00:00",
            "name":"DARVON-N"
         }
      ],
      "admission":{
         "admissionDate":"2013-08-18T00:00:00",
         "assignedLocation":{
            "bedNo":"1",
            "ward":"MS",
            "roomNo":"2108"
         },
         "admissionType":"1",
         "providers":[
            {
               "role":"AdmittingDoctor",
               "id":"1456",
               "name":{
                  "salutation":"MD",
                  "last":"LORENTE",
                  "first":"MIGUEL"
               }
            }
         ]
      },
      "patientId":"521064099606ff088f5a69a4",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-18T06:44:33",
         "firstPHCPVisit":"None",
         "registration":"2013-08-18T06:07:24",
         "firstBedAssignment":"2013-08-18T05:59:20",
         "firstAttendVisit":"2013-08-18T06:03:34",
         "lastEDMove":"2013-08-18T05:59:43",
         "radiologyOrder":"2013-08-18T06:44:12",
         "firstFinancialRegistration":"2013-08-18T06:44:03",
         "arrival":"2013-08-18T05:59:20",
         "lastBedAssignment":"2013-08-18T05:59:43",
         "careComplete":"2013-08-18T09:01:47",
         "lastMedicalScreening":"2013-08-18T06:03:34",
         "lastFinancialRegistration":"2013-08-18T06:44:03",
         "encounterLock":"None",
         "labOrderTime":"2013-08-18T06:44:12",
         "triage":"2013-08-18T06:15:59",
         "observation":"None",
         "firstMedicalScreening":"2013-08-18T06:03:34",
         "medicineOrder":"2013-08-18T06:44:12",
         "departure":"2013-08-18T09:54:20",
         "bedRequest":"None",
         "encounterCreation":"2013-08-18T05:56:38"
      },
      "homeMedications":[
         {
            "frequency":"daily",
            "medication":"Plavix Oral",
            "dosage":"75 mg"
         },
         {
            "frequency":"daily",
            "medication":"Januvia Oral",
            "dosage":"100 mg"
         },
         {
            "frequency":"daily",
            "medication":"pantoprazole Oral",
            "dosage":"40 mg"
         },
         {
            "frequency":"daily",
            "medication":"Simvastatin Oral",
            "dosage":"40 mg"
         },
         {
            "frequency":"twice a day",
            "medication":"Ranitidine Oral",
            "dosage":"150 mg"
         },
         {
            "frequency":"daily",
            "medication":"Calcium-Vitamin D Oral",
            "dosage":"600mg"
         },
         {
            "frequency":"daily",
            "medication":"B-Complex Oral",
            "dosage":"None"
         },
         {
            "frequency":"daily",
            "medication":"Multi-Vite Oral",
            "dosage":"1 tablet"
         },
         {
            "frequency":"as needed, every 6 hours",
            "medication":"Demerol Oral",
            "dosage":"100 mg"
         },
         {
            "frequency":"four times a day",
            "medication":"Valium Oral",
            "dosage":"10 mg"
         },
         {
            "frequency":"as needed",
            "medication":"tramadol Oral",
            "dosage":"50 mg"
         },
         {
            "frequency":"daily",
            "medication":"hydroxyzine HCl Oral",
            "dosage":"100 mg"
         },
         {
            "frequency":"as needed",
            "medication":"epi-pen",
            "dosage":"None"
         },
         {
            "frequency":"as needed",
            "medication":"DuoNeb Inhl",
            "dosage":"2.5-0.5 mg/3 mL"
         }
      ],
      "financialClass":"R",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.081369",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.081362",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.081367",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.081370",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.081372",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"None",
               "method":"None",
               "diastolic":"None"
            },
            "respiration":{
               "value":"None",
               "unit":"bpm"
            },
            "weight":{
               "value":"47.63",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"21.2"
            },
            "pulse":{
               "value":"None",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"150",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T09:19:11",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"138",
               "method":"None",
               "diastolic":"80"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"78",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T09:35:52",
            "temperature":{
               "value":"98.1",
               "method":"None",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"145",
               "method":"None",
               "diastolic":"68"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"73",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T08:59:34",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-18T05:59:19.970000",
            "name":"Neck Pain, >24Hrs Old"
         }
      ],
      "discharge":{
         "date":"2013-08-18T00:00:00",
         "edDischargeTime":"2013-08-18T09:54:20",
         "condition":"Improved"
      },
      "diagnoses":[
         {
            "code":"722.4",
            "type":"Cervical Disc Degeneration",
            "description":""
         },
         {
            "code":"847.0",
            "type":"Cervical Sprain",
            "description":""
         },
         {
            "code":"722.6",
            "type":"Degenerative Disc Disease-DJD",
            "description":""
         },
         {
            "code":"719.7",
            "type":"Difficulty Walking",
            "description":""
         },
         {
            "code":"783.7",
            "type":"Adult Failure to Thrive",
            "description":""
         }
      ],
      "visitNumber":"3147132",
      "lastModified":"2013-08-20T03:22:51.080989",
      "creationTime":"2013-08-19T19:39:09.143000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.081374",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.081376",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.081378",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.081380",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.081381",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.081383",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.081385",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.081386",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"86017545243754652",
      "medicationsOrdered":[
         {
            "orderId":"10862718",
            "dosageForm":"SYRG",
            "minAmount":5,
            "orderedTime":"2013-08-18T06:00:00",
            "dispenseAmount":"1",
            "code":"41210204",
            "dispenseUnit":"SYRG",
            "unit":"ML",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/521064919606ff0890ee2d63"
   },
   {
      "patientType":"I1",
      "intakesOutputs":[
         {
            "intakes":[
               {
                  "amount":0.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-18T05:07:00"
         },
         {
            "intakes":[
               {
                  "amount":350.0,
                  "type":"IVPB"
               }
            ],
            "observedTime":"2013-08-18T17:30:00"
         },
         {
            "intakes":[
               {
                  "amount":10.0,
                  "type":"SUPPR"
               }
            ],
            "observedTime":"2013-08-18T17:31:00"
         },
         {
            "outputs":[
               {
                  "amount":350.0,
                  "type":"FOLEY"
               }
            ],
            "observedTime":"2013-08-19T19:57:00"
         },
         {
            "outputs":[
               {
                  "amount":900.0,
                  "type":"FOLEY"
               }
            ],
            "observedTime":"2013-08-19T07:57:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"1360",
            "name":{
               "salutation":"MD",
               "last":"LAGUD",
               "first":"ADINARAYANA"
            }
         },
         {
            "role":"ReferringDoctor",
            "id":"8899",
            "name":{
               "middle":"DOCTOR",
               "last":"NO",
               "first":"REFERRING"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"2960",
            "name":{
               "salutation":"DO",
               "last":"HARBOUR",
               "first":"DAVID"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"unmarried",
         "name":{
            "middle":"R",
            "last":"Patient 11",
            "first":"Test"
         },
         "ssn":"5593816572954667983",
         "id":"521031bd9606ff087e811535",
         "contactDetails":{
            "homePhone":"(109)105-1860",
            "currentAddress":"0206 GHEGYRQBIR CYNPR^^ZRYOBHEAR^SY^107828888^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1939-03-06T00:00:00",
         "mrn":"6468386868979942367",
         "race":"Other",
         "sex":"male",
         "ethinicGroup":"O"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.082207",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.082204",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.082197",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.082216",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.082213",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.082210",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.082209",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"521031bd9606ff088d28a8e2",
      "allergies":[
         {
            "name":"No known drug Allergies"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2012-09-28T00:00:00",
            "name":"NO KNOWN ALLERGIES"
         }
      ],
      "admission":{
         "admissionDate":"2013-08-18T00:00:00",
         "assignedLocation":{
            "bedNo":"1",
            "ward":"PC",
            "roomNo":"3402"
         },
         "admissionType":"1",
         "providers":[
            {
               "role":"AdmittingDoctor",
               "id":"1360",
               "name":{
                  "salutation":"MD",
                  "last":"LAGUD",
                  "first":"ADINARAYANA"
               }
            }
         ]
      },
      "patientId":"521031bd9606ff087e811535",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-18T02:42:31",
         "firstPHCPVisit":"None",
         "registration":"2013-08-18T02:30:38",
         "firstBedAssignment":"2013-08-18T02:23:53",
         "firstAttendVisit":"2013-08-18T02:24:33",
         "lastEDMove":"2013-08-18T02:23:53",
         "radiologyOrder":"2013-08-18T02:36:05",
         "firstFinancialRegistration":"2013-08-18T02:51:37",
         "arrival":"2013-08-18T02:23:53",
         "lastBedAssignment":"2013-08-18T02:23:53",
         "careComplete":"2013-08-18T04:33:22",
         "lastMedicalScreening":"2013-08-18T02:24:33",
         "lastFinancialRegistration":"2013-08-18T02:51:37",
         "encounterLock":"None",
         "labOrderTime":"2013-08-18T02:36:05",
         "triage":"2013-08-18T02:44:06",
         "observation":"None",
         "firstMedicalScreening":"2013-08-18T02:24:33",
         "medicineOrder":"2013-08-18T02:36:05",
         "departure":"2013-08-18T05:50:23",
         "bedRequest":"None",
         "encounterCreation":"2013-08-18T02:22:41"
      },
      "homeMedications":[
         {
            "frequency":"twice a day",
            "medication":"Advair Diskus Inhl",
            "dosage":"1 puff"
         },
         {
            "frequency":"as needed, every 6 hours",
            "medication":"Acetaminophen Oral",
            "dosage":"650 mg"
         },
         {
            "frequency":"daily",
            "medication":"Fluoxetine Oral",
            "dosage":"20 mg"
         },
         {
            "frequency":"twice a day",
            "medication":"Mucinex Oral",
            "dosage":"600 mg"
         },
         {
            "frequency":"daily",
            "medication":"Protonix Oral",
            "dosage":"40 mg"
         },
         {
            "frequency":"daily",
            "medication":"Prednisone Oral",
            "dosage":"40 mg"
         },
         {
            "frequency":"daily",
            "medication":"tiotropium bromide Inhl",
            "dosage":"1 capsule"
         },
         {
            "frequency":"three times a day",
            "medication":"Xanax Oral",
            "dosage":"0.5 mg"
         },
         {
            "frequency":"daily",
            "medication":"Aspirin Oral",
            "dosage":"81 mg"
         },
         {
            "frequency":"nightly",
            "medication":"Lipitor Oral",
            "dosage":"40 mg"
         },
         {
            "frequency":"daily",
            "medication":"cholecalciferol (vitamin D3) SL",
            "dosage":"1000 UNITS"
         },
         {
            "frequency":"daily",
            "medication":"Docusate Sodium Oral",
            "dosage":"100 mg"
         },
         {
            "frequency":"daily",
            "medication":"Azithromycin Oral",
            "dosage":"500 mg"
         }
      ],
      "financialClass":"Z",
      "vipIndicator":"R",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.082164",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.082029",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.082159",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.082168",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.082171",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"96",
               "method":"None",
               "diastolic":"57"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"47.63",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"16.9"
            },
            "pulse":{
               "value":"88",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"168",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T02:54:34",
            "temperature":{
               "value":"98.5",
               "method":"Oral",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"86",
               "method":"None",
               "diastolic":"62"
            },
            "respiration":{
               "value":"16",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"81",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T04:45:00",
            "temperature":{
               "value":"98.5",
               "method":"Oral",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"None",
               "method":"None",
               "diastolic":"None"
            },
            "respiration":{
               "value":"None",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"77",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T04:07:35",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-18T02:23:53.177000",
            "name":"Abdominal Pain"
         }
      ],
      "discharge":{
         "date":"2013-08-18T00:00:00",
         "edDischargeTime":"2013-08-18T05:50:23",
         "condition":"Fair"
      },
      "diagnoses":[
         {
            "priority":"8",
            "code":"2607",
            "type":"N",
            "codingMethod":"V7",
            "description":"ONPGREVNY CARHZBAVN ABF"
         },
         {
            "priority":"9",
            "code":"2607",
            "type":"C",
            "codingMethod":"V7",
            "description":"ONPGREVNY CARHZBAVN ABF"
         },
         {
            "priority":"0",
            "code":"8167",
            "type":"F",
            "codingMethod":"V7",
            "description":"FRCGVPRZVN ABF"
         },
         {
            "priority":"0",
            "code":"77379",
            "type":"F",
            "codingMethod":"V7",
            "description":"FRCFVF"
         },
         {
            "priority":"0",
            "code":"27909",
            "type":"F",
            "codingMethod":"V7",
            "description":"BOF PUE OEBAP J(NP) RKNP"
         },
         {
            "priority":"0",
            "code":"5615",
            "type":"F",
            "codingMethod":"V7",
            "description":"SNVYHER GB GUEVIR-NQHYG"
         }
      ],
      "visitNumber":"3147127",
      "lastModified":"2013-08-20T03:22:51.081687",
      "creationTime":"2013-08-20T00:05:50.641000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.082177",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.082181",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.082185",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.082186",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.082188",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.082190",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.082192",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.082194",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"6468386868979942367",
      "medicationsOrdered":[
         {
            "orderId":"10863754",
            "dosageForm":"TAB",
            "minAmount":1,
            "orderedTime":"2013-08-19T12:51:00",
            "dispenseAmount":"1",
            "code":"41221510",
            "unit":"MG",
            "dispenseUnit":"TAB",
            "providerInstruction":"^_SEDATIVE (ANXIETY, INSOMNIA,  SEDATION, SEIZURES, DRUG WITHDRAWAL) COMMON SIDE EFFECTS: DROWSINESS,  FATIGUE, FALL RISK, DROWSINESS,  IMPAIRED COGNITION, SLURRED SPEECH_",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/521031bd9606ff088d28a8e2"
   },
   {
      "patientType":"I1",
      "intakesOutputs":[
         {
            "outputs":[
               {
                  "amount":600.0,
                  "type":"VOID"
               }
            ],
            "observedTime":"2013-08-19T06:00:00"
         },
         {
            "intakes":[
               {
                  "amount":1800.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-18T17:57:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"1757",
            "name":{
               "salutation":"MD",
               "last":"NALIPIREDDY",
               "first":"VASUDEVA"
            }
         },
         {
            "role":"AttendingDoctor",
            "id":"0152",
            "name":{
               "salutation":"MD",
               "last":"AZIZ",
               "first":"NABIL"
            }
         },
         {
            "role":"ReferringDoctor",
            "id":"8899",
            "name":{
               "middle":"DOCTOR",
               "last":"NO",
               "first":"REFERRING"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"0424",
            "name":{
               "salutation":"MD",
               "last":"CATENA",
               "first":"WILLIAM"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"1451",
            "name":{
               "salutation":"MD",
               "last":"LOPEZ",
               "first":"RAPHEL"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"2960",
            "name":{
               "salutation":"DO",
               "last":"HARBOUR",
               "first":"DAVID"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"unmarried",
         "name":{
            "middle":"N",
            "last":"Patient 12",
            "first":"Test"
         },
         "ssn":"6881109113969007163",
         "id":"52052e1152ce5f5b949318e2",
         "contactDetails":{
            "homePhone":"(564)064-1331",
            "currentAddress":"9797 SNOVRA PVE^^ZRYOBHEAR^SY^107288888^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1972-03-27T00:00:00",
         "mrn":"7702028039215406625",
         "race":"Other",
         "sex":"female",
         "ethinicGroup":"O"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.082833",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.082830",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.082823",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.082842",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.082839",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.082836",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.082835",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"52108aec9606ff087e811847",
      "allergies":[
         {
            "name":"mango topically"
         },
         {
            "severityLevel":"other",
            "reaction":"UN^",
            "identificationDate":"2013-08-18T00:00:00",
            "name":"NO ALLERGY INFO",
            "type":"drug"
         },
         {
            "severityLevel":"other",
            "type":"food",
            "identificationDate":"2013-08-18T00:00:00",
            "name":"MANGO"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-18T00:00:00",
            "name":"BUTORPHANOL"
         },
         {
            "name":"Stadol"
         }
      ],
      "admission":{
         "dischargeDate":"2013-08-19T00:00:00",
         "admissionType":"1",
         "providers":[
            {
               "role":"AdmittingDoctor",
               "id":"1757",
               "name":{
                  "salutation":"MD",
                  "last":"NALIPIREDDY",
                  "first":"VASUDEVA"
               }
            }
         ],
         "assignedLocation":{
            "ward":"ED"
         },
         "admitReason":"URINARY PROBLEM",
         "admissionDate":"2013-08-18T00:00:00"
      },
      "patientId":"52052e1152ce5f5b949318e2",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-18T09:02:38",
         "firstPHCPVisit":"None",
         "registration":"2013-08-18T08:51:47",
         "firstBedAssignment":"2013-08-18T08:56:13",
         "firstAttendVisit":"2013-08-18T09:02:23",
         "lastEDMove":"2013-08-18T09:22:23",
         "radiologyOrder":"2013-08-18T09:29:05",
         "firstFinancialRegistration":"2013-08-18T09:09:32",
         "arrival":"2013-08-18T08:50:00",
         "lastBedAssignment":"2013-08-18T09:22:23",
         "careComplete":"2013-08-18T10:35:55",
         "lastMedicalScreening":"2013-08-18T09:02:23",
         "lastFinancialRegistration":"2013-08-18T09:09:32",
         "encounterLock":"None",
         "labOrderTime":"2013-08-18T09:29:05",
         "triage":"2013-08-18T09:06:36",
         "observation":"None",
         "firstMedicalScreening":"2013-08-18T09:02:23",
         "medicineOrder":"2013-08-18T09:29:05",
         "departure":"2013-08-18T12:02:57",
         "bedRequest":"None",
         "encounterCreation":"2013-08-18T08:51:46"
      },
      "homeMedications":[
         {
            "frequency":"daily",
            "medication":"Singulair Oral",
            "dosage":"10 mg"
         },
         {
            "frequency":"nightly",
            "medication":"Cymbalta Oral",
            "dosage":"30 mg"
         },
         {
            "frequency":"daily, as needed",
            "medication":"Lorazepam Oral",
            "dosage":"0.5 mg"
         },
         {
            "frequency":"as needed, every 6 hours",
            "medication":"Lortab Oral",
            "dosage":"5/325 mg"
         },
         {
            "frequency":"daily",
            "medication":"Bactrim DS Oral",
            "dosage":"160-800 mg"
         },
         {
            "frequency":"None",
            "medication":"Macrobid Oral",
            "dosage":"Unknown"
         }
      ],
      "financialClass":"Q",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.082802",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.082795",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.082800",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.082803",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.082804",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"134",
               "method":"None",
               "diastolic":"80"
            },
            "respiration":{
               "value":"16",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"70",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T10:39:43",
            "temperature":{
               "value":"98.7",
               "method":"Oral",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"141",
               "method":"None",
               "diastolic":"71"
            },
            "respiration":{
               "value":"16",
               "unit":"bpm"
            },
            "weight":{
               "value":"72.57",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"27.5"
            },
            "pulse":{
               "value":"82",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"163",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T09:12:28",
            "temperature":{
               "value":"98.9",
               "method":"None",
               "unit":"F"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-18T08:51:58.350000",
            "name":"Urinary Problem"
         }
      ],
      "discharge":{
         "date":"2013-08-19T00:00:00",
         "edDischargeTime":"2013-08-18T12:02:57",
         "condition":"Improved"
      },
      "diagnoses":[
         {
            "priority":"8",
            "code":"3778",
            "type":"N",
            "codingMethod":"V7",
            "description":"HEVA GENPG VASRPGVBA ABF"
         },
         {
            "priority":"9",
            "code":"3778",
            "type":"C",
            "codingMethod":"V7",
            "description":"HEVA GENPG VASRPGVBA ABF"
         },
         {
            "priority":"0",
            "code":"4037",
            "type":"F",
            "codingMethod":"V7",
            "description":"SRZ TRAVGNY FLZCGBZF ABF"
         },
         {
            "priority":"0",
            "code":"I8779",
            "type":"F",
            "codingMethod":"V7",
            "description":"ZVPEB VASRP ABF J ERFVF"
         }
      ],
      "visitNumber":"3147135",
      "lastModified":"2013-08-20T03:22:51.082436",
      "creationTime":"2013-08-19T17:54:01.978000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.082807",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.082809",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.082811",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.082813",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.082814",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.082816",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.082818",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.082820",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"7702028039215406625",
      "medicationsOrdered":[
         {
            "orderId":"10862896",
            "dosageForm":"TAB",
            "minAmount":10,
            "orderedTime":"2013-08-18T22:00:00",
            "dispenseAmount":"1",
            "code":"41238676",
            "dispenseUnit":"TAB",
            "unit":"MG",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/52108aec9606ff087e811847"
   },
   {
      "patientType":"O5",
      "intakesOutputs":[
         {
            "intakes":[
               {
                  "amount":240.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-18T06:00:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"1360",
            "name":{
               "salutation":"MD",
               "last":"LAGUD",
               "first":"ADINARAYANA"
            }
         },
         {
            "role":"AttendingDoctor",
            "id":"3750",
            "name":{
               "salutation":"MD",
               "last":"ONEILL-ROSADO",
               "first":"OSCAR"
            }
         },
         {
            "role":"ReferringDoctor",
            "id":"1360",
            "name":{
               "salutation":"MD",
               "last":"LAGUD",
               "first":"ADINARAYANA"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"0135",
            "name":{
               "salutation":"MD",
               "last":"ASLAM",
               "first":"MUHAMMAD"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"3548",
            "name":{
               "salutation":"MD",
               "last":"GOODMAN",
               "first":"GARY"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"unmarried",
         "name":{
            "last":"Patient 13",
            "first":"Test"
         },
         "ssn":"8507031265628369092",
         "id":"520fa7f89606ff088f5a5edc",
         "contactDetails":{
            "homePhone":"(212)324-0818",
            "currentAddress":"9929 GUVFGYR QBJA EBNQ^^ZRYOBHEAR^SY^10789^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1948-07-01T00:00:00",
         "mrn":"8201314135885238387",
         "race":"Caucasian",
         "sex":"female",
         "ethinicGroup":"O"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.083464",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.083460",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.083454",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.083472",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.083470",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.083467",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.083465",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"520fa7f89606ff0889e59706",
      "allergies":[
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"XOPENEX"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"DAIRY EASE"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"PREDNISONE"
         },
         {
            "name":"most antibiotics"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"SULFA(SULFONAMIDE ANTIBIOTICS)"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"LATEX, NATURAL RUBBER"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"EGG/POULTRY"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"PENICILLIN G"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"SULFITE"
         }
      ],
      "admission":{
         "dischargeDate":"2013-08-18T00:00:00",
         "admissionType":"1",
         "providers":[
            {
               "role":"AdmittingDoctor",
               "id":"1360",
               "name":{
                  "salutation":"MD",
                  "last":"LAGUD",
                  "first":"ADINARAYANA"
               }
            }
         ],
         "assignedLocation":{
            "ward":"ED"
         },
         "admitReason":"WEAKNESS",
         "dischargeDisposition":"01",
         "admissionDate":"2013-08-17T00:00:00"
      },
      "patientId":"520fa7f89606ff088f5a5edc",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"None",
         "firstPHCPVisit":"None",
         "registration":"2013-08-17T16:42:38",
         "firstBedAssignment":"2013-08-17T16:34:47",
         "firstAttendVisit":"None",
         "lastEDMove":"2013-08-17T16:34:47",
         "radiologyOrder":"2013-08-17T16:48:10",
         "firstFinancialRegistration":"2013-08-17T17:05:05",
         "arrival":"2013-08-17T16:34:47",
         "lastBedAssignment":"2013-08-17T16:34:47",
         "careComplete":"2013-08-17T17:27:32",
         "lastMedicalScreening":"2013-08-17T16:38:31",
         "lastFinancialRegistration":"2013-08-17T17:05:05",
         "encounterLock":"None",
         "labOrderTime":"2013-08-17T16:48:10",
         "triage":"2013-08-17T16:43:57",
         "observation":"None",
         "firstMedicalScreening":"2013-08-17T16:38:31",
         "medicineOrder":"2013-08-17T16:48:26",
         "departure":"2013-08-17T19:12:29",
         "bedRequest":"None",
         "encounterCreation":"2013-08-17T16:32:55"
      },
      "homeMedications":[
         {
            "frequency":"daily",
            "medication":"Atenolol Oral",
            "dosage":"25 mg"
         },
         {
            "frequency":"twice a day",
            "medication":"Advair Diskus Inhl",
            "dosage":"250-50 mcg/Dose"
         },
         {
            "frequency":"as needed, every 4 hours",
            "medication":"Atrovent Nebulizer",
            "dosage":"2 puffs"
         }
      ],
      "financialClass":"R",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.083433",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.083427",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.083432",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.083435",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.083436",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"121",
               "method":"None",
               "diastolic":"52"
            },
            "respiration":{
               "value":"14",
               "unit":"bpm"
            },
            "weight":{
               "value":"52.62",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"21.2"
            },
            "pulse":{
               "value":"68",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"157",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T16:48:57",
            "temperature":{
               "value":"99",
               "method":"None",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"117",
               "method":"None",
               "diastolic":"45"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"75",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T18:48:29",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"119",
               "method":"None",
               "diastolic":"60"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"60",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T17:32:04",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-17T16:34:47.523000",
            "name":"Weakness"
         }
      ],
      "discharge":{
         "date":"2013-08-18T00:00:00",
         "edDischargeTime":"2013-08-17T19:12:29",
         "disposition":"01",
         "condition":"Stable"
      },
      "diagnoses":[
         {
            "code":"786.50",
            "type":"Chest Pain",
            "description":""
         },
         {
            "code":"411.1",
            "type":"Intermediate Coronary Syndrome",
            "description":""
         }
      ],
      "visitNumber":"3147108",
      "lastModified":"2013-08-20T03:22:51.083053",
      "creationTime":"2013-08-19T12:30:37.103000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.083439",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.083441",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.083443",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.083445",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.083446",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.083448",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.083450",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.083451",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"8201314135885238387",
      "medicationsOrdered":[
         {
            "orderId":"10862455",
            "dosageForm":"HFAA",
            "minAmount":1,
            "orderedTime":"2013-08-17T21:23:00",
            "dispenseAmount":"2",
            "code":"45410076",
            "unit":"PUFF",
            "dispenseUnit":"HFAA",
            "providerInstruction":"^FOR SHORTNESS OF BREATH.  _ANTICHOLINERGIC (COPD, ASTHMA,  GASTRIC SPASM) COMMON SIDE EFFECTS: BLURRED VISION,  URINARY RETENTION, DRY MOUTH, CONSTIPATION, NAUSEA/VOMITING,  DIZZINESS_",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/520fa7f89606ff0889e59706"
   },
   {
      "patientType":"O5",
      "intakesOutputs":[
         {
            "intakes":[
               {
                  "amount":0.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-18T05:15:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"1360",
            "name":{
               "salutation":"MD",
               "last":"LAGUD",
               "first":"ADINARAYANA"
            }
         },
         {
            "role":"ReferringDoctor",
            "id":"1360",
            "name":{
               "salutation":"MD",
               "last":"LAGUD",
               "first":"ADINARAYANA"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"0210",
            "name":{
               "salutation":"MD",
               "middle":"CHAPMAN",
               "last":"BEAN",
               "first":"L"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"3548",
            "name":{
               "salutation":"MD",
               "last":"GOODMAN",
               "first":"GARY"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"unmarried",
         "name":{
            "last":"Patient 14",
            "first":"Test"
         },
         "ssn":"1006750455958886482",
         "religion":"NP",
         "id":"520fc6bb9606ff0886a6e2dc",
         "contactDetails":{
            "homePhone":"(109)471-0739",
            "currentAddress":"1233 FCEVAT ONEAPU 931^^ZRYOBHEAR^SY^107138888^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1993-02-12T00:00:00",
         "mrn":"3251029079434470886",
         "race":"Black",
         "sex":"male",
         "ethinicGroup":"C"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.084148",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.084142",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.084132",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.084166",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.084160",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.084154",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.084152",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"520fc6bb9606ff088a65e0f5",
      "allergies":[
         {
            "name":"No known drug Allergies"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"NO KNOWN ALLERGIES"
         }
      ],
      "admission":{
         "dischargeDate":"2013-08-18T00:00:00",
         "admissionType":"1",
         "providers":[
            {
               "role":"AdmittingDoctor",
               "id":"1360",
               "name":{
                  "salutation":"MD",
                  "last":"LAGUD",
                  "first":"ADINARAYANA"
               }
            }
         ],
         "assignedLocation":{
            "ward":"ED"
         },
         "admitReason":"CHEST PAIN",
         "dischargeDisposition":"01",
         "admissionDate":"2013-08-17T00:00:00"
      },
      "patientId":"520fc6bb9606ff0886a6e2dc",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-17T19:49:06",
         "firstPHCPVisit":"None",
         "registration":"2013-08-17T18:53:53",
         "firstBedAssignment":"2013-08-17T18:50:10",
         "firstAttendVisit":"None",
         "lastEDMove":"2013-08-17T18:50:10",
         "radiologyOrder":"2013-08-17T19:19:01",
         "firstFinancialRegistration":"2013-08-17T19:20:50",
         "arrival":"2013-08-17T18:50:10",
         "lastBedAssignment":"2013-08-17T18:50:10",
         "careComplete":"2013-08-17T20:19:16",
         "lastMedicalScreening":"2013-08-17T19:16:38",
         "lastFinancialRegistration":"2013-08-17T19:20:50",
         "encounterLock":"None",
         "labOrderTime":"2013-08-17T19:18:41",
         "triage":"2013-08-17T18:56:36",
         "observation":"None",
         "firstMedicalScreening":"2013-08-17T19:16:38",
         "medicineOrder":"2013-08-17T19:22:12",
         "departure":"2013-08-17T22:00:54",
         "bedRequest":"None",
         "encounterCreation":"2013-08-17T18:48:57"
      },
      "homeMedications":[
         {
            "frequency":"None",
            "medication":"None",
            "dosage":"None"
         }
      ],
      "financialClass":"O",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.084099",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.084093",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.084098",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.084101",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.084103",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"158",
               "method":"None",
               "diastolic":"69"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"63",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T21:40:37",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"None",
               "method":"None",
               "diastolic":"None"
            },
            "respiration":{
               "value":"None",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"None",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T21:42:52",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"159",
               "method":"None",
               "diastolic":"74"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"129.27",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"38.7"
            },
            "pulse":{
               "value":"75",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"183",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T18:58:19",
            "temperature":{
               "value":"98.0",
               "method":"Temporal",
               "unit":"F"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-17T21:38:14.780000",
            "name":"Chest Pain"
         }
      ],
      "discharge":{
         "date":"2013-08-18T00:00:00",
         "edDischargeTime":"2013-08-17T22:00:54",
         "disposition":"01",
         "condition":"Stable"
      },
      "diagnoses":[
         {
            "code":"786.59",
            "type":"Atypical Chest Pain",
            "description":""
         },
         {
            "code":"794.31",
            "type":"Abnormal ECG",
            "description":""
         }
      ],
      "visitNumber":"3147113",
      "lastModified":"2013-08-20T03:22:51.083739",
      "creationTime":"2013-08-19T13:15:17.140000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.084106",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.084110",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.084114",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.084117",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.084121",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.084124",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.084126",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.084127",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"3251029079434470886",
      "medicationsOrdered":[
         {
            "orderId":"10862369",
            "dosageForm":"SOLN",
            "minAmount":5,
            "orderedTime":"2013-08-17T17:48:00",
            "dispenseAmount":"1",
            "code":"41246680",
            "unit":"MG",
            "dispenseUnit":"SOLN",
            "providerInstruction":"^PAIN SCALE 6-10.",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/520fc6bb9606ff088a65e0f5"
   },
   {
      "patientType":"I1",
      "intakesOutputs":[
         {
            "outputs":[
               {
                  "amount":800.0,
                  "type":"VOID"
               }
            ],
            "observedTime":"2013-08-18T18:00:00"
         },
         {
            "intakes":[
               {
                  "amount":50.0,
                  "type":"LUNCH"
               }
            ],
            "observedTime":"2013-08-19T18:31:00"
         },
         {
            "outputs":[
               {
                  "amount":1500.0,
                  "type":"VOID"
               }
            ],
            "observedTime":"2013-08-19T07:16:00"
         },
         {
            "outputs":[
               {
                  "amount":400.0,
                  "type":"VOID"
               }
            ],
            "observedTime":"2013-08-18T07:39:00"
         },
         {
            "intakes":[
               {
                  "amount":100.0,
                  "type":"BKFST"
               }
            ],
            "observedTime":"2013-08-19T08:59:00"
         },
         {
            "outputs":[
               {
                  "amount":600.0,
                  "type":"VOID"
               }
            ],
            "observedTime":"2013-08-18T05:45:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"1348",
            "name":{
               "salutation":"MD",
               "last":"KUMAR",
               "first":"NAVEEN"
            }
         },
         {
            "role":"AttendingDoctor",
            "id":"2524",
            "name":{
               "salutation":"DO",
               "last":"TARASCHI",
               "first":"PETER"
            }
         },
         {
            "role":"ReferringDoctor",
            "id":"1348",
            "name":{
               "salutation":"MD",
               "last":"KUMAR",
               "first":"NAVEEN"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"3548",
            "name":{
               "salutation":"MD",
               "last":"GOODMAN",
               "first":"GARY"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"unmarried",
         "name":{
            "middle":"R",
            "last":"Patient 15",
            "first":"Test"
         },
         "ssn":"776632643284610425",
         "religion":"NP",
         "id":"52018a837103425d497300b6",
         "contactDetails":{
            "homePhone":"(109)020-7514",
            "currentAddress":"9033 EBYYVAT EBPX QEVIR^^ZRYOBHEAR^SY^107128888^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1932-02-13T00:00:00",
         "mrn":"4914511469397018757",
         "race":"Caucasian",
         "sex":"male",
         "ethinicGroup":"O"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.084777",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.084774",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.084768",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.084786",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.084784",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.084780",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.084779",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"520fb12257fa8368940097c3",
      "allergies":[
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-06T00:00:00",
            "name":"CIPROFLOXACIN"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-06T00:00:00",
            "name":"COMPAZINE"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-06T00:00:00",
            "name":"MORPHINE"
         }
      ],
      "admission":{
         "admissionDate":"2013-08-17T00:00:00",
         "assignedLocation":{
            "bedNo":"1",
            "ward":"PC",
            "roomNo":"3101"
         },
         "admissionType":"1",
         "providers":[
            {
               "role":"AdmittingDoctor",
               "id":"1348",
               "name":{
                  "salutation":"MD",
                  "last":"KUMAR",
                  "first":"NAVEEN"
               }
            }
         ]
      },
      "patientId":"52018a837103425d497300b6",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-17T17:36:14",
         "firstPHCPVisit":"2013-08-17T17:24:15",
         "registration":"2013-08-17T17:23:01",
         "firstBedAssignment":"2013-08-17T17:23:44",
         "firstAttendVisit":"None",
         "lastEDMove":"2013-08-17T17:23:44",
         "radiologyOrder":"2013-08-17T17:32:04",
         "firstFinancialRegistration":"2013-08-17T19:20:47",
         "arrival":"2013-08-17T17:21:00",
         "lastBedAssignment":"2013-08-17T17:23:44",
         "careComplete":"2013-08-17T18:45:41",
         "lastMedicalScreening":"2013-08-17T17:24:15",
         "lastFinancialRegistration":"2013-08-17T19:20:47",
         "encounterLock":"None",
         "labOrderTime":"2013-08-17T17:32:04",
         "triage":"2013-08-17T17:32:25",
         "observation":"None",
         "firstMedicalScreening":"2013-08-17T17:24:15",
         "medicineOrder":"2013-08-17T17:32:04",
         "departure":"2013-08-17T20:32:01",
         "bedRequest":"None",
         "encounterCreation":"2013-08-17T17:22:59"
      },
      "homeMedications":[
         {
            "frequency":"as needed, three times a day",
            "medication":"Bentyl Oral",
            "dosage":"20 mg"
         },
         {
            "frequency":"as needed, every 4 hours",
            "medication":"Tramadol Oral",
            "dosage":"100 mg"
         },
         {
            "frequency":"daily",
            "medication":"Plavix Oral",
            "dosage":"75 mg"
         },
         {
            "frequency":"nightly",
            "medication":"pravastatin Oral",
            "dosage":"40 mg"
         },
         {
            "frequency":"daily",
            "medication":"Aspirin Oral",
            "dosage":"81 mg"
         },
         {
            "frequency":"as needed, nightly",
            "medication":"Ambien Oral",
            "dosage":"2.5mg"
         }
      ],
      "financialClass":"R",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.084745",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.084739",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.084743",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.084747",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.084748",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"L Arm",
               "orthostatic":"Supine",
               "systolic":"128",
               "method":"Auto",
               "diastolic":"68"
            },
            "respiration":{
               "value":"None",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"20.3"
            },
            "pulse":{
               "value":"74",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T18:17:24",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"L Arm",
               "orthostatic":"Standing",
               "systolic":"96",
               "method":"Auto",
               "diastolic":"52"
            },
            "respiration":{
               "value":"None",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"77",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T18:17:00",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"120",
               "method":"None",
               "diastolic":"71"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"68.04",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"20.3"
            },
            "pulse":{
               "value":"85",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"183",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T17:35:01",
            "temperature":{
               "value":"97.2",
               "method":"Temporal",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"140",
               "method":"None",
               "diastolic":"73"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"66",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T19:41:36",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-17T17:23:20.910000",
            "name":"Syncope"
         }
      ],
      "discharge":{
         "date":"2013-08-17T00:00:00",
         "edDischargeTime":"2013-08-17T20:32:01",
         "condition":"Good"
      },
      "diagnoses":[
         {
            "priority":"8",
            "code":"5680",
            "type":"N",
            "codingMethod":"V7",
            "description":"FLAPBCR NAQ PBYYNCFR"
         },
         {
            "priority":"9",
            "code":"5680",
            "type":"C",
            "codingMethod":"V7",
            "description":"FLAPBCR NAQ PBYYNCFR"
         },
         {
            "priority":"0",
            "code":"1159",
            "type":"F",
            "codingMethod":"V7",
            "description":"NHG ARHEBCGUL VA BGU QVF"
         },
         {
            "priority":"0",
            "code":"0637",
            "type":"F",
            "codingMethod":"V7",
            "description":"NARZVN ABF"
         },
         {
            "priority":"0",
            "code":"5615",
            "type":"F",
            "codingMethod":"V7",
            "description":"SNVYHER GB GUEVIR-NQHYG"
         },
         {
            "priority":"0",
            "code":"5975",
            "type":"F",
            "codingMethod":"V7",
            "description":"QVSSVPHYGL VA JNYXVAT"
         }
      ],
      "visitNumber":"3147109",
      "lastModified":"2013-08-20T03:22:51.084390",
      "creationTime":"2013-08-19T19:27:43.261000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.084751",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.084753",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.084755",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.084756",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.084759",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.084761",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.084762",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.084763",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"4914511469397018757",
      "medicationsOrdered":[
         {
            "orderId":"10862604",
            "dosageForm":"TAB",
            "minAmount":20,
            "orderedTime":"2013-08-18T00:00:00",
            "dispenseAmount":"1",
            "code":"41241261",
            "unit":"MG",
            "dispenseUnit":"TAB",
            "providerInstruction":"^AUTO-SUBSTITUTION FOR PRAVASTATIN 40 MG. STATIN (LOWERS  CHOLESTEROL/TRIGLYCERIDES) COMMON SIDE EFFECTS: HEADACHE, UPSET  STOMACH, MUSCLE CRAMPS/PAIN,  CONSTIPATION_",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/520fb12257fa8368940097c3"
   },
   {
      "patientType":"I1",
      "intakesOutputs":[
         {
            "intakes":[
               {
                  "amount":50.0,
                  "type":"SUPPR"
               }
            ],
            "observedTime":"2013-08-18T18:00:00"
         },
         {
            "intakes":[
               {
                  "amount":80.0,
                  "type":"SUPPR"
               }
            ],
            "observedTime":"2013-08-19T18:26:00"
         },
         {
            "intakes":[
               {
                  "amount":50.0,
                  "type":"BKFST"
               }
            ],
            "observedTime":"2013-08-19T08:21:00"
         },
         {
            "intakes":[
               {
                  "amount":320.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-19T07:26:00"
         },
         {
            "intakes":[
               {
                  "amount":50.0,
                  "type":"LUNCH"
               }
            ],
            "observedTime":"2013-08-19T12:59:00"
         },
         {
            "intakes":[
               {
                  "amount":240.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-18T06:00:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"0687",
            "name":{
               "salutation":"MD",
               "last":"DONTINENI",
               "first":"SRINIVAS"
            }
         },
         {
            "role":"AttendingDoctor",
            "id":"2227",
            "name":{
               "salutation":"MD",
               "last":"SAHAY",
               "first":"SANGITA"
            }
         },
         {
            "role":"ReferringDoctor",
            "id":"0687",
            "name":{
               "salutation":"MD",
               "last":"DONTINENI",
               "first":"SRINIVAS"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"0210",
            "name":{
               "salutation":"MD",
               "middle":"CHAPMAN",
               "last":"BEAN",
               "first":"L"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"2245",
            "name":{
               "salutation":"MD",
               "last":"SANABRIA",
               "first":"GUILLERMO"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"3548",
            "name":{
               "salutation":"MD",
               "last":"GOODMAN",
               "first":"GARY"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"divorced",
         "name":{
            "middle":"S",
            "last":"Patient 16",
            "first":"Test"
         },
         "ssn":"4030389439533362792",
         "religion":"NP",
         "id":"52054fa852ce5f5b85a04177",
         "contactDetails":{
            "homePhone":"(109)020-3710",
            "currentAddress":"2959 FCNEEBJ UNJX EBNQ^^ZRYOBHEAR^SY^10712^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1928-08-09T00:00:00",
         "mrn":"7481156590283442879",
         "race":"Caucasian",
         "sex":"female",
         "ethinicGroup":"O"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.085391",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.085388",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.085382",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.085400",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.085397",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.085394",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.085393",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"520fe10157fa83689776652c",
      "allergies":[
         {
            "severityLevel":"other",
            "reaction":"UN^",
            "identificationDate":"2011-09-26T00:00:00",
            "name":"PENICILLIN CLASS ALLERGY",
            "type":"drug"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2011-11-11T00:00:00",
            "name":"SULFONYLUREA ALLERGY"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2011-11-11T00:00:00",
            "name":"CODEINE"
         },
         {
            "severityLevel":"other",
            "reaction":"UN^",
            "identificationDate":"2011-09-26T00:00:00",
            "name":"SULFA(SULFONAMIDE ANTIBIOTICS)",
            "type":"drug"
         },
         {
            "name":"SULFA (SULFONAMIDES)"
         },
         {
            "name":"PENICILLINS"
         }
      ],
      "admission":{
         "admissionDate":"2013-08-17T00:00:00",
         "assignedLocation":{
            "bedNo":"1",
            "ward":"PC",
            "roomNo":"3117"
         },
         "admissionType":"1",
         "providers":[
            {
               "role":"AdmittingDoctor",
               "id":"0687",
               "name":{
                  "salutation":"MD",
                  "last":"DONTINENI",
                  "first":"SRINIVAS"
               }
            }
         ]
      },
      "patientId":"52054fa852ce5f5b85a04177",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-17T23:59:09",
         "firstPHCPVisit":"None",
         "registration":"2013-08-17T20:45:43",
         "firstBedAssignment":"2013-08-17T20:43:57",
         "firstAttendVisit":"2013-08-17T20:57:52",
         "lastEDMove":"2013-08-17T20:43:57",
         "radiologyOrder":"2013-08-17T20:59:51",
         "firstFinancialRegistration":"2013-08-17T21:09:32",
         "arrival":"2013-08-17T20:43:57",
         "lastBedAssignment":"2013-08-17T20:43:57",
         "careComplete":"2013-08-17T23:10:21",
         "lastMedicalScreening":"2013-08-17T20:57:52",
         "lastFinancialRegistration":"2013-08-17T21:09:32",
         "encounterLock":"None",
         "labOrderTime":"2013-08-17T21:01:03",
         "triage":"2013-08-17T20:55:23",
         "observation":"None",
         "firstMedicalScreening":"2013-08-17T20:57:52",
         "medicineOrder":"2013-08-17T20:59:51",
         "departure":"2013-08-18T00:33:56",
         "bedRequest":"None",
         "encounterCreation":"2013-08-17T20:42:49"
      },
      "homeMedications":[
         {
            "frequency":"daily",
            "medication":"Norvasc Oral",
            "dosage":"5 mg"
         },
         {
            "frequency":"twice a day",
            "medication":"Metoprolol Tartrate Oral",
            "dosage":"50 mg"
         },
         {
            "frequency":"every 6 hours",
            "medication":"Xopenex Nebulizer",
            "dosage":"0.63 mg"
         },
         {
            "frequency":"daily",
            "medication":"Seroquel Oral",
            "dosage":"150mg"
         },
         {
            "frequency":"daily",
            "medication":"Namenda Oral",
            "dosage":"5 mg"
         },
         {
            "frequency":"daily",
            "medication":"Aspirin Oral",
            "dosage":"325 mg"
         },
         {
            "frequency":"daily",
            "medication":"Diovan Oral",
            "dosage":"160 mg"
         },
         {
            "frequency":"None",
            "medication":"Exelon Oral",
            "dosage":"9.5mg/24 hour transdermal patch "
         },
         {
            "frequency":"daily",
            "medication":"Lasix Oral",
            "dosage":"20 mg"
         },
         {
            "frequency":"as needed, every 6 hours",
            "medication":"Zofran Oral",
            "dosage":"4mg"
         },
         {
            "frequency":"daily",
            "medication":"Plavix Oral",
            "dosage":"75 mg"
         },
         {
            "frequency":"daily",
            "medication":"Zantac Oral",
            "dosage":"150 mg"
         },
         {
            "frequency":"daily hold if SBP < 100",
            "medication":"Zestoretic Oral",
            "dosage":"20mg-25mg"
         }
      ],
      "financialClass":"Z",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.085360",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.085354",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.085359",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.085362",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.085363",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"154",
               "method":"None",
               "diastolic":"49"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"64",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T22:25:31",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"163",
               "method":"None",
               "diastolic":"61"
            },
            "respiration":{
               "value":"24",
               "unit":"bpm"
            },
            "weight":{
               "value":"52.16",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"19.7"
            },
            "pulse":{
               "value":"61",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"163",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T20:57:58",
            "temperature":{
               "value":"95.6",
               "method":"None",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"163",
               "method":"None",
               "diastolic":"55"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"57",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T00:15:53",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-17T20:43:57.867000",
            "name":"Fall Injury"
         },
         {
            "complaintTime":"2013-08-17T20:43:57.887000",
            "name":"Chest Wall Pain"
         }
      ],
      "discharge":{
         "date":"2013-08-17T00:00:00",
         "edDischargeTime":"2013-08-18T00:33:56",
         "condition":"Stable"
      },
      "diagnoses":[
         {
            "priority":"8",
            "code":"68581",
            "type":"N",
            "codingMethod":"V7",
            "description":"SENPGHER GUERR EVOF-PYBF"
         },
         {
            "priority":"9",
            "code":"68581",
            "type":"C",
            "codingMethod":"V7",
            "description":"SENPGHER GUERR EVOF-PYBF"
         },
         {
            "priority":"0",
            "code":"2607",
            "type":"F",
            "codingMethod":"V7",
            "description":"ONPGREVNY CARHZBAVN ABF"
         },
         {
            "priority":"0",
            "code":"6850",
            "type":"F",
            "codingMethod":"V7",
            "description":"SENPGHER BS FGREAHZ-PYBF"
         },
         {
            "priority":"0",
            "code":"274",
            "type":"F",
            "codingMethod":"V7",
            "description":"PUE NVEJNL BOFGEHPG ARP"
         },
         {
            "priority":"0",
            "code":"3631",
            "type":"F",
            "codingMethod":"V7",
            "description":"PUE XVQARL QVF FGNTR VVV"
         },
         {
            "priority":"0",
            "code":"2029",
            "type":"F",
            "codingMethod":"V7",
            "description":"NBEGVP INYIR QVFBEQRE"
         },
         {
            "priority":"0",
            "code":"R6667",
            "type":"F",
            "codingMethod":"V7",
            "description":"HAFCRPVSVRQ SNYY"
         },
         {
            "priority":"0",
            "code":"28178",
            "type":"F",
            "codingMethod":"V7",
            "description":"UL XVQ ABF J PE XVQ V-VI"
         },
         {
            "priority":"0",
            "code":"20567",
            "type":"F",
            "codingMethod":"V7",
            "description":"PNEQVNP QLFEULGUZVNF ARP"
         }
      ],
      "visitNumber":"3147119",
      "lastModified":"2013-08-20T03:22:51.084998",
      "creationTime":"2013-08-19T22:20:46.522000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.085366",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.085368",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.085371",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.085372",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.085374",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.085376",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.085378",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.085379",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"7481156590283442879",
      "medicationsOrdered":[
         {
            "orderId":"10864124",
            "dosageForm":"MISC",
            "minAmount":1,
            "orderedTime":"2013-08-19T19:00:00",
            "dispenseAmount":"1",
            "code":"00000212",
            "dispenseUnit":"MISC",
            "unit":"EA",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/520fe10157fa83689776652c"
   },
   {
      "patientType":"I",
      "intakesOutputs":[
         {
            "outputs":[
               {
                  "amount":600.0,
                  "type":"VOID"
               }
            ],
            "observedTime":"2013-08-18T05:24:00"
         },
         {
            "intakes":[
               {
                  "amount":100.0,
                  "type":"BKFST"
               }
            ],
            "observedTime":"2013-08-18T08:23:00"
         },
         {
            "outputs":[
               {
                  "amount":2.0,
                  "type":"STOOL"
               }
            ],
            "observedTime":"2013-08-19T07:51:00"
         },
         {
            "intakes":[
               {
                  "amount":120.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-17T07:54:00"
         },
         {
            "intakes":[
               {
                  "amount":275.0,
                  "type":"IV"
               }
            ],
            "observedTime":"2013-08-18T17:30:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"8690687",
            "name":{
               "last":"DONTINENI",
               "first":"SRINIVAS"
            }
         },
         {
            "role":"ReferringDoctor",
            "id":"8690687",
            "name":{
               "last":"DONTINENI",
               "first":"SRINIVAS"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"widow",
         "name":{
            "middle":"Y",
            "last":"Patient 17",
            "first":"Test"
         },
         "ssn":"6934587726558018553",
         "religion":"ME",
         "sex":"female",
         "contactDetails":{
            "homePhone":"(109)539-7398",
            "currentAddress":"2212 GJVA YNXRF QE^^ZRYOBHEAR^SY^10712^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1939-02-06T00:00:00",
         "mrn":"8115366209594917246",
         "race":"Caucasian",
         "id":"520ed2df57fa836891d232ad"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.217087",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.217083",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.217071",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.217096",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.217094",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.217090",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.217089",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"520ed2df57fa836891d232ae",
      "allergies":[
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2012-03-26T00:00:00",
            "name":"NO KNOWN ALLERGIES"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"PREDNISONE"
         }
      ],
      "admission":{
         "dischargeDate":"2013-08-19T00:00:00",
         "admissionDate":"2013-08-17T00:00:00"
      },
      "patientId":"520ed2df57fa836891d232ad",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-17T03:25:10",
         "firstPHCPVisit":"None",
         "registration":"2013-08-17T01:34:15",
         "firstBedAssignment":"2013-08-17T02:09:39",
         "firstAttendVisit":"2013-08-17T02:11:18",
         "lastEDMove":"2013-08-17T02:09:39",
         "radiologyOrder":"2013-08-17T03:50:02",
         "firstFinancialRegistration":"2013-08-17T03:16:08",
         "arrival":"2013-08-17T01:33:00",
         "lastBedAssignment":"2013-08-17T02:09:39",
         "careComplete":"2013-08-17T03:55:49",
         "lastMedicalScreening":"2013-08-17T02:11:18",
         "lastFinancialRegistration":"2013-08-17T03:16:08",
         "encounterLock":"None",
         "labOrderTime":"2013-08-17T02:15:00",
         "triage":"2013-08-17T02:20:36",
         "observation":"None",
         "firstMedicalScreening":"2013-08-17T02:11:18",
         "medicineOrder":"2013-08-17T02:15:20",
         "departure":"2013-08-17T05:52:55",
         "bedRequest":"None",
         "encounterCreation":"2013-08-17T01:34:11"
      },
      "homeMedications":[
         {
            "frequency":"daily",
            "medication":"Crestor Oral",
            "dosage":"None"
         },
         {
            "frequency":"None",
            "medication":"gabapentin Oral",
            "dosage":"None"
         },
         {
            "frequency":"None",
            "medication":"gabapentin Oral",
            "dosage":"80 mg po bid"
         },
         {
            "frequency":"daily",
            "medication":"Crestor Oral",
            "dosage":"10 mg"
         },
         {
            "frequency":"daily",
            "medication":"Diltiazem Oral",
            "dosage":"180 mg"
         }
      ],
      "financialClass":"R",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.217046",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.217039",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.217044",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.217048",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.217049",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"145",
               "method":"None",
               "diastolic":"69"
            },
            "respiration":{
               "value":"16",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"72",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T05:01:47",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"126",
               "method":"None",
               "diastolic":"71"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"70",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T03:02:00",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"133",
               "method":"None",
               "diastolic":"65"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"62.14",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"25.1"
            },
            "pulse":{
               "value":"67",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"157",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T02:23:04",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-17T01:38:42.647000",
            "name":"Abdominal Pain"
         },
         {
            "complaintTime":"2013-08-17T01:38:42.653000",
            "name":"Medical Complaint"
         }
      ],
      "discharge":{
         "date":"2013-08-19T00:00:00",
         "edDischargeTime":"2013-08-17T05:52:55",
         "condition":"Good"
      },
      "diagnoses":[
         {
            "priority":"8",
            "code":"29859",
            "type":"N",
            "codingMethod":"V7",
            "description":"FHORAQB VASEP-VAVG RCVFQ"
         }
      ],
      "visitNumber":"3147083",
      "lastModified":"2013-08-20T03:22:51.216540",
      "creationTime":"2013-08-19T19:10:16.364000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.217053",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.217055",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.217057",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.217059",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.217060",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.217062",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.217064",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.217066",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"8115366209594917246",
      "medicationsOrdered":[
         {
            "orderId":"10862898",
            "dosageForm":"TAB",
            "minAmount":2,
            "orderedTime":"2013-08-18T13:00:00",
            "dispenseAmount":"2",
            "code":"41211057",
            "dispenseUnit":"TAB",
            "unit":"MG",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/520ed2df57fa836891d232ae"
   },
   {
      "patientType":"O5",
      "intakesOutputs":[
         {
            "outputs":[
               {
                  "amount":500.0,
                  "type":"VOID"
               }
            ],
            "observedTime":"2013-08-18T04:54:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"1360",
            "name":{
               "salutation":"MD",
               "last":"LAGUD",
               "first":"ADINARAYANA"
            }
         },
         {
            "role":"ReferringDoctor",
            "id":"8899",
            "name":{
               "middle":"DOCTOR",
               "last":"NO",
               "first":"REFERRING"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"0210",
            "name":{
               "salutation":"MD",
               "middle":"CHAPMAN",
               "last":"BEAN",
               "first":"L"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"3548",
            "name":{
               "salutation":"MD",
               "last":"GOODMAN",
               "first":"GARY"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"married",
         "name":{
            "last":"Patient 18",
            "first":"Test"
         },
         "ssn":"6666344897135229581",
         "religion":"NP",
         "id":"520fe7ee57fa836894009bfc",
         "contactDetails":{
            "homePhone":"(109)043-7220",
            "currentAddress":"933 JULABG QE^^CNYZ ONL^SY^10787^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1981-05-07T00:00:00",
         "mrn":"9176143321831297221",
         "race":"Caucasian",
         "sex":"female",
         "ethinicGroup":"O"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.217744",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.217741",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.217735",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.217753",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.217751",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.217747",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.217746",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"520fe7ee57fa83688fa0f3f1",
      "allergies":[
         {
            "name":"flu shot"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"WELLBUTRIN"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"TAGAMET"
         },
         {
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"FLU VACCINE"
         }
      ],
      "admission":{
         "dischargeDate":"2013-08-18T00:00:00",
         "admissionType":"1",
         "providers":[
            {
               "role":"AdmittingDoctor",
               "id":"1360",
               "name":{
                  "salutation":"MD",
                  "last":"LAGUD",
                  "first":"ADINARAYANA"
               }
            }
         ],
         "assignedLocation":{
            "ward":"ED"
         },
         "admitReason":"CHEST PAIN",
         "dischargeDisposition":"01",
         "admissionDate":"2013-08-17T00:00:00"
      },
      "patientId":"520fe7ee57fa836894009bfc",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"None",
         "firstPHCPVisit":"2013-08-17T21:33:53",
         "registration":"2013-08-17T21:21:08",
         "firstBedAssignment":"2013-08-17T21:22:55",
         "firstAttendVisit":"None",
         "lastEDMove":"2013-08-17T21:22:55",
         "radiologyOrder":"2013-08-17T21:37:00",
         "firstFinancialRegistration":"2013-08-17T21:43:42",
         "arrival":"2013-08-17T21:15:00",
         "lastBedAssignment":"2013-08-17T21:22:55",
         "careComplete":"2013-08-17T23:43:07",
         "lastMedicalScreening":"2013-08-17T21:33:53",
         "lastFinancialRegistration":"2013-08-17T21:43:42",
         "encounterLock":"None",
         "labOrderTime":"2013-08-17T21:37:00",
         "triage":"2013-08-17T21:58:31",
         "observation":"None",
         "firstMedicalScreening":"2013-08-17T21:33:53",
         "medicineOrder":"2013-08-17T21:37:00",
         "departure":"2013-08-18T01:01:10",
         "bedRequest":"None",
         "encounterCreation":"2013-08-17T21:21:02"
      },
      "homeMedications":[
         {
            "frequency":"None",
            "medication":"None",
            "dosage":"None"
         }
      ],
      "financialClass":"N",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.217713",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.217707",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.217712",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.217715",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.217716",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"109",
               "method":"None",
               "diastolic":"58"
            },
            "respiration":{
               "value":"16",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"61",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T00:41:22",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"115",
               "method":"None",
               "diastolic":"63"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"94.35",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"35.7"
            },
            "pulse":{
               "value":"77",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"163",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T22:08:54",
            "temperature":{
               "value":"98.1",
               "method":"None",
               "unit":"F"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-17T21:21:21.100000",
            "name":"Chest Pain"
         }
      ],
      "discharge":{
         "date":"2013-08-18T00:00:00",
         "edDischargeTime":"2013-08-18T01:01:10",
         "disposition":"01",
         "condition":"Good"
      },
      "diagnoses":[
         {
            "code":"786.50",
            "type":"Chest Pain",
            "description":""
         }
      ],
      "visitNumber":"3147120",
      "lastModified":"2013-08-20T03:22:51.217343",
      "creationTime":"2013-08-19T12:36:11.581000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.217719",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.217721",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.217722",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.217725",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.217726",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.217728",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.217730",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.217731",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"9176143321831297221",
      "medicationsOrdered":[
         {
            "orderId":"10862474",
            "dosageForm":"PGBK",
            "minAmount":20,
            "orderedTime":"2013-08-17T21:26:00",
            "dispenseAmount":"2",
            "code":"41210755",
            "unit":"MEQ",
            "dispenseUnit":"PGBK",
            "providerInstruction":"^*** HIGH-ALERT MEDICATION *** *******************************FOR PATIENTS WITH SRCR LESS THAN 2.0** GIVE IF K+ LEVEL LESS THAN 3.0 (GIVE IV OR PO ROUTE) INFUSE 2 X 20 MEQ IVPB= 40 MEQ DOSE",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/520fe7ee57fa83688fa0f3f1"
   },
   {
      "patientType":"I1",
      "intakesOutputs":[
         {
            "intakes":[
               {
                  "amount":440.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-18T17:15:00"
         },
         {
            "outputs":[
               {
                  "amount":350.0,
                  "type":"VOID"
               }
            ],
            "observedTime":"2013-08-19T02:14:00"
         },
         {
            "intakes":[
               {
                  "amount":200.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-18T05:46:00"
         },
         {
            "intakes":[
               {
                  "amount":75.0,
                  "type":"SUPPR"
               }
            ],
            "observedTime":"2013-08-19T18:02:00"
         },
         {
            "intakes":[
               {
                  "amount":600.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-19T05:35:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"1360",
            "name":{
               "salutation":"MD",
               "last":"LAGUD",
               "first":"ADINARAYANA"
            }
         },
         {
            "role":"ReferringDoctor",
            "id":"8899",
            "name":{
               "middle":"DOCTOR",
               "last":"NO",
               "first":"REFERRING"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"2959",
            "name":{
               "salutation":"DPM",
               "middle":"W",
               "last":"TINSLEY",
               "first":"ROBERT"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"3047",
            "name":{
               "salutation":"MD",
               "last":"TIRADOBERNARDINI",
               "first":"REINA"
            }
         },
         {
            "role":"ConsultingDoctor",
            "id":"3548",
            "name":{
               "salutation":"MD",
               "last":"GOODMAN",
               "first":"GARY"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"unmarried",
         "name":{
            "middle":"W",
            "last":"Patient 19",
            "first":"Test"
         },
         "ssn":"845355249701183473",
         "religion":"NP",
         "id":"520ffe6357fa836897766720",
         "contactDetails":{
            "homePhone":"(109)504-8629",
            "currentAddress":"9706 JRFGJBBQ OYIQ^^ZRYOBHEAR^SY^107898888^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1951-08-04T00:00:00",
         "mrn":"8831782780706069977",
         "race":"Caucasian",
         "sex":"male",
         "ethinicGroup":"O"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.218385",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.218382",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.218375",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.218394",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.218391",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.218388",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.218387",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"520ffe6357fa836897766721",
      "allergies":[
         {
            "name":"No known drug Allergies"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-02-08T00:00:00",
            "name":"NO KNOWN ALLERGIES"
         }
      ],
      "admission":{
         "admissionDate":"2013-08-17T00:00:00",
         "assignedLocation":{
            "bedNo":"1",
            "ward":"MS",
            "roomNo":"2117"
         },
         "admissionType":"1",
         "providers":[
            {
               "role":"AdmittingDoctor",
               "id":"1360",
               "name":{
                  "salutation":"MD",
                  "last":"LAGUD",
                  "first":"ADINARAYANA"
               }
            }
         ]
      },
      "patientId":"520ffe6357fa836897766720",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-17T23:06:53",
         "firstPHCPVisit":"2013-08-17T22:59:33",
         "registration":"2013-08-17T22:51:15",
         "firstBedAssignment":"2013-08-17T22:55:06",
         "firstAttendVisit":"None",
         "lastEDMove":"2013-08-17T22:55:06",
         "radiologyOrder":"2013-08-17T23:09:28",
         "firstFinancialRegistration":"2013-08-17T23:05:39",
         "arrival":"2013-08-17T22:51:00",
         "lastBedAssignment":"2013-08-17T22:55:06",
         "careComplete":"2013-08-18T01:40:41",
         "lastMedicalScreening":"2013-08-17T22:59:33",
         "lastFinancialRegistration":"2013-08-17T23:05:39",
         "encounterLock":"None",
         "labOrderTime":"2013-08-17T23:09:28",
         "triage":"2013-08-17T23:10:57",
         "observation":"None",
         "firstMedicalScreening":"2013-08-17T22:59:33",
         "medicineOrder":"2013-08-17T23:09:28",
         "departure":"2013-08-18T03:44:58",
         "bedRequest":"None",
         "encounterCreation":"2013-08-17T22:51:13"
      },
      "homeMedications":[
         {
            "frequency":"None",
            "medication":"Insulin: Regular Sub-Q",
            "dosage":"non-compliant"
         },
         {
            "frequency":"None",
            "medication":"non-compliant with all meds",
            "dosage":"None"
         }
      ],
      "financialClass":"Z",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.218345",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.218338",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.218344",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.218347",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.218351",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"201",
               "method":"None",
               "diastolic":"128"
            },
            "respiration":{
               "value":"16",
               "unit":"bpm"
            },
            "weight":{
               "value":"108.86",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"30.8"
            },
            "pulse":{
               "value":"99",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"188",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T23:16:12",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"142",
               "method":"None",
               "diastolic":"82"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"63",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T03:20:42",
            "temperature":{
               "value":"97.9",
               "method":"Tympanic",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"200",
               "method":"None",
               "diastolic":"113"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"92",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T23:59:46",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"193",
               "method":"None",
               "diastolic":"131"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"96",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T02:26:36",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"193",
               "method":"None",
               "diastolic":"131"
            },
            "respiration":{
               "value":"20",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"97",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-18T02:28:47",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-17T22:51:28.130000",
            "name":"Foot Injury"
         }
      ],
      "discharge":{
         "date":"2013-08-17T00:00:00",
         "edDischargeTime":"2013-08-18T03:44:58",
         "condition":"Good"
      },
      "diagnoses":[
         {
            "priority":"8",
            "code":"03858",
            "type":"N",
            "codingMethod":"V7",
            "description":"QZVV PVEP AG FG HAPAGEYQ"
         },
         {
            "priority":"9",
            "code":"03858",
            "type":"C",
            "codingMethod":"V7",
            "description":"QZVV PVEP AG FG HAPAGEYQ"
         },
         {
            "priority":"0",
            "code":"58591",
            "type":"F",
            "codingMethod":"V7",
            "description":"HYPRE BS NAXYR"
         },
         {
            "priority":"0",
            "code":"3997",
            "type":"F",
            "codingMethod":"V7",
            "description":"CYRHENY RSSHFVBA ABF"
         },
         {
            "priority":"0",
            "code":"I3645",
            "type":"F",
            "codingMethod":"V7",
            "description":"YBAT-GREZ HFR BS VAFHYVA"
         },
         {
            "priority":"0",
            "code":"2897",
            "type":"F",
            "codingMethod":"V7",
            "description":"ULCREGRAFVBA ABF"
         },
         {
            "priority":"0",
            "code":"21691",
            "type":"F",
            "codingMethod":"V7",
            "description":"YNGR RSS PI-QLFNEGUEVN"
         },
         {
            "priority":"0",
            "code":"5651",
            "type":"F",
            "codingMethod":"V7",
            "description":"SYNGHY/REHPGNG/TNF CNVA"
         }
      ],
      "visitNumber":"3147122",
      "lastModified":"2013-08-20T03:22:51.217964",
      "creationTime":"2013-08-20T00:00:33.569000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.218354",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.218356",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.218358",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.218360",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.218364",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.218366",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.218367",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.218369",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"8831782780706069977",
      "medicationsOrdered":[
         {
            "orderId":"10862970",
            "dosageForm":"CREA",
            "minAmount":1,
            "orderedTime":"2013-08-18T16:00:00",
            "dispenseAmount":"0.06666",
            "code":"41211096",
            "unit":"APPLIC",
            "dispenseUnit":"CREA",
            "providerInstruction":"^TO AFFECTED AREA",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/520ffe6357fa836897766721"
   },
   {
      "patientType":"I1",
      "intakesOutputs":[
         {
            "intakes":[
               {
                  "amount":350.0,
                  "type":"IVPB"
               }
            ],
            "observedTime":"2013-08-18T18:00:00"
         },
         {
            "intakes":[
               {
                  "amount":675.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-19T17:56:00"
         },
         {
            "intakes":[
               {
                  "amount":900.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-18T17:30:00"
         },
         {
            "intakes":[
               {
                  "amount":350.0,
                  "type":"IVPB"
               }
            ],
            "observedTime":"2013-08-17T18:00:00"
         },
         {
            "outputs":[
               {
                  "amount":800.0,
                  "type":"VOID"
               }
            ],
            "observedTime":"2013-08-19T06:00:00"
         },
         {
            "intakes":[
               {
                  "amount":1160.0,
                  "type":"ORAL"
               }
            ],
            "observedTime":"2013-08-17T17:14:00"
         },
         {
            "outputs":[
               {
                  "amount":1200.0,
                  "type":"VOID"
               }
            ],
            "observedTime":"2013-08-18T06:28:00"
         }
      ],
      "facilityId":"869",
      "immunizations":[
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"hepatitisa",
            "name":"Hepatitis A"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"polio",
            "name":"Polio"
         },
         {
            "dateReceived":"2013-12-12T14:21:56",
            "id":"influenzahighdose",
            "name":"Influenza (High Dose)"
         }
      ],
      "providers":[
         {
            "role":"AttendingDoctor",
            "id":"1757",
            "name":{
               "salutation":"MD",
               "last":"NALIPIREDDY",
               "first":"VASUDEVA"
            }
         }
      ],
      "patient":{
         "facilityId":"869",
         "maritalStatus":"unmarried",
         "name":{
            "middle":"Z",
            "last":"PAtient 20",
            "first":"Test"
         },
         "ssn":"390738379610184520",
         "id":"520edf3c57fa836894008b4f",
         "contactDetails":{
            "homePhone":"(109)268-2420",
            "currentAddress":"9918 ZNFPBG FG A R^^CNYZ ONL^SY^107838888^HF^^^^OERINEQ"
         },
         "dateOfBirth":"1953-11-13T00:00:00",
         "mrn":"4211233649542592234",
         "race":"Caucasian",
         "sex":"female",
         "ethinicGroup":"O"
      },
      "medicationsAdministered":[
         {
            "completionStatus":"ordered",
            "code":"1234-5678-90",
            "systemDataTime":"2013-08-20T03:22:51.219135",
            "notes":"Take 2 time per day",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny teneo",
               "role":"Admitting physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"2193"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.219131",
            "substanceManufacturerName":"Ranbaxy",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.219122",
            "location":"Meds",
            "startTime":"2013-10-22T17:28:33",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"12312",
            "unit":"mg"
         },
         {
            "completionStatus":"ordered",
            "code":"1341-3418-10",
            "systemDataTime":"2013-08-20T03:22:51.219144",
            "notes":"as needed",
            "barcodeId":"0123456789",
            "provider":{
               "name":"johnny doe",
               "role":"Ordered physician ",
               "degree":"MD",
               "assigningAuthority":"Melborune regional medical center",
               "id":"4213"
            },
            "substanceLotNumber":"10",
            "substanceExpirationDate":"2015-01-02T03:22:51.219142",
            "substanceManufacturerName":"cipla",
            "amount":20,
            "stopTime":"2013-08-30T03:22:51.219139",
            "location":"ED",
            "startTime":"2013-08-20T03:22:51.219137",
            "actionCode":"12",
            "substanceRefusalReason":"patient already taking Bactrim DS medication for headache",
            "id":"52289",
            "unit":"mg"
         }
      ],
      "id":"520edf3c57fa836898c2832b",
      "allergies":[
         {
            "name":"No known drug Allergies"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"NKA"
         },
         {
            "severityLevel":"other",
            "type":"drug",
            "identificationDate":"2013-08-17T00:00:00",
            "name":"NO KNOWN ALLERGIES"
         }
      ],
      "admission":{
         "admissionDate":"2013-08-17T00:00:00",
         "assignedLocation":{
            "ward":"2412-1",
            "roomNo":"MS"
         }
      },
      "patientId":"520edf3c57fa836894008b4f",
      "expectedAdmitDate":"None",
      "physicalAssessment":{
         "eent":{
            "throat":{
               "swelling":"False",
               "description":"Further description will be available here",
               "mucosa":"dry"
            },
            "eyes":{
               "right":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               },
               "left":{
                  "swelling":"True",
                  "conjunctiva":"pink",
                  "description":"Further description will be available here",
                  "condition":"normal",
                  "sclera":"white"
               }
            },
            "nose":{
               "swelling":"True",
               "description":"Further description will be available here",
               "skinIntegrity":"intact"
            },
            "description":"Further description will be available here",
            "ears":{
               "right":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               },
               "left":{
                  "swelling":"True",
                  "description":"Further description will be available here",
                  "skinIntegrity":"intact"
               }
            }
         },
         "psychoSocial":{
            "affect":"flat",
            "notes":"Observation Notes",
            "description":"Further description will be available here",
            "behavior":"calm",
            "auxiliaryData":{

            }
         },
         "g":{
            "auxiliaryData":{

            },
            "urine":{
               "color":"yellow",
               "output":"Does not void",
               "clarity":"cloudy",
               "symptoms":"Urgency"
            },
            "description":"Further description will be available here"
         },
         "respiratory":{
            "shortOfBreath":"False",
            "shallow":"regular",
            "breathingPattern":"regular",
            "description":"Further description will be available here",
            "symmetry":"regular",
            "oxygenInUse":"False",
            "chestTubeInUse":"False",
            "breathSounds":{
               "rightUpperLobe":"normal",
               "rightMiddleLobe":"normal",
               "leftLowerLobe":"normal",
               "bilateral":"normal",
               "rightLowerLobe":"normal",
               "leftUpperLobe":"normal"
            },
            "coughType":"No Cough",
            "effort":"labored"
         },
         "neurological":{
            "auxiliaryData":{

            },
            "pupil":{
               "right":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               },
               "left":{
                  "reactionToLight":"reactive",
                  "shape":"round",
                  "unit":"mm",
                  "size":"40"
               }
            },
            "description":"Further description will be available here",
            "orientation":{
               "person":"unresponsive",
               "mentation":"normal",
               "place":"oriented",
               "facialExpression":"normal",
               "time":"oriented",
               "levelOfConsciousness":"conscious"
            }
         },
         "iv":{
            "startDate":"2013-07-20T01:51:31.677479",
            "description":"Further description will be available here",
            "auxiliaryData":{

            },
            "guage":"guage",
            "site":"left hand",
            "lumens":"lumens",
            "tubeChange":"2013-07-20T01:51:31.677506",
            "appearanceOfSite":"compromised",
            "dressingChange":"2013-07-20T01:51:31.677501",
            "line":"IO"
         },
         "comaAssessment":"MENDS",
         "integumentary":{
            "nutrition":"very poor",
            "description":"Further description will be available here",
            "mobility":"very limited",
            "auxiliaryData":{

            },
            "frictionAndShear":"potential problem",
            "skinCondition":"normal",
            "moisture":"rarely moist",
            "activity":"chair fast",
            "sensoryPerception":"very limited"
         },
         "painAssessment":{
            "auxiliaryData":{

            },
            "description":"Further description will be available here",
            "painScale":"flacc"
         },
         "musculoskeletal":{
            "supportiveDevices":[
               "Ambulatory Aid"
            ],
            "description":"Further description will be available here",
            "amputation":"amputation description goes here",
            "auxiliaryData":{

            },
            "strenght":{
               "legs":{
                  "right":"weak",
                  "left":"strong"
               },
               "arms":{
                  "right":"weak",
                  "left":"strong"
               },
               "hands":{
                  "right":"strong",
                  "left":"weak"
               }
            },
            "deformity":"deformity description goes here",
            "gait":"observed",
            "fracture":"fracture description goes here",
            "contracture":"contracture description goes here"
         },
         "motorResponse":{

         },
         "gi":{
            "luq":"present",
            "description":"Further description will be available here",
            "tube":"NG Tube",
            "auxiliaryData":{

            },
            "llq":"absent",
            "appearance":"present",
            "tenderness":"tender",
            "ruq":"absent",
            "rlq":"absent",
            "palpation":"soft"
         },
         "cardiovascular":{
            "extremity":{
               "right":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               },
               "left":{
                  "color":"normal",
                  "actionsTaken":"actions details.",
                  "description":"Further description will be available here",
                  "temperature":"warm",
                  "location":"location of measure"
               }
            },
            "assessment":{
               "heartRate":"80 bpm",
               "pacemaker":"Temporary",
               "heartMonitorInUse":"False",
               "hearSounds":"lub"
            },
            "description":"Further description will be available here",
            "pulse":{
               "description":"Further description will be available here",
               "capillaryRefill":{
                  "rate":"Greater than 3 seconds",
                  "location":"RUE"
               },
               "edema":{
                  "rating":"3+",
                  "description":"pitting",
                  "location":"LUE"
               },
               "rate":"77 bpm",
               "location":"left",
               "rhythm":"Regular",
               "avFistula":"Thrill",
               "method":"Doppler"
            }
         }
      },
      "milestoneDraft":{
         "firstNurseVisit":"2013-08-17T03:35:30",
         "firstPHCPVisit":"None",
         "registration":"2013-08-17T02:35:46",
         "firstBedAssignment":"2013-08-17T02:20:57",
         "firstAttendVisit":"2013-08-17T02:28:22",
         "lastEDMove":"2013-08-17T02:20:57",
         "radiologyOrder":"2013-08-17T02:33:56",
         "firstFinancialRegistration":"2013-08-17T03:16:15",
         "arrival":"2013-08-17T02:20:57",
         "lastBedAssignment":"2013-08-17T02:20:57",
         "careComplete":"2013-08-17T05:55:32",
         "lastMedicalScreening":"2013-08-17T02:28:22",
         "lastFinancialRegistration":"2013-08-17T03:16:15",
         "encounterLock":"None",
         "labOrderTime":"2013-08-17T02:33:56",
         "triage":"2013-08-17T02:30:46",
         "observation":"None",
         "firstMedicalScreening":"2013-08-17T02:28:22",
         "medicineOrder":"2013-08-17T02:34:10",
         "departure":"2013-08-17T06:35:31",
         "bedRequest":"None",
         "encounterCreation":"2013-08-17T02:19:29"
      },
      "homeMedications":[
         {
            "frequency":"daily",
            "medication":"Norvasc Oral",
            "dosage":"2.5 mg"
         },
         {
            "frequency":"four times a day",
            "medication":"Alprazolam Oral",
            "dosage":"1 mg"
         },
         {
            "frequency":"1/2 tab daily",
            "medication":"Triamterene-Hydrochlorothiazid Oral",
            "dosage":"37.5-25 mg"
         },
         {
            "frequency":"nightly",
            "medication":"citalopram Oral",
            "dosage":"40 mg"
         },
         {
            "frequency":"as needed",
            "medication":"Betamethasone Valerate Topical",
            "dosage":"None"
         }
      ],
      "financialClass":"N",
      "vipIndicator":"A",
      "socialHistory":{
         "psychoDetail":{
            "isCareOther":"True",
            "isCultural":"True",
            "culturalDetail":"patient have religious or cultural practices"
         },
         "alcohol":{
            "lastUseDate":"2013-08-20T03:22:51.219094",
            "isActive":"True",
            "drinkPerWeek":"2-4"
         },
         "tobacco":{
            "yearsOfUse":"5",
            "smokingHistory":"Current less than daily",
            "frequency":"Every 2 Hours",
            "lastUseDate":"2013-08-20T03:22:51.219087",
            "cessationDetail":{
               "date":"2013-08-20T03:22:51.219093",
               "givenBy":"Dr. Johnny Teneo"
            },
            "type":[
               "Cigarette",
               "Chewing",
               "Pipe"
            ],
            "isActive":"True"
         },
         "recreationalDrugs":[
            {
               "comment":"patient take drug 1-2 days/week",
               "frequency":"1-2 days/week",
               "lastUseDate":"2013-08-20T03:22:51.219096",
               "drug":"Cocaine"
            },
            {
               "comment":"patient take drug Less than 1 day a week",
               "frequency":"Less than 1 day a week",
               "lastUseDate":"2013-08-20T03:22:51.219098",
               "drug":"Marijuana"
            }
         ]
      },
      "vitals":[
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"122",
               "method":"None",
               "diastolic":"74"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"39.92",
               "method":"None",
               "unit":"Kg"
            },
            "bmi":{
               "value":"16.6"
            },
            "pulse":{
               "value":"88",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"155",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T02:54:05",
            "temperature":{
               "value":"96.9",
               "method":"None",
               "unit":"F"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"None",
               "method":"None",
               "diastolic":"None"
            },
            "respiration":{
               "value":"None",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"93",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T03:17:15",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"112",
               "method":"None",
               "diastolic":"84"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"86",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T04:24:14",
            "temperature":{
               "value":"None",
               "method":"None",
               "unit":"None"
            }
         },
         {
            "bloodPressure":{
               "site":"None",
               "orthostatic":"None",
               "systolic":"135",
               "method":"None",
               "diastolic":"73"
            },
            "respiration":{
               "value":"18",
               "unit":"bpm"
            },
            "weight":{
               "value":"None",
               "method":"None",
               "unit":"None"
            },
            "bmi":{
               "value":"None"
            },
            "pulse":{
               "value":"94",
               "method":"None",
               "unit":"bpm"
            },
            "height":{
               "value":"None",
               "method":"None",
               "unit":"cm"
            },
            "observationTime":"2013-08-17T06:23:54",
            "temperature":{
               "value":"98.4",
               "method":"Temporal",
               "unit":"F"
            }
         }
      ],
      "complaints":[
         {
            "complaintTime":"2013-08-17T02:20:57.263000",
            "name":"Breathing Difficulty"
         }
      ],
      "discharge":{
         "date":"2013-08-17T00:00:00",
         "edDischargeTime":"2013-08-17T06:35:31",
         "condition":"Fair"
      },
      "diagnoses":[
         {
            "priority":"8",
            "code":"264",
            "type":"N",
            "codingMethod":"V7",
            "description":"CARHZBAVN, BETNAVFZ ABF"
         },
         {
            "priority":"9",
            "code":"264",
            "type":"C",
            "codingMethod":"V7",
            "description":"CARHZBAVN, BETNAVFZ ABF"
         },
         {
            "priority":"0",
            "code":"3997",
            "type":"F",
            "codingMethod":"V7",
            "description":"CYRHENY RSSHFVBA ABF"
         },
         {
            "priority":"0",
            "code":"9761",
            "type":"F",
            "codingMethod":"V7",
            "description":"FRP ZNY ARB OENVA/FCVAR"
         },
         {
            "priority":"0",
            "code":"9407",
            "type":"F",
            "codingMethod":"V7",
            "description":"ZNY ARB OEBAPU/YHAT ABF"
         },
         {
            "priority":"0",
            "code":"0418",
            "type":"F",
            "codingMethod":"V7",
            "description":"ZNYAHGEVGVBA ZBQ QRTERR"
         },
         {
            "priority":"0",
            "code":"274",
            "type":"F",
            "codingMethod":"V7",
            "description":"PUE NVEJNL BOFGEHPG ARP"
         },
         {
            "priority":"0",
            "code":"0637",
            "type":"F",
            "codingMethod":"V7",
            "description":"NARZVN ABF"
         },
         {
            "priority":"0",
            "code":"I638",
            "type":"F",
            "codingMethod":"V7",
            "description":"OZV YRFF GUNA 97,NQHYG"
         },
         {
            "priority":"0",
            "code":"56487",
            "type":"F",
            "codingMethod":"V7",
            "description":"ERFCVENGBEL NOABEZ ARP"
         },
         {
            "priority":"0",
            "code":"3637",
            "type":"F",
            "codingMethod":"V7",
            "description":"PUEBAVP XVQARL QVF ABF"
         },
         {
            "priority":"0",
            "code":"28178",
            "type":"F",
            "codingMethod":"V7",
            "description":"UL XVQ ABF J PE XVQ V-VI"
         }
      ],
      "visitNumber":"3147087",
      "lastModified":"2013-08-20T03:22:51.218630",
      "creationTime":"2013-08-20T01:21:07.198000",
      "medicalHistory":{
         "medical":[
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Migraine",
               "diagnosedDate":"2013-08-20T03:22:51.219101",
               "isActive":"False"
            },
            {
               "category":"head",
               "comments":"Patient has multiple issues with his head",
               "specificParts":"",
               "diagnosedWith":"headache",
               "cause":"Sinus",
               "diagnosedDate":"2013-08-20T03:22:51.219106",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Left Ear",
               "diagnosedWith":"Deaf",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.219108",
               "isActive":"True"
            },
            {
               "category":"ear",
               "comments":"Patient cannot hear without a hearing aide",
               "specificParts":"Right Ear",
               "diagnosedWith":"Hard of Hearing",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.219110",
               "isActive":"False"
            },
            {
               "category":"Integumentary",
               "comments":"Eczema at some parts of body",
               "specificParts":"",
               "diagnosedWith":"Eczema",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.219111",
               "isActive":"True"
            },
            {
               "category":"Cancer",
               "comments":"Cancer is cured for the patient using medical treatment",
               "specificParts":"Skin",
               "diagnosedWith":"Skin Cancer",
               "cause":"",
               "diagnosedDate":"2013-08-20T03:22:51.219115",
               "isActive":"False"
            }
         ],
         "surgical":[
            {
               "date":"2013-08-20T03:22:51.219117",
               "procedure":"Heart Surgery",
               "comments":"Surgery was successful"
            },
            {
               "date":"2013-08-20T03:22:51.219118",
               "procedure":"Ankle Surgery",
               "comments":"Patient need to rest his ankle"
            }
         ]
      },
      "mrn":"4211233649542592234",
      "medicationsOrdered":[
         {
            "orderId":"10863829",
            "dosageForm":"SOLP",
            "minAmount":1000,
            "orderedTime":"2013-08-19T13:38:00",
            "dispenseAmount":"1",
            "code":"41600830",
            "unit":"ML",
            "dispenseUnit":"SOLP",
            "providerInstruction":"^PER EMERGENCY HYPOGLYCEMIA PROTOCOL.",
            "maxAmount":0
         }
      ],
      "resource_uri":"/v1/encounters/520edf3c57fa836898c2832b"
   }
]
}

p = {"data": {"bmi": {"lowerLimit": None, "route": None, "site": None, "value": "0.78", "method": None, "unit": "bmi prime", "upperLimit": None}, "bloodPressure": {"method": "sphygmomanometer", "orthostatic": "95", "systolic": "155", "site": "R-arm", "diastolic": "83"}, "temperature": {"lowerLimit": None, "route": None, "site": None, "value": "91.8", "method": "oral", "unit": "F", "upperLimit": None}, "weight": {"lowerLimit": None, "route": None, "site": None, "value": "75", "method": "axle weigher", "unit": "kg", "upperLimit": None}, "encounterId": "525255b9313f1718f8b1f78c", "observedBy": None, "pulse": {"lowerLimit": None, "route": None, "site": None, "value": "82", "method": "monitor", "unit": "bpm", "upperLimit": None}, "height": {"lowerLimit": None, "route": None, "site": None, "value": "166", "method": "stadiometers", "unit": "cm", "upperLimit": None}, "referenceRange": None, "sleep": None, "pulseOX": None, "observationTime": "2013-07-29T11:41:25", "respiration": {"lowerLimit": None, "route": None, "site": None, "value": "25", "method": "monitor", "unit": "bpm", "upperLimit": None}, "pain": None, "glucose": None}}

for ele in d['data']:
    ele['vitals'] = p
    print ele 


