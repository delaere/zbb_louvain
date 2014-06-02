from math import exp

from math import tanh

class MLP_Higgs_vs_Bkg_ZH125_comb_2_5_3_1_1000:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.445235)/0.307413
		self.input1 = (in1 - 0.487302)/0.29068
		self.input2 = (in2 - 0.530975)/0.330691
		if index==0: return self.neuron0x1de98920();
		return 0.
	def neuron0x1de84530(self):
		return self.input0
	def neuron0x1de84870(self):
		return self.input1
	def neuron0x1de95840(self):
		return self.input2
	def neuron0x1de95b90(self):
		input = -4.65978
		input = input + self.synapse0x1de4cd00()
		input = input + self.synapse0x1de6b290()
		input = input + self.synapse0x1de95e40()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1de95e80(self):
		input = -4.12053
		input = input + self.synapse0x1de961c0()
		input = input + self.synapse0x1de96200()
		input = input + self.synapse0x1de96240()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1de96280(self):
		input = 0.189403
		input = input + self.synapse0x1de965c0()
		input = input + self.synapse0x1de96600()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1de96640(self):
		input = -0.207938
		input = input + self.synapse0x1de96980()
		input = input + self.synapse0x1de969c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1de96a00(self):
		input = -0.34606
		input = input + self.synapse0x1de96d40()
		input = input + self.synapse0x1de96d80()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1de96dc0(self):
		input = -0.254256
		input = input + self.synapse0x1de97100()
		input = input + self.synapse0x1de97140()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1de97180(self):
		input = 0.563476
		input = input + self.synapse0x1de974c0()
		input = input + self.synapse0x1de97500()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1de97540(self):
		input = 0.0875851
		input = input + self.synapse0x1de97880()
		input = input + self.synapse0x1ddf74a0()
		input = input + self.synapse0x1ddf74e0()
		input = input + self.synapse0x1de979d0()
		input = input + self.synapse0x1de97a10()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1de97a50(self):
		input = -0.287523
		input = input + self.synapse0x1de97d90()
		input = input + self.synapse0x1de97dd0()
		input = input + self.synapse0x1de97e10()
		input = input + self.synapse0x1de97e50()
		input = input + self.synapse0x1de97e90()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1de97ed0(self):
		input = -0.063349
		input = input + self.synapse0x1de98210()
		input = input + self.synapse0x1de98250()
		input = input + self.synapse0x1de98290()
		input = input + self.synapse0x1de982d0()
		input = input + self.synapse0x1de98310()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1de98350(self):
		input = -2.69858
		input = input + self.synapse0x1de98690()
		input = input + self.synapse0x1de986d0()
		input = input + self.synapse0x1de6b330()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1de98920(self):
		input = -4.6907
		input = input + self.synapse0x1de95af0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x1de4cd00(self):
		return (self.neuron0x1de84530()*1.36824)
	def synapse0x1de6b290(self):
		return (self.neuron0x1de84870()*-0.190458)
	def synapse0x1de95e40(self):
		return (self.neuron0x1de95840()*0.367418)
	def synapse0x1de961c0(self):
		return (self.neuron0x1de84530()*-1.73995)
	def synapse0x1de96200(self):
		return (self.neuron0x1de84870()*0.122952)
	def synapse0x1de96240(self):
		return (self.neuron0x1de95840()*-0.165155)
	def synapse0x1de965c0(self):
		return (self.neuron0x1de95b90()*-0.134061)
	def synapse0x1de96600(self):
		return (self.neuron0x1de95e80()*-0.175466)
	def synapse0x1de96980(self):
		return (self.neuron0x1de95b90()*0.777708)
	def synapse0x1de969c0(self):
		return (self.neuron0x1de95e80()*-1.61514)
	def synapse0x1de96d40(self):
		return (self.neuron0x1de95b90()*1.94481)
	def synapse0x1de96d80(self):
		return (self.neuron0x1de95e80()*-1.96929)
	def synapse0x1de97100(self):
		return (self.neuron0x1de95b90()*1.98922)
	def synapse0x1de97140(self):
		return (self.neuron0x1de95e80()*-2.01413)
	def synapse0x1de974c0(self):
		return (self.neuron0x1de95b90()*-2.67226)
	def synapse0x1de97500(self):
		return (self.neuron0x1de95e80()*2.03552)
	def synapse0x1de97880(self):
		return (self.neuron0x1de96280()*0.41126)
	def synapse0x1ddf74a0(self):
		return (self.neuron0x1de96640()*-0.612838)
	def synapse0x1ddf74e0(self):
		return (self.neuron0x1de96a00()*-1.21539)
	def synapse0x1de979d0(self):
		return (self.neuron0x1de96dc0()*-0.654902)
	def synapse0x1de97a10(self):
		return (self.neuron0x1de97180()*1.33093)
	def synapse0x1de97d90(self):
		return (self.neuron0x1de96280()*0.245568)
	def synapse0x1de97dd0(self):
		return (self.neuron0x1de96640()*0.905254)
	def synapse0x1de97e10(self):
		return (self.neuron0x1de96a00()*2.01441)
	def synapse0x1de97e50(self):
		return (self.neuron0x1de96dc0()*2.53087)
	def synapse0x1de97e90(self):
		return (self.neuron0x1de97180()*-4.10296)
	def synapse0x1de98210(self):
		return (self.neuron0x1de96280()*-0.0392889)
	def synapse0x1de98250(self):
		return (self.neuron0x1de96640()*0.518912)
	def synapse0x1de98290(self):
		return (self.neuron0x1de96a00()*0.679865)
	def synapse0x1de982d0(self):
		return (self.neuron0x1de96dc0()*0.7057)
	def synapse0x1de98310(self):
		return (self.neuron0x1de97180()*-1.58642)
	def synapse0x1de98690(self):
		return (self.neuron0x1de97540()*-2.35477)
	def synapse0x1de986d0(self):
		return (self.neuron0x1de97a50()*7.26011)
	def synapse0x1de6b330(self):
		return (self.neuron0x1de97ed0()*1.63993)
	def synapse0x1de95af0(self):
		return (self.neuron0x1de98350()*11.5346)
