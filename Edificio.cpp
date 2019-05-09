#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <string>
#include <sstream>

using namespace std;

void leap_frog(float t_inicial, float t_final);
void leap_frog_100omegas(float t_inicial, float t_final);

int main(){
    
    double t_ini=0.0;
    double t_fin=10.0;
    
    leap_frog(t_ini, t_fin);
    leap_frog_100omegas(t_ini, t_fin);
    
    return(0); 
}


//leap frog para omega fijo
void leap_frog(float t_inicial, float t_final){
    
    double V1_sig=0, V2_sig=0, V3_sig=0, U1_sig=0, U2_sig=0,  U3_sig=0, V1_ant, V2_ant, V3_ant, U1_ant, U2_ant,  U3_ant;
    double gamma=0, m=1000, k=2000, coef_1=1, dt=0.1;
   
    double omega= coef_1*sqrt(k/m);
 
    ofstream outfile;
    outfile.open("data_posiciones.dat");
    while (t_inicial<t_final){
        
        V1_ant=V1_sig;
        V2_ant=V2_sig;
        V3_ant=V3_sig;
              
        U1_ant=U1_sig;
        U2_ant=U2_sig;
        U3_ant=U3_sig;
        
        outfile << U1_sig <<" "<< U2_sig <<" "<< U3_sig <<" "<< t_inicial <<endl;
        
        V1_ant= V1_ant-(dt/(2*m))*(sin(t_inicial*omega)+(V1_ant*-gamma)+(U2_ant*k)-(U1_ant*2*k));
        V1_sig= V1_ant+(dt/m)*(sin(t_inicial*omega)+(V1_ant*-gamma)+(U2_ant*k)-(U1_ant*2*k));
        U1_sig= U1_ant+(V1_sig*dt);
        V2_ant= V2_ant-(dt/(2*m))*((V2_ant*-gamma)+(U3_ant*k)+(U1_ant*k)-(U2_ant*2*k));
        V2_sig= V2_ant+(dt/m)*((V2_ant*-gamma)+(U3_ant*k)+(U1_ant*k)-(U2_ant*2*k));
        U2_sig= U2_ant+(V2_sig*dt);
        V3_ant= V3_ant-(dt/(2*m))*((V3_ant*-gamma)+(U2_ant*k)-(U3_ant*k));
        V3_sig= V3_ant+dt*(1/m)*((V3_ant*-gamma)+(U2_ant*k)-(U3_ant*k));
        U3_sig= U3_ant+(V3_sig*dt);
        
        t_inicial= t_inicial+dt;
          
    }
    
    outfile.close();
}
    

// leapfrog para 100 omegas  
void leap_frog_100omegas(float t_inicial, float t_final){
    
    double V1_sig=0, V2_sig=0, V3_sig=0, U1_sig=0, U2_sig=0, U3_sig=0, V1_ant, V2_ant, V3_ant, U1_ant, U2_ant,  U3_ant, varios_omegas[100];
    double gamma=0, m=1000, k=2000, dt=0.1, coef_i=0.2, avance=(0.028);
    std::string nombre = "";
    
    
            
    for(int i=0; i<100; i++){
       
        varios_omegas[i]=(coef_i+i*avance)*sqrt(k/m);
    }
    
    for(int i=0; i<100; i++){
        
        nombre= static_cast<std::ostringstream*>(&(std::ostringstream() << i+1))->str();
        ofstream outfile;
        outfile.open("datos_omega"+nombre+".dat");
        
        while (t_inicial<t_final){

            V1_ant=V1_sig;
            V2_ant=V2_sig;
            V3_ant=V3_sig;

            U1_ant=U1_sig;
            U2_ant=U2_sig;
            U3_ant=U3_sig;

            outfile << U1_sig <<" "<< U2_sig <<" "<< U3_sig <<" "<< t_inicial <<endl;

            V1_ant= V1_ant-(dt/(2*m))*(sin(t_inicial*varios_omegas[i])+(V1_ant*-gamma)+(U2_ant*k)-(U1_ant*2*k));
            V1_sig= V1_ant+(dt/m)*(sin(t_inicial*varios_omegas[i])+(V1_ant*-gamma)+(U2_ant*k)-(U1_ant*2*k));
            U1_sig= U1_ant+(V1_sig*dt);
            V2_ant= V2_ant-(dt/(2*m))*((V2_ant*-gamma)+(U3_ant*k)+(U1_ant*k)-(U2_ant*2*k));
            V2_sig= V2_ant+(dt/m)*((V2_ant*-gamma)+(U3_ant*k)+(U1_ant*k)-(U2_ant*2*k));
            U2_sig= U2_ant+(V2_sig*dt);
            V3_ant= V3_ant-(dt/(2*m))*((V3_ant*-gamma)+(U2_ant*k)-(U3_ant*k));
            V3_sig= V3_ant+dt*(1/m)*((V3_ant*-gamma)+(U2_ant*k)-(U3_ant*k));
            U3_sig= U3_ant+(V3_sig*dt);

            t_inicial= t_inicial+dt;
        }
        
        outfile.close();
        
    }
    
            
}