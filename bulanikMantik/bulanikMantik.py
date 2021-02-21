import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as karar

sicaklik=karar.Antecedent(np.arange(15,41,1),'sicaklik')
nem=karar.Antecedent(np.arange(0,41,1),'nem' )
ruzgar=karar.Antecedent(np.arange(10,51,1),'ruzgar')

sonuc=karar.Consequent(np.arange(0,101,1), 'sonuc durumu')

sicaklik['çok düşük']=fuzz.trimf(sicaklik.universe,[0,0,10])
sicaklik['düşük']=fuzz.trimf(sicaklik.universe,[0,10,20])
sicaklik['normal']=fuzz.trimf(sicaklik.universe,[10,20,30])
sicaklik['yüksek']=fuzz.trimf(sicaklik.universe,[20,30,40])
sicaklik['çok yüksek']=fuzz.trimf(sicaklik.universe,[30,40,40])

nem['çok düşük']=fuzz.trimf(nem.universe,[0,0,10])
nem['düşük']=fuzz.trimf(nem.universe,[0,10,20])
nem['normal']=fuzz.trimf(nem.universe,[10,20,30])
nem['yüksek']=fuzz.trimf(nem.universe,[20,30,40])
nem['çok yüksek']=fuzz.trimf(nem.universe,[30,40,40])

ruzgar['çok düşük']=fuzz.trimf(ruzgar.universe, [10,10,20])
ruzgar['düşük']=fuzz.trimf(ruzgar.universe, [10,20,30])
ruzgar['normal']=fuzz.trimf(ruzgar.universe, [20,30,40])
ruzgar['yüksek']=fuzz.trimf(ruzgar.universe, [30,40,50])
ruzgar['çok yüksek']=fuzz.trimf(ruzgar.universe, [40,50,50])

sonuc['evde kal']=fuzz.trimf(sonuc.universe, [0,0,25])
sonuc['çıkmamalısın']=fuzz.trimf(sonuc.universe, [0,25,50])
sonuc['çıkabilirsin']=fuzz.trimf(sonuc.universe, [25,50,75])
sonuc['kesin çık']=fuzz.trimf(sonuc.universe, [50,75,100])
sonuc['asla girme']=fuzz.trimf(sonuc.universe, [75,100,100])

sicaklik['normal'].view()
sicaklik.view()
nem.view()
ruzgar.view()
sonuc.view()

kural1=karar.Rule(sicaklik['çok düşük'] & nem['çok düşük'] & ruzgar['çok düşük'],sonuc['evde kal'])
kural2=karar.Rule(sicaklik['çok düşük'] & nem['normal'] & ruzgar['çok düşük'],sonuc['evde kal'])
kural3=karar.Rule(sicaklik['düşük'] & nem['normal'] & ruzgar['normal'],sonuc['çıkabilirsin'])
kural4=karar.Rule(sicaklik['düşük'] & nem['düşük'] & ruzgar['normal'],sonuc['çıkabilirsin'])
kural5=karar.Rule(sicaklik['normal'] & nem['yüksek'] & ruzgar['normal'],sonuc['kesin çık'])
kural6=karar.Rule(sicaklik['normal'] & nem['yüksek'] & ruzgar['düşük'],sonuc['çıkabilirsin'])
kural7=karar.Rule(sicaklik['yüksek'] & nem['çok yüksek'] & ruzgar['düşük'],sonuc['çıkmamalısın'])
kural8=karar.Rule(sicaklik['yüksek'] & nem['çok yüksek'] & ruzgar['çok düşük'],sonuc['çıkmamalısın'])
kural9=karar.Rule(sicaklik['çok yüksek'] | nem['normal'] & ruzgar['normal'],sonuc['çıkmamalısın'])
kural10=karar.Rule(sicaklik['çok yüksek'] & nem['çok yüksek'] | ruzgar['normal'],sonuc['çıkabilirsin'])
kural11=karar.Rule(sicaklik['çok düşük'] & nem['düşük'] & ruzgar['normal'],sonuc['çıkabilirsin'])
kural12=karar.Rule(sicaklik['normal'] & nem['düşük'] & ruzgar['normal'],sonuc['kesin çık'])
kural13=karar.Rule(sicaklik['normal'] | nem['çok yüksek'] | ruzgar['normal'],sonuc['çıkabilirsin'])
kural14=karar.Rule(sicaklik['yüksek'] & nem['normal'] & ruzgar['normal'],sonuc['kesin çık'])
kural15=karar.Rule(sicaklik['çok yüksek'] | nem['yüksek'] & ruzgar['normal'],sonuc['evde kal'])
kural16=karar.Rule(sicaklik['normal'] & nem['normal'] & ruzgar['normal'],sonuc['asla girme'])
kural17=karar.Rule(sicaklik['normal'] | nem['yüksek'] | ruzgar['normal'],sonuc['asla girme'])
kural18=karar.Rule(sicaklik['düşük'] & nem['düşük'] & ruzgar['çok düşük'],sonuc['kesin çık'])

sonuc_karar=karar.ControlSystem([kural1,kural2,kural3,kural4,kural5,kural6,kural7,kural8,kural9,kural10,kural11,kural12,kural13,kural14,kural15,kural16,kural17,kural18])

sonuc_=karar.ControlSystemSimulation(sonuc_karar)

sonuc_.input['sicaklik']=22.5
sonuc_.input['nem']=13.04
sonuc_.input['ruzgar']=0.8

sonuc_.compute()
print(sonuc_.output['sonuc durumu'])
sonuc.view(sim=sonuc_)