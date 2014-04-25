
class TF1;

TF1* GetSFLight(TString meanminmax, TString tagger, TString TaggerStrength, Float_t Etamin, Float_t Etamax, TString DataPeriod);
TF1* GetSFlmean(TString tagger, TString TaggerStrength, float Etamin, float Etamax, TString DataPeriod);
TF1* GetSFlmin(TString tagger, TString TaggerStrength, float Etamin, float Etamax, TString DataPeriod);
TF1* GetSFlmax(TString tagger, TString TaggerStrength, float Etamin, float Etamax, TString DataPeriod);
