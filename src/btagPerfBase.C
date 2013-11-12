#include "UserCode/zbb_louvain/interface/btagPerfBase.h"
#include <cmath>

double btagPerfBase::getbEffScaleFactor( btagPerfBase::SystematicVariation mode, int flavor, int algo, double pt, double eta) const {
  btagPerfBase::value result = getbEffScaleFactor(flavor, algo, pt, eta);
  switch(mode) {
    case btagPerfBase::MEAN:
      return result.first;
    case btagPerfBase::MIN:
      return result.first - result.second;
    case btagPerfBase::MAX:
      return result.first + result.second;
    case btagPerfBase::MIN_BC:
      if (std::abs(flavor)!=5&&std::abs(flavor)!=4) return result.first;
      return result.first - result.second;
    case btagPerfBase::MAX_BC:
      if (std::abs(flavor)!=5&&std::abs(flavor)!=4) return result.first;
      return result.first + result.second;
    case btagPerfBase::MIN_L:
      if (std::abs(flavor)==5||std::abs(flavor)==4) return result.first;
      return result.first - result.second;
    case btagPerfBase::MAX_L:
      if (std::abs(flavor)==5||std::abs(flavor)==4) return result.first;
      return result.first + result.second;
  }
  return 0.;
}

double btagPerfBase::getbEfficiency( btagPerfBase::SystematicVariation mode, int flavor, int algo, double pt, double eta) const {
  btagPerfBase::value result = getbEfficiency(flavor, algo, pt, eta);
  return result.first;/*
  switch(mode) {
    case btagPerfBase::MEAN:
      return result.first;
    case btagPerfBase::MIN:
      return result.first - result.second;
    case btagPerfBase::MAX:
      return result.first + result.second;
      }*/
  return 0.;
}

