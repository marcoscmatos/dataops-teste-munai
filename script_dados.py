import pandas
from icecream import ic 
dados_csv = pandas.read_csv('dados/patients.csv')


data = {
  "resourceType" : "Patient",
  # from Resource: id, meta, implicitRules, and language
  # from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ 'type': 'TAX', 'value': 'CPF' }], # An identifier for this patient || usar o BR
  "active" :True, # Whether this patient's record is in active use
  "name" : [{ 'text': '$Nome' }], # A name associated with the patient
  "telecom" : [{ 'phone': 'Telefone' }], # A contact detail for the individual
  "gender" : "<code>", # IF 'MASCULINO' male | female | other | unknown
  "birthDate" : "<Data de Nascimento>", # FAZER A TRANSFORMACAO PRA AAAA-MM-DD The date of birth for the individual
  "birthCountry": [{ 'code' : '10' }], # usar os códigos 10	BRASIL https://simplifier.net/redenacionaldedadosemsaude/brpais-duplicate-2
}



