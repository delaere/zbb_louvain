from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_Bkg_3j_ZH125_comb_9_9_300_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.467176)/0.243159
		self.input1 = (in1 - 0.52708)/0.296356
		self.input2 = (in2 - 0.534793)/0.314261
		if index==0: return self.neuron0x2834d9e0();
		return 0.
	def neuron0x283476e0(self):
		return self.input0
	def neuron0x28347a20(self):
		return self.input1
	def neuron0x28347d60(self):
		return self.input2
	def neuron0x283481d0(self):
		input = -0.0121004
		input = input + self.synapse0x282ec870()
		input = input + self.synapse0x28348480()
		input = input + self.synapse0x283484c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x28348500(self):
		input = 0.84672
		input = input + self.synapse0x28348840()
		input = input + self.synapse0x28348880()
		input = input + self.synapse0x283488c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x28348900(self):
		input = 5.40581
		input = input + self.synapse0x28348c40()
		input = input + self.synapse0x28348c80()
		input = input + self.synapse0x28348cc0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x28348d00(self):
		input = 1.82563
		input = input + self.synapse0x28349040()
		input = input + self.synapse0x28349080()
		input = input + self.synapse0x283490c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x28349100(self):
		input = -0.61836
		input = input + self.synapse0x28349440()
		input = input + self.synapse0x28349480()
		input = input + self.synapse0x283494c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x28349500(self):
		input = -6.69411
		input = input + self.synapse0x28349840()
		input = input + self.synapse0x28349880()
		input = input + self.synapse0x282ec8b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x283499d0(self):
		input = 2.14497
		input = input + self.synapse0x28349c80()
		input = input + self.synapse0x28349cc0()
		input = input + self.synapse0x28349d00()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x28349d40(self):
		input = 0.458339
		input = input + self.synapse0x2834a080()
		input = input + self.synapse0x2834a0c0()
		input = input + self.synapse0x2834a100()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2834a140(self):
		input = -0.54645
		input = input + self.synapse0x2834a480()
		input = input + self.synapse0x2834a4c0()
		input = input + self.synapse0x2834a500()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2834a540(self):
		input = 0.0653596
		input = input + self.synapse0x2834a880()
		input = input + self.synapse0x2834a8c0()
		input = input + self.synapse0x2834a900()
		input = input + self.synapse0x2834a940()
		input = input + self.synapse0x2834a980()
		input = input + self.synapse0x2834a9c0()
		input = input + self.synapse0x282dcec0()
		input = input + self.synapse0x282dcfa0()
		input = input + self.synapse0x282dcfe0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2834ac10(self):
		input = 0.285103
		input = input + self.synapse0x2834af50()
		input = input + self.synapse0x2834af90()
		input = input + self.synapse0x2834afd0()
		input = input + self.synapse0x2834b010()
		input = input + self.synapse0x2834b050()
		input = input + self.synapse0x2834b090()
		input = input + self.synapse0x2834b0d0()
		input = input + self.synapse0x2834b110()
		input = input + self.synapse0x2834b150()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2834b190(self):
		input = 0.41309
		input = input + self.synapse0x2834b4d0()
		input = input + self.synapse0x2834b510()
		input = input + self.synapse0x2834b550()
		input = input + self.synapse0x2834b590()
		input = input + self.synapse0x2834b5d0()
		input = input + self.synapse0x2834b610()
		input = input + self.synapse0x2834b650()
		input = input + self.synapse0x2834b690()
		input = input + self.synapse0x2834b6d0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2834b710(self):
		input = 0.459789
		input = input + self.synapse0x2834ba50()
		input = input + self.synapse0x2834ba90()
		input = input + self.synapse0x2834bad0()
		input = input + self.synapse0x2834bb10()
		input = input + self.synapse0x2834bb50()
		input = input + self.synapse0x2834bb90()
		input = input + self.synapse0x2834bbd0()
		input = input + self.synapse0x2834bc10()
		input = input + self.synapse0x2834bc50()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2834bc90(self):
		input = 0.315334
		input = input + self.synapse0x282dc8d0()
		input = input + self.synapse0x282dc910()
		input = input + self.synapse0x282ec980()
		input = input + self.synapse0x282ec9c0()
		input = input + self.synapse0x282eca00()
		input = input + self.synapse0x2834aa00()
		input = input + self.synapse0x2834aa40()
		input = input + self.synapse0x2834aa80()
		input = input + self.synapse0x2834aac0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2834c3e0(self):
		input = 0.230944
		input = input + self.synapse0x2834c720()
		input = input + self.synapse0x2834c760()
		input = input + self.synapse0x2834c7a0()
		input = input + self.synapse0x2834c7e0()
		input = input + self.synapse0x2834c820()
		input = input + self.synapse0x2834c860()
		input = input + self.synapse0x2834c8a0()
		input = input + self.synapse0x2834c8e0()
		input = input + self.synapse0x2834c920()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2834c960(self):
		input = 0.332741
		input = input + self.synapse0x2834cca0()
		input = input + self.synapse0x2834cce0()
		input = input + self.synapse0x2834cd20()
		input = input + self.synapse0x2834cd60()
		input = input + self.synapse0x2834cda0()
		input = input + self.synapse0x2834cde0()
		input = input + self.synapse0x2834ce20()
		input = input + self.synapse0x2834ce60()
		input = input + self.synapse0x2834cea0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2834cee0(self):
		input = 0.0379295
		input = input + self.synapse0x2834d220()
		input = input + self.synapse0x2834d260()
		input = input + self.synapse0x2834d2a0()
		input = input + self.synapse0x2834d2e0()
		input = input + self.synapse0x2834d320()
		input = input + self.synapse0x2834d360()
		input = input + self.synapse0x2834d3a0()
		input = input + self.synapse0x2834d3e0()
		input = input + self.synapse0x2834d420()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2834d460(self):
		input = -0.233368
		input = input + self.synapse0x2834d7a0()
		input = input + self.synapse0x2834d7e0()
		input = input + self.synapse0x2834d820()
		input = input + self.synapse0x2834d860()
		input = input + self.synapse0x2834d8a0()
		input = input + self.synapse0x2834d8e0()
		input = input + self.synapse0x2834d920()
		input = input + self.synapse0x2834d960()
		input = input + self.synapse0x2834d9a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2834d9e0(self):
		input = 0.0196513
		input = input + self.synapse0x2834ab00()
		input = input + self.synapse0x2834dd20()
		input = input + self.synapse0x2834dd60()
		input = input + self.synapse0x2834dda0()
		input = input + self.synapse0x2834dde0()
		input = input + self.synapse0x2834de20()
		input = input + self.synapse0x2834de60()
		input = input + self.synapse0x2834dea0()
		input = input + self.synapse0x2834dee0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x282ec870(self):
		return (self.neuron0x283476e0()*-1.41749)
	def synapse0x28348480(self):
		return (self.neuron0x28347a20()*-0.803547)
	def synapse0x283484c0(self):
		return (self.neuron0x28347d60()*-0.290594)
	def synapse0x28348840(self):
		return (self.neuron0x283476e0()*-0.123158)
	def synapse0x28348880(self):
		return (self.neuron0x28347a20()*-0.282542)
	def synapse0x283488c0(self):
		return (self.neuron0x28347d60()*-1.06627)
	def synapse0x28348c40(self):
		return (self.neuron0x283476e0()*-1.38565)
	def synapse0x28348c80(self):
		return (self.neuron0x28347a20()*-1.48189)
	def synapse0x28348cc0(self):
		return (self.neuron0x28347d60()*-0.705154)
	def synapse0x28349040(self):
		return (self.neuron0x283476e0()*0.0249757)
	def synapse0x28349080(self):
		return (self.neuron0x28347a20()*0.136413)
	def synapse0x283490c0(self):
		return (self.neuron0x28347d60()*0.996174)
	def synapse0x28349440(self):
		return (self.neuron0x283476e0()*1.76989)
	def synapse0x28349480(self):
		return (self.neuron0x28347a20()*-0.748787)
	def synapse0x283494c0(self):
		return (self.neuron0x28347d60()*-1.82891)
	def synapse0x28349840(self):
		return (self.neuron0x283476e0()*-2.92811)
	def synapse0x28349880(self):
		return (self.neuron0x28347a20()*-0.862399)
	def synapse0x282ec8b0(self):
		return (self.neuron0x28347d60()*0.0150819)
	def synapse0x28349c80(self):
		return (self.neuron0x283476e0()*0.710978)
	def synapse0x28349cc0(self):
		return (self.neuron0x28347a20()*0.339911)
	def synapse0x28349d00(self):
		return (self.neuron0x28347d60()*-1.2952)
	def synapse0x2834a080(self):
		return (self.neuron0x283476e0()*-0.769277)
	def synapse0x2834a0c0(self):
		return (self.neuron0x28347a20()*0.646728)
	def synapse0x2834a100(self):
		return (self.neuron0x28347d60()*0.66923)
	def synapse0x2834a480(self):
		return (self.neuron0x283476e0()*0.117861)
	def synapse0x2834a4c0(self):
		return (self.neuron0x28347a20()*1.8162)
	def synapse0x2834a500(self):
		return (self.neuron0x28347d60()*-0.214971)
	def synapse0x2834a880(self):
		return (self.neuron0x283481d0()*0.763315)
	def synapse0x2834a8c0(self):
		return (self.neuron0x28348500()*-0.430257)
	def synapse0x2834a900(self):
		return (self.neuron0x28348900()*0.386164)
	def synapse0x2834a940(self):
		return (self.neuron0x28348d00()*-1.58458)
	def synapse0x2834a980(self):
		return (self.neuron0x28349100()*-0.573771)
	def synapse0x2834a9c0(self):
		return (self.neuron0x28349500()*1.81683)
	def synapse0x282dcec0(self):
		return (self.neuron0x283499d0()*-0.390124)
	def synapse0x282dcfa0(self):
		return (self.neuron0x28349d40()*-0.844297)
	def synapse0x282dcfe0(self):
		return (self.neuron0x2834a140()*0.83986)
	def synapse0x2834af50(self):
		return (self.neuron0x283481d0()*0.771972)
	def synapse0x2834af90(self):
		return (self.neuron0x28348500()*0.555804)
	def synapse0x2834afd0(self):
		return (self.neuron0x28348900()*2.22315)
	def synapse0x2834b010(self):
		return (self.neuron0x28348d00()*-0.817834)
	def synapse0x2834b050(self):
		return (self.neuron0x28349100()*-0.173353)
	def synapse0x2834b090(self):
		return (self.neuron0x28349500()*0.645791)
	def synapse0x2834b0d0(self):
		return (self.neuron0x283499d0()*-0.063577)
	def synapse0x2834b110(self):
		return (self.neuron0x28349d40()*-0.517941)
	def synapse0x2834b150(self):
		return (self.neuron0x2834a140()*0.537281)
	def synapse0x2834b4d0(self):
		return (self.neuron0x283481d0()*-0.947103)
	def synapse0x2834b510(self):
		return (self.neuron0x28348500()*0.226327)
	def synapse0x2834b550(self):
		return (self.neuron0x28348900()*-0.087863)
	def synapse0x2834b590(self):
		return (self.neuron0x28348d00()*0.372048)
	def synapse0x2834b5d0(self):
		return (self.neuron0x28349100()*1.04705)
	def synapse0x2834b610(self):
		return (self.neuron0x28349500()*-2.2397)
	def synapse0x2834b650(self):
		return (self.neuron0x283499d0()*1.35673)
	def synapse0x2834b690(self):
		return (self.neuron0x28349d40()*0.535024)
	def synapse0x2834b6d0(self):
		return (self.neuron0x2834a140()*-0.664003)
	def synapse0x2834ba50(self):
		return (self.neuron0x283481d0()*-0.610669)
	def synapse0x2834ba90(self):
		return (self.neuron0x28348500()*-0.0874786)
	def synapse0x2834bad0(self):
		return (self.neuron0x28348900()*-0.699082)
	def synapse0x2834bb10(self):
		return (self.neuron0x28348d00()*1.07797)
	def synapse0x2834bb50(self):
		return (self.neuron0x28349100()*0.0731239)
	def synapse0x2834bb90(self):
		return (self.neuron0x28349500()*-0.993717)
	def synapse0x2834bbd0(self):
		return (self.neuron0x283499d0()*0.00848937)
	def synapse0x2834bc10(self):
		return (self.neuron0x28349d40()*0.471066)
	def synapse0x2834bc50(self):
		return (self.neuron0x2834a140()*-0.866111)
	def synapse0x282dc8d0(self):
		return (self.neuron0x283481d0()*0.783725)
	def synapse0x282dc910(self):
		return (self.neuron0x28348500()*0.63941)
	def synapse0x282ec980(self):
		return (self.neuron0x28348900()*3.09591)
	def synapse0x282ec9c0(self):
		return (self.neuron0x28348d00()*-0.868737)
	def synapse0x282eca00(self):
		return (self.neuron0x28349100()*-1.26341)
	def synapse0x2834aa00(self):
		return (self.neuron0x28349500()*0.375027)
	def synapse0x2834aa40(self):
		return (self.neuron0x283499d0()*-0.145154)
	def synapse0x2834aa80(self):
		return (self.neuron0x28349d40()*-0.899224)
	def synapse0x2834aac0(self):
		return (self.neuron0x2834a140()*0.577264)
	def synapse0x2834c720(self):
		return (self.neuron0x283481d0()*-0.704435)
	def synapse0x2834c760(self):
		return (self.neuron0x28348500()*0.0993559)
	def synapse0x2834c7a0(self):
		return (self.neuron0x28348900()*-0.245827)
	def synapse0x2834c7e0(self):
		return (self.neuron0x28348d00()*0.787721)
	def synapse0x2834c820(self):
		return (self.neuron0x28349100()*0.392731)
	def synapse0x2834c860(self):
		return (self.neuron0x28349500()*-1.68999)
	def synapse0x2834c8a0(self):
		return (self.neuron0x283499d0()*0.746027)
	def synapse0x2834c8e0(self):
		return (self.neuron0x28349d40()*0.841724)
	def synapse0x2834c920(self):
		return (self.neuron0x2834a140()*-0.497657)
	def synapse0x2834cca0(self):
		return (self.neuron0x283481d0()*0.247236)
	def synapse0x2834cce0(self):
		return (self.neuron0x28348500()*-0.0136343)
	def synapse0x2834cd20(self):
		return (self.neuron0x28348900()*-0.221489)
	def synapse0x2834cd60(self):
		return (self.neuron0x28348d00()*0.850157)
	def synapse0x2834cda0(self):
		return (self.neuron0x28349100()*-0.0845061)
	def synapse0x2834cde0(self):
		return (self.neuron0x28349500()*0.11551)
	def synapse0x2834ce20(self):
		return (self.neuron0x283499d0()*-0.248293)
	def synapse0x2834ce60(self):
		return (self.neuron0x28349d40()*-0.240807)
	def synapse0x2834cea0(self):
		return (self.neuron0x2834a140()*0.195182)
	def synapse0x2834d220(self):
		return (self.neuron0x283481d0()*-0.88239)
	def synapse0x2834d260(self):
		return (self.neuron0x28348500()*0.22196)
	def synapse0x2834d2a0(self):
		return (self.neuron0x28348900()*-0.519075)
	def synapse0x2834d2e0(self):
		return (self.neuron0x28348d00()*0.193653)
	def synapse0x2834d320(self):
		return (self.neuron0x28349100()*1.35107)
	def synapse0x2834d360(self):
		return (self.neuron0x28349500()*-2.49219)
	def synapse0x2834d3a0(self):
		return (self.neuron0x283499d0()*1.83986)
	def synapse0x2834d3e0(self):
		return (self.neuron0x28349d40()*1.60586)
	def synapse0x2834d420(self):
		return (self.neuron0x2834a140()*-0.600599)
	def synapse0x2834d7a0(self):
		return (self.neuron0x283481d0()*0.693275)
	def synapse0x2834d7e0(self):
		return (self.neuron0x28348500()*-0.262024)
	def synapse0x2834d820(self):
		return (self.neuron0x28348900()*0.790701)
	def synapse0x2834d860(self):
		return (self.neuron0x28348d00()*-0.996847)
	def synapse0x2834d8a0(self):
		return (self.neuron0x28349100()*-0.122814)
	def synapse0x2834d8e0(self):
		return (self.neuron0x28349500()*0.871803)
	def synapse0x2834d920(self):
		return (self.neuron0x283499d0()*-0.351741)
	def synapse0x2834d960(self):
		return (self.neuron0x28349d40()*-0.56876)
	def synapse0x2834d9a0(self):
		return (self.neuron0x2834a140()*0.995015)
	def synapse0x2834ab00(self):
		return (self.neuron0x2834a540()*-3.62899)
	def synapse0x2834dd20(self):
		return (self.neuron0x2834ac10()*-3.1429)
	def synapse0x2834dd60(self):
		return (self.neuron0x2834b190()*2.51094)
	def synapse0x2834dda0(self):
		return (self.neuron0x2834b710()*2.55656)
	def synapse0x2834dde0(self):
		return (self.neuron0x2834bc90()*-3.34613)
	def synapse0x2834de20(self):
		return (self.neuron0x2834c3e0()*1.93597)
	def synapse0x2834de60(self):
		return (self.neuron0x2834c960()*0.432997)
	def synapse0x2834dea0(self):
		return (self.neuron0x2834cee0()*2.77182)
	def synapse0x2834dee0(self):
		return (self.neuron0x2834d460()*-3.26342)
