#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include "square.h"
#include "cells.h"
#include "hardrods.h"
#include "Planegen.h"
#include "histogram.h"
#include "Planegen.h"
#include <cstdlib>
#include <cmath>
#include <time.h>
#include <vector>
#include <vector>
#include <array>
using namespace std;

#ifndef MC_H
#define MC_H

class MC
{
    private:
    	//data members;
    	std::vector<HR> VRodlist; // the list storage the Vertical Rods;
        std::vector<HR> HRodlist; // the list storage the Horizantal Rods;
        std::vector<HR> URodlist; // the list storage the Up Rods;
    	int n0,n1,n2; // size of the box
    	int length; // length of the rod
    	long int step;
    	double z; 
    	double nh,nv,nu,dh,dv,du,ah,av,au;
        

    public:
        enum INIT {EMPTY,BOX,PLANE};
    	MC(long int ST, int LEN, int N0, int N1, int N2, double Z); //(x->n0, y->n1,z->n2)

    	// ********* Getters********//

        const vector<HR>& getVRodlist() const;
        const vector<HR>& getHRodlist() const;
        const vector<HR>& getURodlist() const;

    	// ******** Other Functianality *******//
        void Add(Cells &s,double &prob,double &proba);
        void Del(Cells &s,double &prob,double &probd,double &size);
    	void MCRUN(int init);  //init stands for the initial configuration: enum INIT {EMPTY,BOX,PLANE};
        void Zvs_();
        

    	void plot(const vector<HR>& VRodlist, const vector<HR>& HRodlist,const vector<HR>& URodlist);

};

#endif /* MC_H */