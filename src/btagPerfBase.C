#include "UserCode/zbb_louvain/interface/btagPerfBase.h"

double btagPerfBase::getbEffScaleFactor( btagPerfBase::SystematicVariation mode, int flavor, int algo, double pt, double eta) const {
  btagPerfBase::value result = getbEffScaleFactor(flavor, algo, pt, eta);
  switch(mode) {
    case btagPerfBase::MEAN:
      return result.first;
    case btagPerfBase::MIN:
      return result.first - result.second;
    case btagPerfBase::MAX:
      return result.first + result.second;
  }
  return 0.;
}

double btagPerfBase::getbEfficiency( btagPerfBase::SystematicVariation mode, int flavor, int algo, double pt, double eta) const {
  btagPerfBase::value result = getbEfficiency(flavor, algo, pt, eta);
  switch(mode) {
    case btagPerfBase::MEAN:
      return result.first;
    case btagPerfBase::MIN:
      return result.first - result.second;
    case btagPerfBase::MAX:
      return result.first + result.second;
  }
  return 0.;
}

