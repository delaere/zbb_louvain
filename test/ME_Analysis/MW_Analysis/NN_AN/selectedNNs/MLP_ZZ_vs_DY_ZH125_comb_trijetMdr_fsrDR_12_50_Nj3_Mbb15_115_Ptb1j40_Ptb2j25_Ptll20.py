from math import exp

from math import tanh

class Final12/MLP_ZZ_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_50_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2,in3,in4,in5):
		self.input0 = (in0 - 19.3926)/1.0044
		self.input1 = (in1 - 19.9308)/0.807903
		self.input2 = (in2 - 21.1534)/1.47427
		self.input3 = (in3 - 10.8329)/1.15652
		self.input4 = (in4 - 10.2844)/32.8326
		self.input5 = (in5 - 1.79526)/0.816131
		if index==0: return self.neuron0x350f7950();
		return 0.
	def neuron0x350f29a0(self):
		return self.input0
	def neuron0x350f2c50(self):
		return self.input1
	def neuron0x350f2f90(self):
		return self.input2
	def neuron0x350f32d0(self):
		return self.input3
	def neuron0x350f3610(self):
		return self.input4
	def neuron0x350f3950(self):
		return self.input5
	def neuron0x350f3dc0(self):
		input = 0.160298
		input = input + self.synapse0x350f4070()
		input = input + self.synapse0x350f40b0()
		input = input + self.synapse0x350f40f0()
		input = input + self.synapse0x350f4130()
		input = input + self.synapse0x350f4170()
		input = input + self.synapse0x350f41b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x350f41f0(self):
		input = -0.216985
		input = input + self.synapse0x350f4530()
		input = input + self.synapse0x350f4570()
		input = input + self.synapse0x350f45b0()
		input = input + self.synapse0x350f45f0()
		input = input + self.synapse0x350f4630()
		input = input + self.synapse0x350f4670()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x350f46b0(self):
		input = 0.976081
		input = input + self.synapse0x350f49f0()
		input = input + self.synapse0x350f4a30()
		input = input + self.synapse0x350f4a70()
		input = input + self.synapse0x350f4ab0()
		input = input + self.synapse0x350f4af0()
		input = input + self.synapse0x35043ac0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x350f4c40(self):
		input = -0.858104
		input = input + self.synapse0x350f4f80()
		input = input + self.synapse0x350f4fc0()
		input = input + self.synapse0x350f5000()
		input = input + self.synapse0x350f5040()
		input = input + self.synapse0x350f5080()
		input = input + self.synapse0x350f50c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x350f5100(self):
		input = 0.398313
		input = input + self.synapse0x350f5440()
		input = input + self.synapse0x350f5480()
		input = input + self.synapse0x350f54c0()
		input = input + self.synapse0x350f5500()
		input = input + self.synapse0x350f5540()
		input = input + self.synapse0x350f5580()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x350f55c0(self):
		input = -0.295446
		input = input + self.synapse0x350f5900()
		input = input + self.synapse0x350f5940()
		input = input + self.synapse0x350f5980()
		input = input + self.synapse0x35043b00()
		input = input + self.synapse0x3509ccc0()
		input = input + self.synapse0x35043ef0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x350f5bd0(self):
		input = -0.508062
		input = input + self.synapse0x350f5f10()
		input = input + self.synapse0x350f5f50()
		input = input + self.synapse0x350f5f90()
		input = input + self.synapse0x350f5fd0()
		input = input + self.synapse0x350f6010()
		input = input + self.synapse0x350f6050()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x350f6090(self):
		input = -1.25804
		input = input + self.synapse0x350f63d0()
		input = input + self.synapse0x350f6410()
		input = input + self.synapse0x350f6450()
		input = input + self.synapse0x350f6490()
		input = input + self.synapse0x350f64d0()
		input = input + self.synapse0x350f6510()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x350f6550(self):
		input = 0.613561
		input = input + self.synapse0x350f6890()
		input = input + self.synapse0x350f68d0()
		input = input + self.synapse0x350f6910()
		input = input + self.synapse0x350f6950()
		input = input + self.synapse0x350f6990()
		input = input + self.synapse0x350f69d0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x350f6a10(self):
		input = 0.322181
		input = input + self.synapse0x350f6d50()
		input = input + self.synapse0x350f6d90()
		input = input + self.synapse0x350f6dd0()
		input = input + self.synapse0x350f6e10()
		input = input + self.synapse0x350f6e50()
		input = input + self.synapse0x350f6e90()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x350f6ed0(self):
		input = 0.118194
		input = input + self.synapse0x35043910()
		input = input + self.synapse0x35043950()
		input = input + self.synapse0x35043fd0()
		input = input + self.synapse0x35044010()
		input = input + self.synapse0x35044050()
		input = input + self.synapse0x35044090()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x350f59c0(self):
		input = -0.329053
		input = input + self.synapse0x350f77d0()
		input = input + self.synapse0x350f7810()
		input = input + self.synapse0x350f7850()
		input = input + self.synapse0x350f7890()
		input = input + self.synapse0x350f78d0()
		input = input + self.synapse0x350f7910()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x350f7950(self):
		input = 0.115615
		input = input + self.synapse0x350f7c90()
		input = input + self.synapse0x350f7cd0()
		input = input + self.synapse0x350f7d10()
		input = input + self.synapse0x350f7d50()
		input = input + self.synapse0x350f7d90()
		input = input + self.synapse0x350f7dd0()
		input = input + self.synapse0x350f7e10()
		input = input + self.synapse0x350f7e50()
		input = input + self.synapse0x350f7e90()
		input = input + self.synapse0x350f7ed0()
		input = input + self.synapse0x350f7f10()
		input = input + self.synapse0x350f7f50()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x350f4070(self):
		return (self.neuron0x350f29a0()*-0.31432)
	def synapse0x350f40b0(self):
		return (self.neuron0x350f2c50()*-0.367962)
	def synapse0x350f40f0(self):
		return (self.neuron0x350f2f90()*0.0511627)
	def synapse0x350f4130(self):
		return (self.neuron0x350f32d0()*0.475635)
	def synapse0x350f4170(self):
		return (self.neuron0x350f3610()*0.49283)
	def synapse0x350f41b0(self):
		return (self.neuron0x350f3950()*-0.16639)
	def synapse0x350f4530(self):
		return (self.neuron0x350f29a0()*-0.0901252)
	def synapse0x350f4570(self):
		return (self.neuron0x350f2c50()*0.219055)
	def synapse0x350f45b0(self):
		return (self.neuron0x350f2f90()*0.0230232)
	def synapse0x350f45f0(self):
		return (self.neuron0x350f32d0()*-0.561968)
	def synapse0x350f4630(self):
		return (self.neuron0x350f3610()*0.10566)
	def synapse0x350f4670(self):
		return (self.neuron0x350f3950()*-0.425009)
	def synapse0x350f49f0(self):
		return (self.neuron0x350f29a0()*-0.981285)
	def synapse0x350f4a30(self):
		return (self.neuron0x350f2c50()*-0.598048)
	def synapse0x350f4a70(self):
		return (self.neuron0x350f2f90()*0.0922043)
	def synapse0x350f4ab0(self):
		return (self.neuron0x350f32d0()*1.7487)
	def synapse0x350f4af0(self):
		return (self.neuron0x350f3610()*0.410047)
	def synapse0x35043ac0(self):
		return (self.neuron0x350f3950()*0.401386)
	def synapse0x350f4f80(self):
		return (self.neuron0x350f29a0()*0.987683)
	def synapse0x350f4fc0(self):
		return (self.neuron0x350f2c50()*0.254622)
	def synapse0x350f5000(self):
		return (self.neuron0x350f2f90()*-0.0434669)
	def synapse0x350f5040(self):
		return (self.neuron0x350f32d0()*-1.54208)
	def synapse0x350f5080(self):
		return (self.neuron0x350f3610()*0.502725)
	def synapse0x350f50c0(self):
		return (self.neuron0x350f3950()*-0.175024)
	def synapse0x350f5440(self):
		return (self.neuron0x350f29a0()*0.430249)
	def synapse0x350f5480(self):
		return (self.neuron0x350f2c50()*-0.0555825)
	def synapse0x350f54c0(self):
		return (self.neuron0x350f2f90()*-0.0496314)
	def synapse0x350f5500(self):
		return (self.neuron0x350f32d0()*-0.277336)
	def synapse0x350f5540(self):
		return (self.neuron0x350f3610()*-0.249382)
	def synapse0x350f5580(self):
		return (self.neuron0x350f3950()*-0.309406)
	def synapse0x350f5900(self):
		return (self.neuron0x350f29a0()*-0.023686)
	def synapse0x350f5940(self):
		return (self.neuron0x350f2c50()*0.227811)
	def synapse0x350f5980(self):
		return (self.neuron0x350f2f90()*-0.388208)
	def synapse0x35043b00(self):
		return (self.neuron0x350f32d0()*-0.308062)
	def synapse0x3509ccc0(self):
		return (self.neuron0x350f3610()*0.152196)
	def synapse0x35043ef0(self):
		return (self.neuron0x350f3950()*-0.0928856)
	def synapse0x350f5f10(self):
		return (self.neuron0x350f29a0()*0.250036)
	def synapse0x350f5f50(self):
		return (self.neuron0x350f2c50()*-0.0152426)
	def synapse0x350f5f90(self):
		return (self.neuron0x350f2f90()*0.0204375)
	def synapse0x350f5fd0(self):
		return (self.neuron0x350f32d0()*-0.519459)
	def synapse0x350f6010(self):
		return (self.neuron0x350f3610()*0.183515)
	def synapse0x350f6050(self):
		return (self.neuron0x350f3950()*-0.381374)
	def synapse0x350f63d0(self):
		return (self.neuron0x350f29a0()*1.07634)
	def synapse0x350f6410(self):
		return (self.neuron0x350f2c50()*0.185244)
	def synapse0x350f6450(self):
		return (self.neuron0x350f2f90()*-0.0538494)
	def synapse0x350f6490(self):
		return (self.neuron0x350f32d0()*-1.80956)
	def synapse0x350f64d0(self):
		return (self.neuron0x350f3610()*0.307455)
	def synapse0x350f6510(self):
		return (self.neuron0x350f3950()*-0.00127505)
	def synapse0x350f6890(self):
		return (self.neuron0x350f29a0()*-0.547745)
	def synapse0x350f68d0(self):
		return (self.neuron0x350f2c50()*1.02157)
	def synapse0x350f6910(self):
		return (self.neuron0x350f2f90()*-0.981821)
	def synapse0x350f6950(self):
		return (self.neuron0x350f32d0()*1.02453)
	def synapse0x350f6990(self):
		return (self.neuron0x350f3610()*0.336625)
	def synapse0x350f69d0(self):
		return (self.neuron0x350f3950()*-0.829306)
	def synapse0x350f6d50(self):
		return (self.neuron0x350f29a0()*-0.387269)
	def synapse0x350f6d90(self):
		return (self.neuron0x350f2c50()*-0.356806)
	def synapse0x350f6dd0(self):
		return (self.neuron0x350f2f90()*0.610161)
	def synapse0x350f6e10(self):
		return (self.neuron0x350f32d0()*0.158236)
	def synapse0x350f6e50(self):
		return (self.neuron0x350f3610()*0.00755696)
	def synapse0x350f6e90(self):
		return (self.neuron0x350f3950()*-0.263707)
	def synapse0x35043910(self):
		return (self.neuron0x350f29a0()*-0.28274)
	def synapse0x35043950(self):
		return (self.neuron0x350f2c50()*0.231032)
	def synapse0x35043fd0(self):
		return (self.neuron0x350f2f90()*-0.0622014)
	def synapse0x35044010(self):
		return (self.neuron0x350f32d0()*-0.464265)
	def synapse0x35044050(self):
		return (self.neuron0x350f3610()*-0.0242093)
	def synapse0x35044090(self):
		return (self.neuron0x350f3950()*-0.245147)
	def synapse0x350f77d0(self):
		return (self.neuron0x350f29a0()*-0.0845056)
	def synapse0x350f7810(self):
		return (self.neuron0x350f2c50()*-0.00865707)
	def synapse0x350f7850(self):
		return (self.neuron0x350f2f90()*-0.530099)
	def synapse0x350f7890(self):
		return (self.neuron0x350f32d0()*0.495103)
	def synapse0x350f78d0(self):
		return (self.neuron0x350f3610()*-0.249793)
	def synapse0x350f7910(self):
		return (self.neuron0x350f3950()*-0.0650909)
	def synapse0x350f7c90(self):
		return (self.neuron0x350f3dc0()*-0.210485)
	def synapse0x350f7cd0(self):
		return (self.neuron0x350f41f0()*0.226373)
	def synapse0x350f7d10(self):
		return (self.neuron0x350f46b0()*-1.10105)
	def synapse0x350f7d50(self):
		return (self.neuron0x350f4c40()*0.950439)
	def synapse0x350f7d90(self):
		return (self.neuron0x350f5100()*0.216467)
	def synapse0x350f7dd0(self):
		return (self.neuron0x350f55c0()*0.0846223)
	def synapse0x350f7e10(self):
		return (self.neuron0x350f5bd0()*0.0997765)
	def synapse0x350f7e50(self):
		return (self.neuron0x350f6090()*1.13438)
	def synapse0x350f7e90(self):
		return (self.neuron0x350f6550()*-1.08389)
	def synapse0x350f7ed0(self):
		return (self.neuron0x350f6a10()*0.431581)
	def synapse0x350f7f10(self):
		return (self.neuron0x350f6ed0()*0.231566)
	def synapse0x350f7f50(self):
		return (self.neuron0x350f59c0()*-0.255982)
